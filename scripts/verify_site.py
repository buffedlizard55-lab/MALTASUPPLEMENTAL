#!/usr/bin/env python3
"""Static integration checks for the Malta Trip Companion.

Run from the repository root with: python3 scripts/verify_site.py
No third-party packages or outbound network are required.
"""
from __future__ import annotations

import json
import re
import sys
from datetime import date, datetime, timedelta
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
PAGES_DIR = ROOT / "pages"
REQUIRED = {
    "id", "name", "category", "area", "address", "hours", "price_range",
    "description", "source_url", "source_type", "date_checked", "confidence", "notes",
}
SOURCE_TYPES = {"official", "map", "review", "social"}
CONFIDENCES = {"verified", "partially verified", "unverified"}
TOPICS = ("transport", "food", "activities", "everyday", "radio", "expenses")
ERRORS: list[str] = []


def fail(message: str) -> None:
    ERRORS.append(message)


class HTMLAudit(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.refs: list[tuple[str, str]] = []
        self.ids: set[str] = set()
        self.refresh: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if attributes.get("id"):
            self.ids.add(str(attributes["id"]))
        for attribute in ("href", "src", "action"):
            if attributes.get(attribute):
                self.refs.append((attribute, str(attributes[attribute])))
        if tag == "meta" and str(attributes.get("http-equiv", "")).lower() == "refresh":
            self.refresh.append(str(attributes.get("content", "")))


def markdown_ids(path: Path) -> set[str]:
    text = path.read_text(encoding="utf-8")
    return set(re.findall(r"^\|\s*([A-Z]+-\d{3})\s*\|", text, re.M))


def audit_data() -> int:
    source_text = (ROOT / "docs/SOURCES.md").read_text(encoding="utf-8")
    question_text = (ROOT / "docs/OPEN_QUESTIONS.md").read_text(encoding="utf-8")
    source_ids = markdown_ids(ROOT / "docs/SOURCES.md")
    question_ids = set(re.findall(r"^\|\s*(Q-\d{3})\s*\|", question_text, re.M))
    source_rows = [line.split("|") for line in source_text.splitlines() if line.startswith("| ")]
    source_urls = {parts[3].strip() for parts in source_rows if len(parts) > 3 and parts[3].strip().startswith("https://")}
    total = 0
    loaded: dict[str, dict] = {}

    for topic in TOPICS:
        path = DATA_DIR / f"{topic}.json"
        if not path.exists():
            fail(f"missing data file: {path.relative_to(ROOT)}")
            continue
        try:
            dataset = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            fail(f"{path.relative_to(ROOT)}: invalid JSON: {exc}")
            continue
        loaded[topic] = dataset
        records = dataset.get("records")
        if not isinstance(records, list):
            fail(f"{path.relative_to(ROOT)}: expected a records array")
            continue
        ids: set[str] = set()
        for index, record in enumerate(records, start=1):
            total += 1
            label = f"{path.relative_to(ROOT)} record {index}"
            if not isinstance(record, dict):
                fail(f"{label}: expected an object")
                continue
            missing = REQUIRED - record.keys()
            if missing:
                fail(f"{label}: missing fields {sorted(missing)}")
                continue
            record_id = str(record["id"])
            if record_id in ids:
                fail(f"{label}: duplicate id {record_id}")
            ids.add(record_id)
            if record["source_type"] not in SOURCE_TYPES:
                fail(f"{label}: source_type {record['source_type']!r} is not allowed")
            if record["confidence"] not in CONFIDENCES:
                fail(f"{label}: confidence {record['confidence']!r} is not allowed")
            try:
                date.fromisoformat(str(record["date_checked"]))
            except ValueError:
                fail(f"{label}: date_checked must be a real YYYY-MM-DD date")
            urls: list[str] = []
            if record["source_url"]:
                urls.append(str(record["source_url"]))
            for source in record.get("additional_sources", []) or []:
                if not isinstance(source, dict):
                    fail(f"{label}: additional_sources entries must be objects")
                    continue
                if source.get("url"):
                    urls.append(str(source["url"]))
                if source.get("type") and source["type"] not in SOURCE_TYPES:
                    fail(f"{label}: additional source type {source['type']!r} is not allowed")
            for url in urls:
                if urlsplit(url).scheme != "https":
                    fail(f"{label}: source must use HTTPS: {url}")
                if url not in source_urls:
                    fail(f"{label}: source URL absent from docs/SOURCES.md: {url}")
            encoded = json.dumps(record, ensure_ascii=False)
            for ref in re.findall(r"\bQ-\d{3}\b", encoded):
                if ref not in question_ids:
                    fail(f"{label}: unknown open-question reference {ref}")
            for ref in re.findall(r"\b[A-Z]+-\d{3}\b", encoded):
                if ref.startswith("Q-"):
                    continue
                if ref not in source_ids:
                    fail(f"{label}: unknown source-log reference {ref}")

        page = PAGES_DIR / f"{topic}.html"
        if not page.exists():
            fail(f"missing topic page: {page.relative_to(ROOT)}")
        elif topic != "expenses":
            expected = f'data-topic-data="../data/{topic}.json"'
            if expected not in page.read_text(encoding="utf-8"):
                fail(f"{page.relative_to(ROOT)} does not load {topic}.json")
        elif 'fetch("../data/expenses.json"' not in page.read_text(encoding="utf-8"):
            fail("pages/expenses.html does not load data/expenses.json")

    # Itinerary calendar and blank-starter arithmetic.
    expenses = loaded.get("expenses", {})
    expected_dates = [(date(2026, 10, 13) + timedelta(days=offset)).isoformat() for offset in range(7)]
    trip_dates = expenses.get("trip_dates", [])
    if [item.get("date") for item in trip_dates] != expected_dates:
        fail("expense planner dates must cover 13–19 October 2026 exactly")
    for item in trip_dates:
        try:
            expected_day = date.fromisoformat(item["date"]).strftime("%a")
            if not str(item.get("label", "")).startswith(expected_day):
                fail(f"weekday label does not match {item.get('date')}: {item.get('label')}")
        except (KeyError, ValueError):
            fail(f"invalid expense date entry: {item}")
    starter_count = len(expenses.get("trip_items", [])) + len(trip_dates) * len(expenses.get("daily_templates", []))
    if starter_count != 32:
        fail(f"expected 32 blank expense starter lines, got {starter_count}")

    option_ids: set[str] = set()
    for record in expenses.get("records", []):
        options = (record.get("details") or {}).get("budget_options", [])
        for option in options:
            option_id = str(option.get("id", ""))
            if not option_id or option_id in option_ids:
                fail(f"missing or duplicate price-option id: {option_id!r}")
            option_ids.add(option_id)
            if not isinstance(option.get("amount"), (int, float)) or option["amount"] < 0:
                fail(f"invalid published amount in {record.get('id')}: {option}")

    radio = loaded.get("radio", {}).get("records", [])
    expected_radio = {
        "radio-sportsworld-2026-10-17": ("15:06", "18:59"),
        "radio-sportsworld-2026-10-18": ("16:06", "19:59"),
    }
    for record in radio:
        if record.get("id") not in expected_radio:
            continue
        start, end = expected_radio[record["id"]]
        start_hour, start_minute = map(int, start.split(":"))
        calculated = datetime(2026, 10, 9, start_hour, start_minute) + timedelta(minutes=233)
        if calculated.strftime("%H:%M") != end:
            fail(f"radio duration arithmetic changed for {record['id']}")
        if start not in str(record.get("hours", "")) or end not in str(record.get("hours", "")):
            fail(f"radio display time does not match audit for {record['id']}")

    return total


def audit_local_links() -> int:
    html_paths = sorted(ROOT.glob("*.html")) + sorted(PAGES_DIR.glob("*.html"))
    parsed: dict[Path, HTMLAudit] = {}
    for path in html_paths:
        parser = HTMLAudit()
        parser.feed(path.read_text(encoding="utf-8"))
        parsed[path.resolve()] = parser

    count = 0
    for path in html_paths:
        parser = parsed[path.resolve()]
        refs = list(parser.refs)
        for content in parser.refresh:
            match = re.search(r"url\s*=\s*['\"]?([^'\";]+)", content, re.I)
            if match:
                refs.append(("refresh", match.group(1).strip()))
        for kind, ref in refs:
            url = urlsplit(ref)
            if url.scheme or url.netloc or ref.startswith(("mailto:", "tel:", "data:")):
                continue
            target = path.resolve() if not url.path else (path.parent / unquote(url.path)).resolve()
            count += 1
            if not target.exists():
                fail(f"{path.relative_to(ROOT)}: missing local {kind} target {ref}")
                continue
            if url.fragment and target.suffix.lower() == ".html":
                target_parser = parsed.get(target)
                if target_parser is None:
                    target_parser = HTMLAudit()
                    target_parser.feed(target.read_text(encoding="utf-8"))
                    parsed[target] = target_parser
                if unquote(url.fragment) not in target_parser.ids:
                    fail(f"{path.relative_to(ROOT)}: missing #{url.fragment} in {target.relative_to(ROOT)}")

    for path in ROOT.glob("*.html"):
        if path.name in {"index.html", "sources.html"}:
            continue
        text = path.read_text(encoding="utf-8")
        if 'http-equiv="refresh"' not in text or 'name="robots" content="noindex,follow"' not in text:
            fail(f"legacy root route {path.name} must be a noindex compatibility redirect")

    css = (ROOT / "css/style.css").read_text(encoding="utf-8")
    if "@media (max-width:" not in css:
        fail("responsive CSS breakpoint missing")
    js = (ROOT / "js/site.js").read_text(encoding="utf-8")
    if "aria-expanded" not in js or "nav-toggle" not in js:
        fail("mobile-navigation state handling missing from js/site.js")
    return count


def main() -> int:
    if not ROOT.exists():
        print("Repository root could not be located.", file=sys.stderr)
        return 1
    record_count = audit_data()
    link_count = audit_local_links()
    if ERRORS:
        print("FAIL — integration checks found problems:\n")
        for error in ERRORS:
            print(f"  - {error}")
        return 1
    source_count = len(markdown_ids(ROOT / "docs/SOURCES.md"))
    question_count = len(re.findall(r"^\|\s*(Q-\d{3})\s*\|", (ROOT / "docs/OPEN_QUESTIONS.md").read_text(encoding="utf-8"), re.M))
    print(f"PASS — {record_count} records; {source_count} source IDs; {question_count} open questions.")
    print("PASS — schema/enums, source and question references, trip dates, blank-line math and radio duration arithmetic.")
    print(f"PASS — {link_count} local links/assets/fragments across root and topic pages; responsive shell and legacy redirects checked.")
    print("External link liveness and visual rendering are not tested by this offline gate.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
