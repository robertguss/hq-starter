---
tags:
  - library
title: "dennisonbertram/ux-toolkit: Claude Code plugin: UX story generation, browser-based UX testing, and automated issue implementation"
url: "https://github.com/dennisonbertram/ux-toolkit"
company: [personal]
topics: []
created: 2026-04-18
source_type: raindrop
raindrop_id: 1688629210
source_domain: "github.com"
source_type_raindrop: link
collection: "unsorted"
collection_id: -1
hydrated: true
hydrated_at: 2026-04-20
hydrated_via: github-api
---
## Excerpt

Claude Code plugin: UX story generation, browser-based UX testing, and automated issue implementation - dennisonbertram/ux-toolkit

## Raw Content

<!-- Hydrated 2026-04-20 via github-api -->

# UX Toolkit — Claude Code Plugin

A three-skill Claude Code plugin for end-to-end UX quality assurance:

1. **`/ux-paths`** — Analyze your codebase and generate an exhaustive catalog of user journey stories (short, medium, and long flows)
2. **`/ux-walker`** — Walk those stories through a real browser, audit UX quality, auto-fix small issues, and file GitHub issues for larger ones
3. **`/walk-the-issues`** — Groom open GitHub issues and implement them one-by-one with branching, swarm implementation, testing, and PR creation

## Install

```bash
# From the Claude Code marketplace (when published)
/plugin marketplace add dennisonbertram/ux-toolkit
/plugin install ux-toolkit

# Or for local development
claude --plugin-dir /path/to/ux-toolkit
```

## Usage

```
/ux-paths                    # Generate user journey catalog
/ux-paths authentication     # Focus on a specific area

/ux-walker                   # Walk all stories through the browser
/ux-walker http://localhost:3000 --full    # Full re-walk
/ux-walker --focus "onboarding"            # Focus on a topic

/walk-the-issues             # Groom + implement all open issues
```

## Workflow

The three skills form a pipeline:

```
/ux-paths → generates docs/ux-paths/catalog.md
     ↓
/ux-walker → tests catalog in browser, files GitHub issues
     ↓
/walk-the-issues → grooms + implements those issues with PRs
```

## Requirements

- [Claude Code](https://claude.ai/code) CLI
- `gh` CLI (authenticated) — for issue filing and PR creation
- `agent-browser` — for browser automation in ux-walker
- A running dev server for your app (ux-walker auto-detects or accepts a URL)

## Skills Overview

### `/ux-paths` — User Journey Story Generator

Spawns a swarm of parallel sub-agents to:
1. **Discover** your app's features, routes, and capabilities
2. **Generate** realistic user journey stories (8-12 parallel agents)
3. **Consolidate** into a deduplicated catalog with coverage matrix

Output: `docs/ux-paths/catalog.md`

### `/ux-walker` — Browser-Based UX Testing

Walks the story catalog through a real browser using `agent-browser`:
- Sequential story walks with parallel fix agents
- 7-criterion UX audit rubric (simplicity, disclosure, layout, visual, happy-path, a11y, error-handling)
- Auto-fixes small issues (CSS, typos, spacing) in worktree-isolated branches
- Files GitHub issues for larger problems with screenshots and evidence
- Generates comprehensive run reports

Output: `docs/ux-walker/latest-report.md`

### `/walk-the-issues` — Issue Grooming & Implementation Loop

Two-phase workflow:
1. **Grooming** — Parallel agents evaluate all open issues for clarity, scope, and blockers
2. **Implementation Loop** — For each well-specified issue: branch → research → swarm implement → test → PR

Output: PRs for each issue with regression tests and documentation

## License

MIT
