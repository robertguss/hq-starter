---
tags:
  - task
title: "Prototype libcst edit engine"
status: todo
priority: 1
company: personal
initiative: "[[initiatives/pyloop]]"
due:
created: 2026-04-20
completed:
---

## Context

PyLoop's main technical wedge is AST-native editing. Build a first prototype proving that Python code edits can be applied through `libcst` transformations rather than raw text diffs, including safe import handling and syntactically valid output.

## Done When

- a minimal end-to-end AST edit prototype exists
- at least one representative code change is applied through `libcst`
- syntactic validity is preserved automatically
- limitations, edge cases, and next implementation steps are documented
