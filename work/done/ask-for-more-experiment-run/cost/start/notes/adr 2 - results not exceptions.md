# ADR 2 — Business failures are results, not exceptions

Status: **Accepted**
Date: 2026-02-10
Decided by: TO, RL, MS, BA (PO informed)
Related: ADR-001 (vertical slices), Rafe's error-handling notes

---

## Context

Most domain operations can fail for ordinary business reasons:

- a member is suspended and tries to borrow
- a member already has the maximum number of loans
- a copy is already on loan, or has been withdrawn
- a loan was already returned
- a book is created without a title

None are bugs; they're expected outcomes the desk shows a librarian ("Can't lend — member is suspended").

The early loan design threw error classes (`LoanError`, `MemberSuspendedError`, ...). Rafe then tried both styles (see `rafe-notes-error-handling.md`):

- With exceptions, signatures don't show how a function can fail.
- Untyped `catch`: `catch (e)` gives `unknown`, and you're back to `instanceof` chains.
- Forgetting a case is easy and nothing warns you.
- "Fails with X" tests are clunkier with `assert.throws` + class checks.
- Domain functions are pure (no I/O), so no async/stack-unwinding argument applies.

## Decision

1. **Business failures are returned, never thrown.** Such operations return a `Result`.

2. **The `Result` type** lives in `shared/result.ts`:

   ```ts
   export type Ok<T> = { readonly ok: true; readonly value: T };
   export type Err<E> = { readonly ok: false; readonly error: E };
   export type Result<T, E> = Ok<T> | Err<E>;

   export function ok<T>(value: T): Ok<T> { return { ok: true, value }; }
   export function err<E>(error: E): Err<E> { return { ok: false, error }; }
   ```

   Callers narrow on `result.ok`; plain `if`, no helper library or `map`/`flatMap` for now.

3. **Errors are kebab-case string literals**, grouped as union types per slice:

   ```ts
   export type LoanError =
     | 'member-suspended'
     | 'member-has-overdue-loans'
     | 'loan-limit-reached'
     | 'copy-withdrawn'
     | 'copy-not-available'
     | 'already-returned';
   ```

   - lowercase, describing *what is wrong*, not what to do
   - no error classes or message strings in the domain; the desk/UI decides wording later
   - a slice's union can include another's when composing operations (e.g. `SuspensionError = MemberError | 'still-has-overdue-loans'`)

4. **Exceptions are only for programmer bugs**: an impossible state, a broken invariant, a malformed calendar date passed in by our own code. These may throw; the domain doesn't catch them.

5. **Tests compare results directly.**

   ```ts
   assert.deepEqual(checkOut({ ...input, member: suspended }), err('member-suspended'));
   ```

## Consequences

Good:

- Signatures document failure modes (`Result<Loan, LoanError>`).
- Exhaustiveness checks catch a missing `LoanError` case.
- Tests are short and read like the rules.
- Error codes are stable identifiers, mappable to desk messages (and translations, if ever) in one place.

Less good:

- More `if (!r.ok) return r;` boilerplate when chaining. Accepted: explicit, and chaining is rare.
- One error per call (the first failing rule), so check order is part of the behaviour; tests pin it where users see it (e.g. suspended before loan limit).
- No stack traces for business failures. Fine; they aren't bugs.

## Alternatives considered

- **Keep the error class hierarchy.** Rejected: untyped `catch`, no signal when a case is forgotten.
- **Return `null`/`undefined`.** Loses *why* it failed; the desk needs the reason.
- **A third-party result library.** Rejected: no dependencies, and the type is six lines.
- **Error objects with a `code` field.** Possible later, but strings suffice today and compare cleanly in tests.

## Not decided here

- Mapping error codes to human-readable messages (later, with whatever UI exists).
- A richer error payload (e.g. `{ code: 'loan-limit-reached', limit: 5 }`). Plain strings until needed.

## Actions

- RL: loan design sketches to return `Result` instead of throwing
- BA: rewrite the failing-case test names around error codes
- TO: add `shared/result.ts` with tests
