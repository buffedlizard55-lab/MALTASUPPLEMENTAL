# MALTASUPPLEMENTAL

Tourism & recreation companion for the **Thunderpick World Championship 2026** trip to Malta —
**13–19 October 2026** (6 nights), staying at **AX ODYCY Malta**, Qawra Coast Road, Qawra SPB 1902
(Deluxe sea view), with the CS2 Finals at **BLAST Arena Studios** (Malta Fairs & Conventions Centre,
Ta' Qali, ATD 4000, Ħ'Attard), **14–18 October 2026**.

Built for a US (California) traveler: event-day transport, food, activities, everyday life, live sport on
the radio (Kalshi-relevant sports), and a fill-ready expense planner. **No hallucinations policy:** every
fact is sourced and confidence-labelled; anything unverifiable lives in `docs/OPEN_QUESTIONS.md` and is
labelled on-page — never guessed.

Live site (GitHub Pages): `https://buffedlizard55-lab.github.io/MALTASUPPLEMENTAL/`

## Pages

| Page | Contents |
|---|---|
| [Overview](index.html) | Executive summary — the five answers, verified/flagged ledger, next-session queue |
| [Qawra Base](qawra.html) | **Start here** — AX ODYCY hotel facts, what's walkable (aquarium, beach, casino, promenade), evening loops |
| [The Event](event.html) | TWC 2026 Finals: dates, venue, teams, format, streams, door/bag policy |
| [Getting Around](getting-around.html) | **Event-day transport (bus 186)**, airport transfers (TD1), fares & cards, taxis/rideshare, ferries — scored convenience/price/value/feasibility |
| [Food & Drink](restaurants.html) | Qawra/Buġibba standouts (ratings + review counts), hotel dining, Maltese classics, cafés, $30/day plan |
| [Landmarks](landmarks.html) | Valletta, Mdina, temples, Blue Grotto, Dingli, Three Cities, Gozo & Comino — official entry prices |
| [Activities & Gaming](activities.html) | In-window events (Middle Sea Race, In Guardia, Gozo festival), LAN cafés, diving, boats, beaches |
| [Everyday Life](everyday.html) | SIM/eSIM, plugs (Type G 230 V), 112, money/VAT/tipping, weather, health, customs, packing |
| [Radio & Kalshi](radio.html) | Malta FM/DAB+ dial, Sportsworld & talkSPORT live-PL windows, MW8 slate in Malta time, Kalshi-from-Malta rules |
| [Costs & Budget](costs.html) | Prize covers/excludes, tax question, **data-driven expense planner** (2-minute fill) |
| [Entry & Address](logistics.html) | Entry checklist, EES/ETIAS, the confirmed hotel & venue addresses |
| [Hotspawn & Prize](hotspawn.html) | Giveaway audit, Terms clause table, confirmations checklist (privacy-scrubbed) |
| [Sources](sources.html) | Every URL used, tagged Official / Verified / Estimate / Flag + not-found register |

## Repository structure

```
data/            # single source of truth — schema in data/SCHEMA.md
  transport.json food.json activities.json qawra.json everyday.json radio.json expenses.json
docs/            # workstream protocol artefacts
  PLAN.md SOURCES.md STATUS.md OPEN_QUESTIONS.md HANDOFF.md
scripts/
  check-data.py  # integration gate: schema + data↔page coverage + link + nav checks
*.html css/ js/  # static GitHub Pages site (no build step; js/site.js = mobile nav + calculator)
```

Every page item is backed by a `data/*.json` record (fields: id, name, category, area, address, hours,
price_range, description, source_url, source_type, date_checked, confidence, notes). Pages show the record
`id` as the row anchor so data ↔ page consistency is machine-checkable:

```bash
python3 scripts/check-data.py   # must print ALL CHECKS PASSED
```

## How this was built (workstream protocol)

Workstreams A–G owned disjoint files (A transport, B food, C activities/Qawra, D everyday, E radio,
F expenses, G shell/integration) — see `docs/PLAN.md`. Cross-workstream notes went to `docs/HANDOFF.md`;
the master claim log is `docs/SOURCES.md`. This Arena session worked on a single branch
(`arena/9327905a-maltasupplemental`) with file-ownership isolation instead of one branch per workstream,
then merged to `main` via one PR.

## Verified headline facts (9 Oct 2026 session)

- **Event:** TWC 2026 Finals Oct 14–18, BLAST Studios Malta (MFCC, Ta' Qali, Ħ'Attard), 8 teams, $1M —
  organiser PR + HLTV + BLAST's own venue guide (bag policy, prohibited items).
- **Event-day transport:** bus **186** is the only one-seat bus from Qawra/Buġibba to Ta' Qali (~32 min);
  fares official at publictransport.com.mt (Day €2.50/€2.00; Explore 7-day €25; Explore Flex €27 incl.
  Airport Direct; TD1 €3.50). Bolt/eCabs ≈ €15–25 for late returns *(estimate)*.
- **Radio:** BBC World Service (Sportsworld, live PL at weekends) and talkSPORT both on Malta's **DAB+
  block 6A**; MW8 fixtures land 17–19 Oct exactly — see the Radio page's Malta-time table. **Kalshi: Malta
  is not a restricted jurisdiction** (Member Agreement 21 Sep 2026).
- **Everyday:** Type G / 230 V, 112, eSIM/SIM €10–15, VAT-included prices, ~25 °C and swimmable seas.

## Known limitations (detail in docs/OPEN_QUESTIONS.md + on-page flags)

- Google Maps reviews, Yelp, Instagram, TikTok, Facebook, X and Reddit are login-walled from the research
  environment — popularity signal enters via TripAdvisor/Wanderlog aggregators and named community threads
  only. Every such item is labelled `review`/`community` with confidence ≤ "partially verified".
- BirguFest 2026 dates conflict across sources (9–10 vs 16–17 Oct) — **do not plan around it** until the
  Birgu Local Council confirms.
- The tallinja winter-fare switchover (historically ~19 Oct) is unpublished for 2026/27 — the trip straddles
  it (at worst €0.50/ride).
- Sportsworld/talkSPORT publish their exact weekend commentary picks only days ahead — re-check T-7.
- Unpriced on purpose (no official source found): Comino boats (except the official Explore Flex bundle),
  Saluting Battery, Gamers Lounge session rates, the Qawra–Ta' Qali taxi fare (map estimate only).
- Prize paperwork (Hotspawn): written coverage/waiver confirmations still outstanding — see
  [Hotspawn & Prize](hotspawn.html) before non-refundable bookings.

## Next-session work queue

1. Itinerary arrives → fill `data/expenses.json` + the [calculator](costs.html#budget-calc) (2 minutes).
2. T-7 re-checks: 186 times in the tallinja app · Sportsworld/talkSPORT picks for 17–18 Oct · winter-fare
   date · BirguFest · Gozo Highspeed restricted sailings (14 & 17 Oct) · EES status · Middle Sea Race gun
   time · passport validity.
3. Book the Hypogeum (€35, 10 per tour) if wanted — hard booking constraint.
4. Collect the five written confirmations in the [Hotspawn checklist](hotspawn.html); screenshot the
   intermittent giveaway/Terms pages.
5. Price Comino boats + Saluting Battery from operators; buy/bring a **DAB+ radio** (US AM/FM ≠ DAB+).
6. Kalshi: screenshot kalshi.com/legal + help before flying (they can amend the restricted list unilaterally).

## Privacy

The private Hotspawn correspondence is strictly internal — no email content, handles or names appear in this
repository. If you contribute: never commit email text, names, handles or home addresses.

## Disclaimer

Research for personal travel planning — not legal, tax, immigration or betting advice. Estimates are labelled;
re-open every primary source before acting. Nothing here authorises betting or trading anywhere.
