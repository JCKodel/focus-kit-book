# m4-review

**Objective.** After this delivery the author knows what Part III, and the Prologue and Parts I and II it builds on, still owe the reader, as findings each decided, with every confirmed finding a line in the queue; the review is recorded so that chapter 23 can tell it, and the recipe of a milestone review lives in docs/05 §8, where the next one reads it.

**Behaviour.**

* A fresh session that knows only the product questions reads the book from the Prologue to chapter 16, in order and in both editions, the way a reader would, and reports findings. It edits nothing.
* Each finding names where it is (file and line, in one or both editions), which product question of docs/00 it fails, or M4's paragraph, what is wrong and what the reader loses. A finding may be in any chapter from the Prologue to 16.
* The review checks M4's paragraph clause by clause: each clause gets the chapter and section that teaches it, and the guided project's tag the reader follows there. A clause with nowhere to point to is a finding.
* The review does not report what `make verify` already guards. It covers value, what is missing, whether a reader can follow each chapter from the earlier ones alone, whether the code a chapter prints can be followed from what the chapter says, and whether the Portuguese means what the English means.
* The /apply session checks each finding against the text and gives its assessment. The author decides each one, confirmed or rejected, with a one-sentence reason. Nothing is fixed.
* Each confirmed finding becomes a `[ ]` line in docs/06, in a new milestone M4.1 between M4 and M5, by the review's session. A finding already covered by an existing line adds no line; the existing line gains words only if the finding adds something, and the record says "already queued".
* docs/05 §8 holds the recipe of the review of a milestone of chapters, so that the M5 review follows it without reopening this page or m3-review's.
* The whole run is recorded, so chapter 23 can tell it and quote it.

**Contract.**

* docs/05 §8 gains the recipe, in the process's own words, with `m3-review` named as its first occurrence and this delivery as the second (AGENTS.md, abstraction on the second occurrence). It says, in substance:
  * Before the run: `main` with only the review's own `/propose` changes uncommitted; `make verify` green.
  * What is read, in order: docs/00 (audience, values, product questions), docs/04 §"Writing the book" and §"Prose rules", then the chapters from `00-` to the last chapter of the part, each chapter English then Portuguese. The milestone's paragraph is quoted in the request. Nothing else from docs/, work/ or scripts/; the guided project's tags only as the links the chapters print.
  * Turn 1, the review, headless and detached from the repository's root: `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1 nohup claude -p "<request>" --model <model> --setting-sources project --strict-mcp-config --permission-mode default --permission-prompts none --output-format stream-json --verbose --allowedTools "Read" "Glob" "Grep"`. Auto-memory is off because the reader does not have the host's notes on this project.
  * The request, in English, recorded word for word, says what the four review lines of this page's Behaviour say, and asks for the findings in the shape m3-review used (`### F<n>.` with Where, Question, What, Reader; then `## Paragraph`, one line per clause, `<clause>: <chapter §section> · <tag or "no tag">` or `<clause>: FINDING F<n>`).
  * The book's /apply session assesses each finding; the author decides each, `F<n>: confirmed|rejected, <reason>`.
  * Turn 2, sent with `--resume <the review's session id>`, never `--continue` (m3-review: `--continue` reached the /apply session running in the same directory): the decisions word for word as the author approved them, and the request to write the confirmed findings into docs/06 as `## M<n>.1. What the review of M<n> found`, after the milestone and before the next, with a paragraph "When this milestone closes, …" and one `[ ]` line per finding, and to stage it. Flags as turn 1, with `--permission-mode acceptEdits --allowedTools "Read" "Edit" "Bash(git add docs/06-Queue.md)" "Bash(git diff *)" "Bash(git status *)"`. Corrections are further recorded turns to the same session. docs/06 is not edited by hand for these lines.
  * No confirmed finding: no new milestone; the README says so.
  * A denied call is recorded, never retried by another route. Notes the host writes outside the repository are deleted after the run. Session ids and absolute paths are left out of the record.
  * The record, `work/done/<slug>-run/`: `README.md` (date, `claude --version`, model, the book's commit, commands, allowlists, the paragraph check one line per clause, counts read, confirmed, rejected and already queued, denied calls, what diverged), `turn-N.txt` (text blocks byte for byte, tool calls as `[tool <name>] <relative path or command>`), `findings.md` (as reported, byte for byte), `decisions.md` (each request, word for word), `queue.diff` (docs/06 before and after the lines).
  * A milestone that also changed the guided project gets a code review of its own, a separate delivery whose findings join the same `M<n>.1`.
* This run, following §8 as written by this delivery: model `claude-opus-5-5`; chapters `00-` to `16-`; the request says Part III is optional in the book (docs/00 Contents) and still owes the reader of Parts I and II everything question 5 asks; M4's paragraph quoted: "When this milestone closes, a reader can organize code by feature with exceptions as values, and knows when the four pieces pay their way and when they do not."
* Recorded in `work/done/m4-review-run/`, as §8 says.
* docs/03: no new term; milestone review and finding are used as defined.
* docs/06: under M4, `[>] m4-review` (this /propose), `[x]` by /apply; `[ ] m4-code-review` after it (this /propose); the new milestone M4.1 with its lines, by the run.

**Out of scope.**

* Fixing any finding: each waits as a line in M4.1.
* The clinic's code from `book-v1/closing-a-milestone` to `book-v1/four-pieces`: `m4-code-review`, a delivery of its own.
* Following Part III on an empty directory to prove the paragraph: a delivery of its own if a finding asks for it.
* Parts IV and V: not written yet.
* Telling this review in the book: chapter 23, which reads both records.
* Rewriting `work/done/m3-review.md` or its run to match §8: a record says what happened.

**Done when.**

* [x] docs/05 §8 holds the recipe, naming m3-review as the first occurrence; the run followed it.
* [x] Run recorded in `work/done/m4-review-run/`; every denied call in the README; no note of the host left outside the repository.
* [x] The paragraph check, one line per clause, in the README.
* [x] Every finding decided by the author with its reason; every request a recorded turn; no chapter edited.
* [x] docs/06 has M4.1 with one line per confirmed finding not already queued (or the README says there were none); `m4-review` `[x]`.
* [x] `make verify` green, the disclosure scan included.
* [x] Page in `work/done/`, staged, commit message suggested.

**What happened.**

* docs/05 §8 gained the recipe before turn 1, so the run followed it as written: m3-review is named as the first occurrence and this delivery as the second.
* The run is in `work/done/m4-review-run/`: 15 findings read, 15 confirmed, none rejected, none already queued. M4.1 holds 15 lines. The paragraph check points every clause to chapter 14 or 15 and its tag. No clause is a finding of its own, but F3 (what makes one feature), F7 (chapter 15's tag holds a delivery the reader never built) and F12 (no piece that has a job and still does not pay) weaken what they point to.
* The /apply session's assessment: every finding holds against the text. F4, F12 and F15 are narrowed: chapter 14 does say an exception can become a refusal; chapter 15 does name a cost; chapter 16 does explain its 33 of 77. The author accepted it whole.
* Turn 1 made one call outside its allowlist, a `Bash` of `ls` and `wc`, which the host allowed as read-only, as it allowed `grep` in m3-review. No call was denied.
* Turn 2 staged the whole of docs/06, so `kit-milestone-review`, a line the author added in another session during the run, is staged with this delivery. The README says so.
* Nothing else diverged from the page. Documents: docs/05 §8. docs/03 unchanged. No ADR. No chapter edited; nothing of M4.1 fixed.
