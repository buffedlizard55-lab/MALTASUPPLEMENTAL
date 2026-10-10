#!/usr/bin/env python3
"""Repeatable integration check for the Malta Field Guide.

Run from any directory with: python3 scripts/verify_site.py
This validates the local site and source log. It does not fetch external URLs or
replace the three factual/usability review passes.
"""
from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent.parent
REQUIRED_FIELDS = [
    "id", "name", "category", "area", "address", "hours", "price range",
    "description", "source_url", "source_type", "date_checked", "confidence", "notes",
]
SOURCE_TYPES = {"official", "map", "review", "social"}
CONFIDENCE = {"verified", "partially verified", "unverified"}
EXTERNAL_SCHEMES = {"http", "https", "mailto", "tel", "data", "javascript"}
failures: list[str] = []
notes: list[str] = []


def fail(message: str) -> None:
    failures.append(message)


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: list[str] = []
        self.links: list[tuple[str, str, str]] = []
        self.record_sources: list[tuple[str, str]] = []
        self.nav_stack: list[dict[str, object]] = []
        self.nav_links: list[str] = []
        self.aria_refs: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr = {key: (value or "") for key, value in attrs}
        if attr.get("id"):
            self.ids.append(attr["id"])
        if "href" in attr:
            self.links.append((attr["href"], attr.get("target", ""), attr.get("rel", "")))
        if "src" in attr:
            self.links.append((attr["src"], "", ""))
        if attr.get("data-record-source"):
            self.record_sources.append((attr["data-record-source"], attr.get("data-record-filter", "")))
        for key in ("aria-controls", "aria-labelledby", "aria-describedby", "aria-owns"):
            if attr.get(key):
                self.aria_refs.extend(attr[key].split())
        if tag == "nav" and "primary-nav" in attr.get("class", "").split():
            self.nav_stack.append({"links": []})
        elif tag == "a" and self.nav_stack:
            self.nav_stack[-1]["links"].append(attr.get("href", ""))

    def handle_endtag(self, tag: str) -> None:
        if tag == "nav" and self.nav_stack:
            self.nav_stack.pop()


def parse_page(path: Path) -> PageParser:
    parser = PageParser()
    parser.feed(path.read_text(encoding="utf-8"))
    parser.close()
    return parser


def record_urls(text: str) -> set[str]:
    found = set()
    for raw in re.findall(r"https?://[^\s<>\"']+", text):
        found.add(raw.rstrip(".,;:!?)\]}"))
    return found


# 1. JSON schema, enums, unique IDs, and claim-level source-log coverage.
data_by_file: dict[Path, list[dict[str, object]]] = {}
all_ids_by_file: dict[Path, set[str]] = {}
source_text = (ROOT / "docs/SOURCES.md").read_text(encoding="utf-8")
logged_urls = record_urls(source_text)
for file_path in sorted((ROOT / "data").glob("*.json")):
    try:
        records = json.loads(file_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"{file_path.relative_to(ROOT)}: cannot parse JSON: {exc}")
        continue
    if not isinstance(records, list):
        fail(f"{file_path.relative_to(ROOT)}: expected a top-level list of records")
        continue
    data_by_file[file_path.resolve()] = records
    ids: set[str] = set()
    for position, record in enumerate(records, 1):
        label = f"{file_path.relative_to(ROOT)} record #{position}"
        if not isinstance(record, dict):
            fail(f"{label}: expected an object")
            continue
        missing = [key for key in REQUIRED_FIELDS if key not in record]
        extra = [key for key in record if key not in REQUIRED_FIELDS]
        if missing or extra:
            fail(f"{label}: schema mismatch; missing={missing}, extra={extra}")
            continue
        record_id = str(record["id"])
        if record_id in ids:
            fail(f"{label}: duplicate id {record_id!r}")
        ids.add(record_id)
        if record["source_type"] not in SOURCE_TYPES:
            fail(f"{label} ({record_id}): unsupported source_type {record['source_type']!r}")
        if record["confidence"] not in CONFIDENCE:
            fail(f"{label} ({record_id}): unsupported confidence {record['confidence']!r}")
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(record["date_checked"])):
            fail(f"{label} ({record_id}): date_checked must be YYYY-MM-DD")
        if record["confidence"] != "verified" and not str(record["notes"]).strip():
            fail(f"{label} ({record_id}): non-verified records need explanatory notes")
        url = str(record["source_url"]).strip()
        if url and url not in logged_urls:
            fail(f"{label} ({record_id}): primary source URL missing from docs/SOURCES.md: {url}")
        if not url and record["confidence"] != "unverified":
            fail(f"{label} ({record_id}): only an unverified record may have no source URL")
        for note_url in record_urls(str(record["notes"])):
            if note_url not in logged_urls:
                fail(f"{label} ({record_id}): notes URL missing from docs/SOURCES.md: {note_url}")
    all_ids_by_file[file_path.resolve()] = ids

record_total = sum(len(records) for records in data_by_file.values())
notes.append(f"schema: {record_total} records across {len(data_by_file)} JSON files")

# 2. HTML links, page fragments, navigation parity, ARIA references and JSON filters.
html_files = sorted([*ROOT.glob("*.html"), *(ROOT / "pages").glob("*.html")])
parsers: dict[Path, PageParser] = {path.resolve(): parse_page(path) for path in html_files}
navs: dict[Path, list[str]] = {}
link_count = 0
filter_count = 0
for page in html_files:
    resolved_page = page.resolve()
    parser = parsers[resolved_page]
    duplicates = sorted({value for value in parser.ids if parser.ids.count(value) > 1})
    if duplicates:
        fail(f"{page.relative_to(ROOT)}: duplicate id(s): {', '.join(duplicates)}")
    ids_here = set(parser.ids)
    for ref in parser.aria_refs:
        if ref not in ids_here:
            fail(f"{page.relative_to(ROOT)}: ARIA reference {ref!r} has no matching id")
    if parser.nav_stack:
        fail(f"{page.relative_to(ROOT)}: unclosed primary navigation")
    # Reparse nav links using a lightweight scan so each page's relative paths can be normalized.
    nav_match = re.search(r'<nav\b[^>]*class=["\'][^"\']*\bprimary-nav\b[^"\']*["\'][^>]*>(.*?)</nav>',
                          page.read_text(encoding="utf-8"), re.S)
    if nav_match:
        raw_nav = re.findall(r'<a\b[^>]*href=["\']([^"\']+)["\']', nav_match.group(1), re.S)
        normalized = []
        for href in raw_nav:
            parts = urlsplit(href)
            target = (page.parent / unquote(parts.path)).resolve() if parts.path else resolved_page
            try:
                relative_target = target.relative_to(ROOT.resolve()).as_posix()
            except ValueError:
                relative_target = str(target)
            normalized.append(relative_target + (f"#{unquote(parts.fragment)}" if parts.fragment else ""))
        navs[resolved_page] = normalized

    for href, target_attr, rel in parser.links:
        if not href:
            continue
        parts = urlsplit(href)
        if parts.scheme.lower() in EXTERNAL_SCHEMES or href.startswith("//"):
            if target_attr == "_blank" and "noopener" not in rel.split():
                fail(f"{page.relative_to(ROOT)}: external _blank link lacks rel=noopener: {href}")
            continue
        target_path = (page.parent / unquote(parts.path)).resolve() if parts.path else resolved_page
        link_count += 1
        if not target_path.exists():
            fail(f"{page.relative_to(ROOT)}: broken local link/resource {href!r}")
            continue
        if parts.fragment and target_path.suffix.lower() == ".html":
            target_parser = parsers.get(target_path)
            if target_parser is None:
                try:
                    target_parser = parse_page(target_path)
                    parsers[target_path] = target_parser
                except (OSError, UnicodeDecodeError):
                    target_parser = None
            if target_parser and unquote(parts.fragment) not in target_parser.ids:
                fail(f"{page.relative_to(ROOT)}: fragment #{parts.fragment} does not exist in {target_path.relative_to(ROOT)}")

    for data_source, raw_filter in parser.record_sources:
        data_path = (page.parent / unquote(urlsplit(data_source).path)).resolve()
        records = data_by_file.get(data_path)
        if records is None:
            fail(f"{page.relative_to(ROOT)}: record source is not a checked data file: {data_source}")
            continue
        wanted = {item.strip() for item in raw_filter.split(",") if item.strip()}
        known = {str(record.get("id", "")) for record in records}
        missing = sorted(wanted - known)
        if missing:
            fail(f"{page.relative_to(ROOT)}: data filter references missing ID(s): {', '.join(missing)}")
        filter_count += len(wanted)

if navs:
    reference_page = next(iter(navs))
    reference_nav = navs[reference_page]
    for page, items in navs.items():
        if items != reference_nav:
            fail(f"{page.relative_to(ROOT)}: primary navigation differs from {reference_page.relative_to(ROOT)}")
    notes.append(f"navigation: identical on {len(navs)} pages")
notes.append(f"HTML: {len(html_files)} pages and {link_count} local links/resources checked")
notes.append(f"JSON page filters: {filter_count} record IDs checked")

# 3. Confirm the Sources page snapshot contains all logged source claims and open questions.
source_claim_count = 0
in_source_table = False
for line in source_text.splitlines():
    if line.startswith("|") and ("Claim supported" in line or "Evidence actually viewed" in line) and "URL" in line:
        in_source_table = True
        continue
    if line.startswith("|") and in_source_table and set(line.replace("|", "").strip()) <= {"-", ":", " "}:
        continue
    if line.startswith("|") and in_source_table:
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) >= 4:
            source_claim_count += len(record_urls(cells[1]))
        continue
    if in_source_table:
        in_source_table = False

question_text = (ROOT / "docs/OPEN_QUESTIONS.md").read_text(encoding="utf-8")
question_ids = re.findall(r"^\|\s*(OQ-\d+)\s*\|", question_text, re.M)
source_page = (ROOT / "pages/sources.html").read_text(encoding="utf-8")
source_page_count = len(re.findall(r'class="source-entry"', source_page))
question_page_ids = set(re.findall(r'id="(OQ-\d+)"', source_page))
missing_questions = sorted(set(question_ids) - question_page_ids)
if source_page_count != source_claim_count:
    fail(f"pages/sources.html embeds {source_page_count} source entries, but docs/SOURCES.md contains {source_claim_count} claim rows")
if missing_questions:
    fail(f"pages/sources.html is missing open-question ID(s): {', '.join(missing_questions)}")
notes.append(f"source snapshot: {source_page_count}/{source_claim_count} claims; {len(question_ids)} open questions")

for note in notes:
    print(f"  · {note}")
if failures:
    print(f"\nFAIL — {len(failures)} problem(s):")
    for message in failures:
        print(f"  ✗ {message}")
    sys.exit(1)
print("\nPASS — local integration checks green (external URL liveness and browser rendering are not checked).")
