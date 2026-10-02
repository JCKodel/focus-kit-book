# Decision: how renewals work

**Date:** 2026-03-30
**Who was in on it:** Tamsin (TO), Rafe (RL), Marek (MS), Bex (BA), Juno (JA). Odile confirmed by message the same afternoon.
**Status:** decided, implemented in `renewLoan` (features/loans/loan.ts)

Not a formal ADR, just writing it down so we stop re-litigating it in the chat.

---

## Background

At kickoff the rule from Odile was "unlimited renewals". In practice at Saltgate that meant a librarian re-stamping the card whenever someone asked, sometimes for months. Wren mentioned a member who had the same gardening book for most of last year. Nobody minded at the time because nobody else wanted it, but Odile agreed that "unlimited" was more habit than policy.

Two separate questions came up while Rafe was writing `renewLoan`:

1. **How many times** can a loan be renewed?
2. **From when** does the new due date count — from today, or from the current due date?

The second one turned out to be the more interesting one.

## Q1: cap on renewals

- Agreed: **max 2 renewals per loan** (`MAX_RENEWALS = 2`).
- With a 21-day loan period that's up to 63 days in total on one loan, which Odile thought was "more than generous".
- After the second renewal the member has to bring the book back. They can borrow it again straight away if nobody else needs it; that's a fresh loan with a fresh renewal count.
- Third renewal attempt → `renewal-limit-reached`.

Juno asked if the cap should be configurable. Tamsin: it's a constant, change the constant. Nobody pushed back.

## Q2: what the 21 days are added to

Rafe's first version did `addDays(today, LOAN_PERIOD_DAYS)`. Marek flagged it in review.

Example Marek put in the PR:

- Loan due 2026-04-20.
- Member renews early, on 2026-04-15, because they're going away.
- "From today" → new due date 2026-05-06. The member just **lost 5 days** they'd already been given.
- "From due date" → new due date 2026-05-11. Member gets the full extra period.

Under "from today" the system punishes people for being organised. Odile's reaction: "That's exactly backwards. The people who renew early are the ones we *want*."

**Decision: a renewal adds 21 days to the current due date, not to today.**

- Renewing a few days early must never cost the member days.
- Renewing **on the due date itself is allowed** — that's the last day you can do it. Bex wanted that spelled out as its own test because the desk gets a lot of "it's due today, can I still renew?" questions.
- Renewing once it's actually overdue is not allowed → `loan-overdue`. They have to bring it in (or sort out the overdue first). Odile was clear on this: renewing is a courtesy for people who are on time.

Rafe asked whether someone could game this by renewing on day 1, twice, and get 63 days up front. Yes, technically. Nobody thinks that matters. Odile: "If they want it that badly, let them have it."

## Other rules that fell out of this

- Suspended members can't renew → `member-suspended`. (Same check as checkout.)
- Renewing a returned loan → `already-returned`.
- Order of checks in the code: returned → suspended → overdue → limit. Bex wants the error you get to be the most useful one; e.g. if a suspended member tries to renew an overdue loan, "suspended" is what the librarian needs to know first.

## Tests added (BA)

- renews from the due date, not from today
- early renewal keeps the remaining days
- renewal allowed on the due date
- renewal refused once overdue
- third renewal refused
- suspended member can't renew

## Actions

- [x] RL — change `renewLoan` to add to `dueOn`
- [x] BA — tests above
- [x] MS — double-check `addDays` across month ends (fine; it's all calendar days)
- [ ] JA — tell Wren and the desk staff the new cap before anything goes near them
- [ ] TO — add a comment in `loan.ts` so the next person doesn't "fix" it back
