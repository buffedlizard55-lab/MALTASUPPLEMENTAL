#!/usr/bin/env python3
"""Rebuild the embedded source/question snapshot in pages/sources.html.

Run from anywhere with: python3 scripts/build_sources_page.py
The surrounding report, navigation and page design remain hand-maintained.
"""
from __future__ import annotations

import html
import re
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parent.parent
PAGE = ROOT / "pages/sources.html"
SOURCES = ROOT / "docs/SOURCES.md"
QUESTIONS = ROOT / "docs/OPEN_QUESTIONS.md"


def inline_markdown(value: str) -> str:
    value = html.escape(value.strip(), quote=False)
    value = re.sub(r"`([^`]+)`", r"<code>\1</code>", value)
    value = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", value)
    value = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", value)
    return value


def urls_in_cell(value: str) -> list[str]:
    urls = re.findall(r"https?://[^\s<>\"']+", value)
    return [url.rstrip(".,;:!?)\]}") for url in urls]


def read_source_groups() -> list[tuple[str, list[tuple[str, str, str, str]]]]:
    groups: list[tuple[str, list[tuple[str, str, str, str]]]] = []
    current_name: str | None = None
    current_entries: list[tuple[str, str, str, str]] = []
    in_source_table = False

    def flush() -> None:
        nonlocal current_name, current_entries
        if current_name and current_entries:
            groups.append((current_name, current_entries))
        current_name = None
        current_entries = []

    for line in SOURCES.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            flush()
            heading = line[3:].strip()
            if heading.startswith("Seeded during") or heading.startswith("Workstream "):
                current_name = heading
            in_source_table = False
            continue
        if not current_name:
            continue
        if line.startswith("|") and ("Claim supported" in line or "Evidence actually viewed" in line) and "URL" in line:
            in_source_table = True
            continue
        if in_source_table and line.startswith("|"):
            cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
            if len(cells) >= 4 and cells[1].startswith(("http://", "https://")):
                claim, url_cell, accessed, workstream = cells[:4]
                for url in urls_in_cell(url_cell):
                    current_entries.append((claim, url, accessed, workstream))
        elif in_source_table:
            in_source_table = False
    flush()
    return groups


def render_source_groups() -> str:
    blocks = ['<div class="source-groups">']
    for name, entries in read_source_groups():
        blocks.append('<details class="source-group">')
        blocks.append(
            '<summary><span>' + inline_markdown(name) + '</span>'
            f'<span class="source-count">{len(entries)} source entries</span></summary>'
        )
        blocks.append('<div class="source-entry-list">')
        for claim, url, accessed, workstream in entries:
            host = urlsplit(url).netloc.removeprefix("www.")
            blocks.append(
                '<article class="source-entry">'
                '<div class="source-entry-meta">'
                f'<span>{inline_markdown(accessed)}</span><span>{inline_markdown(workstream)}</span>'
                '</div>'
                f'<p>{inline_markdown(claim)}</p>'
                f'<a class="source-link" href="{html.escape(url, quote=True)}" '
                f'target="_blank" rel="noopener noreferrer">{html.escape(host)} ↗</a>'
                '</article>'
            )
        blocks.append('</div></details>')
    blocks.append('</div>')
    return '\n'.join(blocks)


def read_questions() -> tuple[list[tuple[str, str, str, str, str]], list[str]]:
    table: list[tuple[str, str, str, str, str]] = []
    resolved: list[str] = []
    in_questions = False
    in_resolved = False
    for line in QUESTIONS.read_text(encoding="utf-8").splitlines():
        if line.startswith("# Open questions"):
            in_questions = True
            in_resolved = False
            continue
        if line.startswith("## Resolved items"):
            in_questions = False
            in_resolved = True
            continue
        if line.startswith("## "):
            in_questions = False
            in_resolved = False
            continue
        if in_questions and line.startswith("| OQ-"):
            cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
            if len(cells) >= 5:
                table.append(tuple(cells[:5]))
        elif in_resolved and line.startswith("- "):
            resolved.append(line[2:].strip())
    return table, resolved


def render_questions() -> str:
    questions, _ = read_questions()
    blocks = ['<div class="question-list">']
    for question_id, priority, workstream, question, treatment in questions:
        blocks.append(
            f'<article class="question-item" id="{html.escape(question_id, quote=True)}">'
            '<details><summary>'
            f'<span class="question-id">{inline_markdown(question_id)}</span>'
            f'<span class="question-meta">{inline_markdown(priority)} · {inline_markdown(workstream)}</span>'
            f'<span class="question-title">{inline_markdown(question)}</span>'
            '</summary>'
            f'<p><strong>Safe treatment:</strong> {inline_markdown(treatment)}</p>'
            '</details></article>'
        )
    blocks.append('</div>')
    return '\n'.join(blocks)


def render_resolved() -> str:
    _, items = read_questions()
    return '<ul class="resolved-list">' + ''.join(
        f'<li>{inline_markdown(item)}</li>' for item in items
    ) + '</ul>'


def replace_between(text: str, start: str, end: str, replacement: str) -> str:
    left = text.index(start)
    right = text.index(end, left) + len(end)
    return text[:left] + replacement + text[right:]


def main() -> None:
    text = PAGE.read_text(encoding="utf-8")
    text = replace_between(text, '<div class="question-list">', '</div>', render_questions())
    text = replace_between(text, '<ul class="resolved-list">', '</ul>', render_resolved())
    source_start = '<div class="source-groups">'
    section_end = '\n    </section>'
    start = text.index(source_start)
    section_close = text.index(section_end, start)
    outer_close = text.rfind('</div>', start, section_close)
    if outer_close < 0:
        raise RuntimeError("cannot find the end of the source-groups wrapper")
    text = text[:start] + render_source_groups() + text[outer_close + len('</div>'):]
    PAGE.write_text(text, encoding="utf-8")
    groups = read_source_groups()
    question_rows, resolved_rows = read_questions()
    print(f"Rebuilt {PAGE.relative_to(ROOT)}: {sum(len(rows) for _, rows in groups)} source entries across {len(groups)} groups; {len(question_rows)} open questions and {len(resolved_rows)} resolved snapshots.")


if __name__ == "__main__":
    main()
