---
tags:
  - index
title: Distillery
---

# Distillery

Content marketing system. Compiles company knowledge and external signals into publishable content across channels.

## Architecture

```
library/ items  (raw signals)
       |
       v
library/index.md  (compiled wiki — synthesis, concepts, connections)
       |
       |------------------+
       v                  v
knowledge/          distillery/content/
(company context)-->  (what we publish)
```

**Inputs:**

- `knowledge/` — company strategy, competitive research, market positioning, team context, domain expertise. What makes your company unique and what you know about your space.
- `library/` — external signals: articles, blog posts, social media posts, conference talks, meeting transcripts, conversations. Raw material with full content stored in the body. The `library/index.md` serves as a compiled wiki — a synthesized, categorized, cross-linked summary of everything in the library. This is the intermediate "understanding" layer between raw signals and published content.

**Outputs:**

- `distillery/content/<channel_id>/` — one file per published or planned content piece, organized by channel. Full post text in the body, metadata and analytics in frontmatter.

**Channels:**

- `distillery/channels/` — channel definitions with voice, format, audience, and tactical rules. These instruct the AI agent on how to draft for each channel.

**Research briefs:**

- `distillery/research/` — Alan (research profile) writes ranked claims here. Mira reads from here before drafting. File-based handoff pattern; see [[research/index|research/]].

The agent acts as the compiler: reads knowledge + library context, follows channel instructions, produces drafts. You review and publish manually.

## Design Principles

### No automated signal ingestion

You add signals manually to `library/`. Manual curation is better signal quality than automated scraping.

### Library stores raw content, not just pointers

Library files store the full text/transcript/content in their body, not just a URL and summary. This follows the Karpathy knowledge base model: raw data is the foundation. The vault must be self-contained — the agent should be able to generate content from library + knowledge without fetching external URLs.

### Knowledge + Library = inputs, Distillery = output only

Distillery does not have its own intake mechanism. It is purely a content output layer that compiles from two existing HQ sources:

- `knowledge/` for company context (strategy, research, positioning)
- `library/` for external signals (articles, transcripts, conversations)

This avoids duplicating data between folders and keeps a clean separation: knowledge is accumulated understanding, library is consumed raw material, distillery content is what we publish.

### Library index as compiled wiki (Karpathy model)

Following Karpathy's LLM knowledge base pattern: raw data goes into `library/` items, then Bot compiles `library/index.md` as a wiki — summarizing all items, categorizing by concept, surfacing connections and patterns, and maintaining cross-references. This is the intermediate "understanding" layer between raw signals and published content.

The three-layer flow: `library/ items` (raw) -> `library/index.md` (compiled wiki) -> `distillery/content/` (published). Knowledge feeds in at the content generation stage as company context.

## Channels

| Channel                                                     | Cadence | Description                                   |
| ----------------------------------------------------------- | ------- | --------------------------------------------- |
| [[channels/blog\|Blog]]                                     | —       | Long-form writing on personal site / platform |
| [[channels/newsletter\|Newsletter]]                         | —       | Email subscriber channel                      |
| [[channels/twitter\|Twitter / X]]                           | —       | Short posts, threads, real-time commentary    |
| [[channels/linkedin\|LinkedIn]]                             | —       | Professional network posts                    |
| [[channels/youtube\|YouTube]]                               | —       | Video content                                 |
| [[channels/podcast\|Podcast]]                               | —       | Audio episodes                                |
| [[channels/example-blog\|Example Blog]] (reference)         | 2/month | Reference template only                       |
| [[channels/example-linkedin\|Example LinkedIn]] (reference) | 3/week  | Reference template only                       |

## Pillars

Content pillars are the themes that your content orbits around. Define 3-5 that map to your positioning.

<!-- Example:
| Pillar | Description |
|---|---|
| technical | Deep dives on your core technology stack |
| case-studies | Client projects, challenges, outcomes |
| personal | Founder journey, lessons learned, team building |
| industry | Trends and analysis in your target market |
-->
