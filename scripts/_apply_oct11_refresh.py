#!/usr/bin/env python3
"""One-off helper: apply the 11 October 2026 (second session) verified refresh.

Kept in scripts/ as a record of exactly which fields changed; not part of the
validator or the test suite.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"

SOURCES_ADDITION = """

## Second 11 October 2026 session — independent re-verification (UTC)

All rows below were fetched during this session. Each claim is limited exactly as described; nothing is transferred from a directory listing to on-location reception, admission or price.

| Claim / record | URL | Date accessed (UTC) | Workstream | Source type / limitation |
|---|---|---|---|---|
| Malta Public Transport official fare table: day routes €2.00 winter / €2.50 summer; night (N) €3.00; Special Services (S) €3.00; tallinja Direct (TD) €3.00; TD1 €3.50. Tickets cost the same in cash or by contactless card and are valid 2 hours with free transfers; a €50 fine applies without a valid ticket. | https://www.publictransport.com.mt/fares-and-tickets/ | 2026-10-11 | A — Transport | Official operator page read 11 Oct. The page states the winter fare of €2.00 applied from 19 Oct 2025 to 13 Jun 2026 and lists “Day Routes (Summer) €2.50”, but it does not print the 2026/27 winter start date, so the trip’s exact seasonal boundary is inferred from the operator’s own pattern only. |
| Malta Public Transport travel cards: 12 Single Day Journeys €19 (shareable; night routes and Airport Direct consume two journeys; six-month validity); Explore Adult 7-day €25 (unlimited day/night routes and select Special Services, excludes tallinja Direct; individual use); Explore Child 7-day €7 (ages 4–10; under 4 free); Explore Flex 4-day €21 / 7-day €27; Explore Flex sightseeing bundles 4-day/7-day €36/€42 (Gozo Highspeed return or Harbour Cruise), €53/€59 (2 Islands; Golden Comino summer only), €68/€74 (both), €41/€51 (Hop-On Hop-Off); €6 for two Airport Direct trips as an Explore Flex add-on. | https://www.publictransport.com.mt/fares-and-tickets/ | 2026-10-11 | A — Transport | Official operator page read 11 Oct. Card terms are as published; the page’s own text notes TD routes are excluded from the 7-day unlimited benefit and that TD1 costs €3.50 per journey. |
| Malta Public Transport sales points include offices inside the Welcomer’s Hall and at Baggage Reclaim at Malta International Airport, the Valletta Terminal, the Buġibba Terminal and Sliema Ferries, plus card-dispensing machines in tourist areas and retail outlets such as Agenda, 8TillLate and WH Smith. | https://www.publictransport.com.mt/office-and-ticket-machine/ | 2026-10-11 | A — Transport | Official operator page linked from the fare page read 11 Oct. Buġibba Terminal is the closest listed card-sales office to the Qawra base; opening hours were not verified. |
| BLAST’s Malta studio is described by the organizer’s own event partner as a 1,000 m² studio and operations centre in Ta’ Qali, opened in 2025 under a three-year GamingMalta agreement covering nine events; BLAST-run events there sell tickets with a live studio audience (BLAST Slam VI, Feb 2026 “LAN Playoffs (with studio audience)”; BLAST Premier Bounty Malta, July 2026, tickets from €10.00). | https://eventworks.mt/blog/blast-slam-viii-malta-dota-2-october-2026 | 2026-10-11 | A/C — Transport & Activities | EventWorks is BLAST’s Malta ticketing partner; page read 11 Oct. This is venue-capability precedent for organizer-run events, not evidence that the Thunderpick Finals (operated by GAM3RS_X) sells tickets or admits the public. |
| BLAST studio base in Ta’ Qali reported by Times of Malta: three-year deal for nine major esports events plus an operations centre in Ta’ Qali. | https://timesofmalta.com/article/danish-esports-brand-blast-sets-base-ta-qali.1114836 | 2026-10-11 | A — Transport | National newspaper report read 11 Oct; corroborates the studio’s Ta’ Qali location, not event admission. |
| Independent esports press describes the Thunderpick World Championship 2026 as scheduled for October 14–18 at the BLAST Arena studio, Malta, with two GSL groups and a single-elimination playoff; all matches Bo3 except the Bo5 grand final. | https://www.hltv.org/news/45525/falcons-and-furia-headline-thunderpick-world-championship-team-list | 2026-10-11 | A/C — Transport & Activities | Professional esports outlet, not the organizer. Repeats the 14–18 Oct window and venue; says nothing about public tickets or doors. |
| Thunderpick states the five-day Finals will be broadcast live on its Twitch, Kick and YouTube channels. | https://esportsbrief.substack.com/p/thunderpick-world-championship-2026-return | 2026-10-11 | C — Activities | Secondary report quoting Thunderpick (13 Aug 2026); used only to show a broadcast alternative exists, not as an admission or rights statement. Companion coverage: https://g3newswire.com/thunderpick-world-championship-returns-to-malta-with-1m-prize-pool/ |
| No public ticket sale or spectator policy for the Thunderpick World Championship 2026 Finals was found in the checks completed for this session, including the official event page, the Thunderpick release and an esports event directory that lists the tournament without a ticket link. | https://visitesports.com/locations/mt/malta | 2026-10-11 | A — Transport | Third-party directory read 11 Oct. Absence of a ticket listing is not proof that no tickets exist; treat attendee access as unconfirmed and ask the organizer. |
| Uber publishes a Malta International Airport page that says taxis are not available for airport rides there and directs riders to UberX instead, quoting an average €20 fare for rides of about 19 minutes from MLA; two 2026 third-party guides state that Uber does not operate in Malta and recommend Bolt or eCabs. | https://www.uber.com/global/en/r/airports/mla/taxi/ | 2026-10-11 | A — Transport | Operator page plus conflicting guides: https://www.malta-spirit.com/guides/taxis-bolt-and-ride-share-malta/ and https://hubpymalta.com/what-to-do/malta-airport-guide.html. The conflict is recorded, not resolved; confirm in the app. UberX availability, coverage and quote for Qawra–Ta’ Qali remain unverified. |
| Bolt is described in Maltese national media as the leading ride-hailing platform operating in Malta, with the app now available in Maltese; Bolt publishes Malta service and airport pickup pages. | https://timesofmalta.com/article/bolt-becomes-first-ridehailing-app-available-maltese.1117399 | 2026-10-11 | A — Transport | Newspaper report of the provider’s own announcement (Oct 2025), used to corroborate that Bolt operates in Malta; no fare or availability promise. |
| talkSPORT is carried on Malta DAB+ block 6C at 185.360 MHz under the service label “Sports Channel (Talk Sport)”; WorldDAB’s Malta multiplex table lists a “Sports Channel” DAB+ service on the Digi B multiplex alongside Capital FM, Jazz FM and LBC 97.3, and Wikipedia’s talkSPORT article lists “DAB+: 6C (Malta)” among the station’s frequencies. talkSPORT is an official English Premier League audio broadcaster and the league’s global audio partner. | https://radioinmalta.com/en/dab/6c.php | 2026-10-11 | E — Radio sports | Specialist directory (Radio in Malta) read 11 Oct with corroboration from https://www.worlddab.org/countries/malta/multiplexes and https://en.wikipedia.org/wiki/Talksport. What the Malta relay actually carries (live match commentary versus talk-only output), its rights scope and indoor reception at Qawra are NOT verified. Treat as the highest-priority receiver scan target, not as confirmed commentary. |
| Malta DAB+ block 6A (181.936 MHz, allotment MLT00017, on air since July 2008, transmitter sites Għargħur 10 kW and Żebbuġ Gozo) carries, among others: BBC World Service, Rai Radio Uno/Due/Tre, Net FM, Vibe HD, Radju Malta 1, ONE Radio, RTK, Radju Marija, Campus FM, All 80s/Groove/Rock, Bay 89.7, Bay Easy, Classic Choice, Galaxy, Ignited Radio, Radio Deejay, RTL 102.5, Voice of America. | https://radioinmalta.com/en/dab/6a.php | 2026-10-11 | E — Radio sports | Specialist technical directory read 11 Oct. Station list and block data are published directory entries, not a measured scan at Qawra or Ta’ Qali. |
| Malta’s DAB+ multiplexes are operated by Digi B Network on blocks 6A, 6C and 12A with national coverage; the 6C station list (185.360 MHz, allotment MLT00018) also includes Capital (London), Gold (UK), Smooth Radio (UK), LBC 97.3, Jazz FM, XFM Malta, Radio Italia, Radio Margherita, EWTN, Vatican Radio, Opera Channel, All Country, All Dance HD and Magic Malta (HD). | https://radioinmalta.com/en/dab/6c.php | 2026-10-11 | E — Radio sports | Corroborated by https://www.worlddab.org/countries/malta and the MCA’s DAB+ consultation table of block frequency ranges: https://www.mca.org.mt/sites/default/files/MCA-C-21-4261%20-%20DAB%20Plus%20Consultation_0.pdf . Directory evidence only. |
| Vibe FM is published as the official radio partner of the Malta Premier League (360 Sports / YoHealth Malta Premier) and distributes via FM 88.7, DAB+ and online; its league page carries matchday roundups rather than a listed live-commentary schedule. | https://vibe.mt/maltapremier/ | 2026-10-11 | E — Radio sports | Station’s own page read 11 Oct. Domestic-league partnership is stated; live commentary of a named match was not verified, and the frequency comes from the Broadcasting Authority list at https://ba.org.mt/stations-licenced . |
| Kalshi’s own help centre says trading from outside the United States is possible from many countries and that a customer may use the platform while travelling abroad, subject to the Member Agreement and geographic requirements; third-party guides conflict, one stating that access is restricted to US residents who pass KYC and warning of temporary geo-blocking while travelling. | https://help.kalshi.com/en/articles/14026044-can-i-trade-on-kalshi-from-outside-the-united-states | 2026-10-11 | E — Radio sports | Kalshi help-centre page read 11 Oct (undated). Conflicting guidance: https://tech-insider.org/prediction-markets/how-to-trade-on-kalshi/ . Kalshi is a CFTC-designated contract market: https://www.predictionmarket.tools/is-kalshi-legal . Eligibility remains account- and product-specific; confirm with Kalshi support before relying on it in Malta. |
| Malta uses Type G (British three-pin) sockets at 230 V / 50 Hz; a US Type A/B plug needs an adapter, and single-voltage high-wattage appliances (for example hair dryers) also need a converter because a plug adapter does not change voltage. Dual-voltage devices marked 100–240 V 50/60 Hz need only the adapter. | https://www.power-plugs-sockets.com/us/malta/ | 2026-10-11 | D — Everyday | Two independent travel-reference pages read 11 Oct (also https://www.checkplug.com/usa-to-malta). Consumer reference pages, not the Maltese regulator; the voltage/frequency/plug-type trio is consistent across both and with the Government of Malta overview already logged. |
| Malta Tourism Authority guidelines (document issued for the 1 July 2026 change): the eco-contribution is €1.50 per night for each guest aged 18 or over at the start of the visit, capped at €22.50 per person per visit; a “visit” is an uninterrupted stay in one or more licensable properties; the amount must be disclosed separately from accommodation fees on a fiscal receipt; the cap is reduced on later stays when evidence of earlier contributions is retained. The separate text saying the reporting obligation applies only to stays exceeding 15 nights explains the €22.50 cap (15 nights × €1.50) rather than exempting short stays. | https://mta.com.mt/docs/Eco-Contribution-Accommodation-Guidelines-2026.pdf | 2026-10-11 | D — Everyday | Official MTA guidelines PDF read 11 Oct. Applies to licensable accommodation; the actual charge on this booking still depends on the hotel invoice and guest ages. See OQ-25. |
| Dated long-range outlook snapshots for the trip window: AccuWeather’s Qawra October 2026 monthly page shows 13 Oct “morning rain, then thunderstorms” 75/66 °F, 14 Oct sunshine 76/63 °F, 15 Oct mostly sunny 77/62 °F, 16 Oct “thunderstorms, mainly early” 76/62 °F, 17 Oct “a couple of afternoon showers” 74/61 °F; timeanddate’s Qawra two-week table shows 13–15 Oct sunny to mostly sunny, 16 Oct sprinkles late/overcast, 17 Oct mostly sunny. | https://www.accuweather.com/en/mt/qawra/233869/october-weather/233869 | 2026-10-11 | D — Everyday | Two commercial forecast providers read 11 Oct; their 13 October entries disagree, which is itself the point. Monthly/2-week outlooks change and are not a substitute for the daily Malta Met Office forecast. Second source: https://www.timeanddate.com/weather/@2562641 |
"""


def load(name: str) -> dict:
    return json.loads((DATA / name).read_text(encoding="utf-8"))


def save(name: str, payload: dict) -> None:
    (DATA / name).write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


def find(payload: dict, record_id: str) -> dict:
    for record in payload["records"]:
        if record["id"] == record_id:
            return record
    raise SystemExit(f"record not found: {record_id}")


def upsert(payload: dict, record: dict, after: str | None = None) -> None:
    for index, existing in enumerate(payload["records"]):
        if existing["id"] == record["id"]:
            payload["records"][index] = record
            return
    if after is None:
        payload["records"].append(record)
        return
    for index, existing in enumerate(payload["records"]):
        if existing["id"] == after:
            payload["records"].insert(index + 1, record)
            return
    payload["records"].append(record)


# ---------------------------------------------------------------- transport
transport = load("transport.json")
transport["last_updated"] = "2026-10-11"
transport["intro"] = (
    "Start with the organizer’s actual attendee location and daily finish time. Route 186 and Route 214 are "
    "public-bus candidates between Qawra and Ta’ Qali, not confirmed hotel-to-entrance journeys. Malta Public "
    "Transport’s published fares were read directly on 11 October 2026 (single day-route journeys €2.50 in the "
    "summer window / €2.00 in winter, €3.00 night and Tallinja Direct, €3.50 on TD1, €19 for 12 journeys, €25 for "
    "the 7-day Explore Adult card), and travel cards can be bought at the Buġibba Terminal. Ticket-holder access "
    "to the Thunderpick Finals is still unconfirmed; use the date-specific planner for both directions and keep a "
    "live-quote taxi fallback, especially for the 17 October evening diversion."
)

venue = find(transport, "twc-2026-venue-dates")
venue["hours"] = (
    "Official TWC page lists the overall event window 12–19 October 2026: arrival 12 October, media day 13 October, "
    "Group Stage 14–16 October, Playoffs 17–18 October, departure 19 October. It does not publish daily public "
    "match/door times, ticket sales or attendee instructions. Independent esports press repeats a 14–18 October "
    "competition window at the BLAST Arena studio."
)
venue["description"] = (
    "The official Thunderpick page confirms the phase dates and Malta as the location; a Thunderpick-issued release "
    "names BLAST Studios Malta, and independent esports press places the tournament at the BLAST Arena studio in "
    "Ta’ Qali, Attard. BLAST’s Malta ticketing partner describes a 1,000 m² studio in Ta’ Qali that hosts ticketed "
    "events with a live studio audience for BLAST-run tournaments — precedent only, because this event is operated "
    "by GAM3RS_X. No public ticket sale or spectator policy for these Finals was found on 11 October 2026, so "
    "attendee access is unconfirmed rather than refused."
)
venue["notes"] = (
    "The official Thunderpick page was rechecked 11 October 2026. Thunderpick’s announcement names BLAST Studios "
    "Malta: https://www.prnewswire.com/news-releases/thunderpick-world-championship-2026-returns-to-malta-with-1-million-prize-pool-302850221.html . "
    "BLAST’s attendee guide is for a previous, separate event and gives the MFCC address: "
    "https://blast.tv/cs/news/malta-fan-guide . Neither confirms the TWC attendee pin, attendee entrance, tickets, "
    "or exact daily match/door times. Do not transfer earlier BLAST event access rules. Official 9 October X post "
    "points to an opening-day schedule, but its attached image was not readable in extracted text; no match times "
    "inferred: https://x.com/thunderpickco/status/2108604711968317828 . Re-read 11 October 2026: EventWorks, "
    "BLAST’s Malta ticketing partner, lists BLAST Arena Studios Malta at MFCC South Gate National Stadium, "
    "Millennium Stand, Attard ATD 4000 and sells studio-audience tickets for BLAST-run events (from €10.00 for the "
    "July 2026 BLAST Premier Bounty): https://eventworks.mt/premier-bounty-presented-by-polymarket ; it also "
    "describes the studio as 1,000 m² in Ta’ Qali: "
    "https://eventworks.mt/blog/blast-slam-viii-malta-dota-2-october-2026 . Times of Malta reported BLAST’s "
    "three-year, nine-event Ta’ Qali base: "
    "https://timesofmalta.com/article/danish-esports-brand-blast-sets-base-ta-qali.1114836 . HLTV independently "
    "places the tournament on 14–18 October at the BLAST Arena studio: "
    "https://www.hltv.org/news/45525/falcons-and-furia-headline-thunderpick-world-championship-team-list . "
    "Thunderpick says all matches will be broadcast live on its Twitch, Kick and YouTube channels: "
    "https://esportsbrief.substack.com/p/thunderpick-world-championship-2026-return and "
    "https://g3newswire.com/thunderpick-world-championship-returns-to-malta-with-1m-prize-pool/ . An esports event "
    "directory lists the tournament with dates but no ticket link: https://visitesports.com/locations/mt/malta . "
    "Absence of a ticket listing is not proof that none exists — confirm with the organizer before travelling."
)
venue["price range"] = (
    "Spectator ticket price/access not verified — no public sale found; BLAST-run events at the same studio sold "
    "tickets from €10.00 (July 2026 precedent only)"
)

fare_record = find(transport, "mpt-fares-cards")
fare_record["name"] = "Bus fares, travel cards and where to buy them"
fare_record["hours"] = (
    "Published fare table read 11 October 2026: day routes €2.50 summer / €2.00 winter per single journey; night "
    "routes (N) €3.00; Special Services (S) €3.00; tallinja Direct (TD) €3.00; TD1 €3.50. Singles are valid two "
    "hours with free transfers, cost the same in cash or by contactless card, and a €50 fine applies without a "
    "valid ticket. Travel cards: 12 Single Day Journeys €19 (shareable; night/Airport Direct consume two journeys; "
    "valid six months from first use); Explore Adult 7-day €25 (day and night routes plus select Special Services, "
    "excludes Tallinja Direct; individual use); Explore Child 7-day €7 (ages 4–10; under 4 travel free); Explore "
    "Flex 4-day €21 / 7-day €27; Explore Flex sightseeing bundles €36–€74 depending on days and inclusions."
)
fare_record["description"] = (
    "Malta Public Transport’s own fare page was read on 11 October 2026, replacing the earlier inference from "
    "third-party summaries. Every published tourist ticket type is now recorded with the operator as the source, "
    "including the two-hour transfer window, the €50 no-valid-ticket fine and the sales channels. The page states "
    "that the €2.00 winter fare applied from 19 October 2025 to 13 June 2026 and lists the summer day-route fare as "
    "€2.50, but it does not print the 2026/27 winter start date, so the exact seasonal boundary for the trip is "
    "recorded separately as an open item."
)
fare_record["price range"] = (
    "Official operator fares: single day route €2.50 summer / €2.00 winter; night, Special Services and Tallinja "
    "Direct €3.00; TD1 €3.50; 12 Single Day Journeys €19; Explore Adult 7-day €25; Explore Child 7-day €7; Explore "
    "Flex 4-day €21 / 7-day €27"
)
fare_record["notes"] = (
    "Official fare table and travel-card terms read 11 October 2026: "
    "https://www.publictransport.com.mt/fares-and-tickets/ . Sales offices and card machines: "
    "https://www.publictransport.com.mt/office-and-ticket-machine/ . The same page states the €2.00 winter fare "
    "applied 19 October 2025 – 13 June 2026 and lists a separate summer day-route fare of €2.50; it does not state "
    "the 2026/27 winter start date. Card conditions as published: the 7-day Explore Adult card is individual and "
    "excludes tallinja Direct routes; the 12-journey card is shareable. Recheck the day before travel, because "
    "seasonal prices and card inclusions change."
)

upsert(
    transport,
    {
        "id": "mpt-seasonal-fare-window-2026",
        "name": "Which single-journey fare applies during 13–19 October 2026",
        "category": "Bus fares",
        "area": "Malta and Gozo",
        "address": "Not applicable — fare rules",
        "hours": (
            "Malta Public Transport’s fare page read 11 October 2026 lists day-route singles at €2.50 (summer) and "
            "€2.00 (winter) and states that the €2.00 winter fare applied from 19 October 2025 to 13 June 2026. It "
            "does not print the start date of the 2026/27 winter period."
        ),
        "description": (
            "The trip runs 13–19 October 2026. On the operator’s own pattern the cheaper winter single begins after "
            "19 October, so the higher summer single price is the planning figure to budget for this trip; the "
            "operator’s page does not state the 2026/27 changeover date, so this remains a planning inference, not "
            "a published trip-week fare. Budget either way with the day-route single (€2.50), or buy a travel card, "
            "which removes the uncertainty for a multi-day stay."
        ),
        "source_url": "https://www.publictransport.com.mt/fares-and-tickets/",
        "source_type": "official",
        "date_checked": "2026-10-11",
        "confidence": "partially verified",
        "notes": (
            "Evidence: the official fare table and the sentence “With effect from 19 October 2025 to 13 June 2026, "
            "the winter fare of €2.00 … applies”: https://www.publictransport.com.mt/fares-and-tickets/ . The trip "
            "window (13–19 October) sits inside a period the operator prices as summer on its own published table, "
            "but no 2026/27 winter start date is printed, and third-party guides that assert specific changeover "
            "dates are not operator sources and were not adopted. Resolve by rechecking the operator page or the "
            "tallinja app immediately before travel."
        ),
        "price range": (
            "Planning figure €2.50 per single day-route journey during the trip; €2.00 winter rate expected to "
            "resume after 19 October 2026 (not published on the checked page)"
        ),
    },
    after="mpt-fares-cards",
)

upsert(
    transport,
    {
        "id": "mpt-card-sales-points",
        "name": "Where to buy bus tickets and travel cards near Qawra",
        "category": "Bus fares",
        "area": "Malta International Airport, Valletta, Buġibba (Qawra side) and Sliema",
        "address": (
            "Sales offices: Welcomer’s Hall and Baggage Reclaim, Malta International Airport; Valletta Terminal; "
            "Buġibba Terminal; Sliema Ferries. Card-dispensing machines in tourist areas and retail outlets such as "
            "Agenda, 8TillLate and WH Smith."
        ),
        "hours": (
            "Not published on the checked pages; office opening hours were not verified. On-bus purchase is always "
            "possible with cash or a contactless bank card or phone."
        ),
        "description": (
            "The operator lists the Buġibba Terminal as a travel-card sales office, which is the closest listed "
            "sales point to the AX ODYCY base in Qawra, and also sells cards at the airport on arrival and at "
            "Valletta Terminal and Sliema Ferries. Buying on board is possible for single journeys; cards are the "
            "cheaper option for a six-night stay with repeated event travel and sightseeing."
        ),
        "source_url": "https://www.publictransport.com.mt/office-and-ticket-machine/",
        "source_type": "official",
        "date_checked": "2026-10-11",
        "confidence": "partially verified",
        "notes": (
            "Sales-point list linked from the official fare page read 11 October 2026: "
            "https://www.publictransport.com.mt/fares-and-tickets/ and "
            "https://www.publictransport.com.mt/office-and-ticket-machine/ . Retail-outlet names are the operator’s "
            "own examples. Buġibba Terminal was not visited and its office hours, stock and payment methods were "
            "not verified; airport offices are in the Welcomer’s Hall and at Baggage Reclaim."
        ),
        "price range": (
            "Cards as published: 12 Single Day Journeys €19; Explore Adult 7-day €25; Explore Child 7-day €7; "
            "Explore Flex 4-day €21 / 7-day €27; single on-bus journeys €2.50 summer / €2.00 winter"
        ),
    },
    after="mpt-seasonal-fare-window-2026",
)

route186 = find(transport, "qawra-taqali-route-186")
route186["price range"] = (
    "Regular day-route single fare: €2.50 in the operator’s summer table, €2.00 winter (2-hour validity with free "
    "transfers); covered by the Explore Adult 7-day card (€25) but not by the 7-day Explore card on tallinja Direct "
    "routes"
)
route186["notes"] = (
    route186["notes"]
    + " Fare context added 11 October 2026 from the operator’s published table: "
    "https://www.publictransport.com.mt/fares-and-tickets/ . Route 186 is a day route, so a single journey costs "
    "the day-route price (€2.50 summer planning figure) and is included in the 7-day Explore Adult card; travel "
    "cards can be bought at the Buġibba Terminal, the closest listed sales office to Qawra: "
    "https://www.publictransport.com.mt/office-and-ticket-machine/ ."
)

route214 = find(transport, "qawra-taqali-route-214-alternative")
route214["price range"] = "Regular day-route single fare: €2.50 (summer table) / €2.00 winter; included in the 7-day Explore Adult card (€25)"

td1 = find(transport, "airport-direct-td1-qawra")
td1["notes"] = (
    td1["notes"]
    + " Fare context re-verified 11 October 2026 against the operator’s own table, which lists Tallinja Direct "
    "routes at €3.00 and TD1 at €3.50: https://www.publictransport.com.mt/fares-and-tickets/ . The same page "
    "states that the 7-day Explore Adult card excludes tallinja Direct routes, while the 12 Single Day Journeys "
    "card may be used on the Airport Direct service at a cost of two journeys per trip."
)
if "€3.50" not in td1["price range"]:
    td1["price range"] = "€3.50 per passenger on TD1; cash or contactless onboard; not covered by the 7-day Explore card"

uber = find(transport, "uber-malta")
uber["name"] = "Ride-hailing in Malta — Bolt, eCabs and the conflicting Uber status"
uber["category"] = "On-demand transport"
uber["area"] = "Malta (provider pages and two conflicting 2026 guides); coverage in Qawra and at the Ta’ Qali venue not verified"
uber["hours"] = "App-based, on demand; provider pages describe 24/7 requesting but no trip-time availability or waiting time was verified."
uber["description"] = (
    "Two ride-hailing providers are documented as operating in Malta: Bolt, described in Maltese national media as "
    "the leading ride-hailing platform on the islands and offering English-language service through its Malta "
    "pages, and eCabs, a long-standing Maltese operator with pre-booking. Uber’s position is contradictory in the "
    "sources checked on 11 October 2026: Uber publishes a Malta airport page that mentions UberX rides with an "
    "average €20 fare for roughly 19-minute trips from MLA, while two 2026 third-party guides state that Uber does "
    "not operate in Malta. Treat Bolt and eCabs as the reliable options, confirm Uber in the app on arrival, and "
    "never accept an unlicensed driver approaching inside the terminal."
)
uber["source_url"] = "https://www.uber.com/global/en/r/airports/mla/taxi/"
uber["date_checked"] = "2026-10-11"
uber["notes"] = (
    "Uber’s Malta airport page read 11 October 2026: https://www.uber.com/global/en/r/airports/mla/taxi/ (it says "
    "taxis are not available for MLA rides and points riders to UberX, quoting an average €20 for a 19-minute "
    "trip). Conflicting third-party guides also read 11 October 2026: "
    "https://www.malta-spirit.com/guides/taxis-bolt-and-ride-share-malta/ and "
    "https://hubpymalta.com/what-to-do/malta-airport-guide.html (both say Uber does not operate in Malta). Bolt’s "
    "presence in Malta is reported by Times of Malta: "
    "https://timesofmalta.com/article/bolt-becomes-first-ridehailing-app-available-maltese.1117399 , with provider "
    "pages at https://bolt.eu/en/cities/malta/ and https://bolt.eu/en/airports/mla/ . eCabs: https://ecabs.com.mt/ . "
    "No Qawra–Ta’ Qali quote, event-night supply, pickup point or waiting time was verified for any provider; "
    "compare live quotes and keep the bus as the priced fallback."
)
uber["price range"] = (
    "Live in-app quotes only: Uber’s own page quotes about €20 for an average 19-minute UberX trip from MLA; "
    "no Qawra–Ta’ Qali or event-night price verified, and third-party airport-to-Buġibba estimates (roughly "
    "€25–€35) are guide figures, not quotes"
)

mode = find(transport, "mode-comparison-summary")
mode["price range"] = (
    "Verified operator prices for budgeting: day-route single €2.50 summer / €2.00 winter (2-hour transfers); "
    "night, Special Services and Tallinja Direct €3.00; TD1 €3.50; 12 Single Day Journeys €19; Explore Adult "
    "7-day €25; Explore Child €7; Explore Flex 4-day €21 / 7-day €27; €50 fine without a valid ticket. "
    "Taxi/ride-hailing and car hire need live quotes; ferry fares depend on route."
)
mode["description"] = (
    "Convenience, price, value and feasibility compared for the Qawra base: public buses are the only fully "
    "publicly priced mode, and on 11 October 2026 the operator’s own fare table, card terms and sales points were "
    "read directly so the planner can use exact figures instead of inferred ones. Route 186 connects Qawra to "
    "Ta’ Qali with a return via Buġibba; taxis and ride-hailing are door-to-door but unquoted; a rental car only "
    "makes sense if the traveler accepts left-side driving, insurance excess and unverified venue parking. The "
    "unresolved variables are the confirmed TWC access/entrance, the daily finish time and the 17 October evening "
    "diversion."
)
mode["notes"] = (
    mode["notes"]
    + " Repriced 11 October 2026 from the operator’s published table and card terms: "
    "https://www.publictransport.com.mt/fares-and-tickets/ . The same page confirms the two-hour transfer window, "
    "the excluded tallinja Direct routes from the 7-day Explore card, and the €50 fine for travelling without a "
    "valid ticket."
)
mode["date_checked"] = "2026-10-11"

save("transport.json", transport)

# ------------------------------------------------------------------- radio
radio = load("radio.json")
radio["last_updated"] = "2026-10-11"
radio["intro"] = (
    "Radio snapshot for 13–19 October 2026. The clearest English-language sports lead is talkSPORT, carried on "
    "Malta DAB+ block 6C (185.360 MHz) under the service label “Sports Channel (Talk Sport)”: talkSPORT is an "
    "official Premier League audio broadcaster, so this is the first receiver scan to try on 17–18 October 2026. "
    "What the Malta relay actually carries, and its indoor reception, are unverified. Malta’s block 6A carries BBC "
    "World Service (Sportsworld, dated 17–18 October episodes, general live sport) plus Rai Radio Uno/Due/Tre, NET "
    "FM and Vibe HD; Vibe FM is the published radio partner of the Malta Premier League. The six BBC Radio 5 Live "
    "and 5 Sports Extra Premier League episode records remain UK-only schedule evidence. Kalshi’s own help centre "
    "says trading from many countries and while travelling abroad is possible subject to its Member Agreement, "
    "while third-party guidance conflicts; eligibility stays account-specific. No named-event carriage was "
    "verified."
)

sports_channel = find(radio, "worlddab-sports-channel-lead")
sports_channel["id"] = "talksport-dab-6c-malta"
sports_channel["name"] = "talkSPORT — Malta DAB+ block 6C (service label “Sports Channel”)"
sports_channel["category"] = "DAB+"
sports_channel["area"] = (
    "Malta DAB+ block 6C (185.360 MHz) under the Digi B multiplex; reception at AX ODYCY and the Ta’ Qali venue not tested"
)
sports_channel["address"] = "Not applicable — broadcast service; tune by service name “Sports Channel” on block 6C"
sports_channel["hours"] = (
    "No dated Malta trip-week schedule was published in the sources checked. talkSPORT’s UK output carries live "
    "Premier League commentary and around-the-clock sports talk; the relay’s own schedule could not be read remotely."
)
sports_channel["description"] = (
    "Three independent listings agree that a sports service is carried on Malta DAB+ block 6C: the specialist "
    "Radio in Malta directory names it “Sports Channel (Talk Sport)”, WorldDAB’s Malta multiplex table lists a "
    "“Sports Channel” DAB+ service on the Digi B multiplex, and Wikipedia’s talkSPORT article lists “DAB+: 6C "
    "(Malta)” among the station’s frequencies. talkSPORT is an official English Premier League audio broadcaster "
    "and the league’s global audio partner, which makes the 6C service the single most promising lead for English "
    "live football commentary on a radio in Malta during the 17–18 October fixture window. The unresolved step is "
    "what the Malta relay actually transmits: it could carry talkSPORT’s live match commentary or only its "
    "talk/analysis output, and rights scopes differ between the UK and international feeds. Scan block 6C first "
    "and confirm with the broadcast content itself."
)
sports_channel["source_url"] = "https://radioinmalta.com/en/dab/6c.php"
sports_channel["date_checked"] = "2026-10-11"
sports_channel["notes"] = (
    "Read 11 October 2026: Radio in Malta’s 6C station list gives frequency 185.360 MHz, allotment MLT00018, on "
    "air since 2012, and lists “Sports Channel (Talk Sport)” at 32 kbps HE-AAC v2 alongside Capital (London), Gold "
    "(UK), Smooth Radio (UK), LBC 97.3, Jazz FM, XFM Malta, Opera Channel, EWTN, Vatican Radio, Radio Italia, Radio "
    "Margherita, All Country, All Dance HD and Magic Malta (HD): https://radioinmalta.com/en/dab/6c.php . WorldDAB’s "
    "Malta multiplex page lists a “Sports Channel” regular DAB+ service: "
    "https://www.worlddab.org/countries/malta/multiplexes . Wikipedia’s talkSPORT article lists the station’s "
    "DAB+ frequency for Malta as 6C: https://en.wikipedia.org/wiki/Talksport . Malta’s three DAB+ blocks (6A, 6C, "
    "12A) are operated by Digi B Network: https://www.worlddab.org/countries/malta and the MCA DAB+ consultation "
    "table ::: https://www.mca.org.mt/sites/default/files/MCA-C-21-4261%20-%20DAB%20Plus%20Consultation_0.pdf . "
    "Limitations: these are directory entries, not an operator schedule; the label is “Sports Channel” rather than "
    "the station name on some receivers; the 32 kbps bit rate is the directory’s figure; and no reception test or "
    "rights confirmation was possible. Do not present this as guaranteed live Premier League commentary — verify "
    "on a receiver in Malta."
)
sports_channel["price range"] = "Free-to-air if broadcast; DAB+ receiver required (hardware price not checked)"

upsert(
    radio,
    {
        "id": "malta-dab-plus-tuning-guide",
        "name": "Malta DAB+ tuning guide — blocks 6A, 6C and 12A",
        "category": "DAB+",
        "area": "Malta and Gozo (national Digi B multiplexes); indoor reception varies by building",
        "address": "Not applicable — technical tuning data; scan by service name on a DAB+ receiver",
        "hours": (
            "Not a schedule. Published block data: 6A 181.936 MHz (allotment MLT00017, on air since July 2008, "
            "transmitters Għargħur 10 kW and Żebbuġ, Gozo); 6C 185.360 MHz (allotment MLT00018, on air since 2012); "
            "12A 223.936 MHz (Digi B 2)."
        ),
        "description": (
            "Malta has used DAB+ (not older DAB) since 2008, with national coverage from the Digi B Network "
            "multiplexes on blocks 6A, 6C and 12A, so a DAB+-compatible receiver is required and should find the "
            "services by name rather than by dial frequency. Practical split for this trip: block 6A carries BBC "
            "World Service, Rai Radio Uno/Due/Tre, Net FM, Vibe HD and most Maltese services; block 6C carries the "
            "‘Sports Channel’ (Talk Sport) service plus UK relays such as LBC 97.3, Capital, Gold, Smooth and Jazz "
            "FM. A one-touch scan of the three blocks is the fastest way to answer the radio question in Malta "
            "itself."
        ),
        "source_url": "https://radioinmalta.com/en/dab/",
        "source_type": "official",
        "date_checked": "2026-10-11",
        "confidence": "partially verified",
        "notes": (
            "Block and station data read 11 October 2026 from the Radio in Malta DAB+ pages: "
            "https://radioinmalta.com/en/dab/ , https://radioinmalta.com/en/dab/6a.php and "
            "https://radioinmalta.com/en/dab/6c.php . Corroborated by WorldDAB’s Malta country page and multiplex "
            "table (multiplexes operated by Digi B Network; coverage via 6A/6C/12A): "
            "https://www.worlddab.org/countries/malta and https://www.worlddab.org/countries/malta/multiplexes , "
            "and by the MCA’s DAB+ consultation frequency table: "
            "https://www.mca.org.mt/sites/default/files/MCA-C-21-4261%20-%20DAB%20Plus%20Consultation_0.pdf . "
            "Radio in Malta is a specialist enthusiast directory and WorldDAB is an industry association, so both "
            "are directory evidence, not the Maltese network operator’s live data: service names, bit rates and "
            "block contents can change, and reception inside a seafront hotel or a metal-framed studio building was "
            "not measured. Verify by scanning on arrival; the station list is not a programme guide."
        ),
        "price range": (
            "Broadcast reception is free; a DAB+ receiver is required (hardware not priced here). A pocket DAB+ "
            "receiver or a phone with a DAB+ accessory is the lightest option for a trip"
        ),
    },
    after="talksport-dab-6c-malta",
)

upsert(
    radio,
    {
        "id": "vibe-fm-malta-premier-radio-partner",
        "name": "Vibe FM — published radio partner of the Malta Premier League (88.7 FM / DAB+)",
        "category": "FM",
        "area": "Malta (nationwide licensed FM, 88.7 MHz; also on DAB+ as Vibe HD)",
        "address": "Not applicable — broadcast service",
        "hours": (
            "No dated trip-week commentary schedule was found. Vibe FM’s league page carries matchday roundups and "
            "features rather than a live-commentary grid."
        ),
        "description": (
            "Vibe FM describes itself as the official radio partner of the Malta Premier League (the 360 Sports / "
            "YoHealth Malta Premier) and distributes on FM 88.7 MHz, DAB+ and online. This is the clearest "
            "documented link between a Maltese radio station and domestic football coverage, and the domestic "
            "fixture during the trip is Gżira United v Mosta on 14 October 2026 — but a partnership page is not "
            "proof that a named match is called live, and no commentary schedule was found. Ask the station or "
            "check on matchday."
        ),
        "source_url": "https://vibe.mt/maltapremier/",
        "source_type": "official",
        "date_checked": "2026-10-11",
        "confidence": "partially verified",
        "notes": (
            "Station page read 11 October 2026: https://vibe.mt/maltapremier/ (states “Vibe FM | Official Radio "
            "Partner” for the Malta Premier and lists FM 88.7, DAB+ and online as its platforms). The FM frequency "
            "is also on the Broadcasting Authority nationwide list: https://ba.org.mt/stations-licenced . Vibe FM "
            "appears on the DAB+ block 6A station list as “Vibe HD”: https://radioinmalta.com/en/dab/6a.php . The "
            "page’s content is roundups and features; live commentary of a named fixture was not verified, and "
            "unlike the Premier League, Maltese domestic football is played in Maltese and English coverage is not "
            "documented."
        ),
        "price range": "Free-to-air broadcast; FM or DAB+ receiver required; hardware price not checked",
    },
    after="net-fm-fm-101",
)

netfm = find(radio, "net-fm-fm-101")
netfm["notes"] = (
    netfm["notes"]
    + " Also carried on Malta DAB+ block 6A (181.936 MHz) under the service name “Net FM”, per the Radio in Malta "
    "6A station list read 11 October 2026: https://radioinmalta.com/en/dab/6a.php . This gives a second tuning "
    "route if the FM signal is weak inside the hotel."
)
netfm["price range"] = "Free-to-air on FM 101 MHz and on DAB+ block 6A; receiver cost not checked"

fixtures = find(radio, "epl-fixtures-trip-weekend-17-19-oct")
fixtures["notes"] = (
    fixtures["notes"]
    + " Radio-side follow-up added 11 October 2026: talkSPORT, an official Premier League audio broadcaster, is "
    "listed on Malta DAB+ block 6C at 185.360 MHz as the “Sports Channel (Talk Sport)” service — see the talkSPORT "
    "record in this dataset — which makes block 6C the priority receiver test during these fixtures. That relay’s "
    "actual content is still unverified, so the fixture list remains separate from carriage."
)

kalshi = find(radio, "kalshi-epl-serie-a-radio-overlap-oct-2026")
kalshi["description"] = (
    "Kalshi’s EPL and Serie A pages checked on 11 October 2026 list trip-weekend soccer markets on 16–18 October "
    "whose kickoff windows overlap BBC World Service Sportsworld, Rai Radio Uno’s Tutto il calcio, Radio Sportiva’s "
    "Diretta Sportiva and potentially the talkSPORT relay on Malta DAB+ block 6C. A market listing is still not "
    "proof of Malta radio commentary, and — separately — account eligibility matters: Kalshi’s own help centre says "
    "trading from outside the United States is possible from many countries and that customers may use the platform "
    "while travelling abroad subject to its Member Agreement, while third-party guidance says access is limited to "
    "US residents who pass KYC and warns of temporary geo-blocking while travelling. Confirm eligibility with Kalshi "
    "support before relying on it during the trip."
)
kalshi["notes"] = (
    kalshi["notes"]
    + " Eligibility evidence added 11 October 2026: Kalshi help centre, “Can I trade on Kalshi from outside the "
    "United States?” https://help.kalshi.com/en/articles/14026044-can-i-trade-on-kalshi-from-outside-the-united-states "
    "(says yes from many countries and that use while travelling abroad is permitted subject to the Member "
    "Agreement and geographic requirements) against conflicting third-party guidance "
    "https://tech-insider.org/prediction-markets/how-to-trade-on-kalshi/ (states access is restricted to US "
    "residents who pass KYC and that travellers may hit temporary geo-blocks). Kalshi’s regulatory status is as a "
    "CFTC-designated contract market: https://www.predictionmarket.tools/is-kalshi-legal . Also added: the Malta "
    "DAB+ block 6C relay of the “Sports Channel (Talk Sport)” service — "
    "https://radioinmalta.com/en/dab/6c.php — is the closest thing found to English live football commentary on "
    "Malta radio, but its content is unverified. No market-to-broadcast mapping exists in any source checked."
)
kalshi["price range"] = (
    "Radio broadcasts are free-to-air with a suitable receiver; Kalshi pricing and account eligibility from Malta "
    "are not verified (Kalshi’s own help centre and third-party guidance conflict)"
)

save("radio.json", radio)

# --------------------------------------------------------------- everyday
everyday = load("everyday.json")
everyday["last_updated"] = "2026-10-11"

power = find(everyday, "malta-electricity")
power["hours"] = "Not a schedule — plug/voltage reference for packing"
power["description"] = (
    "Malta uses Type G sockets (British three rectangular pins) at 230 V / 50 Hz, so a US Type A/B plug needs a "
    "travel adapter. Voltage matters as well as shape: laptops, phones, tablets and camera chargers are normally "
    "dual-voltage (100–240 V, 50/60 Hz) and need only the adapter, while single-voltage high-wattage appliances "
    "such as some hair dryers, straighteners and kettles can be damaged at 230 V and need a converter rather than "
    "an adapter. Hotels on the island commonly provide a limited number of adapters at reception, but that is not "
    "guaranteed — pack at least one Type G adapter and, for the event days, a power bank."
)
power["notes"] = (
    power["notes"]
    + " Re-verified 11 October 2026 with two independent travel-reference pages that both give Type G / 230 V / "
    "50 Hz for Malta and both warn that an adapter does not change voltage: "
    "https://www.power-plugs-sockets.com/us/malta/ and https://www.checkplug.com/usa-to-malta . These are consumer "
    "reference pages rather than a Maltese regulator, but they agree with each other and with the Government of "
    "Malta overview already logged. One page checked in the same batch (travelpowerplugs.com) incorrectly told US "
    "travellers that no adapter is needed; that claim contradicts the others and was not used."
)
power["price range"] = "Complimentary adapter availability not guaranteed; a Type G adapter is an inexpensive item to bring from home (not priced here)"
power["date_checked"] = "2026-10-11"

upsert(
    everyday,
    {
        "id": "eco-contribution-2026",
        "name": "Hotel eco-contribution (Malta Tourism Authority) — what this stay implies",
        "category": "Money, cards & tipping",
        "area": "Malta-wide, collected by licensed accommodation such as AX ODYCY",
        "address": "Not applicable — statutory contribution collected by the accommodation provider",
        "hours": (
            "Applies from 1 July 2026: €1.50 per night for each guest aged 18 or over at the start of the visit, "
            "capped at €22.50 per eligible person per visit; it must appear as a separate line on the invoice or "
            "fiscal receipt."
        ),
        "description": (
            "Malta Tourism Authority guidelines written for the 1 July 2026 increase confirm the rate (€1.50 per "
            "night), the age threshold (18 or over at the start of the visit) and the cap (€22.50 per person per "
            "visit) that hotels such as AX ODYCY collect on separately billed invoices. For this trip the arithmetic "
            "is six nights × €1.50 = €9.00 per eligible adult — but that is a conditional calculation from the "
            "supplied 13–19 October dates, not a quoted charge: the actual figure depends on the nights the hotel "
            "bills and on each guest’s age at check-in. The guidelines also clarify that a “visit” is an "
            "uninterrupted stay and that the cap corresponds to fifteen chargeable nights, which explains the "
            "separate “15-night” wording; it is a cap mechanism, not an exemption for short stays."
        ),
        "source_url": "https://mta.com.mt/docs/Eco-Contribution-Accommodation-Guidelines-2026.pdf",
        "source_type": "official",
        "date_checked": "2026-10-11",
        "confidence": "verified",
        "notes": (
            "Guidelines PDF read 11 October 2026: "
            "https://mta.com.mt/docs/Eco-Contribution-Accommodation-Guidelines-2026.pdf — it states the €1.50 rate "
            "per night per guest aged 18+, the €22.50 maximum per person per visit, that the amount is chargeable "
            "per night the accommodation is made available, that a “visit” is an uninterrupted stay in one or more "
            "licensable properties, that receipts must disclose it separately, and that the cap is applied against "
            "earlier contributions when evidence is retained. The MTA service page already logged carries the same "
            "rate and cap: https://mta.com.mt/services/environmental-contribution/ . Open item OQ-23/OQ-25 is now "
            "narrowed to the hotel invoice itself: how many nights are billed and which guests are 18+, so the €9 "
            "example is not presented as a charge."
        ),
        "price range": "€1.50 per person per night (guests 18+), maximum €22.50 per person per visit; six nights would be €9.00 per eligible adult if all six nights are billable",
    },
    after="malta-currency-cards",
)

weather = find(everyday, "october-weather-forecast")
weather["hours"] = (
    "Snapshot read 11 October 2026. AccuWeather’s Qawra October page: 13 Oct morning rain then thunderstorms "
    "24/19 °C, 14 Oct sunshine 24/17 °C, 15 Oct mostly sunny 25/17 °C, 16 Oct thunderstorms mainly early 24/17 °C, "
    "17 Oct a couple of afternoon showers 23/16 °C. timeanddate’s Qawra two-week table: 13–15 Oct sunny to mostly "
    "sunny, 16 Oct sprinkles late/overcast, 17 Oct mostly sunny, 18 Oct overcast, 19 Oct decreasing cloudiness."
)
weather["description"] = (
    "Two providers were read on 11 October 2026 so the trip week has a dated outlook rather than a monthly average. "
    "They agree on a warm, humid week in the mid-20s °C with the chance of showers, but they disagree on the "
    "arrival day itself — AccuWeather’s monthly page shows rain and thunderstorms for 13 October while "
    "timeanddate’s two-week table shows sun — which is exactly why the daily Malta Met Office forecast should be "
    "rechecked immediately before departure and each morning. Late-October sea temperatures stay warm enough for "
    "swimming for many visitors, but wind and rain can change boat and outdoor plans, including any Middle Sea "
    "Race viewing on 17 October."
)
weather["notes"] = (
    weather["notes"]
    + " Dated snapshots read 11 October 2026: https://www.accuweather.com/en/mt/qawra/233869/october-weather/233869 "
    "(monthly outlook with day-by-day 13–17 October entries) and https://www.timeanddate.com/weather/@2562641 "
    "(two-week table for Qawra). Both are commercial forecast products; monthly and long-range outlooks are the "
    "least reliable layer of a forecast and change frequently. Neither is the official Maltese meteorological "
    "service; the Malta Met Office forecast remains the reference to verify: https://maltametoffice.com/en/forecast/ . "
    "Temperatures in the sources were published in Fahrenheit and are converted here (75 °F ≈ 24 °C, 62 °F ≈ 17 °C)."
)
weather["date_checked"] = "2026-10-11"
weather["price range"] = "Not applicable — weather outlook; check the live daily forecast before outdoor plans"

save("everyday.json", everyday)

# --------------------------------------------------------------- expenses
expenses = load("expenses.json")
expenses["last_updated"] = "2026-10-11"
expenses["intro"] = (
    "A blank-by-default planner for 13–19 October 2026. Enter full trip/party amounts in euros (€) consistently; no "
    "flight, hotel, meal, fare, ticket, or reimbursement amount has been assumed. Bus and travel-card prices are now "
    "published and verified on the transport page if you want a benchmark for the transport rows; the only "
    "hotel-side figure with an official basis is the €1.50-per-night eco-contribution for guests aged 18+."
)

hotel_charges = find(expenses, "hotel-separate-charges")
hotel_charges["description"] = (
    "Optional line for charges shown separately on the confirmed hotel invoice. The Malta Tourism Authority’s "
    "guidelines confirm a contribution of €1.50 per night for each guest aged 18 or over from 1 July 2026, capped "
    "at €22.50 per person per visit and disclosed separately on the invoice. A six-night stay would therefore be "
    "€9.00 per eligible adult if all six nights are billable — a conditional calculation from the supplied dates, "
    "not the traveler’s confirmed amount. Do not duplicate amounts already included in the accommodation total."
)
hotel_charges["notes"] = (
    hotel_charges["notes"]
    + " Guidelines PDF read in full on 11 October 2026: "
    "https://mta.com.mt/docs/Eco-Contribution-Accommodation-Guidelines-2026.pdf . It confirms the €1.50 nightly "
    "rate, the 18+ age test at the start of the visit, the €22.50 per-person cap, that the cap corresponds to "
    "fifteen chargeable nights (explaining the “15-night” wording recorded as OQ-25), and that the amount must be "
    "shown separately on a fiscal receipt. The remaining open point is the invoice itself — billable nights and "
    "guest ages — so no amount is prefilled."
)
hotel_charges["price range"] = (
    "€1.50 per person per night for guests aged 18+, maximum €22.50 per person per visit; six chargeable nights "
    "would be €9.00 per eligible adult. Not a confirmed charge — verify on the hotel invoice."
)

event_access = find(expenses, "event-access")
event_access["description"] = (
    "Optional placeholder only. Tournament dates and the venue are documented, and BLAST has sold studio-audience "
    "tickets for other events it operates at the same Ta’ Qali studio, but no public ticket sale or spectator "
    "policy for these Finals — operated by GAM3RS_X — was found on 11 October 2026. Thunderpick says all matches "
    "are broadcast on its Twitch, Kick and YouTube channels. Leave this row blank until the organizer confirms how "
    "the traveler can attend; if attendance turns out to be impossible, no event ticket cost exists."
)
event_access["notes"] = (
    event_access["notes"]
    + " Re-checked 11 October 2026: the official event page still publishes no ticket link or spectator policy "
    "(https://world-championship.thunderpick.io/2026-finals/); BLAST’s Malta ticketing partner sells studio-audience "
    "tickets for BLAST-run events from €10.00 "
    "(https://eventworks.mt/premier-bounty-presented-by-polymarket) — precedent only; and an esports event "
    "directory lists the tournament without a ticket link (https://visitesports.com/locations/mt/malta). "
    "Thunderpick’s broadcast statement: "
    "https://esportsbrief.substack.com/p/thunderpick-world-championship-2026-return ."
)
event_access["date_checked"] = "2026-10-11"

save("expenses.json", expenses)

# --------------------------------------------------------------- sources log
sources_path = ROOT / "docs" / "SOURCES.md"
sources_text = sources_path.read_text(encoding="utf-8")
if "Second 11 October 2026 session" not in sources_text:
    sources_path.write_text(sources_text.rstrip("\n") + "\n" + SOURCES_ADDITION, encoding="utf-8")
    print("docs/SOURCES.md updated")
print("data files updated")
