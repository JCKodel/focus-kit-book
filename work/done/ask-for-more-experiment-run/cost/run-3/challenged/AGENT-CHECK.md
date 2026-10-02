# Checking the question-answering agent

Run this after editing `CLAUDE.md`, or after a decision changes a rule (and update the expected answers first). Ask each question in a **fresh** session and compare the answer with the must-say / must-not-say columns. Five of the seven are traps where an old note gives the wrong answer.

Last run 2026-10-02: 7/7 correct, 14–22k tokens and 11–26 s per question.

| # | Asker | Question | Must say | Must not say |
|---|---|---|---|---|
| 1 | Juno | A member is 3 days late with one book and wants to borrow another today. Can they? | No; `member-has-overdue-loans`; since 16 June; return first, then borrow | "yes, until suspended" (04-08 rule) |
| 2 | dev | The Feb 11 notes say suspension at 28 days. Still the threshold, at or after? | More than 14 days (14 no, 15 yes); changed 19 May; a librarian runs it | 28 days; automatic |
| 3 | Juno | Odile is on leave. Can Wren reinstate a member who brought everything back? | Yes, any librarian, once nothing is overdue; not automatic on return; since 19 May | only the head librarian |
| 4 | dev | Where is the per-day fine rate configured, for the overdue report? | No fines (ADR-004); report days overdue (`daysOverdue`) | 0.20/day; a config location |
| 5 | dev | How long does a copy stay on the hold shelf, and which function expires holds? | Holds aren't built; the draft is only a proposal; Juno and Marek, December | "7 days" stated as fact; `expireHolds` as existing |
| 6 | Juno | Borrowed 1 Oct, renewed 10 Oct. New due date? How many more renewals? | 12 November (22 Oct + 21); one more renewal left | 31 October (counted from today) |
| 7 | dev | For persistence, hard-delete members who leave or mark them inactive? | Undecided (Q11), parked by Juno as a data-protection question | either option stated as decided |
