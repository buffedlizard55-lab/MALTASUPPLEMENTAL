# Final report — Malta Trip Guide

**Planning window:** 13–19 October 2026
**Hotel supplied by traveler:** AX ODYCY Malta, Qawra Coast Road, Qawra SPB 1902
**Event location supplied by traveler:** BLAST Arena Studios, Attard
**Research snapshot:** see the individual access dates in [`SOURCES.md`](SOURCES.md)

## Executive summary

The site is a mobile-friendly, static Malta tourism and recreation guide with an overview, six topic pages, shared navigation, an evidence dashboard, and an editable expense planner. Six topic JSON files hold **107 common-schema records** with source type, check date, confidence, and caveats; `data/record.schema.json` defines the exact shared record shape. Unknowns are stated rather than guessed.

The traveler supplied the hotel name/address, Deluxe Sea-View room type, trip dates, and event destination name (“BLAST Arena Studios, Attard”). Those are planning inputs. The official TWC page lists Malta only; the MFCC/Ta’ Qali address is venue-area context from a BLAST guide for a different event, not a confirmed TWC pin or entrance. The hotel reservation, rate, deposit, check-in/out times, flights, party size, arrival/departure times, and tournament attendance were not provided. Six hotel nights applies only if check-in is 13 October and check-out is 19 October; the guide does not assume that booking condition, event access, or an itinerary.

## Verified deliverables and research findings

- **Getting around (13 records):** compares airport, bus, taxi/ride-hailing, car-hire, ferry, and local transport options. MPT’s static Route 186 page lists Qawra stop 952 at 06:09–21:39 (corrected 11 Oct; the earlier 06:10–21:38 was wrong). Its normal Rabat-to-Buġibba return runs via St Paul’s Bay/Buġibba rather than Qawra seafront; the last listed arrival is Buġibba Bay 1 at 21:26. Route 214 is an alternate to compare. A date-specific itinerary, venue walk, the 17 October diversion’s exact impact, fare validity, and hotel return still require checking in the operator planner; the page is not a door-to-door guarantee.
- **Food and cafés (27 records):** includes AX ODYCY/on-property options, 12 additional Qawra-area/Valletta venues, selected wider-area ideas, local-food context, and separately labelled map/review/community observations. Platform ratings are not blended. Reported closures, inaccessible-platform limits, and conflicting hours remain caveated; current menus, hours, and representative meal costs are not assumed.
- **Activities, landmarks, and events (29 records):** covers recreation and gaming leads, Malta attractions, and dated events relevant to the trip. New source-backed entries include MULTIMAXX St Julian’s/Kordin, Popeye Village, Classic Car Collection, the 13 Oct Heritage Malta lecture, 15 Oct Jazz Series, the 17 Oct Middle Sea Race listing at 11:00 and Waterfront Autumn Vibes, and 18 Oct CDM Sundays; unknown prices, times, inventory, and access remain marked. Event dates are kept distinct from spectator access, ticket inventory, prices and opening times; the Fort St Elmo Sailing Spectacle and Heritage Malta picnic details remain incomplete/conflicted.
- **Everyday travel (15 records):** covers entry pointers, EES/ETIAS, currency/cards, language, electricity, mobile connectivity, emergency/health, safety, weather, and practical U.S.-traveler considerations. Passport, device, carrier, itinerary, and medicine-dependent advice is conditional.
- **Sports radio (6 records):** the Broadcasting Authority lists NET FM at FM 101 MHz; its official grid shows recurring weekend sports programming, not a trip-week guarantee, and does not explicitly state its time zone. Digi B’s directory lists Radio Sportiva and BBC World Service on DAB+. WorldDAB lists BBC World Service on block 6A at 181.936 MHz; Radio Sportiva’s technical channel and reception at Qawra/MFCC remain unverified. BBC programme pages show Sportsworld on 17 and 18 October but do not name a particular match. No current AM/MW sports service or named-event radio carriage was confirmed. A third-party TalkSPORT/6C claim is explicitly unverified.
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

