---
tags:
  - library
title: "Introducing the Vercel plugin for coding agents - Vercel"
url: "https://vercel.com/changelog/introducing-vercel-plugin-for-coding-agents"
company: [personal]
topics: []
created: 2026-03-19
source_type: raindrop
raindrop_id: 1649725582
source_domain: "vercel.com"
source_type_raindrop: article
collection: "AI Tools & News"
collection_id: 69284314
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

Introducing the Vercel Plugin for coding agents such as Claude Code, Cursor, and more featuring the latest Vercel libraries, platform, and product knowledge.

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: Introducing the Vercel plugin for coding agents - Vercel – Vercel

URL Source: https://vercel.com/changelog/introducing-vercel-plugin-for-coding-agents

Markdown Content:
# Introducing the Vercel plugin for coding agents - Vercel
[Skip to content](https://vercel.com/changelog/introducing-vercel-plugin-for-coding-agents#geist-skip-nav)

[](https://vercel.com/home)

*   Products

    *   ##### [AI Cloud](https://vercel.com/ai)

        *   [AI Gateway One endpoint, all your models](https://vercel.com/ai-gateway)
        *   [Sandbox Isolated, safe code execution](https://vercel.com/sandbox)
        *   [Vercel Agent An agent that knows your stack](https://vercel.com/agent)
        *   [AI SDK The AI Toolkit for TypeScript](https://sdk.vercel.ai/)
        *   [v0 Build applications with AI](https://v0.app/)

    *   ##### Core Platform

        *   [CI/CD Helping teams ship 6× faster](https://vercel.com/products/previews)
        *   [Content Delivery Fast, scalable, and reliable](https://vercel.com/cdn)
        *   [Fluid Compute Servers, in serverless form](https://vercel.com/fluid)
        *   [Workflow Long-running workflows at scale](https://vercel.com/workflows)
        *   [Observability Trace every step](https://vercel.com/products/observability)

    *   ##### [Security](https://vercel.com/security)

        *   [Bot Management Scalable bot protection](https://vercel.com/security/bot-management)
        *   [BotID Invisible CAPTCHA](https://vercel.com/botid)
        *   [Platform Security DDoS Protection, Firewall](https://vercel.com/security)
        *   [Web Application Firewall Granular, custom protection](https://vercel.com/security/web-application-firewall)

*   Resources

    *   ##### Company

        *   [Customers Trusted by the best teams](https://vercel.com/customers)
        *   [Blog The latest posts and changes](https://vercel.com/blog)
        *   [Changelog See what shipped](https://vercel.com/changelog)
        *   [Press Read the latest news](https://vercel.com/press)
        *   [Events Join us at an event](https://vercel.com/events)

    *   ##### Learn

        *   [Docs Vercel documentation](https://vercel.com/docs)
        *   [Academy Linear courses to level up](https://vercel.com/academy)
        *   [Knowledge Base Find help quickly](https://vercel.com/kb)
        *   [Community Join the conversation](https://community.vercel.com/)

    *   ##### Open Source

        *   [Next.js The native Next.js platform](https://vercel.com/frameworks/nextjs)
        *   [Nuxt The progressive web framework](https://nuxt.com/)
        *   [Svelte The web’s efficient UI framework](https://svelte.dev/)
        *   [Turborepo Speed with Enterprise scale](https://vercel.com/solutions/turborepo)

*   Solutions

    *   ##### Use Cases

        *   [AI Apps Deploy at the speed of AI](https://vercel.com/ai)
        *   [Composable Commerce Power storefronts that convert](https://vercel.com/solutions/composable-commerce)
        *   [Marketing Sites Launch campaigns fast](https://vercel.com/solutions/marketing-sites)
        *   [Multi-tenant Platforms Scale apps with one codebase](https://vercel.com/solutions/multi-tenant-saas)
        *   [Web Apps Ship features, not infrastructure](https://vercel.com/solutions/web-apps)

    *   ##### Tools

        *   [Marketplace Extend and automate workflows](https://vercel.com/marketplace)
        *   [Templates Jumpstart app development](https://vercel.com/templates)
        *   [Partner Finder Get help from solution partners](https://vercel.com/partners/solution-partners)

    *   ##### Users

        *   [Platform Engineers Automate away repetition](https://vercel.com/solutions/platform-engineering)
        *   [Design Engineers Deploy for every idea](https://vercel.com/solutions/design-engineering)

*   [Enterprise](https://vercel.com/enterprise)
*   [Pricing](https://vercel.com/pricing)

Ask AI

Ask AI[Log In](https://vercel.com/login)

[Sign Up](https://vercel.com/signup)[Sign Up](https://vercel.com/signup)

[Blog](https://vercel.com/blog)/[Changelog](https://vercel.com/changelog)

# Introducing the Vercel plugin for coding agents

## Authors

[![Image 1](https://assets.vercel.com/image/upload/f_auto,c_fill,w_48,h_48,q_75/contentful/image/e5382hct74si/4FeHGwRwyOKnWUVO2j8myT/4ea8fc5ac3df4d024fa9984f4da5bea8/melkey.jpg)](https://twitter.com/melkeydev)

![Image 2](https://assets.vercel.com/image/upload/f_auto,c_fill,w_48,h_48,q_75/contentful/image/e5382hct74si/75pWy8nmLyZddnFQwtb7JT/ab3171051c3229ae8fb2a0fa19443375/T0CAQ00TU-U0A2MCXAED9-56e8dbaf3ee1-512.jpg)

[![Image 3](https://assets.vercel.com/image/upload/f_auto,c_fill,w_48,h_48,q_75/contentful/image/e5382hct74si/6qvpRjZDpvV0JLU8mXx2v4/53962a54ad214cde165e18813940354e/806FE12B-9B25-4A8F-AB72-0853E48B1734_1_105_c_2__1_.jpg)](https://twitter.com/andrewqu)

1 min read

Copy URL

Copied to clipboard!

Mar 17, 2026

Claude Code and Cursor can now further understand Vercel projects using the new Vercel plugin and a full platform knowledge graph.

The plugin observes real-time activity, including file edits and terminal commands, to dynamically inject Vercel knowledge into the agent's context. Key capabilities include:

*   **Platform knowledge:** Access 47+ skills covering the Vercel platform, including Next.js, AI SDK, Turborepo, Vercel Functions, and Routing Middleware, powered by a relational knowledge graph

*   **Specialized tooling:** Use three specialist agents (AI Architect, Deployment Expert, Performance Optimizer) and five slash commands (`/bootstrap`, `/deploy`, `/env`, `/status`, `/marketplace`)

*   **Context management:** An injection engine and project profiler rank, deduplicate, and budget-control loaded context

*   **Code validation:**`PostToolUse` validation catches deprecated patterns, sunset packages, and stale APIs in real time

Instead of standard retrieval, the plugin compiles pattern matchers at build time and runs a priority-ranked injection pipeline across seven lifecycle hooks. Skills fire when glob patterns, bash regexes, import statements, or prompt signals match, and are then deduplicated across the session to ensure accurate agent responses.

The plugin currently supports Claude Code and Cursor, with OpenAI Codex support coming soon.

Install the plugin via npx:

`1npx plugins add vercel/vercel-plugin`

Directly in Claude Code via the official marketplace:

`1/plugin install vercel`

Or directly in Cursor:

`1/add-plugin vercel`

Explore the source code in the [Vercel plugin repository](https://github.com/vercel/vercel-plugin).

**Ready to deploy?**Start building with a free account. Speak to an expert for your _Pro_ or Enterprise needs.

[Start Deploying](https://vercel.com/new)[Talk to an Expert](https://vercel.com/contact/sales)

**Explore Vercel Enterprise** with an interactive product tour, trial, or a personalized demo.

[Explore Enterprise](https://vercel.com/try-enterprise)

## Get Started

*   [Templates](https://vercel.com/templates)
*   [Supported frameworks](https://vercel.com/docs/frameworks)
*   [Marketplace](https://vercel.com/marketplace)
*   [Domains](https://vercel.com/domains)

## Build

*   [Next.js on Vercel](https://vercel.com/frameworks/nextjs)
*   [Turborepo](https://vercel.com/solutions/turborepo)
*   [v0](https://v0.app/)

## Scale

*   [Content delivery network](https://vercel.com/cdn)
*   [Fluid compute](https://vercel.com/fluid)
*   [CI/CD](https://vercel.com/products/previews)
*   [Observability](https://vercel.com/products/observability)
*   [AI Gateway New](https://vercel.com/ai-gateway)
*   [Vercel Agent New](https://vercel.com/agent)

## Secure

*   [Platform security](https://vercel.com/security)
*   [Web Application Firewall](https://vercel.com/security/web-application-firewall)
*   [Bot management](https://vercel.com/security/bot-management)
*   [BotID](https://vercel.com/botid)
*   [Sandbox New](https://vercel.com/sandbox)

## Resources

*   [Pricing](https://vercel.com/pricing)
*   [Customers](https://vercel.com/customers)
*   [Enterprise](https://vercel.com/enterprise)
*   [Articles](https://vercel.com/i)
*   [Startups](https://vercel.com/startups)
*   [Solution partners](https://vercel.com/partners/solution-partners)

## Learn

*   [Docs](https://vercel.com/docs)
*   [Blog](https://vercel.com/blog)
*   [Changelog](https://vercel.com/changelog)
*   [Knowledge Base](https://vercel.com/kb)
*   [Academy](https://vercel.com/academy)
*   [Community](https://community.vercel.com/)

## Frameworks

*   [Next.js](https://vercel.com/frameworks/nextjs)
*   [Nuxt](https://vercel.com/docs/frameworks/full-stack/nuxt)
*   [Svelte](https://vercel.com/docs/frameworks/full-stack/sveltekit)
*   [Nitro](https://vercel.com/docs/frameworks/backend/nitro)
*   [Turbo](https://vercel.com/solutions/turborepo)

## SDKs

*   [AI SDK](https://ai-sdk.dev/)
*   [Workflow SDK New](https://workflow-sdk.dev/)
*   [Flags SDK](https://flags-sdk.dev/)
*   [Chat SDK](https://chat-sdk.dev/)
*   [Streamdown AI New](https://streamdown.ai/)

## Use Cases

*   [Composable commerce](https://vercel.com/solutions/composable-commerce)
*   [Multi-tenant platforms](https://vercel.com/solutions/multi-tenant-saas)
*   [Web apps](https://vercel.com/solutions/web-apps)
*   [Marketing sites](https://vercel.com/solutions/marketing-sites)
*   [Platform engineers](https://vercel.com/solutions/platform-engineering)
*   [Design engineers](https://vercel.com/solutions/design-engineering)

## Company

*   [About](https://vercel.com/about)
*   [Careers](https://vercel.com/careers)
*   [Help](https://vercel.com/help)
*   [Press](https://vercel.com/press)
*   [Legal](https://vercel.com/legal)
*   [Privacy Policy](https://vercel.com/legal/privacy-policy)

## Community

*   [Open source program](https://vercel.com/open-source-program)
*   [Events](https://vercel.com/events)
*   [Shipped on Vercel](https://vercel.com/shipped)
*   [GitHub](https://github.com/vercel)
*   [LinkedIn](https://linkedin.com/company/vercel)
*   [X](https://x.com/vercel)
*   [YouTube](https://youtube.com/@VercelHQ)

[](https://vercel.com/home)

[Loading status…](https://vercel-status.com/)Select a display theme:system light dark
