---
tags:
  - library
title: "chezmoi-dotfiles/dot_claude/skills/empirical-prompt-tuning/SKILL.md at main · mizchi/chezmoi-dotfiles"
url: "https://github.com/mizchi/chezmoi-dotfiles/blob/main/dot_claude/skills/empirical-prompt-tuning/SKILL.md"
company: [personal]
topics: []
created: 2026-04-21
source_type: raindrop
raindrop_id: 1691696422
source_domain: "github.com"
source_type_raindrop: link
collection: "unsorted"
collection_id: -1
hydrated: true
hydrated_at: 2026-04-22
hydrated_via: github-api
---
## Excerpt

Contribute to mizchi/chezmoi-dotfiles development by creating an account on GitHub.

## Raw Content

<!-- Hydrated 2026-04-22 via github-api -->

# chezmoi-dotfiles

macOS dotfiles managed with [chezmoi](https://www.chezmoi.io/).

## Structure

```
dot_zshrc                 # ~/.zshrc
dot_config/
├── helix/                # Helix editor
├── mise/                 # mise (asdf alternative)
├── sheldon/              # zsh plugin manager
├── starship.toml         # Starship prompt
├── zellij/               # Terminal multiplexer
└── zsh/
    ├── path.zsh          # PATH settings
    ├── functions.zsh     # Shell functions (ghq/fzf)
    └── just.zsh          # just completions
dot_claude/
├── CLAUDE.md             # Claude Code instructions
├── settings.json         # Claude Code settings
└── skills/               # Claude Code skills
    ├── jj/               # Jujutsu VCS
    ├── justfile/         # just command runner
    ├── devbox/           # Nix-based dev environments
    ├── dotenvx/          # Environment variable management
    ├── moonbit-*/        # MoonBit language
    └── agentskills/      # Agent skills docs
```

## Install

```bash
chezmoi init https://github.com/mizchi/chezmoi-dotfiles.git
chezmoi apply

# Setup skills symlinks
~/.claude/skills/install.sh
```

## Pre-commit

Uses [prek](https://github.com/j178/prek) with [secretlint](https://github.com/secretlint/secretlint) to prevent committing secrets.

```bash
prek install
```
