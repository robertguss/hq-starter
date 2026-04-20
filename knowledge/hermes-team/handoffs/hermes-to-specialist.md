---
tags:
  - knowledge
  - hermes-team
  - handoff
title: Hermes → Specialist (Alan / Mira / Turing)
company: personal
from: hermes
to: specialist
input_shape: "scoped_task {title, audience_or_target, acceptance_criteria[], failure_action, deadline?}"
output_shape: "per-specialist default output shape (see profiles/<name>/SOUL.md)"
failure_action: require_review
verification_gate: "acceptance_criteria is non-empty and every criterion is individually checkable"
created: 2026-04-20
---

# Hermes → Specialist

Generic downward-dispatch contract. Hermes is the only profile that can widen any specialist's scope, so the dispatch itself has to be precise — otherwise specialists drift outward to fill the gap.

## Required fields in the dispatch

- **title** — short name for the task
- **audience_or_target** — who the output is for (Alan: the team; Mira: a named channel/audience; Turing: a named repo/branch)
- **acceptance_criteria** — list of checkable conditions. Not aspirations. Not vibes.
- **failure_action** — what happens when a criterion cannot be met (`retry`, `escalate`, `abandon_with_note`)
- **deadline** — optional, but set it when the task feeds a downstream handoff

## Verification gate

Before sending: can I read each acceptance criterion and know how to verify it? If any criterion is "make it good" or "be thorough," rewrite before dispatching.

## Failure action

`require_review` — if a specialist returns work that doesn't satisfy acceptance criteria, Hermes returns it with the failing criterion named, not a vague "try again."
