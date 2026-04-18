---
tags:
  - library
title: "Impeccable: Design skills for AI harnesses"
url: "https://impeccable.style/"
company: [personal]
topics: []
created: 2026-04-07
source_type: raindrop
raindrop_id: 1675824834
source_domain: "impeccable.style"
source_type_raindrop: link
collection: "AI Repos & Open Source"
collection_id: 69284315
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

1 skill, 20 commands, and curated anti-patterns for impeccable frontend design.

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: Impeccable: Design skills for AI harnesses

URL Source: https://impeccable.style/

Markdown Content:
Before commands, before detection, Impeccable teaches your AI real design. Deep reference knowledge across 7 dimensions, loaded every time your AI writes code.

Scale, rhythm, hierarchy, expression

Accessibility, systems, theming

Layout, spacing, composition

Fluid layouts, touch targets

States, feedback, affordances

Micro-interactions, transitions

Clarity, voice, error messages

Run `/impeccable teach` once to set your project's design context. Every command benefits.

18 commands form a shared vocabulary between you and your AI. Each one encodes a specific design discipline, so you can steer with precision.

Create

Evaluate

Refine

Simplify

Harden

System

Create

### /impeccable

Create distinctive, production-grade frontend interfaces with high design quality. Generates creative, polished code that avoids generic AI aesthetics. Use when the user asks to build web components, pages, artifacts, posters, or applications, or when any design skill requires project context. Call with 'craft' for shape-then-build, 'teach' for design context setup, or 'extract' to pull reusable components and tokens into the design system.

Create: Freeform design with full design intelligence

Create

### /shape

Plan the UX and UI for a feature before writing code. Runs a structured discovery interview, then produces a design brief that guides implementation. Use during the planning phase to establish design direction, constraints, and strategy before any code is written.

Create: Plan UX and UI through structured discovery

Evaluate

### /critique

Evaluate design from a UX perspective, assessing visual hierarchy, information architecture, emotional resonance, cognitive load, and overall quality with quantitative scoring, persona-based testing, automated anti-pattern detection, and actionable feedback. Use when the user asks to review, critique, evaluate, or give feedback on a design or component.

→leads to/polish/distill/bolder/quieter/typeset/layout

Evaluate

### /audit

Run technical quality checks across accessibility, performance, theming, responsive design, and anti-patterns. Generates a scored report with P0-P3 severity ratings and actionable plan. Use when the user wants an accessibility check, performance audit, or technical quality review.

→leads to/harden/optimize/adapt/clarify

Refine

### /typeset

Improves typography by fixing font choices, hierarchy, sizing, weight, and readability so text feels intentional. Use when the user mentions fonts, type, readability, text hierarchy, sizing looks off, or wants more polished, intentional typography.

+combines with/bolder/polish

Refine

### /colorize

Add strategic color to features that are too monochromatic or lack visual interest, making interfaces more engaging and expressive. Use when the user mentions the design looking gray, dull, lacking warmth, needing more color, or wanting a more vibrant or expressive palette.

+combines with/bolder/delight

Refine

### /animate

Review a feature and enhance it with purposeful animations, micro-interactions, and motion effects that improve usability and delight. Use when the user mentions adding animation, transitions, micro-interactions, motion design, hover effects, or making the UI feel more alive.

+combines with/delight

Refine

### /delight

Add moments of joy, personality, and unexpected touches that make interfaces memorable and enjoyable to use. Elevates functional to delightful. Use when the user asks to add polish, personality, animations, micro-interactions, delight, or make an interface feel fun or memorable.

+combines with/bolder/animate

Refine

### /bolder

Amplify safe or boring designs to make them more visually interesting and stimulating. Increases impact while maintaining usability. Use when the user says the design looks bland, generic, too safe, lacks personality, or wants more visual impact and character.

↔pairs with/quieter

Refine

### /quieter

Tones down visually aggressive or overstimulating designs, reducing intensity while preserving quality. Use when the user mentions too bold, too loud, overwhelming, aggressive, garish, or wants a calmer, more refined aesthetic.

↔pairs with/bolder

Refine

### /overdrive BETA

Pushes interfaces past conventional limits with technically ambitious implementations — shaders, spring physics, scroll-driven reveals, 60fps animations. Use when the user wants to wow, impress, go all-out, or make something that feels extraordinary.

+combines with/animate/delight

Refine

### /layout

Improve layout, spacing, and visual rhythm. Fixes monotonous grids, inconsistent spacing, and weak visual hierarchy. Use when the user mentions layout feeling off, spacing issues, visual hierarchy, crowded UI, alignment problems, or wanting better composition.

+combines with/distill/adapt

Simplify

### /distill

Strip designs to their essence by removing unnecessary complexity. Great design is simple, powerful, and clean. Use when the user asks to simplify, declutter, reduce noise, remove elements, or make a UI cleaner and more focused.

+combines with/quieter/polish

Simplify

### /clarify

Improve unclear UX copy, error messages, microcopy, labels, and instructions to make interfaces easier to understand. Use when the user mentions confusing text, unclear labels, bad error messages, hard-to-follow instructions, or wanting better UX writing.

+combines with/polish/adapt

Processing Status

Your request is being processed. Please wait while we complete the operation. This may take some time depending on various factors.

⚠️ Warning

Proceeding with this action may result in irreversible consequences to your data and settings configuration.

Saving changes...

About 10 seconds remaining

Delete this project?

This will permanently delete 23 files. You can't undo this.

Confusing copy → Clear, actionable language

Simplify

### /adapt

Adapt designs to work across different screen sizes, devices, contexts, or platforms. Implements breakpoints, fluid layouts, and touch targets. Use when the user mentions responsive design, mobile layouts, breakpoints, viewport adaptation, or cross-device compatibility.

+combines with/polish/clarify

Harden

### /polish

Performs a final quality pass fixing alignment, spacing, consistency, and micro-detail issues before shipping. Use when the user mentions polish, finishing touches, pre-launch review, something looks off, or wants to go from good to great.

Harden: Final pass and design system alignment

Harden

### /optimize

Diagnoses and fixes UI performance across loading speed, rendering, animations, images, and bundle size. Use when the user mentions slow, laggy, janky, performance, bundle size, load time, or wants a faster, smoother experience.

Harden: Performance improvements

Harden

### /harden

Make interfaces production-ready: error handling, empty states, onboarding flows, i18n, text overflow, and edge case management. Use when the user asks to harden, make production-ready, handle edge cases, add error states, design empty states, improve onboarding, or fix overflow and i18n issues.

+combines with/optimize

Every AI model learned from the same templates. Without intervention, they all produce the same predictable mistakes. Impeccable names them, detects them, and teaches the AI to avoid them.

*   use overused fonts like Inter, Roboto, Arial, Open Sans, or system defaults — but also do not simply switch to your second-favorite. Every font in the reflex_fonts_to_reject list above is banned. Look further.
*   use monospace typography as lazy shorthand for "technical/developer" vibes.
*   put large icons with rounded corners above every heading. They rarely add value and make sites look templated.
*   use only one font family for the entire page. Pair a distinctive display font with a refined body font.
*   use a flat type hierarchy where sizes are too close together. Aim for at least a 1.25 ratio between steps.
*   set long body passages in uppercase. Reserve all-caps for short labels and headings.

*   THIS BEFORE TYPING ANY FONT NAME.
*   use a modular type scale with fluid sizing (clamp) on headings.
*   vary font weights and sizes to create clear visual hierarchy.
*   vary your font choices across projects. If you used a serif display font on the last project, look for a sans, monospace, or display face on this one.

*   use gray text on colored backgrounds; it looks washed out. Use a shade of the background color instead.
*   use pure black (#000) or pure white (#fff). Always tint; pure black/white never appears in nature.
*   use the AI color palette: cyan-on-dark, purple-to-blue gradients, neon accents on dark backgrounds.
*   use gradient text for impact — see <absolute_bans> below for the strict definition. Solid colors only for text.
*   default to dark mode with glowing accents. It looks "cool" without requiring actual design decisions.
*   default to light mode "to be safe" either. The point is to choose, not to retreat to a safe option.

*   use modern CSS color functions (oklch, color-mix, light-dark) for perceptually uniform, maintainable palettes.
*   tint your neutrals toward your brand hue. Even a subtle hint creates subconscious cohesion.

*   wrap everything in cards. Not everything needs a container.
*   nest cards inside cards. Visual noise; flatten the hierarchy.
*   use identical card grids (same-sized cards with icon + heading + text, repeated endlessly).
*   use the hero metric layout template (big number, small label, supporting stats, gradient accent).
*   center everything. Left-aligned text with asymmetric layouts feels more designed.
*   use the same spacing everywhere. Without rhythm, layouts feel monotonous.
*   let body text wrap beyond ~80 characters per line. Add a max-width like 65–75ch so the eye can track easily.

*   create visual rhythm through varied spacing: tight groupings, generous separations.
*   use fluid spacing with clamp() that breathes on larger screens.
*   use asymmetry and unexpected compositions; break the grid intentionally for emphasis.

*   Use border-left or border-right greater than 1px as a colored accent stripe on cards, list items, callouts, or alerts. See <absolute_bans> above for the strict CSS pattern.
*   Use glassmorphism everywhere (blur effects, glass cards, glow borders used decoratively rather than purposefully).
*   Use sparklines as decoration. Tiny charts that look sophisticated but convey nothing meaningful.
*   Use rounded rectangles with generic drop shadows. Safe, forgettable, could be any AI output.
*   Use modals unless there's truly no better alternative. Modals are lazy.

*   Use intentional, purposeful decorative elements that reinforce brand.

*   Animate layout properties (width, height, padding, margin). Use transform and opacity only
*   Use bounce or elastic easing. They feel dated and tacky; real objects decelerate smoothly

*   Use motion to convey state changes: entrances, exits, feedback
*   Use exponential easing (ease-out-quart/quint/expo) for natural deceleration
*   For height animations, use grid-template-rows transitions instead of animating height directly

*   Repeat the same information (redundant headers, intros that restate the heading)
*   Make every button primary. Use ghost buttons, text links, secondary styles; hierarchy matters

*   Use progressive disclosure. Start simple, reveal sophistication through interaction (basic options first, advanced behind expandable sections; hover states that reveal secondary actions)
*   Design empty states that teach the interface, not just say "nothing here"
*   Make every interactive surface feel intentional and responsive

*   Hide critical functionality on mobile. Adapt the interface, don't amputate it

*   Use container queries (@container) for component-level responsiveness
*   Adapt the interface for different contexts, not just shrink it

*   Repeat information users can already see

*   Make every word earn its place

See design issues highlighted directly on the page. No screenshots, no guesswork. Impeccable’s overlay shows you exactly what’s wrong and where.

25 deterministic checks

No LLM needed. Pattern matching catches purple gradients, overused fonts, nested cards, low contrast, and more.

Three ways to use it

The **Chrome extension** on any site, embedded in `/critique` during an AI design review, or standalone via `npx impeccable live`.

[![Image 1: Impeccable Chrome extension panel listing detected anti-patterns](https://impeccable.style/assets/extension-detection-nt7x8aj5.png) Available now Chrome extension Install from Chrome Web Store →](https://chromewebstore.google.com/detail/impeccable/bdkgmiklpdmaojlpflclinlofgjfpabf)

### 1 Install the skills Recommended

18 commands that steer your AI toward better design, in real time. The full Impeccable experience.

$`npx skills add pbakaus/impeccable`

Works with Cursor, Claude Code, Gemini CLI, Codex CLI, and more.

Then run `/impeccable teach` to set up your project's design context.

Other install methods

Claude Code plugin

$`/plugin marketplace add pbakaus/impeccable`

Then open `/plugin` in Claude Code

Manual download all 11 providers

### 2 Add the CLI Beta

Scan any file, directory, or live URL for anti-patterns from the terminal. Catches gradient text, AI color palettes, nested cards, low contrast, and 20+ more rules across HTML, CSS, JSX/TSX, Vue, and Svelte. Use it in CI pipelines, pre-commit hooks, or one-off audits to keep AI slop out of production.

$`npm i -g impeccable`

Or use `npx impeccable detect src/` directly without installing.

[Full command reference on npm →](https://www.npmjs.com/package/impeccable)

### 3 Browser extension

Click the toolbar icon on any page and every anti-pattern lights up right where it lives: gradient text, purple palettes, nested cards, tiny body text, and the rest. Works on your localhost, staging, production, or anyone else's site. Great for spot-checking competitors, reviewing PRs visually, or just browsing the web with a sharper eye.

[Install from Chrome Web Store →](https://chromewebstore.google.com/detail/impeccable/bdkgmiklpdmaojlpflclinlofgjfpabf)

### 4 Stay updated

Keep skills current and follow along with new commands, anti-patterns, and the design thinking behind Impeccable.

$`npx impeccable skills update`

Run periodically to pull the latest skill definitions.

[Follow on X@impeccable_ai](https://x.com/impeccable_ai)

*   **Streamlined from 21 to 18 commands.** Removed overlap and confusion: `/arrange` renamed to `/layout`, `/normalize` merged into `/polish` (design system alignment is now part of the final pass), `/onboard` merged into `/harden` (empty states and first-run experiences are part of production readiness), and `/extract` became `/impeccable extract` (a sub-mode alongside craft and teach). Every remaining command has a clearly distinct job.
*   **Automatic cleanup of deprecated skills.** On first load after updating, the skill detects and removes leftover files from renamed or merged commands. No manual cleanup needed.

*   **Renamed `frontend-design` to `impeccable`.** The core skill now shares its name with the project, and the teach subcommand moved from `/teach-impeccable` to `/impeccable teach`. One skill, one namespace.
*   **Data-driven skill rewrite.** The core skill was rebuilt against an internal eval framework that runs the same brief through frontier models with and without the skill loaded, then measures how much the output collapses into monoculture. The result: dramatically more font and color diversity, sharper overall design quality, and much stronger Codex support. The biggest unlock was an anti-attractor procedure that forces the model to enumerate and reject its reflex defaults before picking. Validated on gpt-5.4 and Qwen 3.6 Plus across 15 niches.
*   **Anti-pattern detection engine.** 25 deterministic rules across typography, color, layout, motion, and quality. Handles oklch, oklab, lch, and lab color formats, CSS variables inside border shorthands, gradient-backed text, and emoji-only nodes.
*   **CLI: `npx impeccable detect`.** Scans HTML, CSS, JSX/TSX, Vue, Svelte, and CSS-in-JS. Framework detection, multi-file import tracking, Puppeteer-backed live URL scanning, CI-ready JSON output, and a `--fast` regex mode for huge codebases.
*   **Chrome DevTools extension.** One-click detection on any page: yours, staging, production, or someone else's. Reads live computed styles, surfaces findings in an interactive panel, and highlights elements on the page. In Chrome Web Store review.
*   **`/critique` got teeth.** Persona sub-agents review in parallel, score against Nielsen's heuristics, run the detector automatically, and open a live browser overlay so you can walk each finding in place.
*   **New ways to create with Impeccable.**`/shape` runs a structured discovery interview about purpose, audience, and goals, then produces a design brief before any code is written. `/impeccable craft` chains that brief straight into the full implementation flow so you ship a designed feature instead of a reflex card grid.
*   **New docs site.** Top-level [Docs](https://impeccable.style/skills), [Anti-Patterns](https://impeccable.style/anti-patterns), and [Visual Mode](https://impeccable.style/visual-mode) sections. 18 per-skill pages with before/after demos and the canonical SKILL.md inline, two [tutorials](https://impeccable.style/tutorials), and 38 rule cards with inline visual examples.
*   **New harness: Rovo Dev.** 11 supported AI tools total.

View older releases

*   New provider: **Trae** (China + International)
*   `/critique` now scores against Nielsen's 10 heuristics, tests with persona archetypes, and assesses cognitive load
*   `/audit` now scores 5 dimensions with P0-P3 severity ratings and structured action plans
*   Improved skill descriptions for better agent auto-discovery
*   Fixed invalid YAML frontmatter that broke GitHub preview and Codex loading ([#67](https://github.com/pbakaus/impeccable/issues/67))
*   Codex CLI now uses correct `$` prefix for command references

*   `/typeset` now recommends fixed type scales for app UIs, reserving fluid typography for marketing/content pages

*   3 new skills: `/typeset` (fix typography), `/arrange` (fix layout & spacing), `/overdrive` (technically extraordinary effects, beta)
*   Skills now auto-gather design context via `.impeccable.md`. Run `/teach-impeccable` once, all skills benefit
*   Deep linking to commands (`#cmd-overdrive`, etc.)

*   Added OpenCode provider support
*   Added Pi provider support
*   Recategorized `/onboard` as an enhancement command

*   Added Kiro support (`.kiro/skills/`)
*   Restored prefix toggle: download `i-` prefixed bundles to avoid naming conflicts
*   Audit and critique skills only suggest real, installed commands

*   Unified skills architecture: commands are now skills with `user-invocable: true`
*   Added VS Code Copilot and Google Antigravity support (`.agents/skills/`)
*   New install flow: `npx skills add` as primary, universal ZIP as fallback
*   Added universal ZIP containing all 5 provider directories
*   Renamed `/simplify` to `/distill` to avoid Claude Code conflict

*   Initial release with enhanced frontend-design skill
*   17 design commands: /polish, /audit, /distill, /bolder, and more
*   Support for Cursor, Claude Code, Gemini CLI, and Codex CLI
*   Interactive command cheatsheet

Where do I put the downloaded files?

The easiest way is `npx skills add pbakaus/impeccable`, which auto-detects your AI harness and places files correctly.

If you downloaded the **universal ZIP**, extract it to your **project root** (same level as your `package.json` or `src/` folder). It creates hidden folders for each supported tool: `.cursor/`, `.claude/`, `.gemini/`, `.codex/`, and `.agents/`.

Project-level installation takes precedence and lets you version control your skills.

How do I update to the latest version?

Run `npx impeccable skills update` from your project root. It downloads the latest skills, cleans up deprecated files, and preserves any prefix you use.

*   **Alternative:**`npx skills add pbakaus/impeccable` re-installs from scratch.
*   **Claude Code plugin:** Open `/plugin`, go to the Discover tab.
*   **Manual ZIP:** Download from above and extract to the project root.

Your `.impeccable.md` context file is never overwritten.

Commands or skills aren't appearing. What do I do?

**For commands:** Type `/` in your AI harness and look for commands like `/audit`, `/polish`, etc. If they don't appear, double-check the files are in the correct location.

**For skills:** Skills are applied automatically when relevant. To verify, explicitly mention "use the impeccable skill" in your prompt. This forces the AI to acknowledge and apply it.

**Tool-specific setup:**

*   **Cursor:** Requires Nightly channel + Agent Skills enabled in Settings → Rules
*   **Gemini CLI:** Requires `@google/gemini-cli@preview` + Skills enabled via `/settings`

I'm new to AI harnesses. Where do I start?

Skills and commands are intermediate features. If you're just getting started, learn the basics first:

*   **Claude Code:**[Official Documentation](https://docs.anthropic.com/en/docs/claude-code)
*   **Cursor:**[Cursor Docs](https://docs.cursor.com/)
*   **Gemini CLI:**[Gemini CLI Docs](https://geminicli.com/docs/)
*   **Codex CLI:**[Codex GitHub](https://github.com/openai/codex)

Once you're comfortable with basic prompting and code generation, come back and give Impeccable a try.

Is Impeccable free?
Yes. Everything is **Apache 2.0**: skills, commands, CLI, and the detection engine. Fully open source, free for everyone.

## Work with me

Impeccable is built by [Renaissance Geek](https://renaissance-geek.ai/). I work with enterprise teams on large-scale rollouts, custom integrations, and training for designers and developers. If you're a frontier lab, design tool company, or enterprise looking to raise the bar on AI-generated design, let's talk.

[Get in touch](mailto:paul@renaissance-geek.ai)
