---
tags:
  - library
title: "The Claude Code SDK and the Birth of HaaS (Harness as a Service) | vtrivedy"
url: "https://www.vtrivedy.com/posts/claude-code-sdk-haas-harness-as-a-service?ref=blog.langchain.com"
company: [personal]
topics: []
created: 2026-04-10
source_type: raindrop
raindrop_id: 1679345670
source_domain: "vtrivedy.com"
source_type_raindrop: article
collection: "AI Tools & News"
collection_id: 69284314
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

As tasks require more autonomous behavior, we're seeing a shift from LLM APIs to Harness APIs. Explore how Claude Code's SDK enables rapid agent development through HaaS (Harness as a Service).

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: The Claude Code SDK and the Birth of HaaS (Harness as a Service) | vtrivedy

URL Source: https://www.vtrivedy.com/posts/claude-code-sdk-haas-harness-as-a-service?ref=blog.langchain.com

Published Time: 2025-09-23T14:00:00.000Z

Markdown Content:
As tasks require more autonomous behavior from agents, the core primitive for working with AI is shifting from the **LLM API (chat style endpoints)** to the **Harness API (customizable runtimes)**. I call this **Harness as a Service (HaaS)**. Quickly build, customize, and share agents via a rich ecosystem of agent harnesses. Today we’ll cover how to customize harnesses to build usable agents quickly + the future of agent development in a world of open harnesses.

`client.chat.completions.create() --> client.responses.create() --> agent.query()`

> **Working Definition — Agent Harness:** External set of functionality to enhance a model’s runtime execution. Examples include (1) conversation & context management, (2) a tool invocation layer (MCP/SDK tools), (3) permissions, (4) session & file-system state, (5) loop control & error handling, (6) basic observability/telemetry.

> **Note**: LLM products like the ChatGPT web app or iOS app already wrap models inside their own harness for safety, tool use, etc. But using LLM APIs today requires you to wrap the model inside your own harness. This is changing with Claude Code’s SDK where their existing harness is easily extendable with your own prompts, tools, context, permissions. Users get a customizable agent runtime in a box.

Here are the 3 main ideas we’ll cover:

1.   Why Claude Code’s SDK is currently the best, batteries included way to build and expose a usable agent.
2.   Your job as a builder is to obsessively customize the harness for your task. (with examples)
3.   The future of agentic development via harnesses and the promises of an open harness ecosystem.

In a future blog post we’ll dive into a custom project implementing the details and advanced features of the Claude Code SDK beyond the example shared below, let’s dive in.

## Batteries Included=Speed=Your Agent Actually Exists[](https://www.vtrivedy.com/posts/claude-code-sdk-haas-harness-as-a-service?ref=blog.langchain.com#batteries-includedspeedyour-agent-actually-exists)

The agent building landscape is noisy: agents, frameworks, tools, MCP, Codex, Claude Code, Cursor CLI, you get it. But take a step back. Unless you’re an agent framework company, the goal is to solve your actual problem, not build agent infra. An (in hindsight) obvious but often ignored fact for teams considering an agent for their problem:

> Good agent building is an exercise in iteration. You can’t do iterations if you don’t have a v0.1. A batteries included setup gets your agent in the hands of your internal team. Then you can edit in a loop.

### Why Care About this? Agent Building is an Exercise in Momentum[](https://www.vtrivedy.com/posts/claude-code-sdk-haas-harness-as-a-service?ref=blog.langchain.com#why-care-about-this-agent-building-is-an-exercise-in-momentum)

In agent building, tooling/capabilities can change overnight so you which is great for testing that killer feature that just wouldn’t work before. But to succeed here, you need to be able to test internally (and externally) fast. The Claude Code SDK reduces your TTFF (Time to First Feedback) by serving as your agent quickstart, the `create-react-app --> create-agent-app` if you will.

Frameworks free up your mental capacity to focus on the intricacies of your problem. To move quickly, don’t build everything from scratch and offload some work to existing tooling that can get you up and running while having strong customization for the future. That’s precisely the type of offloading you get in [Claude Code SDK](https://docs.claude.com/en/docs/claude-code/sdk/sdk-overview). I’m not going to list out every feature, their docs are solid, here’s an overview snippet.

> Built on top of the agent harness that powers Claude Code, the Claude Code SDK provides all the building blocks you need to build production-ready agents. Taking advantage of the work we’ve done on Claude Code including: -**Context Management**: Automatic compaction and context management to ensure your agent doesn’t run out of context. -**Rich tool ecosystem**: File operations, code execution, web search, and MCP extensibility -**Advanced permissions**: Fine-grained control over agent capabilities -**Production essentials**: Built-in error handling, session management, and monitoring -**Optimized Claude integration**: Automatic prompt caching and performance optimizations

As you see from their docs, the Claude Code SDK gives you a very usable base set of agent primitives, this is your “harness”. These built-ins save you days to weeks of work, but more importantly, your team is now laser focused on your problem.

Ok so then what’s your job? **Customization with care.**

## Harness Customization, the Approach to Build Any Agent[](https://www.vtrivedy.com/posts/claude-code-sdk-haas-harness-as-a-service?ref=blog.langchain.com#harness-customization-the-approach-to-build-any-agent)

![Image 1: Customize Claude Code&#x27;s Harness to build and expose any agent](https://www.vtrivedy.com/_astro/cc_harness_updated.DHcnsFFo_Z1WNa8e.webp)_Mental Model of customizing a harness and making it usable with the Claude Code SDK_

Every task requires a certain set of tools and instructions, your job is to customize these inputs: **System Prompt, Tools/MCP, Context, Subagents.** Once you have something, run it and observe what your agent is doing, this is your learning signal. Improve your inputs until you get good enough outputs. Here are some details and tips for customizing each part of the harness.

### 1. System Prompt[](https://www.vtrivedy.com/posts/claude-code-sdk-haas-harness-as-a-service?ref=blog.langchain.com#1-system-prompt)

This is the starting place for telling Claude Code everything about your problem, the goal, the environment it will operate in, the tools it can use, instructions and guidelines to follow, rules on formatting, how to interact with the user, etc.

Spend a lot of time here! Prompt engineering is as alive as ever for guiding model behavior. Investing time in your system prompt is the best cost-benefit you’ll get in your agent building journey.

Here’s a template you can use to start but prompt design is an art. You can see a longer example that worked well [here](https://github.com/vtrivedy/claude-banana-story-agent), it’s a project I released with Claude Code’s SDK to autonomously create storybooks from user topics (similar to [Gemini’s Storybook Feature](https://gemini.google/overview/storybook/)).

```
Goal/Persona: "You are "Story Director," an autonomous storybook creation agent that transforms ANY user input into complete illustrated storybooks..."
Environment/Tools Available: ...
Must Follow Instructions: ...
Examples + Tool Usage: ...
Final Checklist: ...
```

Claude Code provides two ways of editing the system prompt: `appendSystemPrompt` and `custom_system_prompt` to add to Claude’s existing system prompt or completely rewrite with your own.

### 2. Tools/MCPs[](https://www.vtrivedy.com/posts/claude-code-sdk-haas-harness-as-a-service?ref=blog.langchain.com#2-toolsmcps)

Claude Code comes with built in tools (web search, grep, file read/write, etc), but you’ll need to define custom logic for tools specific to your use case (ex: image editing API, Slack integration, etc). You don’t have to build all of this from scratch, use existing toolsets packaged as MCPs on platforms like [Smithery](https://smithery.ai/).

For tool design, think deeply 3 things:

1.   What does the agent need to do so it can accomplish the goal I set for it. Is there a tool for it?
2.   Is it clear to the agent when to use the tools in both my system prompt and tool description?
3.   Can I reduce the surface area for error by combining several tools into more atomic outcomes? Ex: `generate_image` —>`generate_page_content`

Anthropic’s blog on [Writing Effective Tools for Agents](https://www.anthropic.com/engineering/writing-tools-for-agents) and Vercel’s blog on [MCP for LLMs not devs](https://vercel.com/blog/the-second-wave-of-mcp-building-for-llms-not-developers) are two excellent resources on tool/MCP design.

### 3. Context[](https://www.vtrivedy.com/posts/claude-code-sdk-haas-harness-as-a-service?ref=blog.langchain.com#3-context)

There’s a lot of [new content on Context Engineering](https://www.philschmid.de/context-engineering). The better context you give your agent, the better it will perform. Some examples for useful context are:

*   **Code documentation and snippets:** Save these as markdown files in the filesystem. DO NOT make the agent search the web for something you already know it will need. It can refer to these snippets as needed.
*   **Memory/User Personalization:** Should your agent behave differently depending on your user? The simplest way of doing this is injecting this info into a ‘user_info.md’ file or a more elaborate memory service.

Rule of thumb: keep all crucial context in your system prompt, especially for the first version. Keep all other helpful context in markdown files and tell your agent when and how to use their content

### 4. Subagents (optional)[](https://www.vtrivedy.com/posts/claude-code-sdk-haas-harness-as-a-service?ref=blog.langchain.com#4-subagents-optional)

For an agent’s first version, I strongly suggest testing everything in a single agent thread to reduce complexity and quickly get your agent into the world. Sub-agents can be useful for 2 use cases initially: **Specialization** and **Parallelization**.

Subagents are defined via YAML in `.claude/agents/{subagent_name}.md`. For example:

```
---
name: character-consistency-checker
description: Expert visual inspector.  Can tell if the character in the generated image matches the character reference image.
tools: Read, Grep, Glob, Bash
---
Your task is to make sure the character in the story matches the reference character.  You will read in 2 images, the character.png and the page.png file.  Then you will output True or False along with a reason for your decision

Make sure to check for the consistency of the size, color, art style, and other factors that would break the flow and overall vibe of the story
```

## HaaS, The Future of Building Custom Agents[](https://www.vtrivedy.com/posts/claude-code-sdk-haas-harness-as-a-service?ref=blog.langchain.com#haas-the-future-of-building-custom-agents)

We’re moving rapidly towards a world where builders create custom harnesses and users plug into them to edit further or use as a product. We’re already starting to see this movement from companies like [bolt](https://x.com/boltdotnew/status/1965448120558559683) who helped kick off the vibe coding revolution. They’re using Codex and Claude Code in their app building product directly and probably did a ton of harness customization to get the product to work well. There’s a massive opportunity for companies to start using existing harnesses as application primitives to build their product experiences around. My bet is that in the next 6 months, the majority of user facing AI products will be using an existing agent harness as their core user interaction pattern.

For builders deeply obsessed with a problem, all of this is a good thing. They can tap into a customizable layer of intelligence that continues to improve while focusing time on user feedback, creating better agent inputs, and engineering more complex and reliable experiences.

The Claude Code SDK won’t be the only game in town, it’s just the most mature today to build on. There’s already great work being done by OpenAI Codex, Gemini CLI, Cursor CLI, Amp, and more. But the goal is clear, everyone wants to become the harness that users plug into for intelligence. Opportunities to do this will revolve around great DX and out of the box intelligence.

### The Open Harness Thesis[](https://www.vtrivedy.com/posts/claude-code-sdk-haas-harness-as-a-service?ref=blog.langchain.com#the-open-harness-thesis)

If you’re excited by this post and releases like [Prime Intellects Environment Hub](https://www.primeintellect.ai/blog/environments), you probably share the vision of a future where many harnesses are open-source so developers can extend them. The original models and their harnesses may not be open source but everything to build the product experience may be. That future is even more exciting because it’s very possible that the base models that drive frontier harnesses will one day also be open source. **This is the Open App Store for Agents.**

Harnesses commodify “agent infra” and shift your effort where it compounds: prompts, tools, and context tuned to your domain. Whether you call it HaaS or just “building agents,” the Claude Code SDK is the easiest harness to build on today. Start from that baseline, specialize aggressively, and improve your agent from its measured outputs.

If this future excites you, please reach out, we’re building here. Until next time, happy harness building.
