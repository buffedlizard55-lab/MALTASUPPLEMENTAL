#!/usr/bin/env python3
"""One-off helper: refresh docs/FINAL_REPORT.md and docs/STATUS.md for the second 11 October 2026 session."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def edit(path: str, pairs: list[tuple[str, str]]) -> None:
    file = ROOT / path
    text = file.read_text(encoding="utf-8")
    for old, new in pairs:
        if old not in text:
            raise SystemExit(f"not found in {path}: {old[:90]!r}")
        text = text.replace(old, new, 1)
    file.write_text(text, encoding="utf-8")


edit(
    "docs/FINAL_REPORT.md",
    [
        (
            "**Delivery PR:** https://github.com/buffedlizard55-lab/MALTASUPPLEMENTAL/pull/31\n**Branch:** `arena/3a5297d2-maltasupplemental`",
            "**Delivery PR:** the second 11 October 2026 session PR on `arena/96208136-maltasupplemental` (previous PR #31 merged to `main` on 11 October 2026)\n**Branch:** `arena/96208136-maltasupplemental`",
        ),
        (
            "Six canonical JSON datasets contain **128 exact-schema records**: transport 16, food 29, activities/events 32, everyday guidance 15, radio 11, and expenses 25.",
            "Six canonical JSON datasets contain **133 exact-schema records**: transport 18, food 29, activities/events 32, everyday guidance 16, radio 13, and expenses 25.",
        ),
        (
            "The refreshed offline validator reports **205 unique record URLs** in `docs/SOURCES.md`, 15 HTML pages, 117 link attributes, 8 shared-navigation destinations, and all 25 expense rows wired.",
            "The refreshed offline validator reports **231 unique record URLs** in `docs/SOURCES.md`, 15 HTML pages, 122 link attributes, 8 shared-navigation destinations, and all 25 expense rows wired.",
        ),
        (
            "### A · Getting around — 16 records",
            "### A · Getting around — 18 records",
        ),
        (
            "October 2026 single-fare validity, TWC entrance/walk, exact outward/return route and diversion impact remain open.",
            "Fares were re-verified directly from the operator on 11 October 2026: single day route €2.50 (summer table) / €2.00 winter with a two-hour transfer window, night/Tallinja Direct €3.00, TD1 €3.50, 12-journey card €19, Explore Adult 7-day €25, Explore Child €7, Explore Flex €21/€27, and a €50 fine without a valid ticket; cards are sold at the Buġibba Terminal, the closest listed office to Qawra. The operator does not print the 2026/27 winter changeover date, so €2.50 is the planning single fare. Ride-hailing coverage was corrected: Bolt is documented as operating in Malta, while Uber’s own Malta airport page and two 2026 third-party guides contradict each other (OQ-27). TWC entrance/walk, exact outward/return route and diversion impact remain open.",
        ),
        (
            "### D · Everyday life — 15 records",
            "### D · Everyday life — 16 records",
        ),
        (
            "Passport, insurance, device/carrier, medicines/customs and other personal advice is not individualized. The recorded forecast does not cover 18–19 October.",
            "Passport, insurance, device/carrier, medicines/customs and other personal advice is not individualized. Power is recorded as Type G / 230 V / 50 Hz with the adapter-versus-converter distinction. The Malta Tourism Authority’s guidelines for the 1 July 2026 eco-contribution were read in full, resolving the “15-night” wording as the €22.50 cap mechanism (OQ-25): €1.50 per night for guests 18+, so six nights implies about €9.00 per eligible adult, subject to the invoice. Two dated forecast snapshots now cover 13–19 October and disagree on 13 October, so the daily Malta Met Office forecast remains the reference.",
        ),
        (
            "### E · Malta sports radio — 11 records",
            "### E · Malta sports radio — 13 records",
        ),
        (
            "Kalshi EPL/Serie A category pages were checked for visible trip-window market timing and overlap. Such a category/fixture listing is not radio evidence, a rights statement, or confirmation of Malta trading eligibility. Generic “Sports Channel” and third-party TalkSPORT/6C references remain unverified scan leads. No physical FM/DAB+ receiver scan was available at AX ODYCY or the event area.",
            "**Upgraded in the second 11 October session:** the “Sports Channel” lead is now recorded as a partially verified talkSPORT carriage listing on Malta DAB+ block 6C (185.360 MHz), corroborated by the Radio in Malta 6C station list (“Sports Channel (Talk Sport)”), WorldDAB’s Malta multiplex table and Wikipedia’s talkSPORT frequency list; talkSPORT is an official Premier League audio broadcaster, making 6C the priority receiver test during the 17–18 October fixtures. What the relay actually transmits, its rights scope and indoor reception remain unverified (OQ-28), and a full DAB+ tuning guide (6A/6C/12A) plus Vibe FM’s published Malta Premier League radio partnership were added. Kalshi EPL/Serie A category pages list trip-window fixtures overlapping the radio windows; Kalshi’s own help centre says travel-abroad use is possible subject to its Member Agreement while third-party guidance says US-resident-only, so eligibility stays account-specific. No physical FM/DAB+ receiver scan was available at AX ODYCY or the event area.",
        ),
        (
            "The planner provides 18 core trip categories plus seven optional daily templates for 13–19 October, editable euro budget/actual values, notes, totals/difference, browser-local autosave, CSV export, and reset. Nothing pre-fills a flight, hotel booking/rate, traveler count, ticket, itinerary, tax amount, or reimbursement. Daily and aggregate rows must not be double-counted. The MTA rate/cap is sourced, but the separate “15-night threshold” wording is ambiguous (OQ-25); any six-night arithmetic is conditional and not a personal charge.",
            "The planner provides 18 core trip categories plus seven optional daily templates for 13–19 October, editable euro budget/actual values, notes, totals/difference, browser-local autosave, CSV export, and reset, together with a documented “when your itinerary arrives” intake that maps each confirmed itinerary item to its row. Nothing pre-fills a flight, hotel booking/rate, traveler count, ticket, itinerary, tax amount, or reimbursement. Daily and aggregate rows must not be double-counted. The MTA rate/cap and the “15-night” cap mechanism are now resolved from the guidelines PDF (OQ-25), so the six-night figure (about €9.00 per eligible adult) is stated as a conditional calculation from published rules and never as a personal charge.",
        ),
        (
            "1. **Implementation and source pass — passed.** `python3 scripts/validate_site.py` reports 6 JSON files / 128 exact-schema records / 205 unique record URLs / 15 HTML pages / 117 link attributes / 8 navigation destinations / 25 planner rows.",
            "1. **Implementation and source pass — passed.** `python3 scripts/validate_site.py` reports 6 JSON files / 133 exact-schema records / 231 unique record URLs / 15 HTML pages / 122 link attributes / 8 navigation destinations / 25 planner rows.",
        ),
        (
            "1. Confirm TWC spectator eligibility, ticket, exact attendee entrance/pin, and daily public arrival/finish times with the organizer; do not borrow access instructions from another BLAST event.\n2. Enter the confirmed hotel and event location/time into MPT’s live planner for each event date; verify stop sides, walks, Route 186 diversion effects, onward Qawra connection, TD1 flight timing, and current fare/card terms. Keep a live taxi/ride-hailing quote for an unsuitable late return.\n3. Recheck NET FM, Rai, Radio Sportiva and BBC schedules close to air; scan FM/DAB+ at the actual hotel/event locations; verify named-match selection, receiver band, and Malta stream territory separately.",
            "1. Confirm TWC spectator eligibility, ticket, exact attendee entrance/pin, and daily public arrival/finish times with the organizer; no public sale was found for these Finals, so ask directly and keep the Twitch/Kick/YouTube broadcast as the fallback (OQ-26). Do not borrow access instructions from another BLAST event.\n2. Enter the confirmed hotel and event location/time into MPT’s live planner for each event date; verify stop sides, walks, Route 186 diversion effects, onward Qawra connection, TD1 flight timing, and the operator’s 2026/27 winter fare changeover. Keep a live Bolt/eCabs quote for an unsuitable late return and record which ride-hailing apps actually show vehicles (OQ-27).\n3. Run the documented five-minute DAB+ test (blocks 6A/6C/12A) at the hotel: confirm the 6C “Sports Channel” content during the 17–18 October Premier League window (OQ-28), BBC World Service *Sportsworld* on 6A, NET FM on FM 101 and Vibe FM on 88.7 FM, and record what each actually carried.",
        ),
        (
            "## Rebase and delivery state",
            """## Second 11 October 2026 session — what changed

Working on `arena/96208136-maltasupplemental` after PR #31 merged, this session re-verified the highest-value claims that were still open and corrected one that was wrong:

- **Transport prices (A):** the operator’s own fare table, travel-card terms, sales points and the €50 fine are now recorded exactly; the €2.50 summer single is the planning fare for 13–19 October, with the operator’s failure to print the 2026/27 changeover noted. Five new/upgraded records cover the seasonal window, sales points and ride-hailing, and the mode comparison was repriced.
- **Event admission (A/C):** BLAST’s Malta studio (Ta’ Qali, MFCC South Gate National Stadium, Attard ATD 4000) and its €10.00 studio-audience ticketing precedent for BLAST-run events are recorded, together with the key negative finding that no public ticket sale or spectator policy for these GAM3RS_X-operated Finals was found; Thunderpick’s Twitch/Kick/YouTube broadcast is the documented alternative (OQ-26).
- **Radio (E):** the former “unverified” Sports Channel lead became a partially verified talkSPORT carriage listing on DAB+ block 6C at 185.360 MHz, with a full 6A/6C/12A tuning guide and Vibe FM’s Malta Premier League partnership added; the relay’s content stays open (OQ-28). Kalshi’s own vs third-party travel-abroad guidance is recorded as a conflict.
- **Everyday (D):** Type G / 230 V / 50 Hz confirmed with the adapter-versus-converter distinction; the MTA eco-contribution guidelines resolved OQ-25 (cap = fifteen nights) and narrowed OQ-23 to the invoice figure; two dated 13–19 October forecast snapshots were added with their disagreement on 13 October flagged.
- **Expense planner (F):** a nine-step “when your itinerary arrives” intake maps each itinerary item to its row and cites the now-verified bus prices; the hotel-charges and event-access rows were updated without prefilling any personal amount.
- **Corrected:** one travel-reference page consulted in this session wrongly told US travellers that no adapter is needed in Malta; it was rejected and the conflict is logged rather than silently averaged.

## Rebase and delivery state""",
        ),
        (
            "The PR #31 branch reconciles later `origin/main` changes at `81930be`",
            "The second-session branch builds directly on merged `main` (PR #31, merge commit `4ed9c5a`), so no rebase conflict exists. The PR #31 branch reconciled later `origin/main` changes at `81930be`",
        ),
    ],
)

edit(
    "docs/STATUS.md",
    [
        (
            "# Delivery status — 11 October 2026 (pre-merge review)",
            """# Delivery status — 11 October 2026 (second session, pre-merge)

**Current session (`arena/96208136-maltasupplemental`):** re-verification and refresh after PR #31 merged to `main` at `4ed9c5a`. Five records were added (133 total: transport 18, food 29, activities 32, everyday 16, radio 13, expenses 25), 231 record URLs are logged in `docs/SOURCES.md`, and 122 link attributes across 15 HTML pages pass the offline validator. Gates re-run after every edit: `python3 scripts/validate_site.py`, `python3 scripts/check_javascript.py`, `node --check js/site.js` and `npm test` (**9/9 Playwright tests**, 42.5s). Key outcomes: exact published bus fares and card terms; the negative finding that no public ticket sale or spectator policy for the Thunderpick Finals exists in the checked sources; talkSPORT upgraded from an unverified lead to a partially verified Malta DAB+ block 6C carriage listing; the MTA “15-night” wording resolved; Type G/230 V power confirmed; two dated trip-week forecast snapshots added. Still open: TWC attendee access (OQ-26), the 6C relay’s actual content (OQ-28), Uber’s status in Malta (OQ-27), trip-specific journeys/walks, and all traveler booking details. No physical receiver test or manual graphical device audit was possible.

## Previous delivery status (PR #31, merged)""",
        ),
    ],
)

print("final report and status updated")
