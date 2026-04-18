---
tags:
  - library
title: "XcodeBuildMCP - AI-Powered Xcode Automation"
url: "https://www.xcodebuildmcp.com/"
company: [personal]
topics: []
created: 2026-03-11
source_type: raindrop
raindrop_id: 1638726314
source_domain: "xcodebuildmcp.com"
source_type_raindrop: link
collection: "AI Tools & News"
collection_id: 69284314
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

Let AI assistants build, test, and debug your iOS apps autonomously. XcodeBuildMCP bridges the gap between AI agents and Xcode.

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: XcodeBuildMCP - AI-Powered Xcode Automation

URL Source: https://www.xcodebuildmcp.com/

Markdown Content:
# XcodeBuildMCP - AI-Powered Xcode Automation

[![Image 1: XcodeBuildMCP](https://www.xcodebuildmcp.com/logo.png)XcodeBuildMCP](https://www.xcodebuildmcp.com/#)[Features](https://www.xcodebuildmcp.com/#features)[See it in Action](https://www.xcodebuildmcp.com/#see-it-in-action)[Xcode Integration](https://www.xcodebuildmcp.com/#xcode-integration)

[1,900](https://github.com/getsentry/XcodeBuildMCP)[Get Started](https://www.xcodebuildmcp.com/#get-started)

available now

# AI-powered

Xcode automation

An MCP server and CLI that gives AI agents full control over Xcode. Build, test, debug, and deploy your iOS and macOS apps without leaving your agent.

[Get Started](https://www.xcodebuildmcp.com/#get-started)[View on GitHub 1,900](https://github.com/getsentry/XcodeBuildMCP)

MIT Licensed Open Source Active Development

## Everything you need for AI-driven development

A complete toolkit for integrating Xcode workflows with AI assistants and automation.

### Autonomous Development

AI agents independently build projects, fix compilation errors, and iterate on solutions without human intervention.

### Complete Workflow

From project creation to device deployment. Manage the entire iOS/macOS development lifecycle through AI commands.

### LLDB Debugging

Attach the debugger, set breakpoints, inspect variables, and execute LLDB commands directly from your AI agent.

### UI Automation

Interact with simulator UI elements, capture screenshots, and automate user interface testing workflows.

### Real Device Testing

Deploy and test on physical devices over USB or Wi-Fi with comprehensive log capture and debugging support.

### Multi-Client Support

Works with Cursor, Claude Code, VS Code, Windsurf, Xcode, and any MCP-compatible client.

## See it in action

Watch XcodeBuildMCP handle real development workflows end to end.

### Agentic Development

AI agents autonomously building, testing, and iterating on iOS projects.

### Debugging

LLDB integration for setting breakpoints, inspecting state, and fixing issues.

### Xcode IDE Integration

Seamless integration with Xcode's coding agents and development tools.

New in v2.0

## First-class CLI

Every MCP tool is also available from the command line. Use it for scripting, CI workflows, or direct terminal usage alongside your AI agents.

*   All MCP tools accessible from the terminal
*   Background process for stateful operations (log capture, debugging, video recording)
*   Works great in CI/CD pipelines and scripting

Terminal

$xcodebuildmcp tools

Available tools (59):simulator/build, simulator/build-and-run,simulator/test, simulator/screenshot,debugging/attach, debugging/breakpoint,ui-automation/tap, ui-automation/swipe ...

$xcodebuildmcp simulator build-and-run \--scheme MyApp --project-path ./MyApp.xcodeproj

Build succeeded. Launching on iPhone 16...

## Deep Xcode interoperability

Two-way integration that works inside Xcode and from external tools.

Inside Xcode

### Works with Xcode's coding agents

XcodeBuildMCP integrates natively with Xcode 26.3's Claude and Codex coding agents. It automatically detects your selected scheme and simulator, using those values for all operations.

*   Auto-detects active scheme and simulator
*   Augments Xcode's agent with build, test, and deploy capabilities
*   Hides redundant tools already served by Xcode natively

From External Agents

### Proxy Xcode's MCP server

Xcode now has its own MCP server for external agents. XcodeBuildMCP proxies those tools automatically, so you only need one server configured in your client.

*   Single server setup for all Xcode capabilities
*   Snapshot SwiftUI previews from external agents
*   Access Apple documentation and Issue Navigator data

Works with your favorite tools

Cursor Claude Code VS Code Windsurf Xcode GitHub Copilot Codex Amp OpenCode

Claude Code

>Add dark mode support to my app.

Edited Theme.swift

Edited SettingsView.swift

Edited ContentView.swift

 Built and launched on iPhone 16

 Navigated to Settings

 Toggled dark mode switch

 Captured screenshot

I've added dark mode support and verified it works in the simulator. The toggle is in Settings and persists across launches.

.xcodebuildmcp/config.yaml

schemaVersion: 1
enabledWorkflows:
  - simulator
  - ui-automation
  - debugging
sessionDefaults:
  scheme: MyApp
  projectPath: ./MyApp.xcodeproj
  simulatorName: iPhone 16

Agent-ready

## Built for AI agents

Configure your project once and let AI agents handle the rest. XcodeBuildMCP gives agents full autonomy over the build, test, and deploy cycle.

*   Project-level config so agents know your scheme, simulator, and workflows
*   Agents independently fix build errors and iterate on solutions
*   Selective workflow loading to reduce agent context window usage
*   Agent skill files to prime your AI with usage instructions

## Get started in seconds

Install XcodeBuildMCP as an MCP server for AI coding agents, or globally for CLI use.

NPX (recommended)Homebrew

MCP server
Add to your MCP client configuration:

{
  "mcpServers": {
    "XcodeBuildMCP": {
      "command": "npx",
      "args": ["-y", "xcodebuildmcp@latest", "mcp"]
    }
  }
}

CLI
Install globally for direct terminal use:

`npm install -g xcodebuildmcp@latest`

[View full documentation](https://github.com/getsentry/XcodeBuildMCP)

## Open source, community driven

XcodeBuildMCP is MIT licensed and welcomes contributions. Help shape the future of AI-powered Xcode development.

[View Issues](https://github.com/getsentry/XcodeBuildMCP/issues)[Contributing Guide](https://github.com/getsentry/XcodeBuildMCP/blob/main/docs/dev/CONTRIBUTING.md)

![Image 2: XcodeBuildMCP](https://www.xcodebuildmcp.com/logo.png)XcodeBuildMCP© 2026 Sentry

[Sentry](https://sentry.io/)[@xcodebuildmcp](https://x.com/xcodebuildmcp)[GitHub](https://github.com/getsentry/XcodeBuildMCP)
