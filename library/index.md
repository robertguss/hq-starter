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

**Cross-references:**

- Planning-rhythm items overlap with Stationery & Journals (Franklin Planner appears in both shelves from different angles).

### Unsorted

> [!abstract] Collection overview
> A catch-all that still clusters tightly: developer platforms, AI tools, and production infrastructure for teams shipping at scale. Background orchestration, mobile dev tooling, AI-driven video/docs, and design-for-builders tooling dominate. Once re-sorted, most items would find homes in `dev-tools-cli/`, `ai-tools-news/`, or `ios-swift/`.

**Key themes:**

- **Background tasks & orchestration** — Durable queues and workflow engines: [[hatchet-devhatchet-run-background-tasks-at-scale]], [[hatchet-the-orchestration-engine-for-teams-who-ship]]. ^theme-async-ops
- **Mobile & Swift tooling** — Platforms for iOS teams: [[tuisttuist-a-virtual-platform-team-for-mobile-devs-who-ship]], [[twostrawsswiftagents-an-agentsmd-file-for-swift-and-swiftui]]. ^theme-mobile-dev
- **AI video & content automation** — HTML-to-video and screen-to-docs: [[heygen-comhyperframes-write-html-render-video-built-for-agen]], [[trupeer-ai-powered-product-videos-documentation-in-minutes]], [[prompt-guide-hyperframes]]. ^theme-ai-video
- **Builder infrastructure** — CI/Mac and plugin integration: [[macstadium-enterprise-mac-solutions-orka-devops-mac-vdi]], [[openaiplugins-openai-plugins]]. ^theme-infra

**Notable items:**

- [[heygen-comhyperframes-write-html-render-video-built-for-agen]] — Agent-first video rendering; write HTML, CLI renders.
- [[cathrynlaverydiagram-design-thirteen-editorial-diagram-types]] — 13 publication-quality diagram types shipped as a Claude Code skill.
- [[tuisttuist-a-virtual-platform-team-for-mobile-devs-who-ship]] — Virtual platform for Swift iOS teams; caching, testing, insights.
- [[hatchet-devhatchet-run-background-tasks-at-scale]] — Durable Postgres-backed task queue with observability.
- [[trupeer-ai-powered-product-videos-documentation-in-minutes]] — Screen recording to studio video + auto-generated docs.
- [[every-claude-code-concept-explained-for-normal-people]] — Educational primer on Claude Code fundamentals.

**Cross-references:**

- Most items are temporarily-homed — candidates for rehoming to `dev-tools-cli/` (Hatchet, MacStadium, diagram skills), `ios-swift/` (Tuist, Swift agents), or `ai-tools-news/` (HyperFrames, Trupeer, plugins).

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
- **AI-first dev tooling** — LLM-aware CLIs and agent scaffolding: [[introducing-vt-the-val-town-cli]], [[one-cookiecutter-to-build-agents-in-seconds]], [[openagents-orgopenagents-openagents-ai-agent-networks-for-op]]. ^theme-ai-first
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

**Cross-references:**

- Indie-publishing tactics overlap with Writing & Content (Substack, KDP) and with Productivity on execution rhythms.
