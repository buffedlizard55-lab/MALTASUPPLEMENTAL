# Malta trip guide — implementation plan

## Repository review and scope reset

The repository is a hand-authored static HTML/CSS/JavaScript site with no application build or test setup. The existing content described a different 13–20 October itinerary and included prize/legal/privacy material outside the requested tourism guide. The work resets it to the traveler-supplied Malta trip window (13–19 October 2026), AX ODYCY in Qawra, and the named BLAST Arena Studios location. User-supplied booking details remain planning inputs unless independently corroborated; event access and route facts are not inferred.

## Shared setup (serial, before topic work)

1. Define one common JSON record schema: `id`, `name`, `category`, `area`, `address`, `hours`, `price range`, `description`, `source_url`, `source_type`, `date_checked`, `confidence`, and `notes`. The canonical `data/record.schema.json` and offline validator enforce these exact 13 keys; the `source_type` values are `official`, `map`, `review`, `social`, and `directory`.
2. Preserve a dependency-free static site. Topic pages render from their workstream JSON data; the expense planner uses a blank-by-default editable form backed by its expense JSON categories.
3. Maintain `docs/SOURCES.md` (claim, URL, UTC access date, workstream, limitation), `docs/OPEN_QUESTIONS.md` (missing/conflicting details), `docs/STATUS.md` (progress/blockers), and `docs/HANDOFF.md` (cross-topic findings).
4. Prefer primary operator, organizer, venue, station, government, or official provider pages for current details. Label review/social snapshots separately. Do not present a fixture list as radio carriage or a route-level bus timetable as a door-to-door trip.
5. Review the repository before any parallel topic work, create this ownership plan first, and do shared setup serially. Avoid concurrent edits to the same file; log cross-workstream findings rather than changing another owner's page/data.

## Workstreams and ownership

| Workstream | Owned data file | Owned page | Scope | Dependencies |
|---|---|---|---|---|
| A. Transport | `data/transport.json` | `getting-around.html` | MLA airport ↔ AX ODYCY; Qawra ↔ user-supplied BLAST Arena Studios destination, with the BLAST Arena Studios venue address (MFCC South Gate National Stadium, Attard ATD 4000) corroborated and the TWC entrance unconfirmed; event-day public transit; ferries, ride-hailing/taxi, car hire; practical mode comparison. Treat trip dates and booking inputs as user-supplied; independently verify route/event facts where possible. | Shared schema and page renderer. |
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

## PR #13 / main reconciliation (10 Oct 2026)

PR #13 was based on an older implementation that added duplicate `/pages/` templates and a separate site builder. `origin/main` already contains the canonical root-page renderer, shared schema/validator, six current JSON datasets, expense planner, and research pages. The reconciliation retained that main architecture, imported only non-duplicate food/activity records, updated the Aquarium and Rolex race facts, and integrated their source/open-question/status/handoff notes. The duplicate `/pages/` copies, `tools/build_site.py`, legacy `data/schema.json`, and duplicate schema document were removed; main’s `.nojekyll`, `docs/DATA_SCHEMA.md`, and validator remain. Legacy `hotel.html`, `itinerary.html`, and `qawra.html` URLs remain noindex notices. No claim was imported without a source and limitation recorded.

## 11 October 2026 verification & completion pass (`arena/c4522181-maltasupplemental`)

Following the 11 October merges on `main`, a three-pass audit and live-source verification was completed across Workstreams A–G:

1. **Workstream A (`data/transport.json`, `getting-around.html`):** Added an explicit mode-comparison record (`mode-comparison-island-and-event`, bringing `data/transport.json` to 14 records and the site to 114 records) and a structured comparison section on `getting-around.html` comparing public bus, ride-hailing/taxis, ferries, and rental cars across convenience, price, value, and feasibility. Read the official Route TD1 timetable (`https://www.publictransport.com.mt/route/TD1/`, chunks 7–9) on 11 October 2026, confirming that TD1 serves `Il-Qawra` stop `Arznell - 950` in both directions (`05:42–00:35` from Airport 1 stop 2550; `05:28–23:26` weekday / `05:27–23:27` weekend toward Airport 3 stop 2552). Also logged Tuesday 13 October (09:30–17:30) construction detours on Attard Routes 54 and 106 from the MPT service-updates page.
2. **Workstream D (`data/everyday.json`):** Read chunks 1–3 of the U.S. State Department Malta Travel Advisory (`https://travel.state.gov/en/international-travel/travel-advisories/malta.html`) on 11 October 2026, confirming emergency number **112** (ambulance, fire brigade, police, emergency medical services), **179** (24/7 national helpline), **116-006** (victim support), upfront payment expectations at private hospitals, and card/ATM guidance (euro official currency, American Express not widely accepted, ATMs accept U.S. bankcards with frequent ATM fees).
3. **Workstream E (`data/radio.json`, `radio.html`):** Logged the Sunday 11 October 2026 BBC *Sportsworld* episode (`https://www.bbc.co.uk/programmes/w1730c9208pxyf8`), which is explicitly billed on the official upcoming-broadcasts page as *"Live sport from around the world - including the English Premier League"*, alongside the 17–18 October episodes (`w1730c92ck0m2cw` and `w1730c92ck0q313`), and added an explicit section on `radio.html` covering EPL, soccer, and live sports likely on Kalshi markets and their broadcast-verification caveats.
4. **Workstream F (`costs.html`, `scripts/validate_site.py`):** Fixed `costs.html` line 176 (`record.price_range` → `record["price range"] || "Not published"`) so every expense card displays its `Price status` field, and added a regression check in `scripts/validate_site.py` preventing `record.price_range` in `costs.html` or `js/site.js`.
5. **Workstream G (`index.html`, `js/site.js`, `sources.html`, `README.md`, `docs/*`):** Synchronized executive summaries, snapshot dates (`9–11 October 2026`), record counts (`114 exact-schema records`), and source/open-question/handoff/status logs.
