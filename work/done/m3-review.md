# m3-review

**Objective.** After this delivery the author knows what Part II, and the Prologue and Part I it builds on, still owe the reader, as findings each decided, with every confirmed finding a line in the queue, and the review recorded so that chapter 23 can tell it.

**Behaviour.**

* A fresh session that knows only the product questions reads the book from the Prologue to chapter 13, in order and in both editions, the way a reader would, and reports findings. It edits nothing.
* Each finding names where it is (file and line, in one or both editions), which product question of docs/00 it fails, or M3's paragraph, what is wrong and what the reader loses. A finding may be in any chapter from the Prologue to 13.
* The review checks M3's paragraph clause by clause: each clause gets the chapter and section that teaches it, and the guided project's tag the reader follows there. A clause with nowhere to point to is a finding.
* The review does not report what `make verify` already guards (parity of structure, em dash, the prose rules, links, disclosure). It covers value, what is missing, whether a reader can follow each chapter from the earlier ones alone, and whether the Portuguese means what the English means.
* The /apply session checks each finding against the text and gives its assessment. The author decides each one, confirmed or rejected, with a one-sentence reason. Nothing is fixed.
* Each confirmed finding becomes a `[ ]` line in docs/06, in a new milestone between M3 and M4 with its own paragraph. If a finding is already covered by an existing line, no new line is added: the existing line gains words only if the finding adds something, and it is marked "already queued".
* The whole run is recorded, so chapter 23 can tell it and quote it.

**Contract.**

* Before the run: this repository on `main`, clean; `make verify` green.
* What is read, in this order: docs/00 (audience, values, product questions), docs/04 §Voice and the prose rules, then `book/en/00-…` to `book/en/13-…` and `book/pt/00-…` to `book/pt/13-…`, chapter by chapter, English then Portuguese. The docs/06 paragraph of M3 is quoted in the request. Nothing else from docs/, work/ or scripts/. The guided project's tags are reached only through the links the chapters print.
* The review, headless, in this repository: `claude -p "<request>"` with `--model claude-opus-5-5 --setting-sources project --strict-mcp-config --permission-mode default --permission-prompts none --output-format stream-json --verbose --allowedTools "Read" "Glob" "Grep"`, started detached (`nohup`) as chapter 12 learned. It stops, and /apply shows the author the findings.
* The request (turn 1) is written in English and recorded word for word. It says, in its own words, everything the four review lines of Behaviour say, and it asks for the findings in this shape, one block each, numbered in the order read:

      ### F<n>. <one-line summary>
      * Where: `book/<ed>/<file>:<line>`[, `book/<ed>/<file>:<line>`]
      * Question: <1 to 6 of docs/00> | paragraph
      * What: <what is wrong, quoting at most one sentence of the book>
      * Reader: <what a reader loses, one sentence>

  followed by `## Paragraph`, one line per clause: `<clause>: <chapter §section> · <tag or "no tag">` or `<clause>: FINDING F<n>`.
* The decisions (turn 2), sent with `--continue`, word for word as the author approves them, in one request: each finding `F<n>: confirmed|rejected, <reason>`. The same request asks the session to write the confirmed findings into docs/06 as a new milestone, `## M3.1. What the review of M3 found`, placed between M3 and M4, with a paragraph in the form of the others ("When this milestone closes, …") and one `[ ]` line per finding, slug and description in the queue's format, and to stage it. This turn runs with `--permission-mode acceptEdits --allowedTools "Read" "Edit" "Bash(git add docs/06-Queue.md)" "Bash(git diff *)" "Bash(git status *)"`. Corrections follow with `--continue`, as recorded turns. docs/06 is not edited by hand for these lines.
* No confirmed finding: no new milestone; the README says so.
* A denied call is recorded, never retried by another route. Notes the host writes outside the repository are deleted after the run. Session ids and absolute paths are left out of the record.
* Recorded in `work/done/m3-review-run/`: `README.md` (date, `claude --version`, model, commands, allowlists, the paragraph check one line per clause, counts of findings read, confirmed and rejected, denied calls, what diverged), `turn-N.txt` (text blocks byte for byte, tool calls as `[tool <name>] <relative path or command>`), `findings.md` (the findings as reported, byte for byte), `decisions.md` (each request sent, word for word), `queue.diff` (docs/06 before and after the lines).
* docs/03: no new term; milestone review and finding are used as defined.
* docs/05 §8, second paragraph, becomes, in substance: the review of a milestone of chapters is a fresh session that reads the book from its start to the end of the part, in both editions, and asks the product questions of docs/00, above all whether every sentence carries value and whether anything the reader needs is missing. It checks the milestone's paragraph clause by clause against the chapters that teach it, and its findings may fall in any chapter it read.
* docs/06: the `m3-review` line becomes `[>]` with its description reading "the Prologue to chapter 13, both editions" (this /propose); `[x]` by /apply; the new milestone M3.1 with its lines, by the run.

**Out of scope.**

* Fixing any finding: each one waits as a line in M3.1.
* Following the chapters on an empty directory to prove the paragraph: a delivery of its own if a finding asks for it.
* Parts III to V: not written yet.
* Telling this review in the book: chapter 23, `beyond-software`, which reads this record.
* Renumbering M4 to M7: M3.1 avoids touching references to them.
* A review of the toolchain deliveries of M3 (`commit-hooks`, `useful-notes`) with `/code-review`: the milestone is chapters; the scripts are guarded by verify.

**Done when.**

* [x] Run recorded in `work/done/m3-review-run/` as the Contract says; every denied call in the README; no note of the host left outside the repository.
* [x] The paragraph check, one line per clause, in the README.
* [x] Every finding decided by the author with its reason; every request a recorded turn; no chapter edited.
* [x] docs/06 has M3.1 with one line per confirmed finding not already queued (or the README says there were none); `m3-review` `[x]`.
* [x] docs/05 §8 says the new reading.
* [x] `make verify` green, the disclosure scan included.
* [x] Page in `work/done/`, staged, commit message suggested.

**What happened.**

* The run is in `work/done/m3-review-run/`: 19 findings read, 19 confirmed, none rejected, none already queued; M3.1 holds 19 lines. The paragraph check put every clause in a chapter except "deliver a milestone, following the guided project", which is F17: nothing tells the reader to build the rest of milestone 1 between chapters 11 and 12.
* Before the run, `make verify` was red on one link, the guided project's tag `book-v1/closing-a-milestone`: chapter 12's commit and tag in the clinic were still the author's to do. The author did them (`c54d011`), and the placeholder `COMMIT_SHA` in `work/done/closing-a-milestone-run/README.md` now names that commit.
* Diverged, each approved by the author before it happened: the run started with this delivery's two uncommitted changes (docs/06's `[>]` line and this page), which the review does not read; both turns ran with `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1`, so the session did not load the host's notes on this project and wrote none; the request names docs/04 §"Writing the book", since Voice is one of its bullets and not a section.
* Diverged: `--continue` takes the most recent conversation of the directory, which was this `/apply` session, not the review. The first send of turn 2 reached it and was stopped before any call or text; the same request went again with `--resume` and the review's session. A later review run from the same directory as the book's own session resumes by id.
* The /apply session's assessment: every finding stands against the text; F14 narrowed, since the chapters do name the second agent and what they miss is that the runs are headless, what `--continue` does, and what an interactive reader does instead. The author accepted it whole.
* Documents: docs/05 §8 says the new reading of a milestone of chapters. docs/03 unchanged. No ADR.
* No chapter edited; nothing of M3.1 fixed.
