# Data Schema

Every item in the `data/*.json` files must follow this structure:

```json
[
  {
    "id": "unique-id",
    "name": "Name of the place, event, or item",
    "category": "Broad category (e.g., 'Restaurant', 'Bus Route', 'FM Station')",
    "area": "Geographic area (e.g., 'Qawra', 'Attard', 'Island-wide')",
    "address": "Physical address if applicable",
    "hours": "Operating hours",
    "price_range": "Price range (e.g., 'Free', '€10-€20', '€€')",
    "description": "Short description",
    "source_url": "URL verifying the information",
    "source_type": "official | map | review | social",
    "date_checked": "YYYY-MM-DD",
    "confidence": "verified | partially verified | unverified",
    "notes": "Any additional context or limitations"
  }
]
```
