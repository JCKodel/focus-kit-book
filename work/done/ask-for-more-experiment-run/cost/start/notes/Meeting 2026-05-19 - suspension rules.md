# Meeting 2026-05-19 — suspension rules (revisited)

**Time:** Tue 19 May, 14:00–15:00, Saltgate back office
**Attendees:** Odile Fenwick, Wren Halloway, Juno Achterberg, Tamsin Oduya, Marek Szolt, Bex Amadi
**Apologies:** Rafe (on leave, back Thu)
**Notes:** MS

## Why

Follow-up promised on 8 Apr: "revisit threshold in ~6 weeks". Wren has run `applySuspensions` on a test copy of the sheet data three Mondays running. Reinstatement bottleneck again too — Odile was away a week in early May and two members couldn't be reinstated meanwhile. One had returned everything and came in twice asking why they still couldn't borrow; Wren explained both times, not thrilled.

Juno: not redesigning suspension, just fixing the two rules the trial runs showed were wrong.

What we're revisiting:

- **Threshold:** 28 days overdue (Feb 11).
- **Reinstatement:** only the head librarian (Jan 26).

## 1. Threshold

Wren's rough numbers from the three trial runs:

- at 28 days: ~4–6 members flagged each week
- people Wren would *actually* have suspended by hand: ~12–15

28 days catches under half of the desk's problem cases. Wren: "By four weeks overdue the book's basically gone. Two weeks is when I start ringing."

Odile asked if 14 days would be too harsh. Discussion:

- No fines (ADR-004), so suspension is the *only* consequence; too lenient means none at all.
- Suspension is cheap to reverse (point 2), so slightly harsh costs less.
- Juno: members already get 21 days plus up to two renewals; 14 days beyond *that* is long.

Marek: at 14 or after 14? Agreed: **more than 14 days overdue**; exactly 14 isn't enough, 15 is. `SUSPEND_AFTER_DAYS_OVERDUE = 14`, compared with `>`.

Member reason text becomes "loan more than 14 days overdue", generated from the constant so they can't drift.

**Decision: suspend once any loan is more than 14 days overdue.** Replaces the 28-day rule from Feb 11.

## 2. Reinstatement

Current rule (Jan 26): only Odile can reinstate. Problems:

- Odile is a bottleneck, especially on leave.
- Librarians already have the conversation with the member, then must find Odile.
- Odile, roughly: "I don't need to be the one who presses the button. I need to trust whoever does."

Bex: what stops reinstatement while the overdue book is still out? Today, only Odile's judgement.

Agreed:

- **Any librarian can lift a suspension.**
- **But only once the member has no overdue loans left.** Anything still overdue → `still-has-overdue-loans`.
- Lifting is a separate step — returning the last overdue book does *not* auto-reinstate. Wren prefers that ("I want to see them at the desk").

**Decision: any librarian may reinstate, once nothing is overdue anymore.** Replaces the head-librarian-only rule from Jan 26.

## 3. Things re-confirmed (no change)

- A librarian runs suspensions and is recorded on each, with date and reason (8 Apr).
- **Suspended members can always return books.**
- Suspended members can't check out or renew.
- No fines (ADR-004).

## Code impact

- `SUSPEND_AFTER_DAYS_OVERDUE` 28 → 14, `>` comparison (features/loans/suspension.ts)
- New `liftSuspension(member, loans, today)` in loans slice; checks overdue loans, then calls members' `reinstateMember`. Members slice stays free of loan knowledge.
- Remove the "head librarian" flag check on reinstate.
- Error `still-has-overdue-loans` (suspension errors = member errors + this one).

## Actions

- [ ] **RL** (Thu) — constant + `liftSuspension`; drop head-librarian check
- [ ] **BA** — tests: exactly 14 days overdue → not suspended; 15 → suspended; already-suspended member unchanged by `applySuspensions`; lift refused while overdue; lift ok after return; suspended member can return
- [ ] **MS** — check `daysOverdue` against month boundaries for the 14/15 tests
- [ ] **JA** — update the rules sheet for desk staff; send to Odile for a read
- [ ] **TO** — review Thursday's PR
- [ ] **WH** — keep doing the Monday trial run for another month, report counts
