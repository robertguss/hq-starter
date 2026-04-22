---
tags:
  - library
title: "Environments Hub: A Community Hub To Scale RL To Open AGI"
url: "https://www.primeintellect.ai/blog/environments"
company: [personal]
topics: []
created: 2026-04-22
source_type: raindrop
raindrop_id: 1692343495
source_domain: "primeintellect.ai"
source_type_raindrop: article
collection: "unsorted"
collection_id: -1
hydrated: true
hydrated_at: 2026-04-22
hydrated_via: defuddle
---
## Excerpt

RL environments are the playgrounds where agents learn. Until now, they’ve been fragmented, closed, and hard to share. We are launching the Environments Hub to change that: an open, community-powered platform that gives environments a true home.Environments define the world, rules and feedback loop of state, action and reward. From games to coding tasks to dialogue, they’re the contexts where AI learns, without them, RL is just an algorithm with nothing to act on.

## Raw Content

<!-- Hydrated 2026-04-22 via defuddle -->

RL environments are the playgrounds where agents learn. Until now, they’ve been fragmented, closed, and hard to share. We are launching the Environments Hub to change that: an open, community-powered platform that gives environments a true home.

Environments define the world, rules and feedback loop of state, action and reward. From games to coding tasks to dialogue, they’re the contexts where AI learns, without them, RL is just an algorithm with nothing to act on.

Environments sit at the center of current AI progress. Each new one expands what we can train, study, and evaluate, making open models more competitive. By lowering the friction to build, share, and reuse environments, the Hub enables anyone in the world to contribute directly to open-source AGI progress.

In last week’s private beta, over 30 researchers and companies contributed environments to the Hub. Starting today, we’re opening it up to everyone - building the open alternative to the closed research tooling of big labs, with infra for RL, Reinforcement Fine-tuning (RFT), compute, and inference. We want to ensure that the next wave of startups, AI progress and adoption is built on open rails and open models, and not fed into the walled gardens of big labs, ultimately entrenching their lead.

![](https://www.youtube.com/watch?v=XT7k82bEz4o)

### Motivation

Most current discussion around RL environments centers on a wave of startups whose business model is to build and sell them exclusively to a handful of large closed labs.

This trend poses both a serious risk and an opportunity. If high-quality environments remain expensive and closed, open-source models will fall further behind. But if a robust ecosystem of open-source environments and training tools emerges, open-source can set the state of the art.

Right now, open research lacks the tools to study many of the questions big labs consider most critical. With this release, we aim to change that. The Environment Hub, together with the RL infrastructure we’re building around it, is designed to enable the next wave of startups and AI progress to be built on open rails and open models.

### Quick Links

- [Environments Hub](https://app.primeintellect.ai/dashboard/environments)
- [Environments Hub Documentation](https://docs.primeintellect.ai/tutorials-environments/environments)
- [prime CLI](https://github.com/PrimeIntellect-ai/prime-cli)
- [verifiers github](https://github.com/willccbb/verifiers)
- [verifiers docs](https://verifiers.readthedocs.io/en/latest/)
- [prime-rl github](https://github.com/primeintellect-ai/prime-rl)

## Features

## Developing and Sharing Environments

Create, manage and share environments for reinforcement learning and evaluation on the Environments Hub:

![Environments Hub](https://cdn.prod.website-files.com/66239f0441b09824acb92c7e/68af4fc26543577e13a7a8df_env-hub-overview.png)

## Evals

Create and explore evaluation reports for environments for various models.

![Evaluation Reports](https://cdn.prod.website-files.com/66239f0441b09824acb92c7e/68af4fd1e0df157c356e0b1b_evals.png)

## RL Training

Environments are natively supported in our scalable [https://github.com/PrimeIntellect-ai/prime-rl](https://github.com/PrimeIntellect-ai/prime-rl) trainer.

![Environments Support](https://cdn.prod.website-files.com/66239f0441b09824acb92c7e/68af4fe4ac828dbbbc85b31d_var0092.png)

## Sandboxes

We’re also launching sandboxes in beta that plug directly into Verifier Environments for secure code execution.

![Sandboxes](https://cdn.prod.website-files.com/66239f0441b09824acb92c7e/68af51de5486f781d66173f7_sandboxes.png)

## Contributors

A big thank you to all contributors during last week’s beta. Special shoutout to Arcee AI, [Hud.so](http://hud.so/), WhyPhy Labs, Groq, and the many individuals who contributed their first environments to the hub!

![Contributors](https://cdn.prod.website-files.com/66239f0441b09824acb92c7e/68af51f9d33899f790709e3c_contr.png)

With this launch, we’re also opening up a list of open and in-progress RFCs and bounties [here](https://docs.google.com/spreadsheets/d/13UDfRDjgIZXsMI2s9-Lmn8KSMMsgk2_zsfju6cx_pNU/edit?usp=sharing). The tasks we’re sourcing are intentional. We want to collectively build towards a state-of-the-art open INTELLECT-3 model in agentic and coding tasks.

Let us know if you'd like to claim a lock on one (via an initial draft PR / design doc) by messaging [Will](https://x.com/willccbb) or [Johannes](https://x.com/johannes_hage) on X or opening a PR to [https://github.com/PrimeIntellect-ai/prime-environments](https://github.com/PrimeIntellect-ai/prime-environments).

If you are interested in RL environments that don't have a bounty figure listed yet, just ask and we'll figure something out based on the difficulty scale we're using.

We are also opening up [applications](https://form.typeform.com/to/ibQawo5e) for novel environments and evals. Researchers accepted in this program will receive compute for running experiments, a stipend and support from our internal research team. Some moonshot examples of environments and evals we’d be especially excited about:

- Robust code-quality evaluations for agentic software engineering
- Evaluating usage of filesystems and memory for long-running tasks
- Adaptive coherent instruction-following for realistic multi-turn interactions
- High-quality creative writing and style adherence
- Generative generalist reward models with process critiques
- Harness and task design for interactive data science + machine learning, such as:
	- Environments for NanoGPT speedrun optimizations
		- Terminal-friendly data visualization
		- Research plan generation, with recent notable papers as golden targets

## Next Steps: Providing Full-Stack AGI Infrastructure

In the last months, we’ve made significant progress scaling agentic RL training to the largest open model sizes. With many crowdsourced environments feeding into INTELLECT-3, we are confident we can train a fully open, state-of-the-art agentic model.

Beyond INTELLECT-3, our focus with the Environments Hub is on making this infrastructure accessible to everyone: enabling researchers and startups alike to train models for their own tasks, integrate tools, run Reinforcement Fine-Tuning (RFT), and optimize agent scaffolds. Our entire stack is open-source ([prime-rl](https://github.com/PrimeIntellect-ai/prime-rl?utm_source=chatgpt.com)), and we are extending it to run seamlessly on top of our global compute supply.

We believe RL is not only the path to AGI, but also the foundation for building AI-native products. The most successful future startups will emerge by creating novel and differentiated environments tailored to their needs. Today, the biggest barrier is not access to models - trillion-parameter agentic models already exist - but the infrastructure and cost of training and serving them at scale. By lowering this barrier, we aim to give any AI builder cheap, seamless access to compute, inference, and training and the full stack rl infrastructure, unlocking more full stack AI startups and builders.

Our goal is to provide every researcher and company with access to an open RL infrastructure stack - currently locked behind the walls of closed labs.

If you’re excited to help shape the future of a truly sovereign open-source AI ecosystem, we’d love to hear from you and invite researchers and companies to:

- **Contribute**: Develop environments & evals for the Environments Hub. [Get Started](https://docs.primeintellect.ai/tutorials-environments/environments)
- **Collaborate**: We’re hiring engineers and researchers at the intersection of AI and distributed systems. [Careers](https://primeintellect.ai/careers)

### Q&A

Join the PI discord to discuss, share feedback, and ask any questions:)
