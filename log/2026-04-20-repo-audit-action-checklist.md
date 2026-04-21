---
tags:
  - log
title: "Repo Audit — Prioritized Action Checklist"
date: 2026-04-20
type: observation
---

## Summary

Prioritized action checklist derived from the 2026-04-20 repository audit. The goal is to move the vault from strong strategic structure to consistent execution.

## Details

## Priority 1 — Make the active initiatives executable

### 1. Upgrade initiative notes from stubs to operating docs
- [ ] Fill in `## Context` in:
  - `initiatives/pyloop.md`
  - `initiatives/sweep.md`
  - `initiatives/sentinel.md`
  - `initiatives/pocket-apologist.md`
- [ ] Replace placeholder `## Key Results` checkboxes with real measurable outcomes
- [ ] Add target dates where known

### 2. Create concrete task files for each active initiative
- [ ] Create 3–7 tasks for `[[initiatives/pyloop]]`
- [ ] Create 3–7 tasks for `[[initiatives/sweep]]`
- [ ] Create at least 1–3 starter tasks for `[[initiatives/sentinel]]`
- [ ] Create at least 1–3 starter tasks for `[[initiatives/pocket-apologist]]`
- [ ] Update `tasks/index.md` so every initiative has real linked tasks

### 3. Set project focus order explicitly
- [ ] Confirm active sequencing:
  1. `[[initiatives/pyloop]]`
  2. `[[initiatives/sweep]]`
  3. `[[initiatives/sentinel]]`
  4. `[[initiatives/pocket-apologist]]`
- [ ] If needed, pause one or more initiatives rather than keeping all four equally active

## Priority 2 — Establish an execution rhythm

### 4. Start weekly logging
- [ ] Create the first weekly summary in `log/weekly/`
- [ ] Add what moved this week by initiative
- [ ] Add blockers and next-week commitments
- [ ] Update `log/weekly/index.md`

### 5. Capture real decisions as they happen
- [ ] Log pricing, scope, launch, and technical-architecture decisions in `log/`
- [ ] Especially capture decisions for:
  - PyLoop v1 scope
  - Sweep launch plan and waitlist strategy
  - Sentinel pricing/positioning

## Priority 3 — Prove the distillery pipeline works

### 6. Run one end-to-end content cycle
- [ ] Create one research brief in `distillery/research/`
- [ ] Draft one content piece in `distillery/content/<channel>/`
- [ ] Update `distillery/plan.md`
- [ ] Use `[[knowledge/pyloop]]` as the likely first source

### Recommended first content test
- [ ] Topic: PyLoop technical deep dive
- [ ] Candidate angle: AST-native Python agent harness vs text-diff agents
- [ ] Candidate outputs:
  - blog post
  - newsletter draft
  - X thread derived from the longform piece

## Priority 4 — Tighten vault hygiene

### 7. Fix naming and scaffolding drift
- [ ] Review `tasks/sentinela/` and rename if it is a typo
- [ ] Remove or populate empty scaffolding folders over time
- [ ] Check all active notes appear in the proper `index.md`

### 8. Keep dashboards and indexes trustworthy
- [ ] Verify every file in `initiatives/`, `tasks/`, `knowledge/`, `library/`, and `log/` appears in the proper index
- [ ] Confirm README “What’s Active Right Now” matches active initiatives
- [ ] Confirm dashboard filters match current frontmatter conventions

## Outcome

Success means the vault stops being mainly a well-designed knowledge system and starts functioning as a weekly execution system: active initiatives with measurable outcomes, visible tasks, regular logs, and at least one proven content-production cycle.