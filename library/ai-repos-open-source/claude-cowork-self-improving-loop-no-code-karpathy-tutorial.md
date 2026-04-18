---
tags:
  - library
title: "Claude Cowork Self-Improving Loop: No-Code Karpathy Tutorial (2026)"
url: "https://open.substack.com/pub/karozieminski/p/claude-cowork-self-improving-automation-karpathy-loop-2026?r=1g8z0m&utm_medium=ios"
company: [personal]
topics: []
created: 2026-04-09
source_type: raindrop
raindrop_id: 1678464289
source_domain: "open.substack.com"
source_type_raindrop: article
collection: "AI Repos & Open Source"
collection_id: 69284315
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

Build a no-code self-improving automation loop in Claude Cowork using Karpathy's autoresearch pattern. Context.md template, eval rubric, and Reflection Skill.

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: Claude Cowork Self-Improving Loop: No-Code Karpathy Tutorial (2026)

URL Source: https://open.substack.com/pub/karozieminski/p/claude-cowork-self-improving-automation-karpathy-loop-2026?r=1g8z0m

Published Time: 2026-04-09T06:26:04+00:00

Markdown Content:
# Claude Cowork Self-Improving Loop: No-Code Karpathy Tutorial (2026)

[![Image 2: Product with Attitude](https://substackcdn.com/image/fetch/$s_!KJxv!,w_40,h_40,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3f411cce-3771-42d9-965e-1c01efe464eb_986x986.png)](https://open.substack.com/)

# [![Image 3: Product with Attitude](https://substackcdn.com/image/fetch/$s_!MMZr!,e_trim:10:white/e_trim:10:transparent/h_220,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5a09c22e-1bc0-4ef8-98a4-e60abf51b130_1344x256.png)](https://open.substack.com/)

Subscribe Sign in

# I Built a Claude Cowork Loop That Improves Itself. Here's the Exact Setup.

### Anthropic slipped Cowork’s most interesting behavior into a support article. I turned it into a Karpathy-inspired system that gets smarter without writing a line of code.

[![Image 4: Karo (Product with Attitude)'s avatar](https://substackcdn.com/image/fetch/$s_!aG8-!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F599e664e-d6b8-4249-814a-4feadc68d706_1096x1096.png)](https://substack.com/@karozieminski)

[Karo (Product with Attitude)](https://substack.com/@karozieminski)

Apr 09, 2026

∙ Paid

107

5

11

Share

_**TL;DR

Cowork Self-Improving Loop = Karpathy Auto-Research pattern + recurring tasks.**_

Somehow, Anthropic managed to hide Cowork’s best kept secret in a support article about recurring tasks.

Very few people seem to know about it, and I haven’t seen anyone intentionally building on top of it.

This guide is my attempt to change that.

By the end, you’ll be running a self-improving loop I built on top of [Karpathy’s Auto-Research Pattern](https://www.mindstudio.ai/blog/what-is-autoresearch-loop-karpathy-business-optimization), adapted for Cowork.

So even if Claude Code feels intimidating, you’re covered.

[![Image 5: Transparent divider.](https://substackcdn.com/image/fetch/$s_!QqMl!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdd302db1-d1e6-4d1d-861a-118f27049ad6_2400x31.png)](https://substackcdn.com/image/fetch/$s_!QqMl!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdd302db1-d1e6-4d1d-861a-118f27049ad6_2400x31.png)

Hey, I’m Karo 🤗

I’m an AI Product Manager and [builder](https://karozieminski.substack.com/p/substack-creator-tools). I write Product with Attitude, a newsletter about building with AI and developing critical AI literacy through practice.

If you’re new here, welcome! 

Here’s what you might have missed:

→ [Claude Cowork Guide for Power Users (2026)](https://karozieminski.substack.com/p/claude-cowork-guide-2026)

→ [Claude Skills Are Taking the AI Community by Storm](https://karozieminski.substack.com/p/claude-skills-anthropic-viral-toolkit-agentic-workflows-community-guide)

Join 17K readers and learn AI the only way it sticks: through immersion in real experiments and real projects.

[SUBSCRIBE](https://karozieminski.substack.com/subscribe)

[![Image 6: Section divider](https://substackcdn.com/image/fetch/$s_!jVAL!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa17b1657-2e33-4bc2-b978-23134ab2fb0e_2396x335.png)](https://substackcdn.com/image/fetch/$s_!jVAL!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa17b1657-2e33-4bc2-b978-23134ab2fb0e_2396x335.png)

## What’s Inside

[![Image 7: Three-dimensional perspective stack showing 3 layered infographics covering Claude Cowork project creation, iteration log, and workflow steps, displayed in a cascading fan arrangement. Created for Product with Attitude.](https://substackcdn.com/image/fetch/$s_!ERwn!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F27f3cfec-96f9-45cc-aa21-92c256399dbe_2647x1117.png)](https://substackcdn.com/image/fetch/$s_!ERwn!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F27f3cfec-96f9-45cc-aa21-92c256399dbe_2647x1117.png)

*   How to turn Anthropic’s Claude Cowork into a self-improving AI agent

*   How Cowork already rewrites its own scheduled task prompts after the first run, even though almost nobody has noticed.

*   The full no-code architecture: context.md, folder instructions, and the improvement directive that makes the loop work.

*   Step-by-step tutorial from project creation to a running automation loop.

*   Ready-to-use prompts.

*   Risks, guardrails, and what happens after 20-30 runs.

[![Image 8: Section divider](https://substackcdn.com/image/fetch/$s_!jVAL!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa17b1657-2e33-4bc2-b978-23134ab2fb0e_2396x335.png)](https://substackcdn.com/image/fetch/$s_!jVAL!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa17b1657-2e33-4bc2-b978-23134ab2fb0e_2396x335.png)

## AI Prompts & Skill Decay: The Problem Self-Improving Loops Fix

> **A workflow could sit at half its potential for months and we’d never know because we stopped looking.**

Every AI workflow decays.

We set up an AI workflow. It works beautifully at first.

Then the world around it changes: files move, naming conventions change, things get re-organized, new edge cases pile up.

The instructions stay frozen, our needs don’t.

The conventional fix would be to open the prompt/Skill, read through it, edit it, test it again. Rinse, repeat, lose a chunk of our busy week to maintenance.

And it has a blind spot: 

we only improve _what we've already seen go wrong_.

New inputs, new edge cases, new failure modes, those slip through.

A self-improving loop changes that. It makes improvement part of the task, not something you remember to do when things go wrong.

[![Image 9: Section divider](https://substackcdn.com/image/fetch/$s_!jVAL!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa17b1657-2e33-4bc2-b978-23134ab2fb0e_2396x335.png)](https://substackcdn.com/image/fetch/$s_!jVAL!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa17b1657-2e33-4bc2-b978-23134ab2fb0e_2396x335.png)

## What Anthropic’s Claude Cowork Does After Its First Scheduled Run

When we set up a recurring task in Cowork and run it for the first time, Claude rewrites the task prompt based on what it learned.

It happens automatically.

It maps connectors, identifies file paths, resolves format issues, effectively improving its own instructions.

That’s because each [scheduled task runs as a completely isolated Cowork session](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-cowork). That means no automatic memory of the conversation that created it and no access to what happened before.

The rewritten prompt is the only thread of continuity; it's effectively the `CLAUDE.md` for that task.

By the second run, the prompt is more precise than what we originally wrote.

And this is the reason the self-improving loop is even possible.

[![Image 10: Section divider](https://substackcdn.com/image/fetch/$s_!jVAL!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa17b1657-2e33-4bc2-b978-23134ab2fb0e_2396x335.png)](https://substackcdn.com/image/fetch/$s_!jVAL!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa17b1657-2e33-4bc2-b978-23134ab2fb0e_2396x335.png)

## The Difference Between The Native Rewriting And A Self-Improving Automation Loop

The difference between this native rewriting and a self-improving loop is one word: strategy.

*   **Native rewriting optimizes for**_**connector accuracy**_**.**

It makes sure Google Drive paths resolve, Slack channels map correctly, and output formats match expectations.

*   **The self-improving loop optimizes for**_**quality**_**and**_**relevance**_**.**

It rewrites the execution strategy itself: what to look for, how to structure outputs, which edge cases to handle, what to skip.

[![Image 11: Section divider](https://substackcdn.com/image/fetch/$s_!jVAL!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa17b1657-2e33-4bc2-b978-23134ab2fb0e_2396x335.png)](https://substackcdn.com/image/fetch/$s_!jVAL!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa17b1657-2e33-4bc2-b978-23134ab2fb0e_2396x335.png)

## The Cowork Self-Improving Loop vs. the Karpathy Loop

This idea isn’t new.

Developers have been building self-improving AI loops in code-heavy tools for months, with [Andrej Karpathy’s autoresearch loop](https://www.mindstudio.ai/blog/what-is-autoresearch-loop-karpathy-business-optimization) going viral.

[![Image 12: X avatar for @karpathy](https://substackcdn.com/image/fetch/$s_!oMwR!,w_40,h_40,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fpbs.substack.com%2Fprofile_images%2F1296667294148382721%2F9Pr6XrPB.jpg) Andrej Karpathy@karpathy I packaged up the "autoresearch" project into a new self-contained minimal repo if people would like to play over the weekend. It's basically nanochat LLM training core stripped down to a single-GPU, one file version of ~630 lines of code, then: - the human iterates on the ![Image 13](https://pbs.substack.com/media/HC1KyorbEAAoGWr.jpg) 7:53 PM · Mar 7, 2026 · 10.9M Views * * * 1.05K Replies · 3.66K Reposts · 28.3K Likes](https://x.com/karpathy/status/2030371219518931079?s=20)
The difference is that those setups require a terminal, scripting knowledge, and a developer workflow.

> **What I’m proposing achieves the same result in Cowork, via a visual interface and one command. No code, no terminal.**

[![Image 14: Section divider](https://substackcdn.com/image/fetch/$s_!jVAL!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa17b1657-2e33-4bc2-b978-23134ab2fb0e_2396x335.png)](https://substackcdn.com/image/fetch/$s_!jVAL!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa17b1657-2e33-4bc2-b978-23134ab2fb0e_2396x335.png)

## Claude Cowork vs Claude Code: Two Paths To The Same Pattern

Both Claude Code and Cowork support self-improving loops, but the implementation is different.

The Code path wins on depth of the optimization system. The Cowork path wins on accessibility. If “self-improving AI workflow without a terminal” describes what you need, this is the tutorial.

**This guide covers the Cowork path exclusively: no terminal, no code repository.**

**And it requires only three things working together:**

Without the improvement directive, Cowork rewrites for connectors.

With it, Cowork rewrites for outcomes.

[![Image 15: Section divider](https://substackcdn.com/image/fetch/$s_!jVAL!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa17b1657-2e33-4bc2-b978-23134ab2fb0e_2396x335.png)](https://substackcdn.com/image/fetch/$s_!jVAL!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa17b1657-2e33-4bc2-b978-23134ab2fb0e_2396x335.png)

[![Image 16](https://substackcdn.com/image/fetch/$s_!b9Wk!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc7a3744f-d15b-463d-b1d8-9d362b772c20_727x52.png)](https://substackcdn.com/image/fetch/$s_!b9Wk!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc7a3744f-d15b-463d-b1d8-9d362b772c20_727x52.png)

_Premium members get the complete playbook: 

- the full architecture diagram, 

- step-by-step setup 

- the Reflection Skill that makes improvement passes surgical, 

- my real before/after context.md showing 10 runs of evolution, 

- the evaluation rubric that measures whether the loop is working,

- and a guardrail system that prevents instruction drift._

## The Full Architecture

Each cycle tightens the Execution Instructions toward our specific workflow. Not a generic template.

After 10+ runs, `context.md` contains a playbook Claude wrote for itself.

Here is how every piece connects:

## This post is for paid subscribers

[Subscribe](https://karozieminski.substack.com/subscribe?simple=true&next=https%3A%2F%2Fkarozieminski.substack.com%2Fp%2Fclaude-cowork-self-improving-automation-karpathy-loop-2026%3Fr%3D1g8z0m%26triedRedirect%3Dtrue&utm_source=paywall&utm_medium=web&utm_content=192698447)

[Already a paid subscriber? **Sign in**](https://substack.com/sign-in?redirect=%2Fp%2Fclaude-cowork-self-improving-automation-karpathy-loop-2026%3Fr%3D1g8z0m%26triedRedirect%3Dtrue&for_pub=karozieminski&change_user=false)

Previous Next

© 2026 Karolina Zieminski · [Privacy](https://substack.com/privacy) ∙ [Terms](https://substack.com/tos) ∙ [Collection notice](https://substack.com/ccpa#personal-data-collected)

[Start your Substack](https://substack.com/signup?utm_source=substack&utm_medium=web&utm_content=footer)[Get the app](https://substack.com/app/app-store-redirect?utm_campaign=app-marketing&utm_content=web-footer-button)

[Substack](https://substack.com/) is the home for great culture

![Image 19: User's avatar](https://substackcdn.com/image/fetch/$s_!TOma!,w_64,h_64,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff4139267-58c3-4420-aa37-8cd8a9f7a198_2320x2320.jpeg)

### Robert Guss, a subscriber of Product with Attitude, shared this with you.

Follow Robert and continue reading Skip

![Image 20](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%26800%26600%268%2624%26800%26600%260%26na&eci=3&event=%7B%7D&event_id=798c683e-118b-4e3a-aed0-cd23c110a2a3&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=19c6ca39-9be6-414e-8efc-05b0bbf983c1&pt=Claude%20Cowork%20Self-Improving%20Loop%3A%20No-Code%20Karpathy%20Tutorial%20(2026)&tw_document_href=https%3A%2F%2Fkarozieminski.substack.com%2Fp%2Fclaude-cowork-self-improving-automation-karpathy-loop-2026%3Fr%3D1g8z0m%26triedRedirect%3Dtrue&tw_iframe_status=0&tw_pid_src=1&twpid=tw.1776471112775.429491625790216912&txn_id=ppzjp&type=javascript&version=2.3.52)![Image 21](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%26800%26600%268%2624%26800%26600%260%26na&eci=3&event=%7B%7D&event_id=798c683e-118b-4e3a-aed0-cd23c110a2a3&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=19c6ca39-9be6-414e-8efc-05b0bbf983c1&pt=Claude%20Cowork%20Self-Improving%20Loop%3A%20No-Code%20Karpathy%20Tutorial%20(2026)&tw_document_href=https%3A%2F%2Fkarozieminski.substack.com%2Fp%2Fclaude-cowork-self-improving-automation-karpathy-loop-2026%3Fr%3D1g8z0m%26triedRedirect%3Dtrue&tw_iframe_status=0&tw_pid_src=1&twpid=tw.1776471112775.429491625790216912&txn_id=ppzjp&type=javascript&version=2.3.52)
