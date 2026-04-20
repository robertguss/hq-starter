---
tags:
  - library
title: "LiveStore: Local-first data layer for high-performance apps"
url: "https://livestore.dev/?ref=console.dev"
company: [personal]
topics: []
created: 2025-06-05
source_type: raindrop
raindrop_id: 1138919190
source_domain: "livestore.dev"
source_type_raindrop: link
collection: "Web Dev"
collection_id: 69284319
hydrated: true
hydrated_at: 2026-04-20
hydrated_via: defuddle
---
## Excerpt

LiveStore is a state management framework based on SQLite and event-sourcing. It’s designed for demanding applications and based on years of research.

## Raw Content

<!-- Hydrated 2026-04-20 via defuddle -->

try here

[Release v0.3](https://docs.livestore.dev/changelog)

Improved syncing + Node adapter

## with synced SQLite

LiveStore is a next-generation state management framework based on reactive SQLite and git-inspired syncing (via event-sourcing).

[

"Events are the most accurate representation of state. LiveStore gets it right."

![David Khourshid](/images/avatars/david-khourshid.jpg)

David Khourshid

](https://x.com/DavidKPiano/status/1923740185520378365)

## How it works

LiveStore is a fully-featured, client-centric data layer (replacing libraries like Redux, MobX, etc.) with a reactive embedded SQLite database powered by real-time sync (via event-sourcing).

## Demos speak louder than words

LiveStore is designed for demanding & high-performance apps. Let's see it in action.

## Designed and optimized for demanding applications

LiveStore is based on years of research and was developed as the data foundation for uncompromising apps like Overtone.

## What LiveStore does vs. what not

LiveStore was designed to be a principled and flexible data layer. It's design decisions might make it unsuitable for some use cases. Learn more about [when to use LiveStore](https://docs.livestore.dev/evaluation/when-livestore).

### What LiveStore does

- Provide a powerful data foundation for your app.
- Reactive query layer with full SQLite support.
- Adapters for most platforms (web, mobile, server/edge, desktop).
- Flexible data modeling and schema management.
- Support true offline-first workflows.
- Custom merge conflict resolution.
- Sync with a [supported provider](https://docs.livestore.dev/reference/syncing/sync-provider/) or roll your own.
- Helps avoid data vendor lock-in.

### What LiveStore doesn't do

- Not a batteries-included framework (no auth, file upload, etc).
- Not a good fit for some [use cases](https://docs.livestore.dev/evaluation/when-livestore).
- Doesn't sync with your existing database.
- Doesn't provide a hosted service.
- Doesn't scale for unbounded amounts of data.
- Doesn't support peer-to-peer/decentralized syncing.
- Sell your data.

## What others are saying

[![David Khourshid](/images/avatars/david-khourshid.jpg)](https://x.com/DavidKPiano/status/1923740185520378365)

[David Khourshid](https://x.com/DavidKPiano/status/1923740185520378365)

[

Creator of XState

Events are the most accurate representation of state. Everything else is a lossy abstraction. LiveStore gets it right ⚡️

](https://x.com/DavidKPiano/status/1923740185520378365)[![Sunil Pai](/images/avatars/sunil-pai.png)

Sunil Pai

Engineer @Cloudflare

I'm so very excited for @schickling's livestore to drop, really deeply considered and principled way to build great user interfaces.

](https://x.com/threepointone/status/1922935305557942401)![Beto Moedano](https://pbs.twimg.com/profile_images/1905007412450320384/UB7A8k0T_400x400.jpg)

Beto Moedano

Developer Advocate @Expo

@livestoredev + @expo + @CloudflareDev = Local-First app with real-time sync, offline persistence, and smooth performance. 🚀

![Jacob Clausen](https://pbs.twimg.com/profile_images/1808122460820430848/sUSrPA5N_400x400.jpg)

Jacob Clausen

App Developer

There's so much to be excited about with @livestoredev. But what really gets me is the extra mile they've gone with the dev tools. Top-tier stuff that adds serious value. Plus, it's an @expo dev plugin, making it seamless and well integrated. A dream combo for offline-first!

[![Peter Pistorius](/images/avatars/peter-pistorius.jpg)

Peter Pistorius

Co-creator RedwoodSDK

What are you syncing about? Just got a preview of @livestoredev v2 by @schickling: it's next-level.

](https://x.com/appfactory/status/1922660472525857235)![Johannes Schickling](/images/avatars/johannes-schickling.jpg)

Johannes Schickling

Creator of LiveStore

I think LiveStore is pretty cool but I'm biased. However, you should give it a try.

## Additional resources

Check out the following resources to learn more about LiveStore.

### Conference talk

You can learn more about LiveStore in some of our past conference talks.

[Read more](https://docs.livestore.dev/misc/community)

### Office hours

Watch some of the past LiveStore office hours recordings and [join the next one](https://docs.livestore.dev/misc/community).

[Read more](https://docs.livestore.dev/misc/community)

### Riffle essay

In the Riffle essay (+ PhD thesis by [Geoffrey Litt](https://www.geoffreylitt.com/)), we explored the idea of reactive SQLite as a modern state management system.

[Read more](https://riffle.systems)

## The story behind LiveStore

LiveStore was designed and developed as foundation for [Overtone](https://overtone.pro), a next-gen music app. To achieve the high-performance requirements of the app, we needed a state management framework that is able to handle the complex data scenarios of the app which started the [Riffle research project](https://riffle.systems) and later became LiveStore.

![](/images/avatars/johannes-schickling.jpg) <svg class="h-20" width="140" height="114" viewBox="0 0 200 114" fill="none" xmlns="http://www.w3.org/2000/svg"><title>LiveStore</title><path d="M13.6349 8.35748 C10.7054 7.61322 5.65263 4.27942 1.64572 3.045 C-3.06849 1.59267 19.1769 6.01324 31.1353 5.17265 C31.4682 5.14925 31.7931 5.12178 32.1092 5.08998 C34.1867 4.88105 36.2765 3.82337 36.6246 3.45132 C38.56 1.38291 35.577 2.66321 31.1353 5.17265 C25.0813 8.593 16.3176 14.2968 13.6047 16.9169 C11.7603 18.6983 11.5315 21.6833 12.1728 25.4595 C13.4905 33.2185 17.2252 40.9888 21.2077 47.9484 C26.5718 57.3224 32.3857 65.2255 33.3494 69.6492 C34.1334 73.2478 31.9175 77.7799 29.3699 82.2154 C27.4341 85.5858 24.5293 86.9889 21.8685 87.6553 C16.0976 89.1005 9.95431 79.7555 5.65099 72.0707 C4.03748 69.1893 4.96266 66.0441 5.75285 63.4152 C9.11411 58.4046 15.0649 52.5344 21.2077 47.9484 C23.187 46.4708 25.1863 45.1264 27.1253 43.9872 C28.7131 43.2388 29.8991 42.7981 33.4709 43.7762" stroke="white" stroke-linecap="round" stroke-linejoin="round" pathLength="1" stroke-dashoffset="0px" stroke-dasharray="0px 1px"></path><path d="M92.7909 17.8196 C94.5301 13.9146 97.1654 7.12193 97.0441 4.48516 C96.985 3.20017 95.5772 2.26791 93.2535 1.71386 C82.2978 -0.898408 73.4433 4.21184 66.724 8.11956 C63.7772 9.8333 62.7065 13.033 62.6516 15.6408 C62.6222 17.0351 63.9575 18.4343 65.0636 19.4757 C73.1905 27.1268 91.0425 26.7937 93.3121 28.2541 C94.4632 28.9947 95.0039 30.5163 95.0828 31.795 C95.1394 32.7117 94.9313 33.5684 94.514 34.3715 C92.5229 38.2021 85.7687 40.8089 80.2554 42.8575 C77.574 43.8538 74.6137 43.4072 71.6332 42.8373 C70.1302 42.5499 68.82 41.577 68.9097 41.0683 C69.579 37.2738 81.6627 35.7073 94.514 34.3715 C102.842 33.5057 111.493 32.7369 117.568 31.5213 C124.257 30.1829 129.591 27.5273 130.533 28.1716 C131.506 28.8367 127.476 31.7737 126.735 33.5673 C125.993 35.361 127.126 36.3275 130.1 36.4244 C137.885 36.6781 144.19 34.8402 146.28 35.5191 C148.495 36.239 145.386 41.3208 143.958 44.1787 C141.89 48.3189 154.47 40.0631 160.165 39.8723 C161.549 39.8259 162.492 41.3208 163.127 42.5227 C164.064 44.2961 159.989 53.5887 152.489 68.0521 C149.815 73.2075 146.706 79.0199 143.234 85.3828 C131.861 106.225 123.317 110.995 116.864 113.115 C113.591 114.19 110.306 112.977 107.598 111.847 C104.657 110.619 102.613 108.13 101.666 105.719 C101.216 104.575 102.042 103.282 103.057 102.077 C104.072 100.872 105.562 99.7142 121.862 88.6882 C129.729 83.3665 141.036 75.7542 152.489 68.0521 C164.765 59.7963 177.209 51.4372 185.765 45.6856" stroke="white" stroke-linecap="round" stroke-linejoin="round" pathLength="1" stroke-dashoffset="0px" stroke-dasharray="0px 1px"></path></svg>

Creator of

[![Overtone](/images/logos/overtone.png)](https://overtone.pro) [![Prisma](/images/logos/prisma.png)](https://prisma.io)

## Get started

Give LiveStore a try. Start with an existing example or add it to your own project.

## Sponsor the project

Become a sponsor and get access to...

- LiveStore devtools
- Discord channel
- Community
