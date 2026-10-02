# Measurement: cost, run 1

The five questions of `../start/questions.md`, each asked word for word in its own fresh headless session in a copy of the setup, read-only (`--permission-mode default --permission-prompts none --allowedTools "Read" "Glob" "Grep"`). Correct: marked against the expected answer by a fresh session that saw the six setups' answers under shuffled letters (see `../../README.md`).

## first

| Question | Input | Output | Cache write | Cache read | Cost (USD) | Seconds | Correct |
|---|---|---|---|---|---|---|---|
| 1. How many days late must a loan be before its member is suspended? | 6 | 1,075 | 10,460 | 54,985 | 0.116 | 11 | yes |
| 2. Who can lift a member's suspension, and when? | 6 | 1,148 | 11,453 | 54,787 | 0.126 | 12 | yes |
| 3. A member renews a loan three days before its due date. What is the new due date? | 4 | 729 | 10,638 | 33,061 | 0.106 | 8 | yes |
| 4. Can a member who has an overdue loan borrow another book? | 6 | 946 | 12,983 | 56,381 | 0.134 | 12 | yes |
| 5. If a book is due on a day the library is closed, does the due date move? | 4 | 848 | 11,682 | 33,060 | 0.117 | 9 | yes |

Answers, byte for byte:

### first, question 1

    A loan has to be **15 or more days overdue**, which the code expresses as "more than 14". At exactly 14 days overdue the member is not yet suspended.

    - **Code:** `SUSPEND_AFTER_DAYS_OVERDUE = 14` at `features/loans/suspension.ts:15`. The check at `features/loans/suspension.ts:22` is `daysOverdue(l, today) > SUSPEND_AFTER_DAYS_OVERDUE`, so it uses a strict `>`.
    - **Tests:** the tests "is not due at exactly the threshold" and "is due one day past the threshold" (`features/loans/loans.test.ts:198`) cover this boundary.
    - **Decided in:** `notes/Meeting 2026-05-19 - suspension rules.md`.

    Some details that often cause confusion:

    - **How days are counted:** a loan counts as overdue from the day after its due date. If a loan was due on 2026-03-22, it is 14 days overdue on 2026-04-05, which is not enough. On 2026-04-06 it is 15 days overdue, and the member can be suspended.
    - **Suspension isn't automatic:** a librarian has to run `applySuspensions`. Wren does this on Monday mornings, and it records the librarian, the date and the reason. There is no nightly job, so in practice the suspension happens at the first Monday run after the loan passes 14 days overdue.
    - **Overdue loans block borrowing first:** a member with any overdue loan, even one day late, already can't check out. That rule comes from the 2026-06-16 meeting.

    **Older notes give different numbers that are no longer the rule:**
    - "28 days / four weeks" appears in the Feb 11 and Apr 8 notes, in Q1 of `questions for odile.md`, and in the ADR-004 text. The May 19 meeting replaced it.
    - "30 days, nightly job" appears in the holds draft v2. It was never adopted.

### first, question 2

    Any librarian can lift a suspension, but only once the member has nothing overdue.

    **In the code:** `liftSuspension` in `features/loans/suspension.ts:48-57`.
    - If any of the member's active loans is overdue on `today`, it refuses with `still-has-overdue-loans` (`suspension.ts:53-54`).
    - Otherwise it calls `reinstateMember` (`features/members/member.ts:52`), which removes the suspension record. If the member wasn't suspended, that returns `not-suspended`.
    - The tests are "cannot lift a suspension while loans are overdue" and "lifts a suspension once overdue loans are returned" (`features/loans/loans.test.ts:215-223`).

    **What this means at the desk:**
    - **Returning the books doesn't lift the suspension.** The member stays suspended until a librarian runs `liftSuspension`.
    - **Only overdue loans block lifting.** Other active loans that aren't overdue yet don't stop it.
    - **"Overdue" starts the day after the due date** (`isOverdue`). A loan that is due today doesn't block lifting.

    **Two things you might not expect in the code:**
    - `liftSuspension` has no librarian parameter, so nothing records who lifted the suspension or when. Suspending does record that (`member.ts:47`). As far as I can see, that difference was never decided either way.
    - `reinstateMember` is exported from the members slice and does not check for overdue loans. The rule is only enforced if callers go through `liftSuspension` in loans, as the comment at `member.ts:50-51` says.

    **Where it was decided:** `Meeting 2026-05-19 - suspension rules.md`. Older notes (Jan 26, Feb 11, Apr 8 and the holds draft v2) say only Odile, the head librarian, can reinstate a member. That was replaced on 2026-05-19, so if you're working from one of those notes, that part is out of date.

### first, question 3

    **The new due date is the old due date plus 21 days.** That is 24 days after the day of the renewal. It is not 21 days from today, so renewing early doesn't cost the member any days.

    Example: a loan due 2026-03-22 is renewed on 2026-03-19. The new due date is 2026-04-12.

    - **Code:** `renewLoan` sets `dueOn: addDays(loan.dueOn, LOAN_PERIOD_DAYS)` (`features/loans/loan.ts:113`), with `LOAN_PERIOD_DAYS = 21` (`features/loans/loan.ts:7`). The comment at `loan.ts:100` says it outright: "A renewal adds a full loan period to the current due date, not to today."
    - **Test:** `features/loans/loans.test.ts:157-159` renews a loan due 2026-03-22 on 2026-03-05. It expects the new due date to be `addDays('2026-03-22', 21)`.
    - **Decided in:** `notes/decision-renewals.md` (2026-03-30).

    The renewal only works if:
    - the member is not suspended,
    - the loan has not been returned,
    - the loan has fewer than `MAX_RENEWALS = 2` renewals (`loan.ts:9`).

    Three days early also means the loan isn't overdue, so that check passes too.

### first, question 4

    **No.** A member with any overdue loan can't check out another book. They aren't suspended yet, but they're still blocked. There's no grace period.

    **In the code:** `checkOut` returns `member-has-overdue-loans` if any of the member's active loans is overdue (`features/loans/loan.ts:67`). The test that pins this down is "refuses a member who has an overdue loan, even before suspension" (`features/loans/loans.test.ts:70`).

    **What "overdue" means here:**
    - A loan is overdue from the day **after** its due date. On the due date itself it isn't overdue (`isOverdue`, `loan.ts:39`).
    - Returned loans never count.
    - One overdue loan is enough, however few days late it is. This is separate from suspension, which only happens once a loan is more than 14 days overdue.

    **Order of checks:** a suspended member gets `member-suspended` first (`loan.ts:64`). Next comes the overdue check, then the 5-loan limit, then the state of the copy.

    **What they can still do:**
    - **Return books:** returns are always accepted.
    - **Renew their other loans that aren't overdue:** renewal only refuses the overdue loan itself (`loan-overdue`, `loan.ts:109`), unless the member is suspended.

    Once they return the overdue book, they can borrow again straight away, as long as they aren't suspended.

    **Where it was decided:** `notes/2026-06-16 meeting.md`. If you're working from an older note, the rule there is different. The April 8 decision (#2) and `questions for odile.md` Q2 say overdue members may keep borrowing until they're suspended. The June 16 meeting replaced that. Also, `retro-march.md` says this block was "decided on the 9th" of March, which is wrong. It dates from 2026-06-16.

### first, question 5

    No. The due date stays where it is. It's always the loan date plus 21 calendar days, and the model doesn't know about opening hours or closures at all.

    **In the code**
    - `features/loans/loan.ts:7`: `LOAN_PERIOD_DAYS = 21`
    - `features/loans/loan.ts:79`: at checkout, `dueOn: addDays(today, LOAN_PERIOD_DAYS)`. There's no calendar lookup and no "next open day" adjustment.
    - `features/loans/loan.ts:113`: renewals work the same way. They add 21 days to the current due date, with no adjustment for closures.

    **Where it was decided:** `notes/holiday closures.md`. Wren raised it at the June retro because of the August closure week. The team looked at skipping closed days, which would need a closures calendar in the model, and turned it down. Nobody would own that calendar, unplanned closures would break it, and changing the calendar later could quietly shift the due dates of existing loans. They chose option C: plain calendar days, and staff handle the edge cases. `2026-09-08 planning.md:22` confirms that opening hours and closures are deliberately left out of the model.

    **What staff do instead** (from `holiday closures.md:29–31`):
    - **Renew the loan** before the closure or when the member comes in. A loan can be renewed on its due date, but not once it's overdue.
    - **Skip suspensions caused by a closure.** Suspension isn't automatic. A librarian runs `applySuspensions`, so they can leave it alone around a closure. The threshold is also more than 14 days overdue, which is longer than any planned closure.
    - **Returns through the book drop** are recorded on the day they're processed. Nothing is backdated.

    The model still counts a loan as overdue from the day after its due date, even during a closure. While it's overdue, the member can't check anything else out (`member-has-overdue-loans`) and can't renew that loan. Staff handle those cases by hand.

## challenged

| Question | Input | Output | Cache write | Cache read | Cost (USD) | Seconds | Correct |
|---|---|---|---|---|---|---|---|
| 1. How many days late must a loan be before its member is suspended? | 4 | 525 | 8,519 | 31,808 | 0.085 | 7 | yes |
| 2. Who can lift a member's suspension, and when? | 4 | 651 | 9,137 | 31,806 | 0.092 | 8 | yes |
| 3. A member renews a loan three days before its due date. What is the new due date? | 4 | 557 | 8,552 | 31,812 | 0.086 | 7 | yes |
| 4. Can a member who has an overdue loan borrow another book? | 6 | 881 | 9,155 | 52,650 | 0.101 | 9 | yes |
| 5. If a book is due on a day the library is closed, does the due date move? | 6 | 834 | 10,607 | 52,254 | 0.112 | 9 | yes |

Answers, byte for byte:

### challenged, question 1

    A loan has to be **more than 14 days overdue**, so 15 days late counts and 14 doesn't. Suspension isn't automatic: a librarian runs `applySuspensions` (Wren does it on Mondays) and the member is suspended then.

    - Code: `features/loans/suspension.ts:15` (`SUSPEND_AFTER_DAYS_OVERDUE = 14`) and the `> 14` check at `suspension.ts:22`
    - Decided at the May 19 meeting. If you see 28 days (Feb 11, Apr 8, `questions for odile.md`) or 30 days with a nightly job (holds draft), those older rules were replaced on May 19.

    I couldn't check for changes since `CLAUDE.md` was written because this directory isn't a git repository.

### challenged, question 2

    Any librarian can lift a suspension, but only once the member has no overdue loans left. If anything is still overdue, the lift is refused with `still-has-overdue-loans`. Returning the books doesn't lift the suspension automatically; a librarian still has to do it.

    - Code: `features/loans/suspension.ts:46-57` (`liftSuspension`). The function doesn't take a librarian argument, so nothing records who lifted the suspension. "Any librarian" comes from the code comment, not from a check in the code.
    - Decided at the May 19 meeting. It replaced the older "only Odile can reinstate" rule from the Jan 26, Feb 11 and Apr 8 notes.

    I couldn't check for rule changes since `CLAUDE.md` was written because this directory isn't a git repository.

### challenged, question 3

    The new due date is the old due date plus 21 days. Renewing three days early doesn't lose those three days, because the 21 days are added to the due date and not to the day of renewal. For example, a loan due 20 October that is renewed on 17 October becomes due 10 November.

    - `features/loans/loan.ts:113`: `dueOn: addDays(loan.dueOn, LOAN_PERIOD_DAYS)`, and `LOAN_PERIOD_DAYS = 21` is at line 7.
    - The deciding note is `decision-renewals.md` (Mar 30). A loan can be renewed at most twice, and renewal is refused if the loan is overdue, the member is suspended, or the loan has already been returned.

    I couldn't check for changes since `CLAUDE.md` was written, because this folder isn't a git repository.

### challenged, question 4

    No. If any of a member's loans is overdue, checkout is refused with `member-has-overdue-loans`. There's no grace period, but the member can still renew loans that aren't overdue yet.

    - Code: `features/loans/loan.ts:67`. A loan counts as overdue from the day after its due date (`loan.ts:37-39`).
    - Decided at the Jun 16 meeting (`notes/2026-06-16 meeting.md`). Before that, overdue members could keep borrowing until they were suspended (Apr 8 notes, `questions for odile.md` Q2). `retro-march.md` says this rule was merged in March, which is wrong.

    I couldn't check for changes since `CLAUDE.md` was written because this folder isn't a git repository.

### challenged, question 5

    No. A loan is due exactly 21 calendar days after checkout, even if that day falls when the library is closed. When it does, librarians handle it by hand: they renew the loan before the closure, or they don't apply a suspension that only came about because of the closure.

    - Code: `features/loans/loan.ts:79` sets `dueOn: addDays(today, LOAN_PERIOD_DAYS)` (renewals do the same at `:113`). The model has no closures calendar.
    - This was decided in `notes/holiday closures.md` (2026-07-14, agreed with Odile, written up by Marek).

    I couldn't run the check for rule changes since `CLAUDE.md` was written, because this folder isn't a git repository.
