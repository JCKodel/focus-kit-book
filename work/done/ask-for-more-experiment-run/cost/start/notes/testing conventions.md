# Testing conventions

Owner: Bex Amadi · written 2026-04-02 after the March retro · agreed by the team

How we write tests in this repo. If you're about to do something different, talk to Bex first or update this page.

## Tooling

- `node:test` for `describe` / `it`, `node:assert/strict` for assertions. Always the **strict** variant.
- Run with `npm test` (= `node --test`). No test framework, no assertion library, no mocking library.

## Where tests live

- Next to the code, in the same slice: `features/loans/loan.ts` → `features/loans/loans.test.ts`.
- File name ends in `.test.ts` so the runner finds it.
- A test file only imports from its own slice and from `shared/`, plus *types* from other slices when it needs to build inputs (a loans test needs a `Copy` and a `Member`).

## Structure: one `describe` per behaviour

- One `describe` block per behaviour or function: `describe('checkOut')`, `describe('returnCopy')`, `describe('overdue')`, `describe('suspension of members')`.
- Not one `describe` per file, and no deep nesting. Two levels max (`describe` → `it`).
- The cases inside read top to bottom as: happy path first, then each refusal.

## Naming: plain language

Test names are sentences someone at the library could read. Odile and Wren have looked at the test output in a demo, and that's the standard.

Good:
- `refuses a suspended member`
- `returned loans do not count towards the limit`
- `a suspended member cannot renew`
- `cannot withdraw a copy twice`

Not good:
- `test checkOut 3`
- `should return err when member.suspension !== undefined`
- `LOAN_LIMIT edge case`

No "should". Say what happens.

## Build plain objects, don't mock

- The domain is plain data and pure functions, so tests build plain objects:
  ```ts
  const member: Member = { id: 'M1', name: 'Tobin Vale', email: 'tobin@example.org' };
  const copy: Copy = { id: 'C-1', bookId: 'B1', status: 'available' };
  ```
- No mocks, no spies, no stubs. If you feel the need for one, the function probably has a hidden dependency (like reading "today" itself) — fix the function instead. `today` is always a parameter.
- Small builder functions with overrides are fine and encouraged:
  ```ts
  function loan(overrides: Partial<Loan> = {}): Loan {
    return { id: 'LN1', /* … */ renewals: 0, ...overrides };
  }
  ```
  `loan({ returnedOn: '2026-03-10' })` says exactly what's special about this case.

## No shared mutable fixtures

This is the one from the retro.

- Module-level constants are fine **only** if nothing ever changes them. Our domain types are `readonly`, which helps; don't cast it away.
- No `let` at module level holding test data. No `beforeEach` that resets arrays. No test that pushes into a list another test reads.
- If a test needs a list, build it inside the test (`Array.from({ length: MAX_ACTIVE_LOANS }, ...)`).
- Every test must pass when run alone with `--test-name-pattern`.

## Asserting Results

- Business failures come back as `Result`, never thrown. Assert the whole thing with `deepEqual`:
  ```ts
  assert.deepEqual(checkOutFor(suspended, copy), { ok: false, error: 'member-suspended' });
  ```
- For success with a big value, `assert.ok(result.ok)` first (it narrows the type), then check the fields that matter.
- Use the exported constants (`MAX_ACTIVE_LOANS`, `LOAN_PERIOD_DAYS`) instead of repeating magic numbers, except in one test per constant that pins the actual value.
- Don't use `assert.throws` for domain rules. If something throws, that's a bug.

## Checklist for a PR

- [ ] new behaviour has a happy-path test and a test for each new error code
- [ ] names read as sentences
- [ ] no mocks, no shared mutable state
- [ ] `npm test` green locally
