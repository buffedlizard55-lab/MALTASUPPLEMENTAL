# Project plan — Malta trip guide

## Repository review (before workstreams)

The repository is a static HTML/CSS/JavaScript site with a sizeable amount of trip, prize, tax, transport and radio material, but no structured data or central source log. The current overview is for **13–20 October 2026**, describes a different base area, and contains substantial Hotspawn/prize material that is outside this request. The supplied hotel is **AX ODYCY, Qawra**, for **13–19 October 2026**; the venue is given by the requester as **BLAST Arena Studios, Attard**. These inputs must replace—not silently inherit—the prior trip assumptions. Existing live prices, event details, broadcast listings and schedules are time-sensitive and need re-checking. Any claim that cannot be confirmed will be labelled or moved to `docs/OPEN_QUESTIONS.md`.

## Shared setup (serial; done before topic work)

1. Create `data/`, `pages/`, and `docs/` (this plan lives in `docs/`).
2. Use JSON as the structured source of truth. Every place/transport/event/radio entry uses the common fields: `id`, `name`, `category`, `area`, `address`, `hours`, `price_range`, `description`, `source_url`, `source_type` (`official`, `map`, `review`, or `social`), `date_checked`, `confidence` (`verified`, `partially verified`, or `unverified`), and `notes`. Topic-specific facts may be added only where the common fields are retained. Unknown values are explicit (`null` / `"Not published"`), never guessed.
3. Keep the site static and GitHub Pages-compatible. The shared shell is owned by G: global navigation, accessible mobile menu, responsive design tokens/components, overview/executive summary, and common source/status notices.
4. `docs/SOURCES.md` is the master claim-to-URL log, including access date and workstream. `docs/OPEN_QUESTIONS.md` records unresolved facts and access blockers; `docs/STATUS.md` tracks progress and blockers; `docs/HANDOFF.md` is for cross-workstream discoveries.

## Workstreams, ownership, dependencies

| ID | Scope | Owned files (and no others) | Dependencies / gate |
|---|---|---|---|
| A — Transport | Airport-to-hotel and hotel-to-BLAST Studios (Attard) on event days; bus, taxi/ride-hail, rental comparison; practical route limits | `data/transport.json`, `pages/transport.html` | Shared schema; requester-provided hotel and venue details; verify current operator routes/fare pages. |
| B — Food & cafes | Useful, well-supported dining/café options around Qawra/Buġibba/St Paul's Bay and a few accessible island choices; clearly distinguish official information from review/social signals | `data/food.json`, `pages/food.html` | Shared schema; base is Qawra; source-access limitations documented. |
| C — Activities | Gaming centres, activities, landmarks and date-window events suited to a Qawra base | `data/activities.json`, `pages/activities.html` | Shared schema; verify locations, trip-window dates and current operating status. |
| D — Everyday life | US-traveller practical guide: plugs/electricity, connectivity, cash/cards, tipping, safety/health, customs/entry, language and October weather | `data/everyday.json`, `pages/everyday.html` | Shared schema; use government/official sources for legal, safety and technical claims. |
| E — Radio sports | Receivable Malta radio (AM/FM/DAB+ or internet radio) plus only official, published sports schedules that overlap 13–19 Oct; separate confirmed schedules from rights/speculation | `data/radio.json`, `pages/radio.html` | Shared schema; use broadcaster/league schedules and Malta multiplex/station sources; do not infer a Malta feed from another country's rights. |
| F — Expense planner | Itinerary-ready, client-side planner with editable actuals/covered items and clear trip-night/date assumptions | `data/expenses.json`, `pages/expenses.html` | Shared schema; hotel dates (13–19 Oct = 6 nights) and explicit cost inputs; no tax/legal assumptions presented as advice. |
| G — Site shell, executive summary & integration | Home/overview, event/hotel reference pages, global navigation, responsive design, README, master logs, integration and final audits | `index.html`, `pages/event.html`, `pages/hotel.html`, `css/style.css`, `js/site.js`, `README.md`, `docs/SOURCES.md`, `docs/OPEN_QUESTIONS.md`, `docs/HANDOFF.md`, `docs/STATUS.md` | Shared setup first; topic pages/data A–F complete before final integration. G is the only owner of shared files. |

## Conflict and branch protocol

Arena pins this session to `arena/6d51b5f5-maltasupplemental`; creating or switching to per-workstream branches would detach this work from the session. Therefore, keep the mandated branch and apply the same ownership boundaries by completing and validating each workstream in sequence. Do not edit another stream's data/page while working a stream. Cross-topic discoveries go to `docs/HANDOFF.md`; G incorporates them after stream work is complete. Shared files remain untouched until integration, except for this plan and the serial shared setup.

## Work sequence / verification gates

1. Shared schema, directories, shell design tokens, common source-log format (serial).
2. A–F, one owner pair at a time, each checked against the common schema and its source links.
3. G integrates; check data/page consistency, internal links, navigation, keyboard/mobile behavior and GitHub Pages paths.
4. Pass 1: implement all requested sections and first local validation.
5. Pass 2: audit every displayed factual line against a source or explicitly label/remove it; check dates, assumptions, mobile/layout and calculator edge cases; fix findings.
6. Pass 3: re-check the original request requirement-by-requirement, links, data schema, open questions and site build/preview; record remaining limitations and next-session actions.

## Evidence policy

A search result or review aggregate is not a primary source. Live/review platforms are not represented as personally queried when access is blocked. Ratings/review counts are dated, attributed to the platform/aggregator and treated as snapshots, not permanent rankings. Event dates/fixtures, transport schedules/fare, venue status, operating hours, legal rules and radio schedules require current primary or official sources. The hotel/date/venue supplied in the request are treated as user-provided inputs until independently confirmed. Any conflicts stay visible; no gap is filled by a plausible-sounding guess.
