---
name: process-pdfs
description: Ingest PDF research papers into the HQ vault as hydrated markdown via marker + Ollama. Use when the user drops PDFs in `inbox/`, asks to process, ingest, or add papers to the vault, mentions arXiv papers or research PDFs, or references this PDF workflow.
---

# process-pdfs

Full lifecycle for adding research papers to the HQ vault: extract PDF → markdown, verify output, weave into `library/index.md` synthesis, remind about DEVONthink archival. Defaults are tuned for AI/ML arXiv papers.

## Quick start

```bash
# Default: Ollama Cloud gemma4:31b-cloud (vision-capable, uses user's Ollama Cloud sub)
uv run .tools/process_pdfs.py --use-llm --llm-service ollama --ollama-model gemma4:31b-cloud

# Multiple PDFs in inbox — dry-run first
uv run .tools/process_pdfs.py --dry-run

# Offline / local fallback
uv run .tools/process_pdfs.py --use-llm --llm-service ollama --ollama-model qwen2.5vl:32b

# Verbose logs (shows full marker command, redacted keys, work dir)
uv run .tools/process_pdfs.py -v --use-llm --llm-service ollama --ollama-model gemma4:31b-cloud
```

Script docstring has the full flag reference: `.tools/process_pdfs.py`.

## Lifecycle

### 1. Detect

Check `inbox/*.pdf`. If empty, report and stop — do not invent work.

### 2. Extract

Run the script. The script streams marker's own output (tqdm bars, LLM calls) live. Watch for the `Copied N image(s) → ...-assets/` log line; if absent for a figure-heavy paper, investigate.

### 3. Verify

For each processed PDF:

- [ ] `.md` written to `library/academic-reference/<slug>.md`
- [ ] Frontmatter `title:` has **no** `**...**` markdown wrappers
- [ ] `library/academic-reference/<slug>-assets/` exists with PNG/JPG figures (when the paper has figures)
- [ ] `hydrated: true` and `hydrated_via: marker+llm-ollama-<model>` set
- [ ] Original PDF moved to `inbox/_processed/<filename>.pdf`

Re-processing (e.g. to compare models): `rm library/academic-reference/<slug>.md && mv inbox/_processed/<file>.pdf inbox/` and re-run. The script is idempotent and skips existing outputs.

### 4. Synthesize into `library/index.md`

**Do not just add a one-liner — the index is a compiled wiki, not a listing** (see project `CLAUDE.md` and `distillery/index.md`).

- Read the current `library/index.md` Synthesis section.
- Identify themes the paper fits (AI/ML agents, LLM reasoning, eval, context engineering, etc.) or propose a new theme if none fits.
- Write a multi-sentence entry that connects the new paper to existing library items using wikilinks — surface patterns and cross-references, not summaries.
- Match the voice and standards in `knowledge/author-profile.md`.

### 5. Archive

PDFs in `inbox/_processed/` are gitignored. User's canonical PDF store is DEVONthink. Remind the user to:

1. Drag the PDF into DEVONthink.
2. `rm inbox/_processed/<filename>.pdf` once filed.
3. Optionally paste the DEVONthink item URL (`x-devonthink-item://<UUID>`) into the `.md`'s `devonthink_url:` frontmatter for round-trip.

### 6. Commit

Do **not** auto-commit. Run the project CLAUDE.md pre-commit checklist:

- Indexes current (library/index.md updated per step 4)
- Frontmatter matches `knowledge/hq-vault-design.md` spec
- All wikilinks resolve

Then surface a proposed commit message and wait for explicit go-ahead.

## References

- Script: `.tools/process_pdfs.py` — all flags + marker/Ollama details in the docstring
- Frontmatter spec: `knowledge/hq-vault-design.md`
- Library synthesis structure: `library/index.md`
- Author voice anchors: `knowledge/author-profile.md`
- Self-contained-vault principle: `distillery/index.md`
- Gitignore rules for PDFs: `.gitignore` (`inbox/*.pdf`, `inbox/_processed/*.pdf`)
