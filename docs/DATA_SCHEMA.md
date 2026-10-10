# Topic data schema

Every record in `data/*.json` uses the same fields; topic-specific record shapes are not added.

| Field | Meaning |
|---|---|
| `id` | Stable, unique slug within that file. |
| `name` | Place, service, event, or planning-item name. |
| `category` | User-facing grouping used by the page filter or expense planner. |
| `area` | Malta locality/region or planning scope such as `Trip-wide`. |
| `address` | Published address; use `Not published` when unavailable. Expense categories may use `Not applicable` because they are not places. |
| `hours` | Source-published hours/schedule; use `Not published` or `Not applicable` when appropriate. |
| `price range` | Source-published current price or an explicit state such as `Not published`, `Not set`, or `Varies`; identify estimates as estimates. |
| `description` | The sourced claim(s) shown to visitors. Keep uncertainty explicit. |
| `source_url` | Primary URL used to check the record. Related corroboration may be listed in `notes` and `docs/SOURCES.md`. |
| `source_type` | Exactly one of `official`, `map`, `review`, `social`, or `directory` (a specialist/technical directory, not necessarily the service operator). |
| `date_checked` | ISO date (`YYYY-MM-DD`) when the URL/claim was last checked. |
| `confidence` | `verified`, `partially verified`, or `unverified`. |
| `notes` | Caveats, conflicts, unknowns, source context, or related corroborating URLs. Never silently promote an unverified claim. |

Each topic file is a JSON object with `topic`, `title`, `last_updated`, `intro`, and a `records` array. The A–E topic pages render their factual listing cards from the corresponding JSON files via `js/site.js`. The F expense planner uses `data/expenses.json` to create editable rows; those records are reference prompts, not prefilled estimates or quotes.
