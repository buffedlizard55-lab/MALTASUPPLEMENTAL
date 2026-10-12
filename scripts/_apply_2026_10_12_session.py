#!/usr/bin/env python3
"""Apply arena/561bff0e session updates (reads made 2026-10-12 UTC) to topic datasets.

Each workstream edits only its owned data file. Appends are additive: existing
wording is preserved and the re-read evidence is appended to `notes`.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
TODAY = "2026-10-12"


def load(name: str) -> dict:
    return json.loads((DATA / name).read_text(encoding="utf-8"))


def save(name: str, data: dict) -> None:
    (DATA / name).write_text(
        json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )


def rec(data: dict, rid: str) -> dict:
    for r in data["records"]:
        if r["id"] == rid:
            return r
    raise KeyError(rid)


def bump(data: dict, rid: str, note: str) -> None:
    r = rec(data, rid)
    r["date_checked"] = TODAY
    r["notes"] = r["notes"].rstrip() + " " + note


# ---------------------------------------------------------------- A · transport
t = load("transport.json")
bump(
    t,
    "route-186-oct17-detour",
    "Re-read 12 October 2026 across three chunks of the live feed: both Route 186 notices and the full dated cluster remain published, including the “starting October 17” wording. See the trip-week detour-watch record for the rest of the feed on the same read.",
)
bump(
    t,
    "mpt-seasonal-fare-window-2026",
    "Fares page re-read 12 October 2026: the winter sentence still prints only “19 October 2025 to 13 June 2026” and no 2026/27 changeover, so the trip-week split remains an inference from third-party season guides, not an operator confirmation.",
)
bump(
    t,
    "event-day-transport-by-date",
    "Inputs re-checked 12 October 2026: the agenda rows and Route 186 grid evidence are unchanged; a new trip-week detour-watch record adds dated detours for 13 October (Routes 54 and 106 toward Attard) and for Routes 46/260 on Monday–Thursday nights.",
)
new = {
    "id": "trip-week-detour-watch",
    "name": "Trip-week detour watch · dated notices for 12–18 October on the live updates feed",
    "category": "Service updates",
    "area": "Attard / Ta’ Qali approaches, Mosta corridor, Marsaxlokk, Dingli and Gozo",
    "address": "Not applicable — operator service notices, not a venue",
    "hours": "Feed read end-to-end (three chunks) on 12 October 2026. Dated inside the trip week: Route 54 and Route 106 detours on Tuesday 13 October 09:30–17:30; Routes 46 and 260 detoured weekly Monday–Thursday 21:00–05:00, starting 12 October and ending 16 October at about 05:00; Routes 2, 213, 3 and 4 detoured all day until 26 November; the Dingli diversion on Routes 52 and 201 runs until 30 June 2027; Routes 81, 210 and 119 carry the every-Sunday Marsaxlokk market diversion until about 17:00; Gozo routes 303, 309, 310, 313, 322, 323, 307 and 330 carry dated detours across 12–15 October.",
    "price range": "Not applicable — service notices; ticket prices are in the fare records",
    "description": "The operator’s live updates feed changes daily, and the 12 October read shows four planning-relevant additions beyond the already-recorded 17–18 October cluster. First, if you scout the venue on the organiser’s Tuesday 13 October media day, the Attard-bound services that touch the corridor carry daytime stop omissions — Route 54 does not serve stops from Fontaine through Aquilina toward Attard, and Route 106 does not serve stops from Wiji through Aquilina toward Attard, both 09:30–17:30. Second, Route 260 — one of the late-return fallback leads toward Sliema/Gżira — has its own Monday-to-Thursday night detour through the early hours of Friday 16 October, so weekday-night fallback chains are degraded as well as the Saturday 19:00–00:00 cluster. Third, a Sunday 18 October Marsaxlokk market outing will hit the routine Sunday diversions on Routes 81, 210 and 119. Fourth, the feed prints expired notices beside current ones (one Routes 203/280/31/41/42/48/N48 notice still shows a 1 July end date), so a notice’s presence is not proof it still runs and its absence is not proof a detour is lifted — re-read the feed and the date-specific planner on each event day rather than trusting this snapshot.",
    "source_url": "https://www.publictransport.com.mt/latest-service-updates/",
    "source_type": "official",
    "date_checked": TODAY,
    "confidence": "verified",
    "notes": "Read 12 October 2026 end-to-end (three chunks) at https://www.publictransport.com.mt/latest-service-updates/ . The same read reconfirmed the previously recorded items: the 17–18 October 19:00–00:00 cluster (Routes 186, 45, 47, 103, 238, 405, 202, 260, 203, 280, 31, 41, 42, 48, N48) with “starting October 17” wording; the older Route 186 Friday/Saturday 20:00–00:00 notice ending “April 21” with no year; and the Saqqajja stop 4627 closure (Routes 109, 109A, 181, 182, 186, 201, 202, 50, 51, 52, 53, 56, N52) until a printed “January 1”. Also dated inside the trip week on this read: a Route 117 detour on Wednesday 14 October 12:00–17:00 and a Route 103 detour ending 12 October 17:00. Verified means the notices are printed on the operator’s page as quoted; none is a saved journey, and stop omissions are not journey cancellations. Recheck the feed and https://www.publictransport.com.mt/journey-planner/ on the day of travel.",
}
t["records"].append(new)
t["last_updated"] = TODAY
save("transport.json", t)

# -------------------------------------------------------------------- C · event
e = load("event.json")
bump(
    e,
    "twc-opening-matchups-14-oct",
    "Liquipedia re-read 12 October 2026: the Upcoming Matches block now names all four opening pairings with clocks printed 04:30, 07:00, 09:30 and 12:00 EDT — 9z–Aurora, Falcons–NIP, Legacy–PARIVISION, FURIA–BetBoom — matching the Malta-time set 10:30, 13:00, 15:30 and 18:00 used here; the 17 October semifinal slot (10:00 EDT / 16:00 Malta) still shows TBD versus TBD.",
)
e["last_updated"] = TODAY
save("event.json", e)

# --------------------------------------------------------------------- E · radio
r = load("radio.json")
bump(
    r,
    "bbc-radio-scotland-trip-week-commentaries",
    "Upcoming page re-read 12 October 2026: the Saturday rows now print the date label “17/10/2026” and later rows print “Thu 22 Oct 2026”; the Benfica v Celtic row still prints no date, so Thursday 15 October remains the most plausible reading, not a scheduled fact.",
)
bump(
    r,
    "radio-sportiva-dab-plus",
    "Palinsesto re-read 12 October 2026: the dated “Sportiva Live” callouts still stop at 5–11 October, so no trip-week match is named; the recurring grid (weekday Diretta Sp.+Calciom. 15:05–17:00, weekend Diretta Sportiva 15:05–17:00) is unchanged.",
)
bump(
    r,
    "bbc-world-service-dab-sportsworld",
    "Upcoming page re-read 12 October 2026: the 17/10/2026 and 18/10/2026 editions (episodes w1730c92ck0m2cw and w1730c92ck0q313) remain listed with unchanged episode IDs; the page renders start times in the viewer’s own clock, so the episode JSON offsets stay the conversion anchor.",
)
r["last_updated"] = TODAY
save("radio.json", r)

# ----------------------------------------------------------------- D · everyday
d = load("everyday.json")
w = rec(d, "october-weather-forecast")
w["description"] = (
    "The Malta Met Office panel now covers 12–18 October, so six of the seven trip days sit inside the national forecast: the national outlook for arrival day, Tuesday 13, is “windy with isolated showers” (NW force 5–6) — the one genuinely unsettled day — while 14–15 October are mainly sunny and 16–18 mainly cloudy, 24–25 °C by day. Monday 19 October remains outside the national panel and is covered only by the UK Met Office’s long-range (BETA) row. The UK panel is sunnier for the 13th than the national one and the two are shown rather than reconciled. Recheck before outdoor and sea activities, and follow marine and lifeguard notices."
)
w["hours"] = (
    "Four dated snapshots; the national panel re-read 12 October 2026. Malta Met Office (national), covering 12–18 Oct: Mon 12 partly cloudy 26/19; Tue 13 windy with isolated showers 25/19, NW F5–6 to NNW F5–6, UV 4; Wed 14 mainly sunny 24/18; Thu 15 mainly sunny 24/18; Fri 16 mainly cloudy 25/17; Sat 17 mainly cloudy 25/17; Sun 18 mainly cloudy 24/18, ESE F2–3 to F4, UV 5. Malta Met Office detail for 13 Oct (last updated 11 Oct 22:15): partly cloudy becoming partly to rather cloudy with a possibility of isolated showers in the evening, high 26 / low 19, light to moderate NW backing WNW, sea slight to moderate, sea temperature 26 °C. Met Office Valletta, covering the whole trip: 13 Oct sunny 25/22 °C; 14 Oct sunny 23/21; 15 Oct sunny 23/22; 16 Oct sunny 24/22; 17 Oct sunny 23/21; 18 Oct sunny intervals 23/21; 19 Oct sunny intervals 23/21 (18th/19th marked BETA). AccuWeather Qawra and two further secondary snapshots retain their earlier readings: 13 Oct morning rain then thunderstorms 24/19; 16 Oct thunderstorms mainly early 24/17; 17 Oct a couple of afternoon showers 23/16."
)
w["date_checked"] = TODAY
w["notes"] = w["notes"].rstrip() + " National panel re-read 12 October 2026 at https://maltametoffice.com/ (homepage panel): it now runs Monday 12 to Sunday 18 October, so 18 October appears in the national forecast for the first time — mainly cloudy 24/18, ESE F2–3 to F4 — closing most of the earlier “18–19 October beyond the national panel” gap; only Monday 19 October (departure) remains outside it. The same site’s detailed-forecast page (https://maltametoffice.com/en/detailed-forecast/ , last updated 11 October 2026 22:15) describes 13 October slightly milder than the homepage row for the same day (high 26 / low 19, light to moderate NW backing WNW versus the panel’s NW F5–6); both are quoted as published and the difference is not reconciled. The national 13 October “windy with isolated showers” also lands heavier than the UK Met Office’s sunny 25/22 for the same day, so pack a light rain layer and treat strong north-westerlies as the arrival-day default; sea temperature is 26 °C but no marine warning, lifeguard or sea-state page was checked beyond the detailed forecast’s “slight to moderate” line."
bump(
    d,
    "etias-status-2026-10",
    "FAQ re-read 12 October 2026: wording unchanged — “ETIAS is currently not in operation and no applications for travel authorisations are collected at this point” and “no action is required from travellers at this point”.",
)
d["last_updated"] = TODAY
save("everyday.json", d)

# -------------------------------------------------------------------- B · food
f = load("food.json")
bump(
    f,
    "food-platform-coverage",
    "Platform access re-checked 12 October 2026: the Yelp search for Qawra restaurants again returned HTTP 403, and no previously blocked social platform became accessible; the coverage limits above are current, not historical.",
)
f["last_updated"] = TODAY
save("food.json", f)

print("Applied session updates to transport, event, radio, everyday, food datasets.")
