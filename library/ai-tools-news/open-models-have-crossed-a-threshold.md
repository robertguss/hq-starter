---
tags:
  - library
title: "Open Models have crossed a threshold"
url: "https://blog.langchain.com/open-models-have-crossed-a-threshold/?utm_campaign=128991943-General%20-%20Corporate%20News&utm_medium=email&_hsmi=26404659&utm_content=26404659&utm_source=hs_email"
company: [personal]
topics: []
created: 2026-04-05
source_type: raindrop
raindrop_id: 1672648498
source_domain: "blog.langchain.com"
source_type_raindrop: article
collection: "AI Tools & News"
collection_id: 69284314
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

💡TL;DR: Open models like GLM-5 and MiniMax M2.7 now match closed frontier models on core agent tasks — file operations, tool use, and instruction following — at a fraction of the cost and latency. Here's what our evals show and how to start using them in Deep Agents.

Over the

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: Open Models have crossed a threshold

URL Source: https://blog.langchain.com/open-models-have-crossed-a-threshold/?_hsmi=26404659

Markdown Content:
![Image 1](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d77bf97ddb73352609004d_72.webp)

## Key Takeaways

**TL;DR:** Open models like GLM-5 and MiniMax M2.7 now match closed frontier models on core agent tasks — file operations, tool use, and instruction following — at a fraction of the cost and latency. Here's what our evals show and how to start using them in Deep Agents.

Over the past few weeks, we’ve been running open weight Large Language Models through [**Deep Agents**](https://github.com/langchain-ai/deepagents?ref=blog.langchain.com) harness evaluations, and the initial results show they are a viable option to use instead of, and alongside, closed frontier models. GLM-5 ([**z.ai**](http://z.ai/?ref=blog.langchain.com)) and [**MiniMax**](https://www.minimax.io/models/text/m27?ref=blog.langchain.com) M2.7 each score similarly to closed frontier models on core agent tasks such as file operations, tool use, and instruction following.

This isn’t surprising if you’ve been following open model progress via the large set of open benchmarks such as [**SWE-Rebench**](https://swe-rebench.com/?ref=blog.langchain.com) and [**Terminal Bench 2.0**](https://www.tbench.ai/leaderboard/terminal-bench/2.0?ref=blog.langchain.com). Tool calling is reliable and instruction following is consistent. For developers deploying agents in production, open models now offer a level of consistency and predictability that makes real-world workflows much more viable.

## Why open models

When exploring open models, builders and customers tend to focus on a few key factors: **cost, latency,** and **task performance**.

In the limit, it would be great to use the smartest frontier model at the highest reasoning level for every task. In practice, two constraints make that unworkable: cost and latency. Closed frontier models can run 8–10x more expensive for high-throughput workloads, and they're often too slow for the response times users expect in interactive products.

| Model | Type | Input ($/M tokens) | Output ($/M tokens) |
| --- | --- | --- | --- |
| Claude Opus 4.6 (Anthropic) | Closed | $5.00 | $25.00 |
| Claude Sonnet 4.6 (Anthropic) | Closed | $3.00 | $15.00 |
| GPT-5.4 (OpenAI) | Closed | $2.50 | $15.00 |
| GLM-5 (Baseten) | Open | $0.95 | $3.15 |
| MiniMax M2.7 (OpenRouter) | Open | $0.30 | $1.20 |

_To put the pricing in context: an application outputting 10M tokens/day costs roughly $250/day on Opus 4.6 versus ~$12/day for MiniMax M2.7. That's about a $87k annual difference._

Open models tend to be smaller than closed frontier models, and can be accelerated on specialized inference infrastructure — providers like [**Groq**](https://groq.com/?ref=blog.langchain.com), [**Fireworks**](https://fireworks.ai/?ref=blog.langchain.com), and [**Baseten**](https://www.baseten.co/?ref=blog.langchain.com) optimize for latency and throughput far beyond what most teams could achieve on their own. [**OpenRouter data**](https://openrouter.ai/z-ai/glm-5/performance?ref=blog.langchain.com) show GLM-5 on Baseten averaging 0.65s latency and 70 tokens/second, compared to 2.56s and 34 tokens/second for Claude Opus 4.6. For latency-sensitive products, that gap is hard to engineer around.

## How we evaluated

We've written about our eval methodology in depth in [**How we build evals for Deep Agents**](https://blog.langchain.com/how-we-build-evals-for-deep-agents/). We run evals using hosted inference providers, but Deep Agents can be run using fully local and private models via Ollama, vLLM, etc.

For open models, we ran seven eval categories: file operations, tool use, retrieval, conversation, memory, summarization, and “unit tests”. These cover tasks that exercise fundamentals: can the model reliably call tools, follow structured instructions, and operate on files? These are the capabilities that gate whether a model is usable in an agentic harness at all.

Each eval case defines success assertions (hard-fail checks that determine correctness) and efficiency assertions (soft checks that measure how the model got there). We report four metrics:

*   **Correctness** — the fraction of tests the model solved: `passed / total`. A score of 0.68 means 68% of test cases were solved correctly. This is the primary quality signal.
*   **Solve rate** — a combined measure of accuracy and speed. For each test, we compute `expected_steps / wall_clock_seconds`; failed tests contribute zero. The final score is the average across all tests. Higher is better — a model that solves tasks both correctly and quickly scores highest.
*   **Step ratio** — how many agentic steps the model actually took compared to how many we expected, aggregated across all tests: `total_actual_steps / total_expected_steps`. A value of 1.0 means the model used exactly the expected number of steps. Above 1.0 means it needed more (less efficient); below 1.0 means it needed fewer steps than initially expected.
*   **Tool call ratio** — same idea as step ratio, but counting individual tool calls instead of steps. 1.0 is on-budget, above is over-budget, below is under-budget.

Step ratio and tool call ratio are _efficiency_ metrics. They don't affect whether a test passes, but they reveal how economically a model reaches the answer. A model that solves a task in 2 steps instead of the expected 5 is both correct _and_ efficient.

## Findings from our evals

These are early results; we’re actively maintaining and expanding our eval set. You can view recent runs in realtime both [**in our GitHub repo**](https://github.com/langchain-ai/deepagents/actions/workflows/evals.yml?ref=blog.langchain.com) and at [**this shared LangSmith project**](https://smith.langchain.com/public/d4245855-4e15-48dc-a39d-8631780a9aeb/d?ref=blog.langchain.com).

### **Open models**

[**View CI run**](https://github.com/langchain-ai/deepagents/actions/runs/23872647281?ref=blog.langchain.com) (click model names to view individual evals)

| Model | Correctness | Passed | Solve Rate | Step Ratio | Tool Call Ratio |
| --- | --- | --- | --- | --- | --- |
| baseten:zai-org/GLM-5 | 0.64 | 94 of 138 | 1.17 | 1.02 | 1.06 |
| ollama:minimax-m2.7 | 0.57 | 85 of 138 | 0.27 | 1.02 | 1.04 |

![Image 2](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d77e082ccb246b42da75e1_image.png)

Per-category correctness:

| Model | Conversation | File Ops | Memory | Retrieval | Summarization | Tool Use | Unit Test |
| --- | --- | --- | --- | --- | --- | --- | --- |
| baseten:zai-org/GLM-5 | 0.38 | 1 | 0.44 | 1 | 0.6 | 0.82 | 1 |
| ollama:minimax-m2.7:cloud | 0.14 | 0.92 | 0.38 | 0.8 | 0.6 | 0.87 | 0.92 |

### Frontier models

[**View CI run**](https://github.com/langchain-ai/deepagents/actions/runs/23871631742?ref=blog.langchain.com) (click model names to view individual evals)

| Model | Correctness | Passed | Solve Rate | Step Ratio | Tool Call Ratio |
| --- | --- | --- | --- | --- | --- |
| anthropic:claude-opus-4-6 | 0.68 | 100 of 138 | 0.38 | 0.99 | 1.02 |
| google_genai:gemini-3.1-pro-preview | 0.65 | 96 of 138 | 0.26 | 0.99 | 1.01 |
| openai:gpt-5.4 | 0.61 | 91 of 138 | 0.61 | 1.05 | 1.15 |

![Image 3](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d77e082ccb246b42da75de_2image.png)

Per-category correctness:

| Model | Conversation | File Ops | Memory | Retrieval | Summarization | Tool Use | Unit Test |
| --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic:claude-opus-4-6 | 0.05 | 1 | 0.67 | 1 | 1 | 0.87 | 1 |
| google_genai:gemini-3.1-pro-preview | 0.24 | 0.92 | 0.62 | 1 | 0.8 | 0.79 | 0.92 |
| openai:gpt-5.4 | 0.29 | 1 | 0.44 | 1 | 0.8 | 0.76 | 1 |

‍_For each model, we opt to use the provider’s default thinking level._‍_For Gemini 3+, this is `high`_‍_For OpenAI, this is `medium`_‍_For Claude, this is without extended thinking_

#### **DIY: Run Deep Agent evals locally**

Our CI runs the same evaluation suite across 52 models organized into groups — including an `open` group (`baseten:zai-org/GLM-5`, `ollama:minimax-m2.7:cloud`, `ollama:nemotron-3-super`) that runs on every eval workflow. You can target any model group:

Run evals against all open models`: pytest tests/evals --model-group open`

Run against a specific model: `pytest tests/evals --model baseten:zai-org/GLM-5`

This makes it straightforward to compare open models against each other and against closed frontier models on the same tasks, using the same grading criteria.

## Using open models in Deep Agents SDK

Swapping to an open model is a one-line change:

GLM-5:

```
# pip install langchain-baseten
from deepagents import create_deep_agent
 
agent = create_deep_agent(model="baseten:zai-org/GLM-5")
```

MiniMax M2.7:

```
# pip install langchain-openrouter
from deepagents import create_deep_agent
 
agent = create_deep_agent(model="openrouter:minimax/minimax-m2.7")
```

That's it. The harness handles the rest — it detects the model's context window size, disables unsupported modalities, and injects the right identity into the system prompt so the agent knows what it's working with.

The same open model is often available through multiple providers. Pick the one that matches your constraints. For example, GLM-5 is available as `baseten:zai-org/GLM-5`, `fireworks:fireworks/glm-5`, or `ollama:glm-5` for self-hosted. Same model, same harness, different infrastructure.

LangChain provides support for the most popular open model providers. The providers we have tested for this release are: Baseten, Fireworks, Groq, OpenRouter, and Ollama (cloud).

### Harness-level adjustments for your model

Open models have different context windows, different tool-calling formats, and different failure modes than closed frontier models. The Deep Agents harness absorbs these differences so you don't have to:

*   **Model identity injection** — the system prompt is patched at runtime with the model's name, provider, context limit, and supported modalities. The agent knows what it is and what it can do.
*   **Context management** — compression, offloading, and summarization thresholds adapt to the model's actual context window, not a hardcoded default. A model with a 4K context gets more aggressive compaction than Opus with 1M.

### Deep Agents CLI

Each model is also available in the Deep Agents CLI. The [**Deep Agents CLI**](https://github.com/langchain-ai/deepagents/tree/main/libs/cli?ref=blog.langchain.com) is our open-source coding agent and alternative to Claude Code.

In addition to all the capabilities in Deep Agents SDK, the CLI supports **Runtime model swapping.** We introduced a new middleware ([**`ConfigurableModelMiddleware`**](https://github.com/langchain-ai/deepagents/blob/8be4a2ee3878a3e15c15d56fd64ba8db248a6328/libs/cli/deepagents_cli/configurable_model.py?ref=blog.langchain.com#L145) ) to enable switching models mid-session without restarting the agent. This enables patterns like using a frontier model for planning and an open model for execution.

You can switch models mid-session with the `/model` slash command. This enables patterns like starting a task with a frontier model for planning, then switching to a cheaper open model for execution.

## What’s next

Some things we’re excited to share soon:

*   Documenting harness tuning patterns for specific open model families
*   Testing multi-model subagent configurations (ex: frontier closed model orchestrator + open model subagents)

Open models work for agents today. We want to show the design patterns that help us engineer a good harness and build targeted evals that measure what matters for your task.

[**Deep Agents**](https://github.com/langchain-ai/deepagents?ref=blog.langchain.com) is open source. Try it with your preferred open model and come build great evals and agents with us.

### Related content

![Image 4](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e127982faf6124b586b6e4_82.png)

Agent Architecture

Deep Agents

Open Source

#### Running Subagents in the Background

![Image 5](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e12735c02bb07c894a067a_hunter-lovell.png)

![Image 6](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e12775881c2a7fc9aba41e_colin-francis.png)

H. Lovell,

C. Francis

April 16, 2026

![Image 7](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)

4

min

![Image 8](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dfc55eabcedb7ed1755cf9_79.png)

Deep Agents

Engineering

#### How We Made Our Docs Test Themselves

![Image 9](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dfc520e7b284e657a1faba_naomi-pentrel.png)

Naomi Pentrel

April 15, 2026

![Image 10](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)

3

min

![Image 11](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dce8678d86f0b97b4bfb03_69755ea1ee1a0520c04789deb8a34ccc.png)

Deep Agents

#### Deep Agents Deploy: an open alternative to Claude Managed Agents

![Image 12](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcee60745f0e15b18ad4d5_sydney-runkle.png)

Sydney Runkle

April 9, 2026

![Image 13](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)

4

min

![Image 14](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)

### S

e

e

w

h

a

t

y

o

u

r

a

g

e

n

t

i

s

r

e

a

l

l

y

d

o

i

n

g

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.
