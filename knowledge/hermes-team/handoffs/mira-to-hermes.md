---
tags:
  - knowledge
  - hermes-team
  - handoff
title: Mira → Hermes
company: personal
from: mira
to: hermes
input_shape: "draft {title, target_channel, audience, thesis (one sentence), body, change_log[] (what changed from prior revision and why)}"
output_shape: "decision {approve_publish | request_changes[] | reject_with_reason}"
failure_action: block
verification_gate: "target_channel and audience are named AND thesis is a single sentence AND siloing rule holds (technical stays technical, theological stays theological)"
created: 2026-04-20
---

# Mira → Hermes

The publication gate. Mira never publishes directly. Hermes runs final QA against `author-profile.md` before anything ships under Robert's name.

## What Hermes checks

- **Siloing rule** — any apologetics leakage in a technical piece is an automatic reject
- **Voice** — Chesterton clarity, Knausgård honesty, Basecamp directness. Does it sound like Robert or like an AI trying to sound like Robert?
- **Hype** — any fake enthusiasm, "game-changer" language, or performative expertise gets cut
- **Claim provenance** — every non-trivial factual claim traces back to Alan's ranked list or Robert's lived experience

## Failure action

`block` — if the siloing rule is violated, reject without editing. The fix is a rewrite by Mira, not a patch by Hermes.
