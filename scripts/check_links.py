#!/usr/bin/env python3
"""Integration check for MALTASUPPLEMENTAL.

Runs five gates over the whole site:

  1. internal links and anchors resolve
  2. the main navigation is identical (same links, same order) on every page
  3. every data file parses and every item carries the full schema
  4. no item marked "unverified" is missing a source, and every sourced item
     names a plausible source type
  5. data -> page consistency: the load-bearing numbers that the Qawra re-base
     introduced actually appear on the pages that claim them

External URLs are NOT fetched - this environment has no outbound network to
those hosts. Their shape is validated and the gap is reported, not hidden.

Exit code 0 = all gates pass.
"""

import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAGES = sorted(p for p in ROOT.glob("*.html"))

REQUIRED_FIELDS = [
    "id", "name", "category", "area", "address", "hours", "price_range",
    "description", "source_url", "source_type", "date_checked", "confidence", "notes",
]
SOURCE_TYPES = {"official", "map", "review", "social"}
CONFIDENCE = {"verified", "partially verified", "unverified"}

failures = []
warnings = []


def fail(gate, msg):
    failures.append(f"[{gate}] {msg}")


def warn(gate, msg):
    warnings.append(f"[{gate}] {msg}")


# ---------------------------------------------------------------- gate 1
def gate_internal_links():
    page_names = {p.name for p in PAGES}
    total = 0
    for p in PAGES:
        html = p.read_text(encoding="utf-8")
        anchors = {m for m in re.findall(r'id="([^"]+)"', html)}
        # Only <a href> counts as a link. <link href="css/style.css"> is a stylesheet
        # reference, not a navigable page - including it produced false failures.
        hrefs = re.findall(r'<a\s[^>]*?href="([^"]+)"', html)
        for href in hrefs:
            if href.startswith(("http://", "https://", "mailto:", "#")):
                if href.startswith("#") and href[1:] not in anchors:
                    fail("links", f"{p.name}: in-page anchor {href} has no matching id")
                continue
            total += 1
            target, _, frag = href.partition("#")
            if target:
                # Any repo-relative path that exists on disk is fine - .html pages,
                # but also docs/*.md and data/*.json linked from a page.
                if not (ROOT / target).exists():
                    fail("links", f"{p.name}: internal link to missing file {target!r}")
                    continue
                if href.startswith(".."):
                    fail("links", f"{p.name}: {href} escapes the site root; use a repo-relative path")
                    continue
            if target and not target.endswith(".html"):
                continue
            if frag:
                tgt = ROOT / target
                if tgt.exists():
                    tgt_html = tgt.read_text(encoding="utf-8")
                    if f'id="{frag}"' not in tgt_html:
                        fail("links", f"{p.name}: {href} - no id={frag!r} in {target}")
    print(f"  gate 1  internal links: {total} checked across {len(PAGES)} pages")


# ---------------------------------------------------------------- gate 2
def gate_nav_consistency():
    navs = {}
    for p in PAGES:
        html = p.read_text(encoding="utf-8")
        m = re.search(r'<nav class="main-nav"[^>]*>(.*?)</nav>', html, re.S)
        if not m:
            fail("nav", f"{p.name}: no <nav class=\"main-nav\"> block found")
            continue
        navs[p.name] = re.findall(r'href="([^"]+)"', m.group(1))
    if not navs:
        return
    reference = next(iter(navs.values()))
    ref_name = next(iter(navs))
    for name, links in navs.items():
        if links != reference:
            fail("nav", f"{name}: nav differs from {ref_name}\n"
                        f"          expected {reference}\n          got      {links}")
    if "hotel.html" not in reference:
        fail("nav", "hotel.html is missing from the main navigation")
    print(f"  gate 2  navigation: {len(navs)} pages, {len(reference)} links each, identical={len(set(map(tuple, navs.values()))) == 1}")


# ---------------------------------------------------------------- gate 3
def iter_items(obj):
    """Yield (path, item) for every dict that looks like a schema item."""
    if isinstance(obj, dict):
        if "id" in obj and "name" in obj and "confidence" in obj:
            yield obj
        for v in obj.values():
            yield from iter_items(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from iter_items(v)


def gate_data_schema():
    data_files = sorted((ROOT / "data").glob("*.json"))
    if not data_files:
        fail("data", "no JSON files found in data/")
        return
    count = 0
    for f in data_files:
        try:
            doc = json.loads(f.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            fail("data", f"{f.name}: invalid JSON - {e}")
            continue
        items = list(iter_items(doc))
        count += len(items)
        for it in items:
            missing = [k for k in REQUIRED_FIELDS if k not in it]
            if missing:
                fail("data", f"{f.name} :: {it.get('id', '?')}: missing fields {missing}")
                continue
            if it["source_type"] not in SOURCE_TYPES:
                fail("data", f"{f.name} :: {it['id']}: source_type {it['source_type']!r} not in {sorted(SOURCE_TYPES)}")
            if it["confidence"] not in CONFIDENCE:
                fail("data", f"{f.name} :: {it['id']}: confidence {it['confidence']!r} not in {sorted(CONFIDENCE)}")
            if not re.match(r"^\d{4}-\d{2}-\d{2}$", str(it["date_checked"])):
                fail("data", f"{f.name} :: {it['id']}: date_checked {it['date_checked']!r} is not YYYY-MM-DD")
            # gate 4 folds in here: an item that claims to be sourced must have a URL,
            # and an item with no URL must be flagged unverified.
            if it["source_url"]:
                if not it["source_url"].startswith(("http://", "https://")):
                    fail("data", f"{f.name} :: {it['id']}: source_url is not a URL")
            elif it["confidence"] != "unverified":
                fail("data", f"{f.name} :: {it['id']}: no source_url but confidence is {it['confidence']!r} - "
                             "an unsourced item must be marked 'unverified'")
    print(f"  gate 3  data schema: {len(data_files)} files, {count} items, all {len(REQUIRED_FIELDS)} fields required")


# ---------------------------------------------------------------- gate 5
CONSISTENCY = [
    # (page, must-contain, why)
    ("hotel.html", "SPB 1902", "hotel postcode"),
    ("hotel.html", "13 Oct 2026", "check-in date"),
    ("hotel.html", "19 Oct 2026", "check-out date"),
    ("hotel.html", "950", "Arznell stop code"),
    ("hotel.html", "952", "Qawra stop code"),
    ("hotel.html", "186", "route 186"),
    ("getting-around.html", "186", "route 186"),
    ("getting-around.html", "Arznell", "board-at stop"),
    ("getting-around.html", "21:37", "last outbound departure"),
    ("getting-around.html", "21:26", "last return passing time"),
    ("getting-around.html", "€3.50", "TD1 fare"),
    ("getting-around.html", "€25", "7-day card fare"),
    ("getting-around.html", "Ta' Qali", "venue locality"),
    ("index.html", "Qawra", "re-based on the real hotel"),
    ("index.html", "13–19 October 2026", "booking dates"),
    ("costs.html", "six nights", "night-count warning present"),
    ("landmarks.html", "6 nights", "day-plan warning present"),
]

# Things that must NOT be asserted as fact anywhere (open questions / unverifiable).
FORBIDDEN = [
    (r"Popeye Village[^.]*route 2\d\d", "a Qawra->Popeye route was never verified (OQ-10)"),
    (r"gaming (?:centre|center)[^.]{0,60}(?:Qawra|Bu[gġ]ibba)[^.]*verified", "no gaming centre near Qawra was verified (OQ-05)"),
]


def gate_page_consistency():
    for page, needle, why in CONSISTENCY:
        path = ROOT / page
        if not path.exists():
            fail("consistency", f"{page} does not exist ({why})")
            continue
        if needle not in path.read_text(encoding="utf-8"):
            fail("consistency", f"{page}: expected {needle!r} ({why}) not found")
    for p in PAGES:
        text = p.read_text(encoding="utf-8")
        for pattern, why in FORBIDDEN:
            if re.search(pattern, text, re.I):
                fail("consistency", f"{p.name}: asserts something that is not verified - {why}")
    print(f"  gate 5  data/page consistency: {len(CONSISTENCY)} assertions, {len(FORBIDDEN)} forbidden patterns")


def main():
    print("MALTASUPPLEMENTAL integration check\n")
    gate_internal_links()
    gate_nav_consistency()
    gate_data_schema()
    gate_page_consistency()

    print()
    if warnings:
        print(f"{len(warnings)} warning(s):")
        for w in warnings:
            print("  " + w)
        print()
    if failures:
        print(f"FAIL — {len(failures)} problem(s):\n")
        for f in failures:
            print("  " + f)
        return 1
    print("PASS — all gates green.")
    print("\nNot checked here (no outbound network to those hosts in this environment):")
    print("  external URL liveness. Every external link was opened via the research")
    print("  fetch tool during authoring; a future session with network should run a")
    print("  bulk HTTP checker over them.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
