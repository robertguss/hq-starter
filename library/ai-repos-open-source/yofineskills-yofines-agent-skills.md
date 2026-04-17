---
tags:
  - library
title: "yofine/skills: yofine's agent skills"
url: "https://github.com/yofine/skills"
company: [personal]
topics: []
created: 2026-04-09
source_type: raindrop
raindrop_id: 1678020845
source_domain: "github.com"
source_type_raindrop: link
collection: "AI Repos & Open Source"
collection_id: 69284315
hydrated: true
hydrated_at: 2026-04-17
hydrated_via: github-api
---
## Excerpt

yofine's agent skills. Contribute to yofine/skills development by creating an account on GitHub.

## Raw Content

<!-- Hydrated 2026-04-17 via github-api -->

# Skills

My personal collection of AI agent skills.

## Overview

This repository contains reusable skills that extend AI agent capabilities. Each skill is a self-contained module that teaches an agent how to perform specific tasks.

## Project Structure

```
skills/
├── blueprinter/      # Technical diagram generation skill
└── README.md
```

## Available Skills

| Skill | Description |
|-------|-------------|
| [blueprinter](./blueprinter/) | Generate technical diagrams in Flat Engineering Blueprint style using HTML/CSS |

### Example: Blueprinter Output

![Claude Code Architecture Blueprint](./images/claudecodesource.png)

## Skill Structure

Each skill contains:

```
skill-name/
└── SKILL.md    # Skill definition with instructions for the agent
```

### SKILL.md Format

```yaml
---
name: skill-name
description: When and how to use this skill
---

# Skill content and instructions...
```

## License

MIT
## Star History

[![Star History Chart](https://api.star-history.com/image?repos=yofine/skills&type=date&legend=top-left)](https://www.star-history.com/?repos=yofine%2Fskills&type=date&legend=top-left)

<br/>
