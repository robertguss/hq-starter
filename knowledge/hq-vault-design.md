---
tags:
  - knowledge
title: "HQ Vault Design"
company: []
topics:
  - vault
  - schema
  - conventions
created: 2026-04-17
---

# HQ Vault Design

## Purpose

Central operational hub. Serves two consumers: a human via Obsidian and an AI agent (Claude Code) via raw file access.

## Design Principles

1. **If it's not in HQ, it doesn't exist.** All operational knowledge, tasks, decisions, and strategic context live here.
2. **README is the map.** ~50 lines, navigational, points to indexes. Bot reads it first every session.
3. **Progressive disclosure.** README -> index files -> individual files. Three layers, never more.
4. **Tags for type, properties for attributes, folders for scope.** Don't mix these.
5. **Bot maintains indexes.** Every create/update operation includes an index update. Indexes don't rot.
6. **Two interfaces, same data.** Human sees dashboards via Obsidian Bases. Bot greps frontmatter. Neither is the source of truth — the markdown files are.

## Vault Structure

```
hq/
  README.md                         # The map + conventions + "what's active now"

  _templates/
    task.md
    initiative.md
    knowledge.md
    library.md
    log-entry.md
    weekly-summary.md

  initiatives/
    index.md                        # All initiatives with status and company
    (flat .md files, one per initiative)

  tasks/
    index.md                        # Active tasks rolled up by initiative
    (flat .md files, one per task)

  knowledge/
    index.md                        # Knowledge articles by topic
    (grows organically)

  library/
    index.md                        # Curated external resources by topic
    (flat .md files, one per resource)

  log/
    index.md                        # Decision records, meeting notes, reviews
    (flat .md files)
    weekly/
      index.md                      # Reverse-chronological list of weekly summaries
      YYYY-Wnn.md                   # One file per ISO week

  inbox/                            # Quick capture, triage weekly

  distillery/
    index.md                        # Distillery overview + content pipeline summary
    channels/
      example-linkedin.md           # Channel instructions + audience data
      example-blog.md
    content/
      example-linkedin/             # One subfolder per channel_id
      example-blog/

  dashboards/
    all-tasks.base                  # All open tasks across all companies
    personal-tasks.base             # Company-filtered tasks (duplicate per company)
    initiatives.base                # Initiative overview
```

## Frontmatter Schemas

### Task

```yaml
---
tags: [task]
title: "Write blog post on X"
status: backlog # backlog | todo | in-progress | blocked | done | cancelled
priority: 2 # 1=high, 2=medium, 3=low
company: company-a # your company slug (list multiple if shared)
initiative: "[[initiative-slug]]" # wikilink, optional (empty for admin/orphan tasks)
due: # YYYY-MM-DD, optional
created: 2026-03-23
completed: # YYYY-MM-DD, filled when status -> done
---
```

Required sections: `## Context`, `## Done When`.

### Initiative

```yaml
---
tags: [initiative]
title: "Content Marketing"
company: company-a # your company slug (list multiple if shared)
status: active # active | paused | completed | abandoned
owner: owner-name
started: 2026-03-01
target_date: # YYYY-MM-DD, optional soft deadline
---
```

Required sections: `## Goal`, `## Context`, `## Key Results`.

### Knowledge

```yaml
---
tags: [knowledge]
title: "Article Title"
company: company-a # your company slug (list multiple if shared)
topics: [] # e.g. [rails, hotwire]
source: "" # URL, optional
created: 2026-03-23
---
```

Minimal schema. Let the body do the work.

### Library

```yaml
---
tags: [library]
title: "Resource Title"
url: "" # External URL, optional (empty for transcripts/conversations)
company: [company-a] # your company slug (list multiple if shared)
topics: [] # e.g. [ai, architecture]
created: 2026-03-24
---
```

Body contains raw content under `## Raw Content` (full text, transcript, or key quotes). Library files store raw data only — synthesis and "why it matters" context belongs in the library index files (`library/_index.md` top-level, `library/<slug>/_index.md` per collection) — the compiled wiki — not in individual files. The vault must be self-contained for content generation without fetching external URLs.

**Library index (`library/_index.md` plus `library/<slug>/_index.md` per collection) is a compiled wiki, not a file listing.** Bot maintains it as a living synthesis document:

- Each concept category includes a summary paragraph synthesizing what the items collectively tell us
- Individual items listed with multi-sentence summaries, not just one-liners
- Cross-references and connections between items are made explicit
- Key takeaways and patterns are surfaced at the category level
- Updated incrementally every time a library item is added or modified

### Log Entry

```yaml
---
tags: [log]
title: "Decision: target market segment X"
date: 2026-03-23
type: decision # decision | meeting | review | observation
---
```

Required sections: `## Summary`, `## Details`, `## Outcome`.

### Weekly Summary

```yaml
---
tags: [log, weekly]
title: "Week 13 — March 23-29"
week: 2026-W13 # ISO week (YYYY-Wnn)
date_start: 2026-03-23 # Monday
date_end: 2026-03-29 # Sunday
---
```

Lives in `log/weekly/`. One file per ISO week, named `YYYY-Wnn.md`.
Index at `log/weekly/index.md` (reverse-chronological).

Required sections: `## TL;DR`, `## By Initiative`, `## Tasks`, `## Decisions`, `## Next Week`, `## Blockers`.

## Conventions

- **File naming:** lowercase-kebab-case, action-first for tasks. Example: `write-blog-post-topic.md`
- **Dates:** YYYY-MM-DD always. Use explicit `created` property, not `file.ctime`.
- **Links:** Wikilinks (`[[note]]`) for internal vault connections. Standard markdown links for external URLs.
- **Status enums:** Small, documented sets. Never free-text status.
- **Priority:** Numbers (1/2/3), not text. Formulas in Bases handle labels.
- **No nesting beyond 2 levels.** Folders are for broad categories. Properties handle fine-grained filtering. Exception: `distillery/content/<channel_id>/` uses 3 levels — content grouped by channel.
- **No status in filenames.** Status lives in frontmatter.
- **No empty placeholder notes.** If a task doesn't have enough context for a sentence, it doesn't deserve a file.
- **`cancelled` is separate from `done`.** Completion metrics stay clean.

## Linking Strategy

1. Tasks link TO initiatives via the `initiative` property using wikilinks. This creates automatic backlinks on the initiative page.
2. Knowledge notes link to initiatives and other knowledge notes in body text, not frontmatter.
3. Never duplicate what Bases can compute. Don't maintain task lists inside initiative notes.

## Dashboards (Obsidian Bases)

Base files in `dashboards/` provide filtered views over tasks and initiatives. They query frontmatter properties and render as tables/cards in Obsidian. Bot reads the underlying markdown files directly.

## Index Maintenance

All index files are maintained by Bot as part of create/update operations:

- `initiatives/index.md` — updated when initiatives are added/changed
- `tasks/index.md` — updated when tasks are added/changed
- `knowledge/index.md` — updated when knowledge articles are added
- `library/_index.md` + `library/<slug>/_index.md` — updated when library resources are added
- `log/index.md` — updated when log entries are added

### Content (Distillery)

```yaml
---
tags: [content]
title: "Post title"
channel: example-linkedin # must match a channel_id in distillery/channels/
pillar: technical # your content pillars
status: published # idea | draft | review | ready | published
author: owner-name
created: 2026-01-27 # YYYY-MM-DD, when file was created
published_date: 2026-01-27 # YYYY-MM-DD, when content was published
url: "" # published URL
cross_posted_from: "" # wikilink to source content file, optional
impressions: # from analytics
engagements: # total engagement count
metrics_updated: # YYYY-MM-DD when metrics last refreshed
---
```

Lives in `distillery/content/<channel_id>/`. Body contains the full post text. Filenames must be unique across the vault — prefix with channel shorthand when the same topic appears on multiple channels.

### Channel (Distillery)

```yaml
---
tags: [channel]
title: "Channel Name"
channel_id: example-linkedin # matches content file `channel` values
company: [company-a]
cadence: "3/week" # target posting frequency
created: 2026-04-08
---
```

Lives in `distillery/channels/`. Body contains channel instructions (tone, format, audience, rules).

## Inbox Workflow

Inbox is for quick capture without structure. Triage weekly: read each item, assign a type tag, move to the right folder, add frontmatter. Items older than 30 days without triage get reviewed for deletion.
