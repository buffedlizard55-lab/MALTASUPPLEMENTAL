#!/usr/bin/env python3
"""One-off helper: update docs/OPEN_QUESTIONS.md for the second 11 October 2026 session."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
path = ROOT / "docs" / "OPEN_QUESTIONS.md"
text = path.read_text(encoding="utf-8")


def swap(old: str, new: str) -> None:
    global text
    if old not in text:
        raise SystemExit(f"not found: {old[:90]!r}")
    text = text.replace(old, new, 1)


# 1. Fare/trip-window row: the operator's own table is now recorded.
swap(
    "| Open — TD1’s official table lists Arznell 950 in both directions with route-level times, but October fare validity, trip-specific departure choice, hotel walk, and venue walk remain unresolved. |",
    "| Partly resolved 2026-10-11 (second session): the operator’s own fare table was read directly and records day-route singles at €2.50 (summer) and €2.00 (winter), with the €2.00 winter fare stated to run 19 Oct 2025 – 13 Jun 2026; €2.50 is therefore the planning single fare for 13–19 October. The 2026/27 winter changeover date is not printed on the page. Travel-card prices, the two-hour transfer window, the €50 no-ticket fine and the Buġibba Terminal sales office are now recorded. Still open: trip-specific departure choice, hotel walk, venue walk and the confirmed TWC entrance. |",
)

# 2. Radio row: replace the old TalkSPORT row with the upgraded status.
swap(
    "| Is TalkSPORT actually carried on Malta DAB+ 6C, and what current technical details identify that multiplex? | A third-party Radio in Malta directory claims “Sports Channel (Talk Sport)” on 6C, but the licensed-provider directory/schedule checked did not corroborate the station or current block details. | Obtain an up-to-date Digi B channel list, authoritative broadcaster/rights-holder confirmation, or a local DAB+ receiver scan with the service name and multiplex data. | Unverified lead only; not counted as confirmed carriage in `radio.html` or `data/radio.json`. |",
    "| Is talkSPORT carried on Malta DAB+ 6C, and does the relay carry live Premier League commentary? | Carriage is now corroborated by three listings (Radio in Malta’s 6C station list labels the service “Sports Channel (Talk Sport)” at 185.360 MHz; WorldDAB’s Malta multiplex table lists a “Sports Channel” DAB+ service; Wikipedia’s talkSPORT article lists “DAB+: 6C (Malta)”). What the relay actually transmits — live match commentary versus talk-only output — plus its rights scope and indoor reception at AX ODYCY remain unverified. | Run the documented five-minute receiver test on arrival: scan 6A/6C/12A, confirm the 6C service label, and note what it carries during the 17–18 October Premier League fixtures; optionally ask the station or Digi B to confirm the relay’s content. | Partly resolved 2026-10-11 (second session): upgraded from “unverified lead” to partially verified carriage, recorded in `data/radio.json` as `talksport-dab-6c-malta`; content and reception still open and never presented as guaranteed commentary. |",
)

# 3. Weather row: add the dated snapshots for the trip window.
swap(
    "| Open — 13–15 Oct snapshot is dated in `data/everyday.json`; no later trip dates were forecast in the checked view. |",
    "| Partly resolved 2026-10-11 (second session): two providers were read for the trip window — AccuWeather’s Qawra October page (13 Oct rain/thunderstorms, 14 Oct sunshine, 15 Oct mostly sunny, 16 Oct early thunderstorms, 17 Oct afternoon showers) and timeanddate’s Qawra two-week table (13–15 Oct sunny to mostly sunny, 16 Oct sprinkles late, 17 Oct mostly sunny, 18 Oct overcast, 19 Oct clearing) — and they disagree on 13 October, so the daily Malta Met Office forecast must still be rechecked on arrival and each morning. |",
)

# 4. OQ-23 resolution.
swap(
    "## OQ-23 — Exact Malta environmental-contribution amount for this booking\n\nThe Malta Tourism Authority states that from 1 July 2026 the contribution is €1.50 per night for each guest aged 18 or over, capped at €22.50 per eligible person per visit, and must appear as a separate invoice/fiscal-receipt item. The conditional six-night arithmetic is €9 per eligible adult only if six nights are billable; the actual amount depends on the booking, guest ages, nights charged, and hotel invoice. Confirm those details with AX ODYCY before entering a budget/actual amount. Source checked 2026-10-10: https://mta.com.mt/services/environmental-contribution/.",
    "## OQ-23 — Exact Malta environmental-contribution amount for this booking\n\n**Resolved at the rule level on 11 October 2026 (second session); the invoice figure remains open.** The Malta Tourism Authority’s guidelines for the 1 July 2026 change state that the contribution is €1.50 per night for each guest aged 18 or over at the start of the visit, capped at €22.50 per eligible person per visit; it is chargeable per night the accommodation is made available, and must be disclosed separately from accommodation fees on a fiscal receipt. For the supplied six-night window the arithmetic is €9.00 per eligible adult. That is a calculation from published rules, not a quoted charge: the amount to budget depends on the nights AX ODYCY bills and on each guest’s age at check-in, so enter the invoice figure. Sources read 11 October 2026: https://mta.com.mt/docs/Eco-Contribution-Accommodation-Guidelines-2026.pdf and https://mta.com.mt/services/environmental-contribution/.",
)

# 5. OQ-25 resolution.
swap(
    "## OQ-25 — MTA “15-Night Threshold” wording\n\nIndependently re-read 11 October: MTA states the €1.50/night/person18+ rate and €22.50/visit cap but separately says “Eco-contribution shall be chargeable on the total number of nights per person of accommodation during the relative period that exceeded fifteen (15) nights.” The guide does not interpret this ambiguous wording as an exemption or extra charge. Six billable nights × €1.50 = €9 is arithmetic only, not confirmation that this booking owes it. Ask MTA/AX ODYCY for current liability/invoice treatment. https://mta.com.mt/services/environmental-contribution/",
    "## OQ-25 — MTA “15-Night Threshold” wording\n\n**Resolved 11 October 2026 (second session).** Reading the MTA guidelines PDF in full shows that the €22.50 per-person cap is produced by fifteen chargeable nights (15 × €1.50), and that the “15-night” sentence describes when the reporting obligation and the nil-charge treatment of unlicensed-interval nights apply to long stays — it is a cap/administration mechanism, not an exemption for short stays and not an extra charge. A short stay is therefore charged €1.50 per night per guest aged 18+, up to the cap. Sources read 11 October 2026: https://mta.com.mt/docs/Eco-Contribution-Accommodation-Guidelines-2026.pdf (rate, cap, “visit” definition, receipt rules); https://mta.com.mt/services/environmental-contribution/. The only remaining question is the invoice figure (OQ-23).",
)

# 6. New open questions for the newly discovered items.
swap(
    "## Upstream reconciliation decisions",
    """## OQ-26 — Can the traveler actually attend the Thunderpick Finals?\n\nNo public ticket sale, spectator policy, spectator entrance or daily door time for the 2026 Finals was found on 11 October 2026, in the official event page, the Thunderpick release or an esports event directory. BLAST sells studio-audience tickets for events it operates at the same Ta’ Qali studio (from €10.00 for the July 2026 BLAST Premier Bounty) — precedent that the room can host an audience, not evidence that this event admits the public. Thunderpick states all matches will be broadcast on its Twitch, Kick and YouTube channels. Resolve by asking the organizer (Thunderpick/GAM3RS_X) directly, or by watching for a ticket or attendee page; until then, treat the trip’s CS2 attendance as unconfirmed and keep the venue trip optional.\n\n## OQ-27 — Does Uber operate in Malta in 2026?\n\nSources conflict. Uber publishes a Malta airport page that says taxis are not available there and points riders to UberX with an average €20 fare for a ~19-minute trip, while two 2026 third-party guides state plainly that Uber does not operate in Malta and recommend Bolt or eCabs. Bolt’s presence is corroborated by national media. Resolve in the app on arrival: open Bolt, eCabs and Uber and check which shows vehicles and an upfront quote for a Qawra–Ta’ Qali trip; record the live quote in the expense planner.\n\n## OQ-28 — What content does the Malta DAB+ 6C “Sports Channel” relay carry?\n\nThe service is directory-corroborated as talkSPORT (see the upgraded row above), but no operator schedule or relay-content description was found remotely. Resolve with the documented receiver test during the 17–18 October Premier League window and record the result (block, service label, programme, whether commentary was continuous) for the next session.\n\n## Upstream reconciliation decisions""",
)

path.write_text(text, encoding="utf-8")
print("OPEN_QUESTIONS.md updated")
