---
tags:
  - library
title: "Open Models have crossed a threshold"
url: "https://www.linkedin.com/pulse/open-models-have-crossed-threshold-mason-daugherty-jsjme?utm_source=share&utm_medium=member_ios&utm_campaign=share_via"
company: [personal]
topics: []
created: 2026-04-04
source_type: raindrop
raindrop_id: 1672467288
source_domain: "linkedin.com"
source_type_raindrop: article
collection: "AI Tools & News"
collection_id: 69284314
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

TL;DR: Open models like GLM-5 and MiniMax M2.7 now match closed frontier models on core agent tasks — file operations, tool use, and instruction following — at a fraction of the cost and latency.

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: Open Models have crossed a threshold

URL Source: https://www.linkedin.com/pulse/open-models-have-crossed-threshold-mason-daugherty-jsjme

Markdown Content:
# Open Models have crossed a threshold

Agree & Join LinkedIn

By clicking Continue to join or sign in, you agree to LinkedIn’s [User Agreement](https://www.linkedin.com/legal/user-agreement?trk=linkedin-tc_auth-button_user-agreement), [Privacy Policy](https://www.linkedin.com/legal/privacy-policy?trk=linkedin-tc_auth-button_privacy-policy), and [Cookie Policy](https://www.linkedin.com/legal/cookie-policy?trk=linkedin-tc_auth-button_cookie-policy).

[Skip to main content](https://www.linkedin.com/pulse/open-models-have-crossed-threshold-mason-daugherty-jsjme#main-content)[LinkedIn](https://www.linkedin.com/?trk=article-ssr-frontend-pulse_nav-header-logo)
*   [Top Content](https://www.linkedin.com/top-content?trk=article-ssr-frontend-pulse_guest_nav_menu_topContent)
*   [People](https://www.linkedin.com/pub/dir/+/+?trk=article-ssr-frontend-pulse_guest_nav_menu_people)
*   [Learning](https://www.linkedin.com/learning/search?trk=article-ssr-frontend-pulse_guest_nav_menu_learning)
*   [Jobs](https://www.linkedin.com/jobs/search?trk=article-ssr-frontend-pulse_guest_nav_menu_jobs)
*   [Games](https://www.linkedin.com/games?trk=article-ssr-frontend-pulse_guest_nav_menu_games)

[Sign in](https://www.linkedin.com/uas/login?session_redirect=%2Fpulse%2Fopen-models-have-crossed-threshold-mason-daugherty-jsjme&fromSignIn=true&trk=article-ssr-frontend-pulse_nav-header-signin)[Join now](https://www.linkedin.com/signup/cold-join?session_redirect=%2Fpulse%2Fopen-models-have-crossed-threshold-mason-daugherty-jsjme&trk=article-ssr-frontend-pulse_nav-header-join)[![Image 1: Mason D.](https://static.licdn.com/aero-v1/sc/h/9c8pery4andzj6ohjkjp54ma2)](https://www.linkedin.com/uas/login?session_redirect=%2Fpulse%2Fopen-models-have-crossed-threshold-mason-daugherty-jsjme&fromSignIn=true&trk=article-ssr-frontend-pulse_nav-header-signin)

![Image 2: Open Models have crossed a threshold](https://media.licdn.com/dms/image/v2/D4E12AQFBlZcWF7PNsQ/article-cover_image-shrink_720_1280/B4EZ1PdYeQHUAI-/0/1775154596514?e=2147483647&v=beta&t=Uk3bgy7WQmSP2_u1xvapO-c6Gu-xCKleBkuk5G33W6Y)

# Open Models have crossed a threshold

*   [Report this article](https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fpulse%2Fopen-models-have-crossed-threshold-mason-daugherty-jsjme&trk=article-ssr-frontend-pulse_ellipsis-menu-semaphore-sign-in-redirect&guestReportContentType=PONCHO_ARTICLE&_f=guest-reporting)

[Mason D.](https://www.linkedin.com/in/mdrxy)![Image 3: Mason D.](https://static.licdn.com/aero-v1/sc/h/9c8pery4andzj6ohjkjp54ma2)

### Mason D.

 Published Apr 2, 2026 

[+ Follow](https://www.linkedin.com/signup/cold-join?session_redirect=%2Fpulse%2Fopen-models-have-crossed-threshold-mason-daugherty-jsjme&trk=article-ssr-frontend-pulse_publisher-author-card)

TL;DR: Open models like GLM-5 and MiniMax M2.7 now match closed frontier models on core agent tasks — file operations, tool use, and instruction following — at a fraction of the cost and latency. Here's what our evals show and how to start using them in Deep Agents.

* * *

Over the past few weeks, we’ve been running open weight Large Language Models through [Deep Agents](https://www.linkedin.com/redir/redirect?url=https%3A%2F%2Fgithub%2Ecom%2Flangchain-ai%2Fdeepagents&urlhash=cQRT&trk=article-ssr-frontend-pulse_little-text-block) harness evaluations, and the initial results show they are a viable option to use instead of, and alongside, closed frontier models. GLM-5 ([z.ai](https://www.linkedin.com/redir/redirect?url=http%3A%2F%2Fz%2Eai&urlhash=OQwk&trk=article-ssr-frontend-pulse_little-text-block)) and [MiniMax](https://www.linkedin.com/redir/redirect?url=https%3A%2F%2Fwww%2Eminimax%2Eio%2Fmodels%2Ftext%2Fm27&urlhash=VBhR&trk=article-ssr-frontend-pulse_little-text-block) M2.7 each score similarly to closed frontier models on core agent tasks such as file operations, tool use, and instruction following.

This isn’t surprising if you’ve been following open model progress via the large set of open benchmarks such as [SWE-Rebench](https://www.linkedin.com/redir/redirect?url=https%3A%2F%2Fswe-rebench%2Ecom%2F&urlhash=R_RF&trk=article-ssr-frontend-pulse_little-text-block) and [Terminal Bench 2.0](https://www.linkedin.com/redir/redirect?url=https%3A%2F%2Fwww%2Etbench%2Eai%2Fleaderboard%2Fterminal-bench%2F2%2E0&urlhash=HAtv&trk=article-ssr-frontend-pulse_little-text-block). Tool calling is reliable and instruction following is consistent. For developers deploying agents in production, open models now offer a level of consistency and predictability that makes real-world workflows much more viable.

### Why open models

When exploring open models, builders and customers tend to focus on a few key factors: cost, latency, and task performance.

In the limit, it would be great to use the smartest frontier model at the highest reasoning level for every task. In practice, two constraints make that unworkable: cost and latency. Closed frontier models can run 8–10x more expensive for high-throughput workloads, and they're often too slow for the response times users expect in interactive products.

![Image 4: Article content](https://www.linkedin.com/pulse/open-models-have-crossed-threshold-mason-daugherty-jsjme)

To put the pricing in context: an application outputting 10M tokens/day costs roughly $250/day on Opus 4.6 versus ~$12/day for MiniMax M2.7. That's about a $87k annual difference.

Open models tend to be smaller than closed frontier models, and can be accelerated on specialized inference infrastructure — providers like [Groq](https://www.linkedin.com/redir/redirect?url=https%3A%2F%2Fgroq%2Ecom%2F&urlhash=2qfY&trk=article-ssr-frontend-pulse_little-text-block), [Fireworks](https://www.linkedin.com/redir/redirect?url=https%3A%2F%2Ffireworks%2Eai%2F&urlhash=Bp62&trk=article-ssr-frontend-pulse_little-text-block), and [Baseten](https://www.linkedin.com/redir/redirect?url=https%3A%2F%2Fwww%2Ebaseten%2Eco%2F&urlhash=szVT&trk=article-ssr-frontend-pulse_little-text-block) optimize for latency and throughput far beyond what most teams could achieve on their own. [OpenRouter data](https://www.linkedin.com/redir/redirect?url=https%3A%2F%2Fopenrouter%2Eai%2Fz-ai%2Fglm-5%2Fperformance&urlhash=tIUu&trk=article-ssr-frontend-pulse_little-text-block) show GLM-5 on Baseten averaging 0.65s latency and 70 tokens/second, compared to 2.56s and 34 tokens/second for Claude Opus 4.6. For latency-sensitive products, that gap is hard to engineer around.

### How we evaluated

We've written about our eval methodology in depth in [How we build evals for Deep Agents](https://www.linkedin.com/redir/redirect?url=https%3A%2F%2Fblog%2Elangchain%2Ecom%2Fhow-we-build-evals-for-deep-agents%2F&urlhash=I9RE&trk=article-ssr-frontend-pulse_little-text-block). We run evals using hosted inference providers, but Deep Agents can be run using fully local and private models via Ollama, vLLM, etc.

For open models, we ran seven eval categories: file operations, tool use, retrieval, conversation, memory, summarization, and “unit tests”. These cover tasks that exercise fundamentals: can the model reliably call tools, follow structured instructions, and operate on files? These are the capabilities that gate whether a model is usable in an agentic harness at all.

Each eval case defines success assertions (hard-fail checks that determine correctness) and efficiency assertions (soft checks that measure how the model got there). We report four metrics:

*   Correctness — the fraction of tests the model solved: passed / total. A score of 0.68 means 68% of test cases were solved correctly. This is the primary quality signal.
*   Solve rate — a combined measure of accuracy and speed. For each test, we compute expected_steps / wall_clock_seconds; failed tests contribute zero. The final score is the average across all tests. Higher is better — a model that solves tasks both correctly and quickly scores highest.
*   Step ratio — how many agentic steps the model actually took compared to how many we expected, aggregated across all tests: total_actual_steps / total_expected_steps. A value of 1.0 means the model used exactly the expected number of steps. Above 1.0 means it needed more (less efficient); below 1.0 means it needed fewer steps than initially expected.
*   Tool call ratio — same idea as step ratio, but counting individual tool calls instead of steps. 1.0 is on-budget, above is over-budget, below is under-budget.

Step ratio and tool call ratio are efficiency metrics. They don't affect whether a test passes, but they reveal how economically a model reaches the answer. A model that solves a task in 2 steps instead of the expected 5 is both correct and efficient.

### Findings from our evals

These are early results; we’re actively maintaining and expanding our eval set. You can view recent runs in realtime both [in our GitHub repo](https://www.linkedin.com/redir/redirect?url=https%3A%2F%2Fgithub%2Ecom%2Flangchain-ai%2Fdeepagents%2Factions%2Fworkflows%2Fevals%2Eyml&urlhash=o2hh&trk=article-ssr-frontend-pulse_little-text-block) and at [this shared LangSmith project](https://www.linkedin.com/redir/redirect?url=https%3A%2F%2Fsmith%2Elangchain%2Ecom%2Fpublic%2Fd4245855-4e15-48dc-a39d-8631780a9aeb%2Fd&urlhash=ipBG&trk=article-ssr-frontend-pulse_little-text-block).

### Open models

[View CI run](https://www.linkedin.com/redir/redirect?url=https%3A%2F%2Fgithub%2Ecom%2Flangchain-ai%2Fdeepagents%2Factions%2Fruns%2F23872647281&urlhash=uBC_&trk=article-ssr-frontend-pulse_little-text-block) (includes links to shared LangSmith experiments)

![Image 5: Article content](https://www.linkedin.com/pulse/open-models-have-crossed-threshold-mason-daugherty-jsjme)

![Image 6: Article content](https://www.linkedin.com/pulse/open-models-have-crossed-threshold-mason-daugherty-jsjme)

Per-category correctness:

![Image 7: Article content](https://www.linkedin.com/pulse/open-models-have-crossed-threshold-mason-daugherty-jsjme)

### Frontier models

[View CI run](https://www.linkedin.com/redir/redirect?url=https%3A%2F%2Fgithub%2Ecom%2Flangchain-ai%2Fdeepagents%2Factions%2Fruns%2F23871631742&urlhash=XJVA&trk=article-ssr-frontend-pulse_little-text-block) (includes links to shared LangSmith experiments)

![Image 8: Article content](https://www.linkedin.com/pulse/open-models-have-crossed-threshold-mason-daugherty-jsjme)

![Image 9: Article content](https://www.linkedin.com/pulse/open-models-have-crossed-threshold-mason-daugherty-jsjme)

Per-category correctness:

![Image 10: Article content](https://www.linkedin.com/pulse/open-models-have-crossed-threshold-mason-daugherty-jsjme)

For each model, we opt to use the provider’s default thinking level.

*   For Gemini 3+, this is high
*   For OpenAI, this is medium
*   For Claude, this is without extended thinking

### DIY: Run Deep Agent evals locally

Our CI runs the same eval suite across 52 models organized into groups — including an open group (baseten:zai-org/GLM-5, ollama:minimax-m2.7:cloud, ollama:nemotron-3-super) that runs on every eval workflow. You can target any model group:

# Run evals against all open models pytest tests/evals --model-group open # Run against a specific model pytest tests/evals --model baseten:zai-org/GLM-5 

This makes it straightforward to compare open models against each other and against closed frontier models on the same tasks, using the same grading criteria.

* * *

## Using open models in Deep Agents SDK

Swapping to an open model is a one-line change:

# pip install langchain-baseten from deepagents import create_deep_agent agent = create_deep_agent(model="baseten:zai-org/GLM-5") # pip install langchain-openrouter from deepagents import create_deep_agent agent = create_deep_agent(model="openrouter:minimax/minimax-m2.7") 

That's it. The harness handles the rest — it detects the model's context window size, disables unsupported modalities, and injects the right identity into the system prompt so the agent knows what it's working with.

The same open model is often available through multiple providers. Pick the one that matches your constraints. For example, GLM-5 is available as baseten:zai-org/GLM-5, fireworks:fireworks/glm-5, or ollama:glm-5 for self-hosted. Same model, same harness, different infrastructure.

LangChain provides support for the most popular open model providers. The providers we have tested for this release are: Baseten, Fireworks, Groq, OpenRouter, and Ollama (cloud).

### Harness-level adjustments for your model

Open models have different context windows, different tool-calling formats, and different failure modes than closed frontier models. The Deep Agents harness absorbs these differences so you don't have to:

*   Model identity injection — the system prompt is patched at runtime with the model's name, provider, context limit, and supported modalities. The agent knows what it is and what it can do.
*   Context management — compression, offloading, and summarization thresholds adapt to the model's actual context window, not a hardcoded default. A model with a 4K context gets more aggressive compaction than Opus with 1M.

### Deep Agents CLI

Each model is also available in the Deep Agents CLI. The [Deep Agents CLI](https://www.linkedin.com/redir/redirect?url=https%3A%2F%2Fgithub%2Ecom%2Flangchain-ai%2Fdeepagents%2Ftree%2Fmain%2Flibs%2Fcli&urlhash=wNcA&trk=article-ssr-frontend-pulse_little-text-block) is our open-source coding agent and alternative to Claude Code.

In addition to all the capabilities in Deep Agents SDK, the CLI supports Runtime model swapping. We introduced a new middleware (ConfigurableModelMiddleware ) to enable switching models mid-session without restarting the agent. This enables patterns like using a frontier model for planning and an open model for execution.

You can switch models mid-session with the /model slash command. This enables patterns like starting a task with a frontier model for planning, then switching to a cheaper open model for execution:

Play Video

Video Player is loading.

Loaded: 0%

Play Back to start

Stream Type LIVE

Current Time 0:00

/

Duration-:-

1x

Playback Rate

Show Captions

Mute

Fullscreen

### What’s next

Some things we’re excited to share soon:

*   Documenting harness tuning patterns for specific open model families
*   Testing multi-model subagent configurations (ex: frontier closed model orchestrator + open model subagents)

Open models work for agents today. We want to show the design patterns that help us engineer a good harness and build targeted evals that measure what matters for your task.

[Deep Agents](https://www.linkedin.com/redir/redirect?url=https%3A%2F%2Fgithub%2Ecom%2Flangchain-ai%2Fdeepagents&urlhash=cQRT&trk=article-ssr-frontend-pulse_little-text-block) is open source. Try it with your preferred open model and come build great evals and agents with us.

[Like](https://www.linkedin.com/signup/cold-join?session_redirect=%2Fpulse%2Fopen-models-have-crossed-threshold-mason-daugherty-jsjme&trk=article-ssr-frontend-pulse_x-social-details_like-toggle_like-cta)

![Image 11: Like](https://www.linkedin.com/pulse/open-models-have-crossed-threshold-mason-daugherty-jsjme)Like

![Image 12: Celebrate](https://www.linkedin.com/pulse/open-models-have-crossed-threshold-mason-daugherty-jsjme)Celebrate

![Image 13: Support](https://www.linkedin.com/pulse/open-models-have-crossed-threshold-mason-daugherty-jsjme)Support

![Image 14: Love](https://www.linkedin.com/pulse/open-models-have-crossed-threshold-mason-daugherty-jsjme)Love

![Image 15: Insightful](https://www.linkedin.com/pulse/open-models-have-crossed-threshold-mason-daugherty-jsjme)Insightful

![Image 16: Funny](https://www.linkedin.com/pulse/open-models-have-crossed-threshold-mason-daugherty-jsjme)Funny

[Comment](https://www.linkedin.com/signup/cold-join?session_redirect=%2Fpulse%2Fopen-models-have-crossed-threshold-mason-daugherty-jsjme&trk=article-ssr-frontend-pulse_comment-cta)

*   Copy
*   LinkedIn
*   Facebook
*   X

 Share 

[![Image 17](https://static.licdn.com/aero-v1/sc/h/bn39hirwzjqj18ej1fkz55671)![Image 18](https://static.licdn.com/aero-v1/sc/h/2tzoeodxy0zug4455msr0oq0v)![Image 19](https://static.licdn.com/aero-v1/sc/h/a0e8rff6djeoq8iympcysuqfu) 50](https://www.linkedin.com/signup/cold-join?session_redirect=%2Fpulse%2Fopen-models-have-crossed-threshold-mason-daugherty-jsjme&trk=article-ssr-frontend-pulse_x-social-details_likes-count_social-actions-reactions)[2 Comments](https://www.linkedin.com/signup/cold-join?session_redirect=%2Fpulse%2Fopen-models-have-crossed-threshold-mason-daugherty-jsjme&trk=article-ssr-frontend-pulse_x-social-details_likes-count_social-actions-comments)

[![Image 20: Avais Aziz, graphic](https://www.linkedin.com/pulse/open-models-have-crossed-threshold-mason-daugherty-jsjme)](https://pk.linkedin.com/in/avaisaziz?trk=article-ssr-frontend-pulse_x-social-details_comments-action_comment_actor-image)

[Avais Aziz](https://pk.linkedin.com/in/avaisaziz?trk=article-ssr-frontend-pulse_x-social-details_comments-action_comment_actor-name) 1w 

*   [Report this comment](https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fpulse%2Fopen-models-have-crossed-threshold-mason-daugherty-jsjme&trk=article-ssr-frontend-pulse_x-social-details_comments-action_comment_ellipsis-menu-semaphore-sign-in-redirect&guestReportContentType=COMMENT&_f=guest-reporting)

This M2.7 result from MiniMax hits different. Those independent LangChain evals showing it matching closed frontier models on core agent tasks, all while delivering the 20x cost edge and 2 to 4x speed, make open models feel truly production ready. The blog numbers on the daily token spend really drive it home.

[Like](https://www.linkedin.com/signup/cold-join?session_redirect=%2Fpulse%2Fopen-models-have-crossed-threshold-mason-daugherty-jsjme&trk=article-ssr-frontend-pulse_x-social-details_comments-action_comment_like)[Reply](https://www.linkedin.com/signup/cold-join?session_redirect=%2Fpulse%2Fopen-models-have-crossed-threshold-mason-daugherty-jsjme&trk=article-ssr-frontend-pulse_x-social-details_comments-action_comment_reply) 1 Reaction 

[![Image 21: Mateusz Mirkowski, graphic](https://www.linkedin.com/pulse/open-models-have-crossed-threshold-mason-daugherty-jsjme)](https://pl.linkedin.com/in/mateusz-mirkowski-18755134?trk=article-ssr-frontend-pulse_x-social-details_comments-action_comment_actor-image)

[Mateusz Mirkowski](https://pl.linkedin.com/in/mateusz-mirkowski-18755134?trk=article-ssr-frontend-pulse_x-social-details_comments-action_comment_actor-name) 1w 

*   [Report this comment](https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fpulse%2Fopen-models-have-crossed-threshold-mason-daugherty-jsjme&trk=article-ssr-frontend-pulse_x-social-details_comments-action_comment_ellipsis-menu-semaphore-sign-in-redirect&guestReportContentType=COMMENT&_f=guest-reporting)

100% agree. Gap is way smaller than people think.

[Like](https://www.linkedin.com/signup/cold-join?session_redirect=%2Fpulse%2Fopen-models-have-crossed-threshold-mason-daugherty-jsjme&trk=article-ssr-frontend-pulse_x-social-details_comments-action_comment_like)[Reply](https://www.linkedin.com/signup/cold-join?session_redirect=%2Fpulse%2Fopen-models-have-crossed-threshold-mason-daugherty-jsjme&trk=article-ssr-frontend-pulse_x-social-details_comments-action_comment_reply) 1 Reaction 

[See more comments](https://www.linkedin.com/signup/cold-join?session_redirect=%2Fpulse%2Fopen-models-have-crossed-threshold-mason-daugherty-jsjme&trk=article-ssr-frontend-pulse_x-social-details_comments_comment-see-more)

To view or add a comment, [sign in](https://www.linkedin.com/signup/cold-join?session_redirect=%2Fpulse%2Fopen-models-have-crossed-threshold-mason-daugherty-jsjme&trk=article-ssr-frontend-pulse_x-social-details_feed-cta-banner-cta)

## More articles by Mason D.

*   [Autonomous context compression](https://www.linkedin.com/pulse/autonomous-context-compression-mason-daugherty-rawve)![Image 22](https://www.linkedin.com/pulse/open-models-have-crossed-threshold-mason-daugherty-jsjme) Mar 11, 2026 
### Autonomous context compression

TL;DR: We’ve added a tool to the Deep Agents SDK (Python) and CLI that allows models to compress their own context…

![Image 23](https://www.linkedin.com/pulse/open-models-have-crossed-threshold-mason-daugherty-jsjme)![Image 24](https://www.linkedin.com/pulse/open-models-have-crossed-threshold-mason-daugherty-jsjme)![Image 25](https://www.linkedin.com/pulse/open-models-have-crossed-threshold-mason-daugherty-jsjme) 58   10 Comments     
*   [Informatics Best-Practices for Gallery, Library, Archive, and Museum Institutions](https://www.linkedin.com/pulse/informatics-best-practices-gallery-library-archive-museum-daugherty)![Image 26](https://www.linkedin.com/pulse/open-models-have-crossed-threshold-mason-daugherty-jsjme) Sep 1, 2022 
### Informatics Best-Practices for Gallery, Library, Archive, and Museum Institutions

As early as the 1960s, Galleries, Libraries, Archives, and Museum (GLAM) institutions began taking steps to realize a…

![Image 27](https://www.linkedin.com/pulse/open-models-have-crossed-threshold-mason-daugherty-jsjme)![Image 28](https://www.linkedin.com/pulse/open-models-have-crossed-threshold-mason-daugherty-jsjme)![Image 29](https://www.linkedin.com/pulse/open-models-have-crossed-threshold-mason-daugherty-jsjme) 30   2 Comments     
*   [Cyborgs Walk Among Us](https://www.linkedin.com/pulse/cyborgs-walk-among-us-mason-daugherty)![Image 30](https://www.linkedin.com/pulse/open-models-have-crossed-threshold-mason-daugherty-jsjme) Jul 12, 2022 
### Cyborgs Walk Among Us

The lines separating humans and technology are blurring. Should we embrace it? Since 2017, I have been a walking cyborg.

![Image 31](https://www.linkedin.com/pulse/open-models-have-crossed-threshold-mason-daugherty-jsjme) 5     
*   [Radio’s Dead, But We’re Still Dancing](https://www.linkedin.com/pulse/radios-dead-were-still-dancing-mason-daugherty)![Image 32](https://www.linkedin.com/pulse/open-models-have-crossed-threshold-mason-daugherty-jsjme) Jul 12, 2022 
### Radio’s Dead, But We’re Still Dancing

Radio hasn’t died--it's just evolved. The Weeknd’s latest album, Dawn FM, has brought listeners an auditory experience…

![Image 33](https://www.linkedin.com/pulse/open-models-have-crossed-threshold-mason-daugherty-jsjme) 27   2 Comments     

## Explore content categories

*   [Career](https://www.linkedin.com/top-content/career/)
*   [Productivity](https://www.linkedin.com/top-content/productivity/)
*   [Finance](https://www.linkedin.com/top-content/finance/)
*   [Soft Skills & Emotional Intelligence](https://www.linkedin.com/top-content/soft-skills-emotional-intelligence/)
*   [Project Management](https://www.linkedin.com/top-content/project-management/)
*   [Education](https://www.linkedin.com/top-content/education/)
*   [Technology](https://www.linkedin.com/top-content/technology/)
*   [Leadership](https://www.linkedin.com/top-content/leadership/)
*   [Ecommerce](https://www.linkedin.com/top-content/ecommerce/)
*   [User Experience](https://www.linkedin.com/top-content/user-experience/)
*   [Recruitment & HR](https://www.linkedin.com/top-content/recruitment-hr/)
*   [Customer Experience](https://www.linkedin.com/top-content/customer-experience/)
*   [Real Estate](https://www.linkedin.com/top-content/real-estate/)
*   [Marketing](https://www.linkedin.com/top-content/marketing/)
*   [Sales](https://www.linkedin.com/top-content/sales/)
*   [Retail & Merchandising](https://www.linkedin.com/top-content/retail-merchandising/)
*   [Science](https://www.linkedin.com/top-content/science/)
*   [Supply Chain Management](https://www.linkedin.com/top-content/supply-chain-management/)
*   [Future Of Work](https://www.linkedin.com/top-content/future-of-work/)
*   [Consulting](https://www.linkedin.com/top-content/consulting/)
*   [Writing](https://www.linkedin.com/top-content/writing/)
*   [Economics](https://www.linkedin.com/top-content/economics/)
*   [Artificial Intelligence](https://www.linkedin.com/top-content/artificial-intelligence/)
*   [Employee Experience](https://www.linkedin.com/top-content/employee-experience/)
*   [Workplace Trends](https://www.linkedin.com/top-content/workplace-trends/)
*   [Fundraising](https://www.linkedin.com/top-content/fundraising/)
*   [Networking](https://www.linkedin.com/top-content/networking/)
*   [Corporate Social Responsibility](https://www.linkedin.com/top-content/corporate-social-responsibility/)
*   [Negotiation](https://www.linkedin.com/top-content/negotiation/)
*   [Communication](https://www.linkedin.com/top-content/communication/)
*   [Engineering](https://www.linkedin.com/top-content/engineering/)
*   [Hospitality & Tourism](https://www.linkedin.com/top-content/hospitality-tourism/)
*   [Business Strategy](https://www.linkedin.com/top-content/business-strategy/)
*   [Change Management](https://www.linkedin.com/top-content/change-management/)
*   [Organizational Culture](https://www.linkedin.com/top-content/organizational-culture/)
*   [Design](https://www.linkedin.com/top-content/design/)
*   [Innovation](https://www.linkedin.com/top-content/innovation/)
*   [Event Planning](https://www.linkedin.com/top-content/event-planning/)
*   [Training & Development](https://www.linkedin.com/top-content/training-development/)

 Show more  Show less 

*   LinkedIn© 2026
*   [About](https://about.linkedin.com/?trk=d_flagship2_pulse_read_footer-about)
*   [Accessibility](https://www.linkedin.com/accessibility?trk=d_flagship2_pulse_read_footer-accessibility)
*   [User Agreement](https://www.linkedin.com/legal/user-agreement?trk=d_flagship2_pulse_read_footer-user-agreement)
*   [Privacy Policy](https://www.linkedin.com/legal/privacy-policy?trk=d_flagship2_pulse_read_footer-privacy-policy)
*   [Your California Privacy Choices](https://www.linkedin.com/legal/california-privacy-disclosure?trk=d_flagship2_pulse_read_footer-california-privacy-rights-act)
*   [Cookie Policy](https://www.linkedin.com/legal/cookie-policy?trk=d_flagship2_pulse_read_footer-cookie-policy)
*   [Copyright Policy](https://www.linkedin.com/legal/copyright-policy?trk=d_flagship2_pulse_read_footer-copyright-policy)
*   [Brand Policy](https://brand.linkedin.com/policies?trk=d_flagship2_pulse_read_footer-brand-policy)
*   [Guest Controls](https://www.linkedin.com/psettings/guest-controls?trk=d_flagship2_pulse_read_footer-guest-controls)
*   [Community Guidelines](https://www.linkedin.com/legal/professional-community-policies?trk=d_flagship2_pulse_read_footer-community-guide)
*   
    *    العربية (Arabic) 
    *    বাংলা (Bangla) 
    *    Čeština (Czech) 
    *    Dansk (Danish) 
    *    Deutsch (German) 
    *    Ελληνικά (Greek) 
    *   **English (English)**
    *    Español (Spanish) 
    *    فارسی (Persian) 
    *    Suomi (Finnish) 
    *    Français (French) 
    *    हिंदी (Hindi) 
    *    Magyar (Hungarian) 
    *    Bahasa Indonesia (Indonesian) 
    *    Italiano (Italian) 
    *    עברית (Hebrew) 
    *    日本語 (Japanese) 
    *    한국어 (Korean) 
    *    मराठी (Marathi) 
    *    Bahasa Malaysia (Malay) 
    *    Nederlands (Dutch) 
    *    Norsk (Norwegian) 
    *    ਪੰਜਾਬੀ (Punjabi) 
    *    Polski (Polish) 
    *    Português (Portuguese) 
    *    Română (Romanian) 
    *    Русский (Russian) 
    *    Svenska (Swedish) 
    *    తెలుగు (Telugu) 
    *    ภาษาไทย (Thai) 
    *    Tagalog (Tagalog) 
    *    Türkçe (Turkish) 
    *    Українська (Ukrainian) 
    *    Tiếng Việt (Vietnamese) 
    *    简体中文 (Chinese (Simplified)) 
    *    正體中文 (Chinese (Traditional)) 

 Language 

[](https://www.linkedin.com/pulse/open-models-have-crossed-threshold-mason-daugherty-jsjme)

![Image 34](https://static.licdn.com/aero-v1/sc/h/5k9cgtx8rhoyqkcxfoncu1svl)
## Sign in to view more content

Create your free account or sign in to continue your search

 Email or phone  

 Password  

Show

[Forgot password?](https://www.linkedin.com/uas/request-password-reset?trk=csm-v2_forgot_password) Sign in 

Sign in with Email

or

New to LinkedIn? [Join now](https://www.linkedin.com/signup/cold-join?session_redirect=%2Fpulse%2Fopen-models-have-crossed-threshold-mason-daugherty-jsjme&trk=pulse-article_contextual-sign-in-modal_join-link)

By clicking Continue to join or sign in, you agree to LinkedIn’s [User Agreement](https://www.linkedin.com/legal/user-agreement?trk=linkedin-tc_auth-button_user-agreement), [Privacy Policy](https://www.linkedin.com/legal/privacy-policy?trk=linkedin-tc_auth-button_privacy-policy), and [Cookie Policy](https://www.linkedin.com/legal/cookie-policy?trk=linkedin-tc_auth-button_cookie-policy).
