# MALTASUPPLEMENTAL

Travel companion for the **Thunderpick World Championship 2026** trip to Malta, **13–19 October 2026**
(6 nights, 7 days), for a US (California) resident departing **SFO**, staying at **AX ODYCY, Qawra**
(Deluxe sea view) — match days **14–18 Oct** at **BLAST Arena Studios, Attard** (Ta' Qali).

This site was built as a **supplement** to the main legal/risk dossier at
`buffedlizard55-lab.github.io/MALTA` — it covers what that
dossier deliberately did not: the itinerary, food, landmarks, activities, getting around (incl. the
event-day hotel→venue plan), radio & sports broadcasts, prize-specific costs, entry/address answers,
and a full audit of the Hotspawn prize.

> **24 Sep 2026:** the MALTA dossier **no longer resolves** — the GitHub repo is not found via the API and the
> Pages site 404s (as does the URL that was supplied as this project's starting point). All cross-links to it have
> been removed; its key conclusions (cost cross-check, due-diligence verdict) are preserved on this site, which is
> now the surviving public record. The privacy exposure that dossier carried (see below) is closed unless the repo
> reappears.

> **9 Oct 2026 (T−4 days):** trip parameters confirmed — **AX ODYCY, Qawra (Deluxe sea view), 13–19 Oct 2026** —
> and the site re-focused on trip planning around the hotel: new **Itinerary** and **Your Base** pages, the
> event-day public-transport plan (Route 186/214), near-hotel food/activities/events research, SIM/eSIM and
> customs sections, a data-driven expense planner, and a data/docs layer (`data/`, `docs/`, `scripts/`).
> Load-bearing sources re-read 9 Oct 2026; GitHub Pages remains enabled (serving `main` from root).

> **Re-based 9 Oct 2026 (parallel Qawra re-base session, merged via PRs #8/#9).** The hotel is
> confirmed: **AX Odycy, Qawra Coast Road, Qawra SPB 1902**, Deluxe sea view, **13–19 October 2026
> (6 nights, 7 days)**. Qawra is on the north-east coast, not the Sliema/St Julian's belt the earlier
> pages assumed, and that changed the transport answer: **bus route 186 runs from the seafront outside
> the hotel straight to the tournament venue at Ta' Qali, every 30 minutes, with no change of bus**
> (stops Arznell 950 / Qawra 952 on the hotel's coast road; outbound 06:08–21:37). See
> [Hotel & Base](hotel.html) and the [event-day transport section](getting-around.html#eventdays).
>
> **Two parallel sessions, one repo (9 Oct 2026).** The Qawra re-base (PRs #8/#9) and this branch's
> trip-planning pass (PR #11) were developed in parallel and merged: this branch was rebased onto
> `main` first and every conflict resolved by keeping the union of both (resolution table in
> `docs/STATUS.md`). Both sessions' pages, data files, docs and verification scripts are in the tree.

## Pages

| Page | Contents |
|---|---|
| [Overview](https://buffedlizard55-lab.github.io/MALTASUPPLEMENTAL/) | Executive summary: the confirmed trip, the five things to lock down first, what's here, top sources |
| [Hotel & Base](hotel.html) | AX Odycy, Qawra: the booking, the four bus stops on the coast road, route 186 to the venue with times, the eleven on-site outlets, verifiable day trips (re-base session) |
| [Itinerary](itinerary.html) | Day-by-day 13–19 Oct skeleton: fixed points (event/radio/ferry), transport legs, day-budget quick reference, pre-departure checklist |
| [Your Base](qawra.html) | Qawra/Buġibba/St Paul's Bay neighbourhood: the hotel (verified), eating, cafés, beaches, aquarium, events, transport from your front door |
| [The Event](event.html) | TWC 2026 Finals: dates, venue (BLAST Arena Studios, Attard), teams, format, streams, ticket notes |
| [Food & Drink](restaurants.html) | Near-hotel picks (Qawra/Buġibba/St Paul's Bay), island-wide top restaurants, Maltese classics, cafés, $30/day verification |
| [Landmarks & Sights](landmarks.html) | 7-day visit plan, near-hotel sights (aquarium etc.), temples, Valletta, Gozo/Comino — official prices |
| [Activities & Gaming](activities.html) | In-window events (incl. CDM Sundays Sun 18 Oct, free), aquarium, gaming/PC venues, day-out activities |
| [Getting Around](getting-around.html) | Event-day hotel→venue plan (Route 186/214), airport↔Qawra, 7 modes scored on convenience/price/value/feasibility |
| [Everyday Life](everyday.html) | Plugs (Type G 230 V), SIM/eSIM bands, customs allowances, 112, language, money/VAT/tipping, water, health, US-citizen packing checklist |
| [Radio & Sports Bets](radio.html) | DAB+/FM/AM guide, verified dated slots (BBC Sportsworld Sat 17/Sun 18), in-window match schedule, Kalshi availability, pre-departure checklist |
| [Costs & Budget](costs.html) | What the prize covers/excludes, 6-night cost model, tax, scenarios, calculator, data-driven expense planner |
| [Entry & Address](logistics.html) | Entry requirements, EES/ETIAS, passport, the address question answered |
| [Hotspawn & Prize](hotspawn.html) | Who Hotspawn/Sophie McCarthy are, T&C audit, 10 flagged irregularities, written-confirmations checklist |
| [All Sources](sources.html) | Every URL used, tagged Official / Verified / Estimate / Flag |
| [Summary stubs](pages/transport.html) | `pages/*.html` — short summary sub-site (transport, food, activities, everyday, radio, expenses) that defers to the main site where they disagree (re-base session) |

## Data & docs layer (single source of truth)

| Path | Purpose |
|---|---|
| `data/schema.md` | Common item schema (id, name, category, area, address, hours, price_range, description, source_url, source_type, date_checked, confidence, notes) |
| `data/trip.json` | Trip parameters (hotel, dates, event) — the shared file every page reads (re-base session) |
| `data/venues.json` | Venue dataset mirrored by hotel.html: on-site + nearby food, activities, landmarks (re-base session) |
| `data/transport.json` | Transport items (routes, passes, taxis, rideshare, ferries) — mirrors Getting Around |
| `data/food.json` | Food & café items (incl. near-hotel) — mirrors Food & Drink |
| `data/activities.json` | Activities, landmarks, gaming venues, events — mirrors Activities / Landmarks / Your Base |
| `data/everyday.json` | Plugs, numbers, money, SIM/eSIM, customs, weather — mirrors Everyday Life / Entry |
| `data/radio.json` | Stations, ensembles, schedules, Kalshi note — mirrors Radio |
| `data/expenses.json` | Expense planner lines (estimates + empty `actual` fields) — mirrors Costs & Budget § 5b |
| `docs/PLAN.md` | The work plan (workstreams, owned files, dependencies, verification gates) |
| `docs/SOURCES.md` | Master source log (claim · URL · date · workstream · status) — accumulates every new source |
| `docs/OPEN_QUESTIONS.md` | Unverified/unresolved register — gaps are never filled with guesses |
| `docs/STATUS.md` | Workstream status, blockers, pass log |
| `docs/HANDOFF.md` | Cross-workstream notes (merged from both sessions) |
| `docs/SCHEMA.md` | Data-item schema quick reference (re-base session; `guide` added to source_type) |
| `docs/FINAL_REPORT.md` | Re-base session's final report incl. the X3-withdrawn correction note |
| `scripts/verify_site.py` | Integration gate: JSON validity + schema, data↔page consistency, internal links/anchors, HTML tag balance, source-log coverage |
| `scripts/check_links.py` | Integration gate (re-base session): internal links incl. pages/ stubs, navigation consistency, data schema, load-bearing page assertions, forbidden patterns |

## Privacy

The private email correspondence between the winner and Hotspawn is **strictly internal**. No email
content is quoted, reproduced or summarised verbatim anywhere in this repository — only the context needed
to answer the research questions (what was asked, what decisions hang on it) appears on-site. On 24 Sep 2026
the site was scrubbed further: the owner's handle, leaderboard position and first name were removed, the draft
reply was replaced by a neutral confirmations checklist, and no winner handles (own or third-party) appear
anywhere. If you contribute: never commit email text, names, handles or addresses.

**Open exposure outside this repo — closed 24 Sep 2026:** the main MALTA dossier previously used the winner's
first name and quoted a short phrase from the correspondence on its public pages. On 24 Sep 2026 that
repository stopped resolving (not found via the GitHub API; Pages 404) — whether it was deleted, renamed or
made private is unknown from here, but the exposure is closed while it stays down. If it ever comes back,
scrub it first.

## Project structure

```
*.html              the site (flat, published as GitHub Pages) — 15 root pages
pages/*.html        summary stub sub-site (re-base session; defers to the main site)
css/ js/            design tokens and the nav toggle + budget calculator
data/               single source of truth — pages must match these files
  trip.json         hotel, dates, event (the parameters every page reads)
  transport.json    every route, fare and mode, with its source
  food.json         near-hotel + island restaurants & cafés (mirrors restaurants.html)
  activities.json   activities, landmarks, gaming venues, events (mirrors activities/landmarks/qawra)
  everyday.json     plugs, numbers, money, SIM/eSIM, customs, weather
  radio.json        stations, ensembles, schedules, Kalshi note
  expenses.json     expense-planner lines (estimates + empty actual fields)
  venues.json       venue dataset mirrored by hotel.html (re-base session)
  schema.md         the common item schema (+ expense extension fields)
docs/               PLAN.md SOURCES.md OPEN_QUESTIONS.md STATUS.md HANDOFF.md SCHEMA.md FINAL_REPORT.md
scripts/
  check_links.py    integration gate (re-base session) — run before every merge
  verify_site.py    integration gate (this branch) — run before every merge
```

Both gates must pass before merging. Serve locally with any static server, e.g.
`python3 -m http.server 8080`.

## Known open items (all flagged on-page; full register in `docs/OPEN_QUESTIONS.md`)

- **Do not book anything** until the prize's cash-alternative / written coverage is confirmed (see
  [Costs](costs.html) and the confirmations checklist in [Hotspawn](hotspawn.html)).
- The T&C residency clause conflicts with the winner's US residence — resolve before ID submission.
  (The full T&Cs were read live on 23 Sep 2026, went down on the morning of 24 Sep, and were **back up later
  on 24 Sep when they were re-read verbatim a second time — identical**. Availability is intermittent and there is
  no Wayback capture: **screenshot both sub-pages now** and still request a PDF.)
- **TWC match-day session/door times are still unpublished** (format page re-read 9 Oct 2026 — "stay tuned");
  the Itinerary skeleton carries the blanks.
- BirguFest 2026 dates are unresolved across four sources; the 2026/27 winter bus-fare switchover
  (summer €2.50 through 18 Oct, winter €2.00 from 19 Oct per 2026 guides — confirm on the operator page);
  the 7-day card's Airport Direct coverage is self-contradictory across three statements on the operator's
  own pages (two say included, one says excluded — flagged 2-vs-1); the talkSPORT/"Sports Channel"
  identification rests on three directory sources vs. the operator's absent catalogue entry.
- US cars have HD Radio, not DAB+ — bring a DAB+ radio or buy one locally. The one *verified, dated*
  English-language Premier League radio slot is BBC World Service **Sportsworld** (DAB+ 6A), Sat 17 Oct
  15:06 and Sun 18 Oct 16:06 Malta time (BBC page re-read 9 Oct 2026 — still listed); talkSPORT on 6C is
  probable, not confirmed.
- Unpriced on purpose (no operator page found): Comino boats, Saluting Battery, Gamers Lounge session
  rates, Mosta Rotunda admission, boat trips from Buġibba/Qawra (marketplace prices only).
  **Resolved 24 Sep evening:** Blue Grotto boats (€10/€5 per 2026 guides, older €8/€4 shown as
  conflict), Fort St Angelo €10, Inquisitor's Palace €6, Ġgantija €10 (combo), Skorba & Ta' Ħaġrat combo €6.
  **Resolved 9 Oct 2026:** Heritage Malta Multisite Pass exact prices (adult €60.00 / child €30 / student €45 /
  senior €45, includes the Malta National Aquarium) and the aquarium's own prices (adult €17.90 door /
  €16.90 online, daily 10:00–20:00) — both from the official tickets page.
- Login-walled platforms (Google Maps, Yelp, Instagram, TikTok, Facebook, X) could not be queried
  directly; their signal enters only via named aggregators — see the not-found register on
  [Sources](sources.html).
- Hotspawn's dedicated /author/ page for Sophie McCarthy 404s after a site restructure; her role is
  verified via article bylines instead (bylines still active 24 Sep 2026). The Gamers Lounge site was
  back up on 24 Sep (retail-forward; no session prices published).

## Next-session work queue

1. **When the confirmed itinerary/fight & hotel numbers land:** fill the Actual column in the
   [expense planner](costs.html#planner) (2 minutes) and lock the budget.
2. Collect the five written confirmations listed on [Hotspawn & Prize](hotspawn.html) (if the prize
   framing still applies to this trip).
3. T-1 week (from 12 Oct): re-check the TWC match schedule (format page), EPL MW7 TV moves, ETIAS
   status, the 19 Oct winter-fare switchover, passport validity, BBC Sportsworld's commentary pick, the
   Middle Sea Race start hour, Gozo Highspeed's restricted 14/17 Oct timetable, and DAB+ 6A/6C carriage
   on arrival. Confirm the exact tallinja stop for the hotel + first/last 186 departures in the app.
4. Kalshi: resolved on the Radio page (official help article + Member Agreement v9.20.2026 — Malta not
   restricted; Italy, France, UK, Ireland, Switzerland, Belgium, Portugal, Poland, Hungary are, so no
   trading during such layovers; Germany/Netherlands/Denmark/Austria are not listed). Screenshot both
   before flying — Kalshi may amend the list unilaterally.
5. BirguFest dates: ask the Birgu Local Council directly once published (birgu-fest.com did not help).
6. Screenshot/save the giveaway page and Terms now (back online since later on 24 Sep, but intermittent), and
   request a PDF of the giveaway T&Cs — no archive copy exists if they vanish again.
7. Book the Hypogeum (€35, 10 per tour) now if wanted — the only sight with a hard booking constraint.
8. Next research session: price Comino boats, the Saluting Battery and the Buġibba/Qawra boat trips from
   operators (the remaining unpriced items); re-sample SFO–MLA fares once the routing is named; re-open
   cfr.gov.mt's VAT page and the State Department fee page (both errored on 24 Sep); confirm public
   holidays & shop hours from a Maltese government page; re-confirm the EES "fully operational from
   10 Apr 2026" date; ask the MALTA-dossier owner to scrub the name/quote.
   **Done in the 24 Sep evening pass:** the Village Fork (Birkirkara), Caviar & Bull (Corinthia Hotel,
   St George's Bay), Country Terrace (Triq iż-Żewwieqa, Mġarr/Għajnsielem, Gozo) and Ta' Tona (Triq
   ir-Rebħa, Mġarr, Gozo) localities; drinking age 17 (secondary sources); Ta' Qali corridor routes
   (52 / 56 / 58 / 186 per third-party guides — slight disagreement kept flagged; confirm in the tallinja
   app with the hotel address); plus the pricing items above.
   **Done in the 9 Oct 2026 pass:** hotel verified (AX ODYCY official site + aggregators); event-day
   transport plan (Route 186/214, TD1/TD5/X3/X1, airport taxi/rideshare bands, Buġibba hub, night buses,
   TQ shuttle precedent); near-hotel food (16 restaurants + 7 cafés, TripAdvisor Oct-2026 lists);
   aquarium + Multisite Pass official prices; CDM Sundays 18 Oct (free) verified on the venue's event site;
   SIM/eSIM 2026 bands; official customs allowances; radio re-verified (BBC Sportsworld, PL MW7, DAB+
   catalogues, station directory); expense planner data file; docs/ + data/ + scripts/ layer.

## Limitations (pass 3 audit, 23 Sep 2026; re-audited 24 Sep 2026)

- The build sandbox has no outbound shell network, so **links were not machine-checked from the shell**;
  every URL was opened via the research fetch tool instead — and in the second verification pass the
  load-bearing sources (giveaway Terms, league fixtures, fares pages, CFR sections, MTA guidelines) were
  re-fetched and re-read directly. A future session with network should still run a bulk link checker.
- Community-platform URLs are flaky (community.hotspawn.com: outage morning of 23 Sep, up later that day,
  sub-pages down on the morning of 24 Sep, **back up later on 24 Sep** — intermittent). Corroborated by other
  sources, flagged on-page, and now covered by a "screenshot both pages" instruction.
- The 23 Sep build contained eleven factual errors that the 24 Sep pass withdrew (see the corrections
  log). All were unsourced or single-source guidebook lines. Claims still badged only "Verified
  23 Sep 2026" have been read once, not twice.
- "Sports Channel" on DAB+ 6C = talkSPORT rests on three independent directories/listening reports
  (radioinmalta, RadioBlog.eu, Wikipedia); the multiplex operator's own catalogue does not list it.
  Treat as probable until tuned in.
- Rai Radio 1's per-match commentary assignments, talkSPORT's Malta feed for 17–19 Oct and BBC
  Sportsworld's commentary pick are not published in advance; the Serie A / EPL / UCL / UEL tables show
  official kick-offs, not verified radio line-ups. Only two of the three Saturday-15:00 EPL games
  receive UK radio commentary at all. UCL/UEL/NFL carriage in Malta is unverified.
- Restaurant ratings/review counts are point-in-time TripAdvisor data; social platforms were not
  directly queryable.
- Cost bands are estimates, not quotes; a parallel independent estimate (MALTA dossier) is shown on the
  Costs page for reconciliation.
- Nothing here is legal or tax advice.

## Corrections log

- **9 Oct 2026 fifth pass (trip re-focus; PR for branch `arena/8ed16394-maltasupplemental`):**
  - *Trip parameters updated site-wide:* confirmed **AX ODYCY, Qawra (Deluxe sea view), 13–19 Oct 2026 (6 nights)**
    replaces the earlier Sliema-base / 13–20 Oct (7-night, prize-Terms) framing. Cost model recomputed
    (food 7 days; eco-tax €9.00; bands $370–866 out-of-pocket / $790–1,646 incl. est. tax — arithmetic
    re-verified line by line in Pass 2); calculator defaults updated (nights 6, eco $11, activities $90).
  - *New pages:* `itinerary.html` (day-by-day skeleton + fixed points + day-budget quick reference +
    pre-departure checklist) and `qawra.html` (Your Base: hotel verified, neighbourhood food/activities/events,
    transport from the front door). Navigation updated on all 14 pages.
  - *Transport (§ 0 on Getting Around):* event-day plan — Route 186 (Buġibba–Qawra–Mosta–Ta' Qali–Rabat,
    ~every 30 min, ~25–30 min) outbound; 186-toward-Buġibba or Route 214 (passes Qawra) return; airport↔Qawra
    options (TD1 €3.50 hourly; TD5 €3.00 limited midday; 214 €2.50/€2.00; X3/X1 standard fare; white-taxi kiosk
    ~€25–28; rideshare ≈ €15–30); Buġibba bus station hub + card sales office; N1/N11 night buses; TQ event-shuttle
    precedent (none announced for TWC as of 9 Oct). Stop-level times remain app-confirmed (operator page is
    JS-driven) — flagged, not guessed.
  - *Food (§ 0 on Food & Drink):* near-hotel section — 16 restaurants + 7 cafés + budget strip, from TripAdvisor
    ranked lists (updated 2025–Oct 2026, read 9 Oct) cross-checked with the island's Definitive(ly) Good Guide
    2026; hotel on-site dining (11 outlets; Minoa = #9 island-wide).
  - *Activities/Landmarks:* window re-titled 13–19 Oct; CDM Sundays (Sun 18 Oct, FREE, Café del Mar Qawra)
    added; BLAST SLAM VIII (8–11 Oct) and Malta Comic Con (10–11 Oct) added to the just-before list; aquarium
    priced officially (adult €17.90 door / €16.90 online; daily 10:00–20:00); Multisite Pass exact prices
    (adult €60 — resolves the 24 Sep flag); 7-day sight plan rebuilt for the Qawra base; near-hotel sights added.
  - *Everyday:* SIM/eSIM 2026 bands (§ 3b) and official customs allowances (§ 3c, Malta Airport verbatim);
    packing checklist updated; SIM budget line aligned to the new bands.
  - *Radio:* window 13–19 Oct; Mon 19 Oct flagged as departure day; BBC Sportsworld re-read (Sat 17/Sun 18
    confirmed, third read); EPL MW7 re-verified against the official PL releases; DAB+ operator catalogue and
    station directory re-read (talkSPORT identification still probable); pre-departure checklist re-dated T−4.
  - *Expenses:* data-driven planner (`data/expenses.json` + costs.html § 5b) with an Actual column per line —
    fills in 2 minutes when the itinerary arrives.
  - *Data/docs layer added:* `data/*.json` (6 topic files, schema in `data/schema.md`), `docs/` (PLAN,
    SOURCES, OPEN_QUESTIONS, STATUS, HANDOFF), `scripts/verify_site.py` (integration gate).
  - *Verification:* `python3 scripts/verify_site.py` green (JSON validity + schema, data↔page consistency,
    internal links/anchors, HTML tag balance, source-log coverage); `node --check js/site.js` OK; all 14 pages
    served locally HTTP 200. Load-bearing external sources re-read via the research tool (the shell has no
    general outbound network).
- **24 Sep 2026 fourth pass (evening session):** full mechanical audit (all 12 pages served locally
  HTTP 200; zero missing internal links; HTML tag-balance clean; `node --check js/site.js` OK; CSS braces
  101/101; calculator arithmetic script-verified against the published $587 / $2,100 / $567 / $1,154 figures).
  Load-bearing sources re-read a third time the same day: TWC format page (unchanged), ETIAS ("not in
  operation"), State Dept Malta advisory (Level 1, 9 Jul 2026), MP Transport fares page (winter window and the
  Airport-Direct self-contradiction unchanged), Valletta Ferry Services (**back on the normal summer schedule —
  the 23–24 Sep swell suspensions had ended**), MTA eco-contribution page, BBC Sportsworld schedule (both
  in-window episodes still listed; UTC−4 rendering 09:06/10:06 ⇒ same 13:06/14:06 GMT), Kalshi help article,
  premierleague.com Oct/Nov amendments page (MW7 table matches exactly, incl. the UEL footnote), the giveaway
  page (live again, "100 entries").
  - *Gap-fills:* priced Fort St Angelo (€10), Inquisitor's Palace (€6), Ġgantija (€10 combo) and the Multisite
    Pass (€30–€60 by type) from the official Heritage Malta pages/store, plus Skorba & Ta' Ħaġrat combo (€6);
    Blue Grotto boats (€10/€5 from two 2026 guides; €8/€4 conflict shown); Village Fork = Birkirkara, Caviar &
    Bull = Corinthia St George's Bay, Country Terrace = Mġarr/Għajnsielem Gozo, Ta' Tona = Mġarr Gozo; Esports
    Plaza corroborated via Instagram; Gamers Lounge FAQ page live; drinking age 17 now secondary-sourced
    (tripbase 2026, WorldAtlas — no Maltese gov page); Ta' Qali corridor bus numbers (52 / 56 / 58 / 186)
    added from third-party guides with the guide-vs-guide disagreement kept flagged.
  - *New content:* Food page gains a community-pulse section (four Reddit threads tabulated with caveats) and
    three cafés (Lot Sixty One, UC Cafè, Piadina Caffe) from TripAdvisor's café lists.
  - *Method note:* the Costs hero "EUR/USD ≈ 1.14" and the calculator/sources "1.145" are the same rounded
    rate — documented on Sources, not an error.
- **24 Sep 2026 third pass (evening session, PR #6):** full site re-opened end-to-end; load-bearing sources
  re-fetched and re-read (Terms verbatim 2nd read; giveaway page; TWC format page; 16 Sep PR; BLAST fan guide;
  premierleague.com October/November amendments — every MW7 fixture confirmed; Malta FA ticketing — Gżira Utd v
  Mosta 14 Oct 19:00 confirmed; BBC Sportsworld schedule; Radio In Malta directory — ONE Radio 92.7 confirmed;
  publictransport.com.mt fares; Valletta Ferry — incl. live "Sliema service suspended for swell" banner; MTA
  eco-contribution; St John's; Hypogeum €35/€50 mechanics; State Dept Malta advisory in full — emergency numbers
  verbatim; ETIAS "not in operation"; Kalshi help article; MCA consumer tools).
  - *Dead links:* the MALTA main dossier repo/site no longer resolves (API + Pages both 404) — all cross-links
    removed site-wide; its archived figures kept as labelled references.
  - *Correction:* Entry page EES note "your first entry is Malta" fixed — with no nonstop SFO→MLA, EES
    registration happens at the first Schengen-entry airport (the connecting hub; Malta only via a non-Schengen
    connection such as Dublin).
  - *Downgrades/notes:* Falcons "Cologne Major winners" note downgraded to secondary-sourced; BBC Sportsworld
    times annotated (page renders viewer-local; both renderings resolve to 13:06/14:06 GMT = 15:06/16:06 CEST);
    Everyday page gained the State Department's 1777 gambling-support and 1772 loneliness numbers.
  - *Intermittencia watchlist:* community.hotspawn.com sub-pages (up/down same day); gozohighspeed.com fares
    sub-page (HTTP 502 in this pass; fares carried from the earlier same-day verification).

- **24 Sep 2026 re-verification (morning session, PR #5):**
  - *Privacy:* handle/leaderboard position/first name removed from index, hotspawn, sources and README;
    draft email replaced by a generic confirmations checklist; "Sophie" → "Hotspawn" in on-page wording.
  - *Landmarks (page rewritten):* "Skara Baħri" temple (does not exist) → Skorba; a Caravaggio "in
    Mdina" withdrawn (both are in St John's Oratory); Fort St Elmo "National Archives" → National War
    Museum; Malta Maritime Museum marked temporarily closed (Heritage Malta); "Cristal Lagoon" → Blue
    Lagoon; official prices added (St John's €15, Hypogeum €35, Ħaġar Qim & Mnajdra €10, Fort St Elmo
    €10, Grand Master's Palace €12, Tarxien €6, St Paul's Catacombs €6); St John's closed Sundays and
    opens 11:00 on Thu 15 Oct.
  - *Activities (page rewritten):* Rolex Middle Sea Race moved from "early November" to **Sat 17 Oct
    2026** (RMYC); MPL Gżira Utd v Mosta 14 Oct 19:00 added (MFA ticketing); Gamers Lounge site back up.
  - *Food:* Is-Serkin located in Rabat (not Valletta); dish descriptions corrected; localities added to
    the Top-10; special-awards table added from the 2026 ceremony page.
  - *Getting around:* "Vaporetto ~€1–2" → Valletta Ferry Services €3.00 single / €5.00 day (€3.50/€5.20
    after 19:30); Gozo Channel €4.65; Gozo Highspeed €7.50 each way (no return fare published; restricted
    schedule 14 & 17 Oct); State Department licensed-taxi advice added.
  - *Everyday:* 196 removed from the emergency list (not on the State Department page); VAT rates
    corrected to 18/12/7/5% (PwC; cfr.gov.mt page errored); US-visitor bullets (cannabis/CBD illegal,
    €10k cash declaration, drone registration, Amex acceptance) added from the State Department.
  - *Radio:* Rai Radio 1 "1062 kHz AM" withdrawn (Rai closed MW on 11 Sep 2022 — AM in Malta = Radju
    Malta 999 kHz only); BBC World Service row corrected to the dated Sportsworld slots (now the lead
    EPL option); UCL MD2 / UEL MD2 official lists and Rai Radio 1 weekend pattern added; Kalshi
    restricted list expanded from the full §VI (55 jurisdictions).
  - *Costs:* new §2b unexpected-costs table; passport renewal $130 + $60 expedite + $22.05 delivery
    (State Dept fee URL 404 — flagged, cross-checked against a 2026 acceptance-facility table);
    calculator now keeps per-element FMV and always adds the tax line.
  - *Entry & Address:* 19 CFR 122.49a(b)(3)(xii) quoted verbatim (US address not required for US
    citizens); EES wording aligned to the live EU page (operational; "fully operational 10 Apr 2026" left
    as a flagged 23 Sep reading).

- Pass 2/3: Radio Sportiva relabelled (private Mediahit station, not Rai); TWC group-stage advancement
  corrected to top-two-per-group; Prosciutteria area corrected to Gżira; full Serie A MD7 table added
  from the official Lega notice; talkSPORT/BBC slot mapping added from premierleague.com.
- Second verification pass (23 Sep 2026, this session): re-verified every load-bearing claim against the
  live primary sources; giveaway T&Cs re-read in full and confirmed verbatim (incl. the duplicated
  section "4" and the orphaned heading); eco-tax band corrected ($26 high → $12 max, since 7 nights ×
  €1.50 can't reach the €22.50 visit cap — subtotals/totals updated to $415–$867 / $835–$1,647);
  passport claim corrected (the Borders Code sets no blank-page minimum — 3-month validity + issued
  within 10 years are the actual Art. 6(1) conditions); EPL audio note refined (two of three Saturday
  15:00 games get BBC audio, the third gets none); talkSPORT-on-6C identification upgraded to three
  independent corroborations; Kalshi help-article link updated to the canonical URL; Malta NT fixture
  dates (1 & 4 Oct, Ta' Qali) verified and cited; Sophie McCarthy citations switched from the 404'd
  author page to live article bylines; TD5 route, Explore Flex Airport-Direct add-on (€6), and the Ryde
  ride-hailing app added; Gamers Lounge reachability flagged with Facebook corroboration.

## Building

Static HTML/CSS/JS, no dependencies. Serve locally with any static server, e.g.:

```bash
python3 -m http.server 8080
# → http://localhost:8080
```

## Method

Every claim carries a source link; every source is tagged by trust level in
[All Sources](sources.html). Conflicting sources are shown, not averaged. Anything that could not be
verified (login-walled social platforms, unpublished schedules, a contradictory operator catalogue) is
explicitly recorded as not found rather than filled in.
