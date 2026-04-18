---
tags:
  - library
title: "Plannotator - Visual Plan Review for Claude Code"
url: "https://plannotator.ai/"
company: [personal]
topics: []
created: 2026-03-10
source_type: raindrop
raindrop_id: 1637294294
source_domain: "plannotator.ai"
source_type_raindrop: link
collection: "AI Tools & News"
collection_id: 69284314
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

Interactive Plan Review: Mark up and refine your plans using a UI, easily share for team collaboration, automatically integrates with Claude Code plan mode.

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: Plannotator - Plan & Code Review for AI Coding Agents

URL Source: https://plannotator.ai/

Published Time: Sat, 18 Apr 2026 05:22:26 GMT

Markdown Content:
# Plannotator - Plan & Code Review for AI Coding Agents

[Plannotator](https://plannotator.ai/)

[Docs](https://plannotator.ai/docs/getting-started/installation/)|[Blog](https://plannotator.ai/blog/)|[GitHub](https://github.com/backnotprop/plannotator)

# Plan and code review 

 for your agents.

Annotate![Image 1](https://plannotator.ai/assets/whiteglove.png)Comment×Own your agent plans before they run. Review agent-written code with a full diff viewer. Share with your team. Your feedback goes straight back to the agent.

Runs locally | natively integrates with agents | free & open source

![Image 2](https://plannotator.ai/assets/icon-claude.svg)Claude Code![Image 3](https://plannotator.ai/assets/icon-codex.png)Codex![Image 4](https://plannotator.ai/assets/icon-copilot.svg)Copilot![Image 5](https://plannotator.ai/assets/icon-gemini.png)Gemini![Image 6](https://plannotator.ai/assets/icon-opencode-dark.svg)OpenCode![Image 7](https://plannotator.ai/assets/icon-pi.svg)Pi![Image 8](https://plannotator.ai/assets/icon-vscode.svg)VS Code

$curl -fsSL https://plannotator.ai/install.sh | bash

[Watch the demo](https://www.youtube.com/watch?v=a_AT7cEN_9I)[Try the demo](https://share.plannotator.ai/)

[](https://github.com/backnotprop/plannotator)|One command. Hooks into your agent automatically.|Zero learning curve

Plan Review

## Annotate the plan before it executes

Select text. Mark it for deletion, add a comment, or write a replacement. Your annotations export as structured feedback that the agent understands.

*   •Inline comments on any section
*   •Mark deletions to remove scope
*   •Version history tracks every revision (plan diffs)
*   •Diff view shows what changed between iterations

Terminal

  ██████  ██████  ██████  ███████
 ██      ██    ██ ██   ██ ██
 ██      ██    ██ ██   ██ █████
 ██      ██    ██ ██   ██ ██
  ██████  ██████  ██████  ███████

  █████   ██████  ███████ ███   ██ ████████
 ██   ██ ██       ██      ████  ██    ██
 ███████ ██   ███ █████   ██ ██ ██    ██
 ██   ██ ██    ██ ██      ██  ████    ██
 ██   ██  ██████  ███████ ██   ███    ██

$

Plannotator

![Image 9: Plannotator plan review with inline annotations](https://plannotator.ai/assets/plan-review.webp)

 Deny with feedback ![Image 10](https://plannotator.ai/assets/whiteglove.png)

Code Review

## Review the diff before you commit

Run `/plannotator-review` and get a PR-style diff viewer for your agent's uncommitted changes. The same workflow you use for human PRs, applied to agent output.

*   •Side-by-side or unified diff view
*   •File tree navigation
*   •Line-level annotations with code suggestions
*   •Stage or unstage files before committing

Terminal

  ██████  ██████  ██████  ███████
 ██      ██    ██ ██   ██ ██
 ██      ██    ██ ██   ██ █████
 ██      ██    ██ ██   ██ ██
  ██████  ██████  ██████  ███████

  █████   ██████  ███████ ███   ██ ████████
 ██   ██ ██       ██      ████  ██    ██
 ███████ ██   ███ █████   ██ ██ ██    ██
 ██   ██ ██    ██ ██      ██  ████    ██
 ██   ██  ██████  ███████ ██   ███    ██

$

Plannotator · Code Review

![Image 11: Plannotator code review with diff annotations](https://plannotator.ai/assets/code-review.webp)

![Image 12](https://plannotator.ai/assets/whiteglove.png) Send feedback 

## How it works... simple.

Plan Review Code Review 

Plannotator · Plan Review

![Image 13: Plannotator plan review showing annotations on an agent's proposed plan](https://plannotator.ai/assets/hiw-plan.webp)![Image 14: Plannotator code review showing diff annotations on agent-written code](https://plannotator.ai/assets/hiw-code.webp)

1
#### Use your agent normally

Work with your coding agent exactly as you do today. When it proposes a plan, Plannotator intercepts the approval step automatically.

2
#### Review on a real surface

Instead of squinting at terminal text, you get a proper review workspace. Annotate inline, mark what needs to change, then approve or deny with structured feedback. You own the specification.

3
#### Feedback flows back

Your annotations are sent directly to the agent as structured feedback. No copy-pasting, no retyping. The agent revises based on exactly what you said.

## Everything the plugin does

### Commands

`Plan review`Automatic: hooks into your agent's plan step

`/plannotator-annotate <file|dir|url>`Annotate any markdown, spec/plan, folder, or URL and send feedback

`/plannotator-last`Annotate the agent's last message

`/plannotator-review <null|pr-url>`Code review for local changes or GitHub and GitLab PRs

### Features

Runs locally Plans never leave your machine

Encrypted sharing Share plans via URL — data lives in the link itself

Version history Every plan revision saved, with diffs between versions

Draft auto-save Annotations survive server crashes and restarts

### Integrations

VS Code Open plans in editor tabs, diff view, editor annotations

Obsidian Auto-save plans to your vault with frontmatter and tags

Bear Save plans with nested tags and project metadata

GitHub PRs Review pull requests by URL with full diff annotations

Integrations for Claude Code, OpenCode, Pi, Codex, and VS Code. Works with any agent that supports plan mode.

[![Image 15: GitHub stars](https://img.shields.io/github/stars/backnotprop/plannotator?style=flat&logo=github&label=stars&color=gray)](https://github.com/backnotprop/plannotator)[View on GitHub →](https://github.com/backnotprop/plannotator)[Read the docs →](https://plannotator.ai/docs/getting-started/installation/)

## Your next plan deserves more than a rubber stamp.

Shape what gets built. Own what ships.

`curl -fsSL https://plannotator.ai/install.sh | bash`

[Watch the demo](https://www.youtube.com/watch?v=a_AT7cEN_9I)[All agent guides →](https://plannotator.ai/docs/getting-started/installation/)

#### Product

*   [Plan Review](https://plannotator.ai/docs/commands/plan-review/)
*   [Code Review](https://plannotator.ai/docs/commands/code-review/)
*   [Install](https://plannotator.ai/docs/getting-started/installation/)

#### Resources

*   [Quickstart](https://plannotator.ai/docs/getting-started/quickstart/)
*   [Claude Code](https://plannotator.ai/docs/guides/claude-code/)
*   [OpenCode](https://plannotator.ai/docs/guides/opencode/)
*   [Blog](https://plannotator.ai/blog/)

#### Community

*   [GitHub](https://github.com/backnotprop/plannotator)
*   [@backnotprop](https://x.com/backnotprop)
*   [@plannotator](https://x.com/plannotator)

![Image 16](https://plannotator.ai/plannotator.webp)Plannotator

© 2026 backnotprop.

Licensed under [MIT](https://github.com/backnotprop/plannotator/blob/main/LICENSE-MIT) or [Apache 2.0](https://github.com/backnotprop/plannotator/blob/main/LICENSE-APACHE), at your option.

[Privacy Policy](https://plannotator.ai/privacy/)

Built by

[![Image 17: backnotprop](https://avatars.githubusercontent.com/u/7244317?u=ca99a5717dd0ce83ad6e9f39a00489f84e501fbe&v=4&s=72)](https://github.com/backnotprop "@backnotprop")[![Image 18: dotemacs](https://avatars.githubusercontent.com/u/152363?v=4&s=72)](https://github.com/dotemacs "@dotemacs")[![Image 19: andreineculau](https://avatars.githubusercontent.com/u/708161?u=02fa2fd38c5d5a481f17b9dad09d77820c71e6a6&v=4&s=72)](https://github.com/andreineculau "@andreineculau")[![Image 20: oorestisime](https://avatars.githubusercontent.com/u/3874836?v=4&s=72)](https://github.com/oorestisime "@oorestisime")[![Image 21: Pran-Ker](https://avatars.githubusercontent.com/u/52480636?u=60f01edf07bc7acc5dc7072e8d4b8b86a1809eb8&v=4&s=72)](https://github.com/Pran-Ker "@Pran-Ker")[![Image 22: Aeg1sx](https://avatars.githubusercontent.com/u/29499164?u=4b768455dab9cd570caa56ca88a7509de874b50c&v=4&s=72)](https://github.com/Aeg1sx "@Aeg1sx")[![Image 23: renovate[bot]](https://avatars.githubusercontent.com/in/2740?v=4&s=72)](https://github.com/renovate%5Bbot%5D "@renovate[bot]")[![Image 24: gwynnnplaine](https://avatars.githubusercontent.com/u/58665842?u=537d8df8797924d878a92ec1f02e790089c8b8b7&v=4&s=72)](https://github.com/gwynnnplaine "@gwynnnplaine")[![Image 25: dmmulroy](https://avatars.githubusercontent.com/u/2755722?u=a9746c9f33b5a17bee04d58b578a12a013b4d41b&v=4&s=72)](https://github.com/dmmulroy "@dmmulroy")[![Image 26: foxytanuki](https://avatars.githubusercontent.com/u/45069709?u=e451c5fb5e567e64c983b9f789243b4aab277a8b&v=4&s=72)](https://github.com/foxytanuki "@foxytanuki")[![Image 27: l10veu602](https://avatars.githubusercontent.com/u/5621442?v=4&s=72)](https://github.com/l10veu602 "@l10veu602")[![Image 28: Exloz](https://avatars.githubusercontent.com/u/45303078?u=5e673e80d924afc64cd8fed7797e3856c1b70409&v=4&s=72)](https://github.com/Exloz "@Exloz")[![Image 29: yonihorn](https://avatars.githubusercontent.com/u/7020718?u=ec4eee26111faa69e6e334d8df410a01e3cf2928&v=4&s=72)](https://github.com/yonihorn "@yonihorn")[![Image 30: nulladdict](https://avatars.githubusercontent.com/u/26379644?u=6e83a0b4dee06b834092a7096c41ed55cb781d06&v=4&s=72)](https://github.com/nulladdict "@nulladdict")[![Image 31: rtsummit](https://avatars.githubusercontent.com/u/4036561?v=4&s=72)](https://github.com/rtsummit "@rtsummit")[![Image 32: stk-code](https://avatars.githubusercontent.com/u/534957?u=0062791cbe569f00e918e98b2e4ab628039d82bf&v=4&s=72)](https://github.com/stk-code "@stk-code")[![Image 33: sylvainDNS](https://avatars.githubusercontent.com/u/16577439?u=d48120660a35ca8ff1352ec7afa14debc218f55c&v=4&s=72)](https://github.com/sylvainDNS "@sylvainDNS")[![Image 34: blimmer](https://avatars.githubusercontent.com/u/630449?u=853443d98e9aabab9766739bc8a382e5ac9a7e58&v=4&s=72)](https://github.com/blimmer "@blimmer")[![Image 35: leoreisdias](https://avatars.githubusercontent.com/u/47978193?u=2da249db6becd09330da98abc7057422caecaa70&v=4&s=72)](https://github.com/leoreisdias "@leoreisdias")[![Image 36: ndesjardins-comact](https://avatars.githubusercontent.com/u/209511412?u=1b351e0085186dceea01ed4dc2caf9487612b1e5&v=4&s=72)](https://github.com/ndesjardins-comact "@ndesjardins-comact")[![Image 37: luyanfeng](https://avatars.githubusercontent.com/u/5779510?u=90536d2bfaef701750102e6d7ac8f1f8a480a9c0&v=4&s=72)](https://github.com/luyanfeng "@luyanfeng")[![Image 38: ShineBreaker](https://avatars.githubusercontent.com/u/102544159?u=fefaaba7abfb8b2fa568068951a6f5bad075047b&v=4&s=72)](https://github.com/ShineBreaker "@ShineBreaker")[![Image 39: punk-dev-robot](https://avatars.githubusercontent.com/u/3915056?u=741a6a1a205df23ac3294990dbb163867130823f&v=4&s=72)](https://github.com/punk-dev-robot "@punk-dev-robot")[![Image 40: pbowyer](https://avatars.githubusercontent.com/u/89852?u=d178a4d1457443c2e1cdac4110e74ab6d13fff25&v=4&s=72)](https://github.com/pbowyer "@pbowyer")[![Image 41: eromoe](https://avatars.githubusercontent.com/u/3938751?u=79e5d2ec6dc29c38938b7d4b84ec1fe0c6c578d2&v=4&s=72)](https://github.com/eromoe "@eromoe")[![Image 42: ZoeImport](https://avatars.githubusercontent.com/u/130266741?u=5cb8f7a79c51f29d85d3aff2a7f2cbc3a16f0bcb&v=4&s=72)](https://github.com/ZoeImport "@ZoeImport")[![Image 43: dezren39](https://avatars.githubusercontent.com/u/11225574?u=797488820e2baf8f59c59e9b04226ff97119e64e&v=4&s=72)](https://github.com/dezren39 "@dezren39")[![Image 44: aviadshiber](https://avatars.githubusercontent.com/u/15234072?u=4e073508d4e420dad81ac08766d4892e4fda834b&v=4&s=72)](https://github.com/aviadshiber "@aviadshiber")[![Image 45: maxim](https://avatars.githubusercontent.com/u/7758?u=9ee6c87103bd4c381de24b59c78df22bb5ad8143&v=4&s=72)](https://github.com/maxim "@maxim")[![Image 46: gwtaylor](https://avatars.githubusercontent.com/u/993736?v=4&s=72)](https://github.com/gwtaylor "@gwtaylor")[![Image 47: dillonoconnor](https://avatars.githubusercontent.com/u/60942873?u=cb9ff21380b614ef94308528f36841c953537c2f&v=4&s=72)](https://github.com/dillonoconnor "@dillonoconnor")[![Image 48: Zengwenj](https://avatars.githubusercontent.com/u/52520814?v=4&s=72)](https://github.com/Zengwenj "@Zengwenj")[![Image 49: daviziks](https://avatars.githubusercontent.com/u/53924113?u=c261d2e254677cd34d668ba052445ac829077689&v=4&s=72)](https://github.com/daviziks "@daviziks")[![Image 50: alexey-igrychev](https://avatars.githubusercontent.com/u/17360817?u=688f39a885a4cc8245c26383337e6b9984773c3e&v=4&s=72)](https://github.com/alexey-igrychev "@alexey-igrychev")[![Image 51: rooterkyberian](https://avatars.githubusercontent.com/u/637466?u=7912413a202659727afe7195da294896c6c14217&v=4&s=72)](https://github.com/rooterkyberian "@rooterkyberian")[![Image 52: djamatgit](https://avatars.githubusercontent.com/u/158511027?v=4&s=72)](https://github.com/djamatgit "@djamatgit")[![Image 53: Thraka](https://avatars.githubusercontent.com/u/2672110?u=7ebd7b7735555f7f37fbada3b2b9e276c4ff84c6&v=4&s=72)](https://github.com/Thraka "@Thraka")[![Image 54: jedzill4](https://avatars.githubusercontent.com/u/13605417?v=4&s=72)](https://github.com/jedzill4 "@jedzill4")[![Image 55: oronbz](https://avatars.githubusercontent.com/u/1288090?u=8aaf807a45ab8bc43c162a870758716f86e4d581&v=4&s=72)](https://github.com/oronbz "@oronbz")[![Image 56: myohei](https://avatars.githubusercontent.com/u/5871276?u=9f88b38700fcd0203af68b2e21fab28223beaaf7&v=4&s=72)](https://github.com/myohei "@myohei")[![Image 57: RobertoArtiles](https://avatars.githubusercontent.com/u/846820?u=74331668758d1d3bd9081eb97a0ce2bf7b0d58a7&v=4&s=72)](https://github.com/RobertoArtiles "@RobertoArtiles")[![Image 58: JayGhiya](https://avatars.githubusercontent.com/u/24807277?u=0d637f18d5ad2fae752315ce23f48241e8ea9eda&v=4&s=72)](https://github.com/JayGhiya "@JayGhiya")[![Image 59: rcdailey](https://avatars.githubusercontent.com/u/1768054?u=3a07ebbf1381519f8b8551cbbdb41c4851832205&v=4&s=72)](https://github.com/rcdailey "@rcdailey")[![Image 60: ohmantics](https://avatars.githubusercontent.com/u/1445253?v=4&s=72)](https://github.com/ohmantics "@ohmantics")[![Image 61: ryan-dsilva](https://avatars.githubusercontent.com/u/145395403?v=4&s=72)](https://github.com/ryan-dsilva "@ryan-dsilva")[![Image 62: waynehsmith](https://avatars.githubusercontent.com/u/17620269?u=dbbf5549f6b17e4dd33d99392978a1a9bdfeb7d9&v=4&s=72)](https://github.com/waynehsmith "@waynehsmith")[![Image 63: charlozard](https://avatars.githubusercontent.com/u/50652288?u=1e4813dae61a1f9d6cfad184d2d16c4100fc018f&v=4&s=72)](https://github.com/charlozard "@charlozard")[![Image 64: andreivladmatei](https://avatars.githubusercontent.com/u/19395668?u=23b151232d775506d3abf19baa31be9761593b43&v=4&s=72)](https://github.com/andreivladmatei "@andreivladmatei")[![Image 65: UberMouse](https://avatars.githubusercontent.com/u/693020?u=1bf013f6f4a8c7972e7cb0281d224a60ce2237fb&v=4&s=72)](https://github.com/UberMouse "@UberMouse")[![Image 66: h4rvey-g](https://avatars.githubusercontent.com/u/32609824?v=4&s=72)](https://github.com/h4rvey-g "@h4rvey-g")[![Image 67: kurtextrem](https://avatars.githubusercontent.com/u/502146?u=bb73286ca8f1b133342c413b8f4f9523d5403c20&v=4&s=72)](https://github.com/kurtextrem "@kurtextrem")[![Image 68: jhillyerd](https://avatars.githubusercontent.com/u/2502736?v=4&s=72)](https://github.com/jhillyerd "@jhillyerd")[![Image 69: Yecats](https://avatars.githubusercontent.com/u/4108756?u=d1e64472f1ce5a3ba74046dfe974cd92ec144308&v=4&s=72)](https://github.com/Yecats "@Yecats")[![Image 70: timrichardson](https://avatars.githubusercontent.com/u/927458?u=a1c3986a7d30a19dd988a91bde18ebea9470dc37&v=4&s=72)](https://github.com/timrichardson "@timrichardson")[![Image 71: kanchev1](https://avatars.githubusercontent.com/u/136312841?v=4&s=72)](https://github.com/kanchev1 "@kanchev1")[![Image 72: Raneddo](https://avatars.githubusercontent.com/u/15713492?u=6e7922ced58f93f29aa33add96ff223373e510ff&v=4&s=72)](https://github.com/Raneddo "@Raneddo")[![Image 73: arogulin](https://avatars.githubusercontent.com/u/1501897?u=d70b27e407160c693fb24be4a16e69b66485c45d&v=4&s=72)](https://github.com/arogulin "@arogulin")[![Image 74: DRBragg](https://avatars.githubusercontent.com/u/26798548?u=5a435c9d766f7c410728ba679b0049edda0b3d0d&v=4&s=72)](https://github.com/DRBragg "@DRBragg")[![Image 75: masterpavan](https://avatars.githubusercontent.com/u/19425282?u=af6819ab89fd58817862988a30b0dc4bbf7bdb0b&v=4&s=72)](https://github.com/masterpavan "@masterpavan")[![Image 76: MarceloPrado](https://avatars.githubusercontent.com/u/8047841?u=3844527e92235b716c256b13db9035e9442481e3&v=4&s=72)](https://github.com/MarceloPrado "@MarceloPrado")[![Image 77: iefnaf](https://avatars.githubusercontent.com/u/37260000?u=000a0ccedb103c30e0310f23294ce9b0a76c725e&v=4&s=72)](https://github.com/iefnaf "@iefnaf")[![Image 78: Flojomojo](https://avatars.githubusercontent.com/u/35773711?u=01d0065558de095148e41b3bc391464e596a207a&v=4&s=72)](https://github.com/Flojomojo "@Flojomojo")[![Image 79: bman654](https://avatars.githubusercontent.com/u/541772?v=4&s=72)](https://github.com/bman654 "@bman654")[![Image 80: andymac4182](https://avatars.githubusercontent.com/u/1297073?u=bd1dd0cffef33a6567bda8408d78731287179632&v=4&s=72)](https://github.com/andymac4182 "@andymac4182")[![Image 81: sercantor](https://avatars.githubusercontent.com/u/32751228?u=d15ec5b89ddfa7a574fded5ad5df1ddfb21ce1e7&v=4&s=72)](https://github.com/sercantor "@sercantor")[![Image 82: ovitrif](https://avatars.githubusercontent.com/u/4588074?u=e5e5d190b1c019ca18533a678da404da4ecd8988&v=4&s=72)](https://github.com/ovitrif "@ovitrif")[![Image 83: axelboman277](https://avatars.githubusercontent.com/u/153374328?v=4&s=72)](https://github.com/axelboman277 "@axelboman277")[![Image 84: rockneurotiko](https://avatars.githubusercontent.com/u/1377584?v=4&s=72)](https://github.com/rockneurotiko "@rockneurotiko")[![Image 85: linxi-1214](https://avatars.githubusercontent.com/u/20988026?u=f2209e95d54ac24d5288e0bb2f345d7759689183&v=4&s=72)](https://github.com/linxi-1214 "@linxi-1214")[![Image 86: 7tg](https://avatars.githubusercontent.com/u/20913374?u=4c923dd56beca8ae8535dd40cfb9bb77b14a5767&v=4&s=72)](https://github.com/7tg "@7tg")[![Image 87: Pollux12](https://avatars.githubusercontent.com/u/39353174?u=068723e547bb5a5fa1d15019f4e5528589e25228&v=4&s=72)](https://github.com/Pollux12 "@Pollux12")[![Image 88: grubmanItay](https://avatars.githubusercontent.com/u/93986984?u=4ef77f4e43929dea19b778442e63e88009c4b425&v=4&s=72)](https://github.com/grubmanItay "@grubmanItay")[![Image 89: 0xbentang](https://avatars.githubusercontent.com/u/33242068?v=4&s=72)](https://github.com/0xbentang "@0xbentang")[![Image 90: hackerbara](https://avatars.githubusercontent.com/u/264918693?u=b54474d0455cdf82842302fd569ff51a69b0a259&v=4&s=72)](https://github.com/hackerbara "@hackerbara")[![Image 91: xrd](https://avatars.githubusercontent.com/u/17064?u=e0d149d8650b8c75234f46e4f18d35b939aedb7d&v=4&s=72)](https://github.com/xrd "@xrd")[![Image 92: romanr](https://avatars.githubusercontent.com/u/329079?u=94fe2508769e13e99e225a7d5be369fb8bb655a3&v=4&s=72)](https://github.com/romanr "@romanr")[![Image 93: dgrissen2](https://avatars.githubusercontent.com/u/123790187?v=4&s=72)](https://github.com/dgrissen2 "@dgrissen2")[![Image 94: TomLucidor](https://avatars.githubusercontent.com/u/85554801?v=4&s=72)](https://github.com/TomLucidor "@TomLucidor")[![Image 95: thoroc](https://avatars.githubusercontent.com/u/2297889?u=6308073e02b024072885528ecef6e78fa7fb5774&v=4&s=72)](https://github.com/thoroc "@thoroc")[![Image 96: PetrBrabec](https://avatars.githubusercontent.com/u/9869048?u=35b62bc74fa594acab10054c7a82aa8c4d6132ae&v=4&s=72)](https://github.com/PetrBrabec "@PetrBrabec")
