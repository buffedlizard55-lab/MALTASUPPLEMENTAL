# Delivery status — Malta trip guide

**Last updated:** 11 October 2026 (UTC)
**Session branch:** `arena/cc913a9b-maltasupplemental`
**Snapshot boundary:** This is a dated work/status snapshot, not a live GitHub or Pages dashboard. The final delivery response reports only GitHub states checked directly after the branch was pushed.

## Integration state

- Work began from `b307c51` on the fixed Arena branch. PR #42’s event-page work merged to `main` at `5cdea68` and is retained in the current tree.
- Upstream PR #43 (`94733df`) added verified hotel and event material; PR #45 (`dc2fe82`) recorded its observed CI, Pages build and live spot-check. Those changes are retained with the transport and MTA claims requalified where the current evidence does not support a categorical conclusion.
- The latest fetched `origin/main` revision for this reconciliation is `dc2fe82`. It has been integrated locally; the merge conflict resolutions preserve both the upstream additions and the trip-date corrections.
- Delivery PR **#46** was opened from this branch to `main`. This file records the local audit snapshot; use the final response for the observed final PR/check/merge/deployment state.

## Workstream status

| Workstream | Status | Current blockers / next action |
|---|---|---|
| **A · Transport** | Reconciled and evidence-qualified | Both MPT pages show the 17 Oct Route 186 notice at 19:00–00:00; the separate 20:00 notice ends around 21 April. Route 214/TQ1 are candidates, not saved journeys. Confirm the gate/finish and run MPT’s dated planner for all routes and walks. October single fare remains unpublished. |
| **B · Food & cafés** | Sourced shortlist retained; coverage limited | Recheck volatile hours, menus, closures and booking terms. Yelp, Instagram, TikTok, Facebook and X access was blocked or limited; accessible map/review/social views were not comprehensive. |
| **C · Activities, landmarks & events** | Dated options retained; access and volatile details qualified | Reconfirm availability, entry, schedules and provisional social/search-derived items directly with organizers. The Chocolate Festival date was not directly fetched from Facebook; hours/free entry are secondary-source claims. |
| **D · U.S.-traveler guide** | Hotel and practical guidance integrated | Traveler-specific passport, booking, device, insurance, room, meal-plan and invoice details are unknown. EES and MTA short-stay wording remain unresolved source conflicts. |
| **E · Malta sports radio** | Separate radio section implemented | No physical FM/DAB+ reception test, named-match carriage confirmation or stream-access test. DAB+ directory labels/blocks remain scan leads; UK BBC schedules do not establish Malta carriage. |
| **F · Expense planner** | Implemented and validated, blank by default | Await itinerary, booking, party size, actual ticket/transport choices and receipts. Taxi, hotel contribution and all personal costs remain optional/unassumed. |
| **H · CS2 event guide** | Integrated from PR #42 and re-audited | Eventbrite listing identifies venue/date, in-person attendance and 18+. A separate listing-card capture and HLTV report record a free reservation offer, but current extracted text did not expose a fee table. Confirm checkout/inventory, attendee gate, per-day validity and 17–18 Oct agenda. |
| **G · Site integration** | Local validation passed; delivery PR opened | Reconciled latest main, resolved integration conflicts, completed three cumulative audit passes and reran the local browser/accessibility suite. Delivery state is reported separately from this dated snapshot. |

## Current transport reading

- MPT’s Route 186 page and latest-service-updates page both show the 17 October notice as **19:00–00:00**, ending on 18 October at approximately midnight. The distinct older **20:00–00:00** notice ends around 21 April. Do not combine the notices into a 19:00–24:00 union.
- The October notice omits stops Gholja 2 through Targa toward Buġibba, but it gives no replacement path and does not establish the effect on a specific Stadium trip or onward Qawra connection. The “weekly on Friday, Saturday” text does not establish a 16 October diversion or clarify later recurrence.
- One static Route 186 variant lists a 20:53 Stadium departure toward Buġibba; this is not evidence that the entire network stops then. That Route 186 direction does not list an Il-Qawra stop, so a journey using it needs a separately checked onward option. Route 214 lists Qawra 952 and Ta’ Qali Qali 2 2542; TQ1 had no timetable or TWC-specific notice. None is a verified event-day itinerary.
- The interactive MPT planner returned instructions rather than a saved date-specific route. Attendee gate, safe walks, end-to-end return, current taxi quote and late-service availability remain unknown. Taxi/ride-hailing and the hotel’s fixed-charge arrangement are fallbacks, not established necessities.

## Other evidence boundaries

- **Ticketing:** the listing’s extracted text shows 18+ and in-person attendance; it does not prove a current ticket, reservation, checkout total, gate or weekend agenda. The free-offer observation is dated and qualified.
- **Fares:** the operator lists €2.00 winter and €2.50 summer day singles, but the only printed winter validity ended 13 June 2026. Do not assign either amount to 13–19 October.
- **Hotel contribution:** the 2026 guideline PDF gives a per-night rate and cap; the current MTA webpage separately says nights exceeding fifteen are chargeable. The official sources do not expressly reconcile short-stay application. Any six-night €9 calculation is conditional; use the hotel invoice.
- **Radio:** broadcast schedules, over-the-air service directories, reception at AX ODYCY/MFCC, named-match carriage and internet streams are distinct evidence types. No physical scan was possible.
- **Research-platform access:** sampled Google Maps/Reviews, TripAdvisor and Reddit/search material was available; Yelp, Instagram, TikTok, Facebook and X direct access was blocked or limited. Coverage is not a comprehensive ranking.

## Local validation snapshot

- `python3 scripts/validate_site.py` — **PASS**: 7 JSON files / 176 exact-schema records / 307 unique record URLs in `docs/SOURCES.md` / 15 HTML pages / 172 link attributes / 9 shared navigation destinations / 25 expense rows.
- `python3 scripts/check_javascript.py` — **PASS**.
- `node --check js/site.js` — **PASS**.
- `npm test` — **PASS**, 11/11 Playwright tests, including 320/360/768/1440 px layouts, axe, navigation, data rendering and planner behavior.
- `git diff --check` — **PASS** after conflict resolution and final report edits.

## Remaining work for the traveler / next session

1. Confirm the reservation, exact attendee gate, 17–18 October agenda and final 14–16 October finish times with Hotspawn/Thunderpick.
2. With the gate and expected finish, run MPT’s dated planner for each event date in both directions. Compare Route 186, Route 214, other live routes and any TQ service notice; record walking sections and the 17 October diversion effect.
3. Confirm the single fare that applies on 13–19 October; neither seasonal single is assigned as a trip quote.
4. If the planner shows no suitable public return—or if the traveler prefers a car—request a live quote from a provider and AX ODYCY Guest Relations. No taxi is booked or priced here.
5. Ask MPT/AX ODYCY to clarify the MTA short-stay contribution wording and follow a current official Malta source for EES enforcement. Use the hotel invoice for actual charges.
6. Recheck event listings, venue hours, restaurant menus, weather and service notices close to the trip; scan FM/DAB+ locally and ask stations about named-match carriage.
7. Paste the confirmed itinerary into the expense planner, review its preview, and export a CSV backup before switching devices.
