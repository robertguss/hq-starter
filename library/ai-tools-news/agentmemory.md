---
tags:
  - library
title: "agentmemory"
url: "https://www.agent-memory.dev/"
company: [personal]
topics: []
created: 2026-04-20
source_type: raindrop
raindrop_id: 1690973413
source_domain: "agent-memory.dev"
source_type_raindrop: link
collection: "unsorted"
collection_id: -1
hydrated: true
hydrated_at: 2026-04-22
hydrated_via: defuddle
---
## Excerpt

Persistent memory for AI coding agents. Runs locally. Zero external databases.

## Raw Content

<!-- Hydrated 2026-04-22 via defuddle -->

01

### HOOKS

12 AUTO-CAPTURE HOOKS PIPED INTO EVERY CODING AGENT. EVERY TOOL CALL, EVERY PROMPT, EVERY STOP BECOMES A COMPRESSED OBSERVATION.

02

### RECALL

TRIPLE-STREAM RETRIEVAL — BM25 + VECTOR + KNOWLEDGE GRAPH. RERANKED ON DEVICE. P50 UNDER 20MS ON A LAPTOP.

03

### CONSOLIDATE

HOURLY SWEEPS COMPRESS RAW OBSERVATIONS INTO SEMANTIC MEMORIES. DUPLICATES MERGED. STALE ROWS DECAYED. AUDIT ROW EMITTED EVERY DELETE.

- 12AUTO-HOOKS
	### CAPTURE EVERYTHING
	Every PreToolUse, PostToolUse, SessionStart, Stop, and the rest fire into the memory pipeline without a line of glue code. Install the plugin, done.
- 51MCP TOOLS
	### NATIVE MCP SURFACE
	memory\_save, memory\_recall, memory\_smart\_search, memory\_sessions, governance, audit, export — full surface behind a single MCP server.
- 119REST ENDPOINTS
	### HTTP FIRST
	Every MCP tool has a REST twin under /agentmemory/\*. Curl it. Fetch it from the browser. Proxy it from your own agent.
- BM25+ VECTOR + GRAPH
	### TRIPLE-STREAM RECALL
	Hybrid retrieval pipes lexical, semantic, and relational scores through an on-device reranker. 95.2% R@5 on LongMemEval-S.
- AUTOCONSOLIDATION
	### RAW → SEMANTIC
	Hourly sweep compresses observations into semantic memories, merges duplicates, decays stale rows with retention scoring, and emits a batched audit row.
- ∞REPLAY
	### JSONL SESSION IMPORT
	Point agentmemory at a Claude Code JSONL transcript and it rehydrates the full session — observations, tool uses, timeline — into the store.
- GRAPHEXTRACTION
	### KNOWLEDGE GRAPH
	Entities and relations extracted on compress. Query with /agentmemory/graph. Visualize in the viewer. Temporal edges supported.
- MESHFEDERATION
	### PEER-TO-PEER SYNC
	Register another agentmemory node, push / pull memories over authenticated HTTPS. Bearer-token required; no silent syncs.
- MDOBSIDIAN EXPORT
	### YOUR NOTES, HYDRATED
	Mirror memories to a sandboxed vault directory. Frontmatter-tagged markdown, ready for Obsidian's graph view.
- 5LLM PROVIDERS
	### BYO MODEL
	Claude subscription (default, zero config), Anthropic API, Gemini, MiniMax, OpenRouter. Detected from env.
- OTELOBSERVABILITY
	### TRACES + LOGS
	iii-observability worker on by default. Exporter: memory for local, OTLP for Jaeger / Honeycomb / Tempo. Every operation produces a span.
- 0EXTERNAL DBs
	### ONE PROCESS
	Runs as a single Node process. No Redis, Kafka, Postgres, Qdrant, Neo4j. State lives on disk as JSON. That's the whole stack.

### SHIP-WITH VIEWER · PORT 3113

The agentmemory server auto-starts a real-time viewer on port 3113. No install, no config. Everything the server sees, the viewer shows.

- LIVE OBSERVATION STREAM · EVERY HOOK AS IT FIRES
- SESSION EXPLORER · REPLAY ANY PAST SESSION
- MEMORY BROWSER · FILTER BY PROJECT / TYPE / CONFIDENCE
- KNOWLEDGE GRAPH VISUALIZATION · FORCE-DIRECTED
- HEALTH DASHBOARD · HEAP / RSS / EVENT LOOP LAG
```
$ open http://localhost:3113
```

SHIP-WITH VIEWER · PORT 3113

![agentmemory viewer live demo](https://www.agent-memory.dev/demo.gif)

AGENTMEMORY MEM0 LETTA COGNEE

RETRIEVAL R@5 95.2%81.4%73.8%78.1%

EXTERNAL DEPS 02 (Qdrant, Neo4j)1 (Postgres)1 (Neo4j)

MCP TOOLS 4412189

AUTO-HOOKS 12000

OPEN SOURCE YES (APACHE-2.0)YESYESYES

1\. START THE MEMORY SERVER

2\. OPEN THE LIVE VIEWER

3\. WIRE UP ANY AGENT

ONE MCP JSON FITS ALMOST EVERYTHING. PICK YOUR AGENT ON THE LEFT, OR PASTE THE UNIVERSAL CONFIG ON THE RIGHT.

AGENTS

[CURSOROPEN](cursor://anysphere.cursor-deeplink/mcp/install?name=agentmemory&config=eyJjb21tYW5kIjoibnB4IiwiYXJncyI6WyIteSIsIkBhZ2VudG1lbW9yeS9tY3AiXSwiZW52Ijp7IkFHRU5UTUVNT1JZX1VSTCI6Imh0dHA6Ly9sb2NhbGhvc3Q6MzExMSJ9fQ%3D%3D) [VS CODEOPEN](vscode:mcp/install?%7B%22name%22%3A%22agentmemory%22%2C%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40agentmemory%2Fmcp%22%5D%2C%22env%22%3A%7B%22AGENTMEMORY_URL%22%3A%22http%3A%2F%2Flocalhost%3A3111%22%7D%7D)

CURSOR / VS CODE ARE ONE-CLICK VIA DEEPLINK. OTHERS COPY THE RIGHT SNIPPET DIRECTLY TO YOUR CLIPBOARD.

UNIVERSAL MCP JSONWORKS FOR CLAUDE DESKTOP · CURSOR · CLINE · WINDSURF · GEMINI CLI · OPENCODE

```
{
  "mcpServers": {
    "agentmemory": {
      "command": "npx",
      "args": ["-y", "@agentmemory/mcp"],
      "env": {
        "AGENTMEMORY_URL": "http://localhost:3111"
      }
    }
  }
}
```
