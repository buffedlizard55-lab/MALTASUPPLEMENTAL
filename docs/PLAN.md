# Malta trip guide — work plan

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
