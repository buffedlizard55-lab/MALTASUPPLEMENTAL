# Delivery status — Malta trip guide

**Last updated:** 11 October 2026 (UTC)
**Session branch:** `arena/cc913a9b-maltasupplemental`
**Snapshot boundary:** Dated implementation and audit notes, not a live GitHub or Pages dashboard. The final response will report GitHub outcomes only after direct post-push inspection.

## Integration state

- Work began at `b307c51`. Upstream PR #42 (`5cdea68`), #43 (`94733df`), #45 (`dc2fe82`), #44 (`c7d1d00`) and #47 (`852343f`) are merged to `main` and retained or reconciled in this branch.
- PR #44 was merged 11 October at 16:01:59 UTC as `c7d1d00`. The upstream delivery note records its main CI as successful, Pages as built, and a live-page spot-check. PR #47 later corrected the README's listed browser widths to 320/360/768/1440 px; that documentation correction is retained.
- PR #44's reported 9 October Virtus.pro withdrawal / Ninjas in Pyjamas replacement is preserved in team data and attributed to HLTV and Hotspawn; the organizer's published pages still showed the original field when last checked.
- This session re-audited PR #44's current-facing copy. Ticket-price evidence is now a dated “Free / Reserve a spot” observation, not a current checkout total. Bus evidence is route-specific; a taxi is optional, not a presumed requirement. MPT's 17 October Route 186 notice is 19:00–00:00; the separate older 20:00 notice ends around 21 April. The MTA short-stay wording remains unresolved.
- PR #46 is open from the fixed branch to `main`. GitHub reported the pushed head `9393755` as `CONFLICTING`; `gh pr checks 46` reported no checks. Main then advanced to `852343f` through PR #47. That newest main revision has been reconciled locally and the full suite passes; commit and push the merge, then inspect the current PR head/check/merge state before attempting the requested merge.

## Workstream status

| Workstream | Status | Remaining work |
|---|---|---|
| **A · Transport** | Updated; evidence-qualified | Confirm the attendee gate/finish, run a date-specific MPT journey in both directions, verify stop sides/walks and October fare; compare Route 186, Route 214 and any TQ notice. No saved door-to-door route or taxi quote. |
| **B · Food & cafés** | Source-linked shortlist retained; coverage limited | Refresh volatile hours, menus and closures. Yelp, Instagram, TikTok, Facebook and X access was blocked or limited; accessible review/search samples are not comprehensive. |
| **C · Activities, landmarks & events** | Dated items retained; access qualified | Reconfirm availability, entry, hours and schedules. The Chocolate Festival date is from a dated search-index snapshot of the organizer's Facebook page; hours/free entry are secondary-source claims. |
| **D · U.S.-traveler guide** | Hotel/practical guidance integrated | Traveler-specific booking, room, passport, device, insurance and invoice remain unknown. EES and MTA short-stay source conflicts remain open. |
| **E · Malta sports radio** | Separate radio section implemented | No physical FM/DAB+ scan, local reception test, named-match carriage confirmation or stream-access test. DAB+ directories and UK BBC fixtures are not Malta reception/carriage proof. |
| **F · Expense planner** | Implemented; blank by default | Await itinerary, booking, party size, ticket/transport choice and actuals. Keep the return ride and all personal costs optional/unassumed. |
| **H · CS2 event guide** | Integrated and re-audited | Confirm current checkout/inventory, traveler reservation, attendee gate, per-day validity, finish discrepancy and 17–18 October agenda. |
| **G · Integration** | Three cumulative passes complete; latest-main tests passed | Finish the merge commit/whitespace check, push only the fixed branch, inspect PR checks/mergeability, then merge by explicit PR number if GitHub allows it. |

## Current evidence boundaries

- **Event:** the 11 October Eventbrite extraction showed venue, dates, 18+, in-person attendance and 14–16 October agenda entries; it did not expose a fee table or weekend entries. A separate listing-card capture and HLTV report record a free reservation offer, but do not prove current price, availability, a personal reservation or guaranteed admission.
- **Return transit:** one static Route 186 variant lists a 20:53 Stadium departure toward Buġibba; that Route 186 direction does not list Il-Qawra. It is not proof that 20:53 is the network's last bus, that every return needs another boarding, or that no other bus works. Route 214/TQ1 remain candidates, not dated trips.
- **Fare:** MPT lists €2.00 winter and €2.50 summer day singles; the only dated winter period ended 13 June 2026. The applicable 13–19 October 2026 fare is unpublished.
- **MTA:** the 2026 guideline rate/cap and webpage “15-Night Threshold” language are not expressly reconciled for a short stay. Six-night €9 is conditional arithmetic, not an assumed charge.
- **Radio:** schedules, named-match carriage, terrestrial reception and internet streams are distinct evidence types. No physical scan or local stream-access test was made.
- **Research coverage:** some Google Maps/Reviews, TripAdvisor and Reddit/search views were accessible; direct Yelp, Instagram, TikTok, Facebook and X access was blocked or limited. No universal ranking is claimed.

## Local validation snapshot

After resolving PR #47 and the latest-main conflicts, `npm test` passed: 7 JSON files / 176 exact-schema records / 307 unique record URLs / 15 HTML pages / 175 link attributes / 9 navigation destinations / 25 expense rows; JavaScript syntax checks passed; Playwright passed 11/11 at 320/360/768/1440 px with axe, page/data parity and planner coverage. Run `git diff --check` after staging this final status edit and before the merge commit.

## Next steps

1. Complete the merge of `origin/main` at `852343f` into this branch while keeping the current evidence corrections.
2. Run the full local validation and `git diff --check`, commit the merge, and push only `arena/cc913a9b-maltasupplemental`.
3. Inspect PR #46 head, checks, reviews and mergeability. Merge with the explicit PR number only if GitHub allows it; then check the resulting Pages outcome.
4. For the traveler: confirm the ticket/gate/weekend agenda; run the dated transit planner; confirm fare and any desired ride quote; clarify MTA/EES; refresh volatile details; fill and export the planner after itinerary/actuals arrive.
