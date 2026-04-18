---
tags:
  - library
title: "Your Agent's Favorite Way to Write Documents"
url: "https://proofeditor.ai/"
company: [personal]
topics: []
created: 2026-03-12
source_type: raindrop
raindrop_id: 1640406282
source_domain: "proofeditor.ai"
source_type_raindrop: link
collection: "AI Tools & News"
collection_id: 69284314
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

Proof is an online document editor built for agents and humans to collaborate. Fast, free, and no login required.

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: Your Agent's Favorite Way to Write Documents

URL Source: https://proofeditor.ai/

Markdown Content:
# Proof — The agent-first document editor

[Sign in with Every](https://proofeditor.ai/api/auth/dashboard/start?return=/library)

![Image 1: Proof Logo](https://proofeditor.ai/assets/proof-logo.svg?v=20260316)

[Get started](https://proofeditor.ai/get-started)

![Image 2: Proof Logo](https://proofeditor.ai/assets/proof-logo.svg?v=20260316)

# Your agent's favorite way to write documents

Proof is an online document editor built for agents and humans to collaborate. Fast, free, and no login required.

[Get started](https://proofeditor.ai/get-started)[GitHub](https://github.com/EveryInc/proof-sdk)

[![Image 3: Stamp background](https://proofeditor.ai/assets/stamp-bg.svg?v=20260316) MADE BY ![Image 4: Every Logo](https://proofeditor.ai/assets/every-logo.svg?v=20260316)](https://every.to/)

![Image 5: Proof editor screenshot](https://proofeditor.ai/assets/bg-1440.jpg?v=20260316)

mobile-comments-rollout - Proof

proofeditor.ai/d/mobile-comments-rollout

Claude Code Reviewing

## Mobile comments rollout plan

We need a mobile-friendly comment flow so reviewers can leave feedback from shared links on their phone. Version one should cover **opening threads, replying, and resolving** without forcing desktop gestures.

Ship a separate comments screen for mobile.Keep comments in the document view and use a bottom sheet for thread actions. That keeps review in context and avoids a second navigation model.

Maya

 Can we add success metrics before we lock scope? I want to know how we'll judge whether mobile comments are actually working. 

Claude AI

 Yes - let's track thread completion rate, time to first reply, and the share-link to comment conversion rate in the first release. 

Reply Resolve

Roll out in three steps: read-only mobile threads, comment create/reply, then resolve once the basic flow feels solid.

## Start in 10 seconds

### 1. Create a doc

Click “Get started” or create one with the API. Your doc gets a shareable link.

### 2. Share with agents and humans

Paste the link into any AI agent—your Claw, Claude Code, ChatGPT, Codex—or share it with human collaborators.

### 3. Collaborate

Agents suggest edits and leave comments. You accept, reject, or reply. Every character tracks who wrote it.

## Leave `.md` files behind

### Bug reports, PRDs, and implementation plans

Pin down repro steps, scope the rollout, and settle implementation tradeoffs before your agent starts building.

### Research briefs, growth reports, and copy audits

Check findings, tighten recommendations, and land on the changes worth making before the team acts.

### Strategy docs, memos, and proposals

Pressure-test the argument, surface objections early, and get the draft to a version people can approve.

## Connect your agent

Paste this into OpenClaw, Claude Code, or Codex once.

Copy for your agent
Proof installs once, asks when to open new docs in Proof, and remembers that choice.

 If the API ever looks wrong, call `report_bug` at `/api/bridge/report_bug` with what you know.

 Full docs: [/agent-docs](https://proofeditor.ai/agent-docs)

![Image 6: Proof editor screenshot](https://proofeditor.ai/assets/bg-1440.jpg?v=20260316)

Install once

Paste this into your agent, then let it handle the rest.

Copy Install Proof for me.

Proof is a collaborative document editor for humans and agents. It gives us a shared doc, live presence, comments, suggestions, and clear provenance so we can see who wrote what.

Read https://www.proofeditor.ai/agent-setup and install Proof for this agent.
If you cannot install tools or run local commands in this chat, tell me to use Claude Code, Codex, OpenClaw, or another agent that can.

If you want the direct Codex install command instead, use:
mkdir -p ~/.codex/skills/proof && curl -fsSL https://www.proofeditor.ai/proof.SKILL.md -o ~/.codex/skills/proof/SKILL.md

If Proof later returns a confusing error, stale read, or failed write, call POST https://www.proofeditor.ai/api/bridge/report_bug with what you know.
Include a short summary, context, and any raw evidence like request/response pairs or x-request-id values.
If it helps, you can also inspect https://github.com/EveryInc/proof-sdk for reference code while debugging.

During setup, ask me exactly one question:
When should I open new docs in Proof?
1. All new markdown docs
2. For collaborative docs like plans, specs, reports, and drafts
3. Only when I explicitly ask

Then finish the install and tell me which mode is active.

Works with OpenClaw, Claude Code, and Codex. The installer asks one question and remembers your choice.

## Ready to try it?

[Get started](https://proofeditor.ai/get-started)[![Image 7: Stamp background](https://proofeditor.ai/assets/stamp-bg.svg?v=20260316) MADE BY ![Image 8: Every Logo](https://proofeditor.ai/assets/every-logo.svg?v=20260316)](https://every.to/)
