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

## Imported collections

Status: **Raindrop + X/Twitter imports complete** — 2026-04-17. 1,498 items across 19 folders, all `hydrated: false`.

### From Raindrop (1,269 items, 18 folders)

| Collection             | Folder                  | Items     |
| ---------------------- | ----------------------- | --------- |
| AI Tools & News        | `ai-tools-news/`        | 482       |
| AI Repos & Open Source | `ai-repos-open-source/` | 318       |
| Marketing & Business   | `marketing-business/`   | 100       |
| Dev Tools & CLI        | `dev-tools-cli/`        | 69        |
| Stationery & Journals  | `stationery-journals/`  | 56        |
| Theology & Faith       | `theology-faith/`       | 50        |
| Personal & Misc        | `personal-misc/`        | 41        |
| Web Dev                | `web-dev/`              | 40        |
| Academic & Reference   | `academic-reference/`   | 30        |
| Design & UI            | `design-ui/`            | 18        |
| Writing & Content      | `writing-content/`      | 15        |
| Productivity           | `productivity/`         | 14        |
| Unsorted               | `unsorted/`             | 13        |
| Cooking                | `cooking/`              | 10        |
| Books & Reading        | `books-reading/`        | 5         |
| iOS & Swift            | `ios-swift/`            | 4         |
| Recipes                | `recipes/`              | 3         |
| Photography            | `photography/`          | 1         |
| **Raindrop total**     |                         | **1,269** |

### From X/Twitter bookmarks (229 items, 1 folder)

Synced via [fieldtheory](https://fieldtheory.dev/cli) (local cache at `~/.ft-bookmarks/bookmarks.jsonl`). Re-sync with `fieldtheory sync --yes` then re-run `python .tools/x_import.py` — importer is idempotent on `tweet_id`.

| Collection  | Folder         | Items   |
| ----------- | -------------- | ------- |
| X/Twitter   | `x-bookmarks/` | 229     |
| **X total** |                | **229** |

## Synthesis

<!-- Compiled wiki entries go here — one section per concept/theme, written after items are reviewed/hydrated. Seeded with Theology & Faith 2026-04-18; remaining collections pending. -->

### Theology & Faith

Robert's theology-faith collection reflects a Reformed Presbyterian sensibility: he curates primary sources from the patristic and Reformation traditions alongside practical Bible software tools, scholarly resources on biblical exegesis and Greek, and working communities like L'Abri. The collection shows an integration of craft (liturgy, spiritual disciplines, theological writing) with serious scholarship — favoring primary texts, rigorous methodology, and traditions that take doctrine seriously.

**Key themes:**

- **Bible software & digital exegesis** — A comprehensive toolkit spanning free and premium software ([[bible-search-and-study-tools-blue-letter-bible]], [[e-sword-free-bible-study-for-the-pc]], [[the-crosswire-bible-society-free-bible-software-bringing-the]]) alongside Greek language resources ([[new-testament-greek-guy-randy-leedy]], [[home-free-greek-forever]]) for inductive study and linguistic precision.
- **Reformed & Puritan theology** — Deep engagement with Calvin, Edwards, and Puritan thought through commentaries ([[calvins-commentaries-monergism]]), resources ([[reformed-theology-at-a-puritans-mind-search-the-scriptures-j]], [[puritan-search]]), and epistemology ([[van-til-reformed-epistemologypdf]]), with supporting communities like Monergism.
- **Patristic & early Christian sources** — Primary texts and scholarly editions of the Church Fathers ([[amazoncom-origen-on-first-principles-readers-edition-oxford]], [[home-christian-classics-ethereal-library]]), grounding theological thinking in apostolic and post-apostolic tradition.
- **Liturgy & worship renewal** — Resources recovering historical Reformed and liturgical practice ([[reformation-worship-book-liturgies-from-the-past-for-the-pre]]) alongside denominational witness ([[the-orthodox-presbyterian-church-presbytery-of-philadelphia]]), bridging scholarship and lived worship.
- **Biblical scholarship & exegesis** — Methodological resources for serious study ([[inductive-bible-study-a-step-by-step-guide-bible-study-tips]], [[international-standard-bible-encyclopedia-introduction-and-m]]) and institutional affiliation ([[society-of-biblical-literature]]) supporting sustained theological interpretation.
- **Theological community & formation** — Centers for intellectual work and spiritual hospitality ([[southborough-labri]], [[home-shepherds-theological-seminary-development]], [[great-commission-publications]]) where thought meets lived discipleship.

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
