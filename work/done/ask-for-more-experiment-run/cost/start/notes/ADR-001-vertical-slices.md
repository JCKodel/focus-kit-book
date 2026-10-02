# ADR-001: Organise code as vertical slices

- **Status:** Accepted
- **Date:** 2026-02-04
- **Author:** Tamsin Oduya
- **Reviewed by:** Rafe Lindqvist, Marek Szolt, Bex Amadi; Juno Achterberg (FYI)

## Context

We are building a domain model for the Hollowmere Lending Library: books and their copies, members, and loans. The kickoff (2026-01-12) set the scope as the domain model plus tests only. There is no UI, no storage, and no import from CardBox in scope.

We need a code layout before the codebase grows. Two options were discussed at the architecture session on 2026-02-03:

1. **Layers.** `controllers/`, `services/`, `repositories/`, `domain/`, with tests in a separate `test/` tree.
2. **Vertical slices.** One folder per feature area (`books`, `members`, `loans`), each holding its code and tests together.

Observations from that session:

- Most changes we expect are about one area of the library's rules ("how renewals work", "when copies can be withdrawn"). In a layered layout such a change is spread over four or five folders.
- Two of the layers (controllers, repositories) would be empty or speculative, because the things they abstract over are out of scope.
- Loans genuinely depend on books (copies) and members. The slices are not independent, and we shouldn't pretend they are.
- Some code is needed everywhere: the error-handling approach (see ADR 2, in progress) and date helpers.
- The library staff should be able to find "the loans rules" and read test names. A `features/loans` folder makes that easy.

## Decision

We organise the code as vertical slices:

```
features/
  books/      book.ts, books.test.ts
  members/    member.ts, librarian.ts, members.test.ts
  loans/      loan.ts, suspension.ts, loans.test.ts
shared/
  result.ts
  dates.ts
```

Rules:

1. **A slice owns its code and its tests.** Tests live next to the code (`*.test.ts`) and run with `node --test`. No separate test tree.
2. **`shared/` is a small kernel.** Only things that are truly generic and used by more than one slice go there: the result type and calendar-date helpers. Domain concepts never go in `shared/`. If `shared/` grows beyond a handful of small files, we stop and talk about it.
3. **Cross-slice imports are allowed, in one direction.** `loans` imports types and small pure functions from `books` (e.g. `Copy`) and `members` (e.g. `Member`, `isSuspended`, `Librarian`). `books` and `members` do not import from `loans`. Members must not know about loans. Books must not know about loans.
4. **Cross-cutting rules live where the knowledge is.** Example: the suspension record (who, when, why) is part of a member and lives in `members`. The *rule* for when someone is suspended depends on loans, so it lives in `loans/suspension.ts` and calls into `members` to apply it.
5. **No layers inside slices until we need them.** If a slice later needs storage or an entry point, it gets them inside its own folder.

## Consequences

**Positive**

- A rule change is usually a change to one folder plus its test file.
- No empty scaffolding. The code we have is the code we need.
- Test coverage is visible per feature. Bex can see at a glance what's tested in loans.
- Odile and Juno can be pointed at `features/loans/loans.test.ts` and read the rules in plain-ish English.

**Negative / risks**

- Less familiar for people used to layered layouts. Mitigated by this ADR and the README.
- Cross-slice imports could drift into a tangle. We rely on the direction rule above; review catches violations. If it becomes a problem we can add a check script.
- `shared/` could become a junk drawer. Rule 2 is the guard; anyone adding a file there flags it in review.
- Where suspension lives took some discussion and may again for future cross-cutting rules. Rule 4 is our default answer.

**Neutral**

- Anything we design later (persistence, a desk UI) will be designed per slice when it comes up, not up front.

## Notes

- Rafe raised fair points in favour of layers, especially familiarity. Agreed to revisit if the codebase grows past what one person can hold in their head; we don't expect that within this project.
- Error handling is decided separately (ADR 2).
