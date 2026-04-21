---
tags:
  - initiative
title: "Build PyLoop — Custom Python Agent Harness"
company: personal
status: active
owner: Robert Guss
started: 2026-04-17
target_date:
---

## Goal

Research and continue building PyLoop, a custom Python agent harness.

## Context

PyLoop is a Python-native coding agent harness built to outperform generic text-diff workflows on Python-heavy projects. It treats Python as structure, not raw text: AST-native editing via `libcst`, TDD enforcement, deterministic self-healing via `ruff` / `ty` / `pytest`, version-exact docs through DocFS, and a persistent memory layer. The target user is the Python-heavy engineer who wants reliable agent loops with cheap or local OSS models, not just frontier-model demos.

The strategic wedge is clear: existing RALPH-style tools are either minimal bash wrappers or general-purpose orchestrators. PyLoop is differentiated by combining AST editing, enforced tests-before-code, deterministic repair loops, AGENTS.md-native context handling, and dual interactive/daemon execution in one Python-specific harness.

## Key Results

- [ ] PyLoop v1 scope is defined as a buildable implementation plan covering the RALPH loop, AST editing, TDD enforcement, deterministic checks, DocFS, and memory
- [ ] A prioritized execution backlog exists with concrete tasks for the first build phase
- [ ] One substantive public artifact ships that explains PyLoop's differentiation clearly (for example: a technical brief, comparison post, or design deep-dive)
