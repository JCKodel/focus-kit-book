# Measurement: cost, run 2

The five questions of `../start/questions.md`, each asked word for word in its own fresh headless session in a copy of the setup, read-only (`--permission-mode default --permission-prompts none --allowedTools "Read" "Glob" "Grep"`). Correct: marked against the expected answer by a fresh session that saw the six setups' answers under shuffled letters (see `../../README.md`).

## first

| Question | Input | Output | Cache write | Cache read | Cost (USD) | Seconds | Correct |
|---|---|---|---|---|---|---|---|
| 1. How many days late must a loan be before its member is suspended? | 6 | 868 | 9,908 | 56,376 | 0.108 | 10 | yes |
| 2. Who can lift a member's suspension, and when? | 8 | 1,605 | 12,578 | 81,091 | 0.149 | 16 | yes |
| 3. A member renews a loan three days before its due date. What is the new due date? | 6 | 880 | 10,268 | 57,047 | 0.111 | 10 | yes |
| 4. Can a member who has an overdue loan borrow another book? | 6 | 862 | 10,343 | 56,634 | 0.111 | 10 | yes |
| 5. If a book is due on a day the library is closed, does the due date move? | 6 | 1,330 | 11,461 | 57,537 | 0.130 | 14 | yes |

Answers, byte for byte:

### first, question 1

    The loan has to be **15 days overdue**. The rule is "more than 14 days," so a loan exactly 14 days overdue does not qualify.

    - **The code:** `SUSPEND_AFTER_DAYS_OVERDUE = 14` (`features/loans/suspension.ts:15`). The check is `daysOverdue(l, today) > SUSPEND_AFTER_DAYS_OVERDUE` (`suspension.ts:22`), and it applies to any active loan the member has.
    - **The tests:** "is not due at exactly the threshold" and "is due one day past the threshold" (`features/loans/loans.test.ts:198-204`).
    - **How days are counted:** a loan is overdue from the day after its due date. If the due date is 2026-03-22, day 14 overdue is 04-05 (no suspension) and day 15 is 04-06 (suspension).

    **It isn't automatic.** The member is only suspended when a librarian runs `applySuspensions`, which records the librarian, the date and the reason. Wren does this on Mondays. So in practice, the suspension starts at the first run after the loan passes 15 days overdue.

    **If you remember a different number:** older notes say 28 days ("four weeks"). That appears in the 02-11 and 04-08 meetings, `questions for odile.md` Q1 and ADR-004. The holds draft says 30 days, but that draft was never adopted. The rule changed to "more than 14 days" in `Meeting 2026-05-19 - suspension rules.md`.

### first, question 2

    **Who:** any librarian. **When:** only once the member has nothing overdue. Returning the books does not lift the suspension on its own; a librarian has to lift it as a separate step.

    **In the code** (`features/loans/suspension.ts:46-57`):
    - `liftSuspension(member, loans, today)` returns `still-has-overdue-loans` if any of the member's active loans is overdue on `today`. Otherwise it calls `reinstateMember` (`features/members/member.ts:52`).
    - `reinstateMember` returns `not-suspended` if the member isn't suspended.
    - Only **overdue** loans block it. A member can still have books out that aren't yet due and be reinstated.
    - `liftSuspension` takes no librarian argument, so nothing records who lifted the suspension. Suspending is different: it records the librarian, the date and the reason.

    The tests that cover this are in `features/loans/loans.test.ts:215-225`: *"cannot lift a suspension while loans are overdue"* and *"lifts a suspension once overdue loans are returned"*.

    **Why, and what changed:** this was decided at the 2026-05-19 meeting (`notes/Meeting 2026-05-19 - suspension rules.md:56`): "any librarian may reinstate, once nothing is overdue anymore." Before that, the rule from 01-26 was that only the head librarian (Odile) could reinstate. That caused a bottleneck: Odile was away for a week in early May, and two members couldn't be reinstated during that time, even though one had already returned everything. Wren asked for lifting to stay a separate step ("I want to see them at the desk").

    If you see "head librarian only" in the 01-26, 02-11 or 04-08 notes or in the holds draft, that rule is out of date. The model has no head-librarian role anymore.

### first, question 3

    The new due date is the **old due date plus 21 days**. That works out to 24 days from the day they renew. The three days left on the loan aren't lost.

    - `renewLoan` sets `dueOn: addDays(loan.dueOn, LOAN_PERIOD_DAYS)` (`features/loans/loan.ts:113`), and `LOAN_PERIOD_DAYS = 21` (`loan.ts:7`).
    - The signed-off test is called "extends from the current due date, not from today" (`features/loans/loans.test.ts:156`).

    **Example:** the loan is due 2026-03-22 and the member renews on 2026-03-19. The new due date is **2026-04-12**, not 2026-04-09.

    The 21 days are plain calendar days. Closures aren't skipped (`holiday closures.md`, 07-14).

    **Limits on renewing:**
    - A loan can be renewed at most 2 times (`MAX_RENEWALS`, `loan.ts:9`). The third attempt is refused with `renewal-limit-reached`.
    - It can be renewed on the due date itself, but not once it's overdue. From the next day it's refused with `loan-overdue`.
    - A suspended member can't renew at all.

    **If someone remembers it differently:** the kickoff and the Loan Service Design draft said loans were 14 days with unlimited renewals. The current rule, max 2 renewals counted from the due date, was set in `decision-renewals.md` on 2026-03-30. The 21-day loan period was set in the 2026-03-09 meeting.

### first, question 4

    **No.** A member with even one overdue loan is refused at checkout with `member-has-overdue-loans`. They don't have to be suspended for this to happen.

    - **The check:** `features/loans/loan.ts:67`. `checkOut` refuses if any of the member's active loans is overdue. Only the suspension check (`member-suspended`, line 64) comes before it, and it runs before the loan-limit and copy checks.
    - **The test Odile signed off on:** "refuses a member who has an overdue loan, even before suspension" (`features/loans/loans.test.ts:70`).
    - **What counts as overdue:** a loan is overdue from the day *after* its due date, never on the due date itself (`isOverdue`, `loan.ts:39-40`). A member whose book is due today can still borrow.
    - **How they can borrow again:** return the overdue book. Returns are always accepted. Once nothing is overdue, the block is gone. A suspension is different: it stays until a librarian lifts it, even after the last book comes back.

    **This rule changed, so people may remember it differently.** Until June, overdue members could keep borrowing until they were suspended (questions Q2 on 02-11, and `notes/2026-04-08-mtg.md`). The block was decided in `notes/2026-06-16 meeting.md`.

    One older note gets the history wrong. `notes/retro-march.md` says the block was decided on 03-09 and merged on 03-25. In fact the 03-09 meeting only asked for a UI warning, and the 04-08 meeting explicitly allowed overdue members to borrow.

### first, question 5

    No. The due date is always the loan date plus 21 calendar days, and closures are ignored.

    **In the code**
    - `checkOut` sets `dueOn: addDays(today, LOAN_PERIOD_DAYS)` (`features/loans/loan.ts:79`), where `LOAN_PERIOD_DAYS = 21` (`loan.ts:7`).
    - `renewLoan` adds 21 days to the current due date the same way (`loan.ts:113`).
    - Nothing in the model knows about opening hours or closures. There's no closures list and no `isOpen`.

    **Why**
    This was decided with Odile on 2026-07-14 (`notes/holiday closures.md`). Wren raised it because of the August building-work closure. The team considered two alternatives: pushing the due date to the next open day, or counting only open days. Both were rejected. Each would need someone to maintain a closure calendar, would make `addDays` depend on data instead of being plain arithmetic, and could quietly change due dates on existing loans if the calendar were edited later. Odile preferred plain calendar days from the start, because closures are rare and mostly known in advance.

    **What staff do instead**
    - Renew the loan before the closure. Renewal works up to and including the due date.
    - Don't apply a suspension that's only due because of a closure. Suspension only happens when a librarian runs `applySuspensions`, so they can skip it or leave that member out. The threshold is also more than 14 days overdue, which is longer than any planned closure.

    **What happens if nobody acts**
    A loan due on a closed day is overdue from the next day (`isOverdue`). Then:
    - It can no longer be renewed (`loan-overdue`, `loan.ts:109`).
    - The member can't borrow anything else (`member-has-overdue-loans`) until the book is returned. The note says to do what you'd do any other day: process the return first, then lend.

    **Book drop**
    Books left in the book drop during a closure are recorded as returned on the day staff process them. Return dates are not backdated.

    A follow-up from that meeting asked Odile to brief the desk team before the August closure. The note doesn't record whether that happened.

## challenged

| Question | Input | Output | Cache write | Cache read | Cost (USD) | Seconds | Correct |
|---|---|---|---|---|---|---|---|
| 1. How many days late must a loan be before its member is suspended? | 6 | 832 | 10,233 | 54,420 | 0.109 | 10 | yes |
| 2. Who can lift a member's suspension, and when? | 8 | 1,224 | 10,636 | 75,508 | 0.125 | 15 | yes |
| 3. A member renews a loan three days before its due date. What is the new due date? | 6 | 631 | 8,194 | 53,098 | 0.089 | 9 | yes |
| 4. Can a member who has an overdue loan borrow another book? | 6 | 740 | 9,668 | 53,144 | 0.103 | 9 | yes |
| 5. If a book is due on a day the library is closed, does the due date move? | 4 | 534 | 8,755 | 32,532 | 0.087 | 7 | yes |

Answers, byte for byte:

### challenged, question 1

    A member becomes due for suspension once any of their loans is **more than 14 days overdue**. At exactly 14 days late nothing happens; at 15 days they qualify. Note that this isn't automatic: a librarian runs the suspension step.

    - `features/loans/suspension.ts:15` sets `SUSPEND_AFTER_DAYS_OVERDUE = 14`, and line 22 compares it with `>`.
    - `features/loans/loans.test.ts:198-204` has two tests, "is not due at exactly the threshold" and "is due one day past the threshold".
    - The decision came from `Meeting 2026-05-19 - suspension rules.md` (19 May 2026). It replaced the old 28-day rule from the 11 Feb meeting, so any note that still says 28 days is out of date.

### challenged, question 2

    Any librarian can lift a suspension, but only once the member has nothing overdue. Returning the last overdue book doesn't lift the suspension by itself. A librarian has to do it as a separate step at the desk.

    - `features/loans/suspension.ts:46-56`: `liftSuspension` returns `still-has-overdue-loans` while any of the member's active loans is overdue. Otherwise it reinstates the member.
    - `features/loans/loans.test.ts:215` and `:222`: "cannot lift a suspension while loans are overdue" and "lifts a suspension once overdue loans are returned".
    - `notes/Meeting 2026-05-19 - suspension rules.md:56`: this decision replaced the old rule from 26 January that only the head librarian (Odile) could reinstate a member.

    One thing I noticed: `liftSuspension` doesn't take a librarian, so the code doesn't record who lifted a suspension. It does record who applied one.

### challenged, question 3

    The new due date is the old due date plus 21 days. Renewing early doesn't cost the member anything. Counted from the day they renew, that's 3 + 21 = 24 days.

    - `features/loans/loan.ts:113`: `dueOn: addDays(loan.dueOn, LOAN_PERIOD_DAYS)`, with `LOAN_PERIOD_DAYS = 21` at line 7.
    - `notes/decision-renewals.md:44` (2026-03-30): "a renewal adds 21 days to the current due date, not to today."

    This only works if the loan hasn't already been renewed twice. A third renewal is refused with `renewal-limit-reached` (`loan.ts:110`).

### challenged, question 4

    No. If a member has any overdue loan, checkout is refused, even when they're far from being suspended. Once they return the overdue book they can borrow again, so at the desk they can return it and then take the new one on the same visit.

    - `features/loans/loan.ts:67`: `checkOut` refuses with `member-has-overdue-loans` if any of the member's loans is overdue. A loan counts as overdue from the day after its due date.
    - `features/loans/loans.test.ts:70`: the test is "refuses a member who has an overdue loan, even before suspension".
    - `notes/2026-06-16 meeting.md` (16 June 2026) made this decision. It replaced the 8 April 2026 rule, which let members keep borrowing until they were suspended. If someone remembers the older rule, that's where it changed.

### challenged, question 5

    No, the due date doesn't move. A loan is due 21 calendar days after checkout, and the model doesn't know which days the library is closed. When a due date lands on a closed day, librarians deal with it by hand: they renew the loan before the closure, and they hold off on suspensions that are only due because of the closure.

    - `features/loans/loan.ts:79` sets `dueOn: addDays(today, LOAN_PERIOD_DAYS)`, which is plain date arithmetic with no closures list.
    - `holiday closures.md` (2026-07-14, agreed with Odile) says: "Due dates do not skip closed days… The model does not know about opening hours or closures at all."

    Side note: that same note gave Bex an open follow-up to add "due dates are calendar days; closures are handled by staff" to the rules list. I didn't check whether a test with that name exists.
