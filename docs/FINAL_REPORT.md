# Malta Trip Guide — final report (11 October 2026)

**Guide:** https://buffedlizard55-lab.github.io/MALTASUPPLEMENTAL/
**Delivery PR:** https://github.com/buffedlizard55-lab/MALTASUPPLEMENTAL/pull/31
**Branch:** `arena/3a5297d2-maltasupplemental`
**Traveler-supplied planning inputs:** AX ODYCY, Qawra Coast Road, Qawra SPB 1902, Deluxe Sea-View room; 13–19 October 2026; event destination/name “BLAST Arena Studios, Attard.” These details do not independently confirm a reservation, room allocation, ticket, spectator access, exact TWC entrance, or door-to-door itinerary.

## Executive summary

The static, mobile-friendly site includes an overview, six data-backed topic pages, shared navigation, source/open-question/status reporting, and a blank-by-default expense planner. Six canonical JSON datasets contain **128 exact-schema records**: transport 16, food 29, activities/events 32, everyday guidance 15, radio 11, and expenses 25. The canonical schema has exactly 13 record fields, including the exact key `price range`; the current source-type enum is `official`, `map`, `review`, and `social`. Records expose source, check date, confidence, and limitations; page renderers use the data rather than recreating facts.

The refreshed offline validator reports **205 unique record URLs** in `docs/SOURCES.md`, 15 HTML pages, 117 link attributes, 8 shared-navigation destinations, and all 25 expense rows wired. The latest local CI-style run passed all nine Playwright tests, including viewport/accessibility checks at 360, 768, and 1440 pixels. The guide is a dated planning snapshot, not a booking, admission, service, radio-reception, or external-link guarantee.

**Complete fresh line-by-line external verification of every retained historical claim and comprehensive all-platform review coverage remain incomplete.** Unresolved facts are not presented as confirmed; the detailed question list is in [`OPEN_QUESTIONS.md`](OPEN_QUESTIONS.md).

## Deliverables and evidence boundaries

### A · Getting around — 16 records

The transport page and data compare public bus, taxi/ride-hailing, rental car, ferry and other island connections by convenience, published price/value, and feasibility. MPT Route 186 lists Qawra stop 952 toward Ta’ Qali Stadium 6227; the return uses opposite-side Stadium stop 2194 toward Buġibba, not the Qawra seafront. The checked timetable shows a last listed 20:53 departure from Stadium and Buġibba Bay 1 arrival at 21:27. These are static route-table entries, not a dated hotel connection. Route 214 is an alternative to compare; MPT also lists a 17 October evening diversion. Airport Direct TD1 lists Il-Qawra Arznell stop 950 in both timetable directions, with route-level times; the flight-specific departure and walk to AX ODYCY still need a planner check. The current mode-comparison record does not treat an old third-party approximately €25 airport-taxi figure as an official fare. October 2026 single-fare validity, TWC entrance/walk, exact outward/return route and diversion impact remain open.

### B · Food and cafés — 29 records

The shortlist includes AX ODYCY/on-property, Qawra-area and wider-area options, with current operator/menu facts separated from dated Maps/review/social snapshots. Ratings are not blended into a universal ranking. Reported closures, profile mismatches, conflicting hours, stale menus, and inaccessible-platform results remain qualified; current menus, hours, representative meal totals and availability are not assumed.

### C · Activities, landmarks and events — 32 records

The page covers attractions, recreation/gaming leads, landmarks and dated event listings. It includes the user-supplied base-hotel record, while booking terms remain unknown. The official Thunderpick page gives the overall event window and Malta as the location; a Thunderpick-issued release and separate-event BLAST/venue listings provide venue-area context only. No source confirms the traveler’s ticket, public spectator access, TWC-specific entrance/gate, daily public door/finish times or exact event itinerary. Ticket inventory, event conflicts, some opening-hour conflicts, gaming-venue status and access details remain caveated.

### D · Everyday life — 15 records

Power, language, currency, entry/EES/ETIAS, mobile options, safety/health and weather are sourced and qualified for date and traveler circumstances. Government of Malta and U.S. State Department sources support emergency number 112. Passport, insurance, device/carrier, medicines/customs and other personal advice is not individualized. The recorded forecast does not cover 18–19 October.

### E · Malta sports radio — 11 records

The page distinguishes an over-the-air service listing, an official programme schedule, local reception, online streaming, fixture data, and named-match carriage. The Broadcasting Authority lists NET FM at FM 101 MHz; its recurring grid is not a dated match lineup. Malta’s DAB+ directory lists BBC World Service, Rai Radio Uno and Radio Sportiva. WorldDAB lists BBC World Service on block 6A at 181.936 MHz; this technical directory is not an indoor signal test.

Official BBC episode JSON gives Sportsworld first-broadcast times with +01:00 offsets on 17 and 18 October, corresponding to 15:06 and 16:06 Malta time. The programme is general live sport, not a named-match listing; the 11 October EPL episode is precedent only. Six BBC Radio 5 Live / 5 Sports Extra episode records list UK EPL commentary during 17–18 October. Two upcoming-page service labels differ from their JSON parent-service fields, so the lineup should be rechecked. These UK records do not establish Malta reception, BBC Sounds access, BBC World Service carriage, or a Maltese frequency. Rai’s official weekend football programme has no checked 17–18 October running order. No current AM/MW sports schedule or named carriage of the TWC, Gżira–Mosta, Rolex Middle Sea Race, or a particular EPL/Serie A match was confirmed.

Kalshi EPL/Serie A category pages were checked for visible trip-window market timing and overlap. Such a category/fixture listing is not radio evidence, a rights statement, or confirmation of Malta trading eligibility. Generic “Sports Channel” and third-party TalkSPORT/6C references remain unverified scan leads. No physical FM/DAB+ receiver scan was available at AX ODYCY or the event area.

### F · Expense planner — 25 blank-by-default rows

The planner provides 18 core trip categories plus seven optional daily templates for 13–19 October, editable euro budget/actual values, notes, totals/difference, browser-local autosave, CSV export, and reset. Nothing pre-fills a flight, hotel booking/rate, traveler count, ticket, itinerary, tax amount, or reimbursement. Daily and aggregate rows must not be double-counted. The MTA rate/cap is sourced, but the separate “15-night threshold” wording is ambiguous (OQ-25); any six-night arithmetic is conditional and not a personal charge.

## Three cumulative verification passes

1. **Implementation and source pass — passed.** `python3 scripts/validate_site.py` reports 6 JSON files / 128 exact-schema records / 205 unique record URLs / 15 HTML pages / 117 link attributes / 8 navigation destinations / 25 planner rows. `python3 scripts/check_javascript.py` and `node --check js/site.js` pass. All six data files parse as JSON.
2. **Requirements and evidence pass — passed with limitations recorded.** The page/data claims were checked for sources, dates, confidence, contradictions, and open questions. Transport compares mode convenience/price/value/feasibility without promising an event-day hotel connection. Radio sources are not conflated with fixture lists, internet streams, or event schedules. Review/social access limitations and unresolved facts remain visible. This is not a complete new line-by-line re-verification of all older claims.
3. **Integration, responsive and functional pass — passed with limits.** `npm ci && npm test` passed **9/9 Playwright tests** (about 1 minute): active-page rendering and axe checks at 360/768/1440 px, responsive overflow, data/render parity, filters, mobile navigation/deep links, expense defaults/totals/persistence/CSV/reset, invalid input, storage denial/corruption, and failed-fetch behavior. A fresh manual graphical screenshot and physical-device test were not available; responsive CSS breakpoints at 900/620/560 px were reviewed in the preceding audit. The validator checks local wiring, not external URL liveness.

After the final documentation conflict commit, rerun `git diff --check` and the local HTTP endpoint smoke test, then review the rebased PR’s final GitHub checks and mergeability. No external-link crawler was run.

## Platform, date and source limitations

A small number of Google Maps profile views and dated TripAdvisor snapshots informed parts of the shortlist. Direct/retry access to Yelp, Instagram, TikTok, Facebook, X and Reddit was blocked or limited; one batch returned five HTTP 403 responses without reliable endpoint attribution. Text from an official X post was available, but its attached opening-day schedule image was not readable. No inaccessible review, post, or schedule content was inferred. Platform coverage is not comprehensive; see [`SOURCES.md`](SOURCES.md) and each topic page.

Primary and supporting URLs, access dates, and source limitations are recorded in [`SOURCES.md`](SOURCES.md). The claim-level refresh boundary is in [`AUDIT_2026-10-11.md`](AUDIT_2026-10-11.md); cross-workstream discoveries are in [`HANDOFF.md`](HANDOFF.md); unresolved claims and proposed checks are in [`OPEN_QUESTIONS.md`](OPEN_QUESTIONS.md).

## Remaining traveler/organizer checks

1. Confirm TWC spectator eligibility, ticket, exact attendee entrance/pin, and daily public arrival/finish times with the organizer; do not borrow access instructions from another BLAST event.
2. Enter the confirmed hotel and event location/time into MPT’s live planner for each event date; verify stop sides, walks, Route 186 diversion effects, onward Qawra connection, TD1 flight timing, and current fare/card terms. Keep a live taxi/ride-hailing quote for an unsuitable late return.
3. Recheck NET FM, Rai, Radio Sportiva and BBC schedules close to air; scan FM/DAB+ at the actual hotel/event locations; verify named-match selection, receiver band, and Malta stream territory separately.
4. Confirm the hotel voucher/invoice, check-in/out, meal plan, nights/guest ages, flights, traveler count, actual prices and prepaid items before completing the planner. Ask AX ODYCY/MTA about the “15-night” language.
5. Verify passport/ETIAS status, phone/carrier/device compatibility, insurance, and medical/customs needs for the traveler’s circumstances; refresh the 18–19 October forecast and volatile operator/event information.
6. Broaden review/social checks when accessible and recheck all volatile business status, opening hours, menus, and ticket availability before visiting.

## Rebase and delivery state

The PR #31 branch reconciles later `origin/main` changes at `81930be`, including the AX ODYCY base-hotel record, the operator night-route notice, seven optional daily expense templates, updated activity/transport/emergency/market evidence, and the upstream browser-test suite. Outdated/duplicate upstream records were not blindly restored where the current main branch intentionally removed them. This rebase preserves both the current main implementation and the trip-specific sourced findings.

PR #31 remains **open and unmerged** until the rebased branch is pushed and GitHub checks/diff/mergeability are reviewed. Use only `arena/3a5297d2-maltasupplemental` for the push and merge PR #31 only when safe. Existing Pages publication targets the `main` root; a successful static build does not certify external links, admission, transit on the travel date, radio reception, or visual behavior on the traveler’s device.
