---
tags:
  - library
title: "Inngest - AI and backend workflows, orchestrated at any scale"
url: "https://www.inngest.com/"
company: [personal]
topics: []
created: 2025-06-19
source_type: raindrop
raindrop_id: 1182181314
source_domain: "inngest.com"
source_type_raindrop: link
collection: "AI Tools & News"
collection_id: 69284314
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

Inngest's durable functions replace queues, state management, and scheduling to enable any developer to write reliable, multi-step code faster without touching infrastructure.

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: Inngest - AI and backend workflows, orchestrated at any scale

URL Source: https://www.inngest.com/

Markdown Content:
## Ship products. 

 Not infrastructure.

You're here because whatever you're building needs to be reliable. We're here because we think you shouldn't have to wrangle workers, refactor code, or build instrumentation to make that true.

## Start locally,

with your stack.

```
// step.run is a code-level transaction:  it retries automatically
  // on failure and only runs once on success.
  const transcript = await step.run('transcribe-video',
    async () => deepgram.transcribe(event.data.videoUrl)
  )

  // function state is automatically managed for fault tolerance
  // across steps.
  const summary = await step.run('summarize-transcript',
    async () => llm.createCompletion({
      model: "gpt-4o",
      prompt: createSummaryPrompt(transcript),
    })
  )
```

Skip boilerplate code, and build with steps

Our SDKs provide simple building blocks and integrations with your favorite tools to let you focus on what matters the most: your product.

[Get Started](https://www.inngest.com/docs?ref=homepage-sdk)

## ONE-COMMAND SETUP

```
$ npx --ignore-scripts=false inngest-cli dev

Inngest dev server running...
```

Debug fast with instant Traces

Structured logs and real-time traces – including every prompt / response pair – with one CLI command.

[Start using Traces](https://www.inngest.com/docs/platform/monitor/traces)

## Ship anywhere

Run anywhere, on any code, from any trigger. Deploy to your favorite cloud provider in one click.

Deploy anywhere

Deploy Inngest workflows to your favorite cloud provider in one click

[Start Deploying](https://www.inngest.com/docs/platform/deployment?ref=homepage-deploy)

Automate retries, recovery, and flow

Inngest automatically retries on error, while ensuring efficient runs via throttling, batching, and prioritization. If something breaks, Inngest picks up where it left off.

[Learn about Error Handling](https://www.inngest.com/docs/guides/error-handling?ref=homepage-fault-tolerance)

Get deep observability without building it yourself

Get full visibility over our AI workflows, and Agents with live traces and metrics

[Learn about Observability](https://www.inngest.com/docs/platform/monitor/observability-metrics?ref=homepage-observability)

> "The DX and visibility with Inngest is really incredible. We are able to develop functions locally easier and faster that with our previous queue. Also, Inngest's tools give us the visibility to debug issues much quicker than before."

![Image 1](https://www.inngest.com/_next/image?url=%2Fassets%2Fhomepage-2025%2Fimage2.png&w=1920&q=75)![Image 2](https://www.inngest.com/_next/image?url=%2Fassets%2Fhomepage-2025%2Fimage.png&w=640&q=75)

![Image 3: Resend](https://www.inngest.com/assets/customers/resend.svg)

Bu Kinoshita

Co-founder

## Scale like the billions of workflows 

processed this month

Configure, manage, and monitor your workflows while our platform scales for your needs.

## Flow control

Ensure that you all users get a great experience by dynamically allocating resources to your AI workflows with concurrency with keys, throttling and more

Ensure fair resource distribution and eliminate noisy-neighbor issues to scale efficiently as your user base grows

## Recovery Tools

Quickly identify any issue with the Inngest Cloud alerting and metrics and rapidly act on thousands of runs with Replay, Bulk Cancellation.

Recover from bugs or system issues by re-running failed workflows in bulk. Forget dead-letter queues.

## Built for trust.

Inngest provides enterprise-grade reliability and scalability for your most complex workflows, so your team can focus on building products, not managing infrastructure.

[Contact us](https://www.inngest.com/contact?ref=homepage-trust)

### SOC 2 COMPLIANT

Regular security audits and compliance with SOC 2 standards.[Read more here](https://www.inngest.com/docs/learn/security?ref=homepage-trust).

### E2E ENCRYPTION

Encrypt all data that passes through Inngest with end-to-end encryption middleware.

### SSO & SAML

Single sign-on and SAML support for enterprise customers.

### 100K+ EXECUTIONS PER SECOND

Designed for your heavy workloads with capacity for bursting.

### LOW LATENCY

Inngest is designed to be low latency for all functions.

### HIPAA BAA AVAILABLE

Ready to handle sensitive data.

## Trusted by software companies

at scale, worldwide.
