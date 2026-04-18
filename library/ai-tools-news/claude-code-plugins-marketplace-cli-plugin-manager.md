---
tags:
  - library
title: "Claude Code Plugins - Marketplace & CLI Plugin Manager"
url: "https://claude-plugins.dev/"
company: [personal]
topics: []
created: 2025-12-12
source_type: raindrop
raindrop_id: 1486086331
source_domain: "claude-plugins.dev"
source_type_raindrop: link
collection: "AI Tools & News"
collection_id: 69284314
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

Install Claude Code plugins directly without manually adding marketplaces first. Simple CLI tool that handles marketplace setup automatically. Browse and install from indexed public plugins.

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: Claude Code Plugins & Agent Skills - Community Registry with CLI

URL Source: https://claude-plugins.dev/

Markdown Content:
# Claude Code Plugins & Agent Skills - Community Registry with CLI

[Claude Code Plugins](https://claude-plugins.dev/)
Community-maintained marketplace

[Feedback](https://discord.gg/K4TbR3d7)[](https://discord.gg/Pt9uN4FXR4)[](https://github.com/Kamalnrf/claude-plugins)

Browse Claude Plugins Browse Agent Skills

# Manage Claude Code plugins with ease

Discover and Install **Claude Code plugins**, even ones with [skills](https://www.anthropic.com/news/skills) quickly. Claude Code normally requires installing a marketplace, then installing plugins from it. This CLI handles both steps automatically in one command. Browse plugins with skills to extend Claude's capabilities—discover AI agents, document processors, and more. [Open-source](https://github.com/Kamalnrf/claude-plugins) and community-maintained.

built with

bun[Val Town](https://www.val.town/x/kamalnrf/claude-plugins-registry)Claude Code 😉

## Quick Start

Install a plugin from the marketplace:

$`npx claude-plugins install <unique-plugin-identifier>`

List all installed plugins:

$`npx claude-plugins list`

Enable or Disable:

$`npx claude-plugins enable <plugin-name>`

$`npx claude-plugins disable <plugin-name>`

Requires Claude Code v2.0.12 or higher. [Learn more →](https://github.com/Kamalnrf/claude-plugins)

## Plugins

With Skills

frontend-design

[@anthropics/claude-code-plugins](https://github.com/anthropics/claude-code)

65.1k

8.9k

development

Create distinctive, production-grade frontend interfaces with high design quality. Generates creative, polished code that avoids generic AI aesthetics.

$npx claude-plugins install @anthropics/claude-code-plugins/frontend-design

document-skills

[@anthropics/anthropic-agent-skills](https://github.com/anthropics/skills)

119.5k

7k

Skills

xlsx docx pptx

Show 1 more skill

Collection of document processing suite including Excel, Word, PowerPoint, and PDF capabilities

$npx claude-plugins install @anthropics/anthropic-agent-skills/document-skills

compound-engineering

[@EveryInc/every-marketplace](https://github.com/EveryInc/compound-engineering-plugin)

8.9k

4.7k

ai-powered compound-engineering workflow-automation

AI-powered development tools that get smarter with every use. Make each unit of engineering work easier than the last. Includes 29 specialized agents, 22 commands, and 19 skills.

$npx claude-plugins install @EveryInc/every-marketplace/compound-engineering

code-review

[@anthropics/claude-code-plugins](https://github.com/anthropics/claude-code)

65.1k

3.5k

productivity

Automated code review for pull requests using multiple specialized agents with confidence-based scoring to filter false positives

$npx claude-plugins install @anthropics/claude-code-plugins/code-review

feature-dev

[@anthropics/claude-code-plugins](https://github.com/anthropics/claude-code)

65.1k

3.5k

development

Comprehensive feature development workflow with specialized agents for codebase exploration, architecture design, and quality review

$npx claude-plugins install @anthropics/claude-code-plugins/feature-dev

python-development

[@wshobson/claude-code-workflows](https://github.com/wshobson/agents)

33.7k

2.2k

languages

Modern Python development with Python 3.12+, Django, FastAPI, async patterns, and production best practices

$npx claude-plugins install @wshobson/claude-code-workflows/python-development

pr-review-toolkit

[@anthropics/claude-code-plugins](https://github.com/anthropics/claude-code)

65.1k

2.2k

productivity

Comprehensive PR review agents specializing in comments, tests, error handling, type design, code quality, and code simplification

$npx claude-plugins install @anthropics/claude-code-plugins/pr-review-toolkit

backend-development

[@wshobson/claude-code-workflows](https://github.com/wshobson/agents)

33.7k

1.9k

development

Backend API design, GraphQL architecture, workflow orchestration with Temporal, and test-driven backend development

$npx claude-plugins install @wshobson/claude-code-workflows/backend-development

code-refactoring

[@wshobson/claude-code-workflows](https://github.com/wshobson/agents)

33.7k

1.8k

utilities

Code cleanup, refactoring automation, and technical debt management with context restoration

$npx claude-plugins install @wshobson/claude-code-workflows/code-refactoring

security-guidance

[@anthropics/claude-code-plugins](https://github.com/anthropics/claude-code)

65.1k

1.8k

security

Security reminder hook that warns about potential security issues when editing files, including command injection, XSS, and unsafe code patterns

$npx claude-plugins install @anthropics/claude-code-plugins/security-guidance

context7

[@anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official)

17.1k

1.7k

development community-managed

Upstash Context7 MCP server for up-to-date documentation lookup. Pull version-specific documentation and code examples directly from source repositories into your LLM context.

$npx claude-plugins install @anthropics/claude-plugins-official/context7

javascript-typescript

[@wshobson/claude-code-workflows](https://github.com/wshobson/agents)

33.7k

1.7k

languages

JavaScript and TypeScript development with ES6+, Node.js, React, and modern web frameworks

$npx claude-plugins install @wshobson/claude-code-workflows/javascript-typescript

commit-commands

[@anthropics/claude-code-plugins](https://github.com/anthropics/claude-code)

65.1k

1.6k

productivity

Commands for git commit workflows including commit, push, and PR creation

$npx claude-plugins install @anthropics/claude-code-plugins/commit-commands

database-design

[@wshobson/claude-code-workflows](https://github.com/wshobson/agents)

33.7k

1.5k

database

Database architecture, schema design, and SQL optimization for production systems

$npx claude-plugins install @wshobson/claude-code-workflows/database-design

ui-designer

[@ananddtyagi/claude-code-marketplace](https://github.com/ananddtyagi/claude-code-marketplace)

527

1.4k

agents subagent

Use this agent when creating user interfaces, designing components, building design systems, or improving visual aesthetics. This agent specializes in creating beautiful, functional interfaces that can be implemented quickly within 6-day sprints. Examples:\n\n<example>\nContext: Starting a new app or feature design

$npx claude-plugins install @ananddtyagi/claude-code-marketplace/ui-designer

code-documentation

[@wshobson/claude-code-workflows](https://github.com/wshobson/agents)

33.7k

1.1k

documentation

Documentation generation, code explanation, and technical writing with automated doc generation and tutorial creation

$npx claude-plugins install @wshobson/claude-code-workflows/code-documentation

agent-sdk-dev

[@anthropics/claude-code-plugins](https://github.com/anthropics/claude-code)

65.1k

1.1k

development

Development kit for working with the Claude Agent SDK

$npx claude-plugins install @anthropics/claude-code-plugins/agent-sdk-dev

context-management

[@wshobson/claude-code-workflows](https://github.com/wshobson/agents)

33.7k

1.1k

ai-ml

Context persistence, restoration, and long-running conversation management

$npx claude-plugins install @wshobson/claude-code-workflows/context-management

typescript-lsp

[@anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official)

17.1k

1.1k

development

TypeScript/JavaScript language server for enhanced code intelligence

$npx claude-plugins install @anthropics/claude-plugins-official/typescript-lsp

agent-orchestration

[@wshobson/claude-code-workflows](https://github.com/wshobson/agents)

33.7k

973

ai-ml

Multi-agent system optimization, agent improvement workflows, and context management

$npx claude-plugins install @wshobson/claude-code-workflows/agent-orchestration
