# Malta guide — final implementation and evidence report

**Research date:** 11 October 2026 UTC · **session branch:** `arena/dfefc16f-maltasupplemental`.

**Website:** <https://buffedlizard55-lab.github.io/MALTASUPPLEMENTAL/> · **Delivery:** [PR #49](https://github.com/buffedlizard55-lab/MALTASUPPLEMENTAL/pull/49) · **observed gates:** [STATUS.md](STATUS.md).

## Scope and result

The guide is built around the traveler-supplied AX ODYCY base, Qawra Coast Road, Qawra SPB 1902, Deluxe sea-view room and 13–19 October 2026 window, with Thunderpick CS2 attendance at the supplied BLAST Arena Studios/Attard destination. The website does not claim a room/ticket reservation was independently confirmed.

The repo already had a working guide at `b307c51`. This session wrote a short plan before owned work, retained shared setup/schema, performed A–F as isolated sequential file-owned workstreams, then integrated shared files under G. The environment fixes the session to one branch and provides no sub-agent runner: separate workstream branches/agents were **not** used. Read-only research could run concurrently. Cross-topic discoveries were recorded in the handoff, not silently treated as another owner's verified result.

`main` advanced during implementation. The session rebased onto `94733df`, preserving PRs #42/#43's eight-record event extension and hotel/taxi/TQ findings. Conflict resolution was field/content-based, not wholesale replacement. Additional unsupported conclusions brought in by that merge were corrected. A second rebase onto `852343f` preserved the later free-reservation/NIP/official-stream corrections (PRs #45/#44/#47). Their historical delivery receipts remain accessible through the handoff’s Git-history link. Unrelated open PRs were left alone.

### Implemented website

- Nine main navigation destinations: overview, event desk, transport, food, activities, everyday, terrestrial sports radio, expense planner and sources/status.
- Seven canonical datasets, **184 exact 13-field records**: transport 28, food 39, activities 44, everyday 19, radio 21, expenses 25, event 8.
- Six overview cards and six event brief/day cards project canonical records. The inherited detailed event dataset remains available in an expandable, filterable reference. Hotel checklist links preserve the upstream hotel's practical guidance without copying a second set of facts.
- Search/category/area/confidence filters, source/notes disclosures, usable deep links (including collapsed records), keyboard skip/menu/Escape behavior, relative project-prefix URLs, load errors and no-JavaScript onward links.
- Legacy routes remain useful pointers rather than competing stale guides. No external fonts/images or production build/runtime packages are required.
- Responsive layout, readable source cards, explicit unknowns and a simplified executive summary. The wide nav no longer leaves a lone link on a second row; narrower layouts use the menu.

### Expense planner

18 core plus seven optional daily rows; amounts start blank. Budget/actual totals, notes, local autosave, reset confirmation and CSV export/template are retained. Quick-fill previews EUR amounts, rejects obvious foreign/ambiguous input, sums distinct accepted same-category lines, avoids overwriting existing budgets and invalidates an edited preview. Deposits/payment holds are not automatically counted as expenses. Explicit wrong years are flagged.

JSON export and confirmation-gated restore were added: EUR/trip/version checks, known row/field checks, nonnegative amounts up to €1 billion with at most two decimal places, notes up to 240 characters and a 1 MB input limit. Invalid/cancelled imports preserve data. Scientific/leading-decimal inputs export normalized amounts; long leading zeros do not silently truncate the value. Notes remain literal text, not HTML. CSV formula-like prefixes are neutralized. CSV is a spreadsheet/manual format, **not** an automatic restore mechanism.

No account, cloud sync, currency conversion, payment or booking action is performed. This remains a simple keyword-assisted planner needing human review, not an accounting or itinerary-understanding guarantee.

## Verified findings — carefully scoped

These are supported observations of cited sources, **not guarantees of future service, personal access or physical reception**. Full claim/URL/access-date/workstream detail is in [SOURCES.md](SOURCES.md); per-record scope is in [the audit](AUDIT_2026-10-11.md).

### Event and transport

- Eventbrite advertised free in-person ages-18+ reservations for 14–18 October at BLAST Arena Studios Malta, MFCC South Gate National Stadium, Attard. Visible Wed/Thu rows show 09:30 check-in, 10:30 games, 22:30 end; Friday 14:00, 15:00, 21:00. The headline ends at 22:00. Weekend rows and FAQ answers were not visible in the extraction—not proven unpublished. Exact agenda timezone, gate, availability, day validity and the traveler's reservation remain open.
- Organizer phases distinguish the 12–19 October operational window from 14–18 competition. Fresh HLTV/Hotspawn reports say NIP replaces Virtus.pro; older field lists are labelled superseded. Liquipedia bracket sections explicitly label EDT clocks; +6-hour Malta conversion is stated as third-party schedule evidence, not door times or exact finishes. Twitch/Kick/YouTube are internet broadcasts, not radio.
- Route 186's static outward/return stop chains support a bus candidate. One 20:53 return variant is earlier than the visible 14–16 agenda finishes, but no exhaustive/date-specific last-bus search was performed. The return does not itself list Il-Qawra; onward travel and safe walks need checking. No second bus or five taxis are mandatory by inference.
- April 20:00 and October 19:00 diversion notices are separate; the October extraction does not settle year/cause. TQ1 currently exposes no timetable. MPT publishes seasonal/card prices, but its explicit winter range ends before this trip; no date-specific October single fare or automatically best-value card is assigned.
- AX ODYCY's FAQ offers Guest Relations taxi arrangements with fixed charges, not a published quote or guaranteed pickup. Transport Malta's meter-reference page carries a 06/04/2022 footer; hypothetical distance arithmetic is not the measured trip or a separately verified current legal ceiling.

### Food, activities and everyday life

- Fresh operator reads support scoped menu/hours/closure findings including Minoa, Cheeky Monkey, Espresso, Lovage and Luzzu. A closing time is not last food service; a 24/7 snack counter is not proof of a full included dinner. Review snapshots remain dated and sometimes inconsistent; no universal popularity ranking is claimed.
- Gaming directory, arcade/VR and attraction/event references are organized separately. No current public walk-in PC café was confirmed. Optional outings are not a booked itinerary. UNO's fresh listing omits a year; some museum clock charts were not freshly transcribed; conflicted closures and out-of-window events are warnings, not recommendations.
- Primary electrical guidance gives Type G / 230 V / 50 Hz and adapter-versus-converter limits. The hotel's 110 V bathroom outlet is explicitly razor-only; each device still needs a rating check.
- Official EU/US guidance supports general entry/cash/customs/health preparation, not individual clearance. €10,000 is an EU cash declaration threshold, not a legal carrying maximum. EES and ETIAS are distinct; ETIAS was not operational as checked. Personal passport, insurance, medical and phone-plan facts are unknown.
- MTA's primary guest notice and 2026 guidelines support €1.50/night for eligible adults, cap €22.50/visit, from 1 July, disclosed separately. Six qualifying nights would be €9/adult; the invoice is not known. A general webpage anomaly is not treated as a short-stay exemption. The hotel gives discretionary tipping guidance, not a universal national percentage.
- The fresh national forecast panel spans 11–17 October; only 13–17 overlap the trip. Recheck 18–19 and all marine/outdoor conditions.

### Receiver-based sports radio

**No named trip-week match was verified through the complete chain of official commentary schedule → Malta carriage of that feed → compatible receiver → local reception.** This is the central unresolved requirement, not something streams or fixtures can substitute for.

The guide provides FM/DAB+ service leads, compatible-receiver guidance, official programme evidence and scan priorities. BBC Sportsworld's episode JSON yields 15:06 Saturday 17 and 16:06 Sunday 18 October Malta time, each 3h53; no named match/Malta relay feed is established. NET recurring sport-branded programmes, Radio Sportiva's previous-week panel, Rai's incomplete trip-week lineup, Vibe's old-season page and UK BBC match schedules are qualified accordingly.

Sports Channel is listed on 12A by WorldDAB versus 6C/TalkSport by an independent directory. The visible operator directory cannot prove absence because hidden “Load more” entries were not audited. No physical receiver scan was possible. DAB+ Band III support matters; HD Radio alone does not decode it. Kalshi help permits conditional overseas use but personal eligibility/current contracts were not established; no trades or access workaround occurred.

## Unresolved issues and limitations

- No itinerary amounts, flights, party size, booking confirmation, live ticket inventory, exact gate, end-to-end journey, measured walk, car/ride quote, parking check or local RF test.
- Current sampled Yelp, Instagram, TikTok, Facebook, Reddit and X direct reads were blocked; Google Maps/TripAdvisor sampling is limited. Inaccessible review text/sentiment and rankings were not invented. Historical indexed observations do not become fresh full-platform access.
- Not every inherited record or supporting URL was externally rechecked in full. Some sources were partially extracted; dates/notes explicitly distinguish those reads and older evidence. A field edit or passing schema does not recertify external truth.
- External-link liveness was checked only where sources were actually fetched; there is no blanket live-link guarantee. No on-location transit, safety, medical, entry or reception guarantee.
- Browser automation uses Chromium, not a comprehensive browser/device/assistive-technology matrix. Accessibility checks are useful but not certification. Screen captures remain local ignored audit artifacts, not site assets.

## Cumulative passes and observed validation

1. **Implementation and integration:** completed A–F/G, repaired a missing transport anchor, and corrected two test selectors affected by nested disclosures/no-JS extraction. Rebased onto `94733df`, retained upstream additions and passed the full **18-test** suite, schema/link validation and JavaScript syntax checks.
2. **Adversarial review/fix:** corrected unsupported fare/return/absence/year claims and a duplicated stale team field; exercised failed fetches, malformed hashes, blocked storage, CSV safety, JSON restore, grouping and currency inputs. Added deposit/hold, numeric-normalization, padded-number, malformed/oversized/wrong-trip-backup and text-year cases; the final expanded full suite passed **21/21**. Its first run found a numeric reload-format regression (20/21); normal money formatting is now preserved while overlong leading-zero values are normalized.
3. **Original-request audit/fix:** matrix below and reconciled README/source/open-question/status/audit/handoff records drafted. The requirement matrix, current-claim scan, all-upstream-ID and diff checks are complete. After the final rebase onto `852343f`, validators and the full **21/21** browser suite passed again. All three cumulative local implementation/evidence-scope passes are complete, without claiming full external re-certification.

Most recent full structural result: **7 JSON / 184 records / 281 cited URLs covered in the source log / 15 HTML pages / 176 local link attributes / 9 nav destinations / 25 expense rows**. URL coverage is a provenance-presence test, not a link-liveness or factual certificate. The current expanded suite has 21 tests, with passing render/overflow/axe checks at 320, 360, 768, 1024 and 1440 px.

## Original-request matrix

| Requirement | Delivery / remaining boundary |
|---|---|
| Correct hotel, room/stay and CS2 focus | Supplied inputs retained; property/event listing checked. No personal reservation claimed. |
| Airport and especially event-day public transport | Routes/fares/cards/mode comparison and departure checklist; no fabricated gate-to-gate timetable. Dated journeys/walks remain open. |
| Taxi/ride-hailing, rentals and other modes | Provider/hotel/regulator references and whole-cost/convenience trade-offs. Quotes, availability, parking and actual value depend on choices. |
| Food/cafés, gaming, landmarks and dated events | Separate searchable canonical guides; live operational gaps and closures labelled. No invented public PC venue. |
| Google Maps, Yelp, Instagram, TikTok, Facebook, Reddit, X | Attempts/access methods logged; blocked/partial coverage explicitly disclosed. Comprehensive cross-platform popularity remains incomplete. |
| Everyday guide for a US traveler | Power, mobile, money/tipping, safety/health, entry/customs/language/weather covered with source and personal-eligibility caveats. |
| Live over-the-air sports, schedules, Kalshi relevance | Dedicated receiver-based guide and schedules/leads. No confirmed named-match RF reception; eligibility/current contract inventory unverified. |
| Quick-to-populate expense planner | Blank rows, preview, totals/autosave, CSV and validated JSON restore. Needs actual itinerary and review. |
| Simple responsive overview/subpages and official sources | Shared navigation, canonical projections, mobile menu, filtering/disclosures, relative URLs and no-JS/failure fallback. |
| Same record schema, ownership and logs | Exact 13 fields, A–F isolated then G; inherited H preserved. Fixed session branch prevents the requested separate-branch execution; documented rather than simulated. |
| Reverification / three cumulative passes | Observed checks and limitations above. Full external line-by-line recertification of all inherited sources is not complete and is not claimed. |
| PR, merge and Pages verification | [PR #49](https://github.com/buffedlizard55-lab/MALTASUPPLEMENTAL/pull/49) opened; final local checks complete and initial PR CI succeeded. Actual merge/build outcome is recorded in the PR delivery receipt after it occurs, not predicted here. |

## Next session — priority order

1. Supply the itinerary/confirmations and resolve event reservation, gate, ID/day validity, weekend agenda and explicit local-time/end-time conflict.
2. Save actual MPT outward/return journeys; confirm walks, October notice year, current fare/card terms and any TQ announcement. Compare real hotel/app/taxi quotes and parking if relevant.
3. Bring/confirm DAB+ Band III hardware, obtain broadcaster/relay match confirmation and scan at AX ODYCY/event locations. Log what is actually heard. Check Kalshi's current requirements with official support without treating markets as radio evidence.
4. Refresh menus/last orders/inventory, gaming status, closure-conflicted outings and dated events; expand review coverage only where accessible. Recheck 18–19 October and marine forecasts.
5. Check personal documents, medicines/insurance, phone/device compatibility, room/meal plan and invoice. Enter actual EUR costs once, review quick-fill and export a private JSON backup.
6. Continue fresh field-by-field source verification on retained historical records and broader real-device/browser/accessibility testing; do not replace missing evidence with confidence labels.

## GitHub delivery evidence

The delivery branch is `arena/dfefc16f-maltasupplemental` and the PR is #49. The initial PR check run [38155423677](https://github.com/buffedlizard55-lab/MALTASUPPLEMENTAL/actions/runs/38155423677) reported SUCCESS. Pages configuration was read as `main` / root, legacy build. This report is a pre-merge audit snapshot; use [the PR conversation and checks](https://github.com/buffedlizard55-lab/MALTASUPPLEMENTAL/pull/49) for the observed numbered merge, resulting main validation/Pages commit and deployed-page spot-check receipt. A prior successful Pages build does not establish that this PR is live.
