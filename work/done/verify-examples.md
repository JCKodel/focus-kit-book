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

* [x] Success and each failure above are demonstrated against extracted code in both editions; a mutation in each edition independently fails with the correct file and line.
* [x] The runtime and installation instructions are exact and reproducible; the check runs locally and in the existing verify CI job.
* [x] `make verify` is green after the last edit and `make book` still builds both editions; added check runtime is recorded.
* [x] Owning documents and both READMEs describe the actual coverage, with no claim that all examples are executable.
* [x] Delivery review passes and only this delivery is staged, archived and offered with a commit message.

**What happened.** `scripts/check_examples.py` reads both editions of chapter 3 with markdown.py's `line_kinds`, takes the one TypeScript block that declares each of `ok`, `err`, `DriverFailure`, `query` and `queryAsync` (`FalhaDoDriver`, `consultar`, `consultarAsync` in Portuguese), writes them in chapter order to a temporary `.mts` module outside the repository, and runs with `node` a second module that imports them under the English names (that import is the edition's map) and runs 11 cases: a value in `ok`; the driver's failure as `DatabaseFailed` with its message; a `TypeError`, another `Error`, a thrown string and a control object passing as the same value; an awaited value in `ok`; the driver's rejection, awaited inside the `try`, as `err`; another rejection and a rejected control object rejecting with the same reason; no rejection escaping unhandled.
A failed case points at the line that declares the function under test, in the edition that failed; a run that records other than 11 cases is a finding.
`make verify` runs it after width; the verify job installs Node 26.12.0 with `actions/setup-node@v4`; docs/01 (scripts, Scripts row, verify row, errors), docs/04 Tests, docs/05 Verify and both READMEs name the coverage and the runtime.

**Divergences.** docs/05 §5's proof of a screen for a toolchain delivery asks for screenshots of the site; this check has no screen (States: inapplicable) and changes nothing the site renders, so the proof is the terminal runs below.
A syntax error is reported where Node stops parsing: an extra `{` at en:222 is reported at en:252, the last line of the last block, still inside the chapter.

**Decisions.** The case "a promise passed to `query` comes back as `ok`" from ch03-query-catch's proof is left out: it creates an unhandled rejection on purpose, which the last case counts as a failure. The cases live in the script as one TypeScript text, the same for both editions. The protocol lines carry a `check-examples` prefix and fold whitespace, so a `console.log` in a chapter or a tab in a detail cannot hide a failure (review points 1 and 2).

**Proof.** Node v26.12.0, `python3 scripts/check_examples.py`: exit 0 on both editions in 0.2 s (the added check runtime). Mutations ran on copies of the chapters outside the repository, `python3 scripts/check_examples.py <copy>`, each exit 1:
* every thrown value translated: en:222 and pt:223 (`query`, `consultar`), four findings each, the other edition untouched;
* the `await` removed: en:242 and pt:243 (`queryAsync`, `consultarAsync`), five findings each, three escaped rejections named;
* the `DriverFailure` block removed: en:1, no block declares it; `FalhaDoDriver` declared twice: pt:215 and pt:219;
* a syntax error: pt:229, en:252, with Node's `SyntaxError`; a fence never closed: its opening line;
* no `node` on the PATH, and a `node` printing v26.11.9: `Makefile:1: examples:` with the required version;
* the cases replaced by none, or by a throw: "0 cases ran; 11 were expected", "the examples did not run: TypeError".
No temporary directory was left behind, and `git status` showed no chapter file changed by the runs. `make verify` green after the last edit; `make book` runs once at the end of the batch, by its driver.

**Delivery review.** A read-only agent on Opus read the diff, the new script and the proof log against this page and docs/04. Points: (1) a `FAIL` line with a tab in its detail was dropped while still counted, a false pass: whitespace folded and every `FAIL` reported. (2) The protocol shared stdout with the chapter: prefixed. (3) A TypeScript fence never closed gave a misleading finding: now its own finding at the opening line. (4) An `export` in a chapter block would collide with the appended export: noted in the docstring, since no block exports. (5) The install lines did not pin 26.12.0: the READMEs link `nodejs.org/dist/v26.12.0/` and say `brew install node` gives the current release. (6) The proof lacked the missing and old Node runs: added. (7) The runtime was not recorded: above. (8) The syntax-error line is Node's: recorded under Divergences. Verify and the proof ran again after the fixes.

```commit
docs(verify-examples): run chapter 3's boundary examples in verify

- check_examples.py runs ok, err, query and queryAsync from each edition
- Node 26.12.0 type stripping, no package; findings at the chapter line
- make verify and the verify job run it; Node set up in Actions
- docs/01, docs/04, docs/05 and both READMEs name coverage and runtime

work/done/verify-examples.md
```
