---
tags:
  - library
title: "Qwen3.6 - How to Run Locally | Unsloth Documentation"
url: "https://unsloth.ai/docs/models/qwen3.6"
company: [personal]
topics: []
created: 2026-04-23
source_type: raindrop
raindrop_id: 1693381203
source_domain: "unsloth.ai"
source_type_raindrop: link
collection: "unsorted"
collection_id: -1
hydrated: true
hydrated_at: 2026-04-23
hydrated_via: defuddle
---
## Excerpt

Run the new Qwen3.6-35-A3B model locally!

## Raw Content

<!-- Hydrated 2026-04-23 via defuddle -->

Qwen3.6 is Alibaba’s new family of multimodal hybrid-thinking models, including: **Qwen3.6-27B** and **35B-A3B**. It delivers top performance for its size, supports 256K context across 201 languages. It excels in agentic coding, vision, chat tasks. Qwen3.6-27B runs on **18GB RAM** setups and 35B-A3B runs on **22GB**. You can now run and train the models in [Unsloth Studio](https://unsloth.ai/docs/models/qwen3.6#unsloth-studio-guide).

[Run Qwen3.6 Tutorials](https://unsloth.ai/docs/models/qwen3.6#qwen3.6-inference-tutorials)

Qwen3.6 GGUFs use Unsloth [Dynamic 2.0](https://unsloth.ai/docs/basics/unsloth-dynamic-2.0-ggufs) for SOTA quant performance - so quants are calibrated on real world use-case datasets and important layers are upcasted. *Thank you Qwen for day zero access.*

- **Developer Role Support** for Codex, OpenCode and more:Our uploads now support the `developer role` for agentic coding tools.
- **Tool calling:** Like [Qwen3.5](https://unsloth.ai/docs/models/qwen3.5), we improved parsing nested objects to make tool calling succeed more.

![](https://unsloth.ai/docs/~gitbook/image?url=https%3A%2F%2F3215535692-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FxhOjnexMCB3dmuQFQ2Zq%252Fuploads%252FTbH2CrUTG2TWwgOP74GF%252FGemma%25204%2520example.gif%3Falt%3Dmedia%26token%3D56409d06-3735-4531-97c0-af9968371a26&width=768&dpr=3&quality=100&sign=cf0414e5&sv=2)

Qwen3.6 running in [Unsloth Studio](https://unsloth.ai/docs/models/qwen3.6#unsloth-studio-guide).

<svg><title>circle-check</title><defs><mask id="_R_11539bsnqj6iv5ubsnpfivb_" style="mask-type:alpha"></mask></defs><rect width="100%" height="100%" fill="currentColor" mask="url(#_R_11539bsnqj6iv5ubsnpfivb_)"></rect></svg>

**NEW: Qwen3.6-27B is out now!**

We conducted [Qwen3.6 GGUF Benchmarks](https://unsloth.ai/docs/models/qwen3.6#unsloth-gguf-benchmarks) to help you pick the best quant.

### ⚙️ Usage Guide

**Table: Inference hardware requirements** (units = total memory: RAM + VRAM, or unified memory)

Qwen3.6

3-bit

4-bit

6-bit

8-bit

BF16

**27B**

15 GB

18 GB

24 GB

30 GB

55 GB

**35B-A3B**

17 GB

23 GB

30 GB

38 GB

70 GB

<svg><title>circle-check</title><defs><mask id="_R_12539bsnqj6iv5ubsnpfivb_" style="mask-type:alpha"></mask></defs><rect width="100%" height="100%" fill="currentColor" mask="url(#_R_12539bsnqj6iv5ubsnpfivb_)"></rect></svg>

For best performance, make sure your total available memory (VRAM + system RAM) exceeds the size of the quantized model file you’re downloading. If it doesn’t, llama.cpp can still run via SSD/HDD offloading, but inference will be slower.

<svg><title>circle-exclamation</title><defs><mask id="_R_12d39bsnqj6iv5ubsnpfivb_" style="mask-type:alpha"></mask></defs><rect width="100%" height="100%" fill="currentColor" mask="url(#_R_12d39bsnqj6iv5ubsnpfivb_)"></rect></svg>

Do NOT use CUDA 13.2 as you may get gibberish outputs. NVIDIA is working on a fix.

**To train Qwen3.6, you can refer to our previous** [**Qwen3.5 fine-tuning guide**](https://unsloth.ai/docs/models/qwen3.5/fine-tune)**.**

### Recommended Settings

- **Maximum context window:** `262,144` (can be extended to 1M via YaRN)
- `presence_penalty = 0.0 to 2.0` default this is off, but to reduce repetitions, you can use this, however using a higher value may result in **slight decrease in performance**
- **Adequate Output Length**: `32,768` tokens for most queries
<svg><title>circle-info</title><defs><mask id="_R_13d39bsnqj6iv5ubsnpfivb_" style="mask-type:alpha"></mask></defs><rect width="100%" height="100%" fill="currentColor" mask="url(#_R_13d39bsnqj6iv5ubsnpfivb_)"></rect></svg>

If you're getting gibberish, your context length might be set too low. Or try using `--cache-type-k bf16 --cache-type-v bf16` which might help.

As Qwen3.6 is hybrid reasoning, thinking and non-thinking mode have different settings:

#### Thinking mode:

General tasks

Precise coding tasks (e.g. WebDev)

temperature = 1.0

temperature = 0.6

top\_p = 0.95

top\_p = 0.95

top\_k = 20

top\_k = 20

min\_p = 0.0

min\_p = 0.0

presence\_penalty = 1.5

presence\_penalty = 0.0

repeat penalty = disabled or 1.0

repeat penalty = disabled or 1.0

Thinking mode for general tasks:

```
temperature=1.0, top_p=0.95, top_k=20, min_p=0.0, presence_penalty=1.5, repetition_penalty=1.0
```

Thinking mode for precise coding tasks:

```
temperature=0.6, top_p=0.95, top_k=20, min_p=0.0, presence_penalty=0.0, repetition_penalty=1.0
```

#### Instruct (non-thinking) mode settings:

General tasks

Reasoning tasks

temperature = 0.7

temperature = 1.0

top\_p = 0.8

top\_p = 0.95

top\_k = 20

top\_k = 20

min\_p = 0.0

min\_p = 0.0

presence\_penalty = 1.5

presence\_penalty = 1.5

repeat penalty = disabled or 1.0

repeat penalty = disabled or 1.0

<svg><title>circle-exclamation</title><defs><mask id="_R_15539bsnqj6iv5ubsnpfivb_" style="mask-type:alpha"></mask></defs><rect width="100%" height="100%" fill="currentColor" mask="url(#_R_15539bsnqj6iv5ubsnpfivb_)"></rect></svg>

To [disable thinking / reasoning](https://unsloth.ai/docs/models/qwen3.6#how-to-enable-or-disable-reasoning-and-thinking), use `--chat-template-kwargs '{"enable_thinking":false}'`

Instruct (non-thinking) for general tasks:

```
temperature=0.7, top_p=0.8, top_k=20, min_p=0.0, presence_penalty=1.5, repetition_penalty=1.0
```

Instruct (non-thinking) for reasoning tasks:

```
temperature=1.0, top_p=0.95, top_k=20, min_p=0.0, presence_penalty=1.5, repetition_penalty=1.0
```

## Qwen3.6 Inference Tutorials:

We'll be using Dynamic 4-bit `UD_Q4_K_XL` GGUF variants for inference workloads. Click below to navigate to designated model instructions:

<svg><title>circle-exclamation</title><defs><mask id="_R_16539bsnqj6iv5ubsnpfivb_" style="mask-type:alpha"></mask></defs><rect width="100%" height="100%" fill="currentColor" mask="url(#_R_16539bsnqj6iv5ubsnpfivb_)"></rect></svg>

Do NOT use CUDA 13.2 as you may get gibberish outputs. NVIDIA is working on a fix.

[Run in Unsloth Studio](https://unsloth.ai/docs/models/qwen3.5#unsloth-studio-guide) [Run in llama.cpp](https://unsloth.ai/docs/models/qwen3.6#llama.cpp-guides)

<svg><title>circle-exclamation</title><defs><mask id="_R_16l39bsnqj6iv5ubsnpfivb_" style="mask-type:alpha"></mask></defs><rect width="100%" height="100%" fill="currentColor" mask="url(#_R_16l39bsnqj6iv5ubsnpfivb_)"></rect></svg>

`presence_penalty = 0.0 to 2.0` default this is off, but to reduce repetitions, you can use this, however using a higher value may result in **slight decrease in performance.**

Currently no Qwen3.6 GGUF works in Ollama due to separate mmproj vision files. Use llama.cpp compatible backends.

### 🦥 Unsloth Studio Guide

Qwen3.6 can be run and fine-tuned in [Unsloth Studio](https://unsloth.ai/docs/new/studio), our new open-source web UI for local AI. Unsloth Studio lets you run models locally on **MacOS, Windows**, Linux and:

- Search, download, [run GGUFs](https://unsloth.ai/docs/new/studio#run-models-locally) and safetensor models
- [**Self-healing** tool calling](https://unsloth.ai/docs/new/studio#execute-code--heal-tool-calling) + **web search**
- [**Code execution**](https://unsloth.ai/docs/new/studio#run-models-locally) (Python, Bash)
- [Automatic inference](https://unsloth.ai/docs/new/studio#model-arena) parameter tuning (temp, top-p, etc.)
- Fast CPU + GPU inference via llama.cpp
- [Train LLMs](https://unsloth.ai/docs/new/studio#no-code-training) 2x faster with 70% less VRAM

![](https://unsloth.ai/docs/~gitbook/image?url=https%3A%2F%2F3215535692-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FxhOjnexMCB3dmuQFQ2Zq%252Fuploads%252FTbH2CrUTG2TWwgOP74GF%252FGemma%25204%2520example.gif%3Falt%3Dmedia%26token%3D56409d06-3735-4531-97c0-af9968371a26&width=768&dpr=3&quality=100&sign=cf0414e5&sv=2)

1

#### Install Unsloth

Run in your terminal:

**MacOS, Linux, WSL:**

```
curl -fsSL https://unsloth.ai/install.sh | sh
```

**Windows PowerShell:**

```
irm https://unsloth.ai/install.ps1 | iex
```

<svg><title>circle-check</title><defs><mask id="_R_fh7l39bsnqj6iv5ubsnpfivb_" style="mask-type:alpha"></mask></defs><rect width="100%" height="100%" fill="currentColor" mask="url(#_R_fh7l39bsnqj6iv5ubsnpfivb_)"></rect></svg>

**Installation will be quick and take approx 1-2 mins.**

2

#### Launch Unsloth

**MacOS, Linux, WSL and Windows:**

```
unsloth studio -H 0.0.0.0 -p 8888
```

![](https://unsloth.ai/docs/~gitbook/image?url=https%3A%2F%2F3215535692-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FxhOjnexMCB3dmuQFQ2Zq%252Fuploads%252Fd1yMMNa65Ccz50Ke0E7r%252FScreenshot%25202026-03-17%2520at%252012.32.38%25E2%2580%25AFAM.png%3Falt%3Dmedia%26token%3D9369cfe7-35b1-4955-b8cb-42f7ecb43780&width=768&dpr=3&quality=100&sign=e483d141&sv=2)

Then open `http://localhost:8888` (or your specific URL) in your browser.

3

#### Search and download Qwen3.6

On first launch you will need to create a password to secure your account and sign in again later. You’ll then see a brief onboarding wizard to choose a model, dataset, and basic settings. You can skip it at any time.

Then go to the [Studio Chat](https://unsloth.ai/docs/new/studio/chat) tab and search for Qwen3.6 in the search bar and download your desired model and quant.

![](https://unsloth.ai/docs/~gitbook/image?url=https%3A%2F%2F3215535692-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FxhOjnexMCB3dmuQFQ2Zq%252Fuploads%252FT6uAnOeF7OU9cuiE8JR5%252FScreenshot%25202026-04-16%2520at%25208.59.33%25E2%2580%25AFAM.png%3Falt%3Dmedia%26token%3D6977f7b6-aff7-494b-84b5-ad737125da31&width=768&dpr=3&quality=100&sign=9403a169&sv=2)

4

#### Run Qwen3.6

Inference parameters should be auto-set when using Unsloth Studio, however you can still change it manually. You can also edit the context length, chat template and other settings.

For more information, you can view our [Unsloth Studio inference guide](https://unsloth.ai/docs/new/studio/chat). Below, the 2-bit Qwen3.6 GGUF made 30+ tool calls, searched 20 sites and executed Python code:

<iframe src="https://cdn.iframe.ly/gNyPyd0e" allowfullscreen="" allow="encrypted-media *;"></iframe>

### 🦙 Llama.cpp Guides

For this guide we will be utilizing Dynamic 4-bit which works great on a 24GB RAM / Mac device for fast inference on [llama.cpp <svg><title>arrow-up-right</title> <defs><mask id="_R_2a8539bsnqj6iv5ubsnpfivb_" style="mask-type:alpha"></mask></defs><rect width="100%" height="100%" fill="currentColor" mask="url(#_R_2a8539bsnqj6iv5ubsnpfivb_)"></rect></svg>](llama.cpphttps://github.com/ggml-org/llama.cpp) . Because the model is only around 72GB at full F16 precision, we won't need to worry much about performance. [See our GGUF collection <svg><title>arrow-up-right</title> <defs><mask id="_R_2c8539bsnqj6iv5ubsnpfivb_" style="mask-type:alpha"></mask></defs><rect width="100%" height="100%" fill="currentColor" mask="url(#_R_2c8539bsnqj6iv5ubsnpfivb_)"></rect></svg>](https://huggingface.co/collections/unsloth/qwen36) .

[27B](https://unsloth.ai/docs/models/qwen3.6#qwen3.6-27b) [35-A3B](https://unsloth.ai/docs/models/qwen3.6#qwen3.6-35b-a3b)

1

Obtain the latest `llama.cpp` **on** [**GitHub here** <svg><title>arrow-up-right</title> <defs><mask id="_R_4ph8l39bsnqj6iv5ubsnpfivb_" style="mask-type:alpha"></mask></defs><rect width="100%" height="100%" fill="currentColor" mask="url(#_R_4ph8l39bsnqj6iv5ubsnpfivb_)"></rect></svg>](https://github.com/ggml-org/llama.cpp) . You can follow the build instructions below as well. Change `-DGGML_CUDA=ON` to `-DGGML_CUDA=OFF` if you don't have a GPU or just want CPU inference. **For Apple Mac / Metal devices**, set `-DGGML_CUDA=OFF` then continue as usual - Metal support is on by default.

2

If you want to use `llama.cpp` directly to load models, you can do the below: (:`Q4_K_XL`) is the quantization type. You can also download via Hugging Face (point 3). This is similar to `ollama run`. Use `export LLAMA_CACHE="folder"` to force `llama.cpp` to save to a specific location. The model has a maximum of 256K context length.

Follow one of the commands for the specific models:

[27B](https://unsloth.ai/docs/models/qwen3.6#qwen3.5-27b) [35-A3B](https://unsloth.ai/docs/models/qwen3.6#qwen3.5-35b-a3b)

#### Qwen3.6-27B:

**Thinking mode:**

General tasks:

For precise coding tasks, change: `temperature=0.6, presence-penalty=0.0`

**Non-thinking mode:**

General tasks:

For reasoning tasks, change: `temperature=1.0, top-p=0.95`

#### Qwen3.6-35B-A3B:

**Thinking mode:**

General tasks:

For precise coding tasks, change: `temperature=0.6, presence-penalty=0.0`

**Non-thinking mode:**

General tasks:

For reasoning tasks, change: `temperature=1.0, top-p=0.95`

3

Download the model via the code below (after installing `pip install huggingface_hub hf_transfer`). You can choose Q4\_K\_M or other quantized versions like `UD-Q4_K_XL`. We recommend using at least 2-bit dynamic quant `UD-Q2_K_XL` to balance size and accuracy. If downloads get stuck, see: [Hugging Face Hub, XET debugging](https://unsloth.ai/docs/basics/troubleshooting-and-faqs/hugging-face-hub-xet-debugging)

4

Then run the model in conversation mode:

```
./llama.cpp/llama-cli \
    --model unsloth/Qwen3.6-35B-A3B-GGUF/Qwen3.6-35B-A3B-UD-Q4_K_XL.gguf \
    --mmproj unsloth/Qwen3.6-35B-A3B-GGUF/mmproj-F16.gguf \
    --temp 1.0 \
    --top-p 0.95 \
    --min-p 0.00 \
    --presence_penalty=1.5 \
    --top-k 20
```

#### Llama-server & OpenAI completion library

To deploy Qwen3.6 for production, we use `llama-server` In a new terminal say via tmux, deploy the model via:

```
./llama.cpp/llama-server \
--model unsloth/Qwen3.6-35B-A3B-GGUF/Qwen3.6-35B-A3B-UD-Q4_K_XL.gguf \
    --mmproj unsloth/Qwen3.6-35B-A3B-GGUF/mmproj-F16.gguf \
    --alias "unsloth/Qwen3.6-35B-A3B" \
    --temp 0.6 \
    --top-p 0.95 \
    --ctx-size 16384 \
    --top-k 20 \
    --min-p 0.00 \
    --port 8001
```

Then in a new terminal, after doing `pip install openai`, do:

```
from openai import OpenAI
import json
openai_client = OpenAI(
    base_url = "http://127.0.0.1:8001/v1",
    api_key = "sk-no-key-required",
)
completion = openai_client.chat.completions.create(
    model = "unsloth/Qwen3.6-35B-A3B",
    messages = [{"role": "user", "content": "Create a Snake game."},],
)
print(completion.choices[0].message.content)
```

### 🍎 MLX Dynamic Quants

We also uploaded dynamic Qwen3.6 4bit and 8bit quants for MacOS devices! Our MLX quant algorithm is still evolving, and we’re actively refining it wherever improvements can be made.

**Qwen3.6-27B MLX:**

[3-bit <svg><title>arrow-up-right</title><defs><mask id="_R_4qeat39bsnqj6iv5ubsnpfivb_" style="mask-type:alpha"></mask></defs><rect width="100%" height="100%" fill="currentColor" mask="url(#_R_4qeat39bsnqj6iv5ubsnpfivb_)"></rect></svg>](https://huggingface.co/unsloth/Qwen3.6-27B-UD-MLX-3bit)

[4-bit <svg><title>arrow-up-right</title><defs><mask id="_R_4qmat39bsnqj6iv5ubsnpfivb_" style="mask-type:alpha"></mask></defs><rect width="100%" height="100%" fill="currentColor" mask="url(#_R_4qmat39bsnqj6iv5ubsnpfivb_)"></rect></svg>](https://huggingface.co/unsloth/Qwen3.6-27B-UD-MLX-4bit)

[MXFP4 <svg><title>arrow-up-right</title><defs><mask id="_R_4quat39bsnqj6iv5ubsnpfivb_" style="mask-type:alpha"></mask></defs><rect width="100%" height="100%" fill="currentColor" mask="url(#_R_4quat39bsnqj6iv5ubsnpfivb_)"></rect></svg>](https://huggingface.co/unsloth/Qwen3.6-27B-UD-MLX-MXFP4)

[NVFP4 <svg><title>arrow-up-right</title><defs><mask id="_R_4r6at39bsnqj6iv5ubsnpfivb_" style="mask-type:alpha"></mask></defs><rect width="100%" height="100%" fill="currentColor" mask="url(#_R_4r6at39bsnqj6iv5ubsnpfivb_)"></rect></svg>](https://huggingface.co/unsloth/Qwen3.6-27B-UD-MLX-NVFP4)

[6-bit <svg><title>arrow-up-right</title><defs><mask id="_R_4reat39bsnqj6iv5ubsnpfivb_" style="mask-type:alpha"></mask></defs><rect width="100%" height="100%" fill="currentColor" mask="url(#_R_4reat39bsnqj6iv5ubsnpfivb_)"></rect></svg>](https://huggingface.co/unsloth/Qwen3.6-27B-UD-MLX-6bit)

[8-bit <svg><title>arrow-up-right</title><defs><mask id="_R_4rmat39bsnqj6iv5ubsnpfivb_" style="mask-type:alpha"></mask></defs><rect width="100%" height="100%" fill="currentColor" mask="url(#_R_4rmat39bsnqj6iv5ubsnpfivb_)"></rect></svg>](https://huggingface.co/unsloth/Qwen3.6-27B-MLX-8bit)

**Qwen3.6-35B-A3B MLX:**

[3-bit <svg><title>arrow-up-right</title><defs><mask id="_R_2debd39bsnqj6iv5ubsnpfivb_" style="mask-type:alpha"></mask></defs><rect width="100%" height="100%" fill="currentColor" mask="url(#_R_2debd39bsnqj6iv5ubsnpfivb_)"></rect></svg>](https://huggingface.co/unsloth/Qwen3.6-35B-A3B-UD-MLX-3bit)

[4-bit <svg><title>arrow-up-right</title><defs><mask id="_R_2dmbd39bsnqj6iv5ubsnpfivb_" style="mask-type:alpha"></mask></defs><rect width="100%" height="100%" fill="currentColor" mask="url(#_R_2dmbd39bsnqj6iv5ubsnpfivb_)"></rect></svg>](https://huggingface.co/unsloth/Qwen3.6-35B-A3B-UD-MLX-4bit)

[8-bit <svg><title>arrow-up-right</title><defs><mask id="_R_2dubd39bsnqj6iv5ubsnpfivb_" style="mask-type:alpha"></mask></defs><rect width="100%" height="100%" fill="currentColor" mask="url(#_R_2dubd39bsnqj6iv5ubsnpfivb_)"></rect></svg>](https://huggingface.co/unsloth/Qwen3.6-35B-A3B-MLX-8bit)

To try them out use:

```
curl -fsSL https://raw.githubusercontent.com/unslothai/unsloth/refs/heads/main/scripts/install_qwen3_6_mlx.sh | sh
source ~/.unsloth/unsloth_qwen3_6_mlx/bin/activate
python -m mlx_vlm.chat --model unsloth/Qwen3.6-27B-UD-MLX-4bit
```

See below for Qwen3.6-27B KL Divergence (KLD) and Perplexity (PPL) scores (lower is better):

### 💡 How to enable or disable thinking

[**Unsloth Studio**](https://unsloth.ai/docs/models/qwen3.6#unsloth-studio-guide) automatically has a 'Think' Toggle for thinking models.

In llama.cpp, you can enable or disable thinking by following the below commands. Use ' `true` ' and ' `false` ' interchangeably.

See code below for enabling / disabling thinking within `llama-server`:

![](https://unsloth.ai/docs/~gitbook/image?url=https%3A%2F%2F3215535692-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FxhOjnexMCB3dmuQFQ2Zq%252Fuploads%252Fj34CUWyxrf0ZxZj4Dn4Z%252Fcurrent%2520weather%2520in%2520amazon.png%3Falt%3Dmedia%26token%3Dc0688e60-8d7d-4273-87af-25332fbd540c&width=768&dpr=3&quality=100&sign=e707fa6f&sv=2)

Unsloth Studio has Think toggle by default

llama-server OS:

Enable Thinking

Disable Thinking

Linux, MacOS, WSL:

```
--chat-template-kwargs '{"enable_thinking":true}'
```

```
--chat-template-kwargs '{"enable_thinking":false}'
```

Windows / Powershell:

```
--chat-template-kwargs "{\"enable_thinking\":true}"
```

```
--chat-template-kwargs "{\"enable_thinking\":false}"
```

As an example for Qwen3.6-35B-A3B to disable thinking (default is enabled):

```
./llama.cpp/llama-server \
    --model unsloth/Qwen3.6-35B-A3B-GGUF/Qwen3.6-35B-A3B-BF16.gguf \
    --alias "unsloth/Qwen3.6-35B-A3B-GGUF" \
    --temp 0.6 \
    --top-p 0.95 \
    --ctx-size 16384 \
    --top-k 20 \
    --min-p 0.00 \
    --port 8001 \
    --chat-template-kwargs '{"enable_thinking":false}'
```

And then in Python:

```
from openai import OpenAI
import json
openai_client = OpenAI(
    base_url = "http://127.0.0.1:8001/v1",
    api_key = "sk-no-key-required",
)
completion = openai_client.chat.completions.create(
    model = "unsloth/Qwen3.6-35B-A3B-GGUF",
    messages = [{"role": "user", "content": "What is 2+2?"},],
)
print(completion.choices[0].message.content)
print(completion.choices[0].message.reasoning_content)
```

### 👨💻 OpenAI Codex & Claude Code

To run the model via local coding agentic workloads, you can [follow our guide](https://unsloth.ai/docs/basics/claude-code). Just change the model name to your 'Qwen3.6' variant and ensure you follow the correct Qwen3.6 parameters and usage instructions. Use the `llama-server` we just set up just then.

After following the instructions for Claude Code for example you will see:

![](https://unsloth.ai/docs/~gitbook/image?url=https%3A%2F%2F3215535692-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FxhOjnexMCB3dmuQFQ2Zq%252Fuploads%252Fup2DMSMPjNR8BM9pgR0v%252Fimage.png%3Falt%3Dmedia%26token%3D152e9ee0-2491-4379-af18-8fca0789b19d&width=768&dpr=3&quality=100&sign=580b633c&sv=2)

We can then ask say `Create a Python game for Chess`:

![](https://unsloth.ai/docs/~gitbook/image?url=https%3A%2F%2F3215535692-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FxhOjnexMCB3dmuQFQ2Zq%252Fuploads%252F9TfMAoKSdMpb8OHKNnHH%252Fimage.png%3Falt%3Dmedia%26token%3D771df3aa-91ab-4c1e-8676-1830058001ca&width=768&dpr=3&quality=100&sign=efa8210a&sv=2) ![](https://unsloth.ai/docs/~gitbook/image?url=https%3A%2F%2F3215535692-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FxhOjnexMCB3dmuQFQ2Zq%252Fuploads%252FWP3lI5mQW2EHB79qqgDz%252Fimage.png%3Falt%3Dmedia%26token%3D55cf3189-e100-419c-a615-024b45948284&width=768&dpr=3&quality=100&sign=96b8fc09&sv=2) ![](https://unsloth.ai/docs/~gitbook/image?url=https%3A%2F%2F3215535692-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FxhOjnexMCB3dmuQFQ2Zq%252Fuploads%252Fn8DZddDODQZGCP8giKYY%252Fimage.png%3Falt%3Dmedia%26token%3D996c8cb9-d199-4045-90f0-408690e02667&width=768&dpr=3&quality=100&sign=59b9ff10&sv=2)

## 📊 Benchmarks

### Unsloth GGUF Benchmarks

We conducted Mean KL Divergence benchmarks for Qwen3.6-35-A3B GGUFs across providers to help you pick the best quant.

- KL Divergence puts nearly all Unsloth GGUFs on the SOTA Pareto frontier
- KLD shows how well a quantized model matches the original BF16 output distribution, indicating retained accuracy.
- This makes Unsloth the top-performing in 21 of 22 sizes
- Only Q6\_K was updated for more Dynamic layers and we introduced a new `UD-IQ4_NL_XL` quant

![](https://unsloth.ai/docs/~gitbook/image?url=https%3A%2F%2F3215535692-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FxhOjnexMCB3dmuQFQ2Zq%252Fuploads%252FHq98A18pHA2ePwlInrFG%252Fqwen36_mean_q6k_corrected_arrow_pareto_fixed.png%3Falt%3Dmedia%26token%3Da5190c8a-4d04-4d4d-be94-dd15214e6687&width=768&dpr=3&quality=100&sign=d0938e2f&sv=2)

35B-A3B - KLD benchmarks (lower is better)

### Official Qwen Benchmarks

#### Qwen3.6-27B

![](https://unsloth.ai/docs/~gitbook/image?url=https%3A%2F%2F3215535692-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FxhOjnexMCB3dmuQFQ2Zq%252Fuploads%252FlvrSCq6GKFGADGSOTE9W%252Fqwen3.6_27b_score.png%3Falt%3Dmedia%26token%3D6f1abf24-6a15-4988-a305-acd5638aaf0d&width=768&dpr=3&quality=100&sign=a848cf34&sv=2)

#### Qwen3.6-35B-A3B

![](https://unsloth.ai/docs/~gitbook/image?url=https%3A%2F%2F3215535692-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FxhOjnexMCB3dmuQFQ2Zq%252Fuploads%252F25aKI2tJR2PNfGfwnbZi%252Fqwen3.6_35b_a3b_score%282%29.png%3Falt%3Dmedia%26token%3Df296d01d-311d-413e-8c62-122728e33008&width=768&dpr=3&quality=100&sign=ecfe4c2c&sv=2)

Last updated
