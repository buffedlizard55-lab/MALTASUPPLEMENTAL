# Final audit report — Malta trip guide

**Audit date:** 11 October 2026 (UTC)
**Session branch:** `arena/cc913a9b-maltasupplemental`
**Starting revision:** `b307c51`
**Integrated upstream:** PR #42 (`5cdea68`), PR #43 (`94733df`), PR #45 (`dc2fe82`) and PR #44 (`c7d1d00`).

## Summary

The repository contains a mobile-friendly, source-linked Malta guide for the traveler-supplied **13–19 October 2026** stay at AX ODYCY in Qawra and the supplied Thunderpick CS2 destination at BLAST Arena Studios, Attard. Dedicated sections cover transport, food/cafés, activities/landmarks/events, practical U.S.-traveler guidance, Malta sports radio, expenses and the CS2 event. Topic pages render from canonical JSON data; citations and access dates are recorded in `docs/SOURCES.md`.

The planner has 18 core categories and seven optional daily rows. It starts blank, previews itinerary quick-fill matches before applying them to blank budget fields, saves only in the current browser, and supports CSV export and reset. It assumes no flight, hotel amount, party size, ticket, transport choice, ride count or personal spend.

The final re-audit preserved PR #44’s dated report that Ninjas in Pyjamas replaced Virtus.pro after Virtus.pro withdrew on 9 October, while qualifying Eventbrite ticket-price wording against the current page-text extraction. It also corrected the Route 186 diversion interpretation, the scope of late-return evidence and the MTA contribution wording. This is a planning aid—not a booking, admission, fare, service, live-availability, trip-itinerary, radio-reception or event-carriage guarantee.

## Material findings and limits

### Thunderpick event, field and access

The Hotspawn/Eventbrite listing read on 11 October identifies **BLAST Arena Studios Malta, MFCC South Gate National Stadium, ATD 4000 Attard**, for **14–18 October**, with in-person attendance and an **18+** condition. It shows check-in/games for 14–16 October: Wednesday and Thursday 09:30/10:30 with agenda rows ending 22:30; Friday 14:00/15:00 ending 21:00. Its headline says 22:00, so the Wednesday/Thursday discrepancy should be reconfirmed. The 17–18 October agenda entries and interactive FAQ answers were not visible in the extracted page.

A separate 11 October listing-card capture and HLTV report record a **“Free / Reserve a spot”** offer, but the current page-text extraction did not expose a fee table or ticket-tier total. This is dated evidence of an advertised offer, not current inventory, a checkout quote, a personal reservation or guaranteed entry. No ticket was purchased or held by this project. The attendee gate, ticket validity/scanning across days, transferability, parking, catering and weekend schedule remain open.

The 2 October HLTV field report listed Virtus.pro; on 9 October HLTV reported that Virtus.pro withdrew for visa and health reasons and Ninjas in Pyjamas took its slot. Hotspawn separately reported the substitution. The organizer’s own published pages still showed the original field when last checked. The current team record therefore keeps the substitution evidence attributed and notes that the organizer’s pages lagged. Team and group details are not a spectator ticket, full schedule or confirmed personal admission.

### Public transport and return planning

- Both Malta Public Transport’s Route 186 page and its latest-service-updates page show the 17 October notice at **19:00–00:00**, ending around midnight on 18 October. A separate older **20:00–00:00** notice ends around 21 April; it is not a competing October window. The prior 19:00–24:00 “union” interpretation was a misread and is not used.
- The October notice says stops Gholja 2 through Targa toward Buġibba will not be served. MPT publishes no replacement path and does not state how a specific Stadium trip or onward Qawra connection is affected. The “weekly on Friday, Saturday” phrase does not establish a 16 October diversion and leaves later recurrence unclear.
- One static Route 186 variant lists a **20:53** departure from Stadium stop 2194 toward Buġibba. That return direction does not list an Il-Qawra stop, so a journey using that particular leg needs a separately checked onward option. This does **not** establish that every public-bus return requires a second boarding, that 20:53 is the network’s last bus, or that no later/alternative service works.
- Route 214 lists Qawra stop 952 and Ta’ Qali Qali 2 stop 2542 on its static route page. TQ1 is another possibility to monitor, but its page showed “Timetable not available!” and no TWC-specific service was found. These are route-level candidates, not a saved trip. The interactive MPT planner extraction yielded instructions, not a date/time-specific journey; the attendee gate, stop-to-gate walk, onward connections and safe walking sections remain unverified.
- A taxi or ride-hailing quote was not obtained. AX ODYCY says Guest Relations can arrange taxis through a firm offering fixed charges, but publishes no price. Taxi/ride-hailing and the hotel’s arrangement are fallbacks if no suitable bus is found or if the traveler chooses one; no taxi is established as necessary.

### Fares and taxi tariffs

MPT publishes day-route singles of **€2.00 winter / €2.50 summer**, plus fare cards and other route prices. Its only dated winter single-fare period shown is **19 October 2025–13 June 2026**. The applicable fare for 13–19 October 2026 is unpublished; neither single rate is assigned to the trip or treated as a quote. Card products are comparison figures, not a purchase recommendation.

Transport Malta’s published maximum taxi meter tariff page says **last updated 6 April 2022**. The guide’s distance figures are arithmetic using assumed distances, not quotes; the road distance from Qawra to the venue was not measured. Ride-hailing prices are dynamic and are not governed by that meter schedule.

### Hotel and U.S.-traveler guidance

AX ODYCY’s own pages provide hotel facilities/contact details and the option to arrange taxis at fixed charges. They do not confirm the traveler’s room, rate, meal plan, booking, check-in/out clock times or taxi price. The guide also records the hotel’s room-name distinction, guest-room sockets, doctor/pharmacy information and tipping statement without converting them into traveler-specific booking facts.

The 2026 MTA guidelines PDF gives a €1.50 nightly contribution for eligible guests aged 18+ and a €22.50 per-person cap. The MTA webpage separately says contribution is chargeable on total nights that “exceeded fifteen (15) nights.” The two official sources do not expressly reconcile treatment of a short stay. Six nights × €1.50 is conditional arithmetic only; it is neither a confirmed charge nor an exemption. Use the hotel invoice and keep OQ-25 open. The official EU EES position and secondary reporting on Malta’s enforcement also remain unreconciled; the guide recommends allowing generous border time without claiming a local queue or enforcement status.

### Sports radio

The dedicated radio page distinguishes official station schedules, technical DAB+ directories, named-match carriage, physical reception and internet streams. NET FM’s recurring programme grid is not a dated promise of a named match. BBC *Sportsworld* is general live sport; BBC UK Premier League listings do not prove Malta frequency/carriage or BBC Sounds access from Malta. The “Sports Channel” block/identity remains a scan lead. No physical FM/DAB+ scan, Malta named-match carriage confirmation or stream-access test was performed.

### Food, activities and review-platform coverage

Restaurant/café, gaming, landmark and trip-window event records remain available with per-record caveats. Some Google Maps/Reviews, TripAdvisor and Reddit/search views were accessible. Direct Yelp, Instagram, TikTok, Facebook and X access was blocked or limited in the recorded checks. The sample is not comprehensive and is not presented as a universal ranking. The Ħamrun Chocolate Festival date was taken from a dated search-index snapshot of the organizer’s Facebook page; its hours/free-entry details come from a secondary guide and remain provisional.

## Cumulative verification passes

1. **Pass 1 — repository, plan and integration.** Reviewed the existing schema/site and `docs/PLAN.md` before topic corrections. Integrated the upstream event guide, hotel additions and later team-field correction while preserving sourced trip-guide content. Reconciled shared pages, JSON, sources and open questions on the fixed Arena branch.
2. **Pass 2 — evidence and requirements review.** Re-read the MPT Route 186 and latest-updates pages, the MPT fares page, Eventbrite listing text, MTA service page and guideline PDF. Corrected the Route 186 19:00/20:00 conflation, removed the unsupported union, kept Route 214/TQ1 as candidates, withdrew the claim that a taxi or second bus is mandatory network-wide, qualified ticket-price evidence, recorded the Virtus.pro/NIP update with its source limits, and reopened the MTA short-stay question. Reviewed radio, travel-practicality, activity and platform-coverage caveats.
3. **Pass 3 — consistency and regression.** Searched current pages/data/docs for categorical “no bus”/taxi claims, stale diversion windows and resolved MTA language; aligned overview, transport, event, expense and evidence records; checked source-log coverage and exact data schema; and reran JavaScript, responsive, accessibility, navigation, data-render and planner tests.

## Local validation results

- `python3 scripts/validate_site.py` — **PASS**: 7 JSON files / 176 exact-schema records / 307 unique record URLs in `docs/SOURCES.md` / 15 HTML pages / 175 link attributes / 9 shared navigation destinations / 25 expense rows.
- `python3 scripts/check_javascript.py` — **PASS**.
- `node --check js/site.js` — **PASS**.
- `npm test` — **PASS, 11/11 Playwright tests**, including 320/360/768/1440 px layouts, axe accessibility checks, topic data/render parity, navigation, planner persistence/CSV/error states and itinerary quick-fill.
- `git diff --check` — **PASS** after conflict resolution and final report edits.

These checks cover repository structure and local behavior. They do not verify external-link liveness, ticket inventory, a live dated transit route, taxi availability, physical radio reception, named-match carriage, every browser/device or exhaustive assistive-technology compatibility.

## Remaining limitations and next-session work

1. Ask Hotspawn/Thunderpick to confirm the attendee gate, the traveler’s own reservation, current ticket price/availability, per-day validity/scanning, Saturday/Sunday agenda and the 22:00 vs 22:30 finish discrepancy.
2. Once the gate and expected finish are known, run MPT’s dated planner for each event date and both directions. Compare Route 186, Route 214, other live routes and any TQ announcement; record stop sides, walking sections and the 17 October diversion effect.
3. Confirm the day-route single fare for 13–19 October. Obtain a current live taxi/ride-hailing or hotel fixed-charge quote only if the traveler wants one or the planner shows no suitable public route.
4. Ask MTA/AX ODYCY to clarify the short-stay contribution wording, and follow an authoritative Malta source for EES enforcement. Use the hotel invoice for any actual charge.
5. Refresh volatile venue hours, menus, ticket availability, weather and bus notices close to travel. Scan FM/DAB+ at the hotel/event area and ask stations directly about named-match carriage.
6. Fill the expense planner only after itinerary, booking, party and actual-cost inputs arrive; review the quick-fill preview and export a CSV backup.

## Delivery boundary

PR #42, PR #43, PR #45 and PR #44 are upstream merged changes incorporated in the current base. This report records the local validation and audit snapshot for the fixed session branch. The final delivery response reports the observed state of this branch’s PR, checks, merge and any Pages deployment only after direct GitHub inspection; no later GitHub outcome is inferred here.
