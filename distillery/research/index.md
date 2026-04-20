---
tags:
  - index
  - distillery
  - research
title: Research Briefs
company: personal
created: 2026-04-20
---

# Research Briefs

Alan's output folder. Each brief is a ranked set of claims with source URLs and confidence tags, written for a specific piece of content. Mira reads from here.

## Convention

- **One file per content piece**, named by slug: `{slug}.md`
- **Author**: always Alan (research profile)
- **Lifecycle**: Alan writes → Mira reads → stays as the durable audit trail
- **Frontmatter** (standard shape):

```yaml
---
title: "<Topic>"
slug: <slug>
author: alan
status: ready-for-draft | in-progress | stale
created: YYYY-MM-DD
source_count: <n>
confidence_summary: <n verified, n probable, n speculative>
next: mira
---
```

## Why briefs live here (not in Alan's memory)

File-based handoff means:

- Mira reads the exact claims Alan validated - no summarization drift
- Obsidian and git both track the handoff
- Weeks later, the draft in `content/<channel>/` can be traced back to the research
- Alan's memory stays focused on research tools, not carrying every past deliverable

## Flow

```
research/<slug>.md  →  content/<channel>/<slug>.md  →  published
(Alan)                 (Mira)                          (you)
```

## See also

- [[../../knowledge/hermes-team/profiles/alan/SOUL|Alan's SOUL]] - operating contract
- [[../../knowledge/hermes-team/team-agents|team-agents.md]] - handoff rules
- [[../channels/youtube|YouTube channel spec]]
- [[../channels/podcast|Podcast channel spec]]
