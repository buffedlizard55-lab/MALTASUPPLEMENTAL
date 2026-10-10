#!/usr/bin/env python3
"""Dependency-free structural checks for the Malta Trip Guide."""

from __future__ import annotations

import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
REQUIRED_FIELDS = {
    "id",
    "name",
    "category",
    "area",
    "address",
    "hours",
    "price_range",
    "description",
    "source_url",
    "source_type",
    "date_checked",
    "confidence",
    "notes",
}
SOURCE_TYPES = {"official", "map", "review", "social"}
CONFIDENCE = {"verified", "partially verified", "unverified"}
EXPECTED_PAGES = {
    "data/transport.json": "getting-around.html",
    "data/food.json": "restaurants.html",
    "data/activities.json": "activities.html",
    "data/everyday.json": "everyday.html",
    "data/radio.json": "radio.html",
}


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.links: list[str] = []
        self.ids: set[str] = set()
        self.has_title = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if values.get("id"):
            self.ids.add(values["id"] or "")
        if tag == "title":
            self.has_title = True
        for key in ("href", "src"):
            value = values.get(key)
            if value is not None:
                self.links.append(value)

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.handle_starttag(tag, attrs)


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def ensure_inside_root(path: Path, label: str) -> Path:
    resolved = path.resolve()
    try:
        resolved.relative_to(ROOT.resolve())
    except ValueError:
        fail(f"{label} escapes the repository: {path}")
    return resolved


def validate_data() -> dict[str, dict]:
    files = sorted(DATA_DIR.glob("*.json"))
    if not files:
        fail("no data/*.json files found")

    datasets: dict[str, dict] = {}
    for file_path in files:
        try:
            data = json.loads(file_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            fail(f"{file_path.relative_to(ROOT)}: invalid JSON ({exc})")
        if not isinstance(data, dict) or not isinstance(data.get("records"), list):
            fail(f"{file_path.relative_to(ROOT)}: expected an object with a records array")
        for key in ("topic", "title", "last_updated", "intro"):
            if not isinstance(data.get(key), str) or not data[key].strip():
                fail(f"{file_path.relative_to(ROOT)}: missing or blank top-level {key}")
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", data["last_updated"]):
            fail(f"{file_path.relative_to(ROOT)}: last_updated must use YYYY-MM-DD")

        seen: set[str] = set()
        for index, record in enumerate(data["records"], start=1):
            label = f"{file_path.relative_to(ROOT)} record {index}"
            if not isinstance(record, dict):
                fail(f"{label}: record must be an object")
            missing = REQUIRED_FIELDS - record.keys()
            extra = record.keys() - REQUIRED_FIELDS
            if missing or extra:
                fail(f"{label}: schema mismatch; missing={sorted(missing)}, extra={sorted(extra)}")
            for field in REQUIRED_FIELDS:
                if not isinstance(record[field], str) or not record[field].strip():
                    fail(f"{label}: {field} must be a non-empty string")
            if record["id"] in seen:
                fail(f"{label}: duplicate id {record['id']!r}")
            seen.add(record["id"])
            if record["source_type"] not in SOURCE_TYPES:
                fail(f"{label}: invalid source_type {record['source_type']!r}")
            if record["confidence"] not in CONFIDENCE:
                fail(f"{label}: invalid confidence {record['confidence']!r}")
            if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", record["date_checked"]):
                fail(f"{label}: date_checked must use YYYY-MM-DD")
            parsed = urlsplit(record["source_url"])
            if parsed.scheme not in {"http", "https"} or not parsed.netloc:
                fail(f"{label}: source_url must be an absolute HTTP(S) URL")
        datasets[file_path.relative_to(ROOT).as_posix()] = data

    for data_path, page_path in EXPECTED_PAGES.items():
        page = ROOT / page_path
        if not page.is_file():
            fail(f"expected topic page is missing: {page_path}")
        html = page.read_text(encoding="utf-8")
        marker = f'data-topic-data="{data_path}"'
        if marker not in html:
            fail(f"{page_path} is not wired to {data_path}")

    expense_data = datasets.get("data/expenses.json")
    if expense_data is None:
        fail("data/expenses.json is missing")
    if len(expense_data["records"]) != 18:
        fail(f"expected 18 expense categories, found {len(expense_data['records'])}")
    costs_html = (ROOT / "costs.html").read_text(encoding="utf-8")
    if not re.search(r"fetch\([\"']data/expenses\.json[\"']\)", costs_html):
        fail("costs.html is not wired to data/expenses.json")

    return datasets


def local_target(page: Path, value: str) -> tuple[Path, str | None] | None:
    value = value.strip()
    if not value:
        return (page, None)
    parsed = urlsplit(value)
    if parsed.scheme or parsed.netloc or value.startswith("//"):
        return None
    fragment = unquote(parsed.fragment) if parsed.fragment else None
    target_text = unquote(parsed.path)
    if not target_text:
        return (page, fragment)
    if target_text.startswith("/"):
        target = ROOT / target_text.lstrip("/")
    else:
        target = page.parent / target_text
    target = ensure_inside_root(target, f"link in {page.relative_to(ROOT)}")
    if target.is_dir():
        target = target / "index.html"
    return target, fragment


def validate_html_links() -> tuple[int, int]:
    pages: dict[Path, LinkParser] = {}
    for page in sorted(ROOT.glob("*.html")):
        parser = LinkParser()
        try:
            parser.feed(page.read_text(encoding="utf-8"))
        except (OSError, UnicodeDecodeError) as exc:
            fail(f"cannot read {page.name}: {exc}")
        if not parser.has_title:
            fail(f"{page.name} is missing a <title>")
        pages[page.resolve()] = parser

    checked = 0
    for page, parser in pages.items():
        for value in parser.links:
            checked += 1
            if value == "#":
                fail(f"empty placeholder link in {page.relative_to(ROOT)}")
            target_info = local_target(page, value)
            if target_info is None:
                continue
            target, fragment = target_info
            if not target.is_file():
                fail(f"broken local link in {page.relative_to(ROOT)}: {value!r}")
            if fragment:
                target_parser = pages.get(target.resolve())
                if target_parser is None:
                    target_parser = LinkParser()
                    target_parser.feed(target.read_text(encoding="utf-8"))
                if fragment not in target_parser.ids:
                    fail(f"missing local fragment in {page.relative_to(ROOT)}: {value!r}")

    # Check any local assets referenced through CSS url(...).
    css_files = sorted((ROOT / "css").glob("*.css"))
    for css_path in css_files:
        css = css_path.read_text(encoding="utf-8")
        for raw in re.findall(r"url\(\s*['\"]?([^'\")]+)", css, flags=re.IGNORECASE):
            value = raw.strip()
            if not value or value.startswith("data:") or value.startswith("#"):
                continue
            parsed = urlsplit(value)
            if parsed.scheme or parsed.netloc:
                continue
            target = ensure_inside_root(css_path.parent / unquote(parsed.path), f"CSS asset in {css_path.relative_to(ROOT)}")
            if not target.is_file():
                fail(f"missing CSS asset in {css_path.relative_to(ROOT)}: {value!r}")

    return len(pages), checked


def validate_navigation() -> int:
    source = (ROOT / "js/site.js").read_text(encoding="utf-8")
    entries = re.findall(r'\["([a-z0-9-]+\.html)",\s*"[^"\\]*(?:\\.[^"\\]*)*"\]', source)
    if not entries:
        fail("could not read any shared navigation destinations in js/site.js")
    for page in entries:
        if not (ROOT / page).is_file():
            fail(f"navigation destination does not exist: {page}")
    return len(entries)


def main() -> None:
    datasets = validate_data()
    page_count, link_count = validate_html_links()
    nav_count = validate_navigation()
    records = sum(len(data["records"]) for data in datasets.values())
    print(
        "PASS: "
        f"{len(datasets)} JSON files / {records} schema-valid records; "
        f"{page_count} HTML pages / {link_count} link attributes checked; "
        f"{nav_count} shared navigation destinations; 18 expense rows wired."
    )


if __name__ == "__main__":
    main()
