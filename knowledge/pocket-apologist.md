---
tags:
  - knowledge
title: "Pocket Apologist — Project Context"
company: personal
topics:
  - pocket-apologist
  - ios
  - apologetics
  - ai
source: ""
created: 2026-04-17
---

# Pocket Apologist — Project Context

Distilled orientation for the distillery. Full PRD (v1.0, 2026-03-03) is the source of truth for specs; this file is for loading project shape quickly when drafting content.

## The pitch

"Duolingo for evangelism." iOS app that equips Christians to practice and defend their faith through AI-powered conversation roleplay, real-time objection answers, and Duolingo-style daily skill-building.

## The problem it solves

98% of evangelical Christians don't evangelize despite believing it's core to their faith. The #1 barrier is fear — of rejection, of saying the wrong thing, of not having answers. Pocket Apologist lets users practice hard conversations in a safe environment, build confidence progressively, and access instant answers mid-conversation.

## Who it's for

- **Anxious Andrew** (28-35) — young Christian with non-believing friends; reads apologetics books but freezes in real conversations. Wants practice in a low-stakes environment.
- **Leader Laura** (35-50) — small group leader who wants to equip her group, not just herself. Wants training tools.
- **College Carlos** (18-22) — campus ministry student facing intellectual challenges daily, needs fast conversational answers.

## Why this exists (market gap)

Apologetics + evangelism + AI has **zero commercial competition.** Existing apps are either static content libraries on Subsplash templates (Cross Examined, Got Questions) or digital tracts from 2015 (GodTools). Meanwhile Bible Chat proved AI + faith is a ~$15M/yr business with 25M users. Pocket Apologist sits at the intersection of proven AI demand and an unserved niche.

## Core experience (MVP)

1. **Quick Answers** — curated objections with a quick reply, a deep explanation, conversation tips.
2. **AI Conversation Coach** — roleplay with a skeptic AI at four difficulty levels (friendly → intellectual debater), with post-session feedback.
3. **Daily Training** — Duolingo-style streaks, XP, levels (Novice → Apprentice → Defender → Apologist).
4. **Conversation Toolkit** — mid-conversation assist: type or speak what the other person just said, get an instant glanceable suggestion.
5. **Topic Library** — structured learning paths on major apologetics topics.
6. **Conversation Journal** — log real conversations, reflect, track growth over time.

## Design principles

- **Confidence over content dumps.** Move Christians from _knowing_ apologetics to _using_ it.
- **Curated content + AI augmentation.** AI plays the skeptic, generates feedback, assists live. It does not replace human-curated theology.
- **Theological guardrails.** Nicene Creed-orthodox. Denomination-aware. Orthodox Christian positions on core doctrine; multiple perspectives on secondary issues (baptism, gifts, eschatology).
- **Premium but approachable.** "Premium study app," not "church bulletin." Design avoids churchy visual tropes.
- **Privacy-first.** Journal and conversation data on-device by default; cloud sync opt-in.
- **Minimal religious imagery.** Let the content be the faith element, not crosses and doves.

## Monetization

- **Free:** 1 roleplay/day, 10 objections, first learning path, 3 toolkit assists/day.
- **Premium ($7.99/mo or $59.99/yr):** unlimited practice, all difficulties, full library, detailed feedback.
- **Future:** church/group licenses, content partnerships, live coaching marketplace.

## Target

$10K+/mo MRR within 12 months of launch.

## Stack (brief)

React Native (Expo) + TypeScript. OpenAI or Anthropic API for AI. RevenueCat for subscriptions. Supabase for auth/sync if needed. Offline-first for curated content.

## Status

Pre-MVP, active development. See [[../initiatives/pocket-apologist|Ship Pocket Apologist iOS App]].

## Writing about this project

**Technical lane** — React Native architecture, AI/RAG over theological content, product and roleplay design, retention mechanics: technical voice. No apologetics framing in the body.

**Theological lane** — evangelism barriers, apologetics pedagogy, why Christians freeze, training the church to engage culture: theological voice. No engineering detail.

**Intersection essays** (long-form only) — "a Reformed view of AI coaching on matters of faith," "what happens when the skeptic in the roleplay is an LLM," "using AI to equip the priesthood of all believers." These are their own category; do not graft onto technical posts.

Robert's conversion from atheism at 20 is **load-bearing** for this project's story. He is building the thing he needed when he was the atheist asking hard questions that Christians couldn't answer, and the thing his Christian friends needed when they were failing to answer him. That backstory is not in every piece, but it sits under every piece.
