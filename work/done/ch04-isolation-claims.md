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
* [x] Both editions explicitly pass the changed-contract and stale-client counterexamples; no claim says a new feature changes no other or that client/server decisions can never disagree.

* [x] Both editions say the same thing, using docs/03's terms and Portuguese example names.
* [x] The opening states the reader's value and the gain is supported; no filler added or useful explanation cut; every number and quoted artifact has its source (docs/00 and docs/04).
* [x] `make verify` and `make book` pass; the author receives `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf` for the passage checks (docs/05 §5).

**Built.** Both editions of chapter 4. Scalable: a change to one feature's implementation stays in its folder, the coupling between slices is what one imports from another (Bogard's rule), and a change to a contract reaches its consumers: `loans/rules.ts` imports `Member` (pt `emprestimos/regras.ts`, `Membro`), so a change to it changes the input of `lend` and the imports name the slices whose tests to run again. What the team gains: the change and the agent's reading are scoped to one feature's implementation plus what the slice imports; the reviewer reads the diff's folders and, for a changed import, the importers and their tests; the shared `mayBorrow` (pt `podePegarEmprestado`) is a pure function on possibly old client data, `overdue: 0` on the client against `overdue: 1` on the server, so `lend` refuses with `HasOverdueBooks` and the `Refused` reply updates the client; the import gives the rule only, the server fetches the member and decides, and the client imports no `.server.ts` file. Key points: Scalable and the last bullet say the same.

**Divergences.** None. No Case A or Case B passage was used or changed; the Ninjobs paragraph ch07-ninjobs-focus committed is untouched.

**Decisions.** The opening makes no isolation or agreement claim and is unchanged. The stale-client example uses chapter 3's `Member` and its `overdue` field, with illustrative values, so no new concept or counted number enters. "Removing loans from the product removes one folder" (Vertical slices) also promises more than the chapter's own imports allow, but that section is outside this page's contract: it becomes a new queue line for M20.

**Proof.** `grep` for "changes no other", "never disagree", "não muda nenhuma outra" and "nunca discorda" in both chapter files finds nothing. `make verify` green after the last edit; `make book` is run once by the batch driver for `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`, for the author's passage checks.

**Delivery review.** A read-only agent on Opus read `git diff HEAD` of both chapter files against this page, docs/04 and chapter 3's pure function. Points: (1) "removing loans removes one folder" contradicts the added counterexample: outside the contract, a new M20 line. (2) "nothing about another feature" in the gain: now "from another feature only what the slice imports, such as `Member`". (3) "the server still checks what the client sends" misdescribes an event that carries only ids: "the server still fetches the member and decides for itself". (4) The key point said the contract names its consumers: "the imports of a changed contract name the slices to check". (5) "whose tests run with it" suggested automation: "whose tests to run again". (6) ", Bogard's goal" read loosely: "as Bogard's rule asks". (7) pt "velho" for data: "desatualizado". (8) Optional merge of two sentences: kept, the server's refusal stays explicit. Verify ran again after the fixes.

```commit
docs(ch04-isolation-claims): keep slices local, check changed contracts

- Scalable: a change inside a slice stays there; a contract has consumers
- The imports of a changed type name the slices whose tests to run
- The shared rule on old client data can decide differently
- The server fetches the member and its refusal updates the client

work/done/ch04-isolation-claims.md
```
