---
tags:
  - library
title: "Seven Claude Code Skills for Python from the Creator of spaCy"
url: "https://pydevtools.com/blog/matthew-honnibal-claude-skills-for-python/"
company: [personal]
topics: []
created: 2026-02-18
source_type: raindrop
raindrop_id: 1606557189
source_domain: "pydevtools.com"
source_type_raindrop: article
collection: "AI Tools & News"
collection_id: 69284314
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

Matthew Honnibal, co-founder of Explosion and creator of spaCy, has published a collection of Claude Code skills for Python development. It’s one of the more thoughtful skill collections I’ve seen.
Claude Code skills are markdown files you place in ~/.claude/commands/. When you type / in Claude Code, the file’s contents are injected as instructions. Think of them as reusable prompts that give Claude a specific methodology for a task, rather than leaving it to improvise.

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: Seven Claude Code Skills for Python from the Creator of spaCy

URL Source: https://pydevtools.com/blog/matthew-honnibal-claude-skills-for-python/

Published Time: 2026-02-16

Markdown Content:
atthew Honnibal, co-founder of [Explosion](https://explosion.ai/) and creator of [spaCy](https://spacy.io/), has published [a collection of Claude Code skills](https://github.com/honnibal/claude-skills) for Python development. It’s one of the more thoughtful skill collections I’ve seen.

[Claude Code skills](https://docs.anthropic.com/en/docs/claude-code/skills) are markdown files you place in `~/.claude/commands/`. When you type `/<skill-name>` in Claude Code, the file’s contents are injected as instructions. Think of them as reusable prompts that give Claude a specific methodology for a task, rather than leaving it to improvise.

That distinction matters. Asking Claude to “review this code” produces shallow observations across many dimensions. These skills force deep, systematic analysis of one dimension at a time, using numbered checklists and concrete examples to keep the output focused. The collection covers type annotations, docstrings, error handling, resilience analysis, property-based testing, mutation testing, and structural overviews.

## pre-mortem: fictional bug reports for working code[](https://pydevtools.com/blog/matthew-honnibal-claude-skills-for-python/#pre-mortem-fictional-bug-reports-for-working-code)

The `pre-mortem` skill looks at working code and writes post-mortem reports for bugs that haven’t happened yet. It doesn’t look for current bugs. It looks for places where the code is fragile against future edits.

The output is written in past tense (“What happened,” “Why it broke”), which forces complete causal chains instead of vague warnings like “this could be a problem.”

Consider this property on a data pipeline result class:

```
@property
def success_rate(self):
    return len(self.valid_rows) / (len(self.valid_rows) + len(self.errors))
```

The skill imagined a scenario: a developer adds multi-field validation, so a single invalid row now produces multiple `ValidationError` objects. The denominator inflates, the numerator doesn’t, and the success rate exceeds 1.0. The formula assumes one error per row, but nothing enforces that. The code works today. It breaks after a plausible refactor.

## contract-docstrings and try-except: two angles on the same code[](https://pydevtools.com/blog/matthew-honnibal-claude-skills-for-python/#contract-docstrings-and-try-except-two-angles-on-the-same-code)

These two skills complement each other well. I analyzed this `save_to_disk` method with both:

```
def save_to_disk(self):
    try:
        os.makedirs(self.cache_dir, exist_ok=True)
        path = os.path.join(self.cache_dir, "cache.json")
        with open(path, "w") as f:
            json.dump(self._store, f)
    except Exception:
        pass
```

The `contract-docstrings` skill documents what a function demands, what it guarantees, and how it fails. Its key instruction: “document what is, not what should be.” For this function, the contract notes that all exceptions are silently discarded: `PermissionError`, `TypeError` from non-serializable values, `OSError` from a full disk. The caller cannot know if the save succeeded.

It also found a subtler problem in the corresponding `load_from_disk` method: `json.load` can return any valid JSON type, so if the cache file somehow contains `[1, 2, 3]`, the load “succeeds” and silently sets the internal store to a list instead of a dict. Every subsequent method call breaks, far from the actual cause.

The `try-except` skill takes a different angle. It audits exception handling with a five-point checklist. The first question, “right mechanism?”, asks whether try/except is appropriate at all. External state operations (filesystem, network) justify try/except. Local value checks should use conditionals instead.

For the same function, it proposes splitting the broad catch into targeted handlers:

```
def save_to_disk(self):
    path = os.path.join(self.cache_dir, "cache.json")
    try:
        os.makedirs(self.cache_dir, exist_ok=True)
    except OSError as e:
        logging.warning("Failed to create cache directory %s: %s", self.cache_dir, e)
        return
    try:
        with open(path, "w") as f:
            json.dump(self._store, f)
    except OSError as e:
        logging.warning("Failed to write cache file %s: %s", path, e)
    # Note: TypeError from json.dump is NOT caught -- it indicates
    # non-serializable data in the cache, which is a bug.
```

`os.path.join`, a pure string operation, moves out of the try block. The `TypeError` from `json.dump` stays uncaught: it’s a bug, not a recoverable error.

One skill documents the current behavior. The other rewrites it. Together they cover both “what is” and “what should be.”

## tighten-types and hypothesis-tests[](https://pydevtools.com/blog/matthew-honnibal-claude-skills-for-python/#tighten-types-and-hypothesis-tests)

The `tighten-types` skill works through six categories of type improvements, ordered by impact. Given a class like:

```
class WeatherCache:
    def __init__(self, ttl=DEFAULT_TTL, cache_dir=CACHE_DIR):
        self.ttl = ttl
        self.cache_dir = cache_dir
        self._store = {}
        self._hits = 0
```

It adds class-level attribute annotations, parameterizes bare `dict` to `dict[str, CacheEntry]`, and spots the repeated `{data, timestamp, city}` dict shape across six locations as a `TypedDict` candidate.

The `hypothesis-tests` skill generates property-based tests with the [Hypothesis](https://hypothesis.readthedocs.io/) library. It builds input strategies that model each function’s valid inputs, then tests properties like roundtrip correctness and idempotence. The “encode constraints, don’t filter” directive (`st.integers(min_value=1)` instead of `st.integers().filter(lambda x: x > 0)`) shows real Hypothesis expertise.

## A note on security[](https://pydevtools.com/blog/matthew-honnibal-claude-skills-for-python/#a-note-on-security)

The skills use `.md.txt` rather than `.md`. GitHub renders `.md` as HTML, so a malicious skill could hide HTML payloads invisible to anyone browsing the repo. `.md.txt` shows raw text, making the full prompt auditable. Skills run with full filesystem and shell access, so this caution matters.

## Getting started[](https://pydevtools.com/blog/matthew-honnibal-claude-skills-for-python/#getting-started)

To install a skill, copy it to `~/.claude/commands/` and rename it from `.md.txt` to `.md`:

```
curl -o ~/.claude/commands/pre-mortem.md \
  https://raw.githubusercontent.com/honnibal/claude-skills/main/pre-mortem.md.txt
```

Then invoke it in Claude Code with `/pre-mortem src/mypackage/`.

The full collection is at [github.com/honnibal/claude-skills](https://github.com/honnibal/claude-skills). If you only install one, make it `pre-mortem`.
