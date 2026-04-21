---
tags:
  - task
title: "Build deterministic check pipeline"
status: todo
priority: 1
company: personal
initiative: "[[initiatives/pyloop]]"
due:
created: 2026-04-20
completed:
---

## Context

PyLoop's efficiency depends on deterministic repair before involving the LLM again. Wire the first check pipeline around `ruff`, `ty`, and `pytest`, with structured outputs that can drive automatic fixes or focused retry prompts.

## Done When

- `ruff`, `ty`, and `pytest` are part of a single ordered check pipeline
- outputs are normalized into structured feedback
- automatic fixes are attempted where safe
- the handoff from deterministic failure to LLM retry is clearly defined
