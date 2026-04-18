---
tags:
  - library
title: "Latitude | The Open-Source LLM Development Platform"
url: "https://latitude.so/developers"
company: [personal]
topics: []
created: 2025-09-18
source_type: raindrop
raindrop_id: 1348169898
source_domain: "latitude.so"
source_type_raindrop: link
collection: "AI Tools & News"
collection_id: 69284314
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

Latitude is an end-to-end platform for prompt engineering where domain experts can collaborate with engineers to ship and maintain production-grade LLM features.

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: AI Agent Observability Platform - Latitude

URL Source: https://latitude.so/developers

Markdown Content:
# AI Agent Observability Platform - Latitude

# Announcing Latitude V2 — an agent issue monitoring platform

# [Join waitlist](https://latitude.so/waitlist)

# A clear path to reliable AI

Production failures become clear signals. Signals become fixes.

[Get started](https://latitude.so/signup)

[Book a demo](https://latitude.so/book-demo)

### 80%

Fewer critical errors reaching production

### 8x

Faster prompt iteration using GEPA (Agrawal et al., 2025)

### 25%

Accuracy increase in the first 2 weeks

[Observability](https://latitude.so/developers)

[Human feedback](https://latitude.so/developers)

[Failure discovery](https://latitude.so/developers)

[Playground](https://latitude.so/developers)

[Evals](https://latitude.so/developers)

[A/B testing](https://latitude.so/developers)

![Image 1](https://framerusercontent.com/images/vACa0Em56RNbgj4hJErECtYXk.png?width=3840&height=2160)

## Observability

Capture real inputs, outputs, and context from live traffic. Understand what your system is actually doing, not what you expect it to do.

[View docs](https://docs.latitude.so/guides/getting-started/introduction)

#### Full traces

Observe your AI’s behaviour in the most comprehensive way

#### Usage statistics

Keep track of the token usage and regulate expenses

AI

behaviour

drifts.

Small

prompt

changes

break

products

in

unexpected

ways,

results

get

worse

and

it's

hard

to

tell

why.

Teams

keep

tweaking,

shipping

while

hoping

the

system

still

works.

From

unp

Your AI

to reliable

Most tools help you see what your AI is doing. The hard part is knowing where it fails and what to change.

Trusted by teams building AI products at scale

[](https://latitude.so/)

[Pricing](https://latitude.so/pricing)

[Docs](https://docs.latitude.so/guides/getting-started/introduction)

[Resources](https://latitude.so/developers)

[![Image 2: Github Icon](https://framerusercontent.com/images/Y2VnwotSBPdl4u29ALWVymZ4LK0.png?width=98&height=96) ![Image 3: Github icon in blue fill](https://framerusercontent.com/images/LDKaT14p4FEQLMTNEJ5teJiWbvk.svg?width=24&height=24) 3,9k](https://github.com/latitude-dev/latitude-llm)

# Enter the reliability loop

A proven method to understand, evaluate, and fix your AI products

[See how it works](https://latitude.so/book-demo)

1. Observability

Capture real inputs, outputs, and context from live traffic to understand what your system is actually doing

![Image 4](https://framerusercontent.com/images/jgHzp3gnC6ctnTAy9qz8V1IG9jM.png?width=560&height=148)

2. Annotations

Annotate responses with real human judgment. Turn intent into a signal the system can learn from.

![Image 5](https://framerusercontent.com/images/qfmyAeckNIBrcbmv6u6L3Oz7zQ.png?width=560&height=148)

3. Error analysis

Automatically group failures into recurring issues, detect common failure modes and keep an eye on escalating issues.

![Image 6](https://framerusercontent.com/images/Jb8BlRX2HkOBAc7Uqp69PT3Y0.png?width=560&height=148)

4. Automatic evals

Convert real failure modes into evals that run continuously & catch regressions before they reach users.

![Image 7](https://framerusercontent.com/images/O8gfTvy5M7MiM1Jb75UbHwjlIE.png?width=560&height=148)

5. Prompt manager + optimizer

Automatically test prompt variations against real evals, then let the system optimize prompts using GEPA to reduce failures over time.

![Image 8](https://framerusercontent.com/images/FGAksuvkdOBIfCIbX2kGzKrgnJ4.png?width=560&height=148)

Get started now

# Start with visibility.

Grow into reliability.

Start the reliability loop with lightweight instrumentation. Go deeper when you’re ready.

[View docs](https://docs.latitude.so/guides/getting-started/introduction)

Providers

[OpenAI](https://latitude.so/developers)

[Anthropic](https://latitude.so/developers)

[Azure](https://latitude.so/developers)

[Google AI Platform](https://latitude.so/developers)

[Amazon Bedrock](https://latitude.so/developers)

[Cohere](https://latitude.so/developers)

[Together AI](https://latitude.so/developers)

[Vertex AI](https://latitude.so/developers)

[Gemini](https://latitude.so/developers)

[Groq](https://latitude.so/developers)

[Mistral AI](https://latitude.so/developers)

[Ollama](https://latitude.so/developers)

[LiteLLM](https://latitude.so/developers)

[Replicate](https://latitude.so/developers)

[AWS SageMaker](https://latitude.so/developers)

[Hugging Face Transformers](https://latitude.so/developers)

[Aleph Aplha](https://latitude.so/developers)

[IBM watsonx.ai](https://latitude.so/developers)

import { LatitudeTelemetry } from '@latitude-data/telemetry'
import OpenAI from 'openai'

const telemetry = new LatitudeTelemetry(
  process.env.LATITUDE_API_KEY,
  { instrumentations: { openai: OpenAI } }
)

async function generateSupportReply(input: string) {
  return telemetry.capture(
    {
      projectId: 123, // The ID of your project in Latitude
      path: 'generate-support-reply', // Add a path to identify this prompt in Latitude
    },
    async () => {
      const client = new OpenAI()
      const completion = await client.chat.completions.create({
        model: 'gpt-4o',
        messages: [{ role: 'user', content: input }],
      })
      return completion.choices[0].message.content
    }
  )
}

TypeScript

Python

#### Instrument once

Add OTEL-compatible telemetry to your existing LLM calls to capture prompts, inputs, outputs, and context.

This gets the loop running and gives you visibility from day one

#### Learn from production

Review traces, add feedback, and uncover failure patterns as your system runs.

Steps 1–4 of the loop work out of the box

#### Go further when it matters

Use Latitude as the source of truth for your prompts to enable automatic optimization and close the loop.

The full reliability loop, when you’re ready

![Image 9](https://framerusercontent.com/images/ol2aIj1nEmUF4O3omhbSBf8bdx8.png?width=256&height=256)

![Image 10](https://framerusercontent.com/images/9Vtta19w3zerUYUoo2L7RQYZ6ts.png?width=256&height=256)

![Image 11](https://framerusercontent.com/images/WQCD6CKb1bbAKHGTSJk04MxhLM.png?width=256&height=256)

![Image 12](https://framerusercontent.com/images/GOqDsvC5PLFGY8x6RTggGGWGMo.png?width=256&height=256)

![Image 13](https://framerusercontent.com/images/KzzUUCHzjvN7OU8mNGVaqaxuI.png?width=256&height=256)

![Image 14](https://framerusercontent.com/images/kopCBimtI0FSFVcqIkfJ5ki5Ms.png?width=256&height=256)

![Image 15](https://framerusercontent.com/images/RKCQJfcQhy15QNVx14H5F5LfU.png?width=256&height=256)

![Image 16](https://framerusercontent.com/images/cznflAyWTTReY8AKAvcNoOZMG7s.png?width=256&height=256)

![Image 17](https://framerusercontent.com/images/SXaO5Atqllis6FAz2Wj95vgbI.png?width=256&height=256)

![Image 18](https://framerusercontent.com/images/mAfsCMPlhLe82s1oxXEuLp3eWw.png?width=256&height=256)

![Image 19](https://framerusercontent.com/images/h5blVJcxmuWY7SjCrFsw5R7FO7w.png?width=256&height=256)

![Image 20](https://framerusercontent.com/images/CaovD9a96F42IwhJRkLfGP3sA.png?width=256&height=256)

![Image 21](https://framerusercontent.com/images/cznflAyWTTReY8AKAvcNoOZMG7s.png?width=256&height=256)

![Image 22](https://framerusercontent.com/images/IRYyVro8kr4iL02o9WtOQMysDi4.png?width=256&height=256)

![Image 23](https://framerusercontent.com/images/RKCQJfcQhy15QNVx14H5F5LfU.png?width=256&height=256)

![Image 24](https://framerusercontent.com/images/SXaO5Atqllis6FAz2Wj95vgbI.png?width=256&height=256)

![Image 25](https://framerusercontent.com/images/mAfsCMPlhLe82s1oxXEuLp3eWw.png?width=256&height=256)

![Image 26](https://framerusercontent.com/images/h5blVJcxmuWY7SjCrFsw5R7FO7w.png?width=256&height=256)

![Image 27](https://framerusercontent.com/images/kopCBimtI0FSFVcqIkfJ5ki5Ms.png?width=256&height=256)

![Image 28](https://framerusercontent.com/images/KzzUUCHzjvN7OU8mNGVaqaxuI.png?width=256&height=256)

![Image 29](https://framerusercontent.com/images/WQCD6CKb1bbAKHGTSJk04MxhLM.png?width=256&height=256)

![Image 30](https://framerusercontent.com/images/GOqDsvC5PLFGY8x6RTggGGWGMo.png?width=256&height=256)

![Image 31](https://framerusercontent.com/images/9Vtta19w3zerUYUoo2L7RQYZ6ts.png?width=256&height=256)

![Image 32](https://framerusercontent.com/images/ol2aIj1nEmUF4O3omhbSBf8bdx8.png?width=256&height=256)

Get started for free

# Build AI

you can trust

Works with Vercel AI SDK, LangChain, OpenAI SDK, and most common model providers.

[Sign up to Latitude](https://latitude.so/signup)

[Book a demo](https://latitude.so/book-demo)

Frequently asked questions

What is Latitude?

How can I see where my AI fails in production?

Is it easy to set up evals in Latitude?

How does Latitude turn AI failures into improvements?

Does Latitude work with our existing stack?

Build reliable AI.

Latitude Data S.L. 2026

All rights reserved.

![Image 33](https://framerusercontent.com/images/WPGopgoeKs4KW6MszUw2W83HnQY.png?width=559&height=126)

Proyecto financiado con el apoyo de ACCIÓ - Generalitat de Catalunya

[Home](https://latitude.so/)

[Pricing](https://latitude.so/pricing)

[Log in](https://app.latitude.so/login)

[Blog](https://latitude.so/blog)

[Docs](https://docs.latitude.so/guides/getting-started/introduction)

[Guides](https://docs.latitude.so/guides/getting-started/quick-start-pm)

[Examples](https://docs.latitude.so/examples/overview)

[Community](https://join.slack.com/t/trylatitude/shared_invite/zt-35wu2h9es-N419qlptPMhyOeIpj3vjzw)

[Support](https://join.slack.com/t/trylatitude/shared_invite/zt-35wu2h9es-N419qlptPMhyOeIpj3vjzw)

[Terms](https://latitude.so/terms)

[Privacy](https://latitude.so/privacy)

![Image 35](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%26800%26600%268%2624%26800%26600%260%26na&eci=3&event=%7B%7D&event_id=f447cd57-39fe-468a-a3de-074d37e69c1c&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=a54ed1c8-ab33-41b3-925e-e67dcf50f993&pt=AI%20Agent%20Observability%20Platform%20-%20Latitude&tw_document_href=https%3A%2F%2Flatitude.so%2F&tw_iframe_status=0&tw_pid_src=1&twpid=tw.1776528866872.289962903279438489&txn_id=r1red&type=javascript&version=2.3.53)![Image 36](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%26800%26600%268%2624%26800%26600%260%26na&eci=3&event=%7B%7D&event_id=f447cd57-39fe-468a-a3de-074d37e69c1c&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=a54ed1c8-ab33-41b3-925e-e67dcf50f993&pt=AI%20Agent%20Observability%20Platform%20-%20Latitude&tw_document_href=https%3A%2F%2Flatitude.so%2F&tw_iframe_status=0&tw_pid_src=1&twpid=tw.1776528866872.289962903279438489&txn_id=r1red&type=javascript&version=2.3.53)
