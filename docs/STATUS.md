# Malta guide — work status

Last updated: 2026-10-10 (UTC)

## Overall

- [x] Repository and legacy-site review completed; `docs/PLAN.md` recorded before topic work.
- [x] Shared folders, schema, source-log format, open-question register, status file and cross-topic handoff established.
- [x] A — Transport data/page: Route 186's published Qawra–Ta' Qali service, airport options, fare caveats, return path, detour and taxi fallback documented; the event-day itinerary remains open.
- [x] B — Food and cafés data/page: official menus, dated prices, review-source caveats and the current Luzzu closure recorded; hotel meal plan remains unknown.
- [x] C — Gaming, landmarks, activities and dated events data/page: TWC spectator access and CDM entry timing remain unresolved.
- [x] D — U.S.-traveler practicalities data/page: ETIAS launch status, individual entry eligibility, carrier/insurance and personal access needs remain open.
- [x] E — Official live radio sports data/page: Malta carriage/stream access for BBC Radio 5 Live and match selection in Sportsworld remain unresolved.
- [x] F — Expense planner data/page: editable browser-only calculator; no fare, room, flight, FX or ticket purchase is assumed.
- [x] G — Responsive shell, executive summary, integration, legacy redirects and README.
- [x] Repeatable source-snapshot generator and local integration checker added.
- [x] Integrated data/page consistency and link checks.
- [x] Pass 1 — factual/source and scope review.
- [x] Pass 2 — usability, completeness and data/page consistency review.
- [x] Pass 3 — responsive/accessibility/bug review (CSS/DOM review and smoke tests; no graphical browser automation is installed in the workspace).

## Current verified anchors

- Malta Tourism Authority says the accommodation environmental contribution effective 1 Jul 2026 is €1.50 per night per guest aged 18+, capped at €22.50/person/visit and itemized separately; confirm the hotel invoice and any third-party coverage.
- Trip brief: AX ODYCY, Deluxe sea-view room, Qawra Coast Road, Qawra SPB 1902, 13–19 October 2026. This is the user's requested scenario, not proof of a hotel reservation.
- Thunderpick's official schedule distinguishes its wider final-stage window (12–19 Oct), media day (13 Oct), group stage (14–16 Oct), playoffs (17–18 Oct), and departure day (19 Oct).
- BLAST's guide for a different 2026 tournament publishes the BLAST Arena Studios/MFCC address at Ta' Qali, but Thunderpick's page itself says only Malta (LAN); TWC public access, ticketing, door times and exact venue remain unconfirmed.
- MPT's current Route 186 timetable shows service every 30 minutes, including Qawra stop 952 (published snapshot 06:10–21:38) and directional Ta' Qali Stadium stops 2194 / 6227. The normal return toward Buġibba runs via St Paul's Bay/Buġibba, not Qawra seafront; the current listing's final arrival at Bugibba Bay 1 is 21:26. These are static timetable details, not a trip-day guarantee.
- MPT's current service-update page lists a Route 186 detour toward Buġibba Friday/Saturday evenings from 19:00 to midnight starting 17 Oct; Gholja 2 through Targa are not served. The impact on the exact Ta' Qali return stop is unresolved; recheck before travel.
- Official MPT fare material lists €2.00 winter and €2.50 summer day-route fares and two-hour validity; the public page does not establish the 2026 October changeover date.
- Aquarium ticket page checked 9 Oct shows adult online/door rates and the current after-16:00 online discount; recheck before purchase.
- Malta Met Office forecast checked 9 Oct reached 15 Oct only; it did not forecast the last four trip days in that snapshot.
- BBC Radio 5 Live official schedule lists Premier League commentary on 17 and 18 Oct; these UK Radio 5 services are not on the Malta DAB+ channel list, and Malta online access remains unconfirmed.
- BBC World Service Sportsworld has scheduled episodes on 17 and 18 Oct; Malta's DAB+ channel listing includes BBC World Service. BBC Radio 5 Sports Extra also lists football coverage, but Malta carriage/stream availability is not confirmed.

## Integrated review passes (10 October 2026; source snapshot 9 October)

- **Pass 1 — facts, sources and scope:** checked 64 topic records across six JSON files against the exact shared keys, allowed source types, confidence values and date format. Every primary source URL and every URL in record notes is represented in `docs/SOURCES.md`. Caveats remain visible for event access, transport, October fares, ticket stock, entry status, radio carriage and personal costs.
- **Pass 2 — completeness, usability and consistency:** confirmed each page data filter matches JSON IDs, local links/fragments resolve (including compatibility redirects), and the generated Sources page contains 142 source entries and all 27 unresolved questions. The overview covers every requested topic and points to next steps.
- **Pass 3 — responsive, accessibility and behavior:** reviewed desktop/mobile CSS breakpoints, semantic sections, skip links, nav controls, labels, ARIA references and duplicate IDs; `node --check` passed for shared and inline scripts. The expense-calculator VM test confirmed unknown age is not assumed, the six-night contribution estimate, fare range, meal multiplier and user-entered USD conversion. The shared JSON-card renderer also passed a smoke test. HTTP smoke checks returned 200 for the site, topic pages, redirects, data, CSS, JavaScript and documentation. The sandbox has no installed graphical browser automation, so pixel-level rendering was not automated; the live preview is available for visual review.
- `python3 scripts/build_sources_page.py` regenerates the claim/question snapshot. `python3 scripts/verify_site.py` checks local schema, source coverage, links/fragments, nav parity, ARIA references and record filters; the checker does not fetch external sites or automate visual rendering.

## Branch and integration coordination

The Arena checkout is fixed to `arena/a15d87d4-maltasupplemental`; all changes remain on that branch. While this work was in progress, `origin/main` advanced from the session base. The latest main history was integrated before preparing the pull request. Overlapping older pages/data were reconciled in favor of the current six-file schema and integrated guide; the useful schema/final-report documentation was refreshed, and old hotel/itinerary/Qawra entry points now redirect to the current guide. Duplicate legacy datasets and the incompatible earlier checker were removed; the replacement checker follows the requested schema. No additional workstream branches were created because this workspace exposes no parallel branch/agent facility. Cross-topic findings remain in `docs/HANDOFF.md`.
