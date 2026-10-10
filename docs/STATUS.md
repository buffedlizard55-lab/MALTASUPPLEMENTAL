# Workstream status

Last updated: **2026-10-10**. Status labels: `not started`, `in progress`, `blocked`, `verified`, `integrated`.

| Workstream | Status | Files | Verification and remaining limits | Last updated |
|---|---|---|---|---|
| Shared setup | integrated | `docs/PLAN.md`, `docs/SOURCES.md`, `docs/OPEN_QUESTIONS.md`, `docs/HANDOFF.md`, `docs/STATUS.md`, `css/style.css`, `js/site.js` | Shared record schema uses the requested `price range` field; responsive shell, navigation, renderer and evidence registers are in place. Six topic datasets contain 70 records; every recorded source URL was reconciled to the source log. | 2026-10-10 |
| A. Transport | integrated | `data/transport.json`, `pages/transport.html` | Eight source-linked records and route/airport/taxi/rental comparisons are integrated. MPT's static Route 186 snapshot lists Qawra stop 952 at 06:10–21:38; the normal return runs via St Paul's Bay/Buġibba rather than Qawra seafront, with last listed arrival Buġibba Bay 1 at 21:26. Event entrance/session, exact boarding stop/venue walk, detour impact and 2026/27 fare season remain open (Q-003–Q-006). | 2026-10-10 |
| B. Food & cafés | integrated | `data/food.json`, `pages/food.html` | Eight Qawra-area venues are integrated with dated platform observations kept separate, not averaged. October menus, hours, exact meal costs and platform-access limitations remain as recorded (Q-007, Q-013). | 2026-10-09 |
| C. Gaming, activities, landmarks & events | integrated | `data/activities.json`, `pages/activities.html` | Twenty source-linked records are integrated. TWC public access, Gamers Lounge public-session pricing, Esports Plaza status, Esplora free-day inclusions and the Picnic/closure conflict remain unresolved (Q-003–Q-004, Q-015–Q-019). | 2026-10-09 |
| D. Everyday life for a US traveler | integrated | `data/everyday.json`, `pages/everyday.html` | Fourteen records are integrated with linked official/verifiable sources. Actual passport, itinerary, carrier and medication are unknown; ETIAS and weather are volatile; no authoritative fixed tipping percentage was found (Q-011, Q-020–Q-024). | 2026-10-09 |
| E. Radio sports broadcasts | integrated | `data/radio.json`, `pages/radio.html` | Two date-specific BBC World Service Sportsworld entries are integrated at 15:06 on 17 Oct and 16:06 on 18 Oct Malta time. Published 3h53 duration calculations give 18:59/19:59 ends, immediately before the next schedule entries. No fixture commentary is named; WorldDAB is an industry directory and hotel reception is untested (Q-009–Q-010). | 2026-10-09 |
| F. Expense planner | integrated | `data/expenses.json`, `pages/expenses.html` | Eighteen source-linked price/unknown records accompany four trip-level and 28 date-specific blank lines. Custom items, quantity arithmetic, budget comparison, optional user-entered FX, local-only storage, CSV export, print and reset are implemented. No meal, taxi, FX, tax, tip, attendance, payment or coverage is assumed; blanks are not free. | 2026-10-09 |
| G. Site shell, executive summary & integration | integrated | `README.md`, `index.html`, `sources.html`, root compatibility pages, shared CSS/JS and integration docs | Executive summary and navigation match the supplied 13–19 Oct trip; legacy routes redirect and old prize/legal material is retired. The offline integration gate passes (70 records, 112 local links/assets/fragments), and JSDOM interaction checks passed. GitHub Pages reported `built` for merge commit `c4a33ec`; external URL liveness and actual browser/device rendering remain unverified. | 2026-10-10 |

## Three cumulative review passes

1. **Pass 1 — implement and source-check:** A–F records/pages and shared shell completed; required fields, allowed source/confidence values, ISO check dates, per-file unique record IDs, source-log URLs/IDs and open-question references were checked. The final dataset count is 70 records across six JSON files.
2. **Pass 2 — independent accuracy review:** rechecked supplied date boundaries and weekday labels, the conditional six-night calculation, all 32 blank starter lines, and the two BBC duration/time-zone calculations. Reviewed source-log coverage for primary/additional data URLs and retained volatile, unpublished, inaccessible or conflicting items as open. The planner exposes 39 unique optional source-price choices; unconfirmed gaming/event items do not get add-to-plan prices.
3. **Pass 3 — integration and usability:** verified all local HTML paths, fragments and assets; ran `node --check js/site.js` and the CSS brace check; exercised the overview, evidence page and all six topic pages in JSDOM at a 390 px viewport. Shared navigation, mobile-menu state, data rendering, topic search/filter, expense arithmetic, paid/remaining totals, budget/FX inputs, local saving, adding/resetting items and CSV action passed without JavaScript errors.

## Remaining traveler-specific and pre-trip actions

- Confirm the hotel reservation/check-in/out, room total, flights, luggage, arrival/departure times and traveler count; enter only confirmed costs in the planner.
- Confirm whether and when the traveler will attend TWC, the ticket/access terms and event-specific entrance; then run MPT's date/time Journey Planner for the venue and return, especially around the 17–18 Oct route notice.
- Recheck fares/card terms, venue prices/hours, event availability, forecast and entry requirements near departure. Confirm personal phone-plan and medication requirements directly with the relevant provider/authority.
- Recheck the BBC schedule and local DAB+ lineup/reception before the radio slots; do not infer a named match from the Sportsworld listings.

## Current execution note

This session is constrained to branch `arena/785456db-maltasupplemental`. Workstreams were performed serially on that branch, following the file ownership in `docs/PLAN.md`. PR #12 merged to `main` as `c4a33ec` on 10 October 2026. GitHub Pages reports the merge build as `built`; that status does not substitute for testing the public page in a browser or on a real device.

## Latest-main reconciliation

While PR #12 was open, `main` advanced with a parallel refocus change. Its added hotel/base/itinerary drafts asserted an unprovided room type, SFO departure and event attendance. This branch keeps the user-supplied-only trip facts: those routes are now noindex redirects, and the unused conflicting `data/trip.json` / `data/venues.json` copies were removed. The six topic datasets remain canonical. The upstream schema documentation and verification-script entry points were retained and corrected for this site's `records` structure and Pages-safe paths.
