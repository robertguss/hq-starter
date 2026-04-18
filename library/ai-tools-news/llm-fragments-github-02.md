---
tags:
  - library
title: "llm-fragments-github 0.2"
url: "https://simonwillison.net/2025/Apr/20/llm-fragments-github/"
company: [personal]
topics: []
created: 2025-04-22
source_type: raindrop
raindrop_id: 1020570617
source_domain: "simonwillison.net"
source_type_raindrop: link
collection: "AI Tools & News"
collection_id: 69284314
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

I upgraded my `llm-fragments-github` plugin to add a new fragment type called `issue`. It lets you pull the entire content of a GitHub issue thread into your prompt as a …

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: llm-fragments-github 0.2

URL Source: https://simonwillison.net/2025/Apr/20/llm-fragments-github/

Published Time: Sat, 18 Apr 2026 12:43:53 GMT

Markdown Content:
# llm-fragments-github 0.2

# [Simon Willison’s Weblog](https://simonwillison.net/)

[Subscribe](https://simonwillison.net/about/#subscribe)

**Sponsored by:** Honeycomb — AI agents behave unpredictably. Get the context you need to debug what actually happened. [Read the blog](https://fandf.co/4sb46pb)

20th April 2025 - Link Blog

**[llm-fragments-github 0.2](https://github.com/simonw/llm-fragments-github/releases/tag/0.2)**. I upgraded my `llm-fragments-github` plugin to add a new fragment type called `issue`. It lets you pull the entire content of a GitHub issue thread into your prompt as a concatenated Markdown file.

(If you haven't seen fragments before I introduced them in [Long context support in LLM 0.24 using fragments and template plugins](https://simonwillison.net/2025/Apr/7/long-context-llm/).)

I used it just now to have Gemini 2.5 Pro provide feedback and attempt an implementation of a complex issue against my [LLM](https://github.com/simonw/llm) project:

llm install llm-fragments-github
llm -f github:simonw/llm \
  -f issue:simonw/llm/938 \
  -m gemini-2.5-pro-exp-03-25 \
  --system 'muse on this issue, then propose a whole bunch of code to help implement it'
Here I'm loading the FULL content of the `simonw/llm` repo using that `-f github:simonw/llm` fragment ([documented here](https://github.com/simonw/llm-fragments-github?tab=readme-ov-file#usage)), then loading all of the comments from [issue 938](https://github.com/simonw/llm/issues/938) where I discuss quite a complex potential refactoring. I ask Gemini 2.5 Pro to "muse on this issue" and come up with some code.

This worked _shockingly_ well. Here's [the full response](https://gist.github.com/simonw/a5f0c1e8184f4ddc8b71b30890fe690c#response), which highlighted a few things I hadn't considered yet (such as the need to migrate old database records to the new tree hierarchy) and then spat out a whole bunch of code which looks like a solid start to the actual implementation work I need to do.

I ran this against Google's free Gemini 2.5 Preview, but if I'd used the paid model it would have cost me 202,680 input tokens, 10,460 output tokens and 1,859 thinking tokens for a total of 62.989 cents.

As a fun extra, the new `issue:` feature itself was written almost entirely by OpenAI o3, again using fragments. I ran this:

llm -m openai/o3 \
  -f https://raw.githubusercontent.com/simonw/llm-hacker-news/refs/heads/main/llm_hacker_news.py \
  -f https://raw.githubusercontent.com/simonw/tools/refs/heads/main/github-issue-to-markdown.html \
  -s 'Write a new fragments plugin in Python that registers issue:org/repo/123 which fetches that issue
 number from the specified github repo and uses the same markdown logic as the HTML page to turn that into a fragment'
Here I'm using the ability to pass a URL to `-f` and giving it the full source of my [llm_hacker_news.py](https://github.com/simonw/llm-hacker-news/blob/main/llm_hacker_news.py) plugin (which shows how a fragment can load data from an API) plus the [HTML source](https://github.com/simonw/tools/blob/main/github-issue-to-markdown.html) of my [github-issue-to-markdown](https://tools.simonwillison.net/github-issue-to-markdown) tool (which I wrote a few months ago [with Claude](https://gist.github.com/simonw/cd1afb97e595b40fdeedebb48be7f4f1)). I effectively asked o3 to take that HTML/JavaScript tool and port it to Python to work with my fragments plugin mechanism.

o3 provided [almost the exact implementation I needed](https://gist.github.com/simonw/249e16edffe6350f7265012bee9e3305#response), and even included support for a `GITHUB_TOKEN` environment variable without me thinking to ask for it. Total cost: 19.928 cents.

On a final note of curiosity I tried running this prompt against [Gemma 3 27B QAT](https://simonwillison.net/2025/Apr/19/gemma-3-qat-models/) running on my Mac via MLX and [llm-mlx](https://github.com/simonw/llm-mlx):

llm install llm-mlx
llm mlx download-model mlx-community/gemma-3-27b-it-qat-4bit

llm -m mlx-community/gemma-3-27b-it-qat-4bit \
  -f https://raw.githubusercontent.com/simonw/llm-hacker-news/refs/heads/main/llm_hacker_news.py \
  -f https://raw.githubusercontent.com/simonw/tools/refs/heads/main/github-issue-to-markdown.html \
  -s 'Write a new fragments plugin in Python that registers issue:org/repo/123 which fetches that issue
 number from the specified github repo and uses the same markdown logic as the HTML page to turn that into a fragment'
That worked [pretty well too](https://gist.github.com/simonw/feccff6ce3254556b848c27333f52543#response). It turns out a 16GB local model file is powerful enough to write me an LLM plugin now!

Posted [20th April 2025](https://simonwillison.net/2025/Apr/20/) at 2:01 pm

## Recent articles

*   [Join us at PyCon US 2026 in Long Beach - we have new AI and security tracks this year](https://simonwillison.net/2026/Apr/17/pycon-us-2026/) - 17th April 2026
*   [Qwen3.6-35B-A3B on my laptop drew me a better pelican than Claude Opus 4.7](https://simonwillison.net/2026/Apr/16/qwen-beats-opus/) - 16th April 2026
*   [Meta's new model is Muse Spark, and meta.ai chat has some interesting tools](https://simonwillison.net/2026/Apr/8/muse-spark/) - 8th April 2026

This is a **link post** by Simon Willison, posted on [20th April 2025](https://simonwillison.net/2025/Apr/20/).

[github 185](https://simonwillison.net/tags/github/)[plugins 127](https://simonwillison.net/tags/plugins/)[ai 1965](https://simonwillison.net/tags/ai/)[generative-ai 1743](https://simonwillison.net/tags/generative-ai/)[local-llms 154](https://simonwillison.net/tags/local-llms/)[llms 1710](https://simonwillison.net/tags/llms/)[ai-assisted-programming 376](https://simonwillison.net/tags/ai-assisted-programming/)[llm 585](https://simonwillison.net/tags/llm/)[gemini 184](https://simonwillison.net/tags/gemini/)[mlx 42](https://simonwillison.net/tags/mlx/)[o3 22](https://simonwillison.net/tags/o3/)[long-context 20](https://simonwillison.net/tags/long-context/)[gemma 14](https://simonwillison.net/tags/gemma/)
### Monthly briefing

Sponsor me for **$10/month** and get a curated email digest of the month's most important LLM developments.

Pay me to send you less!

[Sponsor & subscribe](https://github.com/sponsors/simonw/)

*   [Disclosures](https://simonwillison.net/about/#disclosures)
*   [Colophon](https://simonwillison.net/about/#about-site)
*   ©
*   [2002](https://simonwillison.net/2002/)
*   [2003](https://simonwillison.net/2003/)
*   [2004](https://simonwillison.net/2004/)
*   [2005](https://simonwillison.net/2005/)
*   [2006](https://simonwillison.net/2006/)
*   [2007](https://simonwillison.net/2007/)
*   [2008](https://simonwillison.net/2008/)
*   [2009](https://simonwillison.net/2009/)
*   [2010](https://simonwillison.net/2010/)
*   [2011](https://simonwillison.net/2011/)
*   [2012](https://simonwillison.net/2012/)
*   [2013](https://simonwillison.net/2013/)
*   [2014](https://simonwillison.net/2014/)
*   [2015](https://simonwillison.net/2015/)
*   [2016](https://simonwillison.net/2016/)
*   [2017](https://simonwillison.net/2017/)
*   [2018](https://simonwillison.net/2018/)
*   [2019](https://simonwillison.net/2019/)
*   [2020](https://simonwillison.net/2020/)
*   [2021](https://simonwillison.net/2021/)
*   [2022](https://simonwillison.net/2022/)
*   [2023](https://simonwillison.net/2023/)
*   [2024](https://simonwillison.net/2024/)
*   [2025](https://simonwillison.net/2025/)
*   [2026](https://simonwillison.net/2026/)
