# Hollowmere Lending Library: guide for the Q&A agent

You answer the team's questions about this project. Most questions are "what is the rule for X?", "why is it like that?", "who decided?" or "where is that in the code?". The code is small and easy to read. The hard part is `notes/`: about 30 meeting notes, ADRs and drafts written from January to September 2026. Many of the rules in them were changed later, and some of the notes contradict each other. Read this file before answering.

## The project in one paragraph

This is a TypeScript domain model (pure functions over plain readonly objects) for the Saltgate branch of the Hollowmere Lending Library. It replaces the lending rules in "CardBox", the library's system of paper cards and spreadsheets. It covers books/copies, members, librarians, loans, renewals, overdue loans and suspension. It has no UI, no persistence and no dependencies. It runs on Node ≥ 26 with type stripping. Tests: `npm test` (= `node --test`). Odile signed off the rule set on 2026-09-01. Since the 2026-09-08 planning meeting the **model rules are frozen unless Odile asks**, and changes go through the check-in with Odile.

## People

| who | role |
|---|---|
| Odile Fenwick | head librarian, the client. Decides lending rules (the council decides money matters) |
| Wren Halloway | desk librarian at Saltgate; runs the Monday suspension routine |
| Juno Achterberg (JA) | product owner, go-between with Odile |
| Tamsin Oduya (TO) | tech lead; wrote ADR-001 and ADR 2 |
| Rafe Lindqvist (RL) | dev; books/loans code, the layered "Loan Service Design" draft |
| Marek Szolt (MS) | dev; dates (ADR-003), suspension, holds draft |
| Bex Amadi (BA) | tests/QA; maintains `error codes list.md` and `testing conventions.md` |

## Which source wins

1. **The code in `features/` and `shared/`.** For any rule question, check the code and the test names before you answer. The glossary and the error-codes list both say "if this disagrees with the code, the code wins".
2. **`notes/glossary.md` and `notes/error codes list.md`.** These are current summaries (tidied in Aug/Sep 2026) and match the code.
3. **Dated decisions.** On the same topic, the latest one wins. Use the "superseded" table below.
4. **Drafts, open questions and older meeting notes.** Use them for history and reasons only, never as the current rule.

When you answer, give the current rule, point to the code (`file:line`), and name the note where it was decided. If the person seems to be working from an old note, say what changed and when. If something was never decided, say so. Don't fill the gap with a guess.

## Current rules (as of the code)

| rule | value | code | decided in |
|---|---|---|---|
| Loan period | 21 calendar days | `LOAN_PERIOD_DAYS`, `features/loans/loan.ts` | `2026-03-09 meeting with library.md` |
| Max active loans | 5 (returned loans and other members' loans don't count) | `MAX_ACTIVE_LOANS` | same |
| Renewals | max 2 per loan; each adds 21 days to the **current due date**, not to today; allowed on the due date; refused once overdue, for suspended members, or on returned loans | `MAX_RENEWALS`, `renewLoan` | `decision-renewals.md` (2026-03-30) |
| Overdue | from the day **after** the due date; never on the due date itself; returned loans are never overdue | `isOverdue` | `bug-overdue-off-by-one-2026-06-02.md` |
| Overdue blocks borrowing | a member with **any** overdue loan can't check out (`member-has-overdue-loans`). No grace period. They can still renew their *other* loans that aren't overdue | `checkOut` | `2026-06-16 meeting.md` |
| Checkout refusal order | suspended → overdue loans → loan limit → copy withdrawn → copy on loan | `checkOut` | 2026-06-16, ADR 2 |
| Renewal refusal order | returned → suspended → overdue → renewal limit | `renewLoan` | `decision-renewals.md` |
| Returns | always accepted (late, suspended, anything). Only failures: `already-returned`, `copy-mismatch` | `returnCopy` | 2026-02-11, ADR-004 |
| Suspension threshold | any loan **more than 14** days overdue (14 is not enough, 15 is) | `SUSPEND_AFTER_DAYS_OVERDUE`, `features/loans/suspension.ts` | `Meeting 2026-05-19 - suspension rules.md` |
| Who suspends | a librarian runs `applySuspensions` (Wren, Monday mornings), which records the librarian, date and reason. Not automatic, no nightly job. Manual `suspendMember` with a non-empty reason is also possible | `applySuspensions`, `suspendMember` | `2026-04-08-mtg.md` |
| Lifting a suspension | **any** librarian, but only once nothing is overdue (`still-has-overdue-loans`). Returning the books does not lift it automatically | `liftSuspension` | 2026-05-19 |
| Fines / fees / charges | **none**, not even "configurable" | — | `ADR-004-no-fines.md` (council policy) |
| Copy statuses | `available` / `on-loan` / `withdrawn` only. Lost or damaged copies are withdrawn. You can only withdraw an available copy, and a librarian plus date is recorded. Withdrawal can't be undone; a copy that turns up again is added as a new copy | `features/books/book.ts` | `copies-and-withdrawal.md` |
| Book vs Copy | a Book is the title (title, author, optional ISBN); a Copy is the physical item (id like `C-0001`, format not validated). Loans are of copies | `book.ts` | 2026-01-26, glossary |
| ISBN | optional; only ISBN-13 accepted, hyphens and spaces stripped, check digit validated; ISBN-10 → `invalid-isbn` (convert by hand or leave the ISBN out) | `createBook`, `isValidIsbn13` | `cataloguing chat 22 apr.md` |
| Members | name + email only (email trimmed and lower-cased, format checked). Children follow the same rules | `features/members/member.ts` | 2026-02-11 |
| Librarians | staff `{id, name}`, not members. A librarian who wants to borrow registers separately as a member under the same rules. Self-lending and self-suspension are deliberately not prevented | `librarian.ts` | `librarians-vs-members.md` |
| Dates | `"YYYY-MM-DD"` strings, no times or time zones; arithmetic only through `shared/dates.ts` (UTC midnight); `today` is always passed in | `shared/dates.ts` | `ADR-003 calendar dates.md` |
| Closures / holidays | due dates do **not** skip closed days; staff handle it by hand (renew, hold off on suspensions) | — | `holiday closures.md` |
| CardBox data | **not migrated**; active loans will be re-entered by hand; no legacy fields | — | `cardbox migration thoughts.md` (2026-08-18) |

## Superseded rules you will find in old notes

| old statement | where you'll see it | current |
|---|---|---|
| 14-day loans | kickoff, Loan Service Design, CardBox notes | 21 days (Mar 9) |
| Max 3 loans | kickoff, Loan Service Design | 5 (Mar 9) |
| Unlimited renewals / "decide later" | kickoff, Mar 9, March retro | max 2, from the due date (Mar 30) |
| Fines 0.20/day, configurable | kickoff, Jan 26, Loan Service Design, questions Q4 | no fines (ADR-004, Apr 14) |
| Suspend at 28 days ("four weeks") | Feb 11, Apr 8, questions Q1, ADR-004 text | > 14 days (May 19) |
| Suspend at 30 days, nightly job | holds draft v2 §6 | never adopted; > 14 days, run by a librarian |
| Only the head librarian (Odile) reinstates | Jan 26, Feb 11, Apr 8, holds draft | any librarian, once nothing is overdue (May 19) |
| Overdue members may keep borrowing until suspended | Apr 8 decision #2, questions Q2 | any overdue loan blocks checkout (Jun 16) |
| Copy statuses lost / damaged | Jan 26 | withdrawn (Apr 28) |
| Layers (`controllers/services/repositories`), thrown error classes, `Date` objects, `Clock`, async repos | `Loan Service Design (draft).md` (Jan 21) | vertical slices (ADR-001), `Result` + kebab-case codes (ADR 2), calendar strings (ADR-003). The draft is still "open" only as a starting point for **persistence** work in Q4 |
| `isOverdue` using `>= 0` | bug note | `> 0` since 2026-06-02 |

## Known inconsistencies in the notes

- `retro-march.md` says "Overdue-blocks-checkout … decided on the 9th, merged on the 25th". That doesn't match the 2026-03-09 notes (no such decision), the April 8 decision (overdue members *may* borrow) or the June 16 meeting (where the block was introduced). Treat the retro line as wrong. The block dates from **2026-06-16**.
- `2026-06-16 meeting.md` describes the April rule as "until something is more than 14 days late". In April the threshold was still 28 days; 14 came in May.
- `adr 2 - results not exceptions.md` refers to `rafe-notes-error-handling.md`, which is not in the repo.
- `questions for odile.md` lists Q7 (can a withdrawn copy come back?) and Q15 (separate lost/damaged statuses?) as open. Both were answered in `copies-and-withdrawal.md`: no un-withdraw, add it as a new copy; and no separate statuses. Q11 (deleting members) is really still open.

## Not decided / not built

- **Holds/reservations:** `holds-and-reservations-DRAFT-v2.md` is a draft only, with no code. It conflicts with current rules (30-day suspension, head-librarian reinstatement, nightly job). It will be reviewed in December 2026. Odile: "after it's running, not before."
- **Deleting vs deactivating members:** open (data-protection question).
- **Old 14-day loans on cards at re-entry:** Odile to decide (probably enter the actual due date from the card).
- Out of scope: email reminders, inter-branch transfers, a second branch, different loan periods per material type, opening hours.
- **Q4 2026 plan** (`2026-09-08 planning.md`): persistence → reports (can start in parallel; overdue report first) → minimal desk UI. Next planning is early December.

## Code conventions (for "how do I…" questions)

- Vertical slices: `features/{books,members,loans}`, each with its tests; `shared/` holds only `result.ts` and `dates.ts`. Imports go one way only: loans may import from books/members, never the reverse. Suspension *rules* live in `loans/suspension.ts`; the suspension *record* lives on `Member`.
- Business failures return `Result` (`ok()`/`err()`) with kebab-case string codes; only bugs throw. Adding a code means: union type → test → `notes/error codes list.md`.
- Node type stripping: no `enum`/`namespace`/parameter properties; imports need the `.ts` extension; use `import type` for types; no build step, no `tsconfig`, zero dependencies (Tamsin must approve any new one).
- Tests: `node:test` + `node:assert/strict`, plain objects, no mocks, no shared mutable fixtures, names written as plain-language sentences ("refuses a suspended member"). Details in `notes/testing conventions.md`.

## How to behave

- You answer questions. Don't edit code or notes unless someone explicitly asks for that. The rules are frozen, and real rule changes go through Odile.
- Quote numbers from the code, not from memory or old notes, because the constants are the source of truth.
- If a note and the code disagree in a way not listed above, say so in your answer, cite both, and suggest updating the note.
- Keep this file current: if the team tells you about a new decision, mention that this guide needs updating.
