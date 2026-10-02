# Hollowmere Lending Library — answering team questions

A TypeScript domain model (no UI, no storage) of lending at the Saltgate branch. Client: Odile Fenwick (head librarian). Desk: Wren Halloway. Team: Juno Achterberg (PO), Tamsin Oduya (tech lead), Rafe Lindqvist, Marek Szolt (dates), Bex Amadi (tests).

Each session answers **one question** from a developer or from Juno, then stops. **Read-only:** don't edit anything.

## Answer format

- Give the answer in plain words, one to three sentences, so Juno can repeat it to Odile. If the rule changed, say what it was, what it is now and when.
- Add **one** `Sources:` line: code symbol and file, test name, deciding note and date. Add `(tests not run)` if you couldn't run them.
- Stay under about 120 words unless the asker wants detail or the question is about implementation.
- If you find something stale, end with `Doc drift: <where> says X, code says Y`.
- Refer to people by name or as they/them; the notes don't record anyone's pronouns.
- If it's undecided, say who owns it. If a file isn't in the repo, say so and don't reconstruct what it said. For the tracker, shared drive or chat, point people there; you can't see them.

## Where truth lives

1. **Code**, then **tests** (their names are the rules, signed off by Odile on 1 Sep 2026), then `notes/glossary.md` and `notes/error codes list.md` (kept current), then the most recent dated decision note.
2. Everything else in `notes/` is history. Never quote a note as current without checking the code. Two notes are **drafts that were never built**: `Loan Service Design (draft).md` and `holds-and-reservations-DRAFT-v2.md`. There are no holds, services, `Date` objects, thrown errors or fines in the code.
3. Open only what the question needs. Use the index below rather than reading all of `notes/` (about 41k tokens).
4. Tests are one file per slice: `features/loans/loans.test.ts` (loans and suspension), `features/books/books.test.ts`, `features/members/members.test.ts`. Search with `git grep -n "<word>" -- features shared`; zsh breaks `grep --include=*.ts`. Run tests with `npm test` or `node --test --test-name-pattern="<topic>"` (Node ≥ 26, no dependencies).
5. **Drift check** for questions about rules or decisions: `git log --since=2026-10-02 --name-only -- notes features shared`. This guide covers notes up to `2026-09-08 planning.md`. A newer note or code change wins over this guide.

## Topic index: code → why

Look up the current value in the code; the note explains why.

| Topic | Code | Decided in |
|---|---|---|
| Loan period, loan limit | `LOAN_PERIOD_DAYS`, `MAX_ACTIVE_LOANS` (loans/loan.ts) | 2026-03-09 meeting |
| Renewals: cap, extends from due date, allowed on due date | `MAX_RENEWALS`, `renewLoan` | decision-renewals.md (03-30) |
| Overdue starts the day after the due date | `isOverdue`, `daysOverdue` | bug-overdue-off-by-one (06-02) |
| Any overdue loan blocks checkout; refusal order | `checkOut` | 2026-06-16 meeting |
| Suspension threshold; librarian runs it, no auto/nightly job | `SUSPEND_AFTER_DAYS_OVERDUE`, `applySuspensions` (loans/suspension.ts) | 05-19 meeting; 04-08 |
| Reinstatement by any librarian once nothing is overdue; no auto-reinstate on return | `liftSuspension` | 05-19 meeting |
| Returns always accepted | `returnCopy` | 2026-02-11 |
| Copy statuses, withdrawal (lost/damaged = withdrawn, one-way) | `CopyStatus`, `withdrawCopy` (books/book.ts) | copies-and-withdrawal.md (04-28) |
| ISBN-13 only, ISBN-10 rejected | `isValidIsbn13` | cataloguing chat 22 apr.md |
| Member data: name + email only | `registerMember` (members/member.ts) | 2026-02-11 |
| Librarians are staff, not members; no head-librarian role | `Librarian` (members/librarian.ts) | librarians-vs-members.md |
| No fines at all | — | ADR-004 |
| Calendar-date strings, `today` passed in | shared/dates.ts | ADR-003 |
| Closures: due dates don't skip them, staff handle it | — | holiday closures.md (07-14) |
| No CardBox import; loans re-entered by hand | — | cardbox migration thoughts.md (08-18) |
| Errors returned as codes, never thrown | shared/result.ts | ADR 2; error codes list.md |
| Code layout and import direction (loans → books/members) | features/, shared/ | ADR-001 |
| Status and Q4 plan (persistence → reports → desk UI); rules frozen | — | 2026-09-08 planning |
| How to write tests; Node/TypeScript rules | — | testing conventions.md; node-26-typescript-notes.md |

## Traps: older notes say → now

- 14-day loans, 3-loan limit → changed 03-09
- unlimited or undecided renewals → capped 03-30
- fines 0.20/day → none (ADR-004)
- suspend at 28 days ("four weeks"), or 30 days + nightly job (holds draft) → threshold changed 05-19
- only Odile reinstates → any librarian, 05-19
- overdue members may keep borrowing (04-08 decision; questions Q2) → reversed 06-16
- `lost` / `damaged` statuses → withdrawn, 04-28
- `Date` objects, thrown errors, layered services (Loan Service Design) → ADR-003, ADR 2, ADR-001
- overdue on the due date (`>= 0`) → fixed 06-02

## Known inconsistencies in the notes

- The 06-16 note claims a pointer was added to the 04-08 note. There isn't one.
- `retro-march.md` dates "overdue blocks checkout" to March. Wrong: it was adopted 06-16.
- The 06-16 note says April's threshold was 14 days. It was 28.
- ADR 2's example includes `member-has-overdue-loans`, which was added later, in June.
- `rafe-notes-error-handling.md` is referenced but not in the repo; ask Rafe.
- `questions for odile.md` marks Q7 and Q15 as open. Both were answered in copies-and-withdrawal.md.

## Still open

Member deletion (Q11, parked, Juno). Whether CardBox due dates are kept on re-entry (Odile). Holds: draft only, review in December (Juno, Marek); its numbers are proposals.

## Maintaining this file (for whoever writes up a check-in)

When a decision note lands: add or adjust its row in the topic index, add a trap line if it reverses something, and move the drift-check date and the "covers notes up to" note. Answers ending in `Doc drift:` mean this file needs exactly that. After editing, re-run the questions in `AGENT-CHECK.md`.
