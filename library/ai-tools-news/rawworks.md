---
tags:
  - library
title: "RAW.works"
url: "https://raw.works/"
company: [personal]
topics: []
created: 2026-04-20
source_type: raindrop
raindrop_id: 1690746811
source_domain: "raw.works"
source_type_raindrop: link
collection: "unsorted"
collection_id: -1
hydrated: true
hydrated_at: 2026-04-22
hydrated_via: defuddle
---
## Excerpt

Raymond A. Weitekamp

## Raw Content

<!-- Hydrated 2026-04-22 via defuddle -->

Reasoning models were the first clear proof that language model capability can scale with test-time compute. [Recursive language models (RLMs)](https://arxiv.org/abs/2512.24601) ask what the correct abstraction for spending that compute is.

The insight behind RLMs is obvious in hindsight: it is the direct marriage of two important axes of model capability — reasoning and tool use. This is more radical than it first sounds. RLMs collapse reasoning and tool use into a single inference abstraction: the model treats its own prompt as an environment it can inspect, slice, and recursively query. *Context itself becomes the object of computation.*

This post is my attempt to explain why RLMs matter. I define what a RLM actually is, place it in the short history of reasoning and tool use, walk through the ~6 months of empirical results that have quietly turned “RLM” from a benchmark trick into the next reasoning paradigm, flag the honest limitations, and point at a few places to start building.

## What is a RLM?

A Recursive Language Model, as introduced by [Zhang, Kraska, and Khattab](https://arxiv.org/abs/2512.24601), is an inference paradigm in which a language model treats its input prompt as an environment rather than a fixed string. The root LM is given a REPL in which the prompt is bound to a variable it can inspect, slice, and partition programmatically. When it decides a region is worth a closer look, it issues a recursive subcall — to itself or another LM — over that slice and incorporates the result. Recursion bottoms out at the base model’s ordinary forward pass.

One consequence is that input size is no longer a hard ceiling on the computation. The paper reports RLMs processing inputs up to two orders of magnitude beyond the underlying model’s context window and outperforming vanilla frontier LLMs and common long-context scaffolds across four long-context tasks. Beyond long-context answering, recent results demonstrate that RLMs are a powerful paradigm for a wide variety of challenging tasks.

## Reasoning & Tool Use — A Brief History

Reasoning and tool use are related, but they are not the same thing.

Reasoning is about how well a model can allocate inference-time compute to a problem: break it down, explore alternatives, verify intermediate steps, backtrack, and choose a better answer. Early reasoning gains came from methods like chain-of-thought, self-consistency, and later tree-search-style prompting. Those methods improve how the model thinks even when it never touches the outside world.

Tool use is about whether a model can decide to call an external function, search engine, calculator, browser, code runner, or UI action; pass the right arguments; interpret the result; and continue. That is partly a reasoning problem, but it is also an interface and reliability problem: schemas, argument formatting, retries, stop conditions, state tracking, and error recovery. Toolformer made this distinction especially clear by treating tool use as something a model could learn during generation.

Historically, the timeline looks roughly like this:

**2022: reasoning first, mostly without tools.**  
Chain-of-thought prompting showed that asking models to generate intermediate reasoning steps could dramatically improve multi-step reasoning. Self-consistency pushed this further by sampling multiple reasoning paths and selecting the most consistent answer. The key lesson was that a large share of “reasoning” gains could come from spending more inference-time compute on the same prompt, not just from adding more knowledge.

- Chain-of-Thought Prompting Elicits Reasoning in Large Language Models — [https://arxiv.org/abs/2201.11903](https://arxiv.org/abs/2201.11903)
- Self-Consistency Improves Chain of Thought Reasoning in Language Models — [https://arxiv.org/abs/2203.11171](https://arxiv.org/abs/2203.11171)

**Late 2022: the first real bridge between reasoning and acting.**  
ReAct was the key milestone. It framed the model as alternating between reasoning traces and external actions such as retrieval or environment interaction. This was the moment the field started to see tool use not as a one-off API call, but as a loop in which reasoning selects actions and tool outputs reshape the next reasoning step.

- ReAct: Synergizing Reasoning and Acting in Language Models — [https://arxiv.org/abs/2210.03629](https://arxiv.org/abs/2210.03629)

**2023: tool use becomes an API discipline, not just a prompting trick.**  
Toolformer argued that models could learn when to call tools, which tools to call, and how to incorporate the results. Around the same time, vendors began standardizing function-calling interfaces. OpenAI’s June 2023 function calling release was a major product milestone because it made structured tool invocation reliable enough for developers to build on. This improved tool-use reliability faster than it improved deep reasoning.

- Toolformer: Language Models Can Teach Themselves to Use Tools — [https://arxiv.org/abs/2302.04761](https://arxiv.org/abs/2302.04761)
- OpenAI, “Function calling and other API updates” — [https://openai.com/index/function-calling-and-other-api-updates/](https://openai.com/index/function-calling-and-other-api-updates/)

**2023 also deepened the separation between reasoning and tool use.**  
Tree of Thoughts made it even clearer that inference-time reasoning could improve through internal search alone. It let models explore multiple candidate thought branches, look ahead, and backtrack. That is search over reasoning traces. It can be paired with tools, but it does not require them.

- Tree of Thoughts: Deliberate Problem Solving with Large Language Models — [https://arxiv.org/abs/2305.10601](https://arxiv.org/abs/2305.10601)

**2024: reasoning models become their own product category.**  
OpenAI’s o1 launch was the clearest signal. The company described o1 as a model family designed to “spend more time thinking before they respond,” and the initial API announcement explicitly noted that features like function calling were not yet included. That was strong evidence that, product-wise, reasoning and tool use were still separable.

- OpenAI, “Introducing OpenAI o1-preview” — [https://openai.com/index/introducing-openai-o1-preview/](https://openai.com/index/introducing-openai-o1-preview/)
- OpenAI, “Introducing OpenAI o1” — [https://openai.com/o1/](https://openai.com/o1/)

**2024 is also when agentic tool use got much more serious.**  
Anthropic’s Claude 3.5 Sonnet emphasized stronger tool use for coding and agentic tasks, and later in 2024 Anthropic introduced computer use: a model interacting with a real computer via screenshots, mouse, and keyboard. This is a good example of the two axes starting to merge into one agentic stack.

- Anthropic, “Introducing computer use, a new Claude 3.5 Sonnet, and Claude 3.5 Haiku” — [https://www.anthropic.com/news/3-5-models-and-computer-use](https://www.anthropic.com/news/3-5-models-and-computer-use)
- Anthropic, “Developing a computer use model” — [https://www.anthropic.com/news/developing-computer-use](https://www.anthropic.com/news/developing-computer-use)

**Late 2024 into 2025: vendors start presenting tool use as native, but still distinct from thinking.**  
Google’s Gemini 2.0 messaging explicitly framed the model family around the “agentic era” and native tool use, while keeping “thinking” as a distinct capability for harder multi-step planning. That split mirrors the real architecture: one layer governs deliberation, another governs interaction with external affordances.

- Google, “Google Gemini AI update, December 2024” — [https://blog.google/technology/google-deepmind/google-gemini-ai-update-december-2024/](https://blog.google/technology/google-deepmind/google-gemini-ai-update-december-2024/)

RLMs are the abstraction where that split finally collapses. The past ~6 months of results are what make the case concrete.

## Recent RLM Results

The arc of RLM results moves through three successive failure modes of the single forward pass: **long context**, then **memory**, then **long reasoning**. Each has been demonstrated by its own benchmark — [Oolong](https://arxiv.org/abs/2511.02817), [LongMemEval](https://arxiv.org/abs/2410.10813), and [LongCoT](https://arxiv.org/abs/2604.14140) respectively — and RLM-style systems have posted leading numbers on all three. Just as importantly, the follow-up work is already splitting into two camps: work that strengthens the original RLM implementation, and work that argues the deeper win is broader **externalized program search** rather than recursion alone.

Part of what makes RLMs challenging to appreciate is that frankly there aren’t very many benchmarks that really showcase the differences. In particular, I don’t view Oolong and LongMemEval as having much correlation to performance on real world agentic tasks. LongCoT is much more exciting to me, but it is brand new and only time will tell how it holds up.

**2024: the memory target appears.**  
[LongMemEval](https://arxiv.org/abs/2410.10813) defines the benchmark for long-term interactive memory: 500 questions over sustained chat histories spanning extraction, multi-session reasoning, temporal reasoning, knowledge updates, and abstention. It matters here because it gives RLM-style systems a way to test whether recursive/tool-mediated processing can function as a *memory system*, not just a long-context hack.

- [LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory](https://arxiv.org/abs/2410.10813)

**October 2025: the original public RLM write-up lands.**  
In [Recursive Language Models](https://alexzhang13.github.io/blog/2025/rlm/), Alex Zhang introduces the core idea: treat the prompt as an external environment, manipulate it through a REPL, and recursively subquery models over slices of context. The post reports an unusually strong early result profile: a GPT-5-mini RLM beats GPT-5 by more than 2× on an Oolong split while being cheaper per query on average, beats ReAct + test-time indexing/retrieval on a BrowseComp-Plus-derived long-context research task, and does not visibly degrade even at 10M+ input tokens.

- [Recursive Language Models (original blog post)](https://alexzhang13.github.io/blog/2025/rlm/)

**November 2025: Oolong raises the bar for long-context reasoning.**  
[Oolong](https://arxiv.org/abs/2511.02817) is important because it measures something harder than needle-in-a-haystack retrieval: models have to analyze many local chunks and then aggregate them into a global answer. At release, GPT-5, Claude-Sonnet-4, and Gemini-2.5-Pro all score under 50% on both splits at 128K, making Oolong the clearest early benchmark for the kind of “context as workspace” reasoning RLM is trying to solve.

- [Oolong: Evaluating Long Context Reasoning and Aggregation Capabilities](https://arxiv.org/abs/2511.02817)

**December 2025: the arXiv paper formalizes RLM.**  
The [Recursive Language Models paper](https://arxiv.org/abs/2512.24601) turns the blog’s intuition into a general inference paradigm: prompts are externalized, the LM programmatically inspects and partitions them, and recursive subcalls become part of test-time compute. The headline results are strong: RLMs process inputs up to two orders of magnitude beyond model context windows, outperform vanilla frontier LLMs and common long-context scaffolds across four long-context tasks at comparable cost, and a fine-tuned RLM-Qwen3-8B improves 28.3% on average over its base model.

- [Recursive Language Models (arXiv, Dec. 2025; revised Jan. 2026)](https://arxiv.org/abs/2512.24601)

**February 2026: RLM starts posting real “memory” numbers.**  
In [Recursive Language Models as Memory Systems](https://raw.works/recursive-language-models-as-memory-systems/), I reported early LongMemEval results with DSPy.RLM: 87.2% for a baseline Gemini 3 Flash setup, 89.2% with tools + a delegation prompt, and 89.8% with an observational-memory-style structured scaffold. That was a public Top-5-ish result at the time, below Mastra’s 94.87% but already strong evidence that RLM can act as a competitive memory system without a classical retrieval stack. In [ypi: a recursive coding agent](https://raw.works/ypi-a-recursive-coding-agent/), I show an earlier tool-use REPL path scoring 77.6% on LongMemEval — a useful datapoint because it shows the gradient from “tool-using agent” to “true recursive scaffold” inside the same implementation lineage.

- [Recursive Language Models as Memory Systems](https://raw.works/recursive-language-models-as-memory-systems/)
- [ypi: a recursive coding agent](https://raw.works/ypi-a-recursive-coding-agent/)
- [Observational Memory: 95% on LongMemEval](https://mastra.ai/research/observational-memory)

**March 2026: follow-up papers clarify both the strengths and the limits.**  
[Think, But Don’t Overthink](https://arxiv.org/abs/2603.02615) reproduces RLM and finds that depth-1 recursion helps on Oolong, but deeper recursion can “overthink,” hurting accuracy and exploding runtime and token cost. [Recursive Language Models Meet Uncertainty](https://arxiv.org/abs/2603.15653) pushes a sharper critique: recursion itself is not the whole secret, and uncertainty-aware self-reflective program search can improve up to 22% over RLM under the same time budget. Then [Coding Agents are Effective Long-Context Processors](https://arxiv.org/abs/2603.20432) generalizes the broader thesis: off-the-shelf coding agents outperform published SOTA by 17.3% on average, and on Oolong-Synthetic / Oolong-Real their reported scores (71.75 / 33.73) exceed the paper’s RLM baselines (64.38 / 23.07). That does not really refute RLM; it suggests RLM was the first clearly articulated expression of a larger family of executable, tool-mediated long-context reasoning systems.

- [Think, But Don’t Overthink: Reproducing Recursive Language Models](https://arxiv.org/abs/2603.02615)
- [Recursive Language Models Meet Uncertainty: The Surprising Effectiveness of Self-Reflective Program Search for Long Context](https://arxiv.org/abs/2603.15653)
- [Coding Agents are Effective Long-Context Processors](https://arxiv.org/abs/2603.20432)

**April 2026: the theory catches up to the results.**  
In [The Mismanaged Geniuses Hypothesis](https://alexzhang13.github.io/blog/2026/mgh/), Zhang reframes the whole arc: RLM is not just a benchmark trick for long prompts, but a more expressive scaffold for plans written through code execution, recursive subcalls, and tools-as-functions. That is a useful conceptual update because it connects the empirical results back to the bigger claim: reasoning performance is starting to look less like a property of a single forward pass and more like a property of how well a model can manage executable external computation.

- [The Mismanaged Geniuses Hypothesis](https://alexzhang13.github.io/blog/2026/mgh/)

The empirical case moves just as quickly.

**April 2026: the benchmark story shifts from long context to long reasoning.**  
[LongCoT](https://arxiv.org/abs/2604.14140) introduces 2,500 expert-designed problems for long-horizon chain-of-thought reasoning. At release, the best published models are still under 10% accuracy (GPT-5.2 at 9.8%, Gemini 3 Pro at 6.1%), which makes it an ideal test for whether recursive scaffolds are merely “good at reading long context” or whether they genuinely unlock *reasoning depth*.

- [LongCoT: Benchmarking Long-Horizon Chain-of-Thought Reasoning](https://arxiv.org/abs/2604.14140)

**April 2026: RLM immediately breaks LongCoT open.**  
In [LongCoT — A benchmark worthy of a RLM’s attention](https://raw.works/longcot-a-benchmark-worthy-of-a-rlms-attention/), I showed Claude Sonnet 4.5 + DSPy.RLM reaching **45.4%** on LongCoT-Mini versus **2.6%** for the same model without recursion/tools. Then in [RLMs are SOTA on LongCoT](https://raw.works/rlms-are-sota-on-longcot/), I show the scaffold doing almost all of the lifting for small open models: Qwen3-8B jumps from **0/507** to **33/507 (6.5%)** on LongCoT-Mini; Qwen3.5-9B + DSPy.RLM reaches **15.69%** on full LongCoT, about **1.6×** GPT-5.2 on the same slice; and Qwen3.5-27B + DSPy.RLM reaches **22.18%**, more than **2×** GPT-5.2. If these numbers hold up, they are some of the clearest evidence yet that recursive scaffolds can manufacture reasoning performance that is not visible in the base model alone.

- [LongCoT — A benchmark worthy of a RLM’s attention](https://raw.works/longcot-a-benchmark-worthy-of-a-rlms-attention/)
- [RLMs are SOTA on LongCoT](https://raw.works/rlms-are-sota-on-longcot/)

The arc is now hard to ignore. Oolong gives the **long-context** failure mode. LongMemEval gives the **memory** version. LongCoT gives the **long-reasoning** version. Across all three, the recurring pattern is the same: when the task requires navigating, decomposing, and aggregating information over a structure that is too large or too entangled for one passive forward pass, recursive tool-mediated processing starts to look less like an implementation trick and more like the next reasoning paradigm.

## Challenges with RLMs

A new paradigm is not a clean paradigm. Reasoning models were scoffed at for being too expensive. Early tool calling reliability was horrible. Even some leading reasoning models today are pretty bad at function calling.

RLMs have their challenges. My earliest contributions to the standalone RLM package and the DSPy.RLM implementation were purely practical: budgets, timeouts, managing the recursion depth.

Recursion sounds cool but isn’t always a good thing. Remember those viruses that would make your browser open a million popups until your computer crashed?

Recursion can be scary.

[![Mario Zechner (@badlogicgames): “i’m scared” — in reply to ypi](https://raw.works/images/mario-zechner-im-scared.png)](https://x.com/badlogicgames/status/2022071738146988076)

The most obvious limitations right now are cost and time. RLMs are expensive. They can take a long time. Worse, in the naive implementation that time is unpredictable and unbounded, because the model is deciding for itself how to decompose the problem.

Cost and time will be solved. Use smaller or faster models for each sub-call, and balance the agent-native “self-similar” decomposition with deterministic control of the graph topology and timeline.

The harder challenge, or at least the challenge that is more interesting to me personally, is how to get the language models to “act recursively”.

Obviously the concepts of recursion are in the pre-training data. Clearly reasoning and parallel tool calling are behaviors that the post-training incentivizes. Sub-agents are arguably a close behavioral analog to RLMs. And yet anyone who has worked with RLMs will tell you that the models generally suck at behaving recursively. It is not in their nature to decompose their prompt into sub-queries for many other instances of themselves to help solve them.

## What’s next?

Well one obvious next step is to explicitly post-train the models in a RLM harness. Alex Zhang et al. are actively working in this area: [MIT OASYS on HuggingFace](https://huggingface.co/mit-oasys) (see e.g. [`mit-oasys/rlm-qwen3-8b-v0.1`](https://huggingface.co/mit-oasys/rlm-qwen3-8b-v0.1)).

But what is the reward function for “optimal recursion”? I suspect this is a multi-billion-dollar question.

The most surprising result to me from my last few days of experimenting was [how well very small models can do in RLM harnesses](https://raw.works/rlms-are-sota-on-longcot/). These models are small enough to run on consumer devices, which potentially means that they offer an opportunity to upset the current “balance of power” between the GPU-rich and GPU-poor.

Yes, more money means you can run more. The best GPUs will always be faster. A RLM of Opus is smarter than a RLM of Llama 3. But I cannot help but feel excited and empowered to believe that an individual or consortium running many instances of small models on affordable/legacy/local compute infrastructure can now access model capabilities that are on par with or exceeding those of the most expensive LLMs from the frontier labs. If that is even directionally right, the frontier stops being a place only the largest labs can reach.

## Getting Started with RLMs

Here are just a few of the many ways to get started with RLMs:

- [**alexzhang13/rlm**](https://github.com/alexzhang13/rlm) — the reference implementation from Alex Zhang and the RLM paper authors; the cleanest place to read the core recursion loop.
- [**dspy.RLM**](https://dspy.ai/api/modules/RLM/) — the DSPy integration, which exposes RLM as a composable module inside larger DSPy programs and is what I’ve been using for most of my own experiments.
- [**ax-llm/ax**](https://github.com/ax-llm/ax) — a TypeScript DSPy-style framework with first-class RLM support via `AxAgent` -driven recursive decomposition, bounded sub-queries, and a persistent JS runtime.
- [**rawwerks/rlm-cli**](https://github.com/rawwerks/rlm-cli) — my CLI wrapper around `rlm` with directory-as-context, JSON-first output, and self-documenting commands, for running RLMs against local repos and folders.
- [**rawwerks/ypi**](https://github.com/rawwerks/ypi) — my recursive coding agent built on [Pi](https://github.com/badlogic/pi-mono): one `rlm_query` tool, one `rlm_map` fanout helper, and per-child `jj` workspaces for isolated recursive execution.

## P.S.

I almost forgot: fractals.

[![Lobster mandelbulb](https://raw.works/images/lobster-mandelbulb.png)](https://x.com/raw_works/status/2022010444492517469)

A few days ago I showed [Sonnet 4.5 + `dspy.RLM` hitting 45.4% on LongCoT-Mini](https://raw.works/longcot-a-benchmark-worthy-of-a-rlms-attention/). Exciting results, but a bit pricey for my taste.

So I set out to see what might be possible with some very small models.

First, I wanted to run a 3x2 comparison matrix of doing LLM vs. [RLM](https://github.com/alexzhang13/rlm) vs. [DSPy.RLM](https://dspy.ai/api/modules/RLM/) for both [Qwen 3 8B](https://huggingface.co/Qwen/Qwen3-8B) and the [MIT OASYS RLM finetune](https://huggingface.co/mit-oasys/rlm-qwen3-8b-v0.1).

I will need to save the full analysis for another day (I wasn’t really able to get the finetuned model working), but the meaningful result is that on [LongCoT](https://longcot.ai/) mini, DSPy.RLM can take Qwen 3 8B Instruct from literally 0/507 correct to 33/507 (6.5%). This would be #7 on the leaderboard, from an 8B model!

So my immediate next thought was: “what about Qwen 3.5 9B”? This hit 17.2% on LongCoT mini (3rd place), and was so cheap that I decided to run the full benchmark (all 2500 questions)! (Now using Together AI via OpenRouter, I don’t think their endpoint is quantized but I’m not 100% sure.)

Surprisingly, DSPy.RLM with Qwen 3.5 9B is comfortably SOTA on the full LongCoT at 15.69%, outdoing GPT 5.2 by ~1.6x.

Now I was having too much fun, so I had to run Qwen 3.5 27B (this time via Alibaba Cloud via OpenRouter)…and unsurprisingly, a new LongCoT full king is crowned at 22.18%.

I’m really excited to finally have a meaningful benchmark that can clearly demonstrate the power of RLMs. This clearly deserves a much longer writeup, which I hope to post soon! (And I’m now running [Qwen 3.6 35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B) at the suggestion of many folks on X.)

After [the LongMemEval experiments in February](https://raw.works/recursive-language-models-as-memory-systems/), I’ve been hungry to find a better benchmark that will actually showcase the power of recursive language models (RLMs) on useful tasks. [LongCoT](https://longcot.ai/) is exactly that: a benchmark built to stress-test long-horizon reasoning.

As soon as I saw the benchmark, I aimed [DSPy.RLM](https://dspy.ai/api/modules/RLM/) at it. (Even before [reading the paper](https://arxiv.org/abs/2604.14140).)

## The setup

- **Model:** `claude-sonnet-4-5` for both conditions. Same `max_tokens=64000`, same judge models, same prompts.
- **RLM:** stock `dspy.RLM` 3.1.3, `max_iterations=50`, default Pyodide REPL, `sub_lm=lm`.
- **Vanilla:** raw Anthropic SDK, single user message, no tools. Leaderboard shape.
- **Dataset:** LongCoT-Mini, all 500 questions (easy slices across logic / cs / chemistry / chess / math).

The entire RLM surface area is one dspy Signature:

```python
class LongCoTSolve(dspy.Signature):
    """Solve a LongCoT problem.

    The \`prompt\` already contains the full problem statement and the answer
    format requirement (always ends with \`solution = ...\`). Reason through
    the problem with the available REPL, then return the final response —
    which MUST contain the literal \`solution = ...\` line as instructed.
    """

    prompt: str = dspy.InputField(desc="Full LongCoT problem prompt with answer-format instructions")
    response: str = dspy.OutputField(desc="Full final response containing the required \`solution = ...\` line")
```

## The headline

|  | Vanilla | RLM |
| --- | --- | --- |
| Correct | 13 / 500 | **227 / 500** |
| Accuracy | 2.6% | **45.4%** |
| Captured cost | $31 | $621 |

On the full 500-row overlap: 219 wrong→right flips, 5 right→wrong, 268 both-wrong, 8 both-right. The vanilla 2.6% lines up with the published Sonnet 4.5 Mini number, so the control is calibrated, not sandbagged.

## Per-task

| Task | RLM | Vanilla |
| --- | --- | --- |
| Dungeon · Packaging · Hanoi · Wizards · TrapezoidCounting · Sudoku | 15/15 each (💯) | 0/15 each |
| BlocksWorld | 9/10 | 0/10 |
| Sokoban | 7/10 | 0/10 |
| Chess | **85/100** | 0/100 |
| Chemistry | 31/100 | 13/100 |
| cs / DistMem | 4/25 | 0/25 |
| cs / MaxFlow-MinCut + Hindley-Milner | **0/75** | 0/75 |
| math | **6/95** | 0/95 |

The pattern is coherent: RLM crushes anything whose dependency structure externalises cleanly to code. The orchestrator writes a short Python program, the REPL runs it, the answer comes out. Logic puzzles, Hanoi, Sudoku, chess with Pyodide’s `chess` module — all 💯 or near it.

The walls are the opposite picture. Hindley-Milner and MaxFlow-MinCut go 0/75 because the orchestrator can’t find a decomposition where subproblems can be usefully farmed out — exactly the “graph-structured dependencies” failure the paper calls out.

And math? The paper’s wall holds at least for now, for Sonnet 4.5. 6/95 on Mini isn’t zero, but it’s terrible. Sonnet 4.5 × dspy.RLM replicates the paper’s math result on a different model and split.

## What I think this means for the paper

The paper’s RLM discussion is genuinely thin — one paragraph, one figure, no dedicated table. With that as the bar, cross-model replication is useful:

- **Logic, chess, CS wins: replicate and amplify.** Same shape on a different frontier model.
- **Math stays at zero: maybe?** Model swap doesn’t rescue it. But it’s also from a baseline of 6 so you can argue it’s either modest or infinite improvement.
- **Chemistry lifts modestly** (13 → 31), which is the only spot where I’d push back on the paper’s phrasing — but I’m both a chemist and RLM addict.

P.S. - RLMs are expensive, and supposedly the 500-problem mini version is the *easy* subset of the full 2500-problem set. So…who wants to fund the Opus 4.7 run?

Over the last 2 days, we’ve stumbled upon a really powerful coding agent interaction pattern: git notes as an underground information network.

[Git notes](https://git-scm.com/docs/git-notes) are both ubiquitous (part of git) and “invisible” (GitHub chose not to display them). This presents a very interesting communication channel for agents, who can now include rich details and discussions about the code without cluttering up the “visible” layer of the repo.

[mycelium](https://github.com/openprose/mycelium) is my tool to make these interactions easier.

```bash
# agent arrives, reads what's known about a file
mycelium.sh context src/auth.ts

# agent works...

# agent leaves a note explaining what it did
mycelium.sh note HEAD -k context -m "Refactored retry logic. See warning on auth.ts."
```

Agents read notes on arrival. They leave notes on departure. The network grows.

The CLI makes it easy to link notes and git refs together — files, commits, directories, even edges between notes. Notes can have kinds (`decision`, `warning`, `summary`, `context`) and edges (`depends-on`, `explains`, `warns-about`) but the vocabulary is open. The tool tries to stay unopinionated about the actual workflow. From the [SKILL.md](https://github.com/openprose/mycelium/blob/main/SKILL.md): “That’s the whole contract. How you work, what you build, how you talk to your user — that’s your business. Mycelium just asks you to read the breadcrumbs and leave new ones.”

mycelium is meant to be agent-native — load the SKILL.md into your agent framework and it teaches the convention. But it’s just git & bash, so it works with any agent in any git repo.

```bash
curl -fsSL https://raw.githubusercontent.com/openprose/mycelium/main/install.sh | bash
```

Still wrapping my head around the consequences of this, and very curious to hear your thoughts.

P.S. — this is the foundation of some very cool tools I’m collaborating with [OpenProse](https://openprose.ai/) on.

I built [ypi](https://github.com/rawwerks/ypi) — a recursive coding agent. It’s [Pi](https://github.com/badlogic/pi-mono) that can call itself.

The name comes from the [Y combinator](https://en.wikipedia.org/wiki/Fixed-point_combinator#Y_combinator) in lambda calculus — the fixed-point combinator that enables recursion. (“rpi” has other connotations.)

The idea was inspired by [Recursive Language Models](https://github.com/alexzhang13/rlm) (RLM), which showed that an LLM with a code REPL and a `llm_query()` function can recursively decompose problems, analyze massive contexts, and write code — all through self-delegation.

## The idea

Pi already has a bash REPL. I added one function — `rlm_query` — and a system prompt that teaches Pi to use it recursively. Each child gets its own [jj](https://martinvonz.github.io/jj/) workspace for file isolation. That’s the whole trick.

```
┌──────────────────────────────────────────┐
│  ypi (depth 0)                           │
│  Tools: bash, rlm_query                  │
│  Workspace: default                      │
│                                          │
│  > grep -n "bug" src/*.py                │
│  > sed -n '50,80p' src/app.py \          │
│      | rlm_query "Fix this bug"          │
│            │                             │
│            ▼                             │
│    ┌────────────────────────────┐        │
│    │  ypi (depth 1)            │        │
│    │  Workspace: jj isolated   │        │
│    │  Edits files safely       │        │
│    │  Returns: patch on stdout │        │
│    └────────────────────────────┘        │
│                                          │
│  > jj squash --from <child-change>       │
│  # absorb the fix into our working copy  │
└──────────────────────────────────────────┘
```

The recursion works like this: `rlm_query` spawns a child Pi process with the same system prompt and tools. The child can call `rlm_query` too:

```
Depth 0 (root)    → full Pi with bash + rlm_query
  Depth 1 (child) → full Pi with bash + rlm_query, own jj workspace
    Depth 2 (leaf) → full Pi with bash, but no rlm_query (max depth)
```

Each recursive child gets its own [jj workspace](https://martinvonz.github.io/jj/latest/working-copy/), so the parent’s working copy stays untouched. You review child work with `jj diff`, absorb it with `jj squash --from`.

## How it works

The architecture maps directly to the Python RLM library:

| Piece | Python RLM | ypi |
| --- | --- | --- |
| System prompt | `RLM_SYSTEM_PROMPT` | `SYSTEM_PROMPT.md` |
| Context / REPL | Python `context` variable | `$CONTEXT` file + bash |
| Sub-call function | `llm_query("prompt")` | `rlm_query "prompt"` |

The key insight: Pi’s bash tool **is** the REPL. `rlm_query` **is** `llm_query()`. No bridge needed.

## Guardrails

Recursive agents without guardrails will burn through your API budget. ypi has several:

| Feature | Env var | What it does |
| --- | --- | --- |
| Budget | `RLM_BUDGET=0.50` | Max dollar spend for entire recursive tree |
| Timeout | `RLM_TIMEOUT=60` | Wall-clock limit for entire recursive tree |
| Call limit | `RLM_MAX_CALLS=20` | Max total `rlm_query` invocations |
| Model routing | `RLM_CHILD_MODEL=haiku` | Use cheaper model for sub-calls |
| Depth limit | `RLM_MAX_DEPTH=3` | How deep recursion can go |
| Tracing | `PI_TRACE_FILE=/tmp/trace.log` | Log all calls with timing + cost |

The agent can check its own spend at any time:

```bash
rlm_cost          # "$0.042381"
rlm_cost --json   # {"cost": 0.042381, "tokens": 12450, "calls": 3}
```

## The path here

ypi went through four approaches before landing on the current design:

1. **Tool-use REPL** — Pi’s `completeWithTools()`, ReAct loop. Got 77.6% on LongMemEval.
2. **Python bridge** — HTTP server between Pi and Python RLM. Too complex.
3. **Pi extension** — Custom provider with search tools. Not true recursion.
4. **Bash RLM** — `rlm_query` + `SYSTEM_PROMPT.md`. True recursion via bash. This is the one that stuck.

## Try it

```bash
curl -fsSL https://raw.githubusercontent.com/rawwerks/ypi/master/install.sh | bash
```

Or via npm/bun:

```bash
npm install -g ypi
ypi "What does this repo do?"
```

Or without installing:

```bash
bunx ypi "Refactor the error handling in this repo"
```

Code is at [github.com/rawwerks/ypi](https://github.com/rawwerks/ypi). It’s built on [Pi](https://github.com/badlogic/pi-mono) and inspired by [RLM](https://github.com/alexzhang13/rlm).

My morning’s notes from yesterday:

![screenshot](https://raw.works/recursive-language-models-as-memory-systems/images/screenshot.png)

As I was waiting for Claude Code to help me with my goal of modifying DSPy to be able to “RLM everything”, I came across [this result from Mastra.AI](https://mastra.ai/blog/observational-memory) which describes a SOTA result on [LongMemEval](https://arxiv.org/abs/2410.10813) using an “observational memory” pre-processing approach.

As you can see, my thought was “maybe [RLM](https://arxiv.org/abs/2512.24601) will blow this out of the water?” I wasn’t able to find a public result of LongMemEval using Recursive Language Models, so I decided to explore it myself.

The initial results with Gemini 3 Flash Preview and the [standalone RLM package](https://github.com/alexzhang13/rlm) weren’t great, but in the past I had noticed that Flash struggled to grok the RLM concept. Gemini 3 Pro fared much better.

Surprisingly - the additional structure enforced by [DSPy.RLM](https://dspy.ai/learn/programming/modules/) was a huge boost, enabling Gemini 3 Flash to match Pro with the regular RLM package.

Most of the rest of the day’s experiments were less successful. I was able to eke out a few more points by attempting to re-create Mastra’s “Observational Memory” as a Pydantic type enforced by DSPy, but unfortunately a few hundred dollars worth of GEPA optimizations didn’t bear any additional fruit.

Surprisingly - with the full structure of DSPy.RLM and the structured observation, Gemini 3 Pro is not actually any better on this benchmark.

Here’s a summary of our experiments:

| # | Experiment | Model | Score | Cost/q | Notes |
| --- | --- | --- | --- | --- | --- |
| 1 | dspy.RLM baseline | Gemini 3 Flash | 87.2% | ~$0.01 | Huge boost over standalone RLM with Flash (58%) |
| 2 | \+ session tools (naive) | Gemini 3 Flash | 87.3% | $0.032 | Context rot: +31 flips, -32 regressions = net zero |
| 3 | \+ tools + delegation prompt | Gemini 3 Flash | 89.2% | $0.031 | “Don’t read sessions yourself, delegate” |
| 4 | \+ observational memory (Pydantic) | Gemini 3 Flash | **89.8%** | $0.035 | **Our best.** Typed observations force structured reasoning |
| 5 | GEPA prompt optimization | Gemini 3 Flash | 87.8% | $0.042 | Regressed. ~$400 spent. Overfits to small val sets |
| 6 | Observational memory | Gemini 3 Pro | ~89.6% | ~$0.20 | Pro ≈ Flash with this scaffold |

And here’s how that stacks up on the [LongMemEval](https://arxiv.org/abs/2410.10813) leaderboard:

| # | System | Model | Score | Source |
| --- | --- | --- | --- | --- |
| 1 | [Mastra Observational Memory](https://mastra.ai/blog/observational-memory) | GPT-5-mini | **94.87%** | [mastra.ai/research](https://mastra.ai/research/observational-memory) |
| 2 | [Mastra Observational Memory](https://mastra.ai/blog/observational-memory) | Gemini 3 Pro | 93.27% | [mastra.ai/research](https://mastra.ai/research/observational-memory) |
| 3 | [Vectorize Hindsight](https://www.prnewswire.com/news-releases/vectorize-breaks-90-on-longmemeval-with-open-source-ai-agent-memory-system-302643146.html) | Gemini 3 Pro | 91.40% | Open-source |
| 4 | **dspy.RLM + obs. memory (ours)** | **Gemini 3 Flash** | **89.8%** | [github](https://github.com/rawwerks/longmemeval-rlm) |
| 5 | dspy.RLM + tools + delegation (ours) | Gemini 3 Flash | 89.2% | [github](https://github.com/rawwerks/longmemeval-rlm) |
| 6 | [Mastra Observational Memory](https://mastra.ai/blog/observational-memory) | Gemini 3 Flash | 89.20% | [mastra.ai/research](https://mastra.ai/research/observational-memory) |
| 7 | Standalone [RLM](https://github.com/alexzhang13/rlm) | Gemini 3 Pro | 87.0% | [github](https://github.com/rawwerks/longmemeval-rlm) |

Not bad for a day’s work, we were able to demonstrate a “Top-5” LongMemEval result with very minimal modifications to dspy.RLM, just some helper functions to process the “multi-chat” sessions.

I think this demonstrates a few exciting things:

1. RLMs can be very powerful memory systems without any pre-processing.
2. The structured output enforced by the DSPy.RLM implementation is helpful for keeping (at least these Gemini models) “on the rails” vs. the more freeform standalone RLM package.
3. Very fast and inexpensive models can achieve near-SOTA results inside the RLM scaffolding, and more speculatively…
4. …perhaps RLM as a test-time scaling method is “orthogonal” to model size, in the same way that reasoning models with built-in CoT were able to eke out gains separately from model parameter count.

P.S. — Several improvements to DSPy.RLM were developed during this work and submitted upstream: [stanfordnlp/dspy#9295](https://github.com/stanfordnlp/dspy/pull/9295)

I’m noticing an inversion of caution between the LLMs themselves and the behavior in their official coding agent harnesses.

Claude.ai is very cautious and PC, but Claude Code with skipped permissions will happily plow through obstacles, getting shit done for sure, but perhaps bricking your machine or posting your private data somewhere public or just wrecking your git repo.

ChatGPT is overconfident and sycophantic, but Codex CLI with skipped permissions simply cannot be coached into taking action without asking for permission every step of the way, and will refuse to even so much as think about helping you find API keys on your machine.

Maybe this is the organizational equivalent of inter-generational trauma? Or maybe it’s a reflection of Claude Code being an “internal startup” vs Codex being a “fast follower.”

Inspired by last week’s research report from [Jude Gao](https://x.com/gao_jude) - [“AGENTS.md outperforms skills in our agent evals”](https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals) - this weekend my agents worked hard to make [dirpack](https://github.com/rawwerks/dirpack).

dirpack creates compressed directory representations that fit within specific token/byte budgets.

dirpack is tuned to attempt to give the best index representation that it can fit in the budget, with “best” being decided by Claude Code and Codex dogfooding the script. Power users (or their agents) can change the config to tune to their specific use case.

Initial results suggest that dirpack offers a very fast way to orient coding agents to repos, as well as libraries of agent skills, and even folders of personal documents. More experiments soon…

```bash
curl -fsSL https://raw.githubusercontent.com/rawwerks/dirpack/master/install.sh | bash
```

Or via cargo:

```bash
cargo install dirpack
```

Curious for feedback from you and your agents!

After years of being frustrated by the inability of AI to read my handwritten notes, I am frankly shocked to report that this morning Claude Opus 4.5 simply one-shotted my crappy handwriting.

The singularity is nigh…

![](https://raw.works/images/opus-handwriting-notes-og.jpg)

My handwritten notes from 12.4.25

Here’s what Claude transcribed:

> **12.4.25**
> 
> It sucks that even deep research is just filled with slop, because google is filled with slop.
> 
> Benchmarking (private /ungameable) will become increasingly more valuable.
> 
> Evals. actually

The faint text visible below is bleed-through from writing on the reverse side of the page, not additional notes - and Claude correctly identified that too.

(This is subliminally a commercial for [Hamel Husain](https://twitter.com/HamelHusain) and [Shreya Shankar](https://twitter.com/sh_reya) ’s [course](https://maven.com/parlance-labs/evals), because: Evals. actually)

**Update:** Gemini 3 Pro Preview also one-shotted these notes.

> I’m often asked how big my company is—how many people I employ full-time. The answer is one. Most people lose interest at that point.

It is not crazy to imagine a company with no employees. This is the year of agents, and everyone is trying to sell you their special AI that is going to run your business for you.

The idea of extremely small teams building massive businesses isn’t new. [Roy Bahat argued in 2015](https://also.roybahat.com/the-billion-dollar-one-person-startup-d5a615a8abb9) that a single person could build a $1B company as software and cloud infrastructure reduced the need for employees. Since then, [Sam Altman has talked about betting pools](https://fortune.com/2024/02/04/sam-altman-one-person-unicorn-silicon-valley-founder-myth/) for the first one-person billion-dollar company, and [Dario Amodei has predicted](https://www.inc.com/ben-sherry/anthropic-ceo-dario-amodei-predicts-the-first-billion-dollar-solopreneur-by-2026/91193609) we’ll see a one-employee $1B company by 2026.

Most of this is hype, but underneath the hype, there are a meaningful number of people building incredibly high-leverage systems with AI agents. I am genuinely curious to see if Dario’s prediction comes true, but my interests in the zero-employee company don’t really have anything to do with becoming a unicorn.

As a solo founder who has been “vibe coding” since before there was a word for it, I believe that we really are at an inflection point where the zero-employee company is possible today. At the current pace of AI – if not today, then by the end of the year.

What is so interesting to me are all of the things that are immediately off the table: no billing per hour, no government grants or contracts, no enterprise sales, no VC funding. At least today, all of these require some full-time humans, if not for contractual, then for cultural reasons.

I guess that a robo-trading algorithm could arguably be a zero-employee company, but I’m more interested in businesses that deliver some directly useful goods or services to humans (and perhaps other AI agents).

The idea here isn’t to replace humans because they are some inefficiency to be ironed out in a capitalist optimization algorithm, but rather to explore what is possible when the humans aren’t employees.

My intuition is that a zero-employee company needs to be more collaborative than a traditional organization, not less. Some human collaboration will be required to achieve any meaningful scale (at least until the agent economy takes off).

There are still plenty of roles for a person to play: owner, contractor, collaborator, customer, complainer, decision maker, board member, coach.

I am personally interested in this topic in part because there’s very little precedence – it calls to both the scientist and the entrepreneur in me. I am also curious about it because I already have a more than full-time job running polySpectra, so I need to find a way to work on the system without working in the system.

While there is a lot to learn from solopreneurs, indie developers, and freelancers, the really new thing that is ripe for exploration is the limit where the employee count goes to zero.

It’s important to do a bit of a pre-mortem for this experiment.

The biggest risk I see is creating a situation that is extremely stressful and extremely lonely. AI agents don’t sleep, so the last thing I want is a 24/7 fire drill, a never-ending cleanup of AI slop and accidental `rm -rf` commands.

Similarly, there’s no one to keep you company in a zero-employee firm. It’s sort of weird to even call it a company. There’s no one to vent to and no one to celebrate with. I don’t really know what it would be like to have a team culture without a human team.

I think there are two very likely failure modes of the experiment.

Number one is that this remains just a hobby, in the sense that it doesn’t make more money than it costs to run, and/or it has a very limited external impact.

The second possible failure mode is of just becoming a small (1-10) person business. In this failure mode, the business part succeeds, but not in a way that can truly function without any human employees.

Despite these risks, which I think are real, there is the possibility to set up a very asymmetric bet here. You could call it antifragile, perhaps.

The overhead of a zero employee company is extremely low.

Many people could afford to bankroll a zero-employee company. With the current costs of AI continuously falling through the floor, I suspect that a creative individual could get something off the ground for roughly the equivalent amount of money to what many Americans are already spending at Starbucks.

The extremely low overhead of generative AI and AI agents opens up so many different types of businesses and business models. The downside is a drop in the bucket. The upside is clearly uncapped.
