---
tags:
  - library
title: "Vibe Coding Manual : r/ChatGPTCoding"
url: "https://www.reddit.com/r/ChatGPTCoding/comments/1j5l4xw/vibe_coding_manual/"
company: [personal]
topics: []
created: 2025-05-27
source_type: raindrop
raindrop_id: 1103817094
source_domain: "reddit.com"
source_type_raindrop: link
collection: "AI Tools & News"
collection_id: 69284314
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: hn-reddit-api
---
## Raw Content

<!-- Hydrated 2026-04-18 via hn-reddit-api -->

**Vibe Coding Manual**

**r/ChatGPTCoding**  |  **u/Low_Target2606**  |  **Score:** 349  |  **Comments:** 102



# Vibe Coding Manual: A Template for AI-Assisted Development  
**(Version 1.0 – March 2025)**  

---

## Introduction: The Core Concept of Vibe Coding with AI  

### What is Vibe Coding and What Does It Stand On?  
Vibe coding is a collaborative approach to software development where humans guide AI models (e.g., Claude 3.7, Cursor) to build functional projects efficiently. Introduced by Matthew Berman in his "Vibe Coding Tutorial and Best Practices" (YouTube, 2025), it rests on three pillars:  
1. **Specification:** You define the goal (e.g., "Build a Twitter clone with login").  
2. **Rules:** You set explicit constraints (e.g., "Use Python, avoid complexity").  
3. **Oversight:** You monitor and steer the process to ensure alignment.  

This manual builds on Berman’s foundation, integrating community insights from YouTube comments (e.g., u/nufh, u/robistocco) and Reddit threads (e.g., u/illusionst, u/DonkeyBonked), creating a comprehensive framework for developers of all levels.

### Why Is This Framework Useful?  
AI models are powerful but prone to chaos—over-engineering, scope creep, or losing context. This manual addresses these issues:  
- **Tames Chaos:** Enforces strict adherence to your rules, minimizing runaway behavior.  
- **Saves Time:** Structured steps and summaries reduce rework.  
- **Enables Clarity:** Non-technical users can follow along; programmers gain precision.  

### Key Benefits  
1. **Clarity:** Rules are modular, making them easy to navigate and adjust.  
2. **Control:** You dictate the pace and scope of AI actions.  
3. **Scalability:** Works for small scripts (e.g., a calculator) or large apps (e.g., a web platform).  
4. **Maintainability:** Documentation and tracking ensure long-term project viability.  

---

## Manual Structure: How It’s Organized  
The framework consists of four files in a `.cursor/rules` directory (or equivalent, e.g., Windsurf), each with a distinct purpose:  
1. **Coding Preferences** – Defines code style and quality standards.  
2. **Technical Stack** – Specifies tools and technologies.  
3. **Workflow Preferences** – Governs the AI’s process and execution.  
4. **Communication Preferences** – Sets expectations for AI-human interaction.  

We’ll start with basics for accessibility, then dive into advanced details for technical depth.

---

## Core Rules: A Simple Starting Point  

### 1. Coding Preferences – "Write Code Like This"  
**Purpose:** Ensures clean, maintainable, and efficient code.  
**Rules:**  
- **Simplicity:** "Always prioritize the simplest solution over complexity." *(Matthew Berman)*  
- **No Duplication:** "Avoid repeating code; reuse existing functionality when possible." *(Matthew Berman, DRY from u/DonkeyBonked)*  
- **Organization:** "Keep files concise, under 200-300 lines; refactor as needed." *(Matthew Berman)*  
- **Documentation:** "After major components, write a brief summary in `/docs/[component].md` (e.g., `login.md`)." *(u/believablybad)*  

**Why It Works:** Simple code reduces bugs; documentation provides a readable audit trail.

### 2. Technical Stack – "Use These Tools"  
**Purpose:** Locks the AI to your preferred technologies.  
**Rules (Berman’s Example):**  
- "Backend in Python."  
- "Frontend in HTML and JavaScript."  
- "Store data in SQL databases, never JSON files."  
- "Write tests in Python."  

**Why It Works:** Consistency prevents AI from switching tools mid-project.

### 3. Workflow Preferences – "Work This Way"  
**Purpose:** Controls the AI’s execution process for predictability.  
- **Focus:** "Modify only the code I specify; leave everything else untouched." *(Matthew Berman)*  
- **Steps:** "Break large tasks into stages; pause after each for my approval." *(u/xmontc)*  
- **Planning:** "Before big changes, write a `plan.md` and await my confirmation." *(u/RKKMotorsports)*  
- **Tracking:** "Log completed work in `progress.md` and next steps in `TODO.txt`." *(u/illusionst, u/petrhlavacek)*  

**Why It Works:** Incremental steps and logs keep the process transparent and manageable.

### 4. Communication Preferences – "Talk to Me Like This"  
**Purpose:** Ensures clear, actionable feedback from the AI.  
- **Summaries:** "After each component, summarize what’s done." *(u/illusionst)*  
- **Change Scale:** "Classify changes as Small, Medium, or Large." *(u/illusionst)*  
- **Clarification:** "If my request is unclear, ask me before proceeding." *(u/illusionst)*  

**Why It Works:** You stay informed without needing to decipher AI intent.

---

## Advanced Rules: Scaling Up for Complex Projects  

### 1. Coding Preferences – Enhancing Quality  
**Extensions:**  
- **Principles:** "Follow SOLID principles (e.g., single responsibility, dependency inversion) where applicable." *(u/Yodukay, u/philip_laureano)*  
- **Guardrails:** "Never use mock data in dev or prod—restrict it to tests." *(Matthew Berman)*  
- **Context Check:** "Begin every response with a random emoji (e.g., 🐙) to confirm context retention." *(u/evia89)*  
- **Efficiency:** "Optimize outputs to minimize token usage without sacrificing clarity." *(u/Puzzleheaded-Age-660)*  

**Technical Insight:** SOLID ensures modularity (e.g., a login module doesn’t handle tweets); emoji signal when context exceeds model limits (typically 200k tokens for Claude 3.7).  
**Credits:** Matthew Berman (base), u/DonkeyBonked (DRY), u/philip_laureano (SOLID), u/evia89 (emoji), u/Puzzleheaded-Age-660 (tokens).

### 2. Technical Stack – Customization  
**Extensions:**  
- "If I specify additional tools (e.g., Elasticsearch for search), include them here." *(Matthew Berman)*  
- "Never alter the stack without my explicit approval." *(Matthew Berman)*  

**Technical Insight:** A fixed stack prevents AI from introducing incompatible dependencies (e.g., switching SQL to JSON).  
**Credits:** Matthew Berman (original stack).

### 3. Workflow Preferences – Process Mastery  
**Extensions:**  
- **Testing:** "Include comprehensive tests for major features; suggest edge case tests (e.g., invalid inputs)." *(u/illusionst)*  
- **Context Management:** "If context exceeds 100k tokens, summarize into `context-summary.md` and restart the session." *(u/Minimum_Art_2263, u/orbit99za)*  
- **Adaptability:** "Adjust checkpoint frequency based on my feedback (more/less granularity)." *(u/illusionst)*  

**Technical Insight:** Token limits (e.g., Claude’s 200k) degrade performance beyond 100k; summaries maintain continuity. Tests catch regressions early.  
**Credits:** Matthew Berman (focus), u/xmontc (steps), u/RKKMotorsports (planning), u/illusionst (summaries, tests), u/Minimum_Art_2263 (context).

### 4. Communication Preferences – Precision Interaction  
**Extensions:**  
- **Planning:** "For Large changes, provide an implementation plan and wait for approval." *(u/illusionst)*  
- **Tracking:** "Always state what’s completed and what’s pending." *(u/illusionst)*  
- **Emotional Cues:** "If I indicate urgency (e.g., ‘This is critical—don’t mess up!’), prioritize care and precision." *(u/dhamaniasad, u/capecoderrr)*  

**Technical Insight:** Change classification (S/M/L) quantifies impact (e.g., Small = &lt;50 lines, Large = architecture shift); emotional cues may leverage training data patterns for better compliance.  
**Credits:** u/illusionst (summaries, classification), u/dhamaniasad (emotional prompts).

---

## Practical Example: How It Works  
**Task:** "Build a note-taking app with save functionality."  

1. **Specification:** You say, "I want an app to write and save notes."  
2. **AI Response:**  
   - "🦋 Understood. Plan: 1. Backend (Python, SQL storage), 2. Frontend (HTML/JS), 3. Save function. Proceed?"  
   - You: "Yes."  
3. **Execution:**  
   - After backend: "🐳 Backend done (Medium change). Notes saved in SQL. Updated `progress.md` and `TODO.txt`. Next: frontend?"  
   - After frontend: "🌟 Frontend complete. Added `docs/notes.md` with usage. Done!"  
4. **Outcome:** A working app with logs (`progress.md`, `/docs`) for reference.  

**Technical Note:** Each step is testable (e.g., SQL insert works), and context is preserved via summaries.

---

## Advanced Tips: Maximizing the Framework  

### Why Four Files?  
- **Modularity:** Each file isolates a concern—style, tools, process, communication—for easy updates. *(Matthew Berman)*  
- **Scalability:** Adjust one file without disrupting others (e.g., tweak communication without touching stack). *(u/illusionst)*  

### Customization Options  
- **Beginners:** Skip advanced rules (e.g., SOLID) for simplicity.  
- **Teams:** Add `team-collaboration.mdc`: "Align with team conventions in `team-standards.md`; summarize for peers." *(u/deleatanda5910)*  
- **Large Projects:** Increase checkpoints and documentation frequency.  

### Emotional Prompting  
- Try: "This project is critical—please focus!" Anecdotal evidence suggests improved attention, possibly from training data biases. *(u/capecoderrr, u/dhamaniasad)*  

---

## Credits and Acknowledgments  
This framework owes its existence to the following contributors:
 
   - **Andrej Karpathy:** Coined the term "vibe coding" and introduced it to the broader community in a post on X (February 3, 2025, https://x.com/karpathy/status/1886192184808149383), describing AI-assisted programming with a focus on intuitive, minimal-effort workflows. His work inspired the foundational concept of this framework. 
   - **Matthew Berman:** Core vibe coding rules and philosophy (YouTube, 2025).  
- **YouTube Community:**  
  - u/nufh, u/believablybad (documentation, .md files).  
  - u/robistocco (iterative workflow).  
  - u/xmontc (checkpoints).  
- **Reddit Community:**  
  - u/illusionst (communication, progress tracking).  
  - u/Puzzleheaded-Age-660 (token optimization).  
  - u/DonkeyBonked, u/philip_laureano (KISS, DRY, YAGNI, SOLID).  
  - u/evia89 (emoji context check).  
  - u/dhamaniasad, u/capecoderrr (emotional prompting).  
- **Grok (xAI):** Synthesized this manual, integrating all insights into a cohesive framework at the request of u/Low_Target2606  

---

## Conclusion: Your Guide to Vibe Coding  
This manual is a battle-tested template for harnessing AI in development. It balances simplicity, control, and scalability, making it ideal for solo coders, teams, or even non-technical creators. Use it as-is, tweak it to your needs, and share your results—I’d love to see how it evolves! Post your feedback on Reddit and let’s refine it together. Happy coding!  

---



## Top comments



**u/Slow_Release_6144** (score 46):

> Too many words..killing my vibe



**u/eleqtriq** (score 15):

> This just looks like how senior devs guide junior devs 😂



**u/sethshoultes** (score 10):

> Can you please explain how this works?  
> \&gt; Start every response with a random emoji (e.g., 🐳, 🌟) to signal context retention



**u/duh-one** (score 8):

> I used to do this for years, but back in my day, it was called being an engineering manager



**u/majorleagueswagout17** (score 31):

> You do realize Vibe Coding was a joke right lol
