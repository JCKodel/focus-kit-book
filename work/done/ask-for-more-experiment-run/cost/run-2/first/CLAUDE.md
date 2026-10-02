# Hollowmere Lending Library — guide for answering questions

A TypeScript domain model (no UI, no storage) of lending at the Saltgate branch of the Hollowmere Lending Library: books and copies, members, librarians, loans, renewals, overdue, suspension. Built by a small team for Odile Fenwick (head librarian). The rules are frozen as of the 2026-09-08 planning meeting; changes go through Odile's check-in.

You will mostly be asked questions by the team ("what's the renewal limit?", "why don't we have fines?", "can a librarian reinstate someone?"). This file tells you where the answers are and which sources to trust.

## Source of truth, in order

1. **The code and tests** (`features/`, `shared/`). If anything disagrees with the code, the code wins. Both `notes/glossary.md` and `notes/error codes list.md` say so explicitly.
2. **The latest decision** on a topic, by date. The rules changed a lot between January and June 2026; older notes are full of numbers that are no longer true. Use the supersession table below.
3. **`notes/glossary.md`** (tidied early Sep 2026) and **`notes/error codes list.md`** (checked 2026-08-24). These are current summaries.
4. Everything else in `notes/` is history: meeting minutes, drafts, and scratch notes. Use them for the *why* and the *who*, not for current numbers.

How to answer:
- Check the actual constant or function before stating a number or rule. Cite it as `file:line`.
- For "why" questions, cite the note that made the decision, with its date.
- If an older note says something different, say that the rule changed, when, and where. People often remember the old rule.
- If something was never decided, or is only in a draft, say that. Don't present draft content (holds, Loan Service Design) as how the system works.
- Git history has a single commit ("start"), so it can't tell you who changed what. The notes are the record.
- `npm test` (= `node --test`, Node ≥ 26, no install step) runs everything in about a second. Run it if a question depends on whether behaviour actually works.
- You are answering questions, not changing the project. Don't edit code or notes unless someone asks you to.

## Current rules (verify against code before quoting)

| Rule | Value | Where |
|---|---|---|
| Loan period | 21 days, plain calendar days (closures not skipped) | `LOAN_PERIOD_DAYS`, `features/loans/loan.ts` |
| Max active loans per member | 5 (returned loans and other members' loans don't count) | `MAX_ACTIVE_LOANS`, `loan.ts` |
| Renewals | max 2 per loan; adds 21 days to the **current due date**, not to today; allowed on the due date; not allowed once overdue | `MAX_RENEWALS`, `renewLoan`, `loan.ts` |
| Overdue | from the day **after** the due date; never overdue on the due date itself | `isOverdue`, `loan.ts` |
| Checkout refusals, in this order | `member-suspended` → `member-has-overdue-loans` → `loan-limit-reached` → `copy-withdrawn` → `copy-not-available` | `checkOut`, `loan.ts` |
| Renewal refusals, in this order | `already-returned` → `member-suspended` → `loan-overdue` → `renewal-limit-reached` | `renewLoan`, `loan.ts` |
| Returns | always accepted (overdue, suspended, anything); only fail on `already-returned` / `copy-mismatch` | `returnCopy`, `loan.ts` |
| Suspension threshold | any loan **more than** 14 days overdue (14 = no, 15 = yes) | `SUSPEND_AFTER_DAYS_OVERDUE`, `features/loans/suspension.ts` |
| Who suspends | a librarian runs `applySuspensions` (not automatic, no nightly job); librarian, date and reason are recorded. Manual `suspendMember` with a reason also exists | `suspension.ts`, `features/members/member.ts` |
| Lifting a suspension | **any** librarian, only once nothing is overdue (`still-has-overdue-loans`); returning the last book does not lift it automatically | `liftSuspension`, `suspension.ts` |
| Copy statuses | `available` / `on-loan` / `withdrawn` only. Lost and damaged copies are withdrawn. Can't withdraw an on-loan copy; withdrawal is one-way | `features/books/book.ts` |
| ISBN | optional; ISBN-13 only, hyphens and spaces stripped, check digit validated; ISBN-10 is rejected | `createBook`, `isValidIsbn13`, `book.ts` |
| Members | name + email (trimmed, lower-cased, format check). Nothing else stored | `registerMember`, `member.ts` |
| Librarians | `{ id, name }`, staff, separate from members. No head-librarian role in the model. Staff who borrow register as ordinary members | `features/members/librarian.ts` |
| Fines | none. No fines, fees, or replacement charges | ADR-004 |

All error codes, with which function returns each one, are listed in `notes/error codes list.md`.

## Rules that changed: what older notes get wrong

| Topic | Old (where you'll see it) | Current (decided in) |
|---|---|---|
| Loan period | 14 days (kickoff 01-12, Loan Service Design, CardBox notes) | 21 days (`2026-03-09 meeting with library.md`) |
| Loan limit | 3 (kickoff, Loan Service Design) | 5 (2026-03-09) |
| Renewals | unlimited (kickoff, Loan Service Design); "decide later" (03-09) | max 2, from due date (`decision-renewals.md`, 03-30) |
| Fines | "likely 0.20/day, configurable" (kickoff, 01-26, Loan Service Design, questions Q4) | none (`ADR-004-no-fines.md`, 04-14) |
| Suspension threshold | 28 days / "four weeks" (02-11, 04-08, questions Q1, ADR-004); 30 days (holds draft, never adopted) | more than 14 days (`Meeting 2026-05-19 - suspension rules.md`) |
| Reinstatement | head librarian only (01-26, 02-11, 04-08, holds draft) | any librarian once nothing is overdue (05-19) |
| Overdue member borrowing | allowed until suspended (questions Q2 on 02-11, `2026-04-08-mtg.md`) | refused with `member-has-overdue-loans` (`2026-06-16 meeting.md`) |
| Copy statuses | 5 including `lost`, `damaged` (01-26) | 3 (`copies-and-withdrawal.md`, 04-28) |
| Overdue on the due date | was overdue (bug, May–June 2) | not overdue (`bug-overdue-off-by-one-2026-06-02.md`) |
| Suspension automatic? | automatic flag (02-11); nightly job (holds draft) | a librarian runs it (04-08, confirmed 05-19) |
| Dates | `Date` objects, 23:59 local (Loan Service Design) | `"YYYY-MM-DD"` strings (`ADR-003 calendar dates.md`) |
| Errors | thrown error classes (Loan Service Design) | returned `Result` with kebab-case codes (`adr 2 - results not exceptions.md`) |
| Code layout | controllers/services/repositories (Loan Service Design) | vertical slices (`ADR-001-vertical-slices.md`) |

Known inconsistencies in the notes. Mention these if a question touches them.
- `retro-march.md` says "overdue-blocks-checkout" was decided on 03-09 and merged on 03-25. That's wrong. The 03-09 meeting only asked for a UI warning, the 04-08 meeting explicitly allowed overdue members to borrow, and the block came in on 06-16.
- The 06-16 notes say a pointer was added to the 04-08 note. No such pointer is in `2026-04-08-mtg.md`.
- `adr 2 - results not exceptions.md` (dated 02-10) shows `member-has-overdue-loans` in its example, but that code was added on 06-16. It also links to `rafe-notes-error-handling.md`, which isn't in the repo.
- There is no file called `ADR-002`. ADR 2 is `adr 2 - results not exceptions.md`.

## Notes index

Current and authoritative:
- `glossary.md`: vocabulary plus current rules. Best single summary.
- `error codes list.md`: every error code and the order of checks.
- `ADR-001-vertical-slices.md`: layout. `loans` may import from `books`/`members`, never the other way round. `shared/` holds only `result.ts` and `dates.ts`.
- `adr 2 - results not exceptions.md`: business failures are returned `Result`s, never thrown.
- `ADR-003 calendar dates.md`: dates are strings, UTC arithmetic, `today` is always passed in.
- `ADR-004-no-fines.md`: no money anywhere (council policy, not a technical choice).
- `decision-renewals.md`, `copies-and-withdrawal.md`, `librarians-vs-members.md`, `cataloguing chat 22 apr.md` (ISBN), `holiday closures.md` (07-14, due dates don't skip closures; staff handle them by hand), `cardbox migration thoughts.md` (08-18, no import: active loans get re-entered by hand).
- `Meeting 2026-05-19 - suspension rules.md`, `2026-06-16 meeting.md`: current suspension, reinstatement and overdue-checkout rules.
- `bug-overdue-off-by-one-2026-06-02.md`: why the overdue boundary is `> 0`.
- `testing conventions.md`, `node-26-typescript-notes.md`: how to write and run code and tests (no enums, `.ts` import extensions, `import type`, zero dependencies).
- `2026-09-08 planning.md`: latest status and the Q4 roadmap: (b) persistence → (c) reports → (a) desk UI. Holds will be revisited in December.

Drafts, not implemented. Don't describe them as current behaviour:
- `holds-and-reservations-DRAFT-v2.md`: no code exists. Its suspension, reinstatement and nightly-job sections are out of date.
- `Loan Service Design (draft).md` (01-21): almost everything in it has been superseded (layers, `Date`, exceptions, fines, 14/3/unlimited). The 09-08 planning names it as a starting point for the persistence work only.

Historical (useful for "why" and "when"): `2026-01-12 kickoff.md`, `meeting_2026_01_26.md`, `mtg-2026-02-03-architecture.md`, `2026-02-11 meeting.md`, `2026-03-09 meeting with library.md`, `2026-04-08-mtg.md`, `retro-march.md`, `marek - dates notes.md` (scratch; ADR-003 is the decision), `questions for odile.md` (several answers are now outdated, see the table above. Q7 and Q15 were later answered in `copies-and-withdrawal.md`. Q11, deleting members, is still open).

## Out of scope / not built

Fines (never). CardBox import (decided against). Opening hours and closures. Email reminders. Holds/reservations (draft only). Persistence, UI, reports (planned for Q4 2026, not started in this repo). A second branch. A head-librarian role. Children's cards have the same rules as everyone else.

Still open: whether members can be deleted (data protection, parked). Whether old 14-day loans keep their card due date when re-entered (Odile; probably yes). Holds design questions (see the draft).

## People

- Odile Fenwick: head librarian, the client. Decides lending rules.
- Wren Halloway: librarian at the Saltgate desk. Runs suspensions on Mondays.
- Juno Achterberg (JA): product owner. Brokers with Odile.
- Tamsin Oduya (TO): tech lead. Owns ADR-001 and approves new dependencies.
- Rafe Lindqvist (RL): developer. Loans code, Loan Service Design.
- Marek Szolt (MS): developer. Dates, ADR-003, holds draft.
- Bex Amadi (BA): tests, testing conventions, error codes list, glossary.

## Layout

```
features/books/    book.ts (Book, Copy, ISBN, withdraw)            books.test.ts
features/members/  member.ts (register, suspend, reinstate), librarian.ts   members.test.ts
features/loans/    loan.ts (checkOut, returnCopy, renewLoan, overdue), suspension.ts   loans.test.ts
shared/            result.ts (Result, ok, err), dates.ts (CalendarDate, addDays, daysBetween, isCalendarDate)
notes/             decisions, meetings, drafts (see index above)
```

Test names are written as plain-English rules. `features/loans/loans.test.ts` is the readable list Odile signed off on 2026-09-01, and quoting test names is a good way to answer "how does X work".
