---
tags:
  - library
title: "CLI Introduction | Mistral Docs"
url: "https://docs.mistral.ai/mistral-vibe/introduction"
company: [personal]
topics: []
created: 2026-03-20
source_type: raindrop
raindrop_id: 1650196585
source_domain: "docs.mistral.ai"
source_type_raindrop: article
collection: "AI Tools & News"
collection_id: 69284314
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

Documentation for the deployment and usage of Mistral AI's LLMs

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: CLI Introduction | Mistral Docs

URL Source: https://docs.mistral.ai/mistral-vibe/introduction

Markdown Content:
# CLI Introduction | Mistral Docs

[](https://docs.mistral.ai/)Docs & API

Search docs

⌘K

[Getting Started](https://docs.mistral.ai/)[Models](https://docs.mistral.ai/models)[Products](https://docs.mistral.ai/products)[Developers](https://docs.mistral.ai/developers)[Admin](https://docs.mistral.ai/admin)[API](https://docs.mistral.ai/api)

Search docs

⌘K

Toggle theme[Reach out](https://mistral.ai/contact?utm_source=docs&utm_medium=header_cta&utm_campaign=studio_trial)[Try Vibe](https://console.mistral.ai/codestral/cli?utm_source=docs&utm_medium=header_cta&utm_campaign=studio_trial)

[Le Chat](https://docs.mistral.ai/le-chat/overview)

*   [Overview](https://docs.mistral.ai/le-chat/overview)

*   Conversation   

*   Content Creation   

*   Research & Analysis   

*   Knowledge & Integrations   

[Mistral Vibe](https://docs.mistral.ai/mistral-vibe/overview)

*   [Overview](https://docs.mistral.ai/mistral-vibe/overview)

*   [CLI Introduction](https://docs.mistral.ai/mistral-vibe/terminal)  

    *   [Install](https://docs.mistral.ai/mistral-vibe/terminal/install)
    *   [Quickstart](https://docs.mistral.ai/mistral-vibe/terminal/quickstart)
    *   [Configuration](https://docs.mistral.ai/mistral-vibe/terminal/configuration)

*   [Agents & Skills](https://docs.mistral.ai/mistral-vibe/agents-skills)
*   [Offline / Local](https://docs.mistral.ai/mistral-vibe/local)
*   [Coding](https://docs.mistral.ai/mistral-vibe/using-fim-api)

[Studio](https://docs.mistral.ai/studio-api/overview)

*   [Overview](https://docs.mistral.ai/studio-api/overview)

*   Conversations   

*   Agents   

*   Knowledge & RAG   

*   Document Processing   

*   Audio   

*   [Observability](https://docs.mistral.ai/studio-api/observability)   

*   Workflows   

*   [Moderation & Guardrailing](https://docs.mistral.ai/studio-api/safety-moderation)
*   [Batch Processing](https://docs.mistral.ai/studio-api/batch-processing)

1.   [](https://docs.mistral.ai/)

3.   [Products](https://docs.mistral.ai/products)

5.   [Mistral Vibe](https://docs.mistral.ai/mistral-vibe/overview)

7.   CLI Introduction

# CLI Introduction

**Mistral Vibe** is a command-line coding assistant powered by Mistral's models. It provides a conversational interface to your codebase, allowing you to use natural language to explore, modify, and interact with your projects through a built-in set of tools.

![Image 1: vibe_logo](https://docs.mistral.ai/img/vibe-logo.svg)

The code is available on [GitHub](https://github.com/mistralai/mistral-vibe) under an Apache 2.0 license.

Features

Copy section link
# Features

*   **Interactive Chat**: A conversational AI agent that understands your requests and breaks down complex tasks.
*   **Built-in Toolset**: A suite of tools for file manipulation, code searching, version control, and command execution, right from the chat prompt.
    *   Read, write, and patch files (read_file, write_file, search_replace).
    *   Execute shell commands in a stateful terminal (bash).
    *   Recursively search code with grep (with ripgrep support).
    *   Manage a todo list to track the agent's work.

*   **Project-Aware Context**: Mistral Vibe automatically scans your project's file structure and Git status to provide relevant context to the agent, improving its understanding of your codebase.
*   **Advanced CLI Experience**: Built with modern libraries for a smooth and efficient workflow.
    *   Autocompletion for slash commands (/) and file paths (@).
    *   Persistent command history.
    *   Beautiful Themes.

*   **Highly Configurable**: Customize models, providers, tool permissions, and UI preferences through a simple config.toml file.
*   **Agents & Skills**: Create and manage multiple agents with different skills and permissions.
*   **Safety First**: Features tool execution approval.

Learn More

Copy section link
# Learn More

Find how to install and use Mistral Vibe.

*   [Installation](https://docs.mistral.ai/mistral-vibe/terminal/install): How to Install Mistral Vibe.
*   [Quickstart](https://docs.mistral.ai/mistral-vibe/terminal/quickstart): A quickstart guide to using Mistral Vibe.
*   [Configuration](https://docs.mistral.ai/mistral-vibe/terminal/configuration): How to Configure Mistral Vibe.
*   [Agents & Skills](https://docs.mistral.ai/mistral-vibe/agents-skills): How to use Agents and Skills with Mistral Vibe.
*   [Offline / Local](https://docs.mistral.ai/mistral-vibe/local): How to run Mistral Vibe with a local model.

### WHY MISTRAL

[About us](https://mistral.ai/about)[Our customers](https://mistral.ai/customers)[Careers](https://mistral.ai/careers)[Contact us](https://mistral.ai/contact)

### EXPLORE

[AI Solutions](https://mistral.ai/solutions)[Partners](https://mistral.ai/partners)[Research](https://mistral.ai/news?category=Research)

### DOCUMENTATION

[Documentation](https://docs.mistral.ai/)[Ambassadors](https://docs.mistral.ai/community/ambassadors)[Cookbooks](https://docs.mistral.ai/resources/cookbooks)

### BUILD

[Studio](https://console.mistral.ai/)[Mistral Vibe](https://mistral.ai/products/vibe)[Mistral Code](https://mistral.ai/products/mistral-code)[Mistral Compute](https://mistral.ai/products/mistral-compute)[Try the API](https://docs.mistral.ai/api)

### LEGAL

[Terms of service](https://mistral.ai/terms)[Privacy policy](https://mistral.ai/terms#privacy-policy)[Legal notice](https://mistral.ai/legal)Privacy Choices[Brand](https://mistral.ai/brand)

### COMMUNITY

[Discord↗](https://discord.gg/mistralai)[X↗](https://x.com/mistralai)[Github↗](https://github.com/mistralai)[LinkedIn↗](https://linkedin.com/company/mistralai)[Ambassadors](https://docs.mistral.ai/community/ambassadors)

Mistral AI © 2026

Toggle theme

![Image 2: Sun](https://docs.mistral.ai/assets/sprites/sun.gif)

![Image 3: Grass](https://docs.mistral.ai/_next/image?url=%2Fassets%2Fsprites%2Fgrass_tile.png&w=640&q=75)

![Image 4: Grass](https://docs.mistral.ai/_next/image?url=%2Fassets%2Fsprites%2Fgrass_tile.png&w=640&q=75)

![Image 5: Grass](https://docs.mistral.ai/_next/image?url=%2Fassets%2Fsprites%2Fgrass_tile.png&w=640&q=75)![Image 6: Grass](https://docs.mistral.ai/_next/image?url=%2Fassets%2Fsprites%2Fgrass_tile.png&w=640&q=75)![Image 7: Grass](https://docs.mistral.ai/_next/image?url=%2Fassets%2Fsprites%2Fgrass_tile.png&w=640&q=75)

![Image 8: Grass](https://docs.mistral.ai/_next/image?url=%2Fassets%2Fsprites%2Fgrass_tile.png&w=640&q=75)

![Image 9: Grass](https://docs.mistral.ai/_next/image?url=%2Fassets%2Fsprites%2Fgrass_tile.png&w=640&q=75)

![Image 10: Grass](https://docs.mistral.ai/_next/image?url=%2Fassets%2Fsprites%2Fgrass_tile.png&w=640&q=75)

![Image 11: Grass](https://docs.mistral.ai/_next/image?url=%2Fassets%2Fsprites%2Fgrass_tile.png&w=640&q=75)![Image 12: Grass](https://docs.mistral.ai/_next/image?url=%2Fassets%2Fsprites%2Fgrass_tile.png&w=640&q=75)![Image 13: Grass](https://docs.mistral.ai/_next/image?url=%2Fassets%2Fsprites%2Fgrass_tile.png&w=640&q=75)

![Image 14: Grass](https://docs.mistral.ai/_next/image?url=%2Fassets%2Fsprites%2Fgrass_tile.png&w=640&q=75)

![Image 15: Grass](https://docs.mistral.ai/_next/image?url=%2Fassets%2Fsprites%2Fgrass_tile.png&w=640&q=75)![Image 16: Grass](https://docs.mistral.ai/_next/image?url=%2Fassets%2Fsprites%2Fgrass_tile.png&w=640&q=75)![Image 17: Grass](https://docs.mistral.ai/_next/image?url=%2Fassets%2Fsprites%2Fgrass_tile.png&w=640&q=75)

![Image 18: Cat](https://docs.mistral.ai/assets/sprites/cat-walking-white.gif)

[Mistral Vibe](https://docs.mistral.ai/mistral-vibe/overview)[Install](https://docs.mistral.ai/mistral-vibe/terminal/install)
