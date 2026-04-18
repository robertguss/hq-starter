---
tags:
  - library
title: "kai-os/Carnice-9b · Hugging Face"
url: "https://huggingface.co/kai-os/Carnice-9b"
company: [personal]
topics: []
created: 2026-04-04
source_type: raindrop
raindrop_id: 1672518109
source_domain: "huggingface.co"
source_type_raindrop: article
collection: "AI Tools & News"
collection_id: 69284314
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

We’re on a journey to advance and democratize artificial intelligence through open source and open science.

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: kai-os/Carnice-9b · Hugging Face

URL Source: https://huggingface.co/kai-os/Carnice-9b

Markdown Content:
[![Image 1: banner](https://huggingface.co/kai-os/Carnice-9b/resolve/main/banner.png)](https://huggingface.co/kai-os/Carnice-9b/blob/main/banner.png)

This model would not have been possible without the contributions of [Teknium](https://huggingface.co/teknium), ([Nous Research](https://huggingface.co/NousResearch)), [Zachary Mueller](https://huggingface.co/muellerzr), ([Lambda](https://huggingface.co/lambda)).

Carnice-9b is a standalone merged model tuned specifically for the Hermes Agent harness.

It is built on top of `Qwen/Qwen3.5-9B`, but the training target here was not generic chat quality or leaderboard chasing. The goal was to improve behavior inside Hermes Agent itself: tool calling, terminal use, browser use, multi-step execution, and the exact message patterns the Hermes harness expects.

This repo is the direct-load merged checkpoint form of [kai-os/qwen35-hermes-stage2-adapter-v1](https://huggingface.co/kai-os/qwen35-hermes-stage2-adapter-v1). It loads as its own model without a separate PEFT adapter step.

Important detail: this is a merged standalone checkpoint, not a separate full-parameter training run from scratch.

## [](https://huggingface.co/kai-os/Carnice-9b#training-approach) Training Approach

Carnice-9b was trained in two stages.

*   Stage A was a reasoning repair pass on carefully selected high-signal reasoning data.
*   Stage B was a Hermes-specific refresh pass built around harness-native traces and Hermes-style action structure.

The second stage is the important part for this release. Instead of teaching a generic external tool schema, it was trained on data shaped for the Hermes Agent environment itself.

## [](https://huggingface.co/kai-os/Carnice-9b#hermes-agent-focus) Hermes-Agent Focus

Carnice-9b is intended for Hermes Agent first.

It was tuned around workflows such as:

*   terminal-heavy task execution
*   file editing and structured tool use
*   browser and web-assisted agent behavior
*   multi-turn tool calling inside the Hermes runtime
*   Hermes-native conversation and tool-call formatting

A major design constraint during training was to avoid teaching the model foreign agent habits that would make it awkward inside the Hermes harness.

## [](https://huggingface.co/kai-os/Carnice-9b#data) Data

The Hermes-specialized stage draws primarily from:

*   [kai-os/carnice-glm5-hermes-traces](https://huggingface.co/datasets/kai-os/carnice-glm5-hermes-traces)
*   `open-thoughts/OpenThoughts-Agent-v1-SFT`

The earlier repair stage uses a smaller reasoning mix centered on:

*   `bespokelabs/Bespoke-Stratos-17k`
*   `AI-MO/NuminaMath-CoT`

The release intentionally centers harness-native behavior over broad generic benchmark optimization.

## [](https://huggingface.co/kai-os/Carnice-9b#evaluation) Evaluation

This model is being evaluated primarily inside Hermes Agent rather than through generic standalone chat benchmarks.

The main evaluation focus is official Hermes-compatible benchmark paths and harness-native runs. Partial one-shot numbers exist, but this card intentionally does not center them. For this release, the important point is what the model was optimized for: Hermes Agent execution quality, not shallow benchmark cosmetics.

## [](https://huggingface.co/kai-os/Carnice-9b#usage) Usage

```
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_id = "kai-os/carnice-v1-9b-hermes-agent-stage2-merged"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)
```

## [](https://huggingface.co/kai-os/Carnice-9b#notes) Notes

*   This release is specifically intended for Hermes Agent style use.
*   The model card keeps benchmark discussion intentionally lightweight until the stronger harness-native eval pass is finished.
*   Supplementary diagnostics from the training progression are still available in the repo files, but they are not the main story of the release.
