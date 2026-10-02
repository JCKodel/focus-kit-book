# Copies and withdrawal

_Rafe, 2026-04-28. Reviewed by Tamsin and Bex. Odile signed off 2026-04-30._

## The problem

Since the Jan 26 domain session we've had copy statuses `available | on-loan | lost | damaged`. Implementing it, a few things didn't hold together:

- **Lost and damaged end up in the same place.** Asked Wren what actually happens to a damaged book: if it can be fixed, it's fixed at the desk and goes back on the shelf (never really stops being available). If it can't, it's thrown out or sent to the book sale. A lost book: same end state — gone from the shelf for good.
- **"Lost" is not something we observe.** A book becomes "lost" when a librarian decides it's not coming back. That's a decision, made by a person, on a date.
- Nobody at Saltgate could name a case where the *difference* between lost and damaged changes what the system should do. Odile: "Either we have it or we don't."
- We dropped replacement charges with ADR-004, which was the only thing that cared about the reason.

## Decision

Copy status is now just:

```
available | on-loan | withdrawn
```

- **Lost and damaged copies are withdrawn.** There are no separate `lost`/`damaged` statuses any more.
- Withdrawal is done by a **librarian** and records **who** (librarian id) and **when** (calendar date): `withdrawnBy`, `withdrawnOn`.
- **An on-loan copy can't be withdrawn** → `copy-on-loan`. It has to be returned first. If a member says they lost it, the loan is closed at the desk and then the copy is withdrawn — two steps, on purpose.
- Withdrawing twice → `already-withdrawn`.
- A withdrawn copy can't be checked out → `copy-withdrawn` (distinct from `copy-not-available`, so the desk can tell "gone for good" from "someone has it").
- Withdrawal is one-way in the model. If a "lost" book turns up, it gets added again as a new copy. Wren: happens maybe twice a year, fine.

We considered keeping a free-text `reason` on withdrawal ("lost", "water damage", "sale"). Tamsin's view: nobody's asked for a report on it, add it if someone does. Left out.

## Copies vs books

To restate, since it keeps coming up:

- A **Book** is the title: title, author, optional ISBN.
- A **Copy** is the physical thing on the shelf. Each copy has its own id and status. One book, many copies.
- Copy ids at Saltgate look like `C-0001` (that's the sticker on the spine). The only rule in the model is that the id isn't empty after trimming → `copy-id-required`. We don't validate the format; there are older stickers that don't follow it and Wren isn't relabelling them.
- `availableCopies(copies, bookId)` returns the copies of a book with status `available` — what the desk wants when someone asks "do you have this?".

## Flow at a glance

```
addCopy        →  available
checkOut       →  on-loan
returnCopy     →  available
withdrawCopy   →  withdrawn   (only from available)
```

## What changed in code

- `CopyStatus` reduced to three values (features/books/book.ts)
- `withdrawCopy(copy, librarian, date)` added
- `markLost` / `markDamaged` removed (they were only on a branch, never merged)
- Tests: withdraw available ok; withdraw on-loan refused; withdraw twice refused; withdrawal records librarian + date; checkout of withdrawn copy refused

## Review comments

- Bex: wanted to know if withdrawing should check that the librarian exists. No — the model takes a `Librarian` value, so by the time you have one it's been created properly. Fine.
- Tamsin: keep `withdrawnBy` as the librarian id, not the whole librarian object. Agreed.

## Open

- Should withdrawing the *last* copy of a book do anything to the book? Currently no. Book stays in the catalogue with zero available copies. Odile is happy with that ("we might get another one").

## Actions

- [x] RL — implement above
- [x] BA — tests
- [ ] JA — tell Wren the desk process for "member says they lost it": return, then withdraw
- [ ] TO — update the glossary once the other notes settle
