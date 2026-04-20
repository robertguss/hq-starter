---
tags:
  - knowledge
  - hermes-team
  - handoff
title: Turing → Hermes
company: personal
from: turing
to: hermes
input_shape: "deliverable {branch_name (feature branch, or 'working-tree' for vault/tooling edits with no branch workflow), diff_summary (files[], approx_lines), test_command, test_result (passed|failed), root_cause (one sentence, bugs only), follow_ups[]?}"
output_shape: "decision {approve_merge | reject_with_reason | request_changes[]}"
failure_action: block
verification_gate: "test_result == 'passed' AND branch_name != 'main' (use 'working-tree' when the target has no feature-branch workflow, e.g. Obsidian vault, tooling scripts)"
created: 2026-04-20
---

# Turing → Hermes

The approval gate. Turing never merges to main. Hermes is the only profile that can approve the merge.

## What Hermes checks

- Does the diff match the scope of the original dispatch? (Refactor creep lives here.)
- Are the tests exercising the actual failure mode, not just passing?
- Is the root cause sentence specific enough to prevent recurrence?

## What Hermes does NOT check

- Code style nitpicks. Turing owns the diff's shape.
- Whether a different approach would have been better. That conversation happens before dispatch, not at the merge gate.

## Branch vs working-tree

Product repos: always a feature branch. Main is Hermes-only.

Vault / tooling scripts / docs: no branch workflow exists. Use `branch_name: working-tree` to declare that explicitly. Hermes still reviews the diff; the branch field just documents where the work lives.

Rule: never report `branch_name: main` on a product repo. If you're on main in a product repo, stop and branch first.

## Failure action

`block` — if tests aren't passing, or `branch_name` is literally `main`, reject without reading the diff. Non-negotiable.
