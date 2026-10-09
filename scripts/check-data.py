#!/usr/bin/env python3
"""Integration gate: validate data/*.json schema and check data->page consistency.

Usage: python3 scripts/check-data.py
Exit code 0 = pass. Prints a report either way.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

REQUIRED_FIELDS = [
    "id", "name", "category", "area", "address", "hours", "price_range",
    "description", "source_url", "source_type", "date_checked", "confidence", "notes",
]
SOURCE_TYPES = {"official", "map", "review", "social", "news", "community"}
CONFIDENCE = {"verified", "partially verified", "unverified"}

# Which HTML pages must mention every item id from each data file (prefix match on id).
DATA_TO_PAGES = {
    "transport.json": ["getting-around.html"],
    "food.json": ["restaurants.html"],
    "activities.json": ["activities.html", "landmarks.html"],
    "qawra.json": ["qawra.html"],
    "everyday.json": ["everyday.html"],
    "radio.json": ["radio.html"],
    "expenses.json": ["costs.html"],
}

# Pages that must exist and be linked from index.html
PAGES_LINKED_FROM_INDEX = [
    "index.html", "event.html", "restaurants.html", "landmarks.html", "activities.html",
    "qawra.html", "getting-around.html", "everyday.html", "radio.html", "costs.html",
    "logistics.html", "hotspawn.html", "sources.html",
]

def fail(msg):
    print(f"FAIL: {msg}")
    return 1

def main():
    errors = 0
    data_dir = ROOT / "data"
    json_files = sorted(p for p in data_dir.glob("*.json") if not p.name.startswith("_"))
    if not json_files:
        return fail("no data files found")

    index_html = (ROOT / "index.html").read_text(encoding="utf-8")

    for jf in json_files:
        try:
            payload = json.loads(jf.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            errors += fail(f"{jf.name}: invalid JSON ({e})")
            continue
        items = payload.get("items")
        if not isinstance(items, list):
            errors += fail(f"{jf.name}: missing items list")
            continue
        seen_ids = set()
        for i, item in enumerate(items):
            label = f"{jf.name}[{i}]"
            for f in REQUIRED_FIELDS:
                if f not in item:
                    errors += fail(f"{label}: missing field '{f}'")
            if item.get("source_type") not in SOURCE_TYPES:
                errors += fail(f"{label}: bad source_type {item.get('source_type')!r}")
            if item.get("confidence") not in CONFIDENCE:
                errors += fail(f"{label}: bad confidence {item.get('confidence')!r}")
            sid = item.get("id", "")
            if not re.fullmatch(r"[a-z0-9-]+", sid or ""):
                errors += fail(f"{label}: bad id {sid!r}")
            if sid in seen_ids:
                errors += fail(f"{label}: duplicate id {sid!r}")
            seen_ids.add(sid)
            url = item.get("source_url", "")
            if not re.match(r"https?://", url):
                errors += fail(f"{label}: source_url not a URL: {url!r}")
        # page coverage: every item id must appear in at least one of its mapped pages
        pages = DATA_TO_PAGES.get(jf.name, [])
        for page in pages:
            if not (ROOT / page).exists():
                errors += fail(f"{jf.name}: expected page {page} missing")
        texts = {p: (ROOT / p).read_text(encoding="utf-8") for p in pages if (ROOT / p).exists()}
        missing = [it["id"] for it in items
                   if not any(it["id"] in t for t in texts.values())]
        if missing:
            errors += fail(f"{jf.name}: ids not found in any of {pages}: {', '.join(missing[:10])}"
                           + (" …" if len(missing) > 10 else ""))
        print(f"OK schema: {jf.name} ({len(items)} items)")

    # internal link check across all html files
    html_files = sorted(ROOT.glob("*.html"))
    all_text = {p.name: p.read_text(encoding="utf-8") for p in html_files}
    for name, text in all_text.items():
        for href in re.findall(r'href="([^"]+)"', text):
            if href.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = href.split("#")[0]
            if target and not (ROOT / target).exists():
                errors += fail(f"{name}: broken internal link -> {href}")
        for src in re.findall(r'src="([^"]+)"', text):
            if src.startswith(("http://", "https://")):
                continue
            if not (ROOT / src).exists():
                errors += fail(f"{name}: broken src -> {src}")
    print(f"OK link-check: {len(html_files)} pages scanned")

    # nav consistency: every page listed in PAGES_LINKED_FROM_INDEX must exist and be in index nav
    for page in PAGES_LINKED_FROM_INDEX:
        if not (ROOT / page).exists():
            errors += fail(f"expected page missing: {page}")
        elif page not in index_html:
            errors += fail(f"index.html does not reference {page}")
    print("OK nav-check")

    if errors:
        print(f"\n{errors} problem(s) found")
        return 1
    print("\nALL CHECKS PASSED")
    return 0

if __name__ == "__main__":
    sys.exit(main())
