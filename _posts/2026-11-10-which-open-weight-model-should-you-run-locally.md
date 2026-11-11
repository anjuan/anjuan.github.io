---
title: 'Which Open Weight Model Should You Run Locally?'
author: anjuan
layout: post
date: "2026-11-10"
permalink: /blog/which-open-weight-model-should-you-run-locally/
categories:
  - Tech
excerpt: "On your own hardware, memory replaces price as the budget, so start on a mid-size open weight model that fits your machine, then move down for volume and up for hard work."
comments: false
---

{% include image.html url="/images/which-open-weight-model-should-you-run-locally.png" alt="Graphic novel illustration of a man in a home workshop at night fitting glowing cubes of different sizes into a laptop, a workstation, and a small server rack while a distant data center glows on the horizon." %}


This week, Anthropic published [Which Claude model should you build with?](https://claude.dev/blog/which-claude-model-should-you-build-with/), a playbook for choosing among its models based on what each task needs and what it costs. It's a good read. It also assumes you're renting your models by the token.

I run open weight models at home on a Mac Studio, so I wanted the same playbook for models you download and run yourself. Here it is. The short version is that on your own hardware, memory replaces price as the budget. Most people should start on a mid-size model that fits their memory, then move down for volume and up for hard work.

An open weight model is one whose trained weights you can download, run, and fine-tune yourself. The training data and code usually stay private, so "open weight" is more accurate than "open source." The license, not the download button, decides what you can build with it.

Everything here assumes hardware you own: a laptop, a desktop workstation, or a small server in an office closet. That rules out the largest open models. DeepSeek V4 Pro has 1.6 trillion parameters, Qwen's open flagship has 2.4 trillion, and Mistral Large 4 has about 1 trillion, so all three need data center hardware. The models one or two tiers down now handle most daily work, and that's where this guide lives.

I'll follow three people throughout: a software engineer, a university student, and the owner of a 40-person business.

## TL;DR

Start most work on [Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B) at 4-bit quantization with thinking on. It's a 27B dense model under Apache 2.0 that takes about 18 GB in Ollama's 4-bit build, so it runs on a 24 GB graphics card or a Mac with 32 GB of memory. On Qwen's own evaluation it scored 61.7 on SWE-bench Pro, the top score in a comparison that included Muse Glimmer-30B. If you'd rather use a model from a US lab, [Gemma 4 31B](https://huggingface.co/google/gemma-4-31B-it) and [Muse Glimmer-30B](https://huggingface.co/meta-models/Muse-Glimmer-30B) fill the same slot.

From there:

- Move down to [Gemma 4 E4B](https://huggingface.co/google/gemma-4-E4B-it) or [gpt-oss-20b](https://huggingface.co/openai/gpt-oss-20b) for simple, high-volume work like classification, routing, and extraction, or for anything that has to run on a 16 GB laptop. Both also make good helpers for a bigger model.
- Move sideways to [Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B) when speed matters more than depth. Only about 3B of its 35B parameters work on each token, so it answers much faster than a dense model of the same size.
- Move up to [gpt-oss-120b](https://huggingface.co/openai/gpt-oss-120b) or [Mistral Small 4](https://huggingface.co/mistralai/Mistral-Small-4-119B-2603) when you have 96 to 128 GB of memory and the 27B model keeps falling short.
- Move up again to [GLM-5.3-Flash](https://huggingface.co/zai-org/GLM-5.3-Flash) only if you have a machine with 256 GB of memory or more. That's roughly what its 320B parameters need at 4-bit.

Before you change models, try the two dials every local setup has. The first is reasoning effort: most current open models let you turn thinking up, down, or off for each request. The second is quantization, the number of bits stored for each weight. Going from 8-bit to 4-bit roughly halves the memory a model needs, usually at a small cost in quality.

Neither dial gives a model knowledge it doesn't have. For that you still need a bigger model, and on your own hardware a bigger model means more memory.

## The models side by side

The table lists the models this guide recommends, ordered by the memory they need.

| Model | Lab | Parameters (total / active) | Memory you need at 4-bit (approx.) | Context | License | Built for |
| --- | --- | --- | --- | --- | --- | --- |
| [Gemma 4 E4B](https://huggingface.co/google/gemma-4-E4B-it) | Google (US) | 8B / 4.5B effective | 8 GB | 128K | Apache 2.0 | Phones and light laptops; text, images, audio |
| [Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B) | Alibaba Qwen (China) | 9B dense | 8 to 16 GB | 262K | Apache 2.0 | The strongest small all-rounder |
| [gpt-oss-20b](https://huggingface.co/openai/gpt-oss-20b) | OpenAI (US) | 21B / 3.6B | 16 GB | 128K | Apache 2.0 | Fast reasoning on a laptop |
| [Gemma 4 12B](https://huggingface.co/google/gemma-4-12B-it) | Google (US) | 12B dense | 16 GB | 256K | Apache 2.0 | Laptop work with images and audio |
| [Gemma 4 26B A4B](https://huggingface.co/google/gemma-4-26B-A4B-it) | Google (US) | 25B / 3.8B | 24 to 32 GB | 256K | Apache 2.0 | Speed at mid-size |
| [Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B) | Alibaba Qwen (China) | 35B / 3B | 32 GB | 262K | Apache 2.0 | Speed at mid-size |
| [Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B) | Alibaba Qwen (China) | 27B dense | 24 to 32 GB | 262K | Apache 2.0 | The default; coding and agents |
| [Gemma 4 31B](https://huggingface.co/google/gemma-4-31B-it) | Google (US) | 31B dense | 24 to 32 GB | 256K | Apache 2.0 | Reasoning and documents |
| [Muse Glimmer-30B](https://huggingface.co/meta-models/Muse-Glimmer-30B) | Meta (US) | 30B dense | 24 to 32 GB | 131K | Apache 2.0 | Local agents and tool use |
| [gpt-oss-120b](https://huggingface.co/openai/gpt-oss-120b) | OpenAI (US) | 117B / 5.1B | 80 to 128 GB | 128K | Apache 2.0 | Big-model reasoning at small-model speed |
| [Mistral Small 4](https://huggingface.co/mistralai/Mistral-Small-4-119B-2603) | Mistral AI (France) | 119B / 6.5B | 96 to 128 GB | 256K | Apache 2.0 | One model for chat, code, and documents |

The memory column is what the whole machine needs to run the model with room for a working conversation, not the download size. A 24 GB graphics card and a 32 GB Mac land in the same row because a Mac's graphics processor can use only part of its unified memory by default.

"Total / active" matters for speed. A mixture-of-experts model like gpt-oss-120b stores 117B parameters but uses only 5.1B for each token, so it needs the memory of a big model and runs at the speed of a small one. Dense models use every parameter on every token.

Above 128 GB, three more models are worth knowing. [GLM-5.3-Flash](https://huggingface.co/zai-org/GLM-5.3-Flash) from Z.ai (China, MIT license) has 320B parameters with 18B active, and Z.ai says it approaches Claude Opus 4.8 on coding and agent benchmarks; plan on a machine with 256 GB or more. [DeepSeek V4.1-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash) (China, MIT) has a 552B backbone and a 1M-token context, which puts it on a 512 GB machine or a multi-GPU server. [Qwen3.8-Flash-Next](https://huggingface.co/Qwen/Qwen3.8-Flash-Next) can squeeze onto 128 GB at aggressive quantization, but it's an experimental preview under the more restrictive Qwen Community License, so read the terms before you build on it.

## The software engineer

The engineer should run Qwen3.8-27B as the main coding model and keep a small model loaded beside it for side tasks. Picture someone with a 64 GB laptop who wants a coding agent that keeps the company's code on the machine, including on a plane.

The agent doesn't have to change. Ollama has spoken the Anthropic Messages API since version 0.14, so [Claude Code can drive a local model](https://docs.ollama.com/api/anthropic-compatibility): point `ANTHROPIC_BASE_URL` at `http://localhost:11434` and pass the model name with `--model`. Open source agents like OpenCode connect through the same server's OpenAI-compatible endpoint.

One setting trips up almost everyone. Ollama's [default context window is 4,096 tokens](https://docs.ollama.com/faq), far too small for an agent that reads files, and Ollama recommends at least 32K for Claude Code. Raise `OLLAMA_CONTEXT_LENGTH` before you judge any model.

| Task | Starting model | Starting setting | Why |
| --- | --- | --- | --- |
| Agentic coding: bug fixes, features, tests | Qwen3.8-27B | Thinking on, default effort | Top SWE-bench Pro score (61.7) in Qwen's comparison, run in the Claude Code harness |
| Quick questions, explaining code, small edits | Qwen3.6-35B-A3B | Thinking off | About 3B active parameters, so replies come back fast |
| Helpers that read logs, test output, and search results | Qwen3.5-9B | Thinking off | Mistakes are cheap to spot, and it leaves memory for the main model |
| Code that has to stay on US-developed models | Muse Glimmer-30B | Reasoning strength high | Same memory as Qwen3.8-27B; scored 51.2 on SWE-bench Pro in Meta's tests, against 36.9 for Gemma 4 31B |
| Large refactors and architecture work | gpt-oss-120b or Mistral Small 4 (128 GB); GLM-5.3-Flash (256 GB+) | High effort | Cross-cutting changes need more capacity than a 27B model has |

On 64 GB, Qwen3.8-27B at about 18 GB and Qwen3.5-9B loaded together still leave room for long contexts. Ollama keeps up to three models in memory by default and unloads idle ones after five minutes, so the fast model can swap in when you call it.

When the main model falls short, take these steps in order:

1. Give it a way to check its own work: a test, a build, or a script that hits the endpoint.
2. Raise reasoning effort, or move from 4-bit to 8-bit. Qwen3.8-27B at `Q8_0` is roughly 29 GB, which still fits.
3. Move up a tier, which on local hardware usually means a bigger machine.

One caution on step 2. Qwen's own model card notes that lower reasoning effort can make multi-step agent tasks slower overall, because the model fails more and retries. Measure total time per finished task, not time per reply.

## The university student

The student should start on Qwen3.5-9B and switch to gpt-oss-20b for programming. Picture someone with a 16 GB laptop, a library with unreliable Wi-Fi, and no budget beyond the machine they already own.

On 16 GB, load one model at a time. [LM Studio](https://lmstudio.ai/) is the easiest place to start: a desktop app for downloading quantized models and chatting with them, with no terminal required.

| Task | Starting model | Starting setting | Why |
| --- | --- | --- | --- |
| Math and science problem sets | Qwen3.5-9B | Thinking on | Scored 83.2 on the HMMT February 2025 math contest in Qwen's tests, against 76.7 for gpt-oss-20b |
| Programming assignments | gpt-oss-20b | `Reasoning: high` in the system prompt | Scored 74.6 on LiveCodeBench v6 in the same table, against 65.6 for Qwen3.5-9B |
| Long readings, course packs, photos of notes | Qwen3.5-9B | Thinking off to summarize, on to analyze | 262K-token context and image input |
| Lecture clips and language practice | Gemma 4 12B | Thinking off | Accepts audio in clips of up to 30 seconds, and can translate speech |
| Flashcards and quick summaries | Gemma 4 E4B | Thinking off | The smallest and fastest model here |

The audio limit matters in practice. A recorded lecture has to be cut into 30-second chunks before Gemma 4 12B can transcribe it, so a script or app that does the chunking for you is worth finding first.

Two cautions. Local models don't browse the web, and their knowledge stops at a training cutoff; Gemma 4's pre-training data ends in January 2025. They will describe an outdated world with confidence and sometimes invent citations, so verify every source they hand you. And check your course's AI policy. Running a model locally keeps your work private; it doesn't make it allowed.

With 32 GB, the student can use the engineer's defaults instead: Qwen3.6-35B-A3B for speed or Qwen3.8-27B for depth.

## The small business owner

The owner should buy one 128 GB machine for the office, run Mistral Small 4 on it as the shared assistant, and put a small model in front to sort the inbox. Picture a 40-person services firm that wants help with customer email, contracts, and policy questions without sending client data to anyone else's servers.

The hardware is the whole bill. A [Mac Studio with 128 GB](https://computingforgeeks.com/best-mac-for-local-llm/) was about $5,100 in late October 2026; a workstation with a large graphics card costs more but serves more people at once. After that, every request is free apart from electricity.

| Task | Starting model | Starting setting | Why |
| --- | --- | --- | --- |
| Sorting incoming email and tickets by type and urgency | Gemma 4 E4B | Thinking off, JSON output | Fast, and a wrong label is cheap to catch |
| Drafting replies and everyday staff questions | Mistral Small 4 | `reasoning_effort="none"` | Only 6.5B active parameters, so it stays quick when several people use it |
| Questions about contracts, policies, and scanned forms | Mistral Small 4 | `reasoning_effort="high"` | 256K-token context and image input for scanned pages |
| Agents that read outside email and take actions | Gemma 4 31B | Thinking on, a person approves every action | Lowest prompt-injection success rate (25.6%) in Meta's comparison, against 28.4% for Muse Glimmer-30B and 40.3% for Qwen3.6-27B |

Mistral Small 4 at 4-bit takes roughly 70 to 80 GB, so it fits beside the small router with some room left for conversations. Swap Gemma 4 31B in for agent jobs rather than keeping all three loaded.

Serving a team takes two settings changes. Ollama [listens only on the machine itself by default](https://docs.ollama.com/faq); set `OLLAMA_HOST` to reach it from the office network, and keep it behind the office firewall or VPN, never open to the internet. Ollama also answers one request per model at a time unless you raise `OLLAMA_NUM_PARALLEL`, and memory grows with each parallel slot times the context length. On a GPU workstation, [vLLM](https://vllm.ai/) is built for many simultaneous requests and is the serving path Mistral recommends.

Two questions will come up with clients and insurers. The first is licensing. Every model in the table above is Apache 2.0, which allows commercial use, but not every open model is: Qwen3.8-Flash-Next uses the Qwen Community License, and Mistral Large 4 uses a modified MIT license. Read the license file before you build on a model.

The second is provenance. Weights running on your own machine send nothing back to the lab that trained them, wherever that lab is. Some contracts and government customers still ask which models you use and where they came from. The US and European models in the table cover every tier, so you can answer that question without giving up much.

## The trade-offs

Every local choice trades memory, speed, and quality against each other. Price per token drops out, because you already paid for the machine.

### Capability against memory

A bigger model knows more and reasons better, and it needs more memory to hold. Mixture-of-experts models loosen that link. Think of total parameters as the size of a library and active parameters as the number of books the model pulls off the shelf for each word. Your memory has to hold the whole library, but speed depends on how many books get read.

Treat every score in this guide as a starting point. Each comes from the lab that built the model, run in a setup that lab chose.

### Quantization against quality

Quantization works like JPEG compression: at a sensible setting you can't see the difference, and pushed too far everything gets blocky. Meta measured an average 1.0% drop across 15 benchmarks for its 17 GB 4-bit build of Muse Glimmer-30B, and OpenAI post-trained gpt-oss with 4-bit weights and ran every evaluation that way, so 4-bit is a safe default.

Below 4-bit, quality falls faster. The 284B DeepSeek V4-Flash [fits a 128 GB Mac only at 2-bit](https://insiderllm.com/guides/best-local-llms-mac-2026/), which is a real quality trade. Usually a smaller model at 4-bit beats a bigger model at 2-bit, but test both on your work.

The conversation memory can be compressed too. Ollama's `OLLAMA_KV_CACHE_TYPE=q8_0` [cuts that cache to about half](https://docs.ollama.com/faq) with a very small loss in precision.

### Speed against accuracy

Local speed comes down to memory bandwidth and active parameters. The same 4-bit Muse Glimmer-30B produced 23.7 tokens per second on an Apple M4 Max and 74.9 on an NVIDIA RTX 5090 in Meta's tests.

If you need more speed from the same model, use its draft model before you switch. Muse Glimmer ships a drafter that took the RTX 5090 to 233.4 tokens per second, Gemma 4 has [matching drafter models](https://huggingface.co/google/gemma-4-31B-it-assistant), and Mistral Small 4 has a speculative decoding head. A drafter guesses several tokens ahead and the main model checks them, so output quality stays the same.

For replies a person waits on, turn thinking off or down. When you can check results automatically, run everything at low effort and re-run only the failures at high effort.

### Context against memory

On your own hardware, context costs memory instead of money. Every token in a conversation takes space in the model's cache, and architecture changes that cost a lot: DeepSeek says V4.1-Flash needs [about a quarter of the cache per token](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash) that V4-Flash did.

The pull goes both ways. Qwen advises keeping at least 128K tokens of context for Qwen3.5 models to preserve their thinking, while every parallel conversation multiplies the memory that context takes. Size your context to the job, and check memory use with `ollama ps` before adding users.

## Mixing models

Most local setups settle on two models in memory: a small one for volume and a bigger one for judgment. The rule from Anthropic's post carries over unchanged. Keep small models on work where a mistake is cheap to spot, and keep edits and judgment calls on the main model.

### Put helpers on the small model

In Claude Code, a subagent with `model: haiku` runs on whatever the haiku alias points to, and `ANTHROPIC_DEFAULT_HAIKU_MODEL` [repoints it](https://claude.dev/blog/which-claude-model-should-you-build-with/). Against Ollama, that alias can be a local model:

```bash
export ANTHROPIC_BASE_URL=http://localhost:11434
export ANTHROPIC_AUTH_TOKEN=ollama
export ANTHROPIC_DEFAULT_HAIKU_MODEL=qwen3.5:9b
claude --model qwen3.8:27b
```

The `log-reader` subagent from Anthropic's post now runs on Qwen3.5-9B with no edits. The pair takes about 25 GB before context, per [Ollama's listed sizes](https://ollama.com/library/qwen3.8). Ollama's model pages also offer a one-line shortcut, `ollama launch claude --model qwen3.8`.

### Let code do the routing

The owner's inbox is the simple case. A small model labels each message, and ordinary code sends billing questions to one queue and contract questions to Mistral Small 4. When the rule is that simple, code should pick the model rather than another model.

### Switch at a natural break

A conversation's cache belongs to the model that built it. When you switch, the new model reads the whole conversation from scratch, which takes a while on a laptop once a session runs long. Run `/compact` in Claude Code or start fresh from a short written plan, then switch.

Thinking history is the other trap. Gemma 4 expects earlier turns' reasoning to be removed from the history, except around tool calls, while Qwen3.8 keeps it by default. Runtimes that apply each model's chat template handle this for you; if your own code manages history, strip old reasoning when you change models.

### Run bulk work overnight

Local tokens cost nothing extra, so idle hours are free capacity. Queue the slow jobs, like summarizing a year of contracts or tagging an old ticket archive, on the bigger model after everyone goes home, and check a sample in the morning.

## Check compatibility before switching

Swapping one open model for another is rarely just a name change. Every lab picks its own prompt format, reasoning controls, and recommended settings, and a request built for one model can quietly underperform on the next.

**Prompt formats.** Each model expects its conversation wrapped in its own template. gpt-oss works only with OpenAI's harmony format, Gemma 4 marks its reasoning with its own tokens, and DeepSeek V4.1-Flash ships no standard chat template at all, just a Python encoding library. Let the runtime (Ollama, LM Studio, llama.cpp) apply the template unless you have a strong reason to build prompts yourself.

**Reasoning controls.** Every model turns thinking up and down differently, and the defaults vary more than you'd expect:

| Model | How to set it | Levels |
| --- | --- | --- |
| Qwen3.8-27B | `reasoning_effort`; `enable_thinking` turns it off | low, medium, xhigh (default) |
| Qwen3.5-9B | `enable_thinking` in the chat template options | on (default), off |
| gpt-oss-20b and 120b | `Reasoning: high` in the system prompt | low, medium, high |
| Muse Glimmer-30B | `Reasoning strength: high` in the system prompt | low, medium, high, xhigh |
| Gemma 4 | The <code>&lt;&#124;think&#124;&gt;</code> token at the start of the system prompt | on, off |
| Mistral Small 4 | `reasoning_effort` | none, high |
| GLM-5.3-Flash | `reasoning_effort` | low, high, max (default) |
| DeepSeek V4.1-Flash | Reasoning effort setting | any whole number from 1 to 100 |

GLM-5.3-Flash and Qwen3.8-27B both default to their highest level, which is right for benchmarks and slow for chat. Set the level on purpose.

**Sampling settings.** Qwen recommends a temperature of 1.0 with `top_k` of 20 in thinking mode, Google and Meta recommend 1.0 with `top_k` of 64, and Mistral recommends 0.7 with reasoning on. Runtime defaults don't always match, so copy the settings from each model card.

**Runtime support.** New architectures need runtime updates. At launch, Qwen3.5 required the main branches of vLLM and SGLang, and Meta said Ollama and LM Studio support for Muse Glimmer would arrive in the following days. Check that your runtime version supports a model before you plan around it.

If one system runs several models, build every request for the strictest of them. Leave templates to the runtime, keep each model's reasoning and sampling settings in configuration instead of code, and write tool descriptions precise enough for the most literal model. Then a step can move up or down a tier without a code change.

## Measure on your own work

Published scores pick a starting model; your own tasks pick the winner. Locally, add two measurements the cloud version of this test doesn't need: speed and memory.

1. Pull 20 to 50 real tasks and write an outcome check for each, such as a passing test, a correct label, or an answer you can grade.
2. Run each candidate at two quantization levels and two reasoning levels. Record the pass rate, the total time per finished task, and peak memory. `ollama ps` shows what's loaded and how much memory it uses, and each Ollama API response reports token counts and timings.
3. Plot pass rate against time per task. Keep a two-model setup only if it beats every single model on that chart.
4. Run the winner beside your current setup for a week before you switch.

For a quick check, run one task from your backlog on two models and compare the results and the wall-clock time.

Fit the model to the machine you already own, then let your own work pick the winner.

## Learn more

- [Which Claude model should you build with?](https://claude.dev/blog/which-claude-model-should-you-build-with/) is the Anthropic playbook this guide is modeled on.
- [Ollama's Anthropic compatibility guide](https://docs.ollama.com/api/anthropic-compatibility) covers running Claude Code against local models.
- [Ollama's FAQ](https://docs.ollama.com/faq) covers context length, concurrent requests, network access, and cache quantization.
- [LM Studio](https://lmstudio.ai/) is the easiest desktop app for trying models without a terminal.
- [llama.cpp](https://github.com/ggml-org/llama.cpp), [MLX LM](https://github.com/ml-explore/mlx-lm), and [vLLM](https://vllm.ai/) are the engines underneath most local setups, for any hardware, Apple Silicon, and GPU servers respectively.

### Sources

- Model cards: [Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B), [Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B), [Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B), [Gemma 4](https://huggingface.co/google/gemma-4-12B-it), [Muse Glimmer-30B](https://huggingface.co/meta-models/Muse-Glimmer-30B), [gpt-oss-20b](https://huggingface.co/openai/gpt-oss-20b), [gpt-oss-120b](https://huggingface.co/openai/gpt-oss-120b), [Mistral Small 4](https://huggingface.co/mistralai/Mistral-Small-4-119B-2603), [GLM-5.3-Flash](https://huggingface.co/zai-org/GLM-5.3-Flash), [DeepSeek V4.1-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)
- Ollama library sizes: [qwen3.8](https://ollama.com/library/qwen3.8), [qwen3.5](https://ollama.com/library/qwen3.5)
- Quantized sizes for Qwen3.8-27B: [OrcaRouter](https://www.orcarouter.ai/blog/qwen-3-8-27b-huggingface)
- Mac pricing and memory guidance: [ComputingForGeeks](https://computingforgeeks.com/best-mac-for-local-llm/), [InsiderLLM](https://insiderllm.com/guides/best-local-llms-mac-2026/)
- Qwen3.8-Flash-Next license: [Atomic Chat](https://atomic.chat/models/qwen3-8-flash-next)
- Largest open models: [DeepSeek V4 launch coverage](https://rits.shanghai.nyu.edu/ai/deepseek-releases-v4-open-source-1-6t-moe-with-1m-context), [Qwen3.8 open weights](https://www.alibabacloud.com/blog/alibaba-unveils-qwen3-8-27b-and-releases-weights-of-qwen3-8-flagship-model_603463), [Mistral Large 4 open weights](https://www.datastudios.org/post/mistral-large-4-open-weights-1m-context-modified-mit-license)
