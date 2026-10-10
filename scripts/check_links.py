#!/usr/bin/env python3
"""Compatibility entry point for the repository's local integration gate.

Run `python3 scripts/check_links.py` or `python3 scripts/verify_site.py` from the
repository root. Both names execute the same portable, offline checks.
"""
from verify_site import main

if __name__ == "__main__":
    raise SystemExit(main())
