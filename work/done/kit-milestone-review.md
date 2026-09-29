# kit-milestone-review

**Objective.** After this delivery the book, the guided project and the brownfield fork run focus-kit `bff8414`, each one's docs/05 says that the last line of every milestone is its review, and every open milestone in the three queues ends with that line.

**Behaviour.**

* In each of the three repositories (this book, `../focus-kit-clinic`, `../clahub` on its branch `book`), the kit's files are the ones `SETUP.md` at focus-kit `bff8414` writes, byte for byte, and nothing else of the kit changed. The kit is read with `git -C ../focus-kit show bff8414:SETUP.md`, so a later kit commit does not leak in.
* The clinic's and the fork's docs/05 §4 and §8 read as the kit's template at `bff8414` reads, word for word; the rest of their docs/05 is untouched.
* This book's docs/05 §4 gains the kit's sentence, and §8 opens with the kit's two paragraphs; the chapter-milestone paragraph and the recipe stay; the code review paragraph places `m<n>-code-review` right after its review.
* docs/03's "milestone review" and "finding" say what the new §8 says.
* The book's queue: M4.1, M5, M6 and M7 end with their review line; M1, M2, M3 and M3.1 are unchanged; M4 already ends with `m4-review` and `m4-code-review`.
* The clinic's queue: "Milestone 2: what the review of milestone 1 found" becomes "Milestone 1.1: what the review of milestone 1 found", and "Milestone 3: the owner runs the day" becomes "Milestone 2: the owner runs the day"; each ends with its review line; milestone 1 (closed, reviewed in chapter 12) is unchanged.
* The fork's queue: Milestone 1 ends with its review line.
* The agent stages in each repository and suggests one commit message per repository; the author commits the clinic and the fork first, then the book.

**Contract.**

* **Kit.** focus-kit commit `bff8414` ("every milestone ends with its review; findings open <M>.1"). All three repositories are at `e7607c5` today (book `61a8e3a`, clinic `3f0b47c`, fork `f72e964`).
* **docs/05 §4, all three repositories**, the queue paragraph becomes:

      docs/06: one line per delivery, in order, under milestones. The line never
      leaves the queue; it changes mark: `[ ]` not defined, `[>]` defined and not
      built, `[x]` done. The last line of each milestone is its review (§8). Edited by
      conversation in any session.

* **docs/05 §8, clinic and fork**, the whole section becomes:

      The last line of every milestone is its review, `<milestone>-review`, a
      delivery like the others: /propose writes its page, /apply runs it. It
      checks the milestone's paragraph clause by clause against what the
      deliveries built, and reviews the code with what the host offers. A clause
      no delivery answers is a finding. The review fixes nothing; the person
      decides each finding, confirmed or rejected, with a reason.

      Each confirmed finding becomes a `[ ]` line in a new milestone placed
      right after the reviewed one, numbered with `.1` (M3 is followed by M3.1),
      with its own paragraph, so the lines wait for /propose and nothing
      renumbers. That milestone ends with its own review, which may open `.2`.
      No confirmed finding, no new milestone. A finding is never a fix in the
      middle of the next milestone.

* **docs/05 §8, this book**: its first paragraph ("When a milestone closes, review the whole…") is replaced by the two paragraphs above; "For a milestone of chapters…" and the recipe stay as they are; the last paragraph becomes: "A milestone that also changed the guided project gets a code review of its own, `m<n>-code-review`, a separate delivery placed right after its review, whose findings join the same `M<n>.1`."
* **docs/05 §5 Brownfield project, this book**, gains: "A delivery of this book that is not a chapter may change the fork too (the first were the kit's installs); the author commits it on `book` with the fork's message style and no tag." Precedent: `c3512ab` and `f72e964` on `book`.
* **docs/03, this book**:
  * milestone review · revisão de marco · `<milestone>-review`, docs/05 §8 · "The last delivery of every milestone: its paragraph checked clause by clause against what the deliveries built, then the code reviewed with what the host offers; it fixes nothing, and its confirmed findings open the milestone `<M>.1` right after."
  * finding · achado · none · "One problem a milestone review reports; the person confirms or rejects it with a reason, and a confirmed one becomes a `[ ]` line in the milestone `<M>.1`, never a fix in the middle of the next milestone."
* **The book's docs/06, new lines**, each the last of its milestone, except `m7-review`:
  * M4.1: `[ ] m4.1-review            the review of M4.1 as docs/05 §8 says: the Prologue to chapter 16 read end to end in both editions against the product questions and M4.1's paragraph; each confirmed finding becomes a line in a new milestone M4.2`
  * M5: `[ ] m5-review              the review of M5 as docs/05 §8 says: the Prologue to chapter 20 read end to end in both editions against the product questions and M5's paragraph; each confirmed finding becomes a line in a new milestone M5.1`
  * M6: `[ ] m6-review              the review of M6 as docs/05 §8 says: the Prologue to chapter 25 read end to end in both editions against the product questions and M6's paragraph; each confirmed finding becomes a line in a new milestone M6.1`
  * M7, placed before `launch`: `[ ] m7-review              the review of M7 as docs/05 §8 says: the whole book and its appendices read end to end in both editions against the product questions and M7's paragraph, before v1 is tagged; each confirmed finding becomes a line in a new milestone M7.1`
* **The clinic's docs/06**: the two headings renamed as Behaviour says, paragraphs unchanged; last lines:
  * Milestone 1.1: `[ ] m1.1-review          the review of milestone 1.1 as docs/05 §8 says: its paragraph clause by clause, then the code; confirmed findings open milestone 1.2`
  * Milestone 2: `[ ] m2-review            the review of milestone 2 as docs/05 §8 says: its paragraph clause by clause, then the code; confirmed findings open milestone 2.1`
* **The fork's docs/06**, last line of Milestone 1: `[ ] m1-review                    the review of milestone 1 as docs/05 §8 says: its paragraph clause by clause, then the code; confirmed findings open milestone 1.1`
* **Suggested commits.** Clinic and fork: `Update focus-kit to bff8414`, body: the review is each milestone's last line; docs/05 §4 and §8 follow the kit; review lines queued (the clinic also names the renamed milestones); last line `work/done/kit-milestone-review.md in JCKodel/focus-kit-book`. Book: `chore(kit-milestone-review): reinstall the kit at bff8414, queue the reviews`, last line `work/done/kit-milestone-review.md`.

**Out of scope.**

* The chapters: 7, 8, 9 and 12 follow `bff8414`, and 13, 14 and 15 name the clinic's renamed milestones; the line `kit-milestone-review-chapters`, right after this one in M4.
* Review lines for M1, M2, M3 and M3.1: closed, and `m3-review` and `m4-review` already read everything they built from the Prologue on; a line there would catch no error.
* A code review line for M4.1 to M7: §8 adds `m<n>-code-review` only once a milestone has changed the guided project, known when it closes.
* Moving or retagging any published tag, in the clinic or the fork: tags never move.
* The clinic's and the fork's verify: only Markdown under docs/ and the kit's folders changes, which neither verify reads.
* A recorded run: the clinic's steps of docs/05 §5 are for its deliveries; this changes only its kit and its process documents, as `3f0b47c` did.

**Done when.**

* [x] In each repository, `git diff --cached --stat` lists only the kit's files, docs/05 and docs/06 (the book also docs/03 and this page), and the kit's files match `bff8414`'s SETUP.md.
* [x] The Contract's text is in place, word for word.
* [x] The book's docs/06: `[x] kit-milestone-review`, `[ ] kit-milestone-review-chapters` after it.
* [x] `make verify` green in the book.
* [x] Three commit messages suggested; nothing committed.

**What happened.**

* The kit: a script outside the repository took every file of SETUP.md §3 (the fenced block under each 3.x heading, `<name>` filled for 3.6 to 3.9), 36 files. Run first on `e7607c5`'s SETUP.md, it matched all three repositories byte for byte, which proved the extraction; run on `bff8414`'s, it changed the same 12 files in each: `brainstorm/SKILL.md`, `analyze/SKILL.md` and both `references/documents.md` in the three skill folders. The other 24 files are the same at both kit commits. No repository has a `GEMINI.md` of its own.
* docs/05 §4 and §8: the clinic's and the fork's §8 now equal the template's §8 of `bff8414` (checked with `diff`); §4 is the Contract's paragraph in all three. In the book, the first paragraph of §8 was the same as the old template's, so the same replacement served; the chapter-milestone paragraph and the recipe stay.
* Diverged from the plan, decided by the author: the recipe's step 6 asked turn 2 for a paragraph and one `[ ]` line per finding, with no review line, so a run that followed it word for word would leave `M<n>.1` without the review the new §8 requires. Step 6 now asks for "one `[ ]` line per finding, the last one `m<n>.1-review`".
* Queues: the book gains `m4.1-review`, `m5-review`, `m6-review` and `m7-review` (before `launch`), as the Contract words them; the clinic's two headings renamed with their paragraphs untouched, and `m1.1-review` and `m2-review` added; the fork gains `m1-review`. No other tracked Markdown in the clinic names its milestones 2 or 3; the chapters that do are `kit-milestone-review-chapters`.
* Proof: `make verify` green in the book. The clinic's and the fork's verify were not run (Out of scope).
* Staged: in the clinic and the fork, only the 12 kit files, docs/05 and docs/06; in the book, the same plus docs/03 and this page.
