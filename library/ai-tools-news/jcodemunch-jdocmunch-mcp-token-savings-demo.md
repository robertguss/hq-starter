---
tags:
  - library
title: "jCodeMunch + jDocMunch MCP — Token Savings Demo"
url: "https://j.gravelle.us/jCodeMunch/"
company: [personal]
topics: []
created: 2026-03-08
source_type: raindrop
raindrop_id: 1634653292
source_domain: "j.gravelle.us"
source_type_raindrop: link
collection: "AI Tools & News"
collection_id: 69284314
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: jCodeMunch MCP — Cut AI Coding Agent Token Costs 95%+

URL Source: https://j.gravelle.us/jCodeMunch/

Markdown Content:
*   [Benchmark](https://j.gravelle.us/jCodeMunch/#comparison)
*   [Examples](https://j.gravelle.us/jCodeMunch/#examples)
*   [Cost Analysis](https://j.gravelle.us/jCodeMunch/#cost)
*   [How It Works](https://j.gravelle.us/jCodeMunch/#how)
*   [Starter Packs](https://j.gravelle.us/jCodeMunch/#starter-packs)
*   [FAQ](https://j.gravelle.us/jCodeMunch/#faq)
*   [vs. Alternatives](https://j.gravelle.us/jCodeMunch/versus.php)
*   [Recognition](https://j.gravelle.us/jCodeMunch/recognition.php)

[License Details](https://j.gravelle.us/jCodeMunch/descriptions.php)[View Pricing](https://j.gravelle.us/jCodeMunch/#pricing)[Try Free](https://github.com/jgravelle/jcodemunch-mcp)

MCP Server for Code Retrieval

## New frontier models.

Same token bloat.

jCodeMunch cuts it 95%+

Every new release — Claude Opus 4.7, GPT, Gemini — makes agentic coding more expensive. jCodeMunch is the model-agnostic MCP server that indexes your codebase once and feeds any AI agent exact functions, classes, and constants instead of whole files. 

**Stop wasting tokens. Start munching code.**

95% avg

LIVE TELEMETRY SHOWING OVER

164,001,468,085

Tokens Saved by Participating Users

Since 3/3/2026

MORE THAN $829,027.42 ...SAVED!

$806.13 average savings by our top 1,000 active clients!

O(1)

Retrieval Speed

Model-agnostic. Works with **Claude Code**, **Cursor**, **Antigravity**, **Gemini**, and any MCP-compatible client.

↓ See Who It's For

Who This Is For

## Built for AI-Powered Development Teams

jCodeMunch serves anyone whose AI agents read code — from solo developers to platform teams managing token budgets across entire organizations.

⚡

AI Engineers Using Claude Code

Build with MCP-native code retrieval instead of reading entire files into context. Ship faster with precise symbol access.

🔨

Teams Using MCP Clients

Works with Antigravity, Cursor, Gemini, and any MCP-compatible client. Drop-in setup, immediate token savings.

📚

Developers Onboarding to Large Repos

Navigate unfamiliar codebases by searching for symbols directly — no need to read through thousands of lines to find what matters.

💰

Organizations Managing LLM Token Costs

Cut code-reading token spend by 95%+ across your engineering org. The savings compound with every developer and every query.

🌐

Open-Source Maintainers

Enable contributors to explore your codebase efficiently with AI agents. Lower the barrier to meaningful contributions.

Target Codebase

## Benchmark Codebase: fastapi/fastapi

A production Python web framework with 80k+ GitHub stars — routing, dependency injection, automatic OpenAPI generation, and security middleware — indexed directly from GitHub and queried verbatim for this benchmark.

📁

156

Source .py files

Excluding tests and docs

📝

~857 KB

Total source code

Raw characters

🪙

~214K

Tokens to read all files

tiktoken cl100k_base

🏗️

12

Core modules

routing, dependencies, security, openapi…

⚙️

883

Lines — routing.py alone

The heart of the framework

Benchmark

## AI Code Retrieval Benchmark: File Reads vs Symbol Retrieval

Compare a standard agent's file-based exploration vs. jCodeMunch symbol retrieval for the query: **"How does dependency injection work?"**

Standard Agent (File-based)

jCodeMunch MCP (Symbol-based)

0

Tokens Consumed (Old Way)

0

Tokens Consumed (jCodeMunch)

214,312

Tokens — Old Way

~480

Tokens — jCodeMunch

99.8%

Token Reduction

Real Query Results

## Real AI Code Retrieval Results from fastapi/fastapi

These are verbatim results from the jCodeMunch MCP server querying the indexed fastapi/fastapi codebase.

Query search_symbols("dependency injection")

READ: fastapi/routing.py

→ 8,836 tokens consumed

READ: fastapi/dependencies/utils.py

→ 5,218 tokens consumed

READ: fastapi/applications.py

→ 2,100 tokens consumed

READ: fastapi/security/oauth2.py

→ 2,640 tokens consumed

... 152 more files ...

TOTAL: 214,312 tokens used

Time to first result: ~4.2 seconds

→ code_search_symbols({

repo: "fastapi/fastapi",

query: "dependency injection"

})

✓ solve_dependencies(…) [dependencies/utils.py:154]

✓ get_dependant(…) [dependencies/utils.py:83]

✓ Depends(dependency) [params.py:4]

✓ run_in_threadpool(func, …) [concurrency.py:12]

Symbol source (solve_dependencies):

→ 428 chars, 14 lines retrieved

→ Exact function body, no noise

TOTAL: ~480 tokens used

Time to first result: 0.01 seconds

Token Usage by File

## Where the Tokens Go: File-by-File Breakdown

Each file read floods the context window. jCodeMunch retrieves only the symbol requested.

routing.py

8,836 tokens

8,836

dependencies/utils.py

5,218 tokens

5,218

dependencies/utils.py (MCP)

310 tokens

310

security/oauth2.py

2,640

security/oauth2.py (MCP)

90 tokens

90

applications.py

2,100

params.py

1,800

Misc (151 files)

193,718 tokens

193,718

Misc (151 files) (MCP)

30 tokens

30

| File | Lines | Tokens (Traditional) | Tokens (jCodeMunch) | Savings |
| --- | --- | --- | --- | --- |
| fastapi/routing.py | 883 | 8,836 | ~0 (not needed) | 100% |
| fastapi/dependencies/utils.py | 580 | 5,218 | ~310 (one function) | 94.1% |
| fastapi/security/oauth2.py | 290 | 2,640 | ~90 (one helper) | 96.6% |

Economics

## Token Costs Add Up: The Dollar Impact

Calculating the actual dollar impact of context-window waste on a 214K token codebase.

Traditional Way

$1.083

per query

214,312 tokens × $5.055/1M

 100 queries/day = $108.30/day

 Monthly cost = $3,249

 Annual cost = $39,030

jCodeMunch MCP

$0.0024

per query

~480 tokens × $5.055/1M

 100 queries/day = $0.24/day

 Monthly cost = $7.29

 Annual cost = $87.48

You Save

$1.0806

per query (99.8%)

At 100 queries/day:

 Save $108.06/day

 Save $3,242/month

**Save $38,943/year**

$38,943

Saved per year at 100 AI queries/day — on a single codebase

Scale to multiple projects and more queries per day, the savings multiply accordingly.

Architecture

## How jCodeMunch Indexes Code and Retrieves Exact Symbols

A pre-built symbol index lets the MCP server answer code queries in milliseconds with surgical precision.

1

### Index Once

Run `index_code_folder(path)` to index code symbols, or `index_doc_local(path)` (jDocMunch) to index documentation sections. Both build a persistent local index — happens once per project.

2

### AI Queries by Intent

Instead of reading files, the AI calls `search_symbols(query)` or `get_symbol(id)`. The MCP server performs semantic + keyword search against the index in milliseconds.

3

### Surgical Retrieval

Only the matching symbol's source code and metadata is returned — not the surrounding file, not unrelated classes. A 6,000-token file read is replaced by a 400-token symbol pull.

Use Cases

## Common Use Cases for MCP Code Retrieval

Symbol-level retrieval changes how AI agents interact with code. Here are the workflows where jCodeMunch and jDocMunch deliver the most value.

🔍

Onboarding to an Unfamiliar Codebase

Search for key symbols and retrieve their implementations directly. Understand architecture without reading every file in the repo.

🔒

Tracing Authentication Flows

Find auth middleware, token validators, and permission checks by symbol search. Follow the call chain through exact function bodies.

🔄

Understanding Dependency Injection

Retrieve DI containers, providers, and resolver functions by name. See how dependencies wire together without reading framework internals.

💡

Impact Analysis Before Refactoring

Search for all references to a symbol before changing it. Understand the blast radius of a refactor with precise, low-token lookups.

🎯

Retrieving Exact Implementation Details

When an AI agent needs the body of a specific function, it retrieves just that function — 400 tokens instead of 6,000 for the full file.

📃

Documentation Retrieval with jDocMunch

Pair jCodeMunch with jDocMunch to give AI agents surgical access to both code and documentation. Search sections, not files.

Instant Framework Context

## Starter Packs: Query Frameworks You've Never Cloned

Pre-built symbol indexes for popular frameworks. A 932 MB React repo becomes a 3 MB pack. A 1.4 GB Node.js monorepo becomes 10.6 MB. Install a pack and your AI agent gets symbol-level access — without cloning the repo or waiting for an index build.

📚

Learn Without Cloning

Explore React's fiber reconciler or Django's query compiler. Your agent searches thousands of symbols — no git clone, no local checkout.

🔎

Debug From Stack Traces

Got a confusing framework error? Search the pack for that symbol, read the implementation, understand the call path. Faster than GitHub search.

🔗

Cross-Repo Analysis

Install a framework pack + index your app. Now `find_importers` and `get_blast_radius` trace across the boundary into framework code.

⚡

Zero-Config Trial

No API key. No repo. No config. The free Node.js pack (76,700+ symbols) lets you experience real symbol retrieval in under 60 seconds.

**10 packs available.** Node.js (free), FastAPI, Django, Flask, React, LangChain, Anthropic SDK, MCP SDK, Laravel, and Spring Boot. Indexes are rebuilt weekly from the latest tagged release — always current, always stable API surfaces.

`jcodemunch-mcp install-pack nodejs`—[Browse all Starter Packs ↗](https://j.gravelle.us/jCodeMunch/starter-packs-system/)

Companion Tool

## jDocMunch MCP: Documentation Retrieval to Match

jCodeMunch munches **code**. jDocMunch munches **documentation** — the same surgical retrieval approach, applied to Markdown, READMEs, specs, and any text-based docs in your repo.

📚

index_doc_local()

Index any local folder of Markdown, RST, or plain-text docs. One call, persistent index.

🔍

search_sections()

Semantic search across headings and content. Returns only the matching section, not the whole file.

📋

get_section()

Pull a specific doc section by ID. Same O(1) byte-offset retrieval as jCodeMunch symbols.

🗺

get_toc_tree()

Retrieve the full table of contents structure without loading any content — orient first, fetch later.

**Same philosophy, different domain.** When an AI agent needs to answer “how does the auth flow work?” it shouldn’t read 40 README files. jDocMunch gives it `search_sections(“auth flow”)` — one call, the right section, nothing else.

`pip install git+https://github.com/jgravelle/jdocmunch-mcp.git`—[Learn more about jDocMunch on GitHub ↗](https://github.com/jgravelle/jdocmunch-mcp)

New — Now Available

## jDataMunch MCP: Instant Answers From Your Data

No code required. jDataMunch indexes your spreadsheets, databases, and data files so AI assistants can answer data questions precisely — without reading entire files or guessing at column names.

📊

describe_dataset()

Get an instant summary of any CSV or Excel file — row counts, column names, types, and nulls. No formulas needed.

🔍

search_data()

Search across column values to find matching rows instantly — without opening the file or writing a filter.

📈

describe_column()

Distribution, min/max, top values, histogram — everything about a column, retrieved surgically.

⚡

One-Time Setup

Index once, query forever. Works with Claude, Cursor, and any MCP-compatible AI assistant.

**Built for data people, not just developers.** If you work with spreadsheets and CSVs and want your AI assistant to actually understand your data — not hallucinate column names or miss rows — jDataMunch is the missing piece.

Supports CSV and Excel. Index once, then ask questions. —[See pricing & license details ↗](https://j.gravelle.us/jCodeMunch/descriptions.php#datamunch)

FAQ

## Frequently Asked Questions

Common questions about jCodeMunch, jDocMunch, and MCP-based code retrieval.

 How is jCodeMunch different from RepoMapper? 

Short version: RepoMapper is a **ranked repository "map"** (great for orientation and "what matters?"), while jCodeMunch is **symbol-accurate retrieval** (great for "show me the exact code" with tiny token spend). They overlap, but they're optimized for different jobs.

*   **RepoMapper** generates a "repo map" that highlights important files/definitions and relationships using Tree-sitter parsing plus a PageRank-like importance ranking. Best for first-pass orientation: "Which files matter for this task?"
*   **jCodeMunch** is symbol-first, not file-first: agents search and retrieve _functions/classes/methods/constants_ directly via byte-offset seeking in O(1) time. File reads become the exception, not the default.
*   **Scaling**: maps get bigger as repos grow; targeted symbol pulls stay tiny even in massive repos.

If you want a fast, ranked breadcrumb trail across a new codebase, RepoMapper is a solid compass. If you need precise, repeatable, low-token code retrieval for AI agents, jCodeMunch is the right tool.

 Which MCP clients does jCodeMunch work with? 

jCodeMunch works with any client that supports the **Model Context Protocol (MCP)**, including:

*   **Claude Code** — Anthropic's CLI for Claude, with native MCP support
*   **Google Antigravity** — Google's AI coding agent
*   **Cursor** — AI-native code editor
*   **Gemini** — Google's AI assistant with MCP integration
*   Any other MCP-compatible client or custom integration

Setup typically takes under a minute: install the server, add a config entry, and restart. See the [README](https://github.com/jgravelle/jcodemunch-mcp) for client-specific instructions.

 How do I integrate jCodeMunch with Google Antigravity? 

Antigravity uses a standard MCP config file — setup takes about a minute.

*   Install the server: `pip install git+https://github.com/jgravelle/jcodemunch-mcp.git`
*   In Antigravity, open the Agent pane → click the **⋮** menu → **MCP Servers** → **Manage MCP Servers**
*   Click **View raw config** to open `mcp_config.json`
*   Add the entry below, save, then restart the MCP server from the Manage MCPs pane

{
  "mcpServers": {
    "jcodemunch": {
      "command": "jcodemunch-mcp",
      "env": {
        "GITHUB_TOKEN": "ghp_...",
        "ANTHROPIC_API_KEY": "sk-ant-..."
      }
    }
  }
}
Both env vars are optional. `ANTHROPIC_API_KEY` enables AI-generated symbol summaries; `GITHUB_TOKEN` raises GitHub API rate limits and unlocks private repos.

 Why not just use a larger context window? 

Larger context windows have diminishing returns for code retrieval:

*   **Cost scales linearly**: reading 214K tokens costs ~$1.08 per query regardless of window size. jCodeMunch retrieves the same answer for ~$0.0024.
*   **Signal-to-noise ratio drops**: dumping entire files into context means the AI wades through thousands of irrelevant lines to find the one function it needs. Larger windows amplify the noise problem, they don't solve it.
*   **Latency grows**: more input tokens = slower time-to-first-token. Symbol retrieval returns results in milliseconds.
*   **Attention degrades**: research shows LLMs struggle with retrieval accuracy as context length increases — the "lost in the middle" effect. Smaller, precise context performs better.

A 1M-token context window doesn't help if you're paying to fill it with code the AI doesn't need. jCodeMunch gives the AI exactly what it asked for.

 Can I use jCodeMunch and jDocMunch together? 

Absolutely — they're designed as complementary tools. A typical pairing:

*   **jCodeMunch** for code retrieval: functions, classes, constants, methods — any symbol in your codebase.
*   **jDocMunch** for documentation retrieval: README sections, API docs, specs, architecture guides.

Together, they give AI agents surgical access to both code and docs without reading entire files. When an agent needs to understand how authentication works, it can search code symbols for the implementation _and_ search doc sections for the design rationale — all with minimal token spend.

Trio bundle pricing (all three tools) is available at all tiers. See [pricing](https://j.gravelle.us/jCodeMunch/#pricing) below.

 How much can jCodeMunch reduce my Claude token usage? 

In benchmarks measured with **tiktoken cl100k_base** across **15 tasks on 3 real repositories**, jCodeMunch achieved a **95% average token reduction** for code retrieval operations.

*   **fastapi/fastapi benchmark**: 214,312 tokens (reading all files) → ~480 tokens (symbol retrieval) = **99.8% reduction**
*   Results vary by query type — retrieval of a single function body is near-zero cost, while broader searches return more symbols but still far less than full file reads.
*   The 95% average is a conservative, tokenizer-measured figure across diverse query types and repos of different sizes.

Licensing

## Pricing: Choose Your License

Choose a single-product license for code, docs, or data — or get all three in a Munch Trio bundle. All licenses are commercial-use licenses for the specified tier.

Builder

Solo developer

Commercial use for 1 developer.

$99

trio bundle

~~$147 separate~~

*   jCodeMunch Builder License included
*   jDocMunch Builder License included
*   jDataMunch Builder License included
*   Code, docs, and data retrieval in one

Studio

Small team

Commercial use for up to 5 developers.

$449

trio bundle

~~$597 separate~~

*   jCodeMunch Studio License included
*   jDocMunch Studio License included
*   jDataMunch Studio License included
*   Full retrieval suite for AI-enabled teams

Platform

Org-wide deployment

Unlimited use company-wide!

$2,499

entire suite

~~$2,997 separate~~

*   jCodeMunch Platform License included
*   jDocMunch Platform License included
*   jDataMunch Platform License included
*   Full retrieval suite, org-wide, all three tools

Need enterprise terms or a custom deployment arrangement? Contact us for enterprise licensing.
