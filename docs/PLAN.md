# PLAN — MALTASUPPLEMENTAL (session arena/9327905a-maltasupplemental)

**Date:** 9 Oct 2026 · **Trip:** 13–19 Oct 2026 (6 nights per hotel booking) · **Hotel:** AX ODYCY Malta,
Qawra Coast Road, Qawra SPB 1902 (Deluxe sea view) · **Event:** CS2 Thunderpick World Championship 2026,
BLAST Arena Studios, Attard (Malta Fairs & Conventions Centre, Ta' Qali, Ħ'Attard).

## Goal

A tourism & recreation companion site (GitHub Pages) for the trip: transport (esp. hotel → venue on event
days), food & cafés, gaming/activities/landmarks/events **around the hotel**, everyday-life guide for a US
traveler, live over-the-radio sports broadcasts (Kalshi-relevant: EPL etc.) with verified official schedules,
and a data-driven expense planner ready for the itinerary. Executive summary + sections + subpages, clean UI
on desktop and mobile. **No hallucinations:** every fact sourced, confidence labelled, gaps recorded.

## Workstream → owned files (conflict avoidance)

> **Branch note (deviation, documented):** the protocol suggests one branch per workstream. This Arena
> session is fixed to the single branch `arena/9327905a-maltasupplemental` and must not create other
> branches. Workstream isolation is therefore enforced **by file ownership only** — each workstream edits
> exactly its own `data/*.json` + `pages` and nothing else. Shared files are touched only by G (last) or
> serially in the shared-setup phase. A single PR merges the session branch to `main`.

| WS | Topic | Owned data file | Owned page(s) | Depends on |
|----|-------|-----------------|---------------|------------|
| A | Transport (airport↔hotel, hotel↔BLAST Attard on event days, buses, taxi/rideshare, rentals; cost/feasibility comparison) | `data/transport.json` | `getting-around.html` | shared setup |
| B | Food & cafés (around Qawra/hotel + island classics; Google/Maps/Yelp/IG/TikTok/FB/Reddit/X signal via aggregators) | `data/food.json` | `restaurants.html` | shared setup |
| C | Gaming centers, activities, landmarks, events near the hotel + island day-trips; hotel & Qawra base page | `data/activities.json`, `data/qawra.json` | `activities.html`, `landmarks.html`, `qawra.html` | shared setup |
| D | Everyday life for a US traveler (plugs/voltage, SIM/eSIM, money/tipping, safety, health, customs, language, weather) | `data/everyday.json` | `everyday.html` | shared setup |
| E | Radio sports broadcasts (Malta stations, FM/DAB+, official schedules, trip-date listings, Kalshi-relevant sports) | `data/radio.json` | `radio.html` | shared setup |
| F | Expense planner (data-driven template quick to fill once itinerary lands) | `data/expenses.json` | `costs.html` | shared setup (data schema), WS A/B/C prices at integration |
| G | Site shell, executive summary, navigation, integration, verification gates, README, docs | `data/integration.json` | `index.html`, `event.html`, `logistics.html`, `hotspawn.html`, `sources.html`, `css/`, `js/`, `README.md`, `docs/*` | A–F complete |

Cross-workstream notes go to `docs/HANDOFF.md` — **never** edit another workstream's files.

## Shared setup (done serially first)

1. Folder structure: `docs/`, `data/`, existing `css/ js/` + HTML pages kept (site is pre-existing).
2. Data schema (below) + validation script `scripts/check-data.py` (schema + data↔page consistency gate).
3. Site shell/nav: header/nav on every page; add **Your Base: Qawra & Hotel** (`qawra.html`) and
   **Expense Planner** anchor on costs; header dates updated to **Oct 13–19, 2026**.
4. CSS/design tokens: existing `css/style.css` kept as the token source (read-only for A–F).
5. Source-log format: `docs/SOURCES.md` table — Claim · URL · Date accessed · Workstream · Confidence.

## Data schema (every data file, every item)

```
id, name, category, area, address, hours, price_range, description,
source_url, source_type (official|map|review|social|news|community),
date_checked, confidence (verified|partially verified|unverified), notes
```

Pages are generated from / must match the data files. No fact appears on a page that is not in `data/`.
Anything unverifiable goes in `docs/OPEN_QUESTIONS.md` — **never fill gaps with guesses**.

## Verification gates

- Per-workstream self-check: every fact has a source; every link resolves; no unverified item as fact.
- Integration check after G: `scripts/check-data.py` (schema + page coverage), internal link check,
  mobile/desktop layout sanity, nav consistency.
- Then Passes 1–3 on the integrated result (implement → review for bugs/gaps/edge cases → re-check vs prompt).

## Reporting

`docs/STATUS.md` (workstream · status · blockers · updated), `docs/SOURCES.md` (master log),
`docs/OPEN_QUESTIONS.md` (gaps), `docs/HANDOFF.md` (cross-notes), final report in README + PR description.
