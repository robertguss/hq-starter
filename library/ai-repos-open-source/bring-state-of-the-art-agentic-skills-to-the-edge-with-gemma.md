---
tags:
  - library
title: "Bring state-of-the-art agentic skills to the edge with Gemma 4"
url: "https://developers.googleblog.com/bring-state-of-the-art-agentic-skills-to-the-edge-with-gemma-4/?utm_source=www.theunwindai.com&utm_medium=newsletter&utm_campaign=karpathy-s-autoresearch-for-agent-engineering&_bhlid=a0130544dce34974161fbde939d718ab8a468760"
company: [personal]
topics: []
created: 2026-04-06
source_type: raindrop
raindrop_id: 1674984935
source_domain: "developers.googleblog.com"
source_type_raindrop: article
collection: "AI Repos & Open Source"
collection_id: 69284315
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

Google DeepMind introduces Gemma 4, a family of state-of-the-art open models designed for on-device agentic workflows. Learn how to leverage multi-step planning, 140+ language support, and LiteRT-LM to build powerful, autonomous AI experiences across mobile, desktop, and IoT.

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: Bring state-of-the-art agentic skills to the edge with Gemma 4

URL Source: https://developers.googleblog.com/bring-state-of-the-art-agentic-skills-to-the-edge-with-gemma-4/?_bhlid=a0130544dce34974161fbde939d718ab8a468760

Published Time: 2026-04-02

Markdown Content:
APRIL 2, 2026

Today, Google DeepMind launched [**Gemma 4**](https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/), a family of state-of-the-art open models that redefine what is possible on your own hardware. Now available under the Apache 2.0 license, Gemma 4 gives developers a powerful toolkit for on-device AI development. With Gemma 4, you can now go beyond chatbots to build agents and autonomous AI use cases running directly on-device. Gemma 4 enables multi-step planning, autonomous action, offline code generation, and even audio-visual processing, all without specialized fine-tuning. It’s also built for a global audience with support for over 140 languages.

Sorry, your browser doesn't support playback for this video

Gemma 4 enables visual processing and support in >140 languages

We are excited to announce that you can experience Gemma 4’s expansive capabilities on the edge starting today! Access Android's built-in Gemma 4 model through the new [AICore Developer Preview](https://developers.google.com/ml-kit/genai/aicore-dev-preview), or leverage [Google AI Edge](https://ai.google.dev/edge) to build agentic, in-app experiences across mobile, desktop, and edge devices.

In this post, we’ll show you how to get started with Google AI Edge using both [Google AI Edge Gallery](https://github.com/google-ai-edge/gallery) and [LiteRT-LM](https://ai.google.dev/edge/litert-lm/overview).

### **Discover Agent Skills with Gemma 4 in Google AI Edge Gallery**

**Google AI Edge Gallery**, available on [iOS](https://apps.apple.com/us/app/google-ai-edge-gallery/id6749645337) and [Android](https://play.google.com/store/apps/details?id=com.google.ai.edge.gallery&hl=en_US), allows you to build and experiment with AI experiences that run entirely on-device. Today, we are thrilled to announce the launch of **Agent Skills**, one of the first applications to run multi-step, autonomous agentic workflows entirely on-device. Powered by Gemma 4, Agent Skills can:

*   **Augment the knowledge base**: Gemma 4 can access the information beyond its initial training data using skills to enable agentic enrichment type experiences. For example, you can build a skill to query Wikipedia, allowing the agent to query and respond to any encyclopedic question.

Sorry, your browser doesn't support playback for this video

Query Wikipedia or other knowledge sources

*   **Produce rich, interactive content**: Transform paragraphs or videos into concise summaries or flashcards for studying, or transform data into interactive visualizations or graphs. For example, you can create a skill that automatically summarizes and displays trends in hours of sleep and moods per day based on user speech input:

Sorry, your browser doesn't support playback for this video

Create graphs, flashcards, and other visualizations

*   **Expand Gemma 4's core capabilities**: Integrate with other models, such as text-to-speech, image generation, or music synthesis. For instance, you can utilize skills to pair photos with music that perfectly matches the mood.

Sorry, your browser doesn't support playback for this video

Integrate with other models to synthesize music and understand images

*   **Create****comprehensive end-to-end experiences**: Rather than navigating multiple apps, users can manage complex workflows and build their own applications entirely through conversation with Gemma 4. To illustrate this, we built a working app that describes and plays the vocal calls of animals.

Sorry, your browser doesn't support playback for this video

Build multi-step workflows and end-to-end experiences

To experience the Gemma 4 E2B and E4B models in action, check out the [Google AI Edge Gallery app](https://github.com/google-ai-edge/gallery) today. Within the app, it’s easy to start experimenting and creating your own skills with [our guide](https://github.com/google-ai-edge/gallery/tree/main/skills). We can’t wait to see what you build and share your skills in the Github [Discussion](https://github.com/google-ai-edge/gallery/discussions/categories/skills)!

### **Leverage Gemma 4 across devices with LiteRT-LM**

For developers who are interested in deploying Gemma 4 in-app or across a broader range of devices, [LiteRT-LM](https://ai.google.dev/edge/litert-lm/overview) provides stellar performance with reach across the entire hardware spectrum. LiteRT-LM adds GenAI specific libraries on top of [LiteRT](https://ai.google.dev/edge/litert), which is already trusted by millions of Android and edge developers with its high-performance libraries XNNPack and ML Drift. LiteRT-LM builds on this stack and enhances model performance with the following new features:

*   **Minimal Memory footprint:** Run Gemma 4 E2B using <1.5GB memory on some devices thanks to LiteRT’s support for 2-bit and 4-bit weights along with memory-mapped per-layer embeddings
*   **Constrained decoding**: Get structured, predictable outputs every time, ensuring your AI-driven apps and tool-calling scripts remain reliable in production.
*   **Dynamic context**: Flexibility to handle single models across CPUs and GPUs with dynamic context lengths, allowing you to take full advantage of the Gemma 4 128K context window.

To support the extended context lengths required by agentic use cases, LiteRT-LM leverages cutting-edge GPU optimizations to process **4,000 input tokens** across**2 distinct skills** in **under 3 seconds**.

LiteRT-LM also brings smaller Gemma 4 models to IoT & edge devices with compelling performance on a variety of platforms. These include the Raspberry Pi 5, where running on CPU, it reaches **133 prefill and 7.6 decode tokens/s**, while the NPU acceleration on the Qualcomm Dragonwing IQ8 boosts performance to a more impressive **3,700 prefill and 31 decode tokens/s**.

Ready to get started? Check out the [LiteRT-LM documentation](https://ai.google.dev/edge/litert-lm/overview) for a complete guide and device-specific performance metrics. You can also view the individual model cards for [Gemma 4 E2B](https://huggingface.co/litert-community/gemma-4-E2B-it-litert-lm) and [Gemma 4 E4B](https://huggingface.co/litert-community/gemma-4-E4B-it-litert-lm).

### **Run on any device**

Gemma 4 is available today with support across an unprecedented range of platforms:

*   **Mobile**: Available with CPU/GPU support across both Android and iOS. Developers can also access and deploy Android's built-in and optimized Gemma 4 model system-wide via Android AICore.
*   **Desktop and Web**: Seamless performance on Windows, Linux, and macOS (via Metal), plus native browser-based execution powered by WebGPU.
*   **IoT and robotics**: We are bringing Gemma 4 to the edge on **Raspberry Pi 5** and **Qualcomm Dragonwing IQ8 processor,**which also powers [**Arduino VENTUNO Q**](https://www.qualcomm.com/news/releases/2026/03/arduino-announces-arduino-ventuno-q----powered-by-qualcomm-drago).

Today, we are also launching a new Python package and CLI tool to make it easier than ever to experiment with Gemma in the console, and to power Gemma-based Python pipelines for IoT devices. The `litert-lm` CLI is available on **Linux, macOS, and Raspberry Pi**, enabling developers to try out the latest Gemma 4 model capabilities without writing any code. The CLI now also supports tool calling that powered Agent Skills in Google AI Edge Gallery. Python bindings for LiteRT-LM provide the flexibility to deeply customize your on-device LLM pipeline from Python. Getting started with LiteRT-LM in your terminal is simple using our [guide](http://ai.google.dev/edge/litert-lm/cli).

The era of agentic experiences on-device is here, and we hope you are excited to start building on the edge. Regardless of which device you are building on, get started with our [Agent Skills examples](https://github.com/google-ai-edge/gallery/tree/main/skills) in Google AI Edge Gallery, and [LiteRT-LM getting started guide](https://ai.google.dev/edge/litert-lm/overview). We can’t wait to see what you build!

### **Acknowledgements**

_We'd like to extend a special thanks to our_**_significant contributors_**_for their work on this project:_

_Advait Jain, Alice Zheng, Amber Heinbockel, Andrew Zhang, Byungchul Kim, Cormac Brick, Daniel Ho, Derek Bekebrede, Dillon Sharlet, Eric Yang, Fengwu Yao, Frank Barchard, Grant Jensen, Hriday Chhabria, Jae Yoo, Jenn Lee, Jing Jin, Jingxiao Zheng, Juhyun Lee, Lu Wang, Lin Chen, Majid Dadashi, Marissa Ikonomidis, Matthew Chan, Matthew Soulanille, Matthias Grundmann, Milen Ferev, Misha Gutman, Mohammadreza Heydary, Pradeep Kuppala, Qidong Zhao, Quentin Khan, Ram Iyengar, Raman Sarokin, Renjie Wu, Rishika Sinha, Rodney Witcher, Ronghui Zhu, Sachin Kotwani, Suleman Shahid, Tenghui Zhu, Terry Heo, Tiffany Hsiao, Tyler Mullen, Wai Hon Law, Weiyi Wang, Xiaoming Hu, Xu Chen, Yishuang Pang, Yi-Chun Kuo, Yu-Hui Chen, Zichuan Wei, and the gTech team._

[](https://developers.googleblog.com/subagents-have-arrived-in-gemini-cli/)
Previous

Next

[](https://developers.googleblog.com/closing-the-knowledge-gap-with-agent-skills/)
