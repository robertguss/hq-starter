---
tags:
  - library
title: "How I freed 75GB of disk space in 10 seconds with uv cache prune"
url: "https://medium.com/@brookejamieson/how-i-freed-75gb-of-disk-space-in-10-seconds-with-uv-cache-prune-36da9f734e8d"
company: [personal]
topics: []
created: 2026-03-12
source_type: raindrop
raindrop_id: 1640430451
source_domain: "medium.com"
source_type_raindrop: article
collection: "AI Tools & News"
collection_id: 69284314
hydrated: true
hydrated_at: 2026-04-20
hydrated_via: browser-harness
---

## Excerpt

How I freed 75GB of disk space in 10 seconds with uv cache prune Last updated: 11 March 2026 Last week my laptop was slow and chugging so much I couldn't open Photoshop. I'd been blaming macOS, blaming Chrome, blaming the 67 tabs I had open, but it turned out the actual problem was the uv cache eating my hard drive.

## Raw Content

<!-- Hydrated 2026-04-20 via browser-harness -->

# How I freed 75GB of disk space in 10 seconds with uv cache prune

Last updated: 11 March 2026

![Brooke Jamieson (Senior Developer Advocate, AWS) in a checkered dress poses on a NYC sidewalk in front of a cream-colored classical building with ornate columns, next to large pink balloon letters spelling "uv cache prune"](https://miro.medium.com/v2/resize:fit:2000/1*sqe2-iaqenPF2Tm8WXD85w.png)

Last week my laptop was slow and chugging so much I couldn't open Photoshop. I'd been blaming macOS, blaming Chrome, blaming the 67 tabs I had open, but it turned out the actual problem was the uv cache eating my hard drive.

If you use MCP servers with your coding tools (Kiro, Cursor, Claude Code, etc.), they're probably running uvx under the hood. I wrote about one of my most-used MCPs, the AWS Documentation MCP Server, back in November, and I use several others daily. Every time uvx runs, uv caches the packages it downloads. That cache never cleans itself up.

I ran this:

```
uv cache prune
```

![Terminal window showing the command 'uv cache prune' with output 'Pruning cache at: .cache/uv' and 'Removed 58158 files (1.0GiB)'](https://miro.medium.com/v2/resize:fit:5000/1*G281r4ZjTWK2G7YlOSLcrg.png)

And I got back 60GB. It was just one command, and it took maybe 10 seconds.

Then, this week I ran it again and freed another 15GB. 75GB total, just sitting there doing nothing on my poor little MacBook.

## So why was my cache so big?

uv uses aggressive caching to avoid re-downloading dependencies, which is why uvx feels fast. The trade-off is that the cache grows quietly in the background. Mine got out of control because I use a bunch of different MCP servers that each pull in their own dependencies, and every time uv itself gets updated, the cache version changes, which leaves old entries behind that will literally never be used again. If you experiment with a lot of packages and tools (guilty as charged — if this is wrong I don't want to be right), it adds up even faster.

I kind of wish uv would warn you when the cache gets past a certain size, or at least mention uv cache prune somewhere more prominent. I only found out about it because I went hunting for why my disk was full.

## What uv cache prune does (and doesn't do)

uv cache prune removes unused cache entries. Old versions, stale downloads, things that are never going to be needed again. It doesn't touch anything that's currently in use. From the uv docs:

> uv cache prune removes all unused cache entries. For example, the cache directory may contain entries created in previous uv versions that are no longer necessary and can be safely removed. uv cache prune is safe to run periodically, to keep the cache directory clean.

If you want to see how big your cache is before you prune:

```
du -sh $(uv cache dir)
```

I was super shocked to see how well this worked — probably the longest part of this process was the time I spent staring at my screen not believing the number I was seeing after being baffled and fighting with storage for MONTHS.

There's also uv cache clean which wipes the entire cache (kind of a nuclear option so only do this if you really need a fresh start, or you're feeling scandalous), uv cache clean ruff if you want to clear a specific package, and uv cache prune --ci which is made for CI pipelines where you want to keep source-built wheels but ditch the pre-built ones.

I'm going to start running this at the end of each day before I turn my laptop off for the night. If you use uvx or uv regularly, or any MCPs, check your cache size. You might be sitting on a heap of free disk space you didn't know you had.

### About the Author:

Brooke Jamieson is a Senior Developer Advocate at AWS, focused on AI agents and developer tools. A former fashion model turned mathematician turned AI Engineer, Brooke moved from Australia to New York City for this role. They make byte-sized tech content about AI and AWS, and you can find them on LinkedIn, Instagram or X.
