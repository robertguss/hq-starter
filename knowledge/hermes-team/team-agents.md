---
tags:
  - knowledge
  - hermes-team
title: Hermes Team - Agents Reference
company: personal
topics:
  - hermes
  - multi-agent
  - ai-agents
created: 2026-04-20
---

# Hermes Team - Agents Reference

One file, one purpose: explain the multi-agent team to yourself and anyone else running it six months from now. This file is the live team contract. Keep it under source control; every edit should be a commit.

## Roster

- **Hermes** (orchestrator) — plans, routes, approves, synthesizes. The main profile. Not a specialist.
- **Alan** (research) — source-first, skeptical, uncertainty-tagged. AI-focused.
- **Turing** (engineering) — implementation, tests, reproducibility. Pro + personal code.
- **Mira** (writer) — longform-first, technical-developer audience. YouTube, podcast, tutorials.

See `profiles/<name>/SOUL.md` for each agent's full operating contract.

## When to use which profile

- Starting a new content piece, project, or investigation → **Hermes** scopes and decomposes
- Validating a claim, researching a new model/tool/technique, scanning AI news → **Alan**
- Drafting YouTube scripts, podcast outlines, tutorials, or repurposing content → **Mira**
- Writing code, debugging, running tests, evaluating libraries → **Turing**

## Handoff rules

- **Alan → Mira**: ranked claims with source URLs and confidence tags. No raw transcripts, no draft prose.
- **Alan → Turing**: specific techniques, libraries, or patterns to evaluate. Enough context to reproduce.
- **Turing → Hermes**: feature branch + passing tests + diff summary. Never a direct merge to main.
- **Turing → Mira**: one-paragraph "what changed and why" only when she's writing about it. No surplus.
- **Mira → Hermes**: drafted piece + change log. Not a finished publication. Hermes runs final QA.
- **Hermes → any**: scoped task with acceptance criteria and a failure action.

## Good output per profile

- **Alan**: every claim has a source URL and a confidence tag (`verified` / `probable` / `speculative`)
- **Turing**: every change has a passing test, a reproducible diff, and a one-sentence root cause
- **Mira**: every piece has a named audience, a clear thesis, no hype, and respects the siloing rule in `knowledge/author-profile.md`
- **Hermes**: every synthesis names the contributors and the open questions

## Policy ceilings

- **Alan**: read-only outside `research/`. Can read web, read repo. Cannot run shell commands. Cannot write outside sandbox.
- **Mira**: read research outputs, write to `drafts/` only. Cannot read secrets. Cannot execute code. Cannot publish directly.
- **Turing**: read repo, run sandboxed tests, write to feature branch. Every commit to `main` requires Hermes approval.
- **Hermes**: the only profile that can approve Turing's commits, merge branches, publish Mira's drafts, or trigger paid API calls above a budget ceiling.

**Rule**: no profile gets more permission than its role needs. Hermes is the only one who can widen any other profile's scope.

## Cron schedule

Edit weekly; stagger to avoid 3 AM collisions. Document every scheduled task across every profile before adding a new one.

- Mon 6 AM — **Alan**: weekly AI news digest (models, tools, community shifts)
- Tue 6 AM — **Mira**: draft refresh from Alan's digest (YouTube/podcast candidates)
- Wed 6 AM — **Turing**: test sweep across active repos + flaky test report
- Thu 6 AM — **Hermes**: weekly synthesis + handoff audit + memory-KPI check

## Day-30 failure modes to watch for

From the community ops runbook (Nyk, @nyk_builderz, 2026-04-15):

1. **Profile drift** — SOUL.md edits accumulate. Mira starts drafting implementation notes. Patch: weekly SOUL.md diff vs day-one.
2. **Handoff rot** — contracts exist but nobody enforces them. Alan sends Mira raw transcripts again. Patch: wire handoffs into the harness; fail on shape mismatch.
3. **SOUL.md bloat** — edge cases accumulate, identity gets lost in noise. Patch: cap SOUL.md at 400 words; overflow goes to `AGENTS.md`.
4. **Cron collision** — two profiles run at 3 AM. Patch: one shared cron file (this section), updated before any new schedule is added.

## Memory-KPI

Run weekly per profile:

```bash
for p in alan mira turing; do
  hermes -p $p memory-kpi --json | jq '.source_backed_pct, .stale_notes, .contradiction_notes'
done
```

If `stale_notes` crosses 15% of total notes for any profile, schedule a brain-resolve pass before that profile starts quoting itself from an obsolete context.

## Links

- Setup runbook: [[setup]]
- Alan SOUL: [[profiles/alan/SOUL|Alan]]
- Turing SOUL: [[profiles/turing/SOUL|Turing]]
- Mira SOUL: [[profiles/mira/SOUL|Mira]]
- Voice DNA (required reading for Mira): [[author-profile]]
