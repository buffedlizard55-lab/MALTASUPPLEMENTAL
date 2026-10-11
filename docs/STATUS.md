# Delivery status — Malta trip guide (11 October 2026, session arena/502e2dae)

> **Snapshot boundary:** this status records the completed local verification and Pass 1–3 integration for the `arena/502e2dae-maltasupplemental` session, before the GitHub delivery actions. The merge and post-merge deployment are reported after they are actually checked.

## Integration state

- Work is on the fixed session branch `arena/502e2dae-maltasupplemental`, started at `origin/main` (`b307c51`, merge of PR #33) at parity.
- This session ran the required multi-pass protocol (Pass 1 implement/verify, Pass 2 review for bugs/missing requirements/edge cases, Pass 3 re-check against the request) over the integrated tree, plus a line-by-line fact re-verification of the highest-risk transport, event, fare and radio claims against live sources on 11 October 2026.
- The integration tree has **165 exact-schema records** (transport 25, food 38, activities 39, everyday 18, radio 20, expenses 25), **292 unique record URLs** in the source log, 15 HTML pages / 138 link attributes, eight shared navigation destinations, and all 25 expense rows.

## What this session verified and changed

1. **Event listing re-read (A/C):** the Hotspawn/Eventbrite page read 11 October still shows only the Wed 14 / Thu 15 (09:30–22:30) and Fri 16 (14:00–21:00) agenda rows; the Sat/Sun entries remain hidden behind “Show all agenda”. A “Sales end soon” banner now displays. Existing claims were confirmed unchanged; the re-read is logged in `docs/SOURCES.md`.
2. **Route 186 return grids (A):** the operator’s live route page was parsed stop by stop. The last Stadium 2194 departures toward Buġibba are **20:53 and 20:54** on the published return grids (Buġibba Bay 1 arrivals 21:26/21:36); the toward-Rabat grids run Qawra 952 to about 21:39. The “one static variant” wording was replaced across data/pages/docs with the operator-page finding. Which grid applies on each trip date is not labelled.
3. **Detour scope (A):** the 17 October omitted span (Gholja 2 → Targa) sits between the Stadium 2194 boarding stop and the Buġibba terminus on the operator’s own stop lists, so the traveler’s boarding/alighting stops are not among the omitted stops. The diverted path/timing remains unpublished.
4. **Late-return leads (A):** Route 202 from Stadium 2194 toward Sliema is listed to about 22:08 (operator route page); N212 (Sliema–Buġibba) and N48 (Mosta-corridor stops toward Buġibba) are recorded as unverified night-bus second legs; Moovit’s 23:07 last-202 figure is logged as an unresolved third-party conflict.
5. **Fare season (A/F):** two third-party 2026 fare guides place the summer/winter boundary at 18/19 October, matching the official page’s stated 19-October winter start. The likely split — €2.50 on 13–18 October, €2.00 on 19 October — is recorded at “partially verified” as an inference; the operator has not published a current window.
6. **Card terms (A/F):** the 12-journey card counts Night Routes/Airport Direct at 2 journeys per trip; Explore Flex advertises 2 Airport Direct trips for €6; the fares page contradicts itself on whether Explore Adult 7-day includes Airport Direct — disclosed, not resolved.
7. **Radio re-check (E):** BBC programme pages (5 Live Sport upcoming grid; episode m00334k6) reconfirm the UK 17–18 October commentary listings. UK schedule only — Malta carriage remains unproven.
8. **Data hygiene (G):** canonical key order (`price range` after `hours`) normalized across all six data files; schema/validator results unchanged.

## Local validation results (after edits)

- `python3 scripts/validate_site.py` — **PASS**: 6 JSON files, 165 records, 292 source URLs, 15 HTML pages, 138 link attributes, 8 navigation destinations, 25 expense rows.
- `python3 scripts/check_javascript.py` — **PASS**; `node --check js/site.js` — **PASS**.
- Internal deep-link check (static ids + runtime record ids) — **PASS**, 0 broken.
- `npm test` (validator + JS gate + Playwright) — **PASS**, 11/11 after the session edits (320/360/768/1440 px layouts, axe WCAG 2A/AA/2.1AA, planner persistence/CSV/reset, quick-fill, storage-denial and data-fetch failure cases).

## Current blockers and handoff

- **Event:** current inventory, the traveler’s reservation, per-day scanning/validity, attendee gate, the 22:00-vs-22:30 finish discrepancy, and the 17–18 October agenda remain unconfirmed (Sat/Sun rows were still hidden on the 11 Oct re-read).
- **Transit:** which Route 186 return grid (20:53 or 20:54) runs on each trip date; any event extra service; the dated onward Buġibba→Qawra connection; the after-20:54 fallback legs (202→N212, 405→N48) as date-specific journeys; the 17 October diversion’s actual effect; measured gate/hotel walks; live taxi quotes.
- **Fares:** operator confirmation of the likely €2.50/€2.00 season split remains outstanding.
- **Radio:** no physical FM/DAB+ scan, no Malta carriage confirmation, no named-match output on a locally receivable service; the DAB+ “Sports Channel” block/identity remains a scan lead.
- **MTA:** the guideline PDF and webpage short-stay wording remain unreconciled; use the invoice.
- **Coverage:** Yelp/Instagram/TikTok/Facebook/X remain blocked or limited; review evidence is a dated partial snapshot. No full external-link crawl or physical transit/radio test was claimed.
- **Traveler-specific inputs:** itinerary, party size/ages, booked prices, flights, meal plan, device, insurance. Keep planner fields blank until supplied; the paste-your-itinerary quick-fill remains the hand-off tool.

Workstream ownership, dependencies and next-session tasks remain in `docs/PLAN.md`; cross-topic notes in `docs/HANDOFF.md`; open items in `docs/OPEN_QUESTIONS.md`.
