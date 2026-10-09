## Summary
Rebuilds the MALTASUPPLEMENTAL site around the confirmed itinerary — **AX ODYCY Malta, Qawra (Deluxe sea view), 13–19 Oct 2026** — and implements the parallel-work protocol: `docs/` planning artefacts, a schema-validated `data/` layer (single source of truth), an integration-check script, and refreshed research across all seven workstreams.

## What's in the box
- **A Transport** — Qawra-centric `getting-around.html`: **event-day plan (bus 186 direct Qawra→Ta' Qali ~32 min)**, airport TD1/TD5/214 + white-taxi bands, official 2026 fares & cards (Explore €25 / Flex €27 / 12-journey €19), rideshare, ferries. `data/transport.json` (18 records).
- **B Food** — Qawra/Buġibba section (Venus 4.8/2.9k, Chatterbox 4.9, Ta' Pawla…, hotel dining), Maltese classics, $30/day plan. `data/food.json` (21).
- **C Activities/Qawra** — new **qawra.html** (hotel + walkable neighbourhood), in-window events (Middle Sea Race 17 Oct, In Guardia, Gozo festival; BirguFest date conflict flagged), gaming lounges, day trips. `data/activities.json` (14) + `data/qawra.json` (10).
- **D Everyday** — SIM/eSIM section (2026 prices), plugs/230 V, 112, money/VAT/tipping, weather, customs. `data/everyday.json` (10).
- **E Radio** — trip-weekend playbook: **EPL MW7 slate in Malta time**, BBC WS Sportsworld + talkSPORT on Malta **DAB+ 6A**, verified weekend schedule pattern, NFL/UEFA notes, **Kalshi: Malta not restricted** (Member Agreement 21 Sep 2026). `data/radio.json` (14).
- **F Expenses** — data-driven 10-line template + 6-night calculator (2-minute fill when the itinerary lands). `data/expenses.json`.
- **G Shell** — executive summary rewrite, Qawra Base nav on every page, sources appendix (9 Oct session), README, STATUS/OPEN_QUESTIONS/HANDOFF.

## Verification
- `python3 scripts/check-data.py` → **ALL CHECKS PASSED** (schema, 97 data records, data↔page id coverage, internal links, nav).
- Facts sourced in `docs/SOURCES.md` (claim · URL · date · workstream · confidence); gaps logged in `docs/OPEN_QUESTIONS.md`; unverified items labelled on-page. Login-walled platforms (Google/Yelp/IG/TikTok/FB/X/Reddit) documented as aggregator-only signal.

## Known limitations (also in README / OPEN_QUESTIONS)
BirguFest 2026 dates conflict (do not plan around); winter-fare switchover unpublished (trip straddles); Sportsworld/talkSPORT picks for 17–18 Oct publish T-7; Comino boats / Saluting Battery / Gaming Lounge rates / Qawra–Ta' Qali taxi fare unpriced by design; Hotspawn written confirmations still outstanding.

## Next session
Fill the planner from the itinerary · T-7 re-checks (186 times, radio picks, BirguFest, EES) · book the Hypogeum · collect the prize confirmations · bring/buy a DAB+ radio.
