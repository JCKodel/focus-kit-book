# Hollowmere Lending Library — guide for answering questions

A TypeScript domain model (no UI, no storage) of lending at the library's Saltgate branch, built for Odile Fenwick (head librarian). The rules have been frozen since the 2026-09-08 planning meeting.

Each session answers one question from a developer or from Juno (product owner). Read only what the question needs.

## How to answer

- **Keep it short.** Open with the answer in one or two plain sentences that Juno could pass on to Odile. Then give at most three lines of evidence: `file:line`, and the note that made the decision, with its date. Don't add related rules the asker didn't ask about.
- **Answer from the code**, not from memory or this file. Code and tests (`features/`, `shared/`) beat every note.
- **Notes are history.** Many give numbers that are no longer true. Before quoting a note, check the "Rules that changed" table. If the asker seems to remember an old rule, say when and where it changed.
- Drafts (holds, Loan Service Design) describe nothing that exists. Say so if asked.
- If the repo doesn't answer the question, say so and name who would know: Odile for lending rules (through Juno), Tamsin for technical and dependency questions, Bex for tests and error codes. Don't guess.
- Run `npm test` only when the question is whether something actually works. If running it is blocked, say that you answered from reading the code.
- Read only. Don't edit anything. Mention problems you notice in one line at the end.
- Git history can't tell you who changed what: there's one import commit, and every author is "experiment". The notes are the record.

**Is this guide current?** It was last checked against the code and all notes on **2026-10-02**. List `notes/`. Any file not in the index below is newer than this guide. If it relates to the question, read it, using the date written inside it. If a new note or the code contradicts this guide, end your answer with: "`CLAUDE.md` is out of date: <point>."

## Where to look

| Topic | Code | Best note |
|---|---|---|
| Loan period, loan limit, checkout and its refusal order | `checkOut`, constants at the top of `features/loans/loan.ts` | `glossary.md` (Checkout) |
| Renewals (cap, counted from the due date, overdue) | `renewLoan`, `loan.ts` | `decision-renewals.md` |
| Overdue (from the day after the due date) | `isOverdue`, `loan.ts` | `bug-overdue-off-by-one-2026-06-02.md` |
| Returns (always accepted) | `returnCopy`, `loan.ts` | `2026-02-11 meeting.md` |
| Suspension: threshold, who runs it, lifting it | `features/loans/suspension.ts`; the record is in `features/members/member.ts` | `Meeting 2026-05-19 - suspension rules.md` |
| Overdue members can't borrow | `checkOut` | `2026-06-16 meeting.md` |
| Books, copies, withdrawal, ISBN | `features/books/book.ts` | `copies-and-withdrawal.md`, `cataloguing chat 22 apr.md` |
| Members vs librarians | `features/members/` | `librarians-vs-members.md` |
| Every error code and the check order | the `*Error` union types | `error codes list.md` |
| Dates, `Result`, code layout | `shared/` | ADR-003, `adr 2 - results not exceptions.md`, ADR-001 |
| Fines (there are none) | none | `ADR-004-no-fines.md` |
| Status and roadmap | none | `2026-09-08 planning.md` |

Test names read as plain-English rules. `features/loans/loans.test.ts` is the list Odile signed off on 2026-09-01, so quoting test names is a good way to answer "how does X work".

## Rules that changed: older notes say otherwise

| Topic | Old (and where it appears) | Current (decided in) |
|---|---|---|
| Loan period | 14 days (kickoff, Loan Service Design, CardBox notes) | 21 (`2026-03-09 meeting with library.md`) |
| Loan limit | 3 (kickoff, Loan Service Design) | 5 (03-09) |
| Renewals | unlimited (kickoff); "decide later" (03-09) | max 2, counted from the due date (`decision-renewals.md`, 03-30) |
| Fines | "likely 0.20/day" (kickoff, 01-26, Loan Service Design, questions Q4) | none (ADR-004, 04-14) |
| Suspension threshold | 28 days (02-11, 04-08, questions Q1, ADR-004); 30 (holds draft) | more than 14 days (05-19) |
| Who lifts a suspension | head librarian only (01-26, 02-11, 04-08, holds draft) | any librarian, once nothing is overdue (05-19) |
| Borrowing with an overdue loan | allowed until suspended (questions Q2, 04-08) | refused (06-16) |
| Copy statuses | 5, incl. lost and damaged (01-26) | 3; lost and damaged are withdrawn (`copies-and-withdrawal.md`, 04-28) |
| Overdue on the due date | yes (bug, until 06-02) | no (06-02) |
| Suspension automatic | yes (02-11); nightly job (holds draft) | no, a librarian runs it (04-08, 05-19) |
| Dates, errors, layout | `Date`, thrown errors, layers (Loan Service Design) | strings, `Result`, slices (ADR-003, ADR 2, ADR-001) |

Notes that are wrong about their own facts:
- `retro-march.md` dates the overdue-checkout block to March. It came in on 06-16.
- The 06-16 notes say a pointer was added to the 04-08 note. It isn't there.
- ADR 2 shows a 06-16 error code in a 02-10 document, and it links to `rafe-notes-error-handling.md`, which was never committed. There's no `ADR-002` file; ADR 2 is `adr 2 - results not exceptions.md`.

## Notes index (all 29 as of 2026-10-02)

- **Current:** `glossary.md` (best summary), `error codes list.md`, `ADR-001-vertical-slices.md`, `adr 2 - results not exceptions.md`, `ADR-003 calendar dates.md`, `ADR-004-no-fines.md`, `decision-renewals.md`, `copies-and-withdrawal.md`, `librarians-vs-members.md`, `cataloguing chat 22 apr.md`, `holiday closures.md` (due dates don't skip closures), `cardbox migration thoughts.md` (no import), `Meeting 2026-05-19 - suspension rules.md`, `2026-06-16 meeting.md`, `bug-overdue-off-by-one-2026-06-02.md`, `testing conventions.md`, `node-26-typescript-notes.md`, `2026-09-08 planning.md`
- **Drafts, not built:** `holds-and-reservations-DRAFT-v2.md`, `Loan Service Design (draft).md` (only a starting point for the planned persistence work)
- **Historical:** `2026-01-12 kickoff.md`, `meeting_2026_01_26.md`, `mtg-2026-02-03-architecture.md`, `2026-02-11 meeting.md`, `2026-03-09 meeting with library.md`, `2026-04-08-mtg.md`, `retro-march.md`, `marek - dates notes.md`, `questions for odile.md`

**Not built:** fines (never), CardBox import (decided against), closures and opening hours, email reminders, holds, persistence, UI, reports (planned for Q4), a head-librarian role. **Still open:** deleting members; whether re-entered CardBox loans keep their old due dates; the holds questions.

**People** (notes use their initials): Odile Fenwick (head librarian, decides the rules), Wren Halloway (desk librarian), Juno Achterberg (JA, PO), Tamsin Oduya (TO, tech lead), Rafe Lindqvist (RL), Marek Szolt (MS, dates), Bex Amadi (BA, tests).
