#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["loguru"]
# ///
"""
HQ vault PDF processor — inbox/ → library/ as hydrated markdown.

Current extractor: marker (via `marker_single` CLI).
This is a first-pass experimental script; iteration planned to compare
other extractors (docling, pymupdf4llm, etc.).

Usage:
  # One-time install of marker:
  uv tool install marker-pdf

  # Run with uv (auto-installs loguru via PEP 723 metadata):
  uv run .tools/process_pdfs.py [--limit N] [--dry-run] [--keep-pdf] [--dest DIR]
  # Or with plain python (install loguru yourself: `uv pip install loguru`):
  python .tools/process_pdfs.py ...

  # Higher accuracy with an LLM (tables, equations, inline math).
  # Marker reads API keys from CLI flags; this script promotes env vars
  # (GEMINI_API_KEY / ANTHROPIC_API_KEY / OPENAI_API_KEY) into those flags.
  GEMINI_API_KEY=... uv run .tools/process_pdfs.py --use-llm
  ANTHROPIC_API_KEY=... uv run .tools/process_pdfs.py --use-llm --llm-service anthropic

  # Local LLM via Ollama (vision-capable model required for marker hybrid mode):
  #   ollama pull qwen2.5vl:32b
  uv run .tools/process_pdfs.py --use-llm --llm-service ollama \\
      --ollama-model qwen2.5vl:32b
  # Recommended local vision models for M-series Macs with 64GB+ RAM:
  #   qwen2.5vl:32b   — strong on docs, ~22GB, balanced default
  #   qwen2.5vl:72b   — higher quality, ~50GB
  #   llama3.2-vision:11b — lighter/faster option
  #   minicpm-v:8b    — small and efficient
  #
  # Ollama Cloud: the local Ollama client transparently forwards `:cloud`-
  # tagged models to Ollama's servers after `ollama signin`. No config change
  # here — just pull and pass the tag:
  #   ollama signin
  #   ollama pull <model>:cloud
  #   uv run .tools/process_pdfs.py --use-llm --llm-service ollama \\
  #       --ollama-model <model>:cloud
  # Check available cloud models at ollama.com (vision-capable required).
  #
  # Providers: google (default, Gemini) | anthropic | openai | vertex | ollama | azure

Note on images: marker extracts figures to PNGs alongside its .md output.
This script currently captures only the markdown (image refs will be broken).
Image handling TBD — defer until we're happy with extractor quality.

Defaults:
  - Destination: library/academic-reference/
  - Processed PDFs move to inbox/_processed/ (override with --keep-pdf)
  - Idempotent: skips if a file with the same slug already exists in dest

Flags:
  --limit N         Stop after N PDFs
  --dry-run         Report planned actions; no writes
  --keep-pdf        Do not move PDFs out of inbox/
  --dest DIR        Override destination library folder
  --extractor       Extractor to use (default: marker). Reserved for future comparison.
  --use-llm         Pass marker's --use_llm flag (higher accuracy, needs a backend)
  --llm-service     Backend: google|anthropic|openai|vertex|ollama|azure
  --ollama-model    Ollama model tag (required if --llm-service ollama)
  --ollama-url      Ollama base URL (default: http://localhost:11434)
  --verbose, -v     Enable DEBUG-level logging
"""

import argparse
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from datetime import date
from pathlib import Path

from loguru import logger

VAULT_ROOT = Path(__file__).resolve().parent.parent
INBOX = VAULT_ROOT / "inbox"
PROCESSED = INBOX / "_processed"
DEFAULT_DEST = VAULT_ROOT / "library" / "academic-reference"

SUPPORTED_EXTRACTORS = {"marker"}

LLM_SERVICE_CLASSES = {
    "google": "marker.services.gemini.GoogleGeminiService",
    "vertex": "marker.services.vertex.GoogleVertexService",
    "ollama": "marker.services.ollama.OllamaService",
    "anthropic": "marker.services.claude.ClaudeService",
    "openai": "marker.services.openai.OpenAIService",
    "azure": "marker.services.azure_openai.AzureOpenAIService",
}

LLM_ENV_KEY_FLAGS = {
    "google": ("GEMINI_API_KEY", "--gemini_api_key"),
    "anthropic": ("ANTHROPIC_API_KEY", "--claude_api_key"),
    "openai": ("OPENAI_API_KEY", "--openai_api_key"),
}


def configure_logging(verbose: bool) -> None:
    logger.remove()
    logger.add(
        sys.stderr,
        level="DEBUG" if verbose else "INFO",
        format=(
            "<green>{time:HH:mm:ss}</green> "
            "<level>{level: <8}</level> "
            "<level>{message}</level>"
        ),
        colorize=True,
    )


def slugify(name: str) -> str:
    name = name.lower()
    name = re.sub(r"\.pdf$", "", name)
    name = re.sub(r"[^a-z0-9]+", "-", name)
    name = re.sub(r"-+", "-", name).strip("-")
    return name or "untitled"


def ensure_extractor_available(extractor: str) -> None:
    if extractor == "marker":
        if not shutil.which("marker_single"):
            logger.error("'marker_single' not found on PATH.")
            logger.error("Install with: uv tool install marker-pdf")
            sys.exit(2)
        return
    logger.error(f"Unknown extractor: {extractor}")
    sys.exit(2)


def build_marker_cmd(
    pdf_path: Path,
    work_dir: Path,
    use_llm: bool,
    llm_service: str | None,
    ollama_model: str | None,
    ollama_url: str | None,
) -> tuple[list[str], list[str]]:
    """Build the marker command. Returns (cmd, redacted_cmd_for_logging)."""
    cmd = [
        "marker_single",
        str(pdf_path),
        "--output_dir",
        str(work_dir),
        "--output_format",
        "markdown",
    ]
    redacted = list(cmd)
    if use_llm:
        cmd.append("--use_llm")
        redacted.append("--use_llm")
        service = llm_service or "google"
        cls = LLM_SERVICE_CLASSES.get(service)
        if cls:
            cmd.extend(["--llm_service", cls])
            redacted.extend(["--llm_service", cls])
        env_flag = LLM_ENV_KEY_FLAGS.get(service)
        if env_flag:
            env_name, flag = env_flag
            if os.environ.get(env_name):
                cmd.extend([flag, os.environ[env_name]])
                redacted.extend([flag, "***REDACTED***"])
        if service == "ollama":
            if ollama_model:
                cmd.extend(["--ollama_model", ollama_model])
                redacted.extend(["--ollama_model", ollama_model])
            if ollama_url:
                cmd.extend(["--ollama_base_url", ollama_url])
                redacted.extend(["--ollama_base_url", ollama_url])
    return cmd, redacted


def run_marker(
    pdf_path: Path,
    work_dir: Path,
    use_llm: bool = False,
    llm_service: str | None = None,
    ollama_model: str | None = None,
    ollama_url: str | None = None,
) -> Path:
    cmd, redacted = build_marker_cmd(
        pdf_path, work_dir, use_llm, llm_service, ollama_model, ollama_url
    )
    logger.debug(f"marker cmd: {' '.join(redacted)}")
    logger.info(f"→ Running marker on {pdf_path.name} (output streams below)")
    logger.info("─" * 60)

    t0 = time.monotonic()
    # Inherit stdout/stderr so marker's tqdm progress bars render live.
    result = subprocess.run(cmd)
    elapsed = time.monotonic() - t0

    logger.info("─" * 60)
    if result.returncode != 0:
        logger.error(
            f"marker_single exited with code {result.returncode} after {elapsed:.1f}s"
        )
        raise RuntimeError(f"marker_single failed (exit {result.returncode})")
    logger.success(f"marker finished in {elapsed:.1f}s")

    stem = pdf_path.stem
    candidate = work_dir / stem / f"{stem}.md"
    if candidate.exists():
        logger.debug(f"Found marker output: {candidate}")
        return candidate
    for md in work_dir.rglob("*.md"):
        logger.debug(f"Found marker output (fallback): {md}")
        return md
    raise RuntimeError(f"marker produced no .md in {work_dir}")


IMAGE_REF_PAT = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")


def copy_images_and_rewrite(
    body: str, md_src_dir: Path, assets_dest: Path, slug: str
) -> tuple[str, int]:
    """Copy marker's image sidecars into assets_dest and rewrite body refs
    to point at <slug>-assets/<filename>. HTTP(S) refs are left alone.
    Returns (new_body, num_images_copied).
    """
    refs = list(IMAGE_REF_PAT.finditer(body))
    local_filenames: set[str] = set()
    for m in refs:
        url = m.group(2).strip()
        if url.lower().startswith(("http://", "https://")):
            continue
        local_filenames.add(url.split("#", 1)[0].split("?", 1)[0])

    if not local_filenames:
        return body, 0

    assets_dest.mkdir(parents=True, exist_ok=True)
    copied = 0
    for filename in sorted(local_filenames):
        src = md_src_dir / filename
        if not src.exists():
            logger.warning(f"Image ref not found on disk: {filename}")
            continue
        shutil.copy2(src, assets_dest / filename)
        copied += 1

    def rewrite(m: re.Match) -> str:
        alt = m.group(1)
        url = m.group(2).strip()
        if url.lower().startswith(("http://", "https://")):
            return m.group(0)
        filename = url.split("#", 1)[0].split("?", 1)[0]
        return f"![{alt}]({slug}-assets/{filename})"

    return IMAGE_REF_PAT.sub(rewrite, body), copied


def extract_title(body: str, fallback: str) -> str:
    for line in body.splitlines():
        s = line.strip()
        if s.startswith("# "):
            title = s[2:].strip()
            for marker in ("**", "__", "*", "_"):
                while (
                    title.startswith(marker)
                    and title.endswith(marker)
                    and len(title) > 2 * len(marker)
                ):
                    title = title[len(marker) : -len(marker)].strip()
            return title
    return fallback


def build_frontmatter(*, title: str, source_pdf: str, via: str) -> str:
    today = date.today().isoformat()
    safe_title = title.replace('"', "'")
    return (
        "---\n"
        "tags:\n"
        "  - library\n"
        f'title: "{safe_title}"\n'
        'url: ""\n'
        "company: [personal]\n"
        "topics: []\n"
        f"created: {today}\n"
        "source_type: pdf\n"
        f'source_pdf: "{source_pdf}"\n'
        'devonthink_url: ""\n'
        "hydrated: true\n"
        f"hydrated_at: {today}\n"
        f"hydrated_via: {via}\n"
        "---\n\n"
    )


def process_pdf(
    pdf: Path,
    dest_dir: Path,
    extractor: str,
    keep_pdf: bool,
    dry_run: bool,
    use_llm: bool = False,
    llm_service: str | None = None,
    ollama_model: str | None = None,
    ollama_url: str | None = None,
) -> dict:
    slug = slugify(pdf.name)
    out_path = dest_dir / f"{slug}.md"
    rel_out = out_path.relative_to(VAULT_ROOT)
    info = {"pdf": pdf.name, "slug": slug, "out": str(rel_out)}

    size_mb = pdf.stat().st_size / (1024 * 1024)
    logger.info(f"PDF: {pdf.name} ({size_mb:.1f} MB) → {rel_out}")

    if out_path.exists():
        logger.warning(f"Skipping — output already exists at {rel_out}")
        info["status"] = "skipped_exists"
        return info

    if dry_run:
        logger.info("[dry-run] Would process this PDF")
        info["status"] = "would_process"
        return info

    with tempfile.TemporaryDirectory() as td:
        work = Path(td)
        logger.debug(f"Work dir: {work}")
        if extractor == "marker":
            md_path = run_marker(
                pdf,
                work,
                use_llm=use_llm,
                llm_service=llm_service,
                ollama_model=ollama_model,
                ollama_url=ollama_url,
            )
        else:
            raise RuntimeError(f"unknown extractor: {extractor}")
        body = md_path.read_text(encoding="utf-8").strip()
        logger.info(f"Extracted {len(body):,} chars of markdown")

        assets_dir = dest_dir / f"{slug}-assets"
        body, n_images = copy_images_and_rewrite(body, md_path.parent, assets_dir, slug)
        if n_images:
            logger.info(
                f"Copied {n_images} image(s) → {assets_dir.relative_to(VAULT_ROOT)}/"
            )

    title = extract_title(body, pdf.stem)
    logger.info(f"Title: {title}")

    via = extractor
    if use_llm:
        service = llm_service or "google"
        if service == "ollama" and ollama_model:
            via = f"{extractor}+llm-ollama-{ollama_model}"
        else:
            via = f"{extractor}+llm-{service}"
    fm = build_frontmatter(title=title, source_pdf=pdf.name, via=via)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(f"{fm}## Raw Content\n\n{body}\n", encoding="utf-8")
    logger.success(f"Wrote {rel_out}")

    if keep_pdf:
        logger.info(f"Kept original PDF at {pdf.relative_to(VAULT_ROOT)}")
        info["pdf_action"] = "kept"
    else:
        PROCESSED.mkdir(parents=True, exist_ok=True)
        target = PROCESSED / pdf.name
        shutil.move(str(pdf), str(target))
        logger.info(f"Moved PDF → {target.relative_to(VAULT_ROOT)}")
        info["pdf_action"] = f"moved → {target.relative_to(VAULT_ROOT)}"

    info["status"] = "processed"
    info["title"] = title
    return info


def main() -> None:
    p = argparse.ArgumentParser(
        description="Process PDFs from inbox/ into library markdown."
    )
    p.add_argument("--limit", type=int, default=0, help="Process at most N PDFs")
    p.add_argument("--dry-run", action="store_true")
    p.add_argument(
        "--keep-pdf",
        action="store_true",
        help="Do not move PDFs to inbox/_processed/",
    )
    p.add_argument(
        "--dest", default=str(DEFAULT_DEST), help="Destination library folder"
    )
    p.add_argument(
        "--extractor",
        default="marker",
        choices=sorted(SUPPORTED_EXTRACTORS),
        help="PDF-to-markdown extractor",
    )
    p.add_argument(
        "--use-llm",
        action="store_true",
        help="Use marker's --use_llm flag for higher accuracy (requires API key)",
    )
    p.add_argument(
        "--llm-service",
        choices=sorted(LLM_SERVICE_CLASSES.keys()),
        default=None,
        help="Marker LLM service (default: google/Gemini)",
    )
    p.add_argument(
        "--ollama-model",
        default=None,
        help="Ollama model tag (e.g. qwen2.5vl:32b, gemma4:31b-cloud). "
        "Required if --llm-service ollama.",
    )
    p.add_argument(
        "--ollama-url",
        default=None,
        help="Ollama base URL (default: http://localhost:11434)",
    )
    p.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Enable DEBUG-level logging",
    )
    args = p.parse_args()

    configure_logging(args.verbose)

    if args.use_llm and args.llm_service == "ollama" and not args.ollama_model:
        logger.error(
            "--llm-service ollama requires --ollama-model "
            "(e.g. qwen2.5vl:32b or gemma4:31b-cloud)"
        )
        sys.exit(2)

    dest = Path(args.dest).resolve()
    ensure_extractor_available(args.extractor)

    pdfs = sorted(INBOX.glob("*.pdf"))
    if not pdfs:
        logger.warning(f"No PDFs in {INBOX.relative_to(VAULT_ROOT)}/")
        return

    if args.limit:
        pdfs = pdfs[: args.limit]

    mode = args.extractor
    if args.use_llm:
        service = args.llm_service or "google"
        if service == "ollama" and args.ollama_model:
            mode = f"{args.extractor}+llm-ollama-{args.ollama_model}"
        else:
            mode = f"{args.extractor}+llm-{service}"

    logger.info(f"Extractor mode: {mode}")
    logger.info(f"Destination:    {dest.relative_to(VAULT_ROOT)}/")
    logger.info(f"Found {len(pdfs)} PDF(s) in {INBOX.relative_to(VAULT_ROOT)}/")

    t_total = time.monotonic()
    processed = skipped = errored = 0
    for i, pdf in enumerate(pdfs, start=1):
        logger.info("")
        logger.info(f"═══ [{i}/{len(pdfs)}] {pdf.name} ═══")
        try:
            info = process_pdf(
                pdf,
                dest,
                args.extractor,
                args.keep_pdf,
                args.dry_run,
                use_llm=args.use_llm,
                llm_service=args.llm_service,
                ollama_model=args.ollama_model,
                ollama_url=args.ollama_url,
            )
            if info["status"] == "processed":
                processed += 1
            elif info["status"] == "skipped_exists":
                skipped += 1
        except Exception as e:
            errored += 1
            logger.exception(f"Failed processing {pdf.name}: {e}")

    elapsed = time.monotonic() - t_total
    logger.info("")
    logger.info("═" * 60)
    logger.success(
        f"Done in {elapsed:.1f}s — {processed} processed, "
        f"{skipped} skipped, {errored} errored"
    )


if __name__ == "__main__":
    main()
