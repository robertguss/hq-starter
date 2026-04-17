---
tags:
  - library
title: "Railly/agentfiles: Discover, organize, and edit AI coding agent skills across Claude Code, Cursor, Codex, Windsurf, and more, from inside Obsidian."
url: "https://github.com/Railly/agentfiles"
company: [personal]
topics: []
created: 2026-03-29
source_type: raindrop
raindrop_id: 1664709009
source_domain: "github.com"
source_type_raindrop: link
collection: "AI Repos & Open Source"
collection_id: 69284315
hydrated: true
hydrated_at: 2026-04-17
hydrated_via: github-api
---
## Excerpt

Discover, organize, and edit AI coding agent skills across Claude Code, Cursor, Codex, Windsurf, and more, from inside Obsidian. - Railly/agentfiles

## Raw Content

<!-- Hydrated 2026-04-17 via github-api -->

# Agentfiles

AI skills manager for Obsidian. Browse, create, and manage skills across Claude Code, Cursor, Codex, Windsurf, and 10+ coding agents.

![Browse skills, commands, and agents across 13+ coding assistants](assets/browse.jpeg)

![Dashboard with burn rate, context tax, and health metrics](assets/dashboard.jpeg)

## Install

### From Obsidian (coming soon)

Search **Agentfiles** in Settings > Community plugins.

### Manual

1. Download `main.js`, `manifest.json`, and `styles.css` from the [latest release](https://github.com/Railly/agentfiles/releases/latest)
2. Create `<vault>/.obsidian/plugins/agentfiles/`
3. Copy the three files into that folder
4. Enable in Settings > Community plugins

### Optional: skillkit analytics

```bash
npm i -g @crafter/skillkit
skillkit scan
```

## What it does

- **Browse** skills, commands, and agents from 13+ tools in one place
- **Search** by name or file content with deep search toggle
- **Create** new skills with a stepped wizard (pick tool, type, name)
- **Edit** skills inline with markdown preview and Cmd+S save
- **Marketplace** — install skills from [skills.sh](https://skills.sh)
- **Conversations** — browse Claude Code session history, search, tag, and export to vault
- **Dashboard** — usage analytics, burn rate, context tax, health metrics (requires [skillkit](https://www.npmjs.com/package/@crafter/skillkit))

## Supported tools

| Tool | Skills | Commands | Agents |
|------|--------|----------|--------|
| Claude Code | `~/.claude/skills/` | `~/.claude/commands/` | `~/.claude/agents/` |
| Cursor | `~/.cursor/skills/` | | `~/.cursor/agents/` |
| Codex | `~/.codex/skills/` | `~/.codex/prompts/` | `~/.codex/agents/` |
| Windsurf | `~/.codeium/windsurf/memories/` | | |
| Copilot | `~/.copilot/skills/` | | |
| Amp | `~/.config/amp/skills/` | | |
| OpenCode | `~/.config/opencode/skills/` | | |
| Global | `~/.agents/skills/` | | |

Desktop only (macOS, Windows, Linux) — reads files outside your vault.

## License

MIT
