---
tags:
  - library
title: "The Agentic Coding Flywheel - TL;DR"
url: "https://agent-flywheel.com/tldr"
company: [personal]
topics: []
created: 2026-01-25
source_type: raindrop
raindrop_id: 1560401441
source_domain: "agent-flywheel.com"
source_type_raindrop: link
collection: "AI Tools & News"
collection_id: 69284314
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

13 open-source tools that work together to supercharge multi-agent AI coding workflows.

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: The Agentic Coding Flywheel - TL;DR | Agent Flywheel

URL Source: https://agent-flywheel.com/tldr

Markdown Content:
Open Source Ecosystem

## The Agentic Coding Flywheel TL;DR Edition

16 core tools and 13 supporting utilities that transform multi-agent AI coding workflows. Each tool makes the others more powerful - the more you use it, the faster it spins. While others argue about agentic coding, we're just over here building as fast as we can.

29

Ecosystem Tools

3,600+

GitHub Stars

5

Languages

Scroll to explore

## Why a Flywheel?

A flywheel stores rotational energy - the more you spin it, the easier each push becomes. These tools work the same way. The more you use them, the more valuable the system becomes.

Every agent session generates searchable history (CASS). Past solutions become retrievable memory (CM). Dependencies surface bottlenecks (BV). Agents coordinate without conflicts (Mail). Each piece feeds the others.

The result: I shipped 20,000+ lines of production Go code in a single day with BV. The flywheel keeps spinning faster - my GitHub commits accelerate each week because each tool amplifies the others.

Hover over tools to see connections

/

## Core Flywheel Tools

16

The backbone of multi-agent development: session management, communication, task tracking, static analysis, memory, search, safety guards, multi-repo sync, and automated setup. These tools form a self-reinforcing loop where each makes the others more powerful.

### Mail

Core

MCP Agent Mail

1.4K

[](https://github.com/Dicklesworthstone/mcp_agent_mail_rust)

A mail-like coordination layer for multi-agent workflows. Agents send messages, read threads, and reserve files asynchronously via MCP tools - like Gmail for AI coding agents. HTTP-only FastMCP transport with static export.

#### Why It's Useful

Critical for multi-agent setups. When 5+ Claude Code instances work the same codebase, they need to coordinate who's editing what. Agent Mail prevents merge conflicts via advisory file reservations with pre-commit guard enforcement, and builds an audit trail of all agent decisions via SQLite + Git dual persistence.

#### Key Features

*   Threaded messaging between AI agents
*   Advisory file reservations
*   SQLite-backed persistent storage
*   MCP integration for any compatible agent

#### Tech Stack

Rust SQLite

#### Synergies

BV Task IDs in mail threads link to Beads issues

CM Shared context persists across agent sessions via CM

SLB Two-person approval requests delivered via agent inboxes

NTM NTM-spawned agents auto-register with Agent Mail

### BV

Core

Beads Viewer

891

[](https://github.com/Dicklesworthstone/beads_viewer)

A fast terminal UI for viewing and analyzing Beads issues. Applies graph theory (PageRank, betweenness centrality, critical path) to identify which tasks unblock the most other work.

#### Why It's Useful

Issue tracking is really a dependency graph. BV lets Claude prioritize beads intelligently by computing actual bottlenecks. The --robot-insights flag gives PageRank rankings for what to tackle first.

#### Key Features

*   PageRank-based issue prioritization
*   Critical path analysis
*   Robot mode for AI agent integration
*   Interactive TUI with vim keybindings

#### Tech Stack

Go Bubble Tea Lip Gloss Graph algorithms

#### Synergies

BR Reads and visualizes issues from beads_rust (.beads/*.jsonl)

Mail Task updates trigger notifications via Agent Mail

UBS Bug scanner findings become blocking issues

CASS Search prior sessions for task context

NTM NTM uses --robot-plan for dependency analysis during multi-agent orchestration

### BR

Core

beads_rust

128

[](https://github.com/Dicklesworthstone/beads_rust)

Local-first issue tracking for AI agents. SQLite for fast local queries, JSONL export for git-friendly collaboration. Full dependency graph with blocking/blocked-by relationships, priorities P0-P4.

#### Why It's Useful

Your issues travel with your repo - no external service required. Non-invasive design: never runs git commands automatically. Agents can create, update, and close issues with simple CLI commands. The bd alias provides backward compatibility.

#### Key Features

*   Local-first issue storage
*   Dependency graph tracking
*   Labels, priorities, comments
*   JSON output for agents

#### Tech Stack

Rust Serde JSONL

#### Synergies

BV BV visualizes and analyzes issues created by br

Mail Task updates notify agents via mail

NTM NTM spawns agents that pick work from beads

UBS UBS --beads-jsonl outputs findings as importable beads

### CASS

Core

Coding Agent Session Search

307

[](https://github.com/Dicklesworthstone/coding_agent_session_search)

Blazing-fast search across all your past AI coding agent sessions. Indexes 11 agent formats: Claude Code, Codex, Cursor, Gemini, ChatGPT, Cline, Aider, Pi-Agent, Factory, OpenCode, Amp. Sub-60ms queries with optional semantic search.

#### Why It's Useful

You've solved this problem before - but which session? CASS lets you search 'how did I fix that React hydration error' and instantly find the exact conversation. Three search modes (lexical, semantic, hybrid), HTML export with encryption, and multi-machine sync via SSH.

#### Key Features

*   Unified search across all agent types
*   Sub-second search over millions of messages
*   Robot mode for AI agent integration
*   TUI for interactive exploration

#### Tech Stack

Rust Tantivy Ratatui JSONL parsing

#### Synergies

CM Indexes memories stored by CM for retrieval

NTM Searches all managed agent session histories

BV Links search results to related Beads tasks

### ACFS

Core

Flywheel Setup

234

[](https://github.com/Dicklesworthstone/agentic_coding_flywheel_setup)

One-command bootstrap that transforms a fresh Ubuntu VPS into a fully-configured agentic coding environment. CLI provides doctor (47+ health checks), update (category-specific), cheatsheet (50+ aliases), and session management.

#### Why It's Useful

Setting up a new development environment takes hours. ACFS does it in 30 minutes, installing 30+ tools, three AI agents, and all flywheel tooling. Post-install CLI provides `acfs doctor` for health checks and `acfs update` for maintenance.

#### Key Features

*   acfs doctor: 47+ health checks across 7 categories
*   acfs doctor --deep: Functional tests (auth, DB connectivity)
*   acfs update: Category-specific with --dry-run preview
*   acfs cheatsheet: 50+ aliases for modern CLI tools
*   acfs dashboard: Static HTML dashboard generation
*   Update logging to ~/.acfs/logs/updates/

#### Tech Stack

Bash YAML manifest Next.js wizard

#### Synergies

NTM Installs and configures NTM

Mail Sets up Agent Mail MCP server

DCG Installs DCG safety hooks

### UBS

Core

Ultimate Bug Scanner

132

[](https://github.com/Dicklesworthstone/ultimate_bug_scanner)

A meta-runner that fans out per-language scanners across 8 languages (JS/TS, Python, Go, Rust, C/C++, Java, Ruby, Swift). Uses ast-grep for AST-based pattern matching with 18 detection categories and 1000+ bug patterns.

#### Why It's Useful

AI coding agents move 10-100x faster than humans. UBS keeps pace with sub-5-second scans and auto-wires guardrails into Claude Code, Codex, Cursor, Gemini, and Windsurf agents. The --beads-jsonl output creates Beads issues directly from findings.

#### Key Features

*   1000+ built-in detection patterns
*   Consistent JSON output format
*   Multi-language support
*   Perfect for pre-commit hooks

#### Tech Stack

Bash Pattern matching JSON output

#### Synergies

BV Bug findings become blocking issues via --beads-jsonl

BR Direct JSONL output for beads_rust issue tracking

### DCG

Core

Destructive Command Guard

89

[](https://github.com/Dicklesworthstone/destructive_command_guard)

Claude Code PreToolUse hook that blocks dangerous commands BEFORE execution. 50+ packs across 17 categories: git (reset --hard, force push), filesystem (rm -rf), databases (DROP TABLE), Kubernetes, cloud providers, and more.

#### Why It's Useful

AI agents can and will run 'rm -rf /' if they think it solves your problem. DCG catches catastrophic commands before they execute with sub-millisecond latency. Safe directory exceptions (/tmp, /var/tmp, $TMPDIR) allow temp operations without friction.

#### Key Features

*   Intercepts rm -rf, git reset --hard, etc.
*   SIMD-accelerated pattern matching
*   Configurable allowlists
*   Command audit logging

#### Tech Stack

Rust SIMD Shell integration

#### Synergies

SLB Works alongside SLB for layered command safety

NTM Guards all commands in NTM-managed sessions

### RU

Core

Repo Updater

67

[](https://github.com/Dicklesworthstone/repo_updater)

Multi-repo management system: sync 100+ repos, AI-assisted code review with priority scoring, dependency updates across package managers, and agent-driven commit automation.

#### Why It's Useful

Managing 100+ repos manually is impossible. 'ru sync' handles clone/pull in parallel. 'ru review' discovers issues/PRs via GraphQL batch queries, scores by priority (security+50, bugs+30, age), and spawns isolated Claude Code sessions in worktrees.

#### Key Features

*   One-command multi-repo sync
*   Parallel operations
*   Conflict detection with resolution hints
*   AI code review integration

#### Tech Stack

Bash Git plumbing GitHub CLI

#### Synergies

NTM Uses ntm robot mode API for AI review session management

Mail Coordinates repo claims across parallel agents

BV Multi-repo task tracking via beads integration

### CM

Core

CASS Memory System

152

[](https://github.com/Dicklesworthstone/cass_memory_system)

Cross-agent procedural memory system. Transforms scattered sessions from all your AI agents into persistent, unified knowledge. Three-layer cognitive architecture: Episodic (raw sessions via CASS) → Working (diary summaries) → Procedural (playbook rules with confidence tracking).

#### Why It's Useful

A debugging technique discovered in Cursor is immediately available to Claude Code. Rules have 90-day decay half-life and 4× harmful weight for mistakes. Bad rules auto-invert into anti-pattern warnings. Every agent learns from every other agent's experience.

#### Key Features

*   Three memory layers: episodic, working, procedural
*   MCP integration for any compatible agent
*   Automatic memory consolidation
*   Cross-session context persistence

#### Tech Stack

TypeScript Bun MCP Protocol SQLite

#### Synergies

CASS Primary dependency - provides episodic memory via session search

Mail Memory context shared across agent conversations

BV Task patterns and successful approaches remembered

### NTM

Core

Named Tmux Manager

69

[](https://github.com/Dicklesworthstone/ntm)

A multi-agent tmux orchestration tool with 80+ commands. Spawns Claude, Codex, and Gemini agents in named panes with type classification (cc/cod/gmi). Monitors context windows, detects file conflicts, and provides robot mode for automation.

#### Why It's Useful

Running multiple AI agents simultaneously creates chaos without orchestration. NTM provides the command center: spawn agents with one command, broadcast prompts to specific types, monitor context usage, and coordinate via Agent Mail. Sessions persist across SSH disconnects and system reboots.

#### Key Features

*   Named agent panes with type classification
*   Broadcast prompts to agent types
*   Session persistence across reboots
*   Dashboard view of active agents

#### Tech Stack

Go Bubble Tea tmux

#### Synergies

SLB SLB provides two-person rule safety checks for dangerous commands in NTM sessions

Mail Agents auto-register with Mail; ntm mail commands for messaging; pre-commit guard enforces file reservations

CASS Direct integration via --robot-cass-search and --robot-cass-context commands

BV Graph analysis via --robot-plan and --robot-graph for dependency insights

BR Bead management via --robot-bead-* commands for issue tracking

### SLB

Core

Simultaneous Launch Button

49

[](https://github.com/Dicklesworthstone/simultaneous_launch_button)

Nuclear-launch-style two-person rule for dangerous commands. Four risk tiers classify commands via 40+ regex patterns: CRITICAL (2+ approvals), DANGEROUS (1 approval), CAUTION (30s auto-approve), SAFE (skip). Cryptographic signing, rollback support, and outcome analytics.

#### Why It's Useful

AI agents can and will run destructive commands if they think it solves your problem. SLB intercepts commands like 'rm -rf /', 'DROP DATABASE', and 'terraform destroy' requiring explicit approval from another agent or human reviewer before execution. Watch mode lets reviewing agents stream pending requests.

#### Key Features

*   Two-person rule enforcement
*   Command queue with approval workflow
*   Pattern-based risk detection
*   SQLite persistence

#### Tech Stack

Go Bubble Tea SQLite

#### Synergies

DCG DCG blocks pre-execution, SLB validates with multi-agent approval

NTM Coordinates approval quorum across NTM-managed agents

Mail Approval requests can be routed via Agent Mail

CAAM Account switching can require SLB approval for team workflows

### MS

Core

Meta Skill

10

[](https://github.com/Dicklesworthstone/meta_skill)

Local-first skill management platform: dual persistence (SQLite + Git), hybrid search (BM25 + semantic + RRF), UCB bandit optimization, multi-layer security (ACIP + DCG), graph analysis via bv, MCP server for AI agents.

#### Why It's Useful

AI agents need reusable context to be effective. MS doesn't just store skills—it learns which ones work via UCB bandit optimization. Context-aware auto-loading suggests skills based on project type. Pack contracts optimize token budgets. The MCP server makes skills native tools for any AI agent.

#### Key Features

*   MCP server for native AI agent integration
*   Thompson sampling optimizes suggestions
*   Multi-layer security
*   Hybrid search with RRF

#### Tech Stack

Rust SQLite Tantivy MCP

#### Synergies

CASS One input source for skill extraction (not the only one)

CM Skills and CM memories are complementary knowledge layers

BV Graph analysis via bv for PageRank, bottlenecks, cycles

JFP JFP downloads remote prompts, MS manages local skills

### RCH

Core

Remote Compilation Helper

35

[](https://github.com/Dicklesworthstone/remote_compilation_helper)

Claude Code PreToolUse hook that offloads Rust compilation to remote workers. Intercepts cargo commands, syncs source via rsync + zstd, compiles on server-grade hardware, streams artifacts back.

#### Why It's Useful

Multi-agent swarms trigger many concurrent builds. RCH intercepts commands before execution and routes them to remote workers with health probes and priority scheduling. Agent detection coordinates builds across Claude Code, Codex, and Gemini sessions.

#### Key Features

*   Transparent cargo interception
*   Multi-worker pool with priority scheduling
*   Incremental artifact sync
*   Daemon mode with status monitoring

#### Tech Stack

Rust rsync zstd SSH

#### Synergies

NTM Agents in NTM sessions use RCH for builds

RU RU syncs repos that RCH then builds remotely

BV Build tasks can be tracked via beads

### CAAM

Core

Coding Agent Account Manager

45

[](https://github.com/Dicklesworthstone/coding_agent_account_manager)

Manages multiple accounts for Claude Code, Codex CLI, and Gemini CLI with sub-100ms switching. Vault profiles store auth files for instant activation without browser flows. Smart rotation algorithms automatically select the best profile based on cooldown state, health, and usage patterns.

#### Why It's Useful

When running multiple agents, you'll hit rate limits. CAAM lets you switch accounts instantly - no browser login, no waiting. Profile isolation enables parallel sessions where each agent uses its own credentials. Health scoring (🟢/🟡/🔴) shows which profiles are ready vs. cooling down.

#### Key Features

*   Sub-100ms account switching
*   Multi-provider support
*   Automatic key rotation
*   Session state preservation

#### Tech Stack

TypeScript Bun Keychain

#### Synergies

NTM NTM spawns agents with isolated CAAM profiles for parallel sessions

Mail Account switches can trigger Agent Mail notifications

SLB Team approval workflows for account switching

### WA

Core

WezTerm Automata

42

[](https://github.com/Dicklesworthstone/wezterm_automata)

Terminal hypervisor that captures pane output in real-time, detects agent state transitions through pattern matching, and enables event-driven automation across multiple AI coding agents.

#### Why It's Useful

When running multiple AI agents in WezTerm, you need to know when they hit rate limits, complete tasks, or need approval. WA observes all panes with sub-50ms latency and triggers automated responses.

#### Key Features

*   Real-time terminal observation
*   Intelligent pattern detection
*   Robot Mode JSON API
*   Event-driven automation

#### Tech Stack

Rust WezTerm API SQLite FTS5

#### Synergies

NTM WA observes agents spawned by NTM

Mail State changes trigger Agent Mail notifications

BV Task completions can update bead status

### Brenner

Core

Brenner Bot

28

[](https://github.com/Dicklesworthstone/brenner_bot)

Multi-agent scientific research orchestration platform based on Sydney Brenner's methodology. Manages full research artifact lifecycle: hypotheses, discriminative tests, anomalies, critiques, and evidence packs with cockpit runtime for parallel agent sessions.

#### Why It's Useful

Transforms AI agents into a collaborative research group with rigorous scientific discipline. The Brenner approach emphasizes exclusion over accumulation, third-alternative thinking, and discriminative experiments that collapse hypothesis space fast.

#### Key Features

*   Primary source corpus with citations
*   Multi-agent research sessions
*   Discriminative test ranking
*   Adversarial critique generation

#### Tech Stack

TypeScript Bun Agent Mail Multi-model AI

#### Synergies

Mail Research sessions coordinate via Agent Mail threads with acknowledgment tracking

NTM Cockpit runtime spawns parallel research agents with role-specific prompts

CASS Research session history searchable for prior solutions and patterns

## Supporting Tools

13

Extend the ecosystem with GitHub issue sync, archive search, and prompt crafting utilities. These tools enhance the core flywheel for specialized workflows.

### GIIL

Get Image from Internet Link

24

[](https://github.com/Dicklesworthstone/giil)

Downloads full-resolution images from iCloud, Dropbox, Google Photos, and Google Drive share links using a four-tier capture strategy with headless Chromium automation.

#### Why It's Useful

When debugging remotely, users share cloud links but you're SSH'd into a headless server. GIIL's four-tier capture (download button → CDN interception → element screenshot → viewport fallback) ensures maximum quality retrieval for AI agent analysis.

#### Key Features

*   iCloud share link support
*   CLI-based image download
*   No browser required
*   Works over SSH

#### Tech Stack

Bash curl iCloud API

#### Synergies

Mail Downloaded images can be referenced in Agent Mail

CASS Image analysis sessions are searchable

### SRPS

System Resource Protection Script

50

[](https://github.com/Dicklesworthstone/system_resource_protection_script)

Installs ananicy-cpp with curated rules to auto-deprioritize background processes. Includes sysmoni Go TUI (Bubble Tea) with IO throughput, FD counts, per-core sparklines, JSON export. Works on Linux and WSL2.

#### Why It's Useful

When running cargo build, npm install, or multiple AI agents, SRPS prevents unresponsive systems by lowering priority of known resource hogs. Safety-first: no automated process killing. Helper tools for diagnostics.

#### Key Features

*   Automatic process deprioritization
*   Real-time TUI monitoring
*   1700+ pre-configured rules
*   Custom rule creation

#### Tech Stack

Go C++ananicy-cpp systemd

#### Synergies

NTM Keeps tmux sessions responsive during heavy workloads

SLB Prevents multiple agents from starving each other for resources

DCG Combined safety: resource protection + command protection

PT PT identifies stuck processes, SRPS deprioritizes resource hogs

### XF

X Archive Search

156

[](https://github.com/Dicklesworthstone/xf)

Ultra-fast search over X/Twitter data archives with sub-millisecond latency. Uses hybrid BM25 + semantic search with Reciprocal Rank Fusion. Indexes tweets, likes, DMs, and Grok conversations.

#### Why It's Useful

Your X archive is a goldmine of bookmarks, threads, and ideas, but Twitter's search is terrible. XF makes your archive instantly searchable (<10ms) with both keyword and semantic matching. DM context search shows full conversation threads.

#### Key Features

*   Sub-second search over large archives
*   Semantic + keyword hybrid search
*   No external API dependencies
*   Privacy-preserving local processing

#### Tech Stack

Rust Tantivy Hash embeddings RRF

#### Synergies

CASS Similar search architecture and patterns

CM Found tweets can become memories

### S2P

Source to Prompt TUI

156

[](https://github.com/Dicklesworthstone/source_to_prompt_tui)

World-class terminal UI for combining source code files into LLM-ready prompts. Tree explorer with vim-style navigation, live syntax preview, token counting, and structured XML-like output optimized for AI parsing.

#### Why It's Useful

Crafting prompts with code context is tedious and error-prone. S2P provides visual file selection with sizes and line counts, real-time token/cost estimation, quick file-type shortcuts (1-9,0,r), and produces structured output that LLMs parse reliably.

#### Key Features

*   Interactive file selection
*   Real-time token counting
*   Clipboard integration
*   Gitignore-aware filtering

#### Tech Stack

TypeScript Bun React Ink tiktoken

#### Synergies

CASS Generated prompts become searchable session history

CM Effective prompt patterns stored as procedural memories

### APR

Automated Plan Reviser Pro

85

[](https://github.com/Dicklesworthstone/automated_plan_reviser_pro)

Iterative specification refinement via GPT Pro 5.2 Extended Reasoning + Oracle. Document bundling (README + spec + impl), convergence analytics with weighted scoring, session management, and robot mode JSON API for coding agents.

#### Why It's Useful

Complex specs need 15-20 review cycles. APR automates the loop: rounds 1-3 fix architecture, 4-7 refine interfaces, 8-12 handle edge cases, 13+ polish abstractions. Convergence score (≥0.75 = stable) tells you when to stop.

#### Key Features

*   Automated multi-pass refinement
*   Extended AI reasoning integration
*   Markdown-based plan processing
*   Progressive structure improvement

#### Tech Stack

Bash Oracle CLI GPT Pro Markdown

#### Synergies

JFP Battle-tested prompts can be refined into specifications

CM Refined plans become searchable memories

BV Refined specs generate well-structured beads

### JFP

JeffreysPrompts CLI

120

[](https://jeffreysprompts.com/)

Official CLI for jeffreysprompts.com - browse, search, and install battle-tested prompts as Claude Code skills. Features interactive fzf-style picker and task-based suggestion engine.

#### Why It's Useful

Instead of writing prompts from scratch, install proven patterns. The interactive mode (jfp i) lets you fuzzy-search the entire library, while jfp suggest recommends prompts based on your task description. Premium features include collections, cross-machine sync, and a skills marketplace.

#### Key Features

*   One-command skill installation
*   Browsable prompt categories
*   Claude Code skills integration
*   MCP server for agent access

#### Tech Stack

TypeScript Bun Claude Code Skills API

#### Synergies

MS JFP downloads remote prompts, MS manages local skills - they complement each other

APR Downloaded prompts can be refined into comprehensive specs via APR

CM Effective prompts become retrievable memories

### PT

Process Triage

45

[](https://github.com/Dicklesworthstone/process_triage)

Bayesian-inference zombie/abandoned process detection using four-state classification (Useful, Useful-but-bad, Abandoned, Zombie) with evidence-based posterior probability scoring.

#### Why It's Useful

When builds hang or test runners go rogue, PT computes P(state|evidence) using process type, age, CPU/IO activity, memory, and past decisions. Confidence levels (very_high >0.99 to low <0.80) guide safe termination with identity validation and staged kill signals.

#### Key Features

*   Intelligent process scoring
*   Interactive TUI selection
*   Robot mode for automation
*   Resource usage analysis

#### Tech Stack

Rust Bayesian inference procfs

#### Synergies

SRPS PT terminates stuck processes, SRPS prevents them from hogging resources

NTM Clean up runaway processes in tmux sessions

### TRU

Token-Optimized Notation

156

[](https://github.com/Dicklesworthstone/toon_rust)

Token-optimized notation format for efficient LLM context packing. Compresses structured data into a dense format that maximizes information per token.

#### Why It's Useful

LLM context windows are precious. TRU compresses JSON, YAML, and other structured data into a compact notation that conveys the same information in fewer tokens, letting you fit more context into each request.

#### Key Features

*   40-70% token count reduction
*   Multi-language support
*   Token count statistics
*   Reversible compression

#### Tech Stack

Rust

#### Synergies

S2P Compress source prompts for maximum context efficiency

CASS Compact session data for storage and search

### RP

Rust Proxy

156

[](https://github.com/Dicklesworthstone/rust_proxy)

Transparent HTTP/HTTPS proxy for debugging and inspecting network traffic. Routes requests through a local proxy for analysis.

#### Why It's Useful

When debugging API integrations or AI agent network calls, you need visibility into what's being sent and received. Rust Proxy provides transparent interception without modifying your code.

#### Key Features

*   Transparent HTTP/HTTPS proxying
*   Request/response logging
*   Latency measurement
*   Header inspection

#### Tech Stack

Rust

#### Synergies

RANO Complementary network debugging - proxy vs observer

CASS Log network calls alongside session history

### RANO

Network Observer

156

[](https://github.com/Dicklesworthstone/rano)

Network observer for AI CLI tools that logs requests and responses without proxying. Passive monitoring of LLM API traffic.

#### Why It's Useful

Understanding what your AI agents are actually sending to APIs helps with debugging, cost tracking, and optimization. RANO passively observes network traffic without adding proxy overhead.

#### Key Features

*   Transparent HTTP proxy interception
*   Provider-aware log parsing
*   Token and cost tracking
*   Real-time traffic monitoring

#### Tech Stack

Rust

#### Synergies

CAUT Network observations feed usage tracking

CASS Correlate network calls with session history

### MDWB

Markdown Web Browser

156

[](https://github.com/Dicklesworthstone/markdown_web_browser)

Converts websites to clean Markdown for LLM consumption. Strips ads, navigation, and boilerplate to extract just the content.

#### Why It's Useful

AI agents need web content in a format they can understand. MDWB fetches pages and converts them to clean Markdown, perfect for feeding into LLM context windows.

#### Key Features

*   Clean content extraction
*   Code block preservation
*   Link handling
*   Pipe-friendly output

#### Tech Stack

Rust

#### Synergies

TRU Compress fetched content for maximum token efficiency

CM Store fetched content as memories

### AADC

ASCII Art Diagram Corrector

156

[](https://github.com/Dicklesworthstone/aadc)

Fixes malformed ASCII art diagrams generated by AI. Corrects alignment, box characters, and connection lines.

#### Why It's Useful

AI models often generate ASCII diagrams with alignment issues, broken lines, or inconsistent characters. AADC automatically detects and fixes these problems.

#### Key Features

*   Auto-repair box alignment
*   Connector line fixing
*   Before/after diff preview
*   Clipboard integration

#### Tech Stack

Rust

#### Synergies

S2P Clean up diagrams in generated prompts

CM Store corrected diagrams as memories

### CAUT

Coding Agent Usage Tracker

156

[](https://github.com/Dicklesworthstone/coding_agent_usage_tracker)

Tracks LLM provider usage across multiple coding agents. Monitors API calls, token consumption, and costs.

#### Why It's Useful

When running multiple AI agents simultaneously, costs can spiral. CAUT provides visibility into which agents are using how many tokens and at what cost.

#### Key Features

*   Multi-provider usage aggregation
*   Per-session token breakdown
*   Cost estimation and trends
*   Export to CSV/JSON

#### Tech Stack

Rust

#### Synergies

RANO Network observations feed usage data

NTM Track usage per NTM-managed session

Mail Usage alerts via Agent Mail

## Get Started

The fastest way to set up the entire flywheel ecosystem is with ACFS. One command, 30 minutes, and you're ready to go.

`curl -fsSL https://raw.githubusercontent.com/Dicklesworthstone/agentic_coding_flywheel_setup/main/install.sh | bash -s -- --yes --mode vibe`

Or use the[step-by-step wizard](https://agent-flywheel.com/wizard/os-selection)for guided setup.
