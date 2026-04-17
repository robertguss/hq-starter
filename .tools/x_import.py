#!/usr/bin/env python3
"""
Fieldtheory (X/Twitter bookmarks) -> HQ vault library/x-bookmarks/ importer.

Reads the fieldtheory JSONL cache and writes one markdown file per bookmark
with metadata frontmatter and `hydrated: false`. Idempotent: bookmarks whose
`tweet_id` already exists as a file are skipped.

Sync first:
  fieldtheory sync --yes

Then import:
  python .tools/x_import.py [--limit N] [--dry-run]
"""

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path

VAULT_ROOT = Path(__file__).resolve().parent.parent
LIBRARY_DIR = VAULT_ROOT / "library" / "x-bookmarks"
DEFAULT_JSONL = Path.home() / ".ft-bookmarks" / "bookmarks.jsonl"


def slugify(text: str, max_len: int = 50) -> str:
    s = (text or "").lower().strip()
    s = re.sub(r"https?://\S+", "", s)
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"[-\s]+", "-", s).strip("-")
    if len(s) > max_len:
        s = s[:max_len].rstrip("-")
    return s


def parse_posted_at(value: str) -> str:
    if not value:
        return datetime.utcnow().strftime("%Y-%m-%d")
    for fmt in (
        "%a %b %d %H:%M:%S %z %Y",
        "%Y-%m-%dT%H:%M:%S.%fZ",
        "%Y-%m-%dT%H:%M:%SZ",
    ):
        try:
            return datetime.strptime(value, fmt).strftime("%Y-%m-%d")
        except (ValueError, TypeError):
            pass
    return datetime.utcnow().strftime("%Y-%m-%d")


def existing_ids(lib: Path) -> set:
    ids = set()
    if not lib.exists():
        return ids
    pat = re.compile(r"^tweet_id:\s*\"?(\d+)\"?\s*$", re.M)
    for md in lib.rglob("*.md"):
        try:
            m = pat.search(md.read_text("utf-8"))
            if m:
                ids.add(m.group(1))
        except Exception:
            pass
    return ids


def fmt_yaml_str(value: str) -> str:
    if value is None:
        return '""'
    s = str(value).replace("\\", "\\\\").replace('"', '\\"')
    s = s.replace("\n", " ").replace("\r", " ").strip()
    return f'"{s}"'


def build_title(rec: dict) -> str:
    handle = rec.get("authorHandle") or "unknown"
    text = (rec.get("text") or "").strip()
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"https?://\S+", "", text).strip()
    if not text:
        return f"@{handle} — tweet {rec.get('tweetId', '')}"
    if len(text) > 90:
        text = text[:90].rstrip() + "…"
    return f"@{handle}: {text}"


def render_md(rec: dict) -> str:
    tweet_id = rec.get("tweetId") or rec.get("id") or ""
    url = rec.get("url") or ""
    handle = rec.get("authorHandle") or ""
    author_name = rec.get("authorName") or ""
    title = build_title(rec)
    created = parse_posted_at(rec.get("postedAt") or rec.get("syncedAt") or "")
    text = (rec.get("text") or "").strip()
    engagement = rec.get("engagement") or {}
    links = rec.get("links") or []
    media = rec.get("media") or []
    quoted = rec.get("quotedTweet")
    tags_from_tweet = rec.get("tags") or []

    fm_lines = [
        "---",
        "tags:",
        "  - library",
        f"title: {fmt_yaml_str(title)}",
        f"url: {fmt_yaml_str(url)}",
        "company: [personal]",
        f"topics: {json.dumps(list(tags_from_tweet))}",
        f"created: {created}",
        "source_type: twitter",
        f'tweet_id: "{tweet_id}"',
        'source_domain: "x.com"',
        f"author: {fmt_yaml_str(handle)}",
        f"author_name: {fmt_yaml_str(author_name)}",
        "hydrated: false",
        "---",
        "",
    ]

    body = ["## Tweet", ""]
    if text:
        for line in text.splitlines():
            body.append(f"> {line}" if line else ">")
        body.append("")
    body.append(f"— [@{handle}]({url}) ({author_name})")
    body.append("")

    if engagement:
        stats = " · ".join(
            f"{k.replace('Count', '')}: {v}"
            for k, v in engagement.items()
            if isinstance(v, (int, float))
        )
        if stats:
            body += ["**Engagement:** " + stats, ""]

    if links:
        body += ["## Links", ""]
        body += [f"- {ln}" for ln in links]
        body += [""]

    if media:
        body += ["## Media", ""]
        for m in media:
            if isinstance(m, dict):
                mu = m.get("url") or m.get("expandedUrl") or ""
                body.append(f"- {m.get('type', 'media')}: {mu}")
            else:
                body.append(f"- {m}")
        body += [""]

    if isinstance(quoted, dict):
        qt_text = (quoted.get("text") or "").strip()
        qt_handle = quoted.get("authorHandle") or ""
        qt_url = quoted.get("url") or ""
        body += ["## Quoted tweet", ""]
        if qt_text:
            for line in qt_text.splitlines():
                body.append(f"> {line}" if line else ">")
            body.append("")
        if qt_url:
            body += [f"— [@{qt_handle}]({qt_url})", ""]

    body += [
        "## Raw Content",
        "",
        "<!-- Not yet hydrated. Run the hydrate script to fetch thread / linked article. -->",
        "",
    ]
    return "\n".join(fm_lines) + "\n".join(body)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--jsonl", type=Path, default=DEFAULT_JSONL)
    p.add_argument("--limit", type=int, default=None)
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args()

    if not args.jsonl.exists():
        sys.exit(f"JSONL not found: {args.jsonl}\nRun: fieldtheory sync --yes")

    LIBRARY_DIR.mkdir(parents=True, exist_ok=True)
    existing = existing_ids(LIBRARY_DIR)
    print(f"Source: {args.jsonl}")
    print(f"Target: {LIBRARY_DIR.relative_to(VAULT_ROOT)}")
    print(f"Existing imports: {len(existing)}")
    print(f"Mode: {'DRY-RUN' if args.dry_run else 'WRITE'}")
    print("---")

    created = skipped = 0
    for i, line in enumerate(args.jsonl.read_text("utf-8").splitlines()):
        if args.limit and created + skipped >= args.limit:
            break
        try:
            rec = json.loads(line)
        except json.JSONDecodeError:
            continue

        tid = str(rec.get("tweetId") or rec.get("id") or "")
        if not tid:
            continue
        if tid in existing:
            skipped += 1
            continue

        handle = (rec.get("authorHandle") or "unknown").lower()
        handle_slug = re.sub(r"[^a-z0-9]+", "", handle) or "unknown"
        text_slug = slugify(rec.get("text") or "")
        if text_slug:
            base = f"{handle_slug}-{text_slug}"
        else:
            base = f"{handle_slug}-{tid[-8:]}"
        target = LIBRARY_DIR / f"{base}.md"
        if target.exists():
            target = LIBRARY_DIR / f"{base}-{tid}.md"

        rel = target.relative_to(VAULT_ROOT)
        if args.dry_run:
            print(f"[DRY] {rel}")
        else:
            target.write_text(render_md(rec), encoding="utf-8")
        created += 1

    print("---")
    print(
        f"Done. {'Would create' if args.dry_run else 'Created'}: {created}  Skipped: {skipped}"
    )


if __name__ == "__main__":
    main()
