---
tags:
  - library
title: "herdr — tmux for agents"
url: "https://herdr.dev/"
company: [personal]
topics: []
created: 2026-04-22
source_type: raindrop
raindrop_id: 1692897345
source_domain: "herdr.dev"
source_type_raindrop: link
collection: "unsorted"
collection_id: -1
hydrated: true
hydrated_at: 2026-04-22
hydrated_via: defuddle
---
## Excerpt

Persistent terminal multiplexer for coding agents. Detach, reattach, agents keep running.

## Raw Content

<!-- Hydrated 2026-04-22 via defuddle -->

**herdr is an agent multiplexer that lives in your terminal.**

workspaces, tabs, panes. mouse-native: click, drag, split. every agent at a glance: blocked, working, done. detach and reattach, agents keep running. no gui app, no electron, no mac-only native wrapper. you see the agent's own terminal, not someone's interpretation of it.

$ `curl -fsSL https://herdr.dev/install.sh | sh`

<video controls=""><source src="https://herdr.dev/assets/demo.mp4" type="video/mp4"></video>

---

## how it compares

|  | tmux | gui managers | herdr |
| --- | --- | --- | --- |
| persistent sessions | ✓ | — | ✓ |
| detach / reattach | ✓ | — | ✓ |
| panes, tabs, workspaces | ✓ | ✓ | ✓ |
| agent awareness | — | ✓ | ✓ |
| lives in your terminal | ✓ | — | ✓ |
| real terminal views | ✓ | — | ✓ |
| mouse-native | — | ✓ | ✓ |
| lightweight binary | ✓ | — | ✓ |
| agents can orchestrate | ? | ? | ✓ |

---

## persistence

start herdr on your desktop or server. run your agents, split panes, do your work. press **ctrl+b q** to detach. close your terminal, close your laptop; your agents keep running. open a new terminal, run **herdr**, you're back. same session, same panes, same agents.

---

## from anywhere

need to check on your agents from your phone? just ssh in and run herdr. any ssh client works. no app to download, no account to create.

$ ssh you@yourserver

$ herdr

same session, same agents, same state.

---

## lives in your terminal

not a gui window. not a web dashboard. not electron. **herdr runs inside whatever terminal you already use.** a single rust binary, no dependencies, nothing to configure. it even works inside tmux.

ghostty alacritty kitty wezterm iterm2 tmux

---

## supported agents

<table><thead><tr><th>agent</th><th>idle / done</th><th>working</th><th>blocked</th></tr></thead><tbody><tr><td><a href="https://pi.dev/">pi</a></td><td>✓</td><td>✓</td><td>partial</td></tr><tr><td><a href="https://docs.anthropic.com/en/docs/claude-code">claude code</a></td><td>✓</td><td>✓</td><td>✓</td></tr><tr><td><a href="https://github.com/openai/codex">codex</a></td><td>✓</td><td>✓</td><td>✓</td></tr><tr><td><a href="https://factory.ai/">droid</a></td><td>✓</td><td>✓</td><td>✓</td></tr><tr><td><a href="https://ampcode.com/">amp</a></td><td>✓</td><td>✓</td><td>✓</td></tr><tr><td><a href="https://github.com/anomalyco/opencode">opencode</a></td><td>✓</td><td>✓</td><td>✓</td></tr><tr><td><a href="https://github.com/google-gemini/gemini-cli">gemini cli</a></td><td colspan="3">detected, not fully tested</td></tr><tr><td><a href="https://cursor.com/cli">cursor agent</a></td><td colspan="3">detected, not fully tested</td></tr><tr><td><a href="https://github.com/cline/cline">cline</a></td><td colspan="3">detected, not fully tested</td></tr></tbody></table>

---

## socket api

**agents can use herdr too.** the local unix socket lets agents create workspaces, split panes, spawn other agents, read output, and wait for state changes.

available as CLI commands or as a reusable agent skill.

[socket api →](https://github.com/ogulcancelik/herdr/blob/master/SOCKET_API.md) [agent skill →](https://github.com/ogulcancelik/herdr/blob/master/SKILL.md)

```
# create a workspace and tab
herdr workspace create --cwd ~/project --label "api"
herdr tab create --label "logs"

# split a pane and run
herdr pane split 1-1 --direction right
herdr pane run 1-2 "npm test"

# wait for an agent
herdr wait agent-status 1-1 --status done

# read output
herdr pane read 1-2 --source recent --lines 50
```
