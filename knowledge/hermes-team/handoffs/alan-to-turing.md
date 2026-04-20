---
tags:
  - knowledge
  - hermes-team
  - handoff
title: Alan → Turing
company: personal
from: alan
to: turing
input_shape: "technique_or_library {name, version_or_commit, source_urls[], claimed_behavior, reproducer_hint?, known_tradeoffs[]}"
output_shape: "evaluation {hypothesis, evidence_for[], evidence_against[], conclusion, reproducer (exact command + version)}"
failure_action: require_review
verification_gate: "source_urls is non-empty AND claimed_behavior is stated as a testable assertion, not a vibe"
created: 2026-04-20
---

# Alan → Turing

Alan passes a specific technique, library, or pattern for Turing to actually try. The point is reproducibility — Turing will run it, and the handoff must carry enough context to make that possible without another round-trip.

## Why "testable assertion" matters

"This library is faster" is not a testable assertion. "This library's `tokenize()` is faster than tiktoken on sequences >4k tokens on a single CPU core" is. Turing cannot evaluate the first. Refuse to accept it.

## Failure action

`require_review` — if `claimed_behavior` isn't testable or `source_urls` is empty, Turing returns it to Alan with a specific rewrite request. Not a silent retry.
