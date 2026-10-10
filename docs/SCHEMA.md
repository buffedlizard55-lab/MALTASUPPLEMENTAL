# Shared data schema

The canonical topic-record schema is documented in [`data/schema.md`](../data/schema.md) and established in [`docs/PLAN.md`](PLAN.md). All A–F JSON files use a `records` array and the same required keys: `id`, `name`, `category`, `area`, `address`, `hours`, `price range`, `description`, `source_url`, `source_type`, `date_checked`, `confidence`, and `notes`.

Allowed `source_type` values are `official`, `map`, `review`, and `social`; allowed confidence values are `verified`, `partially verified`, and `unverified`. Missing or volatile facts stay explicitly unknown, and every source URL is recorded in [`docs/SOURCES.md`](SOURCES.md).
