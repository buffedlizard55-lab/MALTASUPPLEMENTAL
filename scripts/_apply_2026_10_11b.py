#!/usr/bin/env python3
"""One-off: add/refresh verified records discovered in the 2026-10-11 re-verification pass.

Canonical 13-field key order is preserved. Every added record cites a URL that is
appended to docs/SOURCES.md by the same script so the validator's source-log gate
stays green.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
CANON = [
    "id", "name", "category", "area", "address", "hours", "price range",
    "description", "source_url", "source_type", "date_checked", "confidence", "notes",
]

TA_URL = "https://www.tripadvisor.com/RestaurantsNear-g608947-d278215-AX_ODYCY_Hotel-Qawra_Island_of_Malta.html"
TA_UK_URL = "https://www.tripadvisor.co.uk/RestaurantsNear-g608947-d278215-AX_ODYCY_Hotel-Qawra_Island_of_Malta.html"
TA_HOTEL_URL = "https://www.tripadvisor.com/Hotel_Review-g608947-d278215-Reviews-or200-AX_ODYCY_Hotel-Qawra_Island_of_Malta.html"

VOLATILE = (
    "Counts are a live platform snapshot read 11 October 2026, not a fixed fact. A second capture of the "
    "same list on a country domain minutes later returned slightly different figures (for example Trattoria "
    "Riccardo 1,965 versus 1,991 reviews and Royale Barrel 129 versus 130), so treat every number as "
    "approximately correct on that date and volatile afterwards. The page interleaves sponsored entries, and "
    "TripAdvisor's own ordering is relevance-based rather than a pure rating or review-count ranking."
)

# --- Workstream B: food -----------------------------------------------------
FOOD_NEW = [
    {
        "id": "tripadvisor-near-ax-odyy-2026-10-11",
        "name": "Most-reviewed places near AX ODYCY · dated TripAdvisor capture",
        "category": "Review research & limitations",
        "area": "Qawra (Saint Paul’s Bay), mostly within 0.5 mi of the hotel",
        "address": "Not applicable — aggregated platform capture; each venue has its own record or is named inline here",
        "hours": "Capture read 11 October 2026 from the TripAdvisor “Restaurants near AX ODYCY Hotel” list, which showed results 1–30 of 1,781. Hours were not captured per venue in this pass.",
        "price range": "Not a price source. TripAdvisor “$$–$$$” bands are relative tiers, not euro quotes.",
        "description": (
            "This is the closest thing to a dated, platform-sourced popularity ranking for the hotel’s immediate "
            "eating area that this research could actually read. Ranking the capture by review volume rather than by "
            "display order gives: Cheeky Monkey Gastropub Qawra ≈2,775 · Nine Lives ≈2,449 · Ta’ Pawla ≈1,826 · "
            "Ocean Basket Malta ≈1,662 · Trattoria Riccardo ≈1,965 · Luzzu ≈1,309 (operator says closed for "
            "refurbishment) · Tagine ≈1,283 · La Sorpresa ≈922 · Peking ≈914 · Knickerbocker ≈698 · Gate of "
            "India ≈678 · Churchill’s ≈514 · La Nave ≈556 · Carvv Grill & Enoteca ≈475 · Chaplin’s ≈591 · "
            "Ta Bertu’s ≈542 · Lovage ≈571 · Ombré ≈100 · Sabi House ≈94 · Kora ≈104. Ratings in the same "
            "capture ran from 4.1 (Ocean Basket) to 5.0 (Sabi House, Minoa), so a big review count and a high score "
            "are separate things. Review volume is evidence that a place is well known, not evidence that it is "
            "open, cheap, good for you, or bookable on your dates."
        ),
        "source_url": TA_URL,
        "source_type": "review",
        "date_checked": "2026-10-11",
        "confidence": "partially verified",
        "notes": (
            f"Fresh read 11 October 2026: {TA_URL} and {TA_UK_URL} ; hotel-page neighbourhood panel {TA_HOTEL_URL} . "
            + VOLATILE
            + " Do not merge these figures with the separate Qawra/Buġibba “Featured” snapshots already in this "
            "dataset; different pages, different sort, different counts. Luzzu is excluded from recommendations "
            "because its operator states it is closed for refurbishment."
        ),
    },
    {
        "id": "royale-barrel-qawra",
        "name": "Royale Barrel Bistro Bar Qawra",
        "category": "Restaurant & bar · Qawra",
        "area": "Qawra",
        "address": "Qawra; the dated capture places it 0 mi from AX ODYCY. Street address not verified from an operator page in this pass.",
        "hours": "Not captured from the operator’s own page in this pass. Check before relying on it.",
        "price range": "TripAdvisor tier “$$–$$$”; not a euro quote.",
        "description": "Brew pub / Mediterranean bistro bar a short walk from the hotel. In the 11 October 2026 capture it showed 4.9 from about 129–130 reviews.",
        "source_url": TA_URL,
        "source_type": "review",
        "date_checked": "2026-10-11",
        "confidence": "unverified",
        "notes": "Existence, proximity and rating come only from a dated review-platform capture; opening hours, menu and price were not confirmed with the operator. " + VOLATILE,
    },
    {
        "id": "mamacita-latino-bar-qawra",
        "name": "Mamacita Latino Bar Qawra",
        "category": "Restaurant & bar · Qawra",
        "area": "Qawra",
        "address": "Qawra, roughly 0.1 mi from AX ODYCY. Street address not verified from an operator page in this pass.",
        "hours": "Not captured from the operator’s own page in this pass. Check before relying on it.",
        "price range": "TripAdvisor tier “$$–$$$”; not a euro quote.",
        "description": "Latin/fusion bar about a short walk from the seafront hotels. Review capture 11 October 2026: 4.9 from about 185–218 reviews — a good example of a busy, well-reviewed bar that is still not a meal-plan inclusion.",
        "source_url": TA_URL,
        "source_type": "review",
        "date_checked": "2026-10-11",
        "confidence": "unverified",
        "notes": "Review-platform capture only; no operator page read. " + VOLATILE,
    },
    {
        "id": "churchills-qawra",
        "name": "Churchill’s Restaurant",
        "category": "Restaurant · Qawra",
        "area": "Qawra",
        "address": "Qawra, roughly 0.2 mi from AX ODYCY. Street address not verified from an operator page in this pass.",
        "hours": "Not captured from the operator’s own page in this pass. Check before relying on it.",
        "price range": "TripAdvisor tier “$$–$$$”; not a euro quote.",
        "description": "Mediterranean/European restaurant near the hotel. Review capture 11 October 2026: 4.5 from about 514 reviews, with plate comments focused on starters and salmon/sunfish pasta.",
        "source_url": TA_URL,
        "source_type": "review",
        "date_checked": "2026-10-11",
        "confidence": "unverified",
        "notes": "Review-platform capture only; no operator page read, no menu or hours confirmation. " + VOLATILE,
    },
    {
        "id": "tagine-qawra",
        "name": "Tagine Restaurant",
        "category": "Restaurant · Indian / Moroccan",
        "area": "Qawra",
        "address": "Qawra; the dated capture lists it 0 mi from AX ODYCY. Street address not verified from an operator page in this pass.",
        "hours": "Not captured from the operator’s own page in this pass. Check before relying on it.",
        "price range": "TripAdvisor tier “$$–$$$”; not a euro quote.",
        "description": "Indian/Moroccan buffet-style cooking in the Qawra tourist strip. Review capture 11 October 2026: 4.4 from about 1,283 reviews — one of the higher-volume Indian/Moroccan entries near the hotel.",
        "source_url": TA_URL,
        "source_type": "review",
        "date_checked": "2026-10-11",
        "confidence": "unverified",
        "notes": "Review-platform capture only. No operator page read, so buffet hours, price and dietary handling are unconfirmed. " + VOLATILE,
    },
    {
        "id": "gate-of-india-qawra",
        "name": "Gate of India Restaurant & Bar",
        "category": "Restaurant · Indian",
        "area": "Qawra",
        "address": "Qawra, roughly 0.2 mi from AX ODYCY. Street address not verified from an operator page in this pass.",
        "hours": "Not captured from the operator’s own page in this pass. Check before relying on it.",
        "price range": "TripAdvisor tier “$$–$$$”; not a euro quote.",
        "description": "Indian restaurant and bar near the hotel. Review capture 11 October 2026: 4.5 from about 678 reviews.",
        "source_url": TA_URL,
        "source_type": "review",
        "date_checked": "2026-10-11",
        "confidence": "unverified",
        "notes": "Review-platform capture only; no operator page read. " + VOLATILE,
    },
    {
        "id": "knickerbocker-qawra",
        "name": "Knickerbocker Restaurant",
        "category": "Café & breakfast · Qawra",
        "area": "Qawra",
        "address": "Qawra, roughly 0.1–0.2 mi from AX ODYCY. Street address not verified from an operator page in this pass.",
        "hours": "Not captured from the operator’s own page in this pass. Check before relying on it.",
        "price range": "TripAdvisor tier “$”; the lowest band in the capture, still not a euro quote.",
        "description": "Café and breakfast spot that also appears on the capture’s “Cheap Eats in Qawra” list. Review capture 11 October 2026: 4.2 from about 695–698 reviews, repeatedly described in the sampled comments as a breakfast stop with large salads.",
        "source_url": TA_URL,
        "source_type": "review",
        "date_checked": "2026-10-11",
        "confidence": "unverified",
        "notes": "Review-platform capture only. “Cheap Eats” is a TripAdvisor filter, not a verified meal price. " + VOLATILE,
    },
    {
        "id": "la-nave-qawra",
        "name": "La Nave",
        "category": "Restaurant · Mediterranean / fusion",
        "area": "Qawra",
        "address": "Qawra; the dated capture places it close to the hotel. Street address not verified from an operator page in this pass.",
        "hours": "Not captured from the operator’s own page in this pass. Check before relying on it.",
        "price range": "TripAdvisor tier “$$–$$$”; not a euro quote.",
        "description": "Mediterranean/fusion restaurant in the Qawra area with a large review base. Review capture 11 October 2026: 4.0 from about 556–565 reviews — the lowest rating among the high-volume entries in this capture, which is a useful counter-example to “most reviewed = best rated”.",
        "source_url": TA_URL,
        "source_type": "review",
        "date_checked": "2026-10-11",
        "confidence": "unverified",
        "notes": "Review-platform capture only; no operator page read. " + VOLATILE,
    },
    {
        "id": "chaplins-pub-diner-qawra",
        "name": "Chaplin’s Pub Diner",
        "category": "Restaurant & bar · Qawra",
        "area": "Qawra",
        "address": "Qawra, roughly 0.1 mi from AX ODYCY. Street address not verified from an operator page in this pass.",
        "hours": "Not captured from the operator’s own page in this pass. Check before relying on it.",
        "price range": "TripAdvisor tier “$$–$$$”; not a euro quote.",
        "description": "Pub/diner in the Qawra strip. Review capture 11 October 2026: 4.4 from about 591 reviews.",
        "source_url": TA_URL,
        "source_type": "review",
        "date_checked": "2026-10-11",
        "confidence": "unverified",
        "notes": "Review-platform capture only; no operator page read. " + VOLATILE,
    },
]

# --- Workstream C: activities / recreation ----------------------------------
ACTIVITY_NEW = [
    {
        "id": "eco-sports-bugibba",
        "name": "Eco Sports Limited — bike, e-bike, SUP and kayak rental",
        "category": "Outdoor activity · Buġibba (near the hotel)",
        "area": "Buġibba, St Paul’s Bay",
        "address": "8 Triq L-Imsell, Buġibba, San Pawl il-Baħar, SPB 2440, Malta · +356 9947 1627 · bookings@ecosportsltd.com",
        "hours": "Listed by review platforms and a directory as split opening hours 09:00–13:00 and 17:00–19:00. The operator’s own booking pages show a request form rather than a posted timetable.",
        "price range": "Published operator daily rates: MTB E-Bike €35 (multiday from €33.33 at 3 days to €25.00 at 21 days); MTB Platinum €30; MTB Gold €25; MTB Silver €17; Trekking Bike €20; 24″ MTB €15; MTB Kids €15 (ages 8–12, must be accompanied). Stand Up Paddle Board from €30; Double SUP €50. Guided bike/e-bike tours from €55 per person (listed as 3 hours, 12–20 people). Malta delivery with collection €20; Gozo delivery €50.",
        "description": "A practical, independently run way to see more of the island than Qawra without using a bus: rental of mountain, trekking and electric bikes plus SUP/kayak hire, and guided tours including a Valletta and Three Cities highlights ride. This is the strongest publicly priced, operator-confirmed recreation lead found near the hotel this pass, and it is a genuine alternative to an event day that finishes after the last bus back to Qawra.",
        "source_url": "https://ecosportsltd.com/",
        "source_type": "official",
        "date_checked": "2026-10-11",
        "confidence": "partially verified",
        "notes": (
            "Operator pages read in full 11 October 2026: https://ecosportsltd.com/ , https://ecosportsltd.com/bike-rentals/ , "
            "https://ecosportsltd.com/watersports-rentals/ , https://ecosportsltd.com/rent/mtb-e-bike-booking-request/ . "
            "Prices are the operator’s published daily rates, not a quote for specific dates, and the booking pages are "
            "request forms rather than an instant checkout. Dated review-platform evidence on the same day: 4.9 from about "
            "158 reviews, ranked first of five “Nature & Parks” entries in Buġibba "
            "(https://www.tripadvisor.com/Attraction_Review-g608948-d5567696-Reviews-Eco_Sports_Malta-Bugibba_St_Paul_s_Bay_Island_of_Malta.html) . "
            "A TripAdvisor owner reply quotes much cheaper historic rates (MTB €10, trekking €15, e-bike €20 per day) — "
            "those are older owner-posted prices and are not the current published rate; treat the operator page as "
            "current. Reviewers describe busy, narrow roads and few bike paths, so plan routes for morning light and "
            "confirm helmet/lock/repair-kit inclusion at booking. Malta drives on the left."
        ),
    },
    {
        "id": "empire-cinema-arcade-bugibba",
        "name": "Empire Cinema, Buġibba — arcade games room",
        "category": "Arcade / games room · Buġibba",
        "area": "Buġibba, St Paul’s Bay",
        "address": "Buġibba, St Paul’s Bay. Street address and current opening hours not verified from an operator page in this pass.",
        "hours": "Not verified. Sessions run around film showings according to the local listing below; check before going.",
        "price range": "Not checked. Arcade credits are normally charged per play, but no current price sheet was read.",
        "description": "The local listing describes the Empire Cinema as popular with local young people partly because of its arcade games room, with a bar, restaurant and food store under one roof. That makes it the closest thing to casual, walk-in gaming in the Buġibba strip, which matters because no public PC-gaming café was verified in this research.",
        "source_url": "https://www.maltascout.com/en/attraction/cinema/the-empire-cinema",
        "source_type": "review",
        "date_checked": "2026-10-11",
        "confidence": "unverified",
        "notes": (
            "Independent Malta listing directory, read via search extract on 11 October 2026 — this session could not "
            "open the page directly, so the description is a search-index extract rather than a full page read. It is "
            "a cinema with an arcade room, not a PC café, not a venue with tournament PCs, and not an esports club. "
            "No age restriction, price list or current trading status was confirmed. Do not plan an event night around it."
        ),
    },
    {
        "id": "malta-game-entertainment-directory-2026-10-11",
        "name": "Malta game & entertainment centres — dated directory read, no walk-in PC venue",
        "category": "Gaming directory & limitations",
        "area": "Malta-wide",
        "address": "Not applicable — platform category listing",
        "hours": "Directory read 11 October 2026. Opening hours shown per venue were inconsistent between captures and are not transcribed here as facts.",
        "price range": "Not a price source. Individual venues publish their own prices (for example The Eden’s arcade credits and MULTIMAXX laser/VR pricing, which have their own records here).",
        "description": "A dated read of the platform’s Malta “Game & Entertainment Centers” category listed MultiMaxx, Laser Tag Malta (marked “Temporarily closed” in this capture), Falcon Archery Malta, The Eden and Gravity Malta / Jurassic Immersive Experience. Arcade and entertainment centres are real and walk-in; a public PC-gaming café for a CS2 attendee is not on that list. This confirms the gap already recorded for esports venues: this research has still not found a venue offering walk-in PC sessions to the public.",
        "source_url": "https://www.tripadvisor.com/Attractions-g190311-Activities-c56-t110-Malta.html",
        "source_type": "review",
        "date_checked": "2026-10-11",
        "confidence": "partially verified",
        "notes": (
            "Platform category page captured 11 October 2026 via search extract; the page could not be opened directly in "
            "this session. The Eden’s own hours appeared on a second platform capture (Thursday 11:00–00:00, Friday to "
            "01:00, Saturday 10:00–01:00, Sunday and Monday to midnight, Tuesday and Wednesday to midnight) but that "
            "capture is undated beyond “2026 Reviews”, so it is a lead, not a timetable. “Temporarily closed” is the "
            "platform’s status word and not proof of permanent closure. A tournament organiser, bootcamp or team "
            "training session is a different product from walk-in public play and must not be presented as one."
        ),
    },
]

SOURCE_ROWS = [
    (
        "Dated TripAdvisor “Restaurants near AX ODYCY Hotel” capture: rating, review count and distance for ~30 "
        "Qawra venues, including Cheeky Monkey ≈2,775, Nine Lives ≈2,449, Ta’ Pawla ≈1,826, Ocean Basket ≈1,662, "
        "Trattoria Riccardo ≈1,965, Luzzu ≈1,309, Tagine ≈1,283, La Sorpresa ≈922, Peking ≈914, Knickerbocker ≈698, "
        "Gate of India ≈678, Lovage ≈571, La Nave ≈556, Ta Bertu’s ≈542, Churchill’s ≈514, Carvv ≈475, Chaplin’s "
        "≈591, Zigumar ≈275, Salia ≈265, Mamacita ≈185–218, Royale Barrel ≈129–130, Kora ≈104, Ombré ≈100, Sabi "
        "House ≈94.",
        TA_URL,
        "2026-10-11",
        "B — Food",
        "Review platform. Read via search extract on the .com and .co.uk domains minutes apart; the two captures "
        "already disagreed on several counts (Trattoria Riccardo 1,965 vs 1,991; Royale Barrel 129 vs 130) and on the "
        "leading pair, which is why every count is recorded as approximate. Sponsored entries are interleaved and the "
        "platform’s display order is relevance-based, not a rating rank. This is the only readable platform-ranked "
        "popularity evidence obtained for the hotel’s immediate area; Yelp, Instagram, TikTok, Facebook, Reddit and X "
        "direct refreshes remain blocked and are not substituted with invented sentiment.",
    ),
    (
        "Eco Sports Limited operator pages: 8 Triq L-Imsell, Buġibba SPB 2440; MTB E-Bike €35/day with multiday "
        "tiers (€33.33 at 3 days to €25.00 at 21 days), MTB Platinum €30, MTB Gold €25, MTB Silver €17, Trekking "
        "€20, 24″ MTB €15, MTB Kids €15 (8–12, accompanied); SUP from €30 and Double SUP €50; guided bike/e-bike "
        "tours from €55 per person; Malta delivery with collection €20, Gozo €50.",
        "https://ecosportsltd.com/",
        "2026-10-11",
        "C — Activities",
        "Official operator site, pages read in full this session. These are published daily rates and request-form "
        "bookings, not a dated quote. A TripAdvisor owner reply quotes much lower historic rates; the operator page "
        "governs.",
    ),
    (
        "Dated review evidence for Eco Sports: 4.9 from about 158 reviews, first of five “Nature & Parks” entries in "
        "Buġibba; split hours reported as 09:00–13:00 and 17:00–19:00; a reviewer paid €55 per e-bike; another "
        "reports €70 for two bikes over two days.",
        "https://www.tripadvisor.com/Attraction_Review-g608948-d5567696-Reviews-Eco_Sports_Malta-Bugibba_St_Paul_s_Bay_Island_of_Malta.html",
        "2026-10-11",
        "C — Activities",
        "Review platform; corroborates the operator’s existence, address and rough price level. Reviewer prices are "
        "individual receipts, not tariff evidence.",
    ),
    (
        "Empire Cinema, Buġibba — description of a cinema with a games room, bar, restaurant and food store, popular "
        "with local young people.",
        "https://www.maltascout.com/en/attraction/cinema/the-empire-cinema",
        "2026-10-11",
        "C — Activities",
        "Independent local listing directory. Search-index extract only; the page itself could not be opened in this "
        "session, so address, hours, prices and age rules are unconfirmed. Cinema arcade, not a PC café.",
    ),
    (
        "Malta “Game & Entertainment Centers” category listing: MultiMaxx, Laser Tag Malta (“Temporarily closed”), "
        "Falcon Archery Malta, The Eden, Gravity Malta / Jurassic Immersive Experience.",
        "https://www.tripadvisor.com/Attractions-g190311-Activities-c56-t110-Malta.html",
        "2026-10-11",
        "C — Activities",
        "Review platform category page via search extract; no public PC-gaming venue appears. “Temporarily closed” "
        "is platform wording, not proof of permanent closure. Confirms the recorded gap rather than closing it.",
    ),
]


def apply() -> None:
    for filename, records in (("food.json", FOOD_NEW), ("activities.json", ACTIVITY_NEW)):
        path = DATA / filename
        payload = json.loads(path.read_text(encoding="utf-8"))
        existing = {r["id"] for r in payload["records"]}
        for record in records:
            if record["id"] in existing:
                raise SystemExit(f"duplicate id {record['id']} in {filename}")
            ordered = {key: record[key] for key in CANON}
            payload["records"].append(ordered)
        path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"{filename}: {len(payload['records'])} records (+{len(records)})")

    log = ROOT / "docs/SOURCES.md"
    text = log.read_text(encoding="utf-8")
    header = (
        "\n## Verification pass — 11 October 2026 (session arena/09cdfbf0)\n\n"
        "Rows below are additive; earlier rows remain historical. Every row records what was actually readable in this "
        "session. Direct page fetches were blocked for most sites, so several rows are explicitly search-index extracts.\n\n"
        "| Claim / scope | URL | Accessed / attempted UTC | Workstream | Result / limitation |\n"
        "|---|---|---|---|---|\n"
    )
    new_rows = "".join(
        f"| {claim} | {url} | {date} | {stream} | {limit} |\n"
        for claim, url, date, stream, limit in SOURCE_ROWS
    )
    if "session arena/09cdfbf0" not in text:
        log.write_text(text + header + new_rows, encoding="utf-8")
        print("docs/SOURCES.md: appended verification-pass table")
    else:
        print("docs/SOURCES.md: section already present, left unchanged")


if __name__ == "__main__":
    apply()