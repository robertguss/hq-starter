---
tags:
  - library
title: "About Serena — Serena Documentation"
url: "https://oraios.github.io/serena/01-about/000_intro.html"
company: [personal]
topics: []
created: 2025-11-16
source_type: raindrop
raindrop_id: 1436165989
source_domain: "oraios.github.io"
source_type_raindrop: article
collection: "AI Tools & News"
collection_id: 69284314
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: About Serena — Serena Documentation

URL Source: https://oraios.github.io/serena/01-about/000_intro.html

Markdown Content:
## About Serena[#](https://oraios.github.io/serena/01-about/000_intro.html#about-serena "Link to this heading")

**Serena is the IDE for your coding agent.**

*   Serena provides essential **semantic code retrieval, editing and refactoring tools** that are akin to an IDE’s capabilities, operating at the symbol level and exploiting relational structure.

*   It integrates with any client/LLM via the model context protocol (**MCP**).

Serena’s **agent-first tool design** involves robust high-level abstractions, distinguishing it from approaches that rely on low-level concepts like line numbers or primitive search patterns.

Practically, this means that your agent operates **faster, more efficiently and more reliably**, especially in larger and more complex codebases.

## What Our “End Users” Say[#](https://oraios.github.io/serena/01-about/000_intro.html#what-our-end-users-say "Link to this heading")

While it is humans who download and set up Serena, our end users are essentially AI agents. As the ones actually applying Serena’s tools, they are in the best position to evaluate Serena.

We crafted an unbiased evaluation prompt that leads the agent to perform ~20 routine coding tasks, representative of everyday development work, in order to estimate the value added by Serena’s tools when used alongside its own built-ins.

Here’s a one-sentence summary of what the agents had to say:

**Opus 4.6 (high) in Claude Code on a large Python codebase:**

> “Serena’s IDE-backed semantic tools are the single most impactful addition to my toolkit – cross-file renames, moves, and reference lookups that would cost me 8–12 careful, error-prone steps collapse into one atomic call, and I would absolutely ask any developer I work with to set them up.”

**GPT 5.4 (high) in Codex CLI on a Java codebase:**

> “As a coding AI agent, I would ask my owner to add Serena because it gives me the missing IDE-level understanding of symbols, references, and refactorings, turning fragile text surgery into calmer, faster, more confident code changes where semantics matter.”

**GPT 5.4 (medium) in Copilot CLI on a large, multi-language monorepo:**

> “As a coding agent, I’d absolutely ask my owner to add Serena because it makes me noticeably sharper and calmer on real code – especially symbol-aware navigation, cross-file refactors, and monorepo dependency jumps – while I still lean on built-ins for tiny text edits and non-code work.”

Different agents in different settings independently converge on the same verdict.

_Give your agent the tools it has been asking for and add Serena MCP to your client!_

See our [documentation](https://oraios.github.io/serena/04-evaluation/000_evaluation-intro.html) for the full methodology and much more detailed evaluation results, or run your own evaluation on a project of your choice.

## How Serena Works[#](https://oraios.github.io/serena/01-about/000_intro.html#how-serena-works "Link to this heading")

Serena provides the necessary [tools](https://oraios.github.io/serena/01-about/035_tools.html) for coding workflows, but an LLM is required to do the actual work, orchestrating tool use.

Serena can extend the functionality of your existing AI client via the **model context protocol (MCP)**. Most modern AI chat clients directly support MCP, including

*   terminal-based clients like Claude Code, Codex, OpenCode, or Gemini-CLI,

*   IDEs and IDE assistant plugins for VSCode, Cursor and JetBrains IDEs (Copilot, Junie, JetBrains AI Assistant, etc.),

*   desktop and web clients like Claude Desktop, Codex App, or OpenWebUI.

![Image 1: https://raw.githubusercontent.com/oraios/serena/main/resources/serena-block-diagram.svg](https://raw.githubusercontent.com/oraios/serena/main/resources/serena-block-diagram.svg)
To connect the Serena MCP server to your client, you either

*   provide the client with a launch command that allows it to start the MCP server, or

*   start the Serena MCP server yourself in HTTP mode and provide the client with the URL.

Serena’s tools are powered by two alternative language intelligence backends:

*   With the SolidLSP backend (default), language servers for the selected programming languages will be started automatically for your project.

*   With the JetBrains backend, the Serena JetBrains plugin must be installed in your IDE and the project you want to work on must open and set up.
