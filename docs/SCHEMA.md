# Topic data schema

Every record in the six topic files under `data/` uses exactly these keys, in this order:

```text
id, name, category, area, address, hours, price range,
description, source_url, source_type, date_checked, confidence, notes
```

Example:

```json
{
  "id": "sample-place",
  "name": "Sample Place",
  "category": "cafe",
  "area": "Qawra",
  "address": "",
  "hours": "Not verified",
  "price range": "Not published",
  "description": "A short, source-supported description.",
  "source_url": "https://example.com/official-page",
  "source_type": "official",
  "date_checked": "2026-10-09",
  "confidence": "partially verified",
  "notes": "State which fields are uncertain and what should be checked."
}
```

Allowed values:

- `source_type`: `official`, `map`, `review`, `social`
- `confidence`: `verified`, `partially verified`, `unverified`
- `date_checked`: ISO date, `YYYY-MM-DD`

Each JSON file is a list of records; metadata belongs in documentation rather than extra record keys. Use an empty string only when a field does not apply or is not established. A partially verified or unverified record must explain its limitations in `notes`; an unsourced or unverified fact must not be presented as established on a page.

Primary URLs and any URLs embedded in record notes must also be represented in `docs/SOURCES.md` with the claim, access date and workstream. Open facts belong in `docs/OPEN_QUESTIONS.md`. Topic pages must agree with their data records.
