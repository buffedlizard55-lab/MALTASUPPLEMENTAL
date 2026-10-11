# Malta Trip Guide

A responsive, source-linked planning guide for the traveler-supplied **13–19 October 2026** stay at **AX ODYCY, Qawra Coast Road, Qawra SPB 1902, Malta**, in a **Deluxe sea-view room**, and the **Counter-Strike 2 Thunderpick World Championship 2026**. Those room/stay details are inputs, not independently verified bookings.

**Website:** <https://buffedlizard55-lab.github.io/MALTASUPPLEMENTAL/>

## Start here

| Page | Purpose |
|---|---|
| [Overview](index.html) | Six canonical summary cards, hotel checklist and guide links |
| [Event desk](event.html) | Advertised access, five day cards, departure checklist and expandable venue/bracket/broadcast reference |
| [Transport](getting-around.html) | Airport and hotel–event route candidates, fares/cards, late-return checks, taxis, rentals and ferries |
| [Food & cafés](restaurants.html) | Operator/menu evidence, nearby and wider-area options, closure warnings and review-platform limitations |
| [Activities & sights](activities.html) | Gaming/arcades, landmarks and dated recreation/event leads |
| [Everyday guide](everyday.html) | US-to-Malta power, connectivity, money, entry/customs, health, safety and weather |
| [Sports radio](radio.html) | Terrestrial receiver/service leads and schedules—not a collection of online streams |
| [Expense planner](costs.html) | 18 core and seven optional daily rows, blank amounts, quick-fill preview, autosave, CSV and JSON backup/restore |
| [Sources & status](sources.html) | Dated source log, access limits, open questions and project reports |

## Important findings and limits

- **Event:** Hotspawn's Eventbrite listing read 11 October advertises free in-person ages-18+ reservations for 14–18 October at BLAST Arena Studios Malta / MFCC South Gate National Stadium, Attard. Wed/Thu show 09:30 check-in, 10:30 games and a 22:30 agenda end; Friday shows 14:00, 15:00 and 21:00. The headline instead ends at 22:00. Weekend agenda/FAQ answers were not visible in the extraction—not proven unpublished. Confirm the timezone, gate, day validity, inventory and your reservation. The organizer's wider 12–19 October window includes production/travel days. See the [canonical event reference](event.html).
- **Transport:** Route 186 is a candidate, not a verified door-to-door journey or last-bus result. One static return variant ends at 20:53 at Stadium 2194 and goes toward Buġibba, not the Qawra seafront. Check both directions, walks and alternatives for the actual date. April's 20:00 diversion and October's 19:00 notice are separate; the October extraction lacks a year. The trip-week single fare/card coverage and best-value purchase remain checks, not assumed costs. Hotel-arranged fixed-charge taxis are an option to quote; the regulator's meter-reference webpage is dated April 2022. No live quote or five-ride purchase is assumed.
- **Food and recreation:** the shortlist distinguishes official menus/hours, third-party review evidence, closed/conflicted businesses and out-of-window events. Featured/sponsored listing order is not a popularity rank. No walk-in PC café was confirmed. Dated attractions still need inventory, weather and transport checks; UNO's 17 October listing has no explicit year in the fresh extraction.
- **Everyday:** Type G, 230 V / 50 Hz; check each device's label. The hotel's 110 V bathroom outlet is razor-only. Primary MTA sources give €1.50/night for eligible adults, capped at €22.50 per visit; six qualifying nights would be €9/adult, not a known invoice. No short-stay exemption is inferred from a contradictory general webpage. ETIAS was not operational when checked; personal entry/insurance/device eligibility remains untested. The fresh national weather panel covers the trip only through 17 October.
- **Radio:** no named trip-week match is verified through the complete chain of official commentary schedule, Malta over-the-air carriage, compatible receiver and actual local reception. BBC Sportsworld's official episode clocks convert to 15:06 Saturday 17 and 16:06 Sunday 18 October in Malta, but no named match/feed is established. UK BBC commentary, fixtures, Kalshi markets and internet streams do not prove Malta RF carriage. The Sports Channel 6C/12A identity/block conflict remains unresolved.
- **Research limits:** limited Google Maps and TripAdvisor views; the sampled Yelp, Instagram, TikTok, Facebook, Reddit and X direct refreshes were blocked. Historical indexed observations are labelled historical, not fresh review text. Not every inherited source was externally rechecked in full. See [the audit](docs/AUDIT_2026-10-11.md) and [open questions](docs/OPEN_QUESTIONS.md).

## Use the expense planner

Enter euros consistently for the whole trip/party. Choose aggregate categories **or** daily rows for a purchase; never both. Published references are not quotes or default purchases.

1. Paste `date | description | EUR amount`, then preview the keyword-based suggestions.
2. Review the mapping and unresolved lines. Accepted distinct lines in the same category are summed; existing budget fields are never overwritten. Foreign-currency/ambiguous amounts and deposits/holds require manual review.
3. Keep refundable holds in notes and enter only retained charges. No currency conversion is performed.
4. Save a **JSON backup** for validated, confirmation-gated restore on this or another device. **CSV is for spreadsheets/manual re-entry**, not automatic restore. Inputs stay in this browser's local storage; there is no account, server sync or payment integration.

Do not put sensitive booking/payment details on a shared device. Back up before clearing site data. Quick-fill is a simple matcher, not an itinerary-understanding or accounting guarantee.

## Development and deployment

Static HTML/CSS/JavaScript and seven JSON datasets; no production build or runtime package installation. GitHub Pages publishes the `main` branch root (`.nojekyll`). All browser paths are relative, including project-prefix hosting.

```sh
npm ci
npm test
python3 -m http.server 8080 --bind 0.0.0.0
```

Tests need Node 22 and Python 3.10+ and use a Linux Chromium setup from `tests/browser-setup.js`. For another supported Chromium installation, set `CHROMIUM_PATH`; `SITE_URL` can target an already-running test server. `npm test` runs exact-schema/source-log/local-link checks, JavaScript syntax checks and Playwright/axe tests. The GitHub validation workflow runs on PRs and pushes to `main`.

Tests establish software behavior—not the truth or live availability of an external listing. Current observed runs and delivery boundaries are in [the final report](docs/FINAL_REPORT.md).

## Maintainer records

- [Plan and fixed-branch ownership protocol](docs/PLAN.md)
- [Exact 13-field data schema](docs/DATA_SCHEMA.md) and [JSON Schema](data/record.schema.json)
- [Sources](docs/SOURCES.md), [open questions](docs/OPEN_QUESTIONS.md), [status](docs/STATUS.md), [handoffs](docs/HANDOFF.md)
- [Audit and per-record evidence scope](docs/AUDIT_2026-10-11.md), [final report](docs/FINAL_REPORT.md)

This session preserves the upstream event/hotel additions from PRs #42/#43 while reconciling unsupported transport, fare, timing and radio inferences. Earlier reports are available in Git history; they are not the current delivery/evidence statement.
