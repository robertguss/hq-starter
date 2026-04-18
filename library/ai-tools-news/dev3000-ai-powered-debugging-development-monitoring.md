---
tags:
  - library
title: "dev3000 - AI-Powered Debugging & Development Monitoring"
url: "https://d3k.vercel.sh/?utm_source=www.theunwindai.com&utm_medium=newsletter&utm_campaign=better-and-open-source-claude-code&_bhlid=d042f9fd1891cbbd34732619e7c4acbcb3d88d9b"
company: [personal]
topics: []
created: 2025-09-10
source_type: raindrop
raindrop_id: 1332708587
source_domain: "d3k.vercel.sh"
source_type_raindrop: link
collection: "AI Tools & News"
collection_id: 69284314
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

Capture your web app's complete development timeline for AI debugging. Unified logs, browser events, and automatic screenshots.

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: dev3000 - AI-Powered Debugging & Development Monitoring

URL Source: https://d3k.vercel.sh/?_bhlid=d042f9fd1891cbbd34732619e7c4acbcb3d88d9b

Markdown Content:
By Vercel Labs

## The AI-enabled browser for development

Run your dev server through dev3000 to capture server logs, browser events, network requests, and screenshots in a unified timeline. Your coding agent gets complete context without you manually copying and pasting.

![Image 1](https://dev3000.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fhero-terminal.0gevr5owsz600.png&w=3840&q=75&dpl=dpl_92NRh1FgMFHjAM4TYLRiFL6uDBuL)![Image 2](https://dev3000.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fhero-app.0ap.uvygn0yb2.png&w=3840&q=75&dpl=dpl_92NRh1FgMFHjAM4TYLRiFL6uDBuL)

Server Logs

Timestamped server logs

Browser Events

Logs, errors & user interactions

Screenshots

Captured on errors & navigation

Network Requests

Complete HTTP requests & responses

## Quick Start

1.   Install dev3000 For the split-screen TUI experience (agent + logs), install [tmux](https://github.com/tmux/tmux) first:

`brew install tmux`
Then install dev3000:

`bun install -g dev3000`
npm and pnpm installs also work. 
2.   Start your dev server Replaces your normal dev command. Starts your dev server & launches a monitored Chrome instance.

`# Instead of running bun run devd3k # or dev3000# Setting a portd3k -p 5000# Custom scriptd3k -s build-start` 
3.   Use your app normally
Interact with your app in the monitored browser. Every log, request, error & page state is captured automatically.

4.   Ask your coding agent to debug
Your agent sees everything: server output, client-side events & visual state at every step.

## Skill Integrations

Works standalone or with skills installed via the skills CLI. d3k ships with a built‑in debugging skill and supports optional packs for Next.js, React performance, and design guidelines.

## Demo

00:00-00:24 00:02 - Start dev3000 00:06 - Server Logs 00:11 - Browser Logs 00:15 - Browser Interactions Keyboard shortcuts (?)Fullscreen (f)

Server Logs

Timestamped server logs

Browser Events

Logs, errors & user interactions

Screenshots

Captured on errors & navigation

Network Requests

Complete HTTP requests & responses

## Frequently Asked Questions

### Which coding agents work with dev3000?

All of them. dev3000 works with any AI coding assistant that can read a skill file or follow CLI output—including Claude Code, Cursor, Windsurf, Codex, and others. It also works standalone in your terminal without any agent.

### Does dev3000 persist browser state between sessions?

Yes. Each project gets a dedicated Chrome profile that preserves login state, cookies, and local storage.

### Can I use Arc or another browser instead of Chrome?

Yes! Use the `--browser` flag with the path to any Chromium-based browser. For Arc: `d3k --browser '/Applications/Arc.app/Contents/MacOS/Arc'`

### Does this only work with Next.js?

No. Works with any framework that runs a dev server—Next.js, Vite, Create React App, Rails, Django, etc. Use `--script` to specify your package.json dev command or `--port` to connect to an existing server.

### How do I stop dev3000?

Ctrl+C terminates the dev server and browser simultaneously.

### Does dev3000 affect my app's performance?

Minimal impact. dev3000 observes browser events passively through Chrome DevTools Protocol. The only overhead is capturing screenshots on errors and navigation, which happens asynchronously.

### Where is my data stored?

All data stays local on your machine. Browser profiles are stored in `~/.dev3000/profiles`, and captured events are kept in memory during your session. Nothing is sent to external servers.

### Can I use dev3000 with my existing dev workflow?

Yes. Replace your normal dev command (`bun run dev`, `npm run dev`, etc.) with `d3k`. Everything else works exactly the same—hot reload, environment variables, custom ports, etc.

### What's the 'sharp' warning during installation?

Ignore it. Sharp is a Next.js image optimization dependency that dev3000 doesn't use. Some package managers run install scripts for all dependencies, but sharp is never invoked at runtime.
