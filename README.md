# Malta Field Guide

A clean, mobile-friendly, source-led tourism and recreation guide for the requested Malta trip scenario:

- **Dates:** 13–19 October 2026
- **Base:** AX ODYCY, Deluxe sea-view room, Qawra Coast Road, Qawra SPB 1902
- **Trip topics:** transport (including event-day planning for BLAST Arena Studios / Ta’ Qali), food and cafés, gaming, landmarks and events, U.S.-traveler practicalities, scheduled live sports radio, an editable expense planner, sources, open questions and a final report.

The hotel and trip details above are the user's brief—not proof of a reservation, airfare, coverage or personal itinerary.

## Start here

- [`index.html`](index.html) — executive summary, dated trip overview and guide navigation
- [`pages/transport.html`](pages/transport.html) — airport and Qawra/Ta’ Qali transport notes, live-planner checks and fare caveats
- [`pages/food.html`](pages/food.html) — source-linked food, cafés and review-source limitations
- [`pages/activities.html`](pages/activities.html) — gaming, attractions, landmarks and dated events
- [`pages/radio.html`](pages/radio.html) — official BBC live-sport schedules, Malta-time conversions and reception caveats
- [`pages/everyday.html`](pages/everyday.html) — entry systems, money, phone, power, health, safety and weather
- [`pages/expenses.html`](pages/expenses.html) — browser-only EUR expense worksheet with optional user-entered USD conversion
- [`pages/sources.html`](pages/sources.html) — claim-level source register, unresolved questions, limitations and next steps

## Evidence and limitations

Research snapshots were checked on **9 October 2026**. Schedules, fares, event access, menus, prices, opening hours, border procedures and weather can change; recheck current operator/government pages before relying on them. TWC-specific public spectator access, a confirmed event entrance, exact event-day bus/return journey, and booking/coverage details are unresolved. Unverified details are marked; this guide does not guess them.

The expense worksheet runs in the visitor's browser and does not send or persist entered amounts. Blank costs are shown as unpriced rather than free. It does not invent airfare, hotel, meal, taxi, insurance or foreign-exchange prices.

The requested review platforms were also researched. Direct access was limited or blocked on several services; the exact evidence and limitations are documented in [`docs/SOURCES.md`](docs/SOURCES.md) and on the report page. Lack of access is not treated as proof that reviews or services do not exist.

This is a planning reference, not immigration, legal, tax, medical, insurance or financial advice.

## How the site works

This is a dependency-free static site. Topic data lives in `data/*.json`; each record follows the shared schema documented in [`docs/PLAN.md`](docs/PLAN.md). Topic pages in `pages/` use a small shared renderer in `js/site.js` and the responsive stylesheet in `css/style.css`. The expense calculator is local to its page.

To preview from the repository root, run a static HTTP server (for example `python3 -m http.server 8000 --bind 0.0.0.0`) and open the root page. The JSON renderer requires HTTP(S), not a `file://` URL.

To publish with GitHub Pages, select the `main` branch and repository root (`/`) as the Pages source after the pull request has been merged. The expected project-site URL is `https://buffedlizard55-lab.github.io/MALTASUPPLEMENTAL/`; publication was not assumed by this repository content.

## Updating claims

1. Recheck the primary source and record its URL, access date and scope in `docs/SOURCES.md`.
2. Update the appropriate topic JSON record and its page wording together; use the shared fields and confidence values exactly.
3. Put unresolved details in `docs/OPEN_QUESTIONS.md` and cross-topic dependencies in `docs/HANDOFF.md`.
4. Update `docs/STATUS.md` and repeat the integrated link, mobile, accessibility, data/page and factual review passes.
