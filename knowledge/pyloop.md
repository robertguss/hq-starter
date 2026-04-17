---
tags:
  - knowledge
title: "PyLoop — Project Context"
company: personal
topics:
  - pyloop
  - python
  - ai
  - agents
source: ""
created: 2026-04-17
---

# PyLoop — Project Context

Distilled orientation for the distillery. Full spec ("Python Agent Harness — Brainstorming Spec," 2026-04-07) is the source of truth; this file is for loading project shape quickly when drafting content.

## The pitch

A **Python-specific coding agent harness** that replaces generic text-based agent workflows with **structure-aware, TDD-enforced, OSS-optimized** development. Generic agents treat Python like any other text file. PyLoop treats it as an AST — so syntax errors become impossible, types are ground truth, and cheap/local OSS models become viable for real work.

## The problem it solves

Generic agents (Claude Code, Cursor, Aider) generate text diffs that routinely break Python indentation, hallucinate syntax, mix doc versions, and forget TDD. 80% of loop iterations are spent re-asking the LLM to fix mistakes it didn't need to make. OSS models suffer the most — their instruction-following depth and syntax precision are weaker than frontier models, so they fail more often on the same loop. PyLoop moves those fixes out of the LLM and into deterministic checks.

## Who it's for

Python-heavy engineers who want an agent loop tuned to their language. First-class audience: Robert + indie/OSS-friendly devs who want to run cheap or local models (Llama, Qwen, DeepSeek) without getting killed by syntax errors and type hallucinations. Secondary: teams doing overnight RALPH loops on Python projects.

## Why this exists (market gap)

Two existing RALPH-style tools frame the space — neither is Python-native:

- **snarktank/ralph** — ~60-line bash script, clever prompt pattern, no self-healing, no AST.
- **michaelshimeles/ralphy** — robust TypeScript orchestrator (engine abstraction, retry/backoff, branch-per-task, smart merge), but still just spawns external tools; doesn't know what's _in_ the code.

**The white space PyLoop owns:** AST-native editing (libcst), enforced TDD, deterministic type-aware self-healing (ty), versioned documentation filesystem (DocFS), and a persistent memory layer. No existing harness combines these.

## Core experience (v1)

1. **RALPH loop** — plan → test-first → AST edit → deterministic checks → structured fix. Synchronous, iterative, modeled after Hermes `run_conversation()`.
2. **AST editing via libcst** — every edit is a concrete syntax tree transformation. 100% syntactically valid output. Imports, aliases, renames handled without missed references.
3. **TDD enforced** — harness physically blocks the LLM from writing implementation code until a test exists. The test is the contract.
4. **Deterministic self-healing** — ruff auto-fix, ty type check, pytest run. ~80% of iterations never touch the LLM.
5. **Structured error feedback** — when the LLM is needed, it gets parsed ty errors and pytest failures, not raw tracebacks.
6. **DocFS** — virtual read-only filesystem at `/docs/<package>-<version>/` for version-exact documentation via `ls`, `cat`, `grep`. Eliminates doc-version hallucination.
7. **Memory layer** — SQLite-backed temporal knowledge graph + AAAK-compressed session summaries. Indexes decisions, conventions, bug history, type patterns. MemPalace-inspired, coding-agent-adapted.
8. **AGENTS.md native** — harness reads and auto-maintains AGENTS.md files per directory (Linux Foundation open standard). `pyloop readiness` command scores and generates them.
9. **Dual-mode execution** — `pyloop tui` for interactive pairing (Hermes-clone Rich UI), `pyloop daemon` for detached overnight loops that survive SSH drops and API failures.

## Design principles

1. **Structure over text.** Every edit goes through the AST. Never raw text diffs.
2. **Tests before code.** TDD is enforced, not optional.
3. **Local-first.** No cloud dependencies required.
4. **OSS-friendly.** Works with cheap/fast/local models by moving intelligence into the harness, not the model.
5. **Self-healing.** Deterministic checks fix 80% of issues without LLM calls.
6. **Memory-aware.** Harness remembers decisions, patterns, and bugs across sessions.
7. **Docs as code.** DocFS exposes versioned docs through standard filesystem commands.
8. **AGENTS.md native.** Reads the open standard; auto-maintains context files.
9. **Dual-mode.** Interactive pairing and autonomous overnight work are equal first-class citizens.

## Stack (brief)

Python 3.12+. **uv** (env + deps), **ty** (type check, Astral), **ruff** (lint + format), **libcst** (AST manipulation), **pytest** (test execution), **SQLite + FTS5** (memory + DocFS index). Rich for TUI. Engine abstraction with OpenRouter/Anthropic/OpenAI/local adapters, exponential backoff + jitter, deferred task retry. No ChromaDB (SQLite FTS5 covers 90% of search).

## Status

Brainstorming spec complete (2026-04-07). Pre-build. V1 scope is buildable overnight. See [[../initiatives/pyloop|Build PyLoop — Custom Python Agent Harness]].

## Writing about this project

**Technical lane** — libcst AST surgery, RALPH loop design, TDD enforcement as an architectural constraint, deterministic self-healing as a replacement for LLM retries, OSS model optimization, temporal knowledge graphs for coding agents, DocFS and version-exact docs, daemon-mode overnight loops, AGENTS.md adoption: technical voice. This is **the** strongest technical-writing vein Robert has right now — a brand-new harness space, underexplored AST-native approaches, direct comparison content (vs Claude Code, Cursor, Aider, Ralph, Ralphy), and a natural fit for long-form deep-dives.

**Business / indie-dev lane** — the economics of OSS-model-first tooling, why most agent harnesses are language-agnostic and why that's a mistake, building tools you use yourself, the case for Python-native over general-purpose agents: indie-business voice.

**Do not mix theology into PyLoop posts.** This is a developer tool; the faith angle is not in the product. Intersection essays about the philosophy of tool-making, human-AI collaboration, or what it means to build for yourself belong in the long-form intersection category — not on PyLoop launch posts or technical tutorials.

Natural content cadence for PyLoop: build-in-public technical posts (design decisions, AST edit patterns, TDD-enforcement internals), comparison posts (PyLoop vs Ralph vs Ralphy, PyLoop vs Claude Code on Python), and overnight-RALPH-loop reports showing real results.
