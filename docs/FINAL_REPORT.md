# Final report — Malta Trip Guide

**Planning window:** 13–19 October 2026
**Hotel supplied by traveler:** AX ODYCY Malta, Qawra Coast Road, Qawra SPB 1902
**Event location supplied by traveler:** BLAST Arena Studios, Attard
**Research snapshot:** see the individual access dates in [`SOURCES.md`](SOURCES.md)

## Executive summary

The site is a mobile-friendly, static Malta tourism and recreation guide with an overview, six topic pages, shared navigation, an evidence dashboard, and an editable expense planner. Six JSON files hold **85 common-schema records** with source type, check date, confidence, and caveats. Unknowns are stated rather than guessed.

The traveler supplied the trip dates and destinations, not the hotel booking, room category, flights, party size, arrival/departure times, or tournament attendance. Six nights applies only if check-in is 13 October and check-out is 19 October. The guide does not assume that booking condition, event access, or an itinerary.

## Verified deliverables and research findings

- **Getting around (13 records):** compares airport, bus, taxi/ride-hailing, car-hire, ferry, and local transport options. Route 186 is a leading Qawra–Ta’ Qali corridor candidate and Route 214 is listed as an alternative to compare. A date-specific MPT itinerary to the event entrance, diversion impact, fare validity, and late return still require checking in the operator planner; the page is not a door-to-door guarantee.
- **Food and cafés (15 records):** includes AX ODYCY/on-property options, Qawra-area venues, selected wider-area ideas, local-food context, and separately labelled map/review/community observations. Platform ratings are not blended. Reported closures and conflicting hours remain caveated; current menus, hours, and representative meal costs are not assumed.
- **Activities, landmarks, and events (20 records):** covers recreation and gaming leads, Malta attractions, and dated events relevant to the trip. Organizer/event dates are kept distinct from spectator access, ticket terms, opening times, or guaranteed availability. Conflicts such as the Heritage Malta picnic listing and site-closure notice remain open.
- **Everyday travel (15 records):** covers entry pointers, EES/ETIAS, currency/cards, language, electricity, mobile connectivity, emergency/health, safety, weather, and practical U.S.-traveler considerations. Passport, device, carrier, itinerary, and medicine-dependent advice is conditional.
- **Sports radio (4 records):** the Broadcasting Authority lists NET FM at FM 101 MHz; NET FM’s official grid shows recurring weekend sports programming, not a trip-week guarantee. Digi B’s directory lists Radio Sportiva and BBC World Service on DAB+, but the current local block/frequency and reception at Qawra are unverified. BBC programme listings show Sportsworld on 17 and 18 October; they do not name a particular match. No current AM/MW sports service or named-event radio carriage was confirmed. A third-party TalkSPORT/6C claim is explicitly unverified.
- **Expense planner (18 blank-by-default categories):** editable EUR budget/actual fields, notes, totals and difference, browser-local autosave, CSV export, source links, and reset are available. The starter has no assumed itinerary, amounts, booking costs, event costs, reimbursement, tax, tip, or exchange rate; blank does not mean free.

The source register, unresolved questions, workstream status, and cross-topic handoffs are in [`SOURCES.md`](SOURCES.md), [`OPEN_QUESTIONS.md`](OPEN_QUESTIONS.md), [`STATUS.md`](STATUS.md), and [`HANDOFF.md`](HANDOFF.md).

## Three cumulative review passes

1. **Implementation and source pass — passed with open questions.** All six data files passed the required common-field and allowed-enum checks. The integrated build reports 85 records, 15 root HTML pages, 79 checked link attributes, eight shared navigation destinations, and all 18 planner rows wired. Page/data references and inline/shared JavaScript syntax were checked.
2. **Independent requirements and evidence pass — passed with limitations recorded.** Reviewed the six requested topics, supplied trip facts, event-vs-access distinction, date/frequency/time-zone claims, source type/confidence, and cross-workstream notes. Inaccessible or limited Google/review/social endpoints and unresolved operator or event details are described in the source and open-question logs. Social-platform non-access is not treated as evidence.
3. **Integration and interaction pass — passed; visual comparison remains limited.** Local HTTP smoke checks returned 200 for the overview, topic pages, data, evidence pages, and legacy notice URLs. A headless DOM run exercised the five record-rendered topics and the expense page; CSS responsive breakpoints and navigation were reviewed. A full desktop/mobile browser screenshot and real-device accessibility check were not available in this environment.

Repeat the repository's offline gate with `python3 scripts/validate_site.py`. It checks the local schema, internal paths, navigation destinations, and expense-row wiring; it is not an external URL crawler.

## Open questions and traveler actions

1. Confirm the hotel reservation, actual check-in/out, room details, booking total, and separately billed charges.
2. Provide flight details, airports, baggage, arrival/departure times, and traveler count before finalizing transfers or total costs.
3. Confirm whether/when the traveler will attend the event, ticket/access terms, session times, and the event-specific public entrance. Then run the official Malta Public Transport planner for the outbound and late-return trip, including the 17 October notice.
4. Recheck 2026/27 fares/cards, live venue hours/menus, event availability, attraction access, and weather before travel.
5. Verify the applicable passport/Schengen and ETIAS status, mobile plan/device compatibility, and medication-specific requirements with the relevant authority/provider.
6. Recheck official radio schedules and DAB+ channel details close to the broadcasts; reception at the hotel has not been tested.

See [`OPEN_QUESTIONS.md`](OPEN_QUESTIONS.md) for the full list, evidence gaps, and proposed next checks.

## Limitations

- Information is a dated research snapshot and can change. The maintained source log gives claim-specific access dates and identifies third-party or non-official evidence.
- Some requested review/social services were blocked or only partially queryable. Google Maps and platform snapshots do not establish current operator hours or prices.
- The offline link checker does not guarantee external-site availability. No automatic crawler of every external source was run.
- A headless DOM simulation is not a substitute for visual review on real desktop/mobile browsers or assistive technologies.
- GitHub Pages is configured to publish the repository root from `main`. The Pages API reported the current `main` build for merge commit `87bca74` as `built`; that confirms the upstream build only, not deployment of this PR's different files or actual browser/device rendering.
- This guide is a planning aid, not a booking, dispatch, immigration, tax, legal, medical, or event-access guarantee.
