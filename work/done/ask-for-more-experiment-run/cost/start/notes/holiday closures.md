# holiday closures — do due dates skip closed days?

**Date:** 2026-07-14
**With:** Odile Fenwick, Wren Halloway, Juno (JA), Marek (MS), Bex (BA)
**Written up by:** MS

Raised at the June retro: Wren pointed out that the Saltgate branch closes for a week in August (building work this year), plus the usual bank holidays and the odd closure for staff training. A 21-day loan issued in mid-July lands squarely in that week. What should the model do?

## Options we looked at

**A. Skip closed days.** Due date = loan date + 21, then if that lands on a closed day, push to the next open day.
- needs a calendar of closures in the model (who maintains it? what about unplanned closures — burst pipe, snow?)
- `addDays` stops being pure arithmetic; every due date depends on data
- changing the closure calendar after the fact would quietly change due dates of existing loans — or not, depending on when we compute them. Marek: "a nightmare to test, honestly"

**B. Count only open days.** 21 *open* days. Same problems as A, worse.

**C. Plain calendar days, humans handle the edge.** Due date is loan date + 21 calendar days, full stop. If it falls on a closed day, the librarians deal with it by hand.

## What Odile said

Leaning C from the start. Closures are rare and mostly known in advance. In CardBox days the desk just re-stamped cards or "didn't make a fuss" about anything due during a closure. There's also the book drop, which is open when the building isn't — Wren checks it first thing on reopening and backdates nothing; returns are recorded the day they're processed.

Wren's worry was suspensions: a loan due in the closure week could tick towards the 14-day limit while the member physically can't come in. Answer: the suspension run is a librarian pressing a button (`applySuspensions`), and the librarian can just not run it, or not act on someone, around a closure. Also 14 days is longer than any planned closure.

## Decision (agreed with Odile)

- **Due dates do not skip closed days.** Plain calendar days. `dueOn = addDays(loanedOn, 21)`, no calendar lookup.
- **If a due date falls on a day the library is closed, librarians handle it by hand.** Typical moves:
  - renew the loan before the closure, or when the member comes in (if they still can)
  - simply don't apply a suspension that's only due because of a closure
  - for the "can't borrow while overdue" check: return first, then lend — same as any other day
- The model does not know about opening hours or closures at all. No `isOpen`, no closures list.

## Why we're comfortable with this

- Keeps dates as pure string arithmetic, which is the whole reason Marek pushed for calendar strings in the first place.
- Every rule stays testable without fixture calendars.
- Puts discretion with the people who know which week the pipes burst.

## Follow-ups

- [x] MS — code change? None needed; the existing month/year-end due date test already covers "plain calendar days". Recorded here instead.
- [ ] JA — Odile to brief the desk team before the August closure: "renew before we close" and "hold off on suspensions for the closure week"
- [ ] BA — add to the rules list: "due dates are calendar days; closures are handled by staff"
- [ ] revisit only if a second branch with different hours ever comes into scope
