# Architecture session — 2026-02-03

**Who:** Tamsin (TO), Rafe (RL), Marek (MS), Bex (BA). Juno dropped in for the last 15 min.
**Topic:** How do we lay out the code? Layers (as in Rafe's draft) vs vertical slices.

---

## Starting point

Rafe's draft proposes `src/controllers`, `src/services`, `src/repositories`, `src/domain`. Tamsin asked to discuss the folder layout before anyone writes much code, since moving things later is annoying.

## Case for layers (Rafe)

- Familiar. Anyone joining knows where a controller goes.
- Clear dependency direction (top → down).
- Repositories as interfaces make swapping storage easy.
- Rafe: "It's boring, and boring is good."

## Case for slices (Tamsin, Marek)

- Tamsin: our domain is three things — books, members, loans. Most changes touch one of them end to end. In a layered layout, a change to "renewals" touches `controllers/`, `services/`, `repositories/`, `domain/`, and `test/services/`. Five folders for one rule.
- In slices it'd be `features/loans/` and that's it.
- Marek: we don't *have* controllers or storage yet. Two of the three layers would be empty or speculative. We'd be building scaffolding for things that are explicitly out of scope (no UI, no persistence per kickoff).
- Tests next to the code they test — Bex liked this a lot. Easier to see what's covered per feature.

## Concerns raised

- **Cross-slice dependencies.** Loans obviously need Copy (books) and Member (members). Rafe: "So the slices aren't independent anyway." Tamsin: fine — loans can import *types* and small functions from books/members. The rule is direction: books and members should not need to know about loans. Marek: what about suspension? It's a member thing but triggered by loans. Some back-and-forth. Leaning: the suspension *record* lives on members, the *rule* (when to suspend) lives in loans. Not fully settled — revisit when we build it.
- **Shared code.** Some things are used everywhere (whatever we do for errors, date helpers). Tamsin: a small `shared/` folder, kept deliberately tiny. If it starts growing, that's a smell.
- **Where do repositories go?** Agreed: we don't need them yet. When we do, they live in the slice that owns the data.
- Rafe asked whether this is premature too — "we're also designing folder structure for things that don't exist". Tamsin: slices are the smaller bet; you can always add a layer inside a slice later.

## Naming bikeshed (short, promise)

- `features/` vs `modules/` vs `src/`. Bex: "features" is what Juno calls them in the tracker anyway. Done.
- Test files: `books.test.ts` next to `book.ts`. One test file per slice to start, split if it gets long.
- Marek wants `shared/` to not be called `utils/` or `common/`, because those names attract junk. Agreed.

## Side discussion: errors

Rafe's draft throws `LoanError` subclasses. Marek and Tamsin both wondered about returning results instead. Rafe has been playing with it already. Agreed to take it as a separate decision rather than mix it into this one. Rafe to write up the findings.

## Juno (last 15 min)

- Doesn't mind either way structurally, but likes "features" because Odile could find the loans folder and read the test names.
- Asked that whatever we choose, we write it down so it doesn't get relitigated every sprint.

## Outcome

- Leaning clearly towards **vertical slices**: `features/books`, `features/members`, `features/loans`, plus a tiny `shared/`.
- Rafe is OK with it — "not my first choice, but I can't argue with the empty folders."
- Not formally decided in the room; Tamsin writes an ADR, everyone comments, then it's decided.

## Actions

- [ ] **TO** — ADR-001 on code structure (vertical slices), circulate by tomorrow
- [ ] **RL** — write up throwing vs result values notes → feeds an ADR on error handling
- [ ] **MS** — dates write-up still pending; aim for end of week
- [ ] **BA** — move the plain-English test list into per-feature sections (books / members / loans)
