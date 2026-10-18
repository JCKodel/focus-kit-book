# verify-examples

**Objective.** A maintainer running `make verify` sees chapter 3's database-boundary examples executed from the actual Markdown in both editions, so a broken example cannot pass unnoticed.

**Behaviour.**

* With the corrected synchronous and asynchronous query examples, verification accepts a successful value and a recognized database failure returned as Result, and observes the identical thrown bug or control object escaping the boundary; the asynchronous cases include a rejected promise awaited inside try.
* Changing either edition to translate every thrown value, or removing the asynchronous await, makes verification exit non-zero and identify the chapter and source line that failed.
* Removing a required example, making its extraction ambiguous, introducing a syntax error or lacking the required runtime fails with an actionable finding; no silent skip or successful empty suite.
* The implementation executes the examples extracted from each edition with only their declared supporting definitions and a deterministic fake driver. Changing only the Portuguese example can fail independently of English.
* Successful checks leave chapter files untouched and no generated source in the repository; no database, server or network is required to run the example cases.

**Contract.** Initial coverage is the Result/ok/err support and synchronous/asynchronous database boundary examples in `book/en/03-simplicity-and-results.md` and its same-named Portuguese edition, as corrected by ch03-query-catch.
Implement the extraction/check in scripts/, with diagnostics `file:line: examples: message` and non-zero exit on failure; Makefile verify invokes it, `.github/workflows/verify.yml` installs its runtime, and the owning descriptions in docs/01, docs/04 Tests, docs/05 Verify and the bilingual README document its coverage and runtime prerequisite.
Use the repository's existing Markdown fence parser to recognize code blocks and preserve source-line mapping.
The exact runnable contract comes from the chapter, not a copied implementation maintained in the test.

**States.** Inapplicable: command-line check, no screen.

**Visual reference.** Inapplicable.

**Out of scope.** Other chapters, exhaustiveness compilation checks owned by ch03-exhaustive-switch, a general snippet platform, real database integration, published playgrounds and changing query semantics, which belong to ch03-query-catch.

**Decisions from the documents.** The queue says to start with query; docs/05 §7's concrete error is the audit's bug/control object being converted and rejected promise escaping Result.
This first delivery covers that example in both languages; further executable examples require subsequent queue lines rather than an abstract framework.
Reuse scripts/markdown.py's existing fence handling, already shared by parity and width (docs/01), rather than introduce a second Markdown parser.

**Definition decision.** The author authorized early definition against prerequisite contracts on 2026-10-18.
`after ch03-query-catch` remains an implementation gate; the corrected examples' contract is sufficient to define this check now.
Runtime: Node.js 26.12.0, already installed locally, with its native TypeScript type stripping and `node:assert/strict`; no npm packages or TypeScript compiler enter this delivery.
Run `python3 scripts/check_examples.py` from `make verify`; that Python runner extracts the blocks to a temporary `.mts` file, runs `node`, maps failures back to Markdown, and cleans its temporary files on both success and failure.
The command fails with a prerequisite diagnostic if Node is absent or below 26.12.0; the existing verify CI job installs 26.12.0 explicitly through `actions/setup-node@v4`.
README.md and README.pt.md name this prerequisite; no changes to release or publishing behavior.
Select exactly one TypeScript block defining each needed function or driver class per edition, using the identifiers fixed below; a missing or duplicate definition is an extraction failure.
Reuse a selected block only once when it contains several definitions.
The four required blocks hold Result/ok/err, the illustrative driver failure, the synchronous boundary and the asynchronous boundary; extraction follows the existing Markdown parser, never translated prose headings or numerical block positions.
Use the declaration names fixed in `ch03-query-catch`: English `DriverFailure`, `query`, `queryAsync`; Portuguese `FalhaDoDriver`, `consultar`, `consultarAsync`; support `Result`, `ok`, `err` remains unchanged.
A small explicit per-edition name map connects the same test cases to those symbols; no transpilation or duplicated wrapper body.
This executes runtime behavior only, not compile-time exhaustiveness, as Node's documentation states: <https://nodejs.org/api/typescript.html>.

**Done when.**

* [ ] Success and each failure above are demonstrated against extracted code in both editions; a mutation in each edition independently fails with the correct file and line.
* [ ] The runtime and installation instructions are exact and reproducible; the check runs locally and in the existing verify CI job.
* [ ] `make verify` is green after the last edit and `make book` still builds both editions; added check runtime is recorded.
* [ ] Owning documents and both READMEs describe the actual coverage, with no claim that all examples are executable.
* [ ] Delivery review passes and only this delivery is staged, archived and offered with a commit message.
