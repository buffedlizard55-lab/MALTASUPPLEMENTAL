# Malta Trip Guide

A mobile-friendly, source-linked travel guide for the trip window **13–19 October 2026**, based at the user-supplied **AX ODYCY, Qawra Coast Road, Qawra SPB 1902** (Deluxe Sea-View room). The event location supplied by the traveler is **BLAST Arena Studios, Attard**.

**Published guide:** <https://buffedlizard55-lab.github.io/MALTASUPPLEMENTAL/>

The official Thunderpick page rechecked on 11 October lists the overall 2026 event window as 12–19 October (arrival 12th, media day 13th, Group Stage 14–16th, Playoffs 17–18th, departure 19th). The Thunderpick-issued release names BLAST Studios Malta; a BLAST attendee guide for a different event gives MFCC/Ta’ Qali venue-area context only. Neither confirms this traveler’s spectator access, ticket, daily public door times, exact event entrance, or transport. Those details remain open.

This is a dated research and planning aid, not a booking or guarantee of future opening hours, fares, availability, event access, radio reception, or programme carriage.

## Pages

| Page | What it covers |
|---|---|
| [Overview](https://buffedlizard55-lab.github.io/MALTASUPPLEMENTAL/) | Executive summary, trip assumptions, priorities, and guide navigation |
| [Transport](https://buffedlizard55-lab.github.io/MALTASUPPLEMENTAL/getting-around.html) | Airport/hotel options and Qawra-to-event travel; compares bus, taxi/ride-hailing, ferries, and car hire |
| [Food & cafés](https://buffedlizard55-lab.github.io/MALTASUPPLEMENTAL/restaurants.html) | Sourced restaurants, cafés, and casual food, with review/social evidence limitations |
| [Activities & sights](https://buffedlizard55-lab.github.io/MALTASUPPLEMENTAL/activities.html) | Gaming options, landmarks, recreation, and dated events during the trip window |
| [Everyday guide](https://buffedlizard55-lab.github.io/MALTASUPPLEMENTAL/everyday.html) | Practical information for a U.S. traveler, with passport, entry, safety, and date-sensitive caveats |
| [Sports radio](https://buffedlizard55-lab.github.io/MALTASUPPLEMENTAL/radio.html) | Malta-receivable AM/FM/DAB+ leads and official station/programme listings; event-specific carriage is not assumed |
| [Expense planner](https://buffedlizard55-lab.github.io/MALTASUPPLEMENTAL/costs.html) | 18 core categories + 7 optional daily rows, local browser autosave, CSV export, and reset |
| [Sources & status](https://buffedlizard55-lab.github.io/MALTASUPPLEMENTAL/sources.html) | Links to the evidence log, open questions, workstream status, handoffs, plan, and schema |

## Key findings and limits

- **Event and venue:** the official Thunderpick page lists the 12–19 October event window and Malta as its location. The Thunderpick release names BLAST Studios Malta; MFCC/Ta’ Qali is venue-area context from a BLAST guide for a different event, not a confirmed TWC attendee pin. Public spectator access, ticket arrangements, door times, and the event-day entrance remain unconfirmed.
- **Event-day transit:** Route 186 and214 are conditional Qawra–Ta’ Qali candidates; final venue entrance, stop sides, safe walks and date-specific outward/return connections remain open. Extracted static timetable variants are not a trip-day guarantee. Recheck17October evening diversion and keep a live-quote taxi fallback.
- **Radio:** NET FM is listed at FM 101 MHz and has recurring weekend sports shows; its grid does not explicitly state a time zone. Malta’s DAB+ directory lists Radio Sportiva and BBC World Service. WorldDAB lists BBC World Service on Digi B Network block 6A at 181.936 MHz, but reception at the hotel/event venue is untested and Radio Sportiva’s current block/frequency was not found. No radio carriage of the TWC, Gżira United–Mosta, or Rolex Middle Sea Race was confirmed.
- **Hotel environmental contribution:** Malta Tourism Authority guidance checked 11 October states €1.50 per night per person aged 18+ from 1 July 2026, capped at €22.50 per eligible person per visit. Six chargeable nights would be €9 per eligible adult, conditionally; actual billable nights, guest ages, and the hotel invoice determine the amount. MTA’s separate “15-Night Threshold” sentence is ambiguous; ask the hotel/MTA to clarify (OQ-25). The planner does not prefill a personal charge.
- **Expense planner:** all budget and actual amounts start blank. Enter amounts in euros on a consistent whole-trip/party basis. The planner stores inputs in this browser/device only, does not send them to a server, exports a CSV backup, and can clear saved entries. Reference URLs are not price quotes.
- **Research-platform limits:** sampled TripAdvisor and a small number of Google Maps profile views informed parts of the food/activities research. Fresh review/social access remained blocked or limited. Official X post text was extracted, but its attached opening-day schedule was unavailable; five403 responses in a parallel batch lacked reliable endpoint labels. Platform coverage is not comprehensive; see the dated notes in `docs/SOURCES.md` and the topic pages.
- **Open questions:** exact event access/times, saved date-specific transit route and return, 17 October diversion impact, trip-week radio schedule/carriage, current business hours/status conflicts, traveler-specific entry/insurance/device details, and the booking itinerary remain unresolved as noted in `docs/OPEN_QUESTIONS.md`.

## Research records

- [`docs/SOURCES.md`](docs/SOURCES.md) — claim, URL, access date, workstream, and source limitations.
- [`docs/OPEN_QUESTIONS.md`](docs/OPEN_QUESTIONS.md) — missing, disputed, or date-sensitive information and how to resolve it.
- [`docs/STATUS.md`](docs/STATUS.md) — workstream progress and blockers.
- [`docs/HANDOFF.md`](docs/HANDOFF.md) — cross-workstream discoveries and follow-ups.
- [`docs/PLAN.md`](docs/PLAN.md) — scope, ownership, and verification plan.
- [`docs/DATA_SCHEMA.md`](docs/DATA_SCHEMA.md) — shared data conventions; topic records use the exact requested common key `price range`.
- [`docs/FINAL_REPORT.md`](docs/FINAL_REPORT.md) — 3-pass audit summary, verified vs. unverified items, limitations, and next-session recommendations.
- [`data/record.schema.json`](data/record.schema.json) — canonical machine-readable schema for the exact 13 fields.

## Build, preview, and deployment

The site is static HTML, CSS, and JavaScript with JSON data; no application build or dependency installation is required. Repository Pages settings checked on 9 October 2026 publish the `main` branch root to the public site. Merging changes to `main` updates the site through GitHub Pages’ existing branch-based publishing. The `.nojekyll` file keeps the source/data tree static. A GitHub Actions workflow validates pull requests and pushes to `main`; it does not replace the configured Pages publisher.

For a local HTTP preview from the repository root:

```bash
python3 -m http.server 8080 --bind 0.0.0.0
# Open http://localhost:8080
```

An HTTP server is needed for browser `fetch()` and the expense planner’s `localStorage` behavior. The deployed planner saves only in the current browser/device; export a CSV before switching devices or clearing browser data.

The Pages workflow and local validator check the exact 13-field record schema and enums, HTTPS primary URLs and their source-log coverage, JavaScript syntax, topic-page/data wiring, and local links. External websites are not guaranteed to remain available; re-open primary sources before acting on date-sensitive information.

## 11 October audit and browser tests

Critical-source refresh and per-record evidence boundary: [`docs/AUDIT_2026-10-11.md`](docs/AUDIT_2026-10-11.md). Full fresh external re-verification of every historical claim is not complete. BBC episode clocks labelled “Local time” do not establish Malta airtime. Optional daily expense rows are traveler-input templates, not price estimates; avoid double counting with aggregate rows.

The deployed site still needs no runtime dependencies or build. Development tests use Node22+, Python3, and npm-distributed headless Chromium (Linux x64); `npm ci && npm test`. Browser setup extracts its bundled supporting libraries; generated screenshots/reports and node_modules are ignored. The suite checks all8active pages at360/768/1440px, WCAG2A/AA/2.1AA axe rules, data/render parity, navigation/deep links, filtering, expense persistence/CSV/reset, invalid amounts, denied/corrupt storage and data-fetch failures. It does not test physical radio reception, live external bookings, personal eligibility, or every browser/device.
