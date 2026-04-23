---
tags:
  - index
title: Library
---

# Library

Compiled wiki of external signals. Each section synthesizes what the items collectively tell us — patterns, connections, and implications for our work. Individual files contain raw content; this index is the understanding layer.

<!-- Bot maintains this as a living synthesis document:
- Each concept category includes a summary paragraph synthesizing what the items collectively tell us
- Individual items listed with multi-sentence summaries, not just one-liners
- Cross-references and connections between items are made explicit
- Key takeaways and patterns are surfaced at the category level
- Updated incrementally every time a library item is added or modified
-->

## Structure

Raw items live in `library/<collection-slug>/*.md`. Each file has metadata-only frontmatter (`hydrated: false`) until fetched with the hydration script. This index is the synthesis layer — produced by compiling across items, not by listing them.

For a filterable database view of all items (group by collection, filter by hydrated/source/etc.), open [`all.base`](all.base) in Obsidian. Views: All, Unhydrated, By source type, Recent, Twitter archive, Gallery.

## Imported collections

Status: **Raindrop + X/Twitter imports complete** — last sync 2026-04-23. 1,631 items across 19 folders. 3 items render-blocked (Cloudflare/auth-gate) pending manual handling; 4 dead-URL items tombstoned.

### From Raindrop (1,372 items, 18 folders)

| Collection             | Folder                  | Items     |
| ---------------------- | ----------------------- | --------- |
| AI Tools & News        | `ai-tools-news/`        | 513       |
| AI Repos & Open Source | `ai-repos-open-source/` | 385       |
| Marketing & Business   | `marketing-business/`   | 100       |
| Dev Tools & CLI        | `dev-tools-cli/`        | 77        |
| Stationery & Journals  | `stationery-journals/`  | 56        |
| Theology & Faith       | `theology-faith/`       | 50        |
| Personal & Misc        | `personal-misc/`        | 42        |
| Web Dev                | `web-dev/`              | 40        |
| Academic & Reference   | `academic-reference/`   | 38        |
| Design & UI            | `design-ui/`            | 18        |
| Productivity           | `productivity/`         | 16        |
| Writing & Content      | `writing-content/`      | 15        |
| Cooking                | `cooking/`              | 10        |
| iOS & Swift            | `ios-swift/`            | 7         |
| Books & Reading        | `books-reading/`        | 5         |
| Recipes                | `recipes/`              | 3         |
| Photography            | `photography/`          | 1         |
| **Raindrop total**     |                         | **1,372** |

_Unsorted folder (13 items at import) was rehomed 2026-04-18 across dev-tools-cli, ai-tools-news, ai-repos-open-source, ios-swift, and productivity._

_Re-sync 2026-04-20: 39 new raindrops imported; 38 rehomed out of `unsorted/` (25 → ai-repos-open-source, 8 → ai-tools-news, 3 → academic-reference, 2 → dev-tools-cli). Hydration via github-api, defuddle, arxiv. Note: the 5 SPA-blocked items deleted in that pass (claude-design, nomic-ai, instasdr, schemaflow, brian-oneill) were **re-created** by the 2026-04-22 re-sync — see below. Deletions don't persist unless the raindrop is also removed from the Raindrop.io account._

_Re-sync 2026-04-22 (**+61 items** net, 69 gross minus 4 duplicate raindrops and 4 dead-URL raindrops tombstoned post-sync). First run of the new **`import-raindrops` skill** (SKILL.md in `.agents/skills/`) which codifies the full Raindrop → vault pipeline. Routing: **35 → ai-repos-open-source/** (all github-api hydrated — heavy agent-skills + agent-harness cluster), **19 → ai-tools-news/** (defuddle + Playwright), **3 → academic-reference/** (DSPy, Externalization, Corpus2Skill — see below), **1 → marketing-business/**, **1 → ios-swift/**, **1 → personal-misc/**. Hydration stack: defuddle replaces Jina Reader as the default HTML tier (Jina account depleted — every article-tier call returned HTTP 402); new **trafilatura** tier added for algorithm diversity; new **playwright+trafilatura** tier added as JS-SPA fallback (headless Chromium renders, then trafilatura extracts). Playwright pass resolved the question on the 7 previous stragglers: agentsearch rendered real content; claude.ai/design and trynia.ai rendered but caught only auth-gate / Cloudflare-challenge text; the other 4 (instasdr.ai, home.nomic.ai, schemaflow.dev, w2prisonbreak.com) failed with ERR_NAME_NOT_RESOLVED / ERR_CONNECTION_CLOSED — **the domains no longer exist**. Dead-URL files deleted and their raindrop_ids tombstoned in `.tools/raindrop_deleted.txt` so they don't resurrect. Residual: 2 items (claude-design, nia) are technically hydrated but the body is render-gate text — kept for the record; true content would require login + paid Cloudflare bypass._

_Re-sync 2026-04-23 (**+9 items**, zero tombstones, zero errors — clean pass). Routing: **3 → ai-tools-news/** ([[a-complete-guide-to-agentsmd]], [[hermes-atlas-the-community-map-for-hermes-agent]], [[qwen36-how-to-run-locally-unsloth-documentation]]), **2 → ai-repos-open-source/** ([[k-dense-aimimeo]], [[ton-anywheremy-favorite-prompts-open-source-prompts]]), **2 → dev-tools-cli/** ([[bpinheiromsmy-setup]], [[fallow-rsfallow-find-unused-code-code-duplication-circular-d]]), **1 → academic-reference/** ([[laws-of-software-engineering]]), **1 → productivity/** ([[refactoringhqtolaria]]). Hydration: 5 github-api (all OK), 4 defuddle (all OK — no fallback needed). Thematic signal: the AGENTS.md/SKILL.md convention continues to dominate — three of the nine items (agentsmd guide, mimeo, my-favorite-prompts) are directly about authoring or auto-generating agent instruction files. Cross-cutting second theme is the move toward **markdown-first personal operating systems** ([[refactoringhqtolaria]] as a Mac app, [[bpinheiromsmy-setup]] as a dotfiles-shaped workspace)._

### From X/Twitter bookmarks (259 items, 1 folder)

Synced via [fieldtheory](https://fieldtheory.dev/cli) (local cache at `~/.ft-bookmarks/bookmarks.jsonl`). Re-sync with `fieldtheory sync --yes` then re-run `python .tools/x_import.py` — importer is idempotent on `tweet_id`.

| Collection  | Folder         | Items   |
| ----------- | -------------- | ------- |
| X/Twitter   | `x-bookmarks/` | 259     |
| **X total** |                | **259** |

_Re-sync 2026-04-20 (afternoon): 30 new X bookmarks imported (7 fresh from `ft sync`, 23 backlog). All hydrated via `hydrate.py --type twitter` (fieldtheory-cache). Dominant themes in the batch: coding-agent workflows (Codex, Claude Code, Hermes/OpenClaw autoresearch), Claude Design + video generation (Hyperframes), terminal tooling (zoxide, fff, skills), and a cybersecurity cluster (Google Workspace compromise forensics, DeepMind cyber paper). Outliers: at-home genome sequencing, ASO playbook, Mac cleaner utilities._

## Synthesis

<!-- Compiled wiki entries go here — one section per concept/theme, written after items are reviewed/hydrated. Seeded with Theology & Faith 2026-04-18; remaining collections pending. -->

### Theology & Faith

> [!abstract] Collection overview
> Robert's theology-faith collection reflects a Reformed Presbyterian sensibility: he curates primary sources from the patristic and Reformation traditions alongside practical Bible software tools, scholarly resources on biblical exegesis and Greek, and working communities like L'Abri. The collection shows an integration of craft (liturgy, spiritual disciplines, theological writing) with serious scholarship — favoring primary texts, rigorous methodology, and traditions that take doctrine seriously.

**Key themes:**

- **Bible software & digital exegesis** — A comprehensive toolkit spanning free and premium software ([[bible-search-and-study-tools-blue-letter-bible]], [[e-sword-free-bible-study-for-the-pc]], [[the-crosswire-bible-society-free-bible-software-bringing-the]]) alongside Greek language resources ([[new-testament-greek-guy-randy-leedy]], [[home-free-greek-forever]]) for inductive study and linguistic precision. ^theme-bible-software
- **Reformed & Puritan theology** — Deep engagement with Calvin, Edwards, and Puritan thought through commentaries ([[calvins-commentaries-monergism]]), resources ([[reformed-theology-at-a-puritans-mind-search-the-scriptures-j]], [[puritan-search]]), and epistemology ([[van-til-reformed-epistemologypdf]]), with supporting communities like Monergism. ^theme-reformed-puritan
- **Patristic & early Christian sources** — Primary texts and scholarly editions of the Church Fathers ([[amazoncom-origen-on-first-principles-readers-edition-oxford]], [[home-christian-classics-ethereal-library]]), grounding theological thinking in apostolic and post-apostolic tradition. ^theme-patristic
- **Liturgy & worship renewal** — Resources recovering historical Reformed and liturgical practice ([[reformation-worship-book-liturgies-from-the-past-for-the-pre]]) alongside denominational witness ([[the-orthodox-presbyterian-church-presbytery-of-philadelphia]]), bridging scholarship and lived worship. ^theme-liturgy
- **Biblical scholarship & exegesis** — Methodological resources for serious study ([[inductive-bible-study-a-step-by-step-guide-bible-study-tips]], [[international-standard-bible-encyclopedia-introduction-and-m]]) and institutional affiliation ([[society-of-biblical-literature]]) supporting sustained theological interpretation. ^theme-biblical-scholarship
- **Theological community & formation** — Centers for intellectual work and spiritual hospitality ([[southborough-labri]], [[home-shepherds-theological-seminary-development]], [[great-commission-publications]]) where thought meets lived discipleship. ^theme-theological-community

**Notable items:**

- [[calvins-commentaries-monergism]] — Gateway to Calvin's exhaustive biblical interpretation and foundational Reformed exegesis.
- [[amazoncom-origen-on-first-principles-readers-edition-oxford]] — John Behr's modern English reader's edition of Origen's ontological and hermeneutical masterwork.
- [[reformation-worship-book-liturgies-from-the-past-for-the-pre]] — Rich liturgical resource endorsed by Sinclair Ferguson and Timothy Keller; bridges Reformation theology and worship practice.
- [[bible-search-and-study-tools-blue-letter-bible]] — Most comprehensive free web-based Bible tool combining multiple translations, commentaries, and original language features.
- [[new-testament-greek-guy-randy-leedy]] — Accessible Greek pedagogy and sentence diagramming for exegetical precision.
- [[van-til-reformed-epistemologypdf]] — Van Til's essay connecting epistemology to Reformed theology and Christian apologetics.
- [[southborough-labri]] — American L'Abri community continuing Schaeffer's model of integrated faith, work, and hospitality.
- [[inductive-bible-study-a-step-by-step-guide-bible-study-tips]] — Methodological guide to interpretive discipline and application across all Scripture.
- [[home-christian-classics-ethereal-library]] — CCEL's vast free corpus of public-domain Christian classics, from Augustine to the Puritans.
- [[the-knights-move-the-relational-logic-of-the-spirit-in-theol]] — Distinctive essay on the relational logic of the Spirit in theological method.

**Cross-references:**

- Bible software items (Logos, e-Sword, Xiphos, BibleAnalyzer) parallel items in `dev-tools-cli/` in their philosophy of craft, open-source culture, and serious professional tooling.
- Patristic and epistemology items (Origen, Van Til) cross with any philosophical or metaphysics material surfaced from other collections during later synthesis passes.

### Academic & Reference

> [!abstract] Collection overview
> A scholar's workbench spanning classical primary sources, rigorous research infrastructure, and computational thinking. The shelf pairs primary-text archives (Perseus, Stanford's ORBIS, Fordham's Internet History Sourcebooks) with citation technique (Turabian, DOI tools, Britannica) and cognitive science (mental models, learning-how-to-learn). Programming sits alongside pedagogy — language theory, C fundamentals, and type-driven design treated as disciplines of thought rather than trade skills.

**Key themes:**

- **Classical & primary sources** — Direct access to canonical texts via [[perseus-digital-library]], [[httpsorbisstanfordedu]], and [[internet-history-sourcebooks-project-fordham]]; engaging original material rather than secondary commentary. ^theme-classical-primary
- **Research infrastructure & citation** — Professional-grade scholarship tools: [[turabian-nb-format-final-04232022pdf]], [[doi-citation-formatter]], [[encyclopedia-britannica-britannica]], [[mdpi-publisher-of-open-access-journals]]. ^theme-research-tools
- **Computational thinking as craft** — Language design and type theory as disciplines: [[contents-build-your-own-lisp]], [[parse-dont-validate]], [[notes-on-data-structures-and-programming-techniques-cpsc-223]], [[how-to-c-as-of-2016]], [[ask-hn-best-resources-to-learn-c-programming-hacker-news]]. ^theme-computation
- **Learning & cognition** — Metacognition and study technique: [[mental-models-how-understanding-the-mind-can-transform-how-y]], [[learn-how-to-learn]], [[the-overnight-student-third-revision-dr-michael-l-jones]], [[uncommon-sense-teaching-teaching-online]]. ^theme-learning-science
- **Philosophy of thought** — Principles of clear thinking: [[chestertons-fence-a-lesson-in-thinking]], [[einstein-combinatory-play-is-the-essential-feature-of-though]], [[the-w-edward-deming-institut]]. ^theme-philosophy-thinking
- **AI & data literacy** — Modern technical literacy grounded in the broader scholarly toolkit, increasingly weighted toward primary-source agent-architecture research: [[foundations-of-generative-ai]], [[data-science-harvard-university]], [[bilevel-autoresearch-meta-autoresearching-itself]] (arxiv — bilevel autoresearch: an outer loop meta-optimizes the inner autoresearch loop by reading its code, identifying bottlenecks, and **generating + injecting new Python search mechanisms at runtime** — Tabu Search, Bandit, Orthogonal Exploration — delivering a 5× improvement over Karpathy-style single-level loops on GPT-pretraining benchmark), [[2604-17091v1]] (arxiv — GenericAgent's case for **contextual information density** as the governing constraint on long-horizon agents, operationalized as four interlocking mechanisms: minimal atomic tools, hierarchical on-demand memory, self-evolution of trajectories into reusable SOPs and code, and active context truncation+compression), [[2603-19312v2]] (arxiv — LeWorldModel: the first JEPA trained stably end-to-end from raw pixels using only a next-embedding prediction loss and **SIGReg**, a one-term Gaussian regularizer that replaces EMA, stop-gradient, and frozen foundation encoders — a 15M-parameter world model trainable on a single GPU that plans **48× faster** than foundation-encoder baselines, built on Balestriero's LeJEPA lineage), [[2512-24601v2]] (arxiv — Recursive Language Models: Zhang/Kraska/Khattab reframe long prompts as REPL **environment** rather than tokens to feed the network, letting the LLM write code that peeks/decomposes/recursively invokes itself over slices of the prompt — handles 10M+ token inputs **two orders of magnitude beyond** model context windows, and the post-trained RLM-Qwen3-8B beats vanilla Qwen3-8B by **+28.3%** while approaching GPT-5 quality on three long-context tasks), [[2603-28052v1]] (arxiv — Meta-Harness: Lee/Nair/Zhang/Lee/Khattab/Finn outer-loop search **over harness code itself**, where an agentic proposer reads all prior candidates' source/scores/traces from a filesystem at **10MTok/iter** — three orders of magnitude past prior text optimizers — beating ACE by 7.7 points with 4× fewer context tokens, +4.7 pts on IMO-level math across five held-out models, and ranking #1 among Haiku 4.5 agents on TerminalBench-2). ^theme-ai-data
- **Scholarly infrastructure portals** — Gateway services to research networks: [[ssrn-home-page]] (Social Science Research Network's preprint archive — extends the citation/research-tools theme into social sciences and economics). ^theme-scholarly-portals

**Notable items:**

- [[perseus-digital-library]] — Authoritative digital archive of ancient texts with Greek/Latin originals and English translations.
- [[contents-build-your-own-lisp]] — Hands-on compiler construction teaching language semantics from first principles.
- [[chestertons-fence-a-lesson-in-thinking]] — Distills a foundational principle for thoughtful critique: understand before changing.
- [[parse-dont-validate]] — Type-driven design essay bridging PL theory to practical systems architecture.
- [[mental-models-how-understanding-the-mind-can-transform-how-y]] — Barbara Oakley's metacognition and learning-optimization framework.
- [[turabian-nb-format-final-04232022pdf]] — Chicago notes-bibliography citation standard for scholarly writing.
- [[httpsorbisstanfordedu]] — Stanford's ORBIS geospatial model of Roman networks — premodern logistics as scholarship.
- [[mark-bernstein]] — Hypertext theorist and writer bridging classical rhetoric to digital narrative.
- [[the-w-edward-deming-institut]] — Quality improvement and systems thinking applied across disciplines.
- [[2604-17091v1]] — GenericAgent paper: argues long-horizon agent performance is governed not by context length but by **contextual information density** — how much decision-relevant signal a finite context actually carries. Frames completeness vs conciseness as the primary architectural tension and proposes self-evolution (distilling verified trajectories into SOPs and executable code) as the mechanism that compounds capability across sessions rather than discarding it with each context expiration.
- [[bilevel-autoresearch-meta-autoresearching-itself]] — Bilevel Autoresearch paper: formalizes autoresearch as bilevel optimization where the outer loop reads the inner loop's code and writes new search mechanisms as runtime Python — Tabu Search, Bandit, Orthogonal Exploration — to escape directions the LLM's default search systematically avoids. The 5× empirical gain on Karpathy's GPT benchmark lands the punchline: _if autoresearch can meta-autoresearch itself, it can in principle meta-autoresearch anything with a measurable objective._
- [[2603-19312v2]] — LeWorldModel paper: argues the usual JEPA stack (EMA target encoders, stop-gradient, six-term losses, frozen foundation encoders) is architectural apology for a representation-collapse problem you can just _regularize away_. Replaces all of it with **one** anti-collapse term — SIGReg, which projects latent embeddings onto random 1D directions and minimizes an Epps–Pulley normality test statistic — on top of a plain next-embedding prediction loss. The payoff: a 15M-parameter world model trainable end-to-end from pixels on a single GPU, planning in under a second, beating DINO-WM on pixel-only manipulation tasks, and exhibiting _emergent temporal path straightening_ in latent space with no explicit term encouraging it. The LeJEPA ([25]) provenance is load-bearing: the same SIGReg regularizer that anchors this paper was originally published by Balestriero + LeCun as a general JEPA stability result.
- [[2512-24601v2]] — Recursive Language Models (RLM) paper: argues long-context handling should not be a property of the model but of the **interface around it**. An RLM treats the user's prompt as a string variable inside a REPL environment that the LLM interacts with by writing code — peeking at slices, decomposing, and recursively invoking itself over chunks. The recursion is symbolic and programmatic, not autoregressive verbalization, which sidesteps the output-length cap that breaks self-delegation. Empirical claims: handles inputs at 10M+ tokens (~100× beyond GPT-5's 272K window) without context rot; the post-trained RLM-Qwen3-8B beats its base model by 28.3% and approaches GPT-5 on three long-context tasks while matching cost. Cited by [[2603-28052v1]] as one of the canonical "adaptive access to external context" mechanisms — RLM operates on the prompt, Meta-Harness operates on the harness, but the access pattern is the same.
- [[2603-28052v1]] — Meta-Harness paper: a harness for optimizing harnesses. The proposer is a coding agent that reads all prior candidates' source code, evaluation scores, and execution traces from a **filesystem** — median 82 files per iteration, 20+ prior candidates referenced per step, 10MTok/iter of diagnostic context (vs 0.002–0.026 MTok for OPRO/TextGrad/AlphaEvolve/GEPA/Feedback Descent/TTT-Discover, per Table 1). The architectural punchline: every prior text optimizer compresses feedback (scalar scores, summaries, short templates) and so loses the information needed to trace downstream failures back to harness decisions; Meta-Harness refuses the compression and lets the agent decide what to inspect. Results: +7.7 pts over ACE on online text classification with 4× fewer context tokens, +4.7 pts on 200 IMO-level problems averaged across five held-out models, #1 ranking among Haiku 4.5 agents on TerminalBench-2.

**2026-04-22 addition (+3 papers):** The re-sync added three papers that sharpen the shelf's agent-era coverage:

- [[corpus2skill-dont-retrieve-navigate]] — **Corpus2Skill** (arxiv 2604.14572, Sun/Wei/Hsieh, Apr 2026): reframes RAG from _retrieval_ to _navigation_. Compiles a document corpus offline into a hierarchical tree of LLM-written summary skill files, then lets the agent walk the tree at serve time with a bird's-eye view — drilling into topic branches, backtracking from dead ends, combining evidence across branches. Outperforms dense retrieval + RAPTOR + agentic RAG on WixQA enterprise support. Directly primary-sources the skill-pack economy's central claim: _skills are a better abstraction than embeddings for organizing corpus knowledge that agents need to traverse_. Pairs with [[2604-17091v1]]'s "self-evolution into reusable SOPs and code" — both papers formalize skill-as-memory from different angles.
- [[externalization-in-llm-agents-a-unified-review-of-memory-ski]] — **Externalization in LLM Agents** (arxiv 2604.08224): the bridging survey this shelf needed. Unifies memory, skills, tools, and world models under one framework of _externalized cognition_ — what the agent offloads from its weights into manipulable artifacts. Makes explicit what the practitioner side has been converging on: persistent memory stores ([[retaindb-persistent-memory-for-ai-agents-sota-on-longmemeval]], [[tschonleberbrainctl-a-cognitive-memory-system-for-ai-agents]], [[milla-jovovichmempalace-the-highest-scoring-ai-memory-system]]), portable skill packs ([[alirezarezvaniclaude-skills-180-production-ready-skills-plug]], [[jeffallanclaude-skills-66-specialized-skills-for-full-stack]]), and navigable knowledge ([[corpus2skill-dont-retrieve-navigate]]) are instances of the same architectural commitment.
- [[dspy-compiling-declarative-language-model-calls-into]] — **DSPy** (arxiv 2310.03714, Khattab et al., Oct 2023): the foundational paper behind the declarative-LLM-calls paradigm that GEPA, LongRA, and the entire "optimize-your-prompts" tooling lineage extends. Older than the rest of this cluster, included now as the primary reference for DSPy work appearing across the library ([[intertwinedspy-agent-skills-dspy-31x-agent-skills-validated]], [[rlm-dspy]], [[gepa-aigepa-optimize-prompts-code-and-more-with-ai-powered-r]], [[why-i-built-dspy-agent-skills]]).

**2026-04-23 addition (+1 item):** [[laws-of-software-engineering]] — a curated collection of software-engineering laws and principles (think: Chesterton's Fence, Conway's Law, Brooks's Law). Fits squarely into `^theme-philosophy-thinking` alongside [[chestertons-fence-a-lesson-in-thinking]]; also serves as a quick-reference index the way [[mental-models-how-understanding-the-mind-can-transform-how-y]] does for general cognition.

**2026-04-23 addition (+2 papers):** Two PDFs ingested via `process-pdfs` (marker → academic-reference). Both share a co-author (**Omar Khattab**, MIT) and both implement the same architectural move — _treat the thing the LLM is supposed to think about as an external, navigable environment that the LLM interacts with by writing code, not as tokens to stuff into a prompt_:

- [[2512-24601v2]] — **Recursive Language Models** (arxiv 2512.24601v2, Zhang/Kraska/Khattab, Jan 2026): replaces `[[httpsarxivorgpdf251224601v1]]`'s arxiv-API stub of the v1 abstract with the full v2 PDF body and figures. The headline finding is mechanical: an RLM exposes the same `string → string` interface as an LLM, but internally hands the prompt to a REPL as a variable, exposes its length as metadata, and lets the LLM write Python that peeks/slices/recurses over it. Symbolic recursion sidesteps the output-length cap that breaks autoregressive self-delegation. Empirically RLMs handle 10M+ token inputs (~100× past GPT-5's 272K window), avoid context rot, and the post-trained RLM-Qwen3-8B beats base by 28.3% while approaching GPT-5 on three long-context tasks at comparable cost. Pairs with [[bilevel-autoresearch-meta-autoresearching-itself]] (both let the LLM _generate runtime code_ that operates on the search/reasoning substrate) and the autoresearch repo [[alexzhang13rlm-general-plug-and-play-inference-library-for-r]] (Zhang's own implementation, already in the practitioner shelf).
- [[2603-28052v1]] — **Meta-Harness: End-to-End Optimization of Model Harnesses** (arxiv 2603.28052v1, Lee/Nair/Zhang/Lee/Khattab/Finn, Stanford+KRAFTON+MIT): treats the LLM harness — the code that decides what to store, retrieve, present — as the optimization target, with a coding agent as the proposer and a filesystem-as-history as the search substrate. The Table 1 contrast is the paper's central argument: prior text optimizers (OPRO, TextGrad, AlphaEvolve, GEPA, Feedback Descent, TTT-Discover) all compress feedback to ≤30K tokens per iteration; Meta-Harness exposes ~10M tokens/iter via filesystem and lets the agent decide what to grep/cat. Beats ACE by 7.7 pts on online text classification with 4× fewer context tokens, +4.7 pts on 200 IMO-level math problems across five held-out models, #1 among Haiku 4.5 agents on TerminalBench-2. Subsumes the entire prior text-optimization cluster — it is the empirical case for _full uncompressed history accessed via tool calls_ as the right primitive for outer-loop search, and explicitly cites RLM as a peer mechanism for adaptive external-context access.

**Cross-references:**

- Classical primary sources overlap with Theology & Faith's patristic theme (Perseus and Christian Classics Ethereal Library both serve canonical-text scholarship).
- Life-of-the-mind items connect to Books & Reading below (Hamming, Hamerton, Waterfield work in the same intellectual-formation register).
- Autonomous-research arxiv items link to the research-automation theme in AI Repos & Open Source (`karpathy/autoresearch`, `jhochenbaum/pi-autoresearch-studio`, `alexzhang13/rlm`) and to `knowledge/autoresearch/` project state — the academic lineage behind the agent-harness research-infra work.
- [[2604-17091v1]] anchors a cluster connecting Academic & Reference to three practitioner-side threads elsewhere in the library: agent frameworks and orchestration in AI Repos & Open Source, persistent agent memory ([[retaindb-persistent-memory-for-ai-agents-sota-on-longmemeval]], [[tschonleberbrainctl-a-cognitive-memory-system-for-ai-agents]], [[milla-jovovichmempalace-the-highest-scoring-ai-memory-system]]), and the skill-pack economy. Its "self-evolution of trajectories into reusable SOPs and code" formalizes what the skill-pack market is already shipping in product form. Its "contextual information density" thesis gives the context-engineering essays in AI Tools & News and the context-optimization tweets in X/Twitter Bookmarks a primary-source paper to anchor to.
- [[bilevel-autoresearch-meta-autoresearching-itself]] and [[2604-17091v1]] are the academic-side pair for agent self-improvement: GenericAgent formalizes it at the _architecture_ level (evolving the agent), Bilevel Autoresearch formalizes it at the _research-pipeline_ level (evolving the search mechanism). Together they bracket the self-evolution theme that the autoresearch repos in AI Repos & Open Source ([[karpathyautoresearch-ai-agents-running-research-on-single-gp]], [[jhochenbaumpi-autoresearch-studio-dashboard-plan-editor-pr-w]], [[alexzhang13rlm-general-plug-and-play-inference-library-for-r]]) and the autoresearch discussion in X/Twitter ([[ericosiu-karpathys-autoresearch-isnt-just-for-ai-research-y]], [[joeldeteves-not-enough-of-you-are-using-autoresearch-in-your-o]], [[benburtenshaw-heres-a-hands-on-guide-to-setup-multi-agent-autore]]) are building in practitioner form.
- [[2603-19312v2]] opens a distinct sub-cluster inside AI & data literacy: **self-supervised representation learning for control**. Where [[2604-17091v1]] and [[bilevel-autoresearch-meta-autoresearching-itself]] treat the LLM as the atomic unit and iterate on the harness around it, LeWorldModel treats the encoder–predictor pair as the atomic unit and iterates on the _regularizer_. Same LeCun-adjacent academic lineage — Balestriero co-authors both LeJEPA (the SIGReg source) and LeWM, LeCun co-authors LeWM — but a different engineering discipline: MPC planning in a compact latent space rather than token-space planning with tools. The common thread linking all three papers: _reduce the number of tunable knobs_ (LeWM from six hyperparameters to one, GenericAgent from context-length heuristics to a single density budget, Bilevel Autoresearch from hand-written search mechanisms to runtime-generated ones), _let the thing run, publish the win_.
- [[corpus2skill-dont-retrieve-navigate]] and [[externalization-in-llm-agents-a-unified-review-of-memory-ski]] together form the **skill-as-primitive** cluster on the paper side — the academic counterpart to AI Repos & Open Source's `^theme-repos-skill-packs-generalist` and `^theme-repos-skill-packs-specialist`. Corpus2Skill is the constructive result (how to distill skills from a corpus); Externalization is the framing result (why skills are the right abstraction). Together with [[2604-17091v1]] they establish: a skill pack is not _just_ a prompt library, it is externalized cognition with navigable structure and measurable impact on task performance.
- [[2512-24601v2]] and [[2603-28052v1]] form a **Khattab-cluster** sub-thread: same co-author (Omar Khattab, MIT — also lead author of [[dspy-compiling-declarative-language-model-calls-into]]), same architectural commitment _treat the substrate as an external environment, let the LLM interact with it by writing code, give it adaptive access rather than a packed prompt_. RLM applies it to the prompt itself; Meta-Harness applies it to the harness around the LLM. Meta-Harness explicitly cites RLM as a peer mechanism for adaptive external-context access, alongside RAG and memory-based agents. Combined with [[bilevel-autoresearch-meta-autoresearching-itself]] (LLM-generated runtime code as the search mechanism) and [[2604-17091v1]] (self-evolution of trajectories into reusable code), the academic shelf now coheres around a single thesis: _the unit of progress is not the model weights, it is the executable code the model produces and operates on, and the right way to scale is to give the model uncompressed access to its own history of such code._
- [[2603-28052v1]] also lands the **end of the prompt-optimization era** as a discrete research thread on the academic side: ACE (cited as the prior SOTA it beats by 7.7 pts), GEPA, OPRO, TextGrad, AlphaEvolve/OpenEvolve, Feedback Descent, TTT-Discover are all collapsed into Table 1 as instances of the same compression-bound paradigm Meta-Harness argues against. The X/Twitter context-engineering tweets ([[ericosiu-karpathys-autoresearch-isnt-just-for-ai-research-y]] et al.) and the `^theme-context-engineering` essays in AI Tools & News now have a primary-source paper to point at when arguing for filesystem-shaped scratch spaces over packed-prompt feedback loops.

### Design & UI

> [!abstract] Collection overview
> A developer-designer's toolkit: component systems, design-to-code bridges, and AI-assisted generation. The shelf pairs practical component libraries (Magic UI, Kibo UI, shadcn) with visual reference archives (Mobbin, Sections) and prototyping tools that collapse the design-to-ship loop. The taste is for good design expressed through reusable tokens and well-built primitives rather than pure aesthetics.

**Key themes:**

- **Component systems & design tokens** — Reusable thematic libraries and token editors: [[magic-ui]], [[kibo-ui]], [[yoinkui]], [[beautiful-themes-for-shadcnui-tweakcn-theme-editor-generator]]. ^theme-component-systems
- **Design-to-code automation** — Tools bridging canvas and implementation: [[pencil-design-on-canvas-land-in-code]], [[paper-design-share-ship]], [[polymet-idea-to-prototype-within-seconds]], [[magic-patterns]]. ^theme-design-to-code
- **Visual inspiration & pattern discovery** — Reference libraries for UI patterns: [[mobbin-ui-ux-design-inspiration-for-mobile-web-apps]], [[sectionswtf-inspiring-web-sections]], [[sarica-studio]]. ^theme-visual-inspiration
- **AI-driven design exploration** — Generative tools amplifying iteration: [[variant-endless-designs-for-your-ideas-just-scroll]], [[freepik]], [[magic-patterns]]. ^theme-ai-design
- **Developer-focused tooling** — Copy-paste components and low-code creative tools: [[21stdev-discover-share-and-craft-ui-components]], [[unicorn-studio-no-code-webgl-tool]], [[yoinkui]]. ^theme-dev-tooling

**Notable items:**

- [[magic-ui]] — High-signal component library with animation and interaction focus.
- [[kibo-ui]] — Large pattern collection for layout and structural solutions.
- [[pencil-design-on-canvas-land-in-code]] — Direct design-in-code workflow; developer-friendly aesthetic.
- [[magic-patterns]] — AI prototyping for teams; bridges ideation and validation.
- [[mobbin-ui-ux-design-inspiration-for-mobile-web-apps]] — Industry standard for pattern reference and competitive analysis.
- [[beautiful-themes-for-shadcnui-tweakcn-theme-editor-generator]] — Theme authoring and customization at the token level.
- [[yoinkui]] — Pragmatic: extract real components from live sites.

**Cross-references:**

- Connects to `web-dev/` and `dev-tools-cli/` for the implementation side — design systems assume a build pipeline.

### Cooking

> [!abstract] Collection overview
> A small whole-foods-forward shelf emphasizing flavor foundations (roasted aromatics, homemade broths) and weeknight-practical technique. Character: craft cooking over shortcuts, building depth through process rather than relying on processed ingredients.

**Key themes:**

- **Roasted aromatics & flavor foundations** — Techniques that build depth at the start of a dish (roasted garlic, caramelized bases) recur across soups and mains. ^theme-roasted-aromatics
- **Vegetable-forward soups** — [[30-minute-broccoli-cheddar-soup]] and [[paneras-broccoli-cheddar-soup-the-girl-who-ate-everything]] — Panera-style remakes done properly at home. ^theme-vegetable-soups

**Notable items:**

- [[30-minute-broccoli-cheddar-soup]] — Whole-ingredient weeknight soup with roasted aromatics and aged cheddar.
- [[paneras-broccoli-cheddar-soup-the-girl-who-ate-everything]] — Copycat recipe for Panera's signature soup.

**Cross-references:**

- Pairs with weeknight-practical items in `recipes/` — same whole-ingredient ethos, different format (full technique vs. quick hit).

### Books & Reading

> [!abstract] Collection overview
> A compact shelf on the life of the mind. Great-engineer wisdom (Hamming's _Art of Doing Science and Engineering_ in two editions), a 19th-century classic on intellectual work (Hamerton), a scholar-translator's archive (Robin Waterfield — Plato, Herodotus, Marcus Aurelius), and a reading-as-infrastructure subscription (Perlego). Character: serious formation, not casual consumption.

**Key themes:**

- **Great-engineer wisdom** — [[book-review-the-art-of-doing-science-and-engineering]] and [[stripe-press-the-art-of-doing-science-and-engineering]] both point to Hamming's capstone lectures on scientific style. ^theme-great-engineers
- **Life of the mind** — [[the-intellectual-life-by-philip-gilbert-hamerton]] — 19th-century philosophical treatise on the conditions for an intellectual life. ^theme-intellectual-life
- **Classical scholarship** — [[robinwaterfield]] — translator of Plato, Herodotus, and Marcus Aurelius; primary-source access through a scholar's curation. ^theme-classical-scholarship

**Notable items:**

- [[stripe-press-the-art-of-doing-science-and-engineering]] — Stripe Press's edition of Hamming's capstone lectures on the style of thinking required for scientific work.
- [[book-review-the-art-of-doing-science-and-engineering]] — Corin Wagen's substantive review of Hamming; worth reading before or alongside the book itself.
- [[the-intellectual-life-by-philip-gilbert-hamerton]] — Gutenberg edition of the 19th-century classic on cultivating intellectual habits.
- [[robinwaterfield]] — Archive of Waterfield's translations and scholarly output on Greek classics.
- [[perlego-an-online-subscription-for-all-your-academic-books]] — Academic ebook subscription covering a million-plus scholarly titles.

**Cross-references:**

- Overlaps with Academic & Reference on classical scholarship and great-thinker mode (Hamming's argument about "style" rhymes with Deming and Einstein items there).

### iOS & Swift

> [!abstract] Collection overview
> A small Swift / Apple-platform shelf — modern SwiftUI desktop apps, AI-assisted iOS shipping tools, and production-scale automation for App Store assets. Developer's lens on the Apple ecosystem: shipping real apps with modern tooling.

**Key themes:**

- **SwiftUI for desktop** — [[whisky-a-modern-wine-wrapper-for-macos-built-with-swiftui]] — high-profile open-source Wine wrapper demonstrating what SwiftUI can do on macOS. ^theme-swiftui-desktop
- **AI-assisted iOS shipping** — [[shipswift-ship-full-stack-ios-apps-with-ai]] — full-stack iOS apps with AI tooling. ^theme-ai-ios-dev
- **Automation at scale** — [[parthjadhavios-marketing-capture-automate-multi-locale-asset]] — automating multi-locale App Store asset generation. ^theme-ios-automation

**Notable items:**

- [[whisky-a-modern-wine-wrapper-for-macos-built-with-swiftui]] — Modern SwiftUI macOS app; demo-worthy codebase for Wine-wrapping on Apple Silicon.
- [[shipswift-ship-full-stack-ios-apps-with-ai]] — Framework for shipping full-stack iOS apps with AI tooling.
- [[parthjadhavios-marketing-capture-automate-multi-locale-asset]] — Multi-locale App Store asset automation.
- [[xcode-instruments-time-profiler-improve-performance-with-ai]] — Antoine van der Lee's guide on driving Xcode's Time Profiler with AI assistance to diagnose performance regressions. Extends `^theme-ai-ios-dev`: the AI-assisted iOS story now includes profiling and optimization, not just green-field app shipping.

### Recipes

> [!abstract] Collection overview
> Three weeknight-practical recipes — sheet pan and stir-fry formats prioritizing speed and whole ingredients. Functions as a quick-hit companion to the deeper `cooking/` shelf.

**Key themes:**

- **One-pan weeknight cooking** — [[sheet-pan-steak-fajitas]], [[easy-beef-stir-fry-spend-with-pennies]], and [[garlic-shrimp-stir-fry-the-modern-proper]] all resolve in 30 minutes or less with minimal cleanup. ^theme-weeknight-practical

**Notable items:**

- [[sheet-pan-steak-fajitas]] — Seasoned steak, peppers, and onions roasted together.
- [[easy-beef-stir-fry-spend-with-pennies]] — Budget-conscious beef stir-fry with proper flavor.
- [[garlic-shrimp-stir-fry-the-modern-proper]] — Garlic-forward, quick-cooking shrimp.

### Photography

> [!abstract] Collection overview
> A single, deliberately-chosen resource: Glass, a members-run community for film and analog photographers that rejects algorithmic feeds in favor of genuine discovery. Reveals a taste for craft tradition over comparison-driven social platforms.

**Notable items:**

- [[glass-photography-community]] — Members-run platform for film/analog photographers; craft-community philosophy.

### Stationery & Journals

> [!abstract] Collection overview
> A deep shelf on analog craft as discipline. Japanese precision (Midori, Hobonichi, MUJI, NOLTY) sits alongside European heritage (Smythson, Clairefontaine) and historical method (Locke's commonplace books, Emerson's notebooks). The unifying conviction: handwriting and paper are load-bearing tools for thinking, journaling, and spiritual formation — not nostalgia, but deliberate practice. Planning systems (Franklin, Full Focus) sit alongside knowledge-capture traditions (commonplace, Zettelkasten) because both are expressions of the same commitment to intentional life.

**Key themes:**

- **Japanese stationery heritage** — Subdued aesthetics, dated planners, and functional minimalism: [[guide-to-nolty-planners-diaries-jetpens]], [[pens-and-pencils-japanese-stationery-muji-usa]]. ^theme-japanese-stationery
- **Fountain pens & writing culture** — Handwriting with a quality pen as deliberate ritual: [[the-gentleman-stationer]], [[cloth-paper-luxury-aesthetic-planners-dividers-inserts]]. ^theme-fountain-pens
- **Leather goods & durability** — Heritage makers and handbound journals built to last: [[luxury-leather-goods-stationery-journals-bags-smythson]], [[boss-leather-co]], [[personalised-leather-journals-notebooks]]. ^theme-leather-durability
- **Knowledge capture & note systems** — Commonplace books, Zettelkasten, and hybrid workflows: [[john-lockes-method-for-common-place-books-1685]], [[the-notecard-system-capture-organize-and-use-everything-you]], [[books-about-personal-knowledge-management-and-zettelkasten]]. ^theme-knowledge-systems
- **Planning systems & routines** — Planning as values-tied discipline, not task management: [[lead-your-life-with-the-franklin-planner-planning-system]], [[finishers-journal-30]], [[companion-notebooks]]. ^theme-planning-systems
- **Paper quality & typography** — Substrate matters: [[clairefontaine-stationery-art-crafts-for-school-office-home]], [[emerson-and-his-notebooks]], [[the-lure-of-paper-systems]]. ^theme-paper-quality

**Notable items:**

- [[guide-to-nolty-planners-diaries-jetpens]] — Deep dive into Japanese planning aesthetic and system design.
- [[luxury-leather-goods-stationery-journals-bags-smythson]] — British heritage brand exemplifying 1887+ craft tradition.
- [[john-lockes-method-for-common-place-books-1685]] — Historical method grounding contemporary note-capture in disciplined philosophy.
- [[lead-your-life-with-the-franklin-planner-planning-system]] — Systems-thinking approach to planning tied to life domains.
- [[clairefontaine-stationery-art-crafts-for-school-office-home]] — Paper standard for fountain-pen writing.
- [[emerson-and-his-notebooks]] — Literary precedent for notebook-as-thinking-tool.
- [[the-lure-of-paper-systems]] — Why paper endures for reflection and capture.
- [[finishers-journal-30]] — Structured journal combining planning with reflection.
- [[books-about-personal-knowledge-management-and-zettelkasten]] — Canonical PKM reading list bridging analog and digital.

**Cross-references:**

- Overlaps with Writing & Content on practice/craft (routines, tools) and with Productivity on planning systems (Franklin Planner, quarterly rhythms).

### Writing & Content

> [!abstract] Collection overview
> A working library spanning craft philosophy, publishing infrastructure, and modern writing tools. Timeless principles (Kerouac's spontaneous prose, Kleon's visual thinking) sit alongside contemporary infrastructure (Substack tooling, Amazon KDP, iPad publishing workflows). The thread: serious prose supported by strategic publishing and editorial discipline — content as craft, not content-marketing grind.

**Key themes:**

- **Writing philosophy & craft** — Voice, process, substance: [[kerouac_spontaneous_prosepdf]], [[writing-is-thinking-learning-to-write-with-confidence]], [[austin-kleon-is-a-writer-who-draws]]. ^theme-craft
- **Publishing infrastructure** — DIY and direct-to-reader stacks: [[home-self-publishing-titans]], [[writestack-substack-1-tool-for-notes]], [[how-to-be-a-youtuber-the-ultimate-guide-thomas-frank]], [[publishing-paperback-novels-with-an-ipad-matt-gemmell]]. ^theme-publishing
- **Editorial craft & content strategy** — Audience-first frameworks and working routines: [[doing-content-right]], [[the-doing-content-right-directory-notion]], [[home-writing-routines]], [[writing-examples]]. ^theme-editorial
- **Writers as platforms** — Individual writers building durable ecosystems: [[every]], [[austin-kleon-is-a-writer-who-draws]]. ^theme-writer-platforms

**Notable items:**

- [[writing-is-thinking-learning-to-write-with-confidence]] — Writing as thinking; decouples ideation from drafting.
- [[austin-kleon-is-a-writer-who-draws]] — Visual-verbal integration; constraint deepens craft.
- [[doing-content-right]] — Steph Smith's systematic approach to audience, strategy, and execution.
- [[publishing-paperback-novels-with-an-ipad-matt-gemmell]] — iPad-native workflow for paperback publishing.
- [[kerouac_spontaneous_prosepdf]] — Kerouac's essay arguing for spontaneity and conviction in prose style.
- [[writestack-substack-1-tool-for-notes]] — Modern Substack growth, scheduling, and voice tooling.
- [[home-self-publishing-titans]] — KDP infrastructure and indie-author playbooks.

**Cross-references:**

- Connects to Stationery & Journals on the analog side of writing craft (notebooks, commonplace books) and to Productivity on working routines.

### Productivity

> [!abstract] Collection overview
> A methodical blend of digital task management (OmniFocus GTD), analog quarterly planning (Full Focus Planner), time-tracking discipline (Toggl), and meeting-centric knowledge graphs (Tana). The shelf prioritizes intentional execution over tool proliferation — systems that connect daily tasks to quarterly and annual outcomes, paired with cognitive tooling (mind-mapping, memory) and practical automation.

**Key themes:**

- **Task management & GTD execution** — Structured capture and clearance: [[learn-omnifocus-omnifocus-video-tutorials-articles-webinars]], [[full-focus-planner-increase-productivity-with-the-1-daily-pl]]. ^theme-gtd-execution
- **Quarterly & annual planning** — Outcomes over activity: [[annual-review]], [[2025-planning-workshop]], [[full-focus-planner-increase-productivity-with-the-1-daily-pl]]. ^theme-quarterly-strategy
- **Time measurement & focus** — Intentional time allocation and low-friction workflow: [[toggl-track-time-tracking-software-for-any-workflow]], [[less-chaos-more-focus-raycast-focus]]. ^theme-time-measurement
- **Meeting capture & knowledge graphs** — Synchronous work made queryable: [[tana]]. ^theme-meeting-capture
- **Cognitive tools & automation** — Mental performance and data workflow: [[kam-knight]], [[excel-spreadsheet-automation-tricks]]. ^theme-cognitive-tools

**Notable items:**

- [[learn-omnifocus-omnifocus-video-tutorials-articles-webinars]] — Video-first GTD system with sustained-adoption focus.
- [[full-focus-planner-increase-productivity-with-the-1-daily-pl]] — Quarterly paper planner tying daily tasks to annual goals across 9 life domains.
- [[toggl-track-time-tracking-software-for-any-workflow]] — Team time-tracking with automated background logging.
- [[tana]] — Meeting-as-product platform building persistent knowledge graphs.
- [[annual-review]] — 63-page strategic review workbook.
- [[kam-knight]] — Speed reading, mind-mapping, and memory ebooks for knowledge retention.
- [[the-john-macarthur-bible-reading-plan]] — Structured spiritual-discipline reading regimen (lives here because of its planning-rhythm ethos).

**2026-04-23 addition (+1 item):** [[refactoringhqtolaria]] — Tolaria, a Mac desktop app for managing markdown knowledge bases (1.3k stars). Positioned for second-brains, company docs as AI context, and storing OpenClaw/assistants memory and procedures. First first-party markdown-KB **native app** in the library — the productized counterpart to Obsidian (which Robert uses for this vault) and the Claude Code/skills-side tools in AI Repos & Open Source. Suggests a cross-cutting "markdown-first personal OS" thread that now spans a native app (Tolaria), a plugin ecosystem (Obsidian skills — [[kepanoobsidian-skills-agent-skills-for-obsidian-teach-your-a]]), and a web KB ([[cabinet-free-open-source-ai-first-knowledge-base]]).

**Cross-references:**

- Planning-rhythm items overlap with Stationery & Journals (Franklin Planner appears in both shelves from different angles).
- Tolaria connects to AI Repos & Open Source's Claude Code / Obsidian-skills cluster and to AI Tools & News's [[cabinet-free-open-source-ai-first-knowledge-base]] as the three shapes of a markdown-first personal OS (native app, plugin ecosystem, web KB).

### Personal & Misc

> [!abstract] Collection overview
> A grab-bag reflecting unusually broad bandwidth: indie game/simulation design, generative music and live coding, modular hardware and privacy-first computing, careercraft concerns, tech-ethics and surveillance, and physical performance tracking. The unifying signal is restless curiosity paired with a bias toward systems and craft — gear chosen deliberately, not by hype.

**Key themes:**

- **Game design & creative systems** — Simulation and spatial mechanics: [[bitcraft]], [[bitcraft-online-on-steam]], [[gdc-vault]]. ^theme-game-design
- **Music & sound as practice** — Generative composition and live coding: [[für-alina-composition-techniques-any-old-music]], [[getting-started-strudel]]. ^theme-music-practice
- **Tools & modular hardware** — Deliberate gear and privacy-first computing: [[smart-desk-mat]], [[introducing-the-framework-desktop-and-newest-framework-lapto]], [[futo]]. ^theme-tools-craft
- **Careercraft & optionality** — Engineering identity, compensation, and agency: [[staff-product-engineer-ghost]], [[ask-hn-who-is-hiring-january-2025-hacker-news]], [[increase-your-optionality]]. ^theme-careercraft
- **Tech ethics & power** — Surveillance, culture, and developer values: [[going-through-snowden-documents-part-1-librootorg]], [[what-do-i-mean-by-some-software-devs-are-ngmi]], [[stop-avoiding-politics]]. ^theme-tech-ethics
- **Physical performance** — Quantified training and recovery: [[whoop-unlock-human-performance-healthspan]], [[starting-strength-gyms-stronger-is-better]]. ^theme-health

**Notable items:**

- [[bitcraft]] — Top-down simulation design with deep economic systems.
- [[futo]] — Privacy-first computing philosophy and self-managed tooling.
- [[going-through-snowden-documents-part-1-librootorg]] — Serious engagement with surveillance and power.
- [[stop-avoiding-politics]] — Willingness to engage political philosophy directly.
- [[smart-desk-mat]] — Taste for attentive physical workspace design.
- [[brettterpstracom]] — Independent creator systems and macOS tooling.
- [[welcome-to-the-10k-institute]] — Deliberate-practice framing of skill development.
- [[starting-strength-gyms-stronger-is-better]] — Barbell-first strength training network.
- [[twaldin-portfolio]] — Tim Waldin's personal site; paired with his agentic-tooling repos ([[twaldinhone-cli-text-optimizer-built-on-gepa-uses-agentic-co]]) in AI Repos & Open Source. Independent-builder archetype with an agent-tooling emphasis.

### Web Dev

> [!abstract] Collection overview
> A catalog of modern web stacks oriented toward shipping full-stack SaaS quickly: React/TypeScript starters, reactive databases, full-stack BaaS, edge compute, and developer-craft tooling. Taste signals lean toward owning the stack (Convex, Appwrite, self-hosted), type-safe primitives (GraphQL, sqlc-style), and DX-first frameworks over convention-heavy frameworks.

**Key themes:**

- **React & SaaS starters** — Production-ready TypeScript/React boilerplates: [[react-starter-kit-launch-your-saas-quickly]], [[open-saas]], [[react-bits]], [[one-a-react-framework]]. ^theme-react-saas
- **Real-time databases** — Reactive data layers and local-first alternatives: [[convex-the-reactive-database-for-app-developers]], [[instantdbinstant-instant-is-a-modern-firebase-we-make-you-pr]], [[livestore-local-first-data-layer-for-high-performance-apps]], [[spacetimedb]]. ^theme-realtime-db
- **Backend & APIs** — Full-stack BaaS and GraphQL-first backends: [[appwrite-build-like-a-team-of-hundreds]], [[graphile-powerful-extensible-and-performant-graphql-apis-rap]], [[build-an-mvp-with-elixir]], [[home-django-rest-framework]]. ^theme-backend-apis
- **Edge & serverless** — Globally distributed compute: [[cloudflare-workers]]. ^theme-edge-deploy
- **DX & build tooling** — Git workflows, code search, and docs frameworks: [[gitbutler]], [[code-search-grep-by-vercel]], [[fumadocs]], [[untitled-ui-react-react-component-library]]. ^theme-devtools-craft
- **Cross-platform & mobile** — React Native/Expo starters: [[obytes-starter-react-nativeexpo-starter]], [[20-starter-templates-to-create-your-react-native-project-wes]]. ^theme-mobile-fullstack

**Notable items:**

- [[convex-the-reactive-database-for-app-developers]] — Reactive database solving state sync for modern apps.
- [[open-saas]] — Full-stack SaaS foundation emphasizing code ownership.
- [[appwrite-build-like-a-team-of-hundreds]] — Self-hosted BaaS for teams who want infra ownership.
- [[cloudflare-workers]] — Edge compute for fast, globally distributed backend logic.
- [[gitbutler]] — Git branching UI that rethinks developer iteration.
- [[graphile-powerful-extensible-and-performant-graphql-apis-rap]] — Postgres-native GraphQL for type-safe APIs.
- [[fumadocs]] — Modern docs framework for shipping knowledge at SaaS velocity.
- [[instantdbinstant-instant-is-a-modern-firebase-we-make-you-pr]] — Firebase alternative with instant sync primitives.
- [[react-starter-kit-launch-your-saas-quickly]] — Fast-path React/TypeScript SaaS scaffold.

**Cross-references:**

- Connects to `design-ui/` for component systems (shadcn, Magic UI, Kibo UI) that sit on top of these stacks, and to `dev-tools-cli/` for build tooling (rolldown, bundlers).

### Dev Tools & CLI

> [!abstract] Collection overview
> A terminal-first toolkit with a clear bias: small, composable binaries, Rust/Go performance, and deep integration with git and AI agents. The shelf covers modernized Unix replacements, next-gen Python (marimo, pyrefly), git-native API clients (Bruno), single-file backends (PocketBase), and LLM-agent scaffolding. Philosophy: serious craft tooling, not toy commands — every item here repays attention with power.

**Key themes:**

- **Terminal & TUI frameworks** — High-performance TUIs and modernized Unix: [[ratatui]], [[charm]], [[eza]]. ^theme-terminal-ui
- **Editor & language tooling** — Fast analyzers and editor integrations: [[dmtrkovalenkofffnvim-the-fastest-and-the-most-accurate-file]], [[pyrefly-a-fast-python-type-checker-and-language-server-pyref]], [[jendrikseippvulture-find-dead-python-code]]. ^theme-editor-lang
- **Git-native API & workflow** — API clients that live in version control: [[bruno-the-git-native-api-client]]. ^theme-api-git
- **CLI frameworks & scaffolding** — Fast, memory-safe CLI generation and templates: [[nashsuautocli-autocli-is-a-blazing-fast-memory-safe-command]], [[cobradev]], [[base]], [[copier]]. ^theme-cli-frameworks
- **Python ecosystem & reactive notebooks** — Modern Python computing: [[marimo-a-next-generation-python-notebook]], [[how-to-set-up-a-perfect-python-project]]. ^theme-python-ecosystem
- **Self-hostable backends & deploy** — Minimal, single-binary platforms: [[pocketbase-open-source-backend-in-1-file]], [[shuttle-build-backends-fast]], [[coolify]]. ^theme-backends-deploy
- **Type-safe codegen** — SQL-to-code and bundler tooling: [[sqlcdev]], [[announcing-rolldown-vite]]. ^theme-codegen
- **AI-first dev tooling** — LLM-aware CLIs and agent scaffolding: [[introducing-vt-the-val-town-cli]], [[one-cookiecutter-to-build-agents-in-seconds]], [[openagents-orgopenagents-openagents-ai-agent-networks-for-op]], [[lazypi-the-fastest-way-to-fall-in-love-with-pi]] (Pi coding-agent setup). ^theme-ai-first
- **Agent-native terminals** — Terminals redesigned from the ground up for agent coordination rather than retrofitted: [[tw93kaku-a-fast-out-of-the-box-terminal-built-for-ai-coding]] (Kaku — fast, out-of-the-box, purpose-built for AI coding; sibling trajectory to Warp in the ai-tools-news shelf). ^theme-agent-terminals
- **Observability & security** — Monitoring and binary analysis: [[better-stack-radically-better-observability-stack]], [[nationalsecurityagencyghidra-ghidra-is-a-software-reverse-en]]. ^theme-observability

**Notable items:**

- [[bruno-the-git-native-api-client]] — Git-native API testing; collections as plain text alongside code.
- [[ratatui]] — Rust TUI framework powering csvlens, oxker, and other production apps.
- [[pocketbase-open-source-backend-in-1-file]] — Realtime DB, auth, files, and admin in a single Go binary.
- [[marimo-a-next-generation-python-notebook]] — Reactive, git-friendly notebook replacing Jupyter.
- [[shuttle-build-backends-fast]] — Deploy Rust services with one annotation; zero-touch AWS provisioning.
- [[sqlcdev]] — Compile SQL to type-safe code; catch schema drift before runtime.
- [[eza]] — Rust `ls` replacement with git awareness and color.
- [[pyrefly-a-fast-python-type-checker-and-language-server-pyref]] — Fast Python type checker and LSP.
- [[introducing-vt-the-val-town-cli]] — Val Town CLI with AGENTS.md context for Claude Code / Cursor.
- [[better-stack-radically-better-observability-stack]] — AI-SRE-flavored observability stack, Datadog alternative.
- [[announcing-rolldown-vite]] — Rust-native Rollup replacement powering Vite's next generation.
- [[tw93kaku-a-fast-out-of-the-box-terminal-built-for-ai-coding]] — Kaku: fast, agent-native terminal; closest peer to Warp in this shelf.

**2026-04-23 addition (+2 repos):** [[fallow-rsfallow-find-unused-code-code-duplication-circular-d]] — Rust CLI that finds unused code, code duplication, circular dependencies, and complexity hotspots in TypeScript/JavaScript projects (900+ stars). Sibling to the Python [[jendrikseippvulture-find-dead-python-code]] already on this shelf, extending the dead-code-finder theme to TS/JS. [[bpinheiromsmy-setup]] — a single-dev setup repo (dotfiles + machine-specific configuration following AGENTS.md/skill-creator conventions). Notable because it treats developer setup itself as agent-readable context — an instance of the broader pattern of turning personal workflows into agent-consumable artifacts.

**Cross-references:**

- Overlaps with `ai-tools-news/` and `ai-repos-open-source/` on agent frameworks and LLM dev tooling, and with `web-dev/` on build/bundler tooling.

### Marketing & Business

> [!abstract] Collection overview
> An indie-bootstrap library that rejects growth-hacking vanity metrics in favor of sustainable revenue, community-driven distribution (Reddit, email, content), and disciplined positioning. Pricing for profitability over scale, digital products over SaaS-only, "boring" businesses with real margins — aligned with Robert's "Kill Your SaaS" ethos and Reformed instinct for craft over hype.

**Key themes:**

- **Indie revenue architecture** — Profitable solo and small-team businesses: [[what-i-learned-from-a-digital-products-expert-who-makes-90-o]], [[building-a-30kmo-portfolio-within-eight-months-of-quitting-h]], [[rosewell-build-a-profitable-saas]], [[the-most-future-proof-job-entrepreneurship]]. ^theme-indie-revenue
- **Positioning & customer psychology** — Authentic positioning and buyer behavior: [[the-slc-approach-building-products-that-customers-love]], [[why-we-buy]], [[how-to-find-buyer-intent-keywords-and-turn-them-into-leads]]. ^theme-positioning
- **Content & organic distribution** — Community-first, no-paid-ads: [[reddit-became-my-most-consistent-growth-engine-once-i-stoppe]], [[reddit-marketing-playbook-500-leads-in-15-days]], [[21-highly-effective-content-templates-for-linkedin-by-charle]]. ^theme-content-distribution
- **Digital products & leverage** — Margin-friendly product shapes: [[24-digital-product-ideas-sorted-by-type-how-to-sell-them-onl]], [[from-0-to-1-million-users-in-6-months-how-i-built-my-viral-a]], [[selling-ebooks-on-amazon-or-your-website-proscons-examples]]. ^theme-digital-products
- **Community & superfans** — Durable moats through loyalty, not algorithms: [[the-modern-marketing-system-we-make-superfans]], [[how-to-make-10kmonth-from-a-community-jordan-godbey-deep-div]], [[growing-a-community-for-digital-nomads-to-33000mo]]. ^theme-community
- **Bootstrap SaaS playbooks** — Minimal-viable stacks and pivots: [[1-week-saas-mvp-checklist-notion]], [[pivoting-to-reach-a-wider-audience-and-hitting-a-5-figure-mr]]. ^theme-saas-solo
- **Boring profitable businesses** — Unsexy niches with predictable revenue: [[discover-boring-businesses-that-quietly-rake-in-the-cash]], [[trustmrr-verified-startup-revenue-database]]. ^theme-boring-profitable

**Notable items:**

- [[from-0-to-1-million-users-in-6-months-how-i-built-my-viral-a]] — 60-page viral playbook: onboarding loops, paywalls, referrals — no paid ads.
- [[reddit-became-my-most-consistent-growth-engine-once-i-stoppe]] — Precision Reddit targeting over volume; subreddit-matching logic.
- [[rosewell-build-a-profitable-saas]] — Course on SaaS ideation and solo-founder exits.
- [[what-i-learned-from-a-digital-products-expert-who-makes-90-o]] — Gumroad-first solopreneur toolkit.
- [[the-modern-marketing-system-we-make-superfans]] — Loyalty over vanity metrics framework.
- [[discover-boring-businesses-that-quietly-rake-in-the-cash]] — Database of niche profitable businesses.
- [[21-highly-effective-content-templates-for-linkedin-by-charle]] — LinkedIn templates from a 300K+ audience.
- [[1-week-saas-mvp-checklist-notion]] — Next.js + Supabase + Stripe stack shipping in a week.
- [[the-most-future-proof-job-entrepreneurship]] — Entrepreneurship framed as AI-resilient career path.
- [[the-slc-approach-building-products-that-customers-love]] — SLC (Simplify, Link, Clarify) product framework.
- [[why-we-buy]] — Behavioral economics applied to buying decisions.
- [[trustmrr-verified-startup-revenue-database]] — Verified MRR data across startups for benchmarking.

**2026-04-22 addition (+1):** [[speedrun-a16z-apply]] — a16z Speedrun accelerator application page; first explicit VC/accelerator artifact in the shelf. Signals a slight broadening from pure indie-bootstrap toward the accelerator-as-option adjacency, though it doesn't yet reshape the shelf's indie-first posture. (A second 2026-04-22 candidate, Brian O'Neill's independent-consultant landing page, was tombstoned after the Playwright pass confirmed `w2prisonbreak.com` no longer resolves.)

**Cross-references:**

- Indie-publishing tactics overlap with Writing & Content (Substack, KDP) and with Productivity on execution rhythms.

### X/Twitter Bookmarks

> [!abstract] Collection overview
> 259 saved tweets forming a working reference archive — not ephemera. Dominated by AI agents, LLM capabilities, and developer craft, with recurring founder/solo-builder voices on distribution-in-the-agentic-era. Robert uses X bookmarks deliberately: the saved tweets are the ones that clarified a hard problem (agent design, prompt engineering, system architecture) or captured a sharp piece of founder reasoning worth returning to. High signal-to-noise compared to a typical bookmark dump.

**Key themes:**

- **AI agents & autonomous systems** — Architecture and workflow of agents that reason and act: [[agentwrapper-85733945]], [[mosescreates-im-going-all-in-on-hermes-nousresearch-teknium-as]], [[av1dlive-in-14-minutes-this-anthropic-engineer-who-wrote-bu]]. ^theme-x-agents
- **LLM knowledge bases & hidden capabilities** — Working with Claude/LLMs as personal knowledge infrastructure: [[karpathy-llm-knowledge-bases-something-im-finding-very-usef]], [[bcherny-i-wanted-to-share-a-bunch-of-my-favorite-hidden-an]]. ^theme-x-llm-capabilities
- **Developer discipline & pipelines** — Repeatable craft: research → build → review → iterate: [[shpigford-my-entire-dev-pipeline-is-basically-just-repeating]], [[ericosiu-karpathys-autoresearch-isnt-just-for-ai-research-y]]. ^theme-x-dev-craft
- **Solo founder & bootstrap strategy** — Economic arguments and playbooks for the agentic era: [[alexprompter-if-i-woke-up-broke-tomorrow-with-50000-in-debt-and]], [[damianplayer-when-anyone-can-build-anything-the-only-moat-left]], [[av1dlive-we-will-soon-have-solo-founder-billionaires-this-w]]. ^theme-x-founder
- **Learning & frontier research** — High-signal resources for staying current: [[cqwww-the-best-book-for-2026-is-available-as-an-open-sou]], [[askalphaxiv-the-best-way-to-learn-frontier-research-is-to-repl]]. ^theme-x-learning
- **Prompt engineering & context optimization** — Context-window discipline and instruction craft: [[alvinsng-useeffect-linting-agent-readiness-context-compress]]. ^theme-x-prompting
- **CEO / enterprise signal on AI** — What serious operators are saying: [[ashleevance-dont-think-ive-heard-any-other-ceo-describe-agent]]. ^theme-x-enterprise-ai

**Voices recurring in the archive (by save count):**

- **@gkisokay** (6 saves) — AI tooling and practical agent applications.
- **@nykbuilderz** (6 saves) — Builder-mindset and agent-framework content.
- **@hooeem** (4 saves) — Prompt engineering and context-window optimization.
- **@oliverhenry** (4 saves) — AI architecture and system thinking.
- **@nickspisak** (4 saves) — Developer discipline and practical tooling.
- **@ernestosoftware** (4 saves) — Software engineering practices and optimization.
- **@aiedge** (4 saves) — AI news, capability tracking, and frontier releases.
- **@bcherny** (3 saves) — Deep dives into Claude Code internals and underused features.
- **@av1dlive** (3 saves) — Anthropic-adjacent engineering and extended-thinking insights.
- **@ryancarson** (3 saves) — Founder and business insights with craft instincts.

**Notable items:**

- [[karpathy-llm-knowledge-bases-something-im-finding-very-usef]] — Karpathy on using LLMs as personal knowledge bases; foundational framing.
- [[bcherny-i-wanted-to-share-a-bunch-of-my-favorite-hidden-an]] — Insider tour of underused Claude Code features.
- [[shpigford-my-entire-dev-pipeline-is-basically-just-repeating]] — Developer discipline compressed into 6 repeatable skills.
- [[mosescreates-im-going-all-in-on-hermes-nousresearch-teknium-as]] — Full agentic-stack commitment; agents + Hermes + Nous Research.
- [[ericosiu-karpathys-autoresearch-isnt-just-for-ai-research-y]] — Autoresearch applied beyond AI research to startup experimentation.
- [[av1dlive-in-14-minutes-this-anthropic-engineer-who-wrote-bu]] — Anthropic engineer on system design at the frontier.
- [[alexprompter-if-i-woke-up-broke-tomorrow-with-50000-in-debt-and]] — First-principles rebuild strategy from a serious operator.
- [[damianplayer-when-anyone-can-build-anything-the-only-moat-left]] — Distribution as the last remaining moat in the agentic era.
- [[av1dlive-we-will-soon-have-solo-founder-billionaires-this-w]] — The economic argument for AI-leveraged solo founders.
- [[ashleevance-dont-think-ive-heard-any-other-ceo-describe-agent]] — CEO-level framing of agentic systems and business implications.
- [[cqwww-the-best-book-for-2026-is-available-as-an-open-sou]] — Open-source reference worth bookmarking.
- [[agentwrapper-85733945]] — Agent framework and architecture reference.

**2026-04-20 addition (+30 items):** The afternoon batch deepens existing themes and surfaces two adjacencies worth naming:

- **Claude Design + video generation** — [[viktoroddy-claude-design-is-insane-just-recorded-a-18-min-tut]], [[nateherk-been-getting-some-crazy-good-video-outputs-lately]], [[liu8in-this-is-insane-in-a-good-way-now-claudeais-got-des]] — Claude Design lands as a serious creative surface; pairs with Hyperframes for animated outputs. New sub-theme under AI agents.
- **Agentic coding workflows mature** — [[iruletheworldmo-a-masterclass-in-coding-agents-from-the-head-of-an]] (Anthropic masterclass), [[rileybrown-my-codex-setup-cannot-be-beat-gt-codex-54-xhigh-fo]] (Codex 5.4 xhigh + Opus 4.7 split), [[joeldeteves-not-enough-of-you-are-using-autoresearch-in-your-o]] (autoresearch in Hermes/OpenClaw), [[benburtenshaw-heres-a-hands-on-guide-to-setup-multi-agent-autore]] (Karpathy-style multi-agent autoresearch), [[nousresearch-the-hermes-agent-creative-hackathon-starts-now-16]] (Hermes hackathon). Extends `^theme-x-agents` — the playbooks are now specific (which model for which task) rather than aspirational.
- **Cybersecurity enters the archive** — [[brendanfalk-to-check-if-your-google-workspace-has-been-comprom]] (Workspace compromise forensics), [[howtoai-google-deepmind-just-dropped-the-most-terrifying-c]] (DeepMind cyber paper). New theme; may warrant its own ^theme-x-security anchor if the cluster grows.
- **Terminal + dev-craft adjacency** — [[heynavtoor-10-terminal-tools-that-make-you-10x-faster-in-2026]], [[emilpriver-alright-my-go-to-extensions-are-pi-fff-uses-fff-by]], [[jakubkrehel-make-interfaces-feel-better-npx-skills-add-jakubkr]] — extends `^theme-x-dev-craft` and cross-references `ai-repos-open-source/` skill-pack economy.
- **Knowledge-workflow tooling** — [[omarsar0-yt-podcast-llm-artifact-this-is-now-my-favorite-wa]] (YT → LLM artifact). Reinforces `^theme-x-llm-capabilities`.

**Cross-references:**

- Agent-and-LLM threads overlap with `ai-tools-news/` and `ai-repos-open-source/` (tweets often preview the tools later written up there).
- Founder/builder tweets overlap with Marketing & Business on distribution and positioning.
- Developer-craft tweets overlap with Dev Tools & CLI on tooling discipline.
- Claude Design / video-generation items cross-reference the Claude Code ecosystem cluster in `ai-repos-open-source/`.

### AI Repos & Open Source

> [!abstract] Collection overview
> 348 GitHub repos — the largest technical-tools shelf in the library and the densest representation of the agentic era. Dominated by agent frameworks (harnesses, orchestration, multi-agent teams), agent-as-backend patterns (Agno, AgentField, LlamaIndex), a fast-growing **skill-pack economy** where portable, composable agent-skills are themselves the product, RAG & vector infrastructure, and production-grade CLI tooling. The repos trend toward serious craft — battle-tested production frameworks over weekend-project toys, and single-file or minimal-infra deployables over microservice sprawl. Memory, sandboxing, and browser/web access show up as first-class primitives, not afterthoughts. As of April 2026, skill packs have become their own taxonomy layer: generalist curated libraries (66–180 skills per repo), single-domain specialists (color science, taste, anti-slop prose), and cross-tool translators that port the same skill across Claude Code, Codex, Cursor, and Copilot.

**Key themes:**

- **Agent frameworks & orchestration** — Multi-agent teams, harnesses, and workflow engines: [[microsoftautogen-a-programming-framework-for-agentic-ai]], [[agno-agiagno-full-stack-framework-for-building-multi-agent-s]], [[hkudsopenharness-openharness-open-agent-harness]], [[jackchen-meopen-multi-agent-production-grade-multi-agent-orc]], [[simstudioaisim-sim-is-an-open-source-ai-agent-workflow-build]], [[openaisymphony-symphony-turns-project-work-into-isolated-aut]]. ^theme-repos-agent-frameworks
- **Agent-as-backend infrastructure** — Agents treated as composable services with identity, audit, state: [[agent-fieldagentfield-framework-for-ai-backend-build-and-run]], [[agent-fieldswe-af-autonomous-software-engineering-fleet-of-a]], [[bytedancedeer-flow-an-open-source-superagent-harness-that-re]]. ^theme-repos-agent-backend
- **Claude Code ecosystem** — Skills, plugins, configs, curated lists: [[anthropicsclaude-code-claude-code-is-an-agentic-coding-tool]], [[alirezarezvaniclaude-skills-180-production-ready-skills-plug]], [[hesreallyhimawesome-claude-code-agents-a-curated-list-of-awe]], [[affaan-meverything-claude-code-complete-claude-code-configur]], [[kepanoobsidian-skills-agent-skills-for-obsidian-teach-your-a]], [[ykdojoclaude-code-tips-45-tips-for-getting-the-most-out-of-c]], [[dennisonbertramux-toolkit-claude-code-plugin-ux-story-genera]]. ^theme-repos-claude-ecosystem
- **Agent skill packs — generalist curated libraries** — Broad-coverage skill collections that treat portable capability as the unit of distribution: [[jeffallanclaude-skills-66-specialized-skills-for-full-stack]] (66 full-stack skills), [[mxyhiok-skills-curated-ai-coding-agent-skills-and-agentsmd-p]] (Codex/Claude Code/Cursor/OpenClaw playbooks), [[honnibalclaude-skills-claude-skills-im-experimenting-with-pl]] (spaCy author), [[jimliubaoyu-skills]], [[androidskills]] (Google's Android team), [[omer-metinskills-for-antigravity]], [[intertwinedspy-agent-skills-dspy-31x-agent-skills-validated]] (DSPy 3.1 + GEPA optimization). ^theme-repos-skill-packs-generalist
- **Agent skill packs — specialist & cross-tool** — Single-domain skills plus the translation layer that makes them portable: [[meodaiskillcolor-expert-agent-skill-for-color-science-expert]] (color science, APCA/WCAG), [[leonxlnxtaste-skill-taste-skill-high-agency-frontend-gives-y]] (frontend taste / anti-slop), [[conorbronsdonavoid-ai-writing-skill-that-audits-and-rewrites]] (scrubs AI-patterned prose), [[rohitg00skillkit-supercharge-ai-coding-agents-with-portable]] (skill translator across 40+ tools). ^theme-repos-skill-packs-specialist
- **RAG, vector search, and memory** — Retrieval infrastructure and long-term context: [[quivrhqquivr-opiniated-rag-for-integrating-genai-in-your-app]], [[run-llamallama_index-llamaindex-is-the-leading-framework-for]], [[milla-jovovichmempalace-the-highest-scoring-ai-memory-system]], [[memodb-ioacontext-agent-skills-as-a-memory-layer]], [[rohitg00agentmemory-1-persistent-memory-for-ai-coding-agents]], [[khoj-aikhoj-your-ai-second-brain-self-hostable-get-answers-f]], [[tschonleberbrainctl-a-cognitive-memory-system-for-ai-agents]] (single-file SQLite cognitive memory + MCP). ^theme-repos-rag-memory
- **Web interaction for agents** — Browser automation and sandboxed environments: [[browser-usebrowser-use-make-websites-accessible-for-ai-agent]], [[browser-usebrowser-harness-self-healing-browser-harness-that]] (self-healing variant by same author), [[hacker-valley-mediainterceptor-agent-driven-chrome-extension]] (Chrome extension as CLI surface), [[revylaiapp-explorer-map-every-screen-and-user-path-in-a-mobi]] (mobile navigation mapping), [[agent-infrasandbox-all-in-one-sandbox-for-ai-agents-that-com]], [[d4vinciscrapling-an-adaptive-web-scraping-framework-that-han]], [[panniantongagent-reach-give-your-ai-agent-eyes-to-see-the-en]]. ^theme-repos-web-interaction
- **Agentic developer tooling** — Terminal-first pair programmers and code agents: [[aider-aiaider-aider-is-ai-pair-programming-in-your-terminal]], [[charmbraceletcrush-the-ai-coding-agent-for-your-favourite-te]], [[stablyaiorca-orca-is-the-next-gen-ide-for-building-with-codi]], [[openaicodex-plugin-cc-use-codex-from-claude-code-to-review-c]]. ^theme-repos-dev-tooling
- **Always-on & overnight agent runtime** — The "agent that doesn't stop working when you do" pattern: [[lnikellloopndroll-keep-codex-running-forever]] (continuous Codex loop), [[kunchenguidgnhf-before-i-go-to-bed-i-tell-my-agents-good-nig]] (overnight handoff workflow), [[edxethpi-subagents]], [[robzolkoslazypi-pi-coding-agent-setup-for-the-lazy]]. ^theme-repos-always-on
- **Semantic search & knowledge** — Local semantic search CLIs, knowledge platforms: [[dennisonbertramlgrep-local-semantic-code-search-cli-with-mul]], [[forloopcodescontextplus-semantic-intelligence-for-large-scal]], [[hilashcabinet-ai-first-knowledge-base-and-startup-os]]. ^theme-repos-semantic-search
- **Token optimization & cost** — LLM efficiency and throughput: [[rtk-airtk-cli-proxy-that-reduces-llm-token-consumption-by-60]], [[superlinked-the-vector-computer]]. ^theme-repos-cost-perf
- **Research automation** — Autonomous research and benchmarking pipelines: [[karpathyautoresearch-ai-agents-running-research-on-single-gp]], [[jhochenbaumpi-autoresearch-studio-dashboard-plan-editor-pr-w]], [[orchestra-researchai-research-skills-comprehensive-open-sour]], [[sakanaaitreequest-a-tree-search-library-with-flexible-api-fo]], [[alexzhang13rlm-general-plug-and-play-inference-library-for-r]] (Recursive Language Models inference lib). ^theme-repos-research
- **Creative & experiment tooling** — Open media studios and local-first ML ops: [[jamiepinevoicebox-the-open-source-voice-synthesis-studio]] (voice-synthesis studio), [[gradio-apptrackio-a-lightweight-local-first-and-experiment-t]] (HuggingFace local-first experiment tracker). ^theme-repos-creative
- **Curriculum & learning paths** — Build-it-yourself pedagogy for the agentic era: [[rohitg00ai-engineering-from-scratch-learn-it-build-it-ship-i]] (4.3k-star end-to-end curriculum). ^theme-repos-curriculum
- **Minimal single-binary backends** — Embedded realtime infra eliminating microservice overhead: [[pocketbasepocketbase-open-source-realtime-backend-in-1-file]]. ^theme-repos-minimal-backends

**Notable items:**

- [[anthropicsclaude-code-claude-code-is-an-agentic-coding-tool]] — Claude Code itself; the agentic coding tool that anchors this entire ecosystem.
- [[microsoftautogen-a-programming-framework-for-agentic-ai]] — Microsoft's battle-tested multi-agent programming framework.
- [[run-llamallama_index-llamaindex-is-the-leading-framework-for]] — Dominant data-indexing framework for agentic retrieval.
- [[quivrhqquivr-opiniated-rag-for-integrating-genai-in-your-app]] — Production-grade opinionated RAG framework.
- [[agent-fieldagentfield-framework-for-ai-backend-build-and-run]] — Production control plane: cryptographic identity, audit trails, multi-SDK.
- [[agno-agiagno-full-stack-framework-for-building-multi-agent-s]] — Full-stack multi-agent framework with memory and reasoning built in.
- [[aider-aiaider-aider-is-ai-pair-programming-in-your-terminal]] — Mature terminal-based pair programmer; works with Claude and GPT.
- [[browser-usebrowser-use-make-websites-accessible-for-ai-agent]] — Browser automation making web apps directly accessible to agents.
- [[pocketbasepocketbase-open-source-realtime-backend-in-1-file]] — Realtime DB, auth, files, admin in a single Go binary.
- [[rtk-airtk-cli-proxy-that-reduces-llm-token-consumption-by-60]] — Transparent token-cost reduction via compression/caching (Robert's own tool).
- [[khoj-aikhoj-your-ai-second-brain-self-hostable-get-answers-f]] — Self-hostable AI second-brain with semantic retrieval.
- [[alirezarezvaniclaude-skills-180-production-ready-skills-plug]] — 180-skill Claude Code skill pack; reference for the ecosystem.
- [[dennisonbertramlgrep-local-semantic-code-search-cli-with-mul]] — Lightweight semantic code-search CLI using embeddings.
- [[stablyaiorca-orca-is-the-next-gen-ide-for-building-with-codi]] — IDE designed ground-up for AI-native development.
- [[karpathyautoresearch-ai-agents-running-research-on-single-gp]] — Karpathy's autoresearch: agents doing research on a single GPU.
- [[keygraphhqshannon-fully-autonomous-ai-hacker-to-find-actual]] — Autonomous vulnerability-research agent with real findings.
- [[ag-ui-protocolag-ui-ag-ui-the-agent-user-interaction-protoco]] — Standardized protocol for agent ↔ user interaction.
- [[djayatillakestudybible-mcp-bible-study-mcp-server-with-greek]] — Bible-study MCP server with Greek/Hebrew support; Robert-adjacent niche.
- [[jeffallanclaude-skills-66-specialized-skills-for-full-stack]] — 66-skill full-stack pack; largest curated skill library behind alirezarezvani's 180-skill reference.
- [[rohitg00skillkit-supercharge-ai-coding-agents-with-portable]] — The translation layer for the skill-pack economy; same skill runs across Claude Code, Codex, Cursor, Copilot, 40+ tools.
- [[meodaiskillcolor-expert-agent-skill-for-color-science-expert]] — Exemplar single-domain skill: 113 references covering color spaces, APCA/WCAG accessibility, pigment mixing; proof specialist skills can be rigorous, not cosmetic.
- [[conorbronsdonavoid-ai-writing-skill-that-audits-and-rewrites]] — Skills as taste-enforcement: audits and rewrites AI-patterned prose, meta-counter to model-homogenization.
- [[lnikellloopndroll-keep-codex-running-forever]] — Canonical "always-on" pattern: agent that doesn't stop when you do.
- [[tschonleberbrainctl-a-cognitive-memory-system-for-ai-agents]] — Single-file SQLite cognitive memory + MCP; minimal-infra counterpart to retaindb and mempalace.
- [[browser-usebrowser-harness-self-healing-browser-harness-that]] — Self-healing browser harness; completes arbitrary tasks without breaking on DOM churn.
- [[rohitg00ai-engineering-from-scratch-learn-it-build-it-ship-i]] — 4.3k-star end-to-end curriculum; the shelf's flagship learning path for agent-era engineering.

**2026-04-23 addition (+2 repos):** Two small, thematically tight items. [[k-dense-aimimeo]] — "clone an expert's way of thinking into your coding agent." Point mimeo at a name (Feynman, Darwin, Curie, Turing…) and it reads the internet on your behalf: pulls canonical sources, YouTube transcripts, articles/PDFs; distills each with a frontier model via OpenRouter (default Gemini 3.1 Pro); clusters recurring ideas; emits a production-ready `SKILL.md` or `AGENTS.md`. This is the **auto-authoring** move for the skill-pack economy — one step up the meta-ladder from [[alirezarezvaniclaude-skills-180-production-ready-skills-plug]] and [[jeffallanclaude-skills-66-specialized-skills-for-full-stack]]. Pairs directly with [[corpus2skill-dont-retrieve-navigate]] (academic side) and [[externalization-in-llm-agents-a-unified-review-of-memory-ski]] as the "if skills are externalized cognition, mimeo is the factory." [[ton-anywheremy-favorite-prompts-open-source-prompts]] — small open-source prompt library; extends `^theme-repos-claude-ecosystem` on the hand-curated end of the spectrum (contrast with mimeo's generated approach and alirezarezvani's 180-skill scale).

**2026-04-22 addition (+35 repos):** The largest single-session addition yet. Sharpens five existing themes and opens two new sub-clusters:

- **Paper ↔ reference-impl pairing surfaces directly** — [[lsdefinegenericagent-self-evolving-agent-grows-skill-tree-fr]] is the first-party reference implementation of the [[2604-17091v1]] paper already anchored in Academic & Reference. The repo description — _grows a skill tree from a 3.3k-line seed, full system control with 6× less token consumption_ — is the paper's architecture made executable. Same author, same thesis: skill externalization compounds across sessions. Similarly [[lambda-calculus-llmlambda-rlm-method-for-long-context-rlms-u]] extends [[alexzhang13rlm-general-plug-and-play-inference-library-for-r]] into verifiable lambda-calculus territory, tightening the RLM (Recursive Language Model) cluster.
- **Agent-ergonomic CLI primitives — a new `^theme-repos-agent-ergonomics` sub-cluster.** Kun Chen's five-repo drop ([[kunchenguidaxi-design-principles-for-agent-ergonomics-higher]], [[kunchenguidchrome-devtools-axi-the-most-agent-ergonomic-brow]], [[kunchenguidgsh-a-battery-included-posix-compatible-generativ]], [[kunchenguidno-mistakes-git-push-no-mistakes]], [[kunchenguidtreehouse-manage-worktrees-without-managing-workt]]) articulates a coherent design thesis: rebuild CLI primitives (shell, browser devtools, git push, worktrees) around _agent_ ergonomics — higher accuracy at lower token cost than MCP or raw CLI. This is the first time in the library that a single contributor has published a full agent-tool suite organized around explicit design principles (axi is the README; the others are exemplars). Sibling trajectory to Claude Code's SDK but for the Codex/GPT lineage.
- **GEPA as a standalone cluster** — [[gepa-aigepa-optimize-prompts-code-and-more-with-ai-powered-r]] is the canonical GEPA repo (Reflective Text Evolution for prompt/code optimization), with [[twaldinhone-cli-text-optimizer-built-on-gepa-uses-agentic-co]] as a downstream user — GEPA-powered CLI text optimizer that uses agentic coding CLIs themselves as mutator + observer, eliminating API-key dependency. Together with the new [[dspy-compiling-declarative-language-model-calls-into]] paper and existing [[intertwinedspy-agent-skills-dspy-31x-agent-skills-validated]], GEPA anchors the declarative-LLM-calls lineage on the repo side. Adds a `^theme-repos-prompt-optimization` cluster.
- **Skill-pack economy extends into standalone plugin format** — [[vercel-labsskills-the-open-agent-skills-tool-npx-skills]] (Vercel's `npx skills` — skills as npm-style packages), [[addyosmaniagent-skills-production-grade-engineering-skills-f]] (Addy Osmani production skills), [[therealseandonahoeagents-md-drop-in-agentsmd-that-makes-ever]] (drop-in AGENTS.md), [[alchaincyfhuashu-design-huashu-design-html-native-design-ski]] (Claude Code HTML-native design), [[dennisonbertramclaude-mac-guardian-macos-health-security-and]] (macOS health plugin), [[ehmocode-overhaul-skill-opinionated-interactive-health-audit]] (codebase audit skill), [[chezmoi-dotfilesdot_claudeskillsempirical-prompt-tuningskill]] (mizchi's empirical prompt-tuning skill in dotfiles), [[michaelschadecodex-goodies]] (codex configs), [[codejunkie99agentic-stack-one-brain-many-harnesses-portable]] (portable `.agent/` folder across harnesses), [[cortexkitopencode-magic-context-opencode-plugin-for-magic-co]] (OpenCode plugin for magic context / cross-session memory). The distribution format is stabilizing — npm/drop-in AGENTS.md/portable-folder are starting to look like the three viable shapes. The `^theme-repos-skill-packs-generalist` and `^theme-repos-claude-ecosystem` themes now span curated libraries, single-domain specialists, translation layers, _and_ standalone distributable plugins.
- **Claude Design as a first-party design surface** — [[rohitg00awesome-claude-design-claude-design-designmd-prompts]] catalogs DESIGN.md prompts, remix recipes, skills, and video teardowns for Claude Design, giving the X/Twitter Claude Design cluster ([[viktoroddy-claude-design-is-insane-just-recorded-a-18-min-tut]], [[nateherk-been-getting-some-crazy-good-video-outputs-lately]], [[liu8in-this-is-insane-in-a-good-way-now-claudeais-got-des]]) a repo-level artifact to point at. Cross-references Design & UI.
- **Always-on / overnight runtime cluster grows** — [[dicklesworthstoneagentic_coding_flywheel_setup-bootstraps-a]] (30-minute Ubuntu VPS bootstrap to multi-agent AI dev env), [[marcusquinnaidevops-vibe-coding-is-easy-devops-is-hard-openc]] (OpenCode + Git agent automation for apps + business + personal), [[yeachan-heooh-my-codex-omx-oh-my-codex-your-codex-is-not-alo]] (OmX: Codex plugin with hooks/HUDs/agent teams — already indexed), [[q00ouroboros]] (Robert's own self-referential loop framework). Extends `^theme-repos-always-on` with the VPS-bootstrap tier that eliminates the last manual setup step.
- **Agent-native task queue** — [[barnum-circusbarnum-task-queue-orchestrator-for-ai-agents]] fills a real gap: a task queue _designed for_ agents rather than retrofitted from Celery/Sidekiq. Joins `^theme-repos-agent-frameworks`.
- **Swarm / multi-agent** — [[unclebobswarm-forge]] (Uncle Bob's swarm repo) and [[tinyhumansaiopenhuman-your-personal-ai-super-intelligence-pr]] (private personal superintelligence) extend multi-agent coordination and self-hosted agent stacks.
- **New adjacency: `^theme-repos-security`** — [[gitleaksgitleaks-find-secrets-with-gitleaks]] (secrets scanner). First explicit security tooling in the shelf beyond `keygraphhqshannon` (vuln-finding agent); pairs with the new [[crabtrap-secure-agents-in-production]] essay in AI Tools & News as the operational + tooling halves of the same emerging concern.
- **New adjacency: data extraction from agent environments** — [[0xseroai-data-extraction-extract-all-your-personal-data-hist]] pulls user data/history out of Cursor, Codex, Claude Code, Windsurf, and Trae. Frames the agent-IDE as a data source worth querying, not just a UI.
- **Document intelligence without vectors** — [[vectorlessflowvectorless-reasoning-native-document-intellige]] is the "reasoning-native, no-embeddings" counter-position to the RAG/vector cluster — aligned in spirit with [[corpus2skill-dont-retrieve-navigate]]'s "navigate, don't retrieve" thesis.
- **ML-engineer-as-agent** — [[huggingfaceml-intern-ml-intern-an-open-source-ml-engineer-th]] (HuggingFace's open-source ML engineer that reads papers, trains, ships) joins `^theme-repos-research` as the production-ML sibling of `karpathy/autoresearch`.
- **Decision-support agent** — [[harshilmathurautodecision-a-decision-operating-system-for-hi]] — a decision OS that simulates disagreement and stress-tests high-stakes choices. New angle on agents: deliberation as a primitive, not just task execution.
- **Pipeline glue** — [[timf34arxiv2md-convert-arxiv-papers-to-markdown]] is the same class of tool as Robert's `.tools/process_pdfs.py` + `.tools/hybrid_arxiv_marker.py`, worth referencing when iterating on the process-pdfs skill.
- **Thematic outlier worth noting** — [[tw93kami-good-content-deserves-good-paper]] (tw93's Kami — "good content deserves good paper") is the stationery/print-mindset crossover with the agentic-tooling ecosystem; pairs with Stationery & Journals.
- **pi extension** — [[shpetimapi-fff-a-helpful-pi-extension-to-improve-file-search]] extends the pi coding-agent family ([[robzolkoslazypi-pi-coding-agent-setup-for-the-lazy]], [[edxethpi-subagents]]) with fff-integrated file search, matching Robert's own use of fff.

**Cross-references:**

- Heavy overlap with `ai-tools-news/` (same agentic ecosystem from a news-and-product angle rather than repo angle) and with `dev-tools-cli/` (Claude Code tooling, terminal-first agents).
- Obsidian-skills repos connect to `stationery-journals/` PKM cluster (Zettelkasten, commonplace, digital-analog hybrid workflows).
- Skill-pack themes link to AI Tools & News' Claude Code SDK & skills cluster (product framing of the same ecosystem).
- Single-domain skill specialists (color, taste, anti-slop prose) connect to Writing & Content and Design & UI as craft enforcement primitives.
- Autonomous-research items cross-reference `academic-reference/` ([[bilevel-autoresearch-meta-autoresearching-itself]], [[2604-17091v1]]) and `knowledge/autoresearch/` project state. GenericAgent's repo ([[lsdefinegenericagent-self-evolving-agent-grows-skill-tree-fr]]) is the 2604-17091v1 paper's reference implementation — direct paper ↔ code pairing.
- Bible-study MCP server connects to Theology & Faith's Bible-software theme.
- GEPA cluster ([[gepa-aigepa-optimize-prompts-code-and-more-with-ai-powered-r]], [[twaldinhone-cli-text-optimizer-built-on-gepa-uses-agentic-co]]) pairs with `academic-reference/` DSPy paper ([[dspy-compiling-declarative-language-model-calls-into]]) as the declarative-LLM-calls lineage on repo + paper sides.
- Corpus2Skill paper ([[corpus2skill-dont-retrieve-navigate]]) primary-sources the skill-pack economy; [[vectorlessflowvectorless-reasoning-native-document-intellige]] is its repo-side cousin.
- Kun Chen's agent-ergonomics suite (`kunchenguid/*`) anchors a new repo-level design-principles cluster; cross-references Dev Tools & CLI on terminal-first craft and AI Tools & News on the Claude Code / Codex ergonomics debate.

### AI Tools & News

> [!abstract] Collection overview
> 490 items — the largest shelf in the library, a working archive of the agentic-AI news/product/essay cycle. Recurring through every slice: agent frameworks, harnesses-as-a-service (HaaS), Claude Code SDK and skill ecosystems, agent-as-backend platforms, RAG/memory as table-stakes infrastructure, and the "dark factory" pattern where humans specify intent and agents autonomously iterate. Developer environments are being reconfigured around agents (Warp, Tembo, sidecar IDEs), not retrofitted. Differentiation has moved from base models to orchestration, skills, and distribution. A newer signal in the April 2026 cohort: the education and hosted-tool surface is maturing — OpenAI Academy publishes formal Codex tutorials, TED hosts breakthrough-agent origin stories, and AI-first knowledge bases (Cabinet, DeepWiki) ship as productized alternatives to raw RAG infra.

**Key themes:**

- **Agent frameworks & orchestration** — Harnesses, multi-agent systems, and workflow engines: [[agent-zero]], [[agentso-the-original-ai-agents-platform]], [[oh-my-openagent-the-best-agent-harness]], [[openfang-the-agent-operating-system]], [[intent-the-developer-workspace-for-agent-orchestration]], [[the-harness-is-the-product-3niac]], [[agent-flywheel-ai-agents-coding-for-you]] (hosted agentic-coding flywheel). ^theme-tools-agent-frameworks
- **Claude Code SDK & skills** — The ecosystem anchoring Robert's daily work: [[claude-code-a-highly-agentic-coding-assistant-deeplearningai]], [[the-claude-code-sdk-and-the-birth-of-haas-harness-as-a-servi]], [[the-magic-of-claude-code]], [[the-agent-skills-directory]], [[axiom-claude-code-agents-for-ios-development]], [[highlights-from-the-claude-4-system-prompt]], [[unslopify-workflwow-for-repoprompt]] (RepoPrompt workflow guide). ^theme-tools-claude-ecosystem
- **Agent-as-backend & infrastructure** — Agents treated as first-class services: [[agentuity-the-agent-native-cloud-platform-for-ai-agents]], [[insforge-give-agents-everything-they-need-to-ship-fullstack]], [[instantdb-the-best-backend-for-ai-coded-apps]], [[inngest-ai-and-backend-workflows-orchestrated-at-any-scale]], [[build-ai-agents-that-run-in-production]]. ^theme-tools-agent-backend
- **Agentic coding platforms** — Agent-native development environments: [[opencode-the-open-source-ai-coding-agent]], [[plandex-open-source-ai-coding-agent-for-large-tasks]], [[qoder-the-agentic-coding-platform]], [[predev-self-driving-agentic-engineering]], [[warp-the-agentic-development-environment]], [[tembo-coding-agents-that-work-where-you-do]], [[you-might-never-open-your-editor-again-sidecar]]. ^theme-tools-agentic-coding
- **The dark-factory pattern** — Full-autonomy essays and flywheel analysis: [[the-dark-factory-pattern-moving-from-ai-assisted-to-fully-au]], [[the-folder-is-the-agent]], [[the-agentic-coding-flywheel-tldr]], [[building-a-fully-agentic-engineer-and-growing-it-to-500k-arr]], [[how-i-created-openclaw-the-breakthrough-ai-agent]] (TED talk on OpenClaw origin — solo-builder → agent-team narrative). ^theme-tools-dark-factory
- **RAG, memory, knowledge graphs** — Persistent context and retrieval infrastructure: [[retaindb-persistent-memory-for-ai-agents-sota-on-longmemeval]], [[building-a-knowledge-graph-with-llamacloud-neo4j-llamaindex]], [[gemini-file-search-cloudflare-workers-the-production-rag-sta]], [[neo4j-llm-knowledge-graph-builder-extract-nodes-and-relation]], [[implementing-advanced-retrieval-rag-strategies-with-neo4j]], [[the-developers-guide-to-graphrag-for-accurate-contextual-gen]]. ^theme-tools-rag-memory
- **AI-first knowledge bases** — Productized alternatives to raw RAG: [[cabinet-free-open-source-ai-first-knowledge-base]] (open-source AI-first KB; complements the repo-level [[hilashcabinet-ai-first-knowledge-base-and-startup-os]]), [[deepwiki-ai-documentation-you-can-talk-to-for-every-repo]] (conversational AI documentation layer over GitHub repos). ^theme-tools-knowledge-bases
- **Recursive / meta-reasoning models** — Emerging pattern of models that recursively invoke themselves: [[rlm-dspy]] (DSPy's Recursive Language Models module — RLM moving from research curiosity into mainstream frameworks). ^theme-tools-recursive-models
- **Education & tutorials** — Formal learning layer maturing beyond blog posts: [[introduction20to20codex]] (OpenAI Academy's official Codex intro), [[index-1088468798]] (Simon Willison's "Building with LLMs" PyCon 2025 tutorial). ^theme-tools-education
- **Browser & web automation** — Agents interacting with real web apps: [[browser-use-the-ai-browser-agent]], [[browseros-open-source-ai-browser-privacy-first-alternative-t]], [[apify-full-stack-web-scraping-and-data-extraction-platform]], [[firecrawl]]. ^theme-tools-browser-automation
- **Prompt engineering & context craft** — Tooling and essays on context mastery: [[promptlayer-the-cleanest-way-to-prompt-engineer-platform-for]], [[promptmetheus-prompt-engineering-ide]], [[16x-prompt-ai-coding-with-advanced-context-management]], [[the-claude-ai-cheat-code-list-from-think-harder-to-xml-magic]], [[how-to-write-a-great-agentsmd-lessons-from-over-2500-reposit]], [[how-to-build-reliable-ai-workflows-with-agentic-primitives-a]]. ^theme-tools-prompt-engineering
- **Workforce & GTM agents** — Business-process automation via agents: [[relevance-ai-build-your-ai-workforce-ai-for-business]], [[polsia-ai-that-runs-your-company]], [[salesco-ai-first-cold-email-platform-for-b2b-teams]], [[postiz-the-all-in-one-agentic-social-media-scheduling-tool]]. ^theme-tools-workforce-agents
- **Multimodal: video, design, UX** — Agentic creative tooling: [[descript-edit-videos-podcasts-like-a-doc-ai-video-editor]], [[calesthioopenmontage-worlds-first-open-source-agentic-video]], [[ux-pilot-superfast-ux-design-with-ai]], [[gamma-best-ai-presentation-maker-website-builder]], [[guiddemagically-create-video-documentation-with-ai]]. ^theme-tools-multimodal

**Notable items:**

- [[claude-code-a-highly-agentic-coding-assistant-deeplearningai]] — DeepLearning.AI's analysis of what makes Claude Code agentic.
- [[the-claude-code-sdk-and-the-birth-of-haas-harness-as-a-servi]] — HaaS (Harness as a Service) framing for Claude Code's product layer.
- [[the-dark-factory-pattern-moving-from-ai-assisted-to-fully-au]] — Maps the progression: manual → assisted → fully autonomous development.
- [[building-effective-ai-agents-anthropic]] — Anthropic's canonical guide on building effective agents.
- [[building-a-fully-agentic-engineer-and-growing-it-to-500k-arr]] — Case study: autonomous engineering agent scaled to $500k ARR.
- [[warp-the-agentic-development-environment]] — Next-generation terminal built for agent coordination.
- [[retaindb-persistent-memory-for-ai-agents-sota-on-longmemeval]] — SOTA on LongMemEval; memory infra for long-running agents.
- [[how-to-write-a-great-agentsmd-lessons-from-over-2500-reposit]] — AGENTS.md best practices from a 2,500-repo survey.
- [[browser-use-the-ai-browser-agent]] — Browser automation as a first-class primitive for agents.
- [[opencode-the-open-source-ai-coding-agent]] — Open-source Claude Code competitor; full agentic workflow under permissive license.
- [[composio-access-250-apps-in-just-one-line-of-code]] — Integration layer connecting agents to 250+ enterprise tools.
- [[hermes-agent-documentation-hermes-agent]] — Nous Research's reasoning-focused agent architecture.
- [[tinfoil-verifiably-private-ai-powered-by-secure-enclaves]] — Privacy-first AI execution via secure enclaves.
- [[gitagent-your-repository-becomes-your-agent]] — Repository-as-agent-state paradigm for development workflows.
- [[how-to-build-reliable-ai-workflows-with-agentic-primitives-a]] — Foundational design patterns for reliable agentic workflows.
- [[zero-to-builder-from-i-cant-code-to-shipping-apps-in-60-days]] — Accelerated skill acquisition via agent leverage.
- [[the-agent-skills-directory]] — Reusable-capabilities framework for agent composition.
- [[xcodebuildmcp-ai-powered-xcode-automation]] — iOS development specifics for agentic workflows (connects to `ios-swift/`).
- [[cabinet-free-open-source-ai-first-knowledge-base]] — Open-source AI-first knowledge base; product layer on top of the RAG/memory infrastructure this shelf documents.
- [[deepwiki-ai-documentation-you-can-talk-to-for-every-repo]] — Conversational AI documentation over any GitHub repo; collapses docs-browsing into chat.
- [[how-i-created-openclaw-the-breakthrough-ai-agent]] — Peter Steinberger TED talk; canonical founder-origin story for the solo-builder → agent-team transition.
- [[introduction20to20codex]] — OpenAI Academy's formal Codex intro; signals education layer maturing beyond ad-hoc blog posts.
- [[rlm-dspy]] — DSPy's Recursive Language Models module; RLM pattern entering mainstream frameworks.

**2026-04-23 addition (+3 items):** [[a-complete-guide-to-agentsmd]] (aihero.dev deep-dive on AGENTS.md conventions — joins [[how-to-write-a-great-agentsmd-lessons-from-over-2500-reposit]] and [[therealseandonahoeagents-md-drop-in-agentsmd-that-makes-ever]] as the third AGENTS.md anchor; the genre now has a canonical beginner guide, a 2,500-repo survey, and a drop-in repo). [[hermes-atlas-the-community-map-for-hermes-agent]] is the community hub for Nous Research's Hermes Agent — 93 repos across 12 categories, 6 curated lists — the ecosystem-level view complementing [[hermes-agent-documentation-hermes-agent]] and [[hermes-agent-the-complete-beginners-guide-apr-2026]]; all three Hermes items now form a product→docs→community triangle. [[qwen36-how-to-run-locally-unsloth-documentation]] is Unsloth's official Qwen3.6 local-run guide (Unsloth-Dynamic-2 quants, Unsloth-Studio instructions) — continues the local-inference thread alongside [[recursive-language-models]] and the Ollama-centric items in `ai-repos-open-source/`.

**2026-04-22 addition (+23 items):** The re-sync clusters cleanly into four moves:

- **Agent memory / knowledge infra as productized surface** — [[agentmemory]] (agent-memory.dev product page) and [[brainctl-persistent-memory-for-ai-agents]] (brainctl.org landing page for [[tschonleberbrainctl-a-cognitive-memory-system-for-ai-agents]]) join [[retaindb-persistent-memory-for-ai-agents-sota-on-longmemeval]] and [[cabinet-free-open-source-ai-first-knowledge-base]] as the products-layer of `^theme-tools-rag-memory`. Memory infrastructure has stabilized enough to have marketing sites, not just repos.
- **Agent platforms + frameworks, continued proliferation** — [[hyperagent]], [[hermes-agent-the-complete-beginners-guide-apr-2026]] (tutorial layer around Nous Research's Hermes), [[herdr-tmux-for-agents]] (tmux-as-harness), [[nia-agentic-search-for-external-and-internal-data]] (agentic search across internal + external data — still unhydrated, SPA). Each extends `^theme-tools-agent-frameworks` but none individually reshapes the space; the signal is _quantity_ — the agent-platform market is saturating without clear winners yet.
- **Essays sharpen the meta-commentary** — four essays worth reading as a set: [[fuck-you-show-me-the-prompt]] (Hamel Husain's canonical piece on why opaque LLM frameworks fail — prompt transparency as a non-negotiable), [[crabtrap-secure-agents-in-production]] (Brex on operationalizing agent security — pairs with the new [[gitleaksgitleaks-find-secrets-with-gitleaks]] repo), [[what-if-you-dont-need-mcp-at-all]] (Mario Zechner's counter-position to MCP — frames the protocol as overfitted ceremony), [[why-i-built-dspy-agent-skills]] (justification essay for `intertwine/dspy-agent-skills` — DSPy + skills as the same abstraction from two sides). Plus [[ai-harness-engineering-compatibility-matrix]] (Cody Lindley) — a working compatibility matrix across harnesses, the first attempt in the library at a cross-vendor comparison artifact. Together they signal: the ecosystem is mature enough for _principled disagreement_, not just product announcements.
- **Models, formats, infra** — [[kimi-k26-tech-blog-advancing-open-source-coding]] (Kimi K2.6 release note; open-source Chinese coding model advancing), [[recursive-language-models]] (Alex Zhang's blog post on RLMs — pairs with [[rlm-dspy]] and [[alexzhang13rlm-general-plug-and-play-inference-library-for-r]] as the third RLM reference), [[toon]] (TOON format — token-efficient data representation; `^theme-repos-cost-perf` adjacency on the tools side), [[environments-hub-a-community-hub-to-scale-rl-to-open-agi]] (Prime Intellect's community RL environments hub — the "gym for open AGI" pitch), [[vllm-recipes]] (vLLM's official recipes book, serving docs). Infra and formats getting documented enough to teach from.
- **Grab-bag** — [[claude-design]], [[agentsearch-by-nozomio-labs-browse-any-docs-using-bash]], [[nia-agentic-search-for-external-and-internal-data]] are the three SPA-blocked stragglers; frontmatter + URL preserved for future manual hydration. [[rawworks]] and [[savings-kill-dumb-subscriptions-with-alive]] are lighter saves (creative-tooling studio, subscription-killer utility) — included for completeness, probably don't carry their weight.

**Cross-references:**

- Heavy overlap with AI Repos & Open Source (same ecosystem viewed from news/product angle vs repo angle); many items are news coverage of repos documented there.
- Claude Code ecosystem items connect to Dev Tools & CLI (terminal-first agents, Claude Code configs).
- Workforce-agents theme overlaps with Marketing & Business (agents for sales, outreach, content).
- iOS-specific agent tools connect to iOS & Swift.
- AI-first knowledge-base items (Cabinet, DeepWiki) cross-reference the semantic-search cluster in AI Repos & Open Source and the RAG/memory theme here — same capability staged as product vs primitive.
- Recursive Language Models (RLM) link to [[alexzhang13rlm-general-plug-and-play-inference-library-for-r]] in AI Repos & Open Source (research-infra counterpart to the DSPy docs) and to [[lambda-calculus-llmlambda-rlm-method-for-long-context-rlms-u]] (lambda-calculus extension).
- Education-layer items pair with curriculum repos (`rohitg00/ai-engineering-from-scratch`) as matched formal/informal learning paths.
- Security essays ([[crabtrap-secure-agents-in-production]]) + security repos ([[gitleaksgitleaks-find-secrets-with-gitleaks]]) form the beginnings of a cross-shelf `security` adjacency; also connects to the X/Twitter 2026-04-20 cybersec cluster.
- Memory-product pages ([[agentmemory]], [[brainctl-persistent-memory-for-ai-agents]]) cross-reference [[externalization-in-llm-agents-a-unified-review-of-memory-ski]] in `academic-reference/` as the survey that frames what these products instantiate.
