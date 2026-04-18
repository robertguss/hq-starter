---
tags:
  - library
title: "Intent - The developer workspace for agent orchestration"
url: "https://www.augmentcode.com/product/intent"
company: [personal]
topics: []
created: 2026-03-07
source_type: raindrop
raindrop_id: 1633495867
source_domain: "augmentcode.com"
source_type_raindrop: link
collection: "AI Tools & News"
collection_id: 69284314
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

A public beta desktop app for spec-driven development with living specs. Plan, execute, and iterate on complex coding tasks with AI agents. Currently available for macOS (Apple Silicon).

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: Intent - Build with Intent

URL Source: https://www.augmentcode.com/product/intent

Markdown Content:
# Intent - Build with Intent | Augment Code
[Skip to content](https://www.augmentcode.com/product/intent#main-content)

[![Image 1: Augment Code](https://www.augmentcode.com/augment_code_wordmark.svg?dpl=dpl_7gBYUoBoJx7ZFDQrdiHx6N6Mo1qD)](https://www.augmentcode.com/)

Product

[Context Engine](https://www.augmentcode.com/context-engine)[Pricing](https://www.augmentcode.com/pricing)[Docs](https://docs.augmentcode.com/)[Blog](https://www.augmentcode.com/blog)

Resources

[Sign in](https://app.augmentcode.com/)[Download](https://cdn.augmentcode.com/stable/Intent-latest-arm64.dmg)

Product

[Agent](https://www.augmentcode.com/product/ide-agents)[Intent](https://www.augmentcode.com/product/intent)[Code Review](https://www.augmentcode.com/product/code-review)[Slack](https://www.augmentcode.com/product/slack)[CLI](https://www.augmentcode.com/product/CLI)[Context Engine MCP](https://www.augmentcode.com/product/context-engine-mcp)[Changelog](https://www.augmentcode.com/changelog)

[Context Engine](https://www.augmentcode.com/context-engine)[Pricing](https://www.augmentcode.com/pricing)[Docs](https://docs.augmentcode.com/)[Blog](https://www.augmentcode.com/blog)Resources

[Customers](https://www.augmentcode.com/customers)[Careers](https://www.augmentcode.com/careers)[ContextWiki](https://www.augmentcode.com/open-source)[Status Page](https://status.augmentcode.com/)[Trust Center](https://trust.augmentcode.com/)[Security](https://www.augmentcode.com/security)

[Talk to Sales](https://www.augmentcode.com/contact)[Sign in](https://app.augmentcode.com/)

[](https://www.augmentcode.com/)[Download](https://cdn.augmentcode.com/stable/Intent-latest-arm64.dmg)

Public Beta

# Build with Intent.

A developer workspace where agents are coordinated, specs stay alive, and every workspace is isolated.

[Download for Mac](https://cdn.augmentcode.com/stable/Intent-latest-arm64.dmg)

[For Apple Silicon](https://cdn.augmentcode.com/stable/Intent-latest-arm64.dmg)

See how it works

Add JWT auth middleware — acme-corp/api-gateway⌘K

Coordinator×

auth-middleware...×

a3f7b2c: Add...×

AGENTS / Coordinator / Coordinator agent

We need JWT authentication across the API gateway and auth service. Tokens should be issued by auth-service and validated by the gateway middleware.

I'll implement JWT auth across both services. Let me analyze the current codebase and create a plan.

2h ago

Make sure we support token refresh and handle expired tokens gracefully. Also add rate limiting to the token endpoint.

Good call. I'll add token refresh logic and rate limiting. Let me break this into parallel tasks across both repos.

1h ago

Go ahead and implement it. Start with the auth-service token issuance, then the gateway middleware.

I'll coordinate agents across both services. Spawning specialists now:

Auth Token Agent Running...

Implementing JWT issuance and refresh in auth-service

// token-service.ts

export class TokenService{

async issueToken(user: User) {

const payload = { sub: user.id,

Gateway Middleware Agent Running...

Adding JWT validation middleware to API gateway

// auth-middleware.ts

export function jwtMiddleware(

req: Request, res: Response,

Both agents are working in parallel across repos. Current progress:

*   • **Auth Token Agent:** Implementing token issuance, refresh, and revocation endpoints
*   • **Gateway Middleware Agent:** Adding JWT validation with RS256 and token expiry handling

Just now

Claude Opus 4.6@

Spec×

NOTES / Spec

### JWT Authentication — Cross-Service Implementation

Overview

Implement JWT-based authentication across api-gateway and auth-service. Tokens are issued by auth-service using RS256 signing, validated by gateway middleware. Support token refresh, revocation, and graceful expiry handling.

Architecture

*   • auth-service: token issuance, refresh, revocation
*   • api-gateway: JWT validation middleware, rate limiting
*   • Signing: RS256 with rotating key pairs
*   • Token lifetime: 15m access, 7d refresh
*   • Storage: Redis for revocation list

Endpoints

*   • POST /auth/token — issue access + refresh tokens
*   • POST /auth/refresh — rotate refresh token
*   • POST /auth/revoke — add token to revocation list
*   • GET /auth/.well-known/jwks — public key endpoint

Tasks

✓Set up RS256 key pair generation

✓Implement token issuance endpoint

✓Add refresh token rotation

/JWT validation middleware in gateway in progress

Rate limiting on /auth/token

Integration tests across services

Update API documentation

Add JWT auth middleware

acme-corp/api-gateway

Agents Context Changes 5 Files

Agent orchestration

A coordinator agent breaks down your task into a spec, then delegates work to specialist agents that run in parallel.

Coordinator

30m

I'll coordinate the JWT implementation across both services...

2 delegated agents

Auth Token Agent

running

Gateway Middleware Agent

running

Background agents 3

Test Suite Agent

Lint & Type Check

Docs Generator

Context

Context about the task, shared with all agents in this space.

Spec

Changes 5

Changes made to files by agents working in this space.

feat/jwt-auth → main

■auth-middleware.ts src/middleware+89-3

■token-service.ts src/services+142-0

■security.ts src/config+12-4

■auth.test.ts tests/integration+67-0

■routes.ts src+8-2

Files

The agents in this space are working off a copy of your files.

src

tests

config

docs

p 3000 Terminal ls npm run test:watch --...

+

See It In Action

## Orchestrate your agents like a system, not a swarm.

Intent — demo

Click to play demo

See It In Action

## Orchestrate your agents like a system, not a swarm.

Intent — demo

Click to play demo

BUILD WITH A LIVING SPEC

## Your spec is the source of truth. It stays that way.

Traditional specs rot the moment code ships. Living specs don't.

When an agent completes work, the spec updates to reflect reality. When requirements change, updates propagate to all active agents.

No more "what did we decide?" No more outdated PRDs. The living spec is the source of truth because it maintains itself.

Intent

···

▸auth-refactor.md Updated 2m ago

Migrate to JWT-based auth with automatic token refresh.

security backend

Requirements

✓JWT token-based authentication

○Refresh token rotation

○Session invalidation endpoint

Implementation Plan

1/3 complete

✓Create token service Auth Agent

done

2 Update auth middleware API Agent

3 Add refresh endpoint Test Agent

Decision: Using RS256 for token signing

BUILD WITH A COORDINATED TEAM

## A coordinator plans. Specialists execute. A verifier checks.

A Coordinator agent breaks down your spec into tasks, and delegates to Implementors that can run in waves. A Verifier agent checks the results against the spec. The Coordinator keeps them aligned and handles handoffs.

You can customize this to bring in your own specialist agents, and control how they're orchestrated.

Intent

···

Coordinator orchestrating

Delegating auth refactor tasks...

Auth Agent jwt-service.ts

Implementing token validation...

API Agent routes/auth.ts

Updating endpoints...

Test Agent auth.test.ts

Writing tests...

↔All agents synced to auth-refactor.md

BUILD IN ONE PLACE

## Code, browser, terminal, and git. One window.

Stop switching between your IDE, terminal, browser, and git client.

Intent has a built-in Chrome browser for previewing local changes. Git integration for staging, committing, and branch management.

Intent

···

●jwt-service.ts

1

2

3

4

5

6

●auth-spec.md

●Coordinator

●localhost:3000

BUILD WITHOUT LOSING STATE

## Close it. Reopen tomorrow. Everything is exactly where you left it.

Resumable sessions mean your workspace state persists across sessions. Close Intent, reopen it tomorrow, and everything is exactly as you left it.

Auto-commit captures work as it completes. Branch management is built-in. Your progress is always saved.

Intent

···

⎇auth-refactor worktree

a3f2c1d Add JWT validation Auth Agent

b7e4a2f Update middleware API Agent

✓PR #142 merged→main

⎇api-v2 worktree

c9d1e3a Add schema types Schema Agent

d2f5b8c Create endpoints Route Agent

✓PR #143 merged→main

BUILD WITH THE RIGHT MODEL

## Opus for architecture. Sonnet for speed. Pick per task.

Not every task needs the same model. Use Opus for complex architecture, Sonnet for rapid iteration, GPT 5.2 for deep code analysis or code review.

Intent supports all major state-of-the-art models. Mix and match based on what each task needs.

Intent

···

Specialists 6 included

Investigate

Explore codebase, assess feasibility

Implement

Execute implementation plans

Verify

Check implementations match specs

Critique

Review specs for feasibility

Debug

Analyze and fix issues

Code Review

Automated reviews with severity

BUILD WITH YOUR OWN AGENTS

## Bring Claude Code, Codex, or OpenCode. No Augment subscription required.

Already have a Claude Code, Codex, or OpenCode subscription? Use them directly in Intent. Try the full workspace experience without an Augment subscription.

You'll miss some powerful features like the Context Engine, but you can explore spec-driven development and agent orchestration for free.

Intent

···

Choose your provider

Augment Active

Claude Code

OpenAI Codex

OpenCode

BUILD WITH DEEP CONTEXT

## Every agent sees your entire codebase.

Every agent in Intent is powered by our industry-leading Context Engine. Whether it's the coordinator planning your work or specialists executing tasks, they all share deep understanding of your entire codebase.

[Discover the Context Engine](https://www.augmentcode.com/context-engine)

New Paradigm

## What is Spec-Driven Development?

Spec-Driven Development puts living specs at the center of your workflow.

Instead of writing code and hoping it matches the plan, you write a living spec and let agents implement it. As they work, the spec updates to reflect what was actually built.

The result: living specs that are always accurate, agents that stay aligned, and code that matches intent.

[Read our manifesto](https://www.augmentcode.com/blog/the-end-of-linear-work)

Code-First

Living Specs

Source of truth

Code

Spec

Documentation

Manual, drifts

Auto-updated

Agent alignment

Re-explain each time

Automatic

Refactoring

Break and fix

Spec-guided

Built For You

## Built for developers shipping with AI

Learning to run multiple AI agents

Already running multiple AI agents

Want a unified workspace

Tired of re-explaining context

Get Started

## Build with Intent

Orchestrate your agents like a system, not a swarm. Define what gets built, delegate to agents that stay aligned, and maintain full visibility from first commit to merge.

[Download for Mac](https://cdn.augmentcode.com/stable/Intent-latest-arm64.dmg)

[For Apple Silicon](https://cdn.augmentcode.com/stable/Intent-latest-arm64.dmg)

[Contact Sales](https://www.augmentcode.com/contact)

007

## Frequently asked questions

01 How much does Intent cost?

During this public beta period, Intent uses your regular Augment credits—the same way credits are consumed in our CLI or IDE extensions. There's no separate pricing for Intent.

02 How do I report bugs or provide feedback?

Inside the app, you can use the built-in feedback feature to report issues or share suggestions. You can also reach us directly at [intentfeedback@augmentcode.com](mailto:intentfeedback@augmentcode.com).

03 What about Windows and Linux?

We currently don't have any plan for these platforms today but if the Beta does well on Mac, we will actively start the development for both platforms.

[![Image 2: Augment Code](https://www.augmentcode.com/augment_code_wordmark.svg?dpl=dpl_7gBYUoBoJx7ZFDQrdiHx6N6Mo1qD)](https://www.augmentcode.com/)

### PRODUCT

*   [Agent](https://www.augmentcode.com/product/ide-agents)
*   [Intent](https://www.augmentcode.com/product/intent)
*   [Code Review](https://www.augmentcode.com/product/code-review)
*   [Slack](https://www.augmentcode.com/product/slack)
*   [CLI](https://www.augmentcode.com/product/CLI)
*   [Pricing](https://www.augmentcode.com/pricing)

### RESOURCES

*   [Customers](https://www.augmentcode.com/customers)
*   [Docs](https://docs.augmentcode.com/)
*   [Blog](https://www.augmentcode.com/blog)
*   [Guides](https://www.augmentcode.com/guides)
*   [Learn](https://www.augmentcode.com/learn)
*   [Tools](https://www.augmentcode.com/tools)
*   [AI Engineering Playbook](https://www.augmentcode.com/resources/ai-powered-engineering-at-scale)

### COMPANY

*   [Careers](https://www.augmentcode.com/careers)
*   [Press Inquiries](mailto:press@augmentcode.com)
*   [Press Kit](https://www.dropbox.com/scl/fo/pt4cxyhlyug03qpu19m66/AMYHXqBCjQdjhx8heH2TrJ0?rlkey=u8esym6obngbl1g77ft9r97pm&st=jejivpse&dl=1)
*   [Contact Sales](https://www.augmentcode.com/contact)
*   [Contact Support](https://support.augmentcode.com/)
*   [Changelog](https://www.augmentcode.com/changelog)
*   [Privacy & Security](https://www.augmentcode.com/security)
*   [Trust Center](https://trust.augmentcode.com/)
*   [Status Page](https://status.augmentcode.com/)

### LEGAL

*   [Cookie Policy](https://www.augmentcode.com/legal/cookie-policy)
*   [Privacy Policy](https://www.augmentcode.com/legal/privacy-policy)
*   [SLA and Support Policy](https://www.augmentcode.com/legal/sla-and-support-policy)
*   Terms of Service 

[![Image 3: Augment Code](https://www.augmentcode.com/augment_code_wordmark.svg?dpl=dpl_7gBYUoBoJx7ZFDQrdiHx6N6Mo1qD)](https://www.augmentcode.com/)

© 2026 Augment Code. All rights reserved.

[](https://x.com/augmentcode)[](https://bsky.app/profile/augmentcode.com)[](https://www.linkedin.com/company/augmentinc/)[](https://www.youtube.com/@Augment-Code)[](https://www.reddit.com/r/AugmentCodeAI/)

DARK

LIGHT

SYSTEM
