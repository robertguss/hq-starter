---
tags:
  - library
title: "Autonomous Local Agents - Byterover"
url: "https://docs.byterover.dev/cookbook/autonomous-local-model"
company: [personal]
topics: []
created: 2026-04-15
source_type: raindrop
raindrop_id: 1685220768
source_domain: "docs.byterover.dev"
source_type_raindrop: article
collection: "AI Repos & Open Source"
collection_id: 69284315
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

Run your OpenClaw/Hermes agent and ByteRover memory system entirely on local models using LM Studio - no cloud API keys required.

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: Autonomous Local Agents - Byterover

URL Source: https://docs.byterover.dev/cookbook/autonomous-local-model

Markdown Content:
# Autonomous Local Agents - Byterover

[Skip to main content](https://docs.byterover.dev/cookbook/autonomous-local-model#content-area)

[Byterover home page![Image 4: light logo](https://mintcdn.com/byterover-d775e347/bilxWUswopsRO7Ve/logo/light.svg?fit=max&auto=format&n=bilxWUswopsRO7Ve&q=85&s=19379de8bfbfc914bdcc7024bd6a5249)![Image 5: dark logo](https://mintcdn.com/byterover-d775e347/bilxWUswopsRO7Ve/logo/dark.svg?fit=max&auto=format&n=bilxWUswopsRO7Ve&q=85&s=699fcf3c8f8da0ca3930f90173b99bfc)](https://byterover.dev/)

Search...

Ctrl K

*   [Support](mailto:support@byterover.dev)
*   [Dashboard](https://app.byterover.dev/)
*   [Dashboard](https://app.byterover.dev/)

Search...

Navigation

ByteRover Cookbook

Autonomous Local Agents

[Docs](https://docs.byterover.dev/)[Autonomous Agents](https://docs.byterover.dev/autonomous-agents/overview)[Changelog](https://docs.byterover.dev/changelog)[Archived (v2.6.0 and earlier)](https://docs.byterover.dev/archived/local-vs-cloud)

*   [Community](https://discord.gg/UMRrpNjh5W)
*   [Blog](https://byterover.dev/blog)

##### Getting Started

*   [Overview](https://docs.byterover.dev/)
*   [Quickstart](https://docs.byterover.dev/quickstart)
*   [Local vs Cloud](https://docs.byterover.dev/local-vs-cloud)
*   Common Workflows  

##### LLM Providers

*   [Overview](https://docs.byterover.dev/external-llm-providers/overview)

##### Agent Connectors

*   [Overview](https://docs.byterover.dev/connectors/overview)
*   [AI-Powered IDEs](https://docs.byterover.dev/connectors/ai-ides)
*   [Command Line Tools](https://docs.byterover.dev/connectors/cli-tools)
*   [Desktop Apps](https://docs.byterover.dev/connectors/desktop-apps)
*   [VS Code Extensions](https://docs.byterover.dev/connectors/vscode-extensions)

##### Context Tree

*   [Local Context Tree Structure](https://docs.byterover.dev/context-tree/local-space-structure)
*   [The Remote Space](https://docs.byterover.dev/context-tree/the-remote-space)
*   [How Curation Works](https://docs.byterover.dev/context-tree/curation-engine)
*   [How Query Works](https://docs.byterover.dev/context-tree/query-engine)
*   [Session Learning](https://docs.byterover.dev/context-tree/session-learning)
*   [Dreaming](https://docs.byterover.dev/context-tree/dreaming)
*   [Latency Improvement](https://docs.byterover.dev/context-tree/latency-improvement)

##### Knowledge Sharing

*   [Overview](https://docs.byterover.dev/knowledge-sharing/overview)
*   [Worktrees](https://docs.byterover.dev/knowledge-sharing/worktrees)
*   [Sources](https://docs.byterover.dev/knowledge-sharing/sources)

##### Memory Swarm

*   [Memory Swarm](https://docs.byterover.dev/memory-swarm/overview)
*   [Setup and Configuration](https://docs.byterover.dev/memory-swarm/setup)
*   [Swarm Query](https://docs.byterover.dev/memory-swarm/query)
*   [Swarm Curate](https://docs.byterover.dev/memory-swarm/curate)
*   [Provider Reference](https://docs.byterover.dev/memory-swarm/providers)

##### Git-Semantic Version Control

*   [Git-Semantic Version Control](https://docs.byterover.dev/git-semantic/overview)
*   [Getting Started](https://docs.byterover.dev/git-semantic/getting-started)
*   [Staging & Committing](https://docs.byterover.dev/git-semantic/staging-and-committing)
*   [Branching & Merging](https://docs.byterover.dev/git-semantic/branching-and-merging)
*   [Remote Sync](https://docs.byterover.dev/git-semantic/remote-sync)
*   [Command Reference](https://docs.byterover.dev/git-semantic/command-reference)
*   [Migration Guide](https://docs.byterover.dev/git-semantic/migration)

##### Review Changes

*   [Review Changes](https://docs.byterover.dev/review/overview)
*   [Manage Reviews](https://docs.byterover.dev/review/manage-reviews)
*   [Agent Review Workflow](https://docs.byterover.dev/review/agent-workflow)

##### BRV Hub

*   [Overview](https://docs.byterover.dev/brv-hub/overview)
*   [Custom Registries](https://docs.byterover.dev/brv-hub/registries)

##### Headless Mode

*   [Overview](https://docs.byterover.dev/headless-mode/overview)

##### Daemon-First Architecture

*   [Overview](https://docs.byterover.dev/daemon-first-architecture/overview)

##### Reference

*   [CLI reference](https://docs.byterover.dev/reference/cli-reference)

##### FAQs

*   [Overview](https://docs.byterover.dev/faqs/overview)
*   [General](https://docs.byterover.dev/faqs/general)
*   [Installation & Updates](https://docs.byterover.dev/faqs/installation-updates)
*   [Teams & Spaces](https://docs.byterover.dev/faqs/teams-spaces)
*   [Troubleshooting](https://docs.byterover.dev/faqs/troubleshooting)

##### Security

*   [Security & Infrastructure](https://docs.byterover.dev/security)

##### ByteRover Cookbook

*   [Overview](https://docs.byterover.dev/cookbook/overview)
*   [Autonomous Local Agents](https://docs.byterover.dev/cookbook/autonomous-local-model)

On this page

*   [Tested Configuration](https://docs.byterover.dev/cookbook/autonomous-local-model#tested-configuration)
*   [Step 1 — Download the Models](https://docs.byterover.dev/cookbook/autonomous-local-model#step-1-%E2%80%94-download-the-models)
*   [Step 2 — Load Both Models in LM Studio](https://docs.byterover.dev/cookbook/autonomous-local-model#step-2-%E2%80%94-load-both-models-in-lm-studio)
*   [Step 3 — Configure Your Agent](https://docs.byterover.dev/cookbook/autonomous-local-model#step-3-%E2%80%94-configure-your-agent)
*   [Step 4 — Configure ByteRover CLI](https://docs.byterover.dev/cookbook/autonomous-local-model#step-4-%E2%80%94-configure-byterover-cli)
*   [Step 5 — Verify ByteRover Is Working](https://docs.byterover.dev/cookbook/autonomous-local-model#step-5-%E2%80%94-verify-byterover-is-working)
*   [Step 6 — Enable ByteRover Memory Integration](https://docs.byterover.dev/cookbook/autonomous-local-model#step-6-%E2%80%94-enable-byterover-memory-integration)
*   [Reference](https://docs.byterover.dev/cookbook/autonomous-local-model#reference)

ByteRover Cookbook

# Autonomous Local Agents

Run your OpenClaw/Hermes agent and ByteRover memory system entirely on local models using LM Studio - no cloud API keys required.

This guide walks through running both OpenClaw and ByteRover CLI on local LLMs using [LM Studio](https://lmstudio.ai/).
## [​](https://docs.byterover.dev/cookbook/autonomous-local-model#tested-configuration)

Tested Configuration

| Component | Version / Details |
| --- | --- |
| Machine | Mac M4 Pro, RAM 24GB |
| LM Studio | 0.4.9 |
| OpenClaw | 2026.4.12 |
| ByteRover CLI | 3.3.0 |

This is an experimental setup. ByteRover and autonomous agents can run with OpenClaw on a Apple RAM 24GB machine, but for production usage we recommend at least an **Apple M4 with RAM 48GB**.

## [​](https://docs.byterover.dev/cookbook/autonomous-local-model#step-1-%E2%80%94-download-the-models)

Step 1 — Download the Models

Search for and download both GGUF files directly from LM Studio’s **Discover** tab.

1

[](https://docs.byterover.dev/cookbook/autonomous-local-model#)

Download Gemma 4 E4B for OpenClaw

Search for `unsloth/gemma-4-E4B-it-GGUF` and download `gemma-4-E4B-it-UD-Q4_K_XL.gguf`.![Image 6: Download Gemma 4 E4B in LM Studio](https://mintcdn.com/byterover-d775e347/JJP3GvbEXCqL5m62/images/cookbook/autonomous-local-model/cookbook-gemma4-download.png?fit=max&auto=format&n=JJP3GvbEXCqL5m62&q=85&s=fb2b0d0f4bc70e17a2df7adf987f6bed)

2

[](https://docs.byterover.dev/cookbook/autonomous-local-model#)

Download Qwen3.5-9B for ByteRover

Search for `unsloth/Qwen3.5-9B-GGUF` and download `Qwen3.5-9B-Q4_K_S.gguf`.![Image 7: Download Qwen3.5-9B in LM Studio](https://mintcdn.com/byterover-d775e347/JJP3GvbEXCqL5m62/images/cookbook/autonomous-local-model/cookbook-qwen3-5download.png?fit=max&auto=format&n=JJP3GvbEXCqL5m62&q=85&s=1aa66e28ba35a5bd9ff59027bcd5ab73)

On a 24 GB machine, both models fit in memory simultaneously. Gemma 4 E4B at Q4 uses ~8.7 GB and Qwen3.5-9B at Q4 uses ~10.5 GB.

## [​](https://docs.byterover.dev/cookbook/autonomous-local-model#step-2-%E2%80%94-load-both-models-in-lm-studio)

Step 2 — Load Both Models in LM Studio

LM Studio serves all loaded models from a single endpoint at `http://localhost:1234/v1`. Load both models before starting the server.

1

[](https://docs.byterover.dev/cookbook/autonomous-local-model#)

Open My Models

Go to the **Models** tab. You should see both downloaded models listed.![Image 8: LM Studio My Models screen](https://mintcdn.com/byterover-d775e347/JJP3GvbEXCqL5m62/images/cookbook/autonomous-local-model/cookbook-model-load-screen.png?fit=max&auto=format&n=JJP3GvbEXCqL5m62&q=85&s=88e5afbdc67767e4db6ba2225843fdb8)

2

[](https://docs.byterover.dev/cookbook/autonomous-local-model#)

Load Gemma 4 E4B

Click on `gemma-4-E4B-it-UD-Q4_K_XL.gguf` and click **Load**. Note the **API Identifier** — LM Studio assigns it `google/gemma-4-e4b`. This is the model ID you will use in OpenClaw’s config.![Image 9: Gemma 4 E4B load configuration](https://mintcdn.com/byterover-d775e347/JJP3GvbEXCqL5m62/images/cookbook/autonomous-local-model/cookbook-gemma4-load-configuration.png?fit=max&auto=format&n=JJP3GvbEXCqL5m62&q=85&s=42716d4b3fa6f11838f60af340162398)

3

[](https://docs.byterover.dev/cookbook/autonomous-local-model#)

Load Qwen3.5-9B

Click on `Qwen3.5-9B-Q4_K_S.gguf.gguf` and click **Load**. The API Identifier will be `qwen3.5-9b`.![Image 10: Qwen3.5-9B load configuration](https://mintcdn.com/byterover-d775e347/CwFsarNhiOxIuSd8/images/cookbook/autonomous-local-model/cookbook-qwen3-load-configuration.png?fit=max&auto=format&n=CwFsarNhiOxIuSd8&q=85&s=3289b90155714efb3e7e56c2dd66c065)

4

[](https://docs.byterover.dev/cookbook/autonomous-local-model#)

Verify both models are ready

Open the **Developer** tab. Both models should show **READY** status, reachable at `http://127.0.0.1:1234`.![Image 11: Both models loaded and ready in LM Studio Developer tab](https://mintcdn.com/byterover-d775e347/JJP3GvbEXCqL5m62/images/cookbook/autonomous-local-model/cookbook-local-model-load-success.png?fit=max&auto=format&n=JJP3GvbEXCqL5m62&q=85&s=c897a3407df97ef3182b31883a86147e)Confirm with:

```
curl http://localhost:1234/v1/models
```

The response should list both `google/gemma-4-e4b` and `qwen3.5-9b`.

## [​](https://docs.byterover.dev/cookbook/autonomous-local-model#step-3-%E2%80%94-configure-your-agent)

Step 3 — Configure Your Agent

Both OpenClaw and Hermes use the same local provider setup. Pick the agent you are using.

*    OpenClaw 
*    Hermes 

Run the OpenClaw onboard wizard:

```
openclaw onboard
```

1

[](https://docs.byterover.dev/cookbook/autonomous-local-model#)

Select Custom Provider

When prompted for **Model/auth provider**, scroll down and select **Custom Provider**.![Image 12: Select Custom Provider in OpenClaw onboard wizard](https://mintcdn.com/byterover-d775e347/JJP3GvbEXCqL5m62/images/cookbook/autonomous-local-model/cookbook-openclaw-local-model-select-local-LLM-provider.png?fit=max&auto=format&n=JJP3GvbEXCqL5m62&q=85&s=d08403274879f2c54c90d2a2093833ff)

2

[](https://docs.byterover.dev/cookbook/autonomous-local-model#)

Enter the endpoint details

Fill in the following when prompted:

| Field | Value |
| --- | --- |
| API Base URL | `http://localhost:1234/v1` |
| API Key | _(leave blank)_ |
| Endpoint compatibility | `OpenAI-compatible` |
| Model ID | `google/gemma-4-e4b` |
| Model alias | `google-gemma-4-e4b` |

The wizard verifies the endpoint and reports **Verification successful**.![Image 13: OpenClaw Custom Provider setup and verification](https://mintcdn.com/byterover-d775e347/JJP3GvbEXCqL5m62/images/cookbook/autonomous-local-model/cookbook-openclaw-local-model-setup.png?fit=max&auto=format&n=JJP3GvbEXCqL5m62&q=85&s=6ec930aaf72596ddf0e292efa28f94e6)

3

[](https://docs.byterover.dev/cookbook/autonomous-local-model#)

Start OpenClaw and verify

Launch OpenClaw. It will use `google/gemma-4-e4b` served by LM Studio at `localhost:1234`.![Image 14: OpenClaw running with local Gemma model](https://mintcdn.com/byterover-d775e347/JJP3GvbEXCqL5m62/images/cookbook/autonomous-local-model/cookbook-openclaw-local-model-sample-usage.png?fit=max&auto=format&n=JJP3GvbEXCqL5m62&q=85&s=d6123e1a69412fa92b314b774b38fda3)

**Context limit** — OpenClaw works normally 50,000 tokens and above. To update this, edit `openclaw.json` manually, then run `openclaw gateway restart` to apply changes.![Image 15: Context limit exceeded warning in OpenClaw](https://mintcdn.com/byterover-d775e347/JJP3GvbEXCqL5m62/images/cookbook/autonomous-local-model/cookbook-openlcaw-local-model-context-limit-excedded-issue.png?fit=max&auto=format&n=JJP3GvbEXCqL5m62&q=85&s=db0f1cba1b6bc60753d48c249ab6cc5b)

Resulting openclaw.json config

The wizard writes the following into `~/.openclaw/openclaw.json`. You can also add this manually:

```
{
  "models": {
    "mode": "merge",
    "providers": {
      "custom-localhost-1234": {
        "baseUrl": "http://localhost:1234/v1",
        "api": "openai-completions",
        "models": [
          {
            "id": "google/gemma-4-e4b",
            "name": "gemma-4-E4B-it (Local)",
            "contextWindow": 50000,
            "maxTokens": 50000,
            "input": ["text"],
            "cost": { "input": 0, "output": 0, "cacheRead": 0, "cacheWrite": 0 },
            "reasoning": false
          }
        ]
      }
    }
  },
  "agents": {
    "defaults": {
      "model": {
        "primary": "custom-localhost-1234/google/gemma-4-e4b"
      },
      "models": {
        "custom-localhost-1234/google/gemma-4-e4b": {
          "alias": "google-gemma-4-e4b"
        }
      }
    }
  }
}
```

Run the Hermes model setup wizard:

```
hermes setup model
```

1

[](https://docs.byterover.dev/cookbook/autonomous-local-model#)

Select Custom Provider

When prompted for the model provider, scroll down and select **Custom Provider (any OpenAI or Anthropic compatible endpoint)**.![Image 16: Select Custom Provider in Hermes setup wizard](https://mintcdn.com/byterover-d775e347/JJP3GvbEXCqL5m62/images/cookbook/autonomous-local-model/cookbook-hermes-local-model-select-custome-provider.png?fit=max&auto=format&n=JJP3GvbEXCqL5m62&q=85&s=5aa365efd367f2507f9b47c340d9e51a)

2

[](https://docs.byterover.dev/cookbook/autonomous-local-model#)

Enter the endpoint details

Fill in the following when prompted:

| Field | Value |
| --- | --- |
| API Base URL | `http://localhost:1234/v1` |
| API Key | _(leave blank)_ |
| Endpoint compatibility | `OpenAI-compatible` |
| Model ID | `google/gemma-4-e4b` |

![Image 17: Hermes local LLM provider configuration](https://mintcdn.com/byterover-d775e347/JJP3GvbEXCqL5m62/images/cookbook/autonomous-local-model/cookbook-hermes-local-model-select-local-LLM-provider.png?fit=max&auto=format&n=JJP3GvbEXCqL5m62&q=85&s=10c6f3c32cb0627bb69fc9ef1f66910e)The wizard confirms the endpoint and model are configured.![Image 18: Hermes local model setup complete](https://mintcdn.com/byterover-d775e347/JJP3GvbEXCqL5m62/images/cookbook/autonomous-local-model/cookbook-hermes-local-model-setup.png?fit=max&auto=format&n=JJP3GvbEXCqL5m62&q=85&s=c5217dca5ed325c21d5c781638301f3a)

3

[](https://docs.byterover.dev/cookbook/autonomous-local-model#)

Configure context length

Hermes will prompt you to set the context length. Set it to match the model’s context window (`65000` tokens for Gemma 4 E4B because hermes agent required minimum 64000 tokens).![Image 19: Hermes context length configuration](https://mintcdn.com/byterover-d775e347/JJP3GvbEXCqL5m62/images/cookbook/autonomous-local-model/cookbook-hermes-local-model-context-length.png?fit=max&auto=format&n=JJP3GvbEXCqL5m62&q=85&s=494032d77772cfc02c2f40e8e9762879)

4

[](https://docs.byterover.dev/cookbook/autonomous-local-model#)

Start Hermes and verify

Launch Hermes. It will use `google/gemma-4-e4b` served by LM Studio at `localhost:1234`.![Image 20: Hermes running with local Gemma model](https://mintcdn.com/byterover-d775e347/JJP3GvbEXCqL5m62/images/cookbook/autonomous-local-model/cookbook-hermes-local-model-sample-usage.png?fit=max&auto=format&n=JJP3GvbEXCqL5m62&q=85&s=96a08790456e27b6fa21894428a65581)

## [​](https://docs.byterover.dev/cookbook/autonomous-local-model#step-4-%E2%80%94-configure-byterover-cli)

Step 4 — Configure ByteRover CLI

Connect ByteRover to the same local endpoint and select the Qwen model.

*    TUI 
*    CLI 

1

[](https://docs.byterover.dev/cookbook/autonomous-local-model#)

Open the providers command

In the ByteRover TUI, type `/providers` and press Enter.![Image 21: ByteRover TUI /providers command](https://mintcdn.com/byterover-d775e347/JJP3GvbEXCqL5m62/images/cookbook/autonomous-local-model/cookbook-byterover-setup-local-model-providers-command-sample.png?fit=max&auto=format&n=JJP3GvbEXCqL5m62&q=85&s=059d0d3474758d5fe7628d58a274094a)

2

[](https://docs.byterover.dev/cookbook/autonomous-local-model#)

Select OpenAI Compatible

Scroll to **OpenAI Compatible** and press Enter. This covers LM Studio, Ollama, and any other OpenAI-compatible local server.![Image 22: Select OpenAI Compatible provider](https://mintcdn.com/byterover-d775e347/JJP3GvbEXCqL5m62/images/cookbook/autonomous-local-model/cookbook-byterover-setup-local-model-select-local-LLM-provider.png?fit=max&auto=format&n=JJP3GvbEXCqL5m62&q=85&s=d61f13ecc2cd39a84c9cbce6621ed11b)

3

[](https://docs.byterover.dev/cookbook/autonomous-local-model#)

Enter the base URL

When prompted, enter `http://localhost:1234/v1` and press Enter. Leave the API key blank.![Image 23: Enter LM Studio base URL](https://mintcdn.com/byterover-d775e347/JJP3GvbEXCqL5m62/images/cookbook/autonomous-local-model/cookbook-byterover-setup-local-model-register-local-model-endpoint.png?fit=max&auto=format&n=JJP3GvbEXCqL5m62&q=85&s=0607578592130db48f10ba17ef46cce6)

4

[](https://docs.byterover.dev/cookbook/autonomous-local-model#)

Select the Qwen model

From the model list, select `qwen3.5-9b` (128K ctx).![Image 24: Select qwen3.5-9b model](https://mintcdn.com/byterover-d775e347/JJP3GvbEXCqL5m62/images/cookbook/autonomous-local-model/cookbook-byterover-setup-local-model-selecting-model.png?fit=max&auto=format&n=JJP3GvbEXCqL5m62&q=85&s=2297be32a00249cff462422ad95dda27)

1

[](https://docs.byterover.dev/cookbook/autonomous-local-model#)

Connect the local provider

```
brv providers connect openai-compatible --base-url http://localhost:1234/v1
```

2

[](https://docs.byterover.dev/cookbook/autonomous-local-model#)

Switch to the Qwen model

```
brv model switch qwen3.5-9b
```

## [​](https://docs.byterover.dev/cookbook/autonomous-local-model#step-5-%E2%80%94-verify-byterover-is-working)

Step 5 — Verify ByteRover Is Working

Run a quick curate command to confirm ByteRover is using the local Qwen model.

1

[](https://docs.byterover.dev/cookbook/autonomous-local-model#)

Run a curate command

```
/curate "caching algorithm list: lru, lfu, fifo"
```

![Image 25: ByteRover curate command sample](https://mintcdn.com/byterover-d775e347/JJP3GvbEXCqL5m62/images/cookbook/autonomous-local-model/cookbook-byterover-sample-curate-command-sample.png?fit=max&auto=format&n=JJP3GvbEXCqL5m62&q=85&s=aabccde73ef7f448d3750e8921631576)

2

[](https://docs.byterover.dev/cookbook/autonomous-local-model#)

Confirm it processes with the local model

ByteRover sends the request to Qwen3.5-9B on LM Studio. You can watch the LM Studio Developer tab update in real time.![Image 26: ByteRover curate working with Qwen local model](https://mintcdn.com/byterover-d775e347/JJP3GvbEXCqL5m62/images/cookbook/autonomous-local-model/cookbook-byterover-curate-is-working.png?fit=max&auto=format&n=JJP3GvbEXCqL5m62&q=85&s=7a4329e4fb7748db55f48fb8422b69d9)

3

[](https://docs.byterover.dev/cookbook/autonomous-local-model#)

Review the results

ByteRover returns structured knowledge extracted from the curate request.![Image 27: ByteRover curate result in terminal](https://mintcdn.com/byterover-d775e347/JJP3GvbEXCqL5m62/images/cookbook/autonomous-local-model/cookbook-byterover-result-sample.png?fit=max&auto=format&n=JJP3GvbEXCqL5m62&q=85&s=aca7ab45a6bb7aa3f195a72e22e36ffa)The context tree is updated with new memory files you can inspect directly.![Image 28: ByteRover memory file created in VS Code](https://mintcdn.com/byterover-d775e347/JJP3GvbEXCqL5m62/images/cookbook/autonomous-local-model/cookbook-byterover-result-sample-2.png?fit=max&auto=format&n=JJP3GvbEXCqL5m62&q=85&s=baffaa5f3701283c86b093a4cde03558)![Image 29: Checking new memory file via ByteRover commands](https://mintcdn.com/byterover-d775e347/JJP3GvbEXCqL5m62/images/cookbook/autonomous-local-model/cookbook-byterover-vc-commands-checking-new-memory-file.png?fit=max&auto=format&n=JJP3GvbEXCqL5m62&q=85&s=b3766863f5622f6873d6d8bfa2d1d54e)

## [​](https://docs.byterover.dev/cookbook/autonomous-local-model#step-6-%E2%80%94-enable-byterover-memory-integration)

Step 6 — Enable ByteRover Memory Integration

Connect your agent to ByteRover for persistent memory across sessions.

## [OpenClaw Integration Configure ByteRover as the context engine for OpenClaw](https://docs.byterover.dev/autonomous-agents/openclaw)

## [Hermes Integration Configure ByteRover as the memory provider for Hermes](https://docs.byterover.dev/autonomous-agents/hermes)

## [​](https://docs.byterover.dev/cookbook/autonomous-local-model#reference)

Reference

## [LLM Providers Connect an external provider or use the built-in LLM](https://docs.byterover.dev/external-llm-providers/overview)

## [Onboard Context Learn how to seed your context tree with existing knowledge](https://docs.byterover.dev/common-workflows/onboard-context)

## [Reference Configuration details, troubleshooting, and advanced topics](https://docs.byterover.dev/autonomous-agents/openclaw-reference)

## [Local & Cloud Exploring local & cloud options](https://docs.byterover.dev/local-vs-cloud)

[Overview](https://docs.byterover.dev/cookbook/overview)

Ctrl+I

[x](https://x.com/kevinnguyendn)[github](https://github.com/campfirein)[linkedin](https://www.linkedin.com/company/byterover)

[Powered by This documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com/?utm_campaign=poweredBy&utm_medium=referral&utm_source=byterover-d775e347)

![Image 30: Download Gemma 4 E4B in LM Studio](https://mintcdn.com/byterover-d775e347/JJP3GvbEXCqL5m62/images/cookbook/autonomous-local-model/cookbook-gemma4-download.png?w=1100&fit=max&auto=format&n=JJP3GvbEXCqL5m62&q=85&s=de672dd57ebd11270c05898da6cffad2)

![Image 31: Download Qwen3.5-9B in LM Studio](https://mintcdn.com/byterover-d775e347/JJP3GvbEXCqL5m62/images/cookbook/autonomous-local-model/cookbook-qwen3-5download.png?w=1100&fit=max&auto=format&n=JJP3GvbEXCqL5m62&q=85&s=f651290a7829235bf6fd979d3a84d773)

![Image 32: LM Studio My Models screen](https://mintcdn.com/byterover-d775e347/JJP3GvbEXCqL5m62/images/cookbook/autonomous-local-model/cookbook-model-load-screen.png?w=1100&fit=max&auto=format&n=JJP3GvbEXCqL5m62&q=85&s=15adb579f06a89cd233f44670efc3752)

![Image 33: Gemma 4 E4B load configuration](https://mintcdn.com/byterover-d775e347/JJP3GvbEXCqL5m62/images/cookbook/autonomous-local-model/cookbook-gemma4-load-configuration.png?w=1100&fit=max&auto=format&n=JJP3GvbEXCqL5m62&q=85&s=8d1aa23059a5e35ffd3b3d94c3f74edd)

![Image 34: Qwen3.5-9B load configuration](https://mintcdn.com/byterover-d775e347/CwFsarNhiOxIuSd8/images/cookbook/autonomous-local-model/cookbook-qwen3-load-configuration.png?w=1100&fit=max&auto=format&n=CwFsarNhiOxIuSd8&q=85&s=f2cb073067a3af355667cf74ea44c9fc)

![Image 35: Both models loaded and ready in LM Studio Developer tab](https://mintcdn.com/byterover-d775e347/JJP3GvbEXCqL5m62/images/cookbook/autonomous-local-model/cookbook-local-model-load-success.png?w=1100&fit=max&auto=format&n=JJP3GvbEXCqL5m62&q=85&s=f7a60127ce23feb548f52fd50eee60af)

![Image 36: Select Custom Provider in OpenClaw onboard wizard](https://mintcdn.com/byterover-d775e347/JJP3GvbEXCqL5m62/images/cookbook/autonomous-local-model/cookbook-openclaw-local-model-select-local-LLM-provider.png?w=1100&fit=max&auto=format&n=JJP3GvbEXCqL5m62&q=85&s=a3c6f69da0c81ef01c588201816e03d6)

![Image 37: OpenClaw Custom Provider setup and verification](https://mintcdn.com/byterover-d775e347/JJP3GvbEXCqL5m62/images/cookbook/autonomous-local-model/cookbook-openclaw-local-model-setup.png?w=1100&fit=max&auto=format&n=JJP3GvbEXCqL5m62&q=85&s=5354495c362b044a6fb28c01accf3b4a)

![Image 38: OpenClaw running with local Gemma model](https://mintcdn.com/byterover-d775e347/JJP3GvbEXCqL5m62/images/cookbook/autonomous-local-model/cookbook-openclaw-local-model-sample-usage.png?w=1100&fit=max&auto=format&n=JJP3GvbEXCqL5m62&q=85&s=e91545170db78430a2b48760bc84c27d)

![Image 39: Context limit exceeded warning in OpenClaw](https://mintcdn.com/byterover-d775e347/JJP3GvbEXCqL5m62/images/cookbook/autonomous-local-model/cookbook-openlcaw-local-model-context-limit-excedded-issue.png?w=1100&fit=max&auto=format&n=JJP3GvbEXCqL5m62&q=85&s=408976a6339b1ff8cd97844871f9f8ce)

![Image 40: Select Custom Provider in Hermes setup wizard](https://mintcdn.com/byterover-d775e347/JJP3GvbEXCqL5m62/images/cookbook/autonomous-local-model/cookbook-hermes-local-model-select-custome-provider.png?w=1100&fit=max&auto=format&n=JJP3GvbEXCqL5m62&q=85&s=f2a1347a3de24912e3d9d37b9f0d588f)

![Image 41: Hermes local LLM provider configuration](https://mintcdn.com/byterover-d775e347/JJP3GvbEXCqL5m62/images/cookbook/autonomous-local-model/cookbook-hermes-local-model-select-local-LLM-provider.png?w=1100&fit=max&auto=format&n=JJP3GvbEXCqL5m62&q=85&s=5e1c83bbadcae87bcca9db314958a34c)

![Image 42: Hermes local model setup complete](https://mintcdn.com/byterover-d775e347/JJP3GvbEXCqL5m62/images/cookbook/autonomous-local-model/cookbook-hermes-local-model-setup.png?w=1100&fit=max&auto=format&n=JJP3GvbEXCqL5m62&q=85&s=8aab8669ed95b48a9bb49ba9ff08bc7c)

![Image 43: Hermes context length configuration](https://mintcdn.com/byterover-d775e347/JJP3GvbEXCqL5m62/images/cookbook/autonomous-local-model/cookbook-hermes-local-model-context-length.png?w=1100&fit=max&auto=format&n=JJP3GvbEXCqL5m62&q=85&s=e486a6ceb007faacf2391bd9dc41467e)

![Image 44: Hermes running with local Gemma model](https://mintcdn.com/byterover-d775e347/JJP3GvbEXCqL5m62/images/cookbook/autonomous-local-model/cookbook-hermes-local-model-sample-usage.png?w=1100&fit=max&auto=format&n=JJP3GvbEXCqL5m62&q=85&s=40ae12a89d779a991a1804ae270777a7)

![Image 45: ByteRover TUI /providers command](https://mintcdn.com/byterover-d775e347/JJP3GvbEXCqL5m62/images/cookbook/autonomous-local-model/cookbook-byterover-setup-local-model-providers-command-sample.png?w=1100&fit=max&auto=format&n=JJP3GvbEXCqL5m62&q=85&s=bfa44ea9072faf3ccbbdcf18aef00f87)

![Image 46: Select OpenAI Compatible provider](https://mintcdn.com/byterover-d775e347/JJP3GvbEXCqL5m62/images/cookbook/autonomous-local-model/cookbook-byterover-setup-local-model-select-local-LLM-provider.png?w=1100&fit=max&auto=format&n=JJP3GvbEXCqL5m62&q=85&s=346cd566de229de135afc35fa7700868)

![Image 47: Enter LM Studio base URL](https://mintcdn.com/byterover-d775e347/JJP3GvbEXCqL5m62/images/cookbook/autonomous-local-model/cookbook-byterover-setup-local-model-register-local-model-endpoint.png?w=1100&fit=max&auto=format&n=JJP3GvbEXCqL5m62&q=85&s=b6df644686759b404f38a253ca744f4f)

![Image 48: Select qwen3.5-9b model](https://mintcdn.com/byterover-d775e347/JJP3GvbEXCqL5m62/images/cookbook/autonomous-local-model/cookbook-byterover-setup-local-model-selecting-model.png?w=1100&fit=max&auto=format&n=JJP3GvbEXCqL5m62&q=85&s=f06b41a0b77aadc63716216ea92fc3f9)

![Image 49: ByteRover curate command sample](https://mintcdn.com/byterover-d775e347/JJP3GvbEXCqL5m62/images/cookbook/autonomous-local-model/cookbook-byterover-sample-curate-command-sample.png?w=1100&fit=max&auto=format&n=JJP3GvbEXCqL5m62&q=85&s=4c12571783f164973543a8953d107448)

![Image 50: ByteRover curate working with Qwen local model](https://mintcdn.com/byterover-d775e347/JJP3GvbEXCqL5m62/images/cookbook/autonomous-local-model/cookbook-byterover-curate-is-working.png?w=1100&fit=max&auto=format&n=JJP3GvbEXCqL5m62&q=85&s=0635aa40d132971f252292f035b8b8ed)

![Image 51: ByteRover curate result in terminal](https://mintcdn.com/byterover-d775e347/JJP3GvbEXCqL5m62/images/cookbook/autonomous-local-model/cookbook-byterover-result-sample.png?w=1100&fit=max&auto=format&n=JJP3GvbEXCqL5m62&q=85&s=1b6b481edec09f9764af44ec4b9a98a1)

![Image 52: ByteRover memory file created in VS Code](https://mintcdn.com/byterover-d775e347/JJP3GvbEXCqL5m62/images/cookbook/autonomous-local-model/cookbook-byterover-result-sample-2.png?w=1100&fit=max&auto=format&n=JJP3GvbEXCqL5m62&q=85&s=b180dc5a2de0ae26931fc3e036201f06)

![Image 53: Checking new memory file via ByteRover commands](https://mintcdn.com/byterover-d775e347/JJP3GvbEXCqL5m62/images/cookbook/autonomous-local-model/cookbook-byterover-vc-commands-checking-new-memory-file.png?w=1100&fit=max&auto=format&n=JJP3GvbEXCqL5m62&q=85&s=57e33e977a3972e57f83e64d6ac7824d)
