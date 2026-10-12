<!-- Session addendum appended by the arena/1005fdbf session; historical sections below are preserved. -->
# Delivery status — Malta trip guide

## Current delivery session — `arena/57ad3983-maltasupplemental` (11–12 October 2026 UTC)

**Stage:** Main was fast-forwarded from `ac487ae` to `8799b1b4` (PRs #68–#70). The stash was applied with conflicts in seven files; all seven were resolved by retaining upstream Kalshi, service-notice and forecast material while restoring this branch’s event-price and Route 186 direction corrections. No merge/PR state is inferred below; GitHub delivery is recorded after it is observed. PR #71 remains a separate open branch and was not checked out or merged.

| Workstream | Status | Remaining boundary |
|---|---|---|
| **A · Transport** | Current correction distinguishes Stadium 2194 Buġibba return through 20:53 from outbound Stadium 6227 22:04/22:08 rows; retains the Route 46/260, 54/106, 17–18 October and Saqqajja notices. | No date-specific planner journey, gate/walk, onward Buġibba–Qawra connection, confirmed notice effect, trip-week fare or live ride quote. |
| **B · Food & cafés** | TripAdvisor search scope and five directly re-read profiles are described as a mutable sample, not a Qawra-only ranking; platform limits remain explicit. | Menus/hours/trading and blocked-platform coverage require direct checks. |
| **C · Events & activities** | Eventbrite listing separated from generic recommendation card; no event-specific checkout price/reservation is claimed. | Booking/inventory, ID/day validity, gate, weekend doors/finish and FAQ answers remain unknown. |
| **D · Everyday guide** | ETIAS wording is trip-specific and date-qualified; EES remains separate; Malta national 13–18 October panel and UK Met Office long-range snapshots are kept distinct. | Recheck entry and weather; no Malta national value for 19 October, sea-state or marine warning was checked. |
| **E · Sports radio** | Mainline Kalshi market data and official schedule material retained; listings are not presented as carriage or reception. | Named-match Malta carriage, receiver compatibility and physical signal remain unverified. |
| **F · Expense planner** | Blank-by-default rows and preview-based quick-fill retained. | Populate only after actual bookings, itinerary, party and receipts/quotes arrive. |
| **G · Integration** | Executive summary, pages, data, source log, open questions, handoff and three-pass plan aligned; current `npm test` and whitespace gate pass. | PR and GitHub Pages state to be added only after observation. |

**Gate results (12 October 2026 UTC):** `npm test` PASS — 7 JSON files / 218 exact-schema records / 351 unique record URLs / 15 HTML pages / 374 link attributes / 9 shared navigation destinations / 25 expense rows. JavaScript syntax PASS; Playwright **26/26 PASS**, with axe at 320/360/768/1024/1440 px. `git diff --cached --check` PASS. Tests do not verify current external facts, live inventory, actual route operation, radio carriage or physical reception.

## Previous session addendum — `arena/2b38c9c6-maltasupplemental` (11 October 2026; retained history)

**Stage:** Passes 1–3 on the integrated tree. Repository review complete; changes limited to the files each workstream owns, with documentation and tests integrated last.

| Workstream | Status | Blockers / next check |
|---|---|---|
| **A · Transport** | Operator service-updates feed re-read end to end. Two trip-window notices — Routes 46/260 Mon–Thu 21:00–05:00 (12–16 October) and Routes 54/106 daytime Attard detours (13 October) — are now detailed in their own record; they had previously appeared only as a passing mention inside the 17 October diversion record. Fares page unchanged; TQ1 still prints “Timetable not available!”. | Whether either new notice touches a stop on the Qawra ↔ Ta' Qali journey needs the date-specific planner; no event-specific service is published; trip-week fare split still an inference. |
| **B · Food & cafés** | No new platform evidence; Yelp 403, Reddit 403 and Google Maps' JavaScript shell re-confirmed this session. | Platform limits unchanged; venue hours/menus and the Empire Cinema arcade lead still to re-confirm. |
| **C · Gaming, landmarks & events** | Eventbrite listing re-read with no change to venue, dates, agenda rows or the hidden Saturday/Sunday rows. | Reservation, door times, weekend agenda, gate and FAQ answers remain unpublished. |
| **D · Everyday guide** | Second Met Office Valletta read covering 13–21 October recorded alongside the earlier snapshot. | Forecast values are indicative; national-panel coverage of 18–19 October still not published. |
| **E · Sports radio** | Kalshi market listings now verified from the exchange's own read-only API and published as a market-versus-radio table; no Thunderpick fixture listed in the sampled open CS2 games. | No named match is yet verified on a Maltese frequency, and no receiver scan has been made. |
| **F · Expense planner** | Unchanged; 25 rows blank by design and covered by tests. | Itinerary and amounts still to be supplied by the traveller. |
| **G · Integration** | New records, page sections, quick links, source rows, open questions, README and this ledger updated; regression test added for the market-versus-radio distinction. | Local gates re-run below; PR opened and merged by explicit number, with the observed Pages state recorded in `docs/FINAL_REPORT.md`. |

**Gate results (11 October 2026–12 October 2026 UTC, this session):** `python3 scripts/validate_site.py` PASS — 7 JSON files / 218 exact-schema records / 353 unique record URLs / 15 HTML pages / 377 link attributes / 9 navigation destinations / 25 expense rows.

**Delivery (observed):** PR #69 rebased onto `main` `4725130` (one `docs/PLAN.md` conflict resolved by content), required check “Schema, browser and accessibility checks” SUCCESS, merged **2026-10-12T00:10:37Z** as **`926c33b7`**; Pages build for that commit reports `built`, and the deployed `radio.html` and `getting-around.html` were fetched to confirm the new section and record render. A post-merge Pass 2 correction (two notices were already mentioned in passing inside `route-186-oct17-detour`; now corrected everywhere to “detailed in full, not first observed”) ships in the follow-up PR recorded in `docs/FINAL_REPORT.md`. `python3 scripts/check_javascript.py` PASS. `npx playwright test` — 26/26 after the new regression test was added (25 passed before it).


## Current session addendum — `arena/9bd7eeb7-maltasupplemental` (11 October 2026)

**Stage:** Pass 1 (implement and verify), Pass 2 (adversarial review) and Pass 3 (full re-check against the request) run in that order on `origin/main` `ae69ab1`. Gate results are recorded in the section below. The GitHub PR is the source of truth for merge state.

| Workstream | Status | Blockers / next check |
|---|---|---|
| **A · Transport** | Route 186 re-read: stop index (chunks 1–3), timetable grids (chunks 12, 13, 15), service-update notices, taxi tariff re-checked. Qawra 952 kept as a 06:09–06:10 range. | Stadium 2194 return 20:53/20:54 not reproduced this session (OQ-S1); no date-specific planner result; late return still needs taxi or ride-hail. |
| **B · Food & cafés** | No new platform evidence. Social platforms returned HTTP 403 again (OQ-S4). | Yelp, Instagram, TikTok, Facebook and X absent; no universal ranking. Menus, hours and closures to reconfirm. |
| **C · Gaming, landmarks & events** | Eventbrite, Thunderpick, HLTV and Liquipedia re-checked. NIP for Virtus.pro and Attard venue confirmed. | Weekend agenda hidden; reservation and gate unconfirmed; Esports Kingdom “Valletta” excerpt conflicts (OQ-S6). |
| **D · Everyday guide** | ETIAS not in operation (EU page); EES fully operational from 10 April 2026 (EU FAQ); eco-contribution (€1.50 per night, €22.50 cap) re-checked. | Invoice itemisation (OQ-23); separate EES secondary-reporting conflict as stated in the record. |
| **E · Radio** | BBC Sportsworld 17 October 14:06 BST = 15:06 Malta re-checked; regulator FM list and 6C re-checked; DAB+ directory corrected to first page only. | Sports Channel block unresolved (OQ-28); no named-match carriage verified; Kalshi Member Agreement not opened (OQ-S5). |
| **F · Expense planner** | Unchanged. Amounts blank by design; 25 rows wired per validator. | Itinerary not yet supplied. |
| **G · Integration** | This session's blocks added to PLAN, STATUS, HANDOFF, OPEN_QUESTIONS and SOURCES. Previous session headings relabelled as previous. | Gates in the next section. |

**Gate results (11 October 2026, this session):** validator PASS; JavaScript check PASS; Playwright 23/23 passed. Details in `docs/PLAN.md` "Current session plan".

## Current session addendum — `arena/1005fdbf-maltasupplemental` (11 October 2026)

**Stage:** Passes 1–3 complete on the branch; radio workstream verified and committed; full local suite run. PR opened from this branch and merged to `main`; the Pages build for the merge commit is reported as observed, not assumed.

| Workstream | Status | Blockers / next check |
|---|---|---|
| **A · Transport** | Route 186 diversion dated to a 17-October start; three unlabelled timetable variants recorded instead of a single last-bus figure; Route 405 and the MFCC switchboard added; Uber URL recorded as a dead end | No date-specific planner run, no confirmed gate, no measured walks; trip-week fare season still rests on third-party evidence; TQ event service still unpublished |
| **B · Food & cafés** | Community picks from six r/malta threads added as a dated, unranked shortlist drawn from search extracts | Direct reddit.com access is 403 here; Yelp, Instagram, TikTok, Facebook and X remain unreachable; no venue checked for current trading |
| **C · Activities, gaming, landmarks & events** | Three dated events added (Gozo kite festival, Studio Theatre, Malta Comic Con at MFCC) | Aggregator-only listings; Gozo logistics and Studio Theatre venue unverified; no PC-gaming café exists in the verified record |
| **D · Everyday (U.S. traveller)** | State Department advisory, consular contacts, safety and STEP section added; all eight requested topics have records | EES/ETIAS status remains date-sensitive and conflicting; mobile/eSIM and weather records stay partially verified |
| **E · Sports radio** | DAB+ block question resolved to 6C with dated observations; 12A claim superseded and purged from every surface; block map and corrected row live | What “Sports Channel” airs on 17–18 October is unverified; no receiver scan; no station publishes a trip-week named-match list |
| **F · Expense planner** | Unchanged this session — blank by design, quick-fill preview, CSV/JSON backup, covered by tests | Nothing to plan until the traveller's actual itinerary and amounts are entered |
| **G · Shell, executive summary, integration** | Overview, README, final report, handoff, open questions and source log corrected; anchor sweep clean | Live Pages rendering still to be confirmed after merge |

**Evidence delta this session:** 199 → 212 exact-schema records; 314 → 322 logged record URLs.

**Last updated:** 11 October 2026 (UTC)
**Current session branch:** `arena/3031b29b-maltasupplemental`
**Snapshot boundary:** the addendum directly below is this session; later sections are historical mainline snapshots, not a live dashboard.

## Current session addendum — `arena/3031b29b-maltasupplemental` (11 October 2026)

**Stage:** Passes 1–3 executed on a tree started from `main` `ae69ab1`; local gates run; **delivered as PR #60** (merged to `main` at 2026-10-11 18:43:26 UTC, merge commit `b8af702b664893ce00c6d4951c178fd7a1b92190`), with the required “Schema, browser and accessibility checks” job **passing** at 1 m 13 s on the pushed head and the GitHub Pages latest-build endpoint reporting `built` for that same merge commit. Two parallel sessions merged during the pass (PRs #58, #59); both were integrated with their blocks preserved and their three corrections folded in. The public radio page was then fetched and confirmed to render the new trip-window live-sport table — a browser-level content check of the deployment, not an external-link or reception test.

| Workstream | Status | Blockers / next check |
|---|---|---|
| **A · Transport** | Service-updates page re-read a fourth time (17–18 October cluster enumerated: Routes 186, 202, 260, 47, 103, 45, 405, 238, 203, 280, 31, 41, 42, 48, N48); TQ1/TQ2 definitions and the March 2026 Ta' Qali special-service precedent added; fares page re-read unchanged | No TWC/TQ notice published; date-specific planner run, attendee gate, measured walks, onward Buġibba→Qawra leg and a live taxi quote still open; Friday 16 October diversion question unresolved |
| **B · Food & cafés** | One data-integrity fix: the `espresso-odycy` record (hotel 24/7 coffee bar) was carrying Minoa's hours, address, menu URL and review figures; it was rebuilt from the operator's own Espresso page fetched 11 October 2026 and a regression test now guards the separation. Otherwise unchanged — dated TripAdvisor review-volume snapshot and access limits retained | Platform refreshes (Yelp/Instagram/TikTok/Facebook/Reddit/X) remain unavailable; menus, hours and closures need direct reconfirmation |
| **C · Gaming, activities, landmarks & events** | Ticketing listing re-read 11 October: still “Sales end soon”, ages 18+, venue coordinates 35.8957343/14.4168839, six visible lineup names plus “View all”, Sat/Sun agenda still hidden; the word “Free” appeared only on a “You might also like” card in this read, so the price stays flagged for checkout | Reservation/inventory, gate, ID rules, per-day scanning, weekend agenda and the 18:00 vs 18:30 opener outlier stay open |
| **D · U.S.-traveler essentials** | Weather record extended: national panel corroborated by a second Maltese outlet for 13–17 October and three third-party forecasts read for 18–19 October, labelled as leads | Personal entry/insurance/device facts unknown; 18–19 October still outside the national panel |
| **E · Sports radio** | Three new records (BFBS Radio 2 non-Malta negative; PBS Radju Malta/Radju Malta 2 carriage lead; trip-window sport calendar) and a new dated trip-window live-sport table; EPL fixtures independently corroborated; talkSPORT “DAB+: 6C (Malta)” infobox lead recorded | No receiver scan, no confirmed Malta carriage of any named match, “Sports Channel” identity still unresolved, no radio carriage proven for the NFL London game |
| **F · Expense planner** | Unchanged: blank by default, quick-fill preview, local-only autosave, CSV export, validated JSON backup | Await the itinerary; enter only confirmed amounts |
| **G · Shell / integration** | Executive summary and radio hub updated; source log, open questions, handoff, plan, status and README refreshed; full local suite run before delivery | Push branch, open PR, merge by explicit number, then record the Pages build |

**Parallel-session integration:** `main` advanced twice during this pass (PRs #58, #59). Conflicts in `README.md`, `docs/HANDOFF.md`, `docs/OPEN_QUESTIONS.md`, `docs/SOURCES.md` and `docs/STATUS.md` were resolved by keeping both sessions' blocks, and three upstream corrections were folded in: the Eventbrite “Free” wording is now qualified everywhere, the 2194 last-return rows carry a reproducibility caveat (OQ-S1), and the DAB+ directory claim is now “visible list, not exhaustive” (OQ-S3).

**Fresh evidence (11 October 2026 UTC, this session):** Wikipedia talkSPORT frequency infobox (“DAB+: 6C (Malta)”) and its “every Premier League match” international-audio statement; BFBS Radio 2 schedule with live EPL commentary entries; BFBS frequency tables with no Malta row; the Radio Malta article’s 31 March 1979 BFBS-Malta closure; PBS/FIFA-EBU radio carriage described by a rights directory; three sports calendars for the trip window; The Athletic’s NFL London kick-off clock; BBC Sport, Sky Sports and a UK TV listing for the 17–19 October EPL clocks; the Wikipedia special-services table for TQ1/TQ2; a March 2026 Ta’ Qali special-service news report; Times of Malta weather page; holiday-weather and weather25 18–19 October leads; the Eventbrite listing; and the operator’s service-updates, fares and Route 186 pages. Every URL and its limit is in `docs/SOURCES.md`; unresolved claims are in `docs/OPEN_QUESTIONS.md`.


**Last updated:** 11 October 2026 (UTC)
**Current session branch:** `arena/b29d95ae-maltasupplemental`
**Snapshot boundary:** Current-session addendum below; later sections are historical mainline snapshots, not a live dashboard.

## Current session addendum — `arena/b29d95ae-maltasupplemental` (11 October 2026)

**Stage:** Delivered. PR #64 merged to `main` at 2026-10-11 19:10:02 UTC as `60fea6d` after rebasing through `614a67b` (PRs #56–#66 integrated, including the parallel 6C radio-block resolution); the Pages latest-build endpoint reports `built` for that commit. Repository reviewed at `main` `ae69ab1` (PR #55 merge tip); shared setup (schema, shell, CSS, source-log format, planner, CI, tests) verified present and left intact. Workstreams ran serially on this fixed Arena branch with the established file-ownership map; cross-stream findings went to `docs/HANDOFF.md`. Time-critical sources re-read (Eventbrite, MPT updates + fares, Liquipedia bracket, BBC Sportsworld/Sportsound, EU ETIAS FAQ, met panels, one platform access check); Passes 1–3 and the local suite are the gates before the PR.

| Workstream | Status | Blockers / next check |
|---|---|---|
| **A · Transport** | Full service-updates re-read; two-notice Route 186 distinction reconfirmed; fallback-route stop detail for the Sat 17 cluster added to the night-routes record. Rebased onto main's three-variant timetable finding (OQ-S1) | No date-specific planner run, gate walk or live quote; “April 21” year, the exact last departure and TQ services still open. |
| **B · Food & cafés** | Platform-coverage record updated: Yelp re-attempted today, still HTTP 403 | Counts drift; other platforms remain blocked/limited; reconfirm hours/menus in person. |
| **C · Gaming, activities & event** | Weekend match clocks now pinned from a direct bracket read (SF 16:00/19:00 Sat; 3rd 13:30 + Final 17:00 Sun); garbled search-extract pairing discarded | Organizer Sat/Sun door rows, FAQ answers, reservation/inventory remain open. |
| **D · U.S.-traveler essentials** | ETIAS record tightened to the trip-week answer (not in operation; no action required; several-months notice promise) | EES Malta conflict open; weather panels disagree for 13th/18th; national panel 18–19 coverage unverified (AccessDenied). |
| **E · Sports radio** | New record: named BBC Radio Scotland weekend commentaries (Dundee v Rangers, Celtic v Hearts) with official programme IDs; 5 Live record corroborated. Merged with the parallel sessions' 6C resolution — no block conflict remains | UK output only — no Malta carriage, reception or named-match chain; undated Thursday Benfica v Celtic row stays a lead; what 6C's “Sports Channel” airs is still open. |
| **F · Expense planner** | Unchanged, blank-by-default; verified untouched by this pass | Awaiting the traveler's itinerary and receipts. |
| **G · Integration (last)** | Exec summary, README recheck note, source log, handoff, open questions and this status updated; full local suite is the pre-PR gate | Open the PR from this branch, merge by explicit number, observe Pages build, write the session report. |

**Fresh evidence (11 October UTC, delivery session):** Eventbrite full read; Liquipedia bracket all seven chunks (EDT-labelled clocks converted +6 h to Malta); MPT latest-service-updates all three chunks and fares page; BBC Sportsworld `p002w5vq` and Sportsound `b0079g4q` upcoming pages plus episode `m00334k6`; EU ETIAS FAQ; UK Met Office Valletta panel (updated 10 Oct 12:27); Malta met office 7-day URL AccessDenied; Yelp 403. Exact rows are in `docs/SOURCES.md` under the `arena/b29d95ae-maltasupplemental` header.

## Previous session addendum — `arena/08099cd9-maltasupplemental` (11 October 2026)

**Stage:** verification pass complete on the branch from `ae69ab1` (equal to `origin/main`). Local gates were green before the edits (validator, JavaScript check, 23/23 Playwright).

| Workstream | Status | Blockers / next check |
|---|---|---|
| **A · Transport** | Fares page re-read: €2.50 summer and €2.00 winter wording, €19 / €25 / €21 / €27 products and the €6 Airport Direct add-on match the record. | No saved hotel-to-venue journey; timetable grids not re-read; the 19 Oct winter switch is not a printed 2026/27 changeover; no live taxi quote. |
| **B · Food & cafés** | No new reads. | Yelp, Instagram, TikTok, Facebook, Reddit and X direct access still blocked or unverified. Not a universal popularity ranking. |
| **C · Event & activities** | Organiser page, Eventbrite, HLTV NIP and talent articles, and Liquipedia extract re-read. Dates, format, NIP replacement and CEST clocks confirmed. The “Free” claim is now recorded with its actual evidence. | Ticket-block price, inventory, Saturday/Sunday agenda and whether one reservation covers all days remain unconfirmed. Organiser's own page does not list team names, so team evidence is third-party. |
| **D · Everyday** | ETIAS official page re-read: not in operation. | Pre-departure recheck of ETIAS and EES (the EES conflict is still open). |
| **E · Sports radio** | Radio In Malta directory re-read: talkSPORT labelled “Sports Channel” on DAB+ (no block). Radio Sportiva is listed on DAB+ with no block. | No receiver scan; no named-match carriage on a Malta multiplex; 6C vs 12A still conflicting. |
| **F · Expense planner** | Unchanged. | Needs the traveler's itinerary and confirmed charges. |
| **G · Integration** | Session notes, SOURCES, OPEN_QUESTIONS, HANDOFF and README updated; gates rerun. | PR and merge are recorded in the final report. |

**Corrections made this session:** the event-ticket note no longer says the ticket block showed “Free” on this read (HLTV corroborates free entry instead).

**Not claimed:** no Google reviews, Yelp, Instagram, TikTok, Facebook, Reddit or X access was achieved in this session; the Thunderpick root domain returned 401 to the fetch tool.

## Previous session addendum — `arena/67d511d1-maltasupplemental` (11 October 2026)

**Stage:** Passes 1–3 and the full local suite are complete on the tree rebased onto `origin/main` `6da8aba` (including PRs #51–#56). PR #55 is open; the updated head still needs to be pushed and its required checks/mergeability re-observed. Pages verification is pending.

| Workstream | Status | Blockers / next check |
|---|---|---|
| **A · Transport** | Latest-main per-date plan covers 13–19 Oct, with a derived Route 186 outbound and a clear late-return constraint; key MPT/Eventbrite/taxi sources re-read | No date-specific MPT planner result, confirmed event gate, measured walks or onward Buġibba→Qawra link; weekend agenda, late bus alternatives, live quote and TQ service remain open. |
| **B · Food & cafés** | Latest-main food shortlist plus dated TripAdvisor review-volume snapshot retained; count drift and Featured/sponsored-order limits are stated | Google Maps/TripAdvisor sampling limited; Yelp, Instagram, TikTok, Facebook, Reddit and X direct refreshes are blocked/limited in recorded checks; no universal rating/popularity ranking. Reconfirm menus, hours, closures. |
| **C · Gaming, landmarks & events** | Latest-main event desk includes the 14 October opening matchups with clocks converted to Malta local; activities/popularity additions retained | Organizer agenda still hides 17–18 Oct times; fourth opener has an 18:00/18:30 source outlier; reservation, gate and volatile hours remain unconfirmed; no current walk-in PC café verified. |
| **D · U.S.-traveler essentials** | Existing official-source guide retained | Personal entry, insurance, room/equipment, phone plan and invoice remain unknown; weather is a dated forecast, not guarantee. |
| **E · Sports radio** | Fresh BBC/NET/Rai/Radio Sportiva/DAB source reads; added a 13–19 Oct listening table, receiver checklist and recurring Radio Sportiva weekday/weekend grid; recorded the competing 6C/12A/RAVE listings | No receiver scan, local reception or named-match Malta carriage confirmed; Sports Channel identity/block and exact relay content remain unresolved. |
| **F · Expense planner** | Existing blank-by-default quick-fill, totals, local save, CSV and validated JSON backup retained; not prefilled | Await actual itinerary/party/booking data; only enter confirmed quotes and charges. |
| **G · Shell / executive summary / integration (last)** | Latest-main overview, per-date transport, timezone-pinned matchup and popularity updates preserved; radio table remains mobile-labelled; local gates pass | Push the rebased fixed branch, refresh PR #55 checks/mergeability, then merge and record the Pages build. |

**Fresh evidence (11 October UTC):** Eventbrite listing; Thunderpick official phase page; MPT Route 186, fares and latest service notices; Transport Malta taxi page (footer 06/04/2022); Digi B operator directory; WorldDAB; Radio in Malta 6C; 2023 RadioBlog 6C observation; conflicting RAVE/185.36 list; BBC episode JSON and upcoming list; NET FM weekly grid; Radio Sportiva official weekday/weekend grid; Rai programme page; AX ODYCY property page. Exact URLs and limits are in `docs/SOURCES.md`; unresolved claims are in `docs/OPEN_QUESTIONS.md`.

**Local gates after rebase (observed on `6da8aba`):** `validate_site.py` passed with 7 datasets / 199 exact-schema records / 319 source-log URLs / 15 HTML pages / 340 link attributes / 9 navigation destinations / 25 expense rows; JavaScript syntax and `git diff --check` passed. `npm test` passed **23/23**, including axe at 320/360/768/1024/1440 px, the per-date transport/opening-matchup test, and the radio-table test at 320/360/720/1440 px. These are local software checks, not external truth, dated transport operations or RF reception guarantees.

## Previous mainline session snapshot — `arena/dd9dd00c-maltasupplemental`

| Workstream | Status | Blocker |
|---|---|---|
| A · Transport | Route 186 20:53/20:54 grids, October 17–18 19:00–00:00 diversion, and fare table re-read. Saqqajja stop 4627 closure added as partially verified. | No saved hotel-to-gate journey. Closure year and effect on Stadium stops not printed. |
| B · Food | Qawra TripAdvisor Featured snapshot updated with sponsored cards and numbered entries 1–3. | Yelp, Instagram, TikTok, Facebook and X were not re-attempted. Not a popularity ranking. |
| C · Activities / event | Eventbrite and Thunderpick pages re-read. Visible lineup is six names plus View all. HLTV, Hotspawn and Liquipedia say NIP replaced Virtus.pro. | Sat/Sun agenda, inventory and reservation remain open. The 16 September organizer release still named Virtus.pro. |
| D · Everyday | Gov.mt electricity wording and Malta Met Office panel through 17 October re-read. | 18–19 October national panel still absent. Valletta longer view not re-opened. |
| E · Radio | BBC JSON offsets reconfirmed (14:06 and 15:06 +01:00). Premier League kickoffs re-read. | No named match heard on a Malta receiver. |
| F · Expenses | Adapter/radio keywords added. Amounts stay blank. | Traveler itinerary not supplied. |
| G · Integration | Overview rewritten for scanning; hubs replace retired redirects. Delivery follows the local test run. | Physical transit, radio scan and external-link crawl remain out of scope. |

The sections below are earlier session snapshots, not this session’s live status.

**Previous snapshot updated:** 11 October 2026 (UTC)
**Session branch:** `arena/cc913a9b-maltasupplemental`
**Snapshot boundary:** Updated after observing PR #46 merge and its GitHub Pages build on 11 October 2026 (UTC); this is still a dated snapshot, not a live dashboard.

## Integration and delivery

- The session began at `b307c51`. Upstream PRs #42 (`5cdea68`), #43 (`94733df`), #45 (`dc2fe82`), #44 (`c7d1d00`), #47 (`852343f`) and #49 (`12578cd`) are merged to `main`; the current upstream tree has been integrated on this branch.
- PR #49 adds an expanded source-led guide, keeps all upstream event/hotel changes, adds safe JSON expense backup/restore, and broadens the automated review suite. Its evidence scope and historical pass details are preserved in the audit/history docs.
- The delivery head `3ad5100` incorporated `main` through PR #49 at `12578cd`, retaining the exact schema and upstream record IDs. The latest MPT extraction separates the April 20:00 diversion from the October 19:00 notice and notes that the latter excerpt lacks a year. Static Route 186 evidence is not a full-network last-bus finding; no taxi is assumed as mandatory.
- GitHub Pages latest-build endpoint reported build `1276765781` for merge commit `25e01762d310bdc71deaa9dc9602f96a7d4565f9`, status `built`, created 16:38:04 and updated 16:38:24 UTC. The Pages API reports the public URL `https://buffedlizard55-lab.github.io/MALTASUPPLEMENTAL/` and source `main` `/`; this is a GitHub build-state observation, not an independent browser/content check.
- A fresh MTA guest-facing notice plus the 2026 guidelines support €1.50/night for eligible 18+ guests, capped at €22.50/visit and separately itemized. The general MTA service page still has anomalous “exceeded fifteen nights” wording; OQ-25 treats that as a webpage anomaly, not a short-stay exemption. A six-qualifying-night €9 figure is conditional arithmetic, never a personal invoice.
- PR #46 was merged to `main` on 11 October 2026 at 16:38:02 UTC. GitHub reports merge commit `25e01762d310bdc71deaa9dc9602f96a7d4565f9`, from session head `3ad510058c77c41cf2920949b4047d921d870578`. Its “Schema, browser and accessibility checks” run passed at 16:37:43 UTC; the PR was `CLEAN` and `MERGEABLE` before merge.

## Workstream status

| Workstream | Status | Remaining traveler/source checks |
|---|---|---|
| **A · Transport** | Route and fare evidence qualified | Confirm event gate/finish; save dated MPT journeys in both directions; verify stop sides, safe walks, October notice year and applicable single/card terms. TQ1 has no timetable. No live taxi quote. |
| **B · Food & cafés** | Source-linked guide; partial review coverage | Refresh current menus, hours, closures and booking terms. Yelp/Instagram/TikTok/Facebook/Reddit/X direct access was blocked in sampled requests; Maps/TripAdvisor coverage is limited, not comprehensive. |
| **C · Activities, gaming, sights** | Searchable and caveated | Confirm availability, access, hours and dated social/search leads; no walk-in PC café was verified. |
| **D · U.S.-traveler guide** | Practical evidence integrated | Traveler-specific booking, room, passport, insurance, phone/device and invoice remain unknown; check entry and weather again near departure. |
| **E · Malta sports radio** | Dedicated receiver-based section | No physical DAB+/FM scan or reception test; no complete named-match chain (official schedule + Malta carriage + compatible receiver + local signal) confirmed. |
| **F · Expenses** | Blank-by-default planner with CSV/JSON backup | Enter only confirmed itinerary/actuals. JSON restore is consent-gated and validated; CSV is for spreadsheet/manual use. |
| **H · CS2 event extension** | Integrated and re-audited | Confirm checkout/inventory, own reservation, timezone, attendee gate, validity, exact finish discrepancy and weekend agenda. |
| **G · Integration** | Three cumulative passes complete; PR #46 merged, required CI passed, and Pages latest-build endpoint reports `built` | No repository delivery gate remains. Keep open factual limits visible; remaining work is traveler- and date-specific. |

## Current evidence and access limits

- **Tickets/event:** the 11 October Eventbrite read shows in-person 18+ attendance and visible 14–16 October agenda entries. The page heading says 22:00 while Wed/Thu rows extend to 22:30. Its free-reservation offer is evidence of what was advertised, not personal reservation, current inventory or a checkout total. Weekend rows/FAQ answers were not visible in extraction, not proven unpublished.
- **Transit:** one static Route 186 return variant lists 20:53 at Stadium stop 2194 toward Buġibba and omits Il-Qawra; it does not establish the network's last bus or that a second boarding is always necessary. Route 214 is a candidate, not a saved journey. The October diversion excerpt's missing year is open.
- **Fares:** MPT's explicit winter single-fare period ends 13 June 2026. Do not assign either €2.00 winter or €2.50 summer to 13–19 October without current confirmation.
- **Radio:** weekly schedules, named-match rights/carriage, DAB/FM technical listings, physical signal and online streams are distinct. UK fixtures/streams are not Malta reception evidence; Sports Channel's 6C/12A labels conflict.
- **MTA:** guest notice/guidelines support the nightly rate and cap. The general webpage wording remains an anomaly; actual guest ages, billable nights and invoice remain traveler-specific.
- **External research:** limited Google Maps/TripAdvisor views and historical indexed community data are not a comprehensive review sample. No universal ratings/popularity claim is made.

## Local validation snapshot

PR #49 was opened from this fixed branch after the final rebase. Its initial GitHub validation run [38155423677](https://github.com/buffedlizard55-lab/MALTASUPPLEMENTAL/actions/runs/38155423677) succeeded. This document records the pre-merge local gates; the PR's live state/checks and its post-merge delivery comment are the authoritative merge/build receipt, not an unobserved prediction in this file. GitHub Pages is configured for `main` at `/`; publishing that setting is not itself proof that this PR is deployed.

## Session `arena/502e2dae-maltasupplemental` — verification pass and reconciliation (11 October 2026)

This session ran the requested Passes 1–3 over the integrated tree and re-verified the highest-risk claims against live sources (Eventbrite listing, MPT Route 186/202 pages, MPT fares page, BBC programme pages). It recorded: the operator-page confirmation of the last Stadium 2194 returns (20:53/20:54, Buġibba Bay 1 21:26/21:36); the detour-scope clarification (the omitted Gholja 2 → Targa span excludes the traveler’s boarding/alighting stops); unverified later-return leads (Route 202 toward Sliema to about 22:08, then N212; shuttle 405 to Mosta then N48); the likely fare split €2.50 on 13–18 October / €2.00 on 19 October at “partially verified” (two third-party 2026 season guides plus the official winter-start date — not operator confirmation); and the Explore-card terms/contradiction disclosure. The fare-inference previously rejected for want of a stated season boundary is reinstated on that new evidence and labelled accordingly everywhere.

This branch then reconciled advancing `main` (PRs #42–47, then PR #49) by content, keeping both sides’ net-new work — including PR #49’s expanded datasets, planner hardening and test suite. All gate results for the final merged tree are reported in `docs/FINAL_REPORT.md` after the runs actually executed; unverifiable items stay in `docs/OPEN_QUESTIONS.md`.

After resolving the latest-main conflicts, `npm test` passed: **7 datasets / 184 exact-schema records / 281 unique record URLs in the source log / 15 HTML pages / 176 link attributes / 9 shared navigation destinations / 25 expense rows**; shared/inline JavaScript checks passed; Playwright passed **21/21** tests, including 320/360/768/1024/1440 px layouts, axe, source/data projections, backup validation, error/storage cases and planner quick-fill. `git diff --check` passed after conflict resolution and these documentation edits.

After resolving latest-main conflicts and before delivery, `npm test` passed: **7 datasets / 184 exact-schema records / 281 unique record URLs in the source log / 15 HTML pages / 176 link attributes / 9 shared navigation destinations / 25 expense rows**; shared/inline JavaScript checks passed; Playwright passed **21/21** tests, including 320/360/768/1024/1440 px layouts, axe, source/data projections, backup validation, error/storage cases and planner quick-fill. No application code/data changed after this run. `git diff --check` passed after the post-merge reporting edits.

## Session `arena/09cdfbf0-maltasupplemental` — second re-verification pass (11 October 2026)

This session reviewed the repository at `250e6bd`, re-verified the highest-risk external claims against live sources, and
closed the two weakest evidence gaps rather than restating the existing ones.

**Access reality this session:** direct page fetches were blocked for most sites (Eventbrite returned "Something went wrong",
maltapublictransport.com errored), but the search index was readable. Every new row in `docs/SOURCES.md` therefore states
explicitly whether it is a full page read or a search-index extract; no extract is presented as a page read.

**What was verified or newly evidenced**

| Area | Result |
|---|---|
| Event | 14–18 Oct, BLAST Arena Studios, Attard, 8 teams, $1m — corroborated across HLTV, Liquipedia, Hotspawn and the organiser's release. NIP-for-Virtus.pro substitution confirmed as current (9 Oct). Wednesday match starts 10:30 / 13:00 / 15:30 / 18:30 CEST corroborate the listing's "games 10:30". |
| Food | TripAdvisor's *Restaurants near AX ODYCY Hotel* list was readable; recorded ranked **by review volume** with explicit volatility evidence (two captures minutes apart disagreed). 9 new food records, 1 platform-ranked capture. |
| Gaming | Dated Malta "Game & Entertainment Centers" directory read confirms arcades exist and **no public PC café is listed** — the gap is now evidenced, not just unresearched. Empire Cinema arcade added as an unconfirmed lead. |
| Recreation | Eco Sports Limited (Buġibba) added with **official published prices** (e-bike €35/day, SUP from €30, tours from €55) — the strongest operator-priced near-hotel option found to date. |
| Radio | NET FM grid re-read live a second time (Fri 18:30 *Mhux Premier biss*, Sat 16:00 *Hits & Score*, Sun 15:00 *Sports Box*) — a stability check, not independent corroboration. DAB+ "Sports Channel" block conflict widened: an encyclopaedia list puts 185.36 MHz to "RAVE Radio". |
| Everyday | EES Malta conflict strengthened with named reporting (Guardian/Sunday Times, 14 Sep 2026) and Malta's own airport page; ETIAS boundary risk for these exact dates made explicit. |

**Corrections made during review:** removed a duplicated paragraph in `ees-malta-implementation-conflict`; fixed a misspelled
record ID (`…-odyy-` → `…-odycy-`) so the public anchor is correct; added cross-references so the three TripAdvisor snapshot
records no longer read as competing claims about the same page.

**Gate results for this session's tree:** `python3 scripts/validate_site.py` — PASS, 7 JSON files / 196 exact-schema
records / 317 unique record URLs / 15 HTML pages / 234 link attributes / 9 navigation destinations / 25 expense rows.
`python3 scripts/check_javascript.py` — PASS. `npx playwright test` — 21/21 passed. Manual Chromium pass at 390 px and
1280 px: zero horizontal overflow and zero console errors on the three pages changed this session.

## Delivery observed — session `arena/09cdfbf0-maltasupplemental`

PR **#51** (head `a20368c`) merged into `main` on **11 October 2026 at 17:13:35 UTC** as merge commit `6859c46`. Its required
check, run [38158610565](https://github.com/buffedlizard55-lab/MALTASUPPLEMENTAL/actions/runs/38158610565) (“Schema, browser
and accessibility checks”), passed. The GitHub Pages latest-build record for that commit reports **built**, 17:13:36 → 17:13:53
UTC. No browser-level fetch of the live site was possible in this session (network policy allows only GitHub API and
package-registry hosts), so this is a build-state observation and not a content verification.

## Traveler-time follow-up

The repository merge, required PR check and Pages build record are complete. Remaining work needs traveler-specific information or a check close to the trip:

1. Confirm reservation, attendee gate/day validity, timezone, exact finish and Saturday/Sunday event agenda with Hotspawn/Thunderpick.
2. Save dated public-transport journeys both ways; verify stop sides, safe walks, the October notice year/effect, current fares and any TQ announcement. Request a live hotel/taxi quote only if desired or needed.
3. Refresh venue, restaurant, gaming and attraction hours/availability, weather and service notices close to travel; locally scan FM/DAB+ and ask stations about any named match.
4. Confirm MTA invoice handling/eligible nights if the webpage wording remains unclear; recheck entry/EES status against authoritative guidance and the traveler’s own documents.
5. Populate the expense planner only after itinerary/party/booking details arrive; review the quick-fill preview and keep a private backup.

## Session `arena/d840a59d-maltasupplemental` — second 11 October pass: per-date transport plan and timezone-pinned clocks

Branch `arena/d840a59d-maltasupplemental` started at `main` commit `250e6bd0ea5722cbad5a5ec21fc3117f2eee8fe0` (PR #48 merge) with a clean tree. Work was serial on the fixed branch under the same A–G ownership boundaries; no other branch was touched.

**What changed**

- **A · Transport:** added the canonical `event-day-transport-by-date` record and the `getting-around.html#event-day-by-date` section, giving one transport decision for each of the seven trip days. Re-read the Route 186 outbound grids (Qawra 952 last 21:39; Stadium 6227 last 22:04/22:08; Rabat 4 22:13/22:18), the complete latest-service-updates page (both Route 186 notices, the 17–18 October cluster on fourteen further routes, the Saqqajja 4627 closure, and no TQ/Thunderpick service) and the TQ1 page (still “Timetable not available!”). Re-read the fare page: the winter sentence still ends 13 June 2026 and the Explore Adult contradiction persists.
- **C/H · Event:** added the `twc-opening-matchups-14-oct` record and the `event.html#opening-matchups` section. The Malta local clocks for the four 14 October openers (10:30, 13:00, 15:30, 18:00) were established by comparing two renderings of the same bracket table six hours apart — the first clock evidence in this project that is timezone-reconciled instead of assumed. Re-read the Eventbrite listing in full; the weekend agenda and FAQ answers are still not exposed.
- **E · Radio:** read the DAB+ operator directory in full (38 rendered entries, no “Sports Channel”, Radio Sportiva the only sports-branded entry) and re-read Vibe FM’s football page (still 2025/26 season, newest post May 2026). Both narrow the radio claims rather than adding stations.
- **G · Integration:** page sections, navigation shortcuts, one new Playwright test, and updates to `SOURCES.md`, `OPEN_QUESTIONS.md`, `HANDOFF.md`, `PLAN.md`, `FINAL_REPORT.md`, the audit log and the README.

**Gates observed on this branch:** `python3 scripts/validate_site.py` → 7 JSON files / 199 exact-schema records after integrating latest `main` (186 on this branch before that merge) / 319 unique record URLs in the source log / 15 HTML pages / 325 link attributes / 9 navigation destinations / 25 expense rows; `python3 scripts/check_javascript.py` → shared and inline JavaScript syntax pass; `npx playwright test` → **22/22** passing, including the five viewport/axe sweeps and the new per-date plan and matchups test.

**Blockers:** none for delivery. Every remaining gap needs traveler-specific input or a date-local check: the reservation and weekend agenda, the attendee gate and walks, the dated Buġibba → Qawra connection, a live ride quote, the operator-dated October fare, a physical radio scan, and the planner inputs.

### Delivery receipt — PR #56 (observed)

- PR [#56](https://github.com/buffedlizard55-lab/MALTASUPPLEMENTAL/pull/56) was opened from `arena/d840a59d-maltasupplemental` after the branch merged latest `main` (`21d13d1`, PRs #51–#54) and its four conflicts were resolved by content.
- Required check “Schema, browser and accessibility checks” run [38159932939](https://github.com/buffedlizard55-lab/MALTASUPPLEMENTAL/actions/runs/38159932939) completed with conclusion `SUCCESS` before merge.
- `gh pr merge 56 --merge` succeeded: GitHub reports state `MERGED` at **2026-10-11T17:32:11Z**, merge commit **`6da8aba73608964678411a939b27c1c6b5501fe9`**.
- GitHub Pages latest-build record reports status **`built`** for that same merge commit, updated **17:32:33Z**; the public URL is <https://buffedlizard55-lab.github.io/MALTASUPPLEMENTAL/>.
- Independent content check (not just build state): the published `getting-around.html` was fetched after the build and contains the new “Transport by date · 13–19 October 2026” section with all seven dated rows and their evidence links.

## Suggested work for the next session, in priority order

1. **Reservation and weekend agenda (blocks everything else).** Reserve on the Eventbrite listing, then get the Saturday 17 / Sunday 18 door, game and finish times from Hotspawn/Thunderpick and the answers to the nine FAQ items (day validity, per-day scanning, gate, parking, catering, transferability). The per-date transport table changes the moment those times exist.
2. **Dated journeys in both directions.** Run MPT’s planner for each event date from AX ODYCY to the venue pin and back, save the results, and resolve the Buġibba → Qawra onward leg. Confirm the correct Qawra stop side and walk both ends.
3. **Return cover.** Check MPT service updates daily 14–18 October for a TQ special service; otherwise pre-book a taxi/ride-hailing return per event evening and record the quoted price in the planner (never a guessed amount).
4. **Fare confirmation.** Ask MPT or the tallinja app which single fare applies 13–19 October 2026 and whether Explore Adult 7-day includes Airport Direct — the fare page still contradicts itself on that point.
5. **Radio, locally.** Buy or borrow a Band III DAB+ receiver in Malta, scan 6C then 12A, and log the actual service label, block, time and any named match heard. Ask NET FM, Vibe FM and Radio Sportiva about trip-week football coverage; nothing published so far establishes a named match.
6. **Planner population.** Enter only confirmed bookings and actuals once the itinerary arrives; use the quick-fill preview, keep refundable holds in notes, and export a JSON backup.
7. **Optional polish.** Resolve the 18:00-vs-18:30 clock outlier against the organiser’s live bracket; refresh menus/hours and the 18–19 October forecast close to travel; extend review-platform coverage where access allows.
