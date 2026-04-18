---
tags:
  - library
title: "https://arxiv.org/pdf/2603.03329"
url: "https://arxiv.org/pdf/2603.03329"
company: [personal]
topics: []
created: 2026-04-10
source_type: raindrop
raindrop_id: 1679340817
source_domain: "arxiv.org"
source_type_raindrop: document
collection: "AI Repos & Open Source"
collection_id: 69284315
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: arxiv-api
---
## Raw Content

<!-- Hydrated 2026-04-18 via arxiv-api -->

**AutoHarness: improving LLM agents by automatically synthesizing a code harness**

**Authors:** Xinghua Lou, Miguel Lázaro-Gredilla, Antoine Dedieu, Carter Wendelken, Wolfgang Lehrach, Kevin P. Murphy

**Published:** 2026-02-10T14:12:54Z

## Abstract

Despite significant strides in language models in the last few years, when used as agents, such models often try to perform actions that are not just suboptimal for a given state, but are strictly prohibited by the external environment. For example, in the recent Kaggle GameArena chess competition, 78% of Gemini-2.5-Flash losses were attributed to illegal moves. Often people manually write "harnesses" around LLMs to prevent such failures. In this paper, we demonstrate that Gemini-2.5-Flash can automatically synthesize such a code harness, using a small number of rounds of iterative code refinement given feedback from the (game) environment. The resulting harness prevents all illegal moves in 145 different TextArena games (both 1-player and 2-player), enabling the smaller Gemini-2.5-Flash model to outperform larger models, such as Gemini-2.5-Pro. Pushing our technique to the limit, we can get Gemini-2.5-Flash to generate the entire policy in code, thus eliminating the need to use the LLM at decision making time. The resulting code-policy receives a higher average reward than Gemini-2.5-Pro and GPT-5.2-High on 16 TextArena 1-player games. Our results show that using a smaller model to synthesize a custom code harness (or entire policy) can outperform a much larger model, while also being more cost effective.
