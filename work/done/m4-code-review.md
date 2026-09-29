# m4-code-review

**Objective.** After this delivery the author knows what the clinic's code that Part III shows still owes, as findings each decided, with every confirmed finding a line in M4.1; the review is recorded so that chapter 23 can tell it, and the recipe of a milestone's code review lives in docs/05 §8, where the M5 review reads it.

**Behaviour.**

* `/code-review high` reviews the clinic's code that M4 added, `book-v1/closing-a-milestone` to `book-v1/four-pieces`, headless, from the clinic's root. The kit update `kit-milestone-review` made after that tag is left out. The review edits nothing.
* The /apply session checks each finding against the clinic's code and documents and gives its assessment. The author decides each one, confirmed or rejected, with a one-sentence reason. Nothing is fixed.
* A confirmed finding that an existing M4.1 line already covers adds no line. That line gains words only if the finding adds something, and the record says "already queued".
* A confirmed finding that a line of the clinic's milestone 1.1 covers (`route-errors` and `minutes-of` may overlap) still becomes an M4.1 line. The line names the clinic's line and what the finding adds to it. The clinic's docs/06 is never touched.
* The review's own session writes each confirmed finding as a `[ ]` line in the book's M4.1, just before `m4.1-review`, and adds a clause about the clinic's code to M4.1's paragraph. It stages the book's docs/06. Nothing in the clinic changes.
* docs/05 §8 holds the recipe of a milestone's code review, so that `m5-code-review` (if M5 changes the guided project) follows it without reopening this page or chapter 12's.
* The whole run is recorded, so chapter 23 can tell it and quote it.

**Contract.**

* The range. `c54d011...e6653b5`, three dots, the form of Claude Code's documentation, as chapter 12's run README explains. `c54d011` is `book-v1/closing-a-milestone`, `e6653b5` is `book-v1/four-pieces`, and the range is one commit, `clinic-orchestrator-tests` ("Move each client hook's events into tested plain functions"): 28 files, 2987 insertions, 697 deletions (`git diff --stat`).
* Before the run:
  * Book: `main`, with only this `/propose`'s changes uncommitted, and `make verify` green.
  * Clinic: `main`, clean, at `a3e2470`, equal to `origin/main`. `a3e2470` ("Update focus-kit to bff8414") comes after the range and touches only the kit's files, `docs/05` and `docs/06` (14 files, no `src/`), so the tree the review reads differs from `e6653b5` only there. If the clinic has moved past `a3e2470` when /apply starts, /apply stops and asks.
  * /apply checks from Claude Code's documentation, never by running a review, that `--add-dir` lets the resumed session read, edit and `git add` in the book's directory under `acceptEdits` and the allowlist of turn 2. The README records the answer. If it does not, the fallback below applies.
* Turn 1, the review, from the clinic's root, detached:
  `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1 nohup claude -p "/code-review high c54d011...e6653b5" --model claude-opus-5-5 --setting-sources project --strict-mcp-config --permission-mode default --permission-prompts none --output-format stream-json --verbose --allowedTools "Bash(git diff *)" "Bash(git log *)" "Bash(git show *)" "Bash(git status *)" "Bash(npm *)" "Bash(npx *)"`
  The model and level are chapter 12's, for chapter 12's reason: breadth suits one look at the whole, and the person's decision filters what is uncertain. Auto-memory is off and the run is detached, as §8 learned in m4-review and in chapter 12.
* The assessment and the decisions. The book's /apply session assesses each finding. The author decides each one, `<n>: confirmed|rejected, <reason>`, in one sentence, and approves the request word for word before it is sent.
* Turn 2, the decisions and the lines, with `--resume <turn 1's session id>`, never `--continue`, from the clinic's root, flags as turn 1 plus `--add-dir ../focus-kit-book`, with `--permission-mode acceptEdits` and this `--allowedTools` replacing turn 1's: `"Read" "Edit" "Bash(git -C ../focus-kit-book add docs/06-Queue.md)" "Bash(git -C ../focus-kit-book diff *)" "Bash(git -C ../focus-kit-book status *)"`. The request, in English, says:
  * the decisions, word for word;
  * write each confirmed finding not already queued as one line in `../focus-kit-book/docs/06-Queue.md`, inside M4.1's block, before `m4.1-review`, in this shape:
    `[ ] clinic-<slug>  <what the clinic's code does afterwards>, by a recorded run`
    (the shape of `clinic-orchestrator-tests`: a delivery of this book that changes the guided project, with no chapter and no tag, whose clinic line the clinic's own `/propose` adds when it runs); a finding a clinic milestone 1.1 line covers gets its M4.1 line too, which names that clinic line and what the finding adds;
  * an M4.1 line that already covers a finding gets no new line, only words if the finding adds something;
  * add to M4.1's paragraph one clause saying what the clinic's code does once those lines are done;
  * in English, with no em dash; edit nothing else, in either repository; stage with exactly `git -C ../focus-kit-book add docs/06-Queue.md`, and check with `git -C ../focus-kit-book diff --cached` and `git -C ../focus-kit-book status --short`.
  Corrections are further turns to the same session, recorded. The book's docs/06 is not edited by hand for these lines.
* Fallback. If `--add-dir` does not allow turn 2, or the resumed session cannot or will not write the lines, a fresh interactive session in the book gets the same request, recorded as a turn. The README says so.
* No confirmed finding: M4.1 is unchanged and the README says so.
* A denied call is recorded, never retried by another route. Notes the host writes outside the repository are deleted after the run, in the clinic's and in the book's auto-memory folders. Session ids and absolute paths are left out of the record.
* The record, `work/done/m4-code-review-run/`: `README.md` (date, `claude --version`, model, the book's commit and the clinic's, the range and the target form, the `--add-dir` check, commands, allowlists, counts read, confirmed, rejected and already queued (with the queue), denied calls, what diverged); `turn-N.txt` (text blocks byte for byte, tool calls as `[tool <name>] <relative path or command>`); `findings.md` (as reported, one block each, byte for byte); `decisions.md` (each request, word for word); `queue.diff` (the book's docs/06 before and after the lines).
* docs/05 §8, last paragraph: the sentence on `m<n>-code-review` becomes its recipe, in the process's words, naming `closing-a-milestone` as the first occurrence and this delivery as the second. In substance:
  1. The range: from the previous milestone's last chapter tag to this milestone's last chapter tag, three dots; the README says how many commits it holds, names any commit of the milestone past the last tag, and says whether it is reviewed and why.
  2. Before the run: the book as step 1 of the chapters' recipe; the guided project on `main`, clean, equal to `origin/main`, with nothing in `src/` past the range's end.
  3. Turn 1: turn 1 above, with `<model>` and `<range>`.
  4. The /apply session assesses; the author decides each finding.
  5. Turn 2: turn 2 above, with `m<n>.1-review` and M<n>.1. If the milestone review found nothing and M<n>.1 does not exist, turn 2 creates it as the chapters' recipe says.
  6. The fallback, "already queued" in either queue, denied calls, notes of the host, the record: as above.
  Written before turn 1, so the run follows §8 as written, as m4-review did.
* docs/03: no new term. milestone review, finding, guided project and chapter tag are used as defined.
* docs/06: `[>] m4-code-review` (this /propose); `[x]` by /apply; M4.1's new lines and clause by turn 2.

**Out of scope.**

* Fixing any finding: each waits as a line in M4.1.
* A paragraph check: m4-review checked M4's paragraph clause by clause, and the clinic's milestone paragraphs belong to the clinic's own reviews.
* The clinic's own queue, even where a finding overlaps its milestone 1.1: its `/propose` adds each line when that delivery runs; writing it now would give one line two sources.
* `a3e2470` and the kit's files: they are not the clinic's code, and `kit-milestone-review` delivered them.
* The clinic's `m1.1-review` and `m2-review`: the clinic's milestones, not the book's.
* `/code-review ultra`: billed, and chapter 12 set `high` as the book's level.
* Telling this review in the book: chapter 23, which reads the record.
* Rewriting chapter 12's run or page to match the recipe: a record says what happened.

**Done when.**

* [x] docs/05 §8 holds the code-review recipe, naming closing-a-milestone as the first occurrence, written before turn 1; the run followed it.
* [x] The `--add-dir` check and the target form in the README, from the documentation, without running a review.
* [x] Run recorded in `work/done/m4-code-review-run/`; every denied call in the README; no note of the host left outside either repository.
* [x] Every finding decided by the author with its reason; every request a recorded turn; no clinic file changed.
* [x] The book's docs/06 has one M4.1 line per confirmed finding not already queued, and the paragraph's clause, or the README says there were none; `m4-code-review` `[x]`.
* [x] `make verify` green, the disclosure scan included.
* [x] Page in `work/done/`, staged, commit message suggested.

**What happened.**

* docs/05 §8 gained the recipe of a milestone's code review before turn 1, so the run followed it as written: closing-a-milestone is named as the first occurrence and this delivery as the second.
* The `--add-dir` check, from the CLI reference and the permissions page: an added directory is read and edited under the session's permission mode, and `acceptEdits` accepts edits there. Turn 2 wrote and staged the lines from the clinic's root; the fallback was not needed.
* The run is in `work/done/m4-code-review-run/`: 9 findings read, 7 confirmed, 2 rejected, none already queued in M4.1. The /apply session's assessment: 1 and 2 break the rule of an update `(current) => State` that docs/01 and the delivery state, though no click reaches the overwrite today; 6 is the same fix as 1, 7 the same as 3; 8 was recorded on purpose by the delivery; 9 asks the Orchestrator level, which docs/04 keeps without a DOM, to test the hook. The author accepted it whole.
* Diverged: the author chose one M4.1 line for each pair of findings that one change settles, 1 with 6 and 3 with 7, so seven confirmed findings are five lines (`clinic-booking-submit`, `clinic-hours-save`, `clinic-hours-report`, `clinic-update-type`, `clinic-event-shapes`), and M4.1's paragraph gained one clause about the clinic's orchestrators.
* The clinic's milestone 1.1: `clinic-hours-report` names its `[x] orchestrator-tests` line, which left `forward` and the `saving` report in the hook untested. Finding 5 falls under its paragraph's clause on repeated code, but under no line. The clinic's docs/06 is untouched.
* Turn 2 had one call denied, a `cd` with `git status` and `grep` on the book's docs/06; it was not retried by another route, and the session read the file with `Read`. Turn 1 had none. No correction was needed, so there is no turn 3.
* For later: M4.1's `ch15-submit-event` asks chapter 15 to explain `shown`, which `clinic-booking-submit` removes; the order of the two is decided when they are built.
* No clinic file changed; no note of the host was written. Documents: docs/05 §8. docs/03 unchanged. No ADR.
