# Final report — Malta Trip Guide (13–19 October 2026)

Last updated: 2026-10-11 (UTC)

## 1. What was verified

- **Canonical root-page architecture and shared 13-field schema:**
  - The site is built on the canonical root HTML pages (`index.html`, `getting-around.html`, `restaurants.html`, `activities.html`, `everyday.html`, `radio.html`, `costs.html`, `sources.html`), shared `css/style.css` and `js/site.js`, `data/record.schema.json`, and `scripts/validate_site.py`.
  - Every record across the six topic JSON files (`109` records total: `14` transport, `27` food, `29` activities, `15` everyday, `6` radio, `18` expenses) uses the exact 13 required fields (`id`, `name`, `category`, `area`, `address`, `hours`, `price range`, `description`, `source_url`, `source_type`, `date_checked`, `confidence`, `notes`), strict `source_type` values (`official`, `map`, `review`, `social`), and strict `confidence` values (`verified`, `partially verified`, `unverified`).
- **Workstream A — Getting around (`data/transport.json`, `getting-around.html`, 14 records):**
  - **Tournament window & venue context:** Official Thunderpick page (`https://world-championship.thunderpick.io/2026-finals/`, rechecked 11 Oct 2026) confirms the 12–19 October 2026 event window (12 Oct Arrival, 13 Oct Media Day, 14–16 Oct Group Stage, 17–18 Oct Playoffs, 19 Oct Departure) and lists Malta as the location. A Thunderpick-issued PR Newswire release names BLAST Studios Malta; a BLAST fan guide for a separate event places BLAST Arena Studios at MFCC, Ta’ Qali, ATD 4000 Ħ’Attard (kept strictly as venue-area context).
  - **Public transport:** Malta Public Transport Route 186 links Qawra stop 952 (listed 06:10–21:38 at a 30-minute frequency) and Ta’ Qali Stadium stop 2194; its normal return from Rabat/Ta’ Qali runs via St Paul’s Bay/Buġibba rather than the Qawra seafront (last listed arrival at Buġibba Bay 1 is 21:26). Route 214 links Qawra stop 952, Ta’ Qali stop Qali 2 (2542), and the airport. Airport Direct TD1 runs hourly (€3.50 without an eligible unlimited card) and includes Qawra stop Arznell 950.
  - **Service alerts (rechecked 11 Oct 2026):** MPT’s service updates (`https://www.publictransport.com.mt/latest-service-updates/`) confirm a Route 186 diversion on Saturday 17 October from 19:00 to approximately 00:00 toward Buġibba omitting stops Gholja 2 through Targa, plus a long-term construction closure of stop Saqqajja (ID 4627, in Rabat) on Route 186 through 1 January.
  - **Fares, ride-hailing/taxis, car hire & ferries:** MPT lists €2 winter / €2.50 summer cash/contactless day fares (2-hour transfer window), €19 12-journey card, and €25 Explore Adult 7-day card. Bolt, eCabs, and Malta Taxi (+356 2182 3017 advertised 24/7) provide app/dispatch ride-hailing and taxis; airport rental desks are at Park East Level 1 (~3-minute walk); Valletta Ferry Services (€3/€5 day, €3.50/€5.20 night), Gozo Channel (€4.65 standard adult passenger tariff), and Gozo Highspeed (€6.50–€8.50 one-way, with 14 and 17 Oct race schedule restrictions) are compared in `mode-comparison-summary` and `getting-around.html`.
- **Workstream B — Food & cafés (`data/food.json`, `restaurants.html`, 27 records across 6 categories):**
  - Covers five AX ODYCY venues (Minoa Mediterranean Fusion, Trattoria Riccardo, Deck & Keel, Espresso Grab & Go, Medusa Sky Bar), eight nearby Qawra/Buġibba/St Paul’s Bay restaurants (Cheeky Monkey Gastropub, Sabi House, Lovage Bistro, Peking To-Go / Peking Street Food, Venus Restaurant, Ta’ Pawla, Nine Lives, Made in Sud), four nearby cafés/bakeries (Ombré Café Bistro, Cheeky Monkey Crêperie, Café Maroc, Michele’s Cafe), six Valletta/St Julian’s/Mġarr venues (Gululu, Sole by Tarragon, il-Barri, Caffè Cordina, Ta’ Nenu, Is-Suq Tal-Belt), Maltese food/community notes, and two explicit closure/status warnings (Luzzu closed for refurbishment per 29 Sep 2026 operator notice; The Meeting Point marked CLOSED on TripAdvisor).
- **Workstream C — Gaming, activities, landmarks & events (`data/activities.json`, `activities.html`, 29 records across 7 categories):**
  - Covers dated trip-window events (TWC Finals 12–19 Oct; 13 Oct Fort St Elmo lecture *‘Their native valour’* at 19:00, €5; 14 Oct Gżira United v Mosta FC at Tony Bezzina Stadium at 19:00, €10/€6; 15 Oct Valletta Waterfront Jazz Series Vol. 2 at 19:30, €25 listed; 17 Oct 47th Rolex Middle Sea Race start at 11:00 in Grand Harbour; 17–18 Oct free Valletta Waterfront *Autumn Vibes*; 18 Oct *In Guardia* at Fort St Elmo at 10:00/11:00–12:00, €10/€17; 18 Oct *CDM Sundays* at Café del Mar, 17+), two conflicted/incomplete event listings (17 Oct *Picnic in the 1800s* vs. Borġ in-Nadur road-works closure; 17 Oct Fort St Elmo *Sailing Spectacle*), three active arcade/VR/laser-tag options (The Eden XP Arcade; MULTIMAXX St Julian’s and Kordin), three PC gaming centre status conflicts (The Gamers Lounge, Esports Plaza, Eden Esports Centre), and twelve north-Malta/Valletta/Mdina/UNESCO attractions (Malta National Aquarium with 19:30 last entry, Malta Classic Car Collection, Popeye Village, Comino/Blue Lagoon timed QR pass rules, St John’s Co-Cathedral, Grand Master’s Palace, National Museum of Archaeology, Fort St Elmo, Ta’ Qali Artisan Village, Mdina, St Paul’s Catacombs, Ħaġar Qim & Mnajdra).
- **Workstream D — Everyday guide for a U.S. traveler (`data/everyday.json`, `everyday.html`, 15 records across 5 categories):**
  - Covers UK-style Type G plugs (230 V, 50 Hz), GO (€15.99/28 days) and Melita (€10 starter SIM/eSIM) prepaid options, euro currency and discretionary tipping caveats, U.S. passport short-stay Schengen rules, EU Entry/Exit System (EES operational since 10 Apr 2026), ETIAS status (rechecked 11 Oct 2026: still not in operation), emergency number 112 and U.S. Embassy Malta (+356 2561 4000, Ta’ Qali National Park Street, Attard), coastal/rip-current safety, Maltese and English official languages, CEST (UTC+2) time through 25 Oct 2026, left-hand driving, cannabis/CBD border warning, and the **11 October 2026 Malta Met Office 7-day forecast snapshot** covering 13–17 October (Tue 13 Oct isolated showers 26°C/19°C; Wed 14–Fri 16 Oct mainly sunny 24–25°C/17–18°C; Sat 17 Oct mainly cloudy 23°C/18°C; detailed forecast sea temperature 26°C).
- **Workstream E — Sports radio & Kalshi markets (`data/radio.json`, `radio.html`, 6 records):**
  - Verifies NET FM on FM 101 MHz (licensed by the Broadcasting Authority; recurring Saturday 16:00 *Hits & Score* and Sunday 15:00 *Sports Box* grid), Digi B Network’s Malta DAB+ directory listings for Radio Sportiva and BBC World Service, WorldDAB’s specialist technical directory listing for BBC World Service on Digi B Network block 6A at 181.936 MHz, BBC *Sportsworld* dated broadcasts on Saturday 17 October (13:06 GMT / 15:06–18:59 Malta CEST, 3h 53m) and Sunday 18 October (14:06 GMT / 16:06–19:59 Malta CEST, 3h 53m; programme overview states coverage includes the English Premier League), Radio Sportiva’s *Diretta Sportiva* schedule (which notes live coverage can extend to 24:00 for Serie A, Serie B, Coppa Italia, European Cups, F1, and MotoGP), and **Kalshi’s 16–18 October EPL and Serie A market kickoff schedules** (`https://kalshi.com/category/sports/soccer/epl`, `https://kalshi.com/category/sports/soccer/serie-a`, `https://kalshi.com/category/sports/esports/cs2`, checked 11 Oct 2026) that overlap those weekend radio broadcast windows.
- **Workstream F — Expense planner (`data/expenses.json`, `costs.html`, 18 records):**
  - Provides 18 blank-by-default budget/actual categories with browser-local `localStorage` autosave, CSV export, reset, and sourced Malta Tourism Authority environmental contribution rules (€1.50 per night per guest aged 18+ from 1 Jul 2026, capped at €22.50 per person per visit; six billable nights = €9 per eligible adult conditionally). Fixed `costs.html` so each expense card renders `record["price range"]` under Price status.

## 2. What could not be verified (and is recorded in `docs/OPEN_QUESTIONS.md`)

- **Thunderpick World Championship 2026 Finals attendee logistics:** Official Thunderpick pages checked through 11 October 2026 still do not publish the exact street address/pin, daily public match/door start times, spectator admission/ticket rules, or event shuttle details.
- **Date-and-time-specific transit itinerary & 17 October return impact:** Because exact daily TWC door/finish times and the TWC entrance pin are unpublished, a date-and-time-specific door-to-door journey-planner result and the exact effect of the Saturday 17 October 19:00–00:00 Route 186 diversion on the traveler’s post-event return remain open.
- **October 2026 single-bus-fare seasonal cutoff:** MPT’s fare page lists €2 winter and €2.50 summer cash/contactless day fares, but its displayed seasonal date labels do not specify which single fare applies on 13–19 October 2026.
- **Radio reception, match-specific commentary & Kalshi eligibility:** Local indoor FM/DAB+ reception at AX ODYCY and MFCC could not be physically tested from this environment; Radio Sportiva’s current DAB+ block/frequency is not stated on Digi B’s channel page; neither BBC *Sportsworld* nor Radio Sportiva had published its match-by-match commentary selection for 16–18 October as of 11 October; Kalshi’s CS2 page on 11 October showed games through 11 October only (not yet 14–18 October TWC Finals); no Malta radio carriage was confirmed for CS2/TWC, Gżira United–Mosta, or the Rolex Middle Sea Race; TalkSPORT on DAB+ 6C remains an uncorroborated third-party directory claim; and Kalshi account/trading access while physically in Malta is not verified.
- **18–19 October weather forecast:** The Malta Met Office 7-day forecast fetched 11 October covers 13–17 October; Sunday 18 October and Monday 19 October remain beyond the 7-day window.
- **Blocked/limited third-party review & social platforms:** Direct automated requests to Yelp, Instagram, TikTok, Facebook, X, and live Reddit refreshes returned HTTP 403 or login barriers; Google Maps views were limited profile snapshots.
- **Venue/event conflicts & traveler-specific booking inputs:** Sabi House closing time (22:00 operator vs. 23:00 TripAdvisor), St Paul’s Catacombs Friday hours (19:00 Heritage Malta summer chart vs. 17:00 Google Maps), Borġ in-Nadur road-works closure vs. the 17 October picnic listing, PC gaming centre walk-in status (The Gamers Lounge, Esports Plaza, Eden Esports Centre), and the traveler’s actual flight numbers, hotel invoice, meal plan, and ticket confirmations remain open.

- **Getting around (13 records):** compares airport, bus, taxi/ride-hailing, car-hire, ferry, and local transport options. MPT’s static Route 186 timetable (re-read 11 Oct) lists Qawra stop 952 at 06:09–21:39 toward Ta’ Qali Stadium stop 6227 (06:39–22:08). The Rabat-to-Buġibba return (re-read 11 Oct) serves Stadium stop 2194 (05:52–20:53) via St Paul’s Bay/Buġibba rather than the Qawra seafront stops (950–955); the last listed arrival is Buġibba Bay 1 (stop 2527) at 21:27. Route 214 is an alternate to compare. The full fare table is recorded, but the October 2026 single-fare window is not established by the operator page. A date-specific itinerary, venue walk, the 17 October diversion’s exact impact, the Saqqajja (4627) stop closure on the Rabat side, fare validity, and hotel return still require checking in the operator planner; the page is not a door-to-door guarantee.
- **Food and cafés (27 records):** includes AX ODYCY/on-property options, 12 additional Qawra-area/Valletta venues, selected wider-area ideas, local-food context, and separately labelled map/review/community observations. Platform ratings are not blended. Reported closures, inaccessible-platform limits, and conflicting hours remain caveated; current menus, hours, and representative meal costs are not assumed.
- **Activities, landmarks, and events (29 records):** covers recreation and gaming leads, Malta attractions, and dated events relevant to the trip. New source-backed entries include MULTIMAXX St Julian’s/Kordin, Popeye Village, Classic Car Collection, the 13 Oct Heritage Malta lecture, 15 Oct Jazz Series, the 17 Oct Middle Sea Race listing at 11:00 and Waterfront Autumn Vibes, and 18 Oct CDM Sundays; unknown prices, times, inventory, and access remain marked. Event dates are kept distinct from spectator access, ticket inventory, prices and opening times; the Fort St Elmo Sailing Spectacle and Heritage Malta picnic details remain incomplete/conflicted.
- **Everyday travel (15 records):** covers entry pointers, EES/ETIAS, currency/cards, language, electricity, mobile connectivity, emergency/health, safety, weather, and practical U.S.-traveler considerations. Passport, device, carrier, itinerary, and medicine-dependent advice is conditional.
- **Sports radio (6 records):** the Broadcasting Authority lists NET FM at FM 101 MHz; its official grid shows recurring weekend sports programming, not a trip-week guarantee, and does not explicitly state its time zone. Digi B’s directory lists Radio Sportiva and BBC World Service on DAB+. WorldDAB lists BBC World Service on block 6A at 181.936 MHz; Radio Sportiva’s technical channel and reception at Qawra/MFCC remain unverified. BBC programme pages confirm Sportsworld episodes dated 17 and 18 October but do not name a particular match; displayed start times proved viewer-time-zone-dependent across checks, so no definitive start time is asserted. NET FM’s grid also lists a Friday 18:30 show, ‘Mhux Premier biss’ (16 October in the trip window), whose content is unverified. No current AM/MW sports service or named-event radio carriage was confirmed. A third-party TalkSPORT/6C claim is explicitly unverified.
- **Expense planner (18 blank-by-default categories):** editable EUR budget/actual fields, notes, totals and difference, browser-local autosave, CSV export, source links, and reset are available. The starter has no assumed itinerary, personal amounts, booking costs, event costs, reimbursement, tax total, tip, or exchange rate; blank does not mean free. The MTA’s published environmental-contribution rate is €1.50/night/person aged 18+ (capped at €22.50/person); six chargeable nights would be €9 per eligible adult only conditionally, and the actual invoice remains unknown.

- **Pass 1 (Implementation & live-source verification):** Refreshed time-sensitive official sources on 11 October 2026; added `mode-comparison-summary` (`data/transport.json`) and the mode comparison section (`getting-around.html`); added `kalshi-epl-serie-a-radio-overlap-oct-2026` (`data/radio.json`) and updated `radio.html`; harmonized categories across `data/food.json`, `data/activities.json`, and `data/everyday.json`; added the 13–19 October day-by-day planning framework to `index.html`; fixed `costs.html` to read `record["price range"]`; and updated `docs/SOURCES.md`, `docs/OPEN_QUESTIONS.md`, `docs/HANDOFF.md`, `docs/STATUS.md`, and `README.md`.
- **Pass 2 (Bug, requirement, assumption & edge-case check):** Enforced strict 4-value `source_type` (`official`, `map`, `review`, `social`) in `data/record.schema.json` and `scripts/validate_site.py`; added automated validation that `costs.html` reads `record["price range"]`; verified all 109 records and 191 unique URLs against `docs/SOURCES.md`; and tested all pages and interactive scripts.
- **Pass 3 (Final line-by-line prompt check):** Re-verified all workstreams A–G against the prompt’s scope, hotel/event parameters, zero-hallucination standard, and documentation requirements.

## 4. Next-session recommendations

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
