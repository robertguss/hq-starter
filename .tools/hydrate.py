#!/usr/bin/env python3
"""
HQ vault library/ hydrator — tiered, one URL type at a time.

Usage:
  # GitHub
  GITHUB_TOKEN=$(op item get "GitHub - PAT (fine-grained)" --vault=ArvoClaw --fields token --reveal) \\
    python .tools/hydrate.py --type github [--limit N] [--dry-run] [--force]

  # Article (HTML pages via Jina Reader)
  JINA_API_KEY=$(op read 'op://ArvoClaw/Jina - Reader API Key/api_key') \\
    python .tools/hydrate.py --type article --limit 100    # recommended: batched

  # Article anonymous (slower, ~10s/item)
  python .tools/hydrate.py --type article --limit 25

Flags:
  --type     Fetcher tier to run (github now; article/arxiv/pdf/hn later)
  --limit N  Stop after N items hydrated (excluding skips)
  --dry-run  Classify and report; no writes
  --force    Re-hydrate items already marked hydrated: true

Idempotency: items with `hydrated: true` in frontmatter are skipped
unless --force. The GitHub fetcher replaces the `## Raw Content`
placeholder with the repo README and sets `hydrated: true`,
`hydrated_at: YYYY-MM-DD`, `hydrated_via: github-api`.
"""

import argparse
import base64
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

VAULT_ROOT = Path(__file__).resolve().parent.parent
LIB = VAULT_ROOT / "library"

FM_PAT = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
RAW_PLACEHOLDER_PAT = re.compile(
    r"## Raw Content\n+<!--\s*Not yet hydrated[^>]*-->\n?",
    re.MULTILINE,
)


# ---------- frontmatter helpers ----------


def parse_frontmatter(text: str):
    m = FM_PAT.match(text)
    if not m:
        return None, text
    return m.group(1), text[m.end() :]


def get_fm_field(fm: str, key: str):
    m = re.search(rf"^{re.escape(key)}:\s*(.*?)\s*$", fm, re.M)
    if not m:
        return None
    v = m.group(1)
    if len(v) >= 2 and v[0] == '"' and v[-1] == '"':
        v = v[1:-1]
    return v


def set_fm_field(fm: str, key: str, value: str) -> str:
    pattern = re.compile(rf"^{re.escape(key)}:\s*.*$", re.M)
    new_line = f"{key}: {value}"
    if pattern.search(fm):
        return pattern.sub(new_line, fm)
    return fm.rstrip() + "\n" + new_line


# ---------- GitHub fetcher ----------


def extract_github_repo(url: str):
    try:
        u = urllib.parse.urlparse(url)
    except Exception:
        return None
    if u.netloc.lower().lstrip("www.") != "github.com":
        return None
    parts = [p for p in u.path.split("/") if p]
    if len(parts) < 2:
        return None
    owner, repo = parts[0], parts[1]
    if repo.endswith(".git"):
        repo = repo[:-4]
    # Skip gists, orgs pages, settings etc.
    if owner.lower() in {
        "orgs",
        "settings",
        "features",
        "topics",
        "sponsors",
        "marketplace",
    }:
        return None
    return owner, repo


def gh_api_get(path: str, token: str | None = None):
    url = f"https://api.github.com{path}"
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "hq-vault-hydrator/0.1",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.headers, json.load(resp)


def fetch_github(url: str, token: str | None):
    parsed = extract_github_repo(url)
    if not parsed:
        raise ValueError(f"Not a repo URL: {url}")
    owner, repo = parsed
    meta = {"owner": owner, "repo": repo}

    # Repo metadata
    try:
        hdrs, info = gh_api_get(f"/repos/{owner}/{repo}", token)
    except urllib.error.HTTPError as e:
        if e.code == 404:
            raise FileNotFoundError(
                f"Repo {owner}/{repo} not found (deleted or renamed)"
            )
        raise
    meta["description"] = info.get("description") or ""
    meta["stars"] = info.get("stargazers_count", 0)
    meta["language"] = info.get("language") or ""
    meta["default_branch"] = info.get("default_branch") or "main"
    meta["rate_remaining"] = hdrs.get("X-RateLimit-Remaining", "?")

    # README
    try:
        _, readme = gh_api_get(f"/repos/{owner}/{repo}/readme", token)
        content = base64.b64decode(readme.get("content") or "").decode(
            "utf-8", errors="replace"
        )
        meta["readme_path"] = readme.get("path", "README.md")
        body = content
    except urllib.error.HTTPError as e:
        if e.code == 404:
            body = f"_(no README found)_\n\n**Description:** {meta['description']}"
            meta["readme_path"] = None
        else:
            raise
    return body, meta


# ---------- Article fetcher (Jina Reader) ----------

ARTICLE_EXCLUDE_HOSTS = {
    "github.com",
    "www.github.com",
    "gist.github.com",
    "x.com",
    "twitter.com",
    "t.co",
    "youtube.com",
    "www.youtube.com",
    "m.youtube.com",
    "youtu.be",
    "arxiv.org",
    "www.arxiv.org",
    "news.ycombinator.com",
    "reddit.com",
    "old.reddit.com",
    "www.reddit.com",
    "up.raindrop.io",
    "api.raindrop.io",
}


def is_article_url(url: str) -> bool:
    if not url:
        return False
    try:
        u = urllib.parse.urlparse(url)
    except Exception:
        return False
    host = u.netloc.lower()
    if host in ARTICLE_EXCLUDE_HOSTS:
        return False
    if host.endswith(".reddit.com") or host.endswith(".youtube.com"):
        return False
    if url.lower().endswith(".pdf"):
        return False
    if "application/pdf" in url.lower() or "application%2fpdf" in url.lower():
        return False
    if not host:
        return False
    return u.scheme in ("http", "https")


def fetch_article_jina(url: str, token: str | None, max_retries: int = 3):
    endpoint = f"https://r.jina.ai/{url}"
    headers = {
        "User-Agent": "hq-vault-hydrator/0.1",
        "Accept": "text/plain",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    backoff = 2.0
    for attempt in range(max_retries + 1):
        req = urllib.request.Request(endpoint, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=90) as resp:
                body = resp.read().decode("utf-8", errors="replace")
                hdrs = resp.headers
            meta = {
                "bytes": len(body),
                "rate_remaining": hdrs.get("X-RateLimit-Remaining", "?"),
            }
            return body, meta
        except urllib.error.HTTPError as e:
            if e.code == 404:
                raise FileNotFoundError(f"Jina 404 for {url}")
            if e.code in (429, 502, 503, 504) and attempt < max_retries:
                time.sleep(backoff)
                backoff *= 2
                continue
            raise
        except (TimeoutError, urllib.error.URLError):
            if attempt < max_retries:
                time.sleep(backoff)
                backoff *= 2
                continue
            raise


# ---------- Hydration loop ----------


def hydrate_file(
    md_path: Path, fetcher_name: str, fetcher, force: bool, dry_run: bool
) -> tuple[str, str]:
    text = md_path.read_text("utf-8")
    fm, body = parse_frontmatter(text)
    if fm is None:
        return "skip", "no frontmatter"
    if get_fm_field(fm, "hydrated") == "true" and not force:
        return "skip", "already hydrated"
    url = get_fm_field(fm, "url")
    if not url:
        return "skip", "no url"

    try:
        content, meta = fetcher(url)
    except FileNotFoundError as e:
        content = f"<!-- {e} -->"
        meta = {"error": "404"}
    except Exception as e:
        return "error", f"{type(e).__name__}: {e}"

    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    fm = set_fm_field(fm, "hydrated", "true")
    fm = set_fm_field(fm, "hydrated_at", today)
    fm = set_fm_field(fm, "hydrated_via", fetcher_name)

    header_line = f"## Raw Content\n\n<!-- Hydrated {today} via {fetcher_name}"
    if "error" in meta:
        header_line += f" — {meta['error']}"
    header_line += " -->\n\n"
    replacement = header_line + content.rstrip() + "\n"

    if RAW_PLACEHOLDER_PAT.search(body):
        new_body = RAW_PLACEHOLDER_PAT.sub(lambda _: replacement, body, count=1)
    else:
        new_body = body.rstrip() + "\n\n" + replacement

    new_text = f"---\n{fm}\n---\n{new_body}"
    if dry_run:
        return "would-write", str(meta.get("readme_path") or meta.get("error") or "?")
    md_path.write_text(new_text, encoding="utf-8")
    return "ok", f"stars={meta.get('stars', '?')} path={meta.get('readme_path', '?')}"


def _short_url(url: str, max_len: int = 60) -> str:
    if not url or url == "?":
        return "?"
    if len(url) <= max_len:
        return url
    return url[: max_len - 1] + "…"


def _is_unhydrated(md: Path) -> bool:
    try:
        text = md.read_text("utf-8")
    except Exception:
        return False
    fm, _ = parse_frontmatter(text)
    if fm is None:
        return True
    return get_fm_field(fm, "hydrated") != "true"


def collect_candidates(type_filter: str):
    url_pat = re.compile(r'^url:\s*"?([^"\s]+)"?\s*$', re.M)
    out = []
    for md in sorted(LIB.rglob("*.md")):
        if md.name == "index.md":
            continue
        try:
            text = md.read_text("utf-8")
        except Exception:
            continue
        m = url_pat.search(text)
        if not m:
            continue
        url = m.group(1).strip()
        if type_filter == "github":
            if extract_github_repo(url):
                out.append(md)
        elif type_filter == "article":
            # Skip GitHub (handled elsewhere) + excluded hosts
            if extract_github_repo(url):
                continue
            if is_article_url(url):
                out.append(md)
    return out


def main():
    p = argparse.ArgumentParser()
    p.add_argument(
        "--type",
        required=True,
        choices=["github", "article"],
        help="Fetcher tier",
    )
    p.add_argument(
        "--limit", type=int, default=None, help="Max new hydrations this run"
    )
    p.add_argument(
        "--concurrency", type=int, default=1, help="Parallel workers (I/O-bound)"
    )
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--force", action="store_true")
    args = p.parse_args()

    if args.type == "github":
        token = os.environ.get("GITHUB_TOKEN")
        if not token:
            print(
                "! GITHUB_TOKEN not set — falling back to unauthenticated (60 req/hr)."
            )
            print(
                "  For full speed run:\n"
                '    GITHUB_TOKEN=$(op item get "GitHub - PAT (fine-grained)" '
                "--vault=ArvoClaw --fields token --reveal) \\\n"
                "      python .tools/hydrate.py --type github"
            )
        fetcher = lambda url: fetch_github(url, token)
        fetcher_name = "github-api"
    elif args.type == "article":
        jina_token = os.environ.get("JINA_API_KEY")
        if not jina_token:
            print(
                "! JINA_API_KEY not set — using anonymous tier (lower rate limits).\n"
                "  If you hit 429s frequently, get a key from https://jina.ai/reader/"
            )
        if not args.limit:
            print(
                "! --limit not set for article tier. Recommend --limit 25 for first batch."
            )
        fetcher = lambda url: fetch_article_jina(url, jina_token)
        fetcher_name = "jina-reader"
    else:
        sys.exit(f"Unknown type: {args.type}")

    all_cands = collect_candidates(args.type)
    # Pre-filter already-hydrated unless --force, so --limit = max NEW hydrations
    if not args.force:
        cands = [md for md in all_cands if _is_unhydrated(md)]
    else:
        cands = list(all_cands)
    if args.limit:
        cands = cands[: args.limit]

    print(f"Type: {args.type}")
    print(
        f"Candidates: {len(all_cands)} total | {len(cands)} to process "
        f"(concurrency={args.concurrency})"
    )
    print(
        f"Mode: {'DRY-RUN' if args.dry_run else 'WRITE'}{' (force)' if args.force else ''}"
    )
    print("---")

    ok = skipped = errored = 0
    wrote = 0
    t0 = time.time()
    total = len(cands)

    # Track in-flight URLs for visibility
    in_flight: dict[Path, tuple[str, float]] = {}
    in_flight_lock = __import__("threading").Lock()

    def _get_url(md: Path) -> str:
        try:
            fm, _ = parse_frontmatter(md.read_text("utf-8", errors="replace"))
            return get_fm_field(fm or "", "url") or "?"
        except Exception:
            return "?"

    def _run_one(md: Path):
        url = _get_url(md)
        with in_flight_lock:
            in_flight[md] = (url, time.time())
            print(
                f"  → [start  {len(in_flight):>2} in-flight]  {md.name}  ({_short_url(url)})",
                flush=True,
            )
        t_start = time.time()
        result = hydrate_file(md, fetcher_name, fetcher, args.force, args.dry_run)
        dur = time.time() - t_start
        with in_flight_lock:
            in_flight.pop(md, None)
        return md, result, dur

    done = 0
    with ThreadPoolExecutor(max_workers=max(1, args.concurrency)) as ex:
        futures = [ex.submit(_run_one, md) for md in cands]
        for fut in as_completed(futures):
            md, (status, detail), dur = fut.result()
            done += 1
            rel = md.relative_to(VAULT_ROOT)
            prefix = f"[{done:>3}/{total}  {time.time() - t0:5.1f}s  {dur:4.1f}s/item]"
            if status == "ok":
                ok += 1
                wrote += 1
                print(f"  ✓ {prefix} {rel}  [{detail}]", flush=True)
            elif status == "would-write":
                wrote += 1
                print(f"  [DRY] {prefix} {rel}  [{detail}]", flush=True)
            elif status == "skip":
                skipped += 1
                if args.dry_run:
                    print(f"  - {prefix} {rel}  ({detail})", flush=True)
            elif status == "error":
                errored += 1
                print(f"  ✗ {prefix} {rel}  ({detail})", flush=True)

            # Periodic summary every 20 completions
            if done % 20 == 0 and done < total:
                elapsed = time.time() - t0
                rate = done / elapsed if elapsed > 0 else 0
                remaining = total - done
                eta = remaining / rate if rate > 0 else 0
                print(
                    f"  ── progress: {done}/{total} ({100 * done / total:.0f}%)  "
                    f"ok={ok} err={errored}  "
                    f"rate={rate:.2f}/s  ETA ~{eta:.0f}s",
                    flush=True,
                )

    elapsed = time.time() - t0
    print("---")
    print(
        f"Done in {elapsed:.1f}s. ok={ok} skipped={skipped} errored={errored}  "
        f"rate={done / elapsed:.2f}/s"
    )


if __name__ == "__main__":
    main()
