# Final report — Malta Trip Guide

**Planning window:** 13–19 October 2026
**Hotel supplied by traveler:** AX ODYCY Malta, Qawra Coast Road, Qawra SPB 1902
**Event location supplied by traveler:** BLAST Arena Studios, Attard
**Research snapshot:** see the individual access dates in [`SOURCES.md`](SOURCES.md)

## Executive summary

The site is a mobile-friendly, static Malta tourism and recreation guide with an overview, six topic pages, shared navigation, an evidence dashboard, and an editable expense planner. Six topic JSON files hold **117 common-schema records** with source type, check date, confidence, and caveats (count after the 11 October merge of both research passes); `data/record.schema.json` defines the exact shared record shape. Unknowns are stated rather than guessed.

The traveler supplied the hotel name/address, Deluxe Sea-View room type, trip dates, and event destination name (“BLAST Arena Studios, Attard”). Those are planning inputs. The official TWC page lists Malta only; the MFCC/Ta’ Qali address is venue-area context from a BLAST guide for a different event, not a confirmed TWC pin or entrance. The hotel reservation, rate, deposit, check-in/out times, flights, party size, arrival/departure times, and tournament attendance were not provided. Six hotel nights applies only if check-in is 13 October and check-out is 19 October; the guide does not assume that booking condition, event access, or an itinerary.

## Verified deliverables and research findings

- **Getting around (15 records):** compares airport, bus, taxi/ride-hailing, car-hire, ferry, and local transport options. MPT’s static Route 186 page lists Qawra stop 952 at 06:09–21:39 in one stop-table variant (06:10–21:38 appears in a parallel variant; the page’s stop tables differ, so stop IDs are treated as provisional). Its normal Rabat-to-Buġibba return runs via St Paul’s Bay/Buġibba rather than Qawra seafront; the last listed arrival is Buġibba Bay 1 at 21:26. Route 214 is an alternate to compare. A date-specific itinerary, venue walk, the 17 October diversion’s exact impact, fare validity, and hotel return still require checking in the operator planner; the page is not a door-to-door guarantee.
- **Food and cafés (27 records):** includes AX ODYCY/on-property options, 12 additional Qawra-area/Valletta venues, selected wider-area ideas, local-food context, and separately labelled map/review/community observations. Platform ratings are not blended. Reported closures, inaccessible-platform limits, and conflicting hours remain caveated; current menus, hours, and representative meal costs are not assumed.
- **Activities, landmarks, and events (30 records):** covers recreation and gaming leads, Malta attractions, and dated events relevant to the trip. New source-backed entries include MULTIMAXX St Julian’s/Kordin, Popeye Village, Classic Car Collection, the 13 Oct Heritage Malta lecture, 15 Oct Jazz Series, the 17 Oct Middle Sea Race listing at 11:00 and Waterfront Autumn Vibes, and 18 Oct CDM Sundays; unknown prices, times, inventory, and access remain marked. Event dates are kept distinct from spectator access, ticket inventory, prices and opening times; the Fort St Elmo Sailing Spectacle and Heritage Malta picnic details remain incomplete/conflicted.
- **Everyday travel (15 records):** covers entry pointers, EES/ETIAS, currency/cards, language, electricity, mobile connectivity, emergency/health, safety, weather, and practical U.S.-traveler considerations. Passport, device, carrier, itinerary, and medicine-dependent advice is conditional.
- **Sports radio (12 records):** the Broadcasting Authority lists NET FM at FM 101 MHz; its official grid shows recurring weekend sports programming, not a trip-week guarantee, and does not explicitly state its time zone. Digi B’s directory lists Radio Sportiva and BBC World Service on DAB+. WorldDAB lists BBC World Service on block 6A at 181.936 MHz; Radio Sportiva’s technical channel and reception at Qawra/MFCC remain unverified. BBC programme pages show Sportsworld on 17 and 18 October but do not name a particular match. No current AM/MW sports service or named-event radio carriage was confirmed. A third-party TalkSPORT/6C claim is explicitly unverified.
- **Expense planner (18 blank-by-default categories plus 7 day rows):** editable EUR budget/actual fields, day-by-day quick-entry rows for 13–19 October, an itinerary/confirmations notes box, notes, totals and difference, browser-local autosave, CSV export of categories, days and notes, source links, and reset are available. The starter has no assumed itinerary, personal amounts, booking costs, event costs, reimbursement, tax total, tip, or exchange rate; blank does not mean free. The MTA’s published environmental-contribution rate is €1.50/night/person aged 18+ (capped at €22.50/person); six chargeable nights would be €9 per eligible adult only conditionally, and the actual invoice remains unknown.

The source register, unresolved questions, workstream status, and cross-topic handoffs are in [`SOURCES.md`](SOURCES.md), [`OPEN_QUESTIONS.md`](OPEN_QUESTIONS.md), [`STATUS.md`](STATUS.md), and [`HANDOFF.md`](HANDOFF.md).

## Three cumulative review passes

1. **Implementation and source pass — passed after both main-branch reconciliations.** `python3 scripts/validate_site.py` reported (at that pass) 6 topic JSON files / 107 exact-schema records, 184 unique primary/cited record URLs present in `docs/SOURCES.md`, 15 root HTML pages / 86 link attributes, 8 navigation destinations, and all 18 planner rows wired. The schema enforces the exact requested `price range` key and five source types, including `directory`. JavaScript syntax, JSON parsing, and staged/unstaged `git diff --check` passed. External URL liveness and full graphical browser rendering remain limited.
2. **Independent requirements and evidence pass — passed with limitations recorded.** Rechecked the supplemental venue/event records against linked operator, organizer, and ticketing sources, including the Aquarium’s current 19:30 last entry and RMYC’s 11:00 race listing. Confirmed the Jazz ticket price/date without claiming seat availability; CDM time/price and Heritage Malta Sailing Spectacle details remain unknown. The TWC page gives Malta only; MFCC is explicitly treated as venue-area context, not a confirmed TWC destination. TWC access, picnic closure, gaming-café status, and platform-access limits remain documented rather than guessed.
3. **Integration pass — passed; visual comparison remains limited.** PR #13’s duplicate `/pages` tree and alternate builder were removed so the existing root-page/JSON renderer remains canonical. The repository validator confirms all 15 root HTML pages, 8 navigation destinations and data/page wiring after the added records. The earlier headless DOM interaction run and responsive-CSS review are from the prior integration; no new full browser screenshot or real-device accessibility audit was available for this additive data update.

**Focused follow-up verification (10 Oct):** the canonical root-page implementation is retained; the supplemental food/activity records and a sourced BBC DAB+ technical record bring the guide to 107 records. The strict shared schema uses the exact `price range` key and preserves `directory` for specialist technical listings; primary and note-level URLs are checked against the source log. The current Aquarium ticket FAQ directly confirms last entry at 19:30, and RMYC lists the 17 October race start at 11:00; public access remains unresolved. The new Jazz record lists €25 but does not infer inventory. The official TWC page lists the overall 12–19 October window but gives Malta only; MFCC is venue-area context from a different BLAST event, not a verified TWC address. WorldDAB’s BBC 6A/181.936 MHz listing and the MTA environmental-contribution rule remain caveated. The conditional €9 per eligible adult applies only to six billable nights and is not a personalized charge. MPT Route 186 return/diversion limitations remain unresolved. Final offline validation passed as recorded above; no external link crawler or full browser rendering was run.

To repeat the offline gate, run `python3 scripts/validate_site.py`. It checks the local schema, source-log URL coverage, internal paths, navigation destinations, and expense-row wiring; it is not an external URL crawler.

## Open questions and traveler actions

1. Confirm the hotel reservation, actual check-in/out, booking total, separately billed charges, and that the booked room matches the supplied Deluxe Sea-View room type.
2. Provide flight details, airports, baggage, arrival/departure times, and traveler count before finalizing transfers or total costs.
3. Confirm the TWC destination address/pin (the supplied name is a planning input; MFCC/Ta’ Qali is only an area lead), attendance, ticket/access terms, session times, and the event-specific public entrance. Then run the official Malta Public Transport planner for the outbound and late-return trip, including the 17 October notice.
4. Recheck 2026/27 fares/cards, live venue hours/menus, event availability, attraction access, and weather before travel.
5. Verify the applicable passport/Schengen and ETIAS status, mobile plan/device compatibility, and medication-specific requirements with the relevant authority/provider.
6. Recheck official radio schedules close to the broadcasts; WorldDAB lists BBC World Service on block 6A (181.936 MHz), but hotel/event reception has not been tested and Radio Sportiva’s technical channel remains unknown.

See [`OPEN_QUESTIONS.md`](OPEN_QUESTIONS.md) for the full list, evidence gaps, and proposed next checks.

## Limitations

- Information is a dated research snapshot and can change. The maintained source log gives claim-specific access dates and identifies third-party or non-official evidence.
- Some requested review/social services were blocked or only partially queryable. Google Maps and platform snapshots do not establish current operator hours or prices.
- The offline link checker does not guarantee external-site availability. No automatic crawler of every external source was run.
- A headless DOM simulation is not a substitute for visual review on real desktop/mobile browsers or assistive technologies.
- GitHub Pages is configured to publish the repository root from `main`. After PR #14 merged, the Pages API reported `built` for its `main` merge commit `2aeb536` (10 October 2026). This confirms the static-site build, not external-link liveness or actual browser/device rendering.
- This guide is a planning aid, not a booking, dispatch, immigration, tax, legal, medical, or event-access guarantee.

## Session update — 11 Oct 2026 (verification pass and merge)

**Verified this session (fetched from the cited pages on 11 Oct, UTC):**
- Thunderpick TWC 2026 finals page: 12–19 Oct overall window; Arrival 12, Media 13, Group Stage 14–16, Playoffs 17–18, Departure 19 Oct; location Malta (LAN event).
- MPT latest service updates: Route 186 diversion from 19:00 on Fri/Sat starting 17 Oct, to about 12:00 AM on 18 Oct; Bugibba-bound stops from Gholja 2 through Targa not served.
- MTA environmental contribution: €1.50 per night per person aged 18+ from 1 July 2026, €22.50 per-person-per-visit cap, separate invoice item (page and guidelines PDF).
- BLAST attendee guide (for a separate January 2026 BLAST Bounty event): venue address MFCC, Ta' Qali, ATD 4000 Ħ'Attard. It remains venue-area context, not confirmation for the TWC.
- Broadcasting Authority list: NET FM at 101 MHz; no AM sports station listed. NET FM weekly grid: Hits & Score Sat 16:00; Sports Box Sun 15:00.
- BBC World Service Sportsworld 17 Oct programme page (13:06 GMT = 15:06 Malta time).

**Corrections and additions made:**
- Added a BBC Radio 5 Live Premier League listing record (partially verified). It is a UK listing; Malta reception and the mapping of 'Next Saturday/Sunday' to 17–18 October are unverified.
- Logged OQ-24 (EPL/soccer radio and Kalshi link — not verified) and OQ-25 (ambiguous MTA '15-night' wording; the €9 six-night example is conditional).
- Qualified the expense planner's eco-contribution example and the executive summary.

**Still unverified / limitations:** Kalshi markets were not checked and are not evidence of broadcasts; no Malta radio station was confirmed to carry EPL or other soccer during 13–19 Oct; the Route 186 stop-level timetable was checked on 9–10 Oct, not re-audited line by line on 11 Oct; the event street address, entrance, spectator access and daily door times remain unconfirmed; blocked platforms (Yelp, Instagram, TikTok, Facebook, X, Reddit) were not re-verified.

**Next-session tasks:** resolve OQ-24/OQ-25 with the BBC/league and MTA/AX ODYCY sources; run the date-specific MPT planner for each event day; confirm event access and entrance once the organizer publishes it; recheck all dated notices within 24 hours of departure.

## Session report — 11 October 2026 (two days before the trip window)

This pass re-verified the volatile facts, expanded the radio workstream, and rebuilt the expense planner for a fast itinerary fill. The offline gate is green:
`python3 scripts/validate_site.py` reports **6 topic JSON files / 117 exact-schema records; 197 unique record URLs present in `docs/SOURCES.md`; 15 HTML pages / 91 link
attributes; 8 navigation destinations; 18 expense categories + 7 day rows wired**, and `node --check` passes on `js/site.js` and every inline script.

### What was verified this session (all re-read on 11 October 2026)

* **Venue address.** BLAST Arena Studios Malta is published at MFCC South Gate National Stadium, Millennium Stand, Attard ATD 4000 by three independent listings — the
  Malta Tourism Authority directory, GamingMalta, the ticketing agent Eventworks and BLAST's attendee guide for another event at the same venue. This upgrades the venue from "venue-area context" to a corroborated address. What is
  *not* verified: that the Thunderpick finals are staged there (the mapping rests on the organizer's own "BLAST Studios Malta" naming) and the event gate, doors or ticket terms.
* **Event-day bus.** Route 186's stop-level timetable shows roughly half-hourly passes through the Mosta corridor with final listed evening times of about
  21:53–21:55 in one table variant (the route page carries several parallel stop-table variants whose stop IDs and times differ). Malta Public Transport's service-update page lists a Route 186 diversion **weekly on Friday and Saturday 19:00–00:00 starting 17 October** (toward Buġibba, stops
  from Gholja 2 through Targa skipped) alongside parallel diversions for 13 other routes in the same corridor, plus a stop closure at Saqqajja (ID 4627) on routes including 186.
* **Late travel.** Night services are confirmed from Buġibba (N212, 23:50–01:30 every 20 minutes, Monday–Sunday) and Valletta (N13, weekdays 23:10–02:10 every 10 minutes) by the
  operator's April 2026 announcement. No night route serving Ta' Qali or Attard was verified — the site tells the traveler to plan a taxi/ride-hailing backup rather than assume one.
* **Fares.** MPT's page shows €2.00 winter / €2.50 summer day-route singles (2-hour validity, cash or contactless), Night Routes €3.00, Special Services €3.00, Tallinja Direct €3.00 / TD1 €3.50, 12 Single Day Journeys €19, Explore Flex from €21/€27, Explore Adult 7-Day €25, Explore Child
  €7, Airport Direct two trips €6, and lists sales points including the airport Welcomer's Hall, Valletta, Buġibba and Sliema Ferries. Its fare text is tied to the period
  "19 October 2025 to 13 June 2026", so the applicable fare for these dates is flagged as unestablished rather than quoted as settled.
* **Radio (5 → 12 records after merging both 11 October passes).** WorldDAB's Malta page confirms three DAB+ multiplexes — Digi B Network 6A (181.936 MHz), Digi B 3 6C (185.360 MHz) and
  Digi B 2 12A (223.936 MHz). BBC World Service and Rai Radiouno appear on 6A; **12A carries a regular service literally named "Sports Channel"**, whose broadcaster the directory
  does not identify. Rai's own programme page confirms "Tutto il calcio minuto per minuto" airs Saturdays and Sundays with Serie A and B coverage in Italian — the most concrete
  live-commentary lead on the Maltese DAB+ line-up. NET FM's published grid (FM 101 MHz) lists Saturday "Hits & Score" at 16:00, Sunday "Sports Box" at 15:00 and Friday
  "Mhux Premier biss" at 18:30, but describes no programme content, so commentary is not claimed. Radio Sportiva is listed in Digi B's directory but no block or frequency was found and the Broadcasting Authority's list does not name it, so it is recorded as a service to scan for rather than confirmed carriage; a third-party "Talk Sport on 6C" claim stays unconfirmed; Calypso's third-party sport listing contradicts the station's own current schedule page.
* **Trip-window sport context.** Recorded as fixture context only (never as carriage): the Premier League matchweek of 17–18 October with official BST kick-offs, UEFA Europa
  League matchday 2 on Thursday 15 October, and the NFL slate of Sunday 18 October (London game 15:30 Malta time; late games after midnight Maltese time). Every one of these
  records states that a fixture is not evidence that a station carries it.
* **Base hotel.** The AX ODYCY's own site is now a record (address, 24-hour front desk, free Wi-Fi, pools, water park, all-inclusive dining, contacts) so the base is documented
  alongside the destination.

### What changed in the product

* `data/transport.json` 13 → **15 records** (a duplicate venue-address record was folded into the updated venue record); `data/radio.json` 5 → **12**; `data/activities.json` 29 → **30**; all datasets re-dated 2026-10-11 with per-record `date_checked`.
* `data/expenses.json` gained a `day_rows` array (7 days, 13–19 October) and `costs.html` gained **day-by-day budget/actual/note rows, an itinerary/confirmations notes box,
  day totals, a grand total and CSV export of all three sections** — so a supplied itinerary can be costed in minutes. Nothing is prefilled.
* `scripts/validate_site.py` now enforces the seven day rows and the planner wiring; `docs/DATA_SCHEMA.md` documents the dataset-level extension.
* `index.html`, `getting-around.html` and `radio.html` were rewritten where the old text understated what is now verified (venue address, evening bus limits, DAB+ multiplexes).

### Verification performed (not just written)

* **Planner simulation:** jsdom loaded `costs.html`, stubbed the data fetch, typed amounts, and checked rendering, totals, storage, CSV and reset — **18/18 checks passed, 0 runtime errors**.
* **Site simulation:** jsdom ran `js/site.js` against all five topic pages — navigation, `aria-current`, card counts vs record counts, source links, confidence pills, search filtering,
  and a check that no `undefined`/`NaN` leaks into rendered text — **49/49 checks passed**; the index menu toggle and footer snapshot date were also exercised.
* **Schema/source gate:** every URL cited anywhere in a record is present in `docs/SOURCES.md` (197 unique URLs), and every record carries a date, confidence and notes.
* **Bug found and fixed by review:** a stylesheet cleanup had corrupted the `.topic-tools label` and `.topic-tools input` selectors; both were restored before commit, which is exactly
  what Pass 2 is for.

### Still unverified / limitations (carry into the next session)

1. **Event access.** Ticket terms, doors, daily match times and the TWC-specific entry gate are still unpublished by the organizer; the venue mapping rests on organizer naming.
2. **Late-night return from Ta' Qali.** No night route serving Ta' Qali/Attard was verified; the 17 October diversion materially affects the Mosta/Naxxar stops on the return leg.
3. **Fares.** The applicable fare for 13–19 October 2026 is not established by the operator's page text; recheck before buying.
4. **Radio reception and carriage.** No DAB+/FM receiver test was possible at the hotel or venue; the broadcaster behind "Sports Channel" (12A) is unknown; no fixture-specific
   commentary carriage was confirmed anywhere. BBC Sportsworld's Malta clock times were deliberately not restated because the BBC page renders times in the viewer's zone.
5. **Platform coverage.** Yelp, Instagram, TikTok, Facebook and X requests were blocked (HTTP 403) and Reddit refreshes were blocked in earlier checks; Google Maps views were limited.
   The food/activities shortlists are therefore sourced from operator pages plus dated TripAdvisor/Maps snapshots, not a comprehensive social-media ranking.
6. **Physical checks.** Walking times from the hotel to its nearest bus stops, the Ta' Qali walk from the stop to the venue gate, and real-device mobile rendering were not measured;
   the responsive CSS and layout were reviewed in code and via DOM simulation only.
7. **External link liveness.** The gate proves a URL is logged, not that the remote site answers today; volatile pages should be re-opened before travel.

### Suggested next-session tasks (priority order)

1. When the itinerary and ticket email arrive: paste them into the planner's notes box, fill the seven day rows, and export the CSV; then convert the confirmed event session times into
   a dated Malta Public Transport planner query for outbound and return on each event day.
2. Ask the organizer (or the ticket-holder channel) for the venue gate, door times and any event shuttle, then update `data/transport.json` and remove the corresponding open question.
3. Re-check fares and travel-card terms on the operator's live pages in the last 48 hours before departure, and read the Route 186/214 service-update page for new notices.
4. Re-scan DAB+ on arrival: identify the "Sports Channel" broadcaster on 12A, confirm BBC World Service and Rai Radiouno reception indoors, and note which of the two sports programmes on
   NET FM (FM 101) is actually commentary. Record findings in `docs/SOURCES.md` and `data/radio.json` (with a new `date_checked`).
5. Confirm the meal plan and whether the environmental contribution is charged on the invoice, then update the hotel rows in the planner.
6. Capture one real phone screenshot per page (desktop and mobile) to close the responsive-rendering gap the automated gate cannot cover.
