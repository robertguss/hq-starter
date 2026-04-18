---
tags:
  - library
title: "Claude Code: An analysis | Notion"
url: "https://southbridge-research.notion.site/claude-code-an-agentic-cleanroom-analysis"
company: [personal]
topics: []
created: 2025-10-06
source_type: raindrop
raindrop_id: 1372661968
source_domain: "southbridge-research.notion.site"
source_type_raindrop: link
collection: "AI Tools & News"
collection_id: 69284314
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

Why Claude Code Matters

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: Claude Code: An analysis

URL Source: https://southbridge-research.notion.site/claude-code-an-agentic-cleanroom-analysis

Markdown Content:
🐸

💡

I should note that this is not a true decompilation or reverse engineering attempt in any real sense, more of an homage to the wonderful work done by the Claude team. None of the examples provided are guaranteed to be in Claude Code (or directly derived/copied from source) - the primary intent is didactic value in learning new ways to orchestrate AI agents.

(Quick note: I appreciate everyone that’s pointed out hallucinations, but these were left in intentionally as artifacts of the generation process. The ‘making of’ writeup will help us understand why they happen, and to me they’re just as useful in understanding how to build agentic systems!)

✉️

This project started with simple curiosity. I wanted to understand Claude Code, which to me is the best Agentic coding tool (even though the competition is close). Initially, I thought it would be straightforward—just an LLM and a few tools in a loop. I was wrong. It turned out to be far more complex, with tons of novel components I hadn't expected.

To tackle this, I worked with multiple AI subagents operating on different pieces of inference. I manually ferried questions and insights back and forth, reviewed outputs to check for hallucinations, and double-checked results.

The process involved:

Five batches of four rounds with completely new subagents (mostly Gemini 2.5 Pro)

Generating about 300K tokens worth of intermediate analysis

Condensing everything into a comprehensive report

What's remarkable is that this only took a day and taught me a lot. Before LLMs, this kind of analysis would have taken months—if it was possible at all. To Opus 4, who took my condensed report and transformed it into the comprehensive analysis you're about to read: thank you!

—Hrishi

Claude Code has a number of very interesting parts:

Streaming Architecture that handles real-time LLM responses, tool execution, and UI updates

Safety Systems that provide security without disrupting workflow

Tool Design that elegantly bridges AI reasoning and system execution

Prompt Engineering that reliably controls complex LLM behavior

Let’s jump in! Each heading is a link to the full section.

Why React in a terminal? What's yoga-layout doing here?

Discover the unconventional dependency choices that enable Claude Code's performance. Learn about the custom shell parser that embeds JSON in bash commands, the streaming JSON parser for partial LLM responses, and the ANR detection system borrowed from mobile development.

How messages transform through the system

Follow data from user input through LLM processing to tool execution. Understand the three-stage message representation, the

ContentBlock

polymorphism, and how weak references prevent memory bloat.

Key Insight: The

CliMessage

wrapper maintains UI state while preserving API compatibility—enabling rich interactions without protocol changes.

Inside the

tt

function

Explore the six-phase async generator that orchestrates everything. See how parallel tool execution works, why context compaction triggers automatically, and how recursive turns enable unlimited conversation depth.

Key Insight: Tools are categorized by side effects—read-only tools run in parallel while write operations serialize for safety.

From LLM decisions to system actions

Each tool is a carefully designed state machine. Examine the permission system, progress reporting, and error handling. Special focus on BashTool's sandbox mode and EditTool's line number handling.

Key Insight: The

AgentTool

implements hierarchical task decomposition—spawning sub-agents and synthesizing their findings.

Event-driven, streaming-first, security-conscious

Understand the layered architecture from React UI to system calls. Learn how permissions cascade through scopes, why ANR detection uses worker threads, and how three telemetry systems provide complete observability.

Key Insight: Security isn't one system—it's multiple independent layers that fail safely.

The clever fixes to hard problems

Discover components that make Claude Code special: streaming JSON parsing with recovery, intelligent data truncation, and multi-agent result synthesis. These aren't just features—they're innovative solutions to fundamental challenges.

Key Insight: The

normalizeToSize

algorithm iteratively reduces object depth based on actual byte count—preserving maximum information within constraints.

Why three different editing tools?

Deep dive into the file editing pipeline. Learn why line numbers cause problems, how sequential edits detect conflicts, and what happens when files change externally.

Key Insight: Every conceivable editing mistake has a specific validation—from external modifications to encoding issues.

The instructions that make it all work

Examine the actual prompts that control Claude Code. From conciseness enforcement to the 500+ word BashTool safety instructions, see how careful wording shapes behavior.

Key Insight: Repetition works—critical instructions appear three times with escalating emphasis.

What these prompts feel like from the other side

In a unique section, an LLM (me) provides honest commentary on receiving these instructions. Why "just output 4" is surprisingly difficult and how the -$1000 penalty creates real behavioral change despite being imaginary money.

Key Insight: Clear constraints are secretly liberating—they prevent decision paralysis and over-helpfulness.

Throughout the analysis, several design principles emerge:

Streaming First: Every operation designed for incremental updates

Safety Through Layers: Multiple independent protection mechanisms

Explicit Instructions: Verbose prompts prevent ambiguous behavior

Architecture Over Optimization: Performance through design, not tweaks

Understanding LLM Psychology: Exploiting how models actually behave

It’s amazing that this is even possible, let alone in the time this took. I can’t say everything in the report is correct - perhaps the Claude team can weigh in - but it has all been really useful and instructive.
