---
tags:
  - task
title: "Implement TDD gate and loop state machine"
status: todo
priority: 1
company: personal
initiative: "[[initiatives/pyloop]]"
due:
created: 2026-04-20
completed:
---

## Context

PyLoop is supposed to enforce tests-before-code rather than merely recommend it. Define and implement the loop states and guardrails that prevent implementation work from proceeding until a test exists and that keep retries structured.

## Done When

- loop states are explicitly defined
- the harness can distinguish test-writing from implementation-writing phases
- implementation is blocked when no test contract exists
- failure/retry transitions are specified clearly enough to code next
