---
tags:
  - library
title: "Blitz · Skip Xcode. Ship with AI."
url: "https://blitz.dev/"
company: [personal]
topics: []
created: 2026-03-22
source_type: raindrop
raindrop_id: 1652773392
source_domain: "blitz.dev"
source_type_raindrop: link
collection: "AI Tools & News"
collection_id: 69284314
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: Blitz — Your AI Agent Can Now Submit iOS Apps

URL Source: https://blitz.dev/

Markdown Content:
## Submit with Agents

Blitz is a free, open-source mac app that lets AI agents submit apps to the App Store.

* * *

![Image 1: Blitz](https://blitz.dev/BlitzBlue.png)Blitz works with Claude Code, Codex, Cursor, OpenCode

![Image 2: Blitz macOS app showing simulator view with sidebar navigation](https://blitz.dev/blitz-app-screenshot.png)

* * *

The new development stack

![Image 3: Claude Code terminal alongside Blitz with an iOS app running in the simulator](https://blitz.dev/dev-stack.png)

* * *

Before![Image 4: App Store submission checklist — all items red, not ready](https://blitz.dev/after_submit_ready.png)

![Image 5](https://blitz.dev/squiggly-arrow.png)

After![Image 6: App Store submission checklist — all items green, ready to submit](https://blitz.dev/before_submit_ready.png)

* * *

* * *

12 Total Apps

5.4h Avg Review Time

36%1st Submit Rejection

0.5 Avg Rejects to Live

[View all on the App Wall →](https://blitz.dev/wall)

* * *

* * *

React Native

![Image 7: Swift](https://blitz.dev/swift-icon.png)

Swift

![Image 8: Flutter](https://blitz.dev/flutter-icon.png)

Flutter

* * *

Can I submit macOS apps with Blitz?
Yes. Blitz supports both iOS and macOS app development. Your agent can build, test, and submit macOS apps to the Mac App Store through the same App Store Connect workflow — metadata, screenshots, code signing, and submission are all handled the same way.

How is Blitz different from Cursor or Windsurf?
Cursor and Windsurf are general-purpose code editors with AI. They help you write code. Blitz isn't a code editor — it's a tool that gives AI agents control over the Apple-platform-specific parts of development that happen outside the editor: simulator management, device interaction, App Store Connect, code signing, and submission. Cursor writes the code, Blitz does everything else. They're complementary.

Does Blitz replace Xcode?
No. You still need Xcode installed for compilation (xcodebuild) and the iOS Simulator runtime. Blitz wraps around Xcode's build tools and adds the agent layer on top. Think of Blitz as the workflow layer between your AI coding agent and Apple's toolchain.

How does the simulator interaction work?
It's real interaction, not just screenshots. Blitz uses simctl (Apple's simulator CLI) and IDB (Facebook's iOS Development Bridge) for simulator control, plus WebDriverAgent for physical device interaction. Your agent can tap at specific coordinates, swipe, type text, scroll, and read the screen via ScreenCaptureKit with a Metal rendering pipeline.

Why not just use Fastlane?
Fastlane is configuration-based — you write a Fastfile and define steps upfront. With Blitz, you tell your AI agent "submit this app to the App Store" and the agent figures out the steps: check if the app record exists, create it if not, fill in metadata, upload screenshots, handle code signing, submit. The agent adapts to the current state rather than following a static script.

Is my App Store Connect data safe?
Blitz runs locally on your Mac for core workflows, and the MCP server runs on localhost. Some features may also communicate with remote services when you use them.

Which AI agents work with Blitz?
Any agent that supports MCP (Model Context Protocol). Today that includes Claude Code, Cursor, Codex, and OpenCode. Blitz exposes 35+ tools via an open standard — it's not locked to any single agent.

Why does Blitz run on macOS only?
Apple platform development requires macOS. You need Xcode, the iOS Simulator, and Apple's code signing tools, all of which are macOS-only. This isn't a limitation of Blitz — it's a limitation of Apple's ecosystem.

* * *

Free and open source. Works with Claude Code, Codex, Cursor, OpenCode.
