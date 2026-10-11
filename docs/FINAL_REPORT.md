# Final audit report — Malta trip guide

**Audit date:** 11 October 2026 (UTC)
**Session branch:** `arena/cc913a9b-maltasupplemental`
**Starting revision:** `b307c51`; the session fetched and integrated `origin/main` at `5cdea689` (PR #42) while work was in progress.

## Summary

The repository now contains the mobile-friendly, static HTML/CSS/JavaScript guide for the traveler-supplied 13–19 October 2026 stay at AX ODYCY in Qawra and the supplied Thunderpick World Championship destination at BLAST Arena Studios, Attard. It includes separate pages for transport, food, activities/sights/events, practical U.S.-traveler guidance, Malta sports radio, expenses, and the CS2 event; each topic uses canonical JSON records and traceable source notes.

The expense planner has 18 core categories plus seven optional daily rows. It starts blank, supports itinerary quick-fill preview that fills only blank fields, browser-local autosave, CSV export and reset. No hotel cost, flight, ticket purchase, party size, ride count, reimbursement or personal spend is assumed.

The event guide from merged PR #42 was retained and re-audited rather than duplicated. The session’s principal correction is the Route 186 notice reading: the current October notice is 19:00–00:00 on both MPT pages. A separate older 20:00–00:00 notice ends around 21 April and is not a conflicting October window.

This is a sourced planning aid—not a booking, admission, fare, service, live availability, trip itinerary, radio reception or event-carriage guarantee.

## Material findings and limits

### Thunderpick World Championship / access and schedule

A Hotspawn/Eventbrite listing read on 11 October identifies BLAST Arena Studios Malta, MFCC South Gate National Stadium, ATD 4000 Attard, and map coordinates 35.8957343, 14.4168839 for this event. It advertises in-person attendance for ages 18+ and shows a live registration page. HLTV reported that tickets were available free; the extracted Eventbrite page did not show a price table, so confirm the total at checkout. No ticket was purchased or held by this project, and a listing does not establish the traveler’s reservation, current inventory, per-day validity/scanning, or guaranteed admission.

The Eventbrite agenda shows check-in at 09:30 and games at 10:30 on 14 and 15 October, with each day listed to 22:30; 16 October is listed 14:00–21:00, with check-in at 14:00 and games at 15:00. Its general header says 09:30–22:00, so exact finishes should be reconfirmed. The 17–18 October agenda rows and FAQ answers were not visible to the extractor. The attendee gate, parking, on-site food and ticket transfer/validity remain open. Official and third-party bracket sources support some match clocks in Malta time, but the organizer still says to stay tuned for its detailed match schedule; treat non-organizer match times as planning estimates. Virtus.pro’s reported replacement by Ninjas in Pyjamas is not yet reflected on the organizer’s own pages.

### Public transport and event return

- A single static Route 186 variant lists a 20:53 departure from Stadium stop 2194 toward Buġibba. It precedes some visible event finishes and flags a return risk; it is **not** the whole network timetable and does not prove that no later bus exists.
- Route 186’s Buġibba-bound stop chain does not list an Il-Qawra stop. An onward service or a separately checked walk may be needed if using that particular route; neither a date-specific connection nor safe walking sections were verified.
- MPT’s static Route 214 page lists Qawra stop 952 and Ta’ Qali Qali 2 stop 2542 on the same route. This is a promising route-level candidate to test, not a verified journey or proof that a chosen event-time trip serves both stops.
- MPT lists TQ1–TQ4 special event services, and a published TQ1 corridor includes Qawra. The TQ1 timetable displayed “Timetable not available!” and no TWC-specific service was found. Monitor the operator’s updates; do not reuse times from a different 2023 event.
- **Route 186 diversion correction:** a fresh 11 October read of both MPT’s Route 186 page and latest-service-updates page shows the 17 October notice at **19:00–00:00**, ending 18 October at approximately midnight. The separate 20:00–00:00 notice ends around 21 April. The earlier “two pages differ; use their 19:00–24:00 union” wording was a misread and has been removed. The notice omits stops Gholja 2 through Targa toward Buġibba but publishes no replacement path and does not establish the effect on a particular Stadium departure or Qawra connection. “Weekly on Friday, Saturday” alongside the 17 October start and 18 October end leaves later recurrence unclear, but does not establish a diversion on Friday 16 October.
- MPT’s fare page lists €2.50 summer / €2.00 winter day-route singles; its stated winter validity ends 13 June 2026. No October 2026 single-fare season was verified. The figures remain comparisons, not a date-specific fare or planner default.
- Transport Malta publishes maximum white-taxi meter rates, but its page footer says last updated 6 April 2022. The guide’s worked distance caps are arithmetic at assumed distances, not current quotes; road distance to the venue was not measured. Compare a current fare/ride-hailing quote only as a fallback if the planner offers no suitable public route.

No date/time-specific end-to-end bus journey was verified: the interactive MPT planner yielded instructions, not a result, and the confirmed attendee gate is still unknown. Recheck all routes, stops and walks in the dated planner once the traveler has that gate and the event finish.

### Sports radio

The separate radio section distinguishes local FM/DAB+ directory evidence, station programme grids, named-match carriage, physical reception and internet streams. Radio in Malta labels a DAB+ “Sports Channel (Talk Sport)” listing on 6C; 2025 scanner directories also point to 6C, while WorldDAB lists a generic sports service on 12A and the local operator directory lists no sports service. These are tuning leads—not verified service identity, current reception at AX ODYCY, or match commentary. No receiver scan was possible.

Official BBC episode records name seven UK Premier League commentaries on 17–18 October, including Bournemouth–Sunderland on 5 Sports Extra 2. That is UK schedule evidence, not Malta FM/DAB+ carriage, BBC World Service output or BBC Sounds access. NET FM’s “Hits & Score” and Rai’s recurring weekend programmes are general programme-grid evidence, not named-match guarantees. The Thunderpick online streams are described separately and are not radio broadcasts.

### Food, activities and research-platform coverage

The existing food, café, gaming, recreation, landmark and dated-event records remain available with per-record source dates and caveats. Some Google Maps/Reviews, TripAdvisor and Reddit/search snapshots were accessible. Direct Yelp, Instagram, TikTok, Facebook and X access was blocked or limited; a Facebook-sourced festival date came from a dated search-index snapshot rather than a direct page read. The accessible sample is not comprehensive and is not presented as a universal ranking. Recheck volatile hours, menus, closures, prices and ticket availability before visiting.

### U.S.-traveler essentials

The everyday guide covers Type G / 230 V / 50 Hz power, emergency contacts, money/phone basics, entry and customs pointers, health/safety, language and trip-date weather. It keeps traveler-specific entry, carrier, device and insurance questions open. The official EU EES page and secondary reporting about Malta’s implementation do not reconcile; the site preserves the conflict and recommends generous border time rather than claiming a local queue or enforcement status. MTA’s 2026 guideline lists €1.50 per eligible night, capped at €22.50 per person, while its current service page separately refers to nights that “exceeded fifteen (15) nights”; the official texts do not explain the short-stay treatment. A six-night €9 calculation is conditional arithmetic only—use the hotel invoice.

## Cumulative verification passes

1. **Implementation pass:** inspected the repository before topic work, preserved and updated `docs/PLAN.md`, checked the seven topic datasets against the exact 13-field schema, reconciled the event page/navigation, verified page/data/source-log wiring, and rechecked the blank-by-default planner and browser behaviors.
2. **Requirements and evidence pass:** compared current-facing page and record claims with dated primary-source reads. Corrected the Route 186 false conflict/union, distinguished the expired April notice, added Route 214 as a qualified route-level candidate, and softened taxi/return certainty. Ticket, fare, stop/gate, schedule, platform-access and radio-reception uncertainties remain explicit.
3. **Final audit pass:** searched for superseded route/return claims, reconciled upstream PR #42 work on the fixed branch, checked source-log coverage, reviewed the diff, and reran schema/JavaScript/browser, mobile-layout and accessibility validation. The exact local gate results are below.

## Validation results

- `python3 scripts/validate_site.py` — **PASS**: 7 JSON files / 175 exact-schema records / 305 unique record URLs logged in `docs/SOURCES.md` / 15 HTML pages / 170 link attributes / 9 shared navigation destinations / 25 expense rows wired.
- `python3 scripts/check_javascript.py` — **PASS**.
- `node --check js/site.js` — **PASS**.
- `npm test` — **PASS**, 11/11 Playwright tests. Coverage includes 320/360/768/1440 px layouts, axe checks, navigation, canonical record rendering and expense-planner scenarios.
- `git diff --check` — **PASS**.

These checks cover repository structure and local behavior. They do not verify external-link liveness, current ticket inventory, a live dated transit journey, taxi availability, physical DAB+/FM reception, named-match carriage or facts hidden behind restricted platform content.

## Remaining limitations / next-session work

1. Ask Hotspawn/Thunderpick to confirm the attendee gate, ticket inventory/reservation, per-day validity/scanning, the 17–18 October agenda, and whether the 14–16 October 22:00/22:30 finish discrepancy is current.
2. With gate and expected finish times, run the MPT planner for each event date and both directions. Compare Route 186, Route 214, other live routes and any TQ event-service announcement; record stop sides and walking sections. Check the 17 October diversion effect. Get a live taxi/ride-hailing quote only if no safe, workable bus itinerary is returned.
3. Confirm the day-route single fare applicable on 13–19 October; do not assign either published seasonal rate without an effective date.
4. Scan FM and DAB+ at the hotel/event area, record actual block/service/audio/reception, and confirm named-match carriage with the station. Recheck BBC/Rai schedules and stream access close to broadcast.
5. Ask MTA/AX ODYCY to reconcile short-stay environmental-contribution wording; use the invoice for the expense planner. Follow up the EES implementation question with an authoritative Malta source.
6. Refresh accessible review platforms and volatile business/event details without implying comprehensive coverage. Populate planner values only after the traveler supplies itinerary, booking, party and actual spend inputs.

Claim-specific evidence and access dates are in `docs/SOURCES.md`; current open items are in `docs/OPEN_QUESTIONS.md`; cross-topic notes are in `docs/HANDOFF.md`; ownership and scope are in `docs/PLAN.md`.

## GitHub delivery snapshot

This report records the local audit candidate at its final local-validation gate. The final response reports the delivery PR, merge result and any observed Pages/CI status from direct GitHub checks; this file is a dated audit snapshot, not a live CI or deployment dashboard.
