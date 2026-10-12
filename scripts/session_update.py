#!/usr/bin/env python3
"""Retired one-shot editor; intentionally performs no data updates.

The original 11 October 2026 patch encoded stale Eventbrite admission and
Route 186 return assumptions. Its logic was disabled before the current data
reconciliation. Current canonical records are maintained in ``data/*.json``;
source history and caveats live in ``docs/SOURCES.md`` and
``docs/OPEN_QUESTIONS.md``. Do not revive this script without fresh source
reads, a reviewed change plan, schema validation, and regression tests.
"""


def main() -> int:
    print(
        "session_update.py is retired and will not modify files. "
        "Edit the canonical data records with current evidence instead."
    )
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
