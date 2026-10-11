# Delivery status — Malta trip guide

**Last updated:** 11 October 2026 (UTC)
**Session branch:** `arena/cc913a9b-maltasupplemental`

## Integration state

- The session began at `b307c51`. During work, `origin/main` advanced via PR #42 to `5cdea689` (merged 11 October 2026); the latest main was fetched and integrated on this fixed branch, and its CS2 event guide was retained and re-audited.
- The Route 186 notice correction and the associated event-bus/page/docs reconciliation are included in the local candidate. Local validation has passed. The delivery PR from this session branch has not yet been created or pushed at this report snapshot.
- PR #42 is an upstream merged change, not this session’s delivery PR. This file is a dated snapshot, not a live GitHub/Pages dashboard.

## Workstream status

| Workstream | Status | Current blockers / next action | Last updated |
|---|---|---|---|
| **A · Transport** | Updated; evidence-qualified | Both current MPT pages show the 17 Oct Route 186 notice at 19:00–00:00; a separate 20:00 notice ends around 21 April. No union is appropriate. Route 214 and TQ1 are route-level possibilities, not saved journeys. Run the dated planner after confirming attendee gate/finish; fare and safe walks remain open. | 2026-10-11 |
| **B · Food & cafés** | Existing data/page retained; platform coverage limited | Recheck selected operators and volatile hours/menus close to travel. Yelp, Instagram, TikTok, Facebook and X were blocked or limited; accessible review/search snapshots are not comprehensive. | 2026-10-11 |
| **C · Activities, landmarks & events** | Existing data/page retained; event claims qualified | Confirm current availability, access and event times directly. Keep social-search-derived dates and provisional details identified as such. | 2026-10-11 |
| **D · U.S. traveler everyday guide** | Existing data/page retained; official-text conflicts open | Clarify EES enforcement and MTA short-stay contribution wording with authorities; traveler’s entry documents and booking remain unknown. | 2026-10-11 |
| **E · Malta sports radio** | Separate radio section implemented; reception not verified | Scan FM/DAB+ at the hotel/event area, confirm named-match carriage with stations, and check stream access and Rai’s trip-week running order. Directories and UK schedules are not local reception/carriage proof. | 2026-10-11 |
| **F · Expense planner** | Implemented and validated; blank by default | Await itinerary, party size, booking, tickets and actuals. No personal costs are assumed; export CSV before changing devices. | 2026-10-11 |
| **H · CS2 event guide** | Integrated from merged PR #42; re-audited | Eventbrite registration is not the traveler’s ticket. Confirm inventory, attendee gate, daily validity/scanning, exact finish-time discrepancy, and the 17–18 Oct agenda. | 2026-10-11 |
| **G · Site integration** | Local validation passed; delivery PR pending | Seven datasets/pages and the inherited event guide are integrated; three cumulative passes are complete. Create a PR from this branch and inspect GitHub checks/mergeability. | 2026-10-11 |

## Current transport reading

- MPT’s Route 186 page and latest-service-updates page both show the 17 October notice as **19:00–00:00**, ending 18 October at approximately midnight. The distinct older **20:00–00:00** notice ends around 21 April and is not a conflicting October window. The intermediate 19:00–24:00 “union” wording is superseded.
- The October notice omits stops Gholja 2 through Targa toward Buġibba. MPT publishes no replacement path and does not say whether a particular Stadium trip or onward Qawra connection changes. The “weekly on Friday, Saturday” wording does not establish a 16 October diversion (the stated start is 17 October) and leaves later recurrence unclear.
- Route 214’s static page lists Qawra stop 952 and Ta’ Qali Qali 2 stop 2542. TQ1’s route page had no timetable and no TWC-specific service was found. These are candidates to check, not event itineraries. One 20:53 Route 186 departure is a single static variant, not evidence that the whole network stops then.

## Cumulative verification passes

1. **Implementation pass:** reviewed the repository and existing schema/site before topic work; reconciled the PR #42 event page/navigation; validated data/page/source-log wiring, the expense planner and responsive shell.
2. **Requirements and evidence pass:** corrected the Route 186 false conflict/union; separated the expired notice; qualified Route 214, TQ1 and taxi references; preserved unknown journey, gate, schedule, fare and radio-reception facts; documented social-platform access limits.
3. **Final audit pass:** searched for superseded route/return claims, reconciled upstream content on the fixed branch, reviewed page/data/source consistency, inspected the diff, and reran local schema, JavaScript, browser/mobile and accessibility checks.

## Local validation results

- `python3 scripts/validate_site.py` — **PASS**: 7 JSON files / 175 exact-schema records / 305 unique record URLs in `docs/SOURCES.md` / 15 HTML pages / 170 link attributes / 9 shared navigation destinations / 25 expense rows.
- `python3 scripts/check_javascript.py` — **PASS**.
- `node --check js/site.js` — **PASS**.
- `npm test` — **PASS**, 11/11 Playwright tests, including 320/360/768/1440 px layouts, axe, navigation, data rendering and expense-planner cases.
- `git diff --check` — **PASS**.

## Remaining blockers

- **Event access:** current ticket inventory, the traveler’s own reservation, daily scanning/validity, attendee gate, on-site logistics, the headline 22:00 vs Wed/Thu 22:30 finish discrepancy, and Saturday/Sunday agenda remain unconfirmed.
- **Transit/fare:** no date-specific end-to-end MPT journey was saved. Compare Route 186, Route 214, other live services and any TQ notice after confirming the gate/finish; check walking sections and diversion effect; confirm October single fare. Keep a live taxi/ride-hailing quote as fallback only if no suitable bus appears.
- **Radio:** no physical FM/DAB+ scan/reception measurement, Malta carriage confirmation, named-match output, BBC Sounds/RaiPlay access check, or Rai trip-week running order was verified.
- **Everyday guidance:** MTA’s official texts do not expressly reconcile short-stay treatment of the “15-night” wording; six-night €9 is conditional arithmetic only. EU and secondary EES statements remain unreconciled.
- **Research coverage:** Google Maps/Reviews, TripAdvisor and some Reddit/search snapshots were accessible; Yelp, Instagram, TikTok, Facebook and X direct access was blocked or limited. The evidence sample is not comprehensive.
- **Traveler inputs:** flights, booking terms, party size/ages, meal plan, ticket, devices, insurance, itinerary and personal expenses remain unknown.

Source access dates and claim limits are in `docs/SOURCES.md`; unresolved items are in `docs/OPEN_QUESTIONS.md`; cross-topic findings are in `docs/HANDOFF.md`; ownership/scope is in `docs/PLAN.md`; the audit summary is in `docs/FINAL_REPORT.md`.
