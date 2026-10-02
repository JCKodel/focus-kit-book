# Questions

The five questions of the cost arm's measurement, written before the runs. Each is asked, word for word, in its own fresh read-only session in a copy of each setup. The answers and files are not given to the agent; this file is not in the run folders.

1. How many days late must a loan be before its member is suspended?
   * Answer: more than 14 days; a loan exactly 14 days overdue does not suspend, 15 does. The 28-day rule of February was replaced.
   * Held by: `notes/Meeting 2026-05-19 - suspension rules.md` (and `SUSPEND_AFTER_DAYS_OVERDUE = 14`, compared with `>`, in `features/loans/suspension.ts`).

2. Who can lift a member's suspension, and when?
   * Answer: any librarian, once the member has nothing overdue; returning the last overdue book does not lift it by itself. This replaced the January rule that only the head librarian could.
   * Held by: `notes/Meeting 2026-05-19 - suspension rules.md`.

3. A member renews a loan three days before its due date. What is the new due date?
   * Answer: the current due date plus 21 days (the remaining three days are kept); a loan can be renewed at most twice.
   * Held by: `notes/decision-renewals.md`.

4. Can a member who has an overdue loan borrow another book?
   * Answer: no; any overdue loan blocks new loans (`member-has-overdue-loans`), with no grace period. The April decision that let them borrow until suspended was reversed on 16 June. Renewing another loan that is not overdue is still allowed.
   * Held by: `notes/2026-06-16 meeting.md` (and `features/loans/loan.ts`).

5. If a book is due on a day the library is closed, does the due date move?
   * Answer: no; due dates are plain calendar days and the system knows nothing about closures. Librarians handle it by hand, for example by renewing before the closure or not applying a suspension caused by it.
   * Held by: `notes/holiday closures.md`.
