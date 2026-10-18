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
* [ ] Execute the printed examples in both editions against every Behaviour input, recording runtime/compiler version, commands and outcomes on this page; the bug and control-object cases fail against the old wrapper and pass against the corrected one.
* [ ] Success, recognized failure and unknown rejection are each checked in the asynchronous variant; no test or log is claimed to make a broad catch selective.

* [ ] Both editions say the same thing, using docs/03's terms and Portuguese example names.
* [ ] The opening states the reader's value and the gain is supported; no filler added or useful explanation cut; every number and quoted artifact has its source (docs/00 and docs/04).
* [ ] `make verify` and `make book` pass; the author receives `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf` for the passage checks (docs/05 §5).
