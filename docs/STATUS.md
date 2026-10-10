# Malta guide — work status

Last updated: 2026-10-09 (UTC)

## Overall

- [x] Repository and legacy-site review completed.
- [x] `docs/PLAN.md` defines the serial work sequence, isolated topic ownership, and required field names.
- [x] Shared evidence and coordination files created before topic-page work.
- [x] A — Transport data/page (route 186 corridor, airport options, fare caveats, live-planner and taxi fallback; date-specific journey/return remain open).
- [x] B — Food and cafés data/page (official menus, dated examples, review-source caveats and current Luzzu closure recorded; hotel meal plan remains unknown).
- [x] C — Gaming, landmarks, activities and dated events data/page (TWC spectator access and CDM entry timing remain unresolved).
- [x] D — U.S. traveler practicalities data/page (ETIAS launch status, individual entry eligibility, carrier/insurance and personal access needs remain open).
- [x] E — Official live radio sports data/page (Malta carriage/stream access for BBC Radio 5 Live and match selection in Sportsworld remain unresolved).
- [x] F — Expense planner data/page (editable browser-only calculator; no fare, room, flight, FX or ticket purchase is assumed).
- [x] G — Responsive shell, executive summary, integration, redirects and README.
- [x] Integrated data/page consistency and link checks.
- [x] Pass 1 — factual/source and scope review.
- [x] Pass 2 — usability, completeness and data/page consistency review.
- [x] Pass 3 — responsive/accessibility/bug review (CSS/DOM review and smoke tests; no graphical browser automation is installed in the workspace).


## Current verified anchors

- Malta Tourism Authority says the accommodation environmental contribution effective 1 Jul 2026 is €1.50 per night per guest aged 18+, capped at €22.50/person/visit and itemized separately; confirm the hotel invoice and any third-party coverage.

- Trip brief: AX ODYCY, Deluxe sea-view room, Qawra Coast Road, Qawra SPB 1902, 13–19 October 2026. This is the user's requested scenario, not proof of a hotel reservation.
- Thunderpick's official schedule distinguishes its wider final-stage window (12–19 Oct), media day (13 Oct), group stage (14–16 Oct), playoffs (17–18 Oct), and departure day (19 Oct).
- BLAST's guide for a different 2026 tournament publishes the BLAST Arena Studios/MFCC address at Ta' Qali, but Thunderpick's page itself says only Malta (LAN); TWC public access, ticketing, door times and exact venue remain unconfirmed.
- MPT's current Route 186 timetable shows service every 30 minutes, including Qawra stop 952 (published snapshot 06:10–21:38) and directional Ta' Qali Stadium stops 2194 / 6227. The normal return toward Buġibba runs via St Paul's Bay/Buġibba, not Qawra seafront; the current listing's final arrival at Bugibba Bay 1 is 21:26. These are static timetable details, not a trip-day guarantee. BLAST's address is from a separate event; Thunderpick-specific venue/access, the correct stop/walk and the actual return remain unconfirmed.
- MPT's current service-update page lists a Route 186 detour toward Buġibba on Friday/Saturday evenings from 19:00 to midnight starting 17 Oct; Gholja 2 through Targa are not served. Its impact on the exact Ta' Qali return stop is unresolved; recheck before travel.
- Official MPT fare material lists €2.00 winter and €2.50 summer day-route fares and a two-hour validity; the public page does not establish the 2026 October changeover date. Do not assign an unverified price to each trip date.
- Aquarium ticket page checked 9 Oct shows adult online/door rates and the current after-16:00 online discount; recheck before purchase.
- Malta Met Office forecast checked 9 Oct reached 15 Oct only; it did not forecast the last four trip days in that snapshot.
- BBC Radio 5 Live official schedule lists Premier League commentary on 17 and 18 Oct; these UK Radio 5 services are not on the Malta DAB+ channel list, and Malta online access remains unconfirmed.
- BBC World Service Sportsworld has scheduled episodes on 17 and 18 Oct; Malta's DAB+ channel listing includes BBC World Service. BBC Radio 5 Sports Extra also lists football coverage, but Malta carriage/stream availability is not confirmed.

## Integrated review passes (2026-10-09)

- **Pass 1 — facts, sources and scope:** checked 64 topic records across six JSON files against the shared keys, source type, confidence and date rules; verified every record's primary URL and every URL cited in record notes is represented in the source log. Key caveats remain visible for event access, transport, October fares, ticket stock, entry status, radio carriage and personal costs.
- **Pass 2 — completeness, usability and consistency:** confirmed every page data filter matches its JSON IDs, every local file/anchor target resolves (including legacy redirects), and the published sources page renders the 147 claim-level source entries and all 27 unresolved questions. Root overview covers the requested topics and gives next actions.
- **Pass 3 — responsive, accessibility and behavior:** reviewed desktop/mobile CSS breakpoints, semantic sections, skip links, nav controls, labels, `aria-*` targets, and duplicate IDs; `node --check` passed for shared and inline scripts. Expense-calculator smoke test passed (unknown age is not assumed, fare ranges calculate, USD appears only for a user-entered rate). HTTP smoke checks returned 200 for the site, topic pages, data, CSS, JS and documentation. The sandbox has no installed graphical browser automation, so pixel-level desktop/mobile rendering was not automated; the live preview is available for visual review.

## Coordination

The Arena checkout is fixed to `arena/a15d87d4-maltasupplemental`.  No parallel branch/agent facility is available in this workspace, so streams will be completed serially within the ownership boundaries in `docs/PLAN.md`. Cross-topic facts and integration dependencies go in `docs/HANDOFF.md`.