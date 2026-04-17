---
tags:
  - library
title: "cmpnd-ai/dspy-tutorial-deep-research: Learn DSPy's core abstractions while building a deep research agent."
url: "https://github.com/cmpnd-ai/dspy-tutorial-deep-research"
company: [personal]
topics: []
created: 2026-03-11
source_type: raindrop
raindrop_id: 1638523925
source_domain: "github.com"
source_type_raindrop: link
collection: "AI Repos & Open Source"
collection_id: 69284315
hydrated: true
hydrated_at: 2026-04-17
hydrated_via: github-api
---
## Excerpt

Learn DSPy's core abstractions while building a deep research agent. - cmpnd-ai/dspy-tutorial-deep-research

## Raw Content

<!-- Hydrated 2026-04-17 via github-api -->

# Tutorial: Learn DSPy by Building a Deep Research Agent

_DSPy by Example_

[DSPy](https://dspy.ai/) takes a fundamentally different approach to AI engineering. It's declarative rather than imperative. It structures its tasks, rather than relying solely on natural language. It can be a bit tricky to get your head around at first. But understanding DSPy is worth the upfront investment as it lets you build reliable, modular, and future-proof AI programs.

This tutorial teaches you DSPy's core abstractions (Signatures and Modules) through progressive, hands-on examples. No DSPy experience is required.

Together, we'll design and build a deep research agent. We'll iterate on the design, adding features as we go, ending up with a multistep workflow with clarification, planning, source gathering, processing, synthesis, and citation. By the end you'll have a working research agent, but more importantly, you'll have a mental model for designing, building, and evolving AI programs with DSPy.

---

### Repo Overview

The entire tutorial is contained in `tutorial.md`.

Notebooks, corresponding to each program we build, are in the `notebooks` folder, along with their output. To run the notebooks, be sure to create a `.env` file in the `notebooks` folder, if you're cloning this repo, and add an `ANTHROPIC_API_KEY` and `TAVILY_API_KEY`. (Alternatively, you could just drop the keys in each notebook.)
