---
tags:
  - library
title: "Organizing Personal and Project Settings in Claude Code"
url: "https://egghead.io/lessons/organizing-personal-and-project-settings-in-claude-code~q7qsw"
company: [personal]
topics: []
created: 2025-10-10
source_type: raindrop
raindrop_id: 1383028009
source_domain: "egghead.io"
source_type_raindrop: article
collection: "AI Tools & News"
collection_id: 69284314
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

Organizing Claude Code settings keeps the team aligned. Separate project rules from personal tweaks so the repo stays clean and flexible.

Ignore person...

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: Organizing Personal and Project Settings in Claude Code

URL Source: https://egghead.io/lessons/organizing-personal-and-project-settings-in-claude-code~q7qsw

Markdown Content:
# Organizing Personal and Project Settings in Claude Code | egghead.io

[egghead.io](https://egghead.io/)

Topics

[Courses](https://egghead.io/q?type=playlist)[Newsletter](https://egghead.io/newsletters/ai-dev-essentials)

Search

[Enroll Today](https://egghead.io/pricing)

[Sign in](https://egghead.io/login)

Open navigation

![Image 1: illustration for Claude Code Essentials](https://egghead.io/_next/image?url=https%3A%2F%2Fres.cloudinary.com%2Fdg3gyk0gu%2Fimage%2Fupload%2Fv1758918145%2Fclaude_hfq89e.png&w=3840&q=75)

Course## [Claude Code Essentials](https://egghead.io/courses/claude-code-essentials~jc0n6)

1.   [1 Combine Claude Code and Your Favorite IDE](https://egghead.io/lessons/combine-claude-code-and-your-favorite-ide~doycf) 
2.   [2 The Essential Claude Code Shortcuts](https://egghead.io/lessons/the-essential-claude-code-shortcuts~dgsee) 
3.   [3 Targeting the Proper Context with Claude Code](https://egghead.io/lessons/targeting-the-proper-context-with-claude-code~2i20r) 
4.   [4 Automate Tasks in Claude Code with Slash Commands](https://egghead.io/lessons/automate-tasks-in-claude-code-with-slash-commands~ylxki) 
5.   [5 The Cost of Context in Claude Code](https://egghead.io/lessons/the-cost-of-context-in-claude-code~rku9p) 
6.   [6 Protect Secrets from Being Read by Claude Code](https://egghead.io/lessons/protect-secrets-from-being-read-by-claude-code~vd9jk) 
7.    7  Organizing Personal and Project Settings in Claude Code      
8.   [8 Customize Global User Settings and the Status Line in Claude Code](https://egghead.io/lessons/customize-global-user-settings-and-the-status-line-in-claude-code~gtxfs) 
9.   [9 CLAUDE.md Initialization and Best Practices in Claude Code](https://egghead.io/lessons/claude-md-initialization-and-best-practices-in-claude-code~jae0x) 
10.   [10 Type-Safe Claude Code Hooks with Bun and TypeScript](https://egghead.io/lessons/type-safe-claude-code-hooks-with-bun-and-type-script~76nmz) 
11.   [11 Rewrite Prompts on the Fly with UserPromptSubmit Hooks](https://egghead.io/lessons/rewrite-prompts-on-the-fly-with-user-prompt-submit-hooks~76rrt) 
12.   [12 Inject Live Data with Custom Hook Functions](https://egghead.io/lessons/inject-live-data-with-custom-hook-functions~6ue6t) 
13.   [13 Generate Multiple Solutions with Template-Driven Hooks](https://egghead.io/lessons/generate-multiple-solutions-with-template-driven-hooks~0frnb) 
14.   [14 Block Prompts with Hook Guardrails](https://egghead.io/lessons/block-prompts-with-hook-guardrails~vhgyz) 
15.   [15 Block Tool Commands Before Execution with PreToolUse Hooks](https://egghead.io/lessons/block-tool-commands-before-execution-with-pre-tool-use-hooks~erv55) 
16.   [16 Guide Claude Code with Rich PreToolUse Feedback](https://egghead.io/lessons/guide-claude-code-with-rich-pre-tool-use-feedback~ex177) 
17.   [17 Enforce Global Rules with User-Level PreToolUse Hooks](https://egghead.io/lessons/enforce-global-rules-with-user-level-pre-tool-use-hooks~lljm2) 

Autoplay is off

off

# Organizing Personal and Project Settings in Claude Code

[![Image 2](blob:http://localhost/a880d0b2a5372f0c3c1ff54eb5d76ff8)![Image 3: John Lindquist](https://egghead.io/_next/image?url=https%3A%2F%2Fd2eip9sf3oo6c2.cloudfront.net%2Finstructors%2Favatars%2F000%2F000%2F005%2Fsquare_64%2Favatar-500x500.jpg&w=96&q=75)](https://egghead.io/q/resources-by-john-lindquist)

Instructor[John Lindquist](https://egghead.io/q/resources-by-john-lindquist)

*   [![Image 4: claude-code](https://egghead.io/_next/image?url=https%3A%2F%2Fres.cloudinary.com%2Fdg3gyk0gu%2Fimage%2Fupload%2Fw_72%2Ch_72%2Fv1683914713%2Ftags%2Fclaude-code.png&w=48&q=75)Claude Code](https://egghead.io/q/claude-code)

## Social Share Links

[Tweet](https://twitter.com/intent/tweet/?text=Organizing%20Personal%20and%20Project%20Settings%20in%20Claude%20Code%20by%20@johnlindquist%20(lesson%20on%20@eggheadio)&url=https%3A%2F%2Fegghead.io%2Flessons%2Forganizing-personal-and-project-settings-in-claude-code~q7qsw)

Copy link

Copy lesson as prompt

Published 7 months ago

Updated 7 months ago

Organizing Claude Code settings keeps the team aligned. Separate project rules from personal tweaks so the repo stays clean and flexible.

## Ignore personal settings

Add to `.gitignore`:

```bash
.claude/settings.local.json
```

## Personalize locally

Use the local file for machine-specific tweaks (paths, extra directories):

```json
{
  "permissions": { "allow": [], "deny": [], "ask": [] },
  "additionalDirectories": ["/Users/you/dev/docs"]
}
```

## Share team rules

Commit `.claude/settings.json` for org-wide policies (e.g., deny reading `.env`):

```json
{
  "permissions": {
    "allow": [],
    "deny": ["Read(.env)"],
    "ask": []
  }
}
```

### Merge semantics

Settings **combine**; they don’t override. A project-level **deny** cannot be undone by a local **allow**.

Transcript Comments (0)

[00:00] Now your settings.local.json should be added to your gitignore. I'll go ahead and create one with the gitignore command. We'll say this is a node project and this just generates one. I'll open it up, gitignore. So just make sure that clod settings.local.json is added in there so that it's removed from git.

[00:21] The reason being that it's quite possible when you're configuring your own settings that maybe you have some documentation you want to add. So let's say an add dir. I want my clod to also be able to look into my dev, kit container, docs directory. And I wanted to remember it for this directory so that now in my settings local json my instance of clod is able to access the docs. So if I clear out the session and I just ask it to please ls the docster, you'll see it has access to that directory and is able to, if I hit ctrl-o, run commands and do things in that directory.

[01:02] Now obviously in other people's machines they won't have this directory set up. They'd want to customize that for themselves and for this specific project. But if you want to hoist something like DENY up into the project level, we can essentially copy and paste this. We'll rename this to settings.json, and this is a file that you would check in. And we're going to remove additional directories.

[01:23] We'll keep readenv, and we'll remove readenv from here. This way this file is checked in and everyone on your project will have the same deny list, and you can have your own custom configuration with your custom paths. If you have custom scripts or custom tools you want to run that are only on your machine you could add those here. And don't necessarily treat your local settings as something that overrides these settings, it's more thinking about it as customizing it for your system. Because if the project level denies this, then adding allow here is not going to override the project level settings.

[02:00] Thanks.

![Image 5](blob:http://localhost/a880d0b2a5372f0c3c1ff54eb5d76ff8)![Image 6: egghead](blob:http://localhost/b9a31d3949b1882a09ed2f8508d538f3)

egghead

Member comments are a way for members to communicate, interact, and ask questions about a lesson.

The instructor or someone from the community might respond to your question Here are a few basic guidelines to commenting on egghead.io

**Be on-Topic**

Comments are for discussing a lesson. If you're having a general issue with the website functionality, please contact us at support@egghead.io.

**Avoid meta-discussion**

*   This was great!
*   This was horrible!
*   I didn't like this because it didn't match my skill level.
*   +1 It will likely be deleted as spam.

**Code Problems?**

Should be accompanied by code! Codesandbox or Stackblitz provide a way to share code and discuss it in context

**Details and Context**

Vague question? Vague answer. Any details and context you can provide will lure more interesting answers!

Send

Markdown supported.

ℹ

 Become a member to join the discussion[Enroll Today](https://egghead.io/pricing)

[![Image 7: egghead.io logo](blob:http://localhost/e501c3f1827e611d8c8188e7a8740c04) Expert led courses for professional front-end web developers.](https://egghead.io/)

*   [Search](https://egghead.io/q)
*   [Articles](https://egghead.io/q?type=article)
*   [Talks](https://egghead.io/talks)
*   [Podcasts](https://egghead.io/podcasts)
*   [Topics](https://egghead.io/topics)
*   [Machine](https://egghead.io/site-directory)

*   [Pricing](https://egghead.io/pricing)
*   [egghead for teams](https://egghead.io/egghead-for-teams)
*   [Store](https://store.egghead.io/)
*   [support@egghead.io](mailto:support@egghead.io)

©egghead.io

[Terms & Conditions](https://egghead.io/privacy)[FAQ](https://egghead.io/faq)

Light Mode
