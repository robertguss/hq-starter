---
tags:
  - library
title: "Python Developer Tooling Handbook"
url: "https://pydevtools.com/handbook/"
company: [personal]
topics: []
created: 2026-01-06
source_type: raindrop
raindrop_id: 1528496302
source_domain: "pydevtools.com"
source_type_raindrop: link
collection: "Web Dev"
collection_id: 69284319
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

This is not a book about programming Python. Instead, the goal of this book is to help you understand the ecosystem of tools used to make Python development easier and more productive. For example, this book will help you make sense of the complex world of building Python packages: what exactly are uv, Poetry, Flit, Setuptools, and Hatch? What are the pros and cons of each? How do they compare to each other? It also covers tools for linting, formatting, and managing dependencies.

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: Python Developer Tooling Handbook

URL Source: https://pydevtools.com/handbook/

Markdown Content:
Tim Hopper

Research engineer and creator of the Python Developer Tooling Handbook.

## What to use.

And why

Python's tooling is a maze of overlapping tools, cautious official docs, and stale blog posts. This handbook tells you what to use today, and why.

By [Tim Hopper](https://tdhopper.com/) · Independent · Unsponsored · Kept current

Python’s tooling ecosystem is fragmented. Dozens of tools solve overlapping problems, official documentation avoids recommending the best modern options, and community advice is scattered across Reddit threads and blog posts that go stale. This handbook cuts through that noise.

It covers [packaging](https://pydevtools.com/handbook/reference/uv/), [linting and formatting](https://pydevtools.com/handbook/reference/ruff/), [testing](https://pydevtools.com/handbook/reference/pytest/), [type checking](https://pydevtools.com/handbook/reference/mypy/), and [dependency management](https://pydevtools.com/handbook/explanation/pyproject-vs-requirements/) with opinionated recommendations and honest trade-offs. Each tool’s [Reference](https://pydevtools.com/handbook/reference/) page links to its official documentation; the handbook complements those docs, the [Python Packaging User Guide](https://packaging.python.org/), and the [Scientific Python Library Development Guide](https://learn.scientific-python.org/development/), not replaces them.

## Get new Python tooling articles in your inbox

One email a month. No spam. Unsubscribe in one click.

## Topic hubs[](https://pydevtools.com/handbook/#topic-hubs)

Curated entry points for the tools and tasks at the heart of modern Python development.

[uv Python’s fastest package and project manager](https://pydevtools.com/handbook/topics/uv/)[Ruff Fast linting and formatting](https://pydevtools.com/handbook/topics/ruff/)[ty Astral’s new type checker](https://pydevtools.com/handbook/topics/ty/)[Testing Pytest, fixtures, parallel runs, and CI](https://pydevtools.com/handbook/topics/testing/)[Packaging Build wheels, lock dependencies, publish to PyPI](https://pydevtools.com/handbook/topics/packaging/)[Security Supply chain, attestations, vulnerability scans](https://pydevtools.com/handbook/topics/security/)[Scientific Python NumPy, CUDA, conda, pixi, ML stacks](https://pydevtools.com/handbook/topics/scientific-python/)[AI Assistants Claude Code, Cursor, Codex, GitHub Copilot](https://pydevtools.com/handbook/topics/ai-assistants/)

## Popular pages[](https://pydevtools.com/handbook/#popular-pages)

## Browse by section[](https://pydevtools.com/handbook/#browse-by-section)

*   **[Tutorial](https://pydevtools.com/handbook/tutorial/)** — Step-by-step guides for setting up tools and workflows.
*   **[How To](https://pydevtools.com/handbook/how-to/)** — Practical solutions to specific problems.
*   **[Explanation](https://pydevtools.com/handbook/explanation/)** — Context and background for understanding the ecosystem.
*   **[Reference](https://pydevtools.com/handbook/reference/)** — Tool-by-tool technical descriptions.

Feedback on any page is welcome via the form at the bottom.

## Recent Blog Posts[](https://pydevtools.com/handbook/#recent-blog-posts)

*   [Apr 16, 2026 ### Astral told you how they secure uv. Here's what to keep. Astral published a detailed writeup of how they secure their org. Most of it is team-scale GitHub policy. Four things translate directly to a solo Python maintainer.](https://pydevtools.com/blog/astral-security-post-what-to-keep/)
*   [Apr 16, 2026 ### PyPI's Second Audit Found 14 Bugs. Two Remain. Trail of Bits audited PyPI. Twelve issues were patched, two accepted. The accepted ones tell you more about PyPI than the twelve that were fixed.](https://pydevtools.com/blog/pypi-second-security-audit/)
*   [Apr 15, 2026 ### Your Python Wheels Still Target 2009 CPUs The wheel format cannot describe a CPU's instruction set, so default wheels compile for the lowest common denominator. Wheel variants would end that.](https://pydevtools.com/blog/your-python-wheels-still-target-2009-cpus/)
*   [Apr 14, 2026 ### uv won developer hearts. Now it has to win READMEs. uv is the most admired tool in the 2025 Stack Overflow survey, but adoption in real repos lags far behind. The gap is not just AI agents. It's the install snippets they read.](https://pydevtools.com/blog/uv-admired-but-not-adopted/)
*   [Apr 9, 2026 ### The Python Packaging Summit Returns to PyCon US The 2026 Packaging Summit convenes in Long Beach on May 15. Here's what's on the table based on the last two years of notes.](https://pydevtools.com/blog/python-packaging-summit-2026/)
*   [Apr 9, 2026 ### How uv Solves Dependencies So Fast Inside uv's dependency resolver: SAT solving, universal lock files, zero-copy deserialization, and why Python's lack of multi-version support makes this problem NP-hard.](https://pydevtools.com/blog/how-uv-solves-dependencies-so-fast/)
*   [Apr 8, 2026 ### LLM-Powered Copycats Are Flooding PyPI A developer published his first PyPI package. Within hours, three AI-generated clones appeared. The pattern is spreading, and it's a supply chain risk.](https://pydevtools.com/blog/llm-powered-copycats-are-flooding-pypi/)
*   [Apr 7, 2026 ### In 2012, Guido Had No Idea NumPy Had Its Own Packaging System A 2012 panel discussion between Guido van Rossum and the scientific Python community reveals how deep the disconnect on packaging ran.](https://pydevtools.com/blog/guido-had-no-idea-about-numpy-distutils/)
*   [Apr 3, 2026 ### Migrating from mypy to ty: Lessons from FastAPI Sebastián Ramírez has adopted ty across FastAPI, Typer, SQLModel, and more. His incremental migration strategy reveals the practical realities of switching type checkers on mature codebases.](https://pydevtools.com/blog/migrating-from-mypy-to-ty-lessons-from-fastapi/)
*   [Mar 24, 2026 ### LiteLLM Got Owned, and Your Dependencies Might Be Next A supply chain attack hit litellm on PyPI, stealing credentials and deploying backdoors. Bernát Gábor's guide shows how to defend against exactly this kind of threat.](https://pydevtools.com/blog/litellm-supply-chain-attack-and-securing-python-dependencies/)

[View all blog posts](https://pydevtools.com/blog/)

Last updated on April 17, 2026

Please submit corrections and feedback...

Search this site Results will appear as you type
