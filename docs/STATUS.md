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

## Merge reconciliation with PR #8 (9 Oct 2026)

While this branch was being worked on, **PR #8 merged to `main`** from a different workstream.
It deleted 3,544 lines — eleven content pages (`event`, `restaurants`, `landmarks`, `activities`,
`getting-around`, `everyday`, `radio`, `costs`, `logistics`, `hotspawn`, `sources`) — and replaced
them with six short `pages/*.html` summaries plus its own `data/` and `docs/` files. Merging was
therefore not a fast-forward and produced 20 conflicts.

**How each conflict was resolved, and why:**

| Conflict | Resolution | Reason |
|---|---|---|
| 11 content pages (modify/delete) | **kept this branch's versions** | main deleted them; they hold the verified, sourced content this project is for |
| `README.md`, `index.html`, `css/style.css` | **kept this branch's versions** | strictly larger; main's are reduced versions of the same files |
| `data/transport.json` (add/add) | **kept this branch's version** | main's recommends a withdrawn route — see below |
| `docs/PLAN|SOURCES|OPEN_QUESTIONS|STATUS|HANDOFF.md` (add/add) | **kept this branch's versions** | 6–48 lines on main vs full logs here |
| `docs/FINAL_REPORT.md`, `docs/SCHEMA.md` | **taken from main** | additive, no conflict |
| `data/{activities,everyday,expenses,food,radio}.json`, `pages/*.html` | **taken from main, then corrected** | additive workstream E/F content this branch lacked |

**Corrections made to what came in from main** — none of these were optional, because each was a
claim badged `verified` that the cited source does not support:

1. **Route X3 was recommended as the way to the venue.** X3 was **withdrawn on 20 April 2025** and
   replaced by route 214. It was badged `confidence: verified`, `source_type: official`,
   `date_checked: 2026-10-09`. It also never served the MFCC — its routing passed *Qali 2 on the
   main road*. Corrected in `pages/transport.html`, struck through with the reason, and the real
   answer (route 186) put in its place.
2. **"TalkSport (DAB+ Malta)" was `verified`** on `radioinmalta.com`, a third-party station
   directory. The multiplex operator's own catalogue does not list it. Downgraded to
   `partially verified`, `source_type: review`. **Radio Sportiva** cited the same directory and was
   downgraded the same way.
3. **"Michele's Cafe" was `partially verified`** on `https://www.tripadvisor.com/` — the homepage,
   not a listing. Downgraded to `unverified`; it must not be presented as a recommendation.
4. **The €12–25 rideshare figures were badged `verified`.** No operator publishes a Qawra↔Ta' Qali
   fare. Left as an estimate, logged as **OQ-04**.

A correction note recording all four was prepended to `docs/FINAL_REPORT.md` rather than the
original text being quietly rewritten.

**Regression guards added** so this cannot come back silently:
`scripts/check_links.py` now scans the `pages/` stubs and `data/*.json` as well as the root pages,
and fails on any bare `Route X3` mention outside an explicit correction, and on any
gaming-category item that places itself near Qawra/Bugibba while claiming to be verified.

Two bugs were found **in the checker itself** while proving those guards worked, and both are worth
recording because a guard that cannot fail is worse than no guard:

- The forbidden-pattern gate only walked root pages, so a regression shipped into `pages/` passed
  silently. Found by re-injecting the PR #8 X3 text and watching the gate stay green.
- The first two gaming patterns were prose regexes and false-fired on this project's own honest
  sentences — `"Gaming centres / LAN venues near Qawra"` and `"Gamers Lounge … no verified Qawra
  branch"`. A regex cannot tell an assertion from a denial, so the guard was moved into the data
  gate where it can read the `confidence` field instead of guessing.
