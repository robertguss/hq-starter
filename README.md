# HQ

Robert Guss's second brain — operational hub for personal projects, content, and long-term thinking.

## Navigation

- [[initiatives/index|Initiatives]] — strategic efforts across projects
- [[tasks/index|Tasks]] — active work items rolled up by initiative
- [[knowledge/index|Knowledge]] — accumulated domain knowledge and references
- [[library/index|Library]] — curated external resources (articles, tools, repos)
- [[log/index|Log]] — decisions, meeting notes, reviews
- `inbox/` — unprocessed items awaiting weekly triage
- `distillery/` — content production: channels, content pipeline, draft generation
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
- Company: single slug (`personal`). Switch to list syntax (`[personal, acme]`) only when sharing work across multiple companies.

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

- [[initiatives/pocket-apologist|Ship Pocket Apologist iOS App]]
- [[initiatives/sweep|Finish Sweep iOS App]]
- [[initiatives/sentinel|Ship Sentinel Ad Blocker iOS App]]
- [[initiatives/pyloop|Build PyLoop — Custom Python Agent Harness]]
