---
tags:
  - library
title: "Meta-Harness: End-to-End Optimization of Model Harnesses | alphaXiv"
url: "https://www.alphaxiv.org/abs/2603.28052"
company: [personal]
topics: []
created: 2026-04-08
source_type: raindrop
raindrop_id: 1677287287
source_domain: "alphaxiv.org"
source_type_raindrop: link
collection: "AI Tools & News"
collection_id: 69284314
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

View recent discussion. Abstract: The performance of large language model (LLM) systems depends not only on model weights, but also on their harness: the code that determines what information to store, retrieve, and present to the model. Yet harnesses are still designed largely by hand, and existing text optimizers are poorly matched to this setting because they compress feedback too aggressively. We introduce Meta-Harness, an outer-loop system that searches over harness code for LLM applications. It uses an agentic proposer that accesses the source code, scores, and execution traces of all prior candidates through a filesystem. On online text classification, Meta-Harness improves over a state-of-the-art context management system by 7.7 points while using 4x fewer context tokens. On retrieval-augmented math reasoning, a single discovered harness improves accuracy on 200 IMO-level problems by 4.7 points on average across five held-out models. On agentic coding, discovered harnesses surpass the best hand-engineered baselines on TerminalBench-2. Together, these results show that richer access to prior experience can enable automated harness engineering.

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: Meta-Harness: End-to-End Optimization of Model Harnesses

URL Source: https://www.alphaxiv.org/abs/2603.28052

Published Time: Mon Mar 30 2026 05:33:50 GMT+0000 (Coordinated Universal Time)

Markdown Content:
Meta-Harness: End-to-End Optimization of Model Harnesses

Yoonho Lee

Stanford

Roshen Nair

Stanford

Qizheng Zhang

Stanford

Kangwook Lee

KRAFTON

Omar Khattab

MIT

Chelsea Finn

Stanford

Project page w/ interactive demo:https://yoonholee.com/meta-harness/

Optimized harness:https://github.com/stanford-iris-lab/meta-harness-tbench2-artifact 0 10 20 30 40

Harness Evaluations

30

35

40

45

50

55

Best Performance (%)

Zero-shot

Few-shot

ACE

OpenEvolve

TTT-Discover

Meta-Harness

Harness Optimizer Search Progress 20

25

30

35

40

Pass Rate (%)

Meta-Harness

(ours)

37.6 Goose

35.5 Terminus-KIRA

33.7

Mini-SWE-

Agent

29.8 Terminus-2

28.3

Claude

Code

27.5

TerminalBench-2 Harness Performance

Human-written

Model-optimized (ours)

Figure 1:(Left)On text classification, Meta-Harness outperforms the best prior hand-

designed harnesses (ACE) and existing text optimizers (TTT-Discover, OpenEvolve), match-

ing the next-best method’s final accuracy after just 4 evaluations.(Right)On TerminalBench-

2, Meta-Harness outperforms all reported Claude Haiku 4.5 harnesses.

Abstract

The performance of large language model (LLM) systems depends not

only on model weights, but also on their harness: the code that determines

what information to store, retrieve, and present to the model. Yet harnesses

are still designed largely by hand, and existing text optimizers are poorly

matched to this setting because they compress feedback too aggressively:

they are memoryless, condition only on scalar scores, or restrict feedback to

short templates or summaries. We introduce Meta-Harness, an outer-loop

system that searches over harness code for LLM applications. It uses an

agentic proposer that accesses the source code, scores, and execution traces

of all prior candidates through a filesystem. On online text classification,

Meta-Harness improves over a state-of-the-art context management system

by 7.7 points while using 4×fewer context tokens. On retrieval-augmented

math reasoning, a single discovered harness improves accuracy on 200

IMO-level problems by 4.7 points on average across five held-out models.

On agentic coding, discovered harnesses surpass the best hand-engineered

baselines on TerminalBench-2.Together, these results show that richer

access to prior experience can enable automated harness engineering.

1 Introduction

Changing the harness around a fixed large language model (LLM) can produce a 6×

performance gap on the same benchmark [47]. The harness—the code that determines what

to store, retrieve, and show to the model—often matters as much as the model itself. This

sensitivity has led to growing interest in harness engineering, the practice of refining the

code around an LLM to improve the overall system’s performance [36; 21; 10; 9]. But despite

its importance, harness engineering remains largely manual: practitioners inspect failures,

1

arXiv:2603.28052v1 [cs.AI] 30 Mar 2026
