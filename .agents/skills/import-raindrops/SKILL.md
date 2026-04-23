---
name: import-raindrops
description: Import Raindrop.io bookmarks into the HQ vault as hydrated library/ markdown. Runs the Raindrop → library/ importer to create stubs with `hydrated: false`, then chains the tiered hydrator across github, arxiv, pdf, defuddle (default HTML), trafilatura (HTML fallback), and social types. Use when the user asks to import, sync, or pull in Raindrop.io bookmarks, mentions raindrops or a Raindrop collection, or drops a raindrop.io URL or collection ID.
---

# import-raindrops

Two-phase workflow for Raindrop.io → HQ vault:

1. **Import** — `.tools/raindrop_import.py` creates one `library/<collection-slug>/<slug>.md` per bookmark with frontmatter and `hydrated: false`. Idempotent by `raindrop_id`.
2. **Hydrate** — `.tools/hydrate.py --type <tier>` fills the `## Raw Content` placeholder per URL type and flips `hydrated: true`.

X/Twitter bookmarks live in a **separate** pipeline (`.tools/x_import.py` + the `fieldtheory` skill). Do **not** run `--type twitter` here — those items are already hydrated in-body upstream.

## Quick start

```bash
# 1. Import (dry-run first if this is a first-time or large sync)
RAINDROP_TOKEN=$(op read 'op://ArvoClaw/Raindrop API/test_token') \
  uv run .tools/raindrop_import.py --dry-run

RAINDROP_TOKEN=$(op read 'op://ArvoClaw/Raindrop API/test_token') \
  uv run .tools/raindrop_import.py

# 2. Hydrate — one tier at a time
GITHUB_TOKEN=$(op item get "GitHub - PAT (fine-grained)" --vault=ArvoClaw --fields token --reveal) \
  uv run .tools/hydrate.py --type github --limit 50

uv run .tools/hydrate.py --type arxiv   --limit 25
uv run .tools/hydrate.py --type pdf     --limit 25

# Default HTML path (no API key, no credits, just the defuddle CLI)
uv run .tools/hydrate.py --type defuddle --limit 50

# Retry defuddle's failures with a different extraction algorithm
uv run --with trafilatura .tools/hydrate.py --type trafilatura --limit 50

# Last-resort for JS-SPAs (headless Chromium renders, then trafilatura extracts)
# First-time only: uv run --with playwright playwright install chromium
uv run --with playwright --with trafilatura .tools/hydrate.py --type playwright --limit 25

uv run .tools/hydrate.py --type social --limit 25

# Optional: only when Jina credits are topped up
# JINA_API_KEY=$(op read 'op://ArvoClaw/Jina - Reader API Key/api_key') \
#   uv run .tools/hydrate.py --type article --limit 100
```

Full flag reference lives in the script docstrings: `.tools/raindrop_import.py` and `.tools/hydrate.py`.

## Lifecycle

### 1. Import

- Confirm `RAINDROP_TOKEN` is resolved via `op read` — never hardcode.
- Default `--collection 0` pulls all collections. Filter with `--collection <ID>` if the user names one.
- Report: count created, count skipped (already present), count tombstoned (in `raindrop_deleted.txt`), and which collection slugs gained new files.

**Deletions don't persist by default.** If the user deletes a `library/<slug>.md` without also removing the raindrop from Raindrop.io, the next import will re-create it. To make a deletion permanent on the vault side, add the `raindrop_id` to `.tools/raindrop_deleted.txt` (one per line, `#` for comments). The importer skips any id in that ledger.

### 2. Hydrate — tier order

Each tier is idempotent (skips items already `hydrated: true` unless `--force`). Run in this order:

- [ ] `--type github` (needs `GITHUB_TOKEN`) — READMEs via GitHub API.
- [ ] `--type arxiv` — abstract + links; heavier extraction lives in the `process-pdfs` skill.
- [ ] `--type pdf` — downloads and extracts inline PDF links.
- [ ] `--type defuddle` — **default HTML fetcher** (local `defuddle` CLI, no API, no credits).
- [ ] `--type trafilatura` — **fallback** for items defuddle can't extract. Different algorithm, pure-Python, installed ad-hoc via `uv run --with trafilatura`.
- [ ] `--type playwright` — **last-resort for JS-SPAs.** Launches headless Chromium, lets the page render, then runs trafilatura over the rendered HTML. Use when defuddle and trafilatura both return empty-shell errors because the content is client-rendered (claude.ai/design, trynia.ai, agentsearch.sh, etc.). Invoke via `uv run --with playwright --with trafilatura .tools/hydrate.py --type playwright`. First-time setup: `uv run --with playwright playwright install chromium` (~170 MB one-time browser download). Slower than other tiers (2–10s per URL). Does **not** solve paywalls, 403s, or 429s.
- [ ] `--type social` — Hacker News and Reddit threads.
- [ ] `--type article` (needs `JINA_API_KEY` with credits) — **opt-in only.** Jina Reader is fast and clean when paid, but the account can run out of credits and return 402 on every call. Do **not** run this tier unless the user explicitly asks or confirms credits are available.

**Skip `--type twitter`.** X bookmarks come from the fieldtheory pipeline.

### 3. Handle the long tail

After defuddle + trafilatura + playwright, some items still won't hydrate. The common classes, with resolutions:

- **JS-SPAs** — use `--type playwright` (above). If that still fails, the page may have additional render gates (login, Cloudflare challenge) — skip or manual copy-paste.
- **403 / 429 / fetch failed / timeout** — the site is blocking or flaky. Retry later, use Wayback Machine, or skip. Playwright can sometimes help here because it presents as a real browser, but site-level blocks (Cloudflare bot mode) often defeat it too.
- **Paywalls** — no extractor will bypass. Skip or manually paste an excerpt.

If the user decides an item isn't worth hydrating, the right move is (a) delete the `library/<slug>.md` file, then (b) add its `raindrop_id` to `.tools/raindrop_deleted.txt` so the next import doesn't re-create it.

List the remaining `hydrated: false` files and surface them to the user; do **not** keep re-running tiers in a loop.

On unfamiliar tiers start with `--limit 25`, spot-check 2–3 outputs, then bump.

### 4. PDFs → DEVONthink reminder

The `pdf` tier writes markdown into `library/` but the canonical PDF belongs in DEVONthink. After a `--type pdf` run, remind the user to archive the PDFs into DEVONthink and (optionally) paste the item URL into each note's `devonthink_url:` frontmatter for round-trip.

### 5. Update the library indexes

Newly hydrated items should be woven into the relevant `library/<slug>/_index.md` (per-collection synthesis) and a summary note added to `library/_CHANGELOG.md`. The top-level `library/_index.md` only needs touching if the batch introduces a genuinely cross-shelf pattern. These index files together form the compiled wiki, not a file listing (see `distillery/index.md` and the project `CLAUDE.md`). Use wikilinks to connect new items to existing themes; don't just append a one-liner.

### 6. Commit

Do **not** auto-commit. Run the project `CLAUDE.md` pre-commit checklist (indexes current, frontmatter matches `knowledge/hq-vault-design.md`, wikilinks resolve), then surface a proposed commit message and wait for explicit go-ahead.

## References

- Import script: `.tools/raindrop_import.py`
- Hydrate script: `.tools/hydrate.py` (all tier details in docstring)
- X/Twitter pipeline (separate): `.tools/x_import.py` + `fieldtheory` skill
- 1Password env template: `.tools/.raindrop.env.tpl`
- Frontmatter spec: `knowledge/hq-vault-design.md`
- Library synthesis structure: `library/_index.md` (top-level) + `library/<slug>/_index.md` (per-collection) + `library/_CHANGELOG.md` (resync log)
