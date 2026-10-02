# Librarians vs members

TO, 2026-04-22. Short note because this came up three times in a week and the answer should live somewhere.

## The question

Wren asked, half-joking, at the April session: "So can I borrow books in this thing or not?" Then Rafe hit the same question from the other side while writing `checkOut` — it takes a `member` and a `librarian`, and Rafe wondered whether a librarian should just *be* a member with an extra flag (`isStaff: true`), since they're both people with names.

Bex's version: "Is there a test for a librarian lending to themselves?"

## Answer: two different things

**Librarians are staff, not members.**

- `Librarian` is `{ id, name }` and lives in `features/members/librarian.ts`. It's an actor: issues loans (`issuedBy`), withdraws copies (`withdrawnBy`), suspends members (`suspension.by`), runs `applySuspensions`, lifts suspensions.
- `Member` is `{ id, name, email, suspension? }`. It's a borrower: has loans, has a loan limit, can be suspended.
- Nothing in the model is both. No `isStaff` flag, no shared base type, no role list.

**A librarian who wants to borrow registers separately as a member.** Just like anyone else: `registerMember` with their name and email, gets a member id, follows the same rules — 5 loans, same loan period, same overdue and suspension rules. Their librarian record and their member record are unrelated as far as the model knows.

## Why not one "person" with roles

Discussed with Odile and Juno, 2026-04-20:

- **Different lifecycles.** Staff join and leave the library's employ; members join and lapse. Odile doesn't want a staff departure to touch someone's borrowing record or vice versa.
- **Different data.** A librarian doesn't need an email in the model; a member must have one. A member can be suspended; "suspending a librarian" isn't a thing here.
- **No special treatment.** Odile was clear: staff borrow under the same rules as the public. That's how it works in CardBox too — staff have ordinary cards. Modelling them as members-with-a-flag invites someone to add "staff get 10 loans" later.
- **Simpler code.** `checkOut` reads naturally: *this librarian* lends *this copy* to *this member*.

## Edge cases we talked through

- **Librarian lends to their own member record.** Allowed — the model can't tell, and doesn't try. Odile: at Saltgate there's usually someone else on the desk, and if not, it's fine. Not worth a rule.
- **Librarian suspends or reinstates their own member record.** Same — not prevented. Odile trusts staff; if it becomes a problem it's an HR conversation, not a code one.
- **Two records, one human.** Yes, deliberately. If reports ever need "which members are also staff", we'll add a link then, not before.
- **Volunteers** (Saturday helpers): not librarians in the model unless they issue loans. Juno to check with Odile whether volunteers do. *(Update 2026-05-05, JA: they don't; they shelve.)*

## In the code

Comment at the top of `librarian.ts` says it in one line. Glossary has the short version under "Librarian". `createLibrarian` only checks for a name (`name-required`); there's deliberately nothing else to validate.

Actions:
- [x] TO — this note
- [x] RL — leave `checkOut` signature as is
- [x] BA — no "librarian lends to self" test; noted as deliberately unconstrained
