---
tags:
  - library
title: "A month of OpEx quick wins"
url: "https://www.jmduke.com/posts/opex-quick-wins.html"
company: [personal]
topics: []
created: 2026-03-30
source_type: raindrop
raindrop_id: 1665334785
source_domain: "jmduke.com"
source_type_raindrop: article
collection: "Marketing & Business"
collection_id: 69284316
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

I spent the past few weeks chasing quick OpEx wins for sport, having felt a nagging sensation that the orchards of our org were a little too-laden with low-h...

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: A month of OpEx quick wins

URL Source: https://www.jmduke.com/posts/opex-quick-wins.html

Published Time: 2026-03-29

Markdown Content:
2026/03/29

I spent the past few weeks chasing quick OpEx wins for sport, having felt a nagging sensation that the orchards of our org were a little too-laden with low-hanging fruit. I've already written about one of them — [self-hosting GitHub Actions](https://www.jmduke.com/posts/how-i-saved-100.html) — but here are a few more that I wanted to write down before I forget.

* * *

## 1. Per-seat pricing in Vercel

Buttondown uses Vercel for the docs and marketing site as well as for our Storybooks. Vercel's Pro plan requires you to pay $20/month per seat. There's a "viewer" role that you can assign to users which gives them access to view stuff, but they can't trigger deployments.

To get around this, I pushed a change to programmatically trigger deploys via GitHub Action rather than using their standard Git integration. What's more, this means we get to consolidate our CI logic a bit — which solves a long-standing annoyance of mine, having queued builds sit and wait for ten minutes only to get ignored because they're irrelevant to the given PR.

## 2. Sentry migration + logging

We were on an old plan that charged us way more, so I migrated us to the most recent pricing grid. (Not _downgraded_, mind you — just moved to the current pricing, which happened to be cheaper. The joys of being a long-tenured customer.)

After that, I took a look at the long pole in our usage-based billing, which was logs. Turns out 30% of our log volume was a duplicate wide event — one `request.started` for every `request.finished`. We never actually need those or look at them, so I removed that.

## 3. S3 to R2

We started using R2 for managing our frontend build tarballs that get deployed to Heroku. But really, that was a Trojan horse for a larger migration: getting off of S3 entirely in favor of R2.

R2 has a [reverse backfill](https://developers.cloudflare.com/r2/data-migration/sippy/) thing and is also compatible with S3's API, so I didn't even have to change any code — just a bunch of keys. The net result was a ~$300/month S3 bill getting chopped down to $20.

## 4. Obsidian Publish to Bun

While I still like [Obsidian for writing internal docs](https://www.jmduke.com/posts/obsidian-for-internal-docs.html), my love of their Publish plugin has come to an end. I replaced it with a hundred-line Bun build script — not unlike the one powering this very blog — and saved $10/month.

## 5. RQ to Postgres

Unshipped RQ entirely as a task runner in favor of Postgres. (I need to write more about this in general.) The noteworthy bit is that we went from paying a comical amount for a tiny bit of Redis hardware — roughly $250/month for two gigs of RAM — to $25/month.

* * *

All in all:

| Change | Before | After | Savings |
| --- | --- | --- | --- |
| Self-hosted CI runners | $300/mo | $100/mo | $200/mo |
| Vercel seats | $200/mo | $40/mo | $160/mo |
| Sentry plan + logs | $200/mo | $80/mo | $120/mo |
| S3 → R2 | $300/mo | $20/mo | $280/mo |
| Obsidian Publish → Bun | $10/mo | $0/mo | $10/mo |
| Redis → Postgres (RQ) | $250/mo | $25/mo | $225/mo |
| **Total** | **$1,260/mo** | **$265/mo** | **$995/mo** |

All in all, a latte shy of one thousand bucks a month for what was probably, in aggregate, a single day of work.

## About the Author

I'm Justin Duke — a software engineer, writer, and founder. I currently work as the CEO of [Buttondown](https://buttondown.com/), the best way to start and grow your newsletter, and as a partner at [Third South Capital](https://thirdsouth.capital/).

### Colophon

You can view a markdown version of this post [here](https://www.jmduke.com/posts/opex-quick-wins.md).
