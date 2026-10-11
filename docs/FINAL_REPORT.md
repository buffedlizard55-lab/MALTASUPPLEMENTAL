# Final audit report — Malta travel guide

**Audit date:** 11 October 2026 (UTC)
**Session branch:** `arena/27302b08-maltasupplemental` (based on `main` at `b307c51`)
**Integrated in this session:** pull request **#42** — workstream H, the CS2 event guide (`data/event.json`, `event.html`, two transport records, fare/taxi/venue evidence)

## Post-merge follow-up addendum — branch `arena/9f6f35c7-maltasupplemental`

PR #42 ("Add CS2 event guide (workstream H)") was merged into `main` at `5cdea68` (squashed `fbb7aa4`) on 11 October 2026 while this session was completing a parallel, independently re-verified re-implementation of the same guide. The merge superseded that parallel content, so the branch was reconciled to the new `main` and now contributes only net-new corrections — no record added, removed or renamed.

The follow-up corrections: the costs-page event-access wording and quick-fill example (the old "no public sale" text and the ticket-price example are gone), the activities callout's "free in-person admission" wording with a link to the CS2 event guide, the radio page's stream wording crediting the organiser's own named channels, and the activities tournament records updated for the 9 October Virtus.pro → Ninjas in Pyjamas substitution. Claim-level evidence is in `docs/AUDIT_2026-10-11.md`.

Integration state on this branch: 7 datasets / **176 exact-schema records** (transport 28, food 38, activities 39, everyday 18, radio 20, expenses 25, event 8) / **307 unique logged record URLs** / 15 HTML pages / **181 link attributes** / 9 navigation destinations / 25 expense rows. Gates: `validate_site.py` PASS, `check_javascript.py` PASS, `node --check js/site.js` PASS, `npm test` PASS (11/11 Playwright at 320/360/768/1440 px with axe), `git diff --check` clean. The event guide itself — `data/event.json` (8 records) and `event.html` — is the merged `main` version.

Delivery (observed): PR #44 was merged by explicit number on 11 October 2026 at 16:01:59 UTC as merge commit `c7d1d00d6dec02c4c9a7b4d73492e086c8f7a72b`; the push-to-main validation run 38153759615 reported **SUCCESS**, and GitHub Pages reported the build for `c7d1d00` as **built**. The published pages were then re-fetched from the live site (homepage, CS2 event guide, getting-around, food & cafés, activities, everyday, sports radio, expense planner and sources) and confirmed to carry the merged corrections.

## Scope and integration

This session opened with the repository already mature: a static, JSON-backed Malta trip guide and a blank-by-default expense planner, published from `main` root via GitHub Pages. One pull request (#42) was still **open and conflicting** with `main` on five files. The session therefore (a) integrated that work by content rather than by side, (b) re-read the load-bearing sources itself instead of inheriting earlier notes, and (c) ran the three cumulative passes on the integrated result.

Integration totals after the merge and this session's edits: **7 data files / 176 exact-schema records** (transport 28, food 38, activities 39, everyday 18, radio 20, event 8, expenses 25), **307 unique record URLs** in the source log, **15 HTML pages / 178 link attributes**, **9 shared navigation destinations**, and **25 expense rows**.

Nothing in this repository is a booking, admission, fare, service, schedule or reception guarantee. The stay, the trip window and "BLAST Arena Studios, Attard" are traveller-supplied inputs; the venue address is separately corroborated from the organiser's own ticketing listing.

## What this session changed

| Change | Detail |
|---|---|
| Merged #42 by content | Kept #42's verified additions (venue/dates/agenda, the fare/card table, the Transport Malta taxi tariff, TQ special event services, richer radio leads, the event page and its eight records) **and** this branch's evidence caveats. A line-level check confirmed no #42 addition was silently dropped in the files that auto-merged; the two documents taken from this branch's side were rewritten here. |
| Re-verified instead of inheriting | The event listing, MPT fares, MPT Route 186 (both diversions, a stop closure, stop-level times), MPT TQ1, the Transport Malta taxi tariff, NET FM's schedule, and AX ODYCY's property + FAQ pages were each fetched directly. Rows are in `docs/SOURCES.md`. |
| Hotel practicalities added to data | The hotel's own FAQ supplied verified, useful detail that now lives in the datasets it belongs to: guest-room sockets and the razor-only 110 V bathroom socket (`malta-electricity`), card acceptance and check-in pre-authorisation (`malta-currency-cards`), the on-call doctor / pharmacy / hospital distance (`emergency-medical-112`), car hire via Guest Relations (`malta-car-hire-airport`), a **new** transport record for taxis arranged at the hotel at fixed charges (`ax-odycy-guest-relations-taxi`), and operator-published tipping guidance (`tipping-no-fixed-rate-verified`). |
| Overview gained a "Your base: AX ODYCY" section | Six data-backed cards (address/contact, room-name check, power, the hotel-arranged taxi, money/tipping, health) that link to the records rather than restating unverifiable claims. |
| Event listing detail sharpened | The listing's own ticket block shows **"Free"** with **"Reserve a spot"** under a **"Sales end soon"** banner; agenda rows render end times (Wed/Thu 09:30–22:30, Fri 14:00–21:00). The free claim is now attributed to the listing itself as well as HLTV, and the nine unrendered FAQ answers are listed explicitly as open. |

## Material findings

### Event and admission

The event's own ticketing listing names *Hotspawn present the Thunderpick World Championships 2026* at **BLAST Arena Studios Malta, MFCC South Gate National Stadium, ATD 4000 Attard**, **Wednesday 14 – Sunday 18 October 2026**, in person, **ages 18+**, with a free "Reserve a spot" block under "Sales end soon", and map coordinates 35.8957343, 14.4168839. Published agenda: Wed 14 and Thu 15 check-in 09:30 / games 10:30 (day to 22:30); Fri 16 check-in 14:00 / games 15:00 (14:00–21:00); Sat 17 and Sun 18 unpublished. The page header says 9:30 AM–10 PM while the Wednesday/Thursday rows extend to 10:30 PM — that discrepancy is recorded, not resolved. **No reservation is held by this project**, and the FAQ answers (parking, per-day scanning, transferability, catering, toilets) never rendered.

### Getting there — and getting back

Route 186 links the Qawra-side stops to Ta' Qali Stadium. The outbound direction clears even a 09:30 check-in. The return direction is the problem: the last listed Stadium-area departure toward Buġibba is **20:53** in one static variant, that direction serves **no Il-Qawra stop** (terminus Buġibba Bay 1, 2527) so a second boarding is mandatory, and MPT's listed night routes cover Buġibba and Valletta — not Ta' Qali or Attard. Two Friday/Saturday diversions were re-read verbatim this session (8 PM–midnight ending 21 April; 7 PM–midnight starting 17 October), both omitting Gholja 2 → Targa toward Buġibba, alongside a separate Saqqajja stop closure. **The published plan is therefore a booked return for every event night**, with three named options: a hotel-arranged fixed-charge taxi (new record), a ride-hailing app, or the TQ special event services that MPT may announce days beforehand (TQ1's corridor runs through St Paul's Bay and Qawra to Buġibba at the €3.00 special-services fare). The TQ1 page still showed "Timetable not available!" when checked.

### Fares, honestly labelled

The operator's fare page gives one table — day single €2.00 winter / €2.50 summer, night €3.00, special services €3.00, tallinja Direct €3.00, TD1 €3.50, €19 12-journey shareable card, €25 Explore Adult 7-day (excludes tallinja Direct), €27 Explore Flex 7-day (includes Airport Direct), €7 Explore Child, €50 fine — but its only dated statement is that the **€2.00 winter single applied 19 October 2025 – 13 June 2026**. No 2026/27 changeover is published, so **€2.50 is this project's planning inference**, labelled as such on the page, in the data and in the planner. Cards sell at the Buġibba Terminal, the closest office to the hotel.

### Taxis

Transport Malta's regulated **maximum** metered tariff was re-read in full (initial €3.50, then €2.50/km stepping down to €0.85/km beyond 20 km, €25/hour waiting, €4.20/hour in traffic, +€4.50 on 25 December and 1 January only). The page footer says **"Page last updated: 06/04/2022"**, so the maxima may have moved. The site's €12.40 / €19.40 / €25.90 / €30.90 caps are **arithmetic at assumed distances, not quotes**, and the road distance was never measured. The hotel states it arranges taxis at fixed charges; no rate is published.

### Sports radio and markets

The strongest English-language lead remains a DAB+ service named "Sports Channel" that one Maltese directory labels "Talk Sport" on block **6C (185.360 MHz)**, while the industry multiplex table lists a "Sports Channel" on **12A** and the Maltese operator's own channel list shows no sports service. NET FM's recurring weekend sports slots were re-verified exactly (Friday 18:30 "Mhux Premier biss", Saturday 16:00 "Hits & Score", Sunday 15:00 "Sports Box"), BBC World Service *Sportsworld* has dated 17–18 October episode starts on DAB+ 6A, and Rai Radio 1's weekend *Tutto il calcio minuto per minuto* is the most likely live Serie A on a Maltese multiplex — but **no station publishes a dated trip-week named-match lineup**, no physical scan was possible, and a UK BBC schedule is not Malta carriage. Kalshi's own help centre says travel-abroad use is possible subject to its Member Agreement while third-party guidance says US-resident-only: the conflict is recorded and no market-to-broadcast link is inferred.

### Everyday life for a US traveller

Type G sockets at 230 V / 50 Hz; the hotel's own FAQ adds three Type G and three two-pin sockets per room and a **razor-only** bathroom socket (220 V and 110 V American-style) that must not be used for chargers. Cards (Amex, Diners, Visa, Mastercard) are accepted at the hotel with a check-in pre-authorisation. Tipping now has two honest readings: the hotel publishes a 10–15% expectation while stating it adds no service charge, and secondary guides say 5–10% where no charge is on the bill — both are shown, neither is prescribed. The MTA eco-contribution rate (€1.50 per eligible guest per night from 1 July 2026, €22.50 cap, charged per night the room is made available and disclosed separately on the receipt) is verified from the guidelines themselves, which were re-read in this session. That re-read also **narrows** the long-standing "15-night" question: the document's only fifteen-day reference defines an "interruption" (up to fifteen days in premises that do not require to be licensed within one visit), so it is not a minimum-stay threshold. The webpage's differently worded heading is recorded rather than reconciled away, and the six-night ≈ €9 figure remains conditional on the invoice. Two dated sources still conflict on whether EES is enforced in full at Malta's borders.

### Expense planner readiness

The planner holds 18 core categories plus seven optional daily rows, all blank, with browser-local autosave, CSV export, a blank template download and a **paste-your-itinerary quick-fill** that previews which row each line would fill and writes only into still-blank budget fields. Nothing is prefilled — not flights, not the hotel rate, not a tip percentage, not a fare. When the itinerary arrives, the remaining work is data entry, not research.

## Provenance carried forward from pull request #42

Because #42 was authored in parallel and merged here, three of its conventions are kept deliberately rather than rewritten:

1. **Clocks are never copied from a third-party renderer.** HLTV and Liquipedia display times in the *fetching client's* timezone — the same match page showed 15:30 in one view and 09:30 in another. Every clock on the site is therefore labelled "Malta time (CEST, UTC+2)" with its UTC/EDT anchor shown, and a third-party time is only admissible when an official source independently reproduces it (as Eventbrite does for the 10:30 games time).
2. **`source_type` is not stretched.** The schema's enum has no value for a community wiki or esports news site, so every event record carries an **official** `source_url` and cites HLTV, Liquipedia and Moovit in `notes`. Third-party evidence never becomes a record's primary source, and sites that contradict official sources (a "Valletta" venue listing, a different prize figure, a €8 taxi base fare) were excluded rather than averaged in.
3. **Superseded duplicates were removed, not layered.** #42's `event-day-late-return` and `venue-nearest-bus-stops` were dropped in favour of the fuller `event-day-late-finish-return-gap` and `mfcc-official-bus-186`, and three expense rows (`event-commute`, `taxi-rideshare`, `local-bus-and-cards`) were re-dated to match the transport findings instead of keeping a 9 October contradiction on the same site.

One open item from that workstream stays open and is tracked: the **Virtus.pro → Ninjas in Pyjamas** substitution (OQ-H5) is reported by HLTV and by Hotspawn, the tournament's own presenting partner, but Thunderpick's page and September release still list Virtus.pro — so it is third-party-reported rather than officially republished, and the event page says so.

## Requirement-by-requirement check

| Original request | Where it is answered | Status |
|---|---|---|
| Transport: airport, hotel ↔ BLAST Arena Studios on event days, buses/taxis/rentals with cost and feasibility | `getting-around.html`, `data/transport.json` (28 records) | Answered with a documented return gap; no date-specific journey or live quote yet |
| Food and cafés from reviews/maps/socials | `restaurants.html`, `data/food.json` (38 records incl. the hotel's own venues) | Answered within disclosed platform limits (Yelp/Instagram/TikTok/Facebook/X blocked) |
| Gaming centres, activities, landmarks, events near the hotel | `activities.html`, `data/activities.json` (39 records) | Answered, including PC-gaming status conflicts recorded rather than resolved |
| Everyday life for a US traveller (plugs, SIM/eSIM, money/tipping, safety, health, customs, language, weather) | `everyday.html`, `data/everyday.json` (18 records) | Answered; tipping now has operator guidance plus a documented conflict |
| Live sports radio during the trip, official schedules, Kalshi-relevant markets | `radio.html`, `data/radio.json` (20 records) | Partly answered: recurring grids and UK fixtures verified, Malta carriage and reception unverified |
| Expense planner ready for a quick fill when the itinerary arrives | `costs.html`, `data/expenses.json` (25 rows) | Answered — blank by default with a preview-then-apply quick-fill |
| Clean, mobile-and-desktop site with sections/subpages and an executive summary | 9 active pages, shared renderer, axe/Playwright gates | Answered; 320/360/768/1440 px checked |
| Verified, sourced, no hallucinations | `docs/SOURCES.md` (307 URLs), `docs/OPEN_QUESTIONS.md`, per-record confidence labels | Enforced by the validator: a record cannot cite a URL that is absent from the source log |
| PR created and merged to `main`; suggestions and limitations | This document + the session PR | See the delivery snapshot below |

## Cumulative verification passes

1. **Pass 1 — implement and integrate.** Merge conflicts resolved by content; datasets enriched from freshly fetched sources; every new URL logged in `docs/SOURCES.md` before the gate was re-run (the validator fails closed on an unlogged URL).
2. **Pass 2 — review for bugs, missing requirements, wrong assumptions.** Merge integrity checked line by line per file; hotel-sourced facts pushed into data rather than hand-written into pages; the trip-week fare relabelled a planning inference wherever it appears; the room-name mismatch surfaced; stale-claim scans for superseded wording return only deliberate provenance notes.
3. **Pass 3 — re-check against the original request and re-run everything.** Requirement table above walked item by item; all seven datasets parse; validator, JavaScript syntax gate, `node --check` and the 11-test Playwright suite (including axe at four widths) pass on the integrated tree; README and the executive summary were rewritten to match the merged evidence rather than either branch's half.

## Validation results (observed)

- `python3 scripts/validate_site.py` — **PASS**: 7 JSON files, 176 exact-schema records, 307 unique record URLs present in `docs/SOURCES.md`, 15 HTML pages / 178 link attributes, 9 navigation destinations, 25 expense rows wired.
- `python3 scripts/check_javascript.py` — **PASS**; `node --check js/site.js` — **PASS**.
- `npm ci` — **PASS** (23 packages, 0 vulnerabilities).
- `npx playwright test` — **PASS, 11/11** in 1.2 minutes on the merged tree.
- `git diff --check` — **PASS**.

These gates check structure and behaviour. They do not certify external-link liveness, current ticket availability, physical access, radio reception, or a dated transit journey.

## Remaining limitations

1. **No reservation, no admission.** The listing says "Sales end soon"; nothing here substitutes for reserving it.
2. **No measured journey.** No attendee gate, no walk distances, no date-specific planner result, no live taxi quote, no verified Buġibba → Qawra connection.
3. **No published trip-week fare** and a taxi tariff last updated in 2022.
4. **No radio reception test** and no Malta carriage confirmation for any named match.
5. **Volatile data by nature:** hours, menus, closures, ticket inventory, diversion notices and the forecast can change between this snapshot (11 October 2026) and travel.
6. **Platform coverage is incomplete:** Yelp, Instagram, TikTok, Facebook and X were blocked or limited; social evidence is dated snapshots, not a ranking.
7. **Traveller-specific inputs are absent:** booking confirmation, room allocation, party size/ages, flights, meal plan, device, insurance, personal spend.
8. **The offline validator is not a web crawler:** a cited URL can rot without the suite noticing.

## Suggested next-session work (priority order)

1. **Reserve the event place now** and read the nine FAQ answers in a browser; record per-day validity, transferability, parking and catering in `data/event.json`.
2. **Run the MPT planner for each event date** in both directions once the gate is known; capture the actual journeys in `data/transport.json`, and check Route 186, Route 214 and TQ services.
3. **Get one real number for the return:** a live Bolt/eCabs quote *and* the hotel's fixed-charge price for Qawra → MFCC after 22:00, so the planner's taxi row can be filled with a quote rather than arithmetic.
4. **Ask MPT which single fare applies on 13–19 October**, or confirm at the Buġibba Terminal on arrival day.
5. **Scan FM/DAB+ at the hotel** (6A, 6C, 12A) during the Saturday 16:00 and Sunday 15:00 windows and record what each service actually carried.
6. **Confirm the hotel voucher/invoice details** (room type against the hotel's room names, meal plan, nights, eco-contribution treatment) and then complete the expense planner from the pasted itinerary.
7. **Refresh the volatile layer** on arrival: service diversions, ticket inventory, menus/hours for the shortlisted venues, and the daily forecast.
8. **Broaden review-platform coverage** where access permits, labelling every rating/count as a dated snapshot.

## Delivery snapshot

Pull request **#43** (`arena/27302b08-maltasupplemental` → `main`) was opened, passed CI ("Schema, browser and accessibility checks" — SUCCESS, including 11/11 Playwright tests), and was **merged by explicit number at 15:54:56 UTC on 11 October 2026** as merge commit `94733df22b670825eb1b39d21d53581d0274e329`. The push-to-main validation run (38153269792) reported **SUCCESS** and GitHub Pages reported the build for that commit as **built** (run 38153269670). The homepage and `event.html` were then fetched live from the published site and confirmed to carry this session's changes, including the new "Your base: AX ODYCY" section. Pull request **#42**, still open and conflicting when this session began, was merged upstream by the parallel session at `5cdea68` while #43 was open; #43 was therefore re-merged against it and its conflicts resolved by content, with a line-level check confirming nothing was lost. **This document describes states actually observed: the local gates above, the merged tree, the source reads dated 11 October 2026, and the GitHub runs named in this paragraph.** Corresponding detail lives in `docs/SOURCES.md` (claim, URL, access date, workstream, limitation), `docs/OPEN_QUESTIONS.md` (unresolved items), `docs/PLAN.md` (ownership and protocol), `docs/HANDOFF.md` (cross-workstream findings) and `docs/STATUS.md` (workstream status).
