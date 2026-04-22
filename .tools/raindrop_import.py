#!/usr/bin/env python3
"""
Raindrop.io -> HQ vault library/ importer.

Creates one markdown file per bookmark in library/, with metadata
frontmatter and a `hydrated: false` flag. Re-running is idempotent:
bookmarks whose `raindrop_id` already exists as a file are skipped.

Usage:
  RAINDROP_TOKEN=$(op read "op://ArvoClaw/Raindrop API/test_token") \\
    python .tools/raindrop_import.py [--collection ID] [--limit N] [--dry-run]

  # or with op run:
  op run --env-file=.tools/.raindrop.env.tpl -- python .tools/raindrop_import.py
"""

import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime
from pathlib import Path

API_BASE = "https://api.raindrop.io/rest/v1"
VAULT_ROOT = Path(__file__).resolve().parent.parent
LIBRARY_DIR = VAULT_ROOT / "library"


def slugify(title: str, max_len: int = 60) -> str:
    s = (title or "").lower().strip()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"[-\s]+", "-", s).strip("-")
    if len(s) > max_len:
        s = s[:max_len].rstrip("-")
    return s or "untitled"


def api_get(path: str, token: str, **params):
    url = f"{API_BASE}{path}"
    if params:
        url += "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(
        url,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def fetch_collections(token):
    data = api_get("/collections", token)
    return {c["_id"]: c.get("title", "Untitled") for c in data.get("items", [])}


def fetch_raindrops(token, collection_id=0, limit=None):
    page = 0
    per_page = 50
    fetched = 0
    while True:
        data = api_get(
            f"/raindrops/{collection_id}",
            token,
            page=page,
            perpage=per_page,
            sort="-created",
        )
        items = data.get("items", [])
        if not items:
            return
        for item in items:
            yield item
            fetched += 1
            if limit and fetched >= limit:
                return
        if len(items) < per_page:
            return
        page += 1
        time.sleep(0.3)


def existing_ids(lib: Path):
    ids = set()
    for md in lib.rglob("*.md"):
        if md.name == "index.md":
            continue
        try:
            m = re.search(r"^raindrop_id:\s*(\d+)\s*$", md.read_text("utf-8"), re.M)
            if m:
                ids.add(int(m.group(1)))
        except Exception:
            pass
    return ids


def deleted_ids(ledger: Path):
    """Read .tools/raindrop_deleted.txt — one raindrop_id per line.
    `#` begins a comment. Blank lines ignored. Returns a set of ints.
    Intentionally-deleted raindrops go here so re-imports skip them
    instead of re-creating the file."""
    ids = set()
    if not ledger.exists():
        return ids
    for line in ledger.read_text("utf-8").splitlines():
        line = line.split("#", 1)[0].strip()
        if not line:
            continue
        try:
            ids.add(int(line))
        except ValueError:
            pass
    return ids


def fmt_tags(tags):
    out = []
    for t in tags or []:
        t = (t or "").strip()
        if not t:
            continue
        if re.search(r'[:\s"\[\]]', t):
            out.append('"' + t.replace('"', '\\"') + '"')
        else:
            out.append(t)
    return "[" + ", ".join(out) + "]" if out else "[]"


def render_md(bm, collection_name):
    title = bm.get("title") or "(untitled)"
    title_esc = title.replace('"', '\\"').replace("\n", " ")
    url = bm.get("link", "")
    rid = bm.get("_id")
    domain = bm.get("domain", "")
    excerpt = (bm.get("excerpt") or "").strip()
    note = (bm.get("note") or "").strip()
    topics = bm.get("tags") or []
    bm_type = bm.get("type", "link")
    coll = bm.get("collection") or {}
    coll_id = coll.get("$id", 0)
    created_raw = bm.get("created", "")
    try:
        created = datetime.fromisoformat(created_raw.replace("Z", "+00:00")).strftime(
            "%Y-%m-%d"
        )
    except Exception:
        created = datetime.utcnow().strftime("%Y-%m-%d")

    fm = "\n".join(
        [
            "---",
            "tags:",
            "  - library",
            f'title: "{title_esc}"',
            f'url: "{url}"',
            "company: [personal]",
            f"topics: {fmt_tags(topics)}",
            f"created: {created}",
            "source_type: raindrop",
            f"raindrop_id: {rid}",
            f'source_domain: "{domain}"',
            f"source_type_raindrop: {bm_type}",
            f'collection: "{collection_name}"',
            f"collection_id: {coll_id}",
            "hydrated: false",
            "---",
            "",
        ]
    )
    body = []
    if note:
        body += ["## Notes", "", note, ""]
    if excerpt:
        body += ["## Excerpt", "", excerpt, ""]
    body += [
        "## Raw Content",
        "",
        "<!-- Not yet hydrated. Run the hydrate script to fetch the full article body. -->",
        "",
    ]
    return fm + "\n".join(body)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--collection", type=int, default=0, help="0 = all collections")
    p.add_argument("--limit", type=int, default=None)
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args()

    token = os.environ.get("RAINDROP_TOKEN")
    if not token:
        sys.exit(
            "RAINDROP_TOKEN not set. Run:\n"
            "  RAINDROP_TOKEN=$(op read 'op://ArvoClaw/Raindrop API/test_token') "
            "python .tools/raindrop_import.py"
        )

    LIBRARY_DIR.mkdir(exist_ok=True)
    existing = existing_ids(LIBRARY_DIR)
    deleted = deleted_ids(Path(__file__).resolve().parent / "raindrop_deleted.txt")
    skip_ids = existing | deleted
    collections = fetch_collections(token)
    print(f"Existing raindrop imports in library/: {len(existing)}")
    if deleted:
        print(f"Tombstoned in raindrop_deleted.txt: {len(deleted)}")
    print(f"Collections resolved: {len(collections)}")
    print(f"Mode: {'DRY-RUN' if args.dry_run else 'WRITE'}")
    if args.limit:
        print(f"Limit: {args.limit}")
    if args.collection:
        print(
            f"Collection filter: {args.collection} ({collections.get(args.collection, '?')})"
        )
    print("---")

    created = skipped = tombstoned = 0
    for bm in fetch_raindrops(token, args.collection, args.limit):
        rid = bm.get("_id")
        if rid in deleted:
            tombstoned += 1
            continue
        if rid in existing:
            skipped += 1
            continue
        coll_id = (bm.get("collection") or {}).get("$id", 0)
        coll_name = collections.get(coll_id, "unsorted")
        coll_slug = slugify(coll_name) or "unsorted"
        coll_dir = LIBRARY_DIR / coll_slug
        coll_dir.mkdir(exist_ok=True)
        slug = slugify(bm.get("title") or "") or f"raindrop-{rid}"
        target = coll_dir / f"{slug}.md"
        if target.exists():
            target = coll_dir / f"{slug}-{rid}.md"
        rel = target.relative_to(VAULT_ROOT)
        if args.dry_run:
            print(f"[DRY] {rel}  ({bm.get('domain', '')})")
        else:
            target.write_text(render_md(bm, coll_name), encoding="utf-8")
            print(f"  + {rel}")
        created += 1

    print("---")
    msg = f"Done. {'Would create' if args.dry_run else 'Created'}: {created}  Skipped: {skipped}"
    if tombstoned:
        msg += f"  Tombstoned: {tombstoned}"
    print(msg)


if __name__ == "__main__":
    main()
