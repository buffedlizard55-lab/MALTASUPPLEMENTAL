# Malta trip guide — final report

**Audit date:** 11 October 2026 (UTC)
**Session branch:** `arena/502e2dae-maltasupplemental`
**Baseline:** `origin/main` at `b307c51` (merge of PR #33), reconciled with `origin/main` at `852343f` (parallel-session PRs #42–47) via a conflict-resolved merge that keeps both sessions' net-new corrections.

### CS2 event and access

This session ran the requested multi-pass protocol over the integrated tree: **Pass 1** implemented and verified the full request; **Pass 2** reviewed for bugs, missing requirements, incorrect assumptions and edge cases; **Pass 3** re-checked the implementation against the original request and improved accuracy, reliability and completeness. The highest-risk factual claims (event listing, Route 186 return, fare seasons, card terms, radio schedules) were re-verified line by line against live sources on 11 October 2026 before any wording changed. Mid-session, the parallel work merged upstream (PRs #42–47: the `event.html` CS2 event guide + `data/event.json`, the TQ1 special-event-service lead, the Transport Malta taxi-tariff record, AX ODYCY FAQ evidence and an MTA guideline re-read) was reconciled into this branch by content, with both sides' corrections preserved.

The delivered site remains the repository's static, JSON-backed Malta trip guide and blank-by-default expense planner. The seven datasets use the shared exact 13-field schema (key order normalized). Merged-tree counts: **184 records** (transport 28, food 39, activities 44, everyday 19, radio 21, expenses 25, event 8), **303 unique record URLs** in the source log, 15 HTML pages, 219 checked link attributes, nine shared navigation destinations, and 25 expense rows.

This is a sourced planning aid, not a booking, admission, price, service, schedule, or reception guarantee. Dates, hotel, and intended venue are traveler-supplied inputs except where separately corroborated.

## Next session — priority order

### Thunderpick World Championship / admission

The Hotspawn/Eventbrite listing was re-read directly and matches the parallel session's confirmed framing: it names *Hotspawn present the Thunderpick World Championships 2026* at BLAST Arena Studios Malta, MFCC South Gate National Stadium, Attard ATD 4000, Wednesday 14 – Sunday 18 October 2026, 9:30 AM – 10 PM, in person, **18+**, with a **“Free”** ticket block and a “Reserve a spot” action under a “Sales end soon” notice. Agenda rows remain visible for Wed 14 / Thu 15 (09:30–22:30) and Fri 16 (14:00–21:00) only; Saturday/Sunday sit behind “Show all agenda”. The headline-vs-rows finish discrepancy (22:00 vs 22:30) persists. Reserve before travel and carry photographic ID. Still open: current inventory, the traveler’s reservation, whether one reservation covers all five days, per-day scanning, transferability, parking/catering, and the attendee gate. The new `event.html` guide (8 records) carries the detailed day-by-day and access material; the Virtus.pro → Ninjas in Pyjamas team substitution remains third-party-reported (OQ-H5) and is labelled as such.

### Public transport — the event-day return problem (core requirement)

The operator’s live Route 186 page was parsed stop by stop, both directions, all published grids:

- **Return (the binding constraint):** the last Stadium 2194 departures toward Buġibba are **20:53 and 20:54** on the published return grids, reaching Buġibba Bay 1 at 21:26 and 21:36. The earlier “one static variant” hedge is replaced: the figure is confirmed on the operator’s current route page. Which grid applies on which trip date is not labelled, so the date-specific planner remains the authority.
- **Outbound:** Qawra stop 952 departures toward the venue run to about 21:39 (Stadium 6227 to about 22:04–22:08); Route 186 reaches the venue in time even for the 09:30 check-in. Getting to the event is not the problem — getting back is.
- **Return path:** the toward-Buġibba direction does not serve any Il-Qawra stop; it terminates at Buġibba Bay 1 (2527), so a second boarding (or walk/taxi from Buġibba) is required. One single fare covers both legs inside the two-hour transfer window.
- **Saturday 17 October detour:** the omitted span “Gholja 2 through Targa” sits **between** the Stadium 2194 boarding stop and the Buġibba terminus on the operator’s own stop lists — the traveler’s boarding and alighting stops are not among the omitted stops. The diverted path and timing remain unpublished, so a particular departure could still be re-timed. Both operator pages read the October window as 19:00–00:00 (an earlier 20:00–24:00 reading was superseded during reconciliation: that window belongs to a separate weekly notice ending 21 April).
- **Late-return leads (unverified, recorded, not claimed as journeys):** Route 202 from the same Stadium 2194 stop toward Sliema is listed on the operator’s route page to about 22:08; night route N212 links Sliema–Buġibba (23:50–01:30); night route N48 is listed at Mosta-corridor stops (Gholja 2, Rotunda 2, Targa) and can be reached via the Ta’ Qali P&R shuttle 405. Moovit’s later 23:07 last-202 figure conflicts with the operator page — logged, operator planner authoritative.
- **One thing could still fix the return:** MPT runs **TQ-numbered special-event services** out of Ta’ Qali for major events (parallel session’s finding), and TQ1’s corridor runs through St Paul’s Bay and Qawra to Buġibba at the €3.00 Special Services fare. The TQ1 page displayed “Timetable not available!” when checked and no TWC notice was found — check service updates daily during 14–18 October.
- **Taxi fallback with an honesty caveat:** Transport Malta publishes **maximum** meter rates (initial €3.50, then €2.50/km stepping down to €0.85/km beyond 20 km, €25/hour waiting, €4.20/hour in traffic), but the page footer says “last updated 06/04/2022”. The worked caps on the site (≈€12.40 at 5 km, €19.40 at 10 km, €25.90 at 15 km, €30.90 at 20 km) are this project’s arithmetic at assumed distances, not quotes; the Qawra-to-venue road distance was never measured; ride-hailing is dynamic and unbound by the tariff. Pre-book rather than hail — no taxi rank at an inland studio was verified.

### Fares — a dated conclusion changed by new evidence

The official fares page, re-read 11 October, still prints only the expired winter window “19 October 2025 to 13 June 2026”. The previous audit **rejected** the €2.50/€2.00 split inference because no source stated the season boundary. This session found two independent third-party 2026 fare guides that do state it — summer singles 14 June–18 October (€2.50), winter singles from 19 October (€2.00) — matching the official window’s own 19-October winter start date. The split is therefore reinstated at **“partially verified”** as a planning inference (€2.50 on 13–18 October; €2.00 on 19 October), explicitly labelled as secondary-guide evidence, not operator confirmation, and not prefilled into the planner. Full published table: day single €2.50 summer / €2.00 winter (two-hour transfers), night €3.00, Special Services €3.00, tallinja Direct €3.00, TD1 €3.50, €19 shareable 12-journey card (Night/Airport Direct count 2 journeys per trip), €25 Explore Adult 7-day (excludes tallinja Direct), €21/€27 Explore Flex 4/7-day (include Airport Direct; €6 two-trip airport add-on), €7 Explore Child, €50 fine. Cards sell at Buġibba Terminal, the closest listed office. The fares page **contradicts itself** on whether Explore Adult 7-day includes Airport Direct — disclosed rather than resolved.

### Sports radio

BBC programme pages reconfirm the UK 17–18 October commentary listings (5 Live Sport grid; episode m00334k6; seven named matches including Bournemouth–Sunderland on 5 Sports Extra 2). These remain UK schedules only. The strongest English-language Malta lead is a DAB+ service named “Sports Channel” (“Talk Sport” on 6C per one Maltese directory; generic on 12A per WorldDAB; absent from the operator list) — a scan lead, not carriage. NET FM is 101 MHz (Friday 18:30, Saturday 16:00, Sunday 15:00 sports slots); **Vibe FM 88.7 FM / DAB+ is the published Malta Premier League radio partner**; BBC World Service *Sportsworld* episodes are dated on DAB+ 6A; Rai Radio 1’s weekend *Tutto il calcio minuto per minuto* is the most likely live Serie A. No station publishes a dated trip-week named-match lineup; no physical scan was possible; a US HD Radio set cannot decode DAB+ (buy one in Malta). Kalshi’s travel-abroad policy conflict is recorded; no market-to-broadcast link is inferred.

### Everyday life, expenses, food/activities

Everyday content matches checked sources with the parallel session’s refinements: Type G 230 V/50 Hz (the hotel FAQ adds a **razor-only** 110 V bathroom socket that must not be used for chargers), AX ODYCY’s own 10–15% tipping expectation vs secondary 5–10% guidance (both shown, neither prescribed), and the MTA eco-contribution narrowed by the guidelines’ own “interruption” definition (the 15-day reference is not a minimum-stay threshold) while the webpage wording stays recorded and the invoice remains authoritative (six nights ≈ €9 is conditional). The EES enforcement conflict (EU vs September secondary reporting) remains recorded, not resolved. The expense planner stays blank by default with preview-then-apply quick-fill, autosave, CSV export and reset; the event evenings’ return is planned as taxi/ride-hailing with amounts left to live quotes. Food/activities disclose platform limits (Yelp/Instagram/TikTok/Facebook/X blocked or limited).

## Cumulative verification passes (this session)

1. **Pass 1 — implement/verify:** baseline gates green; every requirement mapped to a page/record; live re-reads produced the findings above; data/pages/docs updated consistently (workstream order, one writer per file per step).
2. **Pass 2 — review:** static and runtime deep-link resolution checked (0 broken); JSON key order normalized to the canonical 13-field order; the fare-inference reversal documented against the previous audit; detour-scope, card-terms and late-return-lead edge cases added; merge reconciliation with PRs #42–47 resolved by content with line-level checks; stale-phrase scans for superseded “static variant”/“fare unconfirmed” wording.
3. **Pass 3 — re-check vs request:** hotel/event/itinerary facts rechecked against the rendered pages; the Kalshi/radio requirement, everyday US-traveler section, expense quick-fill, Pages structure and source-citation requirements reconfirmed; final gates re-run after edits and after the merge.

## Requirement-by-requirement check (merged tree)

| Original request | Where it is answered | Status |
|---|---|---|
| Transport: airport, hotel ↔ BLAST Arena Studios on event days; compare transit/ride-share/rentals on convenience, price, value, feasibility | `getting-around.html`, `data/transport.json` (28 records incl. mode comparison, taxis, rentals) | Answered with a documented return gap and priced fallbacks; no date-specific journey or live quote yet |
| Public transport to the venue on event days | Route 186 Qawra 952 → Stadium 6227 traced; MFCC booklet endorses 186/202/56 | Outbound answered; return limited by the 20:53/20:54 last departures |
| Food/cafés from Google/Yelp/IG/TikTok/FB/Reddit/X, organized in categories/subpages | `restaurants.html`, `data/food.json` (38 records) | Answered within disclosed platform limits |
| Gaming centres, activities, landmarks, events in the trip window | `activities.html` (39 records), `event.html` + `data/event.json` (8 records) | Answered; out-of-window events recorded as excluded |
| Everyday guide (plugs, SIM/eSIM, money/tipping, safety, health, customs, language, weather) | `everyday.html`, `data/everyday.json` (18 records) | Answered; tipping and EES conflicts documented |
| Radio sports broadcasts with verified official schedules; Kalshi-market sports | `radio.html`, `data/radio.json` (20 records) | Partly answered: schedules verified; Malta carriage/reception unverified by design |
| Expense planner template quick to fill when the itinerary arrives | `costs.html`, `data/expenses.json` (25 rows) | Answered — blank defaults + preview-then-apply quick-fill |
| Executive summary, clean desktop/mobile UI, official source links | `index.html`, 9 active pages, shared renderer, axe/Playwright | Answered; 320/360/768/1440 px verified |
| Verify line by line, no hallucinations | `docs/SOURCES.md` (311 URLs), `docs/OPEN_QUESTIONS.md`, per-record confidence | Enforced: validator fails on a record URL absent from the log |
| PR created and merged to `main`; report with suggestions and limitations | This document + delivery snapshot | See below |

## Validation results (observed after edits and merge reconciliation)

- `python3 scripts/validate_site.py` — **PASS**: 7 JSON files / 184 exact-schema records / 303 unique source URLs / 15 HTML pages / 219 link attributes / 9 navigation destinations / 25 expense rows.
- `python3 scripts/check_javascript.py` — **PASS**; `node --check js/site.js` — **PASS**.
- Internal deep-link check (static ids + runtime record ids): **PASS** — 0 broken.
- `npm ci` / `npm test`: **PASS**, 21/21 Playwright on the merged tree (320/360/768/1024/1440 px, axe WCAG 2A/AA/2.1AA, data/render parity, navigation/deep links, planner persistence/CSV/JSON-restore/reset, quick-fill, storage-denial and data-fetch-failure cases).
- `git diff --check`: **PASS**.

These gates check local structure and behavior. They do not certify external-link liveness, current ticket availability, physical access, radio reception, or a dated transit journey.

## Remaining limitations

1. **No reservation, no admission.** The listing says “Sales end soon”; nothing here substitutes for reserving it, and Sat/Sun agenda remains unpublished.
2. **No measured journey.** No attendee gate, no walk distances, no date-specific planner result, no live taxi quote, no verified Buġibba → Qawra connection.
3. **No published trip-week fare** (the likely split is an inference) and a taxi tariff page last updated in 2022.
4. **No radio reception test** and no Malta carriage confirmation for any named match; UK BBC schedules prove nothing about Malta.
5. **Volatile data by nature:** hours, menus, closures, ticket inventory, diversion notices and the forecast can change between this snapshot (11 October 2026) and travel.
6. **Platform coverage is incomplete:** Yelp, Instagram, TikTok, Facebook and X were blocked or limited; social evidence is dated snapshots, not a ranking.
7. **Traveler-specific inputs are absent:** booking confirmation, party size/ages, flights, meal plan, device, insurance, personal spend.
8. **The offline validator is not a web crawler:** a cited URL can rot without the suite noticing.

## Suggestions for the next session (priority order)

1. **Event access (highest value):** ask Hotspawn/Thunderpick to confirm the traveler’s reservation, current inventory, attendee gate, per-day scanning/validity (one reservation for five days?), the 17–18 October agenda, and the 22:00-vs-22:30 finish discrepancy. Re-read the listing daily as the event approaches.
2. **Transit:** run the MPT planner for each event date both ways with the confirmed gate; determine which Route 186 grid (20:53 or 20:54) applies and whether event extra service exists; **check for TQ1/TQ special-event announcements daily during 14–18 October** (the one development that could restore a bus return); verify the after-20:54 fallback legs (202 → Sliema → N212; 405 → Mosta → N48) as date-specific journeys; recheck both diversion pages for 16–17 October; measure the Qawra-stop-to-hotel and Stadium-to-gate walks; obtain one live evening taxi/ride-hailing quote from the venue to Qawra and compare it against the Transport Malta tariff.
3. **Fares:** confirm the likely €2.50 (13–18 Oct) / €2.00 (19 Oct) split with MPT or a sales point; resolve the Explore Adult 7-day Airport Direct contradiction before buying any card.
4. **Radio:** with a DAB+ receiver bought in Malta, scan 6A/6C/12A and FM at the hotel and venue; record service names, blocks and audio; confirm any named-match carriage with the station (NET FM, Vibe FM, the “Sports Channel”); recheck BBC/Rai/talkSPORT schedules close to air time.
5. **MTA contribution:** the guidelines’ “interruption” reading narrows the question; use the invoice and ask AX ODYCY to confirm the billed amount.
6. **Planner hand-off:** paste the confirmed itinerary into the quick-fill panel (it fills only blank budget fields after preview); export a CSV before switching devices.
7. **Coverage limits:** recheck accessible platforms and volatile menus/hours/closures without implying comprehensive coverage.

Full claim-specific source rows are in `docs/SOURCES.md`; unresolved items in `docs/OPEN_QUESTIONS.md` (including OQ-H5 team substitution); ownership/dependencies in `docs/PLAN.md`; cross-workstream notes in `docs/HANDOFF.md`; the dated claim audit in `docs/AUDIT_2026-10-11.md`.

## Delivery snapshot

Prior observed deliveries on the baseline: pull request **#43** merged at 15:54:56 UTC on 11 October 2026 (`94733df`), with CI and Pages **built** and the live site spot-checked; PRs **#42**, **#44**, **#45**, **#46** and **#47** were merged by explicit number by the parallel sessions and reconciled into this branch (PR #46's fresh full-page reads corrected the Route 186 detour window claim — adopted here; its merge and Pages build were recorded on main via PR **#50**); PR **#49** (source-led refresh, planner hardening, expanded test suite) landed on `main` mid-delivery and was reconciled here by content as well — its new records (`food-platform-coverage`, `water-medication-daily-health`, and others) are preserved. This session’s delivery (PR opened, merged by explicit number onto `main`, Pages build) is reported only after those facts have been checked; this file is not a live CI/Pages dashboard.


---

# Session report — `arena/09cdfbf0-maltasupplemental` (11 October 2026)

**Baseline:** `origin/main` at `250e6bd`. **Scope of this session:** re-verification and gap-closing, not a rebuild. The
site structure, planner and evidence discipline were already in place and were reviewed rather than replaced.

## What this session verified

- **Event (corroborated, not merely repeated).** Thunderpick World Championship Finals run **14–18 October 2026** at
  **BLAST Arena Studios, Attard**, eight teams, $1,000,000 pool — independently consistent across HLTV, Liquipedia,
  Hotspawn and the organiser's own release. The **Ninjas in Pyjamas for Virtus.pro** substitution is confirmed as current
  (9 October reporting, corroborated by Liquipedia's event page, which also lists Virtus.pro as a former participant), and
  the groups are Falcons/NIP/9z/Aurora and FURIA/BETBOOM/Legacy/PARIVISION. Published Wednesday 14 October match starts of
  **10:30, 13:00, 15:30 and 18:30 CEST** independently corroborate the ticket listing's "games 10:30" start — and imply a
  plausible late finish, which is exactly why the return journey is the problem.
- **Food.** TripAdvisor's *Restaurants near AX ODYCY Hotel* list was readable on 11 October 2026 and is now recorded ranked
  **by review volume**, not by the platform's display order. Two captures taken minutes apart on different domains already
  disagreed on several counts, which is recorded as evidence that the figures are volatile rather than smoothed over.
- **Gaming.** A dated read of a Malta "Game & Entertainment Centers" directory lists MULTIMAXX, The Eden, Falcon
  Archery, Gravity/Jurassic and Laser Tag Malta (marked *temporarily closed*), and **no public PC-gaming café**. The
  esports association directory likewise lists training and competition venues only.
- **Recreation near the hotel.** Eco Sports Limited (Buġibba) added with **operator-published daily rates** — the first
  near-hotel activity in this project with a real, sourced price list.
- **Radio.** NET FM's own schedule page was re-read live and returned the same three sports-branded slots (Friday 18:30
  *Mhux Premier biss*, Saturday 16:00 *Hits & Score*, Sunday 15:00 *Sports Box*). The DAB+ "Sports Channel" block conflict
  is now wider, not narrower: an encyclopaedia list labels 185.36 MHz DAB+ as **"RAVE Radio"**.
- **Everyday / entry.** The EES conflict now names Malta in specific reporting, and Malta's own airport page still
  describes arrivals being *randomly selected* for a biometric lane. The ETIAS position is unchanged (not in operation) but
  the **risk is now explicit**: official and industry sources targeted Q4 2026, which contains these travel dates, while a
  September 2026 report says that target has been withdrawn.

## What remains unverified

Nothing below was presented as fact on the site, and each item is recorded in `docs/OPEN_QUESTIONS.md`:

1. **Admission.** No reservation was made, no inventory or checkout tested, and the Saturday/Sunday agenda was still not
   visible on the listing. The attendee gate, ID rules, per-day scanning and transferability are unknown.
2. **The return journey.** The 20:53/20:54 last Stadium departures, the Buġibba-only terminus and the Saturday diversion
   stand as recorded; no date-specific journey, no measured walk, and no live taxi quote were obtained.
3. **Trip-week fares.** The €2.50 (13–18 Oct) / €2.00 (19 Oct) split remains a third-party inference, not an operator
   confirmation.
4. **Named-match radio.** No named trip-week match is verified through the full chain of official schedule → Malta carriage
   → compatible receiver → local signal. UK BBC listings prove nothing about Malta.
5. **Popularity.** One platform, one date, one hotel radius, volatile counts. Yelp, Instagram, TikTok, Facebook, Reddit and
   X were unreadable, so there is no sentiment or trend claim for them.
6. **Empire Cinema arcade** is a search-extract lead: no hours, prices or age rules confirmed.

## Corrections made to existing content

- Removed a duplicated paragraph in `ees-malta-implementation-conflict` (the same cross-reference sentence appeared twice).
- Fixed a misspelled record ID (`tripadvisor-near-ax-odyy-…` → `…-odycy-…`) so the public anchor is correct.
- Added cross-references so the three TripAdvisor snapshot records read as three different pages rather than three
  competing claims, and stated that a repeated read by the same method is a stability check, not corroboration.

## Limitations of this session

- **Direct page fetches were mostly blocked** (Eventbrite returned "Something went wrong"; the bus operator's site
  errored). Several new rows are therefore **search-index extracts**, and every one is labelled as such in
  `docs/SOURCES.md`. An extract is weaker evidence than a full page read and has not been dressed up as one.
- **No new primary-source re-read was possible for transport**, so workstream A is unchanged and its open questions stand.
- **Automated gates check structure and behaviour**, not external truth. A passing suite is not a certificate that any
  listing, price, route or broadcast is still current.

## Suggested next-session work, in priority order

1. **Event access** — confirm reservation, gate, per-day validity, the 17–18 October agenda and the 22:00-vs-22:30 finish
   with the organiser; re-read the listing daily as the event approaches.
2. **Entry requirements** — recheck the official EU ETIAS page in the week before departure, and look for a Malta
   government or eu-LISA statement on the EES pause rather than relying on press reporting.
3. **Transit** — run the operator planner for each event date in both directions with the confirmed gate; check for TQ1
   special-event announcements daily during 14–18 October; obtain one live evening taxi quote to compare against the
   published tariff.
4. **Radio** — buy a DAB+ radio in Malta and actually scan 6A/6C/12A and FM at the hotel and the venue, logging service
   names, blocks and audio. This is the only item on the list that can convert a scan lead into a verified fact.
5. **Popularity and closures** — refresh TripAdvisor counts and the Qawra venue hours/menus close to travel; confirm the
   Empire Cinema arcade directly.
6. **Planner hand-off** — paste the confirmed itinerary into the quick-fill panel (it previews first and fills only blank
   fields), then export a CSV before switching devices.

## Gate results observed for this session's tree

- `python3 scripts/validate_site.py` — **PASS**: 7 JSON files / **196** exact-schema records / **317** unique record URLs /
  15 HTML pages / **234** link attributes / 9 navigation destinations / 25 expense rows.
- `python3 scripts/check_javascript.py` — **PASS**.
- `npx playwright test` — **21/21 passed** (320/360/768/1024/1440 px, axe, data/render parity, navigation and deep links,
  planner persistence, CSV/JSON backup, reset, quick-fill, storage-denial and data-fetch-failure cases).
- Manual Chromium check at 390 px and 1280 px on the three pages changed this session — **zero horizontal overflow, zero
  console errors**, and the new records render.


## Delivery snapshot — session `arena/09cdfbf0-maltasupplemental` (observed)

- Pull request **#51** was opened from `arena/09cdfbf0-maltasupplemental` against `main` and reported `MERGEABLE`/`CLEAN`.
- Its required check **“Schema, browser and accessibility checks”** ([run 38158610565](https://github.com/buffedlizard55-lab/MALTASUPPLEMENTAL/actions/runs/38158610565)) **passed**.
- PR #51 was **merged into `main` on 11 October 2026 at 17:13:35 UTC**, merge commit
  `6859c46efa5053578b41962bed21246ae76fd3aa`, from session head `a20368c`.
- The GitHub Pages latest-build record for that merge commit reports **status `built`**, created 17:13:36 and updated
  17:13:53 UTC.

**What this does not confirm:** this session's network policy allows only GitHub API and package-registry hosts, so
`https://buffedlizard55-lab.github.io/MALTASUPPLEMENTAL/` could not be fetched for a browser-level content check. The Pages
build record above is a GitHub build-state observation only; nobody here loaded the live page and compared it with the
merged tree.
