# Malta trip guide — implementation plan

## Repository review and scope reset

The repository is a hand-authored static HTML/CSS/JavaScript site with no application build or test setup. The existing content described a different 13–20 October itinerary and included prize/legal/privacy material outside the requested tourism guide. The work resets it to the traveler-supplied Malta trip window (13–19 October 2026), AX ODYCY in Qawra, and the named BLAST Arena Studios location. User-supplied booking details remain planning inputs unless independently corroborated; event access and route facts are not inferred.

## Shared setup (serial, before topic work)

1. Define one common JSON record schema: `id`, `name`, `category`, `area`, `address`, `hours`, `price_range`, `description`, `source_url`, `source_type`, `date_checked`, `confidence`, and `notes`.
2. Preserve a dependency-free static site. Topic pages render from their workstream JSON data; the expense planner uses a blank-by-default editable form backed by its expense JSON categories.
3. Maintain `docs/SOURCES.md` (claim, URL, UTC access date, workstream, limitation), `docs/OPEN_QUESTIONS.md` (missing/conflicting details), `docs/STATUS.md` (progress/blockers), and `docs/HANDOFF.md` (cross-topic findings).
4. Prefer primary operator, organizer, venue, station, government, or official provider pages for current details. Label review/social snapshots separately. Do not present a fixture list as radio carriage or a route-level bus timetable as a door-to-door trip.
5. Review the repository before any parallel topic work, create this ownership plan first, and do shared setup serially. Avoid concurrent edits to the same file; log cross-workstream findings rather than changing another owner's page/data.

## Workstreams and ownership

| Workstream | Owned data file | Owned page | Scope | Dependencies |
|---|---|---|---|---|
| A. Transport | `data/transport.json` | `getting-around.html` | MLA airport ↔ AX ODYCY; Qawra ↔ named BLAST Arena Studios/MFCC, Attard; event-day public transit; ferries, ride-hailing/taxi, car hire; practical mode comparison. Treat trip dates and booking inputs as user-supplied; independently verify route/event facts where possible. | Shared schema and page renderer. |
| B. Food & cafés | `data/food.json` | `restaurants.html` | Sourced restaurant, café, and casual-eating shortlist convenient to Qawra/AX ODYCY, with locality and official/map/review/social evidence. Publish live hours/prices only where checked and disclose inaccessible platforms. | Shared schema and page renderer. |
| C. Activities, landmarks & events | `data/activities.json` | `activities.html` | Gaming centres, recreation, landmarks, and dated public events during 13–19 October. Distinguish confirmed listings from seasonal/undated suggestions; do not infer spectator access. | Shared schema and page renderer; event/transport cross-notes go to `docs/HANDOFF.md`. |
| D. Everyday life for a U.S. traveler | `data/everyday.json` | `everyday.html` | Power, mobile service, currency/cards, tipping, safety/emergency/health, entry pointers, language, weather, and practical adaptation. Qualify advice that depends on passport, device, or itinerary. | Shared schema and page renderer. |
| E. Radio sports | `data/radio.json` | `radio.html` | AM/FM/DAB+ services receivable in Malta, official station schedules/listings during 13–19 October where available, and explicit unverified gaps. Do not treat fixture lists as broadcast evidence. | Shared schema and page renderer; published listings may be unavailable. |
| F. Expense planner | `data/expenses.json` | `costs.html` | Editable, blank-by-default categories for the trip; budget/actual totals, local browser autosave, CSV export, and reset. Do not assume the flight, hotel booking, party size, ticket, or third-party coverage. | Shared schema; references A–D sources without turning examples into estimates. |
| G. Integration | Shared site files: `index.html`, `css/style.css`, `js/site.js`, `README.md`, `sources.html`, `docs/*`, `.nojekyll`, `.github/workflows/validate.yml`, `scripts/validate_site.py`; retired legacy entry pages and duplicate/incompatible legacy data artifacts | `index.html` and `sources.html` | Executive summary, accessible responsive navigation, hosting/docs, retired-page notices, automated static validation, Pages deployment, and final integration. Integrates after A–F. | All topic workstreams complete. |

## Execution and verification

Arena fixes this checkout to its session branch, so work is performed on that branch rather than splitting into other branches. Workstreams A–F are completed one at a time under the ownership table; G integrates last. Every data record must have a relevant source URL, access date, allowed source type, confidence, and notes. Missing prices, schedules, opening hours, and booking details remain unset or explicitly qualified.

After integration, perform three cumulative passes:

1. **Implementation pass:** validate all JSON/schema/enums, JavaScript syntax, page/data wiring, local paths/anchors, expense planner behavior where the available test environment permits, and clean repository diff.
2. **Requirements/source pass:** check every requested topic and cross-workstream handoff; review displayed claims against their named sources, preserve platform/access limitations, and fix missing or unsupported content.
3. **Final audit pass:** line-by-line request and page/data consistency review; check mobile/desktop responsive rules, navigation, external-link targets, and local links; update source/open-question/status logs and report what could not be tested. Then verify the existing GitHub Pages branch configuration and PR/merge state.
