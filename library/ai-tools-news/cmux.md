---
tags:
  - library
title: "cmux"
url: "https://www.cmux.dev/"
company: [personal]
topics: []
created: 2026-03-05
source_type: raindrop
raindrop_id: 1629432442
source_domain: "cmux.dev"
source_type_raindrop: link
collection: "AI Tools & News"
collection_id: 69284314
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

Native macOS terminal built on Ghostty. Works with Claude Code, Codex, OpenCode, Gemini CLI, Kiro, Aider, and any CLI tool. Vertical tabs, notification rings, split panes, and a socket API.

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: cmux — The terminal built for multitasking

URL Source: https://www.cmux.dev/

Markdown Content:
# cmux — The terminal built for multitasking

[Docs](https://www.cmux.dev/docs/getting-started)[Blog](https://www.cmux.dev/blog)[Changelog](https://www.cmux.dev/docs/changelog)[Community](https://www.cmux.dev/community)[GitHub](https://github.com/manaflow-ai/cmux)

[Download for Mac](https://github.com/manaflow-ai/cmux/releases/latest/download/cmux-macos.dmg)

[Docs](https://www.cmux.dev/docs/getting-started)[Blog](https://www.cmux.dev/blog)[Changelog](https://www.cmux.dev/docs/changelog)[Community](https://www.cmux.dev/community)

[Download for Mac](https://github.com/manaflow-ai/cmux/releases/latest/download/cmux-macos.dmg)

![Image 1: cmux icon](https://www.cmux.dev/logo.png)
# cmux

The terminal built for

Native macOS app built on Ghostty. Vertical tabs, notification rings when agents need attention, split panes, and a socket API for automation.

[Download for Mac](https://github.com/manaflow-ai/cmux/releases/latest/download/cmux-macos.dmg)[View on GitHub](https://github.com/manaflow-ai/cmux)

## Features

*   -**Vertical tabs**: sidebar shows git branch, working directory, ports, and notification text
*   -**Notification rings**: panes light up when agents need attention
*   -**In-app browser**: split a browser alongside your terminal with a scriptable API
*   -**Split panes**: horizontal and vertical splits within each tab
*   -**Scriptable**: CLI and socket API for automation and scripting
*   -**GPU-accelerated**: powered by libghostty for smooth rendering
*   -**Lightweight**: native Swift + AppKit, no Electron
*   -**Keyboard shortcuts**: [extensive shortcuts](https://www.cmux.dev/docs/keyboard-shortcuts) for workspaces, splits, browser, and more

![Image 2: cmux terminal app screenshot](https://www.cmux.dev/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Flanding-image.70ebd164.png&w=3840&q=75&dpl=dpl_H2VjJQLWJWupsPa4hpM36oqJ1EAc)

## FAQ

How does cmux relate to Ghostty?

cmux is not a fork of Ghostty. It uses [libghostty](https://github.com/ghostty-org/ghostty) as a library for terminal rendering, the same way apps use WebKit for web views. Ghostty is a standalone terminal; cmux is a different app built on top of its rendering engine.

What platforms does it support?

macOS only, for now. cmux is a native Swift + AppKit app.

What coding agents does cmux work with?

All of them. cmux is a terminal, so any agent that runs in a terminal works out of the box: Claude Code, Codex, OpenCode, Gemini CLI, Kiro, Aider, Goose, Amp, Cline, Cursor Agent, and anything else you can launch from the command line.

How do notifications work?

When a process needs attention, cmux shows notification rings around panes, unread badges in the sidebar, a notification popover, and a macOS desktop notification. These fire automatically via standard terminal escape sequences (OSC 9/99/777), or you can trigger them with the [cmux CLI](https://www.cmux.dev/docs/notifications) and [Claude Code hooks](https://www.cmux.dev/docs/notifications).

Can I customize keyboard shortcuts?

Terminal keybindings are read from your Ghostty config file (`~/.config/ghostty/config`). cmux-specific shortcuts (workspaces, splits, browser, notifications) can be customized in Settings. See the [default shortcuts](https://www.cmux.dev/docs/keyboard-shortcuts) for a full list.

How does it compare to tmux?

tmux is a terminal multiplexer that runs inside any terminal. cmux is a native macOS app with a GUI: vertical tabs, split panes, an embedded browser, and a socket API are all built in. No config files or prefix keys needed.

Is cmux free?

Yes, cmux is free to use. The source code is available on [GitHub](https://github.com/manaflow-ai/cmux).

## Community

*   ["Another day another libghostty-based project, this time a macOS terminal with vertical tabs, better organization/notifications, embedded/scriptable browser specifically targeted towards people who use a ton of terminal-based agentic workflows."](https://x.com/mitchellh/status/2024913161238053296)[—![Image 3: Mitchell Hashimoto](https://www.cmux.dev/avatars/mitchellh.jpg)Mitchell Hashimoto, Creator of Ghostty and founder of HashiCorp](https://x.com/mitchellh/status/2024913161238053296)
*   ["This is exactly the product I've been looking for. After two hours this am I've in love."](https://x.com/schrockn/status/2025182278637207857)[—![Image 4: Nick Schrock](https://www.cmux.dev/avatars/schrockn.jpg)Nick Schrock, Creator of Dagster. GraphQL co-creator.](https://x.com/schrockn/status/2025182278637207857)
*   ["I've been using this all weekend and it's amazing."](https://x.com/egrefen/status/2026806171563184199)[—![Image 5: Edward Grefenstette](https://www.cmux.dev/avatars/egrefen.jpg)Edward Grefenstette, Director of Research at Google DeepMind](https://x.com/egrefen/status/2026806171563184199)
*   ["this has been my favorite tool for past two weeks"](https://x.com/max4c_/status/2027266664270889204)[—![Image 6: Max Forsey](https://www.cmux.dev/avatars/max4c_.jpg)Max Forsey](https://x.com/max4c_/status/2027266664270889204)
*   ["cmux 良さそうすぎてついにバイバイ VSCode するときなのかもしれない"— cmux looks so good it might finally be time to say goodbye to VSCode](https://x.com/asaza_0928/status/2026057269075698015)[—![Image 7: あさざ](https://www.cmux.dev/avatars/asaza_0928.jpg)あさざ](https://x.com/asaza_0928/status/2026057269075698015)
*   ["Hey, this looks seriously awesome. Love the ideas here, specifically: the programmability, layered UI, browser w/ api. Looking forward to giving this a spin. Also want to add that I really appreciate Mitchell Hashimoto creating libghostty; it feels like an exciting time to be a terminal user."](https://news.ycombinator.com/item?id=47083596)[—johnthedebs](https://news.ycombinator.com/item?id=47083596)
*   ["Vertical tabs in my terminal 🤤 I never thought of that before. I use and love Firefox vertical tabs."](https://x.com/joeriddles10/status/2024914132416561465)[—![Image 8: Joe Riddle](https://www.cmux.dev/avatars/joeriddles10.jpg)Joe Riddle](https://x.com/joeriddles10/status/2024914132416561465)
*   ["Gave this a run and it was pretty intuitive. Good work!"](https://news.ycombinator.com/item?id=47082577)[—dchu17](https://news.ycombinator.com/item?id=47082577)
*   ["I like it, ran it in the past day on three parallel projects each with several worktrees. Having this paired with lazygit and yazi / nvim made me a bit more productive than usual without having to chase multiple ghostty / iTerm instances. Also feels more natural than tmux."](https://www.reddit.com/r/ClaudeCode/comments/1r9g45u/comment/o6sxbr3/)[—afruth](https://www.reddit.com/r/ClaudeCode/comments/1r9g45u/comment/o6sxbr3/)
*   ["cmux良さそうなので入れてみたけれど、良い"— Tried cmux since it looked good — it's good](https://x.com/northprint/status/2025740286677434581)[—![Image 9: Norihiro Narayama](https://www.cmux.dev/avatars/northprint.jpg)Norihiro Narayama](https://x.com/northprint/status/2025740286677434581)
*   ["cmux is pretty good."](https://x.com/indykish/status/2025318347970412673)[—![Image 10: Kishore Neelamegam](https://www.cmux.dev/avatars/indykish.jpg)Kishore Neelamegam](https://x.com/indykish/status/2025318347970412673)
*   ["cmux.dev に乗り換えた"— Switched to cmux.dev](https://x.com/kataring/status/2026189035056832718)[—![Image 11: かたりん](https://www.cmux.dev/avatars/kataring.jpg)かたりん](https://x.com/kataring/status/2026189035056832718)
*   ["This has been such a useful find. I can't recommend it enough."](https://x.com/scottw/status/2026806893067551084)[—![Image 12: Scott Watermasysk](https://www.cmux.dev/avatars/scottw.jpg)Scott Watermasysk](https://x.com/scottw/status/2026806893067551084)
*   ["grabbed this over the weekend and loved it. been waiting for something like this."](https://x.com/johnblythe/status/2026812731844637010)[—![Image 13: John Blythe](https://www.cmux.dev/avatars/johnblythe.jpg)John Blythe](https://x.com/johnblythe/status/2026812731844637010)
*   ["This is exactly what I've wanted. Amazing job thank you!"](https://x.com/BChris91/status/2026821091637838273)[—![Image 14: Christopher](https://www.cmux.dev/avatars/bchris91.jpg)Christopher](https://x.com/BChris91/status/2026821091637838273)
*   ["Been using this for a week and it's fantastic. Vert tab for each WIP task. Inside, claudes on one side and browser with PR and resources on the other, switch between tasks and stay organized. Mix that with skills to have Claude watch CI recursively, etc. feeling enlightened tbh"](https://x.com/connorelsea/status/2026867085750440390)[—![Image 15: Connor](https://www.cmux.dev/avatars/connorelsea.jpg)Connor](https://x.com/connorelsea/status/2026867085750440390)
*   ["年初にWarpからGhosttyに乗り換えたけど、今はcmuxに乗り換えた💻 垂直タブが便利で、Claude Codeのタスクの終了が通知されるのがありがたい。Ghosttyベースだから爆速動作はそのまま。ghosttyでやったブランチ表示や補完もそのまま使える"— I switched from Warp to Ghostty at the start of the year, but now I've switched to cmux. The vertical tabs are convenient, and I appreciate getting notified when Claude Code tasks finish. It's Ghostty-based so the blazing fast performance carries over. Branch display and completions I set up in Ghostty still work too.](https://x.com/tonkotsuboy_com/status/2028458464801108212)[—![Image 16: 鹿野 壮 Takeshi Kano](https://www.cmux.dev/avatars/tonkotsuboy_com.jpg)鹿野 壮 Takeshi Kano](https://x.com/tonkotsuboy_com/status/2028458464801108212)

[Download for Mac](https://github.com/manaflow-ai/cmux/releases/latest/download/cmux-macos.dmg)[View on GitHub](https://github.com/manaflow-ai/cmux)

[Read the Docs](https://www.cmux.dev/docs)[View Changelog](https://www.cmux.dev/docs/changelog)

### Product

*   [Blog](https://www.cmux.dev/blog)
*   [Community](https://www.cmux.dev/community)
*   [Nightly](https://www.cmux.dev/nightly)

### Resources

*   [Docs](https://www.cmux.dev/docs/getting-started)
*   [Changelog](https://www.cmux.dev/docs/changelog)

### Legal

*   [Privacy](https://www.cmux.dev/privacy-policy)
*   [Terms](https://www.cmux.dev/terms-of-service)
*   [EULA](https://www.cmux.dev/eula)

### Social

*   [GitHub](https://github.com/manaflow-ai/cmux)
*   [X / Twitter](https://twitter.com/manaflowai)
*   [Discord](https://discord.gg/xsgFEVrWCZ)
*   [Contact](mailto:founders@manaflow.com)

© 2026 Manaflow
