---
tags:
  - index
title: Library Changelog
---

# Library Changelog

Append-only log of Raindrop and X/Twitter re-syncs into the library. Newest first.

Each entry captures the items added, routing by collection, hydration stack used, and any tombstones / dead-URL decisions. Thematic notes live in the relevant `library/<slug>/_index.md` — this file is the operational record.

See also: [[_index|Library index]], `.tools/raindrop_import.py`, `.tools/hydrate.py`, `.tools/x_import.py`.

## Raindrop

### 2026-04-23 — +9 items (clean pass)

_**+9 items**, zero tombstones, zero errors — clean pass._

Routing:

- **3 → ai-tools-news/** ([[a-complete-guide-to-agentsmd]], [[hermes-atlas-the-community-map-for-hermes-agent]], [[qwen36-how-to-run-locally-unsloth-documentation]])
- **2 → ai-repos-open-source/** ([[k-dense-aimimeo]], [[ton-anywheremy-favorite-prompts-open-source-prompts]])
- **2 → dev-tools-cli/** ([[bpinheiromsmy-setup]], [[fallow-rsfallow-find-unused-code-code-duplication-circular-d]])
- **1 → academic-reference/** ([[laws-of-software-engineering]])
- **1 → productivity/** ([[refactoringhqtolaria]])

Hydration: 5 github-api (all OK), 4 defuddle (all OK — no fallback needed).

Thematic signal: the AGENTS.md/SKILL.md convention continues to dominate — three of the nine items (agentsmd guide, mimeo, my-favorite-prompts) are directly about authoring or auto-generating agent instruction files. Cross-cutting second theme is the move toward **markdown-first personal operating systems** ([[refactoringhqtolaria]] as a Mac app, [[bpinheiromsmy-setup]] as a dotfiles-shaped workspace).

### 2026-04-22 — +61 items (first `import-raindrops` skill run)

_**+61 items** net, 69 gross minus 4 duplicate raindrops and 4 dead-URL raindrops tombstoned post-sync._

First run of the new **`import-raindrops` skill** (SKILL.md in `.agents/skills/`) which codifies the full Raindrop → vault pipeline.

Routing:

- **35 → ai-repos-open-source/** (all github-api hydrated — heavy agent-skills + agent-harness cluster)
- **19 → ai-tools-news/** (defuddle + Playwright)
- **3 → academic-reference/** (DSPy, Externalization, Corpus2Skill)
- **1 → marketing-business/**
- **1 → ios-swift/**
- **1 → personal-misc/**

Hydration stack changes:

- **defuddle** replaces Jina Reader as the default HTML tier — Jina account depleted; every article-tier call was returning HTTP 402.
- New **trafilatura** tier added for algorithm diversity (retry defuddle failures with a different extractor).
- New **playwright+trafilatura** tier added as JS-SPA fallback (headless Chromium renders, then trafilatura extracts).

Playwright pass resolved the 7 previous stragglers:

- agentsearch rendered real content.
- claude.ai/design and trynia.ai rendered but caught only auth-gate / Cloudflare-challenge text.
- The other 4 (instasdr.ai, home.nomic.ai, schemaflow.dev, w2prisonbreak.com) failed with `ERR_NAME_NOT_RESOLVED` / `ERR_CONNECTION_CLOSED` — **the domains no longer exist**. Dead-URL files deleted; their `raindrop_id`s tombstoned in `.tools/raindrop_deleted.txt` so the next import doesn't resurrect them.

Residual: 2 items (claude-design, nia) are technically hydrated but the body is render-gate text — kept for the record; true content would require login + paid Cloudflare bypass.

### 2026-04-20 — +39 items, 38 rehomed out of unsorted

_39 new raindrops imported; 38 rehomed out of `unsorted/` (25 → ai-repos-open-source, 8 → ai-tools-news, 3 → academic-reference, 2 → dev-tools-cli). Hydration via github-api, defuddle, arxiv._

Note: the 5 SPA-blocked items deleted in that pass (claude-design, nomic-ai, instasdr, schemaflow, brian-oneill) were **re-created** by the 2026-04-22 re-sync (see above). Deletions don't persist unless the raindrop is also removed from the Raindrop.io account — or the id is added to `.tools/raindrop_deleted.txt`.

### 2026-04-18 — initial import + unsorted rehome

_Unsorted folder (13 items at import) rehomed across `dev-tools-cli/`, `ai-tools-news/`, `ai-repos-open-source/`, `ios-swift/`, and `productivity/`._

## X / Twitter

### 2026-04-20 (afternoon) — +30 bookmarks

_30 new X bookmarks imported (7 fresh from `ft sync`, 23 backlog). All hydrated via `hydrate.py --type twitter` (fieldtheory-cache)._

Dominant themes in the batch: coding-agent workflows (Codex, Claude Code, Hermes/OpenClaw autoresearch), Claude Design + video generation (Hyperframes), terminal tooling (zoxide, fff, skills), and a cybersecurity cluster (Google Workspace compromise forensics, DeepMind cyber paper). Outliers: at-home genome sequencing, ASO playbook, Mac cleaner utilities.
