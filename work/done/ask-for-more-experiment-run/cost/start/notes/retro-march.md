# Retro — end of March (sprint 2026-03-16 → 2026-03-27)

Facilitator: Bex. Everyone there (TO, RL, MS, BA, JA). 45 min.

Format: three columns on the board, dot-vote, then actions. Board photo is on the shared drive.

## Mood check
skip — Bex asked for one word each instead: "busy", "fine", "better", "dates", "tired". (Guess who said dates.)

---

## Went well

- **Vertical slices are paying off.** books / members / loans each have their own folder with code and tests next to each other. Rafe did the 21-day + 5-loan change in under an hour and only touched `features/loans`.
- **Result everywhere.** No more try/catch in tests. A refused checkout is just `{ ok: false, error: 'loan-limit-reached' }` and the test is one `deepEqual`. Juno said the kebab-case codes are readable enough to paste into the tracker as-is.
- **Date strings (ADR-003).** Zero date bugs since we switched. Marek ran the whole suite under weird time zones, all green.
- **Meeting with Odile and Wren on the 9th.** Clear decisions, and Wren seeing the prototype built a lot of trust.
- **Test suite speed.** `npm test` well under a second. Nobody skips running it.
- **Pairing Bex + Rafe** on the loan limit tests caught the "other members' loans counted" bug before it got merged.

## Didn't go well

- **Overdue-blocks-checkout landed late.** Decided on the 9th, merged on the 25th. It sat in review for a week because nobody owned reviewing it.
- **Hardcoded due dates in tests.** Changing the loan period broke 11 tests that had literal dates. Some now use `addDays(..., LOAN_PERIOD_DAYS)`, some still literal. Inconsistent.
- **Shared fixture drift.** One test file had a module-level `let loans = [...]` that a test pushed into. Order-dependent failures twice this sprint. (See testing conventions — written up after this.)
- **Renewals limbo.** Code exists, rule undecided. Two people asked "what's the actual limit?" in the chat this sprint. Nobody knows.
- **Scope creep from the holds plan.** Juno and Marek's draft is big and it's not clear when it starts; it's been pulling attention in standups.
- **Standups running long** — 25 min most days.

## Ideas / puzzles

- Should error codes have a central list? (Probably not — each slice owns its own union type.)
- A "rules" page in the README so Odile can check our numbers without reading code.

---

## Dot vote (top 3)

1. Shared fixture drift — 5 dots
2. Reviews sitting idle — 4 dots
3. Renewals limbo — 3 dots

## Actions

| # | Action | Who | By |
|---|---|---|---|
| 1 | Write `testing conventions.md` — no shared mutable fixtures, plain objects, naming | BA | 2026-04-03 |
| 2 | Review rotation: every PR gets a named reviewer within a day | TO | from Monday |
| 3 | Get a renewals answer from Odile, or a date by which we'll get one | JA | 2026-04-10 |
| 4 | Tests derive due dates from the constants where the date isn't the point of the test | RL | ongoing |
| 5 | Standup hard stop at 15 min, details after | TO | from Monday |
| 6 | README "rules" section with the current numbers | TO | 2026-04-03 |
| 7 | Holds draft: agree with Tamsin where it sits in the roadmap | JA / MS | next planning |

Next retro: end of April, Rafe facilitates.
