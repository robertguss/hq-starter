---
tags:
  - library
title: "Introducing vt, the Val Town CLI"
url: "https://blog.val.town/vt-cli"
company: [personal]
topics: []
created: 2025-09-10
source_type: raindrop
raindrop_id: 1333159501
source_domain: "blog.val.town"
source_type_raindrop: article
collection: "Dev Tools & CLI"
collection_id: 69292902
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

Updates and articles from the Val Town team

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: Introducing vt, the Val Town CLI

URL Source: https://blog.val.town/vt-cli

Published Time: Sat, 18 Apr 2026 19:20:36 GMT

Markdown Content:
# Introducing vt, the Val Town CLI | Val Town Blog

[val.town](https://val.town/)[blog.val.town](https://blog.val.town/)

Elsewhere Elsewhere

*   [RSS](https://blog.val.town/rss.xml)
*   [Email](mailto:hi@val.town)
*   [Twitter](https://x.com/ValDotTown)
*   [Bluesky](https://bsky.app/profile/val.town)
*   [Discord](https://discord.val.town/)
*   [YouTube](https://www.youtube.com/@valDotTown)
*   [GitHub](https://github.com/val-town)
*   [LinkedIn](https://www.linkedin.com/company/val-town/)
*   [OSS Pledge](https://opensourcepledge.com/members/val-town/)

[Code and prose written on val.town](https://blog.val.town/source)
# [Introducing vt, the Val Town CLI](https://blog.val.town/vt-cli)

[Wolf Mermelstein](https://404wolf.com/)Sep 10, 2025

Introducing **vt**, the CLI for Val Town that lets you use your favorite editors and local tools. Now you can use VS Code, Claude Code, Codex and more with our super-fast feedback loop, deploying software instantly as you develop it.

To get vt, [install Deno](https://docs.deno.com/runtime/getting_started/installation/), then run

```sh
deno install -grAf jsr:@valtown/vt
```

With vt, you can:

*   Use `vt watch` to watch a folder for changes, pushing updates and redeploying instantly as you save
*   Remix or create brand-new Val Town projects directly from your command line
*   Livestream logs from your Val directly to your terminal
*   Manage branches, switching between separate deployments or prod & dev branches of a project

We designed vt to work much like `git`, so `vt branch` and `vt checkout -b` work just like you'd expect. But the real magic is in the `vt watch` command: vt can resolve deltas between Val Town and a local folder of TypeScript and text files, automatically detecting file changes like renames and modifications. As you edit in VS Code, neovim, or your favorite editor, every time you save the changes go live. Or, if you don't want to live on the edge, you can use `vt push` to explicitly push new changes.

## Bring your own editor - and LLMs!

vt works perfectly with your favorite LLM tools: it can even initialize a [AGENTS.md](https://agents.md/) file that contains all of the context necessary to write code for the Val Town platform.

People are already using vt to build cool projects, like [Geoffrey Litt's Stevens](https://news.ycombinator.com/item?id=43681287) project, a really cool AI personal assistant telegram bot, built locally with cursor and vt. We built Val Town's new [Val search](https://codesearch.val.run/) on Val Town itself, with Claude Code and vt.

## Use the companion browser extension

vt also has a companion browser extension which pairs with `vt watch` to automatically reload the tab as you edit your Val.

It's available for [Chrome](https://chromewebstore.google.com/detail/vt-companion/jjpaicfaaobmjlcppnooejnjnbefalfo) or [Firefox](https://addons.mozilla.org/en-US/firefox/addon/vt-companion/).

If you have `vt watch` running, it should "just work"! The companion communicates with vt's watcher over a local WebSocket connection.

## We want feedback!

vt is a big leap forward in the local development experience for Val Town. But we're always looking to improve and polish the experience. If you have any feedback we'd love to hear it. You can join our Discord server [here](https://discord.gg/dPeaMwfarG), and contribute ideas, PRs, or issues to the [val-town/vt GitHub repo](https://github.com/val-town/vt).

![Image 1: All editors supported](https://imagedelivery.net/iHX6Ovru0O7AjmyT5yZRoA/6c37ffa5-3136-4528-c946-4643806d5100/public)

[Edit on val.town](https://blog.val.town/source)

[Share on Twitter](https://twitter.com/share?text=Introducing%20vt%2C%20the%20Val%20Town%20CLI&urlhttps://blog.val.town/vt-cli=&via=valdottown "Share on Twitter")[Share on Bluesky](https://bsky.app/intent/compose?text=Introducing%20vt%2C%20the%20Val%20Town%20CLI%20https://blog.val.town/vt-cli "Share on Bluesky")[Share on Hacker News](http://news.ycombinator.com/submitlink?u=https://blog.val.town/vt-cli&t=Introducing%20vt%2C%20the%20Val%20Town%20CLI "Share on Hacker News")

**We’re hiring!**![Image 2](https://imagedelivery.net/iHX6Ovru0O7AjmyT5yZRoA/bb3a7d1c-305e-46b8-b560-116eca106300/public)

Join our team and help build the future of programming.

[View open roles →](https://www.val.town/careers)

© 2026 Val Town
