# STATUS

Last updated: 9 Oct 2026

## Workstream status

| ID | Workstream | Status | Blockers | Last updated |
|---|---|---|---|---|
| Setup | Folder structure, data schema, docs, source-log format | **done** | — | 9 Oct 2026 |
| A | Transport (Qawra base) | **done for this session** — route 186, TD1, TD5, 214, 45 and all fares verified against the operator | OQ-02, OQ-03, OQ-04, OQ-08, OQ-09 | 9 Oct 2026 |
| B | Food and cafes (Qawra / St Paul's Bay) | **partial** — 7 on-site outlets verified from the operator; 10 nearby venues from aggregators | OQ-06, OQ-11, OQ-13 | 9 Oct 2026 |
| C | Activities, landmarks, gaming | **partial** — 7 landmarks verified by bus reachability; gaming centres unresolved | OQ-05, OQ-10 | 9 Oct 2026 |
| D | Everyday life (US traveller) | **carried over** from the previous session, not re-verified | — | 24 Sep 2026 |
| E | Radio sports broadcasts | **carried over** from the previous session, not re-verified | in-window schedules not published in advance | 24 Sep 2026 |
| F | Expense planner | **carried over**; still needs the 6-night correction | OQ-01 | 24 Sep 2026 |
| G | Site shell, exec summary, navigation | **in progress** — `hotel.html` added, navigation extended, index re-based on Qawra | OQ-01 | 9 Oct 2026 |

## What changed in this session

The site was built around a **Sliema** base. The traveller's actual hotel is **AX Odycy in Qawra**,
and the booking is **13–19 Oct 2026**, not 13–20 Oct. That invalidated the transport page's central
premise. This session:

1. Verified the hotel, its address and its 11 on-site outlets against the operator.
2. Found and verified the answer to the core question: **route 186 runs from the Qawra seafront
   straight to Ta' Qali**, every 30 minutes, with no change of bus — stop-level times read off the
   operator's own route page.
3. Verified TD1 / TD5 / 214 as the airport options that actually reach Qawra.
4. Re-verified every fare and travel card against the operator's live fares page.
5. Created the `data/` and `docs/` structure the project protocol requires.
6. Added `hotel.html`, extended the navigation, and re-based the executive summary on Qawra.

## Deviation from the protocol (recorded, not hidden)

The protocol asks for one branch per workstream. This session is pinned to
`arena/806552e3-maltasupplemental` and cannot create or push other branches, so conflict avoidance
was enforced by **file ownership** instead of branch isolation — each workstream still touched only
its own data file and page, and shared files only by G. See `docs/PLAN.md` → "Branching — adapted,
and why".

## Verification gate results

| Gate | Result |
|---|---|
| Every data item has a `source_url` | pass — except the two entries deliberately marked `unverified` with an empty source (gaming centres, Popeye Village route), which are recorded in OQ-05 / OQ-10 and are **not** presented as fact on any page |
| Every internal link resolves | checked by `scripts/check_links.py` — see the commit message for the run output |
| Navigation identical across all pages | checked by `scripts/check_links.py` |
| Data ↔ page consistency | checked by `scripts/check_links.py` (spot-asserts the load-bearing numbers) |
| Mobile + desktop layout | existing `css/style.css` breakpoints at 900px and 760px; new page uses only existing classes |
