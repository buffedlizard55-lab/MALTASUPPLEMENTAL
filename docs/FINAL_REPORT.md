# Final report — Malta Trip Companion

**Research snapshot:** 9 October 2026
**Trip window supplied for planning:** 13–19 October 2026
**Hotel supplied for planning:** AX ODYCY Malta, Qawra Coast Road, Qawra SPB 1902

## Executive summary

The repository now provides a focused, mobile-friendly static guide for the supplied Malta trip. It has six topic pages—transport, food and cafés, activities and sights, practical U.S.-traveler guidance, scheduled sports radio, and an editable expense planner—plus a concise overview and an evidence landing page. Structured records retain source links, source types, check dates, confidence labels and caveats. Unknown prices, hours, schedules, entry conditions and venue access are not guessed.

The trip window covers seven calendar dates. Six hotel nights applies only if the reservation is check-in on 13 October and check-out on 19 October. The user has not supplied the hotel booking confirmation/room type, flights, arrival/departure times, traveler count or intended tournament sessions. The planner therefore begins blank and does not assume any event attendance, reimbursement or third-party coverage.

## Verified deliverables

- **Transport:** eight source-linked records compare public transport, Airport Direct, taxi/rideshare and rental options. Route 186 is presented as a corridor to test, not a finalized door-to-door itinerary. The page flags the 17–18 October notice and requires date/time-specific operator-planner checks.
- **Food and cafés:** eight Qawra-area venue records include on-property dining and separate, dated review-platform snapshots. Ratings are not blended and no representative EUR meal cost is inferred.
- **Activities and sights:** 20 records cover attractions, dated event leads and gaming options. Spectator access, gaming walk-in terms and event conflicts remain visible where not confirmed.
- **Everyday travel:** 14 records link entry, money, phone, health, power, safety, weather and practical guidance to official or otherwise identified sources. Advice that depends on nationality, carrier or medicine is explicitly conditional.
- **Scheduled radio sport:** two official BBC World Service Sportsworld programme entries are recorded for 17 and 18 October, with Malta-local starts at 15:06 and 16:06. Their published 3h53 duration yields calculated ends at 18:59 and 19:59. Neither listing names a specific match; hotel DAB+ reception is untested.
- **Expense planner:** 18 optional price/unknown reference cards accompany four trip-level and 28 date-specific blank lines. Users can add custom entries, calculate quantity × unit cost, compare an optional budget limit, enter their own EUR-per-USD rate, save locally in the browser, export CSV and print. Reference prices are not included unless selected.
- **Evidence and maintenance:** source, open-question, handoff, schema, status and planning registers are maintained in `docs/`. Root compatibility URLs redirect to the current guide rather than presenting stale prize/legal pages or unsupported itinerary claims.

## Open questions and traveler-specific actions

1. Confirm the hotel reservation, actual check-in/out times, room details and booking total; six nights remains conditional on 13/19 October check-in/out.
2. Supply flight airports/numbers, baggage, arrival/departure times and traveler count before finalizing airport options or costs.
3. Confirm whether and when the traveler will attend the tournament, and obtain the event-specific entrance, ticket/access terms and session times. Then use the official MPT planner for the exact trip and return, especially around the 17–18 October route notice.
4. Recheck 2026/27 bus fare/card terms, supplier prices, venue hours, event availability and weather before travel. Restaurant records do not establish an average meal budget.
5. Recheck ETIAS immediately before departure; its 9 October status was not operating, while an older EU forecast placed a possible start in Q4 2026.
6. Confirm the traveler’s actual passport/Schengen history, mobile carrier plan and any medication-specific requirements with the relevant official sources.
7. Recheck BBC schedule changes and the local DAB+ channel list; bring a DAB+ capable receiver if relying on over-the-air radio and test reception on arrival.
8. Obtain organizer confirmation before relying on Heritage Malta’s Picnic listing, which conflicts with the current Borġ in-Nadur closure notice.

All 24 unresolved items and proposed evidence/actions are recorded in `docs/OPEN_QUESTIONS.md`.

## Limitations

- External source freshness is not guaranteed after the 9 October snapshot. The repository's offline verification script checks URL presence and internal structure, not whether external sites remain live.
- JSDOM exercised shared navigation, data rendering, search/filtering and expense interactions at a 390 px viewport; it is not a real-device visual/accessibility audit.
- The current source inventory flags direct-access failures and platform limitations. WorldDAB is an industry directory rather than the local DAB operator; hotel indoor radio reception has not been measured.
- No actual booking, flight itinerary, tournament ticket, attendance schedule, roaming plan, medicine list, exchange rate, taxes/tips or supplier quotes are inferred.
- GitHub Pages is configured to publish `main` from the repository root; the GitHub Pages API reported the post-merge build for `c4a33ec` as `built`. This confirms the build state, not the live browser rendering, external link liveness or real-device appearance; recheck after future content changes.
- This guide is a personal planning aid, not legal, tax, medical or immigration advice, a live dispatch service, or a guarantee of availability or access.

## Verification record

The three cumulative review passes are documented in `docs/STATUS.md`. Final local checks completed:

- 70 topic and price-reference records passed common-schema, allowed-enum, date, unique-ID, source URL/log and open-question reference checks.
- 101 unique source-log IDs and 24 open questions were recognized; trip-date weekdays, the conditional six-night calculation, 32 blank expense lines and radio duration arithmetic were checked.
- 112 local HTML links, fragments and assets resolved across root and topic pages; all legacy root routes were checked as redirects.
- JSDOM smoke tests passed for the overview, evidence page and all six topic pages, including responsive-menu state, data rendering, search/filter and expense math, local storage, price insertion, CSV action and reset.
- `node --check js/site.js`, CSS brace balance (114/114) and `git diff --check` passed.

Run `python3 scripts/verify_site.py` (or `python3 scripts/check_links.py`) from the repository root to repeat the offline integration gate. It does not replace outbound source checks or a device-level visual review.
