---
tags:
  - library
title: "Ref - Context for your coding agent"
url: "https://ref.tools/"
company: [personal]
topics: []
created: 2026-03-12
source_type: raindrop
raindrop_id: 1640411715
source_domain: "ref.tools"
source_type_raindrop: link
collection: "AI Tools & News"
collection_id: 69284314
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

Give your agent the docs it needs to succeed. Exactly the tokens you need, no bloat.

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: Ref - Context for your agent

URL Source: https://ref.tools/

Markdown Content:
#### Stop hallucinations by searching public and private docs. No context bloat.

How it works

Ref connects your AI coding tools with documentation context. It includes an up-to-date index of public documentation and it can ingest your private documentation (eg. GitHub repos, PDFs) as well. Your AI tools access this context through Model Context Protocol (MCP).

![Image 1: How Ref works diagram](https://ref.tools/images/diagram-light-mode.png)

The ref-context MCP server provides two tools that your agent can use to access documentation:

### search_documentation

Search through technical documentation for any platform, framework, API, service, database, or library. It can search public and private documentation sets. Finds exactly what you need, down to the specific section.

### read_url

Read the full content of any web page or Github file (public or private). Perfect for following links in documentation and accessing content that wasn't directly found in search.

Choose for yourself.

### Cobble together a bunch of different tools.

*   Code snippets → Context7
*   Web search → Exa
*   Web scraping → Firecrawl
*   Private code search → GitHub
*   PDF search → ???

OR

Secure & Enterprise ready.

### SOC2 Compliant![Image 2: SOC2 Compliant](https://ref.tools/images/soc2_badge.webp)

Ref works with Vanta to ensure SOC2 compliance. See our [Trust Center](https://trust.ref.tools/) and [Privacy & Security](https://docs.ref.tools/support/privacy-security) pages to understand our security and privacy practices.

### SSO & MCP OAuth

Ref offers Single Sign-On via major identity providers such as Okta and Google Workspace. Users can use OAuth to connect making it easy and secure to manage Ref across your organization.

### Active prompt injection mitigation

Every piece of context returned by Ref is scanned for prompt injection attacks so your coding agent is never following malicious instructions. We work with [Centure](https://centure.ai/) to provide this service.

[Learn more about Enterprise](https://tally.so/r/mZpYp0)

Pricing

### Free

#### 200 credits

*   1 credit per tool call
*   Up to 3 Plans
*   Up to 3 small repos
*   Up to 100 PDF pages
*   Up to 1,000 file uploads

[Sign up for Free](https://ref.tools/signup?tier=free)

### Basic

#### $19 / month 

 2000 credits

*   1 credit per tool call
*   Unlimited Plans
*   Up to 10 small repos
*   Up to 1 large repo
*   Up to 1,000 PDF pages
*   Up to 4,000 file uploads

[Sign up for Basic](https://ref.tools/signup?tier=basic)

### Pro

#### $50 / month 

 6000 credits

*   1 credit per tool call
*   Unlimited Plans
*   Up to 50 small repos
*   Up to 5 large repos
*   Up to 5,000 PDF pages
*   Up to 50,000 file uploads

[Sign up for Pro](https://ref.tools/signup?tier=pro)

### Max

#### $200 / month 

 30000 credits

*   1 credit per tool call
*   Unlimited Plans
*   Unlimited small repos
*   Up to 25 large repos
*   Up to 25,000 PDF pages
*   Up to 500,000 file uploads

[Sign up for Max](https://ref.tools/signup?tier=max)

#### Pay-as-you-go Credits

All paid plans include the option to purchase additional credits on-demand at **$10 per 1,000 credits**. Purchased credits roll over month-to-month and never expire, giving you flexibility to scale your usage as needed.

#### Repository Sizes

**Small repos** contain up to 4,000 indexed files, suitable for most projects. **Large repos** contain more than 4,000 indexed files, typically used for monorepos or very large codebases. Both types provide full search and context capabilities.

Additional Offerings

### Enterprise

*   SOC2
*   SSO + MCP OAuth
*   Priority support
*   Custom contracting and pricing
*   Advanced admin controls

[Contact us](https://tally.so/r/mZpYp0)

### Better AI Eng

Schedule a session with your team on how to get the most out of your AI dev tool stack, not just Ref.

[Learn more](https://tally.so/r/m6XOD5)

Faster. Cheaper. More Accurate.

### Beyond Pre-training

Access documentation for new releases, niche libraries, and specific versions that weren't in your model's training data, ensuring your AI has the most up-to-date information.

### Faster, Token-Efficient Responses

Our specialized processing delivers more relevant information in fewer tokens, making code assistance faster and reducing your API costs compared to generic search tools.

### Code-Aware Processing

Unlike general web crawlers, Ref is built specifically for technical documentation, preserving code blocks, formatting, and API signatures that generic tools frequently miss or corrupt.

MCP Developer Summit Talk

If you're interested in learning more about Ref and how it leverages advanced MCP patterns, check out my talk at the MCP Developer Summit in London, October 2025.

Vibe code anything.

![Image 3: Backend Engineering](https://ref.tools/images/turbopuffer/f2t_light_horizontal.png)![Image 4: Backend Engineering](https://ref.tools/images/turbopuffer/f2t_dark_horizontal.png)

### Migrate from Firestore to Turbopuffer

Using Cursor and Ref for a smooth database migration resulting in significantly faster search performance for our growing document index.

[Read the case study](https://ref.tools/use-case/turbopuffer)

![Image 5: Backend Engineering](https://ref.tools/images/rime/rime+mcp_light.png)![Image 6: Backend Engineering](https://ref.tools/images/rime/rime+mcp_dark.png)

### Text-to-speech MCP server with Rime

Quickly put together an MCP server to explore voice as a part of software development using Rime to give a coding agent a voice.

[Read the case study](https://ref.tools/use-case/rime)

Built for developers.

### Seamless Integrations via MCP

Built to work with modern AI development tools through MCP, powering Claude, Zed, Cursor, and other coding assistants with high-quality documentation context.

### Support for GitHub repos, LLMs.txt and the rest of the web

Engineers publish knowledge through GitHub repositories and LLMs.txt. Ref natively supports these sources as well as indexing any documentation site on the web.

### Free-range, organic data

Ref respects `robots.txt` and CAPTCHA protection. We believe in being good citizens of the web, and we'll never scrape content that's not meant to be accessed programmatically.

How do I know Ref has the docs I need?

Ref has an extensive index of public documentation so it probably does but don't take our word for it! The easiest way to see what Ref has is try searching for "`tell me about (the library you care about)`" and checkout the results.

[Try the demo](https://ref.tools/chat)

Wait, what about internal docs?

At Ref we know engineering teams don't just work with public APIs. You often reference docs for internal services, design specs, incident reports, team messages and private repos. Your coding agent should be able to access all the same context of a human counterpart. We're working on that.

As of now, Ref supports indexing **private Github repos** and **PDFs**. More sources will be coming soon. Let us know what you'd like to see!
