# Current cross-workstream handoff

**Session:** `arena/dfefc16f-maltasupplemental` · **updated:** 11 October 2026 UTC.

A–F were implemented as isolated sequential workstreams on the fixed session branch; G integrates shared files last. The eight-record event extension (H) and hotel/transport additions were inherited from main PRs #42/#43, not created on another branch here. Historical notes are retained in [HANDOFF_HISTORY.md](HANDOFF_HISTORY.md); their old “current” headings are not current guidance.

| From → to | Finding / decision | Integration outcome / remaining gap |
|---|---|---|
| A/C/H → G/F | Eventbrite advertises free in-person ages-18+ reservations for 14–18 October; visible Wed/Thu agenda ends 22:30 vs headline 22:00, Fri ends 21:00. | Six day/brief projections plus eight detailed event records render canonically. No reservation/inventory, gate, weekend FAQ/agenda or display-timezone guarantee. “Not visible” replaces “unpublished”. |
| A → C/G/F | Static Route 186 return variant does not establish a dated last bus or every route alternative. April 20:00 and October 19:00 notices are separate; October extraction lacks a year. | Removed mandatory second-bus/five-taxi/settled-outbound claims. Use dated outward/return planner and walks, with a quoted fallback. TQ1 has no visible timetable; historical corridor evidence is not a TWC shuttle. |
| A → F/G | Published seasonal fares have no explicit effective October range; card coverage/value requires the actual product and boardings. | No October fare, card purchase or break-even result prefilled. Removed “closest sales point”, guaranteed on-bus payment and automatic better-buy claims. |
| A/D → F/G | Full AX ODYCY FAQ re-read: Guest Relations offers fixed-charge taxi arrangements; full regulator taxi page has April 2022 footer. | Preserved new hotel taxi and meter-reference records, but no actual rate, measured distance, current legal-ceiling certification or applicable app fare regime. |
| B → C/F/G | Food hours, kitchen cutoff, closed/refurbishing properties and menu snapshots are distinct from live reservations. | Shortlist is not a popularity rank. Featured/sponsored ordering and conflicting counts are not compared as a universal league table. Current sampled Yelp/Instagram/TikTok/Facebook/Reddit/X refreshes were blocked. |
| C/H → A/F/G | Fresh organizer phases, HLTV/Hotspawn NIP replacement and Liquipedia EDT bracket sections. | Retained upstream H records; corrected C's older Virtus.pro list and source classification. Third-party match clocks are labelled review evidence, not official door/finish times. Streams remain explicitly internet-only. |
| C → G | No confirmed walk-in PC café; directory absence does not prove closure. UNO date extraction lacks a year; some museum clocks are older chart transcriptions. | Confidence/notes preserve the boundary. UNO title now says year unconfirmed. Do not route to closure-conflicted/out-of-window attractions or assume outings fit around event days. |
| D → F/G | Type G/230 V/50 Hz, device-label check, EU cash declaration and primary MTA nightly rule. Full hotel FAQ supports razor-only 110 V socket, card/pre-authorisation policy, doctor and discretionary tipping guidance. | Adapter is not a converter. €10,000 is a declaration threshold, not a carrying maximum. No short-stay tax exemption inferred. Six qualifying nights €9/adult is arithmetic, not an invoice/default. Hotel room-name equivalence and personal eligibility remain checks. |
| D → C/G | Fresh national forecast covers trip dates 13–17, not 18–19. | Removed inherited “full-window national forecast” implications. Refresh forecasts and marine conditions before outings. |
| E → C/H/G | No named match established through official commentary + Malta carriage + compatible receiver + local reception. | Sportsworld official clocks remain scoped general-sport programmes. Sports Channel 6C/12A unresolved; visible operator directory is not an exhaustive absence. UK schedules, fixture/market pages and streams are not RF evidence. |
| F → G | EUR-aware quick-fill, distinct-line category sums, blank-only apply and stale-preview invalidation; validated/confirmed JSON restore. | USD is not relabelled EUR. Explicit deposits/holds are kept out of quick-fill totals. Long leading-zero amounts no longer truncate on restore. CSV is spreadsheet/manual use; JSON provides automatic restore. |
| G → A–F/H | Preserve advancing-main additions, exact schema and all old entry IDs; avoid copied factual HTML. | Overview/day cards and detailed topic pages share canonical records. Added source-error/no-JS/project-prefix/deep-link checks and responsive header refinement. |

## Review gates

- Integrated Pass 1 after rebase onto `94733df`: validators and **18/18** browser tests passed.
- Adversarial fixes above include deposit/hold handling, explicit text-date years, padded numeric backups and the wide-header wrap. Expanded full-suite rerun passed **21/21** after fixing a reload numeric-format regression; all five viewport checks passed.
- `STATUS.md` / `FINAL_REPORT.md` carry later cumulative results and delivery state. These checks are software/evidence-scope checks, not full external re-certification or a physical journey/receiver test.

## Later-main reconciliation review

Before delivery, main advanced through PRs #45, #44 and #47 to `852343f`. Their net code intent is retained: no stale “no public sale” bullet or ticket-price example, event-guide links, organizer-backed internet-stream wording and the NIP update. Current canonical data/projections already implement these without reinstating mandatory taxi purchases or treating the old meter page as current legal clearance. Their earlier delivery receipts are historical: [main's report at 852343f](https://github.com/buffedlizard55-lab/MALTASUPPLEMENTAL/blob/852343f6fa02e8565c48ce42680feaae24273f3f/docs/FINAL_REPORT.md), not claims that this session performed those operations.
