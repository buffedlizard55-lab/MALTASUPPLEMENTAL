# Malta trip companion — implementation plan

## Repository review

The repository is an existing static HTML/CSS/JavaScript site with a root-level page for most subjects. It has no structured topic data, no `docs/` research register, and no automated checks. The existing content assumes **13–20 October 2026**, an eight-day/seven-night stay, a California/SFO departure, and includes unrelated prize/legal analysis. The user-supplied trip is instead **13–19 October 2026** at **AX ODYCY Malta, Qawra**; arrival/departure times, flights, event-session times, and the confirmed event-day travel plan are not yet supplied. Existing claims and sources must therefore be audited rather than inherited. Keep the user-facing site focused on the requested trip and clearly distinguish verified facts, estimates, and unknowns.

## Shared setup (serial; complete before topic research)

- Preserve the static GitHub Pages deployment model and root `index.html` entry point.
- Add `data/`, `pages/`, and `docs/`; create the shared record schema and source-log format below before editing topic pages.
- Define one responsive shell, navigation, design tokens, accessible card/table/callout styles, and one shared client-side renderer. Topic pages must display their data records rather than introduce unsupported facts in prose.
- Set the trip facts used site-wide: AX ODYCY Malta, Qawra Coast Road, Qawra SPB 1902; 13–19 October 2026; 6 hotel nights if checking in on 13 October and out on 19 October. Do not assume flight times or which tournament days the traveler will attend.
- Establish `docs/SOURCES.md`, `docs/OPEN_QUESTIONS.md`, `docs/HANDOFF.md`, and `docs/STATUS.md` before topic work.

## Shared data contract and evidence rules

Every ordinary list record has these required keys: `id`, `name`, `category`, `area`, `address`, `hours`, `price range`, `description`, `source_url`, `source_type`, `date_checked`, `confidence`, `notes`. `source_type` is one of `official`, `map`, `review`, or `social`; `confidence` is one of `verified`, `partially verified`, or `unverified`. Use `null` or an explicit `Not published / not verified` value instead of inferring missing hours, fares, schedules, or addresses. Topic-specific fields may be added where necessary (for example, route legs, dates, frequencies, or budget inputs). Every factual claim must be tied to a source URL and an access date in `docs/SOURCES.md`; conflicting or unavailable evidence belongs in `docs/OPEN_QUESTIONS.md`. Pages are rendered from or strictly match the associated JSON records. Do not present estimates as operator quotes or third-party listings as official.

Source-log columns: `ID | Claim supported | URL | Source type | Accessed (UTC) | Workstream | Verification note`. Record negative findings (such as an unpublished match listing or inaccessible platform) in the open-questions register, not as positive facts.

## Workstreams and file ownership

| Workstream | Owned files | Scope | Dependencies |
|---|---|---|---|
| A. Transport | `data/transport.json`, `pages/transport.html` | Airport options; AX ODYCY ↔ BLAST Arena Studios / Ta' Qali corridor public-bus directions for confirmed tournament dates; fares, transfers, taxis/ride-hailing, rental feasibility; convenience/price/value comparison | Shared schema, source log, shell; official operator and event venue data |
| B. Food & cafés | `data/food.json`, `pages/food.html` | Curated popular places to eat/cafés near Qawra and useful trip areas; distinguish review signals from verified business facts; disclose access limits for Google/Yelp/social platforms | Shared schema, source log, shell; A for areas/travel context |
| C. Gaming, activities, landmarks & events | `data/activities.json`, `pages/activities.html` | Gaming venues; sights and day trips; only date-relevant events with confirmed dates, plus clearly flagged tentative items | Shared schema, source log, shell; A for travel context and event-day constraints |
| D. Everyday life for a US traveler | `data/everyday.json`, `pages/everyday.html` | Plugs/voltage, mobile data, money, tipping, safety, health, customs/entry, language, weather and practical differences | Shared schema, source log, shell; authoritative US/Maltese/EU sources |
| E. Radio sports broadcasts | `data/radio.json`, `pages/radio.html` | Receivable AM/FM/DAB+ or other radio services; official schedules for sports broadcasts during 13–19 Oct; schedule gaps explicitly noted | Shared schema, source log, shell; official broadcasters, regulators, competitions |
| F. Expense planner | `data/expenses.json`, `pages/expenses.html` | Itinerary-ready editable budget template; separate known amounts, estimates, and user-entered costs; no assumed prize coverage or tax advice | Shared schema, source log, shell; A–E for cost categories |
| G. Site shell, executive summary & integration | `index.html`, shared CSS/JS, navigation, docs landing/audit updates, any integration fixes | Executive summary; navigation; mobile/desktop integration; links, data/page consistency, accessibility and final review | Runs last after A–F; consumes all topics and open questions |

## Conflict avoidance and execution constraint

The requested ownership boundaries are retained. The active Arena session is fixed to branch `arena/785456db-maltasupplemental`; do not create or switch to workstream branches. No separate-agent tool is available in this session, so the workstreams will be executed sequentially on this branch and only in their listed owned files, with G/integration edits last. Relevant cross-topic findings go in `docs/HANDOFF.md` rather than another workstream's files.

## Verification gates / passes

1. **Pass 1 — implement:** verify each source against the statement it supports; populate data and page, open questions, source log, and status.
2. **Pass 2 — independent audit:** check date arithmetic, event/venue and transit feasibility, quoted prices/hours/frequencies, schedule time zones, links, and all high-impact assumptions; remove or downgrade unsupported claims.
3. **Pass 3 — integration audit:** check every supplied requirement against the site; validate JSON, page/data rendering, internal links, responsive/mobile navigation, keyboard access, budget calculations, GitHub Pages paths, and the final source/open-question/status registers. No item without evidence should be presented as verified.

The project is complete only when the integration checks pass and remaining unknowns are visible, actionable, and not guessed.

## Reconciliation with newer main-branch work

While this session was in progress, `main` advanced with a parallel trip-refocus PR. Its new hotel/itinerary/neighborhood drafts treated a Deluxe sea-view booking, SFO departure and tournament attendance as confirmed, although those details were not supplied in this task. Those URLs now redirect to the current guide, and the unused `data/trip.json` / `data/venues.json` copies were removed rather than publishing conflicting facts. The six A–F topic datasets/pages and this plan's uncertainty rules remain the canonical implementation. The upstream schema documentation and validation-script paths were retained in corrected, repository-compatible form.
