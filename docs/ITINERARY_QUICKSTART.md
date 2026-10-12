# Itinerary quickstart — turn a booked itinerary into a filled budget in about five minutes

This page exists for one reason: the trip guide keeps every amount **blank on purpose** until real numbers arrive. When the itinerary (flights, transfers, event days, reservations, receipts) is handed over, paste it into the planner and let the preview do the sorting. Nothing below invents a price.

**Where:** open [`costs.html#quick-fill`](../costs.html#quick-fill) — “Paste your itinerary, fill your budget”.
**Backup:** the planner saves locally in this browser and also offers “Download JSON backup” / “Restore JSON backup” plus CSV export and a blank CSV template (buttons: Download CSV backup, Download JSON backup, Download blank CSV template, Restore JSON backup). Export before switching devices.

## 1 · What to send (checklist)

| Item | Why it matters | Where it lands |
|---|---|---|
| Flight numbers, dates, times, fares paid | anchors arrival/departure days | `flights`, `airport-transfer-arrival`, `airport-transfer-departure` |
| Hotel confirmation: room rate, nights, taxes/eco-contribution line | separates prepaid stay from on-property charges | `hotel-stay`, `hotel-separate-charges` |
| Transfers actually booked (Airport Direct, taxi, hotel taxi, shuttle) with the quoted price | avoids double-counting bus fares you will not pay | `airport-transfer-arrival` / `airport-transfer-departure`, `taxi-rideshare` |
| Which event days you will attend and how you will travel each day | bus vs taxi vs rental changes the daily number | `event-commute`, `local-bus-and-cards`, `taxi-rideshare`, `event-access` |
| Restaurant bookings or expected meal budgets | the largest discretionary block | `food-and-drink`, `daily-2026-10-DD` |
| Museum/outing tickets, boat trips, arcade or esports bookings | fixed leisure costs | `activities-and-sightseeing`, `gaming-and-arcade` |
| SIM/eSIM plan, roaming add-on, bank/ATM fee schedule | small but real | `mobile-connectivity`, `bank-cash-fees` |
| Tickets, receipts and any refundable deposits/holds | refundable amounts must not inflate totals | manual notes, never auto-filled |

## 2 · Accepted paste format

```
# lines starting with # are ignored
2026-10-13 | flight BOS-MLA return fare | €780.00
14/10 | airport transfer to Qawra | €12.50
15 Oct | dinner in Qawra | €38.00
Oct 16 | museum entry | €10
DAB radio receiver and plug adapter €45
```

- **Amounts must be euros.** With a `|` separator the last field is read as the amount (`€5.00`, `5.00` or `5`); without a separator the line must end with a euro amount (`… €38`). A `$`, `£` or `¥` sign (or USD/GBP/CAD/AUD/CHF/JPY) makes the line *skip* rather than guess a conversion — convert it yourself and re-paste.
- **Ambiguous thousands are rejected** (`1,234` / `1.234`); write `1234.00`.
- **Dates** may be `2026-10-14`, `14/10`, `14 Oct` or `Oct 14` (a wrong year is flagged). A dated line with no recognisable keyword falls into that day’s optional daily row; an undated line with no keyword is skipped with a reason.
- **Deposits, holds and pre-authorisations are never auto-filled** — review them manually and keep refundable holds in the notes field.
- **Existing amounts are never overwritten.** The apply button only writes into blank fields, so re-pasting a longer itinerary cannot destroy earlier entries.

## 3 · Keyword → row map (what the preview recognises)

| Keyword family in your line | Planner row |
|---|---|
| flight, airfare, airline, plane | Flights — all travelers |
| hotel, resort, accommodation, room rate | AX ODYCY — full accommodation booking total |
| hotel tax, tourist/city/eco tax, environmental contribution, resort fee | Hotel taxes, environmental contribution, deposits… |
| insurance | Travel / medical insurance |
| passport, visa, travel authorisation | Passport / entry-document costs |
| transfer to the airport / airport drop-off | Airport → AX ODYCY transfer (departure leg) |
| transfer from the airport / airport pickup | Airport → AX ODYCY transfer (arrival leg) |
| Ta’ Qali / BLAST Arena + bus, taxi, ride | AX ODYCY ↔ BLAST Arena Studios event-day travel |
| taxi, Bolt, eCabs, Uber, ride-hailing | Taxi / ride-hailing |
| bus, Tallinja, travel card, route 186/214, public transport | Local buses / travel cards |
| car hire, rental car, fuel, parking | Optional car hire, fuel, parking… |
| food, meal, dinner, lunch, breakfast, café, coffee, snack, pastizzi | Meals, cafés, snacks, and drinks |
| museum, tour, sightseeing, landmark, aquarium, boat trip, ferry ticket, Comino, Gozo | Landmarks, museums, boat trips… |
| gaming, arcade, VR, esports, LAN, PC café | Gaming centres, arcade, VR… |
| event ticket, CS2, Counter-Strike, Thunderpick, TWC, spectator | Thunderpick event ticket / spectator access |
| SIM, eSIM, data, roaming, top-up | Mobile data, local SIM/eSIM, roaming |
| ATM, card fee, foreign transaction, conversion fee | ATM, foreign-transaction, card… fees |
| DAB/DAB+ radio, radio receiver, FM radio, plug adapter, power adapter | Other incidentals and contingency |
| souvenir, gift, laundry, tips | Other incidentals and contingency |

A line that names only “airport” is deliberately left for you to place (arrival vs departure), and a dated line with no keyword goes to that date’s **optional daily spending** row — the planner warns about double counting if you also budget the same spend in a category row.

## 4 · Five-minute workflow

1. **Paste** the itinerary into `costs.html#quick-fill` and press **Preview matches**.
2. **Read the flags** — “no amount found”, “ambiguous”, “deposit or hold”, “dated outside the 13–19 October trip window”. Fix currency and clarity in the text box, then preview again.
3. **Apply to blank budget fields**, then check the three totals (budgeted, actual, difference).
4. **Fill the gaps by hand** — anything the preview skipped (foreign currency, holds, estimates you add yourself).
5. **Export the backup** (JSON for restore in the planner, CSV for a spreadsheet) and keep the refundable holds in the notes, not in the totals.

## 5 · What the planner deliberately does not do

- It does not fetch live prices for taxis, flights, hotels or tickets. Every number is either yours or a blank cell.
- It does not convert foreign currency and does not treat a deposit as a cost.
- It does not sync between devices; the local save is per-browser, so export before switching.
- It does not decide your itinerary. The bus, event and weather guidance lives on the transport, event and everyday pages, and each of those keeps its own verified/unverified boundary.

*This worksheet describes the planner's behaviour as shipped in `costs.html` on 12 October 2026; the parser's keyword list is visible in the page source for audit.*
