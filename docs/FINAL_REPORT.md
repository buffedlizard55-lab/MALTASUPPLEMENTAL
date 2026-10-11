# Final report — Malta Trip Guide

**Planning window:** 13–19 October 2026
**Hotel supplied by traveler:** AX ODYCY Malta, Qawra Coast Road, Qawra SPB 1902
**Event location supplied by traveler:** BLAST Arena Studios, Attard
**Research snapshot:** see the individual access dates in [`SOURCES.md`](SOURCES.md)

## Executive summary

The site is a mobile-friendly, static Malta tourism and recreation guide with an overview, six topic pages, shared navigation, an evidence dashboard, and an editable expense planner. Six topic JSON files hold **107 common-schema records** with source type, check date, confidence, and caveats; `data/record.schema.json` defines the exact shared record shape. Unknowns are stated rather than guessed.

The traveler supplied the hotel name/address, Deluxe Sea-View room type, trip dates, and event destination name (“BLAST Arena Studios, Attard”). Those are planning inputs. The official TWC page lists Malta only; the MFCC/Ta’ Qali address is venue-area context from a BLAST guide for a different event, not a confirmed TWC pin or entrance. The hotel reservation, rate, deposit, check-in/out times, flights, party size, arrival/departure times, and tournament attendance were not provided. Six hotel nights applies only if check-in is 13 October and check-out is 19 October; the guide does not assume that booking condition, event access, or an itinerary.

## Verified deliverables and research findings

- **Getting around (13 records):** compares airport, bus, taxi/ride-hailing, car-hire, ferry, and local transport options. MPT’s static Route 186 timetable (re-read 11 Oct) lists Qawra stop 952 at 06:09–21:39 toward Ta’ Qali Stadium stop 6227 (06:39–22:08). The Rabat-to-Buġibba return (re-read 11 Oct) serves Stadium stop 2194 (05:52–20:53) via St Paul’s Bay/Buġibba rather than the Qawra seafront stops (950–955); the last listed arrival is Buġibba Bay 1 (stop 2527) at 21:27. Route 214 is an alternate to compare. The full fare table is recorded, but the October 2026 single-fare window is not established by the operator page. A date-specific itinerary, venue walk, the 17 October diversion’s exact impact, the Saqqajja (4627) stop closure on the Rabat side, fare validity, and hotel return still require checking in the operator planner; the page is not a door-to-door guarantee.
- **Food and cafés (27 records):** includes AX ODYCY/on-property options, 12 additional Qawra-area/Valletta venues, selected wider-area ideas, local-food context, and separately labelled map/review/community observations. Platform ratings are not blended. Reported closures, inaccessible-platform limits, and conflicting hours remain caveated; current menus, hours, and representative meal costs are not assumed.
- **Activities, landmarks, and events (29 records):** covers recreation and gaming leads, Malta attractions, and dated events relevant to the trip. New source-backed entries include MULTIMAXX St Julian’s/Kordin, Popeye Village, Classic Car Collection, the 13 Oct Heritage Malta lecture, 15 Oct Jazz Series, the 17 Oct Middle Sea Race listing at 11:00 and Waterfront Autumn Vibes, and 18 Oct CDM Sundays; unknown prices, times, inventory, and access remain marked. Event dates are kept distinct from spectator access, ticket inventory, prices and opening times; the Fort St Elmo Sailing Spectacle and Heritage Malta picnic details remain incomplete/conflicted.
- **Everyday travel (15 records):** covers entry pointers, EES/ETIAS, currency/cards, language, electricity, mobile connectivity, emergency/health, safety, weather, and practical U.S.-traveler considerations. Passport, device, carrier, itinerary, and medicine-dependent advice is conditional.
- **Sports radio (6 records):** the Broadcasting Authority lists NET FM at FM 101 MHz; its official grid shows recurring weekend sports programming, not a trip-week guarantee, and does not explicitly state its time zone. Digi B’s directory lists Radio Sportiva and BBC World Service on DAB+. WorldDAB lists BBC World Service on block 6A at 181.936 MHz; Radio Sportiva’s technical channel and reception at Qawra/MFCC remain unverified. BBC programme pages confirm Sportsworld episodes dated 17 and 18 October but do not name a particular match; displayed start times proved viewer-time-zone-dependent across checks, so no definitive start time is asserted. NET FM’s grid also lists a Friday 18:30 show, ‘Mhux Premier biss’ (16 October in the trip window), whose content is unverified. No current AM/MW sports service or named-event radio carriage was confirmed. A third-party TalkSPORT/6C claim is explicitly unverified.
- **Expense planner (18 blank-by-default categories):** editable EUR budget/actual fields, notes, totals and difference, browser-local autosave, CSV export, source links, and reset are available. The starter has no assumed itinerary, personal amounts, booking costs, event costs, reimbursement, tax total, tip, or exchange rate; blank does not mean free. The MTA’s published environmental-contribution rate is €1.50/night/person aged 18+ (capped at €22.50/person); six chargeable nights would be €9 per eligible adult only conditionally, and the actual invoice remains unknown.

The source register, unresolved questions, workstream status, and cross-topic handoffs are in [`SOURCES.md`](SOURCES.md), [`OPEN_QUESTIONS.md`](OPEN_QUESTIONS.md), [`STATUS.md`](STATUS.md), and [`HANDOFF.md`](HANDOFF.md).

## Three cumulative review passes

1. **Implementation and source pass — passed after both main-branch reconciliations.** `python3 scripts/validate_site.py` reports 6 topic JSON files / 107 exact-schema records, 184 unique primary/cited record URLs present in `docs/SOURCES.md`, 15 root HTML pages / 86 link attributes, 8 navigation destinations, and all 18 planner rows wired. The schema enforces the exact requested `price range` key and five source types, including `directory`. JavaScript syntax, JSON parsing, and staged/unstaged `git diff --check` passed. External URL liveness and full graphical browser rendering remain limited.
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

## Session update — 11 Oct 2026 (second pass after merging origin/main)

- Merged `origin/main` (4775239) from another session’s 11 Oct verification and corrected this session’s unsupported claims; see `docs/STATUS.md` “Session pass log” for the three-pass record.
- Verified from primary pages this session: State Department Malta advisory (Level 1; embassy address; no vaccinations; €10,000 limit; riptides); EU ETIAS (not in operation) and EES (fully operational since 10 Apr 2026); Airport Direct TD1–TD5 frequencies and fares; MPT fares (winter €2.00 valid to 13 Jun 2026; summer €2.50, no dates); BBC Radio 5 Live Premier League dated listings (24–25 Oct); Gżira United v Mosta ticket prices and under-16 entry; Heritage Malta picnic time (13:00–16:00, on site 12:45) — the closure notice is still open.
- Not verified and left open: the 112 emergency number; Premier League Matchweek 7 official fixtures and live-audio terms; NET FM Friday 18:30 slot content; WorldDAB Digi B 2 ‘Sports Channel’ identity; TD1 Qawra stop; the TWC entrance and door times; Route 186 Qawra departure minute.


## Session addendum — 11 October 2026 (second session)

This session performed an independent second verification pass on top of the first 11 Oct pass:

- **Re-fetched and updated:** Malta Met Office 7-day forecast (now covering 13–17 Oct: isolated showers 13 Oct, mainly sunny 14–16 Oct, mainly cloudy 17 Oct; 18–19 Oct still outside the window); MPT Route 186 return direction (Stadium 2194 at 05:52–20:53, Qawra seafront stops not served on return, last Buġibba Bay 1 arrival 21:27, correcting the carried-over 21:26); MPT full fare table (€2.00 winter/€2.50 summer day singles, night/special/TD €3.00, TD1 €3.50, €50 no-ticket fine, card prices; October 2026 single-fare window still unsettled); NET FM grid (added the Friday 18:30 ‘Mhux Premier biss’ entry, content unverified); BBC Sportsworld listing (dates confirmed; start-time zone discrepancy documented and definitive times removed); MTA environmental contribution (rate/cap confirmed, ‘visit’ definition and 15-night threshold noted); AX ODYCY property page (4-star, former AX Seashells, contact details).
- **New open questions:** BBC Sportsworld exact start times; NET FM Friday show content. Updated: weather (13–17 Oct resolved, 18–19 Oct open), fare applicability, door-to-door itinerary facts.
- **Verification:** `scripts/validate_site.py` passes (6 JSON files, 108 records, cited-URL coverage, page/link/nav/expense wiring). No unverified claim was promoted to fact; only records whose sources were re-fetched on 11 Oct were changed. GitHub Pages remains configured to publish the `main` branch root.

## Update — 11 Oct 2026 (third pass, arena/d347388b)

**Verified this pass (official sources):**
- Route 186 return stop (Stadium 2194, last 20:53).
- MPT fares, including Explore Flex.
- Uber's Malta service options.
- Premier League kickoffs for 17–19 Oct and UCL matchday 2 kickoffs, in Malta time.
- BBC Sportsworld 17/18 Oct start times and 3 h 53 min durations.
- Rai Radio 1's weekend Serie A programme.
- Kalshi's travel-eligibility wording.
- Malta Aviation Museum and Mosta Rotunda hours and fees.

**Bug fixed:** the expense planner's "Price status" was blank on every row because the code used `price_range` instead of the data key `price range`.

**Partially verified / unverified:**
- TWC match times (community wiki).
- Serie A times (broadcaster report).
- Rai Champions League carriage for 2026–27 (prior-season pattern only).
- Fontanella and Ta' Marija hours.
- Dash Berlin details.
- Airport taxi fare, about €25 (third-party only).

**Limitations:**
- No real-browser screenshot (Chromium download blocked); the DOM test and CSS review stand in.
- No on-site DAB+ reception test.
- Kalshi's country list was not read.

**Next session:**
- Recheck the BBC episode pages from about 15 Oct for the named commentary match.
- Add Europa League 15 Oct fixtures and TWC 15–16 Oct times.
- Add the 18–19 Oct forecast (the Met Office snapshot now covers 13–17 Oct).
- Confirm the TWC entrance and tickets.
- Run the MPT journey planner for each event date.

## Session report — 11 October 2026 (merged branch: night routes, fixture records, planner day rows)

This branch was merged with `origin/main` twice (PRs #21–#22, then PRs #24–#27) so that the parallel 11 October research passes ship as one dataset. Where passes disagreed, the newer re-read was kept; this branch's remaining unique additions are below. The offline gate is green: `python3 scripts/validate_site.py` reports **6 topic JSON files / 128 exact-schema records; 216 unique record URLs present in `docs/SOURCES.md`; 15 HTML pages / 89 link attributes; 8 navigation destinations; 18 expense categories + 7 day rows wired**. jsdom simulations re-run after the merge: planner **18/18**, site **49/49**; `node --check` is clean on `js/site.js` and the inline `costs.html` script.

### This branch's standing additions (kept through both merges)

* **Night routes (transport).** N212 from Buġibba runs 23:50–01:30 every 20 minutes and N13 from Valletta 23:10–02:10 (weekdays) per the operator's April 2026 announcement; **no night route serving Ta' Qali/Attard was verified**, so late exits still need a taxi/ride-hailing backup. The operator's generic night-routes page returned 404 on 11 October.
* **Fixture-context records (radio).** The UEFA Europa League league-phase matchday on Thursday 15 October 2026 and the NFL Sunday slate of 18 October 2026 (official NFL pages, Malta-time conversions) are recorded as fixture context only — a fixture is not evidence of radio carriage.
* **Expense planner day rows.** `data/expenses.json` carries a `day_rows` array (7 trip days, 13–19 October) and `costs.html` renders day-by-day budget/actual/note rows, an itinerary/confirmations notes box, day totals, a grand total and CSV export of categories, days and notes — so a supplied itinerary can be costed day by day. Nothing is prefilled, and category rows and day rows are separate views to avoid double counting.
* **Venue corroboration trail.** The BLAST Arena Studios Malta address (MFCC South Gate National Stadium, Millennium Stand, Attard ATD 4000) was corroborated on 11 October by the MTA directory, GamingMalta, Eventworks, Liquipedia and BLAST's attendee guide for another event at the same venue; the event-to-venue link still rests on the organizer's naming, and the event gate, doors and tickets remain unpublished.

### Reconciliation notes from this merge

* **Route 186.** The final dataset uses the direction-split reading re-checked on 11 October: outbound (Rabat-bound) from Qawra stop 952 (06:09–21:39) to Stadium 6227 (06:39–22:08); return (Buġibba-bound) from Stadium 2194 (05:52–20:53), last listed arrival Buġibba Bay 1 at 21:27, not serving the Qawra seafront stops. Earlier parallel-table variants (06:10–21:38; hour-type ambiguity) are documented in the record notes; the journey planner remains the authority.
* **BBC Sportsworld.** The third pass reconciled the viewer-local vs GMT displays (13:06/14:06 GMT = about 15:06–18:59 and 16:06–19:59 Malta time on 17–18 October); the named commentary match is still unannounced.
* **Radio Sportiva.** Listed in Digi B's directory, but no block or frequency was found and the Broadcasting Authority list does not name it; it remains a service to scan for rather than confirmed carriage.

### Still unverified / limitations

1. **Event access.** Spectator tickets, doors, daily match times and the TWC-specific entrance are unpublished; community-wiki match times are not organizer times.
2. **Late-night return.** No night route to Ta' Qali; the 17 October 19:00–00:00 diversion skips Gholja 2 through Targa toward Buġibba.
3. **Fares.** The October 2026 single-fare season is not established by MPT's page (winter €2.00 / summer €2.50 table; the stated winter window ended 13 June 2026).
4. **Radio reception and carriage.** No DAB+/FM receiver test at the hotel or venue; no fixture-specific commentary carriage confirmed anywhere.
5. **Platform and physical checks.** Social/review platforms partly blocked, walking times and real-device rendering not measured, and external URL liveness was not crawled.

### Suggested next-session tasks (priority order)

1. When the itinerary and ticket email arrive: paste them into the planner's notes box, fill the seven day rows, export the CSV, then convert confirmed session times into dated MPT planner queries for outbound and return on each event day.
2. Re-check the Route 186 return stop/times and the 17 October detour in the live planner within 24 hours of departure; keep the taxi backup for evening sessions.
3. Re-scan DAB+ on arrival: identify the 'Sports Channel' (12A) broadcaster, confirm BBC World Service and Rai Radio Uno reception indoors, and check which NET FM slot is commentary.
4. Confirm the environmental contribution on the invoice and the meal plan, then update the hotel rows in the planner.
5. Recheck the BBC episode pages from about 15 October for the named Sportsworld commentary match.
