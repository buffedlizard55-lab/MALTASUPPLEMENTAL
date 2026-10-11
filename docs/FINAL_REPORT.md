# Final audit report — Malta travel guide

**Audit date:** 11 October 2026 (UTC)
**Session branch:** `arena/ef6c76d6-maltasupplemental`
**PR under delivery:** #33, “Audit Malta guide sources and expand mobile verification”

## Scope and integration

The guide was reconciled on the fixed Arena branch with `origin/main` at `de3303fbfecdf8176afb32002f02be58692d0405`, which includes PR #39 and its accumulated PR #40/#41 work. The non-fast-forward integration preserves PR #33's source-specific corrections while retaining useful upstream material. No topic record was dropped to simplify the merge.

The delivered site remains the repository's static, JSON-backed Malta trip guide and blank-by-default expense planner. The six datasets use the shared exact 13-field schema. Current integration counts: **165 records** (transport 25, food 38, activities 39, everyday 18, radio 20, expenses 25), **288 unique record URLs**, 15 HTML pages, 138 checked link attributes, eight shared navigation destinations, and 25 expense rows.

This is a sourced planning aid, not a booking, admission, price, service, schedule, or reception guarantee. Dates, hotel, and intended venue are traveler-supplied inputs except where separately corroborated.

## Material findings and corrections

### Thunderpick World Championship / admission

A Hotspawn Eventbrite listing read on 11 October advertised an in-person, 18+ event at BLAST Arena Studios Malta, MFCC South Gate National Stadium, Attard ATD 4000, for 14–18 October, with a free “Reserve a spot” action. It showed agenda/check-in entries for 14–16 October. The listing headline says 22:00, while Wednesday/Thursday agenda entries extend to 22:30; confirm exact finish times. The Saturday/Sunday entries were not visible in the extracted page.

That dated listing supersedes the earlier search that found no ticket link and a €10 studio-audience precedent from a separate BLAST-run event. It does **not** establish current ticket inventory, this traveler's reservation, per-day ticket validity/scanning, transferability, exact attendee gate, parking/catering, or weekend agenda. Do not assume admission or transfer another event's entry instructions.

### Public transport and fares

MPT's published fare table lists €2.50 summer and €2.00 winter day-route singles plus cards, but its stated winter validity ends 13 June 2026. No 2026/27 transition date or applicable single fare for 13–19 October was found. The former inference of €2.50 for 13–18 October and €2.00 on 19 October is rejected; both published prices remain comparisons, not trip-date quotes or planner defaults.

One static Route 186 variant lists a 20:53 Stadium 2194 departure toward Buġibba. Its return stop chain does not itself list an Il-Qawra stop, so an onward boarding may be needed, but the date-specific connection and walking sections were not checked. Comparing 20:53 with the visible 14–16 October agenda flags a return risk; it is not a complete route search and does not prove that no later alternative bus exists. MPT's two 17 October Route 186 notices show different windows (19:00–00:00 and 20:00–24:00); plan for their union as an alert, then use the live planner. The notice does not publish a diverted path or establish the effect on a particular Stadium departure or onward Qawra service.

### Sports radio

The BBC upcoming page and six linked episode JSON records name seven UK Premier League commentaries for 17–18 October, including Bournemouth–Sunderland on 5 Sports Extra 2. The parent *Premier League Football* 5 Live programme series is distinguished from the individual match broadcast service. This is UK schedule evidence only—not proof of Malta FM/DAB+ carriage, physical reception, BBC Sounds access, BBC World Service carriage, or named-match output on a local service.

Malta's DAB+ “Sports Channel” identity and block remain unresolved: one specialist directory points to 6C (185.360 MHz), WorldDAB lists a generic service on 12A (223.936 MHz), and the local operator directory lists no sports service. These are scan leads, not proof that the service is talkSPORT or carries commentary. No receiver scan was possible. Rai's recurring weekend programme does not establish a 17–18 October lineup. The 5 Live Sport studio-show page could not be directly fetched; search-result times remain a lead and were not added as verified schedule data.

### MTA environmental contribution and expenses

The 2026 MTA guideline PDF states €1.50 per night for eligible guests aged 18+ at the start of the visit, capped at €22.50 per person per visit and shown separately on a receipt. The current MTA service webpage separately refers to nights that “exceeded fifteen (15) nights”; the two official texts do not expressly reconcile short-stay treatment. Any six-night €9 calculation is conditional arithmetic only, not a confirmed liability, quote, or planner default. Use the booking and final invoice.

The expense planner remains blank by default and can be populated quickly once itinerary/booking details are provided. It does not assume a flight, hotel rate, party size, ticket purchase, ride count, reimbursement, or personal cost. The user can preview quick-fill before applying it, edit budget/actual values, use local autosave, export CSV, and reset.

### Review and social-platform evidence

The repository records the attempts and limits for Google Maps/Reviews, Yelp, Instagram, TikTok, Facebook, Reddit, and X. Some Google Maps/TripAdvisor and Reddit/search snapshots were accessible; Yelp, Instagram, TikTok, Facebook and X access remained blocked or limited. A Facebook-sourced event date was read from a dated search-index snapshot because the page could not be fetched directly. No inaccessible content was inferred, and the review sample is not comprehensive or a universal ranking. Recheck business status, hours, menus, closures, and ticket listings before visiting.

## Cumulative verification passes

1. **Implementation:** validated all six topic JSON files and the common record schema; verified data/source-log/page wiring, local paths, shared navigation, JavaScript syntax, and expense-planner behavior.
2. **Requirements and evidence:** re-read the current request against the rendered data and cross-workstream handoffs; corrected stale ticket, fare, bus-return, MTA, and BBC wording; preserved source dates and explicit uncertainty; kept inaccessible-platform and physical-check limits visible.
3. **Final audit:** searched for superseded claims; recorded remaining risks, blockers and handoffs; inspected the integration diff; ran structural, JavaScript, browser, responsive-layout, and accessibility tests.

## Validation results

- JSON parsing (`python3 -m json.tool` for six datasets plus schema): **PASS**.
- `python3 scripts/validate_site.py`: **PASS** — 6 JSON files / 165 exact-schema records / 288 unique source URLs / 15 HTML pages / 138 link attributes / 8 navigation destinations / 25 expense rows.
- `python3 scripts/check_javascript.py`: **PASS**.
- `node --check js/site.js`: **PASS**.
- `npm ci`: **PASS** (23 packages installed; 0 vulnerabilities reported).
- `npm test`: **PASS**, 11/11 Playwright tests, including 320/360/768/1440 px layouts, axe checks, data/render parity, navigation, and planner cases.
- `git diff --check`: **PASS**.

These gates check local structure and behavior. They do not certify external-link liveness, current ticket availability, factual truth beyond the checked sources, physical access, radio reception, or a dated transit journey.

## Remaining limitations and next-session work

1. Ask Hotspawn/Thunderpick to confirm reservation status, current ticket inventory, attendee gate, per-day ticket scanning/validity, the 17–18 October agenda, and the exact 14–16 October end-time discrepancy.
2. Run the MPT planner for each event date and both directions using the attendee gate once known; compare Route 186, Route 214 and other live options, check the Buġibba-to-Qawra leg and walks, and save the actual journey results. Recheck both diversion pages. Obtain a live taxi/ride-hailing quote if the planner shows no suitable return.
3. Check the applicable October single fare with MPT or at a sales point; do not budget an inferred seasonal rate.
4. With a DAB+ receiver in Malta, scan 6A/6C/12A and FM at the hotel/event area; record actual service names, blocks, audio and reception. Confirm any named-match carriage with the station. Recheck BBC and Rai schedules close to air time.
5. Ask MTA/AX ODYCY to clarify short-stay treatment of the “15-night” text; use the invoice for the planner.
6. Recheck accessible review/social platforms and volatile business details without implying comprehensive coverage. Refresh the forecast and the traveler's actual flight, hotel, age/party, itinerary, device, insurance and expense inputs when supplied.

Full claim-specific source rows are in `docs/SOURCES.md`; current unresolved items are in `docs/OPEN_QUESTIONS.md`; current ownership/dependencies are in `docs/PLAN.md`; cross-workstream notes are in `docs/HANDOFF.md`; the dated claim audit and reconciliation supplement are in `docs/AUDIT_2026-10-11.md`.

## GitHub delivery snapshot

This report captures the local candidate at the PR #33 delivery gate. The final explicit PR merge and any resulting Pages build status are time-dependent GitHub facts and are reported only after they have been checked; this file should not be treated as a live CI/Pages dashboard.

---

## Workstream H addendum — PR #42, 11 October 2026

Everything above describes the PR #33 delivery. **This addendum is authoritative for the current merged tree.**

**This delivery PR:** https://github.com/buffedlizard55-lab/MALTASUPPLEMENTAL/pull/42 · **Branch:** `arena/154ca483-maltasupplemental`

### H · CS2 event guide — 8 records, ninth active page

`event.html` gives the trip's reason for existing a page of its own: venue address and map pin, ticketing terms (free but reserved, in person, **18+**), the published daily agenda, match clocks in Malta time, the eight-team field including the 9 October Virtus.pro → Ninjas in Pyjamas substitution, format and prize split, broadcast talent, official streams, and on-site practicalities. It was **promoted out of the retired noindex stub set** rather than added beside it, so HTML pages stayed at 15 while active pages went 8 → 9.

Two rules govern the page. **Clocks:** HLTV and Liquipedia both render times in the *fetching client's* timezone, so no third-party clock is copied as a local time; every clock is labelled "Malta time (CEST, UTC+2)" with its anchor shown, and the EDT+6h conversion is admissible only because Eventbrite independently publishes "Games 10:30" for Wed 14 October. **Sources:** the `source_type` enum has no value for a community wiki or esports news site, so every record's `source_url` is official and third-party evidence lives in `notes`.

### Unique contributions beyond the event page

- **`tq-event-special-services`** — MPT runs TQ-numbered special event services out of Ta' Qali, and TQ1's corridor runs through St Paul's Bay and **Qawra** at the €3.00 Special Services fare. Its page showed "Timetable not available!" and no TWC notice was found, so it is recorded as **a possibility to watch for, not a plan**, at `partially verified`, with a daily re-check instruction (OQ-H3).
- **`white-taxi-official-tariff`** — Transport Malta's published **maximum** meter rates, read directly, with the caveat that the page footer says "last updated 06/04/2022". The worked caps are labelled as this project's arithmetic at assumed distances and **not quotes**; the road distance was never measured (OQ-H7).
- **Three stale expense rows corrected** — `event-commute`, `taxi-rideshare` and `local-bus-and-cards` still dated from 2026-10-09 and contradicted the transport findings on the same site. The planner remains 25 rows, blank by default, with no invented amounts.

### Aligned to the audit, not against it

PR #33 deliberately downgraded the return-gap finding from `verified` to `partially verified`, reframing it as a **risk from one static Route 186 variant** rather than proof that no later bus exists. This branch's wording was rewritten to match across `index.html`, `README.md`, `event.html`, `getting-around.html` and the three expense rows, so the reconciliation does not silently re-strengthen a claim the audit softened. The TQ1 finding reinforces that caution: it is a second reason not to treat one timetable variant as the whole network.

This branch also **dropped its own duplicate records** rather than layering them on the parallel session's — `event-day-late-return` and `venue-nearest-bus-stops` were superseded by `main`'s `event-day-late-finish-return-gap` and `mfcc-official-bus-186`. One limitation is **withdrawn**: "18–19 October is not forecast" is obsolete, because `main` located the Met Office Valletta view reaching 12–19 October.

### Gates on the merged tree

`python3 scripts/validate_site.py` — **PASS**: 7 JSON files / **175 exact-schema records** (transport 27, event 8, food 38, activities 39, everyday 18, radio 20, expenses 25) / **305 unique record URLs all present in `docs/SOURCES.md`** / 15 HTML pages / 170 link attributes / **9 navigation destinations** / 25 expense rows. `check_javascript.py` and `node --check` — **PASS**. `git diff --check` clean. `npm ci && npm test` — **PASS, 11/11 Playwright**.

### Remaining work suggested for the next session

1. **Expand the ticketing page in a real browser.** The Sat 17 / Sun 18 agenda rows and all nine FAQ answers are client-side and never rendered. Two answers decide real logistics: whether one registration covers all five days, and whether there is on-site parking. A headless-browser fetch step would close a whole class of these gaps at once.
2. **Watch for TQ1 daily during 14–18 October** (OQ-H3) — the only finding that could replace taxi returns with a €3.00 bus.
3. **Re-read the taxi tariff for a post-2022 revision and measure one real road distance** (OQ-H7).
4. **Confirm current inventory and whether a reservation guarantees admission**, and the €0 total at checkout.
5. **Check whether the organiser republishes the NIP substitution** (OQ-H5), then update `event.json` and `activities.json` in the same pass.

### Limitations that remain

The offline validator cannot test external URL liveness, so a source may rot silently. There is no physical FM/DAB+ receiver scan and no manual graphical screenshot, so radio reception and visual layout are reasoned about rather than observed — though Playwright does cover 360/768/1440 px viewports, responsive overflow and axe WCAG 2A/AA/2.1AA. Client-side content is systematically invisible to server-side fetching. Review-platform coverage remains incomplete: Yelp, Instagram, TikTok, Facebook, X and Reddit returned 403 or login-gated responses. **No ticket has been secured, no journey has been ridden, and no radio has been scanned**; this remains a dated planning aid, not a booking, admission, fare, service or reception guarantee.
