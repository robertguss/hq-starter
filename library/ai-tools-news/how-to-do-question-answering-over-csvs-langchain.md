---
tags:
  - library
title: "How to do question answering over CSVs | 🦜️🔗 LangChain"
url: "https://python.langchain.com/docs/how_to/sql_csv/"
company: [personal]
topics: []
created: 2025-08-18
source_type: raindrop
raindrop_id: 1303899314
source_domain: "python.langchain.com"
source_type_raindrop: article
collection: "AI Tools & News"
collection_id: 69284314
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

LLMs are great for building question-answering systems over various types of data sources. In this section we'll go over how to build Q&A systems over data stored in a CSV file(s). Like working with SQL databases, the key to working with CSV files is to give an LLM access to tools for querying and interacting with the data. The two main ways to do this are to either:

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: LangChain overview - Docs by LangChain

URL Source: https://python.langchain.com/docs/how_to/sql_csv/

Markdown Content:
# LangChain overview - Docs by LangChain

[Skip to main content](https://python.langchain.com/docs/how_to/sql_csv/#content-area)

Join us May 13th & May 14th at Interrupt, the Agent Conference by LangChain. [Buy tickets >](https://interrupt.langchain.com/)

[Docs by LangChain home page![Image 1: light logo](https://mintcdn.com/langchain-5e9cc07a/nQm-sjd_MByLhgeW/images/brand/langchain-docs-dark-blue.png?fit=max&auto=format&n=nQm-sjd_MByLhgeW&q=85&s=5babf1a1962208fd7eed942fa2432ecb)![Image 2: dark logo](https://mintcdn.com/langchain-5e9cc07a/nQm-sjd_MByLhgeW/images/brand/langchain-docs-light-blue.png?fit=max&auto=format&n=nQm-sjd_MByLhgeW&q=85&s=0bcd2a1f2599ed228bcedf0f535b45b1)](https://python.langchain.com/)![Image 3: https://mintlify.s3.us-west-1.amazonaws.com/langchain-5e9cc07a/images/brand/langchain-icon.png](https://mintlify.s3.us-west-1.amazonaws.com/langchain-5e9cc07a/images/brand/langchain-icon.png)Open source

Search...

Ctrl K

*   [Ask AI](https://chat.langchain.com/)
*   [GitHub](https://github.com/langchain-ai)
*   [Try LangSmith](https://smith.langchain.com/)
*   [Try LangSmith](https://smith.langchain.com/)

Search...

Navigation

LangChain overview

[Deep Agents](https://python.langchain.com/oss/python/deepagents/overview)[LangChain](https://python.langchain.com/oss/python/langchain/overview)[LangGraph](https://python.langchain.com/oss/python/langgraph/overview)[Integrations](https://python.langchain.com/oss/python/integrations/providers/overview)[Learn](https://python.langchain.com/oss/python/learn)[Reference](https://python.langchain.com/oss/python/reference/overview)[Contribute](https://python.langchain.com/oss/python/contributing/overview)

Python

*   [Overview](https://python.langchain.com/oss/python/langchain/overview)

##### Get started

*   [Install](https://python.langchain.com/oss/python/langchain/install)
*   [Quickstart](https://python.langchain.com/oss/python/langchain/quickstart)
*   [Changelog](https://docs.langchain.com/oss/python/releases/changelog)
*   [Philosophy](https://python.langchain.com/oss/python/langchain/philosophy)

##### Core components

*   [Agents](https://python.langchain.com/oss/python/langchain/agents)
*   [Models](https://python.langchain.com/oss/python/langchain/models)
*   [Messages](https://python.langchain.com/oss/python/langchain/messages)
*   [Tools](https://python.langchain.com/oss/python/langchain/tools)
*   [Short-term memory](https://python.langchain.com/oss/python/langchain/short-term-memory)
*   [Streaming](https://python.langchain.com/oss/python/langchain/streaming)
*   [Structured output](https://python.langchain.com/oss/python/langchain/structured-output)

##### Middleware

*   [Overview](https://python.langchain.com/oss/python/langchain/middleware/overview)
*   [Prebuilt middleware](https://python.langchain.com/oss/python/langchain/middleware/built-in)
*   [Custom middleware](https://python.langchain.com/oss/python/langchain/middleware/custom)

##### Frontend

*   [Overview](https://python.langchain.com/oss/python/langchain/frontend/overview)
*   Patterns  
*   Integrations  

##### Advanced usage

*   [Guardrails](https://python.langchain.com/oss/python/langchain/guardrails)
*   [Runtime](https://python.langchain.com/oss/python/langchain/runtime)
*   [Context engineering](https://python.langchain.com/oss/python/langchain/context-engineering)
*   [Model Context Protocol (MCP)](https://python.langchain.com/oss/python/langchain/mcp)
*   [Human-in-the-loop](https://python.langchain.com/oss/python/langchain/human-in-the-loop)
*   Multi-agent  
*   [Retrieval](https://python.langchain.com/oss/python/langchain/retrieval)
*   [Long-term memory](https://python.langchain.com/oss/python/langchain/long-term-memory)

##### Agent development

*   [LangSmith Studio](https://python.langchain.com/oss/python/langchain/studio)
*   Test  
*   [Agent Chat UI](https://python.langchain.com/oss/python/langchain/ui)

##### Deploy with LangSmith

*   [Deployment](https://python.langchain.com/oss/python/langchain/deploy)
*   [Observability](https://python.langchain.com/oss/python/langchain/observability)

On this page

*   [Create an agent](https://python.langchain.com/docs/how_to/sql_csv/#create-an-agent)
*   [Core benefits](https://python.langchain.com/docs/how_to/sql_csv/#core-benefits)

# LangChain overview

Copy page

LangChain is an open source framework with a prebuilt agent architecture and integrations for any model or tool—so you can build agents that adapt as fast as the ecosystem evolves

Copy page

LangChain is the easy way to start building completely custom agents and applications powered by LLMs. With under 10 lines of code, you can connect to OpenAI, Anthropic, Google, and [more](https://python.langchain.com/oss/python/integrations/providers/overview). LangChain provides a prebuilt agent architecture and model integrations to help you get started quickly and seamlessly incorporate LLMs into your agents and applications.

**LangChain vs. LangGraph vs. Deep Agents**If you are looking to build an agent, we recommend you start with [Deep Agents](https://python.langchain.com/oss/python/deepagents/overview) which comes “batteries-included”, with modern features like automatic compression of long conversations, a virtual filesystem, and subagent-spawning for managing and isolating context.Deep Agents are implementations of LangChain [agents](https://python.langchain.com/oss/python/langchain/agents). If you don’t need these capabilities or would like to customize your own for your agents and autonomous applications, start with LangChain.Use [LangGraph](https://python.langchain.com/oss/python/langgraph/overview), our low-level agent orchestration framework and runtime, when you have more advanced needs that require a combination of deterministic and agentic workflows and heavy customization.

LangChain [agents](https://python.langchain.com/oss/python/langchain/agents) are built on top of LangGraph in order to provide durable execution, streaming, human-in-the-loop, persistence, and more. You do not need to know LangGraph for basic LangChain agent usage.We recommend you use LangChain if you want to quickly build agents and autonomous applications.
## [​](https://python.langchain.com/docs/how_to/sql_csv/#create-an-agent)

 Create an agent

```
# pip install -qU langchain "langchain[anthropic]"
from langchain.agents import create_agent

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

agent = create_agent(
    model="anthropic:claude-sonnet-4-6",
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

# Run the agent
agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
)
```

See the [Installation instructions](https://python.langchain.com/oss/python/langchain/install) and [Quickstart guide](https://python.langchain.com/oss/python/langchain/quickstart) to get started building your own agents and applications with LangChain.

Use [LangSmith](https://python.langchain.com/langsmith/home) to trace requests, debug agent behavior, and evaluate outputs. Set `LANGSMITH_TRACING=true` and your API key to get started.

## [​](https://python.langchain.com/docs/how_to/sql_csv/#core-benefits)

 Core benefits

## [Standard model interface Different providers have unique APIs for interacting with models, including the format of responses. LangChain standardizes how you interact with models so that you can seamlessly swap providers and avoid lock-in. Learn more](https://python.langchain.com/oss/python/langchain/models)

## [Easy to use, highly flexible agent LangChain’s agent abstraction is designed to be easy to get started with, letting you build a simple agent in under 10 lines of code. But it also provides enough flexibility to allow you to do all the context engineering your heart desires. Learn more](https://python.langchain.com/oss/python/langchain/agents)

[![Image 4: https://mintcdn.com/langchain-5e9cc07a/nQm-sjd_MByLhgeW/images/brand/langgraph-icon.png?fit=max&auto=format&n=nQm-sjd_MByLhgeW&q=85&s=b997e1a7487d507a36556eedbfd99f81](https://mintcdn.com/langchain-5e9cc07a/nQm-sjd_MByLhgeW/images/brand/langgraph-icon.png?fit=max&auto=format&n=nQm-sjd_MByLhgeW&q=85&s=b997e1a7487d507a36556eedbfd99f81) ## Built on top of LangGraph LangChain’s agents are built on top of LangGraph. This allows us to take advantage of LangGraph’s durable execution, human-in-the-loop support, persistence, and more. Learn more](https://python.langchain.com/oss/python/langgraph/overview)

[![Image 5: https://mintcdn.com/langchain-5e9cc07a/nQm-sjd_MByLhgeW/images/brand/observability-icon-dark.png?fit=max&auto=format&n=nQm-sjd_MByLhgeW&q=85&s=ccbc183bca2a5e4ca78d30149e3836cc](https://mintcdn.com/langchain-5e9cc07a/nQm-sjd_MByLhgeW/images/brand/observability-icon-dark.png?fit=max&auto=format&n=nQm-sjd_MByLhgeW&q=85&s=ccbc183bca2a5e4ca78d30149e3836cc) ## Debug with LangSmith Gain deep visibility into complex agent behavior with visualization tools that trace execution paths, capture state transitions, and provide detailed runtime metrics. Learn more](https://python.langchain.com/langsmith/observability)

* * *

[Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/overview.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).

[Connect these docs](https://python.langchain.com/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.

Was this page helpful?

Yes No

[Install LangChain Next](https://python.langchain.com/oss/python/langchain/install)

Ctrl+I

[Docs by LangChain home page![Image 6: light logo](https://mintcdn.com/langchain-5e9cc07a/nQm-sjd_MByLhgeW/images/brand/langchain-docs-dark-blue.png?fit=max&auto=format&n=nQm-sjd_MByLhgeW&q=85&s=5babf1a1962208fd7eed942fa2432ecb)![Image 7: dark logo](https://mintcdn.com/langchain-5e9cc07a/nQm-sjd_MByLhgeW/images/brand/langchain-docs-light-blue.png?fit=max&auto=format&n=nQm-sjd_MByLhgeW&q=85&s=0bcd2a1f2599ed228bcedf0f535b45b1)](https://python.langchain.com/)

[github](https://github.com/langchain-ai)[x](https://x.com/LangChain)[linkedin](https://www.linkedin.com/company/langchain)[youtube](https://www.youtube.com/@LangChain)

Resources

[Forum](https://forum.langchain.com/)[Changelog](https://changelog.langchain.com/)[LangChain Academy](https://academy.langchain.com/)[Contact Sales](https://www.langchain.com/contact-sales)

Company

[Home](https://langchain.com/)[Trust Center](https://trust.langchain.com/)[Careers](https://langchain.com/careers)[Blog](https://blog.langchain.com/)

[github](https://github.com/langchain-ai)[x](https://x.com/LangChain)[linkedin](https://www.linkedin.com/company/langchain)[youtube](https://www.youtube.com/@LangChain)

## Chat LangChain

[](https://chat.langchain.com/ "Open chat.langchain.com in a new tab")
