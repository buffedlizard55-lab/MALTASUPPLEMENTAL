# Delivery status — Malta trip guide (11 October 2026)

> **Snapshot boundary:** this status records the completed local reconciliation and validation, immediately before the required GitHub delivery actions. It is not a live PR or Pages status; the merge and post-merge deployment are reported after they are actually checked.

## Update — PR #42 merged; follow-up pass (`arena/9f6f35c7-maltasupplemental`, 11 October 2026)

- `main` is now at `5cdea68`: PR #42 was merged 15:43 UTC (squashed `fbb7aa4`) and carries the CS2 event guide — `data/event.json` (8 records), the full `event.html`, the TQ-special-service and taxi-tariff transport records, the event-day expense rows, nine navigation destinations and a seven-dataset validator.
- The fixed follow-up branch was reconciled to that `main` and contributes only net-new corrections: costs-page event-access wording and quick-fill example; the activities callout wording + CS2-event-guide link; the radio stream wording; and the activities tournament records updated for the 9 October Virtus.pro → NIP substitution. No record was added, removed or renamed.
- Counts and gates on the reconciled branch: validator **PASS** (7 datasets / 175 records / 305 logged URLs / 15 HTML pages / 173 link attributes / 9 nav destinations / 25 expense rows); `check_javascript.py` and `node --check js/site.js` **PASS**; `npm test` **PASS** (11/11 Playwright, 320/360/768/1440 px, axe, parity, planner); `git diff --check` **PASS**.
- Open items are unchanged from the sections below and `docs/OPEN_QUESTIONS.md`: the FAQ answers, the Saturday/Sunday agenda, the attendee gate and walk, the TQ1 monitor, the October single fare, and the taxi tariff's April-2022 vintage.
- Delivery: the branch is pushed and PR #44 carries these corrections; the merge and the Pages build are recorded here only after they are observed.

## Integration state

- Work is on the fixed session branch `arena/ef6c76d6-maltasupplemental`.
- PR #33 began at `854c1e16d94caa6cd7ae35ee44a0040bc5d036fd`; the required upstream snapshot is `origin/main` at `de3303fbfecdf8176afb32002f02be58692d0405`, containing PR #39 and accumulated PR #40/#41 work.
- The local non-fast-forward merge includes that exact upstream snapshot and retains PR #33's specific source corrections and evidence boundaries. At this snapshot, the merge commit is still awaiting commit/push and PR #33 has not yet been merged.
- The integration tree has **165 exact-schema records** (transport 25, food 38, activities 39, everyday 18, radio 20, expenses 25), **288 unique record URLs** in the source log, **15 HTML pages / 138 link attributes**, eight shared navigation destinations, and all 25 expense rows.

## Cumulative verification passes

1. **Implementation:** all six topic JSON files and `data/record.schema.json` parse; `scripts/validate_site.py` passes schema/source-log/page wiring; `scripts/check_javascript.py` and `node --check js/site.js` pass; browser tests cover planner behavior, navigation, data/render parity, and responsive accessibility.
2. **Requirements/evidence:** current-facing claims were reconciled against the inherited source notes. The Eventbrite listing is described as dated evidence of a free 18+ reservation option and the visible 14–16 October agenda, not as this traveler's reservation or guaranteed admission. Route 186's 20:53 time is one static variant; fare-season, onward connection, detour effect, and safe walks remain open. BBC parent-series labels are distinguished from match-specific broadcast services without inferring Malta carriage. The MTA short-stay interpretation remains open.
3. **Final audit:** current pages, data, source notes, handoff, open questions, and plan were reconciled; stale fare-by-date, ticket-access, transit-cutoff, MTA-threshold, and BBC service-label conclusions were corrected or explicitly marked historical. External link liveness, physical radio/transit checks, and comprehensive review-platform coverage were not claimed.

## Local validation results

- `python3 -m json.tool` on all six topic datasets and the record schema — **PASS**.
- `python3 scripts/validate_site.py` — **PASS**: 6 JSON files, 165 records, 288 source URLs, 15 HTML pages, 138 link attributes, 8 navigation destinations, 25 expense rows.
- `python3 scripts/check_javascript.py` — **PASS**.
- `node --check js/site.js` — **PASS**.
- `npm ci` — **PASS** (23 packages installed; npm reported 0 vulnerabilities).
- `npm test` — **PASS**, 11/11 Playwright tests (including 320/360/768/1440 px layouts, axe, rendering, navigation and expense-planner cases).
- `git diff --check` — **PASS**.

## Current blockers and handoff

- **Event:** current inventory, the traveler's own reservation, per-day scanning/validity, attendee gate, exact finish-time discrepancy (listing headline 22:00 vs Wed/Thu agenda rows to 22:30), and 17–18 October agenda remain unconfirmed.
- **Transit/fare:** no date-specific end-to-end journey, onward Buġibba-to-Qawra connection, measured gate/hotel walk, complete alternative-route search, or live taxi quote. The 17 October Route 186 notices show different windows; use the 19:00–24:00 union as a planning alert and verify live. MPT has not established the single fare applicable 13–19 October.
- **Radio:** no physical FM/DAB+ scan, local reception measurement, BBC Sounds/RaiPlay access check, Malta carriage confirmation, or named-match output on a locally receivable service. The DAB+ “Sports Channel” block/identity is a scan lead only; Rai's trip-week running order is not established. UK BBC schedules are not Malta carriage.
- **MTA:** the guideline PDF and the current webpage's “exceeded fifteen nights” text do not expressly reconcile short-stay treatment. Six-night €9 arithmetic is conditional only; use the invoice.
- **Research coverage:** Google Maps/review, TripAdvisor and some Reddit/search snapshots were accessible; Yelp, Instagram, TikTok, Facebook and X access was blocked or limited. The evidence is not comprehensive. Recheck volatile menus, hours, closures, fares, schedules and ticket availability before acting.
- **Traveler-specific unknowns:** booking confirmation, party size/ages, flights, meal plan, actual ticket, itinerary, device, insurance, and personal expenses remain unknown. Keep planner fields blank until the traveler provides them.

The current workstream ownership, dependencies, and next-session tasks remain in `docs/PLAN.md`; cross-topic details are in `docs/HANDOFF.md`; all open items are maintained in `docs/OPEN_QUESTIONS.md`.
---

## Workstream H status — PR #42, 11 October 2026 (`arena/154ca483-maltasupplemental`)

Everything above describes the state as of the PR #33 audit pass. **This section is authoritative for the current merged tree**, which adds workstream H on top of it. **Delivery vehicle: PR #42** — https://github.com/buffedlizard55-lab/MALTASUPPLEMENTAL/pull/42.

`main` carried 165 records across six data files and eight active pages. This session added the event topic and reconciled twice — first against PR #39's extension pass, then against PR #33's audit pass.

| Owner | Canonical data / page | Integrated scope | Remaining |
|---|---|---|---|
| **H · CS2 event (new)** | `data/event.json` / `event.html` | **8 records** and the site's **ninth active page**, promoted out of the retired noindex stub set (so HTML pages stayed at 15). Venue address and map pin, ticketing terms, dates and phases, the published daily agenda, match clocks in Malta time, team field including the 9 Oct Virtus.pro → NIP substitution, format and prize split, broadcast talent, official streams, on-site practicalities. | Sat 17 / Sun 18 agenda rows and all nine FAQ answers are client-side and did not render; current inventory and whether a reservation guarantees admission; the attendee gate; Thu 15 / Fri 16 match clocks were published by no source at any timezone; the NIP substitution is not officially republished (OQ-H5). **No ticket has been secured by this project.** |
| A · Transport (additions) | `data/transport.json` / `getting-around.html` | 25 → **27 records**. Two unique additions: **`tq-event-special-services`** (the TQ1 corridor through Qawra — a possibility to watch for, not a plan) and **`white-taxi-official-tariff`** (Transport Malta's published meter maxima, read directly, with the April-2022 currency caveat). Two checklist items added to the page. | OQ-H3 (will TQ1 run?) and OQ-H7 (tariff currency, unmeasured road distance). |
| F · Expenses (corrections) | `data/expenses.json` | Still **25 rows, still blank by default**. Three rows left stale at 2026-10-09 were brought in line with the transport findings: `event-commute` (no longer implies the event end time is unsettled), `taxi-rideshare` (reframed from "contingency" to the realistic fallback), `local-bus-and-cards` (now carries the €27 Explore Flex recommendation). `event-access` kept as written with only the two budget-relevant FAQ gaps appended. | Actual amounts, party size, flights, reimbursement — unchanged, still traveller-supplied. |
| G · Integration | Shared files | Edited serially per the ownership protocol: `js/site.js` nav 8 → 9; `scripts/validate_site.py` (`EXPECTED_PAGES` + topic-file count 6 → 7); `tests/site.spec.js` (page list, topic map, nav count); `index.html`; `getting-around.html`; `sources.html`; `README.md`; and this docs set. | No physical radio scan, no manual graphical screenshot, no external-link liveness test. |

**Language was aligned to PR #33's audit qualifications.** That pass deliberately downgraded the return-gap finding from `verified` to `partially verified` and reframed it as a *risk from one static Route 186 variant* rather than proof that no later bus exists. This branch's wording was rewritten to match — in `index.html`, `README.md`, `event.html`, `getting-around.html` and the three expense rows — so the reconciliation does not silently re-strengthen a claim the audit softened. The TQ1 finding reinforces that caution rather than undercutting it: it is a second reason not to treat one timetable variant as the whole network.

**Duplicates deliberately dropped.** The parallel session independently found the same Eventbrite listing, so this branch dropped its own overlapping records rather than duplicating them: `event-day-late-return` and `venue-nearest-bus-stops` were superseded by `main`'s `event-day-late-finish-return-gap` and `mfcc-official-bus-186`, and its `twc-2026-venue-dates` and `mpt-fares-cards` rewrites were dropped in favour of `main`'s. One limitation is **withdrawn**: "18–19 October is not forecast" is obsolete, because `main` located the Met Office Valletta view reaching 12–19 October. Reasoning is in `docs/PLAN.md` and `docs/HANDOFF.md`.

### Gates on the merged tree

- `python3 scripts/validate_site.py` — **PASS**: 7 JSON files / **175 exact-schema records** / **305 unique record URLs all present in `docs/SOURCES.md`** / 15 HTML pages / 170 link attributes / **9 shared-navigation destinations** / 25 expense rows wired.
- `python3 scripts/check_javascript.py` and `node --check js/site.js` — **PASS**; `git diff --check` clean.
- `npm ci && npm test` — **PASS, 11/11 Playwright**, including `main`'s itinerary quick-fill regression.
- Counts: transport 27, event 8, food 38, activities 39, everyday 18, radio 20, expenses 25.

Two mechanical notes for the next session. The repository had been fetched **shallowly**, which made `main` and this branch appear to be unrelated roots with no merge-base; `git fetch --unshallow` restored real ancestry before the rebase. And one earlier local commit was rolled back by the workspace before pushing, so the work was recommitted and every gate re-run from a fresh `npm ci`.
