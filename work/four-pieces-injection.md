# four-pieces-injection

**Objective.** After chapter 15 the reader can place every file of a clinic slice in the four pieces, the client orchestrator's two files included, follow a booking through them at the clinic's current code, and say where FOCUS passes a dependency in and why only there: the orchestrator receives its repositories, or the driver they use, because a test passes a second implementation, a fake.

This is the first of two deliveries split from `testing-and-agents` (chapter 16), after `clinic-orchestrator-tests` changed the clinic: chapter 15 says its client orchestrator "injects nothing" and that injecting would be ceremony, and the clinic's code now injects. The author chose to rewrite chapter 15 at the new code rather than tell the change in chapter 16. `testing-and-agents` stays `[ ]` and is proposed again after this one; its page and drafts stay in the working tree.

**Behaviour.**

* The reader can say that the clinic's client orchestrator is two files: `<name>Events.ts`, what each event does as plain functions (the calls to repositories and use cases, in order, and the new state), and the hook `use<Feature>.ts`, only the React part (it holds the state, publishes the in-flight state and the answer, reads the clock, and drops a stale answer).
* The reader can follow a booking from the tap on "Book" to the booking code at the clinic's current code, naming at each step the piece, the file and what it hands on; steps 3 to 6 are unchanged.
* The reader can state the rule and apply it: a piece receives a dependency only where there is a second implementation to pass, and in FOCUS that is only the orchestrator. The route receives the driver, and its test passes an in-memory SQLite; the client's event functions receive their repositories, the real ones by default, and their tests pass fakes. A use case receives no repository (ADR-0016), and a view or a repository has one implementation, so a parameter there would be ceremony (KISS).
* The reader can say who reads the clock: the orchestrator's React part or the route reads `new Date()` and passes `now`; no event function and no use case reads it.

**Contract.**

Chapter 15, `book/en/15-four-pieces.md` and `book/pt/15-four-pieces.md`, rewritten where below says; every other sentence stays.

* Tag: every clinic link and excerpt of chapter 15 moves from `book-v1/closing-a-milestone` (`c54d011`) to `book-v1/four-pieces`, on the clinic's `e6653b5` ("Move each client hook's events into tested plain functions"). The author creates and pushes the tag before `make verify`, since the link check opens every tag URL (docs/05 §5). The opening sentence of section "The four pieces" says, in one clause, that the tag is the code chapter 12 left plus the clinic's first delivery of milestone 2; no more of that delivery's story.
* Section "The four pieces": the table stays (unchanged at `e6653b5`). The slice listing is quoted again from the clinic's docs/01 at the tag, from `rules.ts` to `strings.ts`, now with the `<name>Events.ts` and `<name>Events.test.ts` lines, dedented as before.
* Section "Two sides, one set of rules": "On the client, the orchestrator is the hook `use<Feature>.ts`" becomes the two files of the first Behaviour line. The rest stays.
* Section "One event, one new state", step 2, "The client orchestrator", replaces the old `useBooking.ts` excerpt with, in this order, each linked at the tag:
  * `src/features/appointments/bookingEvents.ts`: from the comment `// Name and phone are checked here to show the message beside the field` to the end of `submit`, whole (`submitStarted`, the comment `` // `state` is the one `submitStarted` accepted. ``, `submit`). Said: `submitStarted` checks name and phone with the use cases and gives the in-flight state; `submit` calls `postAppointment` and `remember` through `repositories` with `now` passed in, and returns either an update to the state or the next event to run (`loadProfessionals`, `loadSlots`).
  * `src/features/appointments/useBooking.ts`: `run`, whole with its comment (`// Any event with a call: ...` to the end of the `useCallback`). Said: the hook sets the in-flight state, reads `new Date()` and passes it, drops an answer that is not the latest, and publishes the update or runs the next event.
  Steps 1 and 3 to 6 keep their text and excerpts, relinked. The way back names `submit`'s update and the hook publishing it in place of "`submit` publishes the step `booked`".
* Section "What the clinic injects", rewritten, same heading:
  * The rule, from ADR-0016 as amended by this delivery (note `[^book-adr-0016]`): the orchestrator is the only piece that receives its dependencies, and it receives them because a test passes a second implementation.
  * The server: `appointmentsRoute(db)` receives the driver and hands it to every repository call; the second implementation is `memoryDatabase` (chapter 14, pointed to). The clinic's docs/01 bullet "Server routes that need the database are functions of it ..." quoted whole, as today.
  * The client: `BookingRepositories` and `bookingRepositories` from `bookingEvents.ts`, whole, and `submit`'s parameter `repositories = bookingRepositories`, already shown in step 2, pointed to. The second implementation is the fake of the event tests, which chapter 16 shows. The clinic's docs/01, section "How the code is organized", quoted from "Its event functions receive their repositories as a parameter" to "no function there reads it."
  * Where nothing is passed, and why: a use case receives no repository (ADR-0016); a view and a repository each have one implementation, so a parameter would exist for ceremony (KISS). One sentence, no excerpt.
  * The last sentence points to chapter 16 for the tests.
* Key points: the fifth becomes "An orchestrator receives its repositories, or the driver they use, because its test passes a second implementation, a fake; no other piece receives a dependency." The first four stay; the third's "each side has its own orchestrator" stays true.
* Exercises 15.1 to 15.3: text unchanged. Their answers are derived again at `e6653b5` and recorded in What happened, replacing `four-pieces`'s for the `exercise-answers` appendix.
* Code: TypeScript, byte for byte from the clinic at `e6653b5`, identical in both editions, outer indentation removed (docs/04 §Writing the book), fence `ts`. Every excerpt kept from `four-pieces` is checked again at `e6653b5`. The docs/01 excerpts: byte for byte in English, translated in Portuguese, which says before them that the original is in English (docs/04 §Evidence).
* Numbers: the statuses the excerpts show (201, 400, 404, 409, 500), as today; no new one.
* docs/03 terms: introduced here: fake (added by this /propose). Changed by this /propose: orchestrator, which now says why only it receives dependencies. Used: those of `four-pieces`, plus unit test only if the text needs it (chapter 16 introduces it).
* Sources: `[^book-adr-0016]` says "amended 2026-09-29" (or the day of the amendment). No new note: the clinic's files and docs/01 are linked in the text at the tag (docs/04).
* Documents:
  * ADR-0016 gains "## Amendment, <date> (four-pieces-injection)": a piece receives a dependency only where there is a second implementation to pass, and in FOCUS that happens only in the orchestrator: the real repository, and the fake a test passes; the server's orchestrator may receive the driver its repositories use, for the same reason. The Decision text is not rewritten.
  * docs/03: fake added and orchestrator changed (this /propose).
  * docs/06: `four-pieces-injection` `[>]` (this /propose), `[x]` by /apply; `testing-and-agents` stays `[ ]`.
  * `work/done/four-pieces.md` is not edited: it records that delivery.

**Out of scope.**

* Chapter 16 and its page: the next delivery, `testing-and-agents`, proposed again.
* Showing a fake or any test here: chapter 16 shows them; this chapter names the fake and points there.
* How the orchestrator tests were built (the recorded run): the author chose not to tell it.
* Any change to the clinic: it is at `e6653b5`, done by `clinic-orchestrator-tests`.
* Chapter 14 and its tag: it quotes `book-v1/closing-a-milestone`, and nothing it shows changed.
* Showing the other seven `<name>Events.ts`: one slice carries the idea; exercise 15.1 takes another.
* Ninjobs, and FOCUS as a warning: not needed.
* Examples in other languages (ADR-0008).

**Done when.**

* [ ] The author created and pushed `book-v1/four-pieces` on `e6653b5`.
* [ ] Both editions rewritten as the Contract says, same heading structure; the opening unchanged unless the new Behaviour needs a word; no draft marker.
* [ ] No sentence left that says the client orchestrator injects nothing, or that injecting would be ceremony; no link to `book-v1/closing-a-milestone` left in chapter 15.
* [ ] No filler and nothing useful cut; every number cites its source.
* [ ] Every code excerpt matches `git show e6653b5:<path>` byte for byte once its outer indentation is put back, checked by script, in both editions; the English docs/01 excerpts match too.
* [ ] ADR-0016 amended as the Contract says.
* [ ] Exercise answers derived again at `e6653b5`, recorded in What happened.
* [ ] `make verify` green, the link check and the disclosure scan included.
* [ ] `make book` builds; both PDF paths given to the author.
* [ ] docs/06 line `[x]`, page in `work/done/`, only this delivery's paths staged, commit message suggested.
