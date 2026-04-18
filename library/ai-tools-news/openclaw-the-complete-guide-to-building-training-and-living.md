---
tags:
  - library
title: "OpenClaw: The complete guide to building, training, and living with your personal AI agent"
url: "https://substack.com/inbox/post/192645190"
company: [personal]
topics: []
created: 2026-04-01
source_type: raindrop
raindrop_id: 1668708012
source_domain: "substack.com"
source_type_raindrop: article
collection: "AI Tools & News"
collection_id: 69284314
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

I built a team of 9 AI agents that run my work and life. Here's how you can too.

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: OpenClaw: The complete guide to building, training, and living with your personal AI agent

URL Source: https://substack.com/inbox/post/192645190

Published Time: 2026-03-31T12:45:57+00:00

Markdown Content:
_👋 Hey there, I’m Lenny. Each week, I answer reader questions about building product, driving growth, and accelerating your career. For more: [Lenny’s Podcast](https://www.lennysnewsletter.com/podcast) | [Lennybot](https://www.lennybot.com/) | [How I AI](https://www.youtube.com/@howiaipodcast) | My favorite [AI/PM courses](https://maven.com/lenny), [public speaking course](https://ultraspeaking.com/lennyslist?via=lenny), and [interview prep copilot](https://www.benerez.com/copilot/lenny)_

_P.S. Get a full free year of Lovable, Manus, Replit, Gamma, n8n, Canva, ElevenLabs, Amp, Factory, Devin, Bolt, Wispr Flow, Linear, PostHog, Framer, Railway, Granola, Warp, Perplexity, Magic Patterns, Mobbin, ChatPRD, and Stripe Atlas [by becoming an Insider subscriber](https://www.lennysnewsletter.com/subscribe?plan=founding). [Yes, this is for real](https://www.lennysnewsletter.com/p/productpass)._

> **“OpenClaw is probably the single most important release of software, probably ever.” —Jensen Huang, Nvidia CEO**

Claire Vo has put together the definitive step-by-step guide to getting started with and mastering OpenClaw. Building on our [podcast episode](https://www.youtube.com/c/LennysPodcast), this post covers everything you need from first install to running a full team of AI agents, plus the specific use cases that have changed her life. Whether you’re brand new to OpenClaw or already running one, Claire’s guide will level you up.

_A big thank-you to [Peter Steinberger](https://x.com/steipete?lang=en), [Dave Morin](https://x.com/davemorin), and [Nat Eliason](https://x.com/nateliason) for reviewing drafts of this post. For more from Claire, check out her podcast [How I AI](https://www.youtube.com/@howiaipodcast) and [ChatPRD](https://www.chatprd.ai/), and find her on [X](https://x.com/clairevo) and [LinkedIn](https://www.linkedin.com/in/clairevo)._

[![Image 1](https://substackcdn.com/image/fetch/$s_!UV3b!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F828cd7bf-7e57-4cc3-bb72-2bcbbf5cac9e_2912x1940.png)](https://substackcdn.com/image/fetch/$s_!UV3b!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F828cd7bf-7e57-4cc3-bb72-2bcbbf5cac9e_2912x1940.png)

At 6 a.m., before I’ve looked at my phone, an AI agent named Polly has already read my email, checked my calendar, and queued up my day. By the time I sit down for coffee, another agent has reminded my husband about spirit day at school. A third AI is halfway through drafting a sales email, which will land in our prospect’s inbox three minutes after they contact us. One of the agents even helped draft this paragraph (though the rest was lovingly written by my human hands).

[![Image 2](https://substackcdn.com/image/fetch/$s_!a38x!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb8fd4dc5-83af-4a21-a7b3-830aad02efac_1456x1256.png)](https://substackcdn.com/image/fetch/$s_!a38x!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb8fd4dc5-83af-4a21-a7b3-830aad02efac_1456x1256.png)

None of this existed three months ago.

If you’re paying attention to AI news, you’ve probably heard about [OpenClaw](https://openclaw.ai/). For a while, it seemed like X was nothing but lobster emojis and breathless posts about _everything_ it can do: [running your business](https://creatoreconomy.so/p/use-openclaw-to-build-a-business-that-runs-itself-nat-eliason), [buying cars](https://aaronstuyvenberg.com/posts/clawd-bought-a-car), planning the AI uprising [with its friends](https://x.com/karpathy/status/2017296988589723767?s=20), and more. You’ve also probably seen some horror stories, like when it started deleting [this user’s full Gmail inbox](https://www.reddit.com/r/technology/comments/1rckxu7/meta_director_of_ai_safety_allows_ai_agent_to/), or that time [it completely screwed up my own personal calendar](https://x.com/clairevo/status/2015555956005011866).

You’re interested, and a little scared. I was too. But the idea of a dedicated personal assistant that could help run my life and businesses was so appealing that I had to dig in. The more I play with OpenClaw, the more convinced I am that it is one of _the_ most powerful AI tools for personal use, and a sign of where these tools are going.

Fast-forward two months, I’m chatting 24/7 with my nine (and counting!) OpenClaw agents, which operate my businesses, write code, close sales deals, and make sure I get to my kids’ basketball games on time.

[![Image 3](https://substackcdn.com/image/fetch/$s_!lK8_!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8d57c3b4-92ff-4c43-8e29-90ebb73fcbea_1456x1080.png)](https://substackcdn.com/image/fetch/$s_!lK8_!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8d57c3b4-92ff-4c43-8e29-90ebb73fcbea_1456x1080.png)

My OpenClaw agents in Telegram

OpenClaw is powerful but a little tricky to set up. After a lot of trial and error, I figured out how to make it work—and make my Claws work for me. Here’s exactly how you can too:

OpenClaw is an open-source personal AI assistant that is more powerful, more autonomous, and more fun to use than anything else I’ve tried. To tell it what needs to be done, you can message it easily on the platforms you already use, like WhatsApp, Telegram, Slack, etc. Then it can control your computer and take care of tasks just as you would, working on its own schedule—even overnight. It’s always on, runs locally, and it can build its own new skills. Teach it once; it handles the rest.

Practically, this means I can text my OpenClaw something like **“Let’s make sure our website always has the latest reasons why we’re better than competitors.”**It will use web search, our GitHub repo, and public APIs to find the information it needs, and ship PRs with the updates. Every week, it will refresh those pages with new data based on new features or market news.

One text turns into an always-on agent. But how you set it up is important, and understanding a few key concepts will save you tens of hours of frustration.

Key OpenClaw concepts:

*   It runs a **local gateway** that takes in messages. Think of this as a general-purpose inbox that can receive instructions from any **channel** (e.g. terminal, Telegram, WhatsApp, etc.)

*   Behind this gateway are **agents**, which have their own identities, tools, and workspaces

*   Agents work on a scheduled set of **cron jobs**and a **heartbeat** that gets checked every 30 minutes

*   It can use (and self-install!) **skills**,**APIs**, and**CLIs** to interact with systems and the outside world

*   It’s deployed on an owned**machine**, like a Mac Mini or a **VPS** on the cloud that you own and operate yourself

I’ve written in detail about the mechanics of OpenClaw [here](https://x.com/clairevo/status/2017741569521271175). The [docs](https://docs.openclaw.ai/) site is also very helpful, especially these top-level pages on channels, agents, and tools:

[![Image 4](https://substackcdn.com/image/fetch/$s_!n-U1!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5790d73f-4f41-4a59-88d3-19bd0978924c_1456x1311.png)](https://substackcdn.com/image/fetch/$s_!n-U1!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5790d73f-4f41-4a59-88d3-19bd0978924c_1456x1311.png)

But enough theory. Let’s set up your sentient virtual lobster.

You have options for where to install your OpenClaw, but most importantly, **do not install it on a work or personal computer that’s actively in use. This is very dangerous.** OpenClaw can technically have access to all the files on the computer it runs on, and no matter how careful you are, you don’t want to risk deleting everything, or emailing your personal files to an unsavory character.

The OpenClaw team has done a great job of hardening security, but it’s best to start with an isolated box.

You have three safe options for installing OpenClaw:

1.   **Sign up for a hosted version of OpenClaw.** Startups are popping up every week that make this easy to do. Some of the more popular options include [StartClaw](https://startclaw.com/), [MyClaw](https://myclaw.ai/), [SimpleClaw](https://www.simpleclaw.com/), [UniClaw](https://uniclaw.ai/), and Every’s [Plus One](https://every.to/plus-one). I experimented with a few of these, and they are slick, but I always got stuck on something. These products will get better, and I expect this to be how most people will experience OpenClaw over time.

2.   **Have it run in a virtual private server.** This may be the cheapest option, but it’s also the most complicated. Some of the more popular options include [Railway](https://railway.com/deploy/openclaw), [Hostinger](https://www.hostinger.com/vps/docker/openclaw), [DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-run-openclaw), [Google Cloud](https://docs.openclaw.ai/install/gcp), and [Render](https://docs.openclaw.ai/install/render). I didn’t try going this route, but many technical people prefer it, because it’s quick, powerful, and doesn’t require new hardware.

3.   **Use a laptop or (yes) a Mac Mini.** I started with an old MacBook Air and eventually moved to a stack of Mac Minis.

[![Image 5](https://substackcdn.com/image/fetch/$s_!yRld!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffa0559ea-fa46-4254-b942-3067a9c1d538_1116x1234.png)](https://substackcdn.com/image/fetch/$s_!yRld!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffa0559ea-fa46-4254-b942-3067a9c1d538_1116x1234.png)

You don’t actually have to run it on a [Mac Mini](https://www.apple.com/mac-mini/)—you can use any computer, even an old laptop—but the Mac Mini is simple, powerful, and compact. And it’s kind of become a meme. This option is the most expensive, at least up front, and time-consuming, but also the most fun, educational, and cute!

If you can swing it, I’d try this. (I got the lowest-end model: M4, 16GB, 256GB, about $600.) Just remember to grab a keyboard, mouse, and a monitor for your initial setup. Use whatever you have lying around; you won’t need it again after everything is running.

OK, you’ve got your machine booted up. Before we install the Claw, here are a few quick things that will make setup easier (this will take you about 10 minutes):

1.   Set up a fresh admin account and password on the computer you’ll be using

2.   [Sign up for a Gmail address](https://accounts.google.com/signin) for your agent (later, you can give it _read-only_ access to your calendar)

3.   Make sure [Chrome](https://www.google.com/chrome/) is installed, which is OpenClaw’s preferred browser

Open the terminal (_Command ⌘ + Space, type “Terminal,” hit Return_), and run:

> **curl -fsSL https://openclaw.ai/install.sh | bash**

This will install everything you need and drop you into the onboarding. If you get stuck, install [Claude Code](https://code.claude.com/) and/or [Codex](https://developers.openai.com/codex/cli) and ask for help!

Once the install is complete, OpenClaw will walk you through a guided onboarding flow step-by-step. The first step is acknowledging a security warning. Read this!

[![Image 6](https://substackcdn.com/image/fetch/$s_!Zm-W!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F12b699ed-042c-4c23-a4a5-8a95a9e60483_1456x1612.png)](https://substackcdn.com/image/fetch/$s_!Zm-W!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F12b699ed-042c-4c23-a4a5-8a95a9e60483_1456x1612.png)

If you’re ready for the adventure, you can continue through the onboarding. Here are my pro tips for the key steps:

If you’re not familiar with working in the terminal, the onboarding process is a little confusing. Use arrow keys to navigate up, down, left, and right, spacebar to select, and enter to submit.

I recommend Claude Opus 4.6 or Codex 5.4 (or whichever model is the most powerful at the time you’re reading this).

You have two options for using paid models like Opus or Codex:

**1. Use an existing subscription**by logging in to your Claude or ChatGPT account.

_Note_: There are some rumors that Anthropic is banning people who reuse their Claude accounts for OpenClaw. When using any third-party account with OpenClaw, review the terms of service and proceed at your own discretion.

**2. Use an API key**, which you can get by setting up a developer account at [Claude](https://platform.claude.com/) or [OpenAI](https://platform.openai.com/). This is the recommended path, and what I use.

[![Image 7](https://substackcdn.com/image/fetch/$s_!Mp_g!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbb3de89a-ecb4-455a-af34-5d88ed4d2f68_1456x480.png)](https://substackcdn.com/image/fetch/$s_!Mp_g!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbb3de89a-ecb4-455a-af34-5d88ed4d2f68_1456x480.png)

The best beginner-friendly channel is Telegram. More on this below.

[![Image 8](https://substackcdn.com/image/fetch/$s_!h62X!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F93c235b4-7bd0-4c88-b72c-fd078feb5c11_1456x895.png)](https://substackcdn.com/image/fetch/$s_!h62X!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F93c235b4-7bd0-4c88-b72c-fd078feb5c11_1456x895.png)

This will give your Claw access to the internet. You can skip and set this up later when you need it.

[![Image 9](https://substackcdn.com/image/fetch/$s_!4cZD!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F44b7bba5-7b70-4bda-b8cf-b05974af82c4_1456x683.png)](https://substackcdn.com/image/fetch/$s_!4cZD!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F44b7bba5-7b70-4bda-b8cf-b05974af82c4_1456x683.png)

I recommend the **gog** skill for Gmail, Google Calendar, and Docs access and **summarize** to start.

[![Image 10](https://substackcdn.com/image/fetch/$s_!M3EN!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe03f1d0f-a09d-4b8f-8459-3ad1a345c4a1_1456x1290.png)](https://substackcdn.com/image/fetch/$s_!M3EN!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe03f1d0f-a09d-4b8f-8459-3ad1a345c4a1_1456x1290.png)

These are helpful tools that keep your OpenClaw setup optimized. I turned on all four of these, but **session memory** is the most important. The others are helpful when you want to debug or optimize your agent.

[![Image 11](https://substackcdn.com/image/fetch/$s_!ZLtu!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd718987e-6a49-4bda-89c0-b8a3684c00f5_1456x685.png)](https://substackcdn.com/image/fetch/$s_!ZLtu!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd718987e-6a49-4bda-89c0-b8a3684c00f5_1456x685.png)

Then your agent will “hatch” in the TUI (Terminal UI). Hello, world!

[![Image 12](https://substackcdn.com/image/fetch/$s_!lIy_!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F08f8f0f4-4d1b-400d-86b1-3da5748b50d5_1456x861.png)](https://substackcdn.com/image/fetch/$s_!lIy_!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F08f8f0f4-4d1b-400d-86b1-3da5748b50d5_1456x861.png)

You’ll want a better chat interface than the terminal, so open up your phone and download [Telegram](https://telegram.org/), a messaging app and the simplest way to connect with your OpenClaw. If you ask OpenClaw, it can walk you through [the setup steps](https://docs.openclaw.ai/channels/telegram), including messaging the @BotFather (yes, really).

Setting up your agent is where you should put on your manager hat. Just like an employee, it can’t be good at _everything_, so think about a specific job for your OpenClaw. Personal assistant? Social media manager? Engineering intern? Start with one idea and you can always add on more later. If you’re unsure where to start, begin with a personal assistant like I did.

This is where things get fun. Once your OpenClaw is hatched, it will start asking you about yourself and itself to build its definitions and operating model.

You should make sure to share:

1.   Your name

2.   Your role/job

3.   Common admin challenges in your life (scheduling, remembering tasks, coordination with your family)

[![Image 13](https://substackcdn.com/image/fetch/$s_!2tqx!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd692c8e7-30d8-44b6-9f17-3e774bcb38b4_1456x907.png)](https://substackcdn.com/image/fetch/$s_!2tqx!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd692c8e7-30d8-44b6-9f17-3e774bcb38b4_1456x907.png)

All this gets written down by the agent and stored in the workspace folder you set up in onboarding (usually _**.openclaw/[agent\_name]-workspace**_) as Markdown files.

Those files become your agent’s identity and operating system. They are read every time your OpenClaw starts up and give your agent everything it needs to do a good job. It’s fun to look at these files; occasionally, you may need to go in and edit them.

*   **AGENTS.md**—OpenClaw’s core set of instructions and memory

*   **SOUL.md**—Your agent’s persona, tone of voice, and clear boundaries

*   **IDENTITY.md**—Your agent’s name, vibe, and personal emoji

*   **TOOLS.md**—Notes on tools and how your agent should use them

*   **USER.md**—All about you, your OpenClaw’s human

[![Image 14](https://substackcdn.com/image/fetch/$s_!rf-H!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6fd30a11-1092-4880-8b75-c8c588ee1e04_1456x850.png)](https://substackcdn.com/image/fetch/$s_!rf-H!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6fd30a11-1092-4880-8b75-c8c588ee1e04_1456x850.png)

Once its identity and role is set, it should ask you to get started on a first task. Time to Claw!

OK, so you finally have this bot set up. What do you actually _do_ with it?

I do a _lot_ with my OpenClaw agents now, but below are some easy places to start. Just copy and paste these prompts and OpenClaw will do the rest.

> _Every Friday, group message me and my husband to confirm the kids’ weekend activity logistics. If there is a conflict, confirm who will pick up each kid and any adjustments we may need to make to lunch or dinner plans. Ask us to explicitly confirm the plan and update our shared family calendar._

[![Image 15](https://substackcdn.com/image/fetch/$s_!KUDd!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F30a44790-cb24-4cf8-bab5-71e97eaac8bb_866x1214.png)](https://substackcdn.com/image/fetch/$s_!KUDd!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F30a44790-cb24-4cf8-bab5-71e97eaac8bb_866x1214.png)

> _Every morning, search for trending Reddit topics (r/funny, r/technology) about product management. Use the [MemeLord API](https://www.memelord.com/docs) to generate one image and one video meme, send it to me for approval, then post to TikTok._

[![Image 16](https://substackcdn.com/image/fetch/$s_!wEIV!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8832b2ec-5cf1-484b-b66d-a72a376c5db0_1600x1419.png)](https://substackcdn.com/image/fetch/$s_!wEIV!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8832b2ec-5cf1-484b-b66d-a72a376c5db0_1600x1419.png)

> _Every morning, look through the signups for the last 24 hours. Find everyone who signed up with a company domain, and categorize into high-value prospects based on our ideal customer profile. For ones with < 1,000 employees, send a light-touch email based on SALES\_PLAYBOOK.md. For companies with > 1,000 employees, enrich their profile with Exa People API and confirm with me before sending._

[![Image 17](https://substackcdn.com/image/fetch/$s_!5gzx!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4c80d510-1519-48be-a6a0-a5bfc6a68b73_978x932.png)](https://substackcdn.com/image/fetch/$s_!5gzx!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4c80d510-1519-48be-a6a0-a5bfc6a68b73_978x932.png)

> _Check all my calendars for any meetings starting in the next 30 minutes. If there is a meeting starting soon, send me a pre-meeting brief on Telegram. Include meeting title and time, who’s attending, and agenda if available from the calendar event description, and our last interaction based on the most recent email thread or meeting notes with this person/company._

[![Image 18](https://substackcdn.com/image/fetch/$s_!ue5f!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc99af76b-50b6-43f2-86b0-821a057654a2_708x986.png)](https://substackcdn.com/image/fetch/$s_!ue5f!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc99af76b-50b6-43f2-86b0-821a057654a2_708x986.png)

> _Every Friday evening, look over our resolved support tickets. If any question has been asked 3+ times this week: (1) flag it as a docs/FAQ candidate, (2) create a Linear issue and assign to @agent to add a docs page to/docs covering the answer, (3) include the standard answer you’ve been giving as a starting point in the issue description._

[![Image 19](https://substackcdn.com/image/fetch/$s_!u5P0!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F933989bc-7cf9-4a39-84a7-7efc70c76878_950x1154.png)](https://substackcdn.com/image/fetch/$s_!u5P0!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F933989bc-7cf9-4a39-84a7-7efc70c76878_950x1154.png)

> _I have a project launching on <date>. Keep a to-do list with everything I tell you I need to do for a successful launch, and break the plan down into daily tasks I can easily get done. At the end of the week, celebrate what I accomplished and flag what I missed. Make sure we do everything possible to make this project successful._

[![Image 20](https://substackcdn.com/image/fetch/$s_!RD0u!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F19db3611-cd89-4c32-b8f3-dd63df6c67fd_836x1078.png)](https://substackcdn.com/image/fetch/$s_!RD0u!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F19db3611-cd89-4c32-b8f3-dd63df6c67fd_836x1078.png)

[![Image 21](https://substackcdn.com/image/fetch/$s_!Y17o!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2b4ffd69-d3c3-4d47-8cd0-be336ecce46b_1456x1392.png)](https://substackcdn.com/image/fetch/$s_!Y17o!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2b4ffd69-d3c3-4d47-8cd0-be336ecce46b_1456x1392.png)
