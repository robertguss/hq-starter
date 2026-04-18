---
tags:
  - library
title: "RetainDB — Persistent Memory for AI Agents | SOTA on LongMemEval"
url: "https://www.retaindb.com/"
company: [personal]
topics: []
created: 2026-04-04
source_type: raindrop
raindrop_id: 1672519383
source_domain: "retaindb.com"
source_type_raindrop: link
collection: "AI Tools & News"
collection_id: 69284314
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

Persistent memory and context infrastructure for AI agents. Scores SOTA on preference recall (LongMemEval). Ship AI agents that remember in under 30 minutes.

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: RetainDB — Persistent Memory for AI Agents | SOTA on LongMemEval

URL Source: https://www.retaindb.com/

Markdown Content:
[retain**db**](https://www.retaindb.com/)

( 01 / 10 )

Memory & context infrastructure for AI agents

## AI agents forget.

_Give yours the memory it deserves._

RetainDB gives your AI agents persistent memory — so users feel understood from session one, never repeat themselves, and keep coming back. Most teams are live in under 30 minutes.

Free to start · no credit card required

user

Built for AI agents that need to remember

The problem most AI agents have

## Every time your user opens a new chat,

_your AI meets them as a stranger._

It doesn't remember their preferences. It doesn't know they've explained their setup twice already. It just starts over.

Your users notice — even if they never say it. There's a low-grade friction to re-explaining context that should already be there. And slowly, quietly, they use your product less.

This is a memory problem.

Most AI agents have it.

Almost none of them have fixed it.

01

Support agents

An agent that already knows your user.

Users stop re-explaining their plan, their history, what they've already tried. The agent picks up exactly where the last conversation ended.

02

Coding agents

No more correcting an agent that forgot your stack.

It knows your constraints, your preferences, what you've already rejected. It compounds knowledge instead of losing it session to session.

03

Research agents

Every run builds on the last.

What's been covered, what was useful, what was a dead end — all carried forward. Research compounds instead of resetting.

04

Sales & outreach agents

Agents that walk in prepared, not cold.

Every interaction, objection, and outcome is remembered. The agent knows what was discussed and what to say next.

Customers who feel known

They reach out once and your agent already knows their history, plan, and what they care about. No more "can you describe the issue again?" — just fast, warm resolutions.

[See how it works](https://www.retaindb.com/use-cases/customer-support)

Support that gets better over time

Every resolved ticket makes the next one faster. Your agent learns from every customer it helps, compounding into a support experience your competitors can't replicate.

[See how it works](https://www.retaindb.com/use-cases/customer-support)

Zero-friction handoffs

When a human takes over, full context travels with them. Your customer never has to repeat themselves. The conversation just continues.

[See how it works](https://www.retaindb.com/use-cases/customer-support)

01

Step 01 — Remember

### User says something.

_We store it._

Every conversation is stored automatically. Next session, your agent already knows who the user is, what they've shared, and what matters to them.

// After each agent turn

await db

.user("usr_01")

.remember(userMessage);▋

02

Step 02 — Recall

### Before every response.

_Get what's relevant._

Before every response, RetainDB pulls exactly what's relevant from that user's history. Your agent gets the right context without the cost of replaying every conversation.

// Before every LLM call

const{ context } = await

db.user("usr_01")

.getContext(userQuery);▋

03

Step 03 — Ground

### Inject memory.

_Ship confidently._

The right context flows into every response automatically. Your AI becomes the assistant that actually listened — users feel remembered, not just handled. One call wraps all three steps if you want it even simpler.

// Or let runTurn() do all three

const{ response } = await

db.user(userId)

.runTurn({

messages,

generate: (ctx) =>

llm.chat(ctx)

});▋

JS, Python & Go

any language, any stack

Under 40ms

memory retrieval, globally

Works with any LLM

OpenAI · Anthropic · Gemini

SOC 2 ready

encrypted at rest + transit

State of the art

Best-in-class at remembering

_what users actually told it._

Highest preference recall on the academic memory benchmark — the category that matters most for personalised agents.

[See full results & methodology](https://www.retaindb.com/benchmark)

Category RetainDB Best other

Single-session preference★88%70%

Single-session user 88%97%

Temporal reasoning 74%77%

Knowledge update 76%89%

Multi-session 68%71%

Overall 79%82%

0%

Remembers user preferences

best score on the academic memory benchmark

0%

Wrong answers from your docs

tested across 16 real questions, March 2026

0%

Overall memory accuracy

across 5 test categories · March 2026

0 ms

Average memory recall time

users never notice the difference

### Your AI answers

from truth.

_Not guesses._

16 real SDK questions. Temperature 0.0. Without RetainDB, GPT-5 hallucinated on 89% of them. With RetainDB grounded to your docs — zero.

Hallucination rate — lower is better

Retaindb · grounded retrieval 0%

0 / 16 hallucinations — documentation-only grounding

GPT-5 Web · web search baseline 89.6%

web search, no docs grounding

GPT-5 · no grounded context 95.5%

same questions, vanilla GPT-5

### Memory benchmark.

_100 / 100._

Correct retrieval across all test cases. 12/12 successful source retrievals across 39 real files.

Memory benchmark

100/ 100

Correct retrievals across all test cases

10/10 test cases · 13ms avg latency

Source benchmark

12/12

Successful retrievals across 39 real files

score 100 · documentation-only grounding

Real example — one benchmark prompt

### Same question.

Two very different answers.

Every question in the matrix looks like this — not cherry-picked. Without grounding, the model confidently invents an API that doesn't exist. With Retaindb, it pulls from your actual docs.

[Full benchmark methodology](https://www.retaindb.com/benchmark)

// Enable Claude extended thinking

response = client.messages.create(

model="claude-3-opus",

extended_thinking=True # ← doesn't exist

)

from anthropic import Anthropic

client= Anthropic()

message= client.messages.create(

model="claude-3-7-sonnet-20250219",

thinking={"type":"enabled", "budget_tokens": 1024},

)

vs. Building it yourself

Most teams who try to build persistent memory in-house underestimate what it actually takes. Deduplication across sessions. Semantic retrieval that doesn't degrade. Per-user isolation. Token-efficient injection under 40ms.

That's 4–8 weeks of engineering work for a first version — and months more to harden it. RetainDB is that layer, already built and tested at scale.

**The trade:** Ship it this week or own it next quarter.

vs. Mem0 and other memory APIs

On the academic benchmark for AI memory, RetainDB scores highest on preference recall — the test that measures whether your AI remembers personal details and context across conversations. 88% vs. the field's 70%.

RetainDB does not use your data to train models. Your users' memory belongs to you. You control what gets stored, retrieved, and how long it's retained.

**The trade:** Best recall on the benchmark that matters, with full data ownership.

vs. Doing nothing

Your current agent starts every session from zero. Your users feel it — even if they haven't put it in words. Churn from agents that feel impersonal is harder to attribute than a broken feature. But it compounds just as fast.

**The trade:** Keep the product as it is, or give it memory in under 30 minutes.

( 08 / 10 )

Enterprise-ready

## Your users' data

stays yours.

_Full stop._

RetainDB is built for teams where data ownership isn't negotiable. Every user's memory is stored in isolation — no cross-contamination, no shared retrieval, no way for one user's data to surface in another's session.

[Enterprise enquiries →](https://cal.com/alameenpd/quick-chat)

SOC 2 ready

Encrypted at rest (AES-256) and in transit.

Per-user data isolation

No cross-user data bleed. No shared retrieval between users or projects.

Self-hosted option

Deploy on your own infrastructure — your Cloudflare account, your Postgres instance.

Deletion on demand

Wipe any user's memory at any time, by API or dashboard.

Retention control

You decide how long data lives. We don't decide for you.

No training on your data

We don't use your users' conversations to improve our models. Ever.

SDK

### Full control.

_Three lines of code._

Install, initialize, and your agent has persistent memory. JS, Python, and Go out of the box. Most teams are in production the same day.

JavaScript TypeScript Python Go

import{ RetainDB }from'retaindb';

const db= new RetainDB({

apiKey: process.env.RETAINDB_KEY

});

// Option A — manual: retrieve → generate → store

const{ context } = await db.user(userId).getContext(query);

const reply=await llm.chat({ system: context });

await db.user(userId).remember(userMessage);

// Option B — automatic: all three in one call

const{ turn } = await db

.user(userId).runTurn({

messages,

waitForMemoryWrite: true,

generate: (ctx) => llm.chat(ctx)

});

// turn.response, turn.writeStatus, turn.memorySummary

MCP

### Memory for any

_agent. No code._

Connect RetainDB as an MCP server. Claude, Cursor, or any MCP-compatible agent instantly gets persistent memory and recall — one config line, no SDK, no build step.

Claude Cursor Any MCP agent

Available MCP tools

retaindb_remember Store a memory from this turn

retaindb_get_context Fetch relevant memories before responding

retaindb_search Semantic search across all stored memories

retaindb_capture_session Extract memories from full conversation

Memory Router

### Memory injected.

_Your code untouched._

Swap one URL. RetainDB intercepts your LLM calls, injects the right memory automatically, and forwards to OpenAI or Anthropic. Your existing code stays exactly the same.

OpenAI compatible Anthropic compatible One line change

Memory Router

api.retaindb.com/v1/router

Injects context · forwards request

OpenAI

gpt-4o, gpt-5

Anthropic

claude-3-7, claude-4

Gemini

gemini-2.0, 2.5

Any OpenAI-compatible

Ollama, Groq, etc.

OAI

OpenAI

GPT-4o · GPT-5

ANT

Anthropic

Claude 3.7 · 4

GEM

Gemini

2.0 · 2.5 Pro

GRQ

Groq

Llama · Mixtral

++

Any LLM

OpenAI-compatible API

What does it actually cost?

The free tier is real — 10,000 memory operations per month, no credit card required. Most teams stay on it through early product. When you need more, paid plans start at $20/month. You'll know when you've outgrown it.

How long does it take to set up?

Under 30 minutes from signup to your AI remembering its first user. Run our setup wizard, connect your knowledge source, add one function call to your existing product. Most of that time is reading the docs.

Is my data safe?

All data is encrypted in storage and in transit. Every project is fully isolated — there's no way for one customer's data to reach another. If you need stricter control, we support self-hosted deployments on your own infrastructure.

Do my users' data stay private?

Yes. Memory is stored per user and only retrieved for that user. You control what gets stored, what gets deleted, and how long it's retained. Users can have their memory wiped at any time.

Will it work with our existing agent?

Yes — RetainDB works with any agent regardless of which model or framework you use. OpenAI, Anthropic, Gemini, LangChain, or anything else. You don't change how your agent works, you just add memory to it.

How is this different from building it ourselves?

Building persistent memory correctly — deduplication, semantic retrieval, multi-user isolation, token management — takes most teams 4–8 weeks. RetainDB is that layer, already built and tested at scale. Your team ships the feature this week, not next quarter.

## Your users deserve an AI

_that remembers them._

The difference between an agent people tolerate and one they love is often this simple: does it remember them? RetainDB is the fastest way to answer that question with yes — for every user, from the very first session.

Most teams go from zero to production memory in under 30 minutes. Free to start. No infrastructure to manage.

88% preference recall·0% hallucination rate·<40ms retrieval·SOC 2 ready

Explore by intent

## Start with the page that matches your search

These are the pages at the center of the new memory, context, and comparison cluster.
