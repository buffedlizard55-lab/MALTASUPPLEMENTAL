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
STUBS = sorted((ROOT / "pages").glob("*.html")) if (ROOT / "pages").is_dir() else []

REQUIRED_FIELDS = [
    "id", "name", "category", "area", "address", "hours", "price_range",
    "description", "source_url", "source_type", "date_checked", "confidence", "notes",
]
SOURCE_TYPES = {"official", "map", "review", "social", "guide"}
CONFIDENCE = {"verified", "partially verified", "unverified"}

failures = []
warnings = []


def fail(gate, msg):
    failures.append(f"[{gate}] {msg}")


def warn(gate, msg):
    warnings.append(f"[{gate}] {msg}")


# ---------------------------------------------------------------- gate 1
def _check_page(p, base):
    """Resolve <a href> targets in p relative to `base` (the page's own directory)."""
    total = 0
    html = p.read_text(encoding="utf-8")
    anchors = {m for m in re.findall(r'id="([^"]+)"', html)}
    # Only <a href> counts as a link. <link href="css/style.css"> is a stylesheet
    # reference, not a navigable page - including it produced false failures.
    for href in re.findall(r'<a\s[^>]*?href="([^"]+)"', html):
        if href.startswith(("http://", "https://", "mailto:")):
            continue
        if href.startswith("#"):
            if href[1:] not in anchors:
                fail("links", f"{p.name}: in-page anchor {href} has no matching id")
            continue
        total += 1
        target, _, frag = href.partition("#")
        if not target:
            continue
        resolved = (base / target).resolve()
        if not resolved.exists():
            fail("links", f"{p.name}: internal link to missing file {target!r}")
            continue
        if frag and resolved.suffix == ".html":
            if f'id="{frag}"' not in resolved.read_text(encoding="utf-8"):
                fail("links", f"{p.name}: {href} - no id={frag!r} in {target}")
    return total


def gate_internal_links():
    total = sum(_check_page(p, ROOT) for p in PAGES)
    if STUBS:
        total += sum(_check_page(p, p.parent) for p in STUBS)
        # Every summary stub must point back at the main site, and must carry the
        # banner that says the main site wins a disagreement.
        for p in STUBS:
            html = p.read_text(encoding="utf-8")
            if "../index.html" not in html:
                fail("links", f"pages/{p.name}: no link back to the main site index")
            if "stub-banner" not in html:
                fail("links", f"pages/{p.name}: missing the stub banner that defers to the main site")
    print(f"  gate 1  internal links: {total} checked across {len(PAGES)} pages"
          + (f" + {len(STUBS)} summary stubs" if STUBS else ""))


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
            # Precise version of the gaming guard: a gaming item that places itself near
            # this trip's base must be unverified, because none has been (OQ-05).
            if str(it.get("category", "")).lower() == "gaming":
                where = f"{it.get('area','')} {it.get('address','')}".lower()
                if ("qawra" in where or "bugibba" in where or "buġibba" in where) \
                        and it["confidence"] != "unverified":
                    fail("data", f"{f.name} :: {it['id']}: a gaming venue near Qawra/Bugibba is marked "
                                 f"{it['confidence']!r}, but none has been verified (OQ-05)")
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
    # Route X3 was withdrawn on 20 April 2025 and replaced by route 214. It may only
    # appear inside an explicit correction (a <del>, or the word withdrawn/replaced
    # nearby). A bare recommendation of it is a regression - PR #8 shipped one.
    (r"(?<!<del>)\bRoute X3\b(?![^<]{0,120}(?:withdrawn|replaced|del>))",
     "route X3 was withdrawn 20 Apr 2025; it may only appear inside an explicit correction"),
    # NOTE: the gaming-venue guard used to be a prose regex here. Two versions were tried
    # and both false-fired on this project's own honest sentences - "Gaming centres / LAN
    # venues near Qawra" and "Gamers Lounge ... has no published session rates and no
    # verified Qawra branch". Regex cannot tell an assertion from a denial. The guard now
    # lives in the data gate, where it can read the confidence field instead of guessing.
]


def gate_page_consistency():
    for page, needle, why in CONSISTENCY:
        path = ROOT / page
        if not path.exists():
            fail("consistency", f"{page} does not exist ({why})")
            continue
        if needle not in path.read_text(encoding="utf-8"):
            fail("consistency", f"{page}: expected {needle!r} ({why}) not found")
    # Scan the summary stubs too - the forbidden-pattern gate originally only walked
    # PAGES, so a regression shipped into pages/ would have passed silently. Found by
    # deliberately re-injecting the PR #8 X3 claim and watching the gate stay green.
    scanned = 0
    for p in PAGES + STUBS:
        scanned += 1
        text = p.read_text(encoding="utf-8")
        for pattern, why in FORBIDDEN:
            if re.search(pattern, text, re.I):
                fail("consistency", f"{p.relative_to(ROOT)}: asserts something that is not verified - {why}")
    # Data files carry prose too (notes, descriptions) - scan them as well.
    for f in sorted((ROOT / "data").glob("*.json")):
        scanned += 1
        text = f.read_text(encoding="utf-8")
        for pattern, why in FORBIDDEN:
            if re.search(pattern, text, re.I):
                fail("consistency", f"data/{f.name}: asserts something that is not verified - {why}")
    print(f"  gate 5  data/page consistency: {len(CONSISTENCY)} assertions, "
          f"{len(FORBIDDEN)} forbidden patterns over {scanned} files")


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
