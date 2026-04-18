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
- **AI & data literacy** — Modern technical literacy grounded in the broader scholarly toolkit: [[foundations-of-generative-ai]], [[data-science-harvard-university]]. ^theme-ai-data

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

**Cross-references:**

- Classical primary sources overlap with Theology & Faith's patristic theme (Perseus and Christian Classics Ethereal Library both serve canonical-text scholarship).
- Life-of-the-mind items connect to Books & Reading below (Hamming, Hamerton, Waterfield work in the same intellectual-formation register).

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
