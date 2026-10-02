# BUG: loan counted as overdue on its own due date

- **Found:** 2026-06-02 by Bex (BA)
- **Fixed:** 2026-06-02 (same afternoon), Marek (MS), reviewed by Rafe (RL)
- **Severity:** medium — wrong answers at the desk, but nothing persisted yet, so no bad data
- **Status:** closed

## What happened

Writing renewal edge tests, Bex added one that, per the plain-English rules list, should obviously pass:

> a member can renew on the due date

It failed with `loan-overdue`.

`isOverdue` was written as

```ts
return isActive(loan) && daysBetween(loan.dueOn, today) >= 0;
```

so on the due date (`daysBetween` = 0) the loan was already overdue. Classic off-by-one. The `>= 0` arrived with the May date refactor, swapping the old `Date`-based comparison for `daysBetween`; the old timestamp version was right by accident.

## Why it matters

"Due on the 22nd" means back *by the end of* the 22nd. Odile confirmed on the chat: "If it's due today it's not late. It's late tomorrow." Wren added that people regularly come in on the due date to renew.

Knock-on effects, all one day early:

- renewals refused on the due date (`loan-overdue`)
- `daysOverdue` one too high everywhere
- so the suspension threshold fired a day early (14 days late counted as 15)
- `overdueLoans` included loans due today — Wren would have phoned people who weren't late

No test caught it: every overdue test used dates well past due, none the boundary.

## Fix

Overdue starts the day **after** the due date. `isOverdue` now compares strictly:

```ts
// A loan is overdue from the day after its due date. On the due date itself
// it is not overdue.
export function isOverdue(loan: Loan, today: CalendarDate): boolean {
  return isActive(loan) && daysBetween(loan.dueOn, today) > 0;
}
```

`daysOverdue` goes through `isOverdue`, so it's fixed too: 0 on the due date, 1 the day after.

## Tests added

In `features/loans/loans.test.ts`:

- `is not overdue on the due date` — due 2026-03-22, checked 2026-03-22 → false
- `is overdue the day after the due date` — checked 2026-03-23 → true, `daysOverdue` = 1
- `can renew on the due date`
- `cannot renew an overdue loan` — now uses the day after, right on the boundary instead of weeks later
- suspension: `is not due at exactly the threshold` / `is due one day past the threshold` — built with `addDays(due, SUSPEND_AFTER_DAYS_OVERDUE)` and `+ 1`, so touching either constant or the comparison breaks them

All green with `node --test`.

## Lessons / follow-ups

- Boundary tests for every date rule, not just "obviously late". Bex is adding a "boundaries" column to the rules list. (BA)
- Comment every date comparison with which side is inclusive. Marek did `isOverdue` and the suspension threshold. (MS)
- Grep for other `>=` / `<=` on `daysBetween` results — done, only the one. (RL)
- Mention at retro — not blame; the tests worked.
- Juno to tell Odile it's fixed and which tests cover it, so the "late tomorrow" wording can be checked against the test list at the next check-in. (JA)

## Timeline

- 10:40 — Bex's new test fails, posted in the chat with output
- 11:15 — Marek finds the `>=`, confirms with a one-line test that `daysOverdue` is off too
- 14:30 — fix + boundary tests up for review
- 15:10 — Rafe approves, merged, full suite green

---
*Side note (MS): second time a date edge has bitten us. The first was the March month-end due date thing, hence the "computes due dates across month and year ends" test. Strings + UTC are fine; our comparisons need care.*
