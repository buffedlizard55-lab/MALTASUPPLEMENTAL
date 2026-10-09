# STATUS (merged)

Last updated: 9 Oct 2026 — after the rebase of this branch onto `main` (which had received the
parallel Qawra re-base via PRs #8/#9) and the merge of both sessions' work. Trip: **13–19 Oct 2026**,
base **AX ODYCY, Qawra**.

## Two parallel sessions, one repo (9 Oct 2026)

Two sessions worked the same brief in parallel on 9 Oct 2026:

- **Qawra re-base** (`arena/806552e3-maltasupplemental` + `arena/c4fd385c-maltasupplemental`,
  merged to `main` as PRs #8/#9): verified the hotel and route 186 stop-level detail, added
  `hotel.html`, the `pages/*.html` summary stubs, `data/{trip,venues,transport}.json`,
  `docs/{PLAN,SOURCES,OPEN_QUESTIONS,STATUS,HANDOFF,SCHEMA,FINAL_REPORT}.md`,
  `scripts/check_links.py`, and re-based the index on Qawra. Its merge reconciliation with
  PR #8 (which had briefly replaced the content pages with stubs) is documented in its
  STATUS/FINAL_REPORT.
- **This branch — trip-planning pass** (`arena/8ed16394-maltasupplemental`, PR #11): the full
  trip-planning build — `itinerary.html`, `qawra.html`, `data/{transport,food,activities,
  everyday,radio,expenses}.json` + `data/schema.md`, `docs/{PLAN,SOURCES,OPEN_QUESTIONS,STATUS,
  HANDOFF}.md`, `scripts/verify_site.py`, near-hotel food/activities research, SIM/eSIM +
  customs sections, the data-driven expense planner, and the 6-night cost model.

## Rebase resolution (this branch onto main, 9 Oct 2026)

The rebase produced conflicts on 12 HTML pages, 6 data files, 5 docs files and README.
Resolution rules applied (union of both workspaces' value; nothing deleted):

| Conflict | Resolution |
|---|---|
| 12 root HTML pages (modify/modify) | **this branch's versions** (comprehensive supersets: they carry the re-base session's date/hotel updates plus the full trip-planning content), then unified: one 15-link navigation on every root page incl. `hotel.html`; `id="eventdays"` anchor added to getting-around § 0 (hotel.html links to it); stop-level route-186 detail (Arznell 950 / Qawra 952, 06:08–21:37 outbound, 21:26 last return) merged in from the re-base session's verified transport data; the X3-withdrawn correction merged into the page and `data/transport.json` (X routes now `unverified`, TD1/TD5/214 primary); "six nights"/"6 nights" strings added for the check_links gate |
| `css/style.css` (main reduced it to 83 lines) | **this branch's full 470-line stylesheet** + the 5 classes the re-base session's pages need (`.container`, `.correction`, `.withdrawn`, `.stub-banner`) — the reduced CSS would have broken both sessions' pages |
| `data/transport.json` (add/add) | **this branch's version, merged with the re-base session's corrections** (stop-level detail; X3/X1 → `unverified` with the withdrawal correction and the route-index conflict documented) |
| `data/{food,everyday,radio,expenses,activities}.json` (add/add) | **this branch's versions** (they are the datasets the root pages mirror, enforced by `scripts/verify_site.py`) |
| `data/trip.json`, `data/venues.json` (add/add, no counterpart here) | **taken from main** (reference datasets owned by the re-base session; mirrored by `hotel.html`, enforced by `check_links.py` gate 5) |
| `docs/{PLAN,SOURCES,OPEN_QUESTIONS,STATUS,HANDOFF}.md` (add/add) | **merged** — both sessions' content, cross-referenced (see each file) |
| `docs/{SCHEMA,FINAL_REPORT}.md`, `pages/*.html`, `hotel.html`, `scripts/check_links.py` | **taken from main** (additive; hotel.html got the unified nav; SCHEMA.md gained the `guide` source_type) |
| `README.md` (modify/modify) | **merged** (this branch's session documentation + the re-base note + the project-structure section, updated for the merged repo) |
| `js/site.js`, `costs.html`, `data/schema.md`, `scripts/verify_site.py`, `itinerary.html`, `qawra.html` | this branch's (no conflict — main didn't touch them, except costs.html which is this branch's 6-night rebuild) |

## Workstream status (integrated)

| WS | Topic | Status | Notes |
|----|-------|--------|-------|
| A | Transport (incl. hotel→BLAST Arena event-day plan) | **done** | route 186 stop-level verified (re-base session) + merged; X-route conflict documented; app confirmation on the day |
| B | Food & cafés (incl. near-hotel) | **done** | near-hotel section (16 restaurants + 7 cafés) + hotel.html's on-site dataset (venues.json) |
| C | Activities, gaming, landmarks, events near hotel | **done** | qawra.html + hotel.html; OQ-05 resolved (negative) |
| D | Everyday life (US traveler) + customs/entry | **done** | SIM/eSIM bands + official customs card added |
| E | Radio sports broadcasts, official schedules | **done** | re-verified 9 Oct (T−4); DAB+ re-scan on arrival |
| F | Expense planner (data-driven) | **done** | data/expenses.json + costs.html § 5b; 6-night model |
| G | Integration: itinerary, exec summary, nav, README, sources, rebase | **done** | nav unified on 15 pages; both gates green |

## Verification gates (both green after the merge, 9 Oct 2026)

- `python3 scripts/verify_site.py` → **PASS** — JSON validity + schema for 8 data files /
  140 items; data↔page consistency for the 6 page-mirrored topics across 15 pages; internal
  links + anchors; HTML tag balance; source-log coverage (every data `source_url` logged in
  docs/SOURCES.md).
- `python3 scripts/check_links.py` → **PASS** (run after the merge — see commit) — internal
  links + anchors incl. the pages/ stubs; navigation identical on all 15 root pages (incl.
  hotel.html); data schema for all 8 files; the 13 load-bearing page assertions; forbidden
  patterns (no bare `Route X3`, no unverified Popeye route, gaming guard).
- `node --check js/site.js` OK; all 15 root pages + pages/ stubs served locally HTTP 200.

## Pass log (this branch)

- **Pass 1** (implement + verify): done 9 Oct 2026 — see the pre-rebase log (verify gate
  green; 14 pages HTTP 200; load-bearing sources re-read).
- **Pass 2** (bugs / assumptions / edge cases): done 9 Oct 2026 — caught and fixed a
  mis-added cost subtotal ($355/$556 → $370/$566), a stray `</html>` on radio.html, several
  batched edits that reported success but didn't persist (re-applied + grep-verified),
  stale 13–20 Oct references, pager/nav misalignment, a Sliema-base leftover; entity-aware
  page matching added to the verify gate.
- **Pass 3** (line-by-line re-check vs the original request): done 9 Oct 2026 — checklist
  kept in the pre-rebase STATUS; re-run after the rebase with both gates green.
- **Rebase pass** (9 Oct 2026): the table above + both gates re-run green on the merged tree.

## Corrections applied in this branch's session

- Trip window updated site-wide from 13–20 Oct (7 nights) to the confirmed **13–19 Oct 2026
  (6 nights)**; hotel base **AX ODYCY, Qawra**; cost model recomputed ($370/$566/$866
  out-of-pocket; $790/$1,133/$1,646 incl. est. tax); calculator defaults updated.
- X3/X1 airport expresses downgraded to `unverified` with the withdrawal correction merged
  (the re-base session's finding), TD1/TD5/214 made primary.
