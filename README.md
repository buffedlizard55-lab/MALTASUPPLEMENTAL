# Malta Trip Guide

A responsive, source-linked planning guide for the traveler-supplied **13–19 October 2026** stay at **AX ODYCY, Qawra Coast Road, Qawra SPB 1902, Malta**, in a **Deluxe sea-view room**, and attendance plans for the **Thunderpick Counter-Strike 2 Finals** at BLAST Arena Studios, Attard. The room, stay and booking details are user inputs, not independently verified reservations.

**Website:** <https://buffedlizard55-lab.github.io/MALTASUPPLEMENTAL/>

## Start here

| Page | Purpose |
|---|---|
| [Overview](index.html) | Executive summary, hotel checklist, dated trip framework and section links |
| [Event desk](event.html) | Published event listing, daily agenda, third-party bracket clocks, access checklist and evidence |
| [Transport](getting-around.html) | Airport/hotel/event options, per-date planning, fare products, buses, taxi/ride-hail, rental and ferry comparison |
| [Food & cafés](restaurants.html) | Hotel dining, nearby and wider-area food, menus, review evidence and platform limitations |
| [Activities & sights](activities.html) | Gaming/arcade status, landmarks, recreation and dated event leads |
| [Everyday guide](everyday.html) | U.S.-traveler power, connectivity, money, entry/customs, safety, health and weather |
| [Sports radio](radio.html) | Terrestrial stations, receiver compatibility, official schedules and trip-window sports |
| [Expense planner](costs.html) | Blank-by-default budget, itinerary quick-fill preview, autosave and export/restore |
| [Sources & status](sources.html) | Source log, limitations, open questions and project reports |

## Decision-critical facts and limits

**Evidence snapshot:** the source reads below were made on **11 October 2026**. This continuation reconciles stored data and page copies against those reads; it did **not** make a new external-page fetch, date-specific journey-planner query, live ride quote, venue visit or radio-receiver test. See [`docs/SOURCES.md`](docs/SOURCES.md), [`docs/OPEN_QUESTIONS.md`](docs/OPEN_QUESTIONS.md) and [`docs/FINAL_REPORT.md`](docs/FINAL_REPORT.md) for dated details and delivery state.

- **Event listing and ticket:** Eventbrite identifies an in-person, 18+ event at BLAST Arena Studios Malta / MFCC South Gate, Attard, for 14–18 October. Its latest ticket-section extraction showed **no event-specific price or reservation action**; “Free / Reserve a spot” appeared only in a “You might also like” card. HLTV’s 2 October free-ticket report is secondary evidence, not current checkout price or inventory. Confirm the actual terms, your own access and the attendee gate with the organizer. The visible agenda covers 14–16 October; its 22:00 page headline conflicts with Wed/Thu rows extending to 22:30. Weekend door times were not visible.
- **Match clocks:** third-party Liquipedia bracket starts read on 11 October list Saturday semifinals at 16:00 and 19:00, and Sunday third-place/final at 13:30 and 17:00 Malta time (pairings TBD). These are match starts, **not organizer door or finish times**.
- **Event transport:** Routes 186 and 214 are candidates from the Qawra side to the Ta’ Qali area, not saved hotel-to-gate journeys. Route 186 toward Buġibba does not list an Il-Qawra stop and terminates at Buġibba Bay 1, so an onward connection must be checked. An earlier Route 186 extraction reported a Stadium 2194 return at 20:53/20:54, but later reads did not reproduce that row; other timetable variants are unlabelled. No dated MPT planner result exists in this guide. Do not treat a static time as the last bus or assume every event finish is later than every possible bus. Check the actual date, direction, gate and onward Qawra journey in MPT’s planner; compare a current ride quote or leave early if its result does not fit. Saturday 17 October has an operator-published 19:00–00:00 diversion window; its exact effect on a journey is not established.
- **Fares:** MPT’s table still prints the winter-single period as 19 October 2025–13 June 2026, not the 2026/27 boundary. Two third-party 2026 fare guides imply a likely €2.50 single on 13–18 October and €2.00 on 19 October. This is an inference, not an operator-confirmed trip-week fare. Taxi/rideshare costs are dynamic and not quoted in the guide.
- **Entry and weather:** the EU ETIAS FAQ read 11 October says the system is not operating, applications are not being collected, travellers need take no action “at this point,” and the EU will announce the start date several months ahead. On that published status and notice process, no ETIAS authorisation is required for this trip; follow any new official notice. EES has a separate, unresolved Malta-specific implementation conflict. The Malta Met Office forecast snapshot covers through 18 October; the UK Met Office Valletta snapshot extends through 19 October (19 marked BETA). The official panels differ; neither forecast is a guarantee.
- **Radio:** station schedules, Malta carriage, compatible receiver, local reception and named-match audio are separate questions. UK BBC schedules are not proof of Maltese carriage; no physical DAB+/FM scan was made. Sports markets/fixtures do not prove radio carriage or a market-to-broadcast link.
- **Food, gaming and activities:** review counts and platform order are dated snapshots, not a universal ranking. Several requested social/review services were blocked or unreadable from this environment. Arcades are distinct from a public PC-gaming café; no public PC café was verified in the available research. Dated activity listings and their hours/prices retain source-specific caveats.
- **Planner:** all amounts start blank. Do not treat published fare/menu/taxi references as quotes, purchases, a booked itinerary or traveler-specific costs. Entries autosave only in the current browser; export a CSV or JSON backup before switching devices.

## Development and validation

Static HTML/CSS/JavaScript and seven JSON datasets; no production build or runtime package installation.

```sh
npm ci
npm test
python3 -m http.server 8080 --bind 0.0.0.0
```

Tests need Node 22 and Python 3.10+ and use the Linux Chromium setup from `tests/browser-setup.js`. For another supported Chromium installation, set `CHROMIUM_PATH`; `SITE_URL` can target an already-running test server. `npm test` runs exact-schema/source-log/local-link checks, JavaScript syntax checks and Playwright/axe tests. These checks establish software behavior, not the truth or live availability of external listings.

`main` is the GitHub Pages publishing branch (`.nojekyll`). Current branch, local gate, pull-request and Pages status must be recorded in [`docs/FINAL_REPORT.md`](docs/FINAL_REPORT.md) only after each state is observed. The old one-shot editor `scripts/session_update.py` is disabled historical code; do not run it on current data. Current fact corrections are reflected in the canonical topic JSON and their page copies.