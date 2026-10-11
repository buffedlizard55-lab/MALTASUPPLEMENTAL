# Delivery status — Malta trip guide

**Last updated:** 11 October 2026 (UTC)
**This session:** `arena/dd9dd00c-maltasupplemental`, started at `250e6bd` (PR #48 merge). Workstream branches were not created because Arena locks the session branch.

| Workstream | Status | Blocker |
|---|---|---|
| A · Transport | Route 186 20:53/20:54 grids, October 17–18 19:00–00:00 diversion, and fare table re-read. Saqqajja stop 4627 closure added as partially verified. | No saved hotel-to-gate journey. Closure year and effect on Stadium stops not printed. |
| B · Food | Qawra TripAdvisor Featured snapshot updated with sponsored cards and numbered entries 1–3. | Yelp, Instagram, TikTok, Facebook and X were not re-attempted. Not a popularity ranking. |
| C · Activities / event | Eventbrite and Thunderpick pages re-read. Visible lineup is six names plus View all. | Sat/Sun agenda, inventory, reservation and NIP/Virtus.pro slot remain open. |
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

## Traveler-time follow-up

The repository merge, required PR check and Pages build record are complete. Remaining work needs traveler-specific information or a check close to the trip:

1. Confirm reservation, attendee gate/day validity, timezone, exact finish and Saturday/Sunday event agenda with Hotspawn/Thunderpick.
2. Save dated public-transport journeys both ways; verify stop sides, safe walks, the October notice year/effect, current fares and any TQ announcement. Request a live hotel/taxi quote only if desired or needed.
3. Refresh venue, restaurant, gaming and attraction hours/availability, weather and service notices close to travel; locally scan FM/DAB+ and ask stations about any named match.
4. Confirm MTA invoice handling/eligible nights if the webpage wording remains unclear; recheck entry/EES status against authoritative guidance and the traveler’s own documents.
5. Populate the expense planner only after itinerary/party/booking details arrive; review the quick-fill preview and keep a private backup.
