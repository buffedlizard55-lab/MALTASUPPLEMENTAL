# Delivery status — Malta trip guide (11 October 2026, session `arena/27302b08-maltasupplemental`)

> **Snapshot boundary:** this status describes the integrated tree, the gates actually run in this session, and the GitHub outcomes for **pull request #43** only after each was observed. Nothing here is a live dashboard.

## Delivery state (observed)

| Step | Observed result |
|---|---|
| Pull request | **#43** — `arena/27302b08-maltasupplemental` → `main`, opened 11 October 2026 |
| CI on the PR | **SUCCESS** — "Schema, browser and accessibility checks" (validate + JavaScript gate + 11 Playwright tests) |
| Conflicts during its life | `main` advanced to `5cdea68` (PR #42 merged upstream) while #43 was open; #43 was re-merged against it, conflicts resolved by content and re-pushed (commit `7817857`) after a line check confirmed main's variants were contained in, or superseded by, this branch's files |
| Merge | **MERGED** 11 October 2026 15:54:56 UTC, merge commit **`94733df22b670825eb1b39d21d53581d0274e329`** |
| CI on `main` | **SUCCESS** (run 38153269792) |
| GitHub Pages | **built** for commit `94733df22b670825eb1b39d21d53581d0274e329` (pages-build-deployment run 38153269670) |
| Deployed page spot-check | Homepage and `event.html` fetched live after the build: the "Your base: AX ODYCY" section, the refreshed eco-contribution wording, the "Free / Reserve a spot / Sales end soon" ticketing line and the TQ1/taxi-tariff pointers are all present |
| Pull request #42 | Already **MERGED** upstream by the parallel session at `5cdea68` before this branch was merged; nothing left open

## Update — PR #42 merged; follow-up pass (`arena/9f6f35c7-maltasupplemental`, 11 October 2026)

- `main` had moved to `5cdea68` (PR #42 merged 15:43 UTC, squashed `fbb7aa4`; `main` has since advanced through the PR #43 integration, `94733df`) and carries the CS2 event guide — `data/event.json` (8 records), the full `event.html`, the TQ-special-service and taxi-tariff transport records, the event-day expense rows, nine navigation destinations and a seven-dataset validator.
- The fixed follow-up branch was reconciled to that `main` and contributes only net-new corrections: costs-page event-access wording and quick-fill example; the activities callout wording + CS2-event-guide link; the radio stream wording; and the activities tournament records updated for the 9 October Virtus.pro → NIP substitution. No record was added, removed or renamed.
- Counts and gates on the reconciled branch: validator **PASS** (7 datasets / 176 records / 307 logged URLs / 15 HTML pages / 181 link attributes / 9 nav destinations / 25 expense rows); `check_javascript.py` and `node --check js/site.js` **PASS**; `npm test` **PASS** (11/11 Playwright, 320/360/768/1440 px, axe, parity, planner); `git diff --check` **PASS**.
- Open items are unchanged from the sections below and `docs/OPEN_QUESTIONS.md`: the FAQ answers, the Saturday/Sunday agenda, the attendee gate and walk, the TQ1 monitor, the October single fare, and the taxi tariff's April-2022 vintage.
- Delivery: the branch is pushed and PR #44 carries these corrections; the merge and the Pages build are recorded here only after they are observed.

## Integration state

- Work is on the fixed session branch `arena/27302b08-maltasupplemental`, which began at `b307c51` — `main` after PR #33.
- **Pull request #42 (workstream H, the CS2 event guide) was still open and conflicting when this session started.** Its branch `arena/154ca483-maltasupplemental` (commit `0c8e8bb`, squashed rebase onto `de3303f`) added `data/event.json`, `event.html`, two transport records (TQ1 special event services, the Transport Malta taxi tariff) and a richer evidence set.
- **The merge was reconciled by content, not by side.** Five files conflicted — `README.md`, `index.html`, `data/expenses.json`, `docs/STATUS.md`, `docs/FINAL_REPORT.md`. The merge keeps `#42`'s verified additions (venue, dates, agenda, fares, taxi tariff, TQ1, radio leads, the event page) **and** this branch's evidence caveats (no reservation held, inventory/attendee gate/weekend agenda unpublished). A line-level check confirmed that **no `#42` addition was silently dropped** in the files that auto-merged; the two documents that were deliberately taken from this branch's side were rewritten in this session, so nothing is lost.
- Integration totals: **7 data files / 176 exact-schema records** (transport 28, food 38, activities 39, everyday 18, radio 20, event 8, expenses 25), **307 unique record URLs** in the source log, **15 HTML pages / 178 link attributes**, **9 shared navigation destinations**, and all **25 expense rows**.

## What this session verified instead of inheriting

Every source below was fetched directly in this session; none of these rows is copied from an earlier session's notes. Full rows are in `docs/SOURCES.md`.

| Source | What it settled | What it did **not** settle |
|---|---|---|
| Eventbrite listing for the Finals | Venue/address, 14–18 October, 09:30 AM–10:30 PM agenda rows for Wed/Thu and 14:00–21:00 for Fri, "ages 18+ / In person", a "Free" ticket block with "Reserve a spot", "Sales end soon", map pin 35.8957343, 14.4168839 | No FAQ answers rendered (parking, per-day scanning, transferability, catering), no attendee gate, no confirmation that this traveller holds a reservation |
| MPT fares page | The full fare table (winter €2.00 / summer €2.50 / night €3.00 / special €3.00 / TD €3.00 / TD1 €3.50), 2-hour transfers, €50 fine, card products (€19 / €25 / €27 / €7), Buġibba sales office | The page's only dated statement is the **expired** winter window (19 Oct 2025 – 13 Jun 2026); the fare applying 13–19 October 2026 is still unpublished |
| MPT Route 186 page | Both Friday/Saturday diversions (8 PM–midnight ending 21 April; 7 PM–midnight starting 17 October, omitting Gholja 2 → Targa toward Buġibba), the Saqqajja stop closure, Stadium stop 6227 departures to 22:04 (Rabat-bound direction) and Qawra-side departures to 21:40 | The diverted path is not published; the static variants are not a date-specific journey; the Buġibba → Qawra connection is still unverified |
| MPT TQ1 page | Still shows "Timetable not available!"; no Thunderpick special service announced | Whether MPT will add an event service — check daily during 14–18 October |
| Transport Malta taxi page | The regulated **maximum** meter tariff, the €4.50 holiday surcharge, 250 Malta / 50 Gozo licensed taxis — and the footer "Page last updated: 06/04/2022" | Current maxima (the page has not been re-published since 2022); any actual quote |
| NET FM schedule | Friday 18:30 "Mhux Premier biss", Saturday 16:00 "Hits & Score", Sunday 15:00 "Sports Box", plus news bulletins | Any dated 16–18 October running order, time zone statement, or promise of commentary on a named fixture |
| AX ODYCY property + FAQ pages | Address/contact, 4-star seafront property; room list including "Deluxe Room with Side Sea View"; guest rooms with three Type G + three two-pin sockets and a **razor-only** 110 V bathroom socket; free Wi-Fi, in-room safe, underground parking, level-11 adults-only pool, water park, doctor on call 24 h against a charge, pharmacy via Guest Relations, ATM nearby, card acceptance with check-in pre-authorisation, **taxis arranged via Guest Relations at fixed charges**, car hire via Guest Relations, and the published tipping line (10–15% expected; no service charge at the hotel) | Dated check-in/check-out clock times, taxi fares, the firm used, meal plan, room allocation, and anything about this traveller's reservation |

## Cumulative verification passes (this session)

1. **Pass 1 — implementation and integration.** All seven topic datasets and the record schema parse. `scripts/validate_site.py` passes schema, source-log coverage, page/data wiring and local-link checks. The merge was verified by diffing every file both ways rather than trusting the merge tool.
2. **Pass 2 — requirements and evidence.** Newly added hotel-sourced claims were pushed back into the datasets they belong to (power, tipping, health, taxi, car hire) rather than hand-written into pages, so pages still render from data. The bus fare that applies in the trip week was labelled a **planning inference** everywhere it appears, because the operator's only dated fare statement has expired. Tipping is presented as *published guidance plus a conflicting secondary range*, never as a rule. The room-name mismatch ("Deluxe sea view" vs the hotel's "Deluxe Room with Side Sea View") was surfaced rather than smoothed over.
3. **Pass 3 — regression and consistency.** The full browser suite (11 tests: 320/360/768/1440 px rendering, axe WCAG 2A/AA/2.1AA, data/render parity for every record in every topic, navigation and deep links, planner defaults/CSV/localStorage/itinerary quick-fill) passes on the integrated tree. Stale-claim scans for the superseded "no public ticket sale found" and "€10.00 BLAST precedent" wording return only deliberate provenance notes.

## Local validation results (observed in this session)

- `python3 scripts/validate_site.py` — **PASS**: 7 JSON files, 176 exact-schema records, 307 unique record URLs present in `docs/SOURCES.md`, 15 HTML pages / 178 link attributes, 9 shared navigation destinations, 25 expense rows wired.
- `python3 scripts/check_javascript.py` — **PASS**.
- `node --check js/site.js` — **PASS**.
- `npm ci` — **PASS** (23 packages, 0 vulnerabilities reported).
- `npx playwright test` — **PASS, 11/11** in 1.2 minutes on the merged tree.
- `git diff --check` — **PASS**.

## Blockers and handoff

- **Event access:** no reservation is held by this project. Inventory, per-day validity/scanning, transferability, the attendee gate and the Sat/Sun agenda all remain unpublished; the listing itself says "Sales end soon" and is the only way to reserve.
- **Transit:** no date-specific end-to-end journey has been produced, no gate/hotel walk measured, no live taxi quote obtained and no Buġibba → Qawra connection verified. The 17 October diversion windows still differ between two MPT pages; plan the union 19:00–24:00 and re-check live. The trip-week single fare remains unpublished.
- **Radio:** still no physical FM/DAB+ scan, no reception measurement, no Malta carriage confirmation, and no named-match output on a locally receivable service. The DAB+ "Sports Channel" block/identity is a scan lead; a UK BBC listing is not Malta carriage.
- **Money/legal:** the MTA "15-night" question was **narrowed in this session** — the 2026 guidelines define the fifteen-day figure as an "interruption" in premises that do not require a licence within one visit, not a minimum-stay threshold — so six nights × €1.50 (about €9 per eligible adult) is ordinary arithmetic, still conditional on the invoice and on guest ages. The MTA webpage's different wording is recorded rather than smoothed over. The EES implementation conflict is recorded, not resolved.
- **Research coverage:** Google Maps/Spotify-style review snapshots and TripAdvisor informed parts of the food work; Yelp, Instagram, TikTok, Facebook and X were blocked or limited. Coverage is not comprehensive.
- **Traveller-specific unknowns:** booking confirmation, room allocation, party size/ages, flights, meal plan, actual ticket, device, insurance and personal expenses. The planner stays blank until they are supplied.

Workstream ownership and next-session tasks are in `docs/PLAN.md`; cross-topic findings are in `docs/HANDOFF.md`; unresolved items are in `docs/OPEN_QUESTIONS.md`; the delivery summary is in `docs/FINAL_REPORT.md`.
