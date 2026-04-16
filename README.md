# HQ

<!-- Replace {{owner_name}} and {{company_description}} with your details -->
{{owner_name}}'s operational hub for {{company_description}}.

## Getting Started

This vault is designed to be operated by a human (via Obsidian) and an AI agent (via Claude Code reading raw files). To set it up:

1. Open this folder as an Obsidian vault
2. Start a Claude Code session in this directory
3. Claude will read the TODO in `CLAUDE.md` and walk you through customization
4. Create your first initiative, add some tasks, and you're running

## Navigation

- [[initiatives/index|Initiatives]] — strategic efforts across your companies
- [[tasks/index|Tasks]] — active work items rolled up by initiative
- [[knowledge/index|Knowledge]] — accumulated domain knowledge and references
- [[library/index|Library]] — curated external resources (articles, tools, repos)
- [[log/index|Log]] — decisions, meeting notes, reviews
- `inbox/` — unprocessed items awaiting weekly triage
- `distillery/` — content marketing: channels, content pipeline, draft generation
- `dashboards/` — Obsidian Bases views (visual dashboards)

## Conventions

### File naming
- lowercase-kebab-case, action-first for tasks
- Example: `write-hotwire-morphing-blog-post.md`

### Frontmatter
- Every file has YAML frontmatter with `tags` and `title`. Most types also include `status`, `company`, and `created` (log entries use `date` and `type` instead — see spec).
- Status enums — never free-text:
  - Tasks: `backlog` | `todo` | `in-progress` | `blocked` | `done` | `cancelled`
  - Initiatives: `active` | `paused` | `completed` | `abandoned`
- Priority: `1` (high), `2` (medium), `3` (low)
- Dates: always YYYY-MM-DD
- Companies: list multiple if shared, e.g. `[company-a, company-b]`

### Linking
- `[[wikilinks]]` for internal vault connections
- Standard markdown links for external URLs
- Tasks link to initiatives via `initiative` property (creates automatic backlinks)

### Structure
- Tags for TYPE: `task`, `initiative`, `knowledge`, `library`, `log`
- Properties for ATTRIBUTES: `company`, `status`, `priority`
- Folders for SCOPE: `tasks/`, `initiatives/`, `knowledge/`, `library/`, `log/`
- Max 2 levels deep. No nested subfolders.

### Index maintenance
- Bot maintains all index files during create/update operations
- Never manually curate task lists inside initiative notes — Bases handle that

## Maintenance

The full schema spec lives in `knowledge/hq-vault-design.md`. Refer to it when adding new file types or changing conventions.

## What's Active Right Now

<!-- Bot maintains this list. Every active initiative should appear here. -->
(No initiatives yet — create your first one in `initiatives/`)
