# HANDOFF — notes between workstreams

Rule: if you find something that belongs to another workstream, write it here. Do not edit their
files. Workstream G sweeps this file at the end of each session and files the items.

## Raised 9 Oct 2026

### For workstream F (expense planner)

- **The night count is wrong on `costs.html`.** It is built for 7 nights / 8 days. The booking is
  **13–19 Oct 2026 = 6 nights / 7 days**. The calculator's `c_nights` default and any hard-coded
  "7 nights" copy need to change. (Raised by A and G; tracked as OQ-01.)
- **Transport budget can now be bottom-up instead of a band.** A concrete per-day figure is
  possible: the €25 Explore Adult 7-Day card covers the whole week including every event-day
  round trip on route 186, plus €3.00–€3.50 each way for the two airport hops = **€31–€32 of
  committed transport spend**, before any rideshare. That is far tighter than the "€35–60" band
  currently on `getting-around.html`.
- **New unavoidable line item: late-night return from Ta' Qali.** The last route 186 back is
  published around 21:26 and no night bus serves Ta' Qali. Any match ending after roughly 20:45
  needs a rideshare or taxi. The price is unknown (OQ-04), so it must be budgeted as a range with
  the range's basis stated, not as a number.

### For workstream B (food)

- AX Odycy has **eleven** food and drink outlets on site (operator's own structured data). The
  restaurants page currently leads with island-wide Top-10 lists; for a Qawra base the on-site and
  Dawret il-Qawra options are the ones that need zero transport. `data/venues.json` → `on_site`
  has them with sources.
- **Minoa is adults-only** (operator's page). Worth stating so nobody plans a family dinner there.
- None of the AX Odycy outlets publish opening hours (OQ-13), which matters when matches are
  running — flag it rather than implying you can book around them.

### For workstream C (activities / gaming)

- **No gaming centre or LAN venue near Qawra could be verified.** `data/venues.json` carries an
  explicitly empty `unverified` entry rather than a name (OQ-05). Do not fill it from memory.
- The Qawra bus network makes a specific set of day trips *verifiable by route*, which is stronger
  evidence than a distance: Mdina/Rabat and Mosta and Ta' Qali on **186**; Valletta on **45**
  (peak-only caveat, OQ-09); Sliema on **212**; Ċirkewwa for Gozo on **221** or **TD1**; Ġgantija…
  no — Ġnaj Tuffieha / Golden Bay on **223**. All from the operator's stop listings.
- **Ta' Qali is not only the venue.** Route 186 serves both "Ta' Qali Stadium" and "Ta' Qali
  Villagg", so the craft village and aviation-museum area are on the same 30-minute ride — a
  sensible non-match-morning plan.

### For workstream E (radio)

- Nothing this session touches radio, but note the base change: any "listen in the hotel room"
  assumption should now say **Qawra**, and DAB+ coverage in the north-east of the island was never
  verified for this specific location. Reception inside a large seafront hotel is untested.

### For workstream G (shell)

- The header on every page reads **"Oct 13–20, 2026"**. It should read **Oct 13–19, 2026**. This is
  a shared file, so only G may change it (OQ-01).
- `landmarks.html` is structured as an **8-day** visit plan. With 6 nights it needs to become a
  7-day plan. Shared-page edit — G only.
- `sources.html` has not been given the 9 Oct 2026 rows yet; they are in `docs/SOURCES.md` and need
  to be rolled up into the page.
