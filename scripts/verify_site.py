#!/usr/bin/env python3
"""MALTASUPPLEMENTAL — integration verification gate.

Checks (run from repo root:  python3 scripts/verify_site.py):
  1. data/*.json parse and every item carries the schema fields with valid enums.
  2. Data <-> page consistency: every data item's name appears on its mapped page(s).
  3. Internal links: every relative href/src in *.html resolves to a file on disk;
     every #anchor resolves to an id in the target page.
  4. HTML tag balance for the container/structural tags (html.parser based).
  5. Source-log coverage: every external source_url in data/*.json appears in
     docs/SOURCES.md.

Exit code 0 = all checks pass; 1 = failures listed on stdout.
"""
import html as html_lib
import json
import os
import re
import sys
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# topic -> pages that must mention every item's name.
# "trip" (data/trip.json) and "venues" (data/venues.json) are the parallel Qawra
# re-base session's reference datasets: they are schema-checked here and their
# load-bearing facts are enforced by scripts/check_links.py gate 5 (hotel.html,
# getting-around.html, index.html, costs.html, landmarks.html). They are not
# page-mirrored by this gate because their primary page is hotel.html, which the
# parallel session owns.
TOPIC_PAGES = {
    "transport": ["getting-around.html"],
    "food": ["restaurants.html"],
    "activities": ["activities.html", "landmarks.html", "qawra.html"],
    "everyday": ["everyday.html", "logistics.html"],
    "radio": ["radio.html"],
    "expenses": ["costs.html"],
}
REFERENCE_TOPICS = {"trip", "venues"}

REQUIRED_FIELDS = ["id", "name", "category", "area", "address", "hours", "price_range",
                   "description", "source_url", "source_type", "date_checked",
                   "confidence", "notes"]
ENUM_SOURCE_TYPE = {"official", "map", "review", "social", "guide"}
ENUM_CONFIDENCE = {"verified", "partially verified", "unverified"}

VOID_TAGS = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link",
             "meta", "param", "source", "track", "wbr"}
CHECK_TAGS = {"html", "head", "body", "header", "footer", "main", "nav", "section",
              "div", "span", "a", "p", "ul", "ol", "li", "table", "thead", "tbody",
              "tfoot", "tr", "td", "th", "h1", "h2", "h3", "h4", "h5", "h6",
              "button", "script", "style", "title", "small", "em", "strong", "form"}

failures = []
notes = []


def fail(msg):
    failures.append(msg)


def norm(s):
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def page_text(page_html):
    """Strip tags/scripts/styles and unescape entities so data names match across inline markup."""
    txt = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", page_html)
    txt = re.sub(r"(?s)<[^>]+>", " ", txt)
    txt = html_lib.unescape(txt)
    return norm(txt)


def read(path):
    with open(os.path.join(ROOT, path), encoding="utf-8") as fh:
        return fh.read()


def iter_items(obj):
    """Yield every dict that looks like a schema item (id+name+confidence),
    wherever it sits in the file — handles both `items` arrays and named sections."""
    if isinstance(obj, dict):
        if "id" in obj and "name" in obj and "confidence" in obj:
            yield obj
        for v in obj.values():
            yield from iter_items(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from iter_items(v)


# ---------------------------------------------------------------- 1. data files
data_items = {}   # topic -> list of items
for fname in sorted(os.listdir(os.path.join(ROOT, "data"))):
    if not fname.endswith(".json"):
        continue
    topic = fname[:-5]
    try:
        blob = json.loads(read(os.path.join("data", fname)))
    except Exception as exc:  # noqa: BLE001
        fail(f"data/{fname}: JSON parse error: {exc}")
        continue
    if "items" in blob:
        items = blob["items"]
    else:
        # named-section files (e.g. data/trip.json, data/venues.json): collect every
        # schema item wherever it sits — same rule as scripts/check_links.py gate 3.
        items = list(iter_items(blob))
    data_items[topic] = items
    for i, item in enumerate(items):
        missing = [f for f in REQUIRED_FIELDS if f not in item]
        if missing:
            fail(f"data/{fname} item #{i} ({item.get('id', '?')}): missing fields {missing}")
            continue
        if item["source_type"] not in ENUM_SOURCE_TYPE:
            fail(f"data/{fname} item {item['id']}: bad source_type {item['source_type']!r}")
        if item["confidence"] not in ENUM_CONFIDENCE:
            fail(f"data/{fname} item {item['id']}: bad confidence {item['confidence']!r}")
        if item["confidence"] != "verified" and not item["notes"].strip():
            fail(f"data/{fname} item {item['id']}: non-verified item has empty notes")
        if item["confidence"] == "unverified":
            notes.append(f"data/{fname} item {item['id']} is 'unverified' — must be in docs/OPEN_QUESTIONS.md")
notes.append(f"data files: {sum(len(v) for v in data_items.values())} items across {len(data_items)} topics")

# ------------------------------------------------- 2. data <-> page consistency
# Rule: every data item must appear (by name) on at least one of its topic's pages.
for topic, items in data_items.items():
    pages = TOPIC_PAGES.get(topic)
    if not pages:
        if topic in REFERENCE_TOPICS:
            notes.append(f"data/{topic}.json: reference dataset ({len(items)} items) — schema-checked only; page consistency enforced by scripts/check_links.py gate 5")
            continue
        fail(f"data/{topic}.json: no page mapping in verify_site.py TOPIC_PAGES")
        continue
    page_norms = {}
    for page in pages:
        try:
            page_norms[page] = page_text(read(page))
        except FileNotFoundError:
            fail(f"data/{topic}.json maps to {page}, which does not exist")
    for item in items:
        needle = norm(item["name"])
        if not any(needle in pn for pn in page_norms.values()):
            fail(f"data/{topic}.json item {item['id']} ({item['name']!r}) not found on any of {pages}")

# --------------------------------------------------------- 3. internal links
class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links = []      # (href, lineno)
        self.ids = set()
        self.stack = []
        self.errors = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag not in VOID_TAGS:
            if tag in CHECK_TAGS:
                self.stack.append((tag, self.getpos()[0]))
        if "id" in attrs:
            self.ids.add(attrs["id"])
        if "href" in attrs:
            self.links.append((attrs["href"], self.getpos()[0]))
        if "src" in attrs:
            self.links.append((attrs["src"], self.getpos()[0]))

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag in self.stack and tag not in VOID_TAGS:
            # startendtag (self-closing) should not stay on the stack
            if self.stack and self.stack[-1][0] == tag:
                self.stack.pop()

    def handle_endtag(self, tag):
        if tag in VOID_TAGS:
            return
        if tag not in CHECK_TAGS:
            return
        if not self.stack:
            self.errors.append(f"line {self.getpos()[0]}: closing </{tag}> with empty stack")
            return
        if self.stack[-1][0] == tag:
            self.stack.pop()
            return
        # search up the stack (tolerate nothing — report mismatch)
        names = [t for t, _ in self.stack]
        if tag in names:
            idx = len(names) - 1 - names[::-1].index(tag)
            unclosed = self.stack[idx + 1:]
            fail(f"tag balance: </{tag}> at line {self.getpos()[0]} closes over unclosed {unclosed}")
            del self.stack[idx:]
        else:
            self.errors.append(f"line {self.getpos()[0]}: stray closing </{tag}>")


html_pages = sorted(f for f in os.listdir(ROOT) if f.endswith(".html"))
page_ids = {}
for page in html_pages:
    parser = LinkParser()
    parser.feed(read(page))
    parser.close()
    for tag, line in parser.stack:
        fail(f"{page}: unclosed <{tag}> opened at line {line}")
    for err in parser.errors:
        fail(f"{page}: {err}")
    page_ids[page] = parser.ids
    for href, line in parser.links:
        if href.startswith(("http://", "https://", "#", "mailto:", "data:", "//")):
            if href.startswith("#") and href[1:] not in parser.ids:
                fail(f"{page}:{line}: anchor {href} has no matching id in {page}")
            continue
        target = href.split("#", 1)[0]
        anchor = href.split("#", 1)[1] if "#" in href else None
        if not target:
            continue
        if not os.path.exists(os.path.join(ROOT, target)):
            fail(f"{page}:{line}: broken internal link {href}")
        elif anchor and target in page_ids or (anchor and os.path.exists(os.path.join(ROOT, target))):
            tgt_ids = page_ids.get(target)
            if tgt_ids is None:
                tp = LinkParser()
                tp.feed(read(target))
                tgt_ids = tp.ids
                page_ids[target] = tgt_ids
            if anchor not in tgt_ids:
                fail(f"{page}:{line}: anchor #{anchor} not found in {target}")
notes.append(f"internal links: {len(html_pages)} pages scanned")

# ------------------------------------------- 5. source-log coverage (data files)
sources_md = read("docs/SOURCES.md") if os.path.exists(os.path.join(ROOT, "docs/SOURCES.md")) else ""
for topic, items in data_items.items():
    for item in items:
        url = item.get("source_url", "")
        if url.startswith("http") and url not in sources_md:
            fail(f"data/{topic}.json item {item['id']}: source_url not logged in docs/SOURCES.md: {url}")

# ------------------------------------------------------------------------ report
for n in notes:
    print(f"  · {n}")
if failures:
    print(f"\nFAIL ({len(failures)} problem(s)):")
    for f in failures:
        print(f"  ✗ {f}")
    sys.exit(1)
print("\nPASS — all verification gates green.")
