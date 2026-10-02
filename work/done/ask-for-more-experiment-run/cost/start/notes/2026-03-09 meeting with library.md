# Meeting with the library — 2026-03-09

Present: Odile Fenwick, Wren Halloway, Juno Achterberg, Tamsin Oduya
Notes: Juno
Location: Saltgate branch, reading room (after closing)

---

## TL;DR

- **Loan period → 21 days** (was 14 from kickoff).
- **Max 5 active loans** per member (was 3).
- Renewals: discussed, **decide later**.
- Prototype feedback mostly positive; a few wording and flow fixes.

---

## 1. Prototype demo

Tamsin walked through the prototype in the terminal + a rough screen Rafe built: register a member, add a book and copies, check out, return, the suspension flag.

Feedback:

- **Wren:** checkout is "faster than CardBox already" — no hunting for spreadsheet tabs. Likes that refusals say *why* (member-suspended, loan-limit-reached etc.), but wants plain words on screen. Tamsin: codes are for the program; the screen translates.
- **Wren:** wants to see who withdrew a copy and when. Already modelled (`withdrawnBy`, `withdrawnOn`).
- **Odile:** suspended state must be impossible to miss on the member screen. UI, not domain.
- **Odile:** what shows when a member has something overdue but isn't suspended? Currently nothing; checkout goes through. Odile wants a visible desk warning. UI note for now; Rafe to consider where a "has overdue loans" check would live.
- **Wren:** returning is one scan, good; works for suspended members.
- **Wren:** member search by email as well as name? App layer; noted for Rafe.

## 2. Loan period

Odile opened: 14 days is too short. Wren's informal tracking at Saltgate since January: many loans get renewed once, mostly in the last couple of days, by people coming in *just* to renew.

> Odile: "Fourteen days was the CardBox default because someone typed it in in 2011. People kept coming back to renew. Make it three weeks."

- Agreed: **21 days**.
- Tamsin: one constant (`LOAN_PERIOD_DAYS`) plus tests with hardcoded due dates. Small.
- Juno: different periods per material type (e.g. new releases)? Odile: not now; one period for everything.

## 3. Loan limit

- Kickoff said 3. Wren: families borrow lots of picture books at once and 3 is a constant argument at the desk.
- Odile proposed 5; Wren would have liked more but 5 is fine.
- Agreed: **max 5 active loans** per member. Returned loans don't count.

## 4. Renewals

Longer discussion, no conclusion.

- Kickoff assumed unlimited. With 21 days, Odile expects less need.
- Wren: unlimited means popular books never come back.
- Options: unlimited / max 1 / max 2 / none.
- Renewing something overdue? Odile leaning no.
- Odile wants a few weeks of 21-day loans in practice first.
- **Decision: decide later.** Keep renewal code in, keep the limit a constant, don't treat the current value as final.

## 5. Other bits

- Fines: still undecided on the library's side; Odile would rather avoid money entirely if suspension works. Nothing for us to do.
- Wren asked about importing the CardBox member list. Tamsin: not this phase; domain model first.
- Odile wants the suspension rule reviewed with real numbers — four weeks may be too lenient. Revisit later.

---

## Decisions
1. Loan period 21 days.
2. Max 5 active loans per member.
3. Renewals: undecided, revisit later.

## Actions
- [ ] RL — `LOAN_PERIOD_DAYS = 21`, `MAX_ACTIVE_LOANS = 5`, update tests
- [ ] RL — sketch an `overdueLoans(loans, today)` helper the screen can use for the warning
- [ ] BA — test cases for the loan limit: returned loans and other members' loans don't count
- [ ] JA — draft plain-language messages for each error code, review with Wren
- [ ] JA — schedule renewals follow-up with Odile (April/May)
- [ ] TO — write up decisions as a note on the shared drive
