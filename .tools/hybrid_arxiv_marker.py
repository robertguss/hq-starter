#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""
Hybrid arxiv2md + marker ingestor for arXiv papers.

For arXiv papers with HTML available, `arxiv2md` gives much cleaner output
than marker (clean tables, proper LaTeX math, correct heading levels, no OCR
errors) but loses algorithm bodies and references figures as remote URLs.
Marker gives messier OCR'd text but preserves algorithm code blocks and
extracts local image assets.

This script combines them:
  - Body, tables, prose, references from arxiv2md
  - Algorithm code blocks from marker's .md
  - Figure image embeds swapped to marker's local -assets/ paths
  - Math `$$ $...$ (N) $$` wrapper bug fixed
  - Vault frontmatter applied

Usage:
  uv run .tools/hybrid_arxiv_marker.py <arxiv_id> <slug>
  # e.g.
  uv run .tools/hybrid_arxiv_marker.py 2603.19312v2 2603-19312v2
"""

import argparse
import re
import sys
import urllib.request
from datetime import date
from pathlib import Path

VAULT_ROOT = Path(__file__).resolve().parent.parent
LIB_DIR = VAULT_ROOT / "library" / "academic-reference"


def fetch_arxiv2md(arxiv_id: str) -> tuple[dict, str]:
    """Fetch arxiv2md output with frontmatter. Return (metadata_dict, body)."""
    url = (
        f"https://arxiv2md.org/api/markdown?url={arxiv_id}"
        "&remove_refs=false&remove_citations=false&remove_toc=false"
        "&frontmatter=true"
    )
    with urllib.request.urlopen(url, timeout=60) as r:
        raw = r.read().decode("utf-8")
    meta: dict = {}
    body = raw
    if raw.startswith("---"):
        end = raw.find("\n---", 4)
        if end > 0:
            fm_block = raw[4:end]
            for line in fm_block.splitlines():
                m = re.match(r'^(\w+):\s*"?(.*?)"?\s*$', line)
                if m:
                    meta[m.group(1)] = m.group(2)
            body = raw[end + 4 :].lstrip("\n")
    return meta, body


def extract_algorithm_blocks(marker_md: str) -> dict[str, str]:
    """Pull fenced code blocks from marker .md, keyed by algorithm number.

    Matches blocks near lines containing 'Algorithm N' markers in surrounding prose.
    """
    blocks: dict[str, str] = {}
    lines = marker_md.splitlines()
    # Find all fenced blocks and the nearest preceding 'Algorithm N' mention
    in_fence = False
    fence_start = None
    current = []
    fences: list[tuple[int, int, str]] = []  # (start, end, content)
    for i, line in enumerate(lines):
        if line.strip().startswith("```"):
            if in_fence:
                fences.append((fence_start, i, "\n".join(current)))
                in_fence = False
                current = []
            else:
                in_fence = True
                fence_start = i
        elif in_fence:
            current.append(line)

    # For each fence, look backward up to 30 lines for 'Algorithm N'
    for start, end, content in fences:
        for j in range(start - 1, max(0, start - 30), -1):
            m = re.search(r"Algorithm\s+(\d+)", lines[j])
            if m:
                blocks[m.group(1)] = content
                break
    return blocks


def build_figure_asset_map(marker_md: str, slug: str) -> dict[str, str]:
    """Map figure number -> local asset path from marker .md.

    Marker emits `![](slug-assets/_page_X_Figure_Y.jpeg)` followed shortly by
    `Figure N: caption...`. Build the mapping by walking that pattern.
    """
    mapping: dict[str, str] = {}
    img_pat = re.compile(rf"!\[\]\(({re.escape(slug)}-assets/[^\)]+)\)")
    fig_pat = re.compile(r"Figure\s+(\d+)\s*[:\.]")
    lines = marker_md.splitlines()
    pending_img: str | None = None
    for line in lines:
        im = img_pat.search(line)
        if im:
            pending_img = im.group(1)
            continue
        if pending_img:
            fm = fig_pat.search(line)
            if fm:
                num = fm.group(1)
                mapping.setdefault(num, pending_img)
                pending_img = None
    return mapping


def fix_math_wrapping(text: str) -> str:
    """arxiv2md emits `$$ $<latex>$ (N) $$` — collapse to `$$<latex>$$ (N)`.

    Also handles the simpler `$$ $<latex>$ $$` case without a tag, and
    `$$ $\\displaystyle<latex>$ $$` variants.
    """

    # Pattern: $$<ws>$<inner>$<ws>(TAG)<ws>$$  OR  $$<ws>$<inner>$<ws>$$
    # Use non-greedy inner match up to a terminating `$` that precedes closing `$$`.
    def replace(m: re.Match) -> str:
        inner = m.group(1).strip()
        tag = m.group(2)
        # drop leading \displaystyle if present (obsidian-friendly)
        inner = re.sub(r"^\\displaystyle\s*", "", inner)
        if tag:
            return f"$$\n{inner}\n$$ ({tag.strip()})"
        return f"$$\n{inner}\n$$"

    # Single-line form
    pattern_inline = re.compile(
        r"\$\$\s*\$(.+?)\$\s*(?:\(([^)]+)\))?\s*\$\$",
        re.DOTALL,
    )
    return pattern_inline.sub(replace, text)


def swap_figure_links(body: str, figure_map: dict[str, str]) -> str:
    """Replace arxiv2md's `Refer to caption: <url>` lines with local image embeds.

    arxiv2md pattern (two adjacent lines):
        Figure: Figure N: <caption>
        Refer to caption: <remote url>
    Rewrite to:
        ![](<marker local asset>)

        Figure N: <caption>

    If no marker mapping exists for that figure, leave the remote URL.
    """
    lines = body.splitlines()
    out: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        m_fig = re.match(r"^Figure:\s*Figure\s+(\d+)\s*[:\.]?\s*(.*)$", line)
        if m_fig and i + 1 < len(lines):
            next_line = lines[i + 1]
            m_cap = re.match(r"^Refer to caption:\s*(\S+)", next_line)
            if m_cap:
                num = m_fig.group(1)
                caption_rest = m_fig.group(2)
                local = figure_map.get(num)
                if local:
                    out.append(f"![]({local})")
                    out.append("")
                    out.append(f"**Figure {num}:** {caption_rest}".rstrip())
                else:
                    out.append(f"![]({m_cap.group(1)})")
                    out.append("")
                    out.append(f"**Figure {num}:** {caption_rest}".rstrip())
                i += 2
                continue
        out.append(line)
        i += 1
    return "\n".join(out)


def insert_algorithm_bodies(body: str, algo_blocks: dict[str, str]) -> str:
    """arxiv2md emits `Figure: Algorithm N <caption>` but no code body.
    Insert a fenced code block with marker's algorithm content right after.

    ar5iv renumbers algorithms (paper's Alg 1 can become `Algorithm 5`), so
    match positionally: the nth Algorithm marker in arxiv2md is paired with
    the nth algorithm extracted from marker (sorted by number).
    """
    marker_in_order = [algo_blocks[k] for k in sorted(algo_blocks, key=int)]
    lines = body.splitlines()
    out: list[str] = []
    marker_idx = 0
    for line in lines:
        m = re.match(
            r"^Figure:\s*(?:Figure\s+\d+:\s*)?Algorithm\s+(\d+)\.?\s*(.*)$", line
        )
        if m:
            rest = m.group(2)
            if marker_idx < len(marker_in_order):
                paper_num = marker_idx + 1
                out.append(f"**Algorithm {paper_num}.** {rest}".rstrip())
                out.append("")
                out.append("```")
                out.append(marker_in_order[marker_idx])
                out.append("```")
                marker_idx += 1
                continue
        out.append(line)
    return "\n".join(out)


def fix_bullet_artifacts(body: str) -> str:
    """Collapse arxiv2md's `- •\n<text>` pattern to `- <text>`."""
    return re.sub(r"^- •\n(\s*)(.+)$", r"- \2", body, flags=re.MULTILINE)


def fix_duplicate_math(body: str) -> str:
    """arxiv2md sometimes emits rendered+LaTeX for inline math adjacent.

    Known pattern: `48 × 48\times` (rendered then LaTeX). Collapse to `$48\times$`.
    Also handle N-arg variants like `200 × 200\times`.
    """

    def replace(m: re.Match) -> str:
        latex = m.group(2)
        return f"${latex}$"

    body = re.sub(r"(\S+\s+×\s+)(\d+\\times)", replace, body)
    # ∼N× rendered as "∼N ×" followed by "N\times" — drop the rendered half
    body = re.sub(
        r"∼\s*\d+\s*×\s+(\d+\\times)", lambda m: f"$\\sim {m.group(1)}$", body
    )
    return body


def fix_abstract_dup(body: str) -> str:
    """Remove leading `Abstract ` word right after `## Abstract` heading."""
    return re.sub(
        r"^(## Abstract\s*\n\s*\n)Abstract\s+",
        r"\1",
        body,
        count=1,
        flags=re.MULTILINE,
    )


def fix_math_underscore_escapes(body: str) -> str:
    """Inside math blocks, arxiv2md sometimes mis-escapes `_` as `*` or `\\_`.

    Restore proper LaTeX subscript syntax inside `$$...$$` and `$...$` blocks
    while preserving the delimiters themselves.
    """

    def _fix(inner: str) -> str:
        inner = inner.replace("\\_", "_")
        # '*{' → '_{' (subscript after a command/identifier)
        inner = re.sub(r"(?<![\\*])\*\{", "_{", inner)
        return inner

    # Display math $$...$$  (preserve the $$ on both ends)
    body = re.sub(
        r"(\$\$)(.+?)(\$\$)",
        lambda m: m.group(1) + _fix(m.group(2)) + m.group(3),
        body,
        flags=re.DOTALL,
    )
    # Inline math $...$ (not preceded/followed by another $)
    body = re.sub(
        r"(?<!\$)(\$)([^$\n]+?)(\$)(?!\$)",
        lambda m: m.group(1) + _fix(m.group(2)) + m.group(3),
        body,
    )
    return body


def strip_toc(body: str) -> str:
    """Drop the initial `## Contents` block arxiv2md prepends."""
    lines = body.splitlines()
    if not lines or not lines[0].strip().startswith("## Contents"):
        return body
    # Keep lines from first non-Contents heading onward
    out_start = 0
    for i, line in enumerate(lines[1:], start=1):
        if line.startswith("## ") or line.startswith("# "):
            out_start = i
            break
    return "\n".join(lines[out_start:])


def build_frontmatter(title: str, source_pdf: str) -> str:
    today = date.today().isoformat()
    return (
        "---\n"
        "tags:\n"
        "  - library\n"
        f'title: "{title}"\n'
        f'url: "https://arxiv.org/abs/{source_pdf.replace(".pdf", "").replace("-", ".")}"\n'
        "company: [personal]\n"
        "topics: []\n"
        f"created: {today}\n"
        "source_type: pdf\n"
        f'source_pdf: "{source_pdf}"\n'
        'devonthink_url: ""\n'
        "hydrated: true\n"
        f"hydrated_at: {today}\n"
        'hydrated_via: "arxiv2md + marker assets + claude-opus-4-7 polish"\n'
        "---\n\n"
    )


def extract_title(body: str, fallback: str) -> str:
    m = re.search(r"^# (.+)$", body, re.MULTILINE)
    if m:
        return m.group(1).strip().strip("*")
    m = re.search(r"^## (.+)$", body, re.MULTILINE)
    if m:
        return m.group(1).strip().strip("*")
    return fallback


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("arxiv_id", help="e.g. 2603.19312v2")
    ap.add_argument("slug", help="e.g. 2603-19312v2 (file slug used for the .md)")
    args = ap.parse_args()

    out_path = LIB_DIR / f"{args.slug}.md"
    if not out_path.exists():
        sys.exit(
            f"Expected existing marker .md at {out_path} (run process_pdfs.py first)"
        )

    marker_md = out_path.read_text(encoding="utf-8")

    print(f"Fetching arxiv2md for {args.arxiv_id} …", file=sys.stderr)
    meta, arxiv_body = fetch_arxiv2md(args.arxiv_id)
    print(
        f"  {len(arxiv_body):,} chars  meta keys: {sorted(meta.keys())}",
        file=sys.stderr,
    )

    print("Extracting algorithm blocks from marker .md …", file=sys.stderr)
    algo_blocks = extract_algorithm_blocks(marker_md)
    print(f"  found algorithms: {sorted(algo_blocks.keys())}", file=sys.stderr)

    print("Building figure→asset map …", file=sys.stderr)
    fig_map = build_figure_asset_map(marker_md, args.slug)
    print(f"  figures mapped: {len(fig_map)}", file=sys.stderr)

    print("Processing arxiv2md body …", file=sys.stderr)
    body = strip_toc(arxiv_body)
    body = fix_math_wrapping(body)
    body = insert_algorithm_bodies(body, algo_blocks)
    body = swap_figure_links(body, fig_map)
    body = fix_bullet_artifacts(body)
    body = fix_duplicate_math(body)
    body = fix_abstract_dup(body)
    body = fix_math_underscore_escapes(body)

    title = meta.get("title") or extract_title(body, args.slug)
    fm = build_frontmatter(title, f"{args.arxiv_id}.pdf")
    final = fm + "## Raw Content\n\n" + body.strip() + "\n"

    out_path.write_text(final, encoding="utf-8")
    print(
        f"Wrote {out_path.relative_to(VAULT_ROOT)} ({len(final):,} chars)",
        file=sys.stderr,
    )


if __name__ == "__main__":
    main()
