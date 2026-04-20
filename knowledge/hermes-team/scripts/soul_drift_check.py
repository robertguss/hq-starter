#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""
Diff each profile's live SOUL.md against its day-one snapshot.

Nyk's failure-mode-1 patch: any new responsibility must get a logged
approval or be reverted. This script surfaces drift — it does not fix it.

Usage: python knowledge/hermes-team/scripts/soul_drift_check.py
       (or run the file directly; it's executable)

Exit codes:
    0 — no drift across any profile
    1 — drift detected, or a required file is missing

No third-party dependencies. Python 3.8+.
"""

from __future__ import annotations

import difflib
import sys
from pathlib import Path

PROFILES = ("alan", "mira", "turing")

SCRIPT_DIR = Path(__file__).resolve().parent
VAULT_ROOT = SCRIPT_DIR.parent.parent.parent  # scripts/ -> hermes-team/ -> knowledge/ -> vault
PROFILES_DIR = Path.home() / ".hermes" / "profiles"


def check_profile(name: str) -> bool:
    """Return True if the profile is clean (no drift, both files present)."""
    live = PROFILES_DIR / name / "SOUL.md"
    baseline = VAULT_ROOT / "knowledge" / "hermes-team" / "profiles" / name / "SOUL.day-one.md"

    if not live.is_file():
        print(f"[{name}] MISSING LIVE: {live}")
        return False
    if not baseline.is_file():
        print(f"[{name}] MISSING BASELINE: {baseline}")
        return False

    live_text = live.read_text()
    baseline_text = baseline.read_text()

    if live_text == baseline_text:
        print(f"[{name}] no drift")
        return True

    print(f"[{name}] DRIFT DETECTED:")
    diff = difflib.unified_diff(
        baseline_text.splitlines(keepends=True),
        live_text.splitlines(keepends=True),
        fromfile=str(baseline),
        tofile=str(live),
    )
    for line in diff:
        sys.stdout.write("    " + line)
    if not live_text.endswith("\n"):
        sys.stdout.write("\n")
    return False


def main() -> int:
    results = [check_profile(p) for p in PROFILES]
    print()
    if all(results):
        print("All SOUL.md files match their day-one baseline.")
        return 0

    print("Drift detected. For each change, either:")
    print("  (a) Log an approval in the vault (commit message naming the responsibility added)")
    print("      and update the baseline:")
    print("      cp ~/.hermes/profiles/<name>/SOUL.md \\")
    print("         knowledge/hermes-team/profiles/<name>/SOUL.day-one.md")
    print("  (b) Revert the live file to match the baseline:")
    print("      cp knowledge/hermes-team/profiles/<name>/SOUL.day-one.md \\")
    print("         ~/.hermes/profiles/<name>/SOUL.md")
    return 1


if __name__ == "__main__":
    sys.exit(main())
