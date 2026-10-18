# ch04-isolation-claims

**Objective.** A reader can use FOCUS to reduce coupling while checking changed contracts and treating the server as authoritative when client and server data differ.

**Behaviour.**
* A feature that changes only its own implementation can keep its change local; the reader understands this as the architecture's aim, not a guarantee that every feature leaves every other file untouched.
* When a shared contract changes, the reader identifies and checks its consumers rather than assuming their tests cannot be affected.
* When the client has old member data but the server knows a loan is overdue, the same pure rule can produce different decisions; the server refuses the loan and its reply updates the client.
* Importing a shared pure function never makes client input trustworthy, replaces server validation, or permits importing a server-only repository into the client.

**Contract.** `book/en/04-focus.md` and `book/pt/04-focus.md`: Scalable, What the team gains, and matching opening/key-point claims.
Keep FOCUS optional, its four pieces and its shared-rule example; qualify isolation and identical decisions using the existing inputs/outputs model from chapter 3.
Sources: Jimmy Bogard's coupling goal, already cited as `bogard-vertical-slice` (<https://www.jimmybogard.com/vertical-slice-architecture/>), the chapter's dependency rule, and docs/03's pure-function definition.
Decision from docs/06: sharing code avoids duplicate rule definitions but cannot make two different inputs equal.
No new domain concept, number or private case.

**States.** Inapplicable: chapter prose, no new screen.

**Visual reference.** Inapplicable: the existing book layout.

**Out of scope.** Redesigning FOCUS, adding a synchronization mechanism or implementing a library: the correction is to what the current examples guarantee.

**Done when.**
* [ ] Both editions explicitly pass the changed-contract and stale-client counterexamples; no claim says a new feature changes no other or that client/server decisions can never disagree.

* [ ] Both editions say the same thing, using docs/03's terms and Portuguese example names.
* [ ] The opening states the reader's value and the gain is supported; no filler added or useful explanation cut; every number and quoted artifact has its source (docs/00 and docs/04).
* [ ] `make verify` and `make book` pass; the author receives `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf` for the passage checks (docs/05 §5).
