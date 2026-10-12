#!/usr/bin/env python3
"""Check that every weekday written next to a 2026 October date matches the calendar.

Scans the topic data, pages and project docs for two phrasings:
  "Friday 16 October" / "Fri 16 Oct"  and  "16 October (Friday)".
A mismatch (for example "Friday 17 October", since 17 Oct 2026 is a Saturday)
fails the check. The check is deliberately narrow: ranges and bare dates are
not parsed, so it is a guard against common slips, not a full date audit.
"""

from __future__ import annotations

import datetime as dt
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
YEAR = 2026
MONTH = 10
DAY_NAMES = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
DAY_RE = r"(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday|Mon|Tue|Wed|Thu|Fri|Sat|Sun)"
MONTH_RE = r"(October|Oct)"
# "Friday 16 October", "Fri 16 Oct", "Friday, 16 October"
WEEKDAY_FIRST = re.compile(rf"\b{DAY_RE}\.?,?\s+(\d{{1,2}})(?:st|nd|rd|th)?\s+(?:of\s+)?{MONTH_RE}\b")
# "16 October (Friday)"
WEEKDAY_IN_PARENS = re.compile(rf"\b(\d{{1,2}})(?:st|nd|rd|th)?\s+(?:of\s+)?{MONTH_RE}\s+\({DAY_RE}\)")
# "17 October, Friday" / "18 October Friday" put the weekday after the date with no
# parentheses, which reads as a claim about the wrong day, so it is rejected outright.
AMBIGUOUS = re.compile(rf"\b(\d{{1,2}})(?:st|nd|rd|th)?\s+(?:of\s+)?{MONTH_RE},?\s+{DAY_RE}\b")


def weekday_index(name: str) -> int:
    lowered = name.lower()
    for index, full in enumerate(DAY_NAMES):
        if lowered == full or lowered == full[:3]:
            return index
    raise ValueError(name)


def scan_files() -> list[Path]:
    paths: list[Path] = []
    paths.extend(sorted((ROOT / "data").glob("*.json")))
    paths.extend(sorted(ROOT.glob("*.html")))
    paths.extend(sorted((ROOT / "docs").glob("*.md")))
    paths.extend(sorted((ROOT / "js").glob("*.js")))
    return [path for path in paths if path.is_file()]


def main() -> int:
    checked = 0
    problems: list[str] = []
    for path in scan_files():
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(ROOT)
        for match in WEEKDAY_FIRST.finditer(text):
            name, day = match.group(1), int(match.group(2))
            checked += 1
            problems_for(rel, match.group(0), name, day, problems)
        for match in WEEKDAY_IN_PARENS.finditer(text):
            day, name = int(match.group(1)), match.group(3)
            checked += 1
            problems_for(rel, match.group(0), name, day, problems)
        for match in AMBIGUOUS.finditer(text):
            problems.append(
                f"{rel}: ambiguous phrasing '{match.group(0)}' — write 'Friday 16 October' or '16 October (Friday)'"
            )
    if problems:
        for problem in problems:
            print(f"FAIL: {problem}", file=sys.stderr)
        return 1
    print(f"PASS: {checked} weekday/date pairs match the 2026 calendar; no ambiguous 'D Month, Weekday' phrasing.")
    return 0


def problems_for(rel: Path, snippet: str, name: str, day: int, problems: list[str]) -> None:
    try:
        actual = dt.date(YEAR, MONTH, day).weekday()
    except ValueError:
        problems.append(f"{rel}: '{snippet}' is not a valid October {YEAR} date")
        return
    if actual != weekday_index(name):
        problems.append(
            f"{rel}: '{snippet}' but {day} October {YEAR} is a {DAY_NAMES[actual].capitalize()}"
        )


if __name__ == "__main__":
    raise SystemExit(main())
