# Malta trip guide — final report

## Current session — fixed branch `arena/33cc3d09-maltasupplemental` (12 October 2026 UTC)

### Delivery summary

Integrated the updated `origin/main` snapshot (`096b659`) into the fixed branch, preserving the PR #77 quickstart, footer hubs, tests and branch-specific evidence. Resolved the shared-data, page and documentation conflicts without discarding either source stream. Work remained serial under A–F ownership; no separate workstream branches or subagents are claimed. Existing 15-page static architecture, seven canonical datasets, exact 13-field schema, renderer/design tokens, expense planner and source log remain in place.

### Newly reconciled evidence and scope

- **Transport:** the independent MPT Route 186 page reads reproduce a static Stadium 2194 → Buġibba Bay 1 example (20:53 → 21:27, 34 minutes) and a selected Qawra 952 → Stadium 6227 example (06:09 → 06:34, 25 minutes). A separate source pass reported 29–33 minutes for other return variants; because the grids are unlabelled and that range does not match the directly displayed 34-minute pair, the guide describes one matched example rather than asserting a general return duration. These are static rows, not a dated planner route, gate walk or onward Qawra connection. The 22:04/22:08 readings are outbound at Stadium 6227, not a later return at 2194. Saturday’s listed 19:00 semifinal start coincides with the published Route 186 diversion-window start; no match finish or suitable journey is confirmed.
- **Event schedule/access:** Liquipedia’s 12 October bracket read lists Saturday semifinals at 16:00/19:00 and Sunday third-place at 13:30 followed by a Best-of-5 Grand Final at 17:00 Malta time; the organizer independently confirms format, not those match clocks. They are third-party starts, not doors or finishes, and pairings remain TBD. Eventbrite’s weekend rows/FAQ answers remain hidden; its “Sales end soon” banner, generic free recommendation and HLTV’s secondary free-ticket report do not establish a current event-specific checkout price, inventory or personal reservation.
- **Radio/markets:** Kalshi’s read-only API on 12 October lists open markets for all four Thunderpick openers dated 14 October; its newest CS2 event dates in that response stopped at 14 October, with no 17–18 October playoff event observed. This supersedes the 11 October no-fixture snapshot. A market is not a broadcast; no named CS2 commentary on a Maltese terrestrial frequency or physical reception was verified. BFBS Malta remains stated as “closed in 1979”; source disagreement on the exact March day is retained.
- **Other workstreams:** earlier source-backed food/review, activities/events, U.S.-traveler essentials, date-qualified weather and blank expense-planner content remains in place. Google Maps values are separate volatile snapshots; Yelp’s HTTP 403 and other platform access limits are not converted into popularity or sentiment claims. Traveler-specific bookings, spending, flights and party details remain unprovided.
- **Provenance:** imported PR #79/#80 rows and the PR #77 source stream are kept distinct in `docs/SOURCES.md`. A malformed upstream source-log leftover row was deliberately not copied. Open questions and cross-stream effects are recorded in `docs/OPEN_QUESTIONS.md` and `docs/HANDOFF.md`.

### Three cumulative verification passes

1. **Pass 1 — implement and verify:** reviewed the repository and integrated the mainline additions into canonical event, radio, transport and source records plus the overview/transport/event/radio pages. Kept every claim linked to the dated source log; carried forward the separate Route 214 airport/event-area candidate and the existing itinerary quickstart.
2. **Pass 2 — adversarial review:** checked ticket-price attribution, match-start vs door/finish wording, Kalshi listing vs radio carriage, event-day diversion timing, Route 186 direction/stop IDs and time arithmetic, open-question references, schema/source-log coverage and stale summaries. The check caught an inconsistent generalized 29–33-minute return claim; user-facing copies now use the directly displayed 20:53→21:27 (34-minute) example and explicitly avoid extrapolating from unlabelled variants. No date-specific transit claim or taxi default is made.
3. **Pass 3 — full request audit:** checked the trip dates/hotel/event context, transit and alternate modes, food/café and requested platform limits, gaming/activities/landmarks/events, U.S.-traveler guidance, separate terrestrial-radio schedules/listings/carriage/reception distinctions, useful but qualified Kalshi context, responsive accessible pages and the blank-by-default expense planner. Remaining research limits and next checks follow below.

### Local gates (12 October 2026 UTC, after mainline integration and correction)

- `npm test` — **PASS**. Validator: 7 JSON files / 220 exact-schema records / 364 unique source URLs logged / 15 HTML pages / 395 link attributes / 9 shared navigation destinations / 25 expense rows.
- `python3 scripts/check_weekdays.py` (included in `npm test`) — **PASS**, 342 weekday/date pairs match the 2026 calendar.
- `python3 scripts/check_javascript.py` (included in `npm test`) — **PASS**.
- Playwright — **28/28 passed**, including axe at 320/360/768/1024/1440 px, planner behavior, quickstart/footer wiring, canonical projections and route/event evidence.
- `git diff --check` and `git diff --cached --check` — **PASS** on the resolved tree.

These software checks do not certify live services, external-link liveness, volatile listings, actual ticket inventory, date-specific transport, ride prices or radio reception.

### Remaining limits and next steps

- Check MPT’s date-specific planner and notices for each flight/event day; confirm Route 186/214 trips and both directions, stops/walks, any onward Buġibba–Qawra service, TQ notices, gate and event pickup rules. Obtain a live taxi/ride-hail/rental quote only if a confirmed bus option does not fit.
- Confirm Eventbrite’s event-specific price, booking/inventory, age/ID rules, attendee gate, day validity and hidden weekend door/finish/FAQ information with the organizer. Recheck the Saturday diversion and any special service.
- Recheck forecasts and official travel/entry guidance near travel; Malta’s national panel does not cover 19 October. No marine forecast or personal legal/medical determination is included.
- No named CS2 match carriage on a Malta terrestrial frequency or physical FM/DAB+ reception was verified. Recheck broadcaster schedules and scan on site; a fixture, station slot, market listing or online feed is not proof of carriage or reception.
- Menu/hours and map/review counts are volatile. Yelp returned 403 and Instagram/TikTok/Facebook/Reddit/X evidence remains limited to the separately recorded access attempts; no unsupported review ranking or sentiment is claimed.
- Flights, ticket bookings, party size, receipts, insurance, devices and actual expenses remain traveler-supplied. Fill the expense planner only from confirmed itinerary amounts and receipts.

### GitHub delivery (pending post-push observation)

The last observed PR #78 state predates this integration: it was open against `main`, `DIRTY`/`CONFLICTING`, with no status checks reported, no review decision, and `mergedAt: null`. The updated base at `096b659` is now integrated locally; the resolved tree passes the full local gate, but this merge commit has not yet been pushed. Re-query PR #78, checks and mergeability after push. No merge result or Pages build is claimed here.

## Previous session — `arena/561bff0e-maltasupplemental` (12 October 2026 UTC)

### Delivery summary

A final pre-departure pass executed on the eve of the trip window (the session opened late 11 October UTC; source reads are dated 12 October). The repository was reviewed at `main` `ac487ae` and found complete and healthy: GitHub Pages static site (15 pages), exact 13-field schema with seven datasets, per-topic pages rendered from JSON, source log, open questions, status ledger, blank-by-default expense planner with itinerary quick-fill, CI workflow and a Playwright/axe suite — all green on the untouched tree. Shared setup was verified serially and left intact; workstreams A–F ran on this fixed Arena branch with the established file-ownership map (`docs/PLAN.md`), G integrated last, and cross-stream findings went to `docs/HANDOFF.md`. Main advanced during the pass (PRs #68–#70 from parallel sessions) and was merged into the branch before delivery: conflicts were resolved keeping both sessions' blocks, this session's trip-week-notice additions were folded into the parallel pass's canonical `mpt-trip-week-notices-2026-10-11` record rather than duplicated, and main's API-verified Kalshi market record is preserved.

This session's increments, all source-read on 12 October 2026 UTC and logged in `docs/SOURCES.md`:

- **Arrival-day weather corrected upward in risk (D).** The Malta Met Office national panel now runs 12–18 October — **18 October appears in the national forecast for the first time** (mainly cloudy 24/18) — and labels **Tuesday 13 October “windy with isolated showers”, NW force 5–6**, materially worse than the UK Met Office's sunny 25/22 for the same day. The national site's own detailed forecast for the 13th is milder (F4→F3–4, high 26 °C, isolated evening showers, sea 26 °C); both readings are quoted side by side, not reconciled. Only departure day 19 October remains outside the national panel (UK BETA rows only).
- **Trip-week detour watch extended (A).** The live service feed (all three chunks) reconfirmed the 17–18 October cluster, both Route 186 notices and the trip-week notices the parallel pass detailed, and added to that record: the routine Sunday Marsaxlokk diversions (relevant to a Sunday 18 October outing), the Dingli diversion, a Route 117 detour on the 14th, Gozo-route detours across 12–15 October, stop-level wording for the 54/106 Attard-bound omissions, and — as a caution — an expired notice still displayed beside current ones.
- **Wednesday openers named (C).** Liquipedia's upcoming-matches block now names all four 14 October openers — 9z–Aurora, Falcons–NIP, Legacy–PARIVISION, FURIA–BetBoom — at EDT clocks that convert to the published Malta set (10:30/13:00/15:30/18:00), corroborating the guide's clock evidence from a fresh path. Eventbrite is unchanged: weekend agenda and FAQ answers still hidden, “Sales end soon”, no reservation test.
- **Radio listings re-read (E).** BBC Sportsound now dates its Saturday rows 17/10/2026 and later rows 22 Oct, bracketing the undated “Benfica v Celtic” row (15 October remains a lead); Sportsworld's 17/18 October episodes are unchanged; Radio Sportiva still names no trip-week match. No Malta carriage evidence changed.
- **Platform honesty (B) and fares (A/F).** Yelp still HTTP 403; the operator's fares page still prints only the 2025–26 winter window, so the trip-week split (€2.50 through 18 Oct, €2.00 on 19 Oct) remains a labelled inference. ETIAS remains not in operation (official EU FAQ re-read).

### What is verified (this pass)

The national 12–18 October panel and the 13 October detailed forecast from the official Malta Met Office pages; the trip-week detour notices as printed on the operator's live feed; the Wednesday opener pairings and bracket clocks from a direct Liquipedia read; the unchanged Eventbrite agenda rows and hidden weekend rows; the unchanged ETIAS non-operation wording; the unchanged BBC/Sportiva listings; the current Yelp block. Everything earlier sessions verified stands unless this pass recorded a change above.

### What remains unverified

Organizer Sat/Sun door/finish times, FAQ answers, reservation/inventory/day validity/gate; a saved date-specific MPT journey; both stop-to-gate walks; the exact last Route 186 return (OQ-S1) and the “April 21” notice year; whether the 260 Mon–Thu detour touches the weekday fallback chains (OQ-T1); any TQ event service; live taxi quotes; the trip-week fare split (inference); any named match on a Malta radio frequency and the 6C “Sports Channel” identity; 19 October's national forecast; the panel-vs-detail weather difference on the 13th; Yelp/Instagram/TikTok/Facebook/Reddit/X sentiment data; and every traveler-personal item (flights, reservation, party, insurance, devices, receipts).

### Passes and observed local gates

1. **Pass 1 — implement and verify:** time-critical sources re-read (Eventbrite; MPT updates in full and fares; Liquipedia; BBC Sportsworld/Sportsound upcoming; Radio Sportiva palinsesto; EU ETIAS FAQ; Malta Met Office panel + detailed forecast; Yelp access check). New/changed claims written only from those reads; every URL logged with its access date.
2. **Pass 2 — adversarial review:** overreach checks on the new claims (weather panel-vs-detail difference kept unreconciled; expired-notice caution added; the undated BBC row left a lead), source-log coverage re-verified by the validator, and the full local suite (validator + JavaScript + Playwright/axe) re-run after the edits and again after the merge with main.
3. **Pass 3 — full request re-check:** the requirement map is walked against the integrated tree; delivery is a PR from this branch merged by explicit number, and only observed GitHub/Pages state is reported afterwards.

### Next-session tasks and limitations (the honest list)

1. **During the trip (13–18 Oct):** re-read the MPT updates feed and journey planner each morning; confirm the actual last Route 186 return on the day; watch for a TQ special-service notice (the one thing that could fix the late return); reserve the free event spot and confirm the gate/day validity with the organizer before the first session; recheck the national weather panel daily (especially 13 and 19 Oct).
2. **Radio scan on the ground:** a physical DAB+ receiver scan at the hotel and venue (block 6C first) is the only way to close the radio question; log service labels, blocks and any named match heard. No remote source can substitute.
3. **Expense planner:** once the itinerary lands, use the quick-fill panel and enter only confirmed amounts; the fare split and the €1.50/night eco-contribution (capped €22.50) remain conditional until receipts exist.
4. **Limitations of this project:** several social/review platforms (Yelp, Instagram, TikTok, Facebook, Reddit, X) are unreachable from the research environment, so “popularity” rests on one dated TripAdvisor capture plus operator pages; review counts drift; no physical transit, reception or device-based visual test was possible; the operator's fare page itself prints an expired winter window; and the site's tests prove software behavior, not the live truth of external listings.

## Previous session — `arena/2b38c9c6-maltasupplemental` (11 October 2026 UTC)
## Previous integrated result — `arena/57ad3983-maltasupplemental` (11–12 October 2026 UTC)

## Previous session — `arena/5ec909ed-maltasupplemental` (11–12 October 2026 UTC)

### Integration boundary

This fixed Arena branch opened PR #71, then incorporated successive `main` advances from PR #69 (`926c33b`), PR #70 (`8799b1b`) and PR #73 (`1382640`). The latest source corrections were already recorded on `main`; this continuation integrated them rather than re-fetching external pages. No parallel agents or workstream branches were used: A–F were handled serially under the ownership map and G integrated last. PR #70 clarified that the Routes 46/260 and 54/106 notices had been mentioned in passing before their stop-level details were given a separate record. Mainline then advanced through PR #74 to `0031757`, which records PR #73’s delivery receipt; that documentation update is also being reconciled here. The final local suite passes. GitHub merged PR #71 as `c4449fb7e7267f16ff113fa8eb5de541dc5a88fb`; its required check passed and the Pages build for that merge commit subsequently reported `built`. This report records that observed delivery; no new external research was performed.

No new Eventbrite checkout/inventory test, dated Malta Public Transport planner query, live taxi/rideshare quote, venue visit or physical radio scan was made. Facts below retain their source dates and limitations in `docs/SOURCES.md` and `docs/OPEN_QUESTIONS.md`.

### Verified findings and boundaries

- **Trip inputs:** AX ODYCY, Qawra, 13–19 October 2026 and “Deluxe sea-view” are traveler-supplied details, not proof of a booking, rate, room allocation, flights or inclusions.
- **Event listing:** the 11 October Eventbrite extraction identifies the in-person, 18+ event at BLAST Arena Studios Malta, MFCC, Attard, for 14–18 October. It shows Wed/Thu 09:30 check-in / 10:30 games and Fri 14:00 / 15:00, but not the weekend door rows. The 22:00 headline conflicts with Wed/Thu agenda rows ending at 22:30. The event-specific ticket section exposes no price, tier, reservation action, checkout or inventory; “Free / Reserve a spot” was in a generic “You might also like” card. HLTV’s 2 October free-ticket report is secondary. The traveler’s own reservation, fees, gate, day validity and weekend doors/finishes remain unknown.
- **Transport:** the current static Route 186 read distinguishes the Buġibba-bound return at Stadium stop 2194 (displayed through 20:53) from the Qawra → Ta’ Qali/Rabat outbound at Stadium stop 6227 (displayed around 22:04/22:08). The return terminates at Buġibba Bay 1, not Qawra, and lists no Il-Qawra stop. These static rows are not tied to a travel date or service-day type and do not prove a complete network search or a date-specific last bus. Check the actual date, gate, both stop sides, walks and onward Buġibba–Qawra leg in MPT’s planner. The 17–18 October detour cluster and Saqqajja closure remain relevant; no TQ/Thunderpick service was published in the recorded feed and TQ1 said “Timetable not available!”.
- **Trip-window notices and fares:** the Routes 46/260 overnight notice (12–16 October) and Routes 54/106 Attard daytime notice (13 October) are separately detailed; they had already been mentioned in passing, and their effect on this traveler’s route is unverified. MPT publishes a two-hour transfer window with free transfers, conditional on actual boardings and operator terms. Its fare page gives no 2026/27 season boundary, so the likely €2.50 (13–18 Oct) / €2.00 (19 Oct) split remains an inference. No bus card, fare, journey or taxi is assumed.
- **Modes and expense guidance:** the transport guide compares public bus, taxi/ride-hail, rental and other local modes for practical fit, cost/value and limitations. It contains no live ride or rental quote, saved door-to-door journey, confirmed late return or measured venue walk; choose using current offers and itinerary. The expense planner stays blank by default with 25 daily/core/optional rows, preview-based quick-fill and tested CSV/JSON workflows.
- **Food and recreation:** the TripAdvisor AX ODYCY search was a 10-mile, 1,869-result “Best Nearby” query using reviews and distance, not a Qawra-only ranking. Five linked profiles were directly re-read as a dated, volatile sample (Cheeky Monkey 3,374; Nine Lives 2,876; Trattoria Riccardo 2,675; Ta’ Pawla 1,872; Minoa 765 reviews). Counts do not establish quality, current hours or availability. Yelp/Reddit access returned 403 and Google Maps yielded a JavaScript shell in the recorded upstream check; no sentiment is inferred. The guide includes gaming/arcades, landmarks, activities and dated event leads; no public walk-in PC gaming café was verified.
- **Everyday travel and weather:** the 11 October EU ETIAS FAQ said ETIAS was not operating, no applications were collected and no action was required “at this point,” with several months’ notice promised before launch; this is dated general guidance, not a permanent exemption or personal legal determination. EES local practice in Malta remains conflicted. Malta’s national Met Office panel covers 13–18 October, not 19; UK Met Office Valletta and AccuWeather views are separate dated snapshots. No marine forecast or sea-state check was made. U.S.-traveler power, money, health, connectivity, entry, safety and customs information is source-linked and not personalized advice.
- **Terrestrial sports radio:** official station schedules and trip-window program leads are kept separate from actual Malta carriage, receiver compatibility and reception. BBC/Rai/NET FM/Radio Sportiva entries are not proof a named match will be heard locally. A read-only Kalshi API snapshot lists trip-window EPL/UCL/NFL markets and no Thunderpick fixture in the sampled open CS2 games; listings are not broadcasts, odds advice or proof of personal eligibility.

### Three cumulative verification passes

1. **Pass 1 — implement and verify:** reconciled the current upstream records/pages and source log with the exact 13-field schema, preserved the shared site and planner, and carried forward dated Eventbrite, MPT, ETIAS/weather, review-platform and radio/Kalshi evidence with explicit limits.
2. **Pass 2 — adversarial review:** checked ticket-price attribution, Route 186 directions/stops/times, onward connection and transfer assumptions, notice impact, taxi defaults, weather/provider attribution, food-ranking scope and market-versus-broadcast wording. Corrected stale conflicting copies and checked that unknowns remain open rather than asserted.
3. **Pass 3 — original-request audit:** mapped the integrated guide to the requested trip context, event-day transport/mode comparison, restaurants/cafés and requested review platforms, gaming/landmarks/dated activities, U.S.-traveler essentials, terrestrial sports-radio schedules, responsive pages, citations and blank expense planner. Limitations and next checks remain documented.

### Local gates observed after the latest `main` integration (12 October 2026 UTC)

- `python3 scripts/validate_site.py` — **PASS**: 7 JSON files, 218 exact-schema records, 351 unique record URLs in `docs/SOURCES.md`, 15 HTML pages, 374 link attributes, 9 shared navigation destinations, 25 expense rows.
- `python3 scripts/check_javascript.py` — **PASS**.
- `npm test` — **PASS, 26/26 Playwright tests**, including axe sweeps at 320/360/768/1024/1440 px, the latest route/date and event-ticket projections, radio/market separation, mobile navigation, expense planner import/export/quick-fill and failure cases.
- `git diff --check` and `git diff --cached --check` — **PASS** at the integrated-tree gate.

These are local structure, behavior and accessibility checks. They do not establish ticket inventory, live transit, ride prices, current external-page truth, forecast accuracy or radio reception.

### Remaining unknowns and next-session checklist

Event-specific ticket price/fees, booking method, availability, personal reservation/access, attendee gate, age/ID policy, day validity and weekend doors/finishes; date-specific MPT journeys in both directions, onward Buġibba–Qawra service, stop/gate walks and the effect of all notices; actual trip-week fare, bus-product suitability, live taxi/rental quotes and venue pickup/parking; ETIAS/EES changes, 19 October Malta national forecast and marine conditions; named-match Malta radio carriage and physical FM/DAB+ reception; current venue menus/hours and mutable platform counts; and traveler-specific flights, party size, receipts, insurance and devices. Recheck volatile items close to travel and populate the planner only from actual bookings, quotes and receipts.

### GitHub delivery state

- **PR #71 merged:** GitHub reports [PR #71](https://github.com/buffedlizard55-lab/MALTASUPPLEMENTAL/pull/71) **MERGED** at `2026-10-12T00:53:20Z` as merge commit `c4449fb7e7267f16ff113fa8eb5de541dc5a88fb`. The required “Schema, browser and accessibility checks” passed on head `b5db81196906626f94499a510bd244edf4539f99` (run [38189621707](https://github.com/buffedlizard55-lab/MALTASUPPLEMENTAL/actions/runs/38189621707)).
- **GitHub Pages:** the Pages latest-build API reported status **`built`** for merge commit `c4449fb7e7267f16ff113fa8eb5de541dc5a88fb` at `2026-10-12T00:53:46Z`. Public URL: <https://buffedlizard55-lab.github.io/MALTASUPPLEMENTAL/>. This is a GitHub build-state observation, not an independent browser/device review of every page.
- **Upstream correction delivery (PR #73; separate branch):** GitHub reports PR [#73](https://github.com/buffedlizard55-lab/MALTASUPPLEMENTAL/pull/73), from `arena/57ad3983-maltasupplemental`, **MERGED** at `2026-10-12T00:35:41Z` as `1382640d027e5bef69b97776bc72c6a1b4cfb096`. Its required “Schema, browser and accessibility checks” passed (run [38188460975](https://github.com/buffedlizard55-lab/MALTASUPPLEMENTAL/actions/runs/38188460975)); post-merge validation (run [38188606027](https://github.com/buffedlizard55-lab/MALTASUPPLEMENTAL/actions/runs/38188606027)) and Pages deployment (run [38188605376](https://github.com/buffedlizard55-lab/MALTASUPPLEMENTAL/actions/runs/38188605376)) succeeded. Those upstream facts are recorded separately from PR #71.

Earlier delivery statements in the historical report sections refer to prior sessions/PRs and do not supersede the observed PR #71 result above.
---

## Previous session — `arena/b29d95ae-maltasupplemental` (11 October 2026 UTC) — historical mainline snapshot

### Delivery summary

A pre-departure delivery pass, two days before the 13 October trip start. The repository was reviewed at `main` `ae69ab1` (the PR #55 merge tip) and found complete: GitHub Pages static site, exact 13-field schema with seven datasets, per-topic pages rendered from JSON, source log, open questions, status ledger, blank-by-default expense planner with itinerary quick-fill, CI workflow and a 23-test Playwright/axe suite. Shared setup was verified serially and left intact; the parallel-work protocol ran with the established file-ownership map on this fixed Arena branch (documented in `docs/PLAN.md`), with cross-stream notes in `docs/HANDOFF.md`. Workstream G integrated last.

This session's increments, all source-read on 11 October 2026 and logged in `docs/SOURCES.md`:

- **Weekend match clocks pinned (C).** A chunk-by-chunk direct read of the Liquipedia bracket supplies the playoff schedule the ticket page still hides: **semifinals 16:00 and 19:00 Saturday 17**, **third-place 13:30 and the best-of-five final 17:00 Sunday 18** (Malta time; pairings TBD; the bracket labels its clocks EDT and EDT+6 h gives Malta CEST). The late-return plan now demonstrably covers all five event days. A search-index extract that appeared to name a “FURIA v BB semifinal” was contradicted by the direct read and discarded; the day-card `twc-day-2026-10-14` contradiction (an unflagged 18:30 next to 18:00) was fixed with the 18:30 figure retained as a labelled outlier, matching `twc-opening-matchups-14-oct`.
- **Named soccer commentaries on official radio listings (E).** The BBC's own Sportsound page names full-commentary **Scottish Premiership Dundee v Rangers (Sat 17, 19:00 UK, Radio Scotland Extra)** and **Celtic v Hearts (Sun 18, 14:00 UK, Radio Scotland)**, plus a Sportsound omnibus and Fan Zone; the 5 Live record was corroborated (Manchester City v Ipswich, Sat 17 14:45, 5 Sports Extra). These join the seven Premier League listings already recorded. All are **UK output** — none is Malta carriage — and a Europa League “Thursday 19:00, Benfica v Celtic” row that prints no date stays a lead.
- **ETIAS trip-week answer (D).** The official EU FAQ now reads *“no action is required from travellers at this point”* and promises several months' notice before any launch — so no ETIAS authorisation is needed for 13–19 October 2026. The executive summary and the everyday record state this as the trip answer; the earlier last-quarter-of-2026 timing risk is retired for this departure.
- **Saturday-night transport risk tightened (A).** The full service-updates page confirms both Route 186 notices and shows the 17–18 October 19:00–00:00 cluster also degrades every fallback lead (202/260 detoured with no stops printed; 405 skips Rotunda 1/Bezzina; 45 skips Rotunda 2→Targa; 47 skips Gatt→Rotunda 1; 48/N48 batched). The pre-booked-return recommendation is strongest for Saturday.
- **Platform honesty (B).** Yelp re-attempted today — still HTTP 403; the recorded access limits are current, not historical.

### What is verified (this pass, on top of the merged body of evidence)

Event venue/address/dates/admission from the ticketing listing; the Wed–Fri agenda rows; the eight-team field with NIP replacing Virtus.pro (9 October, per Liquipedia's participant note and HLTV/Hotspawn); weekend and opener match clocks from the bracket's own EDT labels (converted, third-party, labelled as such); Route 186 grids (three unlabelled variants — see OQ-S1), both detour notices and the detour cluster from operator pages; fare table wording (winter window still printed as 19 Oct 2025 – 13 Jun 2026 only); BBC Sportsworld dated episodes 17–18 October and the named UK PL/Scottish Premiership listings from official programme pages; ETIAS non-operation from the official EU FAQ; UK Met Office Valletta panel covering 13–19 October.

### What remains unverified

Organizer Sat/Sun **door** times and any finish times; the traveler's reservation, inventory, day validity, scanning, gate and parking; FAQ answers (client-rendered, never extracted); a saved date-specific MPT journey in either direction; both stop-to-gate walks; the Buġibba→Qawra onward connection; what actually runs after 20:54 on event nights (the fallback legs are unverified *and* Saturday-degraded); any TQ event service; live taxi/ride-hailing quotes; the 2022-footer taxi tariff as current maxima; the trip-week fare split (inference only); any named match on a Malta radio frequency (schedule, carriage, receiver and reception are four separate unproven links); BBC Sounds/stream access from Malta; the “Sports Channel” 6C/12A identity conflict; the Malta national weather panel for 18–19 October (7-day URL AccessDenied today); sentiment or “trending” data from Yelp/Instagram/TikTok/Facebook/Reddit/X (blocked or limited); and every traveler-personal item (flights, party, invoice, insurance, devices).

### Passes and observed local gates

1. **Pass 1 — implement and verify:** time-critical sources re-read (Eventbrite; MPT updates in full and fares; Liquipedia bracket in full; BBC Sportsworld/Sportsound upcoming pages and episode m00334k6; EU ETIAS FAQ and Commission page; UK Met Office panel; met office access check; Yelp access check). Every claim logged with URL and date; gaps recorded rather than guessed.
2. **Pass 2 — adversarial review:** found and fixed a genuine data contradiction (day card `twc-day-2026-10-14` carrying both 18:00 and 18:30 for the fourth opener) and two stale day cards (`twc-day-2026-10-17/18` saying no first-game time was known when the bracket supplies16:00/19:00 and 13:30/17:00); aligned the executive summary, day framework and bus checks with the weekend clocks and the ETIAS answer; verified the detour-cluster detail against the operator page; confirmed the validator's source-log coverage rule (fixed one abbreviated URL row).
3. **Pass 3 — full request re-check:** the requirement map below was walked against the integrated tree; the complete local suite was re-run afterwards.

**Local gates observed (11 October 2026):** `python3 scripts/validate_site.py` — PASS: 7 JSON files / 200 exact-schema records / 327 unique record URLs in `docs/SOURCES.md` / 15 HTML pages / 341 link attributes / 9 navigation destinations / 25 expense rows. `python3 scripts/check_javascript.py` — PASS. `npx playwright test` — **23/23 passed** (axe at 320/360/768/1024/1440 px; canonical projections; date-by-date transport plan; radio table at 320/360/720/1440 px; planner, quick-fill, CSV/JSON backup and failure modes). These are local software checks, not external truth, dated operations or RF reception.

### Requirement-by-requirement (this integrated tree)

| Requirement | Where it lives | State |
|---|---|---|
| Repo review; plan before parallelizing | `docs/PLAN.md` (this session's plan at top) | Done; single fixed Arena branch adapted and documented |
| Workstreams A–G with owned files; cross-stream notes | data/page pairs per stream; `docs/HANDOFF.md` | Done, serial execution |
| Hotel, dates, room, event venue as inputs | Overview, hotel checklist, event desk | Present; labelled traveler inputs |
| Event → venue transport on event days (public transport) | `getting-around.html#event-day-by-date` + transport records | Done; per-date plan, fares, late-return gap, detours; date-specific planner still required in-country |
| Transport comparison (convenience/price/value/feasibility) | `getting-around.html`, `mode-comparison-summary` | Done; bus priced, others live-quote |
| Food & cafés incl. review-platform research | `restaurants.html`, `data/food.json` | Done; dated review-volume snapshot; platform blocks recorded (Yelp 403 re-confirmed) |
| Gaming centers, activities, landmarks, events | `activities.html`, `event.html` | Done; PC-café absence stated honestly; dated event leads |
| Everyday life for a US traveler | `everyday.html` | Done; ETIAS answer now trip-specific; weather panels disagree and are all shown |
| Live radio sports broadcasts w/ official schedules (Kalshi-relevant sports) | `radio.html`, `data/radio.json` | Done; dated + named UK listings incl. EPL/Scottish Premiership; Malta carriage/reception explicitly unproven |
| Expense planner quick to fill once itinerary arrives | `costs.html#quick-fill`, `data/expenses.json` | Done; blank-by-default, preview, CSV/JSON |
| Categories/sections/subpages; desktop + mobile | All pages; axe 320→1440 | Verified locally |
| Executive summary; sources as official links | `index.html#exec-title`, `docs/SOURCES.md`, `sources.html` | Done |
| No hallucinations; open questions recorded | `docs/OPEN_QUESTIONS.md`, confidence fields | Enforced by validator + review passes |
| GitHub Pages with clean UI | `.nojekyll`, Pages on `main` | Live at https://buffedlizard55-lab.github.io/MALTASUPPLEMENTAL/ |
| PR then merge to main | this branch → PR #64 | Done — merged 19:10:02 UTC as `60fea6d`; Pages build `built` (observed) |

### Delivery observed (11 October 2026)

PR **#64** (“Pre-departure delivery pass: weekend match clocks, named radio commentaries, ETIAS trip answer (rebased on main)”) was rebased onto `main` through PR #66 (`614a67b`), passed its required GitHub check (“Schema, browser and accessibility checks”, run 38166741439, conclusion success), and was **merged to `main` at 2026-10-11 19:10:02 UTC** as merge commit `60fea6df71f1a15e2468e10ad32575b06f89bc83`. GitHub Pages' latest-build endpoint reports the build for that commit as **`built`** (created 19:10:03, updated 19:10:23 UTC) with the public URL https://buffedlizard55-lab.github.io/MALTASUPPLEMENTAL/ sourced from `main` at `/`. These are GitHub build-state observations, not an independent content audit of the deployed bytes.

### Limitations of this session

Search-index extracts were used for some corroboration (and one, the “FURIA v BB semifinal” pairing, was caught contradicting the direct page read and discarded). Only time-critical sources were re-read; older records were re-checked for internal consistency, not re-fetched. No browser crawl of external links was performed from the sandbox (network is restricted; `fetch_page`/search were used instead). No receiver, taxi quote, journey-planner run or venue visit is possible from here.

### Next-session tasks (priority order)

1. **In-country, day-of:** reserve/confirm the Eventbrite spot and carry photo ID; recheck the ticket page for Sat/Sun doors and any schedule change; check MPT service updates daily for a TQ service (TQ1's corridor serves Qawra/Buġibba) — one notice could fix every late return.
2. Run the MPT journey planner for 14–18 October from the actual hotel and confirmed gate; save both directions; verify stop sides, walks and the Buġibba→Qawra link; pre-book the late return (strongest for Sat 17).
3. Scan DAB+ 6A/6C/12A and the FM list at the hotel and venue; log service, block, time, language and named match actually heard; ask the “Sports Channel” operator which block is live.
4. Refresh hours/menus/closures for chosen venues; confirm the Empire Cinema arcade status; recheck the Malta national forecast for 18–19 October and marine notices before any sea activity.
5. When the traveler's itinerary arrives: quick-fill the planner, review the preview, export CSV/JSON; enter only retained charges (keep card holds in notes).
6. Watch the official EU ETIAS page only for future trips; nothing is required for this one. Resolve EES's Malta implementation at the border with generous time.

## Previous session — `arena/1005fdbf-maltasupplemental` (11 October 2026 UTC)

### Delivery summary

The repository was reviewed first and the existing structure preserved: static Pages shell, shared navigation and renderer, the exact 13-field record schema, seven topic datasets, master source log, open questions, status file, blank-by-default expense planner, CI workflow and Playwright suite. Workstreams A–F then ran serially on this one fixed branch, each editing only its owned files, with G correcting the shared surfaces afterwards.

**Evidence delta:** 199 → **215** exact-schema records after integration with the other sessions merged to `main` during this session (radio 28, transport 34, everyday 20, food 49, activities 50, event 9, expenses 25); 314 → **340** logged record URLs. (The counts rise from 212/322 to 215/340 as the other sessions' radio and sport-calendar records merge in; nothing was dropped.)

**The headline correction.** Two earlier sessions had left the sports-radio requirement in a holding pattern: one directory placed a “Sports Channel” on DAB+ block 12A, another on 6C, and the pages told the traveller to scan both without ranking them. A dated field observation of Malta's multiplexes (page updated 30 January 2026) settles it. Its **6C** service table, captioned **13 January 2026**, lists `Sports Channel` — service ID **C02F**, 32 kbit/s, DAB+ stereo HE-AAC v2 — and its **12A** table, same date, lists only Smooth Platform music services with **no sports service at all**. The monitor's own ensemble timeline additionally lists a sports service on 6C in every snapshot from 20.01.2015 to 13.01.2026: roughly a decade of carriage under a stable label. The WorldDAB 12A attribution is now recorded as unsupported and superseded, the record that carried it is marked unverified, and the corrected position has been propagated to the overview, README, final report, handoff and open questions. What remains unverified is narrower and honest: **what the service airs on 17–18 October 2026** (a 2023 enthusiast field report called it a talkSPORT relay) and indoor reception at the hotel or venue.

**Other corrections made this session.** The monitor's **6A** table has a different date from the 6C/12A tables — service names re-listed on 13 January 2026, but the service IDs and bitrates from a table captioned 19 January 2025 — so BBC World Service and Rai carriage is now dated precisely rather than lumped under one date. The Route 186 diversion notice's own wording was read in full: it **starts on 17 October**, so Friday 16 October runs on the ordinary timetable while Saturday 17 October, 19:00–00:00, sits inside the window, and the notice's unrelated April predecessor is recorded separately. The Route 186 page publishes **three unlabelled timetable variants** with the Ta' Qali Stadium stop ending at 20:53/20:54 in one and 22:04/22:08 in others; every page that had quoted a single figure as “the last bus” now states the variant problem instead. Route **405** (Ta' Qali Park & Ride–Mosta) was found calling at Stadium stop 6227, and the **MFCC's own address and switchboard** — Millennium Stand, Level 1, The National Stadium, Ta' Qali, ATD 4000; 2141 0371 / 23380110 — was added as the contact for gate and access questions. Finally, a draft ride-hailing note citing Uber's Malta city page was falsified: that URL returns Uber's own “we couldn't find that page”, so the record was rebuilt on Bolt and eCabs with the dead end written down.

### Pass 3 audit — the original request, line by line

| Original requirement | Where it is answered | Status |
|---|---|---|
| Hotel, dates, event venue and dates | `hotel.html`, `event.html`, `data/event.json` | Met; gate and Saturday/Sunday agenda still unpublished |
| Restaurants, food and cafés from Google/Yelp/Instagram/TikTok/Facebook/Reddit/X | `restaurants.html`; dated TripAdvisor review-volume snapshot plus a new Reddit community-picks record and per-platform coverage statement | Partially met **by access**: TripAdvisor and (via search extracts) Reddit are represented; Google Maps place data, Yelp, Instagram, TikTok, Facebook and X were unreachable from this environment and that is stated on the page rather than papered over |
| Gaming centres | `activities.html`; arcade and VR records; explicit “no public PC-gaming café verified” | Met with an explicit negative finding |
| Landmarks | `landmarks.html`, `activities.html` | Met |
| Categories, sections, subpages, desktop and mobile, fast to find | Navigation across 15 pages, quick-link rows, client-side search/filter, responsive tables with mobile data labels | Met; browser tests assert the mobile/desktop table behaviour |
| Public transport, ride share and other modes compared on convenience, price, value, feasibility | `getting-around.html` mode cards, fare callout, day-by-day plan | Met; judgments are labelled as judgments and no journey time or walk is claimed as measured |
| How to reach BLAST Arena Studios (Attard) by public transport on event days | `#event-day-by-date`, `#event-checklist`, route records | Met as far as the sources allow: the 186 corridor, the asymmetric return, Route 214/202/405 alternates and the late-finish gap are all documented; no confirmed gate, no date-specific planner run |
| Airport and hotel logistics | TD1 and Route 214 records; fare and sales-point records | Met; season boundary remains third-party inference |
| US-traveller everyday life: plugs, SIM/eSIM, money/tipping, safety, health, customs, language, weather | `everyday.html`; 20 records covering all eight topics, now including the State Department advisory and consular contacts | Met |
| Radio: live terrestrial sport with verified official schedules | `radio.html`; block map, listening plan, station records | Met as an evidence set, not a guarantee: carriage is now verified for the sports blocks, Rai's weekend format is official, BBC episode starts are dated, and every interval that is **not** verified is labelled |
| Expense planner ready for quick entry | `costs.html`; blank by default, quick-fill preview, CSV/JSON backup, covered by tests | Met |
| Executive summary, sections and subpages, verified source links | `index.html` executive summary; `sources.html`; `docs/SOURCES.md` | Met; validator confirms every record URL appears in the source log |
| Line-by-line verification, no hallucinated facts | This table, the per-record `date_checked`/`confidence` fields and the open-questions file | Met by process: every correction above came from a re-read, and two claims were removed rather than kept |

### Passes and observed local gates

1. **Pass 1** — fresh primary-source reads; 13 new records with all 13 fields; pages and data kept in step; every new URL logged.
2. **Pass 2** — adversarial review found and fixed: the 6A observation-date mismatch, the surviving 12A claims outside historical records, the single last-bus figure, the unhedged Friday diversion, and a ride-hailing record resting on a dead URL; an in-page anchor sweep across all 15 pages returned zero unresolved targets.
3. **Pass 3** — the table above, plus the full local suite on the final tree.

**Local gate results (observed, final tree after rewriting onto `main`):** `python3 scripts/validate_site.py` → `PASS: 7 JSON files / 215 exact-schema records; 340 unique record URLs found in docs/SOURCES.md; 15 HTML pages / 371 link attributes checked; 9 shared navigation destinations; 25 expense rows wired.` `npm test` → **25 passed (2.3m)**, including both radio tests (the trip-week table at mobile and desktop widths, and the fixture-vs-carriage separation test). Earlier runs during the session gave 23 passed on the pre-integration tree.

**Observed merge and deployment state:** merged from this branch as PR **#61** (merge commit `0d8cf43`, 18:49:43 UTC) and PR **#63** (merge commit `0838994`, 18:54:09 UTC); the `Validate Malta Trip Guide` run on `main` and the `pages build and deployment` run both completed **success** for the merge commits, and the live Pages site was re-read afterwards with the corrected block text present.

### Still needed / next-session priorities

1. **Radio content, not carriage.** With a DAB+ receiver bought in Malta, scan 6C (Sports Channel, Radio Sportiva) and 6A (Rai RadioUno, BBC World Service) at the hotel and the venue and log what actually airs during 17–18 October. Written schedules do not exist for the trip dates on any station's site.
2. **The event-day return.** Confirm the Saturday/Sunday finish times and the attendee gate with the organiser or the MFCC switchboard, run MPT's date-specific planner for 14–18 October, and ask MPT whether a TQ event service will run. The published last return and the published agenda do not currently meet.
3. **Fares.** Ask MPT which single fare applies on 13–19 October; the operator page still prints only the 2025/26 winter window and the trip-week split rests on third-party guides.
4. **Food and activities.** Check the community-picks shortlist for current trading, and confirm aggregator-only events (Gozo kite festival, Studio Theatre) with their organisers.
5. **Platform gaps.** Google Maps place data, Yelp, Instagram, TikTok, Facebook and X remain unreadable from this environment; a session with a browser and a residential IP should close that gap rather than infer from it.

## Previous session — `arena/3031b29b-maltasupplemental` (11 October 2026 UTC)

### What this pass did

The repository was reviewed first and left intact: static Pages site, canonical 13-field schema, seven datasets with matching pages, source/open-question/status/handoff/plan logs, blank-by-default expense planner, CI workflow and the Playwright/axe suite. The session then attacked the remaining weak spot in the original request — a receiver-usable answer about live sports radio — and re-corroborated the trip’s decision-changing facts two days before departure.

### New verified findings, with their limits

- **English EPL commentary on radio: one plausible route, one ruled out, one unproven.** A crowd-edited talkSPORT article lists “DAB+: 6C (Malta)” in its frequency infobox and states that outside the UK and Ireland talkSPORT carries live commentary of every Premier League match in several languages including English. That strengthens — but does not prove — the Maltese 6C “Sports Channel” lead, because the same service is listed on 12A by WorldDAB and the operator’s visible directory shows no sports tile. In parallel, **BFBS Radio 2 was ruled out**: its own schedule page does carry live Premier League commentary, but BFBS Malta closed in 1979 and BFBS frequency tables list UK/Gurkha/overseas-base outlets only; sources disagree on the exact March day (25, 26 or 31 March), so the report uses the year only. **PBS Radju Malta (93.7 FM) and Radju Malta 2 (105.9 FM)** have a radio-carriage precedent — a third-party rights directory describes PBS’s FIFA/EBU 2026 World Cup coverage as including radio on both stations — but that tournament is outside the trip window and no 13–19 October lineup is published.
- **The trip-window sport calendar, checked against departure day.** Inside 13–19 October: the Premier League weekend (17–19 October), Serie A matchday 7, Champions League matchday 2 (13–14 October), an NFL London game on 18 October (listed as Houston Texans v Jacksonville Jaguars; 9:30 a.m. ET = 15:30 Malta) and the CS2 event. Outside the stay: UEFA Champions League matchday 3 (20–21 October), the NBA opener (20 October), the MLB World Series (from 23 October), the F1 United States Grand Prix (23–25 October) and El Clásico (25 October). Fixture clocks were independently corroborated on the BBC Sport and Sky Sports fixture pages against the league’s own amendment article; no radio carriage was found for the NFL game.
- **Transport re-reads.** The complete service-updates page was read again and the weekly Friday/Saturday 19:00–00:00 detour cluster (starting 17 October, ending 18 October at about 00:00, so only the Saturday 17 October evening falls inside the trip) enumerated in full (Routes 186, 202, 260, 47, 103, 45, 405, 238, 203, 280, 31, 41, 42, 48, N48), alongside the older Route 186 20:00–00:00 notice ending 21 April and the Saqqajja stop-4627 closure; still no Thunderpick, BLAST or TQ service was published. TQ1’s published northern corridor (Ta’ Qali → Rabat, Mosta, Naxxar, St Paul’s Bay, Qawra → Buġibba) and TQ2’s central corridor were newly recorded, together with a March 2026 precedent in which MPT ran extra and post-event Ta’ Qali services toward Buġibba and St Paul’s Bay. That precedent is evidence the pattern exists — not a commitment for this event.
- **Weather.** The national forecast panel for 13–17 October was corroborated by a second Maltese outlet (Times of Malta) with identical values; three third-party forecasts were read for 18–19 October and agree only on a rain risk, which is enough to pack a rain layer and nothing more.
- **Data-integrity bug found and fixed (Pass 2):** the canonical `espresso-odycy` record — the hotel's 24/7 coffee bar — was carrying the rooftop restaurant's hours (Wednesday–Saturday 18:30–22:30, ages 16+, €70/€80 tasting menu), its Level 11 address, its menu URL and its TripAdvisor figures. Those facts belong to `minoa-ax-odycy`. The Espresso record was rebuilt from the operator's own outlet page fetched on 11 October 2026 (Level 0, open 24/7, barista coffee/juices/snacks, menu PDF linked but not transcribed), the correction is recorded in its notes for traceability, and a regression test now asserts the two records keep distinct hours, addresses, prices and sources. A cross-record duplicate scan of all 202 records found no other contamination.
- **Event listing re-read:** unchanged apart from the price wording — “Sales end soon”, ages 18+, the same visible agenda, six team names plus “View all”, and map coordinates for the venue. On the 11 October read the word “Free” appeared only on a “You might also like” card rather than inside the ticket block, so free entry remains corroborated by HLTV but unconfirmed at checkout, consistent with the later ticket-section correction now carried in `data/event.json#twc-spectator-tickets`.

### Passes and observed local gates

1. **Pass 1:** fresh reads of the ticketing listing, operator fares/service-updates/Route 186 pages and the radio/fixture/weather sources; new records and notes added with per-claim source rows.
2. **Pass 2:** adversarial review of the new claims — crowd-edited sources labelled as such, third-party calendars kept as leads, “precedent” kept distinct from “announcement”, and the negative BFBS finding stated as a sourced negative rather than a measured scan.
3. **Pass 3:** the original request re-walked line by line against the integrated site, then the full local suite (schema/source-log/local links, JavaScript syntax, Playwright + axe at 320–1440 px) run on the delivered tree.

### Integration of upstream PR updates merged to `main` during this pass

`main` advanced twice while this fixed branch was open (PRs #58 and #59). Their upstream changes were reconciled into the fixed branch, preserving the added records and evidence while folding three corrections into the integrated text:

- **Ticket price wording.** The twelfth pass found that the word “Free” appeared only on a “You might also like” card, not in the Eventbrite ticket block. The executive summary now says *reserve the 18+ spot and confirm the price at checkout*, and the status/handoff/report/source-log lines drop an unqualified “free”.
- **Last-return reproducibility (OQ-S1).** Later 11 October Route 186 reads recorded in the source log did not reproduce the Stadium 2194 “20:53/20:54” rows; another later chunk showed only the opposite direction. A reproducibility caveat was added to the three affected transport records and to the transport page and overview checklist: the direction problem (the return terminates at Buġibba Bay 1, not Qawra) and the need for a date-specific planner check are the solid facts; the exact last minute is published-grid evidence requiring confirmation.
- **DAB+ directory wording (OQ-S3).** The claim that the operator directory was “read in full” is withdrawn — it ends in a “Load more” control — so the radio record now says the *visible* listing showed no “Sports Channel” entry and that the absence is not exhaustive.

### Delivery — observed (not predicted)

PR #60 was merged into `main` at **2026-10-11 18:43:26 UTC**; GitHub reports merge commit `b8af702b664893ce00c6d4951c178fd7a1b92190`. Its required check, “Schema, browser and accessibility checks”, passed on the pushed head (`9c8e05a`) in 1 m 13 s, and the PR was `MERGEABLE` before merge. The GitHub Pages latest-build endpoint reports status `built` for the same merge commit. The published `radio.html` was then fetched and contains the new trip-window live-sport table, the BFBS negative bullet and the PBS lead bullet, and the published `index.html` carries the corrected executive-summary line — a browser-level content check of the deployment, not a crawl of every external link and not an RF or service test.

### Still to do next session

1. Confirm the reservation, gate, ID rules, per-day validity, weekend agenda and the 18:00 vs 18:30 opener outlier with the organiser.
2. Run the operator’s date-specific journey planner for each event date and obtain one live taxi/ride-hailing quote for a late return; keep watching for a TQ service during 14–18 October.
3. Scan DAB+ blocks 6A/6C/12A and the listed FM frequencies in Malta, and log service label, block, language and any named match actually heard.
4. Refresh restaurant/gaming hours and menus directly, and re-check entry rules (ETIAS/EES), weather and transit notices on arrival.
5. When the itinerary arrives, enter confirmed amounts only into the planner and save a private JSON backup.


## Previous session — `arena/67d511d1-maltasupplemental` (11 October 2026 UTC)

### Delivery summary

This session reviewed the integrated repository rather than replacing it. The site already contained GitHub Pages-ready static HTML, shared navigation/renderer, responsive tokens, seven topic datasets using the exact 13-field record schema, a master source log, open questions, workstream status, a blank-by-default expense planner and a Playwright/axe suite. `docs/PLAN.md` now records the current session's owners/dependencies and the serial execution limit (Arena provides a single fixed branch, so no separate workstream agents or branches are claimed).

The new work focused on the radio requirement and integration quality. Live official-source checks refreshed the Thunderpick/Eventbrite listing, MPT Route 186/fares/service notices, Transport Malta taxi tariff, AX ODYCY property listing, BBC episode records, NET FM schedule, Rai Radio 1 programme, the Malta DAB+ directory and Radio Sportiva's current weekly grid. The Sports Radio subpage now has a 13–19 October trip-week table and a receiver scan checklist; it separates dated BBC programme starts from recurring NET/Radio Sportiva/Rai schedules and from named-match carriage. The table has a semantic desktop layout and labelled mobile cards. During this work, `main` also merged PR #56, adding a derived seven-day transport plan and timezone-qualified 14 October opening matchups; these are preserved and their remaining gaps are identified below. The rebased tree also preserves a dated TripAdvisor review-volume snapshot for nearby food alongside its count drift, relevance/sponsored-order caveats; this is not a universal rating/popularity ranking. Review-platform access limits remain explicit, and no sentiment is inferred from blocked sources.

### Highest-value verified findings and boundaries

- **Thunderpick / admission:** the official ticketing listing advertises the in-person 18+ event at BLAST Arena Studios Malta, MFCC South Gate National Stadium, Attard, 14–18 October; the displayed ticket card says “Free / Reserve a spot.” Visible agenda rows cover 14–16 October only, and Wednesday/Thursday row end times (22:30) conflict with the 22:00 listing header. This does not establish the user's reservation, current inventory, day validity, attendee gate, or weekend agenda.
- **Event-day transport:** the rebase adds `data/transport.json#event-day-transport-by-date`, rendered at `getting-around.html#event-day-by-date`, with a date-by-date action for all seven days. For Wed/Thu 14–15 October it derives an 08:39 Route 186 departure from Qawra 952, reaching Stadium 6227 around 09:04–09:09 for the listed 09:30 check-in; Friday’s 21:00 finish is still after the last published 20:53/20:54 Stadium 2194 return. The return terminates at Buġibba Bay 1, not Il-Qawra; the plan treats a pre-booked ride as the reliable late-return option and describes the Saturday 17 diversion cluster. These clock comparisons and the ~20:40 boarding recommendation are **derived from static route grids and advertised agenda**, not saved date-specific MPT journeys. The Sat/Sun agenda, attendee gate, both walking legs, onward Buġibba→Qawra service, live quote and any event service remain unverified. Monday departure options (TD1 / Route 214) are listed, not journey-planner results.
- **CS2 opening-match clocks:** `data/event.json#twc-opening-matchups-14-oct` and `event.html#opening-matchups` pin four third-party bracket starts to Malta CEST 10:30, 13:00, 15:30 and 18:00; a separate source-log row still says 18:30 for the last opener. The organizer has not published a per-match running order, so this 30-minute discrepancy remains open and the bracket start is not an event door time.
- **Fares / taxi comparison:** MPT's official page lists €2.50 summer / €2.00 winter day singles and other cards, but the printed seasonal window ends 13 June 2026; the likely 13–18 / 19 October split is secondary-source inference, not operator confirmation. Transport Malta's tariff page gives maximum meter rates but its footer says last updated 06/04/2022; maxima are not a quote. Bus is the only mode with an applicable operator-published price table; ride-hailing, rental total and current taxi price remain live-quote checks.
- **Terrestrial sports radio:** BBC episode metadata gives Sportsworld starts at 15:06 Malta time on 17 Oct and 16:06 on 18 Oct (each 13,980 seconds / 3 h 53 min); the descriptions are general live sport, not named-match assignments. The Saturday programme starts after the 13:30 EPL kickoff and its scheduled duration overlaps later 16:00/18:30 kickoffs; Sunday starts after 15:00 kickoffs and overlaps the 17:30 kickoff by clock only. Radio Sportiva's official grid currently lists weekday/weekend sports programmes at 15:05–17:00, but its specifically dated “Sportiva Live” callouts visible on 11 Oct cover 5–11 Oct, not the user's dates. NET FM and Rai have recurring grids but no verified trip-week named fixture list. A dated 13 January 2026 field observation of Malta's multiplexes lists “Sports Channel” (service ID C02F, 32 kbit/s) on DAB+ **6C (185.360 MHz)** and shows **no sports service on 12A**; an independent Malta directory agrees on the block and ID. The older WorldDAB entry placing a generic “Sports Channel” on 12A is therefore treated as unsupported and superseded; the remaining uncertainty is content identity (a 2023 enthusiast report called it a talkSPORT relay) and what it airs on 17–18 October. **Scan 6C.** No compatible receiver scan, relay-feed check, indoor signal, named match on a Malta frequency or Kalshi-to-broadcast link is verified.
- **Food / social research:** the repository contains source-linked listings and dated review snapshots. Google Maps / TripAdvisor coverage was limited; Yelp, Instagram, TikTok, Facebook, Reddit and X endpoints were blocked or limited in recorded checks. This is not comprehensive review sampling; “most popular” is not represented as a universal ranking.
- **Trip-specific unknowns:** the supplied hotel/room/date information and event intention are user inputs, not booking confirmation. Traveler's exact itinerary, party size/ages, flights, hotel invoice/meal plan, insurance, SIM/device, tickets and personal expenses remain unknown. The planner therefore starts blank and does not assume bookings or spending.

### Passes and observed local gates

1. **Pass 1 — implementation and evidence:** repository/schema reviewed first; preserved the existing topic structure and source-log format; added the trip-week radio view, receiver steps, official Radio Sportiva schedule evidence, and source/open-question entries.
2. **Pass 2 — adversarial review:** corrected the BBC interval language so the pages use verified start times and published duration rather than an unverified end minute; corrected the claim that Sportsworld starts before the Saturday 13:30 or Sunday 15:00 kickoffs; separated recurring Sportiva/NET/Rai grids from dated named matches; resolved the 6C/12A conflict with a dated multiplex observation (6C carries the service; 12A carries none), corrected every page and document that had told the reader to scan both, and separated what is established (label, service ID, block, bitrate) from what is not (content, named match, reception); checked that unknown route, ticket and reception claims remain caveated; added responsive table labels and a browser assertion.
3. **Pass 3 — original-request audit:** after integrating PR #56, checked the user’s transport, review-platform, activity, U.S.-traveler, radio/Kalshi, expense-planner, navigation and source-verification requirements against the merged data/pages/docs; then reran the complete suite on `origin/main` `6da8aba`.

**Local checks after rebase onto `origin/main` `6da8aba` (observed):** `python3 scripts/validate_site.py` passed with 7 datasets / 199 exact-schema records / 319 unique record URLs / 15 HTML pages / 340 link attributes / 9 shared navigation destinations / 25 expense rows. `python3 scripts/check_javascript.py`, `node --check js/site.js`, and `git diff --check` passed. `npm test` passed **23/23**, including axe at 320/360/768/1024/1440 px, the seven-day transport and opening-matchup projections, and radio-table checks at 320/360/720/1440 px. These verify local structure/rendering, not event-ticket availability, external URL liveness, date-specific operations or RF reception.

### Still needed / next-session priorities

1. Confirm the traveler’s ticket reservation, attendee gate, acceptable ID, per-day scanning/validity, accessibility, weekend agenda and venue-local clocks with Hotspawn/Thunderpick. Resolve the 18:00 vs 18:30 outlier for the fourth 14 October opener; neither match starts nor bracket times are door times.
2. Run MPT's journey planner for each event date using the actual hotel and confirmed gate to verify the derived 08:39 outbound recommendation and return alternatives; confirm stop sides, both walks, the Buġibba→Qawra onward connection, 17 October diversion impact and any TQ service. Obtain a live all-in taxi/ride-hailing quote for each late return; do not treat static timetable grids or derived comparisons as a saved journey.
3. In Malta, scan DAB+ 6C and 6A and the listed FM frequencies at AX ODYCY and the event location. Ask BBC/Digi B, Radio Sportiva, NET, Rai, Vibe and the “Sports Channel” operator about the named fixtures; log service, time, frequency/block, language and audio actually received.
4. Refresh restaurant menus/hours/closures, gaming access, museum/event availability, weather and transit notices close to departure. The blocked social/review-platform gap and small Maps/TripAdvisor sample remain research limits.
5. When the itinerary arrives, enter actual booking/receipt values in the planner; check the quick-fill preview, avoid double-counting aggregate and daily rows, and save a private JSON backup (CSV is for spreadsheets/manual entry).

**Delivery state at report draft:** PR #55 is open. This fixed branch is rebased onto current `main` at `6da8aba` and passes the local 23-test suite, but the updated head still needs to be pushed and its required GitHub checks/mergeability observed. No merge or Pages build for PR #55 is yet verified.

---

## Prior mainline report and audit history

## Previous mainline session — `arena/dd9dd00c-maltasupplemental` (11 October 2026)

Passes 1–3 were run on the tree that started at `250e6bd` (PR #48 on `main`). Arena does not allow a second branch, so workstreams A–F were sequential file owners on this branch and G integrated last.

### Verified in this pass

- Eventbrite still advertises the free 18+ in-person listing at BLAST Arena Studios, MFCC South Gate, ATD 4000 Attard, 14–18 October, headline 9:30 AM–10 PM. Friday’s row header reads 2:00 PM–9:00 PM. Saturday and Sunday stay behind “Show all agenda”. The visible lineup names Legacy, Falcons, FURIA, Betboom, 9z and Aurora, then View all. A merge with `main` kept the HLTV, Hotspawn and Liquipedia account that NIP replaced Virtus.pro. Liquipedia’s opening-match block, re-read during the merge, shows Falcons–NIP, 9z–Aurora, Legacy–PARIVISION and FURIA–BetBoom. The 16 September organizer release still named Virtus.pro.
- Thunderpick’s finals page still gives 12–19 October, media day 13 October, groups 14–16, playoffs 17–18, and a $1,000,000 table. It says Malta, not a street address.
- MPT’s fare table still shows €2.50 summer / €2.00 winter day singles, €3.00 night/special/Tallinja Direct, €3.50 TD1, and a €50 fine. The printed winter window is still 19 October 2025 – 13 June 2026.
- Route 186 search excerpts of the operator page still end two Stadium 2194 return grids at 20:53 and 20:54. The service-updates page still shows the 17–18 October 19:00–00:00 diversion, separate from the April notice.
- A separate notice closes Saqqajja stop 4627 on Route 186 until “January 1” with no year. An earlier same-day stop trace places it before Stadium 2194 on the return. This pass did not re-walk that chain. The notice does not say the Stadium or Qawra stops are closed.
- Qawra TripAdvisor Featured order, first three numbered entries: Trattoria Riccardo (4.8 / 2,675), Minoa (5.0 / 765, closed today in that snapshot), Cheeky Monkey Qawra (4.5 / 3,374). Sponsored cards sat above them. Not a review-count ranking.
- BBC Sportsworld JSON still starts 17 October at 14:06 +01:00 and 18 October at 15:06 +01:00, each 3 hours 53 minutes. No named match.
- Government of Malta still lists 230 V, 50 Hz, UK-style three-pin plugs.
- Malta Met Office’s seven-day panel still ends 17 October and matches the retained 13–17 October figures.

Local gates after the merge with `main`: schema/source/link validator passed (7 files, 197 records, 319 record URLs, 15 pages, 311 link attributes, 9 nav destinations, 25 expense rows). Playwright/axe passed 21/21, including 320–1440 px layouts. Tests do not prove external pages stay live or that a bus/radio signal exists.

### Still unverified

Reservation, inventory, gate, weekend agenda, an organizer-page confirmation of the NIP replacement, a saved hotel-to-gate journey, the Saqqajja closure year, the October single fare as an operator quote, physical FM/DAB+ reception, 18–19 October on Malta’s own seven-day panel, and any personal booking or price. Yelp, Instagram, TikTok, Facebook and X were not re-attempted. `main` moved during this session; PRs #51 and #52 were merged in and their food, gaming and entry-requirement records were kept.

### Next session

1. Open the Eventbrite flow and ask Hotspawn for the hidden agenda, FAQ answers and the full lineup.
2. Save both directions in the MPT journey planner for each event day, including the Saqqajja closure and the 17 October diversion.
3. Ask MPT whether the day-route single on 13–19 October is the summer or winter price.
4. If a late return is required, get a live hotel/taxi/ride quote rather than using the 2022 tariff page.
5. Scan DAB+ blocks 6C (the “Sports Channel” and Radio Sportiva) and 6A (Rai Radio Uno, BBC World Service, Vibe, Net FM) at the hotel and venue on a DAB+ receiver.
6. Refresh weather for 18–19 October and any restaurant hours the night before.
7. Paste only confirmed receipts into the blank planner.

## Previous audit — 11 October 2026 (UTC)
**Session branch:** `arena/502e2dae-maltasupplemental`
**Baseline:** `origin/main` at `b307c51` (merge of PR #33), reconciled with `origin/main` at `852343f` (parallel-session PRs #42–47) via a conflict-resolved merge that keeps both sessions' net-new corrections.

## Latest pass — session `arena/d840a59d-maltasupplemental` (11 October 2026)

**Baseline:** `main` at `250e6bd0ea5722cbad5a5ec21fc3117f2eee8fe0` (PR #48 merge), clean tree at session start. All work ran serially on the fixed branch under the existing A–G ownership boundaries.

### What this pass added

1. **The core transport requirement is now answered per date.** `data/transport.json` gains `event-day-transport-by-date`, rendered at `getting-around.html#event-day-by-date`: for each of the seven trip days it states the outbound plan (Route 186 toward Rabat from Qawra 952, 30-minute pattern, Stadium 6227 about 25–33 minutes later), the return constraint (last listed Stadium 2194 departures 20:53/20:54, terminus Buġibba Bay 1 with no Il-Qawra stop), and one action. The 17 October row carries the diversion window and the fourteen-route detour cluster; the 19 October row carries the airport options. Every derived figure — the ~20:40 boarding recommendation and the “no bus return after the finish” reading — is labelled derived rather than verified, and the unknowns (weekend agenda, gate, walks, onward connection, live quotes) are listed inside the record.
2. **Match clocks are now timezone-reconciled instead of assumed.** `data/event.json` gains `twc-opening-matchups-14-oct`, rendered at `event.html#opening-matchups`. A direct read of the bracket report displayed the four 14 October openers at 04:30 / 07:00 / 09:30 / 12:00; a search-index rendering of the same table read the same day displayed 10:30 / 13:00 / 15:30 / 18:00. The two differ by exactly the EDT-to-CEST offset, which pins the Malta local starts at 10:30, 13:00, 15:30 and 18:00 — corroborated by the ticketing listing’s own “games 10:30” row. This corrected this session’s own first draft, which had quoted the later clocks with no zone evidence.
3. **Radio claims were narrowed, not expanded.** The Malta DAB+ operator directory was read in full (38 rendered entries): there is no service named “Sports Channel”, and the only sports-branded entry is Radio Sportiva; a “Load more” control means the absence is still not exhaustive. Vibe FM’s own Malta Premier page still carries the “2025/2026 Season” label with a May 2026 post as its newest entry, so no trip-week Vibe football broadcast is published. TQ1’s page still reads “Timetable not available!”, and the complete service-updates page published no TQ or Thunderpick/BLAST event service.
4. **A new official disruption is recorded:** stop Saqqajja (ID 4627) is closed for construction on Routes 109, 109A, 181, 182, 186, 201, 202, 50, 51, 52, 53, 56 and N52 until about 1 January. It is not the traveler’s boarding or alighting stop, but it affects two venue-corridor routes.

### Verification performed in this pass

| Check | Result |
|---|---|
| `python3 scripts/validate_site.py` | PASS — 7 JSON files / **199** exact-schema records after the latest-`main` merge (transport 30, food 48, activities 47, everyday 19, radio 21, expenses 25, event 9); 319 unique record URLs present in `docs/SOURCES.md`; 15 HTML pages / 325 link attributes; 9 navigation destinations; 25 expense rows |
| `python3 scripts/check_javascript.py` | PASS — shared and inline JavaScript syntax |
| `npx playwright test` | PASS — **22/22**, including the 320/360/768/1024/1440 px layout and axe sweeps and the new test asserting the seven per-date plan rows, their `datetime` attributes, the canonical record rendering and the event matchups deep link |
| Fresh source reads (all 11 October 2026) | Eventbrite listing (full), MPT fares, MPT service updates (all three chunks), Route 186 grids and notices, TQ1, DAB+ operator directory (both chunks), Vibe FM football page, HLTV bracket report |

### Limits that remain

Nothing in this pass is a booking, an admission, a live quote, a physical journey, an RF measurement or a personal purchase. The Saturday/Sunday agenda, the traveler’s reservation, the attendee gate, both walks, the dated Buġibba → Qawra connection, the operator-dated October single fare, any named-match radio carriage and the expense inputs are all still open and are listed in `docs/OPEN_QUESTIONS.md`. Review-platform coverage (Yelp, Instagram, TikTok, Facebook, X, Reddit) remains partial or blocked; no popularity ranking is asserted.

### CS2 event and access

This session ran the requested multi-pass protocol over the integrated tree: **Pass 1** implemented and verified the full request; **Pass 2** reviewed for bugs, missing requirements, incorrect assumptions and edge cases; **Pass 3** re-checked the implementation against the original request and improved accuracy, reliability and completeness. The highest-risk factual claims (event listing, Route 186 return, fare seasons, card terms, radio schedules) were re-verified line by line against live sources on 11 October 2026 before any wording changed. Mid-session, the parallel work merged upstream (PRs #42–47: the `event.html` CS2 event guide + `data/event.json`, the TQ1 special-event-service lead, the Transport Malta taxi-tariff record, AX ODYCY FAQ evidence and an MTA guideline re-read) was reconciled into this branch by content, with both sides' corrections preserved.

The delivered site remains the repository's static, JSON-backed Malta trip guide and blank-by-default expense planner. The seven datasets use the shared exact 13-field schema (key order normalized). Merged-tree counts: **184 records** (transport 28, food 39, activities 44, everyday 19, radio 21, expenses 25, event 8), **303 unique record URLs** in the source log, 15 HTML pages, 219 checked link attributes, nine shared navigation destinations, and 25 expense rows.

This is a sourced planning aid, not a booking, admission, price, service, schedule, or reception guarantee. Dates, hotel, and intended venue are traveler-supplied inputs except where separately corroborated.

## Next session — priority order

### Thunderpick World Championship / admission

The Hotspawn/Eventbrite listing was re-read directly and matches the ticket-section framing recorded in the updated source log: it names *Hotspawn present the Thunderpick World Championships 2026* at BLAST Arena Studios Malta, MFCC South Gate National Stadium, Attard ATD 4000, Wednesday 14 – Sunday 18 October 2026, 9:30 AM – 10 PM, in person, **18+**, with a **“Free”** ticket block and a “Reserve a spot” action under a “Sales end soon” notice. Agenda rows remain visible for Wed 14 / Thu 15 (09:30–22:30) and Fri 16 (14:00–21:00) only; Saturday/Sunday sit behind “Show all agenda”. The headline-vs-rows finish discrepancy (22:00 vs 22:30) persists. Reserve before travel and carry photographic ID. Still open: current inventory, the traveler’s reservation, whether one reservation covers all five days, per-day scanning, transferability, parking/catering, and the attendee gate. The new `event.html` guide (8 records) carries the detailed day-by-day and access material; the Virtus.pro → Ninjas in Pyjamas team substitution remains third-party-reported (OQ-H5) and is labelled as such.

### Public transport — the event-day return problem (core requirement)

The operator’s live Route 186 page was parsed stop by stop, both directions, all published grids:

- **Return (the binding constraint):** the last Stadium 2194 departures toward Buġibba are **20:53 and 20:54** on the published return grids, reaching Buġibba Bay 1 at 21:26 and 21:36. The earlier “one static variant” hedge is replaced: the figure is confirmed on the operator’s current route page. Which grid applies on which trip date is not labelled, so the date-specific planner remains the authority.
- **Outbound:** Qawra stop 952 departures toward the venue run to about 21:39 (Stadium 6227 to about 22:04–22:08); Route 186 reaches the venue in time even for the 09:30 check-in. Getting to the event is not the problem — getting back is.
- **Return path:** the toward-Buġibba direction does not serve any Il-Qawra stop; it terminates at Buġibba Bay 1 (2527), so a second boarding (or walk/taxi from Buġibba) is required. One single fare covers both legs inside the two-hour transfer window.
- **Saturday 17 October detour:** the omitted span “Gholja 2 through Targa” sits **between** the Stadium 2194 boarding stop and the Buġibba terminus on the operator’s own stop lists — the traveler’s boarding and alighting stops are not among the omitted stops. The diverted path and timing remain unpublished, so a particular departure could still be re-timed. Both operator pages read the October window as 19:00–00:00 (an earlier 20:00–24:00 reading was superseded during reconciliation: that window belongs to a separate weekly notice ending 21 April).
- **Late-return leads (unverified, recorded, not claimed as journeys):** Route 202 from the same Stadium 2194 stop toward Sliema is listed on the operator’s route page to about 22:08; night route N212 links Sliema–Buġibba (23:50–01:30); night route N48 is listed at Mosta-corridor stops (Gholja 2, Rotunda 2, Targa) and can be reached via the Ta’ Qali P&R shuttle 405. Moovit’s later 23:07 last-202 figure conflicts with the operator page — logged, operator planner authoritative.
- **One thing could still fix the return:** MPT runs **TQ-numbered special-event services** out of Ta’ Qali for major events (an earlier recorded source lead), and TQ1’s corridor runs through St Paul’s Bay and Qawra to Buġibba at the €3.00 Special Services fare. The TQ1 page displayed “Timetable not available!” when checked and no TWC notice was found — check service updates daily during 14–18 October.
- **Taxi fallback with an honesty caveat:** Transport Malta publishes **maximum** meter rates (initial €3.50, then €2.50/km stepping down to €0.85/km beyond 20 km, €25/hour waiting, €4.20/hour in traffic), but the page footer says “last updated 06/04/2022”. The worked caps on the site (≈€12.40 at 5 km, €19.40 at 10 km, €25.90 at 15 km, €30.90 at 20 km) are this project’s arithmetic at assumed distances, not quotes; the Qawra-to-venue road distance was never measured; ride-hailing is dynamic and unbound by the tariff. Pre-book rather than hail — no taxi rank at an inland studio was verified.

### Fares — a dated conclusion changed by new evidence

The official fares page, re-read 11 October, still prints only the expired winter window “19 October 2025 to 13 June 2026”. The previous audit **rejected** the €2.50/€2.00 split inference because no source stated the season boundary. This session found two independent third-party 2026 fare guides that do state it — summer singles 14 June–18 October (€2.50), winter singles from 19 October (€2.00) — matching the official window’s own 19-October winter start date. The split is therefore reinstated at **“partially verified”** as a planning inference (€2.50 on 13–18 October; €2.00 on 19 October), explicitly labelled as secondary-guide evidence, not operator confirmation, and not prefilled into the planner. Full published table: day single €2.50 summer / €2.00 winter (two-hour transfers), night €3.00, Special Services €3.00, tallinja Direct €3.00, TD1 €3.50, €19 shareable 12-journey card (Night/Airport Direct count 2 journeys per trip), €25 Explore Adult 7-day (excludes tallinja Direct), €21/€27 Explore Flex 4/7-day (include Airport Direct; €6 two-trip airport add-on), €7 Explore Child, €50 fine. Cards sell at Buġibba Terminal, the closest listed office. The fares page **contradicts itself** on whether Explore Adult 7-day includes Airport Direct — disclosed rather than resolved.

### Sports radio

BBC programme pages reconfirm the UK 17–18 October commentary listings (5 Live Sport grid; episode m00334k6; seven named matches including Bournemouth–Sunderland on 5 Sports Extra 2). These remain UK schedules only. The strongest English-language Malta lead is the DAB+ service “Sports Channel” — label, service ID C02F and block 6C confirmed by a dated 13 January 2026 multiplex observation, content still third-party-reported as a talkSPORT relay — a scan lead, not confirmed carriage. NET FM is 101 MHz (Friday 18:30, Saturday 16:00, Sunday 15:00 sports slots); **Vibe FM 88.7 FM / DAB+ is the published Malta Premier League radio partner**; BBC World Service *Sportsworld* episodes are dated on DAB+ 6A; Rai Radio 1’s weekend *Tutto il calcio minuto per minuto* is the most likely live Serie A. No station publishes a dated trip-week named-match lineup; no physical scan was possible; a US HD Radio set cannot decode DAB+ (buy one in Malta). Kalshi’s travel-abroad policy conflict is recorded; no market-to-broadcast link is inferred.

### Everyday life, expenses, food/activities

Everyday content reflects the checked-source refinements recorded earlier in the repository: Type G 230 V/50 Hz (the hotel FAQ adds a **razor-only** 110 V bathroom socket that must not be used for chargers), AX ODYCY’s own 10–15% tipping expectation vs secondary 5–10% guidance (both shown, neither prescribed), and the MTA eco-contribution narrowed by the guidelines’ own “interruption” definition (the 15-day reference is not a minimum-stay threshold) while the webpage wording stays recorded and the invoice remains authoritative (six nights ≈ €9 is conditional). The EES enforcement conflict (EU vs September secondary reporting) remains recorded, not resolved. The expense planner stays blank by default with preview-then-apply quick-fill, autosave, CSV export and reset; the event evenings’ return is planned as taxi/ride-hailing with amounts left to live quotes. Food/activities disclose platform limits (Yelp/Instagram/TikTok/Facebook/X blocked or limited).

## Cumulative verification passes (this session)

1. **Pass 1 — implement/verify:** baseline gates green; every requirement mapped to a page/record; live re-reads produced the findings above; data/pages/docs updated consistently (workstream order, one writer per file per step).
2. **Pass 2 — review:** static and runtime deep-link resolution checked (0 broken); JSON key order normalized to the canonical 13-field order; the fare-inference reversal documented against the previous audit; detour-scope, card-terms and late-return-lead edge cases added; merge reconciliation with PRs #42–47 resolved by content with line-level checks; stale-phrase scans for superseded “static variant”/“fare unconfirmed” wording.
3. **Pass 3 — re-check vs request:** hotel/event/itinerary facts rechecked against the rendered pages; the Kalshi/radio requirement, everyday US-traveler section, expense quick-fill, Pages structure and source-citation requirements reconfirmed; final gates re-run after edits and after the merge.

## Requirement-by-requirement check (merged tree)

| Original request | Where it is answered | Status |
|---|---|---|
| Transport: airport, hotel ↔ BLAST Arena Studios on event days; compare transit/ride-share/rentals on convenience, price, value, feasibility | `getting-around.html`, `data/transport.json` (28 records incl. mode comparison, taxis, rentals) | Answered with a documented return gap and priced fallbacks; no date-specific journey or live quote yet |
| Public transport to the venue on event days | Route 186 Qawra 952 → Stadium 6227 traced; MFCC booklet endorses 186/202/56 | Outbound answered; return limited by the 20:53/20:54 last departures |
| Food/cafés from Google/Yelp/IG/TikTok/FB/Reddit/X, organized in categories/subpages | `restaurants.html`, `data/food.json` (38 records) | Answered within disclosed platform limits |
| Gaming centres, activities, landmarks, events in the trip window | `activities.html` (39 records), `event.html` + `data/event.json` (8 records) | Answered; out-of-window events recorded as excluded |
| Everyday guide (plugs, SIM/eSIM, money/tipping, safety, health, customs, language, weather) | `everyday.html`, `data/everyday.json` (18 records) | Answered; tipping and EES conflicts documented |
| Radio sports broadcasts with verified official schedules; Kalshi-market sports | `radio.html`, `data/radio.json` (20 records) | Partly answered: schedules verified; Malta carriage/reception unverified by design |
| Expense planner template quick to fill when the itinerary arrives | `costs.html`, `data/expenses.json` (25 rows) | Answered — blank defaults + preview-then-apply quick-fill |
| Executive summary, clean desktop/mobile UI, official source links | `index.html`, 9 active pages, shared renderer, axe/Playwright | Answered; 320/360/768/1440 px verified |
| Verify line by line, no hallucinations | `docs/SOURCES.md` (311 URLs), `docs/OPEN_QUESTIONS.md`, per-record confidence | Enforced: validator fails on a record URL absent from the log |
| PR created and merged to `main`; report with suggestions and limitations | This document + delivery snapshot | See below |

## Validation results (observed after edits and merge reconciliation)

- `python3 scripts/validate_site.py` — **PASS**: 7 JSON files / 184 exact-schema records / 303 unique source URLs / 15 HTML pages / 219 link attributes / 9 navigation destinations / 25 expense rows.
- `python3 scripts/check_javascript.py` — **PASS**; `node --check js/site.js` — **PASS**.
- Internal deep-link check (static ids + runtime record ids): **PASS** — 0 broken.
- `npm ci` / `npm test`: **PASS**, 21/21 Playwright on the merged tree (320/360/768/1024/1440 px, axe WCAG 2A/AA/2.1AA, data/render parity, navigation/deep links, planner persistence/CSV/JSON-restore/reset, quick-fill, storage-denial and data-fetch-failure cases).
- `git diff --check`: **PASS**.

These gates check local structure and behavior. They do not certify external-link liveness, current ticket availability, physical access, radio reception, or a dated transit journey.

## Remaining limitations

1. **No reservation, no admission.** The listing says “Sales end soon”; nothing here substitutes for reserving it, and Sat/Sun agenda remains unpublished.
2. **No measured journey.** No attendee gate, no walk distances, no date-specific planner result, no live taxi quote, no verified Buġibba → Qawra connection.
3. **No published trip-week fare** (the likely split is an inference) and a taxi tariff page last updated in 2022.
4. **No radio reception test** and no Malta carriage confirmation for any named match; UK BBC schedules prove nothing about Malta.
5. **Volatile data by nature:** hours, menus, closures, ticket inventory, diversion notices and the forecast can change between this snapshot (11 October 2026) and travel.
6. **Platform coverage is incomplete:** Yelp, Instagram, TikTok, Facebook and X were blocked or limited; social evidence is dated snapshots, not a ranking.
7. **Traveler-specific inputs are absent:** booking confirmation, party size/ages, flights, meal plan, device, insurance, personal spend.
8. **The offline validator is not a web crawler:** a cited URL can rot without the suite noticing.

## Suggestions for the next session (priority order)

1. **Event access (highest value):** ask Hotspawn/Thunderpick to confirm the traveler’s reservation, current inventory, attendee gate, per-day scanning/validity (one reservation for five days?), the 17–18 October agenda, and the 22:00-vs-22:30 finish discrepancy. Re-read the listing daily as the event approaches.
2. **Transit:** run the MPT planner for each event date both ways with the confirmed gate; determine which Route 186 grid (20:53 or 20:54) applies and whether event extra service exists; **check for TQ1/TQ special-event announcements daily during 14–18 October** (the one development that could restore a bus return); verify the after-20:54 fallback legs (202 → Sliema → N212; 405 → Mosta → N48) as date-specific journeys; recheck both diversion pages for 16–17 October; measure the Qawra-stop-to-hotel and Stadium-to-gate walks; obtain one live evening taxi/ride-hailing quote from the venue to Qawra and compare it against the Transport Malta tariff.
3. **Fares:** confirm the likely €2.50 (13–18 Oct) / €2.00 (19 Oct) split with MPT or a sales point; resolve the Explore Adult 7-day Airport Direct contradiction before buying any card.
4. **Radio:** with a DAB+ receiver bought in Malta, scan 6C and 6A and FM at the hotel and venue; record service names, blocks and audio; confirm any named-match carriage with the station (NET FM, Vibe FM, the “Sports Channel”); recheck BBC/Rai/talkSPORT schedules close to air time.
5. **MTA contribution:** the guidelines’ “interruption” reading narrows the question; use the invoice and ask AX ODYCY to confirm the billed amount.
6. **Planner hand-off:** paste the confirmed itinerary into the quick-fill panel (it fills only blank budget fields after preview); export a CSV before switching devices.
7. **Coverage limits:** recheck accessible platforms and volatile menus/hours/closures without implying comprehensive coverage.

Full claim-specific source rows are in `docs/SOURCES.md`; unresolved items in `docs/OPEN_QUESTIONS.md` (including OQ-H5 team substitution); ownership/dependencies in `docs/PLAN.md`; cross-workstream notes in `docs/HANDOFF.md`; the dated claim audit in `docs/AUDIT_2026-10-11.md`.

## Delivery snapshot

Prior observed deliveries on the baseline: pull request **#43** merged at 15:54:56 UTC on 11 October 2026 (`94733df`), with CI and Pages **built** and the live site spot-checked; PRs **#42**, **#44**, **#45**, **#46** and **#47** were already merged to `main` and their relevant updates were reconciled into the baseline. PR #46's recorded full-page read corrected the Route 186 detour window claim (its merge and Pages build were recorded on `main` via PR **#50**). PR **#49** (source-led refresh, planner hardening, expanded test suite) also landed on `main` mid-delivery and was reconciled by content; its records (`food-platform-coverage`, `water-medication-daily-health`, and others) are preserved. This session’s delivery (PR opened, merged by explicit number onto `main`, Pages build) is reported only after those facts have been checked; this file is not a live CI/Pages dashboard.


---

# Session report — `arena/09cdfbf0-maltasupplemental` (11 October 2026)

**Baseline:** `origin/main` at `250e6bd`. **Scope of this session:** re-verification and gap-closing, not a rebuild. The
site structure, planner and evidence discipline were already in place and were reviewed rather than replaced.

## What this session verified

- **Event (corroborated, not merely repeated).** Thunderpick World Championship Finals run **14–18 October 2026** at
  **BLAST Arena Studios, Attard**, eight teams, $1,000,000 pool — independently consistent across HLTV, Liquipedia,
  Hotspawn and the organiser's own release. The **Ninjas in Pyjamas for Virtus.pro** substitution is confirmed as current
  (9 October reporting, corroborated by Liquipedia's event page, which also lists Virtus.pro as a former participant), and
  the groups are Falcons/NIP/9z/Aurora and FURIA/BETBOOM/Legacy/PARIVISION. Published Wednesday 14 October match starts of
  **10:30, 13:00, 15:30 and 18:00 CEST** independently corroborate the ticket listing's "games 10:30" start — and imply a
  plausible late finish, which is exactly why the return journey is the problem.
- **Food.** TripAdvisor's *Restaurants near AX ODYCY Hotel* list was readable on 11 October 2026 and is now recorded ranked
  **by review volume**, not by the platform's display order. Two captures taken minutes apart on different domains already
  disagreed on several counts, which is recorded as evidence that the figures are volatile rather than smoothed over.
- **Gaming.** A dated read of a Malta "Game & Entertainment Centers" directory lists MULTIMAXX, The Eden, Falcon
  Archery, Gravity/Jurassic and Laser Tag Malta (marked *temporarily closed*), and **no public PC-gaming café**. The
  esports association directory likewise lists training and competition venues only.
- **Recreation near the hotel.** Eco Sports Limited (Buġibba) added with **operator-published daily rates** — the first
  near-hotel activity in this project with a real, sourced price list.
- **Radio.** NET FM's own schedule page was re-read live and returned the same three sports-branded slots (Friday 18:30
  *Mhux Premier biss*, Saturday 16:00 *Hits & Score*, Sunday 15:00 *Sports Box*). The DAB+ "Sports Channel" block conflict
  is now wider, not narrower: an encyclopaedia list labels 185.36 MHz DAB+ as **"RAVE Radio"**.
- **Everyday / entry.** The EES conflict now names Malta in specific reporting, and Malta's own airport page still
  describes arrivals being *randomly selected* for a biometric lane. The ETIAS position is unchanged (not in operation) but
  the **risk is now explicit**: official and industry sources targeted Q4 2026, which contains these travel dates, while a
  September 2026 report says that target has been withdrawn.

## What remains unverified

Nothing below was presented as fact on the site, and each item is recorded in `docs/OPEN_QUESTIONS.md`:

1. **Admission.** No reservation was made, no inventory or checkout tested, and the Saturday/Sunday agenda was still not
   visible on the listing. The attendee gate, ID rules, per-day scanning and transferability are unknown.
2. **The return journey.** The 20:53/20:54 last Stadium departures, the Buġibba-only terminus and the Saturday diversion
   stand as recorded; no date-specific journey, no measured walk, and no live taxi quote were obtained.
3. **Trip-week fares.** The €2.50 (13–18 Oct) / €2.00 (19 Oct) split remains a third-party inference, not an operator
   confirmation.
4. **Named-match radio.** No named trip-week match is verified through the full chain of official schedule → Malta carriage
   → compatible receiver → local signal. UK BBC listings prove nothing about Malta.
5. **Popularity.** One platform, one date, one hotel radius, volatile counts. Yelp, Instagram, TikTok, Facebook, Reddit and
   X were unreadable, so there is no sentiment or trend claim for them.
6. **Empire Cinema arcade** is a search-extract lead: no hours, prices or age rules confirmed.

## Corrections made to existing content

- Removed a duplicated paragraph in `ees-malta-implementation-conflict` (the same cross-reference sentence appeared twice).
- Fixed a misspelled record ID (`tripadvisor-near-ax-odyy-…` → `…-odycy-…`) so the public anchor is correct.
- Added cross-references so the three TripAdvisor snapshot records read as three different pages rather than three
  competing claims, and stated that a repeated read by the same method is a stability check, not corroboration.

## Limitations of this session

- **Direct page fetches were mostly blocked** (Eventbrite returned "Something went wrong"; the bus operator's site
  errored). Several new rows are therefore **search-index extracts**, and every one is labelled as such in
  `docs/SOURCES.md`. An extract is weaker evidence than a full page read and has not been dressed up as one.
- **No new primary-source re-read was possible for transport**, so workstream A is unchanged and its open questions stand.
- **Automated gates check structure and behaviour**, not external truth. A passing suite is not a certificate that any
  listing, price, route or broadcast is still current.

## Suggested next-session work, in priority order

1. **Event access** — confirm reservation, gate, per-day validity, the 17–18 October agenda and the 22:00-vs-22:30 finish
   with the organiser; re-read the listing daily as the event approaches.
2. **Entry requirements** — recheck the official EU ETIAS page in the week before departure, and look for a Malta
   government or eu-LISA statement on the EES pause rather than relying on press reporting.
3. **Transit** — run the operator planner for each event date in both directions with the confirmed gate; check for TQ1
   special-event announcements daily during 14–18 October; obtain one live evening taxi quote to compare against the
   published tariff.
4. **Radio** — buy a DAB+ radio in Malta and actually scan 6C and 6A and FM at the hotel and the venue, logging service
   names, blocks and audio. This is the only item on the list that can convert a scan lead into a verified fact.
5. **Popularity and closures** — refresh TripAdvisor counts and the Qawra venue hours/menus close to travel; confirm the
   Empire Cinema arcade directly.
6. **Planner hand-off** — paste the confirmed itinerary into the quick-fill panel (it previews first and fills only blank
   fields), then export a CSV before switching devices.

## Gate results observed for this session's tree

- `python3 scripts/validate_site.py` — **PASS**: 7 JSON files / **196** exact-schema records / **317** unique record URLs /
  15 HTML pages / **234** link attributes / 9 navigation destinations / 25 expense rows.
- `python3 scripts/check_javascript.py` — **PASS**.
- `npx playwright test` — **21/21 passed** (320/360/768/1024/1440 px, axe, data/render parity, navigation and deep links,
  planner persistence, CSV/JSON backup, reset, quick-fill, storage-denial and data-fetch-failure cases).
- Manual Chromium check at 390 px and 1280 px on the three pages changed this session — **zero horizontal overflow, zero
  console errors**, and the new records render.


## Delivery snapshot — session `arena/09cdfbf0-maltasupplemental` (observed)

- Pull request **#51** was opened from `arena/09cdfbf0-maltasupplemental` against `main` and reported `MERGEABLE`/`CLEAN`.
- Its required check **“Schema, browser and accessibility checks”** ([run 38158610565](https://github.com/buffedlizard55-lab/MALTASUPPLEMENTAL/actions/runs/38158610565)) **passed**.
- PR #51 was **merged into `main` on 11 October 2026 at 17:13:35 UTC**, merge commit
  `6859c46efa5053578b41962bed21246ae76fd3aa`, from session head `a20368c`.
- The GitHub Pages latest-build record for that merge commit reports **status `built`**, created 17:13:36 and updated
  17:13:53 UTC.

**What this does not confirm:** this session's network policy allows only GitHub API and package-registry hosts, so
`https://buffedlizard55-lab.github.io/MALTASUPPLEMENTAL/` could not be fetched for a browser-level content check. The Pages
build record above is a GitHub build-state observation only; nobody here loaded the live page and compared it with the
merged tree.
