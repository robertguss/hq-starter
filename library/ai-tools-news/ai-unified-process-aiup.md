---
tags:
  - library
title: "AI Unified Process - AIUP"
url: "https://aiup.dev/"
company: [personal]
topics: []
created: 2025-11-06
source_type: raindrop
raindrop_id: 1423822785
source_domain: "aiup.dev"
source_type_raindrop: link
collection: "AI Tools & News"
collection_id: 69284314
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: AI Unified Process (AIUP)

URL Source: https://aiup.dev/

Markdown Content:
Agile & Iterative

Requirements- and Spec-driven Development

Agile, iterative, requirements- and spec-driven development powered by AI. Keep requirements at the center while AI handles the rest.

[Read the Complete Story](https://martinelli.ch/spec-driven-development-with-ai-a-new-approach-and-a-journey-into-the-past/)

### The Problem

Traditional development is code-centric. Requirements get outdated, documentation drifts, and when bugs appear, we dig through code to understand what the system was supposed to do.

**AI coding tools make this worse**by generating code faster without fixing the underlying process problems.

**The Determinism Myth:**Some believe AI code generation only works with extensive specifications that force deterministic output. This misses the point entirely.

### The Solution

AI Unified Process flips this around. Requirements stay at the center, and everything else gets generated from them using AI as the consistency engine.

**Iterative Improvement:**Through short iterations, specifications, code, and tests improve together. Documentation enables sustainable development and modernization.

**Test-Driven Consistency:**Tests ensure the system behaves the same regardless of code generation changes, enabling safe refactoring and evolution.

#### Inception

*   Business Requirements Catalog 
*   Initial stakeholder alignment 
*   Test strategy planning 
*   Quick iterations and feedback 

#### Elaboration

*   Business Use Case Diagrams 
*   Entity Models
*   System Use Case Diagrams with business validation 
*   Test case development

#### Construction

*   Detailed System Use Case Specifications 
*   AI-generated application code 
*   Unit testing, integration testing 
*   Developer review and iteration 

#### Transition

*   User acceptance testing 
*   Continuous delivery and stakeholder feedback integration 
*   Production optimization 
*   Continuous improvement 

![Image 1: Process](https://unifiedprocess.ai/process.svg)

Tap to view full size

*   **Requirements-Driven:**Specifications drive everything else, not code
*   **AI-Assisted:**AI handles tedious work, humans focus on business logic
*   **Iterative Improvement:**Specs, code, and tests evolve together through short cycles
*   **Test-Protected:**Comprehensive tests ensure consistent behavior during AI regeneration
*   **Stakeholder-Centric:**Continuous validation with business users
*   **Traceable:**Every line of code traces back to business requirements

### The Determinism Fallacy

Critics argue AI code generation only works with exhaustive specifications that force deterministic output. This assumes we need perfect requirements upfront.

**Reality:**Perfect specifications are impossible and unnecessary. The real value comes from iterative improvement.

### Our Iterative Approach

Through short cycles, specifications become clearer, AI generation improves, and tests get stronger. Each iteration builds on the previous one.

**Key insight:**Tests ensure consistent behavior regardless of how the AI generates code. This enables safe evolution and modernization.

### How Iterative Improvement Works

*   **Start Small:**Begin with basic requirements and generate initial code
*   **Test Everything:**Create comprehensive tests that capture expected behavior
*   **Refine Continuously:**Improve specs based on stakeholder feedback
*   **Regenerate Safely:**Tests protect against regression during AI code updates
*   **Document Reality:**Keep specifications aligned with what actually works

#### Better Business Alignment

Stakeholders review every artifact, ensuring the system matches actual needs

#### Sustainable Development

Living documentation enables refactoring and modernization without losing knowledge

#### Safe AI Evolution

Tests protect system behavior while AI improves code generation quality

#### Iterative Quality

Specifications, code, and tests improve together through continuous cycles

#### Complete Traceability

From business requirement to code line, every connection is maintained

### Requirements & Modeling

The aiup-core plugin provides slash commands that guide Claude through creating requirements catalogs, entity models, use case diagrams, and specifications — all stack-agnostic.

/requirements/entity-model/use-case-diagram/use-case-spec

### Implementation & Testing

The aiup-vaadin-jooq plugin adds technology-specific skills for database migrations, UI implementation with Vaadin, and automated testing with Karibu and Playwright.

/flyway-migration/implement/karibu-test/playwright-test
