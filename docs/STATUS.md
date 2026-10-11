# Delivery status — Malta trip guide

**Last updated:** 11 October 2026 (UTC)
**Current session branch:** `arena/67d511d1-maltasupplemental`
**Snapshot boundary:** Current-session addendum below; later sections are historical mainline snapshots, not a live dashboard.

## Current session addendum — `arena/67d511d1-maltasupplemental` (11 October 2026)

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
