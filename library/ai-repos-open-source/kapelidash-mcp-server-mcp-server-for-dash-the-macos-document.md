---
tags:
  - library
title: "Kapeli/dash-mcp-server: MCP server for Dash, the macOS documentation browser"
url: "https://github.com/Kapeli/dash-mcp-server?tab=readme-ov-file"
company: [personal]
topics: []
created: 2026-03-09
source_type: raindrop
raindrop_id: 1636311315
source_domain: "github.com"
source_type_raindrop: link
collection: "AI Repos & Open Source"
collection_id: 69284315
hydrated: true
hydrated_at: 2026-04-17
hydrated_via: github-api
---
## Excerpt

MCP server for Dash, the macOS documentation browser - Kapeli/dash-mcp-server

## Raw Content

<!-- Hydrated 2026-04-17 via github-api -->

# mcp-server-dash

A Model Context Protocol (MCP) server that provides tools to interact with the [Dash](https://kapeli.com/dash) documentation browser API.

Dash 8 is required. You can download Dash 8 at https://blog.kapeli.com/dash-8.

mcp-name: io.github.Kapeli/dash-mcp-server

<a href="https://glama.ai/mcp/servers/@Kapeli/dash-mcp-server">
  <img width="380" height="200" src="https://glama.ai/mcp/servers/@Kapeli/dash-mcp-server/badge" alt="Dash Server MCP server" />
</a>

## Overview

The Dash MCP server provides tools for accessing and searching documentation directly from Dash, the macOS documentation browser. MCP clients can:

- List installed docsets
- Search across docsets and code snippets
- Load documentation pages from search results
- Enable full-text search for specific docsets

### Notice

This is a work in progress. Any suggestions are welcome!

## Tools

1. **list_installed_docsets**
   - Lists all installed documentation sets in Dash
2. **search_documentation**
   - Searches across docsets and snippets
3. **load_documentation_page**
   - Loads a documentation page from a `load_url` returned by `search_documentation`
4. **enable_docset_fts**
   - Enables full-text search for a specific docset

## Requirements

- macOS (required for Dash app)
- [Dash](https://kapeli.com/dash) installed
- Python 3.11.4 or higher
- uv

## Configuration

### Using uvx

```bash
brew install uv
```

#### in `claude_desktop_config.json`

```json
{
  "mcpServers": {
      "dash-api": {
          "command": "uvx",
          "args": [
              "--from",
              "git+https://github.com/Kapeli/dash-mcp-server.git",
              "dash-mcp-server"
          ]
      }
  }
}
```

#### in `Claude Code`

```bash
claude mcp add dash-api -- uvx --from "git+https://github.com/Kapeli/dash-mcp-server.git" "dash-mcp-server"
```
