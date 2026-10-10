# Malta Trip Guide

A mobile-friendly, source-linked travel guide for the trip window **13–19 October 2026**, based at the user-supplied **AX ODYCY, Qawra Coast Road, Qawra SPB 1902** (Deluxe Sea-View room). The event location supplied by the traveler is **BLAST Arena Studios, Attard**.

**Published guide:** <https://buffedlizard55-lab.github.io/MALTASUPPLEMENTAL/>

The official Thunderpick page checked on 9 October lists the 2026 Finals Group Stage on 14–16 October and Playoffs on 17–18 October. Thunderpick names BLAST Studios Malta; a BLAST attendee guide for a different event identifies the studio as being at the Malta Fairs & Conventions Centre (MFCC), Ta’ Qali, Ħ’Attard. Neither source confirms this traveler’s spectator access, ticket, daily public door times, or exact entrance. Those details remain open.

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
| [Expense planner](https://buffedlizard55-lab.github.io/MALTASUPPLEMENTAL/costs.html) | 18 editable budget/actual categories, local browser autosave, CSV export, and reset |
| [Sources & status](https://buffedlizard55-lab.github.io/MALTASUPPLEMENTAL/sources.html) | Links to the evidence log, open questions, workstream status, handoffs, plan, and schema |

## Key findings and limits

- **Event and venue:** official Thunderpick sources list the Group Stage and Playoffs dates. The BLAST guide supplies venue/address corroboration only; public spectator access, ticket arrangements, door times, and event-day entrance instructions were not confirmed.
- **Event-day transit:** Route 186 is the leading direct public-bus candidate between Qawra and Ta’ Qali; Route 214 is an alternate to compare. The Route 186 timetable is not a saved hotel-to-venue itinerary. MPT lists a 17 October evening diversion (19:00 to approximately midnight); confirm the exact outbound/return stops, walking segments, live timetable, and effect of the diversion close to travel.
- **Radio:** NET FM is listed at FM 101 MHz and has recurring weekend sports shows. Malta’s DAB+ directory lists Radio Sportiva and BBC World Service. Exact DAB+ block/frequency and reception at the hotel/event venue remain unverified; no radio carriage of the TWC, Gżira United–Mosta, or Rolex Middle Sea Race was confirmed. Do not rely on fixtures or general sports listings as proof of carriage.
- **Expense planner:** all budget and actual amounts start blank. Enter amounts in euros on a consistent whole-trip/party basis. The planner stores inputs in this browser/device only, does not send them to a server, exports a CSV backup, and can clear saved entries. Reference URLs are not price quotes.
- **Research-platform limits:** sampled TripAdvisor and a small number of Google Maps profile views informed parts of the food/activities research. Direct Yelp, Instagram, TikTok, Facebook, and X requests, and Reddit refreshes, were blocked or returned HTTP 403 in the relevant checks. Platform coverage is not comprehensive; see the dated notes in `docs/SOURCES.md` and the topic pages.
- **Open questions:** exact event access/times, saved date-specific transit route and return, 17 October diversion impact, trip-week radio schedule/carriage, current business hours/status conflicts, traveler-specific entry/insurance/device details, and the booking itinerary remain unresolved as noted in `docs/OPEN_QUESTIONS.md`.

## Research records

- [`docs/SOURCES.md`](docs/SOURCES.md) — claim, URL, access date, workstream, and source limitations.
- [`docs/OPEN_QUESTIONS.md`](docs/OPEN_QUESTIONS.md) — missing, disputed, or date-sensitive information and how to resolve it.
- [`docs/STATUS.md`](docs/STATUS.md) — workstream progress and blockers.
- [`docs/HANDOFF.md`](docs/HANDOFF.md) — cross-workstream discoveries and follow-ups.
- [`docs/PLAN.md`](docs/PLAN.md) — scope, ownership, and verification plan.
- [`docs/DATA_SCHEMA.md`](docs/DATA_SCHEMA.md) — shared data conventions.

## Build, preview, and deployment

The site is static HTML, CSS, and JavaScript with JSON data; no application build or dependency installation is required. Repository Pages settings checked on 9 October 2026 publish the `main` branch root to the public site. Merging changes to `main` updates the site through GitHub Pages’ existing branch-based publishing. The `.nojekyll` file keeps the source/data tree static. A GitHub Actions workflow validates pull requests and pushes to `main`; it does not replace the configured Pages publisher.

For a local HTTP preview from the repository root:

```bash
python3 -m http.server 8080
# Open http://localhost:8080
```

An HTTP server is needed for browser `fetch()` and the expense planner’s `localStorage` behavior. The deployed planner saves only in the current browser/device; export a CSV before switching devices or clearing browser data.

The Pages workflow and local validation script check JSON/schema, JavaScript syntax, topic-page/data wiring, and local links. External websites are not guaranteed to remain available; re-open primary sources before acting on date-sensitive information.
