---
tags:
  - knowledge
title: "Sentinel — Project Context"
company: personal
topics:
  - sentinel
  - ios
  - privacy
  - ad-blocking
source: ""
created: 2026-04-17
---

# Sentinel — Project Context

Distilled orientation for the distillery. Expand this file as the PRD matures — current content is a minimal pitch-level seed.

## The pitch

Premium iOS ad blocker built on Apple's **NEURLFilter API** (iOS 26+). System-wide URL-level ad and tracker blocking that runs **alongside an active VPN** without occupying the VPN slot. That VPN-coexistence is the core differentiator.

## The problem it solves

iOS users who want both a VPN and an ad blocker currently have to choose — most ad blockers occupy the system VPN slot (Personal VPN / NetworkExtension tunnel), which disables their real VPN. Sentinel uses NEURLFilter instead of a tunneling approach, so it can block ads and trackers while a real VPN (Mullvad, ProtonVPN, NordVPN, etc.) stays connected.

## Who it's for

iOS 26+ users who run a real VPN and refuse to turn it off to use an ad blocker. Privacy-first power users, journalists, and anyone who currently runs one tool at a time because the two categories are architecturally incompatible.

## Why this exists (market gap)

Existing iOS ad blockers — 1Blocker, AdGuard, Wipr, etc. — are either Safari content blockers (browser-only, no system-wide coverage) or VPN-based (steal the VPN slot). NEURLFilter is the first Apple API that lets a third-party app block system-wide URLs without acting as a VPN. Being first on the API with a polished app is the window.

## Core experience

_TBD — expand once PRD is drafted._ At minimum: enable filter → system-wide URL blocking active across all apps → real VPN continues uninterrupted.

## Design principles

_TBD._ Expected anchors based on Robert's stack on Sweep: iOS 26-native Liquid Glass, on-device, zero third-party analytics, honest positioning, one-time pricing (pending decision).

## Monetization

_TBD._

## Target

_TBD._

## Stack (brief)

Swift / SwiftUI / iOS 26+. **NEURLFilter** (NetworkExtension framework, iOS 26 API) is the core technology.

## Status

Pre-MVP. See [[../initiatives/sentinel|Ship Sentinel Ad Blocker iOS App]].

## Writing about this project

**Technical lane** — NEURLFilter API deep-dives, NetworkExtension framework internals, comparisons to content-blocker and VPN approaches, iOS 26 API firsts: technical voice. This is a strong technical-writing vein — the API is new, under-documented, and most iOS devs haven't touched it.

**Business / indie-dev lane** — differentiation against 1Blocker/AdGuard/Wipr, positioning "the ad blocker that doesn't steal your VPN slot," launch timing advantages of being early on a new Apple API: indie-business voice.

**No theological framing** on Sentinel posts. Like Sweep, this is a consumer privacy tool; the faith angle is not in the product. Intersection essays about surveillance, attention, and technology ethics belong in the long-form intersection category, not on top of Sentinel launch content.
