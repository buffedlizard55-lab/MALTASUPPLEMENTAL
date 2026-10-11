# Malta trip guide — work plan

## Scope and repository review

The deliverable is a sourced, mobile-friendly Malta trip guide and a blank-by-default expense planner for the traveler-supplied 13–19 October 2026 stay at AX ODYCY in Qawra, with “BLAST Arena Studios, Attard” as the user-supplied event destination. These are planning inputs, not independent confirmation of a booking, ticket, public entrance, event schedule, or exact venue pin. The site is a static HTML/CSS/JavaScript project with JSON-backed pages, shared navigation and renderer, offline validation, and browser regression tests; no production build step is needed.

Review the repository and existing evidence before edits. Preserve useful main-branch work and its source history; reconcile upstream changes instead of replacing them. The baseline validator checks structure, not the truth of external claims or current link availability.

## Shared setup (serial, before topic work)

1. Use the canonical exact 13-field record schema: `id`, `name`, `category`, `area`, `address`, `hours`, `price range`, `description`, `source_url`, `source_type`, `date_checked`, `confidence`, and `notes`. Keep every record within that schema; topic pages must render the data rather than duplicate or contradict it.
2. Keep the site dependency-light. Preserve the shared renderer, styles, navigation, page structure, and the expense planner's blank defaults unless integration/testing identifies a concrete defect.
3. Maintain `docs/SOURCES.md` (claim, URL, access date, workstream, and limitation), `docs/OPEN_QUESTIONS.md` (missing/conflicting or unresolved details), `docs/STATUS.md` (progress/blockers), and `docs/HANDOFF.md` (cross-workstream discoveries).
4. Prefer primary operator, organizer, station, government, or official provider sources for current facts. Attribute community and social evidence by source and date. Every factual claim needs a traceable source and an appropriate confidence/uncertainty label; do not present unverified claims as fact.
5. The current canonical schema allows exactly `official`, `map`, `review`, and `social`. Label a specialist directory by its publisher/source provenance (the current enum does not include `directory`) and explain in notes that a technical-directory entry does not prove local reception. Do not expand or silently change the schema enum. Where platform coverage is incomplete, document the attempt and limitation rather than implying comprehensive research.

## Parallel-work and ownership protocol

The repository must be reviewed and this ownership plan maintained before topic work. Complete shared schema/source-log setup serially. The Arena checkout is fixed to `arena/3a5297d2-maltasupplemental`; there is no isolated sub-agent or workstream-branch runner in this environment, so execute A–F one at a time on this branch. Each workstream edits only its owned topic data/page files. Do not make cross-workstream edits during another workstream; record relevant discoveries in `docs/HANDOFF.md`. Workstream G performs serial integration and owns shared files, source/audit documentation, validation, and reporting. Avoid concurrent edits to shared files.

## Workstreams, owned files, scope, and dependencies

| Workstream | Owned data file(s) | Owned page(s) | Scope | Dependencies |
|---|---|---|---|---|
| A. Transport | `data/transport.json` | `getting-around.html` | MLA airport ↔ AX ODYCY; Qawra ↔ the user-supplied BLAST Arena Studios destination; event-day public-transit routing; ferries, taxi/ride-hailing, and car hire. Compare convenience, price, value, and feasibility. MFCC/Ta’ Qali references are venue-area context only unless TWC-specific logistics are verified. | Shared schema and renderer; event pin/timing uncertainties go to `docs/OPEN_QUESTIONS.md` or `docs/HANDOFF.md`. |
| B. Food & cafés | `data/food.json` | `restaurants.html` | Sourced restaurants, cafés, and casual eating near Qawra/AX ODYCY and relevant Malta areas; distinguish official facts from Maps/review/social snapshots and record platform access limits. | Shared schema and renderer. |
| C. Activities, landmarks & events | `data/activities.json` | `activities.html` | Gaming venues, recreation, landmarks, and dated public events during 13–19 October. Distinguish confirmed dated listings from seasonal/undated suggestions; do not infer spectator access or public match times. | Shared schema and renderer; transport/event cross-notes go to `docs/HANDOFF.md`. |
| D. Everyday life for a U.S. traveler | `data/everyday.json` | `everyday.html` | Power, mobile service, currency/cards, tipping, safety/emergency/health, entry pointers, language, weather, and practical adaptation. Qualify advice dependent on passport, device, carrier, or itinerary. | Shared schema and renderer. |
| E. Malta radio sports | `data/radio.json` | `radio.html` | Live broadcast receivable on a radio device/frequency in Malta and official station/program schedule evidence for 13–19 October where available. Separate named-match carriage, station schedules, reception, and online streams; fixture listings or streams alone do not prove radio carriage. Log unverified gaps. | Shared schema and renderer; published schedules, reception, and match carriage may remain unconfirmed. |
| F. Expense planner | `data/expenses.json` | `costs.html` | Editable, blank-by-default trip categories and day-by-day rows; budget/actual totals, browser-local autosave, CSV export, and reset. Do not assume flight/hotel cost, party size, ticket purchase, actual itinerary, or reimbursement. | Shared schema; use A–D evidence as context without turning examples into estimates. |
| G. Integration | Shared files: `index.html`, `css/style.css`, `js/site.js`, `README.md`, `sources.html`, `docs/*`, `.github/workflows/validate.yml`, `scripts/validate_site.py`, test/config files, `.nojekyll`, and legacy-page notices | `index.html`, `sources.html`, shared navigation and styles | Executive summary, accessible responsive layout/navigation, shared data rendering, hosting/docs, source and audit integration, automated validation/browser tests, Pages readiness, and final reporting. Integrates after A–F without rewriting unsupported topic facts. | All topic workstreams complete; cross-topic findings arrive through `docs/HANDOFF.md`. |

## Research and evidence requirements

Investigate Google Maps/Google Reviews, Yelp, Instagram, TikTok, Facebook, Reddit, and X, and record source coverage, date, access restrictions, and any unavailable/private/login-gated results. Do not invent review scores, popularity rankings, schedules, prices, opening hours, route connections, broadcast rights, reception, or ticket availability. Record supporting URLs and claim-specific limits in `docs/SOURCES.md`; place missing, conflicting, or unverified facts in `docs/OPEN_QUESTIONS.md`. A route-level timetable is not a door-to-door journey, and a fixture list, online stream, or general sports programme is not evidence of named-match carriage on a Malta radio frequency.

## Three cumulative verification passes

1. **Implementation pass:** validate JSON/schema/enums, source-log coverage, JavaScript syntax, page/data wiring, local paths/anchors, navigation, and expense-planner behavior where the available environment permits. Check local endpoints and data/page consistency.
2. **Requirements and evidence pass:** review every requested topic and handoff; check factual claims against named sources, date/confidence/uncertainty labels, inaccessible-platform disclosures, and unresolved facts. Fix unsupported or contradictory claims without weakening scope.
3. **Final audit pass:** line by line, compare the request with pages/data/reports; repeat structural and functional checks; assess desktop and mobile layout, navigation, internal/external links, and data/page consistency; update sources/open questions/status/handoffs/final report. State what live-link, physical-reception, and graphical visual checks could not be completed. Then inspect the explicit PR, CI, mergeability, and Pages delivery state.

## Historical reconciliation and verification notes

### PR #13 / main reconciliation (10 October 2026)

PR #13 was based on an older implementation that added duplicate `/pages/` templates and a separate site builder. The canonical root-page renderer, shared schema/validator, current topic datasets, expense planner, and research pages were retained. Non-duplicate food/activity records and their source/open-question/status/handoff notes were integrated; the Aquarium and Rolex race facts were updated. Duplicate `/pages/` copies, `tools/build_site.py`, legacy `data/schema.json`, and a duplicate schema document were removed; `.nojekyll`, `docs/DATA_SCHEMA.md`, and the canonical validator were retained. Legacy `hotel.html`, `itinerary.html`, and `qawra.html` URLs remain noindex notices. No unsupported claim was imported.

### Additional 11 October verification pass (PR #28)

The upstream PR #28 work added the `record["price range"]` validator regression guard, a transport mode-comparison summary, bidirectional `Il-Qawra` stop `Arznell (950)` TD1 timetable evidence, U.S. State Department confirmation of 112 emergency services/private-hospital payment expectations/AmEx and ATM notes, and the BBC *Sportsworld* 11 October EPL billing precedent. These sources are historical and claim-specific; they do not establish all event-day journeys, Malta reception, or named-match carriage. The refreshed source/audit documents retain limitations and checked dates.

### Current delivery session — PR #31

All work remains on `arena/3a5297d2-maltasupplemental`. PR #31 is the delivery target. Preserve and inspect later `origin/main` changes before updating the PR branch; rebase safely, reconcile conflicts without dropping relevant content, rerun the cumulative checks, push only this branch, review CI/diff/mergeability, and merge PR #31 by its explicit number when safe. Current audit details and unresolved facts are recorded in `docs/STATUS.md`, `docs/HANDOFF.md`, `docs/OPEN_QUESTIONS.md`, `docs/SOURCES.md`, and `docs/FINAL_REPORT.md`.

### Second 11 October 2026 session (post-merge verification)

Work continued on the fixed session branch `arena/96208136-maltasupplemental` after PR #31 merged. Because this environment has no isolated sub-agent runner, the same ownership-guided serial model was used: workstream A (fares, venue/admission, ride-hailing), E (DAB+ carriage and Kalshi eligibility) and D (power, eco-contribution, weather) were refreshed first, then the shared files (index shell, transport/radio/everyday/costs pages, README and research records) were updated once, in one pass, so no two writers touched a file in the same step. New findings that belong to another workstream are recorded in `docs/HANDOFF.md` rather than edited across owners.

Evidence rules unchanged: every record keeps the canonical 13 fields, every cited URL is logged in `docs/SOURCES.md` with its access date and limitation, and unresolved items moved to (or stayed in) `docs/OPEN_QUESTIONS.md` rather than being inferred. The refresh resolved two long-standing items (published bus fares; the MTA “15-night” wording) and upgraded one previously unverified radio lead (DAB+ block 6C talkSPORT carriage) to a partially verified listing with its content still open.

### Merged third-pass outcome — 11 October 2026

- **Two 11 October sessions reconciled in one branch:** the session already merged via PR #32/#34 (`ad7226c`: exact fares, admission negative finding, DAB+ tuning guide, power, eco-contribution, Kalshi eligibility, Uber conflict, “10-minute intake”) and this session (venue confirmation, attendee-status record, customs record, receiver compatibility, page rewrites, itinerary quick-fill). Neither session's evidence was dropped; where they disagreed the more cautious reading was adopted and the disagreement is disclosed in the record text.
- **Ownership respected:** this session touched only its own page/data/files plus the shared files it owns as workstream G (nav-adjacent prose on `index.html`, `css/style.css`, `tests/site.spec.js`, `docs/*`, `README.md`), and merged rather than reformatted the other session's work.
- **Gates on the merged tree:** validator PASS (140 records / 242 URLs / 130 link attributes / 25 planner rows), JavaScript syntax PASS, Playwright 10/10 PASS.
- **Handed to the traveler:** the itinerary text itself, party size/ages, booked prices, organizer attendee information. Remaining open questions are listed in `docs/OPEN_QUESTIONS.md`.
## Venue-confirmation session (11 October 2026, on top of `origin/main` ad7226c)

Scope for this pass was deliberately narrow: re-verify the claims that carried the most planning risk, correct everything they invalidated, and re-run the full gate set. The shared schema, renderer, styles, navigation, expense-planner defaults and the six-file data layout were left untouched, so the ownership boundaries in the table above still hold. The parallel 11 October pass already on `main` (fares, card sales points, talkSPORT/Vibe FM leads, Uber quote) is preserved and extended, not replaced.

Priorities, in order: (1) confirm the attendee venue, dates, daily times and access from a primary source; (2) re-derive anything that depended on those being unknown — fare by trip date, event-day return feasibility, expense-planner guidance; (3) resolve the recorded BBC service-label mismatch; (4) extend weather coverage to the full stay; (5) re-read the Route 186 diversion notice verbatim and record its ambiguity rather than smoothing it over.

Two evidence rules adopted here. First, when a source states a window for one season only, any extension to the trip dates is recorded as an inference and kept at “partially verified”, not promoted to “verified” — this is why the October fare conclusion is labelled as an inference from the published winter boundary. Second, when two directories disagree on a technical fact such as a DAB+ block, both readings are published side by side and the action becomes “scan both”, rather than picking the more convenient one.

## Historical reconciliation and verification notes

### Post-merge verification session (after PR #31)

PR #31 was already merged into `main` when this session began, so the session branch started at parity with `main`. This session therefore performed a **forward verification and enrichment pass** rather than a rebase. Work remained on `arena/58d6d232-maltasupplemental` throughout.

Corrections and upgrades made, each traceable to a source read during this session:

1. **Venue disambiguation (workstream A).** “BLAST Arena Studios, Attard” and “Ta’ Qali” are the same complex. Verified from BLAST’s own attendee guide (“Malta Fairs & Conventions Centre – BLAST Arena Studios … Ta Qali, ATD 4000 Ħ’Attard”), EventWorks, GamingMalta and the visitmalta.co.uk directory. The prior dataset hedged this as unresolved; routing is now settled while *access* remains open.
2. **Two Route 186 detours, not one (A).** The operator’s own route page lists both a recurring Friday/Saturday 20:00–00:00 notice ending ~21 April and a 19:00–00:00 notice starting 17 October. Both omit stops “from Gholja 2 through Targa” toward Buġibba. Only the 17 October one was previously recorded.
3. **“Sports Channel” upgraded from an unverified lead (E).** Previously recorded as `unverified` with no operator identity. A specialist ensemble listing labels it “Sports Channel (Talk Sport)” at 185.360 MHz, two independent scanner directories place Sports Channel on 185.360 MHz, and the Premier League’s own partner page confirms talkSPORT’s live-commentary rights. It is now `partially verified` and is the page’s primary recommendation, with the identity caveat retained. The WorldDAB 12A placement is recorded as a likely mis-assigned table (its 12A table contains “6c_Test7”/“6c Test12” entries).
4. **Fixture times converted to Malta time (E).** EPL matchweek 8 and Serie A matchday 7 are now listed in Malta time with the conversion rule stated (Malta CEST = UK BST + 1 hour until both change on 25 October; Italy and Malta share CEST, so Serie A times apply directly).
5. **Social/review gap partially closed (B).** Reddit threads and TripAdvisor/Google listing snapshots were reachable through search, adding a popularity snapshot and a community shortlist. Yelp, Instagram, TikTok, Facebook and X remained inaccessible; this limitation is disclosed on the page rather than filled with guesses.

No previously verified claim was weakened without cause, and no unsupported claim was introduced. Every URL cited in a record is logged in `docs/SOURCES.md`, which the offline validator enforces.

## Session plan — 11 October 2026 (branch `arena/b7b7ea21-maltasupplemental`)

### Repository review conclusion

The repository already contains a complete, mature implementation of the requested guide: a static
GitHub Pages site (`index.html` plus six data-backed topic pages and `sources.html`), a shared
accessible renderer (`js/site.js`), design tokens (`css/style.css`), six canonical JSON datasets on
the exact 13-field schema, an offline validator (`scripts/validate_site.py`), a JavaScript syntax
gate (`scripts/check_javascript.py`), and a Playwright/axe browser suite. GitHub Pages is publishing
the `main` root and reported `built` for `4ed9c5a`. Both baseline gates pass on arrival
(128 records, 205 unique logged record URLs, 25 expense rows).

Therefore this session does **not** re-scaffold. It runs the same A–G ownership protocol as a
fresh verification-and-extension pass against the live sources, because the trip now starts in two
days and several previously "beyond the forecast window" or "unpublished" items have become
checkable.

### Workstream scope for this session

| Workstream | Owned files | This session's work |
|---|---|---|
| A · Transport | `data/transport.json`, `getting-around.html` | Re-read Route 186 end-to-end in both directions; establish the return-leg terminus and the Qawra transfer problem; re-read the fare table and its stated validity window; add trip-specific fare scenarios; confirm the 17–18 October Ta' Qali/Mosta evening detour cluster. |
| B · Food & cafés | `data/food.json`, `restaurants.html` | No new claims. Existing records retain their dated snapshots; re-verification of all 29 records against live operator pages is out of scope for one session and is logged as a next-session task. |
| C · Activities | `data/activities.json`, `activities.html` | Resolve the archived "Dash Berlin at UNO Malta" lead on the official ticketing platform; add the Ħamrun Chocolate Festival; record PLAYCON 2026 as explicitly outside the trip window and use it to corroborate the MFCC address. |
| D · Everyday | `data/everyday.json`, `everyday.html` | Extend the weather record to 18–19 October; document the EES implementation conflict between the official EU position and secondary September 2026 reporting. |
| E · Radio sports | `data/radio.json`, `radio.html` | Resolve the BBC service-label discrepancy (programme owner vs broadcast service), add Malta-time conversions for the six named EPL commentaries, and cross-check them against the official fixture record already in the dataset. |
| F · Expenses | `data/expenses.json`, `costs.html` | No structural change; the planner is already blank-by-default and quick-fill. Add the newly verified fare inputs as optional dated reference notes only, never as prefilled amounts. |
| G · Integration | `index.html`, `README.md`, `docs/*`, `sources.html` | Update the executive summary, day framework, source log, open questions, status, handoff, audit and final report; run all gates; open and merge the PR; confirm Pages rebuild. |

### Evidence rules applied this session

1. Every new claim was read directly from a fetched page in this session and is dated 2026-10-11.
2. Timetable variants on a single operator page are reported as ranges with the variant caveat,
   never collapsed into one "official" clock time.
3. A fixture list, a market listing or an internet stream is never treated as radio carriage; a UK
   broadcast listing is never treated as Malta reception.
4. Search-result snippets that could not be confirmed by a direct page fetch are recorded as leads in
   `docs/OPEN_QUESTIONS.md` and are **not** promoted into data records.
5. Arithmetic (fares × journeys, nights × contribution rate) is labelled as arithmetic, with its
   inputs stated, and is never presented as a quoted price or a confirmed charge.

### Outcome of this session's plan

All workstreams completed except two deliberate scope decisions, recorded here rather than left implicit:

- **B · Food** — unchanged, as planned. No new claims; the fresh all-platform re-verification of all 29 records is carried forward as next-session task 6 in `docs/FINAL_REPORT.md`.
- **F · Expenses** — **deviation from plan.** The plan said to add the newly verified fare inputs as optional dated reference notes in `data/expenses.json`. That was not done: the same inputs are already published in `mpt-fares-cards` and `trip-fare-scenarios-13-19-oct` on the transport page and summarised in the `index.html` executive summary, so duplicating them into the planner's data file would have added a second place for one fact to go stale while giving the traveller nothing new. `data/expenses.json` and `costs.html` are therefore untouched and the planner remains blank-by-default with all 25 rows intact.
- **Diff discipline** — a key-order normalisation across all six datasets (the repository stores the 13 fields in two different orders) was started and then **reverted**. It touched 59 records with zero content change, which would have buried the real edits in an unreviewable diff. New records follow the dominant field order of the file they join. Canonicalising the order repo-wide should be its own commit if it is ever wanted.

Gates after the pass on this branch alone: `python3 scripts/validate_site.py` PASS (134 records / 228 URLs / 119 link attributes), `python3 scripts/check_javascript.py` PASS, `npm test` 9/9 Playwright PASS in 36.2s, `git diff --check` clean. **After reconciling with `main`, which had advanced through two further passes to 140 records, the merged tree passes at 162 records / 275 logged URLs / 145 link attributes with 10/10 Playwright tests** (the tenth arrived with `main`). An order-insensitive comparison of every record against `HEAD` confirmed exactly five content changes and six additions, no removals, and no unintended `intro` edits.
