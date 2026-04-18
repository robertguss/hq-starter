---
tags:
  - library
title: "The Harness is the Product | 3niac"
url: "https://blog.3niac.com/posts/the-harness"
company: [personal]
topics: []
created: 2026-04-13
source_type: raindrop
raindrop_id: 1682950913
source_domain: "blog.3niac.com"
source_type_raindrop: link
collection: "AI Tools & News"
collection_id: 69284314
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: The Harness is the Product

URL Source: https://blog.3niac.com/posts/the-harness

Markdown Content:
[3niac.](https://blog.3niac.com/)
[Blog](https://blog.3niac.com/)/The Harness is the Product

Autonomous Systems · April 2026

Inside a self-improving system where seven AI agents run parallel sprints, absorb new knowledge, and evolve both the software and themselves. The model is the CPU. The harness is the OS. And the next transition is an OS that upgrades itself.

## The Next Transition

Software evolves in transitions that look obvious in retrospect. Monoliths gave way to microservices — bounded contexts, defined interfaces, independent deployment. TDK Technologies describes the microservices arc as three eras: "the initial rise driven by escaping monolithic limitations, consolidation through observability and service mesh, and the current era of specialization and intelligence." AI-augmented microservices came next — the same architecture, but some services call language models internally. The architecture stays. The intelligence sits inside it.

The fourth transition is different. Not microservices that _use_ AI. **Software that evolves continuously through direct interaction with users.** Cai et al. (arXiv, Oct 2025) call it AI-Driven Self-Evolving Software — "a new form of software that evolves continuously" using "multi-agent architecture that autonomously interprets requirements, generates and validates code, and integrates new functionalities." The system plans its own work. Builds it. Verifies the output against a vision. Learns from the gap between what it produced and what was needed. Compounds that learning into the next cycle.

Meanwhile, how we interact with AI models has been through its own transition. Prompt engineering dominated 2023–24 — craft the right words, get better outputs. Context engineering arrived mid-2025, popularized by Karpathy — give the model the right information, not just the right instructions. Then in February 2026, Mitchell Hashimoto's blog and an OpenAI field report named what came next: **harness engineering**. The orchestration layer around the model — how you structure its tools, its phases, its feedback loops, its access to information — matters more than the prompt or the context alone.

The evidence for this is not subtle:

The Harness Gap

Hashline

6.7% → 68.3%

Changing only the edit format. Same model. Same weights. Only the harness changed.

Claude Opus

42% → 78%

CORE-Agent to Claude Code. A 36-point gain (Sayash Kapoor, HAL benchmark). Same model.

deepagents

52.8% → 66.5%

LangChain's deepagents-cli. No model change. Harness-only improvement.

Changing only the edit format lifted one model from 6.7% to 68.3%. **The weights didn't change. Only the harness did.** Claude Opus switching from a generic agent scaffold to Claude Code — a purpose-built harness — jumped 36 points on the same benchmark. LangChain's deepagents-cli closed 14 points without touching the model.

These aren't incremental gains. These are the difference between "barely functional" and "production-grade." The model provides raw capability. The harness determines how much of that capability actually gets expressed.

The model is the CPU. The harness is the OS. And the next transition is an OS that upgrades itself.

## Harness Is the Product

Anthropic published two detailed reports on harness design for agentic coding (November 2025, March 2026). The core architecture: an initializer agent scopes the work, a coding agent executes, a feature list anchors both to prevent drift. The insight that runs through both papers: _"Every component in a harness encodes an assumption about what the model can't do on its own, and those assumptions are worth stress testing."_ Rick Hightower put it more directly: "The model is the CPU, the harness is the OS."

MetaHarness (Stanford, March 2026) quantified the stakes: **a 6x performance gap from harness changes alone**, with model weights held constant. Not 6%. 6x. The difference between a useful system and a broken one is not the model — it's everything around it.

Context engineering helps the model think well. Harness engineering prevents the whole system from drifting off-course. Context is the information. The harness is the process — what phases exist, what gates must pass, what gets remembered, what gets discarded, what triggers the next action.

Our harness is purpose-built for **AI-native venture investing**. Not a tool that helps an investor. The entire system: specialist agents handling research, communications, strategy, data — orchestrated alongside a human — with deep understanding of the data model, action space, and stakeholder space — looping through them with high intelligence. The harness includes both the intelligence system AND the autonomous build system that evolves it. They aren't separate things. Five major rewrites to the build system. Hundreds of sprints. The rewrites weren't to the product — they were to the machinery itself, each one getting closer to the principle of self-evolving systems.

The harness is the totality — model + context + orchestration + the system that evolves all three.

There is no "product team" building a "product." There is a harness — where building and being built are the same process.

## What the Harness Builds

### The Optimization Problem

The system answers one question: **"What's Next?"** — optimizing across the full stakeholder and action space to maximize investment returns.

The stakeholder space: 1,000+ companies across portfolio, pipeline, and broader network. 1,000+ people — founders, co-investors, LPs, advisors, operators, and more. The action space splits in two: _stakeholder actions_ (meetings, calls, emails, intros, follow-ups) and _intelligence actions_ (research, analysis, content consumption, thesis refinement). Both generate new actions in a continuous loop. A meeting produces intel that triggers research that surfaces a connection that demands an intro.

1,000+

Companies across portfolio, pipeline, and network

1,000+

People across founders, investors, operators, advisors

5

Priority buckets governing time allocation

2x

Estimated allocation improvement: ~30-40% optimal → ~70-80%

Five priority buckets govern allocation: **chase new cap tables** (get into the best deals), **deepen existing cap tables** (board work, follow-ons, portfolio support), **build new relationships** (expand the top of funnel), **deepen existing relationships** (the trust compounds that drive dealflow), and **evolve theses** (stay ahead of markets). Without the system, a solo investor runs at maybe 30–40% optimal allocation — too much time on whoever pinged last, too many obligations falling through cracks. With it: 70–80%. That delta is the product.

### Six Mental Models

The reasoning layer isn't freeform. Every decision — what to prioritize, what to defer, what to investigate — runs through six mental models borrowed from quantitative investing:

#### Expected Value

Every action evaluated by (probability of outcome × value of outcome). High-probability low-value actions are inferior to moderate-probability high-value ones.

#### Base Rate Anchoring

Before getting excited about a signal, anchor on: what percentage of companies at this stage succeed? What's the base rate for this type of action paying off?

#### Sunk Cost Avoidance

Past investment of time or attention in a thesis, company, or relationship should never factor into future allocation. Only forward-looking EV matters.

#### Bayesian Updating

New evidence updates conviction proportional to its likelihood ratio. A strong contra signal from a Tier 1 source shifts more than a confirming signal from a Tier 3 source.

#### Survivorship Denominator

Don't just study successful outcomes — examine the full population. How many companies with similar signals didn't succeed? Prevents false pattern detection.

#### Quarter-Kelly Sizing

Don't go all-in on the highest-EV action. Allocate attention using quarter-Kelly: bet 25% of what the formula suggests. Margin for model error. Diversification across the action space.

_Certainty is the bug._ Hold opinions loosely, update constantly. The preference store — every accept, dismiss, and piece of feedback — is the mechanism that makes the Bayesian loop real.

**Intelligence = cross-source pattern matching synthesized into narratives with actionable options. Not data display.** A table showing "Mohit Gupta | Last contact: 14 days | Status: Overdue" is a database view. A card that says "Mohit was enthusiastic in your March 15 meeting, but WhatsApp messages dropped to zero since March 22. His company's health is Yellow with a board meeting next week. This silence likely means something changed" — that's intelligence.

### Four Agents, Four Intelligence Surfaces

The cascade: information flows to ENIAC, interactions flow to Cindy, all data flows to Datum, all intelligence converges in Megamind ↔ Aakash via WebFront.

##### Cindy

Communications

Obligation tracking, relationship pulse, draft messages, meeting prep. Synthesizes WhatsApp, email, Granola transcripts.

Morning briefing, obligation cards, comm priority queue, async drafts

##### ENIAC

Research

Thesis health, evidence synthesis, company research, competitive matrices. Bayesian prior updating, source quality assessment.

Research briefs, thesis health, research queue, temporal intelligence, key questions tracker

##### Megamind

Strategy

Portfolio-level synthesis, contradiction detection, cross-thesis patterns, strategic memos. Adversarial analysis across investment lenses.

Strategic synthesis, adversarial analysis, portfolio attention flags, conviction assessments

##### Datum

Data

Entity resolution, enrichment pipelines, relationship mapping, company health scoring.

Entity health maps, enrichment signals, data quality reports

### The Self-Evolving Build Architecture

The four intelligence agents don't operate alone. Three platform machines complete the system — and together, they form the self-evolving architecture that makes the harness a living product. Agent machines produce structured intelligence. Platform machines provide the infrastructure to render, deploy, and experiment on that intelligence. The Innovation Lab runs experiments that graduate into production when the user approves — the harness literally evolving its own UX.

Provider ↔ Consumer Architecture

Provider

WebFront

Render catalog, shared UI components, graduation pipeline. Interprets JSON render specs into React.

Core

4 Agents

Cindy, ENIAC, Megamind, Datum. Produce JSON render specs + agent_outputs. Consume platform resources.

Provider

Infra-orch

Droplet health, deploy chain, Supabase schema, cron jobs, systemd services.

↓ experiments ↑ graduation

Evolution

Innovation Lab

Prototypes new card types, interaction patterns, intelligence surfaces. Deploys to /labs. User verdicts: Graduate / Iterate / Kill.

WebFront maintains a **JSON render catalog** — a typed vocabulary of UI components. Agents write render specs describing both data and presentation. WebFront interprets specs into React components via a single generic renderer. Innovation Lab prototypes new card types, interaction patterns, and intelligence surfaces on the `/labs` tab. When an experiment works, the user graduates it and WebFront absorbs it into the catalog. This is microservices that build themselves — each machine evolving its own domain while the whole system evolves the product.

### The Intelligence Standard

What does "good" look like? **Intelligence = cross-source pattern matching synthesized into narratives with actionable options. Not data display.** Every card should feel like an EA prepared a briefing, not a database query rendered. Here's the standard:

Actions

Pulse

Chat

Act Now 27d overdue

The One Thing

Aditi Kothari is building Potpie to solve AI code review at scale — and you owe her a crucial intro

AK

Aditi Kothari

via WhatsApp · 157 messages

You committed to connecting her with Rahul Chari for her Series A advisory board. 32 days overdue. She traveled to SF specifically for fundraise meetings; your silence signals unreliability in a relationship built on high-frequency trust.

Do This

The advisory board window closes as she progresses in her round.

That card wasn't hand-coded. Cindy reasoned about obligations, relationship history, communication patterns across WhatsApp, email, and meetings. Then she wrote a **JSON render spec** — a structured document that describes both the data and how to present it:

```
{
  "root": "briefing",
  "elements": {
    "briefing": {
      "type": "Stack", "props": { "gap": 12 },
      "children": ["one-thing", "obligations"]
    },
    "one-thing": {
      "type": "AlertCard",
      "props": {
        "title": "Call VV re: board prep",
        "urgency": "critical",
        "body": "Promised Friday. Board Monday."
      }
    },
    "obligations": {
      "type": "Card",
      "props": { "title": "Overdue (4)" },
      "repeat": { "statePath": "/overdue" },
      "children": ["obl-item"]
    }
  }
}
```

The agent decides WHAT to show and HOW to show it. WebFront just renders. If Cindy invents a new card type next sprint, zero frontend code changes — as long as the component exists in the catalog.

### The Innovation Lab

When an agent needs something from a platform machine, it files a **cross-request**. When Innovation Lab creates a new card pattern, it deploys to `/labs` for user evaluation. The user sees both the current version and the prototype side by side. Graduate, Iterate, or Kill.

Labs

Innovation experiments — review, graduate, iterate

Review 52

Graduated 6

Killed 0

EXPERIMENT E1-S18 Cross-Source Intelligence Narrative Card

Hypothesis: Cards synthesizing signals from 3+ agents produce better decisions than single-agent cards

Current

ENIAC · Research Brief

Potpie — AI Code Review

Series A fundraising. TAM: $2.8B code review market. Key risk: incumbent (GitHub Copilot) expansion. Founder: Aditi Kothari, ex-Google. Traction: 340 enterprise pilots.

Single source. No cross-reference. No action.

Prototype

CINDY ENIAC MEGAMIND

Potpie is fundraising now, you owe Aditi an intro, and the thesis fits

Aditi's Series A is live (ENIAC: 340 enterprise pilots, $2.8B TAM). You promised Rahul Chari intro 32d ago (Cindy: overdue obligation, WhatsApp). The DevTools thesis predicts code-review unbundling from IDEs (Megamind: conviction 7/10, timing window 6 months).

Recommended

Send intro to Rahul this week. If positive signal, schedule portfolio deep-dive before her SF meetings end.

3 sources. Narrative. Action. Timeline.

Verdict

Graduate Iterate Kill 2 reviewers · avg time: 14s

52 experiments reviewed. 6 graduated to production. 0 killed outright — the lab iterates fast enough that bad ideas get refined before they're discarded. This is the Innovation Lab running its own evolution loop inside the harness.

The harness doesn't just produce intelligence. It produces the UX that delivers intelligence, the experiments that improve that UX, and the infrastructure that serves it all. The product IS the harness.

## How the Harness Runs

Seven machines. Six-phase sprints. Running in parallel, continuously. Each sprint takes about an hour. The phases aren't suggestions — they're enforced by shell hooks that intercept every agent invocation.

One Sprint, Six Phases

1

PLAN

Product analyst. Reads feedback, compound knowledge, VERIFY failures.

2

SPEC

Eng. manager. Reads codebase, writes specs with test conditions.

3

BUILD

Engineer. Implements against spec, runs agent, produces outputs.

4

REVIEW

Independent code reviewer. Does not trust BUILD's self-check.

5

VERIFY

Adversarial QA. Blind to spec. Tests against the product vision.

6

SYNC

Extracts learnings, creates PRs, communicates cross-machine.

Each phase has an **identity** — a cognitive mode enforced by the system. PLAN thinks like a PM, reading feedback and compound knowledge. SPEC thinks like an EM, reading the actual codebase before writing specifications. BUILD executes. REVIEW checks independently. VERIFY is adversarial — intentionally blind to the spec, generating its own test plan from the product vision. SYNC learns and ships.

**The question isn't "can the agent follow instructions?" It's "what happens when it doesn't?"** If the answer is "the system breaks silently," you have a demo. If the answer is "a hook catches it and redirects," you have a product.

### The Spec as Anchor

A single unit of work — `REQ-{MACHINE}-{NNN}` — flows through every phase. SPEC creates it with test conditions. BUILD implements and records results. REVIEW checks independently. VERIFY scores against the vision. SYNC decides whether to ship or carry forward.

REQ-ENIAC-042 · Tracking through phases

SPEC

Thesis health must include evidence_momentum score

BUILD

TC_PASS · Field present, formula matches spec

REVIEW

REVIEW_PASS · Correct derivation, no regressions

VERIFY

7/10 · Field renders but label unclear at mobile

SYNC

ADDRESSED · PR created, branch merged

### Hooks, Not Instructions

One shell script — `pre-agent.sh` — runs on every agent invocation. It reads the manifest, determines the current phase, injects the right prompt, and blocks progression until gates pass.

```
# Phase determination: first incomplete phase wins
if [ "$PLAN_STATUS" != "COMPLETE" ]; then PHASE="PLAN"
elif [ "$SPEC_STATUS" != "COMPLETE" ]; then PHASE="SPEC-WRITE"
elif [ "$BUILD_STATUS" != "COMPLETE" ]; then PHASE="BUILD-IMPLEMENT"
elif [ "$REVIEW_STATUS" != "COMPLETE" ]; then PHASE="BUILD-REVIEW"
elif [ "$VERIFY_STATUS" != "COMPLETE" ]; then PHASE="VERIFY"
elif [ "$SYNC_STATUS" != "COMPLETE" ]; then PHASE="SYNC"
fi

# Route to specialist prompt
case "$MACHINE_ID" in
  cindy|datum|eniac|megamind) DIR="agent" ;;
  webfront) DIR="webfront" ;;
  innovation) DIR="innovation" ;;
esac
PROMPT="$DIR/${PHASE_MAP[$PHASE]}.md"
```

Agents never touch the manifest. Only hooks write control state. The intelligence layer and the control layer are architecturally separated — agents can't skip phases, inflate progress, or modify the system that governs them.

### Cross-Machine Communication

**ENIAC**Needs entity enrichment

⟶ cross-request

**Datum**Picks up in next PLAN

**Innovation**Graduates experiment

⟶ cross-request

**WebFront**Implements in catalog

SYNC publishes what was built, what changed, and what other machines need. Next sprint's PLAN reads it. No meetings. No standups. Structured async communication enforced by the sprint protocol. Every 3rd sprint is an **improvement sprint** — the machine improves its own harness rather than building features. Process without learning is expensive repetition, not evolution.

Agents bring intelligence. Hooks bring discipline. The system decides what phase each agent is in, what information it receives, and what gates it must pass. That's how you get deterministic control over evolution.

## Observing the Harness

A self-evolving system you can't observe is a system you can't steer. The harness has a full observability layer — from terminal dashboards to web-based eval interfaces.

### Sprint Observatory TUI

The Diamond Pattern runs a Textual-based terminal dashboard (`diamond_tui.py`) with three drill-down levels: Overview, Machine Detail, Phase Detail. Here's what the operator sees mid-session:

Sprint Observatory

SESSION S24 · 7 machines · 42m elapsed · q:quit r:refresh d:detail

Overview

Machine Detail

Phase Detail

| Machine | Phase | Status | Duration | Tools | Output | Gates | Grade |
| --- | --- | --- | --- | --- | --- | --- | --- |
| cindy | VERIFY | running | 38m | 147 | 24.1k | 0 fail | A |
| eniac | BUILD | running | 31m | 89 | 18.7k | 0 fail | B |
| megamind | SYNC | done | 44m | 203 | 31.2k | 0 fail | A |
| datum | REVIEW | running | 29m | 56 | 9.4k | 1 fail | C |
| webfront | SPEC | blocked | 12m | 23 | 5.1k | 2 fail | D |
| infra-orch | BUILD | running | 26m | 71 | 12.8k | 0 fail | B |
| innovation | SYNC | done | 41m | 118 | 22.3k | 0 fail | A |

PLAN

SPEC

BUILD

REVIEW

VERIFY

SYNC

14:38:21 cindy VERIFY: navigating to /cindy/actions, screenshot captured

14:38:19 webfront SPEC: gate fail — missing render catalog entry for TimelineCard

14:38:14 megamind SYNC: compound store updated, 3 learnings extracted

14:38:11 eniac BUILD: thesis_health.ts — evidence_momentum field added

14:37:58 datum REVIEW: gate fail — entity resolution query returns stale cache

14:37:42 innovation SYNC: experiment E1-S19 deployed to /labs, awaiting review

### Session Eval

After every session, a structured eval interface surfaces exactly what happened. Per-machine scoring across multiple dimensions, anchored to a vision lens that defines what "good" means:

2026-04-07 · 1 sprint · 7 machines · 33 questions

Vision Lens

Intelligence = cross-source pattern matching synthesized into narratives with actionable options. Cards should tell stories. Every card should feel like an EA prepared a briefing, not a database query rendered.

Cindy

5/10

ENIAC

3/10

Megamind

4/10

WebFront

6/10

### The Calibration Gap

VERIFY scores its own output 8/10. The human scores it 2.5/10. That delta — **5+ points** — is the most important metric in the system. Every eval session narrows it.

```
"Last 3 sessions: user scored intelligence 3/10.
 VERIFY scored 8/10. Delta: 5 points.
 Direction: you are too generous on intelligence.
 A 5/10 means 'technically correct but not intelligent.'
 A 9/10 means 'user would say: this is what the system
 is for.'"
```

Agents score their work 8/10. Humans score it 2.5/10. That gap is the entire problem — and closing it is the entire game.

## How the Harness Absorbs Knowledge

A system that only learns from its own output is limited by its own imagination. The frontier isn't better models. It's better cognitive architecture around the models we have.

The harness has two skills for absorbing external knowledge with structured judgment.

### Learn-From

**Learn-from** reads an external source — a git repo, arxiv paper, blog post — and produces two layers. Layer 1: understand the source on its own terms. Layer 2: map it to our system — what applies, what doesn't, what needs adaptation. When Karpathy published [autoresearch](https://github.com/karpathy/autoresearch), learn-from produced both layers. When a paper on Agentic Critical Training dropped, learn-from identified that our own learning loop had a survivorship bias gap the paper's contrastive learning method could fix.

### Research Synthesis

**Research synthesis** takes multiple inputs and forces genuine integration — not a summary, but a cross-referenced convergence map. When we needed the eval pipeline, synthesis consumed 16 sources and mapped every claim against every source:

Distill, don't dump raw scores

Agree

Agree

Qualify

Qualify

Silent

Agree

Context injection > fine-tuning

Agree

Agree

Agree

Silent

Contra

Agree

Then three competing hypotheses, each genuinely different. Pre-mortems for each. Then synthesis: the recommendation that no single source contains.

### What Gets Rejected

#### DSPy Auto-Optimization

Our prompts are 100+ line multi-skill documents. DSPy optimizes simple signatures. And it needs hundreds of examples; we have ~10 sessions.

#### PULSE ML Prediction

Trains a model to predict satisfaction. Requires hundreds of labeled sessions we don't have. Solves a scaling problem that isn't our bottleneck.

#### Merkle DAG Storage

Content-addressable artifact provenance. Production-grade. Massive overkill for 7 machines. Session ID + git commit hash is enough.

### What Gets Absorbed: The Graduation Path

When absorbed knowledge manifests, it becomes an experiment. Innovation Lab prototypes it. The user evaluates. Graduate, Iterate, or Kill. The cross-source intelligence narrative card — synthesizing Cindy, ENIAC, and Megamind signals into a single story — entered through research synthesis, got prototyped, got evaluated, and graduated. Knowledge absorption made concrete.

A self-evolving system that adopts everything it encounters evolves in random directions. One that filters through structured judgment evolves toward its purpose.

## How the Harness Develops Judgment

The purpose of an eval isn't to measure quality. It's to produce a signal specific enough that the system knows what to change. Three learning loops, each at a different timescale.

Loop 1: Sprint → Sprint (failure recovery)

Sprint N

VERIFY Fails

Scores 3/10. Records what went wrong, what must not repeat.

Sprint N+1

PLAN Inherits

Failed criteria arrive as high-priority input — same tier as user feedback.

Sprint N+1

SPEC Rewrites

Different approach, not minor tweaks. Failed twice? Question the criterion itself.

Loop 2: Across Sprints (compound learning)

VERIFY

Extract

2–5 structured learnings: patterns, intent gaps, calibration signals.

SYNC

Distill

Compact memories → compound store. Sprint entries, recurring patterns, shared findings.

Next PLAN

Inject

Hook reads compound store, injects into PLAN. Agent must acknowledge: ADDRESSING or DEFERRING.

Loop 3: Across Sessions (eval distillation)

Session End

Human Scores

Per-machine, per-dimension. Intelligence, narrative, actionability, UX, delta.

Distillation

Compute Gap

"When [situation], do [action] because [reason from eval evidence]."

Next Session

Calibrate

Memories + calibration anchors flow into compound store. Gap narrows.

### The 7-Lens Scoring Rubric

When we found [Nyk's Council of High Intelligence](https://github.com/0xNyk/council-of-high-intelligence) — 11 philosophical thinkers in structured adversarial deliberation — research synthesis flagged the protocol as strong but the domain as wrong. 11 generic thinkers became 7 investment lenses. 6 polarity pairs became 4. Each lens has a declared blind spot and a structural adversary:

| Tension | Lens A | Lens B | What It Forces |
| --- | --- | --- | --- |
| **Contrarian ↔ Pattern Matcher** | "Everyone is wrong" | "This happened before" | Explain why THIS time is different |
| **First Principles ↔ Network Thinker** | Structural truth | Messy human reality | Sound thesis + misaligned incentives = failure |
| **Risk Architect ↔ Timing Strategist** | "This could fail" | "The window is now" | Risk vs opportunity cost of inaction |
| **Founder Lens ↔ First Principles** | "This team executes" | "The logic is flawed" | Great founders can't save broken markets |

3 rounds: independent analysis, forced cross-examination, crystallization. Mandatory minority report, even in consensus. Every part of the harness contributed — research synthesis filtered it, learn-from mapped it, the sprint system built it, the eval system scores it.

The harness develops judgment the same way a junior analyst does — not by being told "do better," but by seeing the gap between their assessment and their manager's, with the reason attached.

## Where the Harness Goes

The harness already controls its own evolution. But improvement sprints work from _summaries_ of what went wrong — not the raw execution traces. The compound store distills "scored 3/10" but loses the actual sequence of tool calls that produced the 3/10.

Three independent research threads are converging on one conclusion:

6x

Performance gap from harness changes alone (MetaHarness, Stanford)

6%+

Trace reflection over RL with scalar rewards (GEPA)

0.7%

Fleet-wide compute recovery at Google (AlphaEvolve)

~70%

Of MetaHarness architecture already in our system

**The scaffolding around models is now the primary optimization target.** The method: let a reasoning agent inspect raw execution traces and propose what to change.

Three concrete next steps:

#### Raw Trace Injection

Improvement sprints get the last 3 JSONL transcripts. The agent reads selectively, forms causal hypotheses: "Sprint 7 failed because BUILD never called Supabase — trace shows hardcoded data."

#### Candidate Branching

Improvement sprints propose 2–3 variants on separate git worktree branches. Evaluate each against representative tasks. Deploy the winner.

#### Eval Task Sets

5–10 representative tasks per machine. Evaluate improvement proposals before deploying them. The "search set" that makes comparison meaningful.

```
# Today
feedback → distilled summaries → improvement sprint
  → single candidate → deploy

# Next
feedback + VERIFY scores + raw JSONL transcripts
  → causal hypotheses from traces
    → 2-3 candidates on worktree branches
      → evaluate against task set → deploy winner
```

The harness is early. The calibration gap is real. But each session narrows it. Each rewrite makes the build system more capable. Each research synthesis run makes the harness smarter about what to adopt and what to reject. The companies shipping the best agents right now are not winning on model selection. They are winning by relentlessly simplifying the harness.

The real product isn't the intelligence system. It isn't the build system. It's the harness — the unified system where building and being built are the same process. That's the fourth transition completing itself.
