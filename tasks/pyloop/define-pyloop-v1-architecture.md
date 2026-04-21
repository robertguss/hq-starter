---
tags:
  - task
title: "Define PyLoop v1 architecture"
status: todo
priority: 1
company: personal
initiative: "[[initiatives/pyloop]]"
due:
created: 2026-04-20
completed:
---

## Context

PyLoop needs a concrete v1 architecture before implementation fragments start drifting. Convert the current concept into an implementation-ready structure covering package boundaries, loop phases, engine abstraction, AST editing boundaries, checks pipeline, and TUI/daemon split.

## Done When

- the v1 package/module layout is documented
- core runtime flow from prompt -> test -> edit -> checks -> retry is defined
- responsibilities for engine adapters, AST editing, checks, memory, and docs are separated clearly
- open questions and deferred v2 items are called out explicitly
