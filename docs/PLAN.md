# Workstream Plan

## Constraints
**Note:** As an Arena agent, I am restricted to working solely on the `arena/c4fd385c-maltasupplemental` branch. I cannot create or switch to separate Git branches (like `work/transport`). Therefore, the parallel workstreams will be executed serially on this branch, strictly adhering to the file-ownership rules described below to avoid conflicts and maintain the verifiable structure.

## Dependencies & Shared Setup
1. **Shared Setup (Completed First)**:
   - Folder structure: `docs/`, `data/`, `pages/`, `css/`, `js/`
   - Data schema defined for `data/*.json` files.
   - Initial site shell and navigation structure in `pages/` and `index.html`.
   - Logging files: `docs/SOURCES.md`, `docs/OPEN_QUESTIONS.md`, `docs/STATUS.md`.

## Workstreams and Owned Files

### A. Transport
- **Scope:** Airport, hotel to BLAST Arena Studios (Attard) on event days, buses, taxis/ride share, rentals, cost and feasibility comparison.
- **Owned Files:** `data/transport.json`, `pages/transport.html`
- **Dependencies:** Hotel info (AX ODYCY Malta), Event info (BLAST Arena Studios).

### B. Food and Cafes
- **Scope:** Restaurants, cafes, places to eat near the hotel and in Malta.
- **Owned Files:** `data/food.json`, `pages/food.html`
- **Dependencies:** Hotel location.

### C. Gaming Centers, Activities, Landmarks, Events
- **Scope:** Gaming centers, landmarks, activities, events near hotel and around Malta.
- **Owned Files:** `data/activities.json`, `pages/activities.html`
- **Dependencies:** Event dates (Oct 13-19, 2026), Hotel location.

### D. Everyday Life (US Traveler)
- **Scope:** Plugs/voltage, SIM/eSIM, money/tipping, safety, health, customs, language, weather.
- **Owned Files:** `data/everyday.json`, `pages/everyday.html`
- **Dependencies:** None.

### E. Radio Sports Broadcasts
- **Scope:** Malta stations, frequencies (FM/DAB+), official schedules, trip-date listings (especially EPL, Kalshi markets).
- **Owned Files:** `data/radio.json`, `pages/radio.html`
- **Dependencies:** Event dates (Oct 13-19, 2026).

### F. Expense Planner
- **Scope:** Data-driven template that is quick to fill once the itinerary arrives.
- **Owned Files:** `data/expenses.json`, `pages/expenses.html`
- **Dependencies:** Data from Transport, Food, Activities for base estimates.

### G. Site Shell, Executive Summary, Navigation
- **Scope:** Integrates the others; runs last. Shared files.
- **Owned Files:** `index.html`, `README.md`, `css/style.css`, `js/main.js`, `pages/executive_summary.html`
- **Dependencies:** Runs after A-F complete.
