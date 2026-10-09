# PLAN — Malta / Thunderpick WC 2026 trip site

Last updated: 9 Oct 2026 · Owner: workstream G

## What this project is

A tourism, recreation and logistics site for a trip to Malta to attend the **Counter-Strike 2
Thunderpick World Championship 2026 Finals**. It exists so that a traveller can find food,
activities, transport and everyday-life information quickly, on desktop or mobile, with every
fact traceable to a source.

## Confirmed trip parameters (see `data/trip.json`)

| Item | Value | Source |
|---|---|---|
| Hotel | AX Odycy, Qawra Coast Road, Qawra SPB 1902, Malta | axhotelsmalta.com/odycy/ |
| Room | Deluxe sea view | supplied by traveller |
| Dates | 13 Oct 2026 → 19 Oct 2026 (6 nights, 7 days) | supplied by traveller |
| Event | Thunderpick World Championship 2026 Finals (CS2) | Thunderpick PRNewswire, 13 Aug & 16 Sep 2026 |
| Event dates | 14–18 Oct 2026 | as above, corroborated by HLTV calendar |
| Event venue | BLAST Arena Studios, Malta Fairs & Conventions Centre, Ta' Qali, ATD 4000, Ħ'Attard | BLAST attendee guide |

## Workstreams and file ownership

Each workstream owns exactly one data file and one page, and edits nothing else.

| ID | Workstream | Data file (owns) | Page (owns) | Status |
|---|---|---|---|---|
| A | Transport — airport, hotel→venue on event days, buses, taxis, rideshare, rentals, cost/feasibility | `data/transport.json` | `getting-around.html` | active |
| B | Food and cafes | `data/venues.json` (`on_site`, `nearby`) | `restaurants.html` | active |
| C | Gaming centres, activities, landmarks, events near the hotel | `data/venues.json` (`activities_landmarks`) | `activities.html`, `landmarks.html` | active |
| D | Everyday life for a US traveller — plugs, SIM, money, safety, health, customs, language, weather | `data/everyday.json` (not yet created) | `everyday.html` | carried over |
| E | Radio sports broadcasts — Malta stations, FM/DAB+, official schedules, trip-date listings | `data/radio.json` (not yet created) | `radio.html` | carried over |
| F | Expense planner — data-driven template, quick to fill once the itinerary arrives | `data/expenses.json` (not yet created) | `costs.html` | carried over |
| G | Site shell, executive summary, navigation — integrates the others, runs last | `data/trip.json` | `index.html`, `hotel.html`, `README.md`, `css/style.css`, `js/site.js`, `docs/*` | active |

Shared files (`index.html`, `README.md`, `css/style.css`, `js/site.js`, the navigation block
repeated on every page, and everything under `docs/`) are edited **only by workstream G**, or
serially after the other workstreams have finished.

## Dependencies

```
data/trip.json  (G, written first — everyone reads it)
      │
      ├──> A  data/transport.json ──> getting-around.html
      ├──> B  data/venues.json    ──> restaurants.html
      ├──> C  data/venues.json    ──> activities.html, landmarks.html
      ├──> D  data/everyday.json  ──> everyday.html
      ├──> E  data/radio.json     ──> radio.html
      └──> F  data/expenses.json  ──> costs.html
                     │
                     ▼
                G: index.html + hotel.html + navigation + README + docs/SOURCES.md rollup
```

Nothing downstream of `data/trip.json` may contradict it. If a workstream finds that a trip
parameter is wrong, it edits `docs/HANDOFF.md`, not `data/trip.json`.

## Shared setup (done serially, before parallel work)

1. `data/` folder and the JSON schema — **done** (`data/trip.json`, `data/transport.json`, `data/venues.json`)
2. `docs/` folder: `PLAN.md`, `SOURCES.md`, `OPEN_QUESTIONS.md`, `STATUS.md`, `HANDOFF.md` — **done**
3. Folder structure and page conventions — **done** (flat HTML at repo root, `css/style.css`, `js/site.js`)
4. Design tokens — **carried over** (existing `css/style.css`: `.hero`, `.card`, `.grid`, `.callout`, `.badge`, `.table-wrap`, `.stats`, `.pager`, breakpoints at 900px and 760px)
5. Source-log format — **done** (`docs/SOURCES.md`: claim · URL · date accessed · workstream)

## Data schema (identical fields in every data file)

```
id, name, category, area, address, hours, price_range,
description, source_url, source_type, date_checked, confidence, notes
```

- `source_type` ∈ {`official`, `map`, `review`, `social`}
- `confidence` ∈ {`verified`, `partially verified`, `unverified`}

Pages are generated from, or must match, the data files. A fact that is not in a data file does
not go on a page. Anything that cannot be verified goes to `docs/OPEN_QUESTIONS.md` — it is never
filled with a guess.

## Branching — adapted, and why

The protocol asks for one branch per workstream. **This session is pinned to a single branch,
`arena/806552e3-maltasupplemental`**, and the platform does not permit creating or pushing other
branches. The conflict-avoidance intent is therefore enforced by *file ownership* instead of by
branch isolation: each workstream above still touches only its own data file and page, and shared
files are touched only by G. That adaptation is recorded here and in `docs/STATUS.md` so a future
session does not mistake it for an oversight.

## Verification gates

1. **Per workstream** — every fact has a `source_url`; every link resolves; nothing marked
   `unverified` is presented on a page as fact.
2. **Integration** — after all workstreams land, run `scripts/check_links.py`: internal links,
   navigation consistency across every page, data↔page consistency.
3. **Passes 1–3** on the integrated result, not per branch: implement → review for bugs and
   wrong assumptions → re-check against the original request line by line.
