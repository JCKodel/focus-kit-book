# Hollowmere Lending Library — guide for answering team questions

A TypeScript domain model (no UI, no storage) of lending at the Saltgate branch of the Hollowmere Lending Library. The client is Odile Fenwick (head librarian); Wren Halloway runs the desk. The team: Juno Achterberg (PO, JA), Tamsin Oduya (tech lead, TO), Rafe Lindqvist (RL), Marek Szolt (dates, MS), Bex Amadi (tests, BA).

Your job is mostly to **answer questions** about how the model behaves, why, and who decided it. Don't change code or notes unless someone asks you to.

## How to answer

1. **The code is the truth.** Then the tests (their names are the rules in plain English, signed off by Odile on 1 Sep 2026). Then `notes/glossary.md` and `notes/error codes list.md`, which are kept current. Then the **most recent** dated decision note. Both the glossary and the error list say "if this page and the code disagree, the code wins".
2. **`notes/` is a history, not a spec.** Many notes record rules that were later reversed. Never quote a note as current without checking the code and the superseded list below.
3. **Drafts describe nothing that exists.** `Loan Service Design (draft).md` and `holds-and-reservations-DRAFT-v2.md` were never built. There are no holds, services, repositories, controllers, `Date` objects, thrown errors or fines in the code.
4. Cite places: `features/loans/loan.ts:39` for behaviour, and the note (with its date) for *why*. If a rule changed, say what it was, what it is now, and when it changed.
5. If something isn't decided, say so and name who owns it. Don't guess a number.
6. To check behaviour, run `npm test` (or `node --test --test-name-pattern="renew"`). It needs Node ≥ 26 and has no dependencies. Prefer reading a test over reasoning it out.

## Code map

```
shared/result.ts        Result<T,E>, ok(), err()          (ADR 2)
shared/dates.ts         CalendarDate "YYYY-MM-DD", addDays, daysBetween, isCalendarDate (ADR-003)
features/books/         Book (title), Copy (physical item), ISBN-13, withdrawCopy
features/members/       Member, suspendMember, reinstateMember; Librarian (staff, separate)
features/loans/loan.ts  checkOut, returnCopy, renewLoan, isOverdue, daysOverdue, overdueLoans
features/loans/suspension.ts  shouldBeSuspended, applySuspensions, liftSuspension
```

Slices (ADR-001): `loans` may import from `books` and `members`, never the other way round. Suspension *records* live on members; the suspension *rule* lives in loans.

## Current rules (as of Oct 2026; rules frozen since the 8 Sep planning, changes go via Odile's check-in)

| Rule | Value / behaviour | Code | Decided in |
|---|---|---|---|
| Loan period | 21 calendar days from checkout | `LOAN_PERIOD_DAYS` loan.ts:7 | 2026-03-09 meeting |
| Loan limit | max 5 **active** loans; returned loans and other members' loans don't count | `MAX_ACTIVE_LOANS` loan.ts:8 | 2026-03-09 |
| Renewals | max 2 per loan; adds 21 days to the **current due date**, not to today; allowed on the due date; not once overdue | `MAX_RENEWALS`, `renewLoan` loan.ts:101 | decision-renewals.md (2026-03-30) |
| Overdue | from the day **after** the due date; never for a returned loan | `isOverdue` loan.ts:39 | bug-overdue-off-by-one (2026-06-02) |
| Overdue blocks borrowing | any overdue loan → `member-has-overdue-loans` at checkout; no grace period | loan.ts:67 | 2026-06-16 meeting |
| Renewing other loans | still allowed when a *different* loan is overdue | `renewLoan` | 2026-06-16 |
| Suspension threshold | any loan **more than** 14 days overdue (14 = no, 15 = yes) | `SUSPEND_AFTER_DAYS_OVERDUE` suspension.ts:15 | 2026-05-19 meeting |
| Who suspends | a librarian runs `applySuspensions` (Wren, Monday mornings); records librarian, date, reason. Not automatic, no nightly job. Manual `suspendMember` with a reason also allowed | suspension.ts:28 | 2026-04-08 |
| Who reinstates | **any** librarian, only once nothing is overdue (`still-has-overdue-loans`); returning the last book does **not** auto-reinstate | `liftSuspension` suspension.ts:48 | 2026-05-19 |
| Suspended member | can't check out or renew; can always return | | 2026-02-11, re-confirmed 05-19 |
| Returns | always accepted (late, suspended); only `already-returned` / `copy-mismatch` | `returnCopy` loan.ts:86 | 2026-02-11 |
| Checkout refusal order | suspended → overdue loans → loan limit → copy withdrawn → copy on loan (first match only) | loan.ts:64-71 | 2026-06-16 |
| Renewal refusal order | returned → suspended → overdue → renewal limit | loan.ts:107-110 | decision-renewals.md |
| Copy statuses | `available`, `on-loan`, `withdrawn` only. Lost/damaged = withdrawn. Withdraw only from available, one-way, records who and when | book.ts:12, 59 | copies-and-withdrawal.md (2026-04-28) |
| ISBN | optional; ISBN-13 only, hyphens/spaces stripped, check digit validated; ISBN-10 rejected (`invalid-isbn`), no auto-conversion | book.ts:42 | cataloguing chat 22 apr.md |
| Members | name + email only (trimmed, lower-cased, format-checked). Children have the same rules | member.ts | 2026-02-11 |
| Librarians | staff `{id, name}`, not members. A librarian who borrows registers as a member, same rules. Self-lending or self-reinstating isn't prevented, on purpose. No head-librarian role | librarian.ts | librarians-vs-members.md |
| Fines | **none**. No fees, balances or replacement charges | — | ADR-004 (2026-04-14) |
| Dates | `"YYYY-MM-DD"` strings, UTC maths, no times or time zones; `today` is always a parameter | shared/dates.ts | ADR-003 |
| Closures | due dates don't skip closed days; staff handle it by hand | — | holiday closures.md (2026-07-14) |
| CardBox | no import; active loans get re-entered by hand | — | cardbox migration thoughts.md (2026-08-18) |
| Errors | business failures are returned as kebab-case codes, never thrown | shared/result.ts | ADR 2 |

## Superseded claims (still written in older notes)

| Older note says | Now | Changed by |
|---|---|---|
| 14-day loans (kickoff, Loan Service Design) | 21 days | 2026-03-09 |
| max 3 loans | 5 | 2026-03-09 |
| unlimited renewals; "renewals undecided" (03-09, March retro) | max 2, from due date | 2026-03-30 |
| fines 0.20/day, configurable | no fines | ADR-004 |
| suspend at 28 days / "four weeks" (02-11, 04-08, questions Q1) | > 14 days | 2026-05-19 |
| suspend at 30 days + nightly job (holds draft) | never adopted | — |
| only Odile / head librarian reinstates (01-26, 02-11, 04-08, holds draft) | any librarian, once nothing overdue | 2026-05-19 |
| overdue members may keep borrowing until suspended (04-08 decision 2; questions Q2) | any overdue loan blocks checkout | 2026-06-16 |
| copy statuses incl. `lost`, `damaged` (01-26) | withdrawn | 2026-04-28 |
| `Date` objects, 23:59 due times, `Clock` (Loan Service Design) | calendar-date strings | ADR-003 |
| thrown error classes (Loan Service Design) | `Result` | ADR 2 |
| controllers/services/repositories layers | vertical slices | ADR-001 |
| `isOverdue` used `>= 0` (overdue on the due date) | `> 0` | 2026-06-02 bug fix |

## Known inconsistencies in the notes (don't be thrown by them)

- The 2026-06-16 note says the 04-08 note was "marked with a pointer". It wasn't: `2026-04-08-mtg.md` has no pointer to the June reversal.
- `retro-march.md` says "overdue-blocks-checkout … decided on the 9th, merged on the 25th". That contradicts the 03-09 note, where it was only a UI warning. The rule was actually adopted on 16 June. Treat the retro line as unreliable.
- The 2026-06-16 context says April's rule was "until something is more than 14 days late". In April the threshold was still 28.
- ADR 2 (dated 10 Feb) lists `member-has-overdue-loans` in its example. That code was only added in June, so the example was edited later.
- ADR-001 and ADR 2 refer to `rafe-notes-error-handling.md`, which is not in the repo.
- `questions for odile.md` lists Q7 (can a withdrawn copy come back?) and Q15 (lost vs damaged) as open. Both were answered in `copies-and-withdrawal.md`: withdrawal is one-way (re-add as a new copy), and lost/damaged count as withdrawn.

## Still open / not in the model

- Member deletion vs deactivation (questions Q11), parked as a data-protection question.
- Whether old 14-day due dates on CardBox cards are kept on re-entry (Odile; probably "enter the actual due date from the card").
- Reservations/holds: draft only, revisit in December 2026. Its numbers (30-day suspension, 3 holds, 7-day hold shelf, renewals blocked by holds) are proposals and partly contradict current rules.
- Q4 2026 plan (2026-09-08): persistence (TO) → reports (BA, MS; overdue report first) → minimal desk UI (RL). Nothing built yet.
- Not modelled on purpose: fines, email reminders, opening hours/closures, CardBox import, multiple branches, per-material loan periods, deposits, withdrawal reasons, legacy CardBox ids.

## Conventions (for questions about how to contribute)

- Node 26 runs `.ts` directly through type stripping: no `enum`, no `namespace`, no parameter properties; imports need the `.ts` extension; use `import type` for types. Zero dependencies (`notes/node-26-typescript-notes.md`).
- Tests: `node:test` + `node:assert/strict`, next to the code, plain-English names without "should", plain objects instead of mocks, no shared mutable fixtures, `deepEqual` on whole Results (`notes/testing conventions.md`).
- New error code: add it to the slice union, add a test that produces it, then update `notes/error codes list.md`.
