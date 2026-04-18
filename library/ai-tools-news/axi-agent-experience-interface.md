---
tags:
  - library
title: "AXI: Agent eXperience Interface"
url: "https://axi.md/"
company: [personal]
topics: []
created: 2026-04-09
source_type: raindrop
raindrop_id: 1678698067
source_domain: "axi.md"
source_type_raindrop: link
collection: "AI Tools & News"
collection_id: 69284314
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

10 design principles for agent-ergonomic CLI. 100% task success at the lowest cost — validated across two benchmarks and 915 runs.

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: AXI: Agent eXperience Interface

URL Source: https://axi.md/

Markdown Content:
AXI — Agent eXperience Interface

## Let's build apps that [agents] love.

10 design principles for agent-ergonomic CLI. 100% task success at the lowest cost — validated across two benchmarks and 915 runs.

Avg Cost per Task

chrome-devtools-mcp-code

$0.120

chrome-devtools-mcp

$0.100

chrome-devtools-mcp-search

$0.096

chrome-devtools-mcp-compressed

$0.091

agent-browser

$0.088

dev-browser

$0.078

chrome-devtools-axi

$0.074

Avg Duration per Task

chrome-devtools-mcp-code

36.2s

chrome-devtools-mcp-compressed

29.7s

chrome-devtools-mcp-search

29.4s

dev-browser

28.6s

chrome-devtools-mcp

26.0s

agent-browser

24.6s

chrome-devtools-axi

21.5s

Tell your agent to try it out

`Run `npx -y gh-axi` for Github operations``Run `npx -y chrome-devtools-axi` for browser automation`

Build your own AXI

Install the AXI skill to get the design guidelines and scaffolding:

`npx skills add kunchenguid/axi`

[Github Repo](https://github.com/kunchenguid/axi) · [Kun Chen](https://x.com/kunchenguid) Presents

Premise

## Neither CLI nor MCP gives [agents] enough love.

AI agents interact with external services through two dominant paradigms. The first is **shell-based CLI execution**: the agent runs commands like `gh issue list` or `agent-browser navigate` and parses the text output. The second is **structured tool protocols** like MCP (Model Context Protocol), where the agent invokes typed tool functions through the hosting framework’s native tool-calling interface.

Both approaches have significant problems for agents:

*   **CLI: action and observation are separated.** Browser CLIs return minimal confirmations — `navigate` returns only a page title, `click` returns “Done” — forcing the agent to call `snapshot` after every action. This doubles tool calls and wastes token budget. 
*   **MCP: schema overhead scales with tool count.** A browser MCP server exposes ~30 tools. Their schemas inflate input tokens — MCP conditions average 185K tokens per task vs. 79K for AXI — and the overhead compounds across every turn. 
*   **Both: poor discoverability.** CLI agents must guess subcommands or read `--help`. MCP agents with lazy loading guess wrong tool names — selecting `take_screenshot` (1MB base64 PNG) instead of `take_snapshot` (80KB text) — and crash the session. Neither provides in-context guidance on what to do next. 

Recent debate has framed this as “MCP vs. CLI” [[2]](https://axi.md/#ref-smithery), but the real question is neither _which_ protocol nor _which_ transport, but rather _what design principles_ make an agent-tool interface effective.

AXI is **10 principles for agent-ergonomic CLI design** that treat token budget as a first-class constraint. AXI achieves the reliability advantages MCP promises (structured output, discoverability) at the cost profile of a CLI.

* * *

### Contributions

1.    Ten design principles for agent-ergonomic CLI tools, organized into four categories. 
2.    Reference implementations ([`gh-axi`](https://github.com/kunchenguid/gh-axi) for GitHub, [`chrome-devtools-axi`](https://github.com/kunchenguid/chrome-devtools-axi) for browser automation) demonstrating the principles across two domains. 
3.    Two benchmarks — 490 browser automation runs and [425 GitHub API runs](https://github.com/kunchenguid/axi/blob/main/bench-github/published-results/STUDY.md) — comparing seven interface conditions each, with trajectory-level analysis showing where and why each interface succeeds or fails. 

Context

## Related Work

#### Model Context Protocol (MCP)

Anthropic’s Model Context Protocol [[1]](https://axi.md/#ref-mcp) provides a standardized way to connect AI models to external tools through structured, typed tool definitions. While MCP offers type-safe schemas and discoverable tool catalogs, the schema overhead is substantial. The evaluation below quantifies this cost: MCP conditions use 2.3× more input tokens than AXI (185K vs. 79K per task), and the overhead compounds across multi-step tasks.

#### MCP vs. CLI benchmarks

Mao and Pradhan [[2]](https://axi.md/#ref-smithery) benchmarked 756 runs comparing raw APIs, CLI, and native MCP across GitHub, Linear, and Singapore Bus APIs. They found native MCP achieved 91.7% success vs. 83.3% for CLI, with CLI using 2.9× more billed tokens. However, their CLI was auto-generated from API specs, not hand-designed for agents. They note: “What this does not settle is whether a hand-crafted, agent-first CLI could close the remaining gap.” AXI answers this question directly — an agent-first CLI not only closes the gap but surpasses MCP on every metric.

#### Code execution with MCP

Jones and Kelly [[3]](https://axi.md/#ref-anthropic-code) identified two scaling problems with direct MCP tool calls: tool definitions overload the context window, and intermediate results consume additional tokens as they pass through the model between calls. They proposed presenting MCP tools as a code API that the agent programs against, so that data flows through the execution environment rather than the context window. Varda and Pai [[4]](https://axi.md/#ref-cloudflare-code) independently arrived at the same insight, coining the term “Code Mode” and reporting that LLMs handle complex, multi-step tool interactions better when writing TypeScript than when making direct tool calls. The code-mode condition in our browser benchmark evaluates this approach. Code execution achieves 100% reliability, but write-run-debug loops make it the slowest condition (36.2s avg) and, at $0.120/task, the most expensive condition. In a [separate GitHub benchmark](https://github.com/kunchenguid/axi/blob/main/bench-github/published-results/STUDY.md), code mode was the cheapest MCP condition ($0.101/task) by batching API calls — suggesting the trade-off is domain-dependent.

The Model

## The [10 principles].

1.   **Token-efficient output** — Use TOON format for ~40% token savings over JSON 
2.   **Minimal default schemas** — 3–4 fields per list item, not 10+ 
3.   **Content truncation** — Truncate large text fields with size hints and escape hatches 
4.   **Pre-computed aggregates** — Include aggregated counts and statuses that eliminate round trips 
5.   **Definitive empty states** — Explicit “0 results” rather than ambiguous empty output 
6.   **Structured errors & exit codes** — Idempotent mutations, structured errors, no interactive prompts 
7.   **Ambient context** — Self-install into session hooks so agents see state before invoking 
8.   **Content first** — Prefer showing actual data, not a wall of help text 
9.   **Contextual disclosure** — Append relevant next-step commands after output, not all upfront 
10.   **Consistent way to get help** — Concise per-subcommand reference for when agents need it 

### Efficiency

#### 1. Token-efficient output

Use TOON (Token-Optimized Object Notation) format instead of JSON or tab-separated tables. TOON omits braces, quotes, and commas, yielding approximately 40% token savings over equivalent JSON while remaining unambiguous to LLMs.

Conventional (JSON)

```
[{"number":42,"title":"Fix login bug","state":"open",
 "author":"alice","labels":["bug","P1"]},
{"number":43,"title":"Add dark mode","state":"open",
 "author":"bob","labels":["feature"]}]
```

AXI (TOON)

```
issues[2]{number,title,state}:
  42,Fix login bug,open
  43,Add dark mode,open
```

#### 2. Minimal default schemas

Return 3–4 fields per list item by default, not 10+. Agents rarely need all available fields and can request additional ones explicitly via a `--fields` flag.

#### 3. Content truncation

Truncate large text fields to a configurable limit, appending a size hint such as 
```
(truncated, 2847 chars total — use --full to see complete
            body)
```
. This prevents a single verbose response from consuming the agent’s context budget while preserving enough content for most tasks.

* * *

### Robustness

#### 4. Pre-computed aggregates

Include aggregate or derived fields that eliminate round trips. The most impactful example is `totalCount`: always report the total number of items, not just the page size. Other examples include computed CI status summaries (e.g., “27 passed, 0 failed, 10 skipped”) inline in PR views.

Conventional: no total count

```
$ gh label list
bug    Something isn't working    #d73a4a
docs   Improvements or additions  #0075ca
... (30 rows -- default page, no total)
```

AXI: total count + CI pre-computed

```
$ gh-axi label list
count: 126
labels[126]{name}:
  bug
  docs
  ...

$ gh-axi pr view 51772
pull_request:
  title: "refactor(plugins): route..."
  state: merged
  checks: "27 passed, 0 failed, 10 skipped"
```

#### 5. Definitive empty states

When a query returns no results, output an explicit zero-result message rather than empty output. Agents cannot distinguish “no output” from “command failed silently” without this signal.

#### 6. Structured errors & exit codes

Mutations should be idempotent, errors should be structured and written to stdout (not stderr), and commands must never prompt for interactive input. Reserve stdout for structured data and stderr for debug/log output. Use clean exit codes: 0 for success, 1 for errors.

* * *

### Discoverability

#### 7. Ambient context

Self-install into the agent’s session hooks so that every conversation starts with relevant state already visible — before the agent takes any action. The hook outputs a compact, directory-scoped dashboard to stdout, which the agent receives as initial context.

#### 8. Content first

Running a command with no arguments should display live, actionable data rather than help text. The home view should also include the current executable path, with the home-directory prefix rendered as `~`, and a one-sentence description of what the AXI does.

Conventional: no-args shows help

```
$ gh issue
Work with GitHub issues.

USAGE
  gh issue <command> [flags]

AVAILABLE COMMANDS
  close, create, list, view, ...
```

AXI: no-args shows live state

```
$ gh-axi issue
bin: ~/.local/bin/gh-axi
description: Browse and manage GitHub issues for the current repository
count: 14 of 8771 total
issues[14]{number,title,state}:
  51815,"[Bug]: Telegram plugin...",open
  ...
help[2]:
  Run `gh-axi issue view <number>`
  Run `gh-axi issue create --title "..."`
```

#### 9. Contextual disclosure

Append `help[]` lines after output, suggesting logical next steps as concrete command templates. Carry forward fixed disambiguating flags, but leave runtime values parameterized as placeholders like `<id>` instead of guessing them. This eliminates tool-discovery turns and guides agents through multi-step workflows.

#### 10. Consistent way to get help

Each subcommand should offer a concise `--help` flag as a fallback when contextual hints are insufficient.

Method

## Experimental Setup

#### Conditions

The benchmark evaluates seven agent-tool interface conditions for browser automation:

| Condition | Interface | Description |
| --- | --- | --- |
| **chrome-devtools-axi** | Bash CLI (AXI) | AXI wrapper around chrome-devtools-mcp. Combined operations, TOON metadata, contextual suggestions. |
| **dev-browser** | Bash CLI | Sandboxed browser scripting via `dev-browser run script.js`. Agent writes small JS files and prints only targeted results. |
| **agent-browser** | Bash CLI (Rust) | Vercel’s Agent Browser — the raw CLI baseline. |
| **chrome-devtools-mcp** | MCP (no ToolSearch) | Chrome DevTools MCP server. All ~30 tool schemas loaded upfront. |
| **chrome-devtools-mcp-search** | MCP + ToolSearch | Same MCP server, tools discovered on-demand. |
| **chrome-devtools-mcp-code** | TypeScript scripts | Agent writes `.ts` scripts calling `callTool()` which forwards to chrome-devtools-mcp via a persistent MCP bridge. |
| **chrome-devtools-mcp-compressed** | MCP Compressor CLI | mcp-compressor wraps the MCP server into CLI subcommands. Agent uses Bash. |

#### Task design

The benchmark includes 14 tasks across four categories:

*   **Single-step (4 tasks):**`read_static_page`, `wikipedia_fact_lookup`, `github_repo_stars`, `wikipedia_table_read` — navigate to one page and extract information. 
*   **Multi-step (5 tasks):**`wikipedia_link_follow`, `github_navigate_to_file`, `wikipedia_infobox_hop`, `multi_page_comparison`, `wikipedia_search_click` — navigate, interact, and follow links across pages. 
*   **Investigation (4 tasks):**`wikipedia_deep_extraction`, `github_issue_investigation`, `multi_site_research`, `tabular_data_analysis` — complex multi-page extraction requiring context across navigations. 
*   **Error recovery (1 task):**`navigate_404` — handle failures gracefully. 

#### Infrastructure

Each run creates a fresh workspace with condition-specific `CLAUDE.md`. All MCP-based conditions use the same backend: `chrome-devtools-mcp@latest --headless --isolated`. Agent: Claude Sonnet 4.6. Judge: Claude Sonnet 4.6. Five repeats per condition–task pair: 14 × 7 × 5 = 490 total runs.

A [separate benchmark targeting GitHub API tasks](https://github.com/kunchenguid/axi/blob/main/bench-github/published-results/STUDY.md) (425 runs, 5 conditions, 17 tasks) validates the same pattern in a different domain.

#### Metrics

*   **Task success** (binary): determined by an LLM judge comparing the agent’s answer against a reference answer and rubric. 
*   **Cost** (USD): total API cost, computed from input/output token counts at published rates. 
*   **Duration** (seconds): wall-clock time from task start to final response. 
*   **Turns**: number of tool invocations the agent makes. 

Proof

## Results

490 runs, 14 tasks × 5 repetitions × 7 conditions

Aggregate

| Condition | Success | Avg Cost | Avg Duration | Avg Turns |
| --- | --- | --- | --- | --- |
| **chrome-devtools-axi** | **100%** | **$0.074** | **21.5s** | **4.5** |
| dev-browser | 99% | $0.078 | 28.6s | 4.9 |
| agent-browser | 99% | $0.088 | 24.6s | 4.8 |
| chrome-devtools-mcp-compressed | 100% | $0.091 | 29.7s | 7.6 |
| chrome-devtools-mcp-search | 99% | $0.096 | 29.4s | 7.5 |
| chrome-devtools-mcp | 99% | $0.100 | 26.0s | 6.2 |
| chrome-devtools-mcp-code | 100% | $0.120 | 36.2s | 6.4 |

AXI (`chrome-devtools-axi`) achieves 100% task success at the lowest average cost ($0.074/task), shortest duration (21.5s), and fewest turns (4.5). It is the only condition that leads simultaneously on all four metrics. The field is competitive — dev-browser is within 5% on cost — but AXI’s consistency across the full task suite gives it the edge.

* * *

### Corroborating evidence: GitHub benchmark

A [separate 425-run benchmark](https://github.com/kunchenguid/axi/blob/main/bench-github/published-results/STUDY.md) comparing `gh-axi` against raw `gh` CLI and GitHub MCP across 17 tasks arrives at the same conclusions: **AXI achieves 100% success at $0.050/task**, vs. 86% at $0.054 for CLI and 82–87% at $0.101–$0.148 for MCP. The cost gap widens dramatically on complex tasks: `ci_failure_investigation` costs $0.065 for AXI vs. $0.758 for MCP (12×).

Analysis

## Findings

Finding 1

#### AXI leads on every metric.

`chrome-devtools-axi` achieves 100% success at the lowest cost ($0.074/task), fewest turns (4.5), and fastest execution (21.5s). It is the only condition that leads simultaneously on all four metrics. The field is competitive — `dev-browser` is within 5% on cost ($0.078) — but AXI’s consistency across the full task suite gives it the edge.

Trajectory analysis across all 70 AXI runs reveals multiple mechanisms behind the cost advantage:

*   **Specialized extraction commands.** AXI’s `tables --url` command navigates to a page and returns structured table data in a single step. On extraction tasks, this reduces the entire interaction to 2 turns at $0.047/task — a 3.1× cost reduction vs. MCP-code on the same task ($0.147). 
*   **Pipe-based filtering.** The agent pipes CLI output through shell tools (`| grep`, `| head`, `| tail`) to return only matching lines instead of full accessibility snapshots. This keeps per-turn token volume compact. 
*   **Combined operations.**`open` combines navigate + snapshot; `click --query` returns the updated snapshot with search results automatically. This eliminates the separate `take_snapshot` calls that MCP conditions require after every action. 

Finding 2

#### Code-writing pays a coordination tax.

Both code-writing conditions achieve near-perfect success: `chrome-devtools-mcp-code` at 100% and `dev-browser` at 99%. MCP-code’s perfect reliability comes at $0.120/task and 6.4 turns — 1.6× AXI’s cost. `dev-browser` is more competitive at $0.078 and 4.9 turns, occasionally beating AXI on multi-site tasks where script batching eliminates sequential navigation.

On `multi_site_research`, `dev-browser`’s best run costs $0.059 (4 turns, 3 scripts) vs. AXI’s $0.090 (6 turns). Batching three site visits into three focused scripts avoids the per-navigation overhead of AXI’s sequential `open --query` pattern. The trade-off: when scripts fail, write-run-debug loops push costs higher — `dev-browser` ranges from $0.059 to $0.100 across the 5 runs (1.7× spread).

Finding 3

#### MCP Compressor validates CLI-over-MCP.

[MCP Compressor](https://github.com/atlassian-labs/mcp-compressor/) open sourced by Atlassian (100% success, $0.091/task, 7.6 turns) wraps any MCP server into a single CLI tool, converting each MCP tool into a Bash subcommand. This single change — CLI over MCP — eliminates schema overhead and enables shell composability (`| grep`, `| head`).

The remaining 23% gap to AXI ($0.091 vs. $0.074) comes from two sources: MCP Compressor still requires separate `navigate-page` + `take-snapshot` calls where AXI’s `open` returns both in one due to its ergonomic interface design.

Case Studies

## Trajectory analysis.

### Case A: Specialized extraction — from 11 turns to 2

`wikipedia_deep_extraction` — Navigate to the Wikipedia list of Nobel laureates in Physics and report the winners for the 3 most recent years, including all co-laureates.

chrome-devtools-axi — 2 turns · $0.047

```
Call 1:
$ chrome-devtools-axi tables \
    --url "<nobel-physics-url>" \
    2>/dev/null | tail -100
→ Structured table data: years, names,
   countries, and citations for all
   laureates. 2025, 2024, 2023 are
   the last rows.

Done. Agent reads the output and
responds with all co-laureates for
2023–2025. Total time: 7.9s.
```

chrome-devtools-mcp-code — 11 turns · $0.194

```
Turn 1: Write + run get_nobel.ts
  → Navigate and dump the raw snapshot.

Turns 2–4: Write + run probing scripts
  → Identify the recent-year rows and
  inspect the table structure.

Turns 5–10: Refine extraction logic
  → Track rowspans, filter non-person
  links, and verify co-laureates.

Turn 11: Final extraction succeeds.
  Total time: 58.6s.
```

AXI’s `tables --url` command navigates, extracts, and structures table data in a single operation. The MCP-code agent follows a fundamentally different path: discover tool interfaces, read type signatures, write TypeScript, inspect the rendered table, and refine extraction logic for continuation rows — 11 turns and multiple script iterations to arrive at the same answer. Across all 5 runs, MCP-code costs $0.103–$0.194 (4–11 turns) vs. AXI’s consistent $0.047 (2 turns).

* * *

### Case B: Combined operations still beat a 7-turn script loop

`wikipedia_search_click` — Go to Wikipedia, search for “Turing Award”, and report who the first recipient was.

chrome-devtools-axi — 5 turns · $0.086

```
Call 1:
$ chrome-devtools-axi navigate --url <url>
→ error: "Unknown command: navigate"
   help[1]: Run `--help` to see commands

Call 2:
$ chrome-devtools-axi --help
→ Tips: "Prefer open <url> --query"
   "fill @<uid> --submit fills and
   submits in one step."

Call 3:
$ chrome-devtools-axi open \
    "<wikipedia-main-page>" \
    --query "search"
→ Navigate + filter to search field.
   Agent sees @1_11.

Call 4:
$ chrome-devtools-axi fill @1_11 \
    "Turing Award" --submit
→ Fill + submit + wait + snapshot
   in one command. Article returned.
   "First recipient: Alan Perlis."
```

chrome-devtools-mcp-code — 7 turns · $0.132

```
Turns 1–2: Write + run script
  → Navigate to Wikipedia and capture
  the main-page snapshot.

Turn 3: Write follow-up script
  → First attempt fails after guessing
  the wrong wrapper export name.

Turns 4–6: Read generated exports,
  rewrite with click() + pressKey(),
  and rerun the search sequence.

Turn 7: Final extraction.
  The Turing Award article states the
  first recipient was Alan Perlis.
```

The critical command is `fill @1_11 "Turing Award" --submit`. This single invocation fills the search box, submits the form, waits for the results page, and returns the snapshot — four operations in one step. The MCP-code agent still has to orchestrate these as separate wrapper calls (`click()`, `typeText()`, `pressKey()`, `takeSnapshot()`), and it spent extra turns confirming the generated export names before the sequence ran cleanly. Across the rerun, the task ranged from $0.132 to $0.316 (7–18 turns). This is **Principle 4 (pre-computed aggregates)** applied to actions: the tool does the multi-step work so the agent doesn’t have to.

* * *

### Case C: Query filtering eliminates the snapshot–search cycle

`wikipedia_infobox_hop` — Find the developer of Python from its infobox, then follow the link and report when the Python Software Foundation was founded.

chrome-devtools-axi — 5 turns · $0.082

```
Call 1:
$ chrome-devtools-axi navigate --url <url>
→ error: "Unknown command: navigate"
   help[1]: Run `--help` to see commands

Call 2: --help

Call 3:
$ chrome-devtools-axi open \
    "<python-wiki-url>" \
    --query "stable release developer"
→ Navigate + filter snapshot to
   matching lines. Agent sees
   developer and relevant links.

Call 4:
$ chrome-devtools-axi click @1_161 \
    --query "founded formed"
→ Click PSF link + search result
   page in one command. Found
   "June 2001". Done.
```

agent-browser — 7 turns · $0.164

```
Call 1: --help
  → Discover available commands.

Call 2: open + wait 2000 + snapshot
  → Full snapshot of Python page.
  Agent manually scans for infobox.

Call 3: click + wait 2000 + snapshot
  → Click link. Wait for load.
  Take full snapshot of new page.

Call 4: get url
  → Verify navigation succeeded.

Call 5: find text "Python Software
  Foundation" click + wait + get url
  → Retry click with text match.

Call 6: eval document.querySelector
  → DOM query to extract link URL.

Call 7: open + wait 2000 + snapshot
  → Navigate to PSF page. Full
  snapshot. Manual scan. Done.
```

AXI’s `--query` flag turns every command into a filtered view. `open --query "stable release developer"` returns only the matching lines from the snapshot instead of the full Wikipedia page. `click @id --query "founded formed"` clicks the link _and_ searches the resulting page in one step. The agent-browser condition has no equivalent — every action requires a separate `wait` + `snapshot` cycle, plus verification steps (`get url`, `eval`) to confirm the action worked. This is **Principle 9 (contextual disclosure)**: the tool returns targeted, relevant output after each action instead of dumping the full page state.

Limitations

## Caveats.

*   **Public websites only.** All tasks target public sites (Wikipedia, GitHub, example.com). Results may vary on authenticated or dynamic web applications. 
*   **Single agent model.** Only Claude Sonnet 4.6 is evaluated. Other models may exhibit different sensitivities to output format. 
*   **Read-only tasks.** The benchmark includes only read and navigation operations. Form submissions and complex interactions introduce additional challenges. 
*   **LLM judge.** Task success is determined by an LLM judge, which may introduce scoring biases. 
*   **Domain-specific implementation.** While the AXI principles are domain-general, this evaluation focuses on browser automation. The [GitHub benchmark](https://github.com/kunchenguid/axi/blob/main/bench-github/published-results/STUDY.md) provides cross-domain validation. 

Implication

## The answer is [principled design], not protocol choice.

The debate between CLI and MCP as agent-tool interfaces misses the deeper question: what design principles make any interface effective for agents? This evaluation shows that a principled CLI design (AXI) leads both raw CLI and MCP on every metric — success, cost, duration, and turns.

In browser automation, AXI achieves 100% reliability at $0.074/task and 4.5 turns, compared to $0.088 and 4.8 turns for raw CLI and $0.100 and 6.2 turns for MCP. The primary mechanism is specialized commands: AXI’s `tables --url` reduces extraction tasks to a single 2-turn interaction, while combined operations (`open`, `click --query`) eliminate the separate snapshot calls that MCP conditions require. Shell composability (`| grep`, `| tail`) keeps per-turn token volume compact.

A separate GitHub benchmark validates the same pattern: AXI at 100% success and $0.050/task vs. 86% and $0.054 for CLI, and 82–87% and $0.101–$0.148 for MCP. The 10 AXI principles provide a concrete, testable framework for designing agent-ergonomic interfaces that are both reliable and cost-efficient.
