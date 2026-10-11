# Malta Trip Guide — final report, 11 October 2026

**Guide:** https://buffedlizard55-lab.github.io/MALTASUPPLEMENTAL/

**Delivery PR:** https://github.com/buffedlizard55-lab/MALTASUPPLEMENTAL/pull/29

**Traveler-supplied plan:** AX ODYCY, Qawra Coast Road, Qawra SPB 1902, Deluxe Sea-View; 13–19 October 2026; Thunderpick CS2 finals at BLAST Arena Studios, Attard. These are planning inputs, not independently validated reservation or admission documents.

## Executive summary

The static guide has **eight active pages**: overview, getting around, food/cafés, activities/landmarks/events, everyday travel, sports radio, expense planner and sources/status. Six canonical topic JSON files contain **124 exact-schema records**. Listings expose provenance, check dates, confidence and unknowns. The overview includes a flexible seven-day framework; filters, deep links, mobile navigation and evidence disclosures keep the guide practical without hiding uncertainty.

All **three cumulative local verification passes passed**, including nine real-browser tests per final pass. The first PR #29 CI run also passed; the final editorial update must be checked again before merge. Publication uses the existing GitHub Pages configuration: `main`, repository root. Merge/build outcomes are tracked on the linked PR and GitHub deployment history, and verified separately in the session delivery response.

**Complete fresh line-by-line external verification of every historical claim and comprehensive all-platform review compilation remain incomplete.** The unresolved requirements below are not represented as fully satisfied.

## Deliverables and evidence boundaries

### A · Getting around — 14 records

Mode judgments compare convenience, published prices, value and feasibility—not measured journey times or live quotes. Operator Route 186 gives outbound Qawra 952 → Ta’ Qali Stadium 6227 and return Stadium 2194 → St Paul’s Bay/Buġibba; the return requires a separate hotel connection. TD1’s airport outbound timetable directly includes Qawra Arznell 950. Uber’s Valletta offer is another app lead, not a Qawra/Ta’ Qali supply guarantee.

Event routes are **candidates, not saved date-specific door-to-door directions**. Multiple static timetable variants lack established day-type context, so first/last clock bounds are withheld. Recheck the 17 October evening diversion. €25 Explore Adult and €27 seven-day Flex are distinct products with differently stated inclusions; the October single-fare season remains unresolved.

### B/C · Food — 29 records; activities — 31 records

Hotel/Qawra choices, wider excursions, landmarks, gaming leads and dated trip-window events are organized by category and locality. Selected operator, organizer and ticketing sources were refreshed, including Fontanella, Ta’ Marija, Aviation Museum and Mosta parish visitor information.

Platform reviews remain source-specific, not blended or comprehensively compiled. Closures/status conflicts, picnic access, ticket inventory, exact event times and suspect In Guardia coordinates remain caveated. Aviation Museum’s generic 16:00 last-entry line cannot apply to its published Sunday noon close; confirm Sunday cutoff. Fontanella’s precise hours/address and Ta’ Marija’s October hours/show dates remain open.

### Thunderpick event

The official page confirms arrival 12 October, media 13 October, groups 14–16 October, playoffs 17–18 October and departure 19 October, with Malta as the location. A Thunderpick-issued release names BLAST Studios Malta. Separate-event BLAST/EventWorks listings and a VisitMalta.co.uk directory corroborate MFCC/Ta’ Qali **venue-area context**, not TWC spectator eligibility, attendee entrance/pin, tickets, door/finish times or access policy.

### D · Everyday travel — 15 records

Power/voltage, entry/EES/ETIAS, language, money, mobile connectivity, safety/health and weather are qualified for date and traveler circumstances. The health ministry directly lists emergency ambulance/fire/police **112, 24/7**. No fixed tipping percentage is prescribed. The forecast snapshot covers 13–17 October only. Passport, insurance, carrier/device and medicines/customs cases need the traveler’s own checks.

### E · Sports radio — 10 records

NET FM 101 MHz and recurring station shows; regulator FM tuning reference; Radio Sportiva/BBC World Service DAB+ listings; BBC Sportsworld 17/18 October episode dates; WorldDAB BBC 6A at 181.936 MHz and unidentified Sports Channel 12A at 223.936 MHz scan lead; Rai Radio 1’s recurring weekend football programme and Malta directory entries.

Two BBC Radio 5 Live episode pages support **UK commentary listings** for Brentford–Liverpool on 17 October and Leeds–Manchester United on 18 October. The official Premier League fixture article explicitly labels BST, allowing separate Malta kickoff conversion. Neither establishes Maltese commentary, reception/streaming rights, BBC World Service carriage or Kalshi-market overlap. BBC episode clocks without identified zones are not converted. No current AM sports schedule or named trip-event commentary in Malta was confirmed.

### F · Expense planner — 25 blank rows

18 core categories plus seven optional daily rows; editable euro budget/actual/notes, totals/difference, browser-local autosave, reset confirmation and CSV backup. Negative, nonfinite, more-than-two-decimal and over-€1-billion values are invalid. Corrupted/denied storage and fetch failures produce safe notices. No personal amounts are prefilled; avoid aggregate/daily double counting.

MTA rate/cap are sourced, but its separate 15-night wording remains ambiguous (OQ-25). Six billable nights × €1.50 = €9 is arithmetic only, not a confirmed booking charge. Actual party ages/count, booking terms and invoice remain unknown.

## Three cumulative passes

1. **Pass 1 passed:** implementation, structural/schema validation, shared/inline JavaScript syntax and nine real Chromium browser tests. Fixed legacy `price_range` rendering and reproducible browser library/context setup.
2. **Pass 2 passed:** original-requirements/edge-case review plus cumulative regression; strengthened amount validation and storage recovery; inspected desktop/mobile screenshots.
3. **Pass 3 passed:** reconciled advancing main commits `ab068ed` and `2f90396`, independently checked disputed evidence, clarified directional stops and preserved unsupported upstream findings as archives. Repeated the full suite after both integrations and final spacing edits; latest result **9/9 passed in 46.8 seconds**.

The suite checks eight active pages at **360/768/1440 px** (24 page/viewport combinations), horizontal overflow, axe WCAG 2A/AA/2.1AA rules, canonical card fields, filters, mobile navigation, skip/deep links, expense defaults/totals/persistence/reset, CSV quoting/newlines/formula/BOM safety, invalid inputs, corrupt/denied storage and failed fetch/disabled export.

Structural result: **six datasets / 124 records / 199 unique logged record URLs / 15 root HTML pages / 106 link attributes / eight navigation destinations / 25 planner rows**. Root aliases receive structural validation; the eight active pages receive viewport tests. CI uses Node 22, Python 3 and npm-distributed Linux x64 Chromium. Screenshots/reports are ignored generated artifacts.

Tests do **not** certify external truth, individual eligibility, physical reception, live bookings, every browser/device or exhaustive assistive-technology compatibility.

## Integration and process boundaries

All work stays on `arena/7bf2063c-maltasupplemental`. Plan/ownership, cross-topic handoffs, sources, audit and unresolved questions are maintained in `PLAN.md`, `HANDOFF.md`, `SOURCES.md`, `AUDIT_2026-10-11.md` and `OPEN_QUESTIONS.md`.

Independent research calls ran in parallel. There is no autonomous subagent/workstream-branch runner in this session, so separate-workstream branch implementation was **not performed**. Shared edits and integration were serial and ownership-guided.

Raw upstream docs/leads are retained under `UPSTREAM_2026-10-11_*`, `UPSTREAM_2f90396_*` and `UPSTREAM_RADIO_LEADS.json` as **provenance archives, not current facts**. They can contain withdrawn/conflicting clocks, venue claims or old schema enums. Current records/audit supersede them; prior delivery history is in Git. PR #10 is not part of this delivery and remains untouched.

## Prioritized remaining work

1. Confirm TWC attendee eligibility, ticket, exact entrance/pin and daily public arrival/finish times with the organizer; do not borrow another BLAST event’s access rules.
2. Save live operator-planner outward/return directions for 14–18 October, safe walks/stop sides, diversion effects and airport flight times; retain a live-quote taxi fallback.
3. Complete fresh claim-by-claim audit of retained restaurants/activities and accessible Google/Maps/Yelp/Instagram/TikTok/Facebook/Reddit/X evidence without guessing blocked content.
4. Scan FM/DAB+ at AX ODYCY/venue; verify explicitly zoned official schedules, named-match carriage, Malta streaming rights and any Kalshi-market overlap separately.
5. Confirm booking/party details, inclusions, MTA 15-night wording and invoice; fill the planner from actual itinerary. Refresh 18–19 October weather when available.
6. Test on the traveler’s phone/receiver/browser and with assistive technologies; re-open volatile official sources before departure and each event.

This is a planning aid, not an admission, dispatch, immigration, tax, legal, medical, radio or booking guarantee.


## Merge session — PR #23 (11 October 2026)

The arena/b9943054 branch merged advancing main through PR #29 (browser/accessibility suite, JavaScript checker, conservative record boundaries, `UPSTREAM_*` provenance archives). The merge kept #29’s canonical text and tests, preserving two independently verified records that existed nowhere in the merged tree: the operator night-route notice (`mpt-night-routes-late-return`) and the trip base-hotel record (`ax-odycy-base-hotel`). Earlier-session leads that #29 deliberately withheld from rendering (static Route 186 clock bounds, converted BBC airtimes, fare placeholders, the EventWorks DJ listing, fixture-context radio records) remain archived, not rendered.

Verification in this session: `python3 scripts/validate_site.py` and `python3 scripts/check_javascript.py` pass (126 exact-schema records, 200 record URLs present in `docs/SOURCES.md`, 15 pages, 107 link attributes, eight navigation destinations, 25 expense rows); #29’s nine Playwright browser/accessibility tests pass via the npm-distributed Chromium (`@sparticuz/chromium`), including axe checks at 360/768/1440 px; and the independent DOM harness passes 19/19 planner and 49/49 site checks. No physical-device, FM/DAB+ reception or external-link-liveness test was performed. Remaining work is unchanged from the prioritized list above, with the night-bus question added to `OPEN_QUESTIONS.md`.
