# Holds & reservations — DRAFT v2

**Authors:** Juno Achterberg, Marek Szolt
**Date:** 2026-02-17
**Status:** Draft v2 (v1 was the whiteboard photo from 2026-02-13, now folded in here)
**Reviewers:** Tamsin, Rafe, Bex

---

## 1. Why

Members ask for this constantly. At Saltgate, Wren keeps a paper waiting list behind the desk; CardBox has an unsortable free-text column. When a copy comes back the desk often forgets to check, and someone who waited three weeks never hears.

Odile raised it on 2026-02-11 as the thing that would make the new system feel like an upgrade on day one. So: a new vertical slice, `features/reservations`, next to books, members and loans.

## 2. Scope

In:

- **Holds on a book** (the title), not a specific copy, in one **FIFO queue** per book.
- A returned copy with someone waiting goes to the **hold shelf** for **7 days**; uncollected → hold expires, copy goes to the next in the queue (or back to available).
- **Email notification** when a hold is ready.
- **Renewals blocked** if anyone holds the book.
- **Suspension after 30 days overdue** (§6); suspended members can't place holds.

Out (for this slice):

- Holds on a specific copy or edition.
- Inter-branch holds (only Saltgate for now).
- Online self-service; librarians place holds at the desk for v1.
- Fees for uncollected holds. No money anywhere in this.

## 3. Model

### 3.1 Concepts

- **Hold** — a member's place in a book's queue. `waiting` → `ready` → `collected`, or `waiting`/`ready` → `cancelled` / `expired`.
- **Queue** — a book's `waiting` holds, ordered by `placedOn`, then a sequence number preserving same-day entry order.
- **Hold shelf** — not an entity: the `on-hold-shelf` copies plus the holds they're reserved for.

### 3.2 Copy status

One new status: `available | on-loan | on-hold-shelf | withdrawn`. `on-hold-shelf` copies can only be checked out by the holding member; anyone else gets `copy-reserved`.

### 3.3 Type sketch

For `features/reservations/reservation.ts`. Uses the shared `Result` / `ok()` / `err()`; nothing throws for business failures.

```ts
export type HoldStatus = 'waiting' | 'ready' | 'collected' | 'cancelled' | 'expired';

export type Reservation = {
  readonly id: string;
  readonly bookId: string;
  readonly memberId: string;
  readonly placedOn: CalendarDate;
  readonly sequence: number;          // tie-break inside a day
  readonly status: HoldStatus;
  readonly copyId?: string;           // set when ready
  readonly readyOn?: CalendarDate;    // set when ready
  readonly collectBy?: CalendarDate;  // readyOn + HOLD_SHELF_DAYS
};

export const HOLD_SHELF_DAYS = 7;
export const MAX_ACTIVE_HOLDS = 3;

export type ReservationError =
  | 'member-suspended'
  | 'already-holding-book'
  | 'hold-limit-reached'
  | 'book-has-available-copy'
  | 'hold-not-waiting'
  | 'hold-not-ready'
  | 'hold-expired'
  | 'copy-reserved';
```

Functions:

- `placeHold({ holdId, member, bookId, holds, copies, today })` → `Result<Reservation, ReservationError>`
- `assignReturnedCopy({ copy, holds, today })` → `Result<{ hold, copy } | null, ReservationError>`; `ok(null)` when nobody waits (copy goes back to `available`)
- `expireHolds(holds, copies, today)` → `{ holds, copies }`
- `cancelHold(hold)` → `Result<Reservation, ReservationError>`

`collectBy = addDays(readyOn, HOLD_SHELF_DAYS)` from `shared/dates.ts`.

## 4. Rules

1. Suspended members can't place holds. → `member-suspended`.
2. One hold per member per book. → `already-holding-book`.
3. Max **3 active holds** (waiting + ready). Juno's number; matches the loan cap, easy to explain. → `hold-limit-reached`.
4. No holds on a book with a copy on the shelf; just borrow it. → `book-has-available-copy`.
5. On return (`returnCopy`), a non-empty queue sends the copy `on-hold-shelf` for the **first** waiting hold: `ready`, `readyOn = today`, `collectBy = today + 7`.
6. A normal checkout of that copy by that member → `collected`.
7. `expireHolds` runs in the nightly suspension job. `ready` past `collectBy` → `expired`; the copy moves to the next hold or `available`.
8. **Renewal blocked** while any hold waits: new loan error `book-on-hold`. Stops popular titles being renewed forever.
9. Librarians can cancel a waiting or ready hold any time; a ready copy moves on immediately.
10. Nothing here blocks returns.

## 5. Notifications

- On `ready`, one email (address already on `Member`): title, branch (Saltgate), collect-by date in full ("Tuesday 3 March"). One reminder 2 days before `collectBy`.
- The domain sends no email: `assignReturnedCopy` and `expireHolds` return what changed, and a `notifications` adapter outside the domain emails, keeping slices I/O-free.
- Marek: never a time of day; we only have calendar dates, on purpose.

## 6. Suspension (changes needed for holds)

The queue must keep moving, so suspension ships first.

- Suspended once any loan is **30 days overdue**. Odile said "four weeks" on 2026-02-11; 30 is easier at the desk ("a month") and simpler for the nightly job.
- Suspended members can't borrow, renew or **place holds**. Their waiting holds are **skipped** but keep their position until reinstatement; their ready holds expire immediately.
- Reinstatement stays with the head librarian, as agreed with Odile. Returning is always allowed.

## 7. Edge cases

- **Hold-shelf copy withdrawn**: hold returns to `waiting` at the queue front. `withdrawCopy` refuses `on-hold-shelf` copies until the hold is released → `copy-reserved`.
- **New copy added**: goes to the queue first, like a return; the application layer calls `assignReturnedCopy` after `addCopy`.
- **Two copies returned the same day**, two waiting: each to the next hold, deterministic via `sequence`.
- **Holding a book already on loan**: refused, new error `already-borrowing-book`; renew instead.
- **Hold at the loan limit**: allowed. Still at the limit when collecting → normal loan error; hold stays ready until `collectBy`.
- **Queue position** ("you're 4th"): pure `queuePosition(holds, holdId)`.
- **Expired hold re-placed** goes to the back.
- **Year end**: plain date arithmetic; Marek adds a test with `readyOn = 2026-12-28`.

## 8. Tests (Bex)

Plain objects, `node:test`, `deepEqual` on Results. Minimum:

- places a hold when no copy is available
- refuses a hold from a suspended member
- refuses a second hold on the same book
- refuses a hold when a copy is available
- the first waiting hold gets the returned copy
- a suspended member's hold is skipped but keeps its place
- a ready hold expires the day after collect-by
- an expired hold passes the copy to the next in line
- a loan cannot be renewed while the book has a waiting hold
- a withdrawn hold-shelf copy puts the hold back at the front

## 9. Plan

| Step | What | Who | When |
|---|---|---|---|
| 1 | Suspension at 30 days + nightly job | MS | wk of 23 Feb |
| 2 | `features/reservations` types + `placeHold` + tests | MS | wk of 23 Feb |
| 3 | Copy status `on-hold-shelf`, checkout/withdraw changes | RL | wk of 2 Mar |
| 4 | Return → assign to queue, `expireHolds` | MS / RL | wk of 2 Mar |
| 5 | Renewal blocked when held | RL | wk of 9 Mar |
| 6 | Notification adapter + email wording with Odile | JA | wk of 9 Mar |
| 7 | Walkthrough at Saltgate with Wren | JA / BA | mid-March |

## 10. Open questions

- **Max holds**: 3, or the final loan cap? (JA to confirm with Odile.)
- **Hold shelf 7 days**: Wren thinks 5 might do. Starting with 7; it's a constant.
- **Do waiting holds count toward anything** (e.g. block registration changes)? Assume no.
- **Bounced email**: hold still expires after 7 days? Proposal: yes, the desk also phones for popular titles. Needs Odile's ok.
- **All copies withdrawn**: cancel all holds and notify? Probably; needs wording.
- **Reporting**: Odile will want "most-held titles" for purchasing; outside the slice, but `Reservation` has what's needed.

---

*Next: walk through with Tamsin on Thursday, then start step 1.*
