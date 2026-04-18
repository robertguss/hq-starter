---
tags:
  - library
title: "Open Agents"
url: "https://vercel.com/templates/template/open-agents"
company: [personal]
topics: []
created: 2026-04-13
source_type: raindrop
raindrop_id: 1683728276
source_domain: "vercel.com"
source_type_raindrop: link
collection: "AI Tools & News"
collection_id: 69284314
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

An open-source platform that gives you everything you need to build and run your own background coding agents on Vercel

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: Open Agents

URL Source: https://vercel.com/templates/template/open-agents

Markdown Content:
## Open Agents

Open Agents is an open-source reference app for building and running background coding agents on Vercel. It includes the web UI, the agent runtime, sandbox orchestration, and the GitHub integration needed to go from prompt to code changes without keeping your laptop involved.

The repo is meant to be forked and adapted, not treated as a black box.

### What it is

Open Agents is a three-layer system:

`Web -> Agent workflow -> Sandbox VM`

*   The web app handles auth, sessions, chat, and streaming UI.
*   The agent runs as a durable workflow on Vercel.
*   The sandbox is the execution environment: filesystem, shell, git, dev servers, and preview ports.

#### The key architectural decision: the agent is not the sandbox

The agent does not run inside the VM. It runs outside the sandbox and interacts with it through tools like file reads, edits, search, and shell commands.

That separation is the main point of the project:

*   agent execution is not tied to a single request lifecycle
*   sandbox lifecycle can hibernate and resume independently
*   model/provider choices and sandbox implementation can evolve separately
*   the VM stays a plain execution environment instead of becoming the control plane

### Current capabilities

*   chat-driven coding agent with file, search, shell, task, skill, and web tools
*   durable multi-step execution with Workflow SDK-backed runs, streaming, and cancellation
*   isolated Vercel sandboxes with snapshot-based resume
*   repo cloning and branch work inside the sandbox
*   optional auto-commit, push, and PR creation after a successful run
*   session sharing via read-only links
*   optional voice input via ElevenLabs transcription

### Runtime notes

A few details that matter for understanding the current implementation:

*   Chat requests start a workflow run instead of executing the agent inline.
*   Each agent turn can continue across many persisted workflow steps.
*   Active runs can be resumed by reconnecting to the stream for the existing workflow.
*   Sandboxes use a base snapshot, expose ports `3000`, `5173`, `4321`, and `8000`, and hibernate after inactivity.
*   Auto-commit and auto-PR are supported, but they are preference-driven features, not always-on behavior.

### What is actually required today

These requirements are based on the current `apps/web` codepath, not older setup scripts.

#### Minimum runtime

These are the hard requirements for the app to boot and load server state:

#### Required to sign in and actually use the hosted app

A useful deployment also needs token encryption plus Vercel OAuth sign-in:

Without these, the site can deploy, but Vercel sign-in will not work.

#### Required for GitHub repo access, pushes, and PRs

If you want users to connect GitHub, install the app on repos/orgs, clone private repos, push branches, or open PRs, add these GitHub App values:

#### Optional

*   `REDIS_URL` / `KV_URL`: optional skills metadata cache (falls back to in-memory when not configured).
*   `VERCEL_PROJECT_PRODUCTION_URL` / `NEXT_PUBLIC_VERCEL_PROJECT_PRODUCTION_URL`: canonical production URL for metadata and some callback behavior.
*   `VERCEL_SANDBOX_BASE_SNAPSHOT_ID`: override the default sandbox snapshot.
*   `ELEVENLABS_API_KEY`: voice transcription.

### Deploy your own copy on Vercel

Recommended path: deploy this repo at the repo root on Vercel, then layer on auth and GitHub integration.

1.   Fork this repo.

2.   Create a PostgreSQL database and copy its connection string.

3.   Generate these secrets:

4.   Import the repo into Vercel.

5.   Add at least these env vars in Vercel project settings:

6.   Deploy once to get a stable production URL.

7.   Create a Vercel OAuth app with callback URL:

`https://YOUR_DOMAIN/api/auth/vercel/callback` 
8.   Add these env vars and redeploy:

9.   If you want the full GitHub-enabled coding-agent flow, create a GitHub App using:

    *   Homepage URL: `https://YOUR_DOMAIN`
    *   Callback URL: `https://YOUR_DOMAIN/api/github/app/callback`
    *   Setup URL: `https://YOUR_DOMAIN/api/github/app/callback`

In the GitHub App settings:

    *   enable "Request user authorization (OAuth) during installation"
    *   use the GitHub App's Client ID and Client Secret for `NEXT_PUBLIC_GITHUB_CLIENT_ID` and `GITHUB_CLIENT_SECRET`
    *   make the app public if you want org installs to work cleanly

10.   Add the GitHub App env vars and redeploy.

11.   Optionally add Redis/KV and the canonical production URL vars.

### Local setup

1.   Install dependencies:

2.   Create your local env file:

3.   Fill in the required values in `apps/web/.env`.

4.   Start the app:

If you already have a linked Vercel project, you can still pull env vars locally with `vc env pull`, but setup is now intentionally manual so you can see exactly which values matter.

### OAuth and integration setup

#### Vercel OAuth

Create a Vercel OAuth app and use this callback:

`https://YOUR_DOMAIN/api/auth/vercel/callback`

For local development, use:

`http://localhost:3000/api/auth/vercel/callback`

Then set:

#### GitHub App

You do not need a separate GitHub OAuth app. Open Agents uses the GitHub App's user authorization flow.

Create a GitHub App for installation-based repo access and configure:

*   Homepage URL: `https://YOUR_DOMAIN`
*   Callback URL: `https://YOUR_DOMAIN/api/github/app/callback`
*   Setup URL: `https://YOUR_DOMAIN/api/github/app/callback`
*   enable "Request user authorization (OAuth) during installation"
*   make the app public if you want org installs to work cleanly

For local development, use `http://localhost:3000/api/github/app/callback` for the callback/setup URL and `http://localhost:3000` as the homepage URL.

Then set:

`GITHUB_APP_PRIVATE_KEY` can be stored as the PEM contents with escaped newlines or as a base64-encoded PEM.

### Useful commands

### Repo layout

`apps/web         Next.js app, workflows, auth, chat UIpackages/agent   agent implementation, tools, subagents, skillspackages/sandbox sandbox abstraction and Vercel sandbox integrationpackages/shared  shared utilities`
