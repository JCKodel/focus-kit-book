# ADR-004: No fines

- **Status:** Accepted
- **Date:** 2026-04-14
- **Deciders:** Juno Achterberg (PO), Odile Fenwick (head librarian), Tamsin Oduya (TL)
- **Supersedes:** the fines assumption from the 2026-01-12 kickoff ("fines likely 0.20/day, keep configurable")

## Context

At kickoff Odile said the council was "leaning towards" reintroducing overdue fines at 0.20 per day per item. Juno asked us to assume fines and keep the amount configurable. We built nothing — Tamsin wanted confirmation first — but it sat in the backlog and came up in every overdue discussion.

Since then:

- The council confirmed (via Odile, 2026-04-13) that the Hollowmere Lending Library **will not charge fines**.
- The library is council-funded. Taking money means a cash drawer, daily reconciliation, receipts, an authorised handler, and an audit trail for council finance. Saltgate has none of that and doesn't want it.
- Odile's view, for the record: fines mostly deter the members who'd benefit most, and CardBox-era fines were never worth the effort.
- We already have a lever for non-returners: **suspension** (see 2026-04-08 meeting). Free to administer and reversible.

## Decision

The domain model has **no concept of fines, fees or charges**.

- No fine amount, per-day rate, member balance or "paid" state.
- Overdue loans are handled by: (a) no renewing an overdue loan, and (b) suspension once a loan is overdue long enough. That's it.
- Returning is always possible however late — "you owe money" must never be a reason not to bring a book back.
- No replacement charges for lost or damaged items. That's a catalogue question, not a money one (separate note coming from Rafe).

## Consequences

**Good**

- Simpler model: no money, rounding, currency or partial payments.
- Nothing to reconcile or for the council to audit.
- Desk conversations stay about books.

**Less good**

- Suspension carries all the weight; if the threshold is too lenient, nothing else nudges people. Watch the threshold (Wren already thinks 28 days is too long).
- If the council changes its mind, fines would be a new concept touching members and loans. Acceptable — better than carrying unused config now.

**Neutral**

- The kickoff "keep it configurable" request is dropped, not deferred. Juno is fine with that.

## Alternatives considered

1. **Fines at 0.20/day, configurable.** Rejected: council said no; cash handling.
2. **Track a "notional" fine without collecting it**, as a score. Rafe floated this half-seriously. Rejected: a number nobody acts on; confusing at the desk.
3. **Capped fines** (e.g. max per item). Rejected as for 1.

## Discussion notes

- Marek asked whether this also means no deposits, e.g. for the local history collection. Odile: those items are reference-only and never leave the building. Not modelled.
- Bex asked whether existing tests assumed fines. Only two `todo` placeholders; nothing else changed.
- Wren's view (via Odile): members already feel bad about late books; old fines mostly made people keep the book longer rather than come in and pay. Anecdotal, but it matched Odile's CardBox memories.
- Juno: this is council policy, not a technical decision. Changes come through Odile, and we'd write a new ADR rather than edit this one.

## Follow-ups

- [x] JA — remove "fines" epic from the tracker
- [x] BA — delete the two placeholder fine tests (they were `todo` anyway)
- [ ] TO — make sure nobody adds a `fine` field "just in case" in review
- [ ] JA — get the council's decision in writing onto the shared drive
