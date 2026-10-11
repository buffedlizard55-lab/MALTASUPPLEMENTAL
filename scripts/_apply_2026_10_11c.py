#!/usr/bin/env python3
"""One-off: refresh records whose evidence changed in the 2026-10-11 re-verification pass.

Only existing records are edited, only their own text fields, and every newly cited
URL is appended to docs/SOURCES.md in the same run.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"

EDITS = {
    "data/everyday.json": {
        "ees-malta-implementation-conflict": {
            "notes": (
                "The official EU FAQ was read directly on 11 October 2026 and states: \"This progressive implementation "
                "lasted until 9 April 2026. From 10 April 2026, the EES is fully operational at all external border "
                "crossing points of the European countries using the system.\" It also confirms that for a visa-exempt "
                "traveller the system stores four fingerprints and a facial image, that fingerprints of children under 12 "
                "are not scanned, that a biometric passport is only needed for self-service equipment, and that the "
                "90-days-in-any-180-days limit is calculated as a single period across all EES countries: "
                "https://travel-europe.europa.eu/en/ees/faq . Legal basis cited there: Regulation (EU) 2017/2226 and "
                "Regulation (EU) 2025/1534. **Malta-specific evidence added in this pass.** Malta International "
                "Airport's own passport-control page describes the practical local position: from 12 October 2025 "
                "third-country nationals arriving in or departing from Malta \"may be randomly selected\" for a biometric "
                "lane, with no advance registration required, and children under 12 photographed but not fingerprinted: "
                "https://maltairport.com/practical-information/security-passport-control/passport-control/ . Malta's Home "
                "Affairs Minister was reported saying the country's EES resources are \"already at full capacity\" and that "
                "each registration takes roughly 40 seconds to a minute and a half, after reports of 40-minute-plus "
                "immigration delays: https://timesofmalta.com/article/resources-eu-entryexit-system-already-capacity.1126970 . "
                "For the enforcement delay itself, the strongest secondary evidence read this pass is the Guardian's 14 "
                "September 2026 report of a Sunday Times story of 13 September: nine Schengen states — France, Greece, "
                "Italy, Portugal, Germany, Malta, the Netherlands, Switzerland and Belgium — told the Commission they "
                "needed more time and were informally allowed to keep pausing biometric collection with no deadline set: "
                "https://www.theguardian.com/world/2026/sep/14/eu-countries-delay-ees-entry-exit-system-border-checks-france-greece-portugal-italy . "
                "An earlier, weaker secondary source asserting Malta was \"not operating EES at all borders\" remains in "
                "the historical log but is superseded by the Guardian/Sunday Times account: "
                "https://www.visasupdate.com/post/ees-implementation-delay-schengen-nine-countries-2026 . Still "
                "unresolved: no Malta government or eu-LISA statement confirming or denying the pause was found, and no "
                "source publishes Malta-specific wait times. Do not treat either position as settled; allow generous time "
                "on both the arrival and the departure day."
            ),
        },
        "ees-border-system": {
            "notes": (
                "The EU FAQ says children under 12 are not fingerprint-scanned and that a biometric passport is only "
                "needed for optional self-service equipment, not in principle to cross the border. EES FAQs: "
                "https://travel-europe.europa.eu/en/ees/faq. **Malta operational detail added in this pass:** Malta "
                "International Airport states that from 12 October 2025 third-country nationals arriving at or departing "
                "from Malta may be randomly selected to pass through a biometric passport-control lane, that no "
                "registration is required in advance, and that children below 12 only need a photograph: "
                "https://maltairport.com/practical-information/security-passport-control/passport-control/ . "
                "Malta's Home Affairs Minister was reported in April 2026 saying EES resources were \"already at full "
                "capacity\", that registration averages about 40 seconds to a minute and a half per passenger, and that "
                "40-minute-plus immigration delays had been seen in Malta: "
                "https://timesofmalta.com/article/resources-eu-entryexit-system-already-capacity.1126970 . Actual queue "
                "times are not published here and are not predictable; see the Malta-specific enforcement conflict "
                "recorded separately."
            ),
        },
        "etias-status-2026-10": {
            "description": (
                "The official EU ETIAS site says the system is not in operation and no applications are being collected, "
                "as checked 11 October. The EU says it will announce the start date several months before launch. "
                "Recheck the official page before travel; do not pay an unofficial site claiming to issue an "
                "authorisation. **Timing risk worth acting on:** official and industry sources have long pointed to the "
                "last quarter of 2026, which overlaps this 13–19 October 2026 trip, while at least one September 2026 "
                "report says the EU has stopped printing a Q4-2026 date and that launch may slip to 2027. Because the "
                "trip sits at the boundary, check the official EU page in the days before departure rather than "
                "assuming either outcome."
            ),
            "notes": (
                "Live status and official notices: https://travel-europe.europa.eu/en/etias. A U.S. State Department "
                "Europe guide says U.S. citizens currently need no travel authorisation for the Schengen Area and that "
                "ETIAS \"plans to launch in late 2026\": "
                "https://travel.state.gov/en/international-travel/planning/guidance/europe.html. IATA likewise states "
                "ETIAS \"will start operations in the last quarter of 2026\" and that the fee is EUR 20, warning that "
                "only the official EU site may take applications: https://www.iata.org/en/about/worldwide/europe/new-entry-requirements-eu/ . "
                "The EUR 20 fee comes from Commission Delegated Regulation (EU) 2025/1411 of 17 July 2025, which raised "
                "the original EUR 7 figure; older official pages still quoting EUR 7 are out of date. Against that, a "
                "September 2026 travel-industry summary reports that the official ETIAS page no longer gives a launch "
                "date at all, that only \"not yet in operation\" is stated, and that press reporting points to 2027 at "
                "the earliest: https://onwarditinerary.com/blog/etias-2026-current-status . Because the trip window "
                "straddles the announced Q4-2026 target, this record stays at the official-site position (not in "
                "operation, no applications accepted) and the disagreement is recorded rather than resolved. Status is "
                "date-sensitive; recheck the EU page immediately before travel."
            ),
        },
    },
    "data/radio.json": {
        "net-fm-fm-101": {
            "notes": (
                "Regulator and full station grid freshly read 11 October: https://ba.org.mt/stations-licenced ; "
                "https://netfm.com.mt/ . The operator also lists NET FM on DAB+: https://dab.com.mt/channels/ . "
                "**Independent same-day re-read added in this pass:** the station's own schedule page was opened a "
                "second time on 11 October 2026 and again returned Friday 18:30 \"Mhux Premier biss\", Saturday 16:00 "
                "\"Hits & Score\" and Sunday 15:00 \"Sports Box\", plus the NET News bulletin grid (07:00/12:00/18:00 on "
                "weekdays; 08:00/12:00/18:00 at weekends). A repeat read by the same method is a stability check, not "
                "independent corroboration from a second source. Note that the two sports-branded shows are named "
                "\"Hits & Score\" and \"Sports Box\" and the Friday slot is titled \"Mhux Premier biss\" (\"not just the "
                "Premier\"), which suggests a round-up rather than a dedicated live Premier League commentary slot — "
                "confirm with the station. No local receiver test or named-match running order was obtained. Do not "
                "infer live commentary simply because a slot overlaps a kickoff. Confirm language and local clock with "
                "the station."
            ),
        },
        "talksport-dab-6c-malta": {
            "notes": (
                "Fresh 11 October reads: https://radioinmalta.com/en/dab/6c.php (C02F, DAB+ HE-AAC v2; page marked "
                "under construction); https://www.worlddab.org/why-dab-plus/countries/malta/multiplexes ; "
                "https://dab.com.mt/channels/ (both chunks). Third-party 2025 scanner observations in the historical "
                "source log are not present-day measurements. Scan by service name, record actual block and identify "
                "audio locally; directory agreement is not a substitute. https://talksport.com/schedule/ again "
                "returned \"Sorry, page unavailable\". Source type review denotes an independent technical directory, "
                "not the broadcaster or regulator. **Further conflicting listings added in this pass.** The same "
                "directory's Malta station index, read via search extract on 11 October 2026, appears to attach a "
                "\"DAB+ (Labelled as Sports Channel)\" note and the website talksport.com to a UK-English service in "
                "its list, which corroborates that some Malta DAB+ service is labelled \"Sports Channel\" without "
                "resolving which block carries it: https://radioinmalta.com/en/stations/ . Against that, the "
                "encyclopaedic list of Maltese radio stations puts **185.36 MHz DAB+ to \"RAVE Radio\"** (electronic "
                "music) rather than a sports service, i.e. the same block this directory calls 6C is labelled a music "
                "station elsewhere: https://en.wikipedia.org/wiki/List_of_radio_stations_in_Malta . Both are "
                "third-party listings, the Wikipedia entry is crowd-edited, and neither is a measurement — which is "
                "precisely why the guidance here stays \"scan it yourself\"."
            ),
        },
    },
    "data/activities.json": {
        "twc-2026-teams-format": {
            "description": (
                "The organizer describes eight-team CS2 Finals, a US$1 million prize pool and live Twitch/Kick/YouTube "
                "broadcasts. Its 16 September announcement named Virtus.pro, but 9 October reports from HLTV and "
                "presenting partner Hotspawn say Ninjas in Pyjamas replaces that team after visa/health problems. "
                "Liquipedia independently records the same 9 October replacement and lists Virtus.pro under former "
                "participants. **Groups confirmed in this pass:** Group A Falcons, NIP, 9z, Aurora; Group B FURIA, "
                "BETBOOM, Legacy, PARIVISION; two best-of-three GSL groups feeding a single-elimination playoff with a "
                "third-place decider and a best-of-five grand final. The event desk keeps the field update, format, "
                "talent and third-party bracket clocks together; older field lists are not the current lineup."
            ),
            "notes": (
                "Current integration re-read the full 16 September organizer release, the main HLTV article body at "
                "https://www.hltv.org/news/45688/thunderpick-world-championship-matchups-announced-with-virtuspro-replaced-by-nip "
                "and the complete Hotspawn report at "
                "https://www.hotspawn.com/counter-strike/news/nip-replace-virtus-pro-at-thunderpick-world-championship-2026 . "
                "The later reporting supersedes the Virtus.pro slot in the older release. **Corroboration added in this "
                "pass:** Liquipedia's event page records the 9 October withdrawal/replacement and the same group "
                "composition: https://liquipedia.net/counterstrike/Thunderpick/World_Championship/2026 . HLTV's matchup "
                "article also gives the host-region rule: because the withdrawal came within 20 days of the event, the "
                "replacement had to come from the next eligible team in the host region's VRS — here Europe, which is "
                "NIP. Organizer phase/format reference: https://world-championship.thunderpick.io/2026-finals/ . See "
                "event.html#twc-teams-format and event.html#twc-match-times-malta for the qualified details. Stream "
                "access is not terrestrial radio; future rosters and clocks can change."
            ),
        },
        "twc-day-2026-10-14": {
            "description": (
                "The visible listing provides Wednesday check-in and games times. Its overall headline ends at 22:00 "
                "but this agenda row ends at 22:30; confirm the finish before arranging the return. **Independent "
                "corroboration added in this pass:** the published Wednesday 14 October schedule places the first "
                "matches at 10:30, 13:00, 15:30 and 18:30 CEST — 9z v Aurora 10:30, Falcons v NIP 13:00, Legacy v "
                "PARIVISION 15:30, FURIA v BETBOOM 18:00 — which matches the listing's \"games 10:30\" start. If four "
                "matches run from 10:30 to 18:30, an end time of 22:00–22:30 is plausible but still not confirmed; "
                "these are scheduled start times from esports databases, not door times or a guaranteed finish."
            ),
            "notes": (
                "Organizer stage dates: https://world-championship.thunderpick.io/2026-finals/ . Visible "
                "agenda/ticket conditions: "
                "https://www.eventbrite.co.uk/e/hotspawn-present-the-thunderpick-world-championships-2026-tickets-1988838616841 . "
                "Wednesday match times (10:30, 13:00, 15:30 and 18:30 CEST) corroborated in this pass by HLTV at "
                "https://www.hltv.org/news/45688/thunderpick-world-championship-matchups-announced-with-virtuspro-replaced-by-nip "
                "and Liquipedia at "
                "https://liquipedia.net/counterstrike/Thunderpick/World_Championship/2026 ; both are third-party esports "
                "sources, so treat them as scheduled start times rather than organizer guarantees. No matches, "
                "attendance or personal timetable are booked by this guide. Consult the Transport records for route "
                "candidates; no dated hotel-to-gate journey has been saved."
            ),
        },
    },
}

SOURCE_ROWS = [
    (
        "Guardian report (14 Sep 2026) of a Sunday Times story of 13 Sep 2026: nine Schengen states including Malta told "
        "the Commission they need more time to introduce EES fingerprinting and were informally allowed to keep "
        "pausing collection with no deadline attached.",
        "https://www.theguardian.com/world/2026/sep/14/eu-countries-delay-ees-entry-exit-system-border-checks-france-greece-portugal-italy",
        "2026-10-11",
        "D — Everyday",
        "Established press, secondary. Read via search extract, not a full page read, and it reports another "
        "publication rather than the Commission's own record. No Malta government or eu-LISA confirmation was found, so "
        "the conflict with the official 10 April 2026 position is recorded, not resolved.",
    ),
    (
        "Malta International Airport passport-control page: from 12 October 2025 third-country nationals may be randomly "
        "selected for a biometric lane on arrival or departure; no advance registration; children under 12 photographed "
        "but not fingerprinted.",
        "https://maltairport.com/practical-information/security-passport-control/passport-control/",
        "2026-10-11",
        "D — Everyday",
        "Official airport operator page, read via search extract. It describes random selection rather than universal "
        "capture, which is consistent with a country that is not yet fully enforcing EES at every lane, but the page "
        "carries no date beyond 12 Feb 2026 and does not confirm current practice in October 2026.",
    ),
    (
        "Malta's Home Affairs Minister: EES resources \"already at full capacity\"; registration about 40 seconds to one "
        "and a half minutes per passenger; reports of 40-minute-plus immigration delays in Malta.",
        "https://timesofmalta.com/article/resources-eu-entryexit-system-already-capacity.1126970",
        "2026-10-11",
        "D — Everyday",
        "Established national press, secondary, dated April 2026. A ministerial statement about resourcing, not a "
        "published waiting-time table, and eight months old by the trip.",
    ),
    (
        "IATA: ETIAS \"will start operations in the last quarter of 2026\"; fee EUR 20; only the official EU site may "
        "take applications.",
        "https://www.iata.org/en/about/worldwide/europe/new-entry-requirements-eu/",
        "2026-10-11",
        "D — Everyday",
        "Industry body, not the regulator. Corroborates the EUR 20 fee introduced by Commission Delegated Regulation "
        "(EU) 2025/1411 of 17 July 2025 and the Q4-2026 target, both of which put the trip window at the boundary.",
    ),
    (
        "September 2026 travel-industry summary: the official ETIAS page no longer publishes a launch date, states only "
        "\"currently not in operation\", and press reporting points to 2027 at the earliest; a transitional period and "
        "grace period of at least six months each would follow any launch.",
        "https://onwarditinerary.com/blog/etias-2026-current-status",
        "2026-10-11",
        "D — Everyday",
        "Secondary commentary, not official. Recorded because it directly contradicts the Q4-2026 target in IATA, U.S. "
        "State Department and earlier EU material for a trip that falls in that quarter. Neither position is asserted; "
        "the traveller should recheck the EU page before departure.",
    ),
    (
        "Liquipedia event page: 9 October 2026 Virtus.pro withdrawal and Ninjas in Pyjamas replacement, current eight-team "
        "field and groups, and the same Wednesday 14 October match start times (10:30, 13:00, 15:30, 18:30 CEST).",
        "https://liquipedia.net/counterstrike/Thunderpick/World_Championship/2026",
        "2026-10-11",
        "C — Activities / H — Event",
        "Community-edited esports database. Read via search extract. Useful as an independent second account of the "
        "roster change, but match clocks are scheduled starts, not organizer door times or guaranteed finishes.",
    ),
    (
        "Third-party listings for the same DAB+ block conflict: an encyclopaedia list of Maltese radio stations labels "
        "185.36 MHz DAB+ as \"RAVE Radio\" (electronic music), while the specialist directory labels 6C / 185.360 MHz a "
        "sports service; the directory's station index also carries a \"DAB+ (Labelled as Sports Channel)\" note against "
        "a UK-English talksport.com service.",
        "https://en.wikipedia.org/wiki/List_of_radio_stations_in_Malta ; https://radioinmalta.com/en/stations/",
        "2026-10-11",
        "E — Radio sports",
        "Both are third-party listings read via search extract on 11 October 2026; the encyclopaedia entry is "
        "crowd-edited. Neither is an RF measurement, so the record stays at \"scan by service name locally\" and the "
        "conflict is not resolved.",
    ),
]


def main() -> None:
    for relative, mapping in EDITS.items():
        path = ROOT / relative
        payload = json.loads(path.read_text(encoding="utf-8"))
        by_id = {record["id"]: record for record in payload["records"]}
        for record_id, changes in mapping.items():
            if record_id not in by_id:
                raise SystemExit(f"missing record {record_id} in {relative}")
            for field, value in changes.items():
                by_id[record_id][field] = value
            print(f"updated {relative} :: {record_id} :: {sorted(changes)}")
        path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    log = ROOT / "docs/SOURCES.md"
    text = log.read_text(encoding="utf-8")
    marker = "EES delay report naming Malta, airport border page, ministerial statement"
    if marker not in text:
        rows = "".join(
            f"| {claim} | {url} | {date} | {stream} | {limit} |\n"
            for claim, url, date, stream, limit in SOURCE_ROWS
        )
        log.write_text(text + "\n### Second re-read rows — EES delay report naming Malta, airport border page, ministerial statement, ETIAS timing conflict, Liquipedia roster cross-check, DAB+ block conflict\n\n" + rows, encoding="utf-8")
        print("docs/SOURCES.md: appended second re-read rows")
    else:
        print("docs/SOURCES.md: rows already present")


if __name__ == "__main__":
    main()