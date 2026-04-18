---
tags:
  - library
title: "FlowDeck — The Apple Development CLI. Finally."
url: "https://flowdeck.studio/"
company: [personal]
topics: []
created: 2026-04-09
source_type: raindrop
raindrop_id: 1678700728
source_domain: "flowdeck.studio"
source_type_raindrop: link
collection: "Dev Tools & CLI"
collection_id: 69292902
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

Builds. Tests. Simulators. Devices. Logs. Same commands in terminal, CI, or your favorite editor.

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: FlowDeck — The Apple Development CLI. Finally.

URL Source: https://flowdeck.studio/

Markdown Content:
## Stop babysitting your iOS agent

FlowDeck is the complete Apple development loop for Claude Code, Codex CLI, and beyond.

You work from the terminal now. Use the best AI tools. But Xcode still breaks your flow.

Not anymore.

**One unified tool**Replaces Apple's fragmented CLIs

**Structured JSON output**No more parsing xcodebuild walls

**Direct CLI access**No MCP servers, no wasted tokens

**Real-time log streaming**Agents see what breaks instantly

**Skills & plugins**Claude Code, Codex, OpenCode

**UI Automation**Agents see and interact with screens

Your AI writes the code. FlowDeck closes the loop.

`xcodebuild` builds. That's it. You still need a dozen more tools and shell scripts to glue things together. Then figure out how to parse the output.

FlowDeck is the complete workflow: build, run, test, logs, devices.

**8 commands**, structured output, done.

1`xcrun simctl list devices`

2`xcrun simctl boot [UDID]`

3`xcodebuild -scheme App -destination 'platform=iOS Simulator,id=[UDID]'`

4`xcrun simctl install booted [path]`

5`xcrun simctl launch booted [bundle-id]`

`flowdeck run -S "iPhone 16"`

Done.

`B Build  R Run  T Test  K Clean`

### Interactive Mode

Single keystrokes. Zero context switching. No Xcode needed. Your terminal becomes the command center.

`flowdeck simulator boot "iOS 26"``flowdeck simulator erase`

### Simulator Control

Create, Boot, reset, manage platforms.

`flowdeck ui tap "Login"``flowdeck ui swipe up · flowdeck ui screenshot`

### UI Automation

Tap, swipe, pinch, scroll, screenshot. AI agents can see the screen. Close the loop.

`[net] GET /api → 200``[app] loaded user`

### Log Streaming

OSLog in your terminal. 

Beautifully formatted. Live.

`flowdeck project create MyApp`

### Project Creation

From zero to Xcode project in seconds.

`{"success": true}`

### JSON Output

Machine-readable everything. CI ready.

`flowdeck context`

### Context Discovery

One command shows schemes, targets, simulators

Personal

### FlowDeck CLI

$59/year

All updates included

7-day free trial

*    Full CLI access
*    AI agent integrations
*    2 machines per license

Teams

### FlowDeck for Teams

$299/year

5 to 20+ developers

30-day money-back guarantee

*    Centralized billing
*    24h to first response support
*    Project Setup Assistance

![Image 1](blob:http://localhost/aef335eb562a1da6957ce25a574b4aa1)

Before you say "I can build that myself"...

## Yes, We Know

You could stitch this together yourself. 48 open source projects. 102 config files. Mass ChatGPT and SO threads. We'll wait.

Or you can use one command and be done.

Before you @ us on Twitter...

## Yes, We Also Know

You still need Xcode installed. You just don't need to open it.

FlowDeck uses xcodebuild, simulators, and SDKs under the hood.

We didn't replace Xcode. We just made it so you never have to _look_ at it again.

And honestly? That's the dream.

## Join the Community

Share workflows, get help, shape what comes next.

Get help from the developer directly. Share feedback and feature ideas.

## Frequently Asked Questions

Do I still need Xcode installed?
Yes. FlowDeck uses xcodebuild under the hood. Xcode must be installed, but you won't need to open it.

What macOS and Xcode versions are supported?
macOS 13+, Xcode 15+ (16+ recommended).

How does licensing work?
7-day free trial starts when you purchase. After trial, $59/year. License works on 2 machines.

Is my code private?
Yes. Everything runs locally. Your code never leaves your machine.

Why not just use xcodebuild?
You can. FlowDeck doesn't replace Apple's toolchain; it standardizes how you interact with it. Workflow-level commands instead of flags. Structured results instead of text parsing. Same execution semantics whether you're in terminal, CI, or an automation tool.

How much does the CLI cost?
$59/year. Annual license includes all updates and priority support. 7-day free trial.

When do I need a Business license?
If your team needs centralized billing and admin controls. [Contact us](mailto:support@flowdeck.studio) to discuss your needs.

Does it work with my AI subscription?
Yes. FlowDeck works alongside Claude Code, Codex, OpenCode, any terminal-based AI assistant you already use. No changes to your existing subscriptions.

## Looking for FlowDeck for Cursor?

Get the free extension for hands-on iOS development with a visual interface.
