# Malta trip guide — final report

**Audit date:** 11 October 2026 (UTC)
**Fixed session branch:** `arena/cc913a9b-maltasupplemental`
**Starting revision:** `b307c51`
**Latest-main integration:** PR #49 at `12578cd`
**Delivery PR:** [#46](https://github.com/buffedlizard55-lab/MALTASUPPLEMENTAL/pull/46) — merged to `main` at `25e0176`

## Result

A mobile-friendly, source-linked Malta travel guide is maintained for the user-supplied **13–19 October 2026** stay at **AX ODYCY in Qawra** and the supplied Thunderpick CS2 destination at **BLAST Arena Studios, Attard**. It includes focused pages for the event, transport, food/cafés, gaming/activities/landmarks, U.S.-traveler practicalities, separate Malta sports radio and expenses. Seven canonical JSON datasets contain **184 exact-schema records**. Pages project those records rather than creating a parallel source of facts.

The 25-row expense planner has 18 core categories and seven optional daily rows. Amounts start blank. Quick-fill previews likely EUR matches, sums accepted distinct lines by category, does not overwrite existing budgets, and sends foreign/ambiguous values and refundable holds to manual review. It autosaves locally, exports CSV for spreadsheet/manual use, and offers consent-gated validated JSON backup/restore. It assumes no flight, booking amount, party size, ticket, taxi ride or actual spend.

This final pass reconciled `main` through PR #49 rather than dropping newer upstream work. It retained the fresh CS2 field update (Ninjas in Pyjamas for Virtus.pro, attributed to HLTV and Hotspawn), the hotel/taxi/TQ evidence, the new primary MTA guest notice, the expanded source/evidence logs and safe planner improvements. Local tests pass; they are software/evidence-coverage checks, not a factual certificate or real-world journey test.

## Current sourced findings and caveats

### CS2 event and access

Hotspawn's Eventbrite listing read 11 October names BLAST Arena Studios Malta / MFCC South Gate National Stadium, Attard, for **14–18 October**, with in-person attendance for **18+**. Visible Wednesday/Thursday rows show 09:30 check-in, 10:30 games and a 22:30 agenda end; Friday shows 14:00, 15:00 and 21:00. The header says 22:00, so confirm the finish/timezone. A dated listing capture records a “Free / Reserve a spot” offer, but that is not a current checkout total, available inventory, a reservation for this traveler or guaranteed admission. Weekend agenda entries and FAQ answers were not visible in the extraction, not proven unpublished. The attendee gate, one-ticket/five-day validity, scanning, parking and catering remain open.

The organizer's operational window (12–19 October) is distinct from the public competition dates (14–18 October). HLTV and tournament-presenting partner Hotspawn reported on 9 October that Ninjas in Pyjamas replaced Virtus.pro; the organizer's own pages still showed the original field when last checked. The report keeps this update attributed. Stream channels are internet broadcasts, not radio.

### Transport and fares

- Malta Public Transport's latest-updates extraction shows an October Route 186 diversion at **19:00–00:00** on 17–18 October, omitting Gholja 2 through Targa toward Buġibba. A separate **20:00–00:00** notice ends around 21 April. They are not merged into a 19:00–24:00 union; the October notice excerpt lacks a year/cause, so confirm applicability and effect with MPT.
- One static Route 186 variant lists a **20:53** Stadium stop 2194 departure toward Buġibba and does not list Il-Qawra on that direction. It flags a risk against visible 14–16 October event finishes, but does not establish a network-wide last bus or that every return requires a second boarding. Route 214 is another route-level candidate; TQ1 shows no timetable. No complete dated planner result, gate walk, stop-side walk or onward connection was saved.
- MPT's day-route singles are €2.00 winter / €2.50 summer, but its explicit winter validity ends 13 June 2026. Neither rate is assigned to 13–19 October 2026; ticket-card best value is not assumed. A taxi is optional if selected or needed after checking the dated planner. AX ODYCY says Guest Relations can arrange fixed-charge taxis but publishes no rate; no live quote was obtained. Transport Malta's meter-reference page shows an April 2022 update date, and distance arithmetic is not a trip quote.

### Hotel, practicalities and environmental contribution

AX ODYCY's own pages document facilities, the room-name distinction, guest-room sockets, a razor-only 110 V bathroom socket, doctor/pharmacy guidance and Guest Relations taxi arrangements. They do not verify the traveler's booking, actual room, meal plan, hotel rate, check-in/out clock times or taxi quote. Personal passport, insurance, medical, phone-plan and entry eligibility facts are also unknown.

A freshly read MTA guest-facing notice and the 2026 accommodation guidelines state **€1.50/night** for eligible guests aged 18+ at arrival, capped at **€22.50 per person/continuous visit**, separately from the room rate, effective for stays starting 1 July 2026. Six qualifying nights would be €9 per eligible adult as arithmetic only; the traveler's ages, billable nights and invoice are unknown. The general MTA service page retains “exceeded fifteen nights” wording. OQ-25 records that webpage anomaly; it is not treated as a short-stay exemption or as MTA having corrected the page. Ask the hotel/MTA if needed and use the invoice.

### Radio, food/activity evidence and access limits

The sports-radio page distinguishes official schedules, named-match carriage, DAB+/FM technical listings, physical reception and online streams. **No trip-week match was verified through the full chain of commentary schedule, Malta carriage, compatible receiver and local reception.** BBC Sportsworld episode times are general live sport, not a named local relay. NET recurring slots, UK BBC fixtures, station apps, Twitch/Kick/YouTube and Kalshi listings do not prove Malta terrestrial carriage. Sports Channel's 6C/12A labels conflict; no physical receiver scan was performed.

Food/café, gaming, attraction and dated-event options retain source-specific limits. No current walk-in PC café was confirmed; closed/conflicted and out-of-window entries are warnings, not recommendations. Some Google Maps/Reviews and TripAdvisor views were accessible; sampled Yelp, Instagram, TikTok, Facebook, Reddit and X direct refreshes were blocked or limited. Historical search-index snapshots are labelled historical; no comprehensive review/platform ranking is claimed.

## Three cumulative review passes

1. **Pass 1 — implementation and integration:** reviewed the existing repository and canonical schema before topic work; preserved main's event/hotel additions; integrated seven datasets, shared pages, accessible navigation, sources and expense planner. The inherited upstream pass recorded 18/18 browser checks; this session merged the latest upstream commit and revalidated current files.
2. **Pass 2 — adversarial review:** challenged categorical ticket/price, bus/taxi, fare, diversion, radio and MTA claims; retained unknowns, updated the reported Virtus.pro/NIP field, and reviewed backup/restore and amount parsing. The upstream adversarial suite covers malformed/oversized imports, storage denial, CSV safety, refundable holds, wrong years and no-JavaScript/fetch-failure behavior.
3. **Pass 3 — original-request consistency:** mapped the requested trip topics/review-platform coverage/radio distinctions/expense-planner behavior to pages and docs, kept unverified details in `OPEN_QUESTIONS.md`, confirmed upstream IDs, and reran the complete local suite after integrating PR #49. PR #46 then passed its GitHub check and was merged; the Pages build outcome is recorded below.

## Local validation after latest-main integration

- `npm test` — **PASS**, validator + JavaScript syntax checks + **21/21 Playwright tests**.
- `git diff --check` — **PASS** after resolving the latest-main integration and final report edits.
- GitHub PR #46 check, “Schema, browser and accessibility checks” — **PASS** at 16:37:43 UTC on head `3ad5100`.
- GitHub Pages latest-build record `1276765781` — **built** for merge commit `25e01762d310bdc71deaa9dc9602f96a7d4565f9`, updated at 16:38:24 UTC.
- Validator: **7 JSON files / 184 exact-schema records / 281 unique record URLs present in `docs/SOURCES.md` / 15 HTML pages / 176 link attributes / 9 shared navigation destinations / 25 expense rows**.
- Responsive/accessibility coverage: all active pages at **320/360/768/1024/1440 px**, axe checks, data/render parity, navigation/deep links, JSON backup/restore, CSV safety and planner error cases.
- Automated checks do not establish external URL liveness, ticket inventory, a personal booking, a date-specific live bus journey, taxi availability, physical radio reception, local match carriage or exhaustive device/assistive-technology coverage.

## Remaining limitations and next-session work

1. Confirm the traveler's actual reservation, attendee gate, ID/day validity, exact timezone/finish and Saturday/Sunday event agenda with Hotspawn/Thunderpick.
2. Save date-specific Malta Public Transport journeys in both directions; verify stop sides, safe walks, attendee gate, the October notice year/effect, current single fare and any TQ announcement. Request a live taxi/hotel quote only if desired or needed.
3. Refresh venue, restaurant, gaming and attraction hours/availability, weather and service notices close to travel. Scan FM/DAB+ locally and ask stations whether a named match is carried.
4. Confirm actual MTA invoice handling/eligible nights if the webpage wording remains unclear; check entry and EES status with authoritative sources and use the traveler's own documents/booking.
5. Populate the expense planner only after itinerary/party/booking details arrive, review the preview, and save a private JSON backup (CSV is for spreadsheets/manual re-entry).
6. Continue source-by-source rechecking of inherited records and broader device/accessibility testing; current test success does not imply exhaustive external verification.

## GitHub delivery boundary

PR #49 at `12578cd` was integrated before delivery. PR #46 was merged into `main` on 11 October 2026 at 16:38:02 UTC; GitHub reports merge commit `25e01762d310bdc71deaa9dc9602f96a7d4565f9`, from head `3ad510058c77c41cf2920949b4047d921d870578`. The required “Schema, browser and accessibility checks” run passed. The GitHub Pages latest-build endpoint reports status `built` for the same merge commit; the Pages API lists the public site `https://buffedlizard55-lab.github.io/MALTASUPPLEMENTAL/` with source `main` at `/`. This verifies GitHub's build record, not an independent browser fetch or exhaustive live-content inspection.
