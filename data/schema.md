# Data schema — single source of truth for every topic file

Every item in every `data/*.json` file uses the same fields (the user's parallel-work
protocol, adopted 9 Oct 2026). Pages are generated from / must match these files;
facts are never hand-written into pages without appearing here first.

## Required fields (all items)

| Field | Type | Meaning |
|---|---|---|
| `id` | string | Stable slug, unique per file, e.g. `food-venue-minoa` |
| `name` | string | Display name |
| `category` | string | Topic-specific category (e.g. `restaurant`, `cafe`, `bus-route`, `landmark`, `gaming-venue`, `event`, `radio-station`, `expense-line`) |
| `area` | string | Locality (Qawra, Buġibba, St Paul's Bay, Sliema, Valletta, Attard/Ta' Qali, …) |
| `address` | string | Street address if verified, else `""` |
| `hours` | string | Opening hours if verified, else `""` |
| `price_range` | string | Human-readable price/fare band, else `""` |
| `description` | string | One or two sentences, factual only |
| `source_url` | string | Primary source URL |
| `source_type` | enum | `official` \| `map` \| `review` \| `social` \| `guide` |
| `date_checked` | string | ISO date the source was read, e.g. `2026-10-09` |
| `confidence` | enum | `verified` \| `partially verified` \| `unverified` |
| `notes` | string | Caveats, conflicts, flags (never empty for `partially verified`/`unverified`) |

## File-level structure

```json
{
  "topic": "transport",
  "trip": { "hotel": "AX ODYCY, Qawra Coast Road, Qawra SPB 1902, Malta",
            "dates": "2026-10-13/2026-10-19", "nights": 6,
            "event": "Thunderpick World Championship 2026 Finals, BLAST Arena Studios, Attard (Ta' Qali), match days 2026-10-14/2026-10-18" },
  "generated": "2026-10-09",
  "items": [ … ]
}
```

## Confidence rules

- `verified` — read directly from an official/primary source on `date_checked` (or a named
  aggregator with review counts, cross-checked).
- `partially verified` — some fields confirmed, others not; `notes` must say which.
- `unverified` — could not be confirmed; must also appear in `docs/OPEN_QUESTIONS.md`.
  Never present as fact on a page.

## Source logging

Every `source_url` used by any item must also appear in `docs/SOURCES.md` with:
`claim | URL | date accessed | workstream | status`. `scripts/verify_site.py` checks this.
