---
tags:
  - library
title: "gitagent | your repository becomes your agent"
url: "https://www.gitagent.sh/"
company: [personal]
topics: []
created: 2026-03-01
source_type: raindrop
raindrop_id: 1625095838
source_domain: "gitagent.sh"
source_type_raindrop: link
collection: "AI Tools & News"
collection_id: 69284314
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

A framework-agnostic, git-native standard for defining AI agents. Clone a repo, get an agent.

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: GitAgent — The Open Standard for Git-Native AI Agents

URL Source: https://www.gitagent.sh/

Markdown Content:
Open Standard v0.1.0·Clone a repo. Get an agent.

![Image 1: GitAgent](https://www.gitagent.sh/assets/gitagent-logo-Bz2-gkDG.png)

your repository becomes your agent

The open standard for defining, versioning, and running AI agents natively in git.

A git-native, framework-agnostic, open standard for defining AI agents. Version-controlled config that exports to Claude Code, OpenClaw, Lyzr Agent, Chimera, NanoBot, CrewAgent, and Agents SDK.

Maintained by team [@Lyzr](https://lyzr.ai/)

$ npx @open-gitagent/gitagent@latest run -r https://github.com/shreyas-lyzr/architect -a claude

Runs the GitAgent CLI, pulls the [Architect](https://github.com/shreyas-lyzr/architect) agent from GitHub, and launches it as a Claude Code agent.

Supports

Easy versioning

dev→staging→main

$ tree my-agent-repository/

my-agent-repository/

├── agent.yaml config

├── SOUL.md core

├── RULES.md

├── AGENTS.md

├── INSTRUCTIONS.md

├── scheduler.yml

├── skills/capability

│ └── code-review/

│ └── SKILL.md

├── tools/capability

│ └── search.yaml

├── knowledge/

│ └── index.yaml

├── memory/

│ ├── MEMORY.md

│ └── runtime/live

│ ├── dailylog.md

│ ├── key-decisions.md

│ └── context.md

├── hooks/

│ ├── hooks.yaml

│ ├── bootstrap.md

│ └── teardown.md

├── skillflows/automation

│ └── code-review-flow.yaml

└── compliance/governance

└── regulatory-map.yaml

## AI Agent Design Patterns Built on Git

A gitagent is your git repository as an agent — complete with version control, branching, pull requests, and collaboration built in. These are the architectural patterns that emerge when you define agents as git-native file systems.

Human-in-the-Loop for RL Agents

When an agent learns a new skill or writes to memory, it can open a `branch + PR` for human review before merging.

![Image 2: Human-in-the-Loop for RL Agents: agents create branches and PRs for human review before updating memory or skills](https://www.gitagent.sh/assets/human-in-the-loop-5af7zmsf.png)

LLM Wiki — Persistent Knowledge Base

Instead of RAG that rediscovers knowledge on every query, the LLM **incrementally builds a wiki** from raw sources in `knowledge/`. Compiled pages live in `memory/wiki/` with cross-references, an `index.md` catalog, and a chronological `log.md`. Three skills — `ingest`, `query`, `lint` — maintain the knowledge base over time. Inspired by [Karpathy's LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f). Scaffold with `gitagent init --template llm-wiki`.

![Image 3: LLM Wiki: raw sources in knowledge/ compiled into interlinked wiki pages in memory/wiki/ via ingest, query, and lint skills](https://www.gitagent.sh/assets/llm-wiki-YVNIp4p2.png)

Agent Versioning

Every change to your agent is a `git commit`. Roll back broken prompts, revert bad skills, and explore past versions — full undo history for your agent, powered by git.

![Image 4: Agent Versioning: git commit history showing agent changes that can be reverted](https://www.gitagent.sh/assets/agent-versioning-BCu_nQTL.png)

Live Agent Memory

The `memory/` folder holds a `runtime/` subfolder where agents write live knowledge — `dailylog.md`, `key-decisions.md`, and `context.md` — persisting execution state across sessions.

![Image 5: Live Agent Memory: memory/ folder with runtime logs, key decisions, and context files](https://www.gitagent.sh/assets/live-agent-memory-D7fpIsFv.png)

SkillsFlow

Deterministic, multi-step workflows defined in `workflows/` as YAML. Chain `skill:`, `agent:`, and `tool:` steps with `depends_on` ordering, `${{ }}` template data flow, and per-step `prompt:` overrides.

![Image 6: SkillsFlow: deterministic multi-step workflows chaining skills, agents, and tools via YAML with template data flow](https://www.gitagent.sh/assets/skillsflow-JQlJVItu.png)

Stateless Compute, Git as State

The VM is stateless. Git is the state. Agents run in ephemeral compute, committing every meaningful event — `bootstrap`, `execute`, `checkpoint`, `teardown` — to a `runtime/<date>/<job-id>` branch. Full audit trail, deterministic replay, and failure recovery — all from git history.

![Image 7: Stateless Compute: ephemeral VMs commit every event to git runtime branches for audit and recovery](https://www.gitagent.sh/assets/stateless-compute-Da7liSGE.png)

Shared Context & Skills via Monorepo

Anything placed at the root — `context.md`, `skills/`, `tools/` — is automatically shared across every agent in the monorepo. No duplication, one source of truth.

![Image 8: Shared Context: root-level context.md, skills/, tools/, and knowledge/ inherited by all agents](https://www.gitagent.sh/assets/shared-context-BmLnT3UA.png)

Branch-based Deployment

Use git branches to promote agent changes through environments — just like shipping software.

![Image 9: Branch-based Deployment: dev, staging, and main branches for promoting agent changes](https://www.gitagent.sh/assets/branch-deployment-DNJ6dkV0.png)

Knowledge Tree

The `knowledge/` folder stores entity relationships as a hierarchical knowledge tree + embeddings — letting agents reason over structured data at runtime.

![Image 10: Knowledge Tree: the knowledge/ folder stores entity relationships as a directory tree with embeddings](https://www.gitagent.sh/assets/knowledge-tree-byvgT8Qy.png)

Agent Forking & Remixing

Fork any public agent repo, customize its `SOUL.md`, add your own skills, and PR improvements back upstream — open-source collaboration for AI agents.

![Image 11: Agent Forking & Remixing: fork an agent, customize it, and contribute back via pull request](https://www.gitagent.sh/assets/agent-forking-CogzA65b.png)

CI/CD for Agents

Run `gitagent validate` on every push via GitHub Actions. Test agent behavior in CI, block bad merges, and auto-deploy to production — treat agent quality like code quality.

![Image 12: CI/CD for Agents: GitHub Actions pipeline with validate, test, merge, and deploy stages](https://www.gitagent.sh/assets/ci-cd-agents-BfyErwn2.png)

Agent Diff & Audit Trail

`git diff` shows exactly what changed between agent versions. `git blame` traces every line to who wrote it and when — full traceability out of the box.

![Image 13: Agent Diff & Audit Trail: git diff and git blame showing full traceability of agent changes](https://www.gitagent.sh/assets/agent-diff-audit-BwrzmBRG.png)

Tagged Releases

Tag stable agent versions like `v1.1.0`. Pin production to a tag, canary new versions on staging, and roll back instantly if something breaks.

![Image 14: Tagged Releases: git timeline with version tags, production and staging pointers, and instant rollback](https://www.gitagent.sh/assets/tagged-releases-CKg8gjZp.png)

Secret Management via .gitignore

Agent tools that need API keys or credentials read from a local `.env` file — kept out of version control via `.gitignore`. Agent config is shareable, secrets stay local.

![Image 15: Secret Management: version-controlled agent config separated from ignored .env and credentials](https://www.gitagent.sh/assets/secret-management-SiGnAL-g.png)

Agent Lifecycle with Hooks

Define `bootstrap.md` and `teardown.md` in the `hooks/` folder to control what an agent does when it starts up and what it should do before it stops — injecting lifecycle logic at key points.

![Image 16: Agent Automation Hooks: hooks/ folder with bootstrap.md and teardown.md for agent lifecycle events](https://www.gitagent.sh/assets/agent-automation-hooks-C3LMT_l5.png)

Segregation of Duties (SOD)

No single agent should control a critical process end-to-end. Define roles (maker, checker, executor, auditor) in `agent.yaml` + `DUTIES.md` with conflict matrices and handoff rules — `gitagent validate` catches violations before deployment.

![Image 17: Segregation of Duties: conflict matrix with maker, checker, executor, auditor roles and DUTIES.md policy](https://www.gitagent.sh/assets/segregation-of-duties-e6202xG2.png)

## Why GitAgent: The Git-Native AI Agent Standard

Everything your agent needs, defined in files you already know how to manage.

Git-Native

Version control, branching, diffing, and collaboration built in. Your agent definition is just files in a repo.

Framework-Agnostic

Works with Claude Code, OpenAI, CrewAI, LangChain, and more. Define once, export anywhere.

Compliance-Ready

First-class FINRA, SEC, and Federal Reserve support. Audit logging, supervision, and model risk management.

Composable

Skills, tools, sub-agents, and workflows. Agents can extend, depend on, and delegate to each other.

## How the GitAgent Agent Framework Works

Three files define your agent. Everything else is optional.

```
spec_version: "0.1.0"
name: code-review-agent
version: 1.0.0
description: Automated code review agent
author: gitagent-examples
license: MIT
model:
  preferred: claude-sonnet-4-5-20250929
  fallback:
    - claude-haiku-4-5-20251001
  constraints:
    temperature: 0.2
    max_tokens: 4096
skills:
  - code-review
tools:
  - lint-check
  - complexity-analysis
runtime:
  max_turns: 20
  timeout: 120
```

## Run AI Agents from Git

Clone any agent repo and run it instantly. One command — no setup, no config files to copy.

$ gitagent run -r "https://github.com/shreyaskapale/shreyas-agent" -a claude

→ Clones the repo (cached at `~/.gitagent/cache/`)

→ Reads `agent.yaml` + `SOUL.md` + skills

→ Launches Claude Code with the agent's full identity

`-b develop`—specific branch`--refresh`—force re-clone`-p "Review my code"`—one-shot prompt`-a git`—auto-detect adapter

## Export to Any AI Framework

One agent definition. Every framework.

Claude Code

Export to CLAUDE.md with skills, model hints, and compliance.

`$ gitagent export -f claude-code`

OpenAI Agents SDK

Generate Python code with Agent(), Tool stubs, and type mappings.

`$ gitagent export -f openai`

CrewAI

YAML crew config with role/goal extraction and sub-agent mapping.

`$ gitagent export -f crewai`

OpenClaw

Workspace with config JSON, AGENTS.md, tools, and skills.

`$ gitagent export -f openclaw`

Nanobot

Config JSON + system prompt for Nanobot runtime.

`$ gitagent export -f nanobot`

Lyzr Studio

API payload with provider mapping and credential IDs.

`$ gitagent export -f lyzr`

GitHub Models

Chat completions payload with model namespace mapping.

`$ gitagent export -f github`

System Prompt

Single concatenated markdown for any LLM.

`$ gitagent export -f system-prompt`

## GitAgent CLI: Build & Run AI Agents

Everything you need to build, validate, run, and ship agents.

`init`Scaffold a new agent repo

`$ gitagent init --template <minimal|standard|full>`

Templates: minimal (2 files), standard (skills + tools), full (compliance + hooks + memory)

`validate`Validate agent against spec

`$ gitagent validate --compliance`

JSON schema validation, skill checks, and optional regulatory compliance audit

`run`Run agent with any adapter

`$ gitagent run -a <adapter> -p "prompt"`

Adapters: claude, openai, crewai, openclaw, nanobot, lyzr, github, git (auto-detect)

`export`Export to another framework

`$ gitagent export --format <format> -o output`

Formats: system-prompt, claude-code, openai, crewai, openclaw, nanobot, lyzr, github

`import`Import from Claude, Cursor, CrewAI

`$ gitagent import --from <format> <path>`

Convert existing agent configs into gitagent format

`install`Resolve git-based dependencies

`$ gitagent install`

Shallow-clones dependencies at specified versions into mount paths

`skills`Search, install, list, inspect skills

`$ gitagent skills search "code review"`

Registries: SkillsMP marketplace, GitHub repos, local filesystem

`audit`Generate compliance audit report

`$ gitagent audit`

FINRA 3110, SEC 17a-4, SR 11-7, CFPB checks with pass/fail/warn indicators

`info`Display agent summary

`$ gitagent info`

Shows config, model, skills, tools, compliance, and SOUL.md preview

`lyzr`Create, update, and run on Lyzr Studio

`$ gitagent lyzr run -r <repo> -p "Hello"`

One command: clone → create agent on Lyzr → chat. Saves agent ID for reuse

## Framework Adapters: One Standard, Every Runtime

One agent definition. Eight runtime targets.

Claude Code`claude`

Mode Interactive / one-shot

Req Claude Code CLI

Append system prompt Sub-agents Hook mapping Permission modes

OpenAI Agents SDK`openai`

Mode One-shot

Req OPENAI_API_KEY, Python 3

Auto-generated Python code Tool function stubs Type mappings

CrewAI`crewai`

Mode One-shot

Req CrewAI CLI

YAML config export Role/goal extraction Sub-agent mapping

OpenClaw`openclaw`

Mode One-shot

Req ANTHROPIC_API_KEY, OpenClaw CLI

Auto-provision auth Workspace generation HITL → thinking=high

Nanobot`nanobot`

Mode Interactive / one-shot

Req ANTHROPIC_API_KEY, Nanobot CLI

Auto-provision auth Config + system prompt Environment variables

Lyzr Studio`lyzr`

Mode One-shot

Req LYZR_API_KEY

REST API deployment Agent ID persistence Provider auto-mapping

GitHub Models`github`

Mode One-shot (streaming)

Req GITHUB_TOKEN (models:read)

Model namespace mapping Streaming responses Multi-provider support

Git (Auto-Detect)`git`

Mode Auto

Req Depends on detected adapter

.gitagent_adapter hint Model-based detection File-based fallback

## AI Agent Skills System

Reusable capability modules following the [Agent Skills](https://agentskills.io/) standard.

### SKILL.md Format

```
---
name: code-review
description: Thorough code reviews
license: MIT
compatibility: ">=0.1.0"
allowed-tools: Read Edit Grep Glob Bash
metadata:
  author: "Jane Doe"
  version: "1.0.0"
  category: "developer-tools"
---

# Instructions

Review the code for:
1. Security vulnerabilities
2. Performance issues
3. Code style consistency
```

### Discovery Priority

1

`<agent>/skills/`Agent-local

2

`<agent>/.agents/skills/`agentskills.io

3

`<agent>/.claude/skills/`Claude Code

4

`<agent>/.github/skills/`GitHub

5

`~/.agents/skills/`Personal (global)

### Skill CLI

Search SkillsMP or GitHub

`$ gitagent skills search "code review"`

Install to global or local

`$ gitagent skills install code-review --global`

List discovered skills

`$ gitagent skills list`

Inspect skill metadata

`$ gitagent skills info code-review`

### Registries

SkillsMP REST API marketplace

GitHub Sparse clone from repos

Local Filesystem path copy

## SkillsFlow

Deterministic, multi-step workflows that chain skills together via YAML in `workflows/`.

```
name: code-review-flow
description: Full code review pipeline
triggers:
  - pull_request

steps:
  lint:
    skill: static-analysis
    inputs:
      path: ${{ trigger.changed_files }}

  review:
    agent: code-reviewer
    depends_on: [lint]
    prompt: |
      Focus on security and performance.
      Flag any use of eval() or raw SQL.
    inputs:
      findings: ${{ steps.lint.outputs.issues }}

  test:
    tool: bash
    depends_on: [lint]
    inputs:
      command: "npm test -- --coverage"

  report:
    skill: review-summary
    depends_on: [review, test]
    conditions:
      - ${{ steps.review.outputs.severity != 'none' }}
    inputs:
      review: ${{ steps.review.outputs.comments }}
      coverage: ${{ steps.test.outputs.report }}

error_handling:
  on_failure: notify
  channel: "#eng-reviews"
```

### Key Concepts

Deterministic Execution

Skills run in declared order, not LLM discretion. Every run follows the same path.

Data Flow via Templates

Chain outputs to inputs with ${{ steps.X.outputs.Y }} template syntax.

Per-Step Prompting

Add extra context per step with the prompt: field — guide the agent without changing the skill.

Mixed Step Types

Combine skill:, agent:, and tool: steps in a single flow for maximum flexibility.

### Execution Pipeline

1`lint`skill

2`review`agent

3`test`tool

4`report`skill

## AI Agent Compliance & Governance

First-class regulatory support baked into the manifest. Run `gitagent audit` for a full report.

### Risk Tiers

Low Minimal — standard logging

Standard Audit logging recommended

High HITL required, audit logging, compliance artifacts

Critical Kill switch, immutable logs, quarterly validation

### Compliance Artifacts

```
compliance/
├── risk-assessment.md
├── regulatory-map.yaml
└── validation-schedule.yaml
```

### Regulatory Frameworks

FINRA`Rule 3110, 4511, 2210`

Supervisor assignment, HITL, escalation, retention (6y+), fair/balanced comms

Federal Reserve`SR 11-7, SR 23-4`

Model inventory, validation cadence, ongoing monitoring, vendor due diligence

SEC`Reg S-P, 17a-4`

Audit logging, PII handling, retention (3y+)

CFPB`Circular 2022-03`

Bias testing, fair lending analysis

## Frequently Asked Questions

Common questions about the GitAgent open AI agent standard.

## Quick Start: Define Your First AI Agent

Seven commands from install to deploy.

$ npm install -g gitagent # Install the CLI

$ gitagent init --template standard # Scaffold an agent

$ gitagent validate # Check it's valid

$ gitagent run -d ./my-agent # Run with Claude Code

$ gitagent run -a github -p "Review" # Run with GitHub Models

$ gitagent export --format openai # Export for OpenAI SDK

$ gitagent run -r <repo> -a claude # Run with Claude Code
