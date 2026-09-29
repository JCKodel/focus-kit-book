# errors-and-slices

**Objective.** After chapter 14 the reader can organize code by feature in vertical slices and return every exception as a value, tell an exception from a refusal and from an error, and knows that both principles work without the four pieces of chapter 15.

**Behaviour.**

* The reader can say what a vertical slice is (one folder holds everything a feature needs, no folder per technology or layer, a sub-feature is a subfolder) and what it gains: a change to a feature touches one folder, and removing the feature removes the folder.
* The reader can read the clinic's `src/features/` at the tag and say why `health` has no `rules.ts` or `repository.server.ts` (a file appears when it pays its way) and why `lib/` holds only what two features already share (chapter 13's rule of the second occurrence).
* The reader can sort a failure into one of three: an exception (an expected failure at I/O, returned as a value), a refusal (a rule saying no, returned as a value, no I/O involved) or an error (a bug, thrown, never caught).
* The reader can write the `Result` type, return an exception from the one place that catches it, return a refusal from a pure rule, and handle every case so that a forgotten one fails to compile.
* The reader can follow one failure, `SlotTaken`, from the database index to the message on the screen without a `throw` on the way.
* The reader can list where the clinic catches and say why each one is I/O, the routes' reading of the request body included.

**Contract.**

Chapter 14, `book/en/14-errors-and-slices.md` and `book/pt/14-errors-and-slices.md`:

* Title: "Exceptions as values and vertical slices" / "Exceções como valores e fatias verticais". Opens Part III; like chapter 5, it carries no part heading.
* Voice: instruction to the reader as "you" (docs/04 §Voice).
* Sections, in order (headings may be reworded; both editions keep the same structure):
  1. Opening, at most three sentences: the Objective.
  2. Two principles that stand alone. They need none of the four pieces: any structure the stack favors can put each feature in a folder and return exceptions as values; this is the kit's second answer ([chapter 6, the two choices](06-the-documents.md#the-two-choices)), and chapter 15 adds the pieces. The clinic took FOCUS whole (chapter 7), so its code at the tag shows both. Short.
  3. Vertical slices. The file lists of `src/features/appointments/` and `src/features/health/` at the tag (from `git ls-tree`), with one sentence on what each file is, grouped, not one line per file. The gains of the first Behaviour line. `health` as the slice without a rule; `lib/` and the comment "First use: ...; second use: ..." that its files carry, pointing to chapter 13. The sub-feature stated with docs/03's example `authentication/change-password/`; the clinic has none, said in one clause. One sentence that the slice also bounds what an agent reads, pointing to chapter 16.
  4. Exception, refusal, error. Dart's split (`Exception` and `Error` in `dart:core`) in two sentences; the refusal as the third kind, a rule's answer; the error never caught, it reaches the developer's screen and analytics. The field's name for the principle is said in chapter 6, pointed to, not repeated; one sentence that the kit and the clinic still use its word, `error`, in the `Result`'s field and in their documents, for what this book calls an exception or a refusal. One sentence that the clinic's own docs/03 already calls its rule outcomes refusals.
  5. Exceptions as values in the clinic. Excerpts, in this order, each with its path and a link to the file at the tag: `src/lib/result.ts`, whole; `query` from `src/server/database.server.ts`, with its comment (the one `try`/`catch` a repository's SQL runs inside); `insertAppointment` from `src/features/appointments/repository.server.ts`, with its comment and the `InsertError` type (an exception becomes the refusal `SlotTaken` when the unique index fails, `DatabaseFailed` otherwise); `checkClientPhone` from `src/features/appointments/rules.ts`, with its comment (a refusal from a pure rule); `refusalStatus` from `src/features/appointments/route.server.ts` (a `Record` over `BookingRefusal`: a refusal with no status fails to compile). Then, in one or two sentences, where the clinic catches: `openDatabase`, `query` and `transaction` in `database.server.ts`, the migration runner, `request.ts` on the client, `remembered.ts` for the phone's storage, and each route when it reads the request body, which becomes `BadRequest` on the spot: all I/O. Last, the one `throw` in its source outside test files, in `memoryDatabase` of `src/server/testDatabase.server.ts`: a migration that fails in a test is a bug, an error, so it is thrown.
  6. One failure, end to end. `SlotTaken` in five steps, in prose, after the clinic's docs/01 §How errors travel: the repository returns it, the route answers 409 with `{ "error": { "code": "SlotTaken" } }`, `request.ts` reads the 409 as the refusal, the hook publishes a state that holds it, the view shows "This time is no longer free. Pick another." from `strings.ts`. No excerpt beyond the message; the steps name their files.
  7. Key points, at most five, one of them: an exception exists only at I/O, a refusal only in a rule, and neither is thrown.
  8. Exercises (below).
* Code: TypeScript, byte for byte from the clinic at the tag `book-v1/closing-a-milestone` (commit `c54d011`), identical in both editions, comments included (docs/04: code stays as it ran). The guided project does not change: no run, no new tag.
* Numbers, and only these: 409 (the status), the counts of files the two listings show.
* docs/03 terms: introduced here: vertical slice, exception, refusal (new, added by this /propose), error, Result, exceptions as values. Used: guided project, chapter tag, repository, use case (said in a clause each, taught in chapter 15), delivery.
* Sources (`[^key]`, same keys in both editions):
  * `[^dart-core]`: Dart, `Exception` and `Error` classes of `dart:core`, <https://api.dart.dev/stable/dart-core/Exception-class.html> and <https://api.dart.dev/stable/dart-core/Error-class.html>.
  * `[^go-errors]`: Rob Pike, "Errors are values", The Go Blog, 2015, <https://go.dev/blog/errors-are-values>.
  * `[^rust-result]`: The Rust Programming Language, chapter 9.2, "Recoverable Errors with Result", <https://doc.rust-lang.org/book/ch09-02-recoverable-errors-with-result.html>.
  * `[^vertical-slice]`: Jimmy Bogard, "Vertical Slice Architecture", 2018, <https://www.jimmybogard.com/vertical-slice-architecture/>.
  * `[^book-adr-0016]` (as chapter 6): this book's ADR-0016, where the split and the name are decided.
  * The clinic's files are linked in the text at the tag, with no note (docs/04).
* Exercises, on the clinic, by conversation with the agent, never by hand:
  * 14.1 Ask the agent to list every `try`, `catch` and `throw` in your clinic outside tests, and for each to say what I/O it guards and which value it returns; any that guards no I/O is a candidate for your queue, not a fix now.
  * 14.2 Ask the agent to follow `CancellationTooLate` from the rule to the screen, naming each file; then say which files would have to change if the rule threw it instead.
  * 14.3 Milestone 3 brings `absences`. Ask the agent where its files would go, a folder of its own or a subfolder of `weeklyHours`, and which existing files it would touch; decide, and say why. Nothing is built.
* Documents: docs/03 gains refusal, and exception, error and Result are adjusted to it (this /propose). No ADR amendment: ADR-0016 already says exceptions exist only at I/O and use cases return values; the refusal names that value. docs/06: `errors-and-slices` `[>]` (this /propose), `[x]` by /apply. docs/00 §Contents already names chapter 14. The page's What happened records the exercise answers for the `exercise-answers` appendix.

**Out of scope.**

* Renaming the clinic's `error` field and its "errors as values" wording: the chapter names it once; changing code chapters 11 and 12 quote costs more than it teaches.
* A queue line in the clinic for the routes' body-read `catch`: it is I/O, said in a sentence.
* A sub-feature in the clinic: it has none, and the chapter shows no invented one.
* View, orchestrator, use case and repository as pieces, the flow in one direction and when the pieces pay their way: chapter 15.
* Testing each piece, and how the architecture helps an agent beyond one sentence: chapter 16.
* Ninjobs: the chapter needs no case, and FOCUS is never told as a warning.
* Examples in other languages: Dart, Go and Rust appear only as sources of the idea (ADR-0008).
* The kit's own wording: changed in the kit's repository, if ever, not here.

**Done when.**

* [x] Both editions written, same file name and heading structure, opening with the Objective in at most three sentences; no draft marker.
* [x] No filler and nothing useful cut; every number cites its source.
* [x] Every code excerpt matches `git show c54d011:<path>` byte for byte, checked by script, in both editions; the file listings match `git ls-tree` at the tag.
* [x] The chapter's first TypeScript blocks render: screenshots of the site in light and dark and of the PDF, in both editions (docs/05 §5).
* [x] `make verify` green, the link check and the disclosure scan included (the tag is already pushed).
* [x] `make book` builds; both PDF paths given to the author.
* [x] docs/06 line `[x]`, page in `work/done/`, staged, commit message suggested.

**What happened.**

* Written as the Contract says, in both editions, with no draft marker. The Portuguese edition says "funcionalidade" for feature, as chapter 6 does. The Portuguese heading "Uma falha, de ponta a ponta" became "Uma falha, do começo ao fim": the prose check flags "de ponta" as inflated.
* Diverged, by decision of the author during /apply: the page said the clinic has one `throw` outside test files, in `memoryDatabase`. At the tag there are two in helpers that only tests run: `memoryDatabase` in `src/server/testDatabase.server.ts` (Vitest) and `box` in `src/features/appointments/e2e.server.ts` (Playwright, "not visible"); a third, in `WeeklyHoursView.e2e.ts`, is in a test file. The chapter says the app never throws, names both helpers and shows `memoryDatabase`; both are errors, a failed test.
* Diverged from the Contract's list of catches: `transaction` has no `catch` of its own; it runs inside `query` and rolls back. The chapter says "`openDatabase` and `query` (`transaction` runs inside `query`)".
* `lib/`'s comment "First use: ...; second use: ..." is in `email.ts`, `id.ts`, `name.ts` and `request.ts`; `result.ts`, used by every feature, has none. The chapter names the four.
* `InsertError` and `insertAppointment` are not adjacent in the file, so they are two blocks. Numbers in the prose: 409, 22 and 6 (the two listings); the other counts (three views, five steps) are read off what the chapter shows.
* The byte check: a script outside the repository (not a check of `make verify`: it names no error that happened) took every `ts` block of both editions and found it as a substring of `git show c54d011:<path>`, and every `text` block equal to `git ls-tree -r --name-only c54d011 src/features/<name>`; the blocks of the two editions are identical. All 9 blocks passed in each edition.
* Proof: `work/done/errors-and-slices-site-<en|pt>-<light|dark>.png` (1280 pixels, the first TypeScript blocks of the section on the clinic) and `errors-and-slices-pdf-<en|pt>.png` (English pages 124 and 125, Portuguese 129 and 130). The site shows the code plain, as every earlier block, with no syntax colors; the PDF colors it. Both expand the clinic's tabs to four spaces, and the PDF wraps the long SQL lines at the margin. What the proof found: notes 3 and 4 rendered side by side as one superscript "34" after "Rust"; each language now carries its own note, after "Go" and after "Rust".
* The Dart URLs of the Contract, under `/stable/`, pass the link check; chapter 6 keeps its own note and URLs.
* Exercise answers, for the `exercise-answers` appendix:
  * 14.1: catches at the tag, outside tests: `openDatabase` (the folder and the SQLite file: `DatabaseOpenFailed`), `query` (SQL: `DatabaseFailed`; `transaction` runs inside it), `migrate` twice (the folder and `schema_migration`, then each file: `MigrationFailed`), `request` (the network and the body: `ServerUnreachable`), `readAll` and `keep` in `remembered.ts` (the phone's storage: none remembered, `StorageFailed`), and six `c.req.json().catch` in the routes (two in appointments, two in professionals, one in signIn, one in weeklyHours: `BadRequest`). Throws: `memoryDatabase` and `box`, test helpers. None guards no I/O, so nothing goes to the queue.
  * 14.2: `cancel` in `rules.ts` returns `CancellationTooLate`; the cancel route in `route.server.ts` answers 409 with it; `postCancellation` in `api.ts` names 409 as it and `request.ts` returns it; `useCancel.ts` keeps it as the form's message and `useRemembered.ts` puts the line in the state `tooLate`; `CancelView.tsx` and `RememberedView.tsx` show `cancelErrorStrings` from `strings.ts`. If the rule threw it: `rules.ts`, `route.server.ts` (a `try`/`catch` to keep the 409), `useRemembered.ts` (it calls `cancel` to show whether a line is still cancellable, and would throw while rendering), and the tests `rules.test.ts` and `route.server.test.ts`; `api.ts`, `request.ts` and the views stay as long as the route still answers 409.
  * 14.3: a folder of its own, `features/absences/`: it has its own table, route, rule and screen, and `weeklyHours` does not change when an absence is recorded. It touches `appointments/rules.ts` (`freeSlots` takes the absences), `appointments/route.server.ts` (`slotsOf` reads them), a new migration in `src/server/migrations/`, and the owner's screen that links to it. A subfolder of `weeklyHours` would fit only if absences were edited on that screen; the decision is the reader's.
* Documents: docs/03 gained refusal and adjusted exception, error and Result in /propose, and this delivery kept them; docs/06 line `[x]`. No ADR.
