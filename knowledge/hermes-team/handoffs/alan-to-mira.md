---
tags:
  - knowledge
  - hermes-team
  - handoff
title: Alan → Mira
company: personal
from: alan
to: mira
input_shape: "ranked_claims[] where each item = {claim (one sentence), confidence (verified|probable|speculative), source_urls[] (non-empty), relevance_note (one line)}"
output_shape: "drafted piece + change log (see mira-to-hermes)"
failure_action: block
verification_gate: "every claim has at least one source_url AND a confidence tag in {verified, probable, speculative}"
created: 2026-04-20
---

# Alan → Mira

The canonical siloing handoff. Alan supplies evidence. Mira turns it into communication. If Alan sends raw transcripts or draft prose, Mira becomes a researcher again and the team collapses back to a single generalist.

## What Mira will NOT do on this input

- Re-validate the claims. Mira trusts Alan's confidence tags.
- Promote a `speculative` claim to asserted fact in the draft.
- Add claims not in Alan's list.

## What Mira DOES do

- Select which claims survive the piece's thesis.
- Apply Robert's voice per `author-profile.md`.
- Enforce the siloing rule — technical pieces stay technical.

## Failure action

`block` — if any claim lacks a source_url or confidence tag, return the entire handoff to Alan with the specific claim flagged. Do not partially accept.
