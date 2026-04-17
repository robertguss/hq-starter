---
tags:
  - library
title: "robertguss/tally"
url: "https://github.com/robertguss/tally"
company: [personal]
topics: []
created: 2026-01-05
source_type: raindrop
raindrop_id: 1526335470
source_domain: "github.com"
source_type_raindrop: link
collection: "AI Repos & Open Source"
collection_id: 69284315
hydrated: true
hydrated_at: 2026-04-17
hydrated_via: github-api
---
## Excerpt

Let agents classify your bank transactions

## Raw Content

<!-- Hydrated 2026-04-17 via github-api -->

# Tally

**A local rule engine for transaction classification.** Pair it with an AI assistant to eliminate the manual work.

Works with Claude Code, Codex, Copilot, Cursor, or any command-line AI agent.

## Install

**Linux / macOS**
```bash
curl -fsSL https://tallyai.money/install.sh | bash
```

**PowerShell**
```powershell
irm https://tallyai.money/install.ps1 | iex
```

## Quick Start

```bash
tally init ./my-budget      # Create budget folder
cd my-budget
tally workflow              # See next steps
```

Tell your AI assistant: *"Use tally to categorize my transactions"*

## Documentation

Full documentation is available at **[tallyai.money](https://tallyai.money)**:

- [Quick Start](https://tallyai.money/quickstart.html) - Get running in 5 minutes
- [Guide](https://tallyai.money/guide.html) - Using Tally with AI assistants
- [Reference](https://tallyai.money/reference.html) - merchants.rules and views.rules syntax
- [Formats](https://tallyai.money/formats.html) - settings.yaml and CSV format strings

## Commands

| Command | Description |
|---------|-------------|
| `tally init` | Create a new budget folder |
| `tally workflow` | Show context-aware next steps |
| `tally run` | Generate HTML spending report |
| `tally discover` | Find uncategorized transactions |
| `tally explain` | Explain merchant classifications |
| `tally inspect` | Analyze CSV structure |
| `tally reference` | Show full syntax reference |

## License

MIT
