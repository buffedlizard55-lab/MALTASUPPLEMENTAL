# Malta Trip Guide

A mobile-friendly, source-linked planning site for the traveler-supplied **13–19 October 2026** Malta trip, based at **AX ODYCY in Qawra**, with the supplied Thunderpick CS2 event destination at **BLAST Arena Studios, Attard**. This is a planning aid, not a booking or guarantee. The traveler’s hotel reservation, event ticket, flights, party size, actual costs and final itinerary remain traveler-specific inputs.

**Published site:** <https://buffedlizard55-lab.github.io/MALTASUPPLEMENTAL/>

## Important findings

- **Event:** The Hotspawn/Eventbrite listing read on 11 October identifies BLAST Arena Studios Malta at MFCC South Gate National Stadium, ATD 4000 Attard, and lists 14–18 October, in-person attendance and ages 18+. It shows check-in/games for 14–16 October; the heading says 22:00 while Wednesday/Thursday agenda rows extend to 22:30. Saturday/Sunday entries were hidden behind a control. A separate listing capture and a CS2 news report record a “Free / Reserve a spot” offer, but the current text extraction did not expose a fee table. Confirm current availability and any total at checkout. No ticket or reservation is held; the attendee gate, per-day ticket rules and weekend agenda remain unknown.
- **Public transport:** One static Route 186 variant lists a 20:53 departure from Stadium stop 2194 toward Buġibba; that direction does not list an Il-Qawra stop. This is a route-specific risk, not proof that 20:53 is the network’s last bus or that a second boarding is always necessary. Route 214 lists Qawra stop 952 and Ta’ Qali Qali 2 stop 2542 as another route-level candidate. TQ1 may receive a special event timetable, but none was published for this event when checked. No date-specific, door-to-door journey or safe walking route was verified. Compare all options in Malta Public Transport’s live planner after confirming the gate and finish.
- **17 October diversion:** MPT’s Route 186 and latest-service-updates pages both show the October notice as 19:00–00:00 from 17 October, ending around midnight on 18 October. A separate older 20:00–00:00 notice ends around 21 April. The notice omits Gholja 2 through Targa toward Buġibba but does not give a replacement path or establish a particular event return. No 19:00–24:00 union is used.
- **Fares and taxis:** MPT lists €2.00 winter and €2.50 summer singles, but its only dated winter fare period ended 13 June 2026; the fare for this trip week is not published. Transport Malta’s maximum taxi tariff page says it was last updated in 2022; worked distance amounts are arithmetic at assumed distances, not quotes. AX ODYCY says Guest Relations can arrange taxis through a firm offering fixed charges, but no price is published. Taxi/ride-hailing remains a fallback, not an assumed requirement.
- **Practical travel and hotel:** The guide covers U.S.-traveler power, connectivity, safety, entry and customs pointers, health, weather, and hotel facilities. The MTA guideline PDF and service webpage use different wording about the “15-Night Threshold”; a six-night contribution calculation is conditional, not a confirmed charge. Official and secondary sources also conflict on EES enforcement in Malta. Check your booking and the relevant authorities before travel.
- **Sports radio:** The separate radio page distinguishes official FM/DAB+ schedules from technical directory leads, physical reception and named-match carriage. UK BBC match listings do not establish Malta carriage, and BBC World Service’s Sportsworld is general live sport. No local receiver test or named-match carriage confirmation was obtained.
- **Food, activities and evidence coverage:** Pages cover restaurants, cafés, gaming, landmarks and dated events. Limited Google Maps/Reviews, TripAdvisor and Reddit/search views were accessible; direct Yelp, Instagram, TikTok, Facebook and X access was blocked or limited. This is not a comprehensive review-platform sample or universal ranking. Volatile details should be rechecked.
- **Expense planner:** The planner has 18 core categories and seven optional daily rows, all blank by default. Its itinerary paste-and-preview tool only fills blank budget fields after review. Values are stored in the current browser, with CSV export and reset; no personal costs or transportation choice is assumed.

## Pages

| Page | What it covers |
|---|---|
| [Overview](https://buffedlizard55-lab.github.io/MALTASUPPLEMENTAL/) | Planning priorities, evidence caveats, hotel base and flexible trip framework |
| [CS2 event](https://buffedlizard55-lab.github.io/MALTASUPPLEMENTAL/event.html) | Event listing, venue, visible agenda, tournament details and open access questions |
| [Transport](https://buffedlizard55-lab.github.io/MALTASUPPLEMENTAL/getting-around.html) | Airport and event options, public buses, taxis, fares, ferries, car hire and planner caveats |
| [Food & cafés](https://buffedlizard55-lab.github.io/MALTASUPPLEMENTAL/restaurants.html) | Sourced venues and dated platform/review limitations |
| [Activities & sights](https://buffedlizard55-lab.github.io/MALTASUPPLEMENTAL/activities.html) | Gaming, recreation, landmarks and trip-window events |
| [Everyday guide](https://buffedlizard55-lab.github.io/MALTASUPPLEMENTAL/everyday.html) | Practical U.S.-traveler information, with eligibility and date-sensitive caveats |
| [Sports radio](https://buffedlizard55-lab.github.io/MALTASUPPLEMENTAL/radio.html) | Malta radio schedules and reception/carriage distinctions |
| [Expense planner](https://buffedlizard55-lab.github.io/MALTASUPPLEMENTAL/costs.html) | Blank-by-default budget, itinerary quick-fill preview, local save and CSV |
| [Sources & status](https://buffedlizard55-lab.github.io/MALTASUPPLEMENTAL/sources.html) | Source log, open questions, status, handoff, plan and schema |

## Evidence and project notes

- [`docs/SOURCES.md`](docs/SOURCES.md) — claim-level source URLs, access dates, workstreams and limitations.
- [`docs/OPEN_QUESTIONS.md`](docs/OPEN_QUESTIONS.md) — unverified, conflicting and date-sensitive items.
- [`docs/STATUS.md`](docs/STATUS.md) — dated project and delivery snapshot, not a live dashboard.
- [`docs/HANDOFF.md`](docs/HANDOFF.md) — cross-workstream findings and follow-ups.
- [`docs/PLAN.md`](docs/PLAN.md) — ownership, evidence protocol and cumulative review plan.
- [`docs/FINAL_REPORT.md`](docs/FINAL_REPORT.md) — cumulative audit, results and remaining work.
- [`docs/AUDIT_2026-10-11.md`](docs/AUDIT_2026-10-11.md) — claim-level audit boundaries.
- [`data/record.schema.json`](data/record.schema.json) — canonical 13-field record schema.

The guides render from the topic JSON datasets. The local validator checks the exact schema, source-log URL coverage, JavaScript syntax, page/data wiring, local links and shared navigation. It is not an external URL crawler or a guarantee that an outside fact has not changed.

## Local preview and checks

The site is static HTML, CSS and JavaScript; there is no production build step. An HTTP server is needed for browser `fetch()` and planner `localStorage`:

```bash
python3 -m http.server 8080 --bind 0.0.0.0
# Open http://localhost:8080
```

Run the repository’s checks with Node.js 22+, Python 3 and npm-distributed Chromium:

```bash
npm ci
python3 scripts/validate_site.py
python3 scripts/check_javascript.py
node --check js/site.js
npm test
```

The suite checks all nine active pages at 320/360/768/1440 px, responsive overflow, axe WCAG 2A/AA/2.1AA rules, data/render parity, navigation/deep links, filtering, expense persistence/CSV/reset, invalid amounts, denied/corrupt storage and data-fetch failures. It does not test physical radio reception, external booking availability, a date-specific bus journey, every browser/device or exhaustive assistive-technology compatibility. Generated screenshots/reports and `node_modules` are ignored.

## 11 October research and verification boundary

This is a dated planning aid, not a booking or live-service guarantee. A separate 11 October listing-card capture and HLTV report record a “Free / Reserve a spot” offer for the TWC, but the current extracted Eventbrite text did not expose a fee table; this does not establish current price, inventory, the traveler’s reservation or guaranteed admission. The listing showed agenda entries for 14–16 October only, with a 22:00 headline and Wednesday/Thursday rows extending to 22:30. The 17–18 October agenda, attendee gate and ticket validity remain open. See `event.html`, `docs/SOURCES.md` and `docs/OPEN_QUESTIONS.md`.

The BBC episode records name seven UK Premier League commentaries for 17–18 October; those schedules are not evidence of Malta radio reception, BBC Sounds access, World Service carriage or named-match carriage on a local service. The DAB+ “Sports Channel” identity/block and MTA short-stay “15-night” wording remain unresolved; the published bus single-fare seasons do not establish a date-specific fare for 13–19 October. Review-platform coverage is partial. No full external-link crawl, dated end-to-end transit journey, physical transit/radio test or device-based visual/accessibility audit was completed. Current blockers and source-specific limitations are maintained in the linked docs.
