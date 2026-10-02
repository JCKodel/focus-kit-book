# Error codes list

Maintained by BA. Last checked against the code: **2026-08-24**.

All fallible functions return a `Result` from `shared/result.ts`: either `{ ok: true, value }` or `{ ok: false, error }`, built with `ok()` / `err()`. Nothing throws for business-rule failures. The `error` is always one of the kebab-case string codes below.

If you add or rename a code: update the union type in the slice, add a test that produces it, and update this list. In that order. (If this list and the code disagree, the code wins — then please fix the list.)

---

## books — `features/books/book.ts`

`BookError` (from `createBook`)

| code | meaning |
|---|---|
| `title-required` | title is empty after trimming |
| `author-required` | author is empty after trimming |
| `invalid-isbn` | an ISBN was given but isn't a valid one (see cataloguing chat 22 apr) |

`CopyError` (from `addCopy`, `withdrawCopy`)

| code | meaning |
|---|---|
| `copy-id-required` | copy id is empty after trimming |
| `copy-on-loan` | tried to withdraw a copy that is currently on loan |
| `already-withdrawn` | tried to withdraw a copy that is already withdrawn |

## members — `features/members/member.ts`, `librarian.ts`

`MemberError` (from `registerMember`, `suspendMember`, `reinstateMember`)

| code | meaning |
|---|---|
| `name-required` | member name is empty after trimming |
| `invalid-email` | email (trimmed, lower-cased) doesn't look like an email |
| `reason-required` | suspending with an empty reason |
| `already-suspended` | suspending a member who is already suspended |
| `not-suspended` | reinstating a member who isn't suspended |

`LibrarianError` (from `createLibrarian`)

| code | meaning |
|---|---|
| `name-required` | librarian name is empty after trimming |

Yes, `name-required` exists in both. Different types, same meaning; that's fine.

## loans — `features/loans/loan.ts`

`LoanError` (from `checkOut`, `returnCopy`, `renewLoan`)

| code | where | meaning |
|---|---|---|
| `member-suspended` | checkOut, renewLoan | member is currently suspended |
| `member-has-overdue-loans` | checkOut | member has at least one active overdue loan |
| `loan-limit-reached` | checkOut | member already has 5 active loans (`MAX_ACTIVE_LOANS`) |
| `copy-withdrawn` | checkOut | the copy has been withdrawn |
| `copy-not-available` | checkOut | the copy is already on loan |
| `copy-mismatch` | returnCopy | the copy handed in isn't the one on this loan |
| `already-returned` | returnCopy, renewLoan | the loan has already been returned |
| `loan-overdue` | renewLoan | the loan is overdue, so it can't be renewed |
| `renewal-limit-reached` | renewLoan | loan already renewed `MAX_RENEWALS` (2) times |

Check order in `checkOut`: suspended → overdue loans → loan limit → copy withdrawn → copy on loan. In `renewLoan`: returned → suspended → overdue → renewal limit. You get the first one that applies, not a list.

`returnCopy` has no member checks at all — returning is never refused for who the member is.

## suspension — `features/loans/suspension.ts`

`SuspensionError` = all of `MemberError` **plus**:

| code | meaning |
|---|---|
| `still-has-overdue-loans` | `liftSuspension` refused: the member still has an overdue loan |

`liftSuspension` can also return `not-suspended` (via `reinstateMember`).

`applySuspensions` doesn't return a `Result` — it returns the member list, with newly suspended members updated and everyone else unchanged.

---

## Count

- books: 6
- members: 5 (+1 librarian)
- loans: 9
- suspension: 1 extra

## Notes

- Codes are part of the contract with whatever UI comes later; the desk will show a message per code. Don't rename casually.
- No `unknown-error` / catch-all. If something can't happen, it shouldn't have a code.
- Test files: `features/*/*.test.ts`. Every code above is produced by at least one test (checked 2026-08-24, `grep` + eyeballing).
