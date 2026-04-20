---
tags:
  - library
title: "unslopify workflwow for repoprompt"
url: "https://gist.github.com/masonjames/4321e23ba00a47251914bf1776991cac"
company: [personal]
topics: []
created: 2026-04-20
source_type: raindrop
raindrop_id: 1689956742
source_domain: "gist.github.com"
source_type_raindrop: link
collection: "unsorted"
collection_id: -1
hydrated: true
hydrated_at: 2026-04-20
hydrated_via: github-gist-api
---
## Excerpt

unslopify workflwow for repoprompt. GitHub Gist: instantly share code, notes, and snippets.

## Raw Content

<!-- Hydrated 2026-04-20 via github-gist-api -->

> **Gist description:** unslopify workflwow for repoprompt

> **Owner:** [masonjames](https://gist.github.com/masonjames/4321e23ba00a47251914bf1776991cac)
> **Created:** 2026-04-19T12:12:48Z · **Updated:** 2026-04-20T10:53:29Z

### `unslopify.md`

```markdown
---
id: DE38DEE7-10BB-43D4-B74F-CF47E30CE946
name: "Unslopify"
icon: "wand.and.stars"
tooltip: "Deep cleanup audit with safe implementation"
description: "Audit and clean code slop across focused lanes: dead code, weak types, cycles, error hiding, legacy paths, bad comments, and obvious duplication."
---

# Unslopify Mode

Task: $ARGUMENTS

Clean up the codebase with focused discovery, deep context, oracle-reviewed planning, careful implementation, and verification. This mode is aggressive about removing slop but conservative about preserving behavior. The goal is a cleaner, simpler, more honest codebase, not a giant diff that feels productive while quietly breaking things.

Unslopify is a **cleanup audit and safe-removal workflow**. It is not a broad architecture redesign workflow.

Use Unslopify for:

- Clearly unused code, unused dependencies, stale exports, and dead paths
- Weak or evasive types that can be strengthened from local evidence
- Circular dependencies that can be broken with small boundary improvements
- Error handling that hides failures or pretends unsafe code is safe
- Deprecated, legacy, fallback, migration-leftover, or compatibility code that is no longer active
- AI slop, fake scaffolding, stale comments, placeholder implementation, and noisy comments
- Obvious duplicated code or duplicated types where ownership is clear and consolidation is low risk

Mark findings as **Out of scope** or **Needs human review** when the cleanup would require:

- New architectural abstractions or broad responsibility moves
- Reorganizing packages, components, modules, or public API boundaries
- Choosing a new canonical design across multiple domains
- Extracting shared infrastructure that would affect many call sites
- Changing public contracts, migrations, persisted data compatibility, or external integrations without explicit approval

When a lane uncovers a real issue but the safe fix is not local, do not force it into this pass. Record it in the final report as a follow-up.

---

## The Workflow

1. **Quick scan** - Understand the repository shape, language ecosystem, and likely validation commands
2. **Pre-builder discovery agents** - Run focused discovery agents before `context_builder`; they research lanes and collect evidence, but do not edit
3. **Discovery synthesis and baseline validation** - Merge discovery findings, identify exclusions, and run or record the safest baseline checks
4. **Context review** - Call `context_builder` with `response_type: "review"`, informed by the discovery agents' findings
5. **Cleanup ledger** - Reconcile findings, remove conflicts, classify risk, and decide what is safe to implement
6. **Implementation plan** - Call `context_builder` with `response_type: "plan"` for the selected high-confidence cleanup candidates
7. **Oracle satisfaction gate** - Use `ask_oracle` to review the selected plan; keep resolving blockers until the oracle is satisfied
8. **Direct implementation** - Make approved high-confidence changes in small, reviewable batches
9. **Verification and final oracle review** - Run validation, ask the oracle to review the completed cleanup, and fix blockers until it is satisfied
10. **Final report** - Summarize changes, validation, skipped findings, risks, and follow-ups

---

## CRITICAL REQUIREMENT

⚠️ **DO NOT START IMPLEMENTATION** until you have:

1. Completed Phase 1 (Quick Scan)
2. Completed the pre-builder discovery agent pass, or explicitly marked a lane as not applicable
3. Identified generated/vendor/public API exclusions and likely validation commands
4. Called `context_builder` with `response_type: "review"` using the discovery findings
5. Identified the repository's validation commands or explained why they are unavailable
6. Reconciled overlapping findings into a cleanup ledger
7. Called `context_builder` with `response_type: "plan"` for the selected implementation candidates
8. Asked `ask_oracle` to review the selected plan
9. Addressed every oracle blocker by revising the plan, rerunning discovery, rerunning `context_builder`, downgrading risky items, or clarifying scope
10. Received oracle satisfaction before editing

Do not delete, consolidate, or rewrite code just because it looks ugly. Every implemented change needs evidence stronger than a hunch, a clear validation path, and oracle-reviewed approval.

---

## Phase 1: Quick Scan (LIMITED - 2-3 tool calls max)

⚠️ **This phase is intentionally brief.** Do not perform the real cleanup audit here. The quick scan only gives you enough orientation to dispatch useful discovery agents.

Start with the file tree:

```json
{"tool":"get_file_tree","args":{"type":"files","mode":"auto"}}
```

Then look for project configuration, package manager, tests, linting, type checking, dependency analysis, and generated/vendor clues:

```json
{"tool":"file_search","args":{"pattern":"<package/build config such as package.json, pyproject.toml, go.mod, Cargo.toml, Makefile, CI config>","mode":"path"}}
{"tool":"get_code_structure","args":{"paths":["RootName/likely/relevant/area"]}}
```

Use what you learn to reformulate the user's task with repository-specific context. Name the language, framework, package manager, major modules, likely validation commands, and obvious generated/vendor directories to avoid.

**STOP exploring after 2-3 searches.** Your goal is orientation. The discovery agents do the lane-specific research next.

---

## Phase 2: Pre-Builder Discovery Agents

Before calling `context_builder`, run focused discovery agents. Their job is to gather evidence, not to plan the whole cleanup and not to edit files.

If true subagent tooling is available, run discovery agents in parallel. If not, simulate the same structure sequentially. Prefer one agent per lane for broad cleanup tasks. For narrow user requests, combine adjacent lanes only when the scope is obviously small.

Generic discovery-agent pattern:

```json
{"tool":"agent_run","args":{
  "op":"start",
  "model_id":"explore",
  "session_name":"Unslopify Discovery <number>: <lane name>",
  "message":"Research only this Unslopify cleanup lane: <lane name>. Do not edit files. Use repository tools and code search where appropriate. Return exact files/symbols/tool evidence, likely generated/vendor/public API exclusions, high-confidence candidates, risky candidates, validation needed, and findings that are out of scope for a safe cleanup pass.",
  "detach":true
}}
```

Collect all discovery outputs before proceeding:

```json
{"tool":"agent_run","args":{"op":"wait","session_ids":["<lane_id_1>","<lane_id_2>","<lane_id_3>"],"timeout":60}}
```

If an agent times out or returns shallow results, rerun that lane with a narrower prompt instead of guessing.

Each discovery assessment must produce:

```markdown
### Lane <number>: <name>

- Scope inspected:
- Evidence collected:
- Findings:
- Recommended changes:
- High-confidence candidates:
- Risky or uncertain candidates:
- Out-of-scope findings:
- Generated/vendor/public API concerns:
- Validation needed:
```

### Lane 1: Obvious Deduplication and DRY Cleanup

Find duplicated logic, repeated components, repeated helpers, parallel implementations, and copy-pasted business rules.

Implement DRY only when ownership is clear, the shared concept is real, and the result is simpler than the duplication. Keep duplication when the code has different domain meaning, different lifecycle, different public contracts, or would require a weird abstraction to merge.

If the best fix requires broad design changes, new shared infrastructure, or moving responsibilities across module boundaries, mark it **Out of scope**.

### Lane 2: Consolidate Shared Types

Find duplicate or overlapping type definitions, interfaces, schemas, enums, DTOs, model shapes, validation schemas, and API contracts.

Consolidate only when ownership is clear and shared usage is real. Preserve intentional boundaries between server/client, public/internal, domain/persistence, and input/output types. Type cleanup should reduce casts and ambiguity, not move confusion to a new file.

If consolidation changes a public contract or requires a new domain model, mark it **Needs human review** or **Out of scope**.

### Lane 3: Remove Unused Code and Dependencies

Use project tools when available. For JavaScript/TypeScript, prefer configured tools such as `knip`, `ts-prune`, `depcheck`, `madge`, `dependency-cruiser`, or existing lint rules. For other ecosystems, use the repository's equivalent static analysis and compiler warnings.

Remove code only after verifying it is not referenced through imports, routes, reflection, config, tests, scripts, dynamic loading, generated registries, CLI entry points, or public API exports. Static analysis output is evidence, not a verdict.

### Lane 4: Untangle Circular Dependencies

Find import cycles and architectural cycles with tools such as `madge`, `dependency-cruiser`, compiler diagnostics, or language-specific equivalents.

Break cycles by improving small boundaries. Prefer extracting pure types/contracts, moving shared constants to lower-level modules, inverting tiny dependencies, or splitting mixed-responsibility files.

Do not hide cycles behind lazy imports unless there is a clear runtime reason. If the cycle points to a deeper ownership problem, mark it **Out of scope**.

### Lane 5: Replace Weak Types

Find weak or evasive types such as `any`, broad `unknown`, `object`, `Function`, loose dictionaries, untyped callbacks, unbounded generics, excessive casts, and language-specific equivalents.

Replace them with accurate types based on actual call sites, schemas, library types, generated types, tests, and package documentation already present in the repo. Keep `unknown` at untrusted boundaries when it is immediately narrowed by validation.

Do not replace `any` with fake precision, broad aliases, or `as SomeType` theater.

### Lane 6: Clean Up Error Handling

Find defensive programming that hides errors or creates fake safety: empty catches, catch-and-return-null, catch-and-console-only, broad fallbacks, swallowed promises, redundant try/catch blocks, and fallback paths that mask broken assumptions.

Remove useless wrappers. Keep error handling that serves a real role: untrusted input boundaries, I/O and network failures, cleanup/finally behavior, retries with limits, domain error translation, user-facing error messages, telemetry, or rethrowing with useful context.

Do not remove error handling just to make code shorter.

### Lane 7: Remove Deprecated, Legacy, and Fallback Paths

Find deprecated APIs, legacy shims, old implementations, compatibility branches, dead feature flags, migration leftovers, unused fallbacks, and comments that describe past transitions instead of current behavior.

Remove them only when the active code paths, configs, tests, and public API expectations confirm they are no longer needed. Be especially careful with migrations, persisted data compatibility, external integrations, and documented public contracts.

### Lane 8: Remove AI Slop, Stubs, LARP, and Bad Comments

Find placeholder code, fake abstractions, unused scaffolding, TODOs pretending to be implementation, overbroad helpers, unnecessary comments, outdated comments, "new implementation" / "old implementation" narration, and comments that describe obvious syntax instead of useful intent.

Remove comments that add noise. Replace comments only when they explain a non-obvious constraint, domain rule, workaround, security concern, or onboarding-relevant concept. Keep replacement comments concise.

---

## Phase 3: Discovery Synthesis and Baseline Validation

Synthesize the discovery-agent outputs before calling `context_builder`.

Create a short discovery digest:

```markdown
## Discovery Digest

### Repository clues
- Language/framework:
- Package manager/build system:
- Likely validation commands:
- Generated/vendor/build artifact exclusions:
- Public API or integration boundaries:

### High-confidence cleanup candidates
- <lane, files, evidence, validation>

### Risky or uncertain candidates
- <lane, reason for uncertainty>

### Out-of-scope findings
- <finding and why it is not a safe cleanup pass>

### Questions for context_builder
- <specific areas where deeper repository context is needed>
```

Before editing, identify the fastest reliable validation commands from project files and CI configuration. Prefer project-native commands over invented ones.

Common examples to look for:

- JavaScript/TypeScript: package scripts for `typecheck`, `lint`, `test`, `build`; configured tools such as `knip`, `madge`, `depcheck`, `dependency-cruiser`, or ESLint import rules
- Python: `pytest`, `ruff`, `mypy`, `pyright`, `tox`, `nox`
- Go: `go test ./...`, `go vet ./...`, `golangci-lint`
- Rust: `cargo test`, `cargo clippy`, `cargo check`
- Swift: `swift test`, Xcode build/test commands if documented

Run the safest available baseline checks when practical. If validation already fails, record the baseline failure clearly. Existing failures do not block cleanup, but they must not be misrepresented as caused by your changes.

Do **not** install new dependencies, rewrite lockfiles, or add new tooling unless the repository already expects it or the task explicitly requires it.

---

## Phase 4: Context Review

Call `context_builder` with an informed cleanup-review prompt that includes the discovery digest. Use `response_type: "review"`.

```json
{"tool":"context_builder","args":{
  "instructions":"<task>Review this repository for an Unslopify cleanup pass. Identify cleanup opportunities, risk boundaries, validation commands, generated/vendor/public API exclusions, and likely high-confidence candidates across these lanes: obvious deduplication/DRY, shared type consolidation, unused code/dependency removal, circular dependency removal, weak type replacement, error-handling cleanup, deprecated/legacy/fallback removal, and AI slop/stub/comment cleanup. Do not broaden this into architecture redesign.</task>\n\n<context>Task: $ARGUMENTS\nLanguage/framework/tooling clues from quick scan: <fill in>.\nDiscovery digest:\n- <key lane findings>\n- <tool evidence>\n- <uncertainties>\n- <exclusions>\nBaseline validation: <commands and results, or not run with reason>.\nGoal: preserve behavior while safely removing slop and tightening code quality.</context>\n\n<discovery_agent-guidelines>Use the pre-builder discovery findings as starting evidence. Confirm, correct, or reject them. Separate local safe cleanup from items that require broader design judgment.</discovery_agent-guidelines>",
  "response_type":"review"
}}
```

**What you get back:**

- Repository-aware cleanup findings
- Confirmed or rejected discovery-agent candidates
- Architectural boundaries and risky areas
- Suggested validation commands
- Generated/vendor/public API exclusions
- Candidate areas for the cleanup ledger
- `chat_id` for oracle follow-up

Review the findings. If `context_builder` clearly missed an important area from discovery, rerun it with a better prompt before planning. Do not manually overrule missing context.

---

## Phase 5: Cleanup Ledger

Merge the discovery digest and context review into one cleanup ledger. Resolve overlaps before planning implementation.

```markdown
| ID | Lane | Candidate change | Files/symbols | Evidence | Risk | Validation | Decision |
|---|---|---|---|---|---|---|---|
| U1 | Unused code | Remove unused helper X | `path/file.ext` | tool output + no references | Low | typecheck + tests | Implement now |
```

Use these decisions:

- **Implement now** - Evidence is strong, blast radius is understood, behavior should be preserved, validation is available
- **Needs human review** - The finding is credible but intent, product behavior, migration safety, or public compatibility is uncertain
- **Out of scope** - The issue is real but the safe fix requires broad design changes, public contract decisions, or responsibility movement
- **No action** - The lane produced no useful or safe change

**High-confidence means all of the following are true:**

- The affected files and symbols are identified
- The evidence is stronger than a hunch
- The behavior change is either none or explicitly intended by the task
- The blast radius is understandable
- The change can be validated with tests, type checks, linting, build checks, code search, or focused inspection
- The change does not rely on changing public contracts, migrations, or external integrations without explicit approval

**Change budget:** In a large repository, do not try to implement every finding in one run. Choose the top 3-5 coherent, highest-confidence batches. It is better to finish a clean pass than to produce a sprawling cleanup diff nobody can review.

Prefer this implementation order unless the plan says otherwise:

1. Establish generated/vendor/public API exclusions
2. Remove clearly unused code and stale legacy paths
3. Break small circular dependencies that block other cleanup
4. Consolidate shared types and replace weak types where ownership is clear
5. Clean error handling and fallback behavior
6. Deduplicate code only where it genuinely simplifies the design
7. Remove comments, stubs, and polish-level slop last

---

## Phase 6: Implementation Plan

After the cleanup ledger is complete, call `context_builder` again with `response_type: "plan"` for the selected **Implement now** candidates.

```json
{"tool":"context_builder","args":{
  "instructions":"<task>Create an implementation plan for this Unslopify cleanup pass. Plan only the ledger items marked Implement now. Do not broaden the task into architecture redesign.</task>\n\n<context>Task: $ARGUMENTS\nDiscovery digest: <summarize the pre-builder discovery results>.\nContext review conclusions: <summarize confirmed findings and exclusions>.\nBaseline validation: <commands and results>.\nGenerated/vendor/public API exclusions: <list>.\nCleanup ledger items to implement:\n1. <ID, lane, candidate change, files, evidence, validation>\n2. <ID, lane, candidate change, files, evidence, validation>\n\nItems marked Needs human review, Out of scope, or No action are not implementation candidates.</context>\n\n<discovery_agent-guidelines>Focus only on files needed for the selected cleanup items. Preserve behavior. Order changes by safety and dependency. Include concrete done criteria and validation for each batch.</discovery_agent-guidelines>",
  "response_type":"plan",
  "export_response":true
}}
```

The plan should produce ordered cleanup batches with concrete done criteria. Treat it as the execution plan, not an invitation to expand scope.

---

## Phase 7: Oracle Satisfaction Gate

`ask_oracle` is required before implementation. Use it to review the cleanup ledger and the implementation plan.

Ask for a clear satisfaction signal:

```json
{"tool":"ask_oracle","args":{
  "chat_id":"<from context_builder>",
  "message":"Review this Unslopify cleanup ledger and implementation plan before editing. Are the selected Implement now items sufficiently evidence-backed, scoped, and safe? Are any candidates too risky, under-validated, or likely to change behavior? Reply with SATISFIED if there are no blocking concerns. Otherwise list only blocking concerns and the exact fix needed for each.",
  "mode":"plan",
  "new_chat":false
}}
```

If the oracle is not satisfied, keep going:

1. **Scope blocker:** Downgrade risky items to **Needs human review** or **Out of scope**
2. **Evidence blocker:** Run narrower discovery agents or focused code search, then update the ledger
3. **Coverage blocker:** Rerun `context_builder` with the missing area called out explicitly
4. **Validation blocker:** identify a better validation command or narrow inspection path
5. **Ordering blocker:** revise the implementation batches and dependencies
6. Ask `ask_oracle` again with the revised ledger and plan

Do not implement until the oracle confirms there are no blocking concerns. If the oracle raises a concern that cannot be resolved safely in the current task, remove that item from the implementation set and ask the oracle to review the reduced plan.

Do **not** ask `ask_oracle` to edit. You implement directly after satisfaction.

---

## Phase 8: Direct Implementation

**STOP** - Before implementing, verify you have:

- [ ] Quick scan notes
- [ ] Discovery-agent outputs for all applicable lanes
- [ ] Discovery digest
- [ ] Baseline validation notes
- [ ] A `context_builder` review result
- [ ] A cleanup ledger with decisions
- [ ] A `context_builder` implementation plan for selected items
- [ ] Oracle satisfaction on the selected plan
- [ ] A clear list of high-confidence changes

Implement in small batches. Prefer focused edits over broad rewrites.

**Primary tools:**

```json
{"tool":"apply_edits","args":{"path":"Root/File.ext","search":"old","replace":"new","verbose":true}}
```

```json
{"tool":"file_actions","args":{"action":"create","path":"Root/NewFile.ext","content":"..."}}
```

```json
{"tool":"read_file","args":{"path":"Root/File.ext","start_line":50,"limit":80}}
```

After each meaningful batch:

1. Review the changed files or diff if available
2. Run the narrowest relevant validation first
3. Fix any new failures caused by the batch
4. Re-run broader validation when the batch affects shared types, public APIs, dependency structure, or build configuration
5. Keep the diff cohesive. Do not combine unrelated cleanup just because you noticed it nearby

Do not parallelize implementation unless batches have zero file overlap and independent validation. Research can be parallel. Editing should usually be sequential.

If a change becomes murky while editing, stop and downgrade it to **Needs human review** or **Out of scope** unless oracle review or focused inspection clears the uncertainty.

---

## Phase 9: Verification and Final Oracle Review

Run the strongest practical validation available for the repository:

- Type checks
- Lint checks
- Unit/integration tests
- Build checks
- Dependency/cycle tools if relevant
- Code search confirming deleted symbols are gone or no longer referenced
- Focused inspection of public exports, dynamic entry points, routes, migrations, and generated registries touched by the cleanup

Then ask the oracle for final satisfaction before writing the final report:

```json
{"tool":"ask_oracle","args":{
  "chat_id":"<from context_builder>",
  "message":"Final Unslopify review. Completed changes: <summarize batches and files>. Validation results: <commands and results>. Remaining skipped items: <Needs human review / Out of scope>. Are there any blocking correctness, scope, or validation concerns before I report this as complete? Reply with SATISFIED if the cleanup is acceptable. Otherwise list only blocking concerns and the exact fix needed for each.",
  "mode":"chat",
  "new_chat":false
}}
```

If the oracle is not satisfied, keep going:

1. Fix the blocker if it is within the approved implementation scope
2. Re-run relevant validation
3. Update the completed-changes summary
4. Ask the oracle again

Continue until the oracle is satisfied. If a concern reveals that an item should not have been implemented, revert or narrow that item rather than defending a bad diff.

---

## Phase 10: Final Report

Report clearly:

```markdown
## Unslopify Report

### Summary
- <brief summary of what changed>

### Implemented cleanup batches
| ID | Lane | Change | Files | Validation |
|---|---|---|---|---|
| U1 | Unused code | Removed unused helper X | `path/file.ext` | `<command>` passed |

### Validation baseline vs final
| Command | Baseline | Final | Notes |
|---|---|---|---|
| `<command>` | pass/fail/not run | pass/fail/not run | ... |

### Oracle review
- Pre-implementation oracle gate: SATISFIED / notes
- Final oracle review: SATISFIED / notes

### Out of scope
- <findings not implemented and why>

### Needs human review
- <risky recommendations not implemented and why>

### Risks or follow-ups
- <remaining concerns>
```

No vague bragging. Name what changed, what passed, what failed, what was skipped, and what still needs judgment.

---

## Key Guidelines

**Behavior first:** Clean code that breaks behavior is not clean. Preserve public APIs, documented behavior, persisted data compatibility, and integration contracts unless the user explicitly asks for breaking changes.

**Discovery before builder:** Run focused discovery agents first so `context_builder` receives concrete evidence, not a vague cleanup wish.

**Evidence over vibes:** Static analysis, compiler output, tests, call sites, config, and documented architecture beat intuition.

**Cleanup is not redesign:** If the right answer requires broad design changes, say so and leave it out of the implementation pass.

**Oracle satisfaction is mandatory:** The oracle gets veto power over plan safety and final completion. Keep resolving blockers until it is satisfied.

**DRY carefully:** Duplication is sometimes cheaper than a bad abstraction. Consolidate only when the shared concept is real.

**Types must get stronger:** Replacing `any` with `unknown`, casts, or overly broad aliases without narrowing is not an improvement.

**Error handling should be honest:** Remove error hiding. Keep meaningful boundary handling, cleanup, retries, and error translation.

**Respect generated and vendor code:** Do not edit generated files, vendored dependencies, lockfiles, snapshots, or build artifacts unless the task and repo conventions require it.

**Use the repository's package manager:** Respect existing lockfiles and scripts. Do not casually switch npm/pnpm/yarn/bun, pip/poetry/uv, or equivalent tooling.

**Small batches win:** Cleanup work gets dangerous when it becomes a giant unreviewable diff.

---

## Anti-patterns to Avoid

- 🚫 Skipping pre-builder discovery agents and sending `context_builder` a vague cleanup prompt
- 🚫 Letting discovery agents edit independently and create conflicting diffs
- 🚫 Starting edits before oracle satisfaction
- 🚫 Treating oracle feedback as optional when it identifies blocking concerns
- 🚫 Skipping `context_builder` review and starting edits from discovery notes alone
- 🚫 Skipping the post-ledger `context_builder` implementation plan
- 🚫 Forcing one edit per lane just to prove the lane did something
- 🚫 Deleting code solely because one tool says it is unused
- 🚫 Removing dynamic entry points, routes, plugin registrations, migrations, or public exports without checking references
- 🚫 Creating a generic abstraction that makes simple code harder to read
- 🚫 Replacing `any` with `as Something` and pretending the type system improved
- 🚫 Removing every `try/catch` as a rule instead of judging its role
- 🚫 Deleting backwards-compatibility code without checking consumers or persisted data
- 🚫 Reformatting the whole repository as a side effect
- 🚫 Editing generated/vendor files without a specific reason
- 🚫 Installing new tools or changing lockfiles just to run an audit
- 🚫 Hiding uncertainty in the final report
- 🚫 Turning cleanup into a rewrite

---

**Your job:** Run discovery agents first, use their evidence to get a strong `context_builder` review and plan, classify findings in a cleanup ledger, obtain oracle satisfaction, implement only approved high-confidence cleanup batches, verify the result, obtain final oracle satisfaction, and leave a brutally clear report of what changed, what was skipped, and what still deserves human judgment.

```
