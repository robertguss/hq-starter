---
tags:
  - library
title: "Introduction | Camoufox"
url: "https://camoufox.com/"
company: [personal]
topics: []
created: 2026-03-29
source_type: raindrop
raindrop_id: 1665107928
source_domain: "camoufox.com"
source_type_raindrop: link
collection: "AI Repos & Open Source"
collection_id: 69284315
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

Invisible to anti-bot systems 🎭

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: Introduction | Camoufox

URL Source: https://camoufox.com/

Markdown Content:
## Introduction

### An open source anti-detect browser with robust fingerprint injection. 🦊

[![Image 1: daijro%2Fcamoufox | Trendshift](https://camoufox.com/static/trendshift.svg)](https://trendshift.io/repositories/12224)

* * *

After some time away, I've decided to step down from primary maintainer of Camoufox. The project is in great hands with the team at [Clover Labs](https://cloverlabs.ai/), and you can expect new updates coming soon. I'll still be passively contributing and helping with development. Thanks to everyone who has supported Camoufox along the way. ❤️

**Warning for new 2026 releases!**

 Camoufox is under active development to get back to its original performance. The latest releases are highly experimental (expect breaking changes). Preview releases are available, but are not stable or suitable for production use.

* * *

## Features

*   **Invisible to anti-bot systems**🎭
    *   See the [stealth page](https://camoufox.com/stealth/) for more details

*   **Fingerprint injection & rotation (without JS injection!)**
    *   All navigator properties (device, OS, hardware, browser, etc.) 
    *   Screen size, resolution, window, & viewport properties 
    *   Geolocation, timezone, locale, & Intl spoofing 
    *   WebRTC IP spoofing at the protocol level 
    *   Voices, speech playback rate, etc. 
    *   And much, much more!

*   **Anti Graphical fingerprinting**
    *   WebGL parameters, supported extensions, context attributes, & shader precision formats 
    *   Font spoofing & anti-fingerprinting 

*   **Quality of life features**
    *   Human-like mouse movement 🖱️
    *   Blocks & circumvents ads 🛡️
    *   No CSS animations 💨

*   Debloated & optimized for memory efficiency ⚡
*   [PyPi package](https://pypi.org/project/camoufox/) for updates & auto fingerprint injection 📦
*   Stays up to date with the latest Firefox version 🕓

Get started

python/

* * *

## Design and Implementation

The goal of Camoufox is to provide a robust, undetectable anti-fingerprinting solution that blends in with regular user traffic.

1. Fingerprinting Protection

Many modern 'hardened' browsers and extensions often become counterproductive by making users more distinguishable through detectable JavaScript tampering, blocking certain web APIs, and using static device information. This, ironically, makes the user stand out through your unique browser configuration, making you more trackable and in many cases flagged by anti-bot systems for unusual traffic.

Camoufox solves this through fingerprint rotation at a lower level by modifying device information in the C++ implementation instead of injecting JavaScript, which leaves a trail. Built on Firefox and research from the Tor project, Arkenfox, and CreepJS, Camoufox hopes to take a new approach in avoiding tracking methods to provide robust, undetectable anti-fingerprinting.

2. Crowdblending

A design goal of Camoufox is to blend in with real world traffic. It must behave like a normal user and avoid all statistical fingerprinting, meaning there should _not_ be thousands of requests using the same device information on a large scale.

To achieve this, Camoufox uses [BrowserForge](https://github.com/daijro/browserforge) to rotate device information such as the screen, OS, and hardware to mimic the statistical distribution of device characteristics in real-world traffic. Additionally, Camoufox uses a natural mouse movement algorithm to behave like a normal user.

3. Stealth

Finally, Camoufox should avoid all bot detection, of any kind, by any means. It should not inject any JavaScript into the page or manipulate the main world's DOM in any way. All of Juggler's internal Page Agent Javascript is ran in a sandboxed world. This makes it nearly impossible for a page to detect the presence of Playwright.

Why Firefox and not Chromium?

Camoufox is built on top of Firefox instead of Chromium for these main reasons:

1.   Chrome is bundled with certain features that Chromium does not have. Anti-bot providers can detect if you are using Chromium rather than Chrome. Since Chrome is closed source, patching Chrome is significantly more difficult.
2.   CDP is more widely used and known, so it's a more common target for bot detection
3.   Juggler operates on a lower level than CDP, making it less prone to JS leaks.
4.   Firefox is more ideal for fingerprint rotation. More research has been made on Firefox for fingerprinting resistance than on Chromium.

Is Camoufox open source?

As of v146.0.1-beta.25 (January 2026), **all of Camoufox's source is publicly avaliable**. While some future patches may be closed source, the open sourced code will always remain buildable. However, the official GitHub releases for v135.0.1-beta.24 and lower do have a closed source Canvas patch. You can still build it yourself without the patch.

If you'd like to build Camoufox yourself, see the [build guide](https://camoufox.com/development/buildcli/).
