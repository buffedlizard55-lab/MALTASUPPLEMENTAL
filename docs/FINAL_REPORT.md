# Malta trip guide — final report

## Current session — `arena/3031b29b-maltasupplemental` (11 October 2026 UTC)

### What this pass did

The repository was reviewed first and left intact: static Pages site, canonical 13-field schema, seven datasets with matching pages, source/open-question/status/handoff/plan logs, blank-by-default expense planner, CI workflow and the Playwright/axe suite. The session then attacked the remaining weak spot in the original request — a receiver-usable answer about live sports radio — and re-corroborated the trip’s decision-changing facts two days before departure.

### New verified findings, with their limits

- **English EPL commentary on radio: one plausible route, one ruled out, one unproven.** A crowd-edited talkSPORT article lists “DAB+: 6C (Malta)” in its frequency infobox and states that outside the UK and Ireland talkSPORT carries live commentary of every Premier League match in several languages including English. That strengthens — but does not prove — the Maltese 6C “Sports Channel” lead, because the same service is listed on 12A by WorldDAB and the operator’s visible directory shows no sports tile. In parallel, **BFBS Radio 2 was ruled out**: its own schedule page does carry live Premier League commentary, but BFBS Malta closed on 31 March 1979 and BFBS frequency tables list UK/Gurkha/overseas-base outlets only. **PBS Radju Malta (93.7 FM) and Radju Malta 2 (105.9 FM)** have a radio-carriage precedent — a third-party rights directory describes PBS’s FIFA/EBU 2026 World Cup coverage as including radio on both stations — but that tournament is outside the trip window and no 13–19 October lineup is published.
- **The trip-window sport calendar, checked against departure day.** Inside 13–19 October: the Premier League weekend (17–19 October), Serie A matchday 7, Champions League matchday 2 (13–14 October), an NFL London game on 18 October (listed as Houston Texans v Jacksonville Jaguars; 9:30 a.m. ET = 15:30 Malta) and the CS2 event. Outside the stay: UEFA Champions League matchday 3 (20–21 October), the NBA opener (20 October), the MLB World Series (from 23 October), the F1 United States Grand Prix (23–25 October) and El Clásico (25 October). Fixture clocks were independently corroborated on the BBC Sport and Sky Sports fixture pages against the league’s own amendment article; no radio carriage was found for the NFL game.
- **Transport re-reads.** The complete service-updates page was read again and the 17–18 October Friday/Saturday 19:00–00:00 detour cluster enumerated in full (Routes 186, 202, 260, 47, 103, 45, 405, 238, 203, 280, 31, 41, 42, 48, N48), alongside the older Route 186 20:00–00:00 notice ending 21 April and the Saqqajja stop-4627 closure; still no Thunderpick, BLAST or TQ service was published. TQ1’s published northern corridor (Ta’ Qali → Rabat, Mosta, Naxxar, St Paul’s Bay, Qawra → Buġibba) and TQ2’s central corridor were newly recorded, together with a March 2026 precedent in which MPT ran extra and post-event Ta’ Qali services toward Buġibba and St Paul’s Bay. That precedent is evidence the pattern exists — not a commitment for this event.
- **Weather.** The national forecast panel for 13–17 October was corroborated by a second Maltese outlet (Times of Malta) with identical values; three third-party forecasts were read for 18–19 October and agree only on a rain risk, which is enough to pack a rain layer and nothing more.
- **Data-integrity bug found and fixed (Pass 2):** the canonical `espresso-odycy` record — the hotel's 24/7 coffee bar — was carrying the rooftop restaurant's hours (Wednesday–Saturday 18:30–22:30, ages 16+, €70/€80 tasting menu), its Level 11 address, its menu URL and its TripAdvisor figures. Those facts belong to `minoa-ax-odycy`. The Espresso record was rebuilt from the operator's own outlet page fetched on 11 October 2026 (Level 0, open 24/7, barista coffee/juices/snacks, menu PDF linked but not transcribed), the correction is recorded in its notes for traceability, and a regression test now asserts the two records keep distinct hours, addresses, prices and sources. A cross-record duplicate scan of all 202 records found no other contamination.
- **Event listing re-read:** unchanged apart from the price wording — “Sales end soon”, ages 18+, the same visible agenda, six team names plus “View all”, and map coordinates for the venue. On this read the word “Free” appeared only on a “You might also like” card rather than inside the ticket block, so free entry remains corroborated by HLTV but unconfirmed at checkout, consistent with the parallel session's correction now carried in `data/event.json#twc-spectator-tickets`.

### Passes and observed local gates

1. **Pass 1:** fresh reads of the ticketing listing, operator fares/service-updates/Route 186 pages and the radio/fixture/weather sources; new records and notes added with per-claim source rows.
2. **Pass 2:** adversarial review of the new claims — crowd-edited sources labelled as such, third-party calendars kept as leads, “precedent” kept distinct from “announcement”, and the negative BFBS finding stated as a sourced negative rather than a measured scan.
3. **Pass 3:** the original request re-walked line by line against the integrated site, then the full local suite (schema/source-log/local links, JavaScript syntax, Playwright + axe at 320–1440 px) run on the delivered tree.

### Integration of two parallel sessions merged to `main` during this pass

`main` advanced twice while this branch was open (PRs #58 and #59). Both merges were resolved by hand, keeping each session's record and 202th-session blocks rather than overwriting them, and three corrections from the other sessions were folded into this branch's own text:

- **Ticket price wording.** The twelfth pass found that the word “Free” appeared only on a “You might also like” card, not in the Eventbrite ticket block. The executive summary now says *reserve the 18+ spot and confirm the price at checkout*, and the status/handoff/report/source-log lines drop an unqualified “free”.
- **Last-return reproducibility (OQ-S1).** A later session could not reproduce the Stadium 2194 “20:53/20:54” rows, and this session's own chunk read reproduced only the opposite direction. A reproducibility caveat was added to the three affected transport records and to the transport page and overview checklist: the direction problem (the return terminates at Buġibba Bay 1, not Qawra) and the need for a date-specific planner check are the solid facts; the exact last minute is published-grid evidence requiring confirmation.
- **DAB+ directory wording (OQ-S3).** The claim that the operator directory was “read in full” is withdrawn — it ends in a “Load more” control — so the radio record now says the *visible* listing showed no “Sports Channel” entry and that the absence is not exhaustive.

### Delivery — observed (not predicted)

PR #60 was merged into `main` at **2026-10-11 18:43:26 UTC**; GitHub reports merge commit `b8af702b664893ce00c6d4951c178fd7a1b92190`. Its required check, “Schema, browser and accessibility checks”, passed on the pushed head (`9c8e05a`) in 1 m 13 s, and the PR was `MERGEABLE` before merge. The GitHub Pages latest-build endpoint reports status `built` for the same merge commit. The published `radio.html` was then fetched and contains the new trip-window live-sport table, the BFBS negative bullet and the PBS lead bullet, and the published `index.html` carries the corrected executive-summary line — a browser-level content check of the deployment, not a crawl of every external link and not an RF or service test.

### Still to do next session

1. Confirm the reservation, gate, ID rules, per-day validity, weekend agenda and the 18:00 vs 18:30 opener outlier with the organiser.
2. Run the operator’s date-specific journey planner for each event date and obtain one live taxi/ride-hailing quote for a late return; keep watching for a TQ service during 14–18 October.
3. Scan DAB+ blocks 6A/6C/12A and the listed FM frequencies in Malta, and log service label, block, language and any named match actually heard.
4. Refresh restaurant/gaming hours and menus directly, and re-check entry rules (ETIAS/EES), weather and transit notices on arrival.
5. When the itinerary arrives, enter confirmed amounts only into the planner and save a private JSON backup.


## Current session — `arena/67d511d1-maltasupplemental` (11 October 2026 UTC)

### Delivery summary

This session reviewed the integrated repository rather than replacing it. The site already contained GitHub Pages-ready static HTML, shared navigation/renderer, responsive tokens, seven topic datasets using the exact 13-field record schema, a master source log, open questions, workstream status, a blank-by-default expense planner and a Playwright/axe suite. `docs/PLAN.md` now records the current session's owners/dependencies and the serial execution limit (Arena provides a single fixed branch, so no separate workstream agents or branches are claimed).

The new work focused on the radio requirement and integration quality. Live official-source checks refreshed the Thunderpick/Eventbrite listing, MPT Route 186/fares/service notices, Transport Malta taxi tariff, AX ODYCY property listing, BBC episode records, NET FM schedule, Rai Radio 1 programme, the Malta DAB+ directory and Radio Sportiva's current weekly grid. The Sports Radio subpage now has a 13–19 October trip-week table and a receiver scan checklist; it separates dated BBC programme starts from recurring NET/Radio Sportiva/Rai schedules and from named-match carriage. The table has a semantic desktop layout and labelled mobile cards. During this work, `main` also merged PR #56, adding a derived seven-day transport plan and timezone-qualified 14 October opening matchups; these are preserved and their remaining gaps are identified below. The rebased tree also preserves a dated TripAdvisor review-volume snapshot for nearby food alongside its count drift, relevance/sponsored-order caveats; this is not a universal rating/popularity ranking. Review-platform access limits remain explicit, and no sentiment is inferred from blocked sources.

### Highest-value verified findings and boundaries

- **Thunderpick / admission:** the official ticketing listing advertises the in-person 18+ event at BLAST Arena Studios Malta, MFCC South Gate National Stadium, Attard, 14–18 October; the displayed ticket card says “Free / Reserve a spot.” Visible agenda rows cover 14–16 October only, and Wednesday/Thursday row end times (22:30) conflict with the 22:00 listing header. This does not establish the user's reservation, current inventory, day validity, attendee gate, or weekend agenda.
- **Event-day transport:** the rebase adds `data/transport.json#event-day-transport-by-date`, rendered at `getting-around.html#event-day-by-date`, with a date-by-date action for all seven days. For Wed/Thu 14–15 October it derives an 08:39 Route 186 departure from Qawra 952, reaching Stadium 6227 around 09:04–09:09 for the listed 09:30 check-in; Friday’s 21:00 finish is still after the last published 20:53/20:54 Stadium 2194 return. The return terminates at Buġibba Bay 1, not Il-Qawra; the plan treats a pre-booked ride as the reliable late-return option and describes the Saturday 17 diversion cluster. These clock comparisons and the ~20:40 boarding recommendation are **derived from static route grids and advertised agenda**, not saved date-specific MPT journeys. The Sat/Sun agenda, attendee gate, both walking legs, onward Buġibba→Qawra service, live quote and any event service remain unverified. Monday departure options (TD1 / Route 214) are listed, not journey-planner results.
- **CS2 opening-match clocks:** `data/event.json#twc-opening-matchups-14-oct` and `event.html#opening-matchups` pin four third-party bracket starts to Malta CEST 10:30, 13:00, 15:30 and 18:00; a separate source-log row still says 18:30 for the last opener. The organizer has not published a per-match running order, so this 30-minute discrepancy remains open and the bracket start is not an event door time.
- **Fares / taxi comparison:** MPT's official page lists €2.50 summer / €2.00 winter day singles and other cards, but the printed seasonal window ends 13 June 2026; the likely 13–18 / 19 October split is secondary-source inference, not operator confirmation. Transport Malta's tariff page gives maximum meter rates but its footer says last updated 06/04/2022; maxima are not a quote. Bus is the only mode with an applicable operator-published price table; ride-hailing, rental total and current taxi price remain live-quote checks.
- **Terrestrial sports radio:** BBC episode metadata gives Sportsworld starts at 15:06 Malta time on 17 Oct and 16:06 on 18 Oct (each 13,980 seconds / 3 h 53 min); the descriptions are general live sport, not named-match assignments. The Saturday programme starts after the 13:30 EPL kickoff and its scheduled duration overlaps later 16:00/18:30 kickoffs; Sunday starts after 15:00 kickoffs and overlaps the 17:30 kickoff by clock only. Radio Sportiva's official grid currently lists weekday/weekend sports programmes at 15:05–17:00, but its specifically dated “Sportiva Live” callouts visible on 11 Oct cover 5–11 Oct, not the user's dates. NET FM and Rai have recurring grids but no verified trip-week named fixture list. Radio in Malta and a historical RadioBlog report label “Sports Channel (Talk Sport)” on DAB+ 6C (185.360 MHz); WorldDAB lists a generic channel on 12A, a crowd-edited list associates RAVE Radio with 185.36 MHz, and the operator's visible directory showed no sports tile. The sources do not establish which current block, identity or relay is correct; **scan 6C and 12A without ranking either**. No compatible receiver scan, relay-feed check, indoor signal, named match on a Malta frequency or Kalshi-to-broadcast link is verified.
- **Food / social research:** the repository contains source-linked listings and dated review snapshots. Google Maps / TripAdvisor coverage was limited; Yelp, Instagram, TikTok, Facebook, Reddit and X endpoints were blocked or limited in recorded checks. This is not comprehensive review sampling; “most popular” is not represented as a universal ranking.
- **Trip-specific unknowns:** the supplied hotel/room/date information and event intention are user inputs, not booking confirmation. Traveler's exact itinerary, party size/ages, flights, hotel invoice/meal plan, insurance, SIM/device, tickets and personal expenses remain unknown. The planner therefore starts blank and does not assume bookings or spending.

### Passes and observed local gates

1. **Pass 1 — implementation and evidence:** repository/schema reviewed first; preserved the existing topic structure and source-log format; added the trip-week radio view, receiver steps, official Radio Sportiva schedule evidence, and source/open-question entries.
2. **Pass 2 — adversarial review:** corrected the BBC interval language so the pages use verified start times and published duration rather than an unverified end minute; corrected the claim that Sportsworld starts before the Saturday 13:30 or Sunday 15:00 kickoffs; separated recurring Sportiva/NET/Rai grids from dated named matches; retained the 6C/12A conflict as an unresolved scan lead; checked that unknown route, ticket and reception claims remain caveated; added responsive table labels and a browser assertion.
3. **Pass 3 — original-request audit:** after integrating PR #56, checked the user’s transport, review-platform, activity, U.S.-traveler, radio/Kalshi, expense-planner, navigation and source-verification requirements against the merged data/pages/docs; then reran the complete suite on `origin/main` `6da8aba`.

**Local checks after rebase onto `origin/main` `6da8aba` (observed):** `python3 scripts/validate_site.py` passed with 7 datasets / 199 exact-schema records / 319 unique record URLs / 15 HTML pages / 340 link attributes / 9 shared navigation destinations / 25 expense rows. `python3 scripts/check_javascript.py`, `node --check js/site.js`, and `git diff --check` passed. `npm test` passed **23/23**, including axe at 320/360/768/1024/1440 px, the seven-day transport and opening-matchup projections, and radio-table checks at 320/360/720/1440 px. These verify local structure/rendering, not event-ticket availability, external URL liveness, date-specific operations or RF reception.

### Still needed / next-session priorities

1. Confirm the traveler’s ticket reservation, attendee gate, acceptable ID, per-day scanning/validity, accessibility, weekend agenda and venue-local clocks with Hotspawn/Thunderpick. Resolve the 18:00 vs 18:30 outlier for the fourth 14 October opener; neither match starts nor bracket times are door times.
2. Run MPT's journey planner for each event date using the actual hotel and confirmed gate to verify the derived 08:39 outbound recommendation and return alternatives; confirm stop sides, both walks, the Buġibba→Qawra onward connection, 17 October diversion impact and any TQ service. Obtain a live all-in taxi/ride-hailing quote for each late return; do not treat static timetable grids or derived comparisons as a saved journey.
3. In Malta, scan DAB+ 6A/6C/12A and the listed FM frequencies at AX ODYCY and the event location. Ask BBC/Digi B, Radio Sportiva, NET, Rai, Vibe and the “Sports Channel” operator about the named fixtures; log service, time, frequency/block, language and audio actually received.
4. Refresh restaurant menus/hours/closures, gaming access, museum/event availability, weather and transit notices close to departure. The blocked social/review-platform gap and small Maps/TripAdvisor sample remain research limits.
5. When the itinerary arrives, enter actual booking/receipt values in the planner; check the quick-fill preview, avoid double-counting aggregate and daily rows, and save a private JSON backup (CSV is for spreadsheets/manual entry).

**Delivery state at report draft:** PR #55 is open. This fixed branch is rebased onto current `main` at `6da8aba` and passes the local 23-test suite, but the updated head still needs to be pushed and its required GitHub checks/mergeability observed. No merge or Pages build for PR #55 is yet verified.

---

## Prior mainline report and audit history

## Previous mainline session — `arena/dd9dd00c-maltasupplemental` (11 October 2026)

Passes 1–3 were run on the tree that started at `250e6bd` (PR #48 on `main`). Arena does not allow a second branch, so workstreams A–F were sequential file owners on this branch and G integrated last.

### Verified in this pass

- Eventbrite still advertises the free 18+ in-person listing at BLAST Arena Studios, MFCC South Gate, ATD 4000 Attard, 14–18 October, headline 9:30 AM–10 PM. Friday’s row header reads 2:00 PM–9:00 PM. Saturday and Sunday stay behind “Show all agenda”. The visible lineup names Legacy, Falcons, FURIA, Betboom, 9z and Aurora, then View all. A merge with `main` kept the HLTV, Hotspawn and Liquipedia account that NIP replaced Virtus.pro. Liquipedia’s opening-match block, re-read during the merge, shows Falcons–NIP, 9z–Aurora, Legacy–PARIVISION and FURIA–BetBoom. The 16 September organizer release still named Virtus.pro.
- Thunderpick’s finals page still gives 12–19 October, media day 13 October, groups 14–16, playoffs 17–18, and a $1,000,000 table. It says Malta, not a street address.
- MPT’s fare table still shows €2.50 summer / €2.00 winter day singles, €3.00 night/special/Tallinja Direct, €3.50 TD1, and a €50 fine. The printed winter window is still 19 October 2025 – 13 June 2026.
- Route 186 search excerpts of the operator page still end two Stadium 2194 return grids at 20:53 and 20:54. The service-updates page still shows the 17–18 October 19:00–00:00 diversion, separate from the April notice.
- A separate notice closes Saqqajja stop 4627 on Route 186 until “January 1” with no year. An earlier same-day stop trace places it before Stadium 2194 on the return. This pass did not re-walk that chain. The notice does not say the Stadium or Qawra stops are closed.
- Qawra TripAdvisor Featured order, first three numbered entries: Trattoria Riccardo (4.8 / 2,675), Minoa (5.0 / 765, closed today in that snapshot), Cheeky Monkey Qawra (4.5 / 3,374). Sponsored cards sat above them. Not a review-count ranking.
- BBC Sportsworld JSON still starts 17 October at 14:06 +01:00 and 18 October at 15:06 +01:00, each 3 hours 53 minutes. No named match.
- Government of Malta still lists 230 V, 50 Hz, UK-style three-pin plugs.
- Malta Met Office’s seven-day panel still ends 17 October and matches the retained 13–17 October figures.

Local gates after the merge with `main`: schema/source/link validator passed (7 files, 197 records, 319 record URLs, 15 pages, 311 link attributes, 9 nav destinations, 25 expense rows). Playwright/axe passed 21/21, including 320–1440 px layouts. Tests do not prove external pages stay live or that a bus/radio signal exists.

### Still unverified

Reservation, inventory, gate, weekend agenda, an organizer-page confirmation of the NIP replacement, a saved hotel-to-gate journey, the Saqqajja closure year, the October single fare as an operator quote, physical FM/DAB+ reception, 18–19 October on Malta’s own seven-day panel, and any personal booking or price. Yelp, Instagram, TikTok, Facebook and X were not re-attempted. `main` moved during this session; PRs #51 and #52 were merged in and their food, gaming and entry-requirement records were kept.

### Next session

1. Open the Eventbrite flow and ask Hotspawn for the hidden agenda, FAQ answers and the full lineup.
2. Save both directions in the MPT journey planner for each event day, including the Saqqajja closure and the 17 October diversion.
3. Ask MPT whether the day-route single on 13–19 October is the summer or winter price.
4. If a late return is required, get a live hotel/taxi/ride quote rather than using the 2022 tariff page.
5. Scan DAB+ blocks 6A, 6C and 12A at the hotel and venue on a DAB+ receiver.
6. Refresh weather for 18–19 October and any restaurant hours the night before.
7. Paste only confirmed receipts into the blank planner.

## Previous audit — 11 October 2026 (UTC)
**Session branch:** `arena/502e2dae-maltasupplemental`
**Baseline:** `origin/main` at `b307c51` (merge of PR #33), reconciled with `origin/main` at `852343f` (parallel-session PRs #42–47) via a conflict-resolved merge that keeps both sessions' net-new corrections.

## Latest pass — session `arena/d840a59d-maltasupplemental` (11 October 2026)

**Baseline:** `main` at `250e6bd0ea5722cbad5a5ec21fc3117f2eee8fe0` (PR #48 merge), clean tree at session start. All work ran serially on the fixed branch under the existing A–G ownership boundaries.

### What this pass added

1. **The core transport requirement is now answered per date.** `data/transport.json` gains `event-day-transport-by-date`, rendered at `getting-around.html#event-day-by-date`: for each of the seven trip days it states the outbound plan (Route 186 toward Rabat from Qawra 952, 30-minute pattern, Stadium 6227 about 25–33 minutes later), the return constraint (last listed Stadium 2194 departures 20:53/20:54, terminus Buġibba Bay 1 with no Il-Qawra stop), and one action. The 17 October row carries the diversion window and the fourteen-route detour cluster; the 19 October row carries the airport options. Every derived figure — the ~20:40 boarding recommendation and the “no bus return after the finish” reading — is labelled derived rather than verified, and the unknowns (weekend agenda, gate, walks, onward connection, live quotes) are listed inside the record.
2. **Match clocks are now timezone-reconciled instead of assumed.** `data/event.json` gains `twc-opening-matchups-14-oct`, rendered at `event.html#opening-matchups`. A direct read of the bracket report displayed the four 14 October openers at 04:30 / 07:00 / 09:30 / 12:00; a search-index rendering of the same table read the same day displayed 10:30 / 13:00 / 15:30 / 18:00. The two differ by exactly the EDT-to-CEST offset, which pins the Malta local starts at 10:30, 13:00, 15:30 and 18:00 — corroborated by the ticketing listing’s own “games 10:30” row. This corrected this session’s own first draft, which had quoted the later clocks with no zone evidence.
3. **Radio claims were narrowed, not expanded.** The Malta DAB+ operator directory was read in full (38 rendered entries): there is no service named “Sports Channel”, and the only sports-branded entry is Radio Sportiva; a “Load more” control means the absence is still not exhaustive. Vibe FM’s own Malta Premier page still carries the “2025/2026 Season” label with a May 2026 post as its newest entry, so no trip-week Vibe football broadcast is published. TQ1’s page still reads “Timetable not available!”, and the complete service-updates page published no TQ or Thunderpick/BLAST event service.
4. **A new official disruption is recorded:** stop Saqqajja (ID 4627) is closed for construction on Routes 109, 109A, 181, 182, 186, 201, 202, 50, 51, 52, 53, 56 and N52 until about 1 January. It is not the traveler’s boarding or alighting stop, but it affects two venue-corridor routes.

### Verification performed in this pass

| Check | Result |
|---|---|
| `python3 scripts/validate_site.py` | PASS — 7 JSON files / **199** exact-schema records after the latest-`main` merge (transport 30, food 48, activities 47, everyday 19, radio 21, expenses 25, event 9); 319 unique record URLs present in `docs/SOURCES.md`; 15 HTML pages / 325 link attributes; 9 navigation destinations; 25 expense rows |
| `python3 scripts/check_javascript.py` | PASS — shared and inline JavaScript syntax |
| `npx playwright test` | PASS — **22/22**, including the 320/360/768/1024/1440 px layout and axe sweeps and the new test asserting the seven per-date plan rows, their `datetime` attributes, the canonical record rendering and the event matchups deep link |
| Fresh source reads (all 11 October 2026) | Eventbrite listing (full), MPT fares, MPT service updates (all three chunks), Route 186 grids and notices, TQ1, DAB+ operator directory (both chunks), Vibe FM football page, HLTV bracket report |

### Limits that remain

Nothing in this pass is a booking, an admission, a live quote, a physical journey, an RF measurement or a personal purchase. The Saturday/Sunday agenda, the traveler’s reservation, the attendee gate, both walks, the dated Buġibba → Qawra connection, the operator-dated October single fare, any named-match radio carriage and the expense inputs are all still open and are listed in `docs/OPEN_QUESTIONS.md`. Review-platform coverage (Yelp, Instagram, TikTok, Facebook, X, Reddit) remains partial or blocked; no popularity ranking is asserted.

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
