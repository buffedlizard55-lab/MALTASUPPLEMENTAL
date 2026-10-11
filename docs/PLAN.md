# Malta trip guide — delivery plan

**Session:** 11 October 2026 (UTC) · branch `arena/dfefc16f-maltasupplemental` · reviewed baseline `b307c51`.

## Repository review and approach

The repository already contains a static GitHub Pages site, six 13-field JSON datasets, a shared renderer/CSS/navigation, a browser-local expense planner, a source log and Playwright checks. GitHub reports Pages publishing from `main` at `/`. Preserve useful work and source history, but do not equate inherited `verified` labels or passing tests with fresh source verification. The existing executive summary is too long, repeats topic facts in HTML, and contains prior-session delivery language. This session will simplify the entry point, audit inherited evidence, and strengthen planning and tests.

### Shared setup — serial, before workstreams

- Retain root topic pages, `data/`, `docs/`, `css/`, `js/`, `scripts/`, `tests/` and `.github/workflows/` (no framework migration).
- Retain the exact record schema in `data/record.schema.json`: `id`, `name`, `category`, `area`, `address`, `hours`, `price range`, `description`, `source_url`, `source_type`, `date_checked`, `confidence`, `notes`.
- Retain `official/map/review/social` and `verified/partially verified/unverified`. Record claims, access method and limitations; do not bump a source-check date just for editing a record.
- G alone owns shared shell/navigation, CSS tokens, rendering, summary and source/audit documentation. Summaries must cite/render canonical records rather than introduce unsupported facts.
- Append dated source-log entries in the format **claim | URL | date accessed/attempted | workstream | access result / limitations**. Preserve historical attempts as historical, not current verification.
- Record cross-topic discoveries in `docs/HANDOFF.md`; missing/blocked evidence in `docs/OPEN_QUESTIONS.md`.

## Ownership and dependencies

| Stream | Owned data | Owned page | Scope / dependencies |
|---|---|---|---|
| A · Transport | `data/transport.json` | `getting-around.html` | Airport, Qawra ↔ BLAST/MFCC, event-day buses and return, fares/cards, ride-hailing, rentals/ferries, mode trade-offs. Depends on C's dated event and gate evidence; no invented walks or journey times. |
| B · Food & cafés | `data/food.json` | `restaurants.html` | Hotel/nearby eating, cafés, closures and dated review/social evidence. Depends only on shared schema; no unsupported popularity rankings. |
| C · Activities & events | `data/activities.json` | `activities.html` | Hotel, CS2, public gaming, landmarks and trip-window events. Send gate/timing issues to A via handoff. |
| D · Everyday life | `data/everyday.json` | `everyday.html` | US power/device needs, connectivity, money/tipping, health/safety, entry/customs, language/weather. Distinguish general guidance from personal eligibility. |
| E · Sports radio | `data/radio.json` | `radio.html` | Malta terrestrial FM/AM/DAB+, station schedules, named trip-date commentary, reception and Kalshi-market limitations. UK/online schedules do not establish Malta reception. |
| F · Expenses | `data/expenses.json` | `costs.html` | Blank-by-default, quick itinerary intake, budget/actual totals, persistence/export/restore and error cases. Depends on A–D only for reference prompts, never presumed purchases. |
| G · Integration (last) | Shared files only | `index.html`, `sources.html`, legacy page notices | Concise data-backed executive summary, responsive navigation/design, source log, evidence review, tests, README, final report and GitHub delivery. Depends on A–F. |

## Conflict avoidance and execution

The Arena session is fixed to the branch above. Creating workstream branches, switching to `main`, or pushing another branch is not permitted here. No sub-agent runner is available. A–F therefore operate as isolated, sequential file-owned workstreams; independent read-only research/test commands may run in parallel. No claim is made that autonomous agents or separate branches were used. G integrates serially after A–F. Fetch the current `main` and rebase this session branch before the PR if needed; do not alter unrelated open PRs.

## Verification and delivery gates

1. **Topic self-checks:** examine every record for provenance/qualification and each changed claim against accessible evidence. Test internal links; attempt external sources and record unavailable/blocked access honestly. Source presence is not proof of the claim.
2. **Integration check:** topic data/page parity, navigation/deep links, expense behavior, narrow/mobile/tablet/desktop layout and accessibility.
3. **Pass 1 — implement and verify:** complete topic changes and integration; run all local checks.
4. **Pass 2 — adversarial review:** find unsupported claims, duplicated/stale summary text, false bus/radio certainty, data failures, malformed saved/imported expense data and edge cases; fix and rerun.
5. **Pass 3 — original-request audit:** map every requirement to delivered files/tests or an explicit limitation; inspect diff and final test results. Never describe inaccessible evidence, live reception or personal bookings as verified.
6. Commit and push **only** the fixed session branch; open a numbered PR, wait for its checks, then merge that explicit PR as requested if GitHub rules allow it. Verify the merge and Pages deployment through GitHub. Report limitations and prioritized next-session tasks, not a blanket “no hallucinations” guarantee.

## Advancing-main integration

Fetched `origin/main` at `94733df` after A–F/G implementation. PRs #42/#43 added the event dataset/page expansion, TQ service and taxi references, and hotel FAQ evidence. Rebase this session onto that commit, preserve those additions with the same 13-field schema, recheck the consequential claims and log corrections through G. The retained upstream extension is labelled H in status/audit records; no new H branch or parallel agent was created here. Repeat all integrated checks after resolution. Unrelated open PRs are not merged or closed by this session.

Delivery recheck found further main updates at `852343f` (PRs #45/#44/#47). Review their limited diff and rebase again before opening the delivery PR. Preserve the free-reservation, NIP, event-link and official-stream corrections through the canonical data rather than restoring duplicated old prose; preserve prior delivery receipts through Git history links.

## Observed execution gates

Both rebases were completed; all upstream record IDs are preserved. Pass 1 passed 18/18 browser checks, Pass 2 passed the expanded 21/21 after adversarial fixes, and Pass 3 passed 21/21 again after the latest-main rebase plus schema/link/JS/diff checks and the original-request matrix. [PR #49](https://github.com/buffedlizard55-lab/MALTASUPPLEMENTAL/pull/49) is open and its initial CI passed. Check the final pushed head before an explicit numbered merge; record merge/Pages observations in the PR delivery receipt, not as future facts in these pre-merge documents. Full external re-verification remains expressly incomplete.
