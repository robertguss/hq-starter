---
tags:
  - library
title: "Antfarm — Build your agent team with one command"
url: "https://www.antfarm.cool/"
company: [personal]
topics: []
created: 2026-02-10
source_type: raindrop
raindrop_id: 1592201553
source_domain: "antfarm.cool"
source_type_raindrop: link
collection: "AI Tools & News"
collection_id: 69284314
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

Multi-agent workflows for OpenClaw. Define a team of specialized AI agents in YAML. One install. Zero infrastructure.

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: Antfarm — Build your agent team with one command

URL Source: https://www.antfarm.cool/

Published Time: Wed, 15 Apr 2026 22:41:58 GMT

Markdown Content:
![Image 1: Antfarm](https://www.antfarm.cool/logo.jpeg)

You don't need to hire a dev team. You need to define one. Antfarm gives you a team of specialized AI agents — planner, developer, verifier, tester, reviewer — that work together in reliable, repeatable workflows. One install. Zero infrastructure.

## Antfarm gives you a team of agents that specialize, verify each other, and run the same playbook every time.

`$ curl -fsSL https://raw.githubusercontent.com/snarktank/antfarm/v0.5.1/scripts/install.sh | bash`

v0.5.1

Paste in your terminal, or just ask your OpenClaw to run it.

## What you get: Agent team workflows

Drop in a feature request. Get back a tested PR. The planner decomposes your task into stories. Each story gets implemented, verified, and tested in isolation. Failures retry automatically. Nothing ships without a code review.

plan→setup→implement→verify→test→PR→review

Point it at a repo. Get back a security fix PR with regression tests. Scans for vulnerabilities, ranks by severity, patches each one, re-audits after all fixes are applied.

scan→prioritize→setup→fix→verify→test→PR

Paste a bug report. Get back a fix with a regression test. Triager reproduces it, investigator finds root cause, fixer patches, verifier confirms. Zero babysitting.

triage→investigate→setup→fix→verify→PR

## Why it works

### Deterministic workflows

Same workflow, same steps, same order. Not "hopefully the agent remembers to test."

### Agents verify each other

The developer doesn't mark their own homework. A separate verifier checks every story against acceptance criteria.

### Fresh context, every step

Each agent gets a clean session. No context window bloat. No hallucinated state from 50 messages ago.

### Automatic retries

Failed steps retry automatically with configurable limits per step. The medic watches for stuck agents and cleans up abandoned work.

## How it works

1

### Define

Agents and steps in YAML. Each agent gets a persona, workspace, and strict acceptance criteria. No ambiguity about who does what.

2

### Install

One command provisions everything: agent workspaces, cron polling, subagent permissions. No Docker, no queues, no external services.

3

### Run

Agents poll for work independently. Claim a step, do the work, pass context to the next agent. SQLite tracks state. Cron keeps it moving.

## Minimal by design

YAML + SQLite + cron. That's it. No Redis, no Kafka, no container orchestrator. Antfarm is a TypeScript CLI with zero external dependencies. It runs wherever OpenClaw runs.

![Image 2: Ralph](https://raw.githubusercontent.com/snarktank/ralph/main/ralph.webp)

### Built on the Ralph loop

Each agent runs in a fresh session with clean context. Memory persists through git history and progress files — the same autonomous loop pattern from [Ralph](https://github.com/snarktank/ralph), scaled to multi-agent workflows.

## Quick example

```
$ antfarm workflow install feature-dev
✓ Installed workflow: feature-dev

$ antfarm workflow run feature-dev "Add user authentication with OAuth"
Run: a1fdf573
Workflow: feature-dev
Status: running

$ antfarm workflow status "OAuth"
Run: a1fdf573
Workflow: feature-dev
Steps:
  [done   ] plan (planner)
  [done   ] setup (setup)
  [running] implement (developer)  Stories: 3/7 done
  [pending] verify (verifier)
  [pending] test (tester)
  [pending] pr (developer)
  [pending] review (reviewer)
```

## Build your own

The bundled workflows are starting points. Define your own agents, steps, retry logic, and verification gates in plain YAML and Markdown. If you can write a prompt, you can build a workflow.

```
id: my-workflow
name: My Custom Workflow
agents:
  - id: researcher
    name: Researcher
    workspace:
      files:
        AGENTS.md: agents/researcher/AGENTS.md

steps:
  - id: research
    agent: researcher
    input: |
      Research {{task}} and report findings.
      Reply with STATUS: done and FINDINGS: ...
    expects: "STATUS: done"
```

Full guide: [docs/creating-workflows.md](https://github.com/snarktank/antfarm/blob/main/docs/creating-workflows.md)

## Security

You're installing agent teams that run code on your machine. We take that seriously.

#### Curated repo only

Antfarm only installs workflows from the official [snarktank/antfarm](https://github.com/snarktank/antfarm) repository. No arbitrary remote sources.

#### Reviewed for prompt injection

Every workflow is reviewed for prompt injection attacks and malicious agent files before merging.

#### Community contributions welcome

Want to add a workflow? Submit a PR. All submissions go through careful security review before they ship.

#### Transparent by default

Every workflow is plain YAML and Markdown. You can read exactly what each agent will do before you install it.

## Dashboard

Monitor runs, track step progress, and view agent output in real time.

![Image 3: Antfarm dashboard showing workflow runs and step status](https://www.antfarm.cool/dashboard-screenshot.png)

![Image 4: Antfarm dashboard showing run detail with stories](https://www.antfarm.cool/dashboard-detail-screenshot.png)

## Commands

#### Lifecycle

`antfarm install`Install all bundled workflows

`antfarm uninstall`Full teardown (agents, crons, DB)

#### Workflows

`antfarm workflow run <id> <task>`Start a run

`antfarm workflow status <query>`Check run status

`antfarm workflow runs`List all runs

`antfarm workflow resume <run-id>`Resume a failed run

`antfarm workflow stop <run-id>`Cancel a running workflow

`antfarm workflow ensure-crons <id>`Recreate crons after idle teardown

#### Management

`antfarm workflow list`List available workflows

`antfarm workflow install <id>`Install a single workflow

`antfarm workflow uninstall <id>`Remove a single workflow

`antfarm dashboard`Start the web dashboard

`antfarm logs`View recent log entries
