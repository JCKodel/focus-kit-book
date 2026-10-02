# Hollowmere Lending Library

This is a TypeScript domain model of the lending rules for the Saltgate branch. It replaces "CardBox" (paper cards and spreadsheets). It has no UI, no persistence and no dependencies. It runs on Node ≥ 26 with type stripping. Tests: `npm test`.

Odile signed off the rules on 2026-09-01. Since then they are **frozen unless Odile asks**, and changes go through Juno.

The code is the truth. `notes/` holds about 30 notes from Jan–Sep 2026, and many of their rules were later changed. This file says what is current, so open only the notes a task needs.

## Answering questions

Developers and Juno (product owner, not a developer) ask about 20 questions a day, each in a fresh session. They want a quick answer.

- **Short.** Answer in one or two plain sentences, then the evidence: `file:line` and the deciding note with its date. Usually five lines or fewer; go longer only if asked. For Juno, say the rule the way a librarian would.
- **Confirm in the code** before quoting a number. If the code and this file disagree, the code wins; say this file is stale.
- **If they cite an old note**, say what replaced it and when.
- **If something was never decided, or isn't in the repo, say so.** Don't guess.
- **Don't edit anything when answering a question**, not even a note you know is wrong. Point out the problem and who owns it. Change files only when someone explicitly asks for a change.
- **Refer to people by name**, or as "they". The notes don't state anyone's pronouns.
- **"When was X built / which commit?"** can't be answered from git. The history starts with a single import commit on 2026-10-02, so use the dated notes instead. A note's author is in its header.
- **Check for changes since this file was written.** Do this once, and only for questions about rules or plans. Run these from the repo root exactly as written (no `cd`, no `-C`):
  `git log --oneline --name-only 96ddc80..HEAD -- notes features shared` and `git status --short -- notes features shared`.
  If both print nothing, this file is current. If `git log` fails with `bad revision`, the history was rewritten: use `git log --since=2026-10-02` instead. If the commands are denied, add one line at the end of your answer saying the check couldn't run. Otherwise, read the changed files that touch the question; the newer decision wins. End your answer with: *"`CLAUDE.md` is out of date: `<file>` changes <rule>."*

## Current rules

| rule | value | where | decided |
|---|---|---|---|
| Loan period | 21 calendar days | `LOAN_PERIOD_DAYS`, `features/loans/loan.ts` | Mar 9 meeting |
| Max active loans | 5; returned loans and other members' loans don't count | `MAX_ACTIVE_LOANS` | Mar 9 |
| Renewals | max 2; adds 21 days to the **due date**, not to today; allowed on the due date; refused if overdue, suspended or returned | `renewLoan` | `decision-renewals.md` (Mar 30) |
| Overdue | from the day **after** the due date | `isOverdue` | bug note (Jun 2) |
| Overdue blocks checkout | any overdue loan → `member-has-overdue-loans`; no grace period; the member can still renew loans that aren't overdue | `checkOut` | Jun 16 meeting |
| Refusal order | checkout: suspended → overdue → limit → withdrawn → on loan. Renewal: returned → suspended → overdue → limit | `checkOut`, `renewLoan` | Jun 16, Mar 30 |
| Returns | always accepted; only `already-returned` and `copy-mismatch` can fail | `returnCopy` | Feb 11 |
| Suspension | any loan **more than 14** days overdue (15 counts, 14 doesn't). A librarian runs `applySuspensions` (Wren, Mondays); librarian, date and reason are recorded. Nothing automatic | `features/loans/suspension.ts` | May 19, Apr 8 |
| Lifting a suspension | any librarian, once nothing is overdue (`still-has-overdue-loans`); not automatic on return | `liftSuspension` | May 19 |
| Fines | **none**; council policy | — | ADR-004 |
| Copies | `available` / `on-loan` / `withdrawn`. Lost or damaged copies are withdrawn; only available copies can be withdrawn; can't be undone (re-add as a new copy) | `features/books/book.ts` | `copies-and-withdrawal.md` |
| ISBN | optional; ISBN-13 only, hyphens and spaces stripped, check digit validated | `createBook` | `cataloguing chat 22 apr.md` |
| Members / librarians | a member is name + email (normalised). Librarians are separate staff records; staff borrow as ordinary members | `features/members/` | Feb 11, `librarians-vs-members.md` |
| Dates | `"YYYY-MM-DD"` strings via `shared/dates.ts`; `today` always passed in; closed days are not skipped | `shared/dates.ts` | ADR-003, `holiday closures.md` |
| CardBox | not imported; loans will be re-entered by hand | — | `cardbox migration thoughts.md` |

Full vocabulary: `notes/glossary.md`. All error codes: `notes/error codes list.md`. Both match the code.

## Old rules still found in the notes

- 14-day loans, max 3 loans, unlimited renewals, fines of 0.20/day: from the kickoff (Jan 12), all replaced.
- Suspend at 28 days (Feb 11, Apr 8, `questions for odile.md`) or 30 days with a nightly job (holds draft): replaced by more than 14 days, run by a librarian (May 19).
- Only Odile can reinstate (Jan 26, Feb 11, Apr 8): replaced by any librarian once nothing is overdue (May 19).
- Overdue members can borrow until suspended (Apr 8, questions Q2): replaced by the Jun 16 rule.
- Statuses `lost` / `damaged` (Jan 26): replaced by `withdrawn` (Apr 28).
- Layers, thrown errors and `Date` objects in `Loan Service Design (draft).md`: replaced by slices (ADR-001), `Result` (ADR 2) and date strings (ADR-003). The draft is only a starting point for the Q4 persistence work.

## Known errors in the notes

- `retro-march.md` says overdue-blocks-checkout was merged in March. That's wrong: the Jun 16 note introduced it and describes the earlier behaviour as "since April".
- `2026-06-16 meeting.md` gives the April threshold as 14 days; it was 28 then.
- `questions for odile.md` lists Q7 and Q15 as open, but `copies-and-withdrawal.md` answered both. Q11 (deleting members) is still open.

## Not in the repo (say so, and name who has it)

- `rafe-notes-error-handling.md`: Rafe
- the plain-English rules list: Bex
- plain-language error messages: Juno
- the council's decision on fines in writing: Juno
- the persistence options write-up (due Sep 22): Tamsin
- the guide to reading CardBox loan cards: Marek
- the tracker and the team chat

## Open or not built

- Holds: `holds-and-reservations-DRAFT-v2.md` is a draft only and conflicts with current rules. Review in December.
- Deleting members: still open.
- Re-entering old 14-day loans: Odile to decide.
- Q4 plan: persistence → reports (overdue report first) → desk UI.

## People

Odile Fenwick: head librarian, client. Wren Halloway: desk librarian. Juno Achterberg: product owner. Tamsin Oduya: tech lead, approves dependencies. Rafe Lindqvist and Marek Szolt (dates, suspension): developers. Bex Amadi: tests, owns the error-codes list.

## Code conventions

- Code is in vertical slices `features/{books,members,loans}`, with tests alongside. `shared/` is only `result.ts` and `dates.ts`. Loans may import from books and members, never the other way round.
- Business failures return `Result` with kebab-case codes; only bugs throw. A new code needs: the union type, a test, and a line in `notes/error codes list.md`.
- No `enum` or `namespace`; imports use `.ts` extensions and `import type` for types; no dependencies.
- Tests use `node:test` and `node:assert/strict` with plain objects. No mocks, no shared mutable fixtures. Test names are plain sentences.

## Keeping this file current

When a decision note lands:
1. Update its row in **Current rules** and, if needed, **Old rules**.
2. Replace `96ddc80` in the change check with the new commit hash.

Nothing else here needs regular upkeep.
