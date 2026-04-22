---
tags:
  - library
title: "brainctl — persistent memory for AI agents"
url: "https://www.brainctl.org/"
company: [personal]
topics: []
created: 2026-04-21
source_type: raindrop
raindrop_id: 1691697658
source_domain: "brainctl.org"
source_type_raindrop: link
collection: "unsorted"
collection_id: -1
hydrated: true
hydrated_at: 2026-04-22
hydrated_via: defuddle
---
## Excerpt

A local-first SQLite memory layer for autonomous agents. 201 MCP tools · 19 plugins · hybrid FTS+vector retrieval · MIT licensed.

## Raw Content

<!-- Hydrated 2026-04-22 via defuddle -->

CAnot deployed — no CA yet

```
# install
$ pip install brainctl

# orient → work → persist
from agentmemory import Brain
brain = Brain(agent_id="my-agent")

ctx = brain.orient(project="api-v2")
brain.remember("rate-limit: 100/15s", category="integration")
brain.entity("RateLimitAPI", "service")
brain.wrap_up("auth module complete")
```

## Agents forget. This is the fix.

Every agent session starts from zero. brainctl gives your agent a persistent brain it can read at session start, write to during work, and hand off to the next run.

### sqlite, zero infra

The entire store lives in `brain.db`. WAL mode, foreign keys on, portable across machines. No Docker, no servers, no cloud vendor. Your memories live on your disk — no blobs rented from a chain, no queries billed by the MB, no relayer standing between your agent and its own past.

### hybrid recall

FTS5 full-text search stacks on top of sqlite-vec embeddings via Ollama. Find memories by word or by meaning. Zero API spend on retrieval.

### knowledge graph

Entities, observations, typed relations. Your agent builds a living model of people, services, projects, and decisions — not just a chat log.

### handoff packets

One agent picks up exactly where another left off. Goal, state, open loops, next step — all preserved. Zero context loss across sessions.

### any agent, any stack

Python API, CLI, and a 201-tool MCP server. 19 first-party plugins across agent frameworks (Claude Code, Codex CLI, Cursor, Eliza, Gemini CLI, Goose, Hermes, OpenClaw, OpenCode, Pi, Rig, Virtuals Game, Zerebro) and trading bots (Freqtrade, Jesse, Hummingbot, NautilusTrader, OctoBot, Coinbase AgentKit). Speaks stdio MCP to anything else (VS Code, Claude Desktop, Zed).

### mit, forever

The software is free and will remain so under the MIT license, regardless of the token. The token funds the work; the code funds no one. No storage rent. No per-operation fees. No revocable access. The memory is yours, locally, for as long as you keep the file.

## Caller → core → storage. All local.

Three layers sit between an agent and its memory. Everything below runs on your machine. No API calls on the hot path.

```
caller
  ├── claude code · codex cli · cursor · openclaw
  ├── eliza · hermes · freqtrade · jesse
  ├── vs code · zed  (stdio mcp, no plugin needed)
  ├── ide / cli / python agent
  └── any stdio-speaking mcp client
        │
        ▼
┌────────────────────┐     ┌────────────────────┐
│    Brain API       │     │    MCP server      │
│    python library  │     │    201 tools       │
└─────────┬──────────┘     └──────────┬─────────┘
          │                           │
          └─────────────┬─────────────┘
                        ▼
                   brain core
```

```
session
   │
   ▼
orient  ────►  work  ────►  wrap_up
             │                  │
   ┌─────────┼──────────┐       ▼
   ▼         ▼          ▼    handoff_packets
remember   decide    search      (next session)
   │         │          │
   ▼         ▼          ▼
┌────────────────────────────────────────────────┐
│  every write  →  W(m) gate                       │
│                  surprise score + semantic dedup│
│                                                 │
│  every read   →  hybrid retrieval                │
│                  fts5 + sqlite-vec + rrf merge  │
│                                                 │
│  every conflict → AGM belief revision             │
│                   ranked, collapsed, audited    │
└────────────────────────┬───────────────────────┘
                         ▼
                     brain.db
```

```
brain.db   sqlite · wal · 59 tables · 50 migrations

primitives
──────────
  memories         episodic + semantic, fts5 indexed
  events           temporal thread, causal chains
  entities         typed knowledge graph nodes
  knowledge_edges  typed relations between entities
  decisions        rationale + provenance ledger
  affect_log       emotional salience (VAD coords)
  agent_beliefs    per-agent AGM belief state
  dream_hypotheses consolidation-cycle conjectures
  handoff_packets  session-to-session state
  embeddings       sqlite-vec semantic vectors
  + 49 auxiliary (rbac, quarantine, workspace, audit, …)
                      │
                      │  quiet-hours cron
                      ▼
┌─────────────────────────────────────────────────┐
│  dream cycle                                    │
│  replay episodic → cluster → promote → decay    │
│  hypothesis generation over the knowledge graph │
└─────────────────────────────────────────────────┘

local deps:  sqlite-vec  ·  ollama nomic-embed-text  (no api calls)
```

201

mcp tools

50

migrations

59

tables

19

shipped plugins

## The community token will fund the work. The software stays free.

brainctl is and will remain MIT-licensed. The token exists *so that* the people building the memory layer for autonomous agents can afford to keep building it. No gatekeeping, no paywall, no closed source. Every dollar in and out of the dev wallet is published live on [/transparency](https://www.brainctl.org/transparency). **The ticker has not been finalised and is intentionally not published yet** — anything circulating with a brainctl-style symbol ahead of an announcement here is not us.

```
the token is not yet deployed.

there is no contract address. the token has not launched
on pump.fun. the ticker symbol is intentionally withheld
until launch — any token circulating now under a
brainctl-style ticker is not us. this page will publish the
real ticker and CA the moment we deploy.
the dev wallet below is already live and tracking any SOL
or SPL token that lands in it.
```

```
status:   held privately (anti-sniping hold)
reason:   publishing the pubkey pre-launch lets snipers
          watch it for the createToken tx
goes live: simultaneously with the token launch
detail:    view the transparency page →
```

ticker

withheld until launch

any token in market today claiming to be brainctl is not us

contract address

none — not deployed

launchpad

pump.fun (planned)

chain

solana (planned)

planned supply

1,000,000,000

team allocation

none — fair launch

utility

funds ongoing dev + research
