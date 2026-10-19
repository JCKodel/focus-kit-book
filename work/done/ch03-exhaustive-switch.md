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
* [x] Compile both editions' complete examples and the missing/added-case variants with the recorded TypeScript version and settings; record expected failures and successful repairs on this page.
* [x] Read every exhaustiveness claim in the chapter against the ordinary-switch counterexample; the distinction is consistent throughout.

* [x] Both editions say the same thing, using docs/03's terms and Portuguese example names.
* [x] The opening states the reader's value and the gain is supported; no filler added or useful explanation cut; every number and quoted artifact has its source (docs/00 and docs/04).
* [x] `make verify` and `make book` pass; the author receives `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf` for the passage checks (docs/05 §5).

**Built.** Both editions of chapter 3: the opening, Result, the exception bullet, Why not throw, the gain and the key points now say the type makes the check possible and the handler asks for it; "Every case handled" keeps the union and the `Record`, says what fails when `MemberSuspended` is left out or a refusal is added, adds `messageFor` (pt `mensagemPara`) with a `never` check in `default`, explains the narrowing and the diagnostic, and gives the counterexample: a switch with a generic `default`, or one whose branches return nothing, compiles with a case missing. Source note `[^ts-handbook]` on the two Handbook sections. docs/03: the Result row says the handler asks for the check; the running example row adds `mensagemPara`.

**Divergences.** None. No Case A or Case B passage was used or changed.

**Decisions.** The switch gives the same messages as the `Record`, so the two forms compare on one table and no new concept (an HTTP status, a screen action) enters the chapter. The `default` returns the `never` value, as the Handbook does, and does not throw. A value-returning switch with no `default` fails with TS2366 on the function without naming the case; the Result section says so in one clause and the chapter's line stays on the `never` check. docs/03 lists the new function name only, as it lists `consultar`, and not the local `naoTratada` or `mensagem`.

**Proof.** TypeScript 5.9.3 (`npx -p typescript@5.9.3 tsc --strict --erasableSyntaxOnly --noEmit`) on the two blocks extracted from each edition, with variants written for this proof; Node v26.12.0 ran the complete English blocks.
Complete, both editions: exit 0. `MemberSuspended` / `MembroSuspenso` removed from the map: TS2741, the property is missing but required in `Record<LendRefusal, string>` (pt `Record<RecusaDeEmprestimo, string>`). Removed from the switch: TS2322, `Type '"MemberSuspended"' is not assignable to type 'never'` (pt `"MembroSuspenso"`) at the `const` line. A fourth refusal added to the union: both TS2741 and TS2322, naming it; with its entry and its case restored: exit 0. Counterexamples: a switch with a generic `default` and a `void` switch, each missing a case, exit 0; a value-returning switch with no `default` missing a case, TS2366 on the function.
`make verify` green after the last edit; `make book` is run once by the batch driver for `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`, for the author's passage checks.

**Delivery review.** A read-only agent on Opus read `git diff HEAD` of both chapter files and the docs/03 patch against this page and docs/04, and recompiled the switch variants. Points: (1) "a `switch` that leaves a case out compiles like any other" ignored TS2366: narrowed in both editions to "still compiles when it has a `default` or returns nothing, and when it fails, its error does not name the case". (2) The proof and ticks were not yet on the page: recorded above. (3) "Asked for, the check" read abruptly: "When the handler asks for it, the check", pt "Quando o tratamento a pede". (4) docs/03 lists `mensagemPara` but not `naoTratada` or `mensagem`: kept, the row lists function and type names, not locals (see Decisions). Verify ran again after the fixes.

```commit
docs(ch03-exhaustive-switch): ask for the exhaustive check with never

- A Result makes the cases checkable; the handler asks for the check
- Every case handled adds messageFor with a never check in default
- A generic default or a void switch compiles with a case missing
- docs/03: the Result row and mensagemPara; source note on the Handbook

work/done/ch03-exhaustive-switch.md
```
