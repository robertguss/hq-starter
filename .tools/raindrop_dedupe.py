#!/usr/bin/env python3
"""
Find and remove duplicate raindrops in Raindrop.io.

Groups raindrops by normalized URL (lowercase host, strip leading
`www.`, strip trailing `/`, drop utm_*/ref/source/fbclid/gclid params).
In each dup group the oldest raindrop_id wins; newer rids are deleted
via the API.

If a deleted rid already has a corresponding `library/<...>.md` file
(matched by `raindrop_id` frontmatter), its id is auto-appended to
`.tools/raindrop_deleted.txt` so future imports don't resurrect it.

Usage:
  RAINDROP_TOKEN=$(op read 'op://ArvoClaw/Raindrop API/test_token') \\
    python .tools/raindrop_dedupe.py [--apply] [--limit N]

Default is a dry-run: prints each dup group, marks the winner (keep)
and losers (delete). Pass --apply to actually delete.
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
from pathlib import Path

API_BASE = "https://api.raindrop.io/rest/v1"
VAULT_ROOT = Path(__file__).resolve().parent.parent
LIBRARY_DIR = VAULT_ROOT / "library"
LEDGER_PATH = Path(__file__).resolve().parent / "raindrop_deleted.txt"

TRACKING_PARAMS = {"ref", "source", "fbclid", "gclid", "mc_cid", "mc_eid", "igshid"}


def normalize_url(url: str) -> str:
    """Normalize a URL for dedupe matching. Returns empty string on
    parse errors so those raindrops group together (easier to spot)."""
    try:
        u = urllib.parse.urlparse(url.strip())
    except Exception:
        return ""
    if not u.netloc:
        return ""
    host = u.netloc.lower()
    if host.startswith("www."):
        host = host[4:]
    q = urllib.parse.parse_qsl(u.query, keep_blank_values=False)
    q = [(k, v) for k, v in q if not k.startswith("utm_") and k not in TRACKING_PARAMS]
    q.sort()
    query = urllib.parse.urlencode(q)
    path = u.path.rstrip("/") or "/"
    return urllib.parse.urlunparse((u.scheme.lower(), host, path, "", query, ""))


def api_request(method: str, path: str, token: str, **params):
    url = f"{API_BASE}{path}"
    if params and method == "GET":
        url += "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(
        url,
        method=method,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        body = resp.read().decode("utf-8", "replace")
        return json.loads(body) if body else {}


def fetch_collections(token):
    data = api_request("GET", "/collections", token)
    return {c["_id"]: c.get("title", "Untitled") for c in data.get("items", [])}


def fetch_all_raindrops(token, limit=None):
    page = 0
    per_page = 50
    fetched = 0
    while True:
        data = api_request(
            "GET",
            "/raindrops/0",
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
        time.sleep(0.2)


def vault_rid_to_path():
    """Map raindrop_id -> Path of the library/ file that references it."""
    rid_pat = re.compile(r"^raindrop_id:\s*(\d+)\s*$", re.M)
    out = {}
    if not LIBRARY_DIR.exists():
        return out
    for md in LIBRARY_DIR.rglob("*.md"):
        if md.name == "index.md":
            continue
        try:
            m = rid_pat.search(md.read_text("utf-8"))
        except Exception:
            continue
        if m:
            out[int(m.group(1))] = md
    return out


def index_wikilink_stems():
    """Return a set of basenames (without .md) referenced as [[wikilinks]]
    in library/_index.md and every library/<slug>/_index.md. Used to prefer
    files that have been woven into the synthesis wiki when picking dedupe
    winners."""
    stems = set()
    for idx in [LIBRARY_DIR / "_index.md", *LIBRARY_DIR.glob("*/_index.md")]:
        if not idx.exists():
            continue
        try:
            text = idx.read_text("utf-8")
        except Exception:
            continue
        stems.update(re.findall(r"\[\[([^\[\]|#\n]+?)\]\]", text))
    return stems


def append_to_ledger(rids_with_reasons):
    """Append tombstones with a dated section header. `rids_with_reasons`
    is a list of (rid, reason) tuples."""
    if not rids_with_reasons:
        return
    from datetime import date

    header = f"\n# --- Dedupe tombstones {date.today().isoformat()} ---\n"
    lines = [header] + [f"{rid}  # {reason}\n" for rid, reason in rids_with_reasons]
    with LEDGER_PATH.open("a", encoding="utf-8") as f:
        f.writelines(lines)


def delete_raindrop(rid, token):
    api_request("DELETE", f"/raindrop/{rid}", token)


def _short(s, n=60):
    s = (s or "").replace("\n", " ")
    return s if len(s) <= n else s[: n - 1] + "…"


def main():
    p = argparse.ArgumentParser()
    p.add_argument(
        "--apply", action="store_true", help="Actually delete (default: dry-run)"
    )
    p.add_argument(
        "--limit", type=int, default=None, help="Cap raindrops fetched (testing)"
    )
    args = p.parse_args()

    token = os.environ.get("RAINDROP_TOKEN")
    if not token:
        sys.exit(
            "RAINDROP_TOKEN not set. Run:\n"
            "  RAINDROP_TOKEN=$(op read 'op://ArvoClaw/Raindrop API/test_token') "
            "python .tools/raindrop_dedupe.py"
        )

    print("Fetching collections…")
    collections = fetch_collections(token)
    collections[-1] = "Unsorted"
    collections[0] = "All"

    print("Fetching all raindrops…")
    all_rps = list(fetch_all_raindrops(token, args.limit))
    print(f"  → {len(all_rps)} raindrops fetched")

    groups = {}
    for r in all_rps:
        key = normalize_url(r.get("link", ""))
        if not key:
            continue
        groups.setdefault(key, []).append(r)

    dups = {k: v for k, v in groups.items() if len(v) > 1}
    print(
        f"Dup groups: {len(dups)}  (covering {sum(len(v) for v in dups.values())} raindrops)"
    )
    if not dups:
        print("No duplicates. Exiting.")
        return

    vault_map = vault_rid_to_path()
    index_links = index_wikilink_stems()
    print(
        f"Vault rid→file mappings: {len(vault_map)}  (index wikilinks: {len(index_links)})"
    )

    mode = "APPLY (deleting)" if args.apply else "DRY-RUN (no deletions)"
    print(f"Mode: {mode}")
    print("---")

    losers = []
    vault_files_to_delete = []
    for key, rps in sorted(dups.items()):
        # Winner rule (cascading):
        #   0 vault files: oldest rid wins (Raindrop-side only)
        #   1 vault file:  that rid wins (preserve hydration work)
        #   2+ vault files:
        #     (a) prefer one whose basename is wikilinked in any library/_index.md
        #     (b) else prefer CLEAN slug (no `-<rid>` suffix)
        #     (c) else oldest rid wins
        with_vault = [r for r in rps if r.get("_id") in vault_map]
        if len(with_vault) == 0:
            winner = sorted(rps, key=lambda r: r.get("_id", 0))[0]
        elif len(with_vault) == 1:
            winner = with_vault[0]
        else:
            linked = [r for r in with_vault if vault_map[r["_id"]].stem in index_links]
            if len(linked) == 1:
                winner = linked[0]
            else:
                clean = [
                    r
                    for r in with_vault
                    if not vault_map[r["_id"]].stem.endswith(f"-{r['_id']}")
                ]
                if len(clean) == 1:
                    winner = clean[0]
                else:
                    winner = sorted(with_vault, key=lambda r: r.get("_id", 0))[0]
        to_delete = [r for r in rps if r is not winner]
        # Print in oldest-first order for readability
        rps_sorted = sorted(rps, key=lambda r: r.get("_id", 0))

        print(f"\n{key}  (×{len(rps)})")
        for r in rps_sorted:
            rid = r.get("_id")
            coll_id = (r.get("collection") or {}).get("$id", 0)
            coll = collections.get(coll_id, f"?{coll_id}")
            has_vault = "yes" if rid in vault_map else "no "
            role = "KEEP " if r is winner else "DEL  "
            title = _short(r.get("title") or "")
            created = (r.get("created") or "")[:10]
            print(
                f"  {role} rid={rid:>11}  coll={coll:<22}  created={created}  vault={has_vault}  {title}"
            )

        for r in to_delete:
            rid = r.get("_id")
            reason = (
                f"dup of rid={winner.get('_id')} "
                f"({collections.get((r.get('collection') or {}).get('$id', 0), '?')})"
            )
            losers.append((rid, reason, r))
            # If this loser has a vault file AND winner also has one,
            # the loser's vault file is redundant — queue for deletion.
            # If winner has no vault file, we keep the loser's vault file
            # and re-point its raindrop_id to the winner (so hydration survives).
            if rid in vault_map:
                if winner.get("_id") in vault_map:
                    vault_files_to_delete.append((rid, vault_map[rid]))
                else:
                    vault_files_to_delete.append(
                        ("repoint", rid, winner.get("_id"), vault_map[rid])
                    )

    print("\n---")
    print(f"Losers to delete from Raindrop: {len(losers)}")

    vault_tombstones = [(rid, reason) for rid, reason, _ in losers if rid in vault_map]
    if vault_tombstones:
        print(
            f"Of which {len(vault_tombstones)} have vault files — will be "
            f"tombstoned in {LEDGER_PATH.name}."
        )
    if vault_files_to_delete:
        deletes = [x for x in vault_files_to_delete if x[0] != "repoint"]
        repoints = [x for x in vault_files_to_delete if x[0] == "repoint"]
        if deletes:
            print(f"Vault files to delete (redundant dupes): {len(deletes)}")
            for rid, path in deletes:
                print(f"  - {path.relative_to(VAULT_ROOT)}  (rid={rid})")
        if repoints:
            print(
                f"Vault files to repoint raindrop_id (winner has no vault file): {len(repoints)}"
            )
            for _, old_rid, new_rid, path in repoints:
                print(f"  - {path.relative_to(VAULT_ROOT)}  rid={old_rid} → {new_rid}")
    if not args.apply:
        print("\nDry-run complete. Re-run with --apply to actually delete.")
        return

    # 1) Repoint vault files where winner has no vault copy
    repoints = [x for x in vault_files_to_delete if x[0] == "repoint"]
    for _, old_rid, new_rid, path in repoints:
        text = path.read_text("utf-8")
        new_text = re.sub(
            rf"^raindrop_id:\s*{old_rid}\s*$",
            f"raindrop_id: {new_rid}",
            text,
            count=1,
            flags=re.M,
        )
        if new_text != text:
            path.write_text(new_text, encoding="utf-8")
            print(
                f"  ↻ repointed {path.relative_to(VAULT_ROOT)} rid={old_rid} → {new_rid}"
            )
        else:
            print(
                f"  ! failed to repoint {path.relative_to(VAULT_ROOT)} (pattern not matched)"
            )

    # 2) Delete redundant vault files (both winner + loser had files)
    redundant = [x for x in vault_files_to_delete if x[0] != "repoint"]
    for rid, path in redundant:
        try:
            path.unlink()
            print(f"  ✗ removed {path.relative_to(VAULT_ROOT)}  (rid={rid})")
        except Exception as e:
            print(f"  ! failed to remove {path}: {e}")

    # 3) Delete losers from Raindrop
    print("\nDeleting duplicates from Raindrop…")
    deleted = 0
    failed = 0
    for rid, reason, _ in losers:
        try:
            delete_raindrop(rid, token)
            print(f"  ✓ deleted {rid}")
            deleted += 1
        except urllib.error.HTTPError as e:
            print(f"  ✗ {rid}: HTTP {e.code}")
            failed += 1
        except Exception as e:
            print(f"  ✗ {rid}: {type(e).__name__}: {e}")
            failed += 1
        time.sleep(0.3)  # keep under rate limit

    # 4) Tombstone (belt-and-suspenders — in case a delete silently failed
    # or the raindrop comes back; tombstone prevents re-import)
    if vault_tombstones:
        append_to_ledger(vault_tombstones)
        print(f"Appended {len(vault_tombstones)} tombstones to {LEDGER_PATH.name}")

    print(f"\nDone. Deleted from Raindrop: {deleted}  Failed: {failed}")


if __name__ == "__main__":
    main()
