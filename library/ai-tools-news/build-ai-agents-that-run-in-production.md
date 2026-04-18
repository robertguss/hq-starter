---
tags:
  - library
title: "Build AI Agents That Run in Production"
url: "https://jido.run/"
company: [personal]
topics: []
created: 2026-03-07
source_type: raindrop
raindrop_id: 1633880293
source_domain: "jido.run"
source_type_raindrop: link
collection: "AI Tools & News"
collection_id: 69284314
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

Jido is an open-source agent framework for Elixir. Build supervised AI agents with fault tolerance, tool calling, and multi-agent coordination built in.

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: Build AI Agents That Run in Production

URL Source: https://jido.run/

Markdown Content:
OPEN-SOURCE ELIXIR FRAMEWORK

Jido is an agent framework for Elixir. Define agents, give them tools, and let them work together, with fault tolerance and supervision built in.

New to Elixir? [Start here.](https://jido.run/docs/getting-started/new-to-elixir)• Already an Elixir developer? [Jump to the expert guide.](https://jido.run/docs/getting-started/elixir-developers)

## What people build with Jido

From single-purpose assistants to teams of agents that coordinate autonomously.

### [Coding agents Agents that read, analyze, and refactor code across repositories.](https://jido.run/examples)### [Research and synthesis Multi-step research agents that find sources, verify facts, and produce reports.](https://jido.run/examples)### [Document processing Extract, classify, and route documents: invoices, contracts, support tickets.](https://jido.run/examples)### [Customer support Agents that resolve issues using your knowledge base and escalate when needed.](https://jido.run/examples)### [DevOps and monitoring Agents that watch systems, diagnose problems, and run remediation playbooks.](https://jido.run/examples)### [Data pipelines Agents that collect, transform, and load data from multiple sources on schedule.](https://jido.run/examples)

## Why teams choose Jido

Agent frameworks are everywhere. Here's what makes this one different.

[◉ ### Agents that self-heal When an agent crashes, its supervisor restarts it automatically with clean state. No orchestrator, no manual recovery, no downtime. Learn more →](https://jido.run/features/agents-that-self-heal)[⧉ ### Multi-agent workflows you can test Agents coordinate through typed Actions and Signals, not prompt chains. Debug and test each step independently, just like regular code. Learn more →](https://jido.run/features/multi-agent-coordination)[⬡ ### Observe everything Built-in telemetry and tracing across every agent. See what's happening, trace workflows across processes, catch problems before users do. Learn more →](https://jido.run/features/observe-everything)[▣ ### Start small, grow safely Add one agent to your existing Elixir app. No rewrite, no platform migration. Add more agents, tools, and packages only when you need them. Learn more →](https://jido.run/features/start-small)

◉

### Process isolation

Each agent runs in its own lightweight process with isolated memory. One agent failing never takes down another.

⟳

### Supervision and recovery

OTP supervisors detect crashes and restart agents in milliseconds. Failure recovery is built into the runtime, not bolted on.

⚡

### Massive concurrency

The BEAM scheduler handles thousands of concurrent agent processes with true parallelism. No thread pools, no async/await gymnastics.

jido jido_action jido_signal

jido_ai req_llm llm_db

ash_jido jido_messaging jido_otel

## Build your first agent

Go from zero to a running, supervised agent in under ten minutes.
