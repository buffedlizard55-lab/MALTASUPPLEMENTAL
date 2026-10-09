# OPEN QUESTIONS — things that could not be verified (merged register)

Rule for this file: if it is in here, it is **not** stated as fact anywhere on the site.
Nothing on this list has been filled in with a guess.

**Merged 9 Oct 2026** from two parallel sessions: the Qawra re-base (OQ-01…OQ-13, merged to
`main` via PRs #8/#9) and this branch's trip-planning pass (PR #11). Status notes below record
what each session did with the item.

## OQ register (re-base session, 9 Oct 2026)

| ID | Question | Why it is open | Blocks | First raised | Status after PR #11 |
|---|---|---|---|---|---|
| OQ-01 | Which dates are authoritative: the booking's **13–19 Oct 2026** (6 nights) or the **13–20 Oct 2026** (7 nights) the prize Terms carry? | The traveller supplied 13–19 Oct with the AX Odycy booking; the Terms say 13–20 Oct. | Night counts, eco-tax, food days | 9 Oct 2026 | **Partially resolved:** costs/landmarks/itinerary/radio rebuilt for 6 nights; the Terms' 13–20 window remains quoted+flagged where verbatim. Reconcile when the booking confirmation is in hand. |
| OQ-02 | What is the **2026/27 winter-fare switchover date**? | The operator's fares page still states the winter window as 19 Oct 2025 → 13 Jun 2026 — stale relative to the trip. 2026 guides put summer €2.50 through 18 Oct and winter €2.00 from 19 Oct (inference from guides, not the operator). | Whether a single journey costs €2.00 or €2.50 on 19 Oct | 9 Oct 2026 | Open — flagged on getting-around.html; confirm on the operator page a week out. |
| OQ-03 | What is the **published fixed taxi fare from MLA to Qawra**? | The airport's own fare-table page 404s; the airport now points to the licensed operator Malta Taxi. Guide tables say €25–28. | A concrete airport→hotel taxi figure | 9 Oct 2026 | Open — band €25–28 used with a flag; confirm at the kiosk. |
| OQ-04 | What does a **Bolt/eCabs/Uber ride from Qawra to Ta' Qali** actually cost? | Fares are only revealed in-app from a live GPS position; no published price list. Guide band ≈ €10–18. | The late-night event-day return budget | 9 Oct 2026 | Open — budgeted as a range with the basis stated. |
| OQ-05 | Is there a **gaming centre / LAN venue** within reach of Qawra? | None could be verified in Qawra itself (both sessions searched 9 Oct 2026). The real venues are in Msida/Sliema/St Julian's. | Activities page completeness | 9 Oct 2026 | **Resolved (negative):** no Qawra gaming venue exists; basic internet cafés only (Cyber Zone, A.A, 24/7). The three real venues are listed with call-ahead flags. |
| OQ-06 | **Google Maps, Yelp, Instagram, TikTok, Facebook and X** could not be queried directly. | Login walls and no API access from this environment. Their signal reaches this site only through named aggregators (TripAdvisor ranked lists, things.in, operator pages, Apple Maps). | The original request asked for these platforms specifically | 9 Oct 2026 | Open (environmental) — method notes on restaurants.html and sources.html § 11. |
| OQ-07 | Do the **per-day match times** for TWC 2026 exist yet? | Not published at check time (format page still "stay tuned", re-read 9 Oct 2026). | The event-day transport plan's precision | 9 Oct 2026 | Open — the Itinerary skeleton carries the blanks. |
| OQ-08 | Will route **186 be diverted during 14–18 Oct 2026**? | The operator's live service-updates page lists detours for 10–14 Oct, none on 186; a cached **2025** snapshot showed a weekend 186 detour starting 17 Oct (2025 — weekdays don't line up with 2026). | Nothing, if re-checked in the week of travel | 9 Oct 2026 | Open — re-check item, flagged in data/transport.json transport-186. |
| OQ-09 | Is route **45 (Qawra → Valletta) peak-hours-only**? | A 2025 third-party bus atlas records it as Mon–Fri peak-only; the operator's route page was not read closely enough to confirm or deny. | Off-peak Valletta day trips by bus | 9 Oct 2026 | Open — flagged, not asserted. |
| OQ-10 | Which **bus route serves Popeye Village from Qawra**? | The stop exists in the operator's national stop list ("Bus Stop 1005 Popeye") but no Qawra→Popeye route was verified. | Popeye Village as a confirmed day trip | 9 Oct 2026 | Open — data/venues.json carries an explicitly empty `unverified` entry. |
| OQ-11 | Is **Café del Mar** still operating its beach-club/pool side in mid-October? | Seasonal operation likely but unconfirmed. (Its daily 10:00–00:00 hours and the Sun 18 Oct free CDM Sundays session ARE confirmed on the venue's own event site.) | A beach-club recommendation | 9 Oct 2026 | Partially resolved — hours + CDM Sundays verified (sundays.com.mt, 9 Oct); pool-side operation unconfirmed. |
| OQ-12 | Does the hotel or **Cheeky Monkey Gastropub screen the tournament**? | No source either way. | The "watch it locally" plan for non-attendance days | 9 Oct 2026 | Open — ask on arrival. |
| OQ-13 | Do **AX Odycy's restaurants publish opening hours**? | Not on the operator's pages at check time. | Booking dinner around match times | 9 Oct 2026 | Open — flagged on qawra.html/restaurants.html. |

## Additional items (this branch's trip-planning pass, 9 Oct 2026)

- [ ] **X-route status conflict (X1–X4).** This branch's read of the operator's route index (9 Oct 2026) lists X1–X4; the re-base session recorded the airport X services as **withdrawn 20 Apr 2025** (replaced by TD; 214 took over the X3 corridor); 2026 guides describe X1–X4 as operating. Merged position: treat all X routes as unconfirmed; use TD1/TD5/214; confirm in the tallinja app. (data/transport.json transport-x1 / transport-x3 = `unverified`.)
- [ ] **Hotel booking confirmation not in hand** — the brief states AX ODYCY, Deluxe sea view, 13–19 Oct 2026; the site leads with it, but the confirmed check-in/out dates (and who pays) should be entered in the expense planner when the confirmation arrives.
- [ ] **Who pays for hotel/flights** (prize vs. self-pay) is not stated in the 9 Oct brief — `covered_by` stays TBD in data/expenses.json.
- [ ] Whether the operator runs **TQ special shuttles** (Ta' Qali ↔ Qawra/Buġibba) for TWC — precedent exists (Earth Garden 2023); none announced as of 9 Oct 2026.
- [ ] Exact tallinja stop + first/last 186 departures **in the app on the day** — stop-level times were read off the operator's route page by the re-base session and merged here, but the page is JS-driven; the app is authoritative on the day.
- [ ] **talkSPORT/"Sports Channel"** on DAB+ 6C — three directory sources vs. the operator's absent catalogue entry; tune in on arrival.
- [ ] **DAB+ 6A/6C carriage as of October 2026** — last receiver observation 13 Jan 2026; re-scan on arrival.
- [ ] Unpublished schedules: BBC Sportsworld's commentary pick, talkSPORT's Malta feed for 17–19 Oct, Rai's October per-match assignments, UCL/UEL/NFL carriage in Malta, Middle Sea Race start hour, BirguFest 2026 dates (four conflicting sources).
- [ ] Unpriced: Comino boat fares, Saluting Battery, boat trips from Buġibba/Qawra (marketplace prices only), Mosta Rotunda admission, gaming-venue session rates.
- [ ] Carried from earlier sessions: EES "fully operational from 10 Apr 2026" date (23 Sep reading); ETIAS (not in operation — re-check); passport renewal if expiring before ~mid-Jan 2027 or issued >10 years ago; drinking age 17 (secondary sources); shop opening-hour patterns (no official 2026 source).

## Deliberately unpriced (no operator price found — not estimated)

- Comino boat fares (third-party operators only)
- Malta Taxi airport→Qawra (OQ-03)
- Rideshare Qawra↔Ta' Qali (OQ-04)
- Gaming-centre session rates (OQ-05)
- Popeye Village entry (OQ-10)
- Mosta Rotunda dome climb
- Boat trips from Buġibba/Qawra (St Paul's Islands / Comino day trips — marketplace listings only)
