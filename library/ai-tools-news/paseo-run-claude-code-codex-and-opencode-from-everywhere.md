---
tags:
  - library
title: "Paseo – Run Claude Code, Codex, and OpenCode from everywhere"
url: "https://paseo.sh/"
company: [personal]
topics: []
created: 2026-04-11
source_type: raindrop
raindrop_id: 1680988949
source_domain: "paseo.sh"
source_type_raindrop: link
collection: "AI Tools & News"
collection_id: 69284314
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

A self-hosted daemon for Claude Code, Codex, and OpenCode. Agents run on your machine with your full dev environment. Connect from phone, desktop, or web.

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: Paseo – Run Claude Code, Codex, and OpenCode from everywhere

URL Source: https://paseo.sh/

Markdown Content:
# Paseo – Run Claude Code, Codex, and OpenCode from everywhere

[![Image 1: Paseo](https://paseo.sh/logo.svg)Paseo](https://paseo.sh/)

[Blog](https://paseo.sh/blog)[Docs](https://paseo.sh/docs)[Changelog](https://paseo.sh/changelog)[Download](https://paseo.sh/download)[](https://discord.gg/jz8T2uahpH)[4.0k](https://github.com/getpaseo/paseo)

# Orchestrate coding agents

from your desk and your phone

Run any coding agent from your phone, desktop, or terminal. Self-hosted, multi-provider, open source.

[Download for Mac](https://github.com/getpaseo/paseo/releases/download/v0.1.59/Paseo-0.1.59-arm64.dmg)[Web App](https://app.paseo.sh/)[](https://apps.apple.com/app/paseo-pocket-engineer/id6758887924)[](https://play.google.com/store/apps/details?id=sh.paseo)

[All download options](https://paseo.sh/download)

Supports

Sessions

A

acme/returns-app

main

+247-15

feat/dashboard

#142 ·Open

P

acme/payments

main

fix/stripe-webhook

+38-4

#89 ·Merged

I

acme/infra

main

feat/k8s-autoscale

+91-3

D

acme/design-system

main

MacBook Pro

main acme/returns-app

Commit

+247-15

Orchestrator

Implement

Review

Build me an internal dashboard for tracking customer returns

I'll break this down into planning and implementation.

Run plan-technical codex · plan-technical

Run plan-design claude · plan-design

Wait for agents plan-technical plan-design

Got the plans. Spinning up Codex for implementation.

Run implement codex · 12 files changed

Implementation done. Requesting review from Claude.

Run review claude · no issues found

All tasks complete. Dashboard is ready.

Message the agent, tag @files, or use /commands and /skills

Opus 4.6

npm run dev

`$ npm run dev`

`> acme-returns@0.1.0 dev`

`> next dev --turbopack`

`▲ Next.js 15.3.1 (Turbopack)`

`- Local:   http://localhost:3000`

`✓ Starting...`

`✓ Ready in 1.2s`

`○ Compiling /dashboard ...`

`✓ Compiled /dashboard in 340ms`

`○ Compiling /api/returns ...`

`✓ Compiled /api/returns in 120ms`

Changes

Files

Uncommitted

dashboard.tsx src/pages New

+16-0

`1`

`import { useState } from "react"`

`2`

`import { ReturnTable } from "./components"`

`3`

`4`

`export function Dashboard() {`

`5`

`const [returns, setReturns] = useState([])`

`6`

`const [filter, setFilter] = useState("all")`

`7`

`8`

`return (`

`9`

`<main className="min-h-screen p-8">`

`10`

`<h1>Customer Returns</h1>`

`11`

`<FilterBar value={filter} onChange={setFilter} />`

`12`

`<ReturnTable data={returns} />`

`13`

`<StatusChart data={returns} />`

`14`

`</main>`

`15`

`)`

`16`

`}`

return-table.tsx src/components

+42-8

filter-bar.tsx src/components

+28-3

status-chart.tsx src/components New

+19-0

returns.ts src/api

+12-5

index.tsx src/pages

+6-2

When you want to step away from your desk,

 you can.

The native mobile app has full feature parity with desktop.

![Image 2: Paseo sessions list](https://paseo.sh/phone-1.png)

![Image 3: Paseo agent chat](https://paseo.sh/phone-2.png)

![Image 4: Paseo diff view](https://paseo.sh/phone-3.png)

## Use the best agent for the job

Run multiple providers from a single interface. Paseo runs the native agent harness as you'd normally run it, with your skills, config and MCP servers intact.

Claude Code

Codex

OpenCode

Copilot

Pi

## Your agents, every surface

Run agents on your laptop, a VM, or a dev server. Control them from any device with a direct connection or an E2E encrypted relay.

Desktop

Web

Mobile

CLI

E2E Encrypted Relay

or

Direct Connection

MacBook Pro

Hetzner VM

Dev server

Desktop

Web

Mobile

CLI

E2E Encrypted Relay

or

Direct Connection

MacBook Pro

Hetzner VM

Dev server

## Forget about ports

When agents work in parallel, they all run dev servers. Paseo gives each one a URL based on the branch name, no port conflicts, no guessing.

my-app

fix-auth npm run dev

web.fix-auth.my-app.localhost

add-search npm run dev

web.add-search.my-app.localhost

upgrade-deps npm run dev

web.upgrade-deps.my-app.localhost

## Keyboard-first

Every action has a shortcut. Panels, splits, agents - all from the keyboard.

Switch panels

⌘1-9

Split vertical

⌘D

Split horizontal

⌘Shift D

Close panel

⌘W

New agent

⌘N

Command palette

⌘K

## Local voice

Fully local voice stack. Speech-to-text and text-to-speech run entirely on your machine, nothing leaves your network.

Refactor the auth middleware to use the new session store, then run the test suite

I'll update the auth middleware to use SessionStore instead of the legacy cookie-based approach. Let me refactor the middleware and update the tests.

## Fully scriptable

Everything you can do in the app, you can do from the terminal.

Run agents Loops Schedules

paseo run "implement user authentication"
paseo run --provider codex --worktree feature-x "implement feature X"
paseo run --host devbox:6767 "run the full test suite"

paseo ls                           # list running agents
paseo attach abc123                # stream live output
paseo send abc123 "also add tests" # follow-up task

[Full CLI reference](https://paseo.sh/docs/cli)

## FAQ

+−Is this free?

Yes. Paseo is free and open source. You need Claude Code, Codex, or OpenCode installed with your own credentials. Voice is local-first by default and can optionally use OpenAI speech providers if you configure them.

+−Does my code leave my machine?

Paseo doesn't send your code anywhere. Agents run locally and talk to their own APIs as they normally would. For remote access, you can use the optional[end-to-end encrypted relay](https://paseo.sh/docs/security), connect directly over your local network, or use your own tunnel.

+−What agents does it support?

Claude Code, Codex, and OpenCode. Each agent runs as its own process using its own CLI. Paseo doesn't modify or wrap their behavior.

+−Do I need the desktop app?

No. You can run the daemon headless with`npm install -g @getpaseo/cli && paseo`and use the CLI, web app, or mobile app to connect. The desktop app just bundles the daemon with a UI.

+−How does voice work?

Voice runs locally on your device by default. You talk, the app transcribes and sends it to your agent as text. Optionally, you can configure OpenAI speech providers for higher-quality transcription and text-to-speech. See the[voice docs](https://paseo.sh/docs/voice).

+−Can I connect from outside my network?

Yes. You can use the hosted relay (end-to-end encrypted, Paseo can't read your traffic), set up your own tunnel (Tailscale, Cloudflare Tunnel, etc.), or expose the daemon port directly. See[configuration](https://paseo.sh/docs/configuration).

+−Do I need git or GitHub?

No. Paseo works in any directory. Worktrees are optional and only relevant if you use git. You can run agents anywhere you'd normally work.

+−Can I get banned for using Paseo?

We can't make promises on behalf of providers.

That said, Paseo launches the official first-party CLIs (Claude Code, Codex, OpenCode) as subprocesses. It doesn't extract tokens or call inference APIs directly. From the provider's perspective, usage through Paseo is indistinguishable from running the CLI yourself.

I've been using Paseo with all providers for months without issue.

+−How do worktrees work?

When you launch an agent with the worktree option (from the app, desktop, or CLI), Paseo creates a git worktree and runs the agent inside it. The agent works on an isolated branch without touching your main working directory. See the[worktrees docs](https://paseo.sh/docs/worktrees).

I built Paseo because I wanted better tools for coding agents on my own setup. It's an independent open source project, built around freedom of choice and real workflows. If you like what I'm building, consider becoming a supporter.

- Mo

[Sponsor on GitHub](https://github.com/sponsors/boudra)

Product

[Blog](https://paseo.sh/blog)[Docs](https://paseo.sh/docs)[Changelog](https://paseo.sh/changelog)[CLI](https://paseo.sh/docs/cli)[Privacy](https://paseo.sh/privacy)

Agents

[Claude Code](https://paseo.sh/claude-code)[Codex](https://paseo.sh/codex)[OpenCode](https://paseo.sh/opencode)

Community

[Discord](https://discord.gg/jz8T2uahpH)[GitHub](https://github.com/getpaseo/paseo)

Download

[App Store](https://apps.apple.com/app/paseo-pocket-engineer/id6758887924)[Google Play](https://play.google.com/store/apps/details?id=sh.paseo)[Desktop](https://github.com/getpaseo/paseo/releases)[Web App](https://app.paseo.sh/)
