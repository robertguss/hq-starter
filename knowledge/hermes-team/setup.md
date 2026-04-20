---
tags:
  - knowledge
  - hermes-team
title: Hermes Team - Setup Runbook
company: personal
topics:
  - hermes
  - multi-agent
  - setup
created: 2026-04-20
---

# Hermes Team - Setup Runbook

Concrete steps to create the Alan / Turing / Mira profiles and wire them to the main Hermes orchestrator. Designed for a working Hermes v0.6.0+ base (Multi-Agent Profiles shipped in v0.6.0; current is v0.10.0).

## Prerequisites

- Hermes v0.6.0 or newer installed and running
- A working main Hermes profile (model provider configured, auth working)
- This vault mounted or accessible from the Hermes host

Check version:

```bash
hermes --version
```

If you're below v0.6.0, upgrade before continuing. Profiles don't exist in older versions.

## Step 1 - Create the three specialist profiles

Clone from the main working profile. This copies `config.yaml`, `.env`, and `SOUL.md` from your base — but each new profile gets its own isolated memory, sessions, skills, and gateway state.

```bash
hermes profile create alan --clone
hermes profile create mira --clone
hermes profile create turing --clone
```

## Step 2 - Verify the profiles exist

```bash
hermes profile list
ls ~/.hermes/profiles/
```

You should see `alan/`, `mira/`, `turing/` alongside the main profile.

## Step 3 - Install the SOUL.md files

Replace each cloned `SOUL.md` with the tailored version from this vault:

```bash
cp ~/Projects/vaults/hq-starter/knowledge/hermes-team/profiles/alan/SOUL.md   ~/.hermes/profiles/alan/SOUL.md
cp ~/Projects/vaults/hq-starter/knowledge/hermes-team/profiles/mira/SOUL.md   ~/.hermes/profiles/mira/SOUL.md
cp ~/Projects/vaults/hq-starter/knowledge/hermes-team/profiles/turing/SOUL.md ~/.hermes/profiles/turing/SOUL.md
```

Verify each:

```bash
head -1 ~/.hermes/profiles/alan/SOUL.md
head -1 ~/.hermes/profiles/mira/SOUL.md
head -1 ~/.hermes/profiles/turing/SOUL.md
```

## Step 4 - Wire Mira to the vault voice DNA

Mira's SOUL.md references `knowledge/author-profile.md` as required reading. For that to work, Mira needs read access to the vault. Either symlink the file into her profile or expose the vault path to her at runtime.

Option A — symlink (simplest):

```bash
ln -s ~/Projects/vaults/hq-starter/knowledge/author-profile.md ~/.hermes/profiles/mira/author-profile.md
```

Option B — vault path in her `config.yaml` / `AGENTS.md`. Use this if you want her to see more of the vault (e.g., `distillery/channels/`, `library/`).

## Step 5 - Install the shared team reference

```bash
cp ~/Projects/vaults/hq-starter/knowledge/hermes-team/team-agents.md ~/.hermes/team-agents.md
```

This is the roster + handoffs + policy + cron file. Update it in the vault, not in-place, so edits stay source-controlled.

## Step 6 - Run each profile

```bash
hermes -p alan
hermes -p mira
hermes -p turing
```

Main Hermes (the orchestrator) runs with no `-p` flag.

## Step 7 - First handoff test

Pick a small, real task to prove the handoff chain works. Example: a YouTube video on one recent AI tool.

1. Main Hermes scopes: "Next week's YouTube video on [tool]. Audience: technical developers. Deliverable: script."
2. Hand to Alan: research [tool] — current state, honest community opinion, notable tradeoffs.
3. Alan returns ranked claims with sources and confidence tags.
4. Hand Alan's output to Mira.
5. Mira drafts a YouTube script using the voice in `author-profile.md`.
6. Hand back to main Hermes for final QA.

Watch for: does Mira's draft sound like Robert? Does Alan cite everything? Does the siloing rule hold? If any step feels wrong, adjust the relevant `SOUL.md` in this vault, copy to the live profile, and re-run.

## Step 8 - Schedule weekly maintenance (optional, start after 2 weeks of use)

Add to your calendar or a cron:

- **Weekly SOUL.md diff** — compare each profile's `SOUL.md` to the vault version. Any drift gets reviewed.
- **Weekly memory-KPI** — run the loop in `team-agents.md`. Schedule a brain-resolve pass if `stale_notes` exceeds 15% for any profile.
- **Weekly cron audit** — check `team-agents.md` cron schedule against reality. Stagger any new jobs.

## Notes on the orchestrator profile

The main Hermes profile is the orchestrator. Its `SOUL.md` is your existing one. You don't need to rewrite it — but when you're ready, add these operating principles:

- Plans, decomposes, routes — does not do specialist work itself
- Runs final QA on Mira's drafts, Turing's diffs, and Alan's syntheses
- The only profile that approves merges, publishes drafts, or spends above a budget ceiling
- Structured and decisive in tone

Cap at 400 words (the Nyk SOUL.md bloat rule).

## Roll-forward and roll-back

Every change to a profile's identity happens in this vault first, then `cp` to `~/.hermes/profiles/<name>/SOUL.md`. If a change breaks something, `git log` here is the rollback path — not the live profile directory.
