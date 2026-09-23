# MALTASUPPLEMENTAL

Travel supplement for the **Thunderpick World Championship 2026** trip to Malta, **13–20 October 2026**
(7 nights, 8 days), for a US (California) resident departing **SFO**.

This site is a **supplement** to the main legal/risk dossier at
[buffedlizard55-lab.github.io/MALTA](https://buffedlizard55-lab.github.io/MALTA/) — it covers what that
dossier deliberately does not: food, landmarks, activities, getting around, radio & sports broadcasts,
prize-specific costs, entry/address answers, and a full audit of the Hotspawn prize.

## Pages

| Page | Contents |
|---|---|
| [Overview](https://buffedlizard55-lab.github.io/MALTASUPPLEMENTAL/) | Executive summary, verdict on the prize, what's here, top sources |
| [The Event](event.html) | TWC 2026 Finals: dates, venue, teams, format, streams, ticket notes |
| [Food & Drink](restaurants.html) | Top restaurants, Maltese classics, cafés, $30/day verification |
| [Landmarks & Sights](landmarks.html) | 8-day visit plan, temples, Valletta, Gozo/Comino |
| [Activities & Gaming](activities.html) | In-window events, gaming/PC venues, day-out activities |
| [Getting Around](getting-around.html) | 7 modes scored on convenience/price/value/feasibility; recommended plan |
| [Everyday Life](everyday.html) | Plugs (Type G 230 V), 112, language, money/VAT/tipping, water, health, US-citizen packing checklist |
| [Radio & Sports Bets](radio.html) | DAB+/FM/AM guide, in-window match schedule, Kalshi availability, pre-departure checklist |
| [Costs & Budget](costs.html) | What the prize covers/excludes, out-of-pocket budget, tax, scenarios, calculator |
| [Entry & Address](logistics.html) | Entry requirements, EES/ETIAS, passport, the address question answered |
| [Hotspawn & Prize](hotspawn.html) | Who Hotspawn/Sophie are, T&C audit, 10 flagged irregularities, email draft to send |
| [All Sources](sources.html) | Every URL used, tagged Official / Verified / Estimate / Flag |

## Privacy

The private email correspondence between Danny and Hotspawn (Sophie) is **strictly internal**. No email
content is quoted, reproduced or summarised verbatim anywhere in this repository — only the context needed
to answer the research questions (what was asked, what decisions hang on it) appears on-site, plus a draft
*outbound* reply the owner may choose to send. Third-party winner handles beyond the site owner's own are
deliberately omitted. If you contribute: never commit email text.

## Known open items (all flagged on-page)

- **Do not book anything** until the prize's cash-alternative / written coverage is confirmed (see
  [Costs](costs.html) and the email draft in [Hotspawn](hotspawn.html)).
- The T&C residency clause conflicts with the winner's US residence — resolve before ID submission.
- BirguFest 2026 dates are unresolved across four sources; 2026/27 winter bus-fare switchover is assumed
  but unconfirmed; the 7-day card's Airport Direct coverage is self-contradictory on the two official
  operator pages (Explore-card detail vs Airport Direct FAQ).
- US cars have HD Radio, not DAB+ — bring a radio or buy one locally for the talkSPORT feed.
- Login-walled platforms (Google Maps, Yelp, Instagram, TikTok, Facebook, X) could not be queried
  directly; their signal enters only via named aggregators — see the not-found register on
  [Sources](sources.html).

## Next-session work queue

1. Itinerary arrives → enter confirmed flight/hotel numbers in the [calculator](costs.html) (2 minutes).
2. Collect the five written confirmations listed on [Hotspawn & Prize](hotspawn.html).
3. T-7 days: re-check EPL MW7 kick-offs, the TWC format page, ETIAS status, winter-fare switchover,
   passport validity, and DAB+ 6C carriage on arrival.
4. Email Kalshi support about trading from Malta; keep the written reply.
5. BirguFest dates: ask the Birgu Local Council directly once published.

## Building

Static HTML/CSS/JS, no dependencies. Serve locally with any static server, e.g.:

```bash
python3 -m http.server 8080
# → http://localhost:8080
```

## Method

Every claim carries a source link; every source is tagged by trust level in
[All Sources](sources.html). Conflicting sources are shown, not averaged. Anything that could not be
verified (login-walled social platforms, unpublished schedules, a contradictory operator catalogue) is
explicitly recorded as not found rather than filled in.
