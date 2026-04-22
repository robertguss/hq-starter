---
tags:
  - library
title: "(untitled)"
url: "https://arxiv.org/pdf/2603.19312"
company: [personal]
topics: []
created: 2026-04-21
source_type: raindrop
raindrop_id: 1691375217
source_domain: "arxiv.org"
source_type_raindrop: document
collection: "unsorted"
collection_id: -1
hydrated: true
hydrated_at: 2026-04-22
hydrated_via: arxiv-api
---
## Raw Content

<!-- Hydrated 2026-04-22 via arxiv-api -->

**LeWorldModel: Stable End-to-End Joint-Embedding Predictive Architecture from Pixels**

**Authors:** Lucas Maes, Quentin Le Lidec, Damien Scieur, Yann LeCun, Randall Balestriero

**Published:** 2026-03-13T19:48:14Z

## Abstract

Joint Embedding Predictive Architectures (JEPAs) offer a compelling framework for learning world models in compact latent spaces, yet existing methods remain fragile, relying on complex multi-term losses, exponential moving averages, pre-trained encoders, or auxiliary supervision to avoid representation collapse. In this work, we introduce LeWorldModel (LeWM), the first JEPA that trains stably end-to-end from raw pixels using only two loss terms: a next-embedding prediction loss and a regularizer enforcing Gaussian-distributed latent embeddings. This reduces tunable loss hyperparameters from six to one compared to the only existing end-to-end alternative. With ~15M parameters trainable on a single GPU in a few hours, LeWM plans up to 48x faster than foundation-model-based world models while remaining competitive across diverse 2D and 3D control tasks. Beyond control, we show that LeWM's latent space encodes meaningful physical structure through probing of physical quantities. Surprise evaluation confirms that the model reliably detects physically implausible events.
