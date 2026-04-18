---
tags:
  - library
title: "TurboQuant - Extreme Compression for AI Efficiency"
url: "https://turboquant.net/"
company: [personal]
topics: []
created: 2026-03-29
source_type: raindrop
raindrop_id: 1664668221
source_domain: "turboquant.net"
source_type_raindrop: link
collection: "AI Tools & News"
collection_id: 69284314
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

TurboQuant is a new online vector quantization algorithm that compresses KV cache to 3 bits with zero accuracy loss, cutting memory by 6x and speeding attention up by 8x.

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: TurboQuant.net - Independent TurboQuant Analysis

URL Source: https://turboquant.net/

Markdown Content:
Independent analysis · Built from public research context

## TurboQuant

For Builders Evaluating Compression

Original explainers, benchmark breakdowns, and implementation notes covering TurboQuant, PolarQuant, QJL, and the real systems tradeoffs behind long-context KV-cache compression.

6x+

memory compression

8x

attention speedup (H100)

3-bit

zero-loss compression

Recent Updates

## Latest momentum around TurboQuant

The paper release quickly turned into implementation work, deployment discussion, and practical evaluation around long-context inference.

March 2026

TurboQuant landed in MLX in 25 minutes with GPT-5.4

A builder reported using GPT-5.4 to complete an MLX implementation of TurboQuant in 25 minutes.

[View post](https://x.com/mweinbach/status/2036786698315546728)

March 2026

Google Research formally introduced TurboQuant

The release framed TurboQuant as a near-optimal online quantization method for both KV cache compression and vector search.

Market impact

$MU and $SNDK sold off at the open

After $GOOGL released TurboQuant, both $MU and $SNDK were hit sharply at market open.

Sponsored

Expert Commentary

## A practical read on what TurboQuant changes

One expert view on what is likely already deployed, what still remains hard, and why the paper matters even if most easy gains are gone.

Independent Industry Expert

LLM systems and inference engineering

TurboQuant matters less because it saves a bit more memory, and more because it marks where KV-cache compression starts to hit a real boundary.

KV cache has long been the largest source of memory consumption in large-model inference. What this paper does, in essence, is compress that data in a way that approaches the information-theoretic optimum. It is not just lowering precision. It is reallocating information density: ordinary regions are represented with extremely low bits, while outliers retain higher precision. At the same time, the method stops treating values independently and instead encodes them at the vector level, which fits the inner-product structure of attention itself.

The critical point is that its error is already close to the information-theoretic lower bound, the Shannon limit. That means compression efficiency is already near the theoretical ceiling. The paper reports roughly 4x to 4.5x compression with little visible performance loss. The result is strong, but it also suggests there is not much room left for further compression without harming model quality.

Given how large-tech internal R&D usually works, the optimization effects implied by the paper were likely absorbed in stages before publication. Low-bit quantization has already been widely deployed, from int8 to int4 and beyond, across mainstream inference stacks. Separate handling for outliers is also not new: methods such as SmoothQuant and AWQ are already doing closely related things. KV-cache compression itself, sliding windows, and hierarchical cache designs are already standard practice in large-model systems.

What likely has not fully landed yet is the most extreme part of the paper: vector quantization and coding schemes that move closer to the information-theoretic limit. The barrier is not theory, but implementation. These methods are less GPU-friendly, harder to keep low-latency, and more difficult to stabilize and generalize in production, so they may take much longer to ship.

If I had to estimate roughly how much of the paper's benefit is already reflected in deployed systems, it would look something like this: the earliest KV cache starts at 1x cost; basic quantization gets to around 2x to 3x compression; adding outlier-aware handling can reach about 3x to 4x; the paper pushes that further to around 4x to 4.5x. In other words, most of the easy gains have already been captured. What remains is smaller in upside and increasingly expensive to realize.

The reason is straightforward. Early compression removes redundancy. Later compression starts to hit effective information, so every additional step has a much higher chance of hurting model capability. Error no longer degrades smoothly; beyond a certain point, it can worsen quickly. Engineering difficulty also does not grow linearly. It rises sharply.

You can infer from current model behavior that mainstream systems are already using many of these ideas. Better long-context behavior, lower inference cost, and stable performance all suggest that KV-cache efficiency has already been significantly improved. A team at Google's level has very likely already deployed low-bit quantization, outlier handling, and at least part of KV-cache compression.

That means if this Google paper has an impact on storage, much of that impact has probably already shown up. The parts that have not shown up yet will likely be harder to implement than the gains that came before.

More importantly, the significance of the paper is not just how much more memory it saves. It gives us a boundary. KV-cache compression is approaching its limit, and the remaining room is narrow. The next major change is unlikely to come from compression alone. It will require finding a different path.

Core Innovation

## Why TurboQuant feels like a category-changing result

TurboQuant.net focuses on the engineering meaning of the result: what is original in the method, what the benchmarks actually imply, and where real deployment gains are likely to come from.

*   Require dataset-specific training
*   Store many full-precision normalization constants
*   Long indexing time
*   Visible accuracy loss

*   Random rotation plus polar transform (PolarQuant)
*   1-bit residual correction (QJL) removes normalization overhead
*   Near-zero indexing time
*   Matches the 32-bit baseline on reported benchmarks

AISTATS 2026

#### PolarQuant

Polar-transform core that eliminates normalization overhead

[arXiv: 2502.02617 →](https://arxiv.org/pdf/2502.02617)

AAAI 2025

#### QJL

1-bit unbiased inner-product estimator

[ACM DL →](https://dl.acm.org/doi/10.1609/aaai.v39i24.34773)

Background

## Why TurboQuant matters

A quick look at vector quantization limits and KV cache pressure

### 1 The classical vector-quantization problem

Vector quantization maps high-dimensional vectors into compact codes while minimizing distortion. The theory gives clear lower bounds, but conventional methods stay far from them in practice.

#### Distortion formulas

MSE: D_MSE = E[||x - x̂||²]

Inner product: D_prod = E[|⟨y,x⟩ - ⟨y,x̂⟩|²]

#### Theory

MSE lower bound: D_MSE ≥ 1/4^b

Inner-product lower bound: D_prod ≥ (||y||² / d) · 1/4^b

Classical approaches such as PQ remain noticeably above these bounds.

### 2 The KV cache bottleneck in LLMs

In decoder-only transformers, KV cache stores one key/value pair per token. With long context windows, that memory cost quickly dominates the system budget.

#### Memory estimate

memory ≈ 2 × L × d × 2 bytes (FP16)

128K context + 7B model tens of GB

KV cache share of total memory 80%+

#### What TurboQuant changes

*   ✓ No training and no finetuning
*   ✓ 3.5 bits per channel reaches quality neutrality
*   ✓ LongBench matches FP32
*   ✓ Makes long-context inference viable on edge devices

### 3 Vector search applications

For ANN systems such as FAISS, TurboQuant improves recall while keeping indexing overhead close to zero.

Higher recall

Outperforms PQ and RabbiQ on GloVe

Indexing time ≈ 0

Practical for billion-scale vector stores

Core Principle

## TurboQuant as a two-stage algorithm

TurboQuant = PolarQuant for main compression + QJL for residual correction

### PolarQuant: polar-coordinate transform

The key idea is to remove per-block normalization overhead. PolarQuant rotates the vector randomly so coordinates follow a concentrated distribution that is easy to quantize.

#### Coordinate distribution

f_X(x) = Γ(d/2) / (√π · Γ((d-1)/2))
× (1 - x²)^((d-3)/2)

where x ∈ [-1, 1]

1

Group the d-dimensional vector into pairs to obtain radii and angles

2

Apply recursive polar transforms on the radii

3

Quantize only the angles, whose distribution is highly concentrated

#### Why it works

*   No per-block full-precision constants

Overhead drops to zero. 
*   Near-lossless beyond 4.2x compression

Stronger than conventional baselines. 
*   Gaussian-like coordinates in high dimension

Supports optimal scalar quantizers such as Lloyd-Max. 

Results

## The numbers are the argument

Benchmarks across Gemma, Mistral, and Llama-3.1-8B

### KV cache compression benchmarks

50.06

LongBench score

3.5-bit = full cache

100

Needle In A Haystack

perfect from 4K to 104K

6x+

memory reduction

large cost savings

8x

attention speed

H100 at 4-bit

| Benchmark | TurboQuant 3.5-bit | TurboQuant 2.5-bit | Full Cache |
| --- | --- | --- | --- |
| LongBench | 50.06 | 49.44 | 50.06 |
| Needle In A Haystack | 100 | 99.8 | 100 |
| ZeroSCROLLS | best | near-best | baseline |
| RULER | best | near-best | baseline |
| L-Eval | best | near-best | baseline |

### Vector search benchmark (GloVe d=200)

#### 1@k recall

TurboQuant best

PQ lower

RabbiQ middle

#### Indexing time

TurboQuant≈ 0

PQ (codebook training)long

RabbiQ middle

### Comparison against alternatives

| Method | Needs training | Unbiased | Compression | Speedup |
| --- | --- | --- | --- | --- |
| TurboQuant | No | Yes | 6x+ | 8x |
| KIVI | Calibration | No | 4x | 4x |
| SnapKV | Finetuning | No | 2-4x | 2-4x |
| DuQuant | Calibration | Partial | 4x | 4x |

| Model | Weights | Pure model VRAM | Total VRAM before | Total VRAM after | 4090s before | 4090s after | Change |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ChatGLM-4 (9B) | BF16 | 18 GB | 19.8 GB | 18.3 GB | 1 | 1 | Extra headroom on a single 4090. |
| ChatGLM-4 (9B) | INT8 | 9 GB | 10.8 GB | 9.3 GB | 1 | 1 | Still single-card, with more buffer. |
| ChatGLM-4 (9B) | INT4 | 5 GB | 6.8 GB | 5.3 GB | 1 | 1 | Very comfortable single-card fit. |
| Qwen-2.5 (32B) | BF16 | 64 GB | 69 GB | 64.8 GB | 3 | 3 | Savings help, but not enough to drop a GPU. |
| Qwen-2.5 (32B) | INT8 | 32 GB | 37 GB | 32.8 GB | 2 | 2 | More margin on a 2x4090 node. |
| Qwen-2.5 (32B) | INT4 | 18 GB | 23 GB | 18.8 GB | 2 | 1(-1) | Pulled back under the single-4090 limit. |
| Llama-3.1 (70B) | BF16 | 140 GB | 150 GB | 141.7 GB | 7 | 6(-1) | Drops one RTX 4090 at 100K context. |
| Llama-3.1 (70B) | INT8 | 70 GB | 80 GB | 71.7 GB | 4 | 3(-1) | Material hardware cost reduction. |
| Llama-3.1 (70B) | INT4 | 38 GB | 48 GB | 39.7 GB | 3 | 2(-1) | Brings 70B into a practical dual-4090 envelope. |
| Mixtral 8x22B (141B MoE) | BF16 | 282 GB | 288 GB | 283 GB | 13 | 13 | MoE keeps KV share relatively small. |
| Mixtral 8x22B (141B MoE) | INT8 | 141 GB | 147 GB | 142 GB | 7 | 7 | Lower pressure, but same card class. |
| Mixtral 8x22B (141B MoE) | INT4 | 75 GB | 81 GB | 76 GB | 4 | 4 | Useful slack without a node count change. |
| DeepSeek-R1 (671B MoE) | FP8 | 700 GB | 712 GB | 702 GB | 31 | 30(-1) | Saves one 4090 even at hyperscale. |
| DeepSeek-R1 (671B MoE) | INT4 | 350 GB | 362 GB | 352 GB | 16 | 15(-1) | Still too large for small nodes, but one card disappears. |

Usage

## From paper to production

How to think about integrating TurboQuant into a real stack

### Current status

The paper provides theory and pseudocode, but there is no official open-source implementation yet. Community integration work has started.

*   •llama.cpp Discussion #20969 is tracking integration ideas
*   •Experiments in MLX report around 5x compression with 99.5% quality retention
*   •Open-source code is widely expected around Q2 2026

### Implementation sketch

1

#### Precompute Lloyd-Max centroids

Do it once offline and reuse them.

# Python-like pseudocode
centroids = lloyd_max_quantizer(
    distribution="beta",
    bits=b
)

2

#### Generate a random rotation matrix

Use QR decomposition to build an orthogonal matrix.

# random rotation
G = np.random.randn(d, d)
Pi, _ = np.linalg.qr(G)

3

#### Build quant / dequant primitives

This is the core path for storage and recovery.

def quant(x, Pi, centroids):
    y = Pi @ x
    idx = find_nearest(y, centroids)
    return idx

def dequant(idx, Pi, centroids):
    y = centroids[idx]
    x = Pi.T @ y
    return x

4

#### Integrate inside attention

Store K/V in TurboQuant form and estimate inner products with QJL.

# Transformer attention
k_quant = turboquant_quant(k)
v_quant = turboquant_quant(v)
# use QJL during attention

### Deployment notes

#### Hardware

H100 and A100 are ideal. 4-bit mode is where the paper reports 8x speedups.

FP

#### Mixed precision

Use TurboQuant for KV cache and INT4 for weights to maximize total compression.

#### Edge devices

3-bit KV cache can make 32K+ context feasible on phones with software-only implementations.

### Practical risks and mitigations

#### Random rotation overhead

Pre-generate and reuse the matrices instead of rebuilding them online.

#### Residual norm storage

One FP16 scalar is small enough to keep the overhead negligible.

Suggested open-source path

`fork llama.cpp → add a turboquant_quant kernel`

[](https://github.com/ggerganov/llama.cpp/discussions)

Outlook

## How TurboQuant could shift the AI stack

#### LLM inference

Million-token contexts become materially cheaper, with a path to native support in future model stacks.

#### Vector databases

Real-time indexing and sub-millisecond search become easier to deliver.

#### Edge AI

Long-context inference on mobile and embedded devices becomes more realistic.

#### Multimodal embeddings

The same ideas can extend to image and video embedding compression.

#### Theory extensions

Combining with outlier-handling methods could push the field toward practical 2-bit systems.

#### Community impact

Expect rapid follow-through from ecosystems such as vLLM and Hugging Face.

### Expected timeline

Q2

#### 2026 Q2

Open-source code and framework integrations

Q4

#### 2026 Q4

Commercial products, likely cloud-first

27

#### 2027

Potential normalization as an LLM quantization standard

Risk note: poor random-seed handling could introduce small bias, though the paper argues the effect is negligible in high dimension.

FAQ

## Common questions

The main questions engineers and readers ask first

Resources

## References and links

### Community discussion
