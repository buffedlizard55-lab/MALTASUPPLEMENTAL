# Topic data schema

Each topic file in `data/` uses a top-level `records` array. Its entries carry the same common fields so the shared page renderer can display them consistently.

## Required record fields

| Field | Meaning |
|---|---|
| `id` | Stable identifier, unique within that topic file |
| `name` | Display name |
| `category` | Topic-specific record category |
| `area` | Verified locality or geographic coverage |
| `address` | Verified address, `null`, or an explicit not-published/not-verified note |
| `hours` | Verified hours, `null`, or an explicit not-published/not-verified note |
| `price range` | Supported price/fare information, `null`, or an explicit unknown; never a guessed zero |
| `description` | Short factual summary with uncertainty stated where relevant |
| `source_url` | HTTPS URL for the primary supporting source, when available |
| `source_type` | One of `official`, `map`, `review`, `social` |
| `date_checked` | ISO date, `YYYY-MM-DD` |
| `confidence` | One of `verified`, `partially verified`, `unverified` |
| `notes` | Caveats, conflicts, access limitations and useful source/question IDs |

Optional `additional_sources` entries have a label, HTTPS URL and allowed source type. Topic-specific fields are permitted where needed, but the common fields remain present. The expense file also carries trip dates, blank planner templates, categories/statuses, and optional `details.budget_options`; these are published references, not automatic trip expenses.

## Evidence and rendering rules

- A `verified` label applies only to the claim supported by its source; a venue's hours do not verify a price or event access.
- A `partially verified` or `unverified` record must preserve the unresolved detail in `notes` and, when applicable, refer to `docs/OPEN_QUESTIONS.md`.
- Unknown details are not inferred. Blank planner amounts are excluded from totals and do not mean free.
- Every primary and additional data-source URL must be represented in `docs/SOURCES.md`.
- Topic pages load and render their associated JSON records. Keep page prose aligned with the records and source log.

The complete planning process and review gates are in [`../docs/PLAN.md`](../docs/PLAN.md).
