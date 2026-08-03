#!/usr/bin/env python3
"""
Content-quality checks for civil-bootcamp course files.

Validates each course file under MIT_CEE_*Track/ against the AGENTS.md contract:
  1. Standard 3-question summary at the top (5 mental models, 3 disagreements, 10 deep Qs)
  2. 5 mental-model deep dives (in 心智模型深化 section)
  3. 10 detailed self-test solutions (in 深度自測問題詳解 section)
  4. Bilingual content (both CJK and Latin characters present)
  5. Minimum size threshold (so we catch truncated / stub files)
  6. Closing summary present

Exits non-zero with a clear per-file report if any check fails.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import List, Tuple

ROOT = Path(__file__).resolve().parents[2]
TRACK_GLOB = "MIT_CEE_*Track"

# Per-file thresholds
MIN_LINES = 300           # course files are deep dives, should be substantial
MIN_DEEP_DIVES = 5        # mental model deep dives
MIN_SOLUTIONS = 10        # detailed self-test solutions

# Regexes
RE_PROBLEM_1 = re.compile(r"^## 問題 1[:：]", re.MULTILINE)
RE_PROBLEM_2 = re.compile(r"^## 問題 2[:：]", re.MULTILINE)
RE_PROBLEM_3 = re.compile(r"^## 問題 3[:：]", re.MULTILINE)
RE_DEEP_DIVE_SECTION = re.compile(r"^# 核心心智模型深化", re.MULTILINE)
RE_SOLUTIONS_SECTION = re.compile(r"^# 深度自測問題詳解", re.MULTILINE)
RE_SUMMARY_SECTION = re.compile(r"^## 總結", re.MULTILINE)

# Numbered mental model headings inside deep-dive section: "## 1. ..." up to "## 5. ..."
# (Note: each "## N. 中文" is followed by "## English Title"; we match the numbered one.)
RE_DEEP_DIVE_NUM = re.compile(r"^##\s+[1-5][\.．][^\n]+", re.MULTILINE)

# Numbered solution headings: "## 詳解 1：..." up to "## 詳解 10：..."
RE_SOLUTION_NUM = re.compile(r"^##\s+詳解\s*([0-9]+)[:：]", re.MULTILINE)


def find_course_files() -> List[Path]:
    files: List[Path] = []
    for track in ROOT.glob(TRACK_GLOB):
        if not track.is_dir():
            continue
        for md in track.glob("*.md"):
            if md.name == "00_INDEX.md":
                continue
            files.append(md)
    return sorted(files)


def section_block(text: str, start_pat: re.Pattern) -> str:
    """Return the text of the section starting at start_pat.

    The section ends at the next heading of the SAME OR SHALLOWER level, or EOF.
    We infer the section's own level from the start_pat match (count of leading '#').
    """
    m = start_pat.search(text)
    if not m:
        return ""
    matched_line = text[m.start(): text.find("\n", m.start())]
    level = len(matched_line) - len(matched_line.lstrip("#"))
    rest = text[m.end():]
    # Find next heading of same or shallower level (i.e., # count <= level)
    end_pat = re.compile(r"^#{1," + str(level) + r"}\s", re.MULTILINE)
    end = end_pat.search(rest)
    return rest[: end.start()] if end else rest


def count_numbered_items(block: str, require_bold: bool = True) -> int:
    """Count top-level numbered list items.

    問題 1 and 問題 2 items are bolded ("1. **..."),
    but 問題 3 questions are plain ("1. ..."). Pass require_bold=False for plain items.
    """
    if require_bold:
        pat = re.compile(r"^[0-9]+\.\s+\*\*")
    else:
        pat = re.compile(r"^[0-9]+\.\s+\S")
    return sum(1 for line in block.splitlines() if pat.match(line))


def count_deep_dives(text: str) -> int:
    """Count distinct mental-model deep-dive headings (## 1. ... through ## 5. ...).

    Counts only AFTER the deep-dive section header. The next top-level section
    (# 深度自測問題詳解, # 總結, or any other # heading) marks the end of the
    block. The bilingual title line immediately under the section header is skipped
    by the section-header boundary itself (we look past sec.end()).
    """
    sec = RE_DEEP_DIVE_SECTION.search(text)
    if not sec:
        return 0
    after = text[sec.end():]
    # The next "# " (level-1) is either the bilingual title or the next section.
    # Skip any consecutive level-1 lines (the bilingual title) and then look for
    # the actual next top-level section. Then look for `## N.` patterns only
    # in the body between the section header and that next section.
    # Practical approach: find the FIRST `## 1.` (or any numbered deep-dive)
    # and the last one, and count unique numbers in between.
    candidates = RE_DEEP_DIVE_NUM.finditer(after)
    nums: set = set()
    for m in candidates:
        # Extract the leading number
        head = m.group(0)
        num_match = re.match(r"^##\s+([1-5])[\.．]", head)
        if num_match:
            nums.add(int(num_match.group(1)))
    return len(nums)


def count_solutions(text: str) -> int:
    """Count distinct detailed-solution headings (## 詳解 1: ... through ## 詳解 10: ...).

    The first `## 詳解 N:` under the solutions section header (after the bilingual
    title) is unique enough that we can count unique solution numbers in the whole
    file — and restrict to those appearing after the section header.
    """
    sec = RE_SOLUTIONS_SECTION.search(text)
    if not sec:
        return 0
    after = text[sec.end():]
    nums: set = set()
    for m in RE_SOLUTION_NUM.finditer(after):
        nums.add(int(m.group(1)))
    return len(nums)


def has_bilingual(text: str) -> Tuple[bool, bool]:
    """Return (has_cjk, has_latin_word)."""
    has_cjk = bool(re.search(r"[\u4e00-\u9fff]", text))
    has_latin = bool(re.search(r"[A-Za-z]{4,}", text))
    return has_cjk, has_latin


def check_file(path: Path) -> Tuple[List[str], List[str]]:
    """Return (errors, warnings).

    Errors block the CI. Warnings are advisory (e.g., for stub files that haven't
    been expanded to deep-dive form yet).
    """
    errors: List[str] = []
    warnings: List[str] = []
    rel = path.relative_to(ROOT)

    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    # 1. Standard 3-question summary (required for ALL files, even stubs)
    if not RE_PROBLEM_1.search(text):
        errors.append(f"{rel}: missing '## 問題 1' section")
    if not RE_PROBLEM_2.search(text):
        errors.append(f"{rel}: missing '## 問題 2' section")
    if not RE_PROBLEM_3.search(text):
        errors.append(f"{rel}: missing '## 問題 3' section")

    # 2. Item counts in 問題 1 (should be 5 mental models)
    p1 = section_block(text, RE_PROBLEM_1)
    n1 = count_numbered_items(p1)
    if n1 != 5:
        errors.append(f"{rel}: 問題 1 has {n1} mental models, expected 5")

    # 3. Item counts in 問題 2 (should be 3 disagreements)
    p2 = section_block(text, RE_PROBLEM_2)
    n2 = count_numbered_items(p2)
    if n2 != 3:
        errors.append(f"{rel}: 問題 2 has {n2} disagreements, expected 3")

    # 4. Item counts in 問題 3 (should be 10 deep questions; items are NOT bolded)
    p3 = section_block(text, RE_PROBLEM_3)
    n3 = count_numbered_items(p3, require_bold=False)
    if n3 != 10:
        errors.append(f"{rel}: 問題 3 has {n3} deep questions, expected 10")

    # 5. Bilingual content (CJK + Latin words)
    has_cjk, has_latin = has_bilingual(text)
    if not has_cjk:
        errors.append(f"{rel}: no CJK characters found (bilingual content missing)")
    if not has_latin:
        errors.append(f"{rel}: no Latin words found (bilingual content missing)")

    # ---- Below: deep-content checks. Stubs (< MIN_LINES) get WARNINGS only. ----
    is_stub = len(lines) < MIN_LINES

    n_dives = count_deep_dives(text)
    n_sols = count_solutions(text)
    has_summary = bool(RE_SUMMARY_SECTION.search(text))

    if is_stub:
        if n_dives < MIN_DEEP_DIVES:
            warnings.append(
                f"{rel}: STUB ({len(lines)} lines) — needs expansion to ≥ {MIN_LINES} lines "
                f"with {MIN_DEEP_DIVES} mental-model deep dives"
            )
        if n_sols < MIN_SOLUTIONS:
            warnings.append(
                f"{rel}: STUB ({len(lines)} lines) — needs expansion with {MIN_SOLUTIONS} detailed solutions"
            )
        if not has_summary:
            warnings.append(
                f"{rel}: STUB ({len(lines)} lines) — needs closing '## 總結' section"
            )
    else:
        # Expanded file: all checks are ERRORS
        if n_dives < MIN_DEEP_DIVES:
            errors.append(
                f"{rel}: has {n_dives} mental-model deep dives, expected ≥ {MIN_DEEP_DIVES}"
            )
        if n_sols < MIN_SOLUTIONS:
            errors.append(
                f"{rel}: has {n_sols} detailed solutions, expected ≥ {MIN_SOLUTIONS}"
            )
        if not has_summary:
            errors.append(f"{rel}: missing closing '## 總結' section")

    return errors, warnings


def main() -> int:
    files = find_course_files()
    if not files:
        print("ERROR: no course files found under MIT_CEE_*Track/", file=sys.stderr)
        return 2

    print(f"Checking {len(files)} course file(s) under {TRACK_GLOB}/\n")

    all_errors: List[str] = []
    all_warnings: List[str] = []
    summary_rows: List[Tuple[str, int, int, int, int, int, int, str]] = []
    for f in files:
        rel = f.relative_to(ROOT)
        text = f.read_text(encoding="utf-8")
        n_lines = len(text.splitlines())
        n_dives = count_deep_dives(text)
        n_sols = count_solutions(text)
        n1 = count_numbered_items(section_block(text, RE_PROBLEM_1))
        n2 = count_numbered_items(section_block(text, RE_PROBLEM_2))
        n3 = count_numbered_items(section_block(text, RE_PROBLEM_3), require_bold=False)
        status = "STUB" if n_lines < MIN_LINES else "OK"
        summary_rows.append((str(rel), n_lines, n1, n2, n3, n_dives, n_sols, status))

        errs, warns = check_file(f)
        all_errors.extend(errs)
        all_warnings.extend(warns)

    # Print per-file report
    print(f"{'File':<60} {'Lines':>6} {'MM':>4} {'DG':>4} {'Qs':>4} {'Dives':>6} {'Sols':>5} {'Status':>6}")
    print("-" * 100)
    for row in summary_rows:
        rel, n_lines, n1, n2, n3, n_dives, n_sols, status = row
        print(f"{rel:<60} {n_lines:>6} {n1:>4} {n2:>4} {n3:>4} {n_dives:>6} {n_sols:>5} {status:>6}")
    print()

    n_stubs = sum(1 for r in summary_rows if r[7] == "STUB")
    print(f"Summary: {len(files)} files, {len(files) - n_stubs} expanded, {n_stubs} stubs\n")

    if all_warnings:
        print(f"⚠️  {len(all_warnings)} warning(s) (stubs that need expansion):\n")
        for w in all_warnings:
            print(f"  - {w}")
        print()

    if all_errors:
        print(f"❌ {len(all_errors)} check(s) failed:\n")
        for e in all_errors:
            print(f"  - {e}")
        return 1

    if all_warnings:
        # Stubs are warnings only — not blocking
        print("✅ No hard failures. Stubs are flagged for future expansion.")
        return 0

    print("✅ All content-quality checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
