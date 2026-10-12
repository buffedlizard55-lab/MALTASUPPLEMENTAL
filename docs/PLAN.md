# Current session plan — `arena/99828d92-maltasupplemental` (12 October 2026 UTC)

## Repository review and scope

The repository was reviewed at `main` `956dfd9` (PR #72 merge) on the eve of the trip window. Everything required by the original request is already built and green on the untouched tree: a GitHub Pages static site (15 HTML pages, nine-item shared navigation, executive summary, section hubs), an exact 13-field record schema with seven datasets (218 records), per-topic pages rendered from JSON by `js/site.js`, a master source log, open-questions and status ledgers, a blank-by-default expense planner with itinerary quick-fill, a CI workflow and a Playwright/axe suite. Nothing is rebuilt and no shared setup (folder structure, schema, site shell, CSS tokens, source-log row format) is changed without a source-led reason.

This session is a **final pre-departure verification and delivery pass** on the fixed Arena branch. Arena fixes one branch per session, so workstreams run serially on it with the established ownership map; G integrates last. Cross-topic findings go to `docs/HANDOFF.md`, unknowns stay in `docs/OPEN_QUESTIONS.md`, and every claim is logged with URL and access date in `docs/SOURCES.md`.

| Stream | Owned files | This session |
|---|---|---|
| **A · Transport** | `data/transport.json`, `getting-around.html` | Re-read the operator's Route 186 page and the live service-updates feed (both complete, 12 Oct UTC); record the 30-minute headway, the reproduced 20:53 Stadium 2194 return and its 21:27 Buġibba Bay 1 arrival, and confirm the trip-week notice set. Add the venue's published map pin from the official ticketing listing. |
| **B · Food & cafés** | `data/food.json`, `restaurants.html` | No new platform access; re-confirm the blocked-platform boundary rather than restate it as evidence. |
| **C · Gaming, activities, landmarks & events** | `data/activities.json`, `activities.html`, `data/event.json`, `event.html` | Re-read the ticket listing (agenda, venue block, FAQ state) and the tournament bracket source; keep event facts separate from the generic recommendation card. |
| **D · U.S.-traveler everyday guide** | `data/everyday.json`, `everyday.html` | Independently reproduce the national 12–18 October forecast panel (identical values) and keep it labelled a dated forecast; leave entry/health/power claims untouched where no change was found. |
| **E · Terrestrial sports radio** | `data/radio.json`, `radio.html` | Re-read the three official schedules already cited (BBC World Service Sportsworld, BBC Radio Scotland, Radio Sportiva), the Rai Radio 1 programme page and the DAB+ operator directory; keep fixtures, schedules, carriage and reception strictly separate. |
| **F · Expense planner** | `data/expenses.json`, `costs.html`, `docs/ITINERARY_QUICKSTART.md` | Ship the missing piece for “quick work once the itinerary arrives”: a one-page itinerary-to-planner worksheet (accepted line formats, category mapping, five-minute workflow) wired into the planner page. Amounts stay blank. |
| **G · Site shell, executive summary & delivery** | `index.html`, `js/site.js`, `sources.html`, `README.md`, `docs/*`, tests | Fix the one orphaned page by giving the shell a footer hub row, refresh the executive-summary bullets affected by this pass, log all new sources, run all gates, open the PR, merge it by number and record only observed GitHub/Pages state. |

## Conflict avoidance

One branch (this one), serial execution, one owner per file. Shared files (`index.html`, `js/site.js`, `css/style.css`, `sources.html`, `README.md`, `docs/*`) are touched only by G after A–F. No file is reformatted, no record is deleted or re-keyed, and no unverified item is presented as fact.

## Verification gates (Passes 1–3)

1. **Pass 1 — implement and verify:** each stream re-reads its live sources, writes only its owned data/page pair, and logs every claim with URL and access date; anything not confirmed stays labelled.
2. **Pass 2 — adversarial review:** check the new records for overreach (a timetable row is not a dated last bus; a published pin is not attendee access; a schedule is not carriage; a listing is not a broadcast), re-check page/data consistency, and re-run the validator, the JavaScript check and the full Playwright/axe suite.
3. **Pass 3 — original-request audit:** walk the user's line-by-line requirements against the integrated tree, state verified vs unverified, deliver by PR and merge, observe the Pages build, and report limitations plus next-session tasks.

---

## Previous session plan — `arena/4d02579a-maltasupplemental` (12 October 2026, UTC)

## Repository review (start of session)

- Repo state: `main` = `956dfd9`, branch identical; PR #72 is the latest merge. Open PR #10 (`arena/9327905a`, a different session) is left untouched.
- Existing site: static HTML + seven JSON datasets (218 exact-schema records), a shared renderer (`js/site.js`), a blank-by-default expense planner, Playwright/axe tests and `scripts/validate_site.py`. Baseline gates passed before any edit (validator, JavaScript, Playwright 26/26).
- Environment limit: bash can reach only GitHub and package registries. External pages were read with the web tools (`fetch_page`, `web_search`).

## Protocol adaptation

The parallel protocol asks for one branch per workstream and sub-agents. This session is fixed to `arena/4d02579a-maltasupplemental`, so the workstreams ran **serially in one agent**:

| Workstream | Owned files this session | Dependencies |
|---|---|---|
| A · Transport | `data/transport.json` (wording), `getting-around.html` (rendered) | none |
| B · Food & cafés | none changed (no food re-read in this pass) | — |
| C · Gaming, activities, events | `data/event.json` / `data/activities.json` read only; corrections recorded in logs | A |
| D · Everyday | read only (plug record confirmed on gov.mt) | — |
| E · Sports radio | read only (Kalshi, BFBS, HD Radio) | — |
| F · Expense planner | unchanged (blank by design) | itinerary |
| G · Integration | `scripts/check_weekdays.py`, `package.json`, `index.html` (exec summary), `README.md`, `docs/*` | A–F |

Shared files (`index.html`, `README.md`, `docs/`) were edited once, at integration, not by each workstream.

## Session objectives

1. Re-verify the time-critical trip facts (event dates and venue, teams, opener clocks, the operator's live notices, hotel contact details, plug/voltage, radio and market listings) against live sources, and log each result with a date.
2. Fix any error found, and close the open item where a source resolves it.
3. Add a machine check for the one error class found: weekday/date pairs.
4. Update the executive summary and open questions for anything that changes a decision on the trip.
5. Run the gates, open a PR, merge it into `main`, and record the next-session work.

## Verification gates and passes

- **Pass 1 — implement and verify.** Re-read the operator feed (3 chunks), the organiser finals page, Liquipedia (chunk 0), the PR Newswire release, the hotel contact page, gov.mt, Kalshi events, and HLTV/Fragster/Liquipedia on the NIP replacement. Logged in `docs/SOURCES.md` (top section). Ran `npm test`.
- **Pass 2 — adversarial review.** The new weekday check found three phrasing errors and then flagged the session's own quoted wording. Both were fixed. The fourth opener's “18:30” row was traced to a transcription error (Liquipedia 12:00 EDT = 18:00 Malta). The Route 186 “April 21” notice, which has no year, was kept as an open question (OQ-S7) rather than resolved by guesswork.
- **Pass 3 — full request audit.** Checked the executive summary's claims one by one against the logs. Checked mobile and desktop rendering with a headless screenshot (no horizontal overflow). Recorded what is still unverified (see `docs/OPEN_QUESTIONS.md`, session section, and the handoff).

## Delivery

Commit to `arena/4d02579a-maltasupplemental`, push, open a PR into `main`, wait for the required check, merge by PR number, and record the merge state only after it is observed.

---

## Previous session plan — `arena/5ec909ed-maltasupplemental` (11–12 October 2026, UTC)

## Repository review and integration boundary

The project was reviewed before topic work: GitHub Pages shell, exact 13-field record schema, seven datasets, shared renderer/navigation/CSS, expense planner, source format, status/handoff/open-question logs and CI/Playwright/axe suite are retained. `docs/PLAN.md` remains the coordination and ownership record. This branch is fixed by Arena; A–F run serially on it and G integrates last. No extra workstream branches or parallel agents are claimed.

After PR #71 was opened, `main` advanced through PR #69 (`926c33b`), PR #70 (`8799b1b`) and PR #73 (`1382640`). The updates are being merged into the fixed branch to resolve conflicts and preserve the latest factual corrections. The PR #69 service notices, Kalshi API, forecast/platform reads and browser tests were integrated; PR #70 clarified that the Routes 46/260 and 54/106 notices had already appeared in passing; PR #73 corrected event-ticket attribution, Route 186 directions, review-query scope, ETIAS/weather boundaries and dependent planner wording. Those latest external reads were already logged on `main`; no new source fetch or dated MPT planner/ride query was made in this continuation. Cross-topic findings go in `docs/HANDOFF.md`; unknowns stay in `docs/OPEN_QUESTIONS.md`; sources remain in `docs/SOURCES.md`.

| Stream | Owned files | Integration focus |
|---|---|---|
| **A · Transport** | `data/transport.json`, `getting-around.html` | Keep Stadium 2194 Buġibba return (20:53 static row) separate from Stadium 6227 outbound (about 22:04/22:08); no date-specific result or onward Qawra leg is implied. Preserve notice provenance and compare modes without a taxi default. |
| **B · Food & cafés** | `data/food.json`, `restaurants.html` | Preserve the 10-mile/1,869-result TripAdvisor scope and dated profile sample; no universal ranking or inference from blocked platforms. |
| **C · Gaming, activities, landmarks & events** | `data/activities.json`, `activities.html`, `data/event.json`, `event.html` | Keep Eventbrite event facts separate from the generic recommendation card; no event-specific price, reservation or attendee access is assumed. |
| **D · U.S.-traveler everyday guide** | `data/everyday.json`, `everyday.html` | Keep ETIAS status date-qualified; distinguish Malta national weather coverage (through 18 Oct) from separate UK Met Office/AccuWeather snapshots. |
| **E · Terrestrial sports radio** | `data/radio.json`, `radio.html` | Separate official schedules, trip-date fixtures, Malta carriage, radio market context and physical reception. Listings never stand in for broadcasts. |
| **F · Expense planner** | `data/expenses.json`, `costs.html` | Keep user-specific amounts blank; preserve preview/no-overwrite safeguards, local autosave and export/restore checks. |
| **G · Shared shell, executive summary, integration & delivery (last)** | `index.html`, `README.md`, `docs/*`, shared pages and tests as needed | Integrate corrections without losing A–F evidence; audit current claims against canonical data; run all three passes and gates; record GitHub/Pages only when observed. |

## Cumulative verification passes

1. **Pass 1 — implement and verify:** review the repository and preserve shared setup/schema/source format; integrate the current evidence with source dates and limitations; align canonical records, pages and planner guidance.
2. **Pass 2 — adversarial review:** check event-ticket attribution, route direction/last-row wording, possible onward transit, notice scope, fare/transfer math, taxi/rental assumptions, forecast provider/date, TripAdvisor ranking scope, radio carriage, and stale duplicated copy. Fix contradictions or retain them as explicit questions.
3. **Pass 3 — full request audit:** map the traveler’s stated dates/hotel/event and every requested topic/UI/delivery requirement to the integrated site; rerun validators/browser/accessibility tests; update final report, status, sources, handoff and next-session limits. Push/merge only on the fixed branch and report only observed GitHub state.

---

## Historical mainline plan — `arena/8f0b561b-maltasupplemental` (11 October 2026)

# Malta Trip Guide - Session Plan

## Session: `arena/561bff0e-maltasupplemental` (12 October 2026 UTC)

Repository review at session start (`main` = `ac487ae`, merge of PR #67): the full integrated static Pages site is present — 15 HTML pages, seven exact-schema datasets, shared nav/renderer, CSS tokens, `docs/SOURCES.md` source log, open questions, blank-by-default expense planner with itinerary quick-fill, CI workflow and a Playwright/axe suite — and `python3 scripts/validate_site.py`, the JavaScript checker and all 25 browser tests pass on a clean checkout. **Shared setup is complete and was verified serially before any edit**; nothing is replaced. Arena fixes one branch per session, so the parallel-work protocol runs with the established A–F file-ownership map on this single branch, G integrating shared files last; cross-stream finds go to `docs/HANDOFF.md`, unresolved items to `docs/OPEN_QUESTIONS.md`. (Later in the pass, main advanced with PRs #68–#70 from parallel sessions and was merged into this branch; conflicts were resolved keeping both sessions' blocks, and this session's trip-week-notice additions were folded into the parallel pass's canonical `mpt-trip-week-notices-2026-10-11` record rather than duplicated.)

The trip window opens **13 October — tomorrow** — so this pass is a final **time-critical re-read of the sources that change decisions**, then Passes 1–3 on the integrated result and delivery by PR. No new structure is added unless a fresh read demands it.

| Stream | Owned files | This session |
|---|---|---|
| A · Transport | `data/transport.json`, `getting-around.html` | Re-read the live service-updates feed end-to-end (3 chunks) and the fares page. Folds the 12 October additions (Sunday Marsaxlokk diversions, Dingli diversion, Route 117 on the 14th, Gozo detours, feed-churn caution, 54/106 stop-level wording) into the trip-week notices record; re-confirms the 17–18 October cluster and both Route 186 notices. |
| B · Food & cafés | `data/food.json`, `restaurants.html` | One platform re-check (Yelp, still HTTP 403) recorded in the coverage record; no other change. |
| C · Gaming, activities, landmarks & events | `data/activities.json`, `data/event.json`, `activities.html`, `event.html` | Liquipedia re-read: the upcoming-matches block now names all four Wednesday openers at the EDT clocks that convert to the published Malta times; pairings-corroboration appended to `twc-opening-matchups-14-oct`. |
| D · U.S.-traveler everyday guide | `data/everyday.json`, `everyday.html` | National met panel re-read: now covers 12–18 October (18 October in the national forecast for the first time) with a windy/showery 13th; detailed forecast for the 13th re-read; ETIAS FAQ re-read unchanged. Weather record rewritten around the national panel. |
| E · Sports radio | `data/radio.json`, `radio.html` | Three re-reads (BBC Sportsworld, BBC Sportsound, Radio Sportiva): content unchanged except the Sportsound page now dates its Saturday rows 17/10/2026 and later rows 22 Oct, marginally narrowing the undated Benfica v Celtic row. |
| F · Expense planner | `data/expenses.json`, `costs.html` | Unchanged: amounts stay blank; only confirmed quotes go in. |
| G · Site shell, executive summary & navigation (last) | `index.html`, `js/site.js`, `docs/*`, `README.md`, tests | Executive summary gains an arrival-weather/detour bullet (merged with main's Kalshi bullet); snapshot and footer dates advance; PLAN/STATUS/SOURCES/OPEN_QUESTIONS/HANDOFF/FINAL_REPORT updated; every gate re-run; PR opened and merged by explicit number. |

### Verification gates / passes

1. **Pass 1 — implement and verify:** re-read the time-critical live sources listed above; write only what they say; log every URL and access date in `docs/SOURCES.md`; record the changed gaps in `docs/OPEN_QUESTIONS.md`.
2. **Pass 2 — adversarial review:** check the new claims for overreach (panel-vs-detail weather differences, expired notices still displayed, undated BBC row), confirm every new URL is in the source log, confirm no unverified item is presented as fact, re-run schema/link/JavaScript/browser gates.
3. **Pass 3 — original-request audit:** walk the user’s line-by-line requirements against the integrated tree, confirm the site still answers each, and report only observed PR/Pages state.

## Session: arena/8f0b561b-maltasupplemental (11 October 2026)

This plan and its completion checklist describe the earlier PR #68 documentation pass. It is retained as history; current ownership and verification status are at the top of this file.

### Repository Review

**Starting Point:** Repository at commit `ac487ae472be53b07cc37b1ef839e54460bd6b65` on `main`

**Current State:** The repository contains a comprehensive static GitHub Pages site with:
- 7 JSON data files (transport, food, activities, everyday, radio, expenses, event)
- 15+ HTML pages (index, event, getting-around, restaurants, activities, everyday, radio, costs, hotel, qawra, landmarks, itinerary, logistics, hotspawn, sources)
- Shared CSS (css/style.css)
- JavaScript (js/site.js)
- Documentation (PLAN.md, STATUS.md, SOURCES.md, OPEN_QUESTIONS.md, HANDOFF.md, DATA_SCHEMA.md, FINAL_REPORT.md)
- CI workflow with validation tests
- Canonical 13-field schema for all records

**Trip Context:**
- Hotel: AX ODYCY Malta, Qawra Coast Road, Qawra SPB 1902, Malta
- Room: Deluxe sea view
- Dates: 13th October 2026 - 19th October 2026
- Event: Counterstrike 2 Thunderpick World Championship 2026 at BLAST Arena Studios, Attard
- Website: https://axhotelsmalta.com/odycy/

### Session Objectives

Complete the work to satisfy the entire user prompt through three verification passes:

1. **Pass 1: Implement and verify** - Review all existing work, verify facts, fill gaps
2. **Pass 2: Adversarial review** - Check for bugs, missing requirements, incorrect assumptions
3. **Pass 3: Full request audit** - Map every line of the original request against the integrated result

### Workstream Ownership (Parallel Work Protocol)

| Stream | Owned Files | Focus | Status |
|---|---|---|---|
| **A · Transport** | `data/transport.json`, `getting-around.html` | Airport/hotel/event travel, public bus routes (especially hotel to BLAST Arena Studios), fares, cards, return options, taxi/ride-hailing, rentals, ferries. Compare feasibility, convenience, price, value. | To Do |
| **B · Food & cafés** | `data/food.json`, `restaurants.html` | Qawra/hotel and Malta eateries with Google Reviews, Google Maps, Yelp, Instagram, TikTok, Facebook, Reddit, X sources. Organize by popularity, categories, sections. | To Do |
| **C · Gaming, activities, landmarks & events** | `data/activities.json`, `activities.html`, `data/event.json`, `event.html` | Gaming centers, PC cafes, arcades, landmarks, dated events during trip window. | To Do |
| **D · Everyday life (US traveler)** | `data/everyday.json`, `everyday.html` | Plugs/voltage, SIM/eSIM, money/tipping, safety, health, customs, language, weather. All with official sources. | To Do |
| **E · Sports radio** | `data/radio.json`, `radio.html` | Malta stations, frequencies (FM/DAB+), official schedules, trip-date listings for EPL, soccer, sports broadcasts. Verify live over radio with AM/FM/DAB+ devices. | To Do |
| **F · Expense planner** | `data/expenses.json`, `costs.html` | Data-driven template, quick to fill once itinerary arrives. | To Do |
| **G · Site shell, executive summary & navigation** | `index.html`, `js/site.js`, `css/style.css`, `sources.html`, `README.md`, `docs/*` | Integrates all workstreams, navigation, executive summary, shared files. Runs last. | To Do |

### Conflict Avoidance Rules

1. **File Ownership:** Each workstream edits ONLY its owned files
2. **Shared Files:** Only workstream G edits shared files (navigation, index, CSS, README, executive summary)
3. **Cross-Stream Findings:** Add to `docs/HANDOFF.md`, not to another stream's files
4. **Unverified Items:** Record in `docs/OPEN_QUESTIONS.md`, never present as fact
5. **Branch Strategy:** One branch per workstream, but Arena provides fixed branch, so work serially

### Data Schema (Canonical 13 Fields)

All records must include:
1. `id` - Unique identifier
2. `name` - Display name
3. `category` - Classification
4. `area` - Geographic area
5. `address` - Physical address
6. `hours` - Operating hours
7. `price range` - Cost information
8. `description` - Detailed description
9. `source_url` - Verifiable source URL
10. `source_type` - official/map/review/social
11. `date_checked` - When verified
12. `confidence` - verified/partially verified/unverified
13. `notes` - Additional context

### Verification Gates

#### Pass 1: Implement and Verify
- [ ] Re-read highest-risk sources (Eventbrite, MPT, BBC, EU pages)
- [ ] Verify all existing claims have sources
- [ ] Fill any critical gaps (especially transport routes, radio schedules)
- [ ] Ensure every fact has a source in `docs/SOURCES.md`
- [ ] Record unverified items in `docs/OPEN_QUESTIONS.md`

#### Pass 2: Adversarial Review
- [ ] Check for overreach in claims
- [ ] Verify all URLs work
- [ ] Confirm no unverified item is presented as fact
- [ ] Check mobile and desktop layout
- [ ] Test navigation and links
- [ ] Validate data/page consistency
- [ ] Run `npm test` (validator + JS + Playwright/axe tests)

#### Pass 3: Full Request Audit
- [ ] Map every line of original request to implemented solution
- [ ] Verify accuracy, reliability, completeness
- [ ] Check code quality
- [ ] Run full local gate suite
- [ ] Open PR from this branch
- [ ] Merge PR to main
- [ ] Observe GitHub Pages build
- [ ] Write final report

### Delivery Checklist

- [ ] All workstreams A-F complete their updates
- [ ] Workstream G integrates all changes
- [ ] All three passes complete
- [ ] `docs/SOURCES.md` updated with all new URLs
- [ ] `docs/OPEN_QUESTIONS.md` updated with remaining gaps
- [ ] `docs/STATUS.md` updated with final status
- [ ] `docs/FINAL_REPORT.md` written
- [ ] PR opened from `arena/8f0b561b-maltasupplemental`
- [ ] PR merged to `main`
- [ ] GitHub Pages build verified

### Key Requirements from User Prompt

1. ✅ Tourism and recreation website for Malta trip
2. ✅ Research from Google Reviews, Google Maps, Yelp, Instagram, TikTok, Facebook, Reddit, X
3. ✅ Organized into categories, sections, subpages
4. ✅ Easy to read on desktop and mobile
5. ✅ Easy to find activities, events, places to eat
6. ✅ Guide for best way to get around Malta (public transport, ride share, etc.)
7. ✅ Everyday life for US traveler (plugs, SIM, money, safety, etc.)
8. ✅ Separate section for live radio sports broadcasts (AM/FM/DAB+)
9. ✅ Official schedules from radio stations
10. ✅ Trip-date listings for radio broadcasts
11. ✅ Expense planner template, quick to fill with itinerary
12. ✅ Clean UI, user-friendly, simple
13. ✅ Sections and subpages for different topics
14. ✅ Executive summary
15. ✅ All information in easy-to-read format
16. ✅ Official verified links as sources
17. ✅ Line-by-line verification, no hallucinations
18. ✅ Three passes of verification
19. ✅ Create PR and merge to main

### Dependencies

- Shared schema (`data/record.schema.json`) - FROZEN
- Navigation renderer (`js/site.js`) - FROZEN until G
- CSS tokens (`css/style.css`) - FROZEN until G
- Source log format (`docs/SOURCES.md`) - FROZEN

### Session Execution Order

1. **Serial Phase (this session):**
   - Review repo (COMPLETE)
   - Update this PLAN.md (IN PROGRESS)
   - Workstream A: Transport updates
   - Workstream B: Food & cafés updates
   - Workstream C: Activities & events updates
   - Workstream D: Everyday life updates
   - Workstream E: Sports radio updates
   - Workstream F: Expense planner verification
   - Workstream G: Integration and finalization

2. **Pass 1:** Implement and verify all updates
3. **Pass 2:** Adversarial review of all changes
4. **Pass 3:** Full audit against original request
5. **Delivery:** PR → Merge → Verify Pages build

### Notes

- Arena provides one fixed branch: `arena/8f0b561b-maltasupplemental`
- No isolated workstream runners available
- All workstreams execute serially on this branch
- Strict file ownership enforced
- Cross-topic findings → `docs/HANDOFF.md`
- Unverified gaps → `docs/OPEN_QUESTIONS.md`
- Final integration by G

---

## Historical mainline plan — `arena/2b38c9c6-maltasupplemental` (11 October 2026)

Started at `main` `ac487ae` (PR #67 merge), clean tree. Repository review confirmed the unchanged structure: 15 static pages, seven topic datasets (216 records at review time), the canonical 13-field schema, per-topic pages rendered from JSON by `js/site.js`, `docs/SOURCES.md`, `docs/OPEN_QUESTIONS.md`, the blank-by-default expense planner, the CI workflow and a 25-test Playwright/axe suite. Nothing is rebuilt; shared setup (schema, navigation/renderer, CSS tokens, source-log row format) was re-verified first and left intact. Arena fixes one branch per session, so A–F run serially on this branch under the same ownership map and G integrates last; cross-stream notes go to `docs/HANDOFF.md`.

This pass targets the one prompt requirement whose evidence base was still secondary: **the Kalshi question in the sports-radio section**, plus fresh reads of the trip's most decision-relevant live sources two days before departure.

| Stream | Owned files | This session |
|---|---|---|
| A · Transport | `data/transport.json`, `getting-around.html` | Full three-chunk read of the operator service-updates feed: reconfirmed the 17–18 October cluster and promoted two trip-window notices (Routes 46/260 Mon–Thu 21:00–05:00, 12–16 October; Routes 54/106 daytime Attard detours on 13 October) from a passing mention in the diversion record into their own stop-level record; re-read fares (no change) and TQ1 (still “Timetable not available!”). |
| B · Food & cafés | `data/food.json`, `restaurants.html` | No new platform access: Yelp and Reddit returned HTTP 403 again and Google Maps returned a JavaScript shell, so the platform-coverage limits are re-confirmed rather than restated as fresh evidence. No record change. |
| C · Gaming, activities, landmarks & events | `data/activities.json`, `data/event.json`, `activities.html`, `event.html` | Eventbrite listing re-read in full: venue, dates, 18+ rule, Wed–Fri agenda rows and the hidden Saturday/Sunday rows unchanged. No record change. |
| D · U.S.-traveler everyday guide | `data/everyday.json`, `everyday.html` | Second Met Office Valletta read now covering 13–21 October, recorded alongside the earlier same-day snapshot; no other everyday change. |
| E · Sports radio | `data/radio.json`, `radio.html` | **Primary-source addition:** the exchange's own public API confirms which trip-window fixtures have open markets (EPL 17–19 October, Champions League 13–14 October, NFL 18 October, CS2 sampled to 13 October with no Thunderpick fixture, Serie A future only). New page section and record keep market listings strictly separate from radio carriage. |
| F · Expense planner | `data/expenses.json`, `costs.html` | Unchanged and still blank by design; no amounts are invented while no itinerary is supplied. |
| G · Site shell, executive summary & navigation (last) | `index.html`, `sources.html`, `README.md`, `js/site.js`, `css/style.css`, `docs/*`, tests | Integrate the new evidence, log every URL, add a regression test for the market-versus-radio distinction, run the full gate suite, then deliver by PR and record the observed merge and Pages state. |

### Verification gates / passes

1. **Pass 1 — implement and verify:** each stream re-reads its live sources, writes only its owned data/page pair, and logs every claim with URL and date; anything not confirmed is recorded as printed-but-unresolved, not smoothed over.
2. **Pass 2 — adversarial review:** check the new records for overreach (market listing vs. radio carriage, notice year ambiguity, forecast volatility), confirm no unverified item is presented as fact, and re-run validator, JavaScript and browser gates.
3. **Pass 3 — original-request audit:** walk the user's line-by-line requirements against the integrated tree and report verified vs. unverified, limitations and next-session work.

## Previous Session Plans (Preserved for Reference)

See historical sections below for previous session plans and deliveries.
