---
tags:
  - library
title: "blueprinter by yofine/skills"
url: "https://skills.sh/yofine/skills/blueprinter"
company: [personal]
topics: []
created: 2026-04-09
source_type: raindrop
raindrop_id: 1678020818
source_domain: "skills.sh"
source_type_raindrop: article
collection: "AI Tools & News"
collection_id: 69284314
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

Install the blueprinter skill for yofine/skills

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: blueprinter by yofine/skills

URL Source: https://skills.sh/yofine/skills/blueprinter

Markdown Content:
# blueprinter by yofine/skills

[](https://vercel.com/ "Made with love by Vercel")[Skills](https://skills.sh/)

[Official](https://skills.sh/official)[Audits](https://skills.sh/audits)[Docs](https://skills.sh/docs)

[skills](https://skills.sh/)/[yofine](https://skills.sh/yofine)/[skills](https://skills.sh/yofine/skills)/blueprinter

# blueprinter

Installation

`$ npx skills add https://github.com/yofine/skills --skill blueprinter`

SKILL.md

# Blueprinter

Generate technical diagrams using HTML/CSS following the "Flat Engineering Blueprint" style guidelines.

## Core Philosophy

Precise, Objective, High Data-Ink Ratio. The output should look like a technical specification sheet or an architectural diagram, NOT a marketing landing page.

## Visual Rules

### 1. No Decorations

*   NO drop shadows
*   NO gradients
*   NO glassmorphism/blur
*   NO rounded buttons

### 2. Flat & Outlined

*   Use 1px or 2px solid borders for structure
*   Use white backgrounds for content blocks

### 3. Monochrome Base

| Element | Color |
| --- | --- |
| Background | Light Gray (#f8fafc) |
| Canvas | White (#ffffff) with Slate Border (#cbd5e1) |
| Text (Main) | High contrast Black (#0f172a) |
| Text (Sub) | Slate Gray (#64748b) |
| Accent | Use BLACK or ONE semantic color (e.g., Red for Error) sparingly |

### 4. Typography

*   Headings/Labels: Sans-serif (Inter/Helvetica)
*   Data/Paths/Code: Monospace (JetBrains Mono/Consolas)

### 5. Layout Structure

*   The diagram must be contained within a `diagram-canvas` (a bordered box with padding)
*   Header: Title + Uppercase Subtitle, separated by a solid bottom border
*   Grid/Flexbox alignment: Everything must be strictly aligned

### 6. Elements

*   **Connectors**: Thin, straight or orthogonal lines. Dashed lines for abstract relationships.
*   **Icons**: Simple stroke SVG icons (no fill or complex details)
*   **Badges**: Outlined or solid black/gray blocks. Small font size.

## CSS Variable Reference

```css
:root {
  --c-bg: #f8fafc;         /* Outer Background */
  --c-canvas: #ffffff;     /* Diagram Background */
  --c-border: #cbd5e1;     /* Slate-300 */
  --c-text-main: #0f172a;  /* Slate-900 */
  --c-text-sub: #64748b;   /* Slate-500 */
  --font-ui: 'Inter', sans-serif;
  --font-mono: 'JetBrains Mono', monospace;
}
```

## HTML Structure Template

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[Diagram Title]</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
  <style>
    :root {
      --c-bg: #f8fafc;
      --c-canvas: #ffffff;
      --c-border: #cbd5e1;
      --c-text-main: #0f172a;
      --c-text-sub: #64748b;
      --c-accent: #dc2626;  /* Optional: for errors/warnings only */
      --font-ui: 'Inter', sans-serif;
      --font-mono: 'JetBrains Mono', monospace;
    }

    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      font-family: var(--font-ui);
      background: var(--c-bg);
      padding: 40px;
      min-height: 100vh;
    }

    .diagram-container {
      max-width: 1200px;
      margin: 0 auto;
    }

    .diagram-canvas {
      background: var(--c-canvas);
      border: 1px solid var(--c-border);
      padding: 32px;
    }

    .diagram-header {
      border-bottom: 1px solid var(--c-border);
      padding-bottom: 16px;
      margin-bottom: 24px;
    }

    .diagram-title {
      font-size: 20px;
      font-weight: 600;
      color: var(--c-text-main);
      margin-bottom: 4px;
    }

    .diagram-subtitle {
      font-size: 11px;
      font-weight: 500;
      color: var(--c-text-sub);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    /* Component styles */
    .component {
      border: 1px solid var(--c-border);
      padding: 16px;
      background: var(--c-canvas);
    }

    .component-label {
      font-family: var(--font-mono);
      font-size: 12px;
      color: var(--c-text-sub);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .component-value {
      font-family: var(--font-mono);
      font-size: 14px;
      color: var(--c-text-main);
      font-weight: 500;
    }

    /* Connector lines */
    .connector {
      stroke: var(--c-border);
      stroke-width: 1;
    }

    .connector-dashed {
      stroke: var(--c-border);
      stroke-width: 1;
      stroke-dasharray: 4 4;
    }

    /* Badges */
    .badge {
      display: inline-block;
      font-family: var(--font-mono);
      font-size: 10px;
      padding: 2px 6px;
      border: 1px solid var(--c-border);
      color: var(--c-text-sub);
    }

    .badge-solid {
      background: var(--c-text-main);
      color: var(--c-canvas);
      border-color: var(--c-text-main);
    }
  </style>
</head>
<body>
  <div class="diagram-container">
    <div class="diagram-canvas">
      <div class="diagram-header">
        <div class="diagram-title">[Diagram Title]</div>
        <div class="diagram-subtitle">[Diagram Type / Version]</div>
      </div>
      <!-- Diagram content goes here -->
    </div>
  </div>
</body>
</html>
```

## Usage Guidelines

1.   **Always use the CSS variables** - never hardcode colors
2.   **Keep it flat** - no shadows, no gradients, no blur effects
3.   **Use monospace for data** - any technical values, paths, codes should use `--font-mono`
4.   **Align strictly** - use CSS Grid or Flexbox with consistent gaps
5.   **Connect with lines** - use SVG for connectors between components
6.   **Minimal icons** - if icons are needed, use simple stroke-only SVGs

## Example: Simple System Diagram

```html
<div class="diagram-canvas">
  <div class="diagram-header">
    <div class="diagram-title">System Architecture</div>
    <div class="diagram-subtitle">v1.0 / Overview</div>
  </div>
  
  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 24px;">
    <div class="component">
      <div class="component-label">Client</div>
      <div class="component-value">Web App</div>
    </div>
    <div class="component">
      <div class="component-label">API</div>
      <div class="component-value">REST Gateway</div>
    </div>
    <div class="component">
      <div class="component-label">Database</div>
      <div class="component-value">PostgreSQL</div>
    </div>
  </div>
</div>
```

Weekly Installs

563

Repository

[yofine/skills](https://github.com/yofine/skills "yofine/skills")

GitHub Stars

106

First Seen

Apr 1, 2026

Security Audits

[Gen Agent Trust Hub Pass](https://skills.sh/yofine/skills/blueprinter/security/agent-trust-hub)[Socket Pass](https://skills.sh/yofine/skills/blueprinter/security/socket)[Snyk Pass](https://skills.sh/yofine/skills/blueprinter/security/snyk)

Installed on

codex 489

opencode 482

gemini-cli 481

github-copilot 481

cursor 481

amp 480
