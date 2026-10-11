# Malta Trip Guide

A mobile-friendly, source-linked travel guide for the trip window **13–19 October 2026**, based at the user-supplied **AX ODYCY, Qawra Coast Road, Qawra SPB 1902** (Deluxe Sea-View room). The event location supplied by the traveler is **BLAST Arena Studios, Attard**.

**Published guide:** <https://buffedlizard55-lab.github.io/MALTASUPPLEMENTAL/>

The official Thunderpick page rechecked on 10 October lists the overall 2026 event window as 12–19 October (arrival 12th, media day 13th, Group Stage 14–16th, Playoffs 17–18th, departure 19th). The Thunderpick-issued release names BLAST Studios Malta; venue listings and BLAST’s attendee guide place BLAST Arena Studios at the MFCC South Gate National Stadium, Attard ATD 4000. None of these sources confirms this traveler’s spectator access, ticket, daily public door times, exact event entrance, or transport. Those details remain open.

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

- **Event and venue:** the official Thunderpick page lists the 12–19 October event window and Malta as its location. The Thunderpick release names BLAST Studios Malta; BLAST Arena Studios is listed at MFCC South Gate National Stadium, Attard ATD 4000 (venue listings from Visit Malta, Eventworks and Liquipedia; a BLAST guide for another event gives MFCC/Ta’ Qali context only). The TWC entrance and gate are not separately confirmed. Public spectator access, ticket arrangements, door times, and the event-day entrance remain unconfirmed.
- **Event-day transit:** Route 186 is the leading public-bus corridor between Qawra and Ta’ Qali; Route 214 is an alternate to compare. MPT’s static listing shows Qawra stop 952 at 06:09–21:39 at 30-minute intervals (checked 11 Oct). The normal Rabat-to-Buġibba return runs via St Paul’s Bay/Buġibba, not the Qawra seafront, with a final listed arrival at Buġibba Bay 1 at 21:26—this is not a guaranteed hotel return. MPT also lists a 17 October evening diversion (19:00 to approximately midnight); confirm the exact stops, walking segments, live timetable, and detour impact close to travel.
- **Radio:** NET FM is listed at FM 101 MHz and has recurring weekend sports shows; its grid does not explicitly state a time zone. Malta’s DAB+ directory lists Radio Sportiva and BBC World Service. WorldDAB lists BBC World Service on Digi B Network block 6A at 181.936 MHz, but reception at the hotel/event venue is untested and Radio Sportiva’s current block/frequency was not found. No radio carriage of the TWC, Gżira United–Mosta, or Rolex Middle Sea Race was confirmed. Unverified leads: a Friday 18:30 NET FM slot (‘Mhux Premier biss’, 16 Oct) and a WorldDAB ‘Sports Channel’ on Digi B 2 (12A). Premier League live audio is internet/app-based, and its availability in Malta was not confirmed; BBC Radio 5 Live Premier League listings are UK-based.
- **Hotel environmental contribution:** Malta Tourism Authority guidance checked 10 October states €1.50 per night per person aged 18+ from 1 July 2026, capped at €22.50 per eligible person per visit. Six chargeable nights would be €9 per eligible adult, conditionally; actual billable nights, guest ages, and the hotel invoice determine the amount. The planner does not prefill a personal charge.
- **Expense planner:** all budget and actual amounts start blank. Enter amounts in euros on a consistent whole-trip/party basis. The planner stores inputs in this browser/device only, does not send them to a server, exports a CSV backup, and can clear saved entries. Reference URLs are not price quotes.
- **Research-platform limits:** sampled TripAdvisor and a small number of Google Maps profile views informed parts of the food/activities research. Direct Yelp, Instagram, TikTok, Facebook, and X requests, and Reddit refreshes, were blocked or returned HTTP 403 in the relevant checks. Platform coverage is not comprehensive; see the dated notes in `docs/SOURCES.md` and the topic pages.
- **Open questions:** exact event access/times, saved date-specific transit route and return, 17 October diversion impact, trip-week radio schedule/carriage, current business hours/status conflicts, traveler-specific entry/insurance/device details, the booking itinerary, the emergency number (112 is not confirmed by a source read in this pass), and whether Airport Direct TD1 serves the Qawra stop remain unresolved as noted in `docs/OPEN_QUESTIONS.md`.

## Research records

- [`docs/SOURCES.md`](docs/SOURCES.md) — claim, URL, access date, workstream, and source limitations.
- [`docs/OPEN_QUESTIONS.md`](docs/OPEN_QUESTIONS.md) — missing, disputed, or date-sensitive information and how to resolve it.
- [`docs/STATUS.md`](docs/STATUS.md) — workstream progress and blockers.
- [`docs/HANDOFF.md`](docs/HANDOFF.md) — cross-workstream discoveries and follow-ups.
- [`docs/PLAN.md`](docs/PLAN.md) — scope, ownership, and verification plan.
- [`docs/DATA_SCHEMA.md`](docs/DATA_SCHEMA.md) — shared data conventions; topic records use the exact requested common key `price range`.
- [`data/record.schema.json`](data/record.schema.json) — canonical machine-readable schema for the exact 13 fields.

## Build, preview, and deployment

The site is static HTML, CSS, and JavaScript with JSON data; no application build or dependency installation is required. Repository Pages settings checked on 9 October 2026 publish the `main` branch root to the public site. Merging changes to `main` updates the site through GitHub Pages’ existing branch-based publishing. The `.nojekyll` file keeps the source/data tree static. A GitHub Actions workflow validates pull requests and pushes to `main`; it does not replace the configured Pages publisher.

For a local HTTP preview from the repository root:

```bash
python3 -m http.server 8080
# Open http://localhost:8080
```

An HTTP server is needed for browser `fetch()` and the expense planner’s `localStorage` behavior. The deployed planner saves only in the current browser/device; export a CSV before switching devices or clearing browser data.

The Pages workflow and local validator check the exact 13-field record schema and enums, HTTPS primary URLs and their source-log coverage, JavaScript syntax, topic-page/data wiring, and local links. External websites are not guaranteed to remain available; re-open primary sources before acting on date-sensitive information.
