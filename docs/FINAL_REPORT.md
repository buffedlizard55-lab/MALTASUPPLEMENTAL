# Malta Trip Guide — final report (11 October 2026)

**Guide:** https://buffedlizard55-lab.github.io/MALTASUPPLEMENTAL/
**Delivery PRs:** #35 (`arena/5782956c-maltasupplemental`) merged 11 October 2026 05:19 UTC as `9c3db1f`; this report also covers PR #36 (`arena/10de8b19-maltasupplemental`), rebased onto the current `main`; PRs #31, #32 and #34 merged earlier the same day
**Branch:** `arena/5782956c-maltasupplemental`
**Deployment:** GitHub Pages publishes the `main` branch root. It reported `built` for merge commit `9c3db1f` at 05:19:37 UTC with no error, so https://buffedlizard55-lab.github.io/MALTASUPPLEMENTAL/ serves the merged revision. That is a static-build record, not a browser or device test, and the sandbox network policy prevents fetching the rendered page from here.
**Traveler-supplied planning inputs:** AX ODYCY, Qawra Coast Road, Qawra SPB 1902, Deluxe Sea-View room; 13–19 October 2026; event destination/name “BLAST Arena Studios, Attard.” These details do not independently confirm a reservation, room allocation, ticket, spectator access, exact TWC entrance, or door-to-door itinerary.

## Executive summary

The static, mobile-friendly site includes an overview, six data-backed topic pages, shared navigation, source/open-question/status reporting, and a blank-by-default expense planner. Six canonical JSON datasets contain **140 exact-schema records**: transport 20, food 30, activities/events 33, everyday guidance 17, radio 15, and expenses 25. The canonical schema has exactly 13 record fields, including the exact key `price range`; the current source-type enum is `official`, `map`, `review`, and `social`. Records expose source, check date, confidence, and limitations; page renderers use the data rather than recreating facts.

The refreshed offline validator reports **242 unique record URLs** in `docs/SOURCES.md`, 15 HTML pages, 130 link attributes, 8 shared-navigation destinations, and all 25 expense rows wired. The latest local CI-style run passed all ten Playwright tests, including viewport/accessibility checks at 360, 768, and 1440 pixels. The guide is a dated planning snapshot, not a booking, admission, service, radio-reception, or external-link guarantee.

**Complete fresh line-by-line external verification of every retained historical claim and comprehensive all-platform review coverage remain incomplete.** Unresolved facts are not presented as confirmed; the detailed question list is in [`OPEN_QUESTIONS.md`](OPEN_QUESTIONS.md).

## Deliverables and evidence boundaries

### A · Getting around — 20 records

The transport page and data compare public bus, taxi/ride-hailing, rental car, ferry and other island connections by convenience, published price/value, and feasibility. MPT Route 186 lists Qawra stop 952 toward Ta’ Qali Stadium 6227; the return uses opposite-side Stadium stop 2194 toward Buġibba, not the Qawra seafront. The checked timetable shows a last listed 20:53 departure from Stadium and Buġibba Bay 1 arrival at 21:27. These are static route-table entries, not a dated hotel connection. Route 214 is an alternative to compare; MPT also lists a 17 October evening diversion. Airport Direct TD1 lists Il-Qawra Arznell stop 950 in both timetable directions, with route-level times; the flight-specific departure and walk to AX ODYCY still need a planner check. The current mode-comparison record does not treat an old third-party approximately €25 airport-taxi figure as an official fare. Fares were re-verified directly from the operator on 11 October 2026: single day route €2.50 (summer table) / €2.00 winter with a two-hour transfer window, night/Tallinja Direct €3.00, TD1 €3.50, 12-journey card €19, Explore Adult 7-day €25, Explore Child €7, Explore Flex €21/€27, and a €50 fine without a valid ticket; cards are sold at the Buġibba Terminal, the closest listed office to Qawra. The operator does not print the 2026/27 winter changeover date, so €2.50 is the planning single fare. Ride-hailing coverage was corrected: Bolt is documented as operating in Malta, while Uber’s own Malta airport page and two 2026 third-party guides contradict each other (OQ-27). TWC entrance/walk, exact outward/return route and diversion impact remain open.

### B · Food and cafés — 30 records

The shortlist includes AX ODYCY/on-property, Qawra-area and wider-area options, with current operator/menu facts separated from dated Maps/review/social snapshots. Ratings are not blended into a universal ranking. Reported closures, profile mismatches, conflicting hours, stale menus, and inaccessible-platform results remain qualified; current menus, hours, representative meal totals and availability are not assumed.

### C · Activities, landmarks and events — 33 records

The page covers attractions, recreation/gaming leads, landmarks and dated event listings. It includes the user-supplied base-hotel record, while booking terms remain unknown. The official Thunderpick page gives the overall event window and Malta as the location; a Thunderpick-issued release and separate-event BLAST/venue listings provide venue-area context only. No source confirms the traveler’s ticket, public spectator access, TWC-specific entrance/gate, daily public door/finish times or exact event itinerary. Ticket inventory, event conflicts, some opening-hour conflicts, gaming-venue status and access details remain caveated.

### D · Everyday life — 17 records

Power, language, currency, entry/EES/ETIAS, mobile options, safety/health and weather are sourced and qualified for date and traveler circumstances. Government of Malta and U.S. State Department sources support emergency number 112. Passport, insurance, device/carrier, medicines/customs and other personal advice is not individualized. Power is recorded as Type G / 230 V / 50 Hz with the adapter-versus-converter distinction. The Malta Tourism Authority’s guidelines for the 1 July 2026 eco-contribution were read in full, resolving the “15-night” wording as the €22.50 cap mechanism (OQ-25): €1.50 per night for guests 18+, so six nights implies about €9.00 per eligible adult, subject to the invoice. Two dated forecast snapshots now cover 13–19 October and disagree on 13 October, so the daily Malta Met Office forecast remains the reference.

### E · Malta sports radio — 15 records

The page distinguishes an over-the-air service listing, an official programme schedule, local reception, online streaming, fixture data, and named-match carriage. The Broadcasting Authority lists NET FM at FM 101 MHz; its recurring grid is not a dated match lineup. Malta’s DAB+ directory lists BBC World Service, Rai Radio Uno and Radio Sportiva. WorldDAB lists BBC World Service on block 6A at 181.936 MHz; this technical directory is not an indoor signal test.

Official BBC episode JSON gives Sportsworld first-broadcast times with +01:00 offsets on 17 and 18 October, corresponding to 15:06 and 16:06 Malta time. The programme is general live sport, not a named-match listing (reconfirmed on a later 17 Oct JSON recheck); the 11 October EPL episode is precedent only. Six BBC Radio 5 Live / 5 Sports Extra episode JSON records now **name every trip-weekend UK commentary**: Sat 17 Oct — Manchester City v Ipswich 15:45 Malta (5 Sports Extra), Brentford v Liverpool 16:00 (5 Live), Newcastle v Aston Villa 18:30 (5 Live); Sun 18 Oct — Brighton v Crystal Palace 14:55 (5 Sports Extra), Leeds v Man Utd 15:00 (5 Live), Bournemouth v Sunderland 15:00 (5 Sports Extra 2, newly identified from the Leeds/Brighton episode texts), Nottingham Forest v Arsenal 17:30 (5 Live). The two page-vs-JSON service-label differences are **resolved** by episode long_synopsis cross-references. These UK records do not establish Malta reception, BBC Sounds access, BBC World Service carriage, or a Maltese frequency. Rai’s official weekend football programme has no checked 17–18 October running order. No current AM/MW sports schedule or named carriage of the TWC, Gżira–Mosta, Rolex Middle Sea Race, or a particular EPL/Serie A match **on a Malta-receivable service** was confirmed.

**The “Sports Channel” lead, reconciled across both sessions:** the Radio in Malta directory labels a service “Sports Channel (Talk Sport)” on **block 6C (185.360 MHz)** and Wikipedia’s talkSPORT article lists “DAB+: 6C (Malta)”, but WorldDAB’s Multiplexes table lists a regular “Sports Channel” DAB+ service on **block 12A (223.936 MHz)**, and the Maltese DAB+ operator’s own channel directory lists no sports service at all. Block, service identity, schedule and reception therefore all remain unverified (OQ-28); the page tells the traveller to scan 6A, 6C and 12A and to listen before trusting the name. A full DAB+ tuning guide, Vibe FM’s published Malta Premier League radio partnership and a receiver-compatibility record were added, the last stating plainly that a US HD Radio set cannot decode DAB+ and that the BBC advises buying the DAB+ radio in Malta. Kalshi EPL/Serie A category pages list trip-window fixtures overlapping the radio windows; Kalshi’s own help centre says travel-abroad use is possible subject to its Member Agreement while third-party guidance says US-resident-only, so eligibility stays account-specific. No physical FM/DAB+ receiver scan was available at AX ODYCY or the event area.

### F · Expense planner — 25 blank-by-default rows

The planner provides 18 core trip categories plus seven optional daily templates for 13–19 October, editable euro budget/actual values, notes, totals/difference, browser-local autosave, CSV export, and reset, together with a documented “when your itinerary arrives” intake that maps each confirmed itinerary item to its row. Nothing pre-fills a flight, hotel booking/rate, traveler count, ticket, itinerary, tax amount, or reimbursement. Daily and aggregate rows must not be double-counted. The MTA rate/cap and the “15-night” cap mechanism are now resolved from the guidelines PDF (OQ-25), so the six-night figure (about €9.00 per eligible adult) is stated as a conditional calculation from published rules and never as a personal charge.

## Three cumulative verification passes

1. **Implementation and source pass — passed.** `python3 scripts/validate_site.py` reports 6 JSON files / 140 exact-schema records / 242 unique record URLs / 15 HTML pages / 130 link attributes / 8 navigation destinations / 25 planner rows. `python3 scripts/check_javascript.py` and `node --check js/site.js` pass. All six data files parse as JSON.
2. **Requirements and evidence pass — passed with limitations recorded.** The page/data claims were checked for sources, dates, confidence, contradictions, and open questions. Transport compares mode convenience/price/value/feasibility without promising an event-day hotel connection. Radio sources are not conflated with fixture lists, internet streams, or event schedules. Review/social access limitations and unresolved facts remain visible. This is not a complete new line-by-line re-verification of all older claims.
3. **Integration, responsive and functional pass — passed with limits.** `npm ci` and `npx playwright test` ran in-sandbox and passed **10/10 tests**: active-page rendering and axe checks at 360/768/1440 px, responsive overflow, data/render parity, filters, mobile navigation/deep links, expense defaults/totals/persistence/CSV/reset, itinerary quick-fill preview/apply/overwrite behaviour, invalid input, storage denial/corruption, and failed-fetch behavior. Desktop and mobile screenshots were captured and reviewed for the header, hero, transport, radio and planner views. A physical-device test and a physical radio scan were not available; the validator checks local wiring, not external URL liveness.

After the final documentation conflict commit, `git diff --check` passed and all 23 local HTML/data/CSS/JS/docs endpoints returned HTTP 200. At the post-push pre-merge review, GitHub reported `CLEAN`/`MERGEABLE` and no checks. No external-link crawler was run.

## Platform, date and source limitations

A small number of Google Maps profile views and dated TripAdvisor snapshots informed parts of the shortlist. Direct/retry access to Yelp, Instagram, TikTok, Facebook, X and Reddit was blocked or limited; one batch returned five HTTP 403 responses without reliable endpoint attribution. Text from an official X post was available, but its attached opening-day schedule image was not readable. No inaccessible review, post, or schedule content was inferred. Platform coverage is not comprehensive; see [`SOURCES.md`](SOURCES.md) and each topic page.

Primary and supporting URLs, access dates, and source limitations are recorded in [`SOURCES.md`](SOURCES.md). The claim-level refresh boundary is in [`AUDIT_2026-10-11.md`](AUDIT_2026-10-11.md); cross-workstream discoveries are in [`HANDOFF.md`](HANDOFF.md); unresolved claims and proposed checks are in [`OPEN_QUESTIONS.md`](OPEN_QUESTIONS.md).

## Remaining traveler/organizer checks

1. Confirm TWC spectator eligibility, ticket, exact attendee entrance/pin, and daily public arrival/finish times with the organizer; no public sale was found for these Finals, so ask directly and keep the Twitch/Kick/YouTube broadcast as the fallback (OQ-26). Do not borrow access instructions from another BLAST event.
2. Enter the confirmed hotel and event location/time into MPT’s live planner for each event date; verify stop sides, walks, Route 186 diversion effects, onward Qawra connection, TD1 flight timing, and the operator’s 2026/27 winter fare changeover. Keep a live Bolt/eCabs quote for an unsuitable late return and record which ride-hailing apps actually show vehicles (OQ-27).
3. Run the documented five-minute DAB+ test (blocks 6A/6C/12A) at the hotel: confirm the 6C “Sports Channel” content during the 17–18 October Premier League window (OQ-28), BBC World Service *Sportsworld* on 6A, NET FM on FM 101 and Vibe FM on 88.7 FM, and record what each actually carried.
4. Confirm the hotel voucher/invoice, check-in/out, meal plan, nights/guest ages, flights, traveler count, actual prices and prepaid items before completing the planner. Ask AX ODYCY/MTA about the “15-night” language.
5. Verify passport/ETIAS status, phone/carrier/device compatibility, insurance, and medical/customs needs for the traveler’s circumstances; refresh the 18–19 October forecast and volatile operator/event information.
6. Broaden review/social checks when accessible and recheck all volatile business status, opening hours, menus, and ticket availability before visiting.

## Second 11 October 2026 session — what changed

Working on `arena/96208136-maltasupplemental` after PR #31 merged, this session re-verified the highest-value claims that were still open and corrected one that was wrong:

- **Transport prices (A):** the operator’s own fare table, travel-card terms, sales points and the €50 fine are now recorded exactly; the €2.50 summer single is the planning fare for 13–19 October, with the operator’s failure to print the 2026/27 changeover noted. Five new/upgraded records cover the seasonal window, sales points and ride-hailing, and the mode comparison was repriced.
- **Event admission (A/C) — superseded by the venue-confirmation session:** the earlier negative finding that no public ticket sale or spectator policy existed, and the €10.00 BLAST-event studio-audience ticket precedent, are both replaced. The event’s own ticketing listing now confirms BLAST Arena Studios Malta, MFCC South Gate National Stadium, ATD 4000 Attard, 14–18 October 2026, 9:30 AM–10 PM, in person, ages 18+, with free tickets via “Reserve a spot” (organizer Hotspawn). Thunderpick’s Twitch/Kick/YouTube broadcast remains documented as the remote alternative. See `docs/STATUS.md` and `docs/OPEN_QUESTIONS.md` for the venue-confirmation session record.
- **Radio (E):** the former “unverified” Sports Channel lead became a partially verified talkSPORT carriage listing on DAB+ block 6C at 185.360 MHz, with a full 6A/6C/12A tuning guide and Vibe FM’s Malta Premier League partnership added; the relay’s content stays open (OQ-28). Kalshi’s own vs third-party travel-abroad guidance is recorded as a conflict.
- **Everyday (D):** Type G / 230 V / 50 Hz confirmed with the adapter-versus-converter distinction; the MTA eco-contribution guidelines resolved OQ-25 (cap = fifteen nights) and narrowed OQ-23 to the invoice figure; two dated 13–19 October forecast snapshots were added with their disagreement on 13 October flagged.
- **Expense planner (F):** a nine-step “when your itinerary arrives” intake maps each itinerary item to its row and cites the now-verified bus prices; the hotel-charges and event-access rows were updated without prefilling any personal amount.
- **Corrected:** one travel-reference page consulted in this session wrongly told US travellers that no adapter is needed in Malta; it was rejected and the conflict is logged rather than silently averaged.

## Rebase and delivery state

The second-session branch builds directly on merged `main` (PR #31, merge commit `4ed9c5a`), so no rebase conflict exists. The PR #31 branch reconciled later `origin/main` changes at `81930be`, including the AX ODYCY base-hotel record, the operator night-route notice, seven optional daily expense templates, updated activity/transport/emergency/market evidence, and the upstream browser-test suite. Outdated/duplicate upstream records were not blindly restored where the current main branch intentionally removed them. This rebase completed cleanly, preserves both the current main implementation and trip-specific sourced findings, and leaves the pushed delivery branch five commits ahead of `origin/main` at `81930be`.

At the final pre-merge review, PR #31 was open and GitHub reported `CLEAN`/`MERGEABLE`; `gh pr checks` reported no checks, and no review decision was recorded. Local validation and all nine Playwright tests passed. This report records the state immediately before the merge operation; confirm the merge commit and Pages deployment in GitHub. Existing Pages publication targets the `main` root; a successful static build does not certify external links, admission, transit on the travel date, radio reception, or visual behavior on the traveler’s device.

## Merged third-pass addendum — 11 October 2026

- **Two sessions, one branch.** This delivery reconciles the 11 October session already merged through PR #32/#34 (`ad7226c`) with this session's third pass. All new and changed records were merged record-by-record: the second session's exact fares, admission negative finding, DAB+ tuning guide, power re-verification, eco-contribution resolution, Kalshi eligibility research and Uber conflict are retained side by side with this session's venue confirmation, attendee-status record, customs record, receiver compatibility and fare-value analysis. Where the sessions disagreed, the more cautious reading was adopted and the disagreement is disclosed in the record text.
- **Venue confirmed (this pass):** the Finals run 14–18 October inside the 12–19 October window at BLAST Arena Studios Malta, the studio at the Malta Fairs & Conventions Centre, Ta’ Qali, ATD 4000 Ħ’Attard — corroborated by BLAST’s own guest guide, the VisitMalta business directory and the organizer’s Ta’ Qali-datelined release. Ticket price, public gate, door times and daily match schedule remain unpublished, so attendee access stays the largest open risk (OQ-26).
- **Customs added:** EU entry allowances from the European Union’s official travellers’ page and the U.S. returning-resident exemption from U.S. Customs and Border Protection are now recorded in the everyday guide, closing a stated requirement that had been missing.
- **Expense planner ready for the itinerary:** two complementary hand-offs — a documented intake list and a paste-your-itinerary quick-fill panel that previews every proposed row and writes only to still-blank budget fields, never overwriting typed amounts, and reports unresolvable lines back for a human decision. Amounts still start blank.
- **Evidence counts:** 140 canonical records across six data files; 242 unique record URLs in `docs/SOURCES.md`; 15 HTML pages; 130 link attributes; 8 navigation destinations; 25 expense rows. Gates: validator PASS, JavaScript syntax PASS, Playwright 10/10 PASS.
- **Stated limitations:** organizer attendee access and daily times; the October single-fare season; measured stop-to-hotel and stop-to-gate walks; the 17 October diversion's practical effect; no physical FM/DAB+ scan and no named-match carriage; social-platform review coverage still blocked/limited as logged; 18–19 October beyond the published forecast; external-link liveness outside the offline validator.


## Session `arena/10de8b19` (PR #36) — what changed

Rebased onto the current `main` after the parallel passes merged; this Pass-1/2/3 cycle closed two remaining evidence gaps and fixed one internal inconsistency:

- **Radio (E):** every BBC EPL commentary episode for 17–18 October is now named from official episode JSON with Malta start times, and the page-vs-JSON service-label discrepancy is resolved via the episodes’ own cross-reference texts. A seventh commentary — Bournemouth v Sunderland on 5 Sports Extra 2 — was newly identified inside the Leeds/Brighton episode texts. The Kalshi comparison maps these named windows to named EPL markets (market≠rights, UK-schedule≠Malta-reception caveats retained; the “Sports Channel” block dispute and eligibility evidence from the parallel passes are retained). BBC *Sportsworld* (the Malta-DAB+ service) was rechecked and still has no named match. The radio intro’s earlier certainty about block 6C was aligned with the corrected “block disputed” record.
- **Venue area (A/C):** the 16 September 2026 Thunderpick team-announcement dateline “TA’ QALI, Malta” (PR Newswire) is added to the transport/activities venue records alongside the parallel passes’ guest-guide, ticketing-partner, VisitMalta and press evidence. The TWC attendee pin, entrance, spectator policy and daily public times remain unpublished (OQ-26).
- **Gates:** validator (record counts per the current datasets / all record URLs logged / 15 HTML pages / 8 nav destinations / 25 expense rows), JS checks, `git diff --check`, and `npm test` (9/9 Playwright) re-run on the reconciled tree after each rebase.



---

# Session report — 11 October 2026 (post-#31 verification and enrichment pass)

**Branch:** `arena/58d6d232-maltasupplemental`. PR #31 had already been merged into `main` when this session began, so the branch started at parity with `main` and this work is a forward increment on top of it.

**Note on the figures above:** the counts in the pre-merge section (128 records, 205 logged URLs) describe the state at PR #31. After this session the datasets contain **138 exact-schema records** — transport 18, food 35, activities 33, everyday 15, radio 12, expenses 25 — and `docs/SOURCES.md` logs **215 unique record URLs**.

## What was verified this session

Every item below was read from a primary or named source during this session and is logged in `docs/SOURCES.md`.

- **The venue-name conflict is resolved.** BLAST Arena Studios Malta is the Malta Fairs & Conventions Centre, “MFCC South Gate National Stadium, Millennium Stand, Attard ATD 4000”, physically in the Ta’ Qali area. Sources: BLAST’s own attendee guide, EventWorks, GamingMalta, visitmalta.co.uk. “Attard” and “Ta’ Qali” are the same complex, so the Ta’ Qali bus stops are the correct ones.
- **Route 186 is confirmed from the venue side too.** The MFCC’s own booklet states “BY BUS - FROM VALLETTA no.56, FROM SLIEMA no.202, FROM BUGIBBA no.186”.
- **Route 186 timetable read directly from the operator page.** Buġibba→Rabat calls at Qawra stop 952 then Ta’ Qali Stadium 6227, roughly every 30 minutes from about 06:09 with the last Qawra departure around 21:09; Stadium 6227 arrivals run about 06:34–22:04 in the variant read.
- **Two Route 186 detours, not one.** Both omit stops “from Gholja 2 through Targa” toward Buġibba: one weekly Fri/Sat 20:00–00:00 ending ~21 April, and one weekly Fri/Sat 19:00–00:00 starting 17 October.
- **TWC 2026 field, format and broadcast.** Eight teams (FURIA, Falcons, Legacy, Aurora, BETBOOM, 9z, PARIVISION, Virtus.pro), two GSL BO3 groups feeding a single-elimination bracket, US$1,000,000, streamed on Twitch/Kick/YouTube. Sources: HLTV (2 Oct 2026) and the Thunderpick-issued release.
- **“Sports Channel” on Malta DAB+ block 6C (185.360 MHz) is labelled Talk Sport** by a specialist ensemble listing, corroborated by two independent scanner directories; the Premier League’s own partner page confirms talkSPORT is the only national commercial radio station carrying live Premier League commentary.
- **NET FM’s official weekly grid:** “Hits & Score” Sat 16:00, “Sports Box” Sun 15:00, “Analiżi” Sun 09:45, “Mhux Premier biss” Fri 18:30, at 101 MHz per the Broadcasting Authority.
- **Rai Radio 1’s “Tutto il calcio minuto per minuto” airs Saturday and Sunday** with Serie A/B radiocronache (Rai’s own programme page, episodes listed through 10 Oct 2026). Rai Radio Uno is carried on Malta DAB+ 6A.
- **Fixture times in Malta time** for EPL matchweek 8 (17–19 Oct) and Serie A matchday 7 (16–19 Oct), with the conversion rule stated.
- **Review/community data for Qawra and Buġibba** from TripAdvisor listing pages and r/malta threads, with dates.

## What remains unverified

- **Physical radio reception.** The single largest gap. Every frequency and block comes from a regulator list, a specialist directory or an industry association — none from a measurement at AX ODYCY, in Qawra, or at the venue.
- **“Sports Channel” identity.** The Talk Sport label is directory-grade; no operator or rights-holder confirmation was obtained. Block placement is contested (6C vs WorldDAB’s 12A).
- **Dated trip-week schedules.** No station published a 13–19 October 2026 running order, and no named-match carriage is confirmed for any fixture.
- **TWC access and schedule.** No ticket, spectator policy, entrance, daily match times or finish time has been published by Thunderpick or BLAST.
- **The detour path.** Whether Qawra stops remain served during the Friday/Saturday detours is unknown.
- **October 2026 single bus fare**, the hotel-to-stop walks, and return-direction clock times (Stadium 2194 / 20:53 / Buġibba Bay 1 21:27) — the latter was not re-read this session.
- **Yelp, Instagram, TikTok, Facebook and X.** Still inaccessible to direct requests.
- **Tipping.** No authoritative Maltese source for a standard percentage; deliberately left `unverified`.

## Limitations in the way of a successful project

1. **No on-site measurement is possible from a research environment.** Radio reception, walking routes, bus-stop sides and venue entrances all require a person in Malta with a DAB+ receiver.
2. **Rights and schedules are published late.** Stations typically confirm match selections days ahead, not months, so a trip-week radio schedule cannot be fully verified in advance by design.
3. **The event organiser has published no attendee logistics.** Without door/finish times, event-day transport can only be planned as a range with a fallback.
4. **Several review/social platforms block automated access.** Any “most popular” claim is necessarily partial.
5. **The itinerary has not been provided.** The expense planner is deliberately blank, so no totals can be produced yet.

## Suggested next-session tasks

1. **On arrival:** run a full DAB+ scan at the hotel and record which of Sports Channel, Rai Radio Uno, Radio Sportiva, BBC WS and Net FM appear, on which block, and at what signal strength. Feed the result back into `data/radio.json`.
2. **When the itinerary arrives:** fill the expense planner, then export a CSV backup; add any confirmed flight, ticket and transfer costs as records.
3. **When TWC publishes an attendee guide:** add the entrance, door and finish times, then re-run the MPT journey planner for both directions on 14–18 October and save the actual departures.
4. **Recheck the Route 186 detour path** in the live planner for the event evenings and confirm whether Qawra stops are served.
5. **Open each of the four new food venues' official pages** (Zigumar, Ocean Basket, Ta’ Bertu’s Kitchen, Chatterbox) to replace review-sourced placeholders with operator hours and menu prices.
6. **Re-read the return-direction Route 186 timetable** to confirm or replace the Stadium 2194 / 20:53 / Buġibba Bay 1 21:27 figures.
7. **Refresh the 18–19 October weather forecast** once it enters the Met Office range.

## Verification gates

- `python3 scripts/validate_site.py` → **PASS** — 6 JSON files / 138 exact-schema records / 215 unique logged record URLs / 15 HTML pages / 117 link attributes / 8 navigation destinations / 25 expense rows.
- `python3 scripts/check_javascript.py` and `node --check js/site.js` → **PASS**.
- `npm ci && npm test` → **PASS**, 9/9 Playwright tests, including 360/768/1440 px viewport and axe WCAG 2A/AA/2.1AA checks.
- Manual source spot-checks performed during this session are itemised in the “verified” list above; no claim on the site was accepted on memory alone.
