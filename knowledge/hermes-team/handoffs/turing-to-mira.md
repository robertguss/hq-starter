---
tags:
  - knowledge
  - hermes-team
  - handoff
title: Turing → Mira
company: personal
from: turing
to: mira
input_shape: "one_paragraph_summary {what_changed, why_it_changed, user_visible_effect, gotchas[]?}"
output_shape: "drafted piece + change log (see mira-to-hermes)"
failure_action: require_review
verification_gate: "summary is one paragraph (≤120 words) AND user_visible_effect is stated plainly, no jargon-performance"
created: 2026-04-20
---

# Turing → Mira

Narrow by design. Mira writes about Turing's work only when Robert has decided a piece is warranted. Turing does NOT write tutorials or narrative explanations — that's Mira's scope.

## Scope rule

If Mira needs more context, she asks for specifics ("what version of X, what command reproduces"). Turing answers the specific question. He does not expand the paragraph into a tutorial.

## Failure action

`require_review` — if the summary bloats past ~120 words or drifts into tutorial voice, Mira returns it with a single specific question.
