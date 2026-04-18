---
tags:
  - library
title: "ProgramAsWeights"
url: "https://programasweights.com/"
company: [personal]
topics: []
created: 2026-04-15
source_type: raindrop
raindrop_id: 1685206536
source_domain: "programasweights.com"
source_type_raindrop: link
collection: "AI Tools & News"
collection_id: 69284314
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

Compile natural language specifications into tiny neural programs that run locally via llama.cpp. Once compiled, they work as regular Python functions.

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: PAW — Define functions in English, run them locally

URL Source: https://programasweights.com/

Published Time: Sat, 18 Apr 2026 02:52:06 GMT

Markdown Content:
New: Alien Taboo — describe words to a tiny AI built with PAW.New: Alien Taboo

[Play](https://programasweights.com/alien)

Open source · Local-first · Deterministic

ProgramAsWeights compiles natural language specs into tiny neural programs that run on your machine. Once compiled, they work as regular Python functions — no internet connection, no external service, no per-call fees.

[Try the Playground](https://programasweights.com/playground)[Run in Browser](https://programasweights.com/browser)[Docs](https://programasweights.com/docs)

$pip install programasweights

## What can you build?

Functions that are easy to describe in English but hard to write as rules

### Fuzzy Grep & Search

Typo-tolerant search, semantic matching, near-duplicate detection — what regex and grep can't do

### Format Repair

Fix malformed JSON, normalize dates, repair API inputs that are almost-but-not-quite valid

### Log & Output Triage

Filter verbose logs to just what matters, detect anomalies, compress tracebacks to essentials

### Custom Classification

Define what "important" or "relevant" means in plain English — no training data or ML expertise needed

### Email Triage

Classify emails, messages, or alerts by your own definition of urgency — flag what matters, ignore the rest

### Agent Preprocessing

Parse tool calls, route tasks, validate outputs, redact secrets — lightweight functions for agentic pipelines

## See it in action

Pick a task. We compile it into a neural program. It runs locally on your machine.

## How it works

Three steps from idea to running code

1

### Describe

Write what your function should do in plain English. No training data, no model selection, no hyperparameters.

"Is this message urgent?"

2

### Compile

Our neural compiler transforms your spec into a tiny .paw file (5-22 MB). Takes seconds, not hours.

paw compile --spec "..."

3

### Run

One-time interpreter download (134-594 MB), then each program runs locally. No internet needed after setup.

f("I love this!") → "positive"

NEW: Browser inference

### Compact programs run directly in the browser

No server needed. Programs compiled with the compact interpreter (GPT-2 124M) run entirely client-side via WebAssembly — ~200ms per call. Embed in any webpage with 3 lines of JS.

[Try it live](https://programasweights.com/browser)

## Ready to build your first fuzzy function?

Describe it in English, compile it in seconds, run it forever. No API keys. No fine-tuning pipelines.

[Open Playground](https://programasweights.com/playground)[Run in Browser](https://programasweights.com/browser)[Star on GitHub](https://github.com/programasweights/programasweights-python)

$pip install programasweights

[![Image 1: Paw](https://programasweights.com/paw.svg) PAW](https://programasweights.com/)
Define functions in English. Compile them into neural programs. Run them locally.

© 2026 ProgramAsWeights. Open source under MIT License.
