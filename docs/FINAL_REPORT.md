# Final audit report — Malta travel guide

**Audit date:** 11 October 2026 (UTC)
**Session branch:** `arena/502e2dae-maltasupplemental`
**Baseline:** `origin/main` at `b307c51` (merge of PR #33), at parity at session start

## Scope and integration

This session ran the requested multi-pass protocol over the already-mature guide: **Pass 1** implemented and verified the full request; **Pass 2** reviewed for bugs, missing requirements, incorrect assumptions and edge cases; **Pass 3** re-checked the implementation against the original request and improved accuracy, reliability and completeness. The highest-risk factual claims (event listing, Route 186 return, fare seasons, card terms, radio schedules) were re-verified line by line against live sources on 11 October 2026 before any wording changed.

The delivered site remains the repository's static, JSON-backed Malta trip guide and blank-by-default expense planner. The six datasets use the shared exact 13-field schema (key order now normalized across all files). Integration counts after this pass: **165 records** (transport 25, food 38, activities 39, everyday 18, radio 20, expenses 25), **292 unique record URLs** in the source log, 15 HTML pages, 138 checked link attributes, eight shared navigation destinations, and 25 expense rows.

This is a sourced planning aid, not a booking, admission, price, service, schedule, or reception guarantee. Dates, hotel, and intended venue are traveler-supplied inputs except where separately corroborated.

## What this session verified (live re-reads, 11 October 2026)

### Thunderpick World Championship / admission

The Hotspawn/Eventbrite listing was re-read directly. It still advertises the in-person, 18+ event at BLAST Arena Studios Malta, MFCC South Gate National Stadium, Attard ATD 4000, 14–18 October, with a free “Reserve a spot” action and a new “Sales end soon” banner. Agenda rows remain visible for Wed 14 and Thu 15 (09:30–22:30) and Fri 16 (14:00–21:00) only; the Saturday/Sunday entries are still hidden behind “Show all agenda”. The headline-vs-agenda discrepancy (22:00 vs 22:30) persists. Independent search corroboration (skin.club event page, Esports Kingdom, esports.net, freetips) consistently gives 14–18 October, BLAST Arena Studios, Attard, $1M prize pool, eight teams. None of this establishes this traveler’s reservation, current inventory, per-day scanning or the attendee gate.

### Public transport — the event-day return problem (core requirement)

The operator’s live Route 186 page was parsed stop by stop, both directions, all published grids:

- **Return (the binding constraint):** the last Stadium 2194 departures toward Buġibba are **20:53 and 20:54** on the published return grids, reaching Buġibba Bay 1 at 21:26 and 21:36. The earlier “one static variant” hedge is replaced: the figure is confirmed on the operator’s current route page. Which grid applies on which trip date is not labelled, so the date-specific planner remains the authority.
- **Outbound:** Qawra stop 952 departures toward the venue run to about 21:39 (Stadium 6227 to about 22:04–22:08), so *getting to* an evening session is not the problem — *getting back* is.
- **Return path:** the toward-Buġibba direction does not serve any Il-Qawra stop; it terminates at Buġibba Bay 1 (2527), so a second boarding (or walk/taxi from Buġibba) is required.
- **Saturday 17 October detour:** the omitted span “Gholja 2 through Targa” sits **between** the Stadium 2194 boarding stop and the Buġibba terminus on the operator’s own stop lists — the traveler’s boarding and alighting stops are not among the omitted stops. The diverted path and timing remain unpublished, so a particular departure could still be re-timed. The two conflicting notice windows (19:00–00:00 vs 20:00–24:00) are still planned as their union.
- **Later leads for after 20:54 (unverified, recorded, not claimed as journeys):** Route 202 from the same Stadium 2194 stop toward Sliema is listed on the operator’s route page to about 22:08; night route N212 links Sliema–Buġibba (announcement times 23:50–01:30); night route N48 is listed at Mosta-corridor stops (Gholja 2, Rotunda 2, Targa) toward Buġibba and can be reached via the Ta’ Qali P&R shuttle 405. A third-party (Moovit) listing shows a later 23:07 last-202 figure that the operator page does not — logged as an unresolved conflict, operator planner authoritative.

### Fares — a dated conclusion changed by new evidence

The official fares page, re-read 11 October, still prints only the expired winter window “19 October 2025 to 13 June 2026”. The previous audit **rejected** the €2.50/€2.00 split inference because no source stated the season boundary. This session found two independent third-party 2026 fare guides that do state it — summer singles 14 June–18 October (€2.50), winter singles from 19 October (€2.00) — which matches the official window’s own 19-October winter start date. The split is therefore reinstated at **“partially verified”** as a planning inference (€2.50 on 13–18 October; €2.00 on 19 October), explicitly labelled as secondary-guide evidence, not operator confirmation, and not prefilled into the planner. Card terms were also refined: the 12-journey card counts Night Routes/Airport Direct at 2 journeys per trip; Explore Flex advertises 2 Airport Direct trips for €6; and the fares page **contradicts itself** on whether the Explore Adult 7-day card includes Airport Direct — disclosed rather than resolved.

### Sports radio

BBC programme pages were re-read: the 5 Live Sport upcoming grid (Sat 17 12:00 build-up; Sun 18 12:00 PL Sunday; Sun 18 16:00 Nott’m Forest v Arsenal pre-match) and episode m00334k6 (Premier League Football, Sat 17 Oct 14:45, BBC Radio 5 Sports Extra) confirm the UK commentary listings. These remain UK schedules only. Malta reception, BBC Sounds access from Malta, World Service carriage and the DAB+ “Sports Channel” identity/block remain unverified scan leads; a US HD Radio set cannot decode DAB+.

### Everyday life, expenses, food/activities

No stale claims were found in workstreams B, C, D or F; their content matches the checked sources and discloses platform limits (Yelp/Instagram/TikTok/Facebook/X blocked or limited). The expense planner’s blank defaults, quick-fill preview, autosave, CSV export and reset are intact and tested.

## Cumulative verification passes (this session)

1. **Pass 1 — implement/verify:** baseline gates green (validator, JS checks, 11/11 Playwright). Every requirement in the original prompt was mapped to a page/record; live re-reads produced the findings above; data/pages/docs were updated consistently (workstream order A → E → G, one writer per file per step).
2. **Pass 2 — review:** static and runtime deep-link resolution checked (0 broken); JSON key order normalized to the canonical 13-field order; the fare-inference reversal documented against the previous audit; detour-scope, card-terms and late-return-lead edge cases added; wording search for superseded “static variant”/“fare unconfirmed” claims across index/README/pages.
3. **Pass 3 — re-check against the request:** hotel/event/itinerary facts (AX ODYCY address, Deluxe Sea-View, 13–19 Oct 2026; BLAST Arena Studios, Attard; event days and public-transport requirement) rechecked against the rendered pages; the Kalshi/radio requirement, everyday US-traveler section, expense quick-fill, GitHub Pages structure and source-citation requirements reconfirmed line by line; final gates re-run after edits.

## Validation results (after this session’s edits)

- `python3 scripts/validate_site.py`: **PASS** — 6 JSON files / 165 exact-schema records / 292 unique source URLs / 15 HTML pages / 138 link attributes / 8 navigation destinations / 25 expense rows.
- `python3 scripts/check_javascript.py`: **PASS**; `node --check js/site.js`: **PASS**.
- Internal deep-link check (static ids + runtime record ids): **PASS** — 0 broken.
- `npm ci` / `npm test`: **PASS**, 11/11 Playwright after the session edits (320/360/768/1440 px layouts, axe WCAG 2A/AA/2.1AA, data/render parity, navigation/deep links, planner persistence/CSV/reset, quick-fill, storage-denial and data-fetch-failure cases).
- `git diff --check`: **PASS**.

These gates check local structure and behavior. They do not certify external-link liveness, current ticket availability, physical access, radio reception, or a dated transit journey.

## Remaining limitations and suggestions for the next session

1. **Event access (highest value):** ask Hotspawn/Thunderpick to confirm the traveler’s reservation, current inventory, attendee gate, per-day scanning/validity, the 17–18 October agenda, and the 22:00-vs-22:30 finish discrepancy. The Sat/Sun agenda may appear as the event starts — re-read the listing daily.
2. **Transit:** run the MPT planner for each event date both ways with the confirmed gate; determine which Route 186 return grid (20:53 or 20:54) applies and whether event extra service exists; verify the after-20:54 fallback legs (Route 202 → Sliema → N212; 405 → Mosta → N48) as date-specific journeys; recheck both diversion pages for 16–17 October; measure the Qawra-stop-to-hotel and Stadium-to-gate walks; obtain one live evening taxi/ride-hailing quote from the venue to Qawra as the priced fallback.
3. **Fares:** confirm the likely €2.50 (13–18 Oct) / €2.00 (19 Oct) split with MPT or a sales point; resolve the Explore Adult 7-day Airport Direct contradiction before buying any card.
4. **Radio:** with a DAB+ receiver bought in Malta, scan 6A/6C/12A and FM at the hotel and venue; record service names, blocks and audio; confirm any named-match carriage with the station; recheck BBC/Rai/talkSPORT schedules close to air time. UK BBC episode records are the strongest schedule evidence but prove nothing about Malta reception.
5. **MTA contribution:** ask MTA/AX ODYCY how the “exceeded fifteen nights” wording applies to a six-night stay; use the invoice, keep planner amounts blank.
6. **Planner hand-off:** paste the confirmed itinerary into the quick-fill panel once received (it fills only blank budget fields after preview); export a CSV before switching devices.
7. **Coverage limits:** Yelp, Instagram, TikTok, Facebook and X were blocked or limited throughout; recheck accessible platforms and volatile menus/hours/closures without implying comprehensive coverage. No full external-link crawl, physical transit/radio test, or device-based visual audit was completed in this environment.

Full claim-specific source rows are in `docs/SOURCES.md`; unresolved items in `docs/OPEN_QUESTIONS.md`; ownership/dependencies in `docs/PLAN.md`; cross-workstream notes in `docs/HANDOFF.md`; the dated claim audit in `docs/AUDIT_2026-10-11.md`.

## GitHub delivery snapshot

This report captures the local candidate at the delivery gate. The explicit PR merge and any resulting Pages build status are time-dependent GitHub facts, reported only after they have been checked; this file is not a live CI/Pages dashboard.
