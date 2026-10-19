# ch03-query-catch

**Objective.** A reader keeps only recognized driver failures inside `Result` and can use the boundary correctly for synchronous and asynchronous calls.

**Behaviour.**
* A synchronous call returning a loan yields the same value in `ok`; a recognized driver failure yields `DatabaseFailed` with its message.
* A `TypeError`, an ordinary unrecognized `Error`, a thrown primitive, and a framework control object escape unchanged, by identity where applicable, instead of becoming `DatabaseFailed`.
* An asynchronous call resolves to `ok` with its completed value; a recognized rejected driver failure becomes `err` because the call is awaited inside `try`; an unrecognized rejection still rejects with the original reason.
* A reader passing a promise to the synchronous wrapper sees why it does not handle a later rejection and chooses the asynchronous wrapper.
* The last-copy paragraph keeps the distinction between the particular unique constraint's `AlreadyLent` refusal and other recognized database failures; tests or logging are not offered as a repair for swallowing a bug.

**Contract.** `book/en/03-simplicity-and-results.md` and `book/pt/03-simplicity-and-results.md`, chiefly Where the catch lives, its opening and key points where needed.
Keep `Result`, `ok`, `err`, `DatabaseFailed` and their existing Portuguese names (docs/03).
Use a small explicitly illustrative driver exception class in the lending-library example: recognize that class, rethrow everything else; an actual adapter uses its driver's documented failure discriminator rather than `instanceof Error` or message matching.
Fix the printed declaration names as `DriverFailure`, `query`, `queryAsync` in English and `FalhaDoDriver`, `consultar`, `consultarAsync` in Portuguese; the driver failure extends `Error` with its inherited message constructor.
Use erasable TypeScript syntax and four standalone blocks: Result/ok/err, the illustrative driver failure class, the synchronous wrapper and the asynchronous wrapper.
These exact symbols and block boundaries let `verify-examples` execute the printed code without a copied implementation.
Keep the synchronous signature and add an asynchronous variant returning `Promise<Result<T, DatabaseFailed>>`, with `await` inside `try`.
This is a correction of the audit's observed failure in docs/06, not a production database adapter.
Primary reference: ECMAScript Await and TryStatement semantics, <https://tc39.es/ecma262/multipage/control-abstraction-objects.html#await> and <https://tc39.es/ecma262/multipage/ecmascript-language-statements-and-declarations.html#sec-try-statement>.
The examples remain authored for the chapter (docs/04); no new domain concept or private case.

**States.** Inapplicable: chapter prose, no new screen.

**Visual reference.** Inapplicable: the existing book layout.

**Out of scope.** Driver selection, migrations and product code: there is no library product in this repository; persistent extraction and `make verify` integration belong to `verify-examples`; exhaustive handling belongs to `ch03-exhaustive-switch`.

**Done when.**
* [x] Execute the printed examples in both editions against every Behaviour input, recording runtime/compiler version, commands and outcomes on this page; the bug and control-object cases fail against the old wrapper and pass against the corrected one.
* [x] Success, recognized failure and unknown rejection are each checked in the asynchronous variant; no test or log is claimed to make a broad catch selective.

* [x] Both editions say the same thing, using docs/03's terms and Portuguese example names.
* [x] The opening states the reader's value and the gain is supported; no filler added or useful explanation cut; every number and quoted artifact has its source (docs/00 and docs/04).
* [x] `make verify` and `make book` pass; the author receives `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf` for the passage checks (docs/05 §5).

**What happened.** Both editions of chapter 3's "Where the catch lives" now print four standalone blocks: the existing `Result`/`ok`/`err`, an illustrative `class DriverFailure extends Error {}` (`FalhaDoDriver`), `query` (`consultar`), which returns `err` only for `instanceof DriverFailure` and rethrows everything else, and `queryAsync` (`consultarAsync`), which returns `Promise<Result<T, DatabaseFailed>>` with `ok(await run())` inside the `try`.
The text says a real adapter tests its driver's documented sign, not `instanceof Error` or the message; explains why a promise passed to `query` comes back as `ok` and its rejection escapes; cites the ECMAScript Await and try sections in a new note `[^ecma-await]`; keeps the last-copy paragraph's split between the unique index's `AlreadyLent` and any other failure staying `DatabaseFailed`; and drops the test and log sentence, offering nothing in its place.
The opening and the exception key point name the asynchronous case; docs/03's running example row adds `FalhaDoDriver`, `consultar`, `consultarAsync` (shared patch).

**Divergences.** None. No Case A or Case B passage was used or changed.

**Decisions.** The two catch bodies stay printed in full rather than sharing a helper: the second block exists to show `await` inside `try`. The `queryAsync` signature breaks across three lines to fit the PDF. "Running out of memory" left the list of throws that pass, since in JavaScript it aborts the process and reaches no catch.

**Proof.** Node v26.12.0 (native type stripping) and TypeScript 5.9.3 (`npx -p typescript@5.9.3 tsc --strict --erasableSyntaxOnly --noEmit`, exit 0) on the blocks extracted from each edition, concatenated with a harness written for this proof (`python3 build.py <en|pt> <new|old> > <ed>-<ver>.ts; node <ed>-<ver>.ts`).
New wrapper, both editions, 11 of 11 pass: sync loan in `ok`; `DriverFailure` becomes `DatabaseFailed` with its message; `TypeError`, plain `Error` and a control object escape by identity, a thrown string escapes unchanged; a promise passed to `query` returns `ok` holding that promise; async success resolves `ok` with the value; a rejected `DriverFailure` becomes `err`; an unknown rejection and a control object reject with the same reason.
Old wrapper (HEAD), both editions: the `TypeError`, plain `Error`, string and control object cases fail (all became `DatabaseFailed`); it had no asynchronous variant. No test or log is claimed to make a broad catch selective.
`make verify` green after the last edit; `make book` is run once by the batch driver for `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`, for the author's passage checks.

**Delivery review.** A read-only agent on Opus read `git diff HEAD` of both chapter files and the docs/03 patch against this page and docs/04. Points: (1) the proof was not yet on the page: recorded above. (2) Running out of memory reaches no catch in JavaScript: dropped from the list. (3) "the `try` is over before the promise settles" is not always true (an already rejected promise): replaced by "a `catch` sees a throw, and a rejection is not one until something awaits the promise". (4) "se resolver" is not "settle": gone with (3). (5) "todo outro throw" became "qualquer outro throw". (6) The opening sentence was too long and "and only those" ambiguous: split in two in both editions. Verify and the harness ran again after the fixes.

```commit
docs(ch03-query-catch): catch only the driver's failures, await in try

- query returns err only for the illustrative DriverFailure, rethrows rest
- queryAsync awaits inside the try; a promise passed to query escapes
- The test and log repair for a broad catch is gone; source note on await
- docs/03 adds FalhaDoDriver, consultar and consultarAsync

work/done/ch03-query-catch.md
```
