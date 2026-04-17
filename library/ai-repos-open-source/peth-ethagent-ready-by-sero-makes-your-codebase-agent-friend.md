---
tags:
  - library
title: "peth-eth/agent-ready-by-sero: Makes your codebase agent-friendly and keeps it that way. Small files so agents don't waste tokens. CLAUDE.md in every directory so they don't have to guess. Tests so they check their own work. Run once, it bolts rules into your global config — every project enforces standards automatically."
url: "https://github.com/peth-eth/agent-ready-by-sero"
company: [personal]
topics: []
created: 2026-04-05
source_type: raindrop
raindrop_id: 1673016708
source_domain: "github.com"
source_type_raindrop: link
collection: "AI Repos & Open Source"
collection_id: 69284315
hydrated: true
hydrated_at: 2026-04-17
hydrated_via: github-api
---
## Excerpt

Makes your codebase agent-friendly and keeps it that way. Small files so agents don't waste tokens. CLAUDE.md in every directory so they don't have to guess. Tests so they check their own w...

## Raw Content

<!-- Hydrated 2026-04-17 via github-api -->

# Agent Ready by Sero

Makes your codebase agent-friendly and keeps it that way. Two modes — a quick structural lint for daily use, and a deep scan with auto-fixing for when you're serious.

---

## Two Modes

### `/agent-ready` — Quick Mode (default)

6-check structural lint. Fast, report-only. Use it anytime.

| Check | What It Flags |
|-------|--------------|
| File sizes | Source files over 300 lines |
| Directory bloat | Directories with 20+ files |
| Agent context | Missing CLAUDE.md files in root + key subdirectories |
| Type safety | `any` sprawl (TS), `# type: ignore` (Python), `interface{}` (Go) |
| Linting | Missing linter config |
| Test patterns | Test-to-source ratio below 1:5 |

Output: PASS/WARN/FAIL per check, priority fixes, offer to fix.

### `/agent-ready full` — Full Mode

20 criteria across 5 pillars. Maturity levels L1-L5. Improvement plan. Auto-fixing.

**The 5 Pillars:**

| Pillar | What It Checks |
|--------|---------------|
| **Feedback Loops** | Build command, test command, linter, formatter, type checking, pre-commit hooks |
| **Structure** | File sizes, directory sizes, lock file, type safety violations |
| **Documentation** | CLAUDE.md/AGENTS.md, subdirectory context, README setup, .env.example, .gitignore |
| **Testing** | Tests exist, test-to-source ratio, test patterns |
| **Safety** | No hardcoded secrets, dependency update automation |

**Maturity Levels:**

| Level | Name | What It Means |
|-------|------|---------------|
| **L1** | Functional | Can build, has basics (linter, lock file, README, .gitignore, tests exist) |
| **L2** | Documented | Agent can understand the project (CLAUDE.md, type checking, pre-commit hooks, env docs) |
| **L3** | Agent-Ready | Agent can work effectively (tests runnable, small files, subdir context, good test ratio) |
| **L4** | Optimized | Agent works with confidence (formatter, test patterns, no secrets, dep updates) |
| **L5** | Exemplary | Everything dialed |

**L3 is the target for most projects.**

Full mode scans, scores, generates a prioritized improvement plan, then offers to auto-fix — working one level at a time, committing after each.

## First-Run Integration

On first run, appends **Agent Readiness Standards** to your global `~/.claude/CLAUDE.md` — file size limits, CLAUDE.md requirements, type safety, test minimums, linting. Happens once.

## Installation

```bash
mkdir -p ~/.claude/skills/agent-ready
curl -o ~/.claude/skills/agent-ready/SKILL.md \
  https://raw.githubusercontent.com/peth-eth/agent-ready-by-sero/main/SKILL.md
```

Then run `/agent-ready` in any project.

## What Full Mode Auto-Fixes

**No confirmation needed:**
- Missing CLAUDE.md files (reads directory, writes real context)
- Missing .env.example (scans code for env var usage)
- Missing/sparse .gitignore
- Missing lint/format scripts
- Pre-commit hooks (husky for JS, pre-commit for Python)
- Basic test scaffolds when zero tests exist

**Asks first:**
- Linter rule changes
- TypeScript strict mode
- Dependabot/Renovate setup
- Splitting oversized files
- Type safety violations

## Impact

For a medium project (50-100 source files), going from unstructured to agent-ready:

- **40-60% fewer tokens per task** (smaller files, faster orientation)
- **2-3x faster task completion** (fewer search cycles, less backtracking)
- **3-5x more parallelizable** (independent files instead of monoliths)
