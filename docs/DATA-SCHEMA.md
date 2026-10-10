# Structured content schema

Each entry in `data/*.json` is a content item and must include these fields:

| Field | Meaning / rule |
|---|---|
| `id` | Stable lower-case slug, unique within the data file. |
| `name` | Official / commonly used name. |
| `category` | Item type (restaurant, café, route, station, event, landmark, etc.). |
| `area` | Verified locality or explicitly `Not verified`. |
| `address` | Exact verified address, `Not published`, or `Not applicable` for non-place items. |
| `hours` | Official published hours/schedule or `Not published`; do not infer seasonal hours. |
| `price_range` | Current official price, attributed review-price band, estimate clearly labelled, or `Not published`. |
| `description` | Factual, concise description; separate direct evidence from inference. |
| `source_url` | Primary evidence URL for the main claim; use a working URL. |
| `source_type` | One of `official`, `map`, `review`, `social`. |
| `date_checked` | ISO date when the source was actually checked. |
| `confidence` | `verified`, `partially verified`, or `unverified`. |
| `notes` | Limitations/conflicts; empty string only when there is nothing material to note. |

Optional `supporting_sources` may list additional links with the exact claim each supports. Every displayed claim must appear in structured data or in the executive summary's own structured entry. Unknowns must be explicit; never invent opening times, prices, ratings, public-transport routes, or event/radio schedules. Validate each file with `python tools/build_site.py --check`.
