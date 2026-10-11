#!/usr/bin/env python3
"""One-off helper: add the 11 October 2026 review-snapshot and esports-venue findings."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"


def load(name: str) -> dict:
    return json.loads((DATA / name).read_text(encoding="utf-8"))


def save(name: str, payload: dict) -> None:
    (DATA / name).write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def find(payload: dict, record_id: str) -> dict:
    for record in payload["records"]:
        if record["id"] == record_id:
            return record
    raise SystemExit(f"not found: {record_id}")


# ------------------------------------------------------------------- food
food = load("food.json")
food["last_updated"] = "2026-10-11"
food["intro"] = (
    "A source-backed shortlist centered on AX ODYCY and Qawra, with a few clearly labeled farther outings. Operator "
    "pages and menus are primary; review ratings, counts and guide positions are dated snapshots, not stable quality "
    "measures. Direct TripAdvisor profiles were checked on 9 October 2026 and the TripAdvisor Qawra/Buġibba "
    "“10 best” pages were read again on 11 October 2026 (rankings and review counts captured in a dedicated record). "
    "Limited Google Maps profile views loaded for Minoa and Trattoria Riccardo only. Yelp, Instagram, TikTok, "
    "Facebook and X requests returned HTTP 403; five Reddit threads last read on 24 September could not be refreshed "
    "on 9 October (HTTP 403), and a search-engine view of one 2021 Reddit thread is dated and anecdotal. TripAdvisor "
    "currently labels The Meeting Point Cafe & Snacks Bar CLOSED, without independent operator confirmation. Luzzu’s "
    "operator says it is closed for refurbishment; no reopening date is published. Recheck hours, menu prices, status "
    "and reservations before travelling."
)
food["records"].insert(
    0,
    {
        "id": "tripadvisor-popularity-snapshot-2026-10-11",
        "name": "“Most popular” snapshot — TripAdvisor Qawra and Buġibba lists read 11 October 2026",
        "category": "Review-platform snapshots (dated)",
        "area": "Qawra (Saint Paul’s Bay) and Buġibba / St Paul’s Bay",
        "address": "Not applicable — aggregated platform ranking; each venue’s own address is in its record",
        "hours": (
            "Snapshot taken 11 October 2026. TripAdvisor “10 best restaurants in Qawra/Buġibba” pages: Qawra order "
            "1 Trattoria Riccardo 4.8 (2,651 reviews), 2 Minoa Mediterranean Fusion 5.0 (764), then Cheeky Monkey "
            "Gastropub 4.5 (3,366), Woodhut Pub & Diner 4.6 (597), Luzzu 4.5 (1,582), Churchill’s 4.5 (518), "
            "Knickerbocker 4.2 (700), 9 Ball Cafe 4.7 (60), Quattro Fratelli 3.7 (622), Ocean Basket 5.0 (266), "
            "Deck & Keel 4.9 (969). Buġibba order 1 Venus 4.8 (2,900), 2 Nine Lives 4.7 (2,870), plus Fluid Bistro "
            "& Steak House 4.9 (990), Ta’ Rożi 4.5 (885), Victoria Gastropub 4.3 (2,128), La Stalla 4.2 (1,103), "
            "Travellers Cafe/Bar 4.6 (293), Bugies 4.5 (248), Ta’ Pawla 4.3 (1,870), Kora 4.9 (180)."
        ),
        "price range": (
            "Not applicable — popularity snapshot; each venue’s price band is on its own TripAdvisor listing (mostly "
            "$$–$$$ in these lists, with Minoa listed $$$$)"
        ),
        "description": (
            "This is the direct answer to “which places are most popular”, recorded as a dated platform snapshot "
            "rather than a quality judgement: on 11 October 2026 TripAdvisor’s Qawra list ranked Trattoria Riccardo "
            "first and Minoa Mediterranean Fusion second, and its Buġibba list ranked Venus first and Nine Lives "
            "second. Three of those four are already on this shortlist with operator-sourced details; both Qawra "
            "leaders are at or next to AX ODYCY. Ratings and rankings move with platform policy, seasonal trade and "
            "review velocity, so use the ranking to choose what to try and the individual records to check hours."
        ),
        "source_url": "https://www.tripadvisor.com/Restaurants-g608947-Qawra_Island_of_Malta.html",
        "source_type": "review",
        "date_checked": "2026-10-11",
        "confidence": "partially verified",
        "notes": (
            "TripAdvisor “THE 10 BEST Restaurants in Qawra” page read 11 October 2026: "
            "https://www.tripadvisor.com/Restaurants-g608947-Qawra_Island_of_Malta.html ; companion Buġibba list: "
            "https://www.tripadvisor.com/Restaurants-g608948-Bugibba_St_Paul_s_Bay_Island_of_Malta.html . Both are "
            "review-platform pages: the ranking is the platform’s own ordering at that moment, review counts shift "
            "daily, and a “view” ranking also exists separately. This record deliberately duplicates no operator "
            "facts — hours, menus and status come from the individual venue records. Yelp, Instagram, TikTok, "
            "Facebook and X page requests were still blocked in this session’s checks (HTTP 403 as previously "
            "logged); a search-engine view of one 2021 Reddit thread on Malta gaming places surfaced but is dated "
            "and anecdotal and is not used as a ranking source: "
            "https://www.reddit.com/r/malta/comments/q5vylk/gaming_places_in_malta/ ."
        ),
    },
)
save("food.json", food)

# -------------------------------------------------------------- activities
activities = load("activities.json")
activities["last_updated"] = "2026-10-11"

twc = find(activities, "twc-finals-2026")
twc["hours"] = (
    "Official event window 12–19 October 2026: arrival 12 October, media day 13 October, Group Stage 14–16 October, "
    "Playoffs 17–18 October, departure 19 October. Daily public match/door times and ticket-holder instructions are "
    "not published. For comparison only, BLAST’s attendee guide for a separate event it ran at the same studio "
    "published doors at 13:30, 13:00, 11:00 and 10:30 CEST across four days — no such information exists for these "
    "Finals."
)
twc["description"] = (
    "The official organizer page lists the overall event window, stage dates, and Malta location. A "
    "Thunderpick-issued release names BLAST Studios Malta; BLAST’s ticketing partner and national press place that "
    "studio in Ta’ Qali, Ħ’Attard (Malta Fairs & Conventions Centre). No public ticket sale, spectator policy, "
    "entrance or daily door time for these Finals was found on 11 October 2026, while Thunderpick says all matches "
    "will be broadcast on its Twitch, Kick and YouTube channels — so treat in-person attendance as unconfirmed and "
    "the broadcast as the documented fallback."
)
twc["price range"] = (
    "Spectator access and ticket price not confirmed. Precedent only: BLAST-run events at the same studio sold "
    "tickets from €10.00 (July 2026)"
)
twc["notes"] = (
    twc["notes"]
    + " Re-read 11 October 2026 (second session): BLAST’s own attendee guide for the separate July 2026 Bounty "
    "event names the venue “Malta Fairs & Conventions Centre – BLAST Arena Studios”, address “Malta Fairs & "
    "Conventions Centre, Ta Qali, ATD 4000 Ħ’Attard”, and publishes doors times (13:30 / 13:00 / 11:00 / 10:30 "
    "CEST across its four days) plus advertised meet-and-greets: https://blast.tv/cs/news/malta-fan-guide . Those "
    "are that event’s arrangements and are quoted only to show what TWC has not published. No TWC ticket link was "
    "found on the official page, in the Thunderpick release, or in an esports event directory: "
    "https://visitesports.com/locations/mt/malta . Thunderpick’s stated broadcast channels: "
    "https://esportsbrief.substack.com/p/thunderpick-world-championship-2026-return . Independent scheduling "
    "corroboration (14–18 October, same studio): "
    "https://www.hltv.org/news/45525/falcons-and-furia-headline-thunderpick-world-championship-team-list ."
)

plaza = find(activities, "esports-plaza-sliema-status")
plaza["name"] = "Esports Plaza Gaming Lounge — status conflict (Maps closed vs directories listing it)"
plaza["hours"] = (
    "No current hours verified from the operator. Google Maps marked the place permanently closed as checked 9 "
    "October 2026; the national esports venue directory still lists Esports Plaza as an “Esports Facility/Studio” in "
    "Sliema, and a third-party attraction directory still publishes hours (weekdays from 16:00, weekends from 12:00, "
    "to midnight) that may be stale."
)
plaza["description"] = (
    "This was a PC/console gaming lounge at The Plaza, Sliema. Google Maps reports it permanently closed, and both "
    "the venue’s own domain and the shopping centre’s old page failed when checked; but the Malta esports venue "
    "directory still lists it as an active facility and a third-party attraction directory still carries opening "
    "hours. The conflict is unresolved: do not plan a visit, and call or message before travelling."
)
plaza["notes"] = (
    plaza["notes"]
    + " Added 11 October 2026 (second session): the national esports venue directory still lists Esports Plaza "
    "under “Esports Venues” as an Esports Facility/Studio in Sliema: https://esports.org.mt/esports-venues/ — a "
    "directory entry that can lag reality. A third-party attraction directory publishes hours (Mon–Thu 16:00–00:00, "
    "Fri–Sun 12:00–00:00) and describes a modern gaming lounge: "
    "https://hopsa.io/en/attractions/malta,jedzenie-picie,esports-plaza-gaming-lounge-69cf83a22b . Neither is the "
    "operator, and neither overrides the Maps closure report; treat the venue as unconfirmed and verify by phone "
    "before any trip."
)
plaza["date_checked"] = "2026-10-11"

activities["records"].insert(
    0,
    {
        "id": "malta-esports-venue-directory",
        "name": "Malta esports venue directory — what actually exists (bootcamps and studios, not walk-in cafés)",
        "category": "Dedicated PC gaming — status conflict",
        "area": "Ħamrun, Ta’ Qali, St Julian’s, Sliema and Siġġiewi",
        "address": (
            "Directory entries as published: Level Academy (Ħamrun, educational facility), GMR Concepts Ltd (Ta’ "
            "Qali, bootcamp facility), Eden Esports (St Julian’s, bootcamp facility), Esports Plaza (Sliema, esports "
            "facility/studio), World Pro Racing (Siġġiewi, sim-racing facility/studio)."
        ),
        "hours": (
            "Not published in the directory. Bootcamp and studio facilities are normally used by appointment, teams "
            "or ticketed events rather than drop-in play; no walk-in hours were verified for any entry."
        ),
        "price range": "Not published; no walk-in session rates were found for any listed facility",
        "description": (
            "The national esports venue directory is the clearest published answer to “where can I play” in Malta, "
            "and the answer for a tourist is: nowhere confirmed. Its entries are a school facility, two team "
            "bootcamps, an esports studio and a sim-racing studio — not public PC cafés. Combined with the closed/"
            "unconfirmed status of the legacy PC cafés recorded here, the honest planning conclusion is that the "
            "reliable gaming options during the trip are the event broadcast, the arcade/VR venues (The Eden XP "
            "Arcade; MULTIMAXX St Julian’s and Kordin) and the hotel’s own amenities — with any PC-café visit "
            "confirmed by phone first."
        ),
        "source_url": "https://esports.org.mt/esports-venues/",
        "source_type": "official",
        "date_checked": "2026-10-11",
        "confidence": "partially verified",
        "notes": (
            "Directory read 11 October 2026: https://esports.org.mt/esports-venues/ . It is the Maltese esports "
            "body’s own venue list (source_type recorded as official for that reason) but it is a directory, not a "
            "live operator status page: it may include facilities that have closed, and it does not publish opening "
            "hours, drop-in availability or prices. It carries no 2026-dated confirmation for any single venue. "
            "Cross-reference: the same directory still lists Esports Plaza, which Google Maps marks permanently "
            "closed (see that record). No entry offers verified walk-in PC play for a visitor; if a PC session "
            "matters, ask the facility directly. The 2021 Reddit thread on Malta gaming places is older context "
            "only and is not treated as current: "
            "https://www.reddit.com/r/malta/comments/q5vylk/gaming_places_in_malta/ ."
        ),
    },
)
save("activities.json", activities)

# -------------------------------------------------------------- sources log
addition = """
## Second 11 October 2026 session — review, esports-venue and event-guide additions (UTC)

| Claim / record | URL | Date accessed (UTC) | Workstream | Source type / limitation |
|---|---|---|---|---|
| TripAdvisor’s Qawra “10 best restaurants” page read 11 October 2026 ranks Trattoria Riccardo 4.8 (2,651 reviews) first and Minoa Mediterranean Fusion 5.0 (764) second, followed by Cheeky Monkey Gastropub 4.5 (3,366), Woodhut Pub & Diner 4.6 (597), Luzzu 4.5 (1,582), Churchill’s 4.5 (518), Knickerbocker 4.2 (700), 9 Ball Cafe 4.7 (60), Quattro Fratelli 3.7 (622), Ocean Basket 5.0 (266) and Deck & Keel 4.9 (969). | https://www.tripadvisor.com/Restaurants-g608947-Qawra_Island_of_Malta.html | 2026-10-11 | B — Food & cafés | Review platform, not an operator. Ratings/counts are a dated snapshot and the platform’s ordering can change daily; the same page also shows a separate “view” ranking with different order. No operator fact was taken from this page. |
| TripAdvisor’s Buġibba “10 best restaurants” page read 11 October 2026 ranks Venus 4.8 (2,900 reviews) first and Nine Lives 4.7 (2,870) second, followed by Fluid Bistro & Steak House 4.9 (990), Ta’ Rożi 4.5 (885), Victoria Gastropub 4.3 (2,128), La Stalla 4.2 (1,103), Travellers Cafe/Bar 4.6 (293), Bugies 4.5 (248), Ta’ Pawla 4.3 (1,870) and Kora 4.9 (180). | https://www.tripadvisor.com/Restaurants-g608948-Bugibba_St_Paul_s_Bay_Island_of_Malta.html | 2026-10-11 | B — Food & cafés | Review platform snapshot as above. Yelp, Instagram, TikTok, Facebook and X remained blocked (HTTP 403) in this session’s checks. |
| The Maltese esports body’s venue directory lists Level Academy (Ħamrun, educational), GMR Concepts Ltd (Ta’ Qali, bootcamp), Eden Esports (St Julian’s, bootcamp), Esports Plaza (Sliema, esports facility/studio) and World Pro Racing (Siġġiewi, sim racing) — no public walk-in PC café. | https://esports.org.mt/esports-venues/ | 2026-10-11 | C — Activities | National esports body’s own directory; a listing is not a live operator status page, publishes no hours, prices or drop-in availability, and may lag closures. |
| A third-party attraction directory still publishes Esports Plaza Gaming Lounge (Level 0, The Plaza, Sizza Street, Sliema) with hours Mon–Thu 16:00–00:00 and Fri–Sun 12:00–00:00, conflicting with the Google Maps “permanently closed” report. | https://hopsa.io/en/attractions/malta,jedzenie-picie,esports-plaza-gaming-lounge-69cf83a22b | 2026-10-11 | C — Activities | Third-party directory, not the operator; hours may be stale. Recorded to keep the status conflict explicit, not to reopen the venue as a recommendation. |
| BLAST’s attendee guide for its separate July 2026 Bounty event names the venue “Malta Fairs & Conventions Centre – BLAST Arena Studios”, address “Malta Fairs & Conventions Centre, Ta Qali, ATD 4000 Ħ’Attard”, and publishes doors at 13:30 / 13:00 / 11:00 / 10:30 CEST across its four days, plus advertised meet-and-greets. | https://blast.tv/cs/news/malta-fan-guide | 2026-10-11 | A/C — Transport & Activities | Organizer guide for a different event; quoted only to show what the Thunderpick Finals has not published. Do not transfer doors, access rules or meet-and-greet arrangements to TWC. |
| A search-engine view of an older Reddit thread on Malta gaming places surfaced on 11 October 2026 with 2021-dated replies; its content is not current and is used only to date the community discussion. | https://www.reddit.com/r/malta/comments/q5vylk/gaming_places_in_malta/ | 2026-10-11 | C — Activities | Social platform content dated October 2021; the earlier session logged HTTP 403 on direct refreshes, so this is stale anecdote, not evidence. |
"""

sources_path = ROOT / "docs" / "SOURCES.md"
text = sources_path.read_text(encoding="utf-8")
if "review, esports-venue and event-guide additions" not in text:
    sources_path.write_text(text.rstrip("\n") + "\n" + addition, encoding="utf-8")
    print("SOURCES.md updated")
print("food and activities updated")
