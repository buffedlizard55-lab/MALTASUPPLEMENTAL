#!/usr/bin/env python3
"""Historical editor for the 11 October venue-confirmation refresh.

This script records the earlier pass, but its fare-season and event-access
assumptions were superseded during the PR #33/current-main reconciliation.
It is retained for provenance only and must NOT be rerun on the current data;
see the live records and docs/OPEN_QUESTIONS.md for reconciled claims.
"""

from __future__ import annotations

import json
from pathlib import Path

if __name__ == "__main__":
    raise SystemExit("Disabled historical patch: its assumptions were superseded; do not rerun on reconciled data.")

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
TODAY = "2026-10-11"

EVENTBRITE = "https://www.eventbrite.co.uk/e/hotspawn-present-the-thunderpick-world-championships-2026-tickets-1988838616841"
HLTV = "https://www.hltv.org/news/45615/thunderpick-world-championship-talent-revealed"
PRN_RETURN = "https://www.prnewswire.com/news-releases/thunderpick-world-championship-2026-returns-to-malta-with-1-million-prize-pool-302850221.html"
PRN_FIELD = "https://www.prnewswire.com/news-releases/thunderpick-world-championship-2026-reveals-eight-team-field-for-1-million-malta-finals-302880720.html"
TWC_OFFICIAL = "https://world-championship.thunderpick.io/2026-finals/"
MPT_FARES = "https://www.publictransport.com.mt/fares-and-tickets/"
MPT_186 = "https://www.publictransport.com.mt/route/186/"
MPT_UPDATES = "https://www.publictransport.com.mt/latest-service-updates/"
MPT_NIGHT = "https://www.publictransport.com.mt/new-night-routes/"
MPT_PLANNER = "https://www.publictransport.com.mt/journey-planner/"
METOFFICE_VALLETTA = "https://weather.metoffice.gov.uk/forecast/sq6k4r011"
BBC_PL_UPCOMING = "https://www.bbc.co.uk/programmes/m002h76y/broadcasts/upcoming"
BBC_5LIVE_SPORT = "https://www.bbc.co.uk/programmes/b0070hx6/broadcasts/upcoming"
BBC_EP_1710 = "https://www.bbc.co.uk/programmes/m00334k6"
TALKSPORT_SCHEDULE = "https://talksport.com/schedule/"
GOAL_RADIO_RIGHTS = "https://www.goal.com/en-gb/news/premier-league-radio-commentary/blt3e3f1a90d9deedaf"
WORLDDAB = "https://www.worlddab.org/why-dab-plus/countries/malta/multiplexes"
RADIO_IN_MALTA = "https://radioinmalta.com/en/stations/"
EPL_FIXTURES = "https://www.premierleague.com/en/news/4688862/fixture-amendments-for-premier-league-matches-in-october-and-november"

VENUE_ADDRESS = (
    "BLAST Arena Studios Malta, MFCC South Gate National Stadium, ATD 4000 Attard, Malta "
    "— the address printed on the official ticketing page for this event. "
    "The listing also publishes map coordinates 35.8957343, 14.4168839. "
    "The attendee gate inside the site is not specified."
)

EVENT_DAYS = (
    "Ticketing page (read 11 October 2026) lists Wednesday 14 – Sunday 18 October 2026, 9:30 AM – 10:00 PM, "
    "with day-by-day agenda for three of the five days: Wed 14 Oct check-in 09:30 / games 10:30 (09:30–22:30); "
    "Thu 15 Oct check-in 09:30 / games 10:30 (09:30–22:30); Fri 16 Oct check-in 14:00 / games 15:00 (14:00–21:00). "
    "The Sat 17 Oct and Sun 18 Oct entries sit behind a “Show all agenda” control that did not expand in the "
    "extracted page, so playoff-day door/game times are not yet confirmed."
)

TICKET_PRICE = (
    "Free admission. The Eventbrite listing is priced “Free” and shows a “Reserve a spot” action; no paid tier "
    "was displayed when checked on 11 October 2026. This supersedes the earlier €10.00 figure, which was a "
    "ticket precedent from a separate BLAST-run event at the same studio."
)


def load(name: str) -> dict:
    return json.loads((DATA / name).read_text(encoding="utf-8"))


def save(name: str, data: dict) -> None:
    data["last_updated"] = TODAY
    (DATA / name).write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def replace(records: list[dict], record_id: str, updates: dict) -> None:
    for record in records:
        if record["id"] == record_id:
            record.update(updates)
            return
    raise SystemExit(f"record not found: {record_id}")


def amend(records: list[dict], record_id: str, field: str, addition: str) -> None:
    for record in records:
        if record["id"] == record_id:
            if addition.strip() not in record[field]:
                record[field] = record[field].rstrip() + " " + addition
            return
    raise SystemExit(f"record not found: {record_id}")


def amend_intro(data: dict, addition: str) -> None:
    if addition.strip() not in data["intro"]:
        data["intro"] = data["intro"].rstrip() + " " + addition


def append(records: list[dict], record: dict) -> None:
    if not any(existing["id"] == record["id"] for existing in records):
        records.append(record)


# ---------------------------------------------------------------- activities
activities = load("activities.json")
acts = activities["records"]
replace(acts, "twc-finals-2026", {
    "address": VENUE_ADDRESS,
    "hours": EVENT_DAYS,
    "price range": TICKET_PRICE,
    "description": (
        "Counter-Strike 2 finals, 8 teams, $1,000,000 prize pool, organised by GAM3RS_X for Thunderpick. "
        "The official ticketing listing confirms the attendee venue, the 14–18 October dates, day-by-day "
        "check-in/game times for three days, and an 18+ in-person audience. The organizer’s own page still "
        "describes the wider 12–19 October operational window (arrival 12 Oct, media day 13 Oct, group stage "
        "14–16 Oct, playoffs 17–18 Oct, departure 19 Oct). Media day 13 October is an organizer/team day and "
        "is not listed as a public event day on the ticket page."
    ),
    "source_url": EVENTBRITE,
    "confidence": "verified",
    "notes": (
        "Primary source read 11 October 2026: the official Eventbrite listing "
        f"{EVENTBRITE} , titled “Hotspawn present the Thunderpick World Championships 2026”, organizer Hotspawn, "
        "venue BLAST Arena Studios Malta, MFCC South Gate National Stadium, ATD 4000 Attard, dates "
        "Wednesday 14 – Sunday 18 October, 9:30 AM – 10 PM, highlights “4 days 12 hours”, “ages 18+”, “In person”. "
        "The same page carries a Google Maps transit link to coordinates 35.8957343, 14.4168839. "
        f"HLTV reports the free tickets and links to the same listing: {HLTV} . "
        f"Thunderpick’s own release names BLAST Studios Malta and gives 14–18 October: {PRN_RETURN} . "
        f"A second Thunderpick-issued release names the eight-team field and is datelined “TA’ QALI, Malta”: {PRN_FIELD} . "
        f"The organizer’s tournament page still lists the 12–19 October operational window: {TWC_OFFICIAL} . "
        "This record previously said the attendee pin, entrance, daily public times and ticket price were unconfirmed, "
        "and quoted a €10.00 ticket precedent from a separate BLAST-run event; the ticketing listing resolves the pin, "
        "the dates, three of the five daily schedules, and shows admission is free. Still open: the Saturday 17 and "
        "Sunday 18 agenda entries, the attendee gate inside the MFCC site, ticket availability and per-day scanning, "
        "parking, and on-site catering. See docs/OPEN_QUESTIONS.md."
    ),
})
append(acts, {
    "id": "twc-2026-free-tickets-18plus",
    "name": "TWC 2026 spectator tickets — free, 18+, reserve on Eventbrite",
    "category": "Tournament & trip-window events (13–19 Oct)",
    "area": "Ta’ Qali / Ħ’Attard",
    "address": VENUE_ADDRESS,
    "hours": EVENT_DAYS,
    "price range": "Free. HLTV reports the tickets are free and passes discount code MALTAESPORTS; no paid tier was shown on the listing.",
    "description": (
        "Public spectator attendance is available for the TWC 2026 finals. Tickets are free and reserved through "
        "the Eventbrite listing run by organizer Hotspawn. The listing flags “Sales end soon”, restricts entry to "
        "attendees aged 18+, and lists the confirmed teams Legacy, Falcons, FURIA, Betboom, 9z and Aurora with a "
        "“View all” control for the rest. Book before travelling; do not assume walk-in entry."
    ),
    "source_url": EVENTBRITE,
    "source_type": "official",
    "date_checked": TODAY,
    "confidence": "verified",
    "notes": (
        f"Read 11 October 2026: {EVENTBRITE} . Confirmed on that page: organizer Hotspawn; venue BLAST Arena Studios "
        "Malta, MFCC South Gate National Stadium, ATD 4000 Attard; dates Wednesday 14 – Sunday 18 October 2026; listed "
        "time 9:30 AM – 10 PM; highlights “ages 18+” and “In person”; a “Free / Reserve a spot” action; and a "
        "frequently-asked-questions list that includes “Is my ticket valid for every day of the event?”, "
        "“Will my ticket be scanned on each day?”, “Is parking available at the venue?” and “Will food and drink be "
        f"available at the venue?”. The answers to those questions are behind an interactive control and were not "
        f"readable in the extracted page. HLTV, 2 October 2026: {HLTV} . The eight-team field is also confirmed by "
        f"Thunderpick’s own release {PRN_FIELD} . Ticket inventory, transferability and per-day scanning remain "
        "unverified; the 18+ rule means the traveler must carry photographic ID."
    ),
})
amend_intro(activities,
      "Confirmed on 11 October 2026 from the event’s own ticketing listing: BLAST Arena Studios Malta, MFCC South Gate "
      "National Stadium, ATD 4000 Attard, 14–18 October 2026, free 18+ spectator tickets, with check-in/game times "
      "published for 14, 15 and 16 October; the 17 and 18 October agenda is not yet visible.")
save("activities.json", activities)

# ----------------------------------------------------------------- transport
transport = load("transport.json")
trs = transport["records"]
replace(trs, "twc-2026-venue-dates", {
    "address": VENUE_ADDRESS,
    "hours": EVENT_DAYS,
    "price range": "Free spectator tickets; transport is the cost. Event-day bus fares use the published seasonal single fare or a travel card.",
    "description": (
        "The attendee venue, dates and three of the five daily schedules are now confirmed from the event’s own "
        "ticketing page: BLAST Arena Studios Malta at MFCC South Gate National Stadium, Attard, 14–18 October 2026, "
        "doors 9:30 AM with the event running to 10:00–10:30 PM. This is the pin to enter in the Malta Public "
        "Transport planner; the organizer’s 12–19 October window includes non-public arrival and media days."
    ),
    "confidence": "verified",
    "notes": (
        f"Confirmed 11 October 2026 from the official ticketing listing {EVENTBRITE} : venue BLAST Arena Studios Malta, "
        "MFCC South Gate National Stadium, ATD 4000 Attard; map coordinates 35.8957343, 14.4168839; Wednesday 14 – "
        "Sunday 18 October; 9:30 AM – 10 PM; Wed 14 and Thu 15 check-in 09:30 / games 10:30 to 22:30; Fri 16 "
        "check-in 14:00 / games 15:00 to 21:00. Sat 17 and Sun 18 agenda entries were behind a “Show all agenda” "
        f"control and remain unconfirmed. Organizer window: {TWC_OFFICIAL} . Thunderpick release naming BLAST Studios "
        f"Malta: {PRN_RETURN} . Field announcement datelined TA’ QALI: {PRN_FIELD} . Earlier venue-area context from a "
        "separate BLAST event now matches the ticketed address, but the attendee gate inside the MFCC site is still "
        f"not published. Enter the address or the coordinates in {MPT_PLANNER} for each event date rather than relying "
        "on a route name."
    ),
})
amend(trs, "route-186-oct17-detour", "notes",
      "Independently re-read 11 October 2026 on " + MPT_UPDATES + " . The live notice reads: “Buses on Route 186 will be "
      "on detour. Detour in effect weekly on Friday, Saturday from 7:00 PM to 12:00 AM, starting October 17. Detour ends "
      "October 18 at approximately 12:00 AM. Toward Bugibba, stops from Gholja 2 through Targa will not be served.” "
      "Ambiguity to note: 17 October 2026 is a Saturday and the explicit end time is 18 October at approximately 12:00 AM "
      "(that is, midnight ending Saturday 17 October), yet the same sentence says the detour runs “weekly on Friday, "
      "Saturday”. Whether it also applies on Friday 16 October is therefore not clear from the text and must be checked "
      "with the operator or the planner. The notice also describes the Buġibba-bound direction only; it does not say "
      "whether the Ta’ Qali Stadium stops used by this trip are affected.")
amend(trs, "mpt-seasonal-fare-window-2026", "hours",
      "Applied to this trip: 13–18 October 2026 falls in the summer window (€2.50) and 19 October 2026 — the departure "
      "day — falls on the winter rate (€2.00). Because the page prints no explicit summer 2026 range, this is an "
      "inference from the published winter boundary and is kept at “partially verified”; confirm in the tallinja app on "
      "arrival.")
amend(trs, "mpt-seasonal-fare-window-2026", "price range",
      "Trip-specific reading: €2.50 per single day-route journey on 13–18 October 2026 and €2.00 on 19 October 2026 "
      "(inference, not a quoted range).")
append(trs, {
    "id": "event-day-late-finish-return-gap",
    "name": "The event outlasts the bus — plan a taxi or ride-hailing return",
    "category": "Event-day planning",
    "area": "BLAST Arena Studios (MFCC, Attard) → Qawra",
    "address": VENUE_ADDRESS,
    "hours": (
        "Conflict to plan around. The ticketing listing runs the event to 10:00–10:30 PM on the three days whose "
        "agenda is visible (14, 15 and 16 October). The last listed Route 186 departure from the Ta’ Qali Stadium "
        "area is 20:53, with a listed Buġibba Bay 1 arrival of 21:27, and the normal return runs via St Paul’s "
        "Bay/Buġibba rather than the Qawra seafront. Staying to the end of an event day therefore means no bus "
        "return."
    ),
    "price range": "Bus option €2.50 per single journey (summer table); the late return needs a live taxi or ride-hailing quote, which has not been obtained.",
    "description": (
        "This is the single most important transport finding for the trip. On 14, 15 and 16 October the event is "
        "listed until 22:00–22:30, which is later than the last published Route 186 departure from the Ta’ Qali "
        "Stadium area. Options: leave before the last bus, or book a taxi/ride-hailing return for the end of the "
        "night. On Saturday 17 October the Route 186 evening detour adds a further complication toward Buġibba. "
        "MPT’s night routes do not serve the event area, so get a live quote in Bolt, eCabs, Uber or Malta Taxi "
        "before you travel out."
    ),
    "source_url": EVENTBRITE,
    "source_type": "official",
    "date_checked": TODAY,
    "confidence": "verified",
    "notes": (
        "Derived by comparing two dated operator sources read on 11 October 2026. Event end time: the official "
        f"ticketing listing {EVENTBRITE} shows 09:30–22:30 on Wed 14 and Thu 15 October and 14:00–21:00 on Fri 16 "
        "October, under an overall header of 9:30 AM – 10 PM for 14–18 October. Bus end of service: the Route 186 "
        f"record in this dataset, from {MPT_186} , lists a last Stadium departure of 20:53 and a Buġibba Bay 1 "
        f"arrival of 21:27. Night routes: MPT’s own announcement {MPT_NIGHT} covers Buġibba (N212) and Valletta "
        "(N13) and does not list Ta’ Qali or Attard, so it is not a substitute for the event return. The Saturday 17 "
        f"October evening is additionally affected by the Route 186 detour published on {MPT_UPDATES} . "
        "What is NOT verified: a live taxi or ride-hailing fare for this journey, whether the organizer adds event "
        "shuttles, the Saturday 17 and Sunday 18 event finish times, and the walking route between the MFCC gate and "
        f"the nearest stop. Run each date through {MPT_PLANNER} and keep a live quote as the fallback."
    ),
})
amend_intro(transport,
      "Confirmed 11 October 2026: the attendee venue is BLAST Arena Studios Malta, MFCC South Gate National Stadium, "
      "ATD 4000 Attard, running 14–18 October with event days listed to 22:00–22:30. That outlasts the last listed bus "
      "departure from the Ta’ Qali Stadium area (20:53), so plan a taxi or ride-hailing return, or leave early.")
save("transport.json", transport)

# -------------------------------------------------------------------- radio
radio = load("radio.json")
rds = radio["records"]
replace(rds, "bbc-radio-5-live-premier-league-listings", {
    "hours": (
        "BBC times are UK local (BST, UTC+1); Malta is CEST (UTC+2), so add one hour. Sat 17 Oct: 14:45 BST "
        "Manchester City v Ipswich on 5 Sports Extra (15:45 Malta); 15:00 Brentford v Liverpool on 5 Live (16:00); "
        "17:30 Newcastle United v Aston Villa on 5 Live (18:30). Sun 18 Oct: 13:55 Brighton & Hove Albion v "
        "Crystal Palace on 5 Sports Extra (14:55); 14:00 Leeds United v Manchester United on 5 Live (15:00); 16:30 "
        "Nottingham Forest v Arsenal on 5 Live (17:30). Studio shows on 5 Live: Sat 17 12:00 (13:00 Malta), Sun 18 "
        "12:00 Premier League Sunday (13:00), Sun 18 16:00 pre-match for Forest v Arsenal (17:00), Mon 19 19:00 "
        "Monday Night Club (20:00 Malta)."
    ),
    "notes": (
        f"Re-read 11 October 2026 on the official BBC Premier League Football upcoming page {BBC_PL_UPCOMING} and the "
        f"5 Live Sport upcoming page {BBC_5LIVE_SPORT} . The upcoming page labels Manchester City v Ipswich Town and "
        "Brighton & Hove Albion v Crystal Palace as BBC Radio 5 Sports Extra, and the linked episode record for "
        f"17 October {BBC_EP_1710} also shows “Sat 17 Oct 2026 14:45 BBC Radio 5 Sports Extra” with a publication "
        "window of 2026-10-17T13:45:00+00:00 to 16:00:00+00:00 — so the service-label mismatch recorded earlier is "
        "resolved in favour of 5 Sports Extra. Brentford v Liverpool, Newcastle United v Aston Villa, Leeds United v "
        "Manchester United and Nottingham Forest v Arsenal are listed on BBC Radio 5 Live. These are UK schedules: no "
        "Maltese terrestrial frequency carries 5 Live or 5 Sports Extra in the WorldDAB Malta multiplex listings, and "
        "no BBC Sounds stream access from Malta was verified. Treat this as a fixture-and-commentary reference to "
        "pair with the over-the-air Malta options in this dataset, not as something receivable on an FM/DAB+ set at "
        "AX ODYCY."
    ),
})
replace(rds, "talksport-dab-6c-malta", {
    "name": "“Sports Channel” on Malta DAB+ — directory conflict on which block carries it",
    "hours": (
        "No programme schedule was found for this service, so no trip-week sports lineup can be stated. If it is the "
        "talkSPORT relay, its UK output would include the Saturday 12:30 Premier League commentary slot."
    ),
    "confidence": "partially verified",
    "notes": (
        "Read 11 October 2026. Two directories disagree on the block. WorldDAB’s Malta multiplex page "
        f"{WORLDDAB} lists a regular DAB+ service named “Sports Channel” on Digi B 2, transmitted on Band III 12A at "
        "223.936 MHz, and separately lists a third multiplex Digi B 3 on Band III 6C at 185.360 MHz without a Sports "
        f"Channel entry. The third-party directory Radio in Malta {RADIO_IN_MALTA} describes “Talk Sport · Sports "
        "coverage and sports talk · DAB+ (Labelled as Sports Channel) · Malta · talksport.com · United Kingdom "
        "(English)” and its 6C page places the service on 6C. So the service name is corroborated but the block is "
        "disputed, and the talkSPORT identification rests only on the third-party directory — not on a broadcaster or "
        f"rights-holder statement. TalkSPORT’s own schedule page {TALKSPORT_SCHEDULE} returned “Sorry, page "
        "unavailable” when checked, so no dated lineup could be confirmed. Action: scan a DAB+ receiver at AX ODYCY "
        "across both 12A and 6C for a service named “Sports Channel” and note the actual programme identity."
    ),
})
append(rds, {
    "id": "talksport-saturday-1230-epl-slot",
    "name": "talkSPORT’s Premier League commentary slots during the trip",
    "category": "UK radio schedule — Malta reception not verified",
    "area": "United Kingdom (national radio rights); Malta carriage unconfirmed",
    "address": "Not applicable — a UK national radio service",
    "hours": (
        "Rights-holder slot description, not a dated lineup: talkSPORT carries Premier League commentaries in the "
        "Saturday 12:30 window, Saturday after 19:30, Sunday at 12:00 or after 19:00, and Friday/Monday nights. In "
        "this trip that covers Sat 17 Oct 12:30 BST Everton v Chelsea (13:30 Malta) and Mon 19 Oct 20:00 BST Spurs v "
        "Coventry (21:00 Malta)."
    ),
    "price range": "Free to air on UK DAB/AM; online via the talkSPORT app and site. No Malta over-the-air carriage confirmed.",
    "description": (
        "talkSPORT is the other holder of UK national Premier League radio commentary rights alongside the BBC. Its "
        "published slot allocation puts the Saturday 12:30 kick-off and the Monday-night fixture with talkSPORT, "
        "which in this trip week means Everton v Chelsea on Saturday 17 October and Spurs v Coventry on Monday 19 "
        "October. Whether any of that is receivable on a radio in Malta is a separate, unverified question — see the "
        "“Sports Channel” DAB+ entry in this dataset."
    ),
    "source_url": GOAL_RADIO_RIGHTS,
    "source_type": "review",
    "date_checked": TODAY,
    "confidence": "partially verified",
    "notes": (
        f"Rights allocation table read 11 October 2026 at {GOAL_RADIO_RIGHTS} (dated 14 September 2026): "
        "“Package 2 · Saturday 12:30 · talkSPORT · 43 matches” and “Package 6 · Friday/Monday 19:30–20:00 and any "
        "displaced fixtures played midweek · talkSPORT · 68 matches”; the BBC holds Saturday 15:00, Saturday 17:30 "
        "and Sunday 16:30. Fixtures read 11 October 2026 from the Premier League’s own amended-schedule page "
        f"{EPL_FIXTURES} : Sat 17 Oct 12:30 Everton v Chelsea (TNT Sports on TV) and Mon 19 Oct 20:00 Tottenham v "
        "Coventry. This is a slot allocation plus a fixture list — it is not a confirmed commentary listing for "
        f"either match. TalkSPORT’s own schedule page {TALKSPORT_SCHEDULE} was unreachable (“Sorry, page "
        "unavailable”) when checked, so no dated lineup was verified. UK times are BST (UTC+1); Malta is CEST "
        "(UTC+2), so add one hour. No Malta frequency, Malta stream territory, or physical reception was established. "
        "Provenance note: goal.com is a commercial sports-media publisher, not the rights holder or the broadcaster; "
        "the record schema allows only official/map/review/social, so this secondary media summary is labelled "
        "“review” and the directly quoted fixture times come from the Premier League’s own page."
    ),
})
amend_intro(radio,
      "Refreshed 11 October 2026: BBC now lists named Premier League commentaries for 17–18 October on Radio 5 Live and "
      "5 Sports Extra, with the earlier service-label mismatch resolved; those remain UK schedules, not Malta reception.")
save("radio.json", radio)

# ------------------------------------------------------------------ everyday
everyday = load("everyday.json")
replace(everyday["records"], "october-weather-forecast", {
    "hours": (
        "Three dated snapshots read 11 October 2026. Met Office Valletta, covering the whole trip: 13 Oct sunny "
        "25/22°C; 14 Oct sunny 23/21; 15 Oct sunny 23/22; 16 Oct sunny 24/22; 17 Oct sunny 23/21; 18 Oct sunny "
        "intervals 23/21; 19 Oct sunny intervals 23/21. AccuWeather Qawra: 13 Oct morning rain then thunderstorms "
        "24/19; 14 Oct sunshine 24/17; 15 Oct mostly sunny 25/17; 16 Oct thunderstorms mainly early 24/17; 17 Oct a "
        "couple of afternoon showers 23/16. Malta Met Office 7-day view: 13 Oct isolated showers 26/19; 14 Oct mainly "
        "sunny 24/18; 15–16 Oct mainly sunny 25/17; 17 Oct mainly cloudy 23/18."
    ),
    "description": (
        "The Met Office Valletta view now reaches 19 October, so the whole stay is covered by one official source: "
        "mild and mostly dry, daytime highs around 23–25°C and night-time lows around 21–22°C. AccuWeather’s Qawra "
        "view is noticeably wetter for 13 and 16 October, and the Malta Met Office seven-day view stops at 17 "
        "October. All three are shown rather than reconciled silently. Recheck before outdoor and sea activities, "
        "and follow marine and lifeguard notices."
    ),
    "notes": (
        f"Met Office Valletta page read 11 October 2026: {METOFFICE_VALLETTA} . It lists 12–19 October 2026 "
        "day/night temperatures, labels the 18 and 19 October days as “BETA”, and its long-range section gives "
        "17 October highest 22–23°C / lowest 21–22°C and 18 October highest 23°C / lowest 20–22°C. This closes the "
        "earlier “18–19 October beyond the forecast” gap for planning purposes. The AccuWeather and Malta Met Office "
        "snapshots already recorded in this dataset are retained: they disagree on 13 October (isolated showers or "
        "thunderstorms versus sunny) and neither reaches 19 October. All three are dated forecasts, not observed "
        "conditions, and should be rechecked closer to departure."
    ),
})
save("everyday.json", everyday)

# ------------------------------------------------------------------ expenses
expenses = load("expenses.json")
replace(expenses["records"], "event-access", {
    "address": "BLAST Arena Studios Malta, MFCC South Gate National Stadium, ATD 4000 Attard, Malta — the address on the event’s own ticketing listing.",
    "hours": "Wednesday 14 – Sunday 18 October 2026, 9:30 AM – 10 PM. Check-in 09:30 and games 10:30 on 14 and 15 October; check-in 14:00 and games 15:00 on 16 October. Ages 18+.",
    "description": (
        "Free to attend, but still budget the hidden costs: a reservation is required, entry is 18+, and event days "
        "run later than the last bus, so a taxi or ride-hailing return is the realistic cost. Enter transport, food "
        "at the venue and any merchandise here; enter €0 for admission."
    ),
    "source_url": EVENTBRITE,
    "date_checked": TODAY,
    "confidence": "verified",
    "price range": "Free admission (“Free / Reserve a spot” on the listing). Budget the late-night return instead.",
    "notes": (
        "Confirmed 11 October 2026 from the event’s official ticketing listing "
        f"{EVENTBRITE} : organizer Hotspawn; venue BLAST Arena Studios Malta, MFCC South Gate National Stadium, ATD 4000 "
        "Attard; Wednesday 14 – Sunday 18 October 2026, 9:30 AM – 10 PM; highlights “ages 18+” and “In person”; a free "
        "“Reserve a spot” action. Free ticketing is also reported by HLTV: "
        f"{HLTV} . Organizer window and format: {TWC_OFFICIAL} . Thunderpick release naming BLAST Studios Malta: "
        f"{PRN_RETURN} . Still open, so do not budget against them as settled: the Sat 17 and Sun 18 agenda entries, "
        "whether one ticket covers all five days, venue parking, and on-site food and drink. This row replaces an "
        "earlier version that said spectator access was unconfirmed and quoted a €10.00 precedent from a separate "
        "BLAST-run event."
    ),
})
save("expenses.json", expenses)

print("data reconciled onto origin/main")
for name in ("activities", "transport", "radio", "everyday", "expenses", "food"):
    print(f"  {name}.json: {len(load(name + '.json')['records'])} records")
