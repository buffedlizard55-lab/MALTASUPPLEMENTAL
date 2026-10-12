## Current session plan — `arena/57ad3983-maltasupplemental` (11 October 2026)

### Repository review and shared setup (completed before topic work)

At task start the fixed Arena branch was based on `ac487ae`. Before delivery, upstream main was fast-forwarded through PRs #68–70 to `8799b1b`; their Kalshi, trip-week notice and weather updates were preserved. The repository already contains a static GitHub Pages site, shared navigation/rendering and CSS, the canonical 13-field record schema, seven JSON datasets, topic pages, a source log, open-question/status/handoff records, an expense planner, and CI plus JavaScript/Playwright/axe checks. Preserve that setup: do not replace or reformat unrelated files. No isolated sub-agent/branch runner is available in this session; execute A–F serially on the required fixed branch, keep each stream within its owned files, and run G only after topic work. Cross-topic discoveries go in `docs/HANDOFF.md`; unresolved claims go in `docs/OPEN_QUESTIONS.md`.

### Workstreams, owned files, dependencies

| Stream | Owned files | Dependencies / boundary |
|---|---|---|
| **A · Transport** | `data/transport.json`, `getting-around.html` | Use the user-supplied AX ODYCY and BLAST Arena Studios locations, but verify the event venue/date and operator details. Event-day routing depends on confirmed event dates/times and current operator service notices. Compare bus, taxi/ride-hail, rental and other modes only where evidence supports cost/feasibility. |
| **B · Food & cafés** | `data/food.json`, `restaurants.html` | Near-hotel shortlist; review/social platforms are discovery signals, not proof of current hours, prices or popularity. Record access/coverage limits rather than infer missing platform results. |
| **C · Gaming, activities, landmarks & event** | `data/activities.json`, `data/event.json`, `activities.html`, `landmarks.html`, `event.html` | Verify named venues and trip-window events. Event records provide A's date/venue inputs; unannounced agenda, access, hours and ticket inventory remain open. |
| **D · US-traveler everyday guide** | `data/everyday.json`, `everyday.html` | Official country/operator sources for entry, power, money, connectivity, safety, health, language and weather. Weather/entry guidance is date-sensitive and needs a trip-window check. |
| **E · Live sports radio** | `data/radio.json`, `radio.html` | A listed sport fixture is not proof of Malta radio carriage. Separate station schedule, rights, local frequency/service, trip-date programme listing and actual reception; event/fixture dates must be checked. |
| **F · Expense planner** | `data/expenses.json`, `costs.html` | Keep prices/amounts blank unless supported by an actual booking or quote. Build for quick input after itinerary/party details arrive; verify persistence/export/edge cases. |
| **G · Site shell, executive summary, navigation and integration (last)** | Shared shell/pages as needed, `README.md`, `docs/*`, tests | Integrate A–F without changing their facts, maintain sources/open questions/status, run integration and all three review passes on the integrated result. |

### Verification and delivery passes

1. **Pass 1 — implement/review:** check each stream's claims against accessible primary sources; every record has a source URL, source type, check date, confidence and notes. No unsupported detail is written as fact.
2. **Pass 2 — adversarial review:** inspect for stale dates, unverified platform claims, schema/data-page drift, broken navigation/links, desktop/mobile and planner edge cases; fix or explicitly record blockers.
3. **Pass 3 — original-request audit:** map the deliverable against the user's complete brief, run the full test suite, update `docs/STATUS.md`, `docs/OPEN_QUESTIONS.md`, `docs/SOURCES.md`, `docs/HANDOFF.md` and the final report. Open and merge a PR only if checks pass; the session may push only `arena/57ad3983-maltasupplemental`.

### Integrated review execution — 11 October 2026

- **Pass 1:** preserved the existing Pages shell, schema, datasets, source-log format and planner. The evidence already logged for the current trip-week review, including the latest upstream Kalshi, trip-week service-notice and weather updates, was carried into the integrated tree; this final review did not create a new live-source observation. Claims that remain date-, checkout-, or device-dependent are still explicitly open.
- **Pass 2:** searched the integrated pages and data for stale admission, fare/transfer, return-direction and taxi assumptions. Corrected the residual expense-page statement that tickets were advertised as free, the “taxi every event night” budget advice, and older wording treating a late taxi as the default. Rechecked that Eventbrite’s generic recommendation card is not attributed to TWC; Route 186’s 20:53 Buġibba return is separated from 22:04/22:08 outbound rows at the other Stadium stop; a static table is not a date-specific planner result; one fare is conditional on MPT’s published two-hour rule; and no vehicle, booking, fare split, finish time or return is assumed. Fixed joined adjacent `<li>` source formatting without changing page content.
- **Pass 3:** checked the original requirements against the integrated overview, event desk, seven-day public-transport comparison, food/review-methodology page, activities/landmarks, U.S.-traveler guide, separate official-schedule radio section, expense planner, sources, handoff and open questions. Validator confirms pages project canonical data. Remaining travel-, ticket-, price-, forecast- and reception-specific gaps are reported in `docs/OPEN_QUESTIONS.md` and the final report.

**Local gates on the integrated tree (12 October 2026 UTC):** `npm test` PASS — 7 JSON files / 218 exact-schema records / 351 unique record URLs logged / 15 HTML pages / 374 link attributes / 9 shared navigation destinations / 25 expense rows; shared and inline JavaScript syntax PASS; Playwright **26/26 PASS**, including axe at 320, 360, 768, 1024 and 1440 px, event/date projection, radio and market tables, project-prefix links, and expense import/export/quick-fill edge cases. `git diff --cached --check` PASS. These tests verify local structure, behavior and accessibility, not external link uptime, ticket availability, transport operations, radio carriage or physical reception.


---

## Preserved plan history from the latest integrated main

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

## Current session plan — `arena/2b38c9c6-maltasupplemental` (11 October 2026)

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
