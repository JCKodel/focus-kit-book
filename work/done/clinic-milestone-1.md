# clinic-milestone-1

**Objective.** The guided project's milestone 1 is closed: the five lines after `skeleton` are built with `/propose` and `/apply`, one delivery at a time, each page and each staged change reviewed by the author and committed by them, so chapter 12 has a real, whole milestone to review.

This is the first of two deliveries split from `closing-a-milestone` (chapter 12), which needs a closed milestone of the clinic to review; the second stays `[ ]` in docs/06 and is proposed after this one is done.

**Behaviour.**

* In the clinic's docs/06, every line of "Milestone 1: a client books and cancels" is `[x]`, each with its page in `work/done/`.
* Each of the five deliveries is one commit in the clinic, made by the author with the message the agent suggested (or the author's edit of it), with no tag.
* The milestone's paragraph holds on the running app, checked by the author with `npm run dev`: the owner registers professionals and their weekly hours; a client books a free slot; a client cancels up to 24 hours before, and is told why not after that.
* `npm run verify` is green on the clinic's last commit.
* Anyone can repeat a delivery from the record: the commands, the answers and the author's requests are written down word for word.

**Contract.**

*Before the first run.* The author has committed the clinic's staged `skeleton` delivery, tagged it `book-v1/apply` and pushed both (chapter 11's pending item). The clinic is on `main`, clean, with focus-kit `e7607c5` as installed; the kit is not updated in this delivery.

*Order.* The clinic's queue order: `clinic-setup`, `professionals`, `weekly-hours`, `book-appointment`, `cancel-appointment`. One delivery is committed before the next starts.

*Each delivery, five steps, inside `../focus-kit-clinic`* (the mechanism of chapters 10 and 11; `work/done/brainstorm-run/` is the first occurrence):

1. `/propose`, headless: `claude -p "/propose <slug>"` with the common flags below. Every round of questions is answered with `--continue` and the brief's rule, word for word: `Your call. Say what you chose and why.`
2. Page review. /apply stops and shows the author the page. It may list the holes it sees; the author decides which to send. Each request goes to the same session with `--continue`, word for word as the author gives it. "No correction" is a valid review and is recorded as such. The page is never edited by hand.
3. `/apply`, headless, in a fresh session: `claude -p "/apply <slug>"` with the common flags, `--allowedTools "Bash(npm *)" "Bash(npx *)" "Bash(node *)" "Bash(mkdir *)" "Bash(cp *)" "Bash(git add *)" "Bash(git status *)" "Bash(git diff *)"` and `--disallowedTools "Bash(npm run dev*)"`, the list of chapter 11's run.
4. Staged review. /apply stops and shows the author the staged change and the page's What happened; the requests go to the `/apply` session with `--continue`, as in step 2. Nothing in the clinic is edited by hand.
5. The author commits. No tag. The author pushes whenever they choose; everything is pushed before chapter 12 is proposed.

Common flags: `--model claude-opus-5-5 --setting-sources project --strict-mcp-config --permission-mode acceptEdits --permission-prompts none --output-format stream-json --verbose`.

*When something does not go as planned.*

* A denied call is recorded, never retried by another route.
* A run that cannot finish, or a verify that stays red, stops the delivery; /apply asks the author before any second run.
* If `/propose` splits a line, the new line enters the clinic's queue where the agent puts it. If it lands inside milestone 1, it is built in this delivery with the same five steps, and the README says so; if it lands in milestone 2, it waits.
* If the host writes notes outside the repository (auto-memory, as in chapter 11's run), they are deleted after each delivery, so the next run starts as a reader's would; the README says so.
* If a claim of the milestone's paragraph fails on the running app, /apply stops and asks the author whether it becomes a correction in this delivery or a line of the clinic's queue.

*The record, in this book,* `work/done/clinic-milestone-1-run/`:

```
README.md          host version, model, the clinic's first and last commit, the common flags and the allowlist;
                   then one section per delivery: date, commands, the answers given, the author's requests
                   word for word (or "none"), denied calls, what diverged, the commit's sha and subject;
                   then the milestone check: one line per claim of the paragraph, held or not
<slug>/turn-N.txt  every turn of that delivery, in order: text blocks byte for byte, tool calls as
                   [tool <name>] <relative path or command>
verify.txt         the npm run verify output on the clinic's last commit
```

Absolute paths are removed, so paths are relative to the clinic's root. Session ids are left out, since the disclosure scan matched one in chapter 11. No per-delivery excerpt files (first page, diffs, staged status, commit message): no chapter quotes these runs, and the clinic's commits hold the pages and the code.

*This book's documents, in the same delivery.*

* docs/05 §5, Guided project, gains one sentence: a delivery of this book that is not a chapter may advance the guided project (the first is `clinic-milestone-1`); the author commits each of its deliveries with the kit's message and no tag, and the next chapter tag includes those commits.
* docs/06: `clinic-milestone-1` goes to `[x]`. `closing-a-milestone` stays `[ ]`.
* docs/03: no new term.

*Numbers.* None enters the book in this delivery. Chapter 12 decides which, if any, it cites from this record.

**Out of scope.**

* The whole-milestone review with `/code-review`, its findings as queue lines, and the Ninjobs counter-example: chapter 12, `closing-a-milestone`.
* Any chapter text, in either edition: this delivery only builds and records.
* A chapter tag on the clinic: only chapters tag; chapter 12's tag will include these commits.
* Milestone 2 of the clinic (`absences`, `owner-schedule`, `install`, `deploy`): not needed to close milestone 1.
* Updating focus-kit in the clinic: the runs use `e7607c5`, which chapters 10 and 11 cite.
* Cost or duration numbers: chapter 24.

**Done when.**

* [x] The clinic's `skeleton` commit and tag `book-v1/apply` exist on the remote before the first run.
* [x] Five deliveries (plus any split line inside milestone 1) run the five steps, each a recorded turn sequence; nothing in the clinic edited by hand.
* [x] Each delivery committed by the author, no tag; all pushed.
* [x] The clinic's docs/06 shows milestone 1 all `[x]`, each page in `work/done/`.
* [x] The author ran `npm run dev` and checked every claim of the milestone's paragraph; the README records each.
* [x] `npm run verify` green on the clinic's last commit, saved as `verify.txt`.
* [x] No note of the host left outside the clinic's repository.
* [x] `work/done/clinic-milestone-1-run/` written as the Contract says.
* [x] docs/05 §5 has the sentence; docs/06 line `[x]`.
* [x] `make verify` green in this book, the disclosure scan included.
* [x] Page in `work/done/`, staged, commit message suggested.

## What happened

* The precondition was not met when /apply started: the clinic's `skeleton` delivery was still only staged and `book-v1/apply` did not exist. /apply stopped; the author committed, tagged and pushed, and /apply checked all three on the remote before the first run.
* Six deliveries, not five: `/apply weekly-hours` found a sign-in failing about once in 300 Playwright tests. At the author's request the agent queued it as `e2e-database-busy` inside milestone 1, before `book-appointment`, so it was built here with the same five steps. `/propose` also added three lines to milestone 2 (`owner-password`, `sign-in-limit`, `fake-bookings`); they wait.
* The book's /apply session started every turn through its shell and relayed each stop to the author. Requests were written in English by the agent from the author's choices and approved word for word before sending, except the three that record a manual check, written after the author reported it had worked; the README says which.
* Page reviews: two with corrections (`clinic-setup`, `book-appointment`), four with none. Staged reviews: corrections in `clinic-setup` (a shared fetch helper on its second use, a misplaced fixture), `weekly-hours` (the queue line, the commit message format) and `e2e-database-busy` (the commit message again, and finishing a staging the agent could not do). Every staged review also recorded the author's manual check.
* 25 calls denied across the six `/apply` sessions, none in `/propose`; none was retried by another route from outside the clinic's session. Most were shell loops reading files and `git mv`; one, `git -C . add -A`, left `e2e-database-busy` unstaged until the author's request, with `git add -A`, which is on the allowlist.
* Twice the suggested commit message carried a `Co-Authored-By` trailer; both were corrected by request before the author committed. In `e2e-database-busy` the agent saved that correction as a note in the host's auto-memory; it was deleted after that commit. No other note was left.
* The session's scratch folder was lost before `book-appointment`'s run ended; the raw streams moved to `output/` (never committed) and the run's result was intact.
* The milestone check: every claim of the paragraph held on the running app, each checked by the author at the delivery that built it; the author chose not to repeat them end to end.
* `npm run verify` green on `f16f83b`: 238 Vitest, 144 Playwright, build.
* The record: `work/done/clinic-milestone-1-run/`, as the Contract says. The turn files were derived with a one-off script outside the repository, as in chapters 10 and 11; no script entered `scripts/`.
* No ADR, no new term. docs/05 §5 has the sentence; docs/06 is `[x]`.
