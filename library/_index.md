---
tags:
  - index
title: Library
---

# Library

External signals — articles, repos, papers, bookmarks, transcripts — organized into 18 collections. Each item stores raw content in its body. Synthesis lives in the per-collection `_index.md` files and surfaces here as pointers plus cross-shelf patterns.

> [!tip] The compiled wiki is split across multiple files
> Per-collection synthesis: `library/<slug>/_index.md` (see [Collections](#collections) below).
> Operational log (re-syncs, tombstones, hydration stack changes): [[_CHANGELOG|Library Changelog]].
> Filterable database view: [`all.base`](all.base).

## Structure

Raw items live in `library/<slug>/*.md`. Each file has metadata-only frontmatter (`hydrated: false`) until fetched with the hydration script. Per-collection `_index.md` files compile synthesis for each shelf. This top-level `_index.md` is the cross-shelf view.

## Imported collections

Status: **Raindrop + X/Twitter imports complete** — last sync 2026-04-23. 1,631 items across 19 folders. 3 items render-blocked (Cloudflare/auth-gate) pending manual handling; 4 dead-URL items tombstoned. Full resync history in [[_CHANGELOG|Library Changelog]].

### From Raindrop (1,372 items, 18 folders)

| Collection             | Folder                  | Items     | Synthesis                                               |
| ---------------------- | ----------------------- | --------- | ------------------------------------------------------- |
| AI Tools & News        | `ai-tools-news/`        | 513       | [[ai-tools-news/_index\|AI Tools & News]]               |
| AI Repos & Open Source | `ai-repos-open-source/` | 385       | [[ai-repos-open-source/_index\|AI Repos & Open Source]] |
| Marketing & Business   | `marketing-business/`   | 100       | [[marketing-business/_index\|Marketing & Business]]     |
| Dev Tools & CLI        | `dev-tools-cli/`        | 77        | [[dev-tools-cli/_index\|Dev Tools & CLI]]               |
| Stationery & Journals  | `stationery-journals/`  | 56        | [[stationery-journals/_index\|Stationery & Journals]]   |
| Theology & Faith       | `theology-faith/`       | 50        | [[theology-faith/_index\|Theology & Faith]]             |
| Personal & Misc        | `personal-misc/`        | 42        | [[personal-misc/_index\|Personal & Misc]]               |
| Web Dev                | `web-dev/`              | 40        | [[web-dev/_index\|Web Dev]]                             |
| Academic & Reference   | `academic-reference/`   | 38        | [[academic-reference/_index\|Academic & Reference]]     |
| Design & UI            | `design-ui/`            | 18        | [[design-ui/_index\|Design & UI]]                       |
| Productivity           | `productivity/`         | 16        | [[productivity/_index\|Productivity]]                   |
| Writing & Content      | `writing-content/`      | 15        | [[writing-content/_index\|Writing & Content]]           |
| Cooking                | `cooking/`              | 10        | [[cooking/_index\|Cooking]]                             |
| iOS & Swift            | `ios-swift/`            | 7         | [[ios-swift/_index\|iOS & Swift]]                       |
| Books & Reading        | `books-reading/`        | 5         | [[books-reading/_index\|Books & Reading]]               |
| Recipes                | `recipes/`              | 3         | [[recipes/_index\|Recipes]]                             |
| Photography            | `photography/`          | 1         | [[photography/_index\|Photography]]                     |
| **Raindrop total**     |                         | **1,372** |                                                         |

### From X/Twitter bookmarks (259 items, 1 folder)

Synced via [fieldtheory](https://fieldtheory.dev/cli) (local cache at `~/.ft-bookmarks/bookmarks.jsonl`). Re-sync with `fieldtheory sync --yes` then re-run `python .tools/x_import.py` — importer is idempotent on `tweet_id`.

| Collection  | Folder         | Items   | Synthesis                                   |
| ----------- | -------------- | ------- | ------------------------------------------- |
| X/Twitter   | `x-bookmarks/` | 259     | [[x-bookmarks/_index\|X/Twitter Bookmarks]] |
| **X total** |                | **259** |                                             |

## Collections

One-line hook per shelf — click through to the collection's `_index.md` for themes, notable items, and cross-references.

- [[ai-tools-news/_index|AI Tools & News]] — 513-item working archive of the agentic-AI news/product/essay cycle; agent frameworks, Claude Code SDK, RAG/memory infra, dark-factory essays.
- [[ai-repos-open-source/_index|AI Repos & Open Source]] — 385-repo technical shelf, densest representation of the agentic era; harnesses, skill packs, browser automation, autoresearch, always-on runtime.
- [[marketing-business/_index|Marketing & Business]] — indie-bootstrap library: sustainable revenue, Reddit/community distribution, digital products, boring-profitable businesses.
- [[dev-tools-cli/_index|Dev Tools & CLI]] — terminal-first toolkit biased toward small composable binaries, Rust/Go performance, and deep git + agent integration.
- [[stationery-journals/_index|Stationery & Journals]] — analog craft as discipline: Japanese precision, European heritage, historical method; commonplace books and PKM systems.
- [[theology-faith/_index|Theology & Faith]] — Reformed Presbyterian primary sources, Bible software, patristic/Puritan scholarship, liturgical recovery.
- [[personal-misc/_index|Personal & Misc]] — broad-bandwidth grab-bag: indie games, generative music, modular hardware, careercraft, tech ethics, physical performance.
- [[web-dev/_index|Web Dev]] — modern web stacks for shipping full-stack SaaS quickly; React/TS starters, reactive DBs, edge compute.
- [[academic-reference/_index|Academic & Reference]] — scholar's workbench: classical primary sources, research infrastructure, computational thinking, AI/ML arxiv anchors.
- [[design-ui/_index|Design & UI]] — component systems, design-to-code bridges, AI-assisted generation; Magic UI / Kibo UI / shadcn taste.
- [[productivity/_index|Productivity]] — digital GTD + analog quarterly planning + time-tracking discipline + markdown-KB native apps.
- [[writing-content/_index|Writing & Content]] — craft philosophy, publishing infrastructure, modern writing tools; Kerouac and Kleon alongside Substack-era workflows.
- [[cooking/_index|Cooking]] — whole-foods-forward shelf emphasizing flavor foundations and weeknight-practical technique.
- [[ios-swift/_index|iOS & Swift]] — modern SwiftUI desktop apps, AI-assisted iOS shipping tools, App Store asset automation.
- [[books-reading/_index|Books & Reading]] — compact life-of-the-mind shelf: Hamming, Hamerton, great-engineer wisdom, classical intellectual work.
- [[recipes/_index|Recipes]] — three weeknight-practical recipes, quick companion to the deeper `cooking/` shelf.
- [[photography/_index|Photography]] — single deliberate resource (Glass) signalling a taste for members-run communities over algorithmic feeds.
- [[x-bookmarks/_index|X/Twitter Bookmarks]] — 259 saved tweets: AI agents, LLM capabilities, developer craft, founder reasoning for the agentic era.

## Cross-shelf patterns

Themes that genuinely span 3+ shelves. These are where the library's value compounds — each per-collection `_index.md` notes its slice; this top-level view names the whole.

### AGENTS.md / SKILL.md convention

An emerging documentation format where a markdown file in a repo root reshapes how an AI agent reasons about that project. Spans:

- **AI Tools & News** — how-to guides ([[a-complete-guide-to-agentsmd]], [[how-to-write-a-great-agentsmd-lessons-from-over-2500-reposit]]), Nous Research's Hermes beginners guide.
- **AI Repos & Open Source** — drop-in templates ([[therealseandonahoeagents-md-drop-in-agentsmd-that-makes-ever]]), auto-authoring tools ([[k-dense-aimimeo]]), skill-pack libraries treating portable capability as the unit of distribution.
- **Dev Tools & CLI** — dotfiles reimagined as agent context ([[bpinheiromsmy-setup]]), Val Town CLI shipping with AGENTS.md built in.

### Skill-pack economy

Agents-as-capabilities formalized into distributable packs. Generalist curated libraries, single-domain specialists, and cross-tool translators. Academic side: Corpus2Skill and Externalization papers frame skills as externalized cognition; AI Repos side: 180-skill alirezarezvani pack, 66-skill jeffallan pack, rohitg00/skillkit translator; AI Tools side: Vercel Skills, Addy Osmani production skills, Claude Code skills directory. Three distribution shapes stabilizing: npm-style packages, drop-in AGENTS.md, portable `.agent/` folder.

### Markdown-first personal OS

Three shapes of the same idea: your knowledge base is the operating system.

- **Native app** — [[refactoringhqtolaria]] (Tolaria, Mac desktop markdown-KB manager).
- **Plugin ecosystem** — [[kepanoobsidian-skills-agent-skills-for-obsidian-teach-your-a]] (Obsidian agent skills), and this vault itself.
- **Web KB** — [[cabinet-free-open-source-ai-first-knowledge-base]] (open-source AI-first KB), [[deepwiki-ai-documentation-you-can-talk-to-for-every-repo]] (conversational docs layer).

Underpinned by the stationery/commonplace-book tradition (PKM items in `stationery-journals/`) — digital-analog hybrid as continuity, not replacement.

### Autoresearch / self-evolving agents

The "agent that researches, codes, and improves itself overnight" pattern. Academic-side primary sources: [[bilevel-autoresearch-meta-autoresearching-itself]] (outer loop generates inner search mechanisms at runtime), [[2604-17091v1]] (GenericAgent evolves skill tree from 3.3k-line seed). Repo-side reference impls: [[karpathyautoresearch-ai-agents-running-research-on-single-gp]], [[lsdefinegenericagent-self-evolving-agent-grows-skill-tree-fr]] (first-party 2604-17091 implementation), [[alexzhang13rlm-general-plug-and-play-inference-library-for-r]]. News-side framing: the dark-factory pattern. X/Twitter-side chatter: the autoresearch-is-for-any-domain thread. Direct paper ↔ code ↔ essay ↔ tweet chain.

### Externalization: memory, skills, and knowledge as primitives

Unifying abstraction behind memory products, skill packs, and knowledge graphs: cognition moved out of model weights into manipulable artifacts. [[externalization-in-llm-agents-a-unified-review-of-memory-ski]] is the framing paper. Instances span:

- **Memory products** — [[retaindb-persistent-memory-for-ai-agents-sota-on-longmemeval]], [[tschonleberbrainctl-a-cognitive-memory-system-for-ai-agents]], [[milla-jovovichmempalace-the-highest-scoring-ai-memory-system]], [[agentmemory]], [[brainctl-persistent-memory-for-ai-agents]].
- **Skill packs** — see Skill-pack economy above.
- **Navigable knowledge** — [[corpus2skill-dont-retrieve-navigate]] (constructive result), [[vectorlessflowvectorless-reasoning-native-document-intellige]] (reasoning-native, no-embeddings counter-position to RAG).

### Recursive Language Models + declarative calls

Two intertwined academic lineages with repo + essay expression. **RLM:** models recursively invoking themselves ([[recursive-language-models]] essay, [[rlm-dspy]] module, [[alexzhang13rlm-general-plug-and-play-inference-library-for-r]] inference lib, [[lambda-calculus-llmlambda-rlm-method-for-long-context-rlms-u]] lambda-calculus extension). **DSPy / GEPA:** compiling prompts and programs rather than hand-crafting them ([[dspy-compiling-declarative-language-model-calls-into]] foundational paper, [[gepa-aigepa-optimize-prompts-code-and-more-with-ai-powered-r]] canonical repo, [[twaldinhone-cli-text-optimizer-built-on-gepa-uses-agentic-co]] downstream user, [[intertwinedspy-agent-skills-dspy-31x-agent-skills-validated]] + [[why-i-built-dspy-agent-skills]] essay).

## See also

- [[_CHANGELOG|Library Changelog]] — resync history, hydration stack changes, tombstoned items.
- [`all.base`](all.base) — filterable database view (All, Unhydrated, By source type, Recent, Twitter archive, Gallery).
- `knowledge/hq-vault-design.md` — frontmatter spec.
- `distillery/index.md` — how library feeds content generation.
- `.tools/raindrop_import.py`, `.tools/hydrate.py`, `.tools/x_import.py` — import pipeline.
