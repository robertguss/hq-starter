# HQ Vault — Agent Rules

## Session startup

At the start of every conversation, read all `index.md` files (initiatives, tasks, knowledge, library, log) to familiarize yourself with the business context and current state of work. Do this silently before responding. Robert shouldn't need to re-introduce the context each time. Read individual knowledge files only when needed for the task at hand.

## Before every commit, verify:

1. **Indexes are current** — every file in initiatives/, tasks/, knowledge/, library/, log/ must appear in its index.md
2. **README "What's Active" is current** — every active initiative must be listed
3. **Frontmatter matches spec** — check schemas in knowledge/hq-vault-design.md
4. **All wikilinks resolve** — no links to files that don't exist
5. **Dashboard filters are consistent** — all .base files should have matching guard filters

## When creating any new file:

1. Add frontmatter matching the template in \_templates/
2. Update the relevant index.md
3. If it's an initiative, add to README "What's Active" if active

## When changing the schema:

1. Update the spec FIRST (knowledge/hq-vault-design.md)
2. Update README conventions
3. Update templates in \_templates/
4. Then update existing files

## Obsidian

This is an Obsidian vault. Before creating or editing .md, .base, or .canvas files, check if you have Obsidian-related skills available (e.g. obsidian-markdown, obsidian-bases, json-canvas) and use them.

## Knowledge updates

Knowledge files are append-only by default. When new information arrives, **add it as a dated update** at the bottom of the file — never overwrite or replace existing content. Previous findings and reasoning are valuable context even when conclusions change. Only overwrite when Robert explicitly says to.

## Distillery

- Content architecture is documented in `distillery/index.md` — read it before any content work
- When adding library items: create the file with full raw content in body, then update the relevant `library/<slug>/_index.md` (per-collection synthesis) and `library/_index.md` (top-level cross-shelf view) as a compiled wiki (category summaries, cross-references, patterns — not just a file listing)
- Raw content sources by type:
  - **Web pages/blog posts**: fetch with your preferred URL-to-markdown tool
  - **YouTube videos**: fetch transcript with `youtube-transcript-api` (Python). Usage: `YouTubeTranscriptApi().fetch(video_id, languages=['en'])`, join snippet texts into full transcript.
  - **Transcripts/conversations**: paste directly
  - **GitHub repos**: fetch README from the repo URL
- When creating distillery content: read the target channel file in `distillery/channels/` for voice, format, and tactical rules. Read your author profile in `knowledge/` for voice, personality, and brand anchors.
- **Writing discipline**: use active voice, positive form, concrete language, omit needless words, emphatic words at the end.
- **The Ring**: after drafting any content, run it through "the ring" — a panel of fresh-perspective reviewers defined in the channel file. Each reviewer grades 0-10 with notes. Iterate until Robert is satisfied. The ring reviewers vary per channel to match that channel's audience.

## Conventions

- File naming: lowercase-kebab-case
- Dates: YYYY-MM-DD
- Links: `[[wikilinks]]` for internal, markdown links for external
- Company: single slug (`company: personal`). Switch to list syntax (`company: [personal, acme]`) only when actually sharing work across multiple companies.
- Status enums only — never free text

## Tools

There are various scripts in the @.tools/ directory for working with pdf's, importing raindrop.io bookmarks, and also importing bookmars from Twitter/X
