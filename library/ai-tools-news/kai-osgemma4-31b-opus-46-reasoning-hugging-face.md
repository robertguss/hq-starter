---
tags:
  - library
title: "kai-os/gemma4-31b-Opus-4.6-reasoning · Hugging Face"
url: "https://huggingface.co/kai-os/gemma4-31b-Opus-4.6-reasoning"
company: [personal]
topics: []
created: 2026-04-04
source_type: raindrop
raindrop_id: 1672467925
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

Title: kai-os/gemma4-31b-Opus-4.6-reasoning · Hugging Face

URL Source: https://huggingface.co/kai-os/gemma4-31b-Opus-4.6-reasoning

Markdown Content:
## [](https://huggingface.co/kai-os/gemma4-31b-Opus-4.6-reasoning#gemma-4-31b-opus-reasoning-adapter-v1) Gemma 4 31B Opus Reasoning Adapter v1

This is a private QLoRA adapter for [google/gemma-4-31B-it](https://huggingface.co/google/gemma-4-31B-it), fine-tuned on a cleaned subset of [Crownelius/Opus-4.6-Reasoning-2100x-formatted](https://huggingface.co/datasets/Crownelius/Opus-4.6-Reasoning-2100x-formatted).

The goal of this run was simple: produce a Gemma 4 31B reasoning adapter trained only on Opus-style reasoning data, without mixing in unrelated instruction corpora or agent traces.

## [](https://huggingface.co/kai-os/gemma4-31b-Opus-4.6-reasoning#base-model) Base Model

*   Base model: `google/gemma-4-31B-it`
*   Adapter type: LoRA / QLoRA (`peft`)
*   Quantization: 4-bit NF4
*   Precision: BF16 compute

## [](https://huggingface.co/kai-os/gemma4-31b-Opus-4.6-reasoning#dataset) Dataset

Source dataset:

*   [Crownelius/Opus-4.6-Reasoning-2100x-formatted](https://huggingface.co/datasets/Crownelius/Opus-4.6-Reasoning-2100x-formatted)

Local filtering applied before training:

*   Removed duplicate user prompts
*   Removed obviously bad prompt families and formatting noise
*   Kept reasoning-style rows only

Final local dataset stats:

*   Rows in source: `2160`
*   Rows kept: `2025`
*   Train rows: `1924`
*   Validation rows: `101`
*   Category mix: `1899` math, `126` code

## [](https://huggingface.co/kai-os/gemma4-31b-Opus-4.6-reasoning#training-setup) Training Setup

*   Max sequence length: `4096`
*   Epochs: `2`
*   Learning rate: `1e-4`
*   Per-device batch size: `1`
*   Gradient accumulation: `8`
*   Hardware: NVIDIA GH200

LoRA target modules were adapted for Gemma 4 wrapped linear layers:

*   `q_proj.linear`
*   `k_proj.linear`
*   `v_proj.linear`
*   `o_proj.linear`
*   `gate_proj.linear`
*   `up_proj.linear`
*   `down_proj.linear`

## [](https://huggingface.co/kai-os/gemma4-31b-Opus-4.6-reasoning#validation-metrics) Validation Metrics

Final metrics from the completed run:

*   Eval loss: `3.6018`
*   Eval perplexity: `36.66`
*   Train runtime: `3723s`
*   Epochs completed: `2.0`

## [](https://huggingface.co/kai-os/gemma4-31b-Opus-4.6-reasoning#published-base-model-reference-benchmarks) Published Base-Model Reference Benchmarks

The table below is included for context and comes from Google's official [Gemma 4 31B Instruct model card](https://huggingface.co/google/gemma-4-31B-it). These are **published base-model reference scores for `google/gemma-4-31B-it`**, not adapter-specific evaluation results for this repository.

| Benchmark | Gemma 4 31B | Gemma 3 27B (no think) |
| --- | --- | --- |
| MMLU-Pro | 85.2% | 67.6% |
| AIME 2026 no tools | 89.2% | 20.8% |
| LiveCodeBench v6 | 80.0% | 29.1% |
| Codeforces Elo | 2150 | 110 |
| GPQA Diamond | 84.3% | 42.4% |
| Tau2 (average over 3) | 76.9% | 16.2% |
| HLE no tools | 19.5% | - |
| HLE with search | 26.5% | - |
| BigBench Extra Hard | 74.4% | 19.3% |
| MMMLU | 88.4% | 70.7% |
| MMMU Pro | 76.9% | 49.7% |
| OmniDocBench 1.5 (lower is better) | 0.131 | 0.365 |
| MATH-Vision | 85.6% | 46.0% |
| MRCR v2 8 needle 128k (average) | 66.4% | 13.5% |

Source:

*   [google/gemma-4-31B-it](https://huggingface.co/google/gemma-4-31B-it)

## [](https://huggingface.co/kai-os/gemma4-31b-Opus-4.6-reasoning#usage) Usage

This repository contains a PEFT adapter, not a fully merged standalone model.

Load it with:

*   Base model: `google/gemma-4-31B-it`
*   Adapter: this repository

```
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from peft import PeftModel
import torch

base_id = "google/gemma-4-31B-it"
adapter_id = "kai-os/gemma4-opus-reasoning-adapter-v1"

bnb = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16,
)

tokenizer = AutoTokenizer.from_pretrained(base_id)
base = AutoModelForCausalLM.from_pretrained(
    base_id,
    device_map="auto",
    quantization_config=bnb,
    torch_dtype=torch.bfloat16,
)
model = PeftModel.from_pretrained(base, adapter_id)
```

## [](https://huggingface.co/kai-os/gemma4-31b-Opus-4.6-reasoning#notes) Notes

*   This is a reasoning-focused adapter, not a benchmark-optimized release.
*   The benchmark table above is for the published base model, not this adapter.
*   It is best treated as an experimental distilled reasoning adapter.

## [](https://huggingface.co/kai-os/gemma4-31b-Opus-4.6-reasoning#acknowledgements) Acknowledgements

*   Google for Gemma 4
*   The Opus reasoning dataset authors and maintainers
*   Hugging Face `transformers`, `peft`, and `datasets`
