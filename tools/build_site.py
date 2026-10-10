#!/usr/bin/env python3
"""Validate the structured topic data and build static, GitHub Pages-ready pages."""
from __future__ import annotations

import argparse
import html
import json
import re
import sys
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
PAGES_DIR = ROOT / "pages"
REQUIRED_ITEM_FIELDS = (
    "id", "name", "category", "area", "address", "hours", "price_range",
    "description", "source_url", "source_type", "date_checked", "confidence", "notes",
)
SOURCE_TYPES = {"official", "map", "review", "social"}
CONFIDENCE = {"verified", "partially verified", "unverified"}
NAV_ITEMS = (
    ("overview", "Overview", "../index.html"),
    ("transport", "Transport", "transport.html"),
    ("food", "Food & cafes", "food.html"),
    ("activities", "Activities", "activities.html"),
    ("everyday", "Everyday life", "everyday.html"),
    ("radio", "Radio & sports", "radio.html"),
    ("expenses", "Expense planner", "expenses.html"),
)


def e(value: object) -> str:
    return html.escape(str(value), quote=True)


def is_http_url(value: str) -> bool:
    try:
        parsed = urlparse(value)
    except ValueError:
        return False
    return parsed.scheme in {"https", "http"} and bool(parsed.netloc)


def validate_item(item: object, filename: Path, errors: list[str], seen: set[str]) -> None:
    if not isinstance(item, dict):
        errors.append(f"{filename}: item must be a JSON object")
        return
    for key in REQUIRED_ITEM_FIELDS:
        if key not in item:
            errors.append(f"{filename}: item missing required field {key!r}")
    if any(key not in item for key in REQUIRED_ITEM_FIELDS):
        return
    item_id = item["id"]
    if not isinstance(item_id, str) or not item_id.strip():
        errors.append(f"{filename}: item id must be a non-empty string")
    elif item_id in seen:
        errors.append(f"{filename}: duplicate item id {item_id!r}")
    else:
        seen.add(item_id)
    for key in REQUIRED_ITEM_FIELDS:
        if not isinstance(item[key], str) or not item[key].strip():
            errors.append(f"{filename}: {item_id!r} field {key!r} must be a non-empty string (use an explicit unknown value)")
    if item["source_type"] not in SOURCE_TYPES:
        errors.append(f"{filename}: {item_id!r} has invalid source_type {item['source_type']!r}")
    if item["confidence"] not in CONFIDENCE:
        errors.append(f"{filename}: {item_id!r} has invalid confidence {item['confidence']!r}")
    if not is_http_url(str(item["source_url"])):
        errors.append(f"{filename}: {item_id!r} source_url must be a valid http(s) URL")
    try:
        date.fromisoformat(str(item["date_checked"]))
    except ValueError:
        errors.append(f"{filename}: {item_id!r} date_checked must be YYYY-MM-DD")
    supporting = item.get("supporting_sources", [])
    if not isinstance(supporting, list):
        errors.append(f"{filename}: {item_id!r} supporting_sources must be a list")
    else:
        for source in supporting:
            if not isinstance(source, dict):
                errors.append(f"{filename}: {item_id!r} supporting source must be an object")
                continue
            for key in ("claim", "url", "source_type"):
                if key not in source or not str(source[key]).strip():
                    errors.append(f"{filename}: {item_id!r} supporting source missing {key!r}")
            if source.get("source_type") not in SOURCE_TYPES:
                errors.append(f"{filename}: {item_id!r} supporting source has invalid source_type")
            if source.get("url") and not is_http_url(str(source["url"])):
                errors.append(f"{filename}: {item_id!r} supporting source URL is not http(s)")


def validate_document(doc: object, filename: Path, errors: list[str]) -> None:
    if not isinstance(doc, dict):
        errors.append(f"{filename}: document must be a JSON object")
        return
    for key in ("topic", "title", "intro", "date_checked", "sections"):
        if key not in doc:
            errors.append(f"{filename}: document missing {key!r}")
    topic = doc.get("topic")
    if not isinstance(topic, str) or not re.fullmatch(r"[a-z0-9-]+", topic):
        errors.append(f"{filename}: topic must be a lower-case slug")
    if filename.stem != topic:
        errors.append(f"{filename}: filename must match topic {topic!r}")
    try:
        date.fromisoformat(str(doc.get("date_checked", "")))
    except ValueError:
        errors.append(f"{filename}: date_checked must be YYYY-MM-DD")
    sections = doc.get("sections")
    if not isinstance(sections, list) or not sections:
        errors.append(f"{filename}: sections must be a non-empty list")
        return
    section_ids: set[str] = set()
    item_ids: set[str] = set()
    for section in sections:
        if not isinstance(section, dict):
            errors.append(f"{filename}: section must be a JSON object")
            continue
        for key in ("id", "title", "items"):
            if key not in section:
                errors.append(f"{filename}: section missing {key!r}")
        section_id = section.get("id")
        if not isinstance(section_id, str) or not re.fullmatch(r"[a-z0-9-]+", section_id):
            errors.append(f"{filename}: section id must be a lower-case slug")
        elif section_id in section_ids:
            errors.append(f"{filename}: duplicate section id {section_id!r}")
        else:
            section_ids.add(section_id)
        items = section.get("items")
        if not isinstance(items, list):
            errors.append(f"{filename}: section items must be a list")
            continue
        for item in items:
            validate_item(item, filename, errors, item_ids)


def render_nav(active_topic: str) -> str:
    links = []
    for topic, label, target in NAV_ITEMS:
        if topic == "overview":
            href = "../index.html"
        else:
            href = target
        active = ' aria-current="page"' if topic == active_topic else ""
        links.append(f'<a href="{href}"{active}>{e(label)}</a>')
    links.append('<a href="../docs/SOURCES.md">Sources</a>')
    links.append('<a href="../docs/OPEN_QUESTIONS.md">Open questions</a>')
    return "\n        ".join(links)


def render_section(section: dict) -> str:
    items_html = []
    for item in section.get("items", []):
        confidence_class = {
            "verified": "status-verified",
            "partially verified": "status-partial",
            "unverified": "status-unverified",
        }.get(item["confidence"], "status-unverified")
        source_class = "source-" + item["source_type"]
        detail_rows = [
            ("Area", item["area"]),
            ("Address", item["address"]),
            ("Hours / schedule", item["hours"]),
            ("Price", item["price_range"]),
        ]
        details = "\n".join(
            f'<div class="detail"><dt>{label}</dt><dd>{e(value)}</dd></div>'
            for label, value in detail_rows
        )
        additional = []
        for source in item.get("supporting_sources", []):
            url = e(source["url"])
            label = e(source.get("label", source["claim"]))
            source_type = e(source["source_type"])
            claim = e(source["claim"])
            additional.append(
                f'<li><a href="{url}" rel="noopener noreferrer">{label}</a> '
                f'<span class="source-type">{source_type}</span><br><span class="source-claim">{claim}</span></li>'
            )
        supporting_html = ""
        if additional:
            supporting_html = '<details class="supporting"><summary>More evidence</summary><ul>' + "".join(additional) + "</ul></details>"
        evidence_html = f"\n  {supporting_html}" if supporting_html else ""
        note_html = f'<p class="item-note"><strong>Note:</strong> {e(item["notes"])}</p>' if item["notes"].strip() else ""
        items_html.append(f'''<article class="item-card" id="item-{e(item['id'])}">
  <div class="item-heading">
    <span class="category">{e(item['category'])}</span>
    <span class="confidence {confidence_class}">{e(item['confidence'])}</span>
  </div>
  <h3>{e(item['name'])}</h3>
  <p class="item-description">{e(item['description'])}</p>
  <dl class="details">{details}</dl>
  {note_html}
  <div class="item-source"><a href="{e(item['source_url'])}" rel="noopener noreferrer">Primary source</a>
    <span class="source-type {source_class}">{e(item['source_type'])}</span>
    <span class="checked">Checked {e(item['date_checked'])}</span>
  </div>{evidence_html}
</article>''')
    lead = f'<p class="section-lead">{e(section["lead"])}</p>' if section.get("lead") else ""
    return f'''<section class="content-section" id="{e(section['id'])}">
  <div class="section-title"><span class="section-index">{len(items_html):02d}</span><div><h2>{e(section['title'])}</h2>{lead}</div></div>
  <div class="item-grid">{''.join(items_html)}</div>
</section>'''


def render_page(doc: dict) -> str:
    topic = doc["topic"]
    notes = "".join(f'<li>{e(note)}</li>' for note in doc.get("notes", []))
    notes_section = f'<aside class="page-notes"><h2>Planning notes</h2><ul>{notes}</ul></aside>' if notes else ""
    sections = "\n".join(render_section(section) for section in doc["sections"])
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{e(doc['intro'])}">
  <meta name="theme-color" content="#102b3f">
  <title>{e(doc['title'])} · Malta trip guide</title>
  <link rel="stylesheet" href="../css/style.css">
</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>
  <header class="site-header">
    <div class="header-inner">
      <a class="brand" href="../index.html" aria-label="Malta Trip Companion home"><span class="brand-mark" aria-hidden="true">M</span><span>Malta Trip Companion<small>Qawra · 13–19 October 2026</small></span></a>
      <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="main-nav">Menu</button>
      <nav class="main-nav" id="main-nav" aria-label="Main navigation">
        {render_nav(topic)}
      </nav>
    </div>
  </header>
  <main class="page" id="main">
    <section class="hero hero-compact">
      <p class="eyebrow">{e(topic.replace('-', ' ').upper())} · RESEARCH CHECKED {e(doc['date_checked'])}</p>
      <h1>{e(doc['title'])}</h1>
      <p class="hero-copy">{e(doc['intro'])}</p>
    </section>
    {notes_section}
    {sections}
    <p class="data-notice">Each listing shows its evidence type, confidence, and checked date. Prices and schedules can change; confirm with the linked operator or venue before travel.</p>
  </main>
  <footer class="site-footer">
    <div class="footer-inner"><div><strong>Malta Trip Companion</strong><p>Planning reference only. Confirm time-sensitive details at source.</p></div><div class="footer-links"><a href="../index.html">Overview</a><a href="../docs/SOURCES.md">Sources log</a><a href="../docs/OPEN_QUESTIONS.md">Open questions</a></div></div>
    <div class="footer-bottom">Updated {e(doc['date_checked'])} · Static site; no personal itinerary data is collected.</div>
  </footer>
  <script src="../js/site.js" defer></script>
</body>
</html>
'''


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="validate JSON and generated pages without writing")
    parser.add_argument("topic", nargs="*", help="optional topic slugs to build (default: all data/*.json except schema)")
    args = parser.parse_args()
    files = sorted(p for p in DATA_DIR.glob("*.json") if p.name != "schema.json")
    if args.topic:
        wanted = set(args.topic)
        files = [p for p in files if p.stem in wanted]
        missing = wanted - {p.stem for p in files}
        if missing:
            print("No data file found for: " + ", ".join(sorted(missing)), file=sys.stderr)
            return 2
    errors: list[str] = []
    documents: list[dict] = []
    for filename in files:
        try:
            doc = json.loads(filename.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"{filename}: {exc}")
            continue
        validate_document(doc, filename, errors)
        if isinstance(doc, dict):
            documents.append(doc)
    if errors:
        for error in errors:
            print("ERROR: " + error, file=sys.stderr)
        return 1
    if not documents:
        print("No topic data files found.", file=sys.stderr)
        return 1
    for doc in documents:
        destination = PAGES_DIR / f"{doc['topic']}.html"
        output = render_page(doc)
        if args.check:
            if not destination.exists():
                errors.append(f"{destination}: generated page missing; run python tools/build_site.py")
            elif destination.read_text(encoding="utf-8") != output:
                errors.append(f"{destination}: does not match data; run python tools/build_site.py")
        else:
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_text(output, encoding="utf-8")
            print(f"Built {destination.relative_to(ROOT)}")
    if errors:
        for error in errors:
            print("ERROR: " + error, file=sys.stderr)
        return 1
    if args.check:
        print(f"Validated {len(documents)} topic data file(s) and generated page(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
