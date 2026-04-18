---
tags:
  - library
title: "You might never open your editor again | Sidecar"
url: "https://sidecar.haplab.com/"
company: [personal]
topics: []
created: 2026-02-09
source_type: raindrop
raindrop_id: 1589940378
source_domain: "sidecar.haplab.com"
source_type_raindrop: link
collection: "AI Tools & News"
collection_id: 69284314
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

Use sidecar for planning features, managing workspaces, reviewing diffs, and staging commits. It's the most fun you can have in a terminal.

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: You might never open your editor again | Sidecar

URL Source: https://sidecar.haplab.com/

Published Time: Thu, 05 Mar 2026 17:57:37 GMT

Markdown Content:
Give agents structured work so they can operate autonomously for longer. Tasks persist across context windows, keeping agents on track with clear objectives. Built-in review workflow lets you verify work before moving to the next task.

Split-pane diffs, commit context, fast staging—all without bouncing to an IDE.

Navigate your codebase with a tree view, preview file contents, and jump to any file instantly.

All your agents in one timeline—Claude, Cursor, Gemini, Amp, Kiro, Pi, and more. Search across sessions, pick up where any agent left off.

Create workspaces, pass tasks from td, kick off with configured prompts—no git commands needed. Everything is automatic.

## The Sidecar Workflow

### 1. Plan

Create tasks in [td](https://td.haplab.com/) to give agents clear objectives and context.

### 2. Act

Your agent (Claude, Cursor, etc.) reads the task and writes code.

### 3. Monitor

Watch the agent's progress, diffs, and logs in Sidecar's TUI.

### 4. Review

Verify the changes, commit, and mark the task as done.

## Sidecar's Features

### Plan with [td](https://td.haplab.com/)

Structured work keeps agents focused and autonomous

Tasks persist across context window resets

Built-in review workflow: verify before moving on

Hierarchical subtasks break down complex work

Status tracking: pending, in_progress, blocked, done

Epics group related tasks for larger features

Integrate with git commits and PRs

Current Work

td-a1b2c3 in_progress Implement auth flow

Board

REV td-d4e5f6 Add rate limiting

RDY td-g7h8i9 Fix memory leak

RDY td-j0k1l2 Update API docs

Activity

00:39 td-a1b2c3 Started

00:15 td-d4e5f6 Submitted for review

### Git Status & Diff

Real-time status of staged and unstaged changes

Inline diff viewer with syntax highlighting

Stage/unstage files with single keypress

Commit directly from the interface

View commit history and messages

Branch switching and creation

Stash management

internal/auth/middleware.go

@@ -42,6 +42,14 @@

+func AuthMiddleware(next) {

+ return http.HandlerFunc(w, r) {

+ token := r.Header.Get("Auth")

+ if !ValidateJWT(token) {

+ http.Error(w, "Unauth", 401)

+ }

+ })

+}

### File Browser

Tree view with expand/collapse

File preview with syntax highlighting

Quick jump with fuzzy search

Show git status indicators on files

Open files in external editor

Navigate to file from other plugins

Respect .gitignore patterns

middleware.go | 156 lines | Go

package auth

import (

"net/http"

"strings"

)

// AuthMiddleware validates requests

func AuthMiddleware(next)...

### Unified Conversation Timeline

Chronological view across all coding agents

Claude, Cursor, Gemini, Codex, Amp, Kiro, Pi, Opencode, and Warp in one list

Search across all adapters at once

Filter by agent, date, or content

Expand messages and view tool calls

Token usage and session duration stats

Copy and export conversation content

User

Add JWT auth to the API endpoints

Claude

I'll implement JWT auth for your API.

Let me check the existing auth setup...

-> Read middleware.go

-> Edit jwt.go

-> Write auth_test.go

### Zero-Command Workspace Workflow

No git commands needed--everything is automatic

Pass tasks directly from td to new workspaces

Configure prompt sequences to kick off agents

Create, switch, merge, delete with single keys

PR status and CI checks at a glance

Auto-cleanup after merge

Linked task tracking across workspaces

feature/auth

PR:#47 Add JWT auth

Task:td-a1b2c3 from td

Status:Ready to merge

Quick actions

[n] New workspace + agent

[s] Send task from td

[p] Run prompt sequence

[m] Merge & cleanup

## Additional Features

Just add a couple lines to your AGENTS.md file. No hooks, no agent modifications. Easy to add, easy to remove.

Launches in milliseconds. No waiting for heavy runtimes or dependency resolution.

Switch between plugins instantly with tab/shift-tab. Each plugin is a focused view of your project.

Click, scroll, and navigate with your mouse. Almost every element in the TUI responds to mouse interaction.

Sidecar checks for updates automatically and can update itself in place. Always stay on the latest version.

Works with Claude Code, Codex, Gemini CLI, Opencode, Cursor, Amp Code, Kiro, Pi, and Warp.

Deep integration with git: status, diff, staging, commits, branches, and workspaces.

Built-in themes plus a community theme browser with live previews. Customize colors to match your terminal aesthetic.

Switch back and forth between projects with @. Cursor position, active plugin, and view preferences restore per-project.

Designed to run in a tmux pane beside your agent. Attach and detach seamlessly.

j/k navigation, /search, and familiar modal interactions. Your muscle memory works here.

MIT licensed. Inspect the code, contribute features, or fork for your needs.

No dependencies to install. Download one binary and you're ready to go.

## Even more features

Command Palette

Project Switcher

Split Panes

Diagnostics Overlay

Fuzzy File Finder

Ripgrep Search

Git Graph

Kanban Workspaces

Task Linking

External Editor

System Clipboard

Vim Navigation

Merge Workflow

Worktree Switcher

Global Refresh

Theme Switching

Lightweight

Inline Editor

## Supported Agents

Sidecar reads session data from multiple AI coding tools, giving you a unified view of agent activity

### Claude Code

Anthropic's official CLI for Claude

### Codex

OpenAI's code generation model

### Gemini CLI

Google's multimodal AI assistant

### Opencode

Terminal-first AI coding assistant

### Cursor

AI-first code editor (cursor-agent)

### Amp Code

Amp's AI coding assistant

### Kiro

Amazon's AI coding assistant

### Pi

Pi AI agent (OpenClaw)

### Warp

Warp terminal AI assistant

Each agent stores session data in its own format. Sidecar normalizes and displays them in a unified interface.

## Get started in seconds

$ curl -fsSL https://raw.githubusercontent.com/marcus/sidecar/main/scripts/setup.sh | bash

Also available via

## Sister Projects

[![Image 1: Haplab](https://sidecar.haplab.com/img/haplab-logo.png)](https://haplab.com/)
