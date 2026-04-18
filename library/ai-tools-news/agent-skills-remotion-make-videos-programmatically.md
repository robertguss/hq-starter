---
tags:
  - library
title: "Agent Skills | Remotion | Make videos programmatically"
url: "https://www.remotion.dev/docs/ai/skills"
company: [personal]
topics: []
created: 2026-04-14
source_type: raindrop
raindrop_id: 1683869727
source_domain: "remotion.dev"
source_type_raindrop: article
collection: "AI Tools & News"
collection_id: 69284314
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

Remotion maintains a list of Agent Skills that define best practices for working in Remotion projects.

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: Agent Skills | Remotion | Make videos programmatically

URL Source: https://www.remotion.dev/docs/ai/skills

Published Time: Wed, 15 Apr 2026 20:54:52 GMT

Markdown Content:
# Agent Skills | Remotion | Make videos programmatically

[Skip to main content](https://www.remotion.dev/docs/ai/skills#__docusaurus_skipToContent_fallback)

[![Image 1: Remotion Logo](https://www.remotion.dev/img/new-logo.png)](https://www.remotion.dev/)[Docs](https://www.remotion.dev/docs/)[API](https://www.remotion.dev/docs/api)

[Products](https://www.remotion.dev/docs/ai/skills#)
*   [Player](https://www.remotion.dev/player)
*   [Lambda](https://www.remotion.dev/lambda)
*   [Editor Starter](https://www.remotion.dev/docs/editor-starter)
*   [Timeline](https://www.remotion.dev/docs/timeline)
*   [Recorder](https://www.remotion.dev/docs/recorder)

[Resources](https://www.remotion.dev/docs/ai/skills#)
*   [Prompts](https://remotion.dev/prompts)
*   [Learn](https://www.remotion.dev/learn)
*   [Resources](https://www.remotion.dev/docs/resources)
*   [Blog](https://www.remotion.dev/blog)
*   [Showcase](https://www.remotion.dev/showcase)
*   [Convert a video](https://remotion.dev/convert)
*   [Timing Editor](https://remotion.dev/timing-editor)
*   [Support](https://www.remotion.dev/docs/support)
*   [Templates](https://www.remotion.dev/templates)

[Commercial](https://www.remotion.dev/docs/ai/skills#)
*   [License + Pricing](https://remotion.pro/license)
*   [Store](https://remotion.pro/store)
*   [Success Stories](https://www.remotion.dev/success-stories)
*   [Experts](https://www.remotion.dev/experts)
*   [About us](https://www.remotion.dev/about)
*   [Investors](https://www.remotion.dev/docs/investors)
*   [Contact us](https://www.remotion.dev/contact)

[](https://github.com/remotion-dev/remotion)[](https://remotion.dev/discord)[](https://x.com/remotion)

Search K

*   [Getting started](https://www.remotion.dev/docs/ai/skills#) 
*   [Designing visuals](https://www.remotion.dev/docs/ai/skills#) 
*   [Adding video](https://www.remotion.dev/docs/ai/skills#) 
*   [Adding audio](https://www.remotion.dev/docs/using-audio) 
*   [Parameterized videos](https://www.remotion.dev/docs/parameterized-rendering) 
*   [Captions](https://www.remotion.dev/docs/captions/) 
*   
* * *

*   [Rendering](https://www.remotion.dev/docs/render) 
*   [Server-side rendering](https://www.remotion.dev/docs/ssr) 
*   [Client-side rendering](https://www.remotion.dev/docs/client-side-rendering/) 
*   [Lambda](https://www.remotion.dev/docs/lambda) 
*   [Cloud Run](https://www.remotion.dev/docs/cloudrun) 
*   
* * *

*   [Studio](https://www.remotion.dev/docs/ai/skills#) 
*   [Player](https://www.remotion.dev/docs/player/) 
*   [Building apps](https://www.remotion.dev/docs/ai/skills#) 
*   [Mediabunny](https://www.remotion.dev/docs/mediabunny/) 
*   [AI](https://www.remotion.dev/docs/ai/) 
    *   [Claude Code](https://www.remotion.dev/docs/ai/claude-code)
    *   [Bolt.new](https://www.remotion.dev/docs/ai/bolt)
    *   [Chatbot](https://www.remotion.dev/docs/ai/chatbot)
    *   [Code Generation](https://www.remotion.dev/docs/ai/generate)
    *   [Just-in-time compilation](https://www.remotion.dev/docs/ai/dynamic-compilation)
    *   [Prompt to Motion Graphics SaaS](https://www.remotion.dev/docs/ai/ai-saas-template)
    *   [MCP](https://www.remotion.dev/docs/ai/mcp)
    *   [System Prompt](https://www.remotion.dev/docs/ai/system-prompt)
    *   [Skills](https://www.remotion.dev/docs/ai/skills)

*   [Tooling](https://www.remotion.dev/docs/ai/skills#) 
*   
* * *

*   [API Reference](https://www.remotion.dev/docs/api)
*   [Terminology](https://www.remotion.dev/docs/terminology) 
*   [Snippets](https://www.remotion.dev/docs/ai/skills#) 
*   [FAQ](https://www.remotion.dev/docs/ai/skills#) 
*   [Miscellaneous](https://www.remotion.dev/docs/ai/skills#) 
*   [List of resources](https://www.remotion.dev/docs/resources)
*   [Troubleshooting](https://www.remotion.dev/docs/ai/skills#) 
*   [Get help](https://www.remotion.dev/docs/get-help) 
*   [Upgrading](https://www.remotion.dev/docs/ai/skills#) 
*   [Contributing](https://www.remotion.dev/docs/ai/skills#) 
*   [License & Pricing](https://www.remotion.dev/docs/license)
*   [Acknowledgements](https://www.remotion.dev/docs/acknowledgements)
*   
* * *

*   [Editor Starter](https://www.remotion.dev/docs/editor-starter)
*   [Timeline](https://www.remotion.dev/docs/timeline)
*   [Animated Captions](https://www.remotion.dev/docs/animated-captions)
*   [Recorder](https://www.remotion.dev/docs/recorder)
*   
* * *

*   [Media Parser](https://www.remotion.dev/docs/media-parser/) 
*   [WebCodecs](https://www.remotion.dev/docs/webcodecs/) 

*   [](https://www.remotion.dev/)
*   [AI](https://www.remotion.dev/docs/ai/)
*   Skills

Copy page

# Agent Skills

Remotion maintains a list of [Agent Skills](https://agentskills.io/home) that define best practices for working in Remotion projects.

These skills are useful for AI agents like Claude Code, Codex or Cursor.

You can install them by running:

`npx skills add remotion-dev/skills`Copy

You are also offered the option to add skills when you create a new Remotion project:

`bun create video`Copy

The skills are also available on GitHub [here](https://github.com/remotion-dev/remotion/tree/main/packages/skills).

[Improve this page](https://github.com/remotion-dev/remotion/edit/main/packages/docs/docs/ai/skills.mdx)[Ask on Discord](https://remotion.dev/discord)[Get help](https://www.remotion.dev/docs/get-help)

Last updated on **Apr 10, 2026**

[Previous System Prompt](https://www.remotion.dev/docs/ai/system-prompt)[Next TailwindCSS](https://www.remotion.dev/docs/tailwind)

![Image 2](https://www.remotion.dev/img/new-logo.png)
© Copyright 2026 Remotion AG. 

 Website created with Docusaurus.

Remotion

*   [Getting started](https://www.remotion.dev/docs/)
*   [Templates](https://www.remotion.dev/templates)
*   [API Reference](https://www.remotion.dev/docs/api)
*   [Player](https://www.remotion.dev/player)
*   [Lambda](https://www.remotion.dev/lambda)
*   [Learn](https://www.remotion.dev/learn)
*   [Convert a video](https://convert.remotion.dev/)
*   [Store](https://remotion.pro/store)
*   [GitHub](https://github.com/remotion-dev/remotion)
*   [Remotion Pro](https://remotion.pro/)

Community

*   [Prompt Showcase](https://remotion.dev/prompts)
*   [Showcase](https://www.remotion.dev/showcase)
*   [Experts](https://www.remotion.dev/experts)
*   [Discord](https://remotion.dev/discord)
*   [X](https://x.com/remotion)
*   [YouTube](https://youtube.com/@remotion_dev)
*   [LinkedIn](https://www.linkedin.com/company/remotion-dev/)
*   [Instagram](https://instagram.com/remotion)
*   [TikTok](https://www.tiktok.com/@remotion)

More

*   [About us](https://www.remotion.dev/about)
*   [Contact us](https://www.remotion.dev/contact)
*   [Blog](https://www.remotion.dev/blog)
*   [Success Stories](https://www.remotion.dev/success-stories)
*   [Support](https://www.remotion.dev/docs/support)
*   [Changelog](https://remotion.dev/changelog)
*   [Acknowledgements](https://remotion.dev/acknowledgements)
*   [License](https://remotion.dev/license)
*   [Terms and Conditions](https://remotion.pro/terms)
*   [Privacy Policy](https://remotion.pro/privacy)
*   [Brand](https://remotion.dev/brand)
