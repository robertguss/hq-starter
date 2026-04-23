---
tags:
  - index
title: Dev Tools & CLI
aliases:
  - Dev Tools & CLI
collection: dev-tools-cli
---

# Dev Tools & CLI

> [!abstract] Collection overview
> A terminal-first toolkit with a clear bias: small, composable binaries, Rust/Go performance, and deep integration with git and AI agents. The shelf covers modernized Unix replacements, next-gen Python (marimo, pyrefly), git-native API clients (Bruno), single-file backends (PocketBase), and LLM-agent scaffolding. Philosophy: serious craft tooling, not toy commands — every item here repays attention with power.

## Key themes

- **Terminal & TUI frameworks** — High-performance TUIs and modernized Unix: [[ratatui]], [[charm]], [[eza]]. ^theme-terminal-ui
- **Editor & language tooling** — Fast analyzers and editor integrations: [[dmtrkovalenkofffnvim-the-fastest-and-the-most-accurate-file]], [[pyrefly-a-fast-python-type-checker-and-language-server-pyref]], [[jendrikseippvulture-find-dead-python-code]]. ^theme-editor-lang
- **Git-native API & workflow** — API clients that live in version control: [[bruno-the-git-native-api-client]]. ^theme-api-git
- **CLI frameworks & scaffolding** — Fast, memory-safe CLI generation and templates: [[nashsuautocli-autocli-is-a-blazing-fast-memory-safe-command]], [[cobradev]], [[base]], [[copier]]. ^theme-cli-frameworks
- **Python ecosystem & reactive notebooks** — Modern Python computing: [[marimo-a-next-generation-python-notebook]], [[how-to-set-up-a-perfect-python-project]]. ^theme-python-ecosystem
- **Self-hostable backends & deploy** — Minimal, single-binary platforms: [[pocketbase-open-source-backend-in-1-file]], [[shuttle-build-backends-fast]], [[coolify]]. ^theme-backends-deploy
- **Type-safe codegen** — SQL-to-code and bundler tooling: [[sqlcdev]], [[announcing-rolldown-vite]]. ^theme-codegen
- **AI-first dev tooling** — LLM-aware CLIs and agent scaffolding: [[introducing-vt-the-val-town-cli]], [[one-cookiecutter-to-build-agents-in-seconds]], [[openagents-orgopenagents-openagents-ai-agent-networks-for-op]], [[lazypi-the-fastest-way-to-fall-in-love-with-pi]] (Pi coding-agent setup). ^theme-ai-first
- **Agent-native terminals** — Terminals redesigned from the ground up for agent coordination rather than retrofitted: [[tw93kaku-a-fast-out-of-the-box-terminal-built-for-ai-coding]] (Kaku — fast, out-of-the-box, purpose-built for AI coding; sibling trajectory to Warp in the ai-tools-news shelf). ^theme-agent-terminals
- **Observability & security** — Monitoring and binary analysis: [[better-stack-radically-better-observability-stack]], [[nationalsecurityagencyghidra-ghidra-is-a-software-reverse-en]]. ^theme-observability

## Notable items

- [[bruno-the-git-native-api-client]] — Git-native API testing; collections as plain text alongside code.
- [[ratatui]] — Rust TUI framework powering csvlens, oxker, and other production apps.
- [[pocketbase-open-source-backend-in-1-file]] — Realtime DB, auth, files, and admin in a single Go binary.
- [[marimo-a-next-generation-python-notebook]] — Reactive, git-friendly notebook replacing Jupyter.
- [[shuttle-build-backends-fast]] — Deploy Rust services with one annotation; zero-touch AWS provisioning.
- [[sqlcdev]] — Compile SQL to type-safe code; catch schema drift before runtime.
- [[eza]] — Rust `ls` replacement with git awareness and color.
- [[pyrefly-a-fast-python-type-checker-and-language-server-pyref]] — Fast Python type checker and LSP.
- [[introducing-vt-the-val-town-cli]] — Val Town CLI with AGENTS.md context for Claude Code / Cursor.
- [[better-stack-radically-better-observability-stack]] — AI-SRE-flavored observability stack, Datadog alternative.
- [[announcing-rolldown-vite]] — Rust-native Rollup replacement powering Vite's next generation.
- [[tw93kaku-a-fast-out-of-the-box-terminal-built-for-ai-coding]] — Kaku: fast, agent-native terminal; closest peer to Warp in this shelf.

## 2026-04-23 addition

**2026-04-23 addition (+2 repos):** [[fallow-rsfallow-find-unused-code-code-duplication-circular-d]] — Rust CLI that finds unused code, code duplication, circular dependencies, and complexity hotspots in TypeScript/JavaScript projects (900+ stars). Sibling to the Python [[jendrikseippvulture-find-dead-python-code]] already on this shelf, extending the dead-code-finder theme to TS/JS. [[bpinheiromsmy-setup]] — a single-dev setup repo (dotfiles + machine-specific configuration following AGENTS.md/skill-creator conventions). Notable because it treats developer setup itself as agent-readable context — an instance of the broader pattern of turning personal workflows into agent-consumable artifacts.

## Cross-references

- Overlaps with `ai-tools-news/` and `ai-repos-open-source/` on agent frameworks and LLM dev tooling, and with `web-dev/` on build/bundler tooling.
