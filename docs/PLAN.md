# Malta trip site — implementation plan

## Repository review (starting point)

The repository is a dependency-free static HTML/CSS/JS site with twelve top-level pages and one shared stylesheet/script. It already contains extensive research, but it is centered on an earlier prize-dossier scenario (13–20 October, a different hotel assumption, and extensive Hotspawn/legal/tax material), has no structured `data/` source of truth, and many claims were checked on 23–24 September rather than the current 9 October 2026. The requested trip is now specified as AX ODYCY, Qawra, 13–19 October 2026; event-day transport, practical tourism, an expense template, and verifiable limits are the priorities. Current facts and trip-specific assumptions must be rechecked before reuse.

## Shared setup — serial, before topic work

1. Add `data/` and `pages/` conventions and a documented common record schema using the exact requested field names: `id`, `name`, `category`, `area`, `address`, `hours`, `price range`, `description`, `source_url`, `source_type`, `date_checked`, `confidence`, `notes`. Keep `source_url` a URL string per record; put corroborating URLs and claim-level detail in `docs/SOURCES.md`.
2. Define `docs/SOURCES.md`, `docs/OPEN_QUESTIONS.md`, `docs/STATUS.md`, and `docs/HANDOFF.md` formats. Log each researched claim with URL, access date, and workstream; unresolved claims stay unresolved.
3. Keep the existing static, no-build site shell; establish a coherent navigation and accessible responsive tokens before topic integration. Shared shell files (`index.html`, `css/style.css`, `js/site.js`, `README.md`) are reserved for G / serial integration.

## Shared record and evidence conventions

Every data item uses these exact fields, in this order: `id`, `name`, `category`, `area`, `address`, `hours`, `price range`, `description`, `source_url`, `source_type`, `date_checked`, `confidence`, `notes`. `source_url` is one URL string for the primary supporting source; corroborating URLs and individual claim-to-source mappings belong in `docs/SOURCES.md`. `source_type` is one of `official`, `map`, `review`, or `social`. `date_checked` is ISO `YYYY-MM-DD`. `confidence` is exactly `verified`, `partially verified`, or `unverified`. Use an explicit `Unknown` / `not published` value rather than inventing hours, access, or prices. Page copy must not make claims stronger than its linked data and sources.

## Workstreams and owned files

| ID | Workstream | Owned data file | Owned page | Dependency |
|---|---|---|---|---|
| A | Transport: airport ↔ hotel; AX ODYCY ↔ BLAST Arena Studios / Ta' Qali (Attard) on confirmed event days; buses, taxi/ride-hail, rental, convenience/value/cost/feasibility | `data/transport.json` | `pages/transport.html` | Shared schema; event day/timetable evidence; verified route/stop details |
| B | Restaurants, casual food and cafés: relevant to Qawra/St Paul's Bay and practical day trips; review/popularity evidence and platform limitations | `data/food.json` | `pages/food.html` | Shared schema; sourced venue identity/area/price and review evidence |
| C | Gaming centers, activities, landmarks and dated events | `data/activities.json` | `pages/activities.html` | Shared schema; confirmed opening/event dates and transport links |
| D | US traveler everyday life: plug/voltage, mobile service, payments/tipping, safety/health, customs/entry, language, October weather | `data/everyday.json` | `pages/everyday.html` | Shared schema; authoritative government/operator sources |
| E | Malta radio/sports: terrestrial AM/FM/DAB+ reception, officially listed live broadcasts and trip-date schedules; distinguish likely from confirmed | `data/radio.json` | `pages/radio.html` | Shared schema; station schedules plus official fixture data; flag unpublished schedules |
| F | Expense planner: itinerary-ready, editable inputs and explicit estimate/quote handling | `data/expenses.json` | `pages/expenses.html` | Shared schema; confirmed hotel/trip dates; transparent assumptions |
| G | Site shell, executive summary, navigation, integration and verification | `index.html`, `css/style.css`, `js/site.js`, `README.md`, `pages/sources.html` (publication-facing source log/open questions/final report), existing top-level redirect/compatibility pages as needed; `docs/` integration files | Root `index.html` | A–F data/pages complete; shared setup; runs last |

## Execution / coordination

The session is pinned to one Arena branch and there is no parallel sub-agent/branch tool available. I will therefore follow the same ownership boundaries serially (A–F each edit only its owned data/page files, G owns shared files), preserving complete findings in the single source log rather than making conflicting parallel edits. I will not switch branches. Any cross-topic finding goes into `docs/HANDOFF.md` rather than another stream's files.

## Dependencies and verification gates

- Establish shared folders, schema, source log, status/open-question formats first.
- Finish and self-check A–F independently, then G integrates and updates shared navigation/overview.
- Every factual item must have a source URL, access date, source type, confidence and caveat; page text is generated from or directly matches its data. Do not turn search snippets, review counts, or a route planner into a verified service guarantee.
- Validate JSON; compare page links/data; check internal links, page responses, mobile navigation/layout, and JS; run the requested three review passes on the integrated site.
- Any trip-specific fact not verified by a primary source stays in `docs/OPEN_QUESTIONS.md` and is described as unconfirmed on the site.
