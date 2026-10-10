# Malta Trip Companion

A mobile-friendly, source-linked static guide and editable expense planner for the supplied **13–19 October 2026** stay at **AX ODYCY Malta, Qawra**.

> **Trip facts supplied for planning:** AX ODYCY Malta, Qawra Coast Road, Qawra SPB 1902; travel window 13–19 October 2026. Those seven calendar dates equal six hotel nights only if the booking is check-in on 13 October and check-out on 19 October. Flight details, arrival/departure times, traveler count, confirmed tournament attendance and room total were not supplied.

## Executive summary

The site brings the trip's practical research into six focused topics: transport, food and cafés, activities and landmarks, everyday U.S.-traveler guidance, scheduled live-sport radio, and a quick-fill expense planner. Topic pages show structured records with source links, source types, check dates, confidence labels and caveats. Unknown hours, prices, access rules and schedules are identified rather than filled in with guesses.

The event-day transport page compares public and private options and identifies routes to check in the official operator planner. It is not a confirmed door-to-door itinerary: session times, the event-specific public entrance, the best hotel-side stop and the effect of the 17–18 October route notice still need date- and time-specific verification. The event page likewise does not establish spectator access or ticket terms.

The expense planner begins with blank, editable lines. It does not assume a meal allowance, taxi price, exchange rate, tax, tip, event attendance, payment or outside coverage. Optional published fare/admission references are not added unless selected. Planner entries stay in the current browser on the current device; they are not uploaded or synced.

## Browse the guide

| Topic | Page | What's there |
|---|---|---|
| Overview | [Trip summary](index.html) | Trip facts, the six topic links, priority caveats and research registers |
| Transport | [Getting around](pages/transport.html) | Airport options, local transport and event-day route comparisons; live timetable and access limitations |
| Food | [Food and cafés](pages/food.html) | Qawra-area options, venue details and separately dated review-platform signals |
| Activities | [Activities and sights](pages/activities.html) | Landmarks, gaming leads and dated event listings with access/availability caveats |
| Everyday travel | [Practical guidance](pages/everyday.html) | Source-linked U.S.-traveler, entry, money, phone, health, weather and local-practice checks |
| Radio | [Scheduled live-sport radio](pages/radio.html) | Officially listed broadcasts during the trip, Malta-local time calculations and reception limits |
| Budget | [Expense planner](pages/expenses.html) | Editable itinerary lines, totals, optional user-entered USD conversion, local saving, CSV and print |
| Evidence | [Sources and open questions](sources.html) | How evidence is recorded, checked and qualified |

## Evidence and limitations

- The topic records are in `data/*.json`; the pages under `pages/` render from those records. Each record follows the common fields in [`data/schema.md`](data/schema.md), including the exact `price range` key. Follow the source links on each record for the original evidence.
- The full source register is [`docs/SOURCES.md`](docs/SOURCES.md); unresolved decisions and source gaps are in [`docs/OPEN_QUESTIONS.md`](docs/OPEN_QUESTIONS.md). Cross-topic findings are in [`docs/HANDOFF.md`](docs/HANDOFF.md), and progress is in [`docs/STATUS.md`](docs/STATUS.md).
- Research is a dated snapshot, checked **9 October 2026**. Fares, hours, event listings, border/entry requirements, weather and schedules can change. Re-open the linked official operator, organizer or government source before booking or travelling.
- Some requested review/social platforms or operator subpages could not be accessed. Those limits and conflicts are stated in the relevant records and open-question register; inaccessible information is not treated as confirmed.
- This is a trip-planning aid, not live dispatch, a booking service, legal/tax/medical/immigration advice, or a guarantee of event access, radio reception or venue availability.

## Verify and run locally

Run the portable offline integration gate from the repository root:

```bash
python3 scripts/verify_site.py
```

It checks the JSON contract, source/question references, date and expense arithmetic, local paths/fragments, responsive-shell markers and compatibility redirects. It does not test external link liveness or replace a real-device visual review.

The site uses plain HTML, CSS and JavaScript without a build step or package dependencies. Serve the repository root over HTTP so the topic pages can fetch their JSON data:

```bash
python3 -m http.server 8000
```

Then open `http://localhost:8000/`. Do not open the data-driven pages as `file://` URLs. GitHub Pages can serve the same static site from the repository root.

## Repository layout

```text
index.html                 Executive summary
pages/                     Six topic pages
data/                      Structured research and planner starter data
  schema.md                Common topic-record schema
css/style.css              Responsive shared visual system
js/site.js                 Shared navigation and data renderer
scripts/verify_site.py     Offline integration gate (standard library only)
docs/PLAN.md               Scope, schema, ownership and review passes
docs/SCHEMA.md             Shared schema overview
docs/SOURCES.md            Source and verification log
docs/OPEN_QUESTIONS.md     Unresolved items and next actions
docs/HANDOFF.md            Cross-workstream research handoffs
docs/STATUS.md             Workstream progress
```

Legacy top-level topic URLs are retained as small redirects to the current pages; outdated prize/legal content is not part of this travel companion.
