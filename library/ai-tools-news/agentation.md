---
tags:
  - library
title: "Agentation"
url: "https://agentation.dev/"
company: [personal]
topics: []
created: 2026-02-27
source_type: raindrop
raindrop_id: 1621254242
source_domain: "agentation.dev"
source_type_raindrop: link
collection: "AI Tools & News"
collection_id: 69284314
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

The visual feedback tool for agents.

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: Agentation

URL Source: https://agentation.dev/

Markdown Content:
Agentation is currently desktop only.

## Visual feedback.

For agents.

Agentation turns UI annotations into structured context that AI coding agents can understand and act on. Click any element, add a note, and paste the output into Claude Code, Codex, or any AI tool.

localhost:3000

1

2

3

4

5

Benji's Project

█

## How you use it

1.   Click the  icon in the bottom-right corner to activate
2.   **Hover** over elements to see their names highlighted
3.   **Click** any element to add an annotation
4.   Write your feedback and click **Add**
5.   Click  to copy formatted markdown
6.   Paste into your agent

**Note:** With [MCP](https://www.agentation.com/mcp), you can skip the copy-paste step entirely — your agent already sees what you're pointing at. Just say “address my feedback” or “fix annotation 3.”

## How agents use it

Agentation works best with AI tools that have access to your codebase (Claude Code, Cursor, etc.). When you paste the output, agents get:

*   **CSS selectors** to grep your codebase
*   **Source file paths** to jump directly to the right line
*   **React component tree** to understand the hierarchy
*   **Computed styles** to understand current appearance
*   **Your feedback** with intent and priority

Without Agentation, you’d have to describe the element (“the blue button in the sidebar”) and hope the agent guesses right. With Agentation, you give it `.sidebar > button.primary` and it can grep for that directly.

## Try it

The toolbar is active on this page. Try annotating these demo elements:

### Example Card

Click on this card or select this text to create an annotation. The output will include the element path and your feedback.

## Animation pause demo

Click  in the toolbar to freeze this animation:

## Agents talk back

With [MCP integration](https://www.agentation.com/mcp) and the [Annotation Format Schema](https://www.agentation.com/schema), agents don’t just read your annotations — they can respond to them:

*   **“What annotations do I have?”** — List all feedback across pages
*   **“Should this be 24px or 16px?”** — Agent asks for clarification
*   **“Fixed the padding”** — Agent resolves with a summary
*   **“Clear all annotations”** — Dismiss everything at once

Your feedback becomes a conversation, not a one-way ticket into the void.

## Best practices

*   **Be specific** — “Button text unclear” is better than “fix this”
*   **One issue per annotation** — easier for the agent to address individually
*   **Include context** — mention what you expected vs. what you see
*   **Use text selection** — for typos or content issues, select the exact text
*   **Pause animations** — to annotate a specific animation frame

## Licensing

Agentation is free for individuals and companies for internal use. Use it to annotate your own projects, debug your own apps, or streamline feedback within your team. [Contact us](mailto:benji@dip.org) for a commercial license if you're redistributing Agentation as part of a product you sell.

[Set up real-time sync with MCP →](https://www.agentation.com/mcp)

[Push annotations to external services →](https://www.agentation.com/webhooks)

[Build your own integration with the API →](https://www.agentation.com/api)
