# clinic-orchestrator-tests

**Objective.** Every client orchestrator of the guided project is a set of plain functions that receive their repositories and return the new state, each tested in Vitest with fake repositories, built by the clinic's own `/propose` and `/apply` and recorded, so chapter 16 can show an orchestrator's test and the moment injection pays: a second implementation of the repository, the fake.

This is the first of two deliveries split from `testing-and-agents` (chapter 16), whose first `/apply` named the untested client orchestrators as a gap; the author chose to close it. `testing-and-agents` goes back to `[ ]` and is proposed again after this one; its page and its drafts (`book/*/16-testing-and-agents.md`, marked `status: draft`) stay in the working tree as its base.

**Behaviour.**

* In the clinic, each of the eight hooks (`useBooking.ts`, `useCancel.ts`, `useRemembered.ts`, `useClinic.ts`, `useHealth.ts`, `useProfessionals.ts`, `useOwner.ts`, `useWeeklyHours.ts`) keeps only React: it holds the state, publishes the in-flight state, and publishes what an orchestration function returns. Every call to a repository or a use case, in its order, and every new state are in those functions.
* An orchestration function receives its repositories as a parameter, the real ones by default, and `now` where a use case needs the clock; the hook reads `new Date()` and passes it, so no orchestration function reads the clock.
* Each orchestration function has Vitest tests in Node that pass fake repositories and assert which repository was called, in what order, with what, and the state returned, on success and on each refusal and failure; no module mock (`vi.mock`), no new dependency.
* The app behaves as before: every Vitest and Playwright test that existed passes without changing what it asserts, `npm run verify` is green, and the author checks by hand on `npm run dev` that a client books and cancels (from the list and with the code) and the owner signs in, adds a professional and sets hours.
* The clinic's documents say it: docs/04's Tests table gains an Orchestrator row, docs/01 says where the orchestration functions live and that client orchestrators receive their repositories, and the clinic's queue has the line, done.
* Server routes do not change: a route already receives the driver, and its tests already pass the in-memory SQLite.

**Contract.**

*Before the run.* The clinic is on `main`, clean, at `c54d011` (`book-v1/closing-a-milestone`), with focus-kit `e7607c5` as installed; the kit is not updated. The author has committed this book's pending `docs/03` terms and chapter 14 fix, or leaves them unstaged: this delivery's `/apply` stages only its own paths.

*The run.* The recorded clinic run of `clinic-milestone-1` (the first occurrence): its five steps, common flags, `/apply` allowlist and exits, unchanged. The first `/propose` is:

```
claude -p "/propose orchestrator-tests" <common flags>
```

followed, in the same session with `--continue`, by this brief, word for word:

```
Every client orchestrator, each use<Feature>.ts hook, gets unit tests. Move what each event does out of the hook: the calls to repositories and use cases, in their order, and the new state go into plain functions that receive their repositories as a parameter, the real ones by default, and `now` where a use case needs the clock, and return the new state. The hook only holds the state, publishes the in-flight state and publishes what the function returns. The tests pass fake repositories, in Vitest in Node, with no module mock and no new dependency. Server routes do not change. The app behaves exactly as before. Add the line as the first of milestone 2.
```

Every later round of questions is answered `Your call. Say what you chose and why.` The page review and the staged review are the author's, word for word, as in `clinic-milestone-1`. If the clinic's `/propose` splits the line, every part lands before the next chapter tag, each with the five steps. The author commits each clinic delivery with the kit's message and no tag, and pushes; chapter 16 tags.

*The record,* `work/done/clinic-orchestrator-tests-run/`: the format of `clinic-milestone-1-run/` (README with host, model, first and last commit, flags, allowlist, then per delivery the commands, the answers, the author's requests or "none", the denied calls, what diverged, the commit; `<slug>/turn-N.txt`; `verify.txt` on the clinic's last commit), with the brief above in the README.

*This book's documents, in the same delivery.*

* docs/05 §5, Guided project, gains "A recorded clinic run": the five steps, the common flags, the `/apply` allowlist, the exits and the record's format, moved from `clinic-milestone-1`'s page, which stays as it is; this delivery is the second occurrence.
* docs/06: `clinic-orchestrator-tests` `[>]` (this /propose), `[x]` by /apply; `testing-and-agents` `[ ]`.
* docs/03: no new term (orchestrator, repository, unit test exist).

*Numbers.* None enters the book here; chapter 16 decides.

**Out of scope.**

* Any chapter text, chapter 15's sentence included: `testing-and-agents`.
* A chapter tag on the clinic: chapter 16 tags.
* Server routes and repositories: they already get their fake, the in-memory SQLite.
* A React test renderer, jsdom or Testing Library: the functions run in Node.
* Module mocks: the fake is passed, the point of the injection.
* The rest of the clinic's milestone 2: not needed by chapter 16.
* Updating focus-kit in the clinic: the runs cite `e7607c5`.

**Done when.**

* [x] The clinic was clean at `c54d011` before the first run.
* [x] The clinic delivery (or each part of a split) ran the five steps, each turn recorded; nothing in the clinic edited by hand.
* [x] The eight hooks hold only React; each orchestration function has its Vitest tests with fake repositories; no new dependency in `package.json`.
* [x] The existing tests pass without changing what they assert; `npm run verify` green on the clinic's last commit, saved as `verify.txt`.
* [x] The author's manual check recorded in the README.
* [x] Each clinic delivery committed by the author, no tag; pushed.
* [x] No note of the host left outside the clinic's repository.
* [x] `work/done/clinic-orchestrator-tests-run/` as the Contract says.
* [x] docs/05 §5 has "A recorded clinic run"; docs/06 lines as the Contract says.
* [x] `make verify` green in this book, the disclosure scan included.
* [x] Page in `work/done/`, only this delivery's paths staged, commit message suggested.

## What happened

* The precondition held: the clinic was on `main`, clean, at `c54d011`, with focus-kit `e7607c5`.
* One clinic delivery, `orchestrator-tests`, six turns: `/propose` (its first question round, the brief, the rule), one page review, `/apply`, one staged review. `/propose` did not split the line.
* The clinic's `/propose` first proposed jsdom, Testing Library and `vi.mock`; the brief ruled them out, and it chose on its own that an event returns an update of the current state, so a keystroke typed during a request survives, and that a booking event may return the next event, so the in-between "Loading" stays.
* Page review: four corrections (a manual check in Done when, the injection rule in docs/01, the existing Vitest tests unchanged, a line wrap in docs/06). Staged review: finish moving the page after a denied `git mv`, drop the `Co-Authored-By` trailer, record the manual check.
* Two calls denied, both in `/apply`; none retried from outside the clinic's session.
* The agent saved a note about the trailer in the host's auto-memory for the clinic; it was deleted after the commit.
* The author's manual check on `npm run dev` held: owner signs in, adds a professional and sets hours; a client books and cancels from the list and with the code.
* `npm run verify` green on `e6653b5`: 323 Vitest (85 new, in eight `*Events.test.ts` files), 144 Playwright unchanged, build. No `package.json`, view, route or `*.e2e.ts` in the diff since `c54d011`.
* The functions are named `<name>Events.ts` in the clinic, the name its agent chose; chapter 16 decides how to present them.
* docs/05 §5 has "A recorded clinic run"; the record's step 1 notes that a page may give a brief. The turn files were derived with the one-off script of `clinic-milestone-1`, outside the repository.
* No ADR, no new term.
