# Delivery status — Malta trip guide

**Last updated:** 11 October 2026 (UTC)
**Session branch:** `arena/cc913a9b-maltasupplemental`
**Snapshot boundary:** Dated local audit state, not a live GitHub or Pages dashboard. Check the PR directly before reporting its current state.

## Integration and delivery

- The session began at `b307c51`. Upstream PRs #42 (`5cdea68`), #43 (`94733df`), #45 (`dc2fe82`), #44 (`c7d1d00`), #47 (`852343f`) and #49 (`12578cd`) are merged to `main`; the current upstream tree has been integrated on this branch.
- PR #49 adds an expanded source-led guide, keeps all upstream event/hotel changes, adds safe JSON expense backup/restore, and broadens the automated review suite. Its evidence scope and historical pass details are preserved in the audit/history docs.
- This session reconciled to `main` at `12578cd`, retained the exact schema and all upstream record IDs, and reran the complete suite. The latest MPT extraction separates the April 20:00 diversion from the October 19:00 notice and notes that the latter excerpt lacks a year. Static Route 186 evidence is not a full-network last-bus finding; no taxi is assumed as mandatory.
- A fresh MTA guest-facing notice plus the 2026 guidelines support €1.50/night for eligible 18+ guests, capped at €22.50/visit and separately itemized. The general MTA service page still has anomalous “exceeded fifteen nights” wording; OQ-25 treats that as a webpage anomaly, not a short-stay exemption. A six-qualifying-night €9 figure is conditional arithmetic, never a personal invoice.
- PR #46 is open from the fixed branch to `main`. The last pushed head `7e45b12` was reported `CONFLICTING`; `gh pr checks 46` reported no checks. Main subsequently advanced through PR #49 to `12578cd`. That revision has now been merged locally and the updated tree passes tests; the merge commit/push are pending. Recheck PR head, checks and mergeability after push.

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
| **G · Integration** | Three cumulative passes complete; latest-main tests passed | Run final whitespace check after status edits, commit/push only this branch, inspect PR #46 and merge by explicit number if allowed. |

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

## Next steps

1. Run final conflict-marker, staged/unstaged diff and whitespace checks; commit the merge of `origin/main` at `12578cd`.
2. Push only `arena/cc913a9b-maltasupplemental`; inspect PR #46's exact head, CI, review state and mergeability.
3. If GitHub reports a clean mergeable state and required checks pass (or none are configured), run `gh pr merge 46 --merge`; inspect the actual merge commit, main CI and Pages build/live result before reporting.
4. For the traveler: confirm reservation/gate/weekend schedule, save dated bus journeys, verify fares/optional quotes, clarify the MTA page anomaly/invoice, refresh volatile venue/food/weather data, scan radio locally and enter actual costs.
