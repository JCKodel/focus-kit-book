# The M4.2 review, recorded

The review of milestone M4.2, run on 2026-09-30 as docs/05 §8, "The recipe of a milestone review", says, with the changes §8's last-round rule asks for: the first review of a last round of fixes, which reads only what the round's lines changed.

* Host: Claude Code 2.1.285 (`claude --version`).
* Model: `claude-opus-5-5`, on turn 1, the only turn.
* The book's commit: `a905bfb`, `main`, clean; `make verify` green before turn 1.
* The clinic's commit: `36d7ad9`, `main`, clean, equal to `origin/main`.

## The ranges

Two dots, as the queue's M4.2 closed them, measured by this `/apply`:

* Book: `e18dff8..9e9c282 -- book/`. `e18dff8` is the `/propose` of M4.2's 14 lines; `9e9c282` ticks the push of the two clinic runs. The range holds 16 commits, 12 of which touch `book/`: 14 files, 129 insertions, 43 deletions (`git diff --shortstat`). The two later commits on `main`, `c395a63` and `a905bfb`, touch only `work/` and docs/06, so the range stands.
* Clinic: `6edc9ad..36d7ad9 -- src docs/01-Architecture.md`. Two commits, `21522b8` (`clinic-busy-fields`) and `36d7ad9` (`clinic-hours-answer`): 8 files, 34 insertions, 17 deletions. The clinic's `work/done/` and `docs/06` are left out: they are the runs' records, not what a reader runs.

Before turn 1, the two diffs were written here: `book.diff`, from `git log -p --reverse e18dff8..9e9c282 -- book/` (739 lines), and `clinic.diff`, from `git -C ../focus-kit-clinic log -p --reverse 6edc9ad..36d7ad9 -- src docs/01-Architecture.md` (211 lines). Each hunk sits under the commit whose subject names its M4.2 line.

## The adaptation of the recipe

First occurrence; §8's recipe is unchanged.

* Step 2: the review read the two diffs, and a changed chapter only around a hunk; not docs/00 nor docs/04, since the criterion is §8's blocking definition.
* Step 4: the request asks for a finding only on a changed line or a sentence around it, each marked blocking or not with its reason, in the shape `### F<n>` with Where, Clause, What, Reader, Blocking; the paragraph check answers a chapter clause `no tag`, since M4.2 made no chapter tag, and a code clause with the clinic's commit.
* One session reads both the book's diff and the clinic's, in place of a separate code review.
* Step 5: three decisions, blocking, not blocking or rejected; the first two both become lines.
* Step 6: the lines go at the start of M5, before `git-essentials`, with one opening clause in M5's paragraph; no M4.3.

## Turn 1, the review

Run from the root of this repository, detached with `nohup`:

```
CLAUDE_CODE_DISABLE_AUTO_MEMORY=1 nohup claude -p "<the request of decisions.md, turn 1>" --model claude-opus-5-5 --setting-sources project --strict-mcp-config --permission-mode default --permission-prompts none --output-format stream-json --verbose --allowedTools "Read" "Glob" "Grep"
```

* The session made 18 calls: 8 `Read`, 6 `Grep`, 4 `Bash`. It read both diffs, then the changed chapters 3, 7, 10, 14 and 15 around their hunks; its `Grep` calls searched changed chapters only (1, 3, 4, 7, 10, 13, 15, 16). It read nothing from `docs/`, `scripts/` or `work/` beyond the run folder.
* Its reads of chapter 14 (lines 30 to 329) and chapter 15 (lines 1 to 160 and 380 to 504) span several sections with hunks and the text between them, wider than one section around one hunk. Recorded, not repeated.
* Three `Bash` calls (`ls`, `wc` and `grep` in the run folder; `sed -n` in chapters 7 and 10), which the host allowed as read-only commands though the list did not name them, as in m4-review and m4.1-review.
* **Denied:** one `Bash` call, a `grep -n` of chapter 10 chained with a second `grep`. The session then ran the `Grep` tool on the same file with the same patterns: a retry by another route, which §8 step 8 forbids (see What diverged).
* Nothing changed in either repository.
* The findings, as reported, are `findings.md`; the turn is `turn-1.txt`.

## The paragraph check

As the review reported it, one line per clause:

* chapter 3's key points say only what its run showed: ch3 §Key points · no tag
* chapter 7 says which of the clinic's non-negotiables are the kit's: ch7 §The run on the clinic · no tag
* Part III's definitions of a feature and a unit test fit the clinic's code it shows: ch14 §Vertical slices, §Key points; ch16 §A test for each piece · no tag
* it says what the reader does about a bug that the boundary's catch hides: ch14 §Why not throw, §Exceptions as values in the clinic, §Key points · no tag
* chapter 14's boundary squares with the routes that import a library's type: ch14 §The boundary, §Key points · no tag
* chapter 15 places every catch in a piece: ch15 §What the clinic injects; ch14 §Exceptions as values in the clinic · no tag
* explains the rule its view excerpt shows: ch15 §One event, one new state · no tag
* prints the brief the reader is told to answer with: ch15 §The four pieces · no tag
* its key point on when a piece is written meets its section: ch15 §Key points · no tag
* the clinic's weekly hours editor and booking form take no edit while a save or a booking is in flight: clinic 21522b8
* only the hook can report that a save is in flight: clinic 36d7ad9
* the Portuguese edition uses the terms chapter 3 taught: pt ch1 §Key points; pt ch4 §How it was, §What went wrong, §Where it went, §Key points; pt ch13 §What the process does not have · no tag
* summarizes chapter 10's diff as it is: pt ch10 §Read the page before `/apply` · no tag

The opening clause, "every confirmed finding of the M4.1 review is settled", got no line of its own: the clauses after the colon list those findings, and each is answered above. Every clause points somewhere; the four findings fall on clauses that are answered, with what is still weak.

## The decisions

The book's `/apply` session read each finding against the text and gave its assessment, one line each:

* F1 (ch14:312, both editions): holds, narrowed. The key point's "every repository runs in a test against SQLite" fits the server repositories the section shows, not `request` or `remembered.ts`, which chapter 15 calls client repositories; its second half, logging, is general. Recommended: not blocking, nothing stated about the database is false.
* F2 (ch15:438-439): weak. The route turns an unreadable body into the answer `BadRequest`, not into a `Result`, and chapter 14 files it as a "vexing" parse, so "the repository alone turns an infra exception into a `Result`" holds as written; in the clinic each such catch writes the 400 response directly (`c.json({ error: { code: "BadRequest" } }, 400)`), no `Result`. Recommended: rejected.
* F3 (ch15:18, both editions): holds. The old "answer its questions with the author's brief" became an account of the author's run, so the clause "the brief the reader is told to answer with" is met only by inference. Recommended: not blocking, the brief is printed and the steps can be copied.
* F4 (ch15:150-151): holds, narrowed. `tooLateToCancel` compares the deadline with `now` in the client orchestrator, whose "Forbids" names deciding rules, and the text does not say why that is display, not a rule; "written once, in the use case" is true of `cancellationDeadline` in `rules.ts`. Recommended: not blocking, no sentence is shown false.

The clinic's code: both commits answer their clauses (`disabled={busy}` on the four fields; `WeeklyHoursAnswer` without "saving"). The review could not run the clinic's tests; each run's record (`clinic-busy-fields-run`, `clinic-hours-answer-run`) says `/apply` ran `npm run verify` green and keeps its output in `verify.txt`.

The author rejected all four, not on their merits but to close M4, in one sentence relayed word for word in `decisions.md`: "Não. M4 é M4. Chega de reviews. Senão vamos ficar corrigindo infinitamente." Each is recorded as `rejected, the author closes M4: no more rounds of fixes of M4`.

* Read: 4. Blocking: 0. Not blocking: 0. Rejected: 4 (F1 to F4). Already queued: 0.

## Turn 2, not sent

Turn 2 exists only to write the kept findings into docs/06. None was kept, so the review's session was not resumed: M5's paragraph and lines are untouched, no M4.3 opens, and there is no `queue.diff`.

## The rule that changed

The same decision changed docs/05 §8: a `.1` milestone has no review of its own; it closes when its lines are `[x]` with their proof, and whatever it missed is found by the review of the next milestone. The last-round review text of `52b3a30` is gone; "`.1` is the last" stays. docs/03's rows "milestone review" and "finding" say the same. This was the last review run under the old rule.

## Notes of the host

Auto-memory was off on turn 1. The host's memory folders for this repository and for the clinic held the same files, with the same dates, before turn 1 and after it: no note to delete.

## What diverged

* The `/propose` changes were committed (`a905bfb`) before this run, so turn 1 ran on a clean `main`, not with them uncommitted.
* The review read wider spans of chapters 14 and 15 than one section around a hunk (above).
* After its denied `Bash` grep, the review ran the same search with the `Grep` tool: a retry by another route, against §8 step 8. It read only chapter 10, which it was allowed to read, and changed nothing.
* This `/apply` ran as a batch agent with no conversation: the assessment above was its recommendation, relayed to the author by the driver, who relayed the decision back.
* The page asked for decisions finding by finding and a turn 2; the author closed M4 instead, so turn 2 was not sent and no line reached M5.

## Files

```
README.md     this file
book.diff     the book's range, written before turn 1
clinic.diff   the clinic's range, written before turn 1
turn-1.txt    the review's turn, text byte for byte, calls one line each
findings.md   the findings and the paragraph check, as reported
decisions.md  the request sent, word for word, and the author's decisions
```
