# Measurement: cost, run 3

The five questions of `../start/questions.md`, each asked word for word in its own fresh headless session in a copy of the setup, read-only (`--permission-mode default --permission-prompts none --allowedTools "Read" "Glob" "Grep"`). Correct: marked against the expected answer by a fresh session that saw the six setups' answers under shuffled letters (see `../../README.md`).

## first

| Question | Input | Output | Cache write | Cache read | Cost (USD) | Seconds | Correct |
|---|---|---|---|---|---|---|---|
| 1. How many days late must a loan be before its member is suspended? | 4 | 592 | 8,479 | 33,660 | 0.086 | 7 | yes |
| 2. Who can lift a member's suspension, and when? | 12 | 1,998 | 11,393 | 124,690 | 0.156 | 21 | yes |
| 3. A member renews a loan three days before its due date. What is the new due date? | 6 | 1,033 | 9,920 | 55,573 | 0.111 | 11 | yes |
| 4. Can a member who has an overdue loan borrow another book? | 8 | 1,322 | 11,957 | 80,463 | 0.138 | 30 | yes |
| 5. If a book is due on a day the library is closed, does the due date move? | 6 | 1,052 | 9,702 | 54,846 | 0.110 | 12 | yes |

Answers, byte for byte:

### first, question 1

    A member qualifies for suspension once any of their loans is **more than 14 days overdue**. At exactly 14 days late they don't qualify. At 15 days they do.

    - **Code:** `features/loans/suspension.ts:15` sets `SUSPEND_AFTER_DAYS_OVERDUE = 14`. Line 22 compares with a strict `> SUSPEND_AFTER_DAYS_OVERDUE`. The boundary test at `features/loans/loans.test.ts:195-196` checks both day 14 and day 15.
    - **How days are counted:** a loan only becomes overdue on the day *after* its due date (see the 2026-06-02 off-by-one fix). So for a book due 1 March, 14 days overdue is 15 March, which doesn't trigger suspension. 15 days overdue is 16 March, which does.
    - **It isn't automatic:** the model only reports that the member qualifies. A librarian has to run `applySuspensions`, which Wren does on Monday mornings, so in practice the suspension can land a few days after the threshold.
    - **History:** older notes (02-11, 04-08 and Q1 in the questions list) say 28 days, or "four weeks". That was changed to more than 14 days at the **2026-05-19 meeting**. The holds draft's 30 days was only ever a proposal.

### first, question 2

    **Any librarian** can lift a suspension, but only once the member has **no overdue loans left**.

    **How it works in the code** (`features/loans/suspension.ts:48`)

    - `liftSuspension(member, loans, today)` checks the member's active loans. If any of them is overdue on `today`, it returns `err('still-has-overdue-loans')` and the member stays suspended.
    - Otherwise it calls `reinstateMember` (`features/members/member.ts:52`), which removes the suspension. If the member wasn't suspended in the first place, that returns `not-suspended`.
    - The function doesn't take a librarian, so there's no role check. No head-librarian role exists in the model.
    - Lifting is a separate step that someone has to do. Returning the last overdue book does **not** reinstate the member on its own: the member stays suspended until a librarian calls `liftSuspension`.
    - "Overdue" means from the day after the due date (`isOverdue`). A loan that's still out but not yet past its due date doesn't block reinstatement.

    The tests that cover this are `cannot lift a suspension while loans are overdue` and `lifts a suspension once overdue loans are returned` (`features/loans/loans.test.ts:215`, `:222`). In `members.test.ts:52` and `:58`, `reinstating removes the suspension` and `cannot reinstate a member who is not suspended` cover the member side.

    **How this changed**

    - **Before:** only Odile (the head librarian) could reinstate, at her discretion. Nothing in the code checked whether books were still overdue. This comes from `meeting_2026_01_26.md` and was repeated in the 02-11 and 04-08 notes.
    - **Now:** any librarian, once nothing is overdue. This was decided at `Meeting 2026-05-19 - suspension rules.md`. Odile had become a bottleneck: while she was away in early May, two members couldn't be reinstated. Her words were roughly "I don't need to be the one who presses the button. I need to trust whoever does." Not reinstating automatically was Wren's preference: "I want to see them at the desk".

    If you see "only the head librarian reinstates" in older notes or in `holds-and-reservations-DRAFT-v2.md`, it's out of date. The holds draft was never built.

### first, question 3

    The new due date is **the old due date plus 21 days**. Renewing three days early doesn't change it. The extension counts from the current due date, not from the day the member renews, so they don't lose those three days.

    For example, if the loan is due **2026-10-20** and the member renews on 2026-10-17, the new due date is **2026-11-10**. Counting from the renewal day would have given 2026-11-07, which is wrong.

    **Where this is in the code**
    - `features/loans/loan.ts:113`: `dueOn: addDays(loan.dueOn, LOAN_PERIOD_DAYS)`. The `today` parameter is only used to check whether the loan is overdue. It plays no part in working out the new date.
    - `LOAN_PERIOD_DAYS` is 21 (`loan.ts:7`).
    - The test `features/loans/loans.test.ts:156` is named "extends from the current due date, not from today". It renews on 2026-03-05 a loan due 2026-03-22 and expects the new due date to be 2026-03-22 + 21 = 2026-04-12.

    **When the renewal goes through**
    The renewal only succeeds if all of these hold (`loan.ts:107-110`):
    - the loan hasn't been returned
    - the member isn't suspended
    - this loan isn't overdue (another overdue loan doesn't block it)
    - the loan has been renewed fewer than 2 times

    **Why it works this way**
    `decision-renewals.md` (2026-03-30) decided this. Before that, older notes said renewals were unlimited or still undecided.

### first, question 4

    **No.** If a member has even one overdue loan, `checkOut` refuses with `member-has-overdue-loans`. There's no grace period, and the member doesn't need to be suspended first (`features/loans/loan.ts:67`).

    - **When a loan counts as overdue:** from the day *after* the due date. On the due date itself it isn't overdue yet (`loan.ts:39`), and a returned loan is never overdue.
    - **Order of checks:** a suspended member gets `member-suspended` first. Otherwise the overdue check runs before the loan-limit and copy checks, so the member only sees that one error (`loan.ts:64-71`).
    - **Test:** `refuses a member who has an overdue loan, even before suspension` (`features/loans/loans.test.ts:70`).
    - **What they can still do:** return anything, overdue or not (`loan.ts:85-98`). They can also renew a *different* loan that isn't overdue, because `renewLoan` only checks the loan being renewed (`loan.ts:109`).

    **How this changed:** the 2026-04-08 meeting decided overdue members could keep borrowing until they were suspended (decision 2). At that time suspension came after 28 days. The 2026-06-16 meeting reversed this, so any overdue loan now blocks checkout. Some notes still give the old rule: `2026-04-08-mtg.md` has no pointer to the June change, even though the June note says it does, and `questions for odile.md` Q2 has the old answer. The line in `retro-march.md` saying this was "merged on the 25th" of March is wrong.

### first, question 5

    No. The due date stays where it is. It is always the checkout date plus 21 calendar days, and the model has no idea when the library is open.

    **In the code**
    - At checkout the due date is `addDays(today, LOAN_PERIOD_DAYS)` (`features/loans/loan.ts:79`), with `LOAN_PERIOD_DAYS = 21` (`loan.ts:7`).
    - A renewal sets it to `addDays(loan.dueOn, LOAN_PERIOD_DAYS)` (`loan.ts:113`).
    - Nothing checks for closures. There's no list of closed days and no check for whether the library is open.

    **Why** (`notes/holiday closures.md`, 14 July 2026, agreed with Odile)

    The team looked at two other options: pushing a due date to the next open day, or counting only open days. They chose plain calendar days instead, for these reasons:
    - Both alternatives need a closure calendar that someone would have to maintain, and that calendar can't cover surprise closures.
    - If the calendar changed later, due dates on existing loans could quietly change too.
    - They would make every date rule harder to test.

    **What staff do instead**
    - Renew the loan before the closure, or when the member next comes in.
    - Hold off on the suspension run (`applySuspensions`) for anything that's only late because of a closure. Suspension is never automatic, so the librarian just doesn't press the button. Also, the 14-day threshold is longer than any planned closure.
    - Returns through the book drop are recorded on the day they're processed, not backdated.

    **One consequence to know about:** the model still treats a loan as overdue from the day after its due date, even if the library was closed that day. Until the book comes back, that loan blocks the member from checking out (`member-has-overdue-loans`). At the desk this is handled as usual: return the book first, then lend.

    The note says to revisit this only if a second branch with different opening hours ever comes into scope.

## challenged

| Question | Input | Output | Cache write | Cache read | Cost (USD) | Seconds | Correct |
|---|---|---|---|---|---|---|---|
| 1. How many days late must a loan be before its member is suspended? | 10 | 1,391 | 10,641 | 97,660 | 0.133 | 15 | yes |
| 2. Who can lift a member's suspension, and when? | 12 | 1,974 | 14,241 | 124,618 | 0.178 | 19 | yes |
| 3. A member renews a loan three days before its due date. What is the new due date? | 8 | 1,178 | 10,280 | 75,881 | 0.121 | 13 | yes |
| 4. Can a member who has an overdue loan borrow another book? | 6 | 852 | 10,151 | 54,136 | 0.109 | 9 | yes |
| 5. If a book is due on a day the library is closed, does the due date move? | 8 | 1,142 | 10,203 | 76,078 | 0.120 | 13 | yes |

Answers, byte for byte:

### challenged, question 1

    A member is suspended once any of their loans is **more than 14 days overdue**. At exactly 14 days late nothing happens; at 15 days they're suspended. Suspension isn't automatic: a librarian runs it. The threshold was 28 days until the 19 May 2026 meeting, when it changed to 14.

    Sources: `SUSPEND_AFTER_DAYS_OVERDUE = 14` with a `>` comparison in `shouldBeSuspended` (features/loans/suspension.ts); tests "is not due at exactly the threshold" and "is due one day past the threshold" (features/loans/loans.test.ts); `notes/Meeting 2026-05-19 - suspension rules.md`. (tests not run: running them needed permission, and nobody was available to approve it. The drift check didn't run either, because this folder isn't a git repository.)

### challenged, question 2

    Any librarian can lift a suspension, not just Odile, but only once the member has no overdue loans left. If anything is still overdue, the system refuses with `still-has-overdue-loans`. Returning the last overdue book doesn't lift the suspension on its own; a librarian still has to do it at the desk. Until 19 May 2026 only the head librarian (Odile) could reinstate; that changed at the 19 May meeting.

    Sources: `liftSuspension` (features/loans/suspension.ts); tests "cannot lift a suspension while loans are overdue" and "lifts a suspension once overdue loans are returned" (features/loans/loans.test.ts); `Meeting 2026-05-19 - suspension rules.md` (tests not run: the command was blocked by permissions).

### challenged, question 3

    The new due date is the old due date plus 21 days. Renewing early doesn't cost the member anything, because the 21 days are counted from the current due date, not from the day they renew. So a loan due on 22 March that is renewed on 19 March becomes due on 12 April. The member can renew up to 2 times per loan, as long as the loan isn't overdue and they aren't suspended.

    Sources: `renewLoan` and `LOAN_PERIOD_DAYS` = 21 in `features/loans/loan.ts`; test "extends from the current due date, not from today" in `features/loans/loans.test.ts`; decision-renewals.md (30 Mar 2026) (tests not run: the command was blocked by permissions; drift check not run: the folder isn't a git repository).

### challenged, question 4

    No. A member with even one overdue loan can't borrow anything else, even if they haven't been suspended. The checkout is refused with `member-has-overdue-loans` until every overdue book is back. A loan counts as overdue from the day after its due date. This changed on 16 June 2026: under the 8 April decision, members with overdue loans could still borrow.

    Sources: `checkOut` in `features/loans/loan.ts:67`; test "refuses a member who has an overdue loan, even before suspension" in `features/loans/loans.test.ts`; decided at the 2026-06-16 meeting (tests not run: running them needed approval and none could be given in this session). I also couldn't run the git log check for later changes because this copy isn't a git repository, but `notes/` has nothing newer than `2026-09-08 planning.md`.

### challenged, question 5

    No, the due date doesn't move. It's always the checkout date plus 21 calendar days, and nothing in the model knows when the library is closed. If a book falls due on a closed day, the librarians deal with it by hand. They can renew the loan before the closure, and they can choose not to apply a suspension that only comes from the closure. Odile agreed this on 14 July 2026, and it hasn't changed since.

    Sources: `checkOut` sets `dueOn = addDays(today, LOAN_PERIOD_DAYS)` (features/loans/loan.ts:79); test "computes due dates across month and year ends" (features/loans/loans.test.ts); holiday closures.md (2026-07-14) (tests not run: I wasn't allowed to run them here). The folder isn't a git repository, so I couldn't run the drift check with `git log`. Comparing file dates instead, I found no notes or code newer than `2026-09-08 planning.md`.
