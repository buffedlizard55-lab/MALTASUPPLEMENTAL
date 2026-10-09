# PLAN — Malta / Thunderpick WC 2026 trip site (merged)

Last updated: 9 Oct 2026 · Owner: workstream G · **Merged after the rebase of the
trip-planning branch onto `main`** (which had received the parallel Qawra re-base via
PRs #8/#9).

## What this project is

A tourism, recreation and logistics site for a trip to Malta to attend the **Counter-Strike 2
Thunderpick World Championship 2026 Finals**. It exists so that a traveller can find food,
activities, transport and everyday-life information quickly, on desktop or mobile, with every
fact traceable to a source.

## Confirmed trip parameters (see `data/trip.json`)

| Item | Value | Source |
|---|---|---|
| Hotel | AX Odycy, Qawra Coast Road, Qawra SPB 1902, Malta | axhotelsmalta.com/odycy/ (+contact page) |
| Room | Deluxe sea view | supplied by traveller |
| Dates | 13 Oct 2026 → 19 Oct 2026 (6 nights, 7 days) | supplied by traveller |
| Event | Thunderpick World Championship 2026 Finals (CS2) | Thunderpick PRNewswire, 13 Aug & 16 Sep 2026 |
| Event dates | 14–18 Oct 2026 | as above, corroborated by HLTV calendar |
| Event venue | BLAST Arena Studios, Malta Fairs & Conventions Centre, Ta' Qali, ATD 4000, Ħ'Attard | BLAST attendee guide (+ visitmalta.co.uk listing) |

## Two parallel sessions (9 Oct 2026) and the merge

Both sessions ran the user's parallel-work protocol on the same day, on session-pinned
branches (the platform does not permit creating/pushing other branches), so conflict
avoidance was enforced by **file ownership** instead of branch isolation — each workstream
touched only its own data file(s) and page(s); shared files only by G. The re-base session
merged first (PRs #8/#9); this branch was then **rebased onto main and merged (PR #11)**,
resolving every conflict by keeping the union of both workspaces' content. The full
resolution table is in `docs/STATUS.md` → "Rebase resolution".

## Workstreams and file ownership (integrated, post-merge)

| ID | Workstream | Data file(s) (owns) | Page(s) (owns) | Status |
|---|---|---|---|---|
| A | Transport — airport, hotel→venue on event days, buses, taxis, rideshare, rentals, cost/feasibility | `data/transport.json` | `getting-around.html` | done (both sessions merged) |
| B | Food and cafes | `data/food.json` (root-page mirror) + `data/venues.json` `on_site`/`nearby` (hotel.html mirror, re-base session) | `restaurants.html`, `hotel.html` | done |
| C | Gaming centres, activities, landmarks, events near the hotel | `data/activities.json` + `data/venues.json` `activities_landmarks` (re-base session) | `activities.html`, `landmarks.html`, `qawra.html`, `hotel.html` | done |
| D | Everyday life for a US traveller — plugs, SIM, money, safety, health, customs, language, weather | `data/everyday.json` | `everyday.html`, `logistics.html` | done |
| E | Radio sports broadcasts — Malta stations, FM/DAB+, official schedules, trip-date listings | `data/radio.json` | `radio.html` | done |
| F | Expense planner — data-driven template, quick to fill once the itinerary arrives | `data/expenses.json` | `costs.html` | done |
| G | Site shell, executive summary, navigation, integration — runs last | `data/trip.json` (shared parameters) | `index.html`, `itinerary.html`, `qawra.html`, `hotel.html`, `README.md`, `css/style.css`, `js/site.js`, `docs/*` | done |

Shared files (`index.html`, `README.md`, `css/style.css`, `js/site.js`, the navigation block
repeated on every page, and everything under `docs/`) are edited **only by workstream G**, or
serially after the other workstreams have finished.

## Dependencies

```
data/trip.json  (G, written first — everyone reads it)
      │
      ├──> A  data/transport.json ──> getting-around.html
      ├──> B  data/food.json + data/venues.json ──> restaurants.html, hotel.html
      ├──> C  data/activities.json + data/venues.json ──> activities.html, landmarks.html, qawra.html
      ├──> D  data/everyday.json ──> everyday.html, logistics.html
      ├──> E  data/radio.json ──> radio.html
      └──> F  data/expenses.json ──> costs.html
                     │
                     ▼
                G: index.html + itinerary.html + qawra.html + hotel.html + navigation + README + docs/
```

Nothing downstream of `data/trip.json` may contradict it. If a workstream finds that a trip
parameter is wrong, it edits `docs/HANDOFF.md`, not `data/trip.json`.

## Data schema (identical fields in every data item)

```
id, name, category, area, address, hours, price_range,
description, source_url, source_type, date_checked, confidence, notes
```

- `source_type` ∈ {`official`, `map`, `review`, `social`, `guide`}
- `confidence` ∈ {`verified`, `partially verified`, `unverified`}

Pages are generated from, or must match, the data files. A fact that is not in a data file
does not go on a page. Anything that cannot be verified goes to `docs/OPEN_QUESTIONS.md` — it
is never filled with a guess. (`data/schema.md` documents the same schema plus the
expense-planner extension fields `estimated_low/mid/high`, `actual`, `covered_by`.)

## Shared setup (done serially, before parallel work)

1. `data/` folder and the JSON schema — **done** (`data/trip.json`, `data/transport.json`,
   `data/venues.json`, then this branch's six topic files + `data/schema.md`)
2. `docs/` folder: `PLAN.md`, `SOURCES.md`, `OPEN_QUESTIONS.md`, `STATUS.md`, `HANDOFF.md` —
   **done** (both sessions; merged)
3. Folder structure and page conventions — **done** (flat HTML at repo root, `css/style.css`,
   `js/site.js`; the re-base session's `pages/*.html` summary stubs kept as a sub-site)
4. Design tokens — **this branch's full stylesheet** (the re-base session's reduced CSS would
   have broken both sessions' pages) + the 5 stub classes
5. Source-log format — **done** (`docs/SOURCES.md`: claim · URL · date accessed · workstream,
   merged from both sessions)

## Verification gates

1. **Per workstream** — every fact has a `source_url`; every link resolves; nothing marked
   `unverified` is presented on a page as fact.
2. **Integration** — run **both** scripts:
   - `scripts/check_links.py` (re-base session): internal links + anchors incl. the pages/
     stubs; navigation identical on every root page (incl. hotel.html); data schema for all
     data files; 13 load-bearing page assertions; forbidden patterns (no bare `Route X3`,
     no unverified Popeye route, gaming guard).
   - `scripts/verify_site.py` (this branch): JSON validity + schema (all 8 data files,
     140 items); data↔page consistency for the 6 page-mirrored topics across the 15 root
     pages; internal links + anchors; HTML tag balance; source-log coverage (every data
     `source_url` appears in docs/SOURCES.md).
3. **Passes 1–3** on the integrated result, not per branch: implement → review for bugs and
   wrong assumptions → re-check against the original request line by line. (Pass log:
   `docs/STATUS.md`.)

## Branching — adapted, and why

The protocol asks for one branch per workstream. **Both sessions were pinned to single
branches** (`arena/806552e3-maltasupplemental`, `arena/c4fd385c-maltasupplemental`,
`arena/8ed16394-maltasupplemental`), and the platform does not permit creating or pushing
other branches. The conflict-avoidance intent is therefore enforced by *file ownership*
instead of by branch isolation. When the second branch merged, it **rebased on main first**
and resolved every conflict explicitly (table in `docs/STATUS.md`).
