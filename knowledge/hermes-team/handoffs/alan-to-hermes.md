---
tags:
  - knowledge
  - hermes-team
  - handoff
title: Alan → Hermes (escalation)
company: personal
from: alan
to: hermes
input_shape: "escalation {question, sources_consulted[], contradictions_found[], why_unresolvable (one sentence), options[] (each with tradeoff)}"
output_shape: "decision {choice, reason, or 'abandon'} OR widened_scope {new_permissions, new_sources_allowed}"
failure_action: block
verification_gate: "why_unresolvable is specific (e.g., 'sources disagree on X'), not generic ('need more info')"
created: 2026-04-20
---

# Alan → Hermes

Alan's escape hatch. When uncertainty cannot be resolved from available sources, Alan escalates rather than guessing. The `speculative` tag exists for known-unknowns; escalation exists for blockers.

## When to escalate

- Two independent sources contradict on a load-bearing claim
- The claim requires a paid API / benchmark / access Alan doesn't have
- The claim requires practitioner testimony Alan cannot find

## When NOT to escalate

- Alan is merely uncertain → tag it `speculative` and pass it down the line
- Alan is tired → take a break, do not escalate

## Failure action

`block` — if `why_unresolvable` is generic, Hermes returns it. Escalation without specifics is how Hermes becomes a second researcher.
