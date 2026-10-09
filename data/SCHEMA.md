# Data schema for `data/*.json`

Every topic file is a JSON object: `{"topic": ..., "updated": "YYYY-MM-DD", "items": [...]}`.

Every item has exactly these fields (strings unless noted):

| Field | Meaning | Allowed values / format |
|---|---|---|
| `id` | stable slug, unique within file | kebab-case |
| `name` | display name | — |
| `category` | sub-category within the topic | free but keep consistent per file |
| `area` | locality / neighbourhood | e.g. `Qawra`, `Valletta`, `Island-wide` |
| `address` | street address if known | `""` if not published |
| `hours` | opening hours if known | `""` if not published / "n/a" for non-venues |
| `price_range` | typical cost band | e.g. `€`, `€€`, `€2.00 single`, `Free` |
| `description` | one–two sentence factual summary | facts only, each traceable to `source_url` |
| `source_url` | primary source for the entry | required |
| `source_type` | `official` \| `map` \| `review` \| `social` \| `news` \| `community` | required |
| `date_checked` | ISO date the source was checked | `YYYY-MM-DD` |
| `confidence` | `verified` \| `partially verified` \| `unverified` | required |
| `notes` | caveats, conflicts, cross-refs | `""` ok |

Rules:
- No fact on any HTML page may exist without a matching item here (or in `docs/SOURCES.md` for
  page-level narrative claims sourced to official pages).
- `unverified` items are shown on pages only with an explicit "Unverified" label — never as fact.
- Validation: `python3 scripts/check-data.py` (schema + id uniqueness + page coverage).
