# ch03-exhaustive-switch

**Objective.** A reader can make TypeScript check every refusal with a `Record` or an explicit `never` check, and knows that declaring `Result` alone does not enforce exhaustive handling.

**Behaviour.**
* With the three existing lending refusals, a complete message `Record` and a complete switch with a `never` check compile.
* Remove `MemberSuspended` from the map or its switch branch: each checked example fails compilation at the missing coverage.
* Add a refusal to the union without adding either handler: both examples fail; restoring the handlers makes them compile.
* An ordinary switch that omits a case can compile when no exhaustive check requires it; the text does not promise otherwise or suggest that a generic default message proves completeness.

**Contract.** `book/en/03-simplicity-and-results.md` and `book/pt/03-simplicity-and-results.md`: Result, Exception/refusal/error, Why not throw, Every case handled, opening, gain and key points wherever they promise automatic coverage.
Preserve the existing refusal union and `Record`; add a short authored TypeScript switch whose remaining value must be `never`, with an explanation of the diagnostic when a case remains.
Use docs/03's existing Portuguese identifiers.
Primary references: TypeScript Handbook, Narrowing, Exhaustiveness checking (<https://www.typescriptlang.org/docs/handbook/2/narrowing.html#exhaustiveness-checking>), and Utility Types, Record (<https://www.typescriptlang.org/docs/handbook/utility-types.html#recordkeys-type>).
Decision from docs/06: the representation enables the check; the handler and compiler enforce it.
No new domain concept or private case.

**States.** Inapplicable: chapter prose, no new screen.

**Visual reference.** Inapplicable: the existing book layout.

**Out of scope.** Catch-boundary changes: `ch03-query-catch`; permanent example runner: `verify-examples`; other-language examples: docs/00 limits code to TypeScript.

**Done when.**
* [ ] Compile both editions' complete examples and the missing/added-case variants with the recorded TypeScript version and settings; record expected failures and successful repairs on this page.
* [ ] Read every exhaustiveness claim in the chapter against the ordinary-switch counterexample; the distinction is consistent throughout.

* [ ] Both editions say the same thing, using docs/03's terms and Portuguese example names.
* [ ] The opening states the reader's value and the gain is supported; no filler added or useful explanation cut; every number and quoted artifact has its source (docs/00 and docs/04).
* [ ] `make verify` and `make book` pass; the author receives `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf` for the passage checks (docs/05 §5).
