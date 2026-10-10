# Cross-workstream handoff

Last updated: 2026-10-10 (UTC)

## Shared brief

- Travel window: 13–19 October 2026.
- Base: AX ODYCY, Deluxe sea-view room, Qawra Coast Road, Qawra SPB 1902, Malta. User-provided scenario; booking/coverage is not verified.
- Event: Thunderpick World Championship 2026. Organizer's broader final-stage window is 12–19 Oct; media day 13 Oct; group stage 14–16 Oct; playoffs 17–18 Oct; departure 19 Oct. The public tournament is separately described as 14–18 Oct. Do not conflate those windows.
- Requested/planning destination: BLAST Arena Studios at MFCC, Ta' Qali, ATD 4000. BLAST's guide for a separate 2026 event publishes that studio address; Thunderpick's own page currently confirms only Malta as the LAN location, so its exact venue and access are not established.
- Public TWC attendance, tickets, entry times/policies, match times and any spectator access are unverified. Avoid language suggesting that the user can enter the studio.

## Transport / event handoff (A ↔ C ↔ F)

- MPT's current Route 186 timetable shows a scheduled frequency of every 30 minutes, Qawra stop 952 (the published snapshot begins 06:10 and ends 21:38), and directional Ta' Qali Stadium stops 2194 / 6227. This is the strongest public-bus corridor for the requested trip, but TWC's exact venue/access and the best stop-to-entrance walking leg are not established.
- The normal return toward Buġibba runs via St Paul's Bay and the Buġibba seafront rather than Qawra; the current listing's final Bugibba Bay 1 arrival is 21:26. Verify a date-specific return and onward hotel connection in MPT's planner; a taxi/ride-hail fallback may be needed after a late finish.
- MPT currently lists a Route 186 detour toward Buġibba on Friday/Saturday evenings, 19:00–midnight, starting 17 Oct; Gholja 2 through Targa are skipped. This is particularly relevant to playoff Saturday, but its impact on the exact Ta' Qali boarding/return stop is unresolved. Recheck the notice close to the trip.
- MPT's fare page confirms two-hour day tickets and €2.00 winter / €2.50 summer rates, but the current 2026 page does not publish a complete October 2026 switchover date. The expense planner should use a range and mark the date unresolved.
- Do not assume venue doors match published match times or that special transport will be added for TWC.

## Radio / sports handoff (E ↔ C)

- BBC World Service has official Sportsworld episodes dated 17 and 18 Oct (live sport; GMT episode identifiers). Malta local starts are 15:06 Sat / 16:06 Sun when converting GMT to CEST (UTC+2). BBC World Service appears on the Maltese DAB+ channel operator's official list.
- BBC Radio 5 schedules official PL commentary on 17 Oct: Manchester City–Ipswich at 14:45 BST (Sports Extra), Brentford–Liverpool at 15:00 BST (Radio 5 Live), and Newcastle–Aston Villa at 17:30 BST (Radio 5 Live). On 18 Oct: Brighton–Crystal Palace at 13:55 BST (Sports Extra), Bournemouth–Sunderland on Sports Extra 2 (BBC confirms match assignment; separate start not exposed), Leeds–Manchester United at 14:00 BST (Radio 5 Live), and Nottingham Forest–Arsenal at 16:30 BST (Radio 5 Live). UK→Malta local conversion is +1 hour while Malta is CEST.
- The official Malta DAB+ list includes BBC World Service, not BBC Radio 5 Live/Sports Extra. BBC/PL online access from Malta, a working receiver at the hotel and exact commentary choices in Sportsworld remain unresolved; do not promise listening access.


## Food / review handoff (B ↔ F)

- Workstream B lists Espresso, Trattoria Riccardo, Minoa, Cheeky Monkey, Venus and Ombré with official hours/menu sources and dated euro-price examples. Espresso and Cheeky Monkey price PDFs are from July 2025; treat those amounts as examples, not guaranteed October prices.
- Luzzu's official site says it is closed for refurbishment as of 9 Oct 2026 and gives no reopening date; its 2022 menu is stale and must not be used. Keep it off the open-for-business shortlist unless rechecked.
- The user's meal plan is unknown. Do not assume breakfast/all-inclusive or hotel restaurant credit is covered; leave dining as an editable expense.
- Tripadvisor ratings/counts were observed only in dynamic search-result snapshots, and regional pages differ. Google Maps did not render; Yelp returned U.S. city lookalikes / 403; Instagram/TikTok/Facebook direct fetches returned 403; Reddit was historical/anecdotal and 403; X results were irrelevant/old. No platform snapshot is a ranking or quality guarantee.
- Menu images/PDF text do not establish allergen safety, step-free access, payment acceptance or reservation availability. Ask venues directly where relevant.



## Expense planner handoff (F ↔ A / B / C / D)

- `pages/expenses.html` contains an editable, browser-only EUR worksheet (no persistence/network submission), and optional USD conversion only when the user enters a rate. Empty amounts are excluded and shown as unpriced; only explicitly entered totals, meal/day multiplier, bus range and the opt-in/checkbox environmental-contribution estimate feed its total.
- The starting values (one traveler, seven calendar days, six nights) are labeled assumptions; 13 Oct check-in / 19 Oct checkout has not been verified. Guest age was not supplied, so the eligible 18+ count is blank and no adult is assumed. Hotel/flight/meal-plan/prize coverage and all traveler-specific fees remain unknown.
- MTA's official rate from 1 Jul 2026 is €1.50 per night per guest aged 18+ at the start of the visit, capped at €22.50 per person per visit and itemized separately. The planner checkbox defaults on, but the formula is not included until an eligible-guest count is entered; uncheck it if the user confirms coverage or non-applicability.
- The planner's €2.00–€2.50 single-journey bus range reflects MPT's currently published winter/summer fares only; Oct 2026 changeover is OQ-05. For a pass or Airport Direct, enter an actual card/quote cost and do not double-count rides.
- Optional price anchors are sourced in `data/expenses.json`; dated event availability and the known event-access/time caveats still apply. Do not add an advertised ticket to the user's subtotal unless they choose it and confirm availability.
- G should preserve the form's in-page calculator, integrate the shared renderer for the sourced price references, and test both form/summary behavior and shared mobile navigation.

## U.S. traveler practicalities handoff (D ↔ A / F)

- For a traveler on a U.S. passport, State Department lists no tourist visa for stays up to 90 days; EU guidance requires passport issuance within 10 years and validity at least three months beyond intended departure. The exact nationality, prior Schengen days and route were not supplied.
- Official EU FAQ says EES is fully operational since 10 Apr 2026 and applies to visa-exempt non-EU short-stay visitors. As of 9 Oct ETIAS was not operating and no application was being collected; prior Q4-2026 forecast is not a start date. Recheck before boarding.
- Emergency number 112; State Department says U.S. medical plans often do not cover care abroad, medical care is not free for non-citizens, and recommends travel/medical-evacuation insurance. Prescription/controlled-medicine details are traveler-specific.
- Currency is EUR; State Department says AmEx is not widely accepted and U.S. bank-card ATM withdrawals may incur fees. Roaming, FX/ATM fees, card coverage, tipping and hotel meal plan remain traveler-specific or not fixed.
- Type G plug, 230 V / 50 Hz; inspect device labels. Tap water meets WSC/State Dept potable-water statements; no check of the hotel's plumbing was made.
- State Dept advisory is Level 1 (9 Jul 2026), but warns about riptides, tourist-area theft, left-side driving, narrow/flood-prone roads and uneven pedestrian access. October is in the rainy season; refresh the live Met Office forecast.
- Malta Met Office forecast checked 9 Oct ended 15 Oct; the data snapshot does not cover 16–19 Oct. Do not hard-code those dates as a forecast.

## Activities / gaming handoff (C ↔ A ↔ F)

- Confirmed public gaming option: MULTIMAXX at Bay Street Level 4, St Julian's, with published laser-tag/VR rates and walk-ins. It is a leisure arcade, not a PC-gaming café.
- The Gamers Lounge current site confirms a Msida gaming lounge/retail business and store hours, but not current PC-session rates or walk-in access. Esports Plaza remains unverified (HTTP 503); do not direct the traveler there.
- TWC is confirmed as a Malta LAN, with group stage 14–16 Oct and playoffs 17–18 Oct. TWC-specific public venue, admission, tickets and door times remain unconfirmed. BLAST's published studio address is from a different event.
- Optional dated event: Malta FA lists Gżira United v Mosta on 14 Oct at 19:00 at Tony Bezzina Stadium; adult tickets currently €10, seniors €6, under-16s free with gate ticket. This is a separate trip, not a TWC event.
- Race start: 17 Oct 11:00 from Grand Harbour, with Valletta fortifications given as a viewing area. Heritage Malta’s Picnic in the 1800s at Borġ in-Nadur is also listed 17 Oct 13:00–16:00 (arrive 12:45), €55 non-member / €45 member; current ticket availability is unverified. In Guardia: 18 Oct 11:00, adult €10 show-only / €17 combo, weather permitting. CDM Sundays: 18 Oct 18:00–01:00, 17+ and €10–€15, but its FAQ says tickets are only valid after 20:00; ask before attending and pre-plan a taxi return.
- Aquarium's current ticket page provides after-16:00 rates; its contact page lists 10:00–20:00 daily. Recheck those dynamic details. Ħaġar Qim/Mnajdra accessibility is limited: the visitor centre and Ħaġar Qim accessible with assistance; Mnajdra not accessible.

## Research and integration protocol

- A–F each own exactly one `data/*.json` file and one `pages/*.html` topic page. They edit no shared navigation, stylesheet, root index, shared JS, README, or another stream's files.
- G integrates only after A–F topic content is finished, updates shared shell/source/summary, and runs all three requested passes.
- Use the shared field order and exact key `price range`; log source URLs, access dates, and owning workstreams in `docs/SOURCES.md`. Keep unresolved facts in `docs/OPEN_QUESTIONS.md` and update `docs/STATUS.md` as each gate closes.
- Research Google Maps/reviews, Yelp, Instagram, TikTok, Facebook, Reddit and X as requested; record which platforms could not be accessed directly, and never imply a login-walled page was inspected when only indexed snippets were available.
- Before final integration, cross-check every rendered claim against its data record and source log, validate every JSON file and local link, test the site at mobile and desktop widths, and run Passes 1–3 on the integrated result.