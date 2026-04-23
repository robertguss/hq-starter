---
tags:
  - library
title: "ton-anywhere/my-favorite-prompts: open-source prompts"
url: "https://github.com/ton-anywhere/my-favorite-prompts"
company: [personal]
topics: []
created: 2026-04-23
source_type: raindrop
raindrop_id: 1693965602
source_domain: "github.com"
source_type_raindrop: link
collection: "unsorted"
collection_id: -1
hydrated: true
hydrated_at: 2026-04-23
hydrated_via: github-api
---
## Excerpt

open-source prompts. Contribute to ton-anywhere/my-favorite-prompts development by creating an account on GitHub.

## Raw Content

<!-- Hydrated 2026-04-23 via github-api -->

# my-favorite-prompts

Personal AI workspace for prompts, agents, and skills.

## Layout

- `prompts/` for reusable prompt fragments
- `agents/` for agent definitions
- `skills/` for Codex skills
- `superpowers/` for a separate upstream Superpowers checkout

## Superpowers setup

Bootstrap everything with:

```bash
./bootstrap.sh
```

Update Superpowers later with:

```bash
git -C superpowers pull --ff-only origin main
```

If you add or rename local skills, keep them under `skills/<name>/SKILL.md`.
`skills/superpowers` is reserved for the upstream Superpowers checkout.
