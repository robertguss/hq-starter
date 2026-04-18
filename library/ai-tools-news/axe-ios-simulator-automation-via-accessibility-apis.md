---
tags:
  - library
title: "AXe - iOS Simulator Automation via Accessibility APIs"
url: "https://www.axe-cli.com/"
company: [personal]
topics: []
created: 2026-03-07
source_type: raindrop
raindrop_id: 1633882855
source_domain: "axe-cli.com"
source_type_raindrop: link
collection: "AI Tools & News"
collection_id: 69284314
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

A comprehensive CLI tool for automating iOS Simulators using Apple's Accessibility APIs and HID functionality. Single binary, no servers, no dependencies.

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: AXe - iOS Simulator Automation via Accessibility APIs

URL Source: https://www.axe-cli.com/

Markdown Content:
v1.6.0 available now

![Image 1: AXe](https://www.axe-cli.com/icon.png)![Image 2: AXe](https://www.axe-cli.com/axe-text.png)

## iOS Simulator

automation

A comprehensive CLI tool for automating iOS Simulators using Apple's Accessibility APIs and HID functionality. Single binary, no servers, no external dependencies.

[Get Started](https://www.axe-cli.com/#get-started)[View on GitHub](https://github.com/cameroncooke/AXe)

MIT Licensed Single Binary macOS 14+AI Agent Ready

## Everything you need for simulator automation

Complete control over iOS Simulators through accessibility APIs and HID input.

### Touch & Gestures

Precise tap events, swipe gestures, and low-level touch down/up events. Tap by coordinates, accessibility ID, or label.

### Text & Keyboard Input

Comprehensive text typing with automatic shift handling. Individual key presses, key sequences, and key combos like Cmd+A.

### Hardware Buttons

Simulate Home, Lock/Power, Side, Siri, and Apple Pay buttons with configurable duration and timing controls.

### Screenshots & Streaming

PNG screenshot capture and real-time streaming at 1-30 FPS in multiple formats including MJPEG and raw JPEG.

### Video Recording

H.264 MP4 video recording with hardware-friendly encoding. Configurable quality and scale factors.

### Accessibility Inspection

Extract full accessibility information from any screen. Query accessibility at specific coordinates for precise automation.

Simple & Powerful

## Intuitive CLI commands

Every interaction is a simple command. Tap, swipe, type, capture screenshots, and record video — all from your terminal.

*   No server setup or background daemons required
*   Built-in gesture presets for common interactions
*   Pre/post delay controls for precise timing
*   Pipe text input via stdin for flexible scripting

$axe batch --file login-flow.steps --udid <UDID>

Step 1/8: tap --label "Email" ... OK

Step 2/8: type ... OK

Step 3/8: tap --label "Password" ... OK

Step 4/8: type ... OK

Step 5/8: tap --label "Sign In" ... OK

Step 6/8: sleep 2 ... OK

Step 7/8: screenshot ... OK

All steps completed successfully.

New in v1.6.0

## Batch automation

Execute multi-step interaction workflows in a single invocation. Perfect for login flows, form filling, and complex UI navigation.

*   Sequential execution across multi-screen flows
*   Built-in sleep delays between steps
*   Accessibility caching for faster execution
*   Fail-fast or best-effort execution modes
*   Configurable text submission strategies

## Built for AI agents

Native integration with AI coding assistants for autonomous iOS simulator testing.

Works with your favorite AI tools

Claude Code Codex Cursor VS Code Shell Scripts

## Why AXe?

A lightweight, focused alternative to idb for iOS Simulator UI automation.

### Single Binary

No test runner or harness to install in the simulator. Works out of the box with any booted simulator.

### No Setup Required

No external frameworks to install, no servers to run. Works out of the box on macOS 14+.

### Fast & Lightweight

Purpose-built for UI automation. Minimal overhead, maximum performance for simulator interactions.

### Gesture Presets

Built-in presets for scroll, edge swipes, and common gestures. No coordinate math needed.

### Batch Execution

Run multi-step workflows in a single invocation. Dramatically reduces latency for complex flows.

### Accessibility-First

Built on Apple's Accessibility APIs. Tap elements by label, not just coordinates.

![Image 3: AXe](https://www.axe-cli.com/icon.png)

## Open source, community driven

AXe is MIT licensed and welcomes contributions. Help shape the future of iOS Simulator automation.

[View Issues](https://github.com/cameroncooke/AXe/issues)[Documentation](https://github.com/cameroncooke/AXe)
