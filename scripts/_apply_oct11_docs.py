#!/usr/bin/env python3
"""One-off helper: update the research records for the second 11 October 2026 session."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def replace(path: str, old: str, new: str, count: int = 1) -> None:
    file = ROOT / path
    text = file.read_text(encoding="utf-8")
    if old not in text:
        raise SystemExit(f"pattern not found in {path}: {old[:80]!r}")
    file.write_text(text.replace(old, new, count), encoding="utf-8")


def append(path: str, addition: str) -> None:
    file = ROOT / path
    text = file.read_text(encoding="utf-8")
    marker = addition.strip().splitlines()[0]
    if marker in text:
        print(f"already present in {path}")
        return
    file.write_text(text.rstrip("\n") + "\n" + addition, encoding="utf-8")


# ------------------------------------------------------------------- README
replace(
    "README.md",
    "- **Event and venue:** Thunderpick’s official page confirms the event window and Malta, not an address, spectator policy, entrance or public schedule. A separate-event BLAST guide and venue listings locate BLAST Arena Studios in the MFCC/Ta’ Qali area; do not transfer that event’s ticketing or entrance instructions to TWC.",
    "- **Event, venue and admission:** Thunderpick’s official page confirms the 12–19 October window (matches 14–18 October) and Malta. BLAST’s ticketing partner locates BLAST Arena Studios at MFCC South Gate National Stadium, Millennium Stand, Attard ATD 4000 in Ta’ Qali and sells studio-audience tickets (from €10.00) for BLAST-run events there — precedent only, because these Finals are operated by GAM3RS_X. **No public ticket sale or spectator policy for the Finals was found on 11 October 2026**, and Thunderpick says all matches stream on its Twitch, Kick and YouTube channels. Treat attendance as unconfirmed; ask the organizer.",
)
replace(
    "README.md",
    "- **Event-day transport and modes:** Route 186 is a direct public-bus candidate between Qawra stop 952 and Ta’ Qali Stadium stop 6227; its return boards from the opposite-side Stadium stop 2194 toward Buġibba, not the Qawra seafront. The last listed Stadium departure is 20:53 (with a last listed Buġibba Bay 1 arrival at 21:27); this is not a hotel connection guarantee. Route 214 is an alternative to compare. MPT lists an evening Route 186 diversion on 17 October. TD1’s official timetable lists Il-Qawra Arznell stop 950 in both directions; trip-specific departure choice and the walk to AX ODYCY still need a planner check. Compare bus fares/cards with live taxi/ride-hailing quotes and full car-hire costs; the October 2026 single fare and exact event-day door-to-door route remain open.",
    "- **Event-day transport and prices:** Route 186 is a direct public-bus candidate between Qawra stop 952 and Ta’ Qali Stadium stop 6227; its return boards from the opposite-side Stadium stop 2194 toward Buġibba, not the Qawra seafront (last listed Stadium departure 20:53). Route 214 is an alternative; MPT lists an evening diversion on 17 October. TD1’s timetable lists Il-Qawra Arznell stop 950 in both directions. **Fares were read directly from Malta Public Transport on 11 October 2026**: single day route €2.50 (summer table) / €2.00 winter with a two-hour transfer window, night and Tallinja Direct €3.00, TD1 €3.50, 12-journey card €19, Explore Adult 7-day €25, Explore Child €7, Explore Flex €21/€27, and a €50 fine without a valid ticket. Cards are sold at the Buġibba Terminal, the closest listed office to Qawra. Bolt is documented as operating in Malta; sources conflict on Uber. The exact door-to-door route, safe walks and late return still need a date-specific planner check. The operator’s page does not print the 2026/27 winter changeover, so €2.50 is the planning single fare.",
)
replace(
    "README.md",
    "- **Sports radio:** NET FM is listed at FM 101 MHz with a recurring sports grid. Malta DAB+ listings include BBC World Service, Rai Radio Uno and Radio Sportiva; WorldDAB lists BBC World Service on Digi B block 6A (181.936 MHz). BBC episode JSON gives *Sportsworld* first-broadcast offsets that convert to 15:06 on 17 October and 16:06 on 18 October Malta time. This is general live sport, not a named-match schedule. Six BBC Radio 5 Live / 5 Sports Extra Premier League episode records are UK schedule evidence only; two upcoming-page service labels differ from their JSON parent-service fields and should be rechecked. No Malta reception, stream access or named-match carriage was verified.",
    "- **Sports radio:** the strongest English-language lead is **talkSPORT on Malta DAB+ block 6C (185.360 MHz)**, listed as the service “Sports Channel (Talk Sport)” by the Radio in Malta directory with corroboration from WorldDAB’s Malta multiplex table and Wikipedia’s talkSPORT frequency list. talkSPORT is an official Premier League audio broadcaster, so block 6C is the first receiver scan target during the 17–18 October fixtures — but what the relay actually carries and indoor reception are unverified. Block 6A (181.936 MHz) carries BBC World Service, whose dated *Sportsworld* episodes start about 15:06 on 17 October and 16:06 on 18 October Malta time (general live sport, not a named match), plus Rai Radio Uno/Due/Tre, Net FM and Vibe HD; NET FM is also on FM 101 MHz and Vibe FM (88.7 FM / DAB+) is the published Malta Premier League radio partner. Six BBC Radio 5 Live / 5 Sports Extra Premier League episode records remain UK-only schedule evidence.",
)
replace(
    "README.md",
    "- **Hotel environmental contribution:** Malta Tourism Authority guidance states €1.50 per night per person aged 18+ from 1 July 2026, capped at €22.50 per eligible person per visit. Its separate “15-night threshold” wording is ambiguous; any six-night arithmetic is conditional, not a booking charge. Check the hotel invoice; the planner does not prefill a personal amount.",
    "- **Hotel environmental contribution:** the Malta Tourism Authority’s guidelines for the 1 July 2026 change confirm €1.50 per night for each guest aged 18+ (start of visit), capped at €22.50 per person per visit, disclosed separately on the invoice. The guidelines also explain the previously ambiguous “15-night” wording: the cap equals fifteen chargeable nights, so it is a cap mechanism, not an exemption for short stays. Six nights therefore implies about **€9.00 per eligible adult** — conditional on the invoice, and never prefilled in the planner.",
)
replace(
    "README.md",
    "- **Kalshi and fixtures:** EPL/Serie A category pages were checked for trip-window listings and schedule overlap. A market or fixture listing is not proof of Malta radio commentary, trading eligibility, or a market-to-broadcast link. Those questions remain open.",
    "- **Kalshi, fixtures and eligibility:** EPL/Serie A category pages list trip-window fixtures that overlap the radio windows. Kalshi’s own help centre says trading from outside the United States is possible from many countries and that customers may use the platform while travelling abroad, subject to its Member Agreement and geographic requirements; third-party guidance conflicts, saying access is limited to US residents who pass KYC and warning of temporary geo-blocking while travelling. A market or fixture listing is still not proof of Malta radio commentary or of a market-to-broadcast link; confirm eligibility with Kalshi support.",
)
replace(
    "README.md",
    "- **Expense planner:** all budget and actual fields start blank, including the seven optional daily templates. Enter euros on a consistent whole-trip/party basis and avoid counting the same expense in an aggregate and daily row. Inputs autosave only in this browser/device, are not sent to a server, can be exported as CSV, and can be cleared. Reference URLs are not price quotes.",
    "- **Expense planner:** all budget and actual fields start blank, including the seven optional daily templates, and a documented “when your itinerary arrives” intake maps each itinerary item to its row. Enter euros on a consistent whole-trip/party basis and avoid counting the same expense in an aggregate and daily row. Inputs autosave only in this browser/device, are not sent to a server, can be exported as CSV, and can be cleared. Verified bus/card prices are available as a transport benchmark; reference URLs are still not quotes.",
)

# -------------------------------------------------------------------- PLAN
append(
    "docs/PLAN.md",
    """
### Second 11 October 2026 session (post-merge verification)

Work continued on the fixed session branch `arena/96208136-maltasupplemental` after PR #31 merged. Because this environment has no isolated sub-agent runner, the same ownership-guided serial model was used: workstream A (fares, venue/admission, ride-hailing), E (DAB+ carriage and Kalshi eligibility) and D (power, eco-contribution, weather) were refreshed first, then the shared files (index shell, transport/radio/everyday/costs pages, README and research records) were updated once, in one pass, so no two writers touched a file in the same step. New findings that belong to another workstream are recorded in `docs/HANDOFF.md` rather than edited across owners.

Evidence rules unchanged: every record keeps the canonical 13 fields, every cited URL is logged in `docs/SOURCES.md` with its access date and limitation, and unresolved items moved to (or stayed in) `docs/OPEN_QUESTIONS.md` rather than being inferred. The refresh resolved two long-standing items (published bus fares; the MTA “15-night” wording) and upgraded one previously unverified radio lead (DAB+ block 6C talkSPORT carriage) to a partially verified listing with its content still open.
""",
)

# ------------------------------------------------------------------ HANDOFF
append(
    "docs/HANDOFF.md",
    """
## Second 11 October 2026 verification session — cross-topic notes

| From → To | Finding | Follow-up owner |
|---|---|---|
| A → E | talkSPORT on Malta DAB+ block 6C (185.360 MHz) is the best English football-radio lead; the venue trip and the 17–18 October fixture window now line up with it. | E: record the receiver test result on arrival (block, service label, what it actually carried). |
| A → F | Published bus fares are now exact (€2.50 single / €25 Explore 7-day / €3.50 TD1), so the transport rows can be benchmarked without guessing. | F: keep rows blank until real receipts, but the intake checklist now cites these prices. |
| A → C | No public ticket sale or spectator policy for the Thunderpick Finals was found; BLAST-run events at the same studio did sell tickets from €10. | C: add a watch-party/broadcast alternative row if the organizer confirms attendance is closed. |
| D → F | MTA guidelines confirm €1.50 per night for guests 18+ with a €22.50 per-person cap; the cap equals fifteen nights, resolving the “15-night” wording. Six nights implies €9.00 per eligible adult. | F: hotel-separate-charges row updated; still enter the invoice figure, not the example. |
| D → B/C | Dated 13–17 October forecast snapshots disagree on 13 October (rain vs sun), so outdoor plans need a same-day check. | B/C: recheck the Malta Met Office forecast on the day for terrace dining and outdoor events. |
| E → A | Kalshi’s own help centre permits travel-abroad use subject to its Member Agreement while third-party guides say US-resident-only; users should confirm eligibility rather than assume. | A: no transport impact; keep the Kalshi caveat visible in transport/taxi planning for late finishes. |
""",
)

# -------------------------------------------------------------------- AUDIT
append(
    "docs/AUDIT_2026-10-11.md",
    """
## Addendum — second 11 October 2026 session (supersedes one row above)

The Pass 3 row for radio record `worlddab-sports-channel-lead` is superseded. On re-reading, the Radio in Malta 6C station list explicitly labels the service “Sports Channel (Talk Sport)” at 185.360 MHz, WorldDAB’s Malta multiplex table lists a “Sports Channel” DAB+ service, and Wikipedia’s talkSPORT article lists “DAB+: 6C (Malta)”. The record was re-identified as `talksport-dab-6c-malta` with confidence `partially verified`: carriage on block 6C is directory-corroborated, while the relay’s actual content (live commentary versus talk-only output), rights scope and indoor reception remain unverified. The earlier 12A attribution is not retained as the primary lead.

This session also upgraded A (published fares, venue/admission status, ride-hailing conflict), D (power, eco-contribution, dated weather) and E (DAB+ tuning guide, Vibe FM league partnership, Kalshi eligibility). Five records were added (transport 18, radio 13, everyday 16 within 133 total), and the new URLs are logged in the second 11 October section of `docs/SOURCES.md`. Structural, source-log, JavaScript and 9-test browser gates were re-run after the changes.
""",
)

print("docs updated")
