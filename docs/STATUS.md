# STATUS — workstream tracker

| Workstream | Status | Blockers | Last updated |
|---|---|---|---|
| Shared setup (docs/, data schema, script, nav) | **done** | — | 2026-10-09 |
| A Transport | **done** — `data/transport.json` + getting-around.html (Qawra + event-day plan) | 2026/27 winter-fare window unpublished; 186 timings from unofficial atlas (route existence official) | 2026-10-09 |
| B Food & cafés | **done** — `data/food.json` + restaurants.html (Qawra §0 added) | Login-walled review platforms (aggregator signal only) | 2026-10-09 |
| C Activities/gaming/landmarks + Qawra base | **done** — `data/activities.json`, `data/qawra.json` + activities.html, landmarks.html, qawra.html (new) | BirguFest 2026 dates conflicting; Comino operator prices unverified | 2026-10-09 |
| D Everyday life (US) | **done** — `data/everyday.json` + everyday.html (SIM section added) | — | 2026-10-09 |
| E Radio sports broadcasts | **done** — `data/radio.json` + radio.html (trip-weekend playbook added) | 17–18 Oct Sportsworld commentary pick publishes T-7; talkSPORT 2 DAB+ carriage in Malta unverified | 2026-10-09 |
| F Expense planner | **done** — `data/expenses.json` + costs.html (template table + 6-night calculator) | Final itinerary numbers pending | 2026-10-09 |
| G Integration & site shell | **done** — index/exec summary, nav (Qawra Base added), badges, validation script, docs | — | 2026-10-09 |
| Integration check (`scripts/check-data.py`) | **run** — see PR notes | — | 2026-10-09 |
| Passes 1–3 | **pass 1 done**; pass 2–3 in progress at session end | — | 2026-10-09 |

## Session summary (9 Oct 2026)

- Rebuilt the site around the confirmed itinerary: **AX ODYCY, Qawra, 13–19 Oct 2026**.
- Event confirmed: TWC 2026 Finals **14–18 Oct**, BLAST Arena Studios (MFCC), Ta' Qali, Ħ'Attard.
- Event-day answer: **bus 186** (direct Qawra→Ta' Qali, ~32 min); Bolt/eCabs fallback ≈ €15–25.
- New `data/` layer (7 files, schema-validated) + `docs/` protocol files + `scripts/check-data.py`.
- New page: **qawra.html** (hotel & neighbourhood). Nav updated on all pages.
