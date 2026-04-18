---
tags:
  - library
title: "OpenClaw - OpenClaw"
url: "https://docs.openclaw.ai/"
company: [personal]
topics: []
created: 2026-02-10
source_type: raindrop
raindrop_id: 1592203290
source_domain: "docs.openclaw.ai"
source_type_raindrop: link
collection: "Dev Tools & CLI"
collection_id: 69292902
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: OpenClaw - OpenClaw

URL Source: https://docs.openclaw.ai/

Markdown Content:
![Image 1: OpenClaw](https://mintcdn.com/clawdhub/-t5HSeZ3Y_0_wH4i/assets/openclaw-logo-text-dark.png?fit=max&auto=format&n=-t5HSeZ3Y_0_wH4i&q=85&s=61797dcb0c37d6e9279b8c5ad2e850e4)![Image 2: OpenClaw](https://mintcdn.com/clawdhub/FaXdIfo7gPK_jSWb/assets/openclaw-logo-text.png?fit=max&auto=format&n=FaXdIfo7gPK_jSWb&q=85&s=d799bea41acb92d4c9fd1075c575879f)

> _“EXFOLIATE! EXFOLIATE!”_ — A space lobster, probably

**Any OS gateway for AI agents across Discord, Google Chat, iMessage, Matrix, Microsoft Teams, Signal, Slack, Telegram, WhatsApp, Zalo, and more.**

 Send a message, get an agent response from your pocket. Run one Gateway across built-in channels, bundled channel plugins, WebChat, and mobile nodes.

## What is OpenClaw?

OpenClaw is a **self-hosted gateway** that connects your favorite chat apps and channel surfaces — built-in channels plus bundled or external channel plugins such as Discord, Google Chat, iMessage, Matrix, Microsoft Teams, Signal, Slack, Telegram, WhatsApp, Zalo, and more — to AI coding agents like Pi. You run a single Gateway process on your own machine (or a server), and it becomes the bridge between your messaging apps and an always-available AI assistant.**Who is it for?** Developers and power users who want a personal AI assistant they can message from anywhere — without giving up control of their data or relying on a hosted service.**What makes it different?**

*   **Self-hosted**: runs on your hardware, your rules
*   **Multi-channel**: one Gateway serves built-in channels plus bundled or external channel plugins simultaneously
*   **Agent-native**: built for coding agents with tool use, sessions, memory, and multi-agent routing
*   **Open source**: MIT licensed, community-driven

**What do you need?** Node 24 (recommended), or Node 22 LTS (`22.14+`) for compatibility, an API key from your chosen provider, and 5 minutes. For best quality and security, use the strongest latest-generation model available.

## How it works

The Gateway is the single source of truth for sessions, routing, and channel connections.

## Key capabilities

## Quick start

1

2

3

Need the full install and dev setup? See [Getting Started](https://docs.openclaw.ai/start/getting-started).

## Dashboard

Open the browser Control UI after the Gateway starts.

*   Local default: [http://127.0.0.1:18789/](http://127.0.0.1:18789/)
*   Remote access: [Web surfaces](https://docs.openclaw.ai/web) and [Tailscale](https://docs.openclaw.ai/gateway/tailscale)

![Image 3: OpenClaw](https://mintcdn.com/clawdhub/FaXdIfo7gPK_jSWb/whatsapp-openclaw.jpg?fit=max&auto=format&n=FaXdIfo7gPK_jSWb&q=85&s=b74a3630b0e971f466eff15fbdc642cb)

## Configuration (optional)

Config lives at `~/.openclaw/openclaw.json`.

*   If you **do nothing**, OpenClaw uses the bundled Pi binary in RPC mode with per-sender sessions.
*   If you want to lock it down, start with `channels.whatsapp.allowFrom` and (for groups) mention rules.

Example:

```
{
  channels: {
    whatsapp: {
      allowFrom: ["+15555550123"],
      groups: { "*": { requireMention: true } },
    },
  },
  messages: { groupChat: { mentionPatterns: ["@openclaw"] } },
}
```

## Start here

## Learn more
