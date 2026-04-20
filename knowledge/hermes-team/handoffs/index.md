---
tags:
  - index
  - hermes-team
  - handoff
title: Handoff Contracts
company: personal
topics:
  - hermes
  - multi-agent
  - handoffs
created: 2026-04-20
---

# Handoff Contracts

One file per directed profile pair. Each contract declares the shape of inputs the receiving profile expects, the shape of outputs it returns, the failure action when inputs are malformed, and a single verification gate that must hold before the handoff completes.

Schema lives in YAML frontmatter so a future harness hook can parse and enforce. Body is human-readable context only.

## Rule

Source of truth lives here in the vault. Copy to `~/.hermes/team/handoffs/` for the harness to consume (see [[setup]] step 5a).

Every contract edit is a commit. No contract change without a logged reason.

## Contracts

- [[hermes-to-specialist]] — Hermes → Alan / Mira / Turing (downward dispatch)
- [[alan-to-mira]] — research → writing
- [[alan-to-turing]] — research → engineering
- [[alan-to-hermes]] — research escalation (unresolved uncertainty)
- [[turing-to-hermes]] — engineering deliverable for approval
- [[turing-to-mira]] — engineering context for a writing piece
- [[mira-to-hermes]] — drafted piece for final QA

## Field definitions

- `from` / `to` — profile aliases. Always lowercase.
- `input_shape` — what the receiving profile expects on input. Describe fields, not prose.
- `output_shape` — what the receiving profile returns. Describe fields, not prose.
- `failure_action` — one of `block`, `require_review`, `retry_with_prompt`. Applies when the input shape fails to match.
- `verification_gate` — a single assertion that must be true before the handoff is considered complete. If it cannot be stated in one line, the gate is too broad.

## Enforcement status

Contracts are currently **documentary, not blocking**. The harness does not yet read these files. Until it does, enforcement happens at Hermes-the-orchestrator's review step: when a handoff arrives that violates a contract, Hermes rejects and returns the mismatch to the sender.

Blocking enforcement is a follow-up task — not part of this pass.
