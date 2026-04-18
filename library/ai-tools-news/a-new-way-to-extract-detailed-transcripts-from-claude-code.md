---
tags:
  - library
title: "A new way to extract detailed transcripts from Claude Code"
url: "https://simonwillison.net/2025/Dec/25/claude-code-transcripts/"
company: [personal]
topics: []
created: 2025-12-27
source_type: raindrop
raindrop_id: 1511149911
source_domain: "simonwillison.net"
source_type_raindrop: article
collection: "AI Tools & News"
collection_id: 69284314
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

I’ve released claude-code-transcripts, a new Python CLI tool for converting Claude Code transcripts to detailed HTML pages that provide a better interface for understanding what Claude Code has done than …

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: A new way to extract detailed transcripts from Claude Code

URL Source: https://simonwillison.net/2025/Dec/25/claude-code-transcripts/

Markdown Content:
25th December 2025

I’ve released [claude-code-transcripts](https://github.com/simonw/claude-code-transcripts), a new Python CLI tool for converting [Claude Code](https://claude.ai/code) transcripts to detailed HTML pages that provide a better interface for understanding what Claude Code has done than even Claude Code itself. The resulting transcripts are also designed to be shared, using any static HTML hosting or even via GitHub Gists.

Here’s the quick start, with no installation required if you already have [uv](https://docs.astral.sh/uv/):

```
uvx claude-code-transcripts
```

(Or you could `uv tool install claude-code-transcripts` or `pip install claude-code-transcripts` first, if you like.)

This will bring up a list of your local Claude Code sessions. Hit up and down to select one, then hit `<enter>`. The tool will create a new folder with an `index.html` file showing a summary of the transcript and one or more `page_x.html` files with the full details of everything that happened.

Visit [this example page](https://static.simonwillison.net/static/2025/claude-code-microjs/index.html) to see a lengthy (12 page) transcript produced using this tool.

![Image 1: Screenshot of a claude code transcript spanning 12 pages - the first page shows a summary starting with the first user prompt to clone bellard/quickjs to /tmp](https://static.simonwillison.net/static/2025/claude-code-transcripts-example.jpg)

If you have the [gh CLI tool](https://cli.github.com/) installed and authenticated you can add the `--gist` option—the transcript you select will then be automatically shared to a new Gist and a link provided to `gistpreview.github.io` to view it.

`claude-code-transcripts` can also fetch sessions from Claude Code for web. I reverse-engineered the private API for this (so I hope it continues to work), but right now you can run:

```
uvx claude-code-transcripts web --gist
```

Then select a Claude Code for web session and have that converted to HTML and published as a Gist as well.

The [claude-code-transcripts README](https://github.com/simonw/claude-code-transcripts/blob/main/README.md) has full details of the other options provided by the tool.

#### Why I built this

These days I’m writing significantly more code via Claude Code than by typing text into a text editor myself. I’m actually getting more coding work done _on my phone_ than on my laptop, thanks to the Claude Code interface in Anthropic’s Claude iPhone app.

Being able to have an idea on a walk and turn that into working, tested and documented code from a couple of prompts on my phone is a truly science fiction way of working. I’m enjoying it a lot.

There’s one problem: the actual _work_ that I do is now increasingly represented by these Claude conversations. Those transcripts capture extremely important context about my projects: what I asked for, what Claude suggested, decisions I made, and Claude’s own justification for the decisions it made while implementing a feature.

I value these transcripts a lot! They help me figure out which prompting strategies work, and they provide an invaluable record of the decisions that went into building features.

In the pre-LLM era I relied on issues and issue comments to record all of this extra project context, but now those conversations are happening in the Claude Code interface instead.

I’ve made several past attempts at solving this problem. The first was pasting Claude Code terminal sessions into a shareable format—I [built a custom tool for that](https://simonwillison.net/2025/Oct/23/claude-code-for-web-video/) (called [terminal-to-html](https://tools.simonwillison.net/terminal-to-html/) and I’ve used it a lot, but it misses a bunch of detail—including the default-invisible thinking traces that Claude Code generates while working on a task.

I’ve also built [claude-code-timeline](https://tools.simonwillison.net/colophon#claude-code-timeline.html) and [codex-timeline](https://tools.simonwillison.net/colophon#codex-timeline.html) as HTML tool viewers for JSON transcripts from both Claude Code and Codex. Those work pretty well, but still are not quite as human-friendly as I’d like.

An even bigger problem is Claude Code for web—Anthropic’s asynchronous coding agent, which is the thing I’ve been using from my phone. Getting transcripts out of that is even harder! I’ve been synchronizing them down to my laptop just so I can copy and paste from the terminal but that’s a pretty inelegant solution.

#### How I built claude-code-transcripts

You won’t be surprised to hear that every inch of this new tool was built using Claude.

You can browse [the commit log](https://github.com/simonw/claude-code-transcripts/commits/main/) to find links to the transcripts for each commit, many of them published using the tool itself.

Here are some recent examples:

*   [c80b1dee](https://github.com/simonw/claude-code-transcripts/commit/c80b1dee9429637318f4fae3e5d733ae5c05ab2c) Rename tool from claude-code-publish to claude-code-transcripts—[transcript](https://gistpreview.github.io/?814530b3a70af8408f3bb8ca10f70d57/index.html)
*   [ad3e9a05](https://github.com/simonw/claude-code-transcripts/commit/ad3e9a05058c583bf7327421f727ba08c15aa8a0) Update README for latest changes—[transcript](https://gistpreview.github.io/?9b3fe747343d32c95a8565ef1f8b6e11/index.html)
*   [e1013c54](https://github.com/simonw/claude-code-transcripts/commit/e1013c54a601e79e62a9bf204c5a94acc8845c5f) Add autouse fixture to mock webbrowser.open in tests—[transcript](https://gistpreview.github.io/?1671b49de273d80280ab2ceab690db8c/index.html)
*   [77512e5d](https://github.com/simonw/claude-code-transcripts/commit/77512e5d6905ee8ba678af0e30bcee2dccb549f3) Add Jinja2 templates for HTML generation (#2)—[transcript](https://gistpreview.github.io/?ffc01d1c04e47ed7934a58ae04a066d1/index.html)
*   [b3e038ad](https://github.com/simonw/claude-code-transcripts/commit/b3e038adeac56e81d7c7558f0a7d39a8d44d9534) Add version flag to CLI (#1)—[transcript](https://gistpreview.github.io/?7bdf1535f7bf897fb475be6ff5da2e1c/index.html)

I had Claude use the following dependencies:

*   [click](https://pypi.org/project/click/) and [click-default-group](https://pypi.org/project/click-default-group/) for building the CLI
*   [Jinja2](https://pypi.org/project/Jinja2/) for HTML templating—a late refactoring, the initial system used Python string concatenation
*   [httpx](https://pypi.org/project/httpx/) for making HTTP requests
*   [markdown](https://pypi.org/project/Markdown/) for converting Markdown to HTML
*   [questionary](https://pypi.org/project/questionary/)—new to me, suggested by Claude—to implement the interactive list selection UI

And for development dependencies:

*   [pytest](https://pypi.org/project/pytest/)—always
*   [pytest-httpx](https://pypi.org/project/pytest-httpx/) to mock HTTP requests in tests
*   [syrupy](https://pypi.org/project/syrupy/) for snapshot testing—with a tool like this that generates complex HTML snapshot testing is a great way to keep the tests robust and simple. Here’s [that collection of snapshots](https://github.com/simonw/claude-code-transcripts/tree/main/tests/__snapshots__/test_generate_html).

The one bit that wasn’t done with Claude Code was reverse engineering Claude Code itself to figure out how to retrieve session JSON from Claude Code for web.

I know Claude Code can reverse engineer itself, but it felt a bit more subversive to have OpenAI Codex CLI do it instead. [Here’s that transcript](https://gistpreview.github.io/?e4159193cd2468060d91289b5ccdece3)—I had Codex use `npx prettier` to pretty-print the obfuscated Claude Code JavaScript, then asked it to dig out the API and authentication details.

Codex came up with this _beautiful_`curl` command:

curl -sS -f \
    -H "Authorization: Bearer $(security find-generic-password -a "$USER" -w -s "Claude Code-credentials" | jq-r .claudeAiOauth.accessToken)"  \
    -H "anthropic-version: 2023-06-01" \
    -H "Content-Type: application/json" \
    -H "x-organization-uuid: $(jq -r '.oauthAccount.organizationUuid' ~/.claude.json)" \
    "https://api.anthropic.com/v1/sessions"

The really neat trick there is the way it extracts Claude Code’s OAuth token from the macOS Keychain using the `security find-generic-password` command. I ended up using that trick in `claude-code-transcripts` itself!
