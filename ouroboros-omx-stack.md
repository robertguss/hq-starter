---
title: Ouroboros + Oh-My-Codex — Stacking Guide
tags:
  [ai-agents, workflow, claude-code, codex, ouroboros, oh-my-codex, engineering]
created: 2026-04-22
---

# Ouroboros + Oh-My-Codex — Stacking Guide

My personal workflow for using [Q00/ouroboros](https://github.com/Q00/ouroboros) and [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) together across every project. Claude Code does the thinking (spec, critique, evolve); Codex does the execution (writes the code). The two frameworks carve cleanly along that seam.

> This doc assumes the "Claude Code for planning, Codex for execution" preference. If you flip that, the commands reverse but the architecture still holds.

---

## Mental model

```
  ┌────────────────────────────┐          ┌──────────────────────────────┐
  │    Claude Code session     │          │       Codex session          │
  │                            │          │                              │
  │   OUROBOROS (thinking)     │          │   OMX (execution runtime)    │
  │   ─────────────────────    │  Seed    │   ────────────────────────   │
  │   ooo interview  ──┐       │ ───────► │   $ralplan (plan approval)   │
  │   ooo seed    ──── ┘       │  YAML    │   $team N:executor (parallel)│
  │   ooo evaluate  ◄─────────── results ─┤   $ralph (persistent owner)  │
  │   ooo evolve               │          │   .omx/ durable state        │
  │   ooo ralph (outer loop)   │          │                              │
  └────────────────────────────┘          └──────────────────────────────┘
              ▲                                         │
              │              shared ~/.codex/           │
              │        (skills, rules, config.toml,     │
              └───────  MCP servers, hooks.json) ───────┘
```

**The handoff artifact is a Seed YAML.** Ouroboros produces it in Claude Code. Codex consumes it — either directly via `ouroboros run workflow --runtime codex`, or indirectly by pasting its contents into an OMX session.

---

## The single most important insight

**Ouroboros has a native `CodexCliRuntime` adapter.** It can spawn Codex as its execution runtime and drive it with a Seed, with no OMX involvement needed for the basic path:

```bash
ouroboros run workflow --runtime codex ~/.ouroboros/seeds/seed_<id>.yaml
```

**OMX is the workflow layer that makes the Codex session itself better** — parallel teams, mixed-CLI workers, AGENTS.md orchestration, `.omx/` state, HUD.

They are not competitors. They operate at different layers:

- **Ouroboros** = the spec and the outer evolutionary loop
- **OMX** = the runtime Codex lives inside during execution

Both install skills/config into `~/.codex/`. They coexist by design.

---

## Prerequisites

- **macOS or Linux** (OMX's recommended path; native Windows is a degraded experience, use WSL2)
- **Node.js >= 20** (OMX)
- **Python >= 3.12** (Ouroboros)
- **OpenAI Codex CLI** installed and authenticated (`codex login status` passes)
- **Claude Code** CLI installed and logged into your Max/Pro plan
- **tmux** installed (`brew install tmux` / `apt install tmux`) for OMX team runtime
- **`gh` CLI** authenticated (for `ooo publish`)

---

## Install

Order matters: **OMX first**, **Ouroboros second**. OMX establishes the Codex baseline (`~/.codex/config.toml`, AGENTS.md, skills dir); Ouroboros layers on top and registers its own skills into the same directories.

### 1. Oh-My-Codex

```bash
# Install the official Codex CLI + OMX as a global npm package
npm install -g @openai/codex oh-my-codex

# Interactive setup: prompts, skills, AGENTS.md, config.toml, hooks
omx setup

# Verify install shape
omx doctor

# Prove the Codex auth actually works (doctor doesn't)
codex login status
omx exec --skip-git-repo-check -C . "Reply with exactly OMX-EXEC-OK"
```

`omx setup` installs:

- 30 agent prompts → `~/.codex/prompts/`
- 40 skills → `~/.codex/skills/`
- `~/.codex/config.toml` (MCP servers, HUD, model defaults)
- `~/.codex/hooks.json` (OMX-managed native Codex hooks)
- `AGENTS.md` in project root (orchestration brain, loaded by Codex at session start)

### 2. Ouroboros

One-liner installer (auto-detects Claude Code, Codex, Hermes, OpenCode):

```bash
curl -fsSL https://raw.githubusercontent.com/Q00/ouroboros/main/scripts/install.sh | bash
```

This uses `uv > pipx > pip` in that preference order. Python 3.12+ is enforced.

Then configure per runtime (run both):

```bash
ouroboros setup --runtime claude    # registers MCP server with Claude Code
ouroboros setup --runtime codex     # installs skills into ~/.codex/, writes ~/.ouroboros/config.yaml
```

Claude Code plugin-only alternative (if you don't want the system package):

```bash
claude plugin marketplace add Q00/ouroboros
claude plugin install ouroboros@ouroboros
# Then inside a Claude Code session:
> ooo setup
```

### 3. Verify the stack

Inside a **Claude Code** session:

```
> ooo help
> /mcp    # should show 'ouroboros' as connected
```

Inside a **Codex** session (launched with `omx`):

```
> $deep-interview --help
> ooo help          # Ouroboros skills are available in Codex too
```

Both sets of skills should resolve in both runtimes.

---

## The canonical workflow

Opinionated end-to-end flow for a non-trivial feature.

### Phase 1 — Clarify and specify (Claude Code)

```
# In a Claude Code session, working directory = your project repo

> ooo interview "I want to add multi-tenant isolation to the reporting layer"
```

`ooo interview` runs Socratic Q&A. Each round exposes hidden assumptions; it quantifies ambiguity and will not emit a Seed until **ambiguity ≤ 0.2**.

When interview signals readiness:

```
> ooo seed
```

Seed is written to `~/.ouroboros/seeds/seed_<id>.yaml` with:

- `goal` — primary objective
- `constraints` — hard limits
- `acceptance_criteria` — atomic, testable ACs
- `ontology_schema` — output structure
- `evaluation_principles` — weighted quality rubric
- `exit_conditions` — termination rules
- `metadata.ambiguity_score` (must be ≤ 0.2)
- `metadata.seed_id`

**Pause here.** Read the Seed. It's your contract. If it's wrong, `ooo interview` again before spending any execution tokens.

Optional: if the work is PRD-shaped (stakeholders, user stories), use `ooo pm` instead of `ooo interview` → produces a JSON PMSeed that `ooo publish` can break into GitHub issues.

### Phase 2 — Execute (Codex via OMX)

You have two execution shapes. Pick based on parallelism.

**Shape A — Single persistent owner** (serial, one Codex worker, easier to reason about):

From Claude Code (or terminal):

```bash
ouroboros run workflow --runtime codex ~/.ouroboros/seeds/seed_<id>.yaml
```

This spawns a Codex CLI session with the Seed injected. Because OMX is installed, the session has AGENTS.md, OMX skills, HUD, and state management active. Inside that session:

```
$ralplan "approve the implementation plan for this Seed"
$ralph "carry the approved plan to completion"
```

**Shape B — Parallel team** (multiple Codex workers, much faster for multi-file work):

```bash
omx team 3:executor "execute the spec at ~/.ouroboros/seeds/seed_<id>.yaml"
omx team status <team-name>
```

OMX spawns 3 executor workers in a tmux session, each in its own git worktree. They coordinate through `.omx/state/` shared task queue with claim-safe lifecycle.

**Shape C — Mixed Codex + Claude team** (killer feature for this workflow):

```bash
export OMX_TEAM_WORKER_CLI_MAP=codex,codex,codex,claude,claude
export OMX_TEAM_WORKER_CLI=auto
omx team 5:executor "execute seed at ~/.ouroboros/seeds/seed_<id>.yaml"
```

Three Codex workers write code, two Claude workers do review/test/refactor — all in the same tmux, sharing state. This is the best use of both subscriptions simultaneously.

### Phase 3 — Verify (Claude Code)

Back in Claude Code:

```
> ooo evaluate
```

Runs the 3-stage gate:

1. **Mechanical** (free) — tests pass, linters clean, ACs syntactically satisfied
2. **Semantic** — LLM verification against `evaluation_principles`
3. **Multi-Model Consensus** — independent models vote on whether the Seed's contract is met

If all three pass: merge. If any fail, the output names which AC drifted and why.

### Phase 4 — Evolve (on failure)

```
> ooo evolve
```

Produces a revised Seed informed by the evaluation results. Go back to Phase 2 with the new Seed.

### Phase 5 — Persistent loop (optional, for high-autonomy work)

```
> ooo ralph
```

Automates Phases 2–4 repeatedly until `evolve_step` reports `CONVERGED` (ontology stabilizes across consecutive generations). Survives session restarts — the EventStore reconstructs lineage.

### Phase 6 — Publish (when breaking down for a team)

```
> ooo publish
```

Takes the locked Seed, detects your GitHub repo via `gh`, and creates an Epic issue + Task issues with ACs distributed correctly. Good when handing off to humans.

---

## Command reference

### Ouroboros (use in Claude Code)

| Skill           | Purpose                                       | CLI equivalent                                          |
| --------------- | --------------------------------------------- | ------------------------------------------------------- |
| `ooo setup`     | Register runtime, wire MCP                    | `ouroboros setup --runtime {claude,codex,...}`          |
| `ooo interview` | Socratic Q&A, ambiguity scoring               | `ouroboros init start --llm-backend codex "idea"`       |
| `ooo seed`      | Emit immutable Seed YAML                      | _(bundled in `init start`)_                             |
| `ooo pm`        | PRD-style interview → PMSeed JSON             | _(MCP only)_                                            |
| `ooo run`       | Execute Seed via Double Diamond decomposition | `ouroboros run workflow --runtime codex seed.yaml`      |
| `ooo evaluate`  | 3-stage verification gate                     | _(MCP only)_                                            |
| `ooo evolve`    | Produce revised Seed from eval failures       | _(MCP only)_                                            |
| `ooo ralph`     | Persistent outer loop until convergence       | _(MCP only)_                                            |
| `ooo unstuck`   | 5 lateral-thinking personas                   | _(MCP only)_                                            |
| `ooo qa`        | General-purpose QA verdict on any artifact    | _(skill)_                                               |
| `ooo publish`   | Seed → GitHub Epic/Task issues (via `gh`)     | _(skill)_                                               |
| `ooo status`    | Executions + drift detection                  | `ouroboros status executions` / `status execution <id>` |
| `ooo cancel`    | Kill stuck/orphaned executions                | `ouroboros cancel execution [<id>\|--all]`              |
| `ooo update`    | Upgrade Ouroboros                             | `pip install --upgrade ouroboros-ai`                    |

### OMX (use in Codex session, launched with `omx`)

| In-session skill  | Purpose                                    |
| ----------------- | ------------------------------------------ |
| `$deep-interview` | Scope clarification (**see overlap note**) |
| `$ralplan`        | Approve implementation plan                |
| `$ralph`          | Persistent single-owner completion loop    |
| `$team N:<role>`  | Spawn N parallel workers                   |

| Terminal command             | Purpose                                              |
| ---------------------------- | ---------------------------------------------------- |
| `omx --madmax --high`        | Launch the interactive leader session (default path) |
| `omx --tmux --madmax --high` | Same, but leader in tmux (better for teams)          |
| `omx team N:executor "task"` | Spawn tmux team with N workers + worktrees           |
| `omx team status <name>`     | Check worker health + task distribution              |
| `omx team resume <name>`     | Resume durable team after interruption               |
| `omx team shutdown <name>`   | Clean up workers and state                           |
| `omx exec "..."`             | One-shot Codex invocation (smoke test)               |
| `omx doctor`                 | Install-shape verification                           |
| `omx hud --watch`            | Live status monitor                                  |
| `omx update`                 | Upgrade OMX, reruns setup                            |

---

## Avoiding overlap — three deliberate choices

Ouroboros and OMX each have skills that sound similar but do different things. Pick the right one for each phase.

### `ooo interview` vs `$deep-interview`

Use **`ooo interview`** (Claude Code) for all spec work. Reasons:

- Quantifies ambiguity; hard gate at ≤ 0.2
- Emits an **immutable Seed YAML** — a machine-consumable contract
- Has 3-stage evaluation downstream that scores against this contract

`$deep-interview` (Codex) is lighter — it clarifies scope for `$ralplan`, but doesn't produce a persisted spec artifact. Skip it when you're using Ouroboros; it's for users who run OMX standalone.

### `ooo run` vs `omx team`

Use **`ooo run` / `ouroboros run workflow --runtime codex`** when you want a single deterministic Codex session bound to the Seed.

Use **`omx team N:executor`** when the work has genuinely parallelizable tracks (e.g. backend + frontend + tests). Feed the Seed path into the task prompt; OMX's coordination handles the rest.

**Rule of thumb:** 1 agent if the work is sequential or you want clean reasoning; N agents if the work decomposes. A 3–5-worker mixed Codex+Claude team is the right default for features touching 3+ files.

### `ooo ralph` vs `$ralph`

These look identical but operate at different altitudes:

- **`$ralph`** (OMX/Codex) — keeps a single Codex owner hammering on an approved plan until execution is complete. Inner loop.
- **`ooo ralph`** (Ouroboros) — keeps the _evolution_ loop running: execute → evaluate → evolve → re-execute, until ontology converges across generations. Outer loop.

**Stacked correctly:** `ooo ralph` wraps everything. Inside each of its execute phases, OMX's `$ralph` or `omx team` is what actually does the Codex work. You rarely invoke `$ralph` manually when using Ouroboros — `ooo ralph` calls into OMX's execution primitives for you.

---

## Configuration layout

Reference for where each tool puts its state.

```
~/.ouroboros/
├── config.yaml                # Model routing, runtime backend, per-role LLM config
└── seeds/
    └── seed_<id>.yaml         # Every Seed you've generated

~/.codex/
├── config.toml                # Codex CLI config (OMX adds MCP servers, model defaults)
├── hooks.json                 # Native Codex hooks (OMX-managed + your own)
├── prompts/                   # OMX agent prompts (30)
├── skills/                    # Both OMX (40) and Ouroboros skills coexist here
└── rules/                     # Ouroboros routing rules

~/.claude/
└── mcp.json                   # Ouroboros MCP server registration for Claude Code

<project-root>/
├── AGENTS.md                  # OMX-generated orchestration brain, loaded by Codex
├── .omx/                      # OMX project state
│   ├── state/                 # Task queue, worker claims, mode tracking
│   ├── logs/                  # Session logs
│   ├── hooks/*.mjs            # OMX plugin hooks
│   └── project-memory.json    # MCP-accessible project memory
└── .codex/
    └── hooks.json             # Project-level Codex hooks (optional)
```

**Precedence notes:**

- Per-role Ouroboros model settings live in `~/.ouroboros/config.yaml`, **not** `~/.codex/config.toml`. Easy to get wrong.
- OMX's `gpt-5.4` config seeding recommends `model_context_window = 250000` and `model_auto_compact_token_limit = 200000` — it only writes these when missing, so edit freely.

---

## When to skip one of them

- **Skip Ouroboros** for tight, obvious tasks — rename a field, fix a failing test, a one-line config change. The interview-and-seed ceremony is pure tax when you already know the answer.
- **Skip OMX** when you're in Claude Code and the task doesn't need Codex at all (e.g. planning, design docs, code review of a PR without implementation). `$team` and `$ralph` are irrelevant if you never launch a Codex session.
- **Skip both** for throwaway work that doesn't merit either structure.
- **Use both** when: you're unsure what "done" means AND the work has multiple parallelizable tracks AND you want verified completion. That's their sweet spot.

---

## Troubleshooting

| Symptom                                      | Fix                                                                                                                                 |
| -------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `ooo` skills not resolving in Claude Code    | `/mcp` in Claude Code; if `ouroboros` shows error → `ooo update`; if still broken → `ooo setup`                                     |
| Codex session does not see OMX skills        | `omx doctor`; if skills missing, `omx setup` (refresh preserves your user hooks)                                                    |
| `omx doctor` green but execution fails       | `omx doctor` checks install shape, not auth. Run `codex login status` and `omx exec --skip-git-repo-check -C . "test"`              |
| Ambiguity won't drop below 0.2               | Scope is too big. Break the goal into sub-goals and run separate interviews, or use `ooo unstuck` for lateral framings              |
| Seed runs but evaluation fails every time    | Your ACs are non-atomic. Re-interview; look for ACs with "AND", vague verbs ("improve", "optimize"), or implied multi-file scope    |
| `ooo ralph` never converges                  | `ooo evolve`'s similarity threshold (≥ 0.95) can be too strict for fuzzy domains. Check `ouroboros status execution <id>` for drift |
| Team worker crashes leave stale `.omx/state` | `omx team shutdown <name>`; if that fails, `rm -rf .omx/state/sessions/<stale-id>/`                                                 |
| Non-interactive npm install didn't run setup | Run `omx setup` manually (interactive-only refresh is skipped in CI)                                                                |

---

## Cost awareness

- **`ooo interview`, `ooo seed`, `ooo evaluate`, `ooo evolve`, `ooo ralph`** run under whatever runtime you configured for Ouroboros. On Claude Code, this is your **Max Plan subscription** (no API key needed).
- **`ouroboros run --runtime codex`, `omx team`, `omx exec`** run under **OpenAI API** billing (or your Codex subscription).
- Mixed teams (`OMX_TEAM_WORKER_CLI_MAP=codex,claude,...`) burn both simultaneously.
- `ooo evaluate` stage 1 (mechanical) is free; stages 2–3 (semantic + consensus) are LLM calls that can add up — especially in `ooo ralph` where they run every cycle.

Plan accordingly: interview/spec/evaluate is cheap Claude work, execution is OpenAI spend.

---

## Rule of thumb

> **Ouroboros tells you what to build and checks that you built it. OMX builds it three ways at once inside Codex.**

Claude Code runs the thinking. Codex runs the typing. The Seed is the contract between them.
