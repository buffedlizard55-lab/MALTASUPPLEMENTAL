# HANDOFF — notes between workstreams (merged)

Rule: if you find something that belongs to another workstream, write it here. Do not edit
their files. Workstream G sweeps this file at the end of each session and files the items.

**Merged 9 Oct 2026** from the Qawra re-base session (first sections) and this branch's
trip-planning pass (later sections).

## Raised 9 Oct 2026 (re-base session)

### For workstream F (expense planner)

- **The night count is wrong on `costs.html`.** It is built for 7 nights / 8 days. The booking is
  **13–19 Oct 2026 = 6 nights / 7 days**. The calculator's `c_nights` default and any hard-coded
  "7 nights" copy need to change. (Raised by A and G; tracked as OQ-01.)
  → **Done in this branch:** costs.html rebuilt for 6 nights; calculator default `c_nights` = 6;
  eco-tax default $11 (6 × €1.50 = €9.00); food 7 days.
- **Transport budget can now be bottom-up instead of a band.** €25 Explore Adult 7-Day card
  covers the whole week including every event-day round trip on route 186, plus €3.00–€3.50
  each way for the two airport hops = **€31–€32 of committed transport spend**, before any
  rideshare. That is far tighter than the "€35–60" band on `getting-around.html`.
  → **Kept as a band** on costs/expenses (it includes 2–3 rideshare backup runs); the €31–32
  committed figure is now noted in `data/expenses.json` (exp-transport).
- **New unavoidable line item: late-night return from Ta' Qali.** The last route 186 back is
  published around 21:26 (Bugibba Bay 1) and no night bus serves Ta' Qali. Any match ending
  after roughly 20:45 needs a rideshare or taxi. The price is unknown (OQ-04), so it must be
  budgeted as a range with the range's basis stated, not as a number.
  → **Done:** the 21:26 limit is stated on getting-around § 0 and in data/transport.json.

### For workstream B (food)

- AX Odycy has **eleven** food and drink outlets on site (operator's own structured data). For a
  Qawra base the on-site and Dawret il-Qawra options are the ones that need zero transport.
  `data/venues.json` → `on_site` has them with sources; this branch's `data/food.json` carries
  the same outlets plus 16 nearby restaurants + 7 cafés (restaurants.html § 0).
- **Minoa is adults-only** (operator's page) — stated on the pages so nobody plans a family
  dinner there.
- None of the AX Odycy outlets publish opening hours (OQ-13) — flagged, not implied.

### For workstream C (activities / gaming)

- **No gaming centre or LAN venue near Qawra could be verified** (both sessions, 9 Oct 2026).
  `data/venues.json` carries an explicitly empty `unverified` entry; this branch's
  `data/activities.json` lists the basic internet cafés (Cyber Zone, A.A, 24/7) and the three
  real venues (Gamers Lounge Msida, Esports Plaza Sliema, Eden Esports St Julian's) with
  call-ahead flags. Do not fill the gap from memory.
- The Qawra bus network makes a specific set of day trips *verifiable by route*: Mdina/Rabat
  and Mosta and Ta' Qali on **186**; Valletta on **45** (peak-only caveat, OQ-09); Sliema on
  **212**; Ċirkewwa for Gozo on **221** or **TD1**; Golden Bay on **223**.

## Raised 9 Oct 2026 (this branch — trip-planning pass)

- (setup) Trip parameters confirmed: AX ODYCY Qawra (Deluxe sea view), 13–19 Oct 2026. Every
  workstream keys prices/dates to **6 nights / 7 days**, base **Qawra**.
- (A→G) The event-day hotel→venue plan lives on getting-around § 0 (id="eventdays") and is
  mirrored by `itinerary.html` — the itinerary links to it, it does not re-derive it.
- (B→C) Near-hotel food picks belong to `data/food.json` (restaurants.html § 0); qawra.html
  and hotel.html link to them rather than duplicating them. Two datasets coexist after the
  merge: `data/food.json` (root-page mirror) and `data/venues.json` (hotel.html mirror) —
  consolidate in a future session.
- (E→F) The DAB+ radio cost line (€25–60 estimate) feeds the expense planner's "fixed
  extras" default note.
- (F→G) Expense planner defaults (nights=6, food $30/day, transport band) match the calculator
  defaults on costs.html and the executive summary's headline budget band ($370–866 /
  $790–1,646).
- (G, integration) New pages `itinerary.html` and `qawra.html`; the re-base session's
  `hotel.html` kept. One 15-link navigation on all 15 root pages. `pages/*.html` remain the
  re-base session's stub sub-site (they defer to the main site where they disagree).
- (G→next session) After merge: re-verify the public Pages URL rebuilds from main; run a
  bulk external link checker from a networked environment; fill the expense planner Actual
  column when the confirmed itinerary arrives; consolidate `data/food.json` +
  `data/venues.json` and `qawra.html` + `hotel.html` if the duplication bothers you.
