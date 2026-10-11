## Current session plan — `arena/3031b29b-maltasupplemental` (11 October 2026)

Started at `main` `ae69ab1c3a243685289b16c274fa06a21c9b9167` (PRs #55–#57 merged), clean tree. Repository review confirmed the existing static Pages shell, canonical 13-field schema, seven topic datasets with matching pages, source/open-question/status/handoff logs, expense planner, CI workflow and Playwright/axe suite; nothing is replaced. Shared setup (schema, navigation/renderer, CSS tokens, source-log row format) is unchanged and was re-verified before any edit. Arena still provides one fixed branch and no isolated workstream runner, so A–F run serially with the same ownership boundaries and G integrates shared files last; cross-topic finds go to `docs/HANDOFF.md`, unresolved items to `docs/OPEN_QUESTIONS.md`.

This pass targets the one requirement that is still weakest — a receiver-usable answer on live sports radio, and the trip-window sport calendar behind it — plus fresh corroboration of the trip’s highest-risk facts. Two days before departure, the priorities are the things that change a decision, not new description.

| Stream | Owned files | This session |
|---|---|---|
| A · Transport | `data/transport.json`, event-day notes on `getting-around.html` | Re-read the complete service-updates page a fourth time and enumerate the 17–18 October detour cluster; add the published TQ1/TQ2 route definitions and the dated Ta’ Qali special-service precedent; keep the return-gap and Friday-16-October questions open. |
| B · Food & cafés | `data/food.json`, `restaurants.html` | No new platform access was available in this pass; existing dated review-volume snapshot and access limits stand unchanged rather than being re-asserted as fresh. |
| C · Gaming, activities, landmarks & events | `data/activities.json`, `data/event.json`, `activities.html`, `event.html` | Re-read the ticketing listing for inventory/lineup/agenda drift; no agenda change found. |
| D · U.S.-traveler everyday guide | `data/everyday.json`, `everyday.html` | Add the national forecast’s republication by a second Maltese outlet and the two third-party forecasts that reach 18–19 October, labelled as leads. |
| E · Sports radio | `data/radio.json`, `radio.html` | Three new records: BFBS Radio 2 as a non-Malta option (negative), PBS Radju Malta/Radju Malta 2 as a radio-carriage lead, and the trip-window/out-of-window sports calendar; plus a new dated trip-window live-sport table on the page and independent fixture corroboration. |
| F · Expense planner | `data/expenses.json`, `costs.html` | Unchanged: amounts stay blank; only confirmed quotes go in. |
| G · Site shell, executive summary & navigation (last) | `index.html`, `docs/*`, `README.md`, tests | Fold the new evidence into the executive summary, refresh the source/status/report/handoff records, run every gate, then deliver by PR. |

### Verification gates / passes

1. **Pass 1 — implement and verify:** re-read the highest-risk live sources (ticketing listing, operator fares and service updates, Route 186 grids) and add the new radio/transport/weather evidence with its sources.
2. **Pass 2 — adversarial review:** check the new claims for overreach (crowd-edited sources, third-party calendars, precedent vs. commitment), confirm every new URL is in the source log, confirm no unverified item is presented as fact, and re-run schema/link/JavaScript/browser gates.
3. **Pass 3 — original-request audit:** walk the user’s line-by-line requirements against the integrated result, confirm the site still answers each, and report only observed PR/Pages state.

# Malta trip guide — work plan

## Current session plan — `arena/67d511d1-maltasupplemental` (11 October 2026)

Repository review found the existing static Pages shell, canonical 13-field record schema, per-topic JSON data/pages, source log, open-questions/status records, expense planner, CI workflow and browser tests. Preserve them; do not create duplicate structure. Shared setup is already present and will be kept serial: verify `data/record.schema.json`, existing navigation/renderer and CSS tokens, and the master-source row format before topic work. This Arena session has one fixed branch and no isolated workstream runner, so A–F research/edits run one at a time with the listed ownership; G updates shared presentation/docs after topic work. Cross-stream discoveries go to `docs/HANDOFF.md`/`docs/OPEN_QUESTIONS.md`, not another stream's page/data file. During the session, `origin/main` advanced beyond the starting `250e6bd` through PRs #51–#56. The fixed branch was rebased onto the latest `origin/main` at `6da8aba`, preserving the merged source-led popularity, gaming, entry, per-date event-transport, timezone-pinned matchup and reporting updates before the final integration pass.

| Stream | Owned files | Dependencies / deliverable |
|---|---|---|
| **A · Transport** | `data/transport.json`, `getting-around.html` | Depends on advertised event venue, agenda and hotel input; compare airport and event-day modes, fares/value, last return and caveats. |
| **B · Food & cafés** | `data/food.json`, `restaurants.html` | Depends on location/area inputs; categorize sourced hotel/Qawra/wider-island options and state review-platform access limits. |
| **C · Gaming, activities, landmarks & events** | `data/activities.json`, `activities.html` (and retained `data/event.json`, `event.html`) | Depends on dated event/venue sources; distinguish current admission/status from closed, historical or unverified leads. |
| **D · U.S.-traveler everyday guide** | `data/everyday.json`, `everyday.html` | Depends on the U.S. traveler context; verify plugs, SIM, payments/tipping, safety/health, customs, language and date-sensitive entry/weather. |
| **E · Sports radio** | `data/radio.json`, `radio.html` | Depends on official station schedules plus Malta FM/DAB+ directory evidence; keep schedule, carriage, device compatibility and physical reception distinct. |
| **F · Expense planner** | `data/expenses.json`, `costs.html` | Depends on A–E category taxonomy and eventual traveler itinerary; keep blank until actual amounts, preview before quick-fill and test private backup/export. |
| **G · Site shell, executive summary & navigation (last)** | `index.html`, `js/site.js`, `css/style.css`, `sources.html`, `README.md`, integration tests/docs as needed | Integrates A–F and event work after their facts stabilize; run local-link, data/page, accessibility, mobile/desktop and planner checks. |

## Verification gates / passes

1. **Pass 1:** preserve the shared schema/source-log format; re-read the highest-risk event, transport and radio sources; implement data-backed topic-page additions and log each claim/source/date.
2. **Pass 2:** adversarially review route/date/fare inference, ticket and radio access, platform coverage, mobile layout, source URLs, navigation and planner edge cases; fix or mark open.
3. **Pass 3:** map the full user request against the integrated site, check all owned data/page source links and open questions, run the complete validation/browser suite, then report only observed PR/Pages states.

No parallel branch or agent is claimed. Work stays on the fixed Arena branch and within one workstream's owned files at a time; G handles shared integration last.

## Previous mainline session — `arena/d840a59d-maltasupplemental` (11 October 2026)

Fixed Arena branch, started at `main` `250e6bd0ea5722cbad5a5ec21fc3117f2eee8fe0` (PR #48 merge) with a clean tree. Arena provides no isolated workstream runner, so A–G executed serially with the same file-ownership boundaries: A owned `data/transport.json` and `getting-around.html`, C/H owned `data/event.json` and `event.html`, E owned `data/radio.json` and `radio.html`, and G owned shared documentation, tests and the README. Cross-topic findings went to `docs/HANDOFF.md`; nothing unresolved was written as fact.

Session objectives and what was delivered:

1. **Re-verify the highest-risk claims again, two days before the trip.** Fresh reads of the Eventbrite listing, the MPT fare page, the complete MPT service-updates page, the Route 186 grids, the TQ1 page, the Malta DAB+ operator directory, Vibe FM’s football page and the HLTV bracket report. Each read is logged with its date in `docs/SOURCES.md`.
2. **Close the core requirement — public transport on the event days, day by day.** New canonical record `event-day-transport-by-date` plus `getting-around.html#event-day-by-date`: one outbound plan, one return constraint and one action for each of the seven trip days, with every derived figure labelled as derived.
3. **Fix an unverified assumption found in this session’s own draft.** The bracket clocks initially taken from a search rendering had no stated timezone; a direct read of the same table differed by exactly six hours, which pinned the Malta local starts at 10:30 / 13:00 / 15:30 / 18:00 and produced the new `twc-opening-matchups-14-oct` record and `event.html#opening-matchups` section.
4. **Keep the radio section honest.** The operator directory read in full shows no “Sports Channel” and only Radio Sportiva as sports-branded; Vibe FM’s football page is still on the 2025/26 season. Both narrow the claims; no station was added as a listening plan.
5. **Verify and deliver.** Full local gate suite green (validator, JavaScript check, 22/22 Playwright), then a PR from this branch only, merged by explicit number, with observed GitHub/Pages state reported rather than predicted.

## Current delivery session — `arena/502e2dae-maltasupplemental` (11 October 2026)
## Current session — `arena/dd9dd00c-maltasupplemental` (11 October 2026)

Arena fixes this session to `arena/dd9dd00c-maltasupplemental` and does not provide isolated workstream branches. A–F therefore run serially on this branch, each editing only its owned data file plus matching notes. G edits shared pages, navigation hubs, docs and delivery last. Cross-topic findings go to `docs/HANDOFF.md`. Unverified gaps stay in `docs/OPEN_QUESTIONS.md`.

| Stream | Owned files | This session |
|---|---|---|
| A · Transport | `data/transport.json`, event-day notes on `getting-around.html` | Re-read Route 186 evening grids, fares and service updates. Add the Saqqajja stop-4627 closure as its own record. Do not invent a saved journey. |
| B · Food | `data/food.json` | Re-read the Qawra TripAdvisor list far enough to record the Featured methodology, sponsored cards and the first three numbered entries. Do not call that a popularity ranking. Keep the separate review-volume capture from `main`. |
| C · Activities / event | `data/activities.json`, `data/event.json` | Re-read Eventbrite and the official Thunderpick finals page. Record the visible six-team lineup and the hidden View all control. Keep the HLTV/Hotspawn/Liquipedia group record already on `main`; do not treat Eventbrite’s incomplete image block as a contradiction. |
| D · Everyday | `data/everyday.json` | Re-read Government of Malta electricity wording and the Malta Met Office seven-day panel. Do not reopen every older forecast. Keep the EES/ETIAS conflict already recorded on `main`. |
| E · Radio | `data/radio.json` | Re-read BBC Sportsworld episode JSON and the Premier League amendment article. Keep UK schedules separate from Malta reception. |
| F · Expenses | `costs.html` keyword matcher only | Add adapter/radio-receiver keywords that map to the existing incidentals row. Do not prefill amounts. |
| G · Integration | `index.html`, hubs, docs, tests, PR | Scannable executive summary, event-day bus checks, useful hubs instead of “page moved”, then validate, open the PR from this branch and merge it to `main`. |

Dependencies: shared schema and shell already exist. G waits until A–F data edits are in the files. No workstream rewrites another topic’s page. `origin/main` moved during the session (PRs #51 and #52); those records are retained in the merge.

## Prior delivery session — `arena/09cdfbf0-maltasupplemental` (11 October 2026)

Started from `origin/main` at `250e6bd` (merge of PR #48). Closed the food review-volume gap, recorded that no public PC café was listed, and hardened the EES/ETIAS notes. Merged as PR #51.

## Historical delivery session — `arena/502e2dae-maltasupplemental` (11 October 2026)

This fixed Arena branch began at `origin/main` commit `b307c51e8026ca3589ece815b0fb761eef36094e` (the PR #33 merge), at parity at session start. The parallel-work protocol remains in force: A–F own one topic data file plus its matching page; G owns shared integration and documentation; Arena provides no isolated workstream runner, so research and edits run serially on the fixed branch, shared files only by G. Cross-topic findings go to `docs/HANDOFF.md`; unresolved or conflicting evidence stays in `docs/OPEN_QUESTIONS.md`.

Current session objectives:

1. **Multi-pass verification (requested):** Pass 1 implement/verify every requirement line by line against live sources; Pass 2 bug/assumption/edge-case review; Pass 3 full re-check against the original request with accuracy, reliability, completeness and code-quality improvements. No claims without sources; unverifiable items go to `docs/OPEN_QUESTIONS.md`.
2. **Highest-risk re-verification:** live re-reads of the Eventbrite listing, MPT Route 186/202 pages, MPT fares page and BBC programme pages; update the return-gap, fare-season, detour-scope, card-terms and late-return-lead records and the pages that render them.
3. **Data hygiene:** normalize canonical 13-field key order across all six data files; keep validator/JS/browser gates green; keep static and runtime deep links intact.
4. **Delivery:** commit and push only `arena/502e2dae-maltasupplemental`, open a PR from it, merge by explicit number onto `main` as requested, check the Pages build, and report observed states only — including what remains unverified, limitations and next-session suggestions.

## Previous delivery session — `arena/ef6c76d6-maltasupplemental` (11 October 2026, superseded above)

## Post-merge follow-up session — `arena/9f6f35c7-maltasupplemental` (11 October 2026)

**Session:** 11 October 2026 (UTC) · branch `arena/dfefc16f-maltasupplemental` · reviewed baseline `b307c51`.


## Repository review and approach

**Current session:** 11 October 2026 (UTC) · fixed branch `arena/cc913a9b-maltasupplemental` · starting revision `b307c51` · current upstream integrated locally through PR #49 at `12578cd`.

**Current session:** 11 October 2026 (UTC) · fixed branch `arena/cc913a9b-maltasupplemental` · starting revision `b307c51` · latest-main integration through PR #49 at `12578cd` · delivered by PR #46 as merge commit `25e0176`.

## Repository review and scope

The repository review and plan preceded topic corrections. It already contained a GitHub Pages site, shared renderer/navigation, canonical JSON records, source/open-question logs, browser tests and an expense planner; preserve that work and reconcile incoming `main` rather than replacing it with a second app.

Deliver a mobile-friendly, source-linked guide and an easy-to-fill, blank-by-default expense planner for the user-supplied **13–19 October 2026** stay at **AX ODYCY, Qawra**, with the supplied **BLAST Arena Studios, Attard** Thunderpick CS2 event destination. These are trip inputs, not proof of a booking, room, admission, entrance, live service or price. Cover event/public transport (especially the return), food/cafés, gaming and activities, landmarks/dates, practical U.S.-traveler guidance, separate Malta sports radio, and the planner. Research platform access (Google Maps/Reviews, Yelp, Instagram, TikTok, Facebook, Reddit and X) must be disclosed accurately; access limits are not filled by inference.

## Shared setup — before owned topic work

- Keep the exact 13-field schema in `data/record.schema.json`: `id`, `name`, `category`, `area`, `address`, `hours`, `price range`, `description`, `source_url`, `source_type`, `date_checked`, `confidence`, `notes`.
- Topic pages render canonical records instead of repeating unsourced facts. Use only the schema's allowed enums. Every factual claim must have a traceable source/access date in `docs/SOURCES.md` and a confidence/limitation appropriate to the evidence.
- Maintain `docs/OPEN_QUESTIONS.md` for missing or conflicting facts, `docs/HANDOFF.md` for cross-topic findings, `docs/STATUS.md` for progress and blockers, and `docs/FINAL_REPORT.md` for the audited result. Preserve older audit snapshots as historical rather than live facts.
- Prefer current primary operator, organizer, station, venue, government or provider pages. Do not invent ratings/popularity, opening hours, prices, ticket availability, schedules, routes, radio carriage or reception. Label search-index/community evidence and source-platform blocks; do not claim comprehensive review access.
- The expense planner starts blank, keeps traveler-specific data out of assumptions, previews itinerary matches, never overwrites entered amounts, and makes backup/restore/export behavior explicit and safe.

## Parallel-work ownership protocol

Arena fixes this session to `arena/cc913a9b-maltasupplemental` and provides no isolated agent/workstream branch runner. Therefore A–F execute serially, with the same file ownership boundaries; no separate agents/branches are claimed. G integrates shared work last. Do not edit another topic's data/page outside its pass; add cross-topic findings to the handoff or open-questions log.

| Stream | Owned data | Owned page | Focus |
|---|---|---|---|
| **A · Transport** | `data/transport.json` | `getting-around.html` | Airport/hotel/event travel, dated public-bus candidates, fares/cards, return options, taxi/ride-hailing, ferries/rental; compare feasibility, convenience, price and value without fabricating a journey. |
| **B · Food & cafés** | `data/food.json` | `restaurants.html` | Qawra/hotel and relevant Malta eateries, menus/hours, closure status and clearly scoped Maps/review/social evidence; no universal popularity ranking. |
| **C · Activities, gaming, landmarks & dated events** | `data/activities.json` | `activities.html` | Gaming status, attractions and trip-window events; separate confirmed dates/access from leads and unresolved detail. |
| **D · U.S.-traveler everyday guide** | `data/everyday.json` | `everyday.html` | Power/device compatibility, mobile service, money/tipping, entry/customs, safety/health, language and weather; distinguish general advice from personal eligibility. |
| **E · Malta sports radio** | `data/radio.json` | `radio.html` | Official dated schedules and Malta FM/AM/DAB+ receiver evidence; distinguish named-match carriage, general programming, technical listings, physical reception and internet streams. |
| **F · Expense planner** | `data/expenses.json` | `costs.html` | Blank categories/daily rows, quick-fill preview, totals, local storage, CSV and validated JSON backup/restore; no assumed bookings or costs. |
| **H · CS2 event extension (upstream)** | `data/event.json` | `event.html` | Retain and re-audit the event listing, five-day desk, ticket/field/bracket/broadcast evidence and open access questions. This upstream extension is not a new branch/workstream agent. |
| **G · Integration (last)** | Shared files/docs/validation/tests | `index.html`, `sources.html`, shared shell and legacy links | Responsive overview/navigation, data/source/open-question integration, merge reconciliation, accessibility/browser checks and final PR/delivery report. |

## Cumulative verification passes

1. **Pass 1 — implementation/integration:** review the existing repo and schema before edits; preserve all upstream additions; check canonical data/page wiring, links, JavaScript and planner behavior.
2. **Pass 2 — adversarial evidence and software review:** search for stale/overconfident claims, hidden or missing data, route/price/ticket/radio inference, blocked sources, malformed backup/import data and planner edge cases; fix or record each gap.
3. **Pass 3 — original-request audit:** map every requested topic and research limitation to the guide/docs/tests, compare current claims with the evidence log, inspect incoming `main` IDs and rerun every local gate. Do not describe passing tests as a factual certificate.

PR #49's inherited completion record documents 18/18 after implementation, then an expanded 21/21 adversarial/final run. This session integrated `main` through `12578cd` (PR #49) and reran the full 21-test suite: 184 exact-schema records, 281 source-log URLs, 15 HTML pages, 176 local links, 9 navigation destinations, 25 expense rows; all checks passed. PR #46 head `3ad5100` passed GitHub's “Schema, browser and accessibility checks” and merged at `25e0176`. The latest Pages build record, `1276765781`, reports `built` for that merge commit. A physical trip/receiver test and exhaustive external source re-verification remain out of scope.

## Delivery — observed

PR #46 was merged into `main` on 11 October 2026 at 16:38:02 UTC (merge commit `25e01762d310bdc71deaa9dc9602f96a7d4565f9`). The pushed head was `3ad510058c77c41cf2920949b4047d921d870578`; its required schema/browser/accessibility check passed at 16:37:43 UTC. GitHub Pages latest-build record `1276765781` reports status `built` for the merge commit, updated at 16:38:24 UTC. The Pages source is `main` at `/`; no independent browser-level content fetch was performed.

The local `npm test` suite and `git diff --check` passed after application integration. Report only observed GitHub/deployment outcomes; do not assert personal bookings, service, reception or complete external re-verification. Remaining next steps require traveler/event details or date-local checks: confirm ticket/gate/weekend details, save dated transit journeys, refresh volatile listings and fares, locally scan radio, and enter only actual costs into the planner.
