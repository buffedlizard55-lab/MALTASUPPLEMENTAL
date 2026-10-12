# Current session plan — `arena/5ec909ed-maltasupplemental` (11 October 2026, UTC)

## Repository review and integration boundary

The session began on the fixed Arena branch at `ac487ae` (PR #67 merge), with the existing GitHub Pages site, seven JSON datasets, exact 13-field schema, shared renderer/navigation/CSS, source/open-question/status/handoff logs, expense planner, CI and Playwright/axe suite already present. `docs/PLAN.md`, `data/record.schema.json`, `js/site.js`, `css/style.css` and the source-log format were reviewed before topic edits; preserve them unless an integration defect is found. `origin/main` had advanced to `4725130` with PR #68 and a follow-up documentation commit, so the branch was fast-forwarded on the same fixed branch before edits. PR #68's documentation is an upstream snapshot, not evidence that the current factual claims are correct.

Arena pins this session to `arena/5ec909ed-maltasupplemental`; workstreams A–F therefore run serially on this branch, each respecting the established file ownership. No extra branches or parallel agents are claimed. Cross-topic findings go to `docs/HANDOFF.md`; unresolved claims go to `docs/OPEN_QUESTIONS.md`. G updates shared pages and documentation last.

| Stream | Owned files | This session's focus |
|---|---|---|
| **A · Transport** | `data/transport.json`, `getting-around.html` | Adversarially review the dated hotel↔Attard bus plan and the unlabelled Route 186 variants; retain uncertainty rather than promise a return. Keep fare-season inference, taxi/ride-hail quotes and saved journeys distinct. |
| **B · Food & cafés** | `data/food.json`, `restaurants.html` | Reconcile current access notes without presenting limited platform samples as a universal popularity ranking; no new reviews are asserted. |
| **C · Gaming, activities, landmarks & events** | `data/activities.json`, `activities.html`, `data/event.json`, `event.html` | Correct the Eventbrite ticket-price/action attribution; preserve age/date/visible-agenda evidence but do not infer ticket price or reservation from a recommendation card. |
| **D · U.S.-traveler everyday guide** | `data/everyday.json`, `everyday.html` | Align the ETIAS page with the current EU FAQ's no-action/several-months-notice statement; refresh the 13–19 Oct forecast record from current official pages and retain forecast disagreements. |
| **E · Sports radio** | `data/radio.json`, `radio.html` | Preserve the separate terrestrial-radio scope and distinguish station schedules, Malta carriage, receiver compatibility, reception and online streams. |
| **F · Expense planner** | `data/expenses.json`, `costs.html` | Keep all user-specific amounts blank; verify the existing planner and do not invent itinerary costs. |
| **G · Shell, executive summary, integration & delivery (last)** | `index.html`, `README.md`, `docs/*`, tests and shared pages as needed | Reconcile source/status/open-question/handoff/report files, scan all current claims for contradictions, run the full suite, open a PR only after local gates and record observed PR/Pages state. |

## Cumulative verification passes

1. **Pass 1 — implement and verify:** review the integrated baseline and the highest-risk sources; correct the ticket, ETIAS and weather claims; record each source/date and retain explicit confidence/limits.
2. **Pass 2 — adversarial review:** scan for stale price, admission, route, timetable, timezone, forecast and status language; verify data/page consistency, links, responsive behavior and planner edge cases; fix overclaims or move them to open questions.
3. **Pass 3 — full request audit:** map every requested trip topic and UI/delivery requirement to the integrated site; rerun all local checks; document verified facts, unresolved items, tool/access limitations and next-session tasks. Push and open a PR from this branch; merge only after required checks and mergeability are observed.

---

## Historical mainline plan — `arena/8f0b561b-maltasupplemental` (11 October 2026)

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

## Previous Session Plans (Preserved for Reference)

See historical sections below for previous session plans and deliveries.
