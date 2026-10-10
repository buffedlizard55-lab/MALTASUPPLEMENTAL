# Topic data schema

Every record in `data/*.json` uses exactly the 13 fields defined in the canonical JSON Schema [`record.schema.json`](../data/record.schema.json); topic-specific record fields are not added. All field values are strings.

| Field | Meaning |
|---|---|
| `id` | Stable, unique slug within that file. |
| `name` | Place, service, event, or planning-item name. |
| `category` | User-facing grouping used by the page filter or expense planner. |
| `area` | Malta locality/region or planning scope such as `Trip-wide`. |
| `address` | Published address; use `Not published` when unavailable. Expense categories may use `Not applicable` because they are not places. |
| `hours` | Source-published hours/schedule; use `Not published` or `Not applicable` when appropriate. |
| `price_range` | Source-published current price or an explicit state such as `Not published`, `Not set`, or `Varies`; identify estimates as estimates. |
| `description` | The sourced claim(s) shown to visitors. Keep uncertainty explicit. |
| `source_url` | Primary URL used to check the record. Related corroboration may be listed in `notes` and `docs/SOURCES.md`. |
| `source_type` | Exactly one of `official`, `map`, `review`, or `social`. |
| `date_checked` | ISO date (`YYYY-MM-DD`) when the URL/claim was last checked. |
| `confidence` | `verified`, `partially verified`, or `unverified`. |
| `notes` | Caveats, conflicts, unknowns, source context, or related corroborating URLs. Never silently promote an unverified claim. |

Each topic file is a JSON object with `topic`, `title`, `last_updated`, `intro`, and a `records` array. Dataset-level metadata is separate; every object in `records` must match the schema exactly, use an absolute HTTPS `source_url`, an ISO date, and an allowed source/confidence value. The primary URL and any supporting links in `notes` belong in [`SOURCES.md`](SOURCES.md). The A–E topic pages render factual listing cards from their JSON files via `js/site.js`. The F expense planner uses `data/expenses.json` to create editable rows; those records are optional reference prompts, not prefilled estimates or quotes. The repository validator checks the schema and source-log coverage.
