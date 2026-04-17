---
tags:
  - knowledge
title: "Sweep — Project Context"
company: personal
topics:
  - sweep
  - ios
  - storage
  - privacy
source: ""
created: 2026-04-17
---

# Sweep — Project Context

Distilled orientation for the distillery. Full PRD (v2.0, 2026-04-16) is the source of truth for specs; this file is for loading project shape quickly when drafting content.

## The pitch

The honest iOS photo cleaner. Pay $14.99 once, clean your phone forever. No subscriptions, no analytics, no tracking. Liquid Glass native, iOS 26-only.

## The problem it solves

iPhones fill up with duplicates, screenshots, and oversized videos. Every existing cleaner app is a predatory subscription trap — Cleanup charges $6.99/week, CleanMyPhone $24.99/yr, and all of them ship stale pre-Liquid-Glass UI with third-party analytics SDKs baked in. Users want to clean their phone without being exploited.

## Who it's for

iOS 26 users (iPhone-only in 1.0) who are storage-constrained, privacy-conscious, and allergic to subscription traps. Sub-segment: A17 Pro+ owners who unlock semantic search ("delete all receipts") via Apple Intelligence.

## Why this exists (market gap)

Three structural moats incumbents can't close:

1. **Lifetime pricing** — MacPaw's Setapp anchor forbids one-time IAP.
2. **iOS 26-only design** — incumbents support iOS 13+, can't adopt Liquid Glass cleanly.
3. **Zero third-party analytics** — incumbents have entrenched PostHog/Firebase stacks.

Plus a distinctive "Heavy Hitters" signature view (top 50 biggest files across photos/videos/Live Photos) that no competitor ships.

## Core experience (MVP)

1. **Heavy Hitters** — top 50 biggest files, rendered in <2s from `PHAsset` metadata.
2. **Duplicate / similar photo grouping** — pHash-based exact dupes (green), similar (yellow), ambiguous (gray).
3. **Quality cleanup** — blurred (Laplacian variance), over/under-exposed, screenshots categorized by on-device Visual Intelligence.
4. **Video compression** — in-place HEVC (~70% reduction), resumable, original to Recently Deleted.
5. **Live Photo conversion** — strip .mov companion, reclaim ~3 MB each.
6. **Apple Intelligence semantic search** (A17 Pro+) — natural-language photo queries, one-tap bulk delete.
7. **Cleanup history + undo** — session log with 30-day Recently Deleted restore.
8. **Home Screen widget** — storage donut + "X GB of clutter found."

## Design principles

- **Liquid Glass everywhere.** No multi-iOS design system. iOS 26 is the floor.
- **Honesty floor.** No quantitative claims ("40% freed," "12 GB average") in marketing or UI. Every promise must survive App Review on a real library.
- **On-device only.** No uploads, no analytics, no third-party SDKs beyond RevenueCat (IAP) and Superwall (paywall A/B). Privacy nutrition label declares only "Purchase History."
- **Deep modules, testable in isolation.** PerceptualHasher, DuplicateGrouper, PhotoAnalyzer etc. are pure interfaces with fixture-driven tests.
- **Progressive scan.** Instant Heavy Hitters from metadata; background duplicate/quality scan; Apple Intelligence embeddings on capable hardware.
- **No pre-scan ceremony.** Onboarding is 2 screens + permission; app lands on Heavy Hitters with a non-blocking scan pill.

## Monetization

- **One SKU:** $14.99 non-consumable IAP, lifetime.
- **Free tier:** first full sweep (any category) is free, no credit card. Paywall fires on second deletion action.
- **No subscriptions, ever.** This is a positioning commitment, not a product decision.
- **Restore via Apple ID** — no account creation.

## Target

- 25K downloads month 1 → 600K month 12.
- 2K → 60K paid users over 12 months.
- Cumulative net revenue ~$629K at 12 months.
- North Star: 10% free-to-paid conversion on First-Sweep completers.

## Stack (brief)

Swift 5.9+ / SwiftUI / iOS 26+ / MVVM with `@Observable` / SwiftData / async-await. Vision for photo analysis, Apple Intelligence `AIImageEmbedding` for semantic search, AVFoundation for HEVC compression. RevenueCat for IAP, Superwall for paywall. Crash reporting via MetricKit + OSLog only — no Sentry, no Firebase.

## Status

Pre-build. PRD v2.0 approved 2026-04-16. Ship target July 7, 2026. 6-week waitlist campaign at `sweep.app` running in parallel with build. See [[../initiatives/sweep|Finish Building Sweep iOS App]].

## Writing about this project

**Technical lane** — PhotoKit / Vision / Apple Intelligence integration, Liquid Glass design implementation, SwiftData-backed scan architecture, pHash and duplicate grouping algorithms, App Store Guideline 4.3 navigation, testing deep modules in isolation: technical voice.

**Business / indie-dev lane** — lifetime pricing strategy, structural moats against subscription incumbents, honest marketing as positioning, waitlist + ASA launch playbook, zero-analytics as a feature: indie-business voice.

**Do not mix theology into Sweep posts.** Sweep has no faith angle. It is a consumer productivity app that happens to be built by a Reformed Christian. Intersection essays about honest software, anti-exploitative pricing, or the ethics of consumer apps belong in the long-form intersection category — not in Sweep launch posts.

The load-bearing story for Sweep is the anti-subscription-trap stance — Robert is building the thing he wants to recommend to family members who keep getting burned by weekly billing scams. That frame sits under launch content, not on top of it.
