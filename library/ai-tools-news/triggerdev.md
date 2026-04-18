---
tags:
  - library
title: "Trigger.dev"
url: "https://trigger.dev/"
company: [personal]
topics: []
created: 2026-02-24
source_type: raindrop
raindrop_id: 1616385835
source_domain: "trigger.dev"
source_type_raindrop: link
collection: "AI Tools & News"
collection_id: 69284314
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

Build and deploy fully-managed AI agents and workflows in TypeScript. Long-running tasks with retries, queues, observability, and elastic scaling. No timeouts. No servers to manage.

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: Trigger.dev | Build and deploy fully-managed AI agents and workflows.

URL Source: https://trigger.dev/

Markdown Content:
# Trigger.dev | Build and deploy fully-managed AI agents and workflows.

[](https://trigger.dev/)

*   [How it works](https://trigger.dev/#how-it-works)
*   [Product](https://trigger.dev/product)### Product

[All features](https://trigger.dev/product) #### [AI Agents Build and deploy invincible AI agents.](https://trigger.dev/product/ai-agents)#### [Trigger.dev Realtime Connect your frontend app to your tasks.](https://trigger.dev/product/realtime)#### [Concurrency & queues Control how many tasks run at once.](https://trigger.dev/product/concurrency-and-queues)#### [Scheduled tasks Durable cron schedules without timeouts.](https://trigger.dev/product/scheduled-tasks)#### [Observability & monitoring Real-time monitoring and tracing of tasks.](https://trigger.dev/product/observability-and-monitoring)#### [Roadmap See what we're building next.](https://feedback.trigger.dev/roadmap)    
*   [Changelog](https://trigger.dev/changelog)### Latest changelogs

[All changelog entries](https://trigger.dev/changelog) [v 4.4.4 #### Trigger.dev v4.4.4 April 13](https://trigger.dev/changelog/v4-4-4)[![Image 1: Vercel integration](https://trigger.dev/changelog/vercel-integration/vercel-integration.png) #### Vercel integration March 10](https://trigger.dev/changelog/vercel-integration)[v 4.4.3 #### Trigger.dev v4.4.3 March 10](https://trigger.dev/changelog/v4-4-3)   
*   [Blog](https://trigger.dev/blog)### Latest blog posts

[All blog posts](https://trigger.dev/blog) [![Image 2: We ditched worktrees for Claude Code. Here's what we use instead](https://trigger.dev/blog/parallel-agents-gitbutler/parallel-agents-gitbutler-thumbnail.jpg?1) #### We ditched worktrees for Claude Code. Here's what we use instead April 16](https://trigger.dev/blog/parallel-agents-gitbutler)[![Image 3: Why we replaced Node.js with Bun for 5x throughput](https://trigger.dev/blog/firebun/firebun-thumbnail.jpg) #### Why we replaced Node.js with Bun for 5x throughput March 27](https://trigger.dev/blog/firebun)[![Image 4: 10 Claude Code Tips You Didn't Know](https://trigger.dev/blog/10-claude-code-tips-you-did-not-know/claude-code-10-thumbnail.jpg) #### 10 Claude Code Tips You Didn't Know March 12](https://trigger.dev/blog/10-claude-code-tips-you-did-not-know)   
*   [Docs](https://trigger.dev/docs)### Documentation [Quick start](https://trigger.dev/docs/quick-start)[Writing tasks](https://trigger.dev/docs/tasks/overview)[Official MCP server](https://trigger.dev/docs/mcp-introduction)[Guides & examples](https://trigger.dev/docs/guides/introduction)[Trigger.dev Realtime](https://trigger.dev/docs/realtime)[React Hooks](https://trigger.dev/docs/frontend/react-hooks/overview)[Scheduled tasks (cron)](https://trigger.dev/docs/tasks-scheduled)[Self-hosting](https://trigger.dev/docs/self-hosting/overview)  ### Guides

[View docs](https://trigger.dev/docs/introduction) [How to build AI agents](https://trigger.dev/docs/guides/ai-agents/overview)[Triggering Python scripts](https://trigger.dev/docs/config/extensions/pythonExtension)[Get started with Node.js](https://trigger.dev/docs/guides/frameworks/nodejs)[Get started with Next.js](https://trigger.dev/docs/guides/frameworks/nextjs)[Get started with Bun](https://trigger.dev/docs/guides/frameworks/bun)[Get started with Remix](https://trigger.dev/docs/guides/frameworks/remix)[Using Supabase & Trigger.dev](https://trigger.dev/docs/guides/frameworks/supabase-guides-overview)[Trigger tasks from webhooks](https://trigger.dev/docs/guides/frameworks/webhooks-guides-overview)     
*   [Pricing](https://trigger.dev/pricing)

*   [](https://trigger.dev/discord)
*   [Star 14.6k](https://github.com/triggerdotdev/trigger.dev)
*   [Login](https://cloud.trigger.dev/)
*   [Get started](https://cloud.trigger.dev/)

# Build and deploy fully‑managed AI agents and workflows

Trigger.dev is the platform for building AI workflows in TypeScript. Long-running tasks with retries, queues, observability, and elastic scaling.

[Start building now](https://cloud.trigger.dev/)[14.6k| Open source](https://github.com/triggerdotdev/trigger.dev)

AI agents

Media processing

Media generation

Human in the loop

Streaming

Run Python

Marketing

Browser automation

Scheduled tasks

Concurrency

Retries

Semantic search

Email sequences

```typescript
// AI agent with tool calling - works with any modelexport const researchAgent = task({  id: "research-agent",  run: async ({ topic }: { topic: string }) => {    const messages: CoreMessage[] = [      { role: "user", content: `Research: ${topic}` },    ];
    for (let i = 0; i < 10; i++) {      const { text, toolCalls, steps } = await generateText({        model: anthropic("claude-opus-4-20250514"),        system: "You are a research assistant with web access.",        messages,        tools: { search, browse, analyze },        maxSteps: 5,      });
      if (!toolCalls.length) {        return { summary: text, stepsUsed: steps.length };      }
      for (const call of toolCalls) {        const result = await executeTool(call);        messages.push({ role: "tool", content: result });      }    }  },});
```

Build production-ready AI agents with tool calling, automatic retries, and full observability. Use existing Node.js SDKs and code from your repo.

[Learn about AI agents](https://trigger.dev/docs/guides/ai-agents/overview)

## Trusted by developers at companies all over the world

## How it works

Play

Replay

Full screen

Write tasks in your Trigger folder

## Build invincible AI apps

Offload any long-running async AI tasks to our infrastructure. Create AI agents with human-in-the-loop functionality and stream responses directly to your frontend.

[AI agents overview](https://trigger.dev/product/ai-agents)

[![Image 5: Autonomous agent](https://trigger.dev/images/product/ai-agents/diagrams/auto-agent.png) ### Autonomous agent AI agents that can use judgement to perform complex open-ended tasks. View example](https://trigger.dev/docs/guides/example-projects/vercel-ai-sdk-deep-research)

[![Image 6: Prompt chaining](https://trigger.dev/images/product/ai-agents/diagrams/prompt-chaining.png) ### Prompt chaining Chain AI prompts together to create multi-stage processing flows. View example](https://trigger.dev/docs/guides/ai-agents/generate-translate-copy)

[![Image 7: Routing](https://trigger.dev/images/product/ai-agents/diagrams/routing.png) ### Routing Smart distribution of tasks to specialized AI models based on content analysis. View example](https://trigger.dev/docs/guides/ai-agents/route-question)

[![Image 8: Parallelization](https://trigger.dev/images/product/ai-agents/diagrams/parallelization.png) ### Parallelization Concurrent execution of multiple AI tasks for simultaneous processing and analysis. View example](https://trigger.dev/docs/guides/ai-agents/respond-and-check-content)

[![Image 9: Orchestrator](https://trigger.dev/images/product/ai-agents/diagrams/orchestrator.png) ### Orchestrator Coordinate multiple AI agents to achieve complex objectives. View example](https://trigger.dev/docs/guides/ai-agents/verify-news-article)

[![Image 10: Evaluator-optimizer](https://trigger.dev/images/product/ai-agents/diagrams/evaluator-optimizer.png) ### Evaluator-optimizer Iterative feedback system that continuously evaluates and refines AI outputs. View example](https://trigger.dev/docs/guides/ai-agents/translate-and-refine)

## Deploy and scale to any size

### No timeouts

Write simple, reliable code and never hit a timeout.

### Pay for what you use

Only pay when your code is actually executing.

### No servers to manage

We deploy your tasks and handle scaling for you.

## Find and fix bugs fast

### Alerts for errors

Get notified via email, Slack or webhooks when your tasks or deployments fail.

![Image 11: hero](https://trigger.dev/patterns/alerts-bg.png)

### Advanced filtering

Find runs fast using advanced filtering options, then apply bulk actions to multiple tasks at once.

![Image 12: hero](https://trigger.dev/patterns/alerts-bg.png)

### Versioning

Each deploy is an atomic version ensuring started tasks are not affected by code changes.

![Image 13: hero](https://trigger.dev/patterns/alerts-bg.png)

## Bring your tasks to the foreground

#### Trigger.dev Realtime

### Display the status of your tasks anywhere in your app

Show the run status (in progress, completed, failed) and metadata to provide real-time, contextual information for your users as your tasks progress.

[Realtime docs](https://trigger.dev/docs/realtime/overview)

Update your UI in real-time with the run status

#### Realtime streams

### Stream LLM responses from your runs to your users

Forward streams from any provider through our Realtime API. Build AI agents with tools and context from your runs.

[Realtime streams docs](https://trigger.dev/docs/realtime/streams)

Pipe streams to your frontend from your runs

## True runtime freedom for developers

Unlike restricted runtimes, Trigger.dev lets you freely customize every aspect of your build process, resulting bundle, and final container image.

### Python

Execute Python scripts with automatic package installation through requirements.txt

[Learn more](https://trigger.dev/docs/config/extensions/pythonExtension)

### Prisma

Copy files to the build directory, generate the Prisma client, migrate databases, and more.

[Learn more](https://trigger.dev/docs/config/extensions/prismaExtension)

### Puppeteer

Automate browser capabilities and control web pages.

[Learn more](https://trigger.dev/docs/config/extensions/puppeteer)

### esbuild

Add custom esbuild plugins to your build process.

[Learn more](https://trigger.dev/docs/config/extensions/esbuildPlugin)

### FFmpeg

Add FFmpeg binaries to your project during build time, enabling video manipulation tasks.

[Learn more](https://trigger.dev/docs/config/extensions/ffmpeg)

### apt-get

Easily install any system packages you need, from libreoffice to git

[Learn more](https://trigger.dev/docs/config/extensions/aptGet)

### additionalPackages

Add additional packages which aren't automatically included via imports.

[Learn more](https://trigger.dev/docs/config/extensions/additionalPackages)

### audioWaveform

Produce visual renderings of audio using waveform data.

[Learn more](https://trigger.dev/docs/config/extensions/audioWaveform)

### Custom build extensions

Integrate custom tooling and project-specific requirements directly into your build pipeline.

[Get started](https://trigger.dev/docs/config/extensions/custom)

## All the tools you need to ship

[View all features](https://trigger.dev/product)

### Development

[Write tasks in regular code](https://trigger.dev/docs/guides/introduction)

[Durable cron schedules](https://trigger.dev/product/scheduled-tasks)

[Realtime updates & streaming](https://trigger.dev/product/realtime)

[React hooks](https://trigger.dev/docs/frontend/react-hooks#react-hooks)[MCP Server](https://trigger.dev/docs/mcp-introduction)[Python support](https://trigger.dev/docs/config/extensions/pythonExtension)[Max duration](https://trigger.dev/docs/runs/max-duration#max-duration)[Batch triggering](https://trigger.dev/docs/triggering#tasks-batchtrigger)[Structured inputs / outputs](https://trigger.dev/docs/tasks/schemaTask#schematask)[Waits](https://trigger.dev/docs/wait)[Wait for HTTP callback](https://trigger.dev/docs/wait-for-token)[Preview branches](https://trigger.dev/docs/deployment/preview-branches)[Input Streams](https://trigger.dev/docs/tasks/streams)

### Production

[Multi-region workers](https://trigger.dev/changelog/multi-region-workers)[Static IPs](https://trigger.dev/changelog/static-ips)

[Concurrency & queues](https://trigger.dev/product/concurrency-and-queues)

[Human-in-the-loop](https://trigger.dev/docs/wait-for-token)

[Multiple environments](https://trigger.dev/docs/how-it-works#dev-mode)[Elastic infrastructure](https://trigger.dev/docs/how-it-works#trigger-dev-architecture)[Automatic retries](https://trigger.dev/docs/errors-retrying)[Build extensions](https://trigger.dev/docs/config/extensions/overview)[Checkpointing](https://trigger.dev/docs/how-it-works#the-checkpoint-resume-system)[Machines](https://trigger.dev/docs/machines)[Vercel integration](https://trigger.dev/docs/vercel-integration)[GitHub integration](https://trigger.dev/docs/github-integration)

### Observability

[Observability & monitoring](https://trigger.dev/product/observability-and-monitoring)

[Logging & tracing](https://trigger.dev/docs/logging)[Tags](https://trigger.dev/docs/tags#tags)

[Advanced run filters](https://trigger.dev/product/observability-and-monitoring#advanced-filters)

[Run metadata](https://trigger.dev/docs/runs/metadata#run-metadata)[Bulk actions](https://trigger.dev/docs/bulk-actions)

[Real-time alerts](https://trigger.dev/product/observability-and-monitoring#alerts)

[Query](https://trigger.dev/docs/observability/query)[Dashboards](https://trigger.dev/docs/observability/dashboards)

## Reliable by default

[Docs](https://trigger.dev/docs/errors-retrying)

#### Task retrying

Configure automatic retrying for tasks.

#### handleError()

Conditional retrying based on the error and run.

#### retry.onThrow()

Fine-grained retrying inside tasks.

#### retry.fetch()

Automatically retry requests based on the response.

#### trigger.config

Configure default retrying in your config file.

```typescript
import { task } from "@trigger.dev/sdk";
export const simpleTask = task({  id: "simple-task",  retry: {    maxAttempts: 3,    minTimeoutInMs: 1000,    maxTimeoutInMs: 5000,    factor: 2,    randomize: true,  },  run: async (payload, { ctx }) => {    logger.log(`Attempt ${ctx.attempt.number}`);
    try {      throw new Error("This is an error.");    } catch (error) {      // The error was caught, so no retry    }
    throw new Error("This will cause a retry.");  },});
```

### Works with your existing tech stack…

![Image 14: Vercel logo](https://trigger.dev/tech-stack/vercel.png)

![Image 15: AWS logo](https://trigger.dev/tech-stack/aws.png)

![Image 16: Remix logo](https://trigger.dev/tech-stack/remix.png)

![Image 17: Nuxt logo](https://trigger.dev/tech-stack/nuxt.png)

![Image 18: SvelteKit logo](https://trigger.dev/tech-stack/sveltekit.png)

![Image 19: Fastify logo](https://trigger.dev/tech-stack/fastify.png)

![Image 20: RedwoodJS logo](https://trigger.dev/tech-stack/redwoodjs.png)

![Image 21: Cloudflare logo](https://trigger.dev/tech-stack/cloudflare.png)

![Image 22: ExpressJS logo](https://trigger.dev/tech-stack/expressjs.png)

![Image 23: Astro logo](https://trigger.dev/tech-stack/astro.png)

![Image 24: Google Cloud logo](https://trigger.dev/tech-stack/google-cloud.png)

![Image 25: Azure logo](https://trigger.dev/tech-stack/azure.png)

![Image 26: Netlify logo](https://trigger.dev/tech-stack/netlify.png)

![Image 27: NextJS logo](https://trigger.dev/tech-stack/nextjs.png)

![Image 28: Heart 1](https://trigger.dev/build/_assets/1-OXKMZAUJ.png)![Image 29: Heart 2](https://trigger.dev/build/_assets/2-JH3Y3YJF.png)![Image 30: Heart 3](https://trigger.dev/build/_assets/3-Y24XLZQ2.png)![Image 31: Heart 4](https://trigger.dev/build/_assets/4-I5XLMUM3.png)![Image 32: Heart 5](https://trigger.dev/build/_assets/5-H2LZLREV.png)

### We love open source. Trigger.dev is Apache 2.0 licensed so you can view the source code, contribute and self-host.

#### [14.6k+ stars on GitHub](https://github.com/triggerdotdev/trigger.dev)

#### [Apache 2.0 open source license](https://github.com/triggerdotdev/trigger.dev?tab=Apache-2.0-1-ov-file#readme)

#### [4.8k+ Discord members](https://discord.gg/nkqV9xBYWy)

## Loved by developers

[Join our community](https://discord.gg/nkqV9xBYWy)

> Trigger.dev is redefining background jobs for modern developers.

![Image 33: Paul Copplestone](https://imagedelivery.net/3TbraffuDZ4aEf8KWOmI_w/e82deee8-b8ec-4092-3980-b268688d1900/public)

Paul Copplestone

Supabase

[![Image 34: Supabase logo](https://imagedelivery.net/3TbraffuDZ4aEf8KWOmI_w/bfd6d823-7027-4c8b-0117-ef4085b76200/public)](https://supabase.com/)

> Trigger.dev is one of those tools that you set up once (takes like 30 minutes) and then never have to worry about again. We use it heavily at Magic Patterns and wish we used it earlier. Previously, we had a homegrown cron job solution.. not good.
> 
> 
> 
> [Read Magic Patterns'customer story](https://trigger.dev/customers/magic-patterns-customer-story)

![Image 35: Alex Danilowicz](https://trigger.dev/customers/magic-patterns/alex-danilowicz.png)

Alex Danilowicz

Magic Patterns

[![Image 36: Magic Patterns logo](https://trigger.dev/customers/magic-patterns/magic-patterns-icon.svg)](https://magicpatterns.io/)

> With Trigger.dev, we’ve summarized over a million student interactions in just a couple of weeks. We’re incredibly thankful for tools like Trigger.dev that are empowering us to bring AI-driven solutions to educators and students at scale.
> 
> 
> 
> [Read MagicSchool AI's customer story](https://trigger.dev/customers/magicschool-ai-customer-story)

![Image 37: Ben Duggan](https://trigger.dev/customers/magicschool/ben-duggan.png)

Ben Duggan

MagicSchool AI

[![Image 38: MagicSchool AI logo](https://trigger.dev/customers/magicschool/magicschool-logo.png)](https://magicschool.ai/)

> Trigger.dev lets us focus on AI logic, not infrastructure. We can now ship workflow orchestration the same way we ship backend features.
> 
> 
> 
> [Read Pallet's customer story](https://trigger.dev/customers/pallet-customer-story)

![Image 39: Karl Kaiser](https://trigger.dev/customers/pallet/karl-kaiser.png)

Karl Kaiser

Pallet

[![Image 40: Pallet logo](https://trigger.dev/customers/pallet/pallet-logo.svg)](https://pallet.com/)

> We moved our flick.social workflows from Temporal to Trigger.dev and went from 87% to 100% success. Temporal workers couldn’t stay stable with bursty loads and FFmpeg CPU spikes, which caused queue-depth throttling and missed activities. Trigger.dev handles the load without degrading, and the local testing + observability make diagnosing issues trivial.

![Image 41: Andreas Asprou](https://trigger.dev/testimonials/flick-social/andreas-asprou.png)

Andreas Asprou

Flick.social

[![Image 42: Flick.social logo](https://trigger.dev/testimonials/flick-social/flick-social-logo.svg)](https://www.flick.social/)

> We're using Trigger for our billing, background jobs and deployment pipeline without worrying about operations or infrastructure. It just works.

![Image 43: Andreas Thomas](https://trigger.dev/testimonials/unkey/andreas-thomas-chronark.png)

Andreas Thomas

Unkey

[![Image 44: Unkey logo](https://trigger.dev/testimonials/unkey/unkey.png)](https://www.unkey.com/)

> Trigger.dev is a great way to automate email campaigns with Resend.

![Image 45: Zeno Rocha](https://imagedelivery.net/3TbraffuDZ4aEf8KWOmI_w/3aca9c05-4563-4924-61df-867ec8434200/public)

Zeno Rocha

Resend

[![Image 46: Resend logo](https://imagedelivery.net/3TbraffuDZ4aEf8KWOmI_w/a7941fc0-bfe2-4067-9449-9c593cf54c00/public)](https://resend.com/)

> We have critical business functionalities that need to be reliable and replayable in the event of a failure. Trigger.dev helps us deliver messages over WhatsApp, run thousands of jobs with custom LLM workflows, and execute ETL processes to sync our data across multiple databases without breaking a sweat!

![Image 47: Patryk Maron](https://trigger.dev/testimonials/drpcrd/patryk-maron.png)

Patryk Maron

DRPCRD

[![Image 48: DRPCRD logo](https://trigger.dev/testimonials/drpcrd/drpcrd.png)](https://drpcrd.com/)

> We love Trigger.dev and it’s had a big impact in dev iteration velocity already.

![Image 49: André Neves](https://imagedelivery.net/3TbraffuDZ4aEf8KWOmI_w/3e6a3e0f-e4c9-41e9-3881-ffe4cfc50400/public)

André Neves

ZBD

[![Image 50: ZBD logo](https://imagedelivery.net/3TbraffuDZ4aEf8KWOmI_w/9bfbbd56-ec03-43ef-663a-15595ae7ab00/public)](https://zbd.gg/)

> The first time I used Trigger.dev, I had an a-ha moment, I no longer needed to set up everything with ECS or Lambda. What also stands out is the exceptional support, unlike any I've seen in the web community.

![Image 51: Martin Ruzicka](https://trigger.dev/testimonials/ps-bridal/martin-ruzicka.png)

Martin Ruzicka

P.S. Bridal

[![Image 52: P.S. Bridal logo](https://trigger.dev/testimonials/ps-bridal/ps-bridal.png)](https://psbridal.co.uk/)

> The reliability of Trigger.dev's job scheduling has been essential as we've scaled our evidence collection automation and built our open source community of 600+ compliance professionals.
> 
> 
> 
> [Read Comp AI's customer story](https://trigger.dev/customers/comp-ai-customer-story)

![Image 53: Lewis Carhart](https://trigger.dev/customers/comp-ai/lewis-carhart.png)

Lewis Carhart

Comp AI

[![Image 54: Comp AI logo](https://trigger.dev/customers/comp-ai/comp-ai-logo.svg)](https://trycomp.ai/)

> We migrated from an AWS background job service that required a dedicated expert for maintenance. Trigger.dev's TypeScript support, simplicity and visual feedback let us focus on making AI excellent at UI creation instead of managing infrastructure.
> 
> 
> 
> [Read HeroUI's customer story](https://trigger.dev/customers/hero-ui-customer-story)

![Image 55: Junior Garcia](https://trigger.dev/customers/hero-ui/junior-garcia.png)

Junior Garcia

HeroUI

[![Image 56: HeroUI logo](https://trigger.dev/customers/hero-ui/hero-ui-logo.svg)](https://heroui.com/)

> We needed a sophisticated event engine: chaining LLM queries, orchestrating responses, async tasks, persistent state (without long lived servers), complex concurrency, and variable compute power. Trigger’s managed infra and intuitive SDK allowed us to migrate our entire events engine in a day (with incredible support from the team).

![Image 57: Michael Parker](https://trigger.dev/testimonials/stunt-double/michael-parker.png)

Michael Parker

Stunt Double

[![Image 58: Stunt Double logo](https://trigger.dev/testimonials/stunt-double/stunt-double.png)](https://stuntdouble.io/)

> Trigger is a central part of our architecture. It’s allowed us to build a resilient system to orchestrates data across multiple systems. We love its observability, replayability, and how easily it slots into our existing codebase. It allows us to refine over time how to set the boundaries between async tasks and synchronous business logic.
> 
> 
> 
> [Read NUMI's customer story](https://trigger.dev/customers/numi-customer-story)

![Image 59: Agree Ahmed](https://trigger.dev/testimonials/numi/agree-ahmed.png)

Agree Ahmed

NUMI

[![Image 60: NUMI logo](https://trigger.dev/testimonials/numi/numi.png)](https://numi.tech/)

> Trigger.dev is undoubtedly one of my most cherished services. Throughout my two-decade career, it’s rare to encounter a product or service that truly resonates and makes a significant impact. It just clicks - an absolute game-changer for us. The support is beyond exceptional, and they genuinely care about the product and their users. I wholeheartedly recommend Trigger!

![Image 61: Aaron J. Spurlock](https://trigger.dev/testimonials/midtown/aaron-spurlock.png)

Aaron J. Spurlock

Midtown HI

[![Image 62: Midtown HI logo](https://trigger.dev/testimonials/midtown/midtown-logo.png)](https://midtownhomeimprovements.com/)

> Trigger.dev has become my go-to tool for new projects. I no longer need an additional server and can forget about horizontal scaling!

![Image 63: Nevo David](https://imagedelivery.net/3TbraffuDZ4aEf8KWOmI_w/f577a1b5-e9bc-46ae-af2e-517c8ebef700/public)

Nevo David

Novu

[![Image 64: Novu logo](https://imagedelivery.net/3TbraffuDZ4aEf8KWOmI_w/c89f7bbe-5b66-4b3d-be59-02bcc3a4e800/public)](https://novu.co/)

> For AI powered products, Trigger.dev is my clear go-to tool for building robust serverless pipelines stitching together various LLM calls.

![Image 65: Evan Sandler](https://trigger.dev/testimonials/blee/evan-sandler.png)

Evan Sandler

Blee

[![Image 66: Blee logo](https://trigger.dev/testimonials/blee/blee-icon.png)](https://www.blee.com/)

> Trigger is packaging end-to-end cron, queues and webhooks platform in a slick interface. Integration was quick and we love the support ❤️

![Image 67: Aseem Gupta](https://imagedelivery.net/3TbraffuDZ4aEf8KWOmI_w/521fe3ce-20f6-4f9b-d8de-b1c3b4724100/public)

Aseem Gupta

SuperKalam

[![Image 68: SuperKalam logo](https://imagedelivery.net/3TbraffuDZ4aEf8KWOmI_w/cf46d1a3-604d-4eef-2e18-384b767a6600/public)](https://superkalam.com/)

> The Trigger.dev developer experience is unparalleled for building durable agents. Queues, streaming, retries, logging and more, all with just a few lines of code.
> 
> 
> 
> [Read Capy's customer story](https://trigger.dev/customers/capy-customer-story)

![Image 69: Justin Sun](https://trigger.dev/testimonials/capy/justin-sun.png)

Justin Sun

Capy

[![Image 70: Capy logo](https://trigger.dev/testimonials/capy/capy-logo.svg)](https://capy.ai/)

> Teams routinely find 200% more opportunities and increase proposal output by 70% using GovSignals. We build on Trigger.dev to make that level of scale practical.
> 
> 
> 
> [Read GovSignals's customer story](https://trigger.dev/customers/govsignals-customer-story)

![Image 71: Conner Aldrich](https://trigger.dev/customers/govsignals/conner-aldrich.png)

Conner Aldrich

GovSignals

[![Image 72: GovSignals logo](https://trigger.dev/customers/govsignals/govsignals-logo.svg)](https://govsignals.ai/)

> Trigger.dev was the missing piece in our journey to go fully serverless. It enables us to focus entirely on building our product without worrying about the complexities of background jobs. The best part? We’re continuously adding more jobs as we scale!
> 
> 
> 
> [Read Midday's customer story](https://trigger.dev/customers/midday-customer-story)

![Image 73: Pontus Abrahamsson](https://imagedelivery.net/3TbraffuDZ4aEf8KWOmI_w/d60cc0d1-a132-420a-b7fa-bdb67267f800/public)

Pontus Abrahamsson

Midday

[![Image 74: Midday logo](https://imagedelivery.net/3TbraffuDZ4aEf8KWOmI_w/9c0e5ff1-b718-4b67-8e7c-4a45f4697f00/public)](https://midday.ai/)

> We found software that's open-source friendly called MuPDF which runs in Node.js environments. Combined with using Trigger's tasks and runs, it solved our problem instantly. We are now easily processing around 6,000 documents per month anywhere from one page to hundreds of pages.
> 
> 
> 
> [Read Papermark's customer story](https://trigger.dev/customers/papermark-customer-story)

![Image 75: Marc Seitz](https://trigger.dev/customers/papermark/marc-seitz.png)

Marc Seitz

Papermark

[![Image 76: Papermark logo](https://trigger.dev/customers/papermark/papermark-logo.png)](https://papermark.io/)

> The platform transformed my workflow, I'm thrilled with it! Migrating my agentic workflow from Python to Trigger.dev has been a major win. Rare to find powerful features paired with such responsive assistance.
> 
> 
> 
> [Read Tierly's customer story](https://trigger.dev/customers/tierly-customer-story)

![Image 77: Gerasimos](https://trigger.dev/testimonials/tierly/gerasimos.png)

Gerasimos

Tierly

[![Image 78: Tierly logo](https://trigger.dev/testimonials/tierly/tierly.svg)](https://tierly.app/)

> We’ve been looking for a product like Trigger.dev for a long time - automation that's simple and dev-focused.

![Image 79: Han Wang](https://imagedelivery.net/3TbraffuDZ4aEf8KWOmI_w/4e3d1187-c27b-4bdc-feac-d2e5297e9a00/public)

Han Wang

Mintlify

[![Image 80: Mintlify logo](https://imagedelivery.net/3TbraffuDZ4aEf8KWOmI_w/1a068830-bc93-451c-b5c2-f76b24e42000/public)](https://mintlify.com/)

> Using Trigger.dev for our Slack jobs saved us loads of time! It was much easier to set up than a no-code tool.

![Image 81: Vlad Matsiiako](https://imagedelivery.net/3TbraffuDZ4aEf8KWOmI_w/9c9e9c2e-5ff1-4227-f0d3-514aa2e49300/public)

Vlad Matsiiako

Infisical

[![Image 82: Infisical logo](https://imagedelivery.net/3TbraffuDZ4aEf8KWOmI_w/c01ec071-f909-4eed-2f0a-6db7aa885c00/public)](https://infisical.com/)

> We decided to use Trigger.dev over Inngest or setting up our own dedicated solution. We had also looked into UI-based solutions like Zapier and n8n, but they become complex, really slow, expensive and time-consuming to manage for large automations. Trigger.dev made the most overall sense for us when taking dev-speed, cost, scalability and being future-proof into account.

![Image 83: Sohrab Fadai](https://trigger.dev/testimonials/heartspace-ai/sohrab-fadai.png)

Sohrab Fadai

Heartspace AI

[![Image 84: Heartspace AI logo](https://trigger.dev/testimonials/heartspace-ai/heartspace-ai.png)](https://heartspace.ai/)

> I’m in love with Trigger.dev – it’s so much better than the old bull.js + heroku + redis setup that I used to use. You’ve knocked it out of the park with this tool!

![Image 85: Kushal Byatnal](https://imagedelivery.net/3TbraffuDZ4aEf8KWOmI_w/6738d30f-ccd5-4342-8764-a2194fc0d900/public)

Kushal Byatnal

Extend

[![Image 86: Extend logo](https://imagedelivery.net/3TbraffuDZ4aEf8KWOmI_w/0db95e34-61a0-47ff-879d-7698f3084900/public)](https://www.extend.app/)

> Trigger.dev helps us process bounties & tips on Algora without having to duct-tape queues & crons. With standardized timeouts, retries & logging we get full resilience & observability!

![Image 87: Zaf Cesur](https://trigger.dev/testimonials/algora/zafer-cesur.png)

Zaf Cesur

Algora

[![Image 88: Algora logo](https://trigger.dev/testimonials/algora/algora.png)](https://algora.io/)

> I really enjoyed using Trigger.dev to create jobs through code. I found the API integrations and scheduling features super useful.

![Image 89: Adam Shiervani](https://imagedelivery.net/3TbraffuDZ4aEf8KWOmI_w/36535ea9-56b4-42e3-4e45-ef08d293dd00/public)

Adam Shiervani

BuildJet

[![Image 90: BuildJet logo](https://imagedelivery.net/3TbraffuDZ4aEf8KWOmI_w/06b5fdf7-f7be-424c-a4df-dfa0e3d93100/public)](https://buildjet.com/)

Read more...

### Ready to start building?

Build and deploy your first task in 3 mins with no timeouts and no infrastructure to manage.

[Get started for free](https://cloud.trigger.dev/)

#### Simple pricing

Only pay for what you use and scale with your needs.

[Explore pricing](https://trigger.dev/pricing)

#### Self-host

Trigger.dev is open source and self-hostable.

[Self-hosting docs](https://trigger.dev/docs/v3/open-source-self-hosting)

[](https://trigger.dev/#top)

[](https://trigger.dev/discord)[](https://twitter.com/triggerdotdev)[](https://www.linkedin.com/company/triggerdotdev)[](https://bsky.app/profile/triggerdev.bsky.social)[](https://github.com/triggerdotdev/trigger.dev)

#### Docs

[Introduction](https://trigger.dev/docs/introduction "Introduction")[Quick start](https://trigger.dev/docs/quick-start "Quick start")[Building with AI](https://trigger.dev/docs/guides/ai-agents/overview "Building with AI")[Official MCP server](https://trigger.dev/docs/mcp-introduction "Official MCP server")[Tasks](https://trigger.dev/docs/tasks/overview "Tasks")[Examples](https://trigger.dev/docs/guides/introduction "Examples")[Realtime](https://trigger.dev/docs/realtime/overview "Realtime")[Self-hosting](https://trigger.dev/docs/self-hosting/overview "Self-hosting")

#### Developers

[Careers](https://trigger.dev/careers "Careers")[Changelog](https://trigger.dev/changelog "Changelog")[Blog](https://trigger.dev/blog "Blog")[OSS friends](https://trigger.dev/oss-friends "OSS friends")[Community](https://trigger.dev/discord "Community")[GitHub](https://github.com/triggerdotdev/trigger.dev "GitHub")[vs Temporal](https://trigger.dev/vs/temporal "vs Temporal")[vs BullMQ](https://trigger.dev/vs/bullmq "vs BullMQ")

#### Product

[Pricing](https://trigger.dev/pricing "Pricing")[Product](https://trigger.dev/product "Product")[AI agents](https://trigger.dev/product/ai-agents "AI agents")[Realtime](https://trigger.dev/product/realtime "Realtime")[Observability](https://trigger.dev/product/observability-and-monitoring "Observability")[Roadmap](https://feedback.trigger.dev/roadmap "Roadmap")[Feature requests](https://feedback.trigger.dev/ "Feature requests")[Customers](https://trigger.dev/customers "Customers")

#### Company

[Contact](https://trigger.dev/contact "Contact")[Brand kit](https://trigger.dev/brand "Brand kit")[Terms](https://trigger.dev/legal "Terms")[Privacy](https://trigger.dev/legal/privacy "Privacy")[DPA](https://trigger.dev/legal/dpa "DPA")[Security](https://trigger.dev/security "Security")[SOC2](https://security.trigger.dev/ "SOC2")[GDPR](https://security.trigger.dev/ "GDPR")

© 2026 API Hero Ltd.
