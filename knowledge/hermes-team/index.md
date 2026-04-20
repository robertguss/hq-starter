---
tags:
  - index
  - hermes-team
title: Hermes Team
company: personal
topics:
  - hermes
  - multi-agent
  - ai-agents
created: 2026-04-20
---

# Hermes Team

A three-specialist Hermes multi-agent setup for Robert: **Alan** (research), **Turing** (engineering), **Mira** (writer). The main Hermes profile stays as the orchestrator.

## Why three specialists, not four

The canonical community build (Neo, @NeoAIForecast, 2026-04-12) is four profiles: Hermes + Alan + Mira + Turing. We're running three specialists to start - no "second writer" or "news agent" until the current three prove their handoffs. Every profile adds maintenance overhead (SOUL.md diffs, handoff contracts, memory-KPI audits). Start small.

## Files in this folder

- [[team-agents]] - the live team contract: roster, policy, cron
- [[setup]] - step-by-step CLI runbook to create the profiles and install the SOUL.md files
- [[handoffs/index|handoffs/]] - machine-parseable contracts for every directed profile pair
- `profiles/<name>/SOUL.md` - each specialist's operating contract (identity source of truth)
- `profiles/<name>/SOUL.day-one.md` - frozen day-one snapshot used by the drift check
- `scripts/soul_drift_check.py` - diffs live SOUL.md against day-one baseline (run weekly; Python stdlib only)

## Design decisions

- **One engineering profile**, not two. Pro + personal code live in one profile; context lives in project-level `AGENTS.md` per repo.
- **One writer profile with format skills**, not multiple writers per channel. Mira handles longform first (YouTube script, podcast outline, tutorial), then derives newsletter / thread / LinkedIn via accumulated skills. Same voice, different output shapes.
- **Alan stays AI-focused**. Other research domains (theology, philosophy of mind, music) live in the main Hermes profile or get a dedicated profile later if they become daily work.
- **Siloing rule is load-bearing for Mira**. Technical content stays technical. See `author-profile.md`.
- **No Echo/repurposer profile yet**. Repurposing lives in Mira's skills, per Nous Research's 40%-faster-with-accumulated-skills benchmark. Split later only if Mira's voice starts drifting across formats.

## References

- [[author-profile]] - Robert's voice DNA (required reading for Mira)
- Community source 1: Neo @NeoAIForecast - "How to Build a Multi-Agent Team in Hermes" (2026-04-12)
- Community source 2: Nyk @nyk_builderz - "The Ultimate Hermes Guide - from one agent to a 4-profile team that still feels coherent on day 30" (2026-04-15)

Both articles are in `Clippings/` of this vault.
