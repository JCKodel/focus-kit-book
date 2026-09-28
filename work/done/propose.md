# propose

**Objective.** After chapter 10 the reader can run `/propose` on a queue line, answer its questions, read the page it writes as the record of what the agent understood and of what `/apply` will build, cover its holes by conversation before `/apply`, and split a delivery that does not fit one page.

**Behaviour.**

* The reader can say what `/propose` reads (docs/00, 03, 05, 06, 01 and `work/`), what it asks (only where there is more than one reading and no document closes it, recommendation first), and what it writes: `work/<slug>.md` in the format of docs/05 §3, the mark `[ ]` to `[>]`, and never code, migration, test or configuration.
* The reader can say why the Contract is the one exact section: a wrong screen is fixed in a session, a wrong column is a migration.
* The reader can run `/propose skeleton` on the clinic with this chapter's brief and compare their page with the one recorded in the book.
* The reader treats the page as a document to read, not a step to pass: it is what the agent understood and what will be built. They read it before `/apply`, interpret it, and cover every hole by asking the agent, never by editing by hand (chapter 6), and they know why: a hole found on the page costs one turn of conversation; a hole found after `/apply` costs another `/apply`, and `/apply` costs about twice what `/propose` does.
* The reader can ask a page the review questions: can each Behaviour line become a test or a check? Is the Contract exact, or "none" on purpose? Does Out of scope name what I assumed was in? Is Done when mechanical? Did the agent decide something I would have decided otherwise ("your call" answers first)?
* The reader knows the unit of work: the page and its build are one change that reverts in one step. On trunk they land in one commit, so the page waits uncommitted between `/propose` and `/apply`; on a branch or a worktree the branch may carry several commits, and the delivery reaches the main branch in one merge.
* The reader knows what to do when a scope does not fit one page: it is two deliveries; `/propose` says so, proposes the split, writes only the first, and the second becomes a line where it belongs.

**Contract.**

Chapter 10, `book/en/10-propose.md` and `book/pt/10-propose.md`:

* Title: "`/propose`, one page" / "`/propose`, uma página".
* Voice: instruction to the reader as "you"; the run and the review are the author's, in the first person where they are told (docs/04 §Voice).
* Sections, in order (headings may be reworded; both editions keep the same structure):
  1. Opening, at most three sentences: the Objective.
  2. What it does. What `/propose` reads, how it asks, what it writes and what it never writes, from the kit's `propose/SKILL.md` (paraphrased; at most the two sentences on the Contract quoted). The page's format is docs/05 §3 of the clinic, pointed to at `book-v1/brainstorm`, not repeated. Deciding and doing are separate sessions: one sentence, pointing to chapter 2 (fresh session). The mark `[>]` in one sentence, pointing to chapter 9. The unit of work, in two or three sentences: page and build revert as one; on trunk one commit, so the page waits uncommitted; on a branch several commits and one merge; Part IV teaches the git side. This is why the run leaves the clinic uncommitted.
  3. The run on the clinic. Context: the clinic after `book-v1/brainstorm`, at commit `3f0b47c` "Update focus-kit to e7607c5" (the kit updated as chapter 5 teaches, one commit of its own, so it reverts in one step), its queue's first line `skeleton`. The kit's new ending, which asks the person to read the page before `/apply`, is part of what the run shows. The brief, shown whole. The questions the agent asked and the answers, from `questions.md`, byte for byte. Then the page as the agent first wrote it, quoted whole from the run record, with one sentence after it on what to see.
  4. Read the page before `/apply`. The heart of the chapter. The page is the documentation of what the agent understood and it is what will be built; it is written to be read by a person, interpreted and completed, not generated and applied in the same breath. The cost argument with the numbers (below). The review questions of Behaviour. Then the author's real review of the run's page: each hole found, the request sent to the same session (byte for byte), and the diff from the first page to the reviewed one. If the review finds no hole, the section says so, and the questions stand alone. One sentence: the agent's text reads as right even when it is wrong; the person validates (chapter 6).
  5. When it does not fit. Two deliveries: say so, propose the split, write only the first; the second becomes a line where it belongs (chapter 9). The example is this book's own split: `spec-driven-run` was taken out of chapter 3's delivery and entered the queue before `spec-driven`, the diff of docs/06 at commit `53109f3`, quoted whole (English in both editions, translated with a note in Portuguese, as chapter 9 does). Context before it (the measured run would not fit on the chapter's page), one sentence after it (the new line sits before the chapter that needs it, already `[x]` because page and build landed in one commit).
  6. Key points, at most five, one of them: read the page before `/apply`.
  7. Exercises (below).
* The brief, saved as `work/done/propose-run/brief.md`, and given as answers word for word:

  ```
  # Brief

  ## Delivery
  The first line of the queue: skeleton.

  ## Rule for a question the brief does not answer
  Your call. Say what you chose and why.
  ```

* The run, the same mechanism as chapter 7's (`work/done/brainstorm-run/`, the first occurrence; this is the third with chapter 8). Claude Code headless (`claude -p "/propose skeleton"`), inside `../focus-kit-clinic` at `3f0b47c`, with `--setting-sources project --strict-mcp-config`, the least permission mode that lets it finish (recorded), `--continue` for each answer. Each answer is a brief section word for word, or its rule; /apply writes no other words. Recorded in `work/done/propose-run/`: `brief.md`, the exact commands, `claude --version`, the model, the transcript of every turn (as chapter 7's run: text blocks byte for byte, tool calls as name and relative path), `questions.md`, `skeleton-first.md` (the page as first written), `review.md` (each request of the author and its turn), `skeleton.diff` (first page to reviewed page), and `git status --short` of the clinic after it.
* The review. /apply stops after the run and shows the author the page. The author reads it; each request is sent by /apply to the same session, word for word as the author gives it, as a recorded turn. The page is never edited by hand. /apply writes the chapter only after the author says the review is over.
* The clinic after the run: `work/skeleton.md` and docs/06 with `skeleton` at `[>]`, left in its working tree, not staged, not committed, no tag. The kit puts the page and its build in the same commit; chapter 11 builds this page, and its commit and tag carry both. Chapter 10 has no chapter tag.
* The usage numbers. `work/done/propose-run/usage.txt` holds the author's `/usage` output of 2026-09-28, terminal escapes removed, saved by /propose (already written; /apply does not change it). It is "approximate, based on local sessions on this machine", every project together: the author read it in three projects and got the same figures, so it is not a per-project measure, and the source note says so. The chapter cites both windows: last 24 hours, `/apply` 32% and `/propose` 16%; last 7 days, `/apply` 47% and `/propose` 14%. It says `/apply` costs from twice to more than three times what `/propose` does. /apply cannot measure them and does not recompute them.
* Numbers, and only these: the four usage shares and their two windows; the counts that `53109f3`'s diff shows (none are added). The Claude Code version and model in the run's source note only.
* docs/03 terms used: command, page, delivery, queue, mark, fresh session, project documents, slot, verify, guided project, and the new unit of work (Portuguese "unidade de trabalho"). No other new term: "brief" and "review" are words of the book's runs and prose, not of the method.
* Sources (`[^key]`, same keys in both editions):
  * `[^focus-kit-propose]` (new): `SETUP.md` §3.3 at focus-kit `e7607c58ad38e70e3496518a58d4237612e21ebc`, installed in the clinic at `3f0b47c`.
  * `[^propose-run]` (new): `work/done/propose-run/README.md` on `main`.
  * `[^claude-usage]` (new): "Claude Code `/usage`, read by the author on 2026-09-28, local sessions on one machine, all projects together; `work/done/propose-run/usage.txt`."
  * `[^focus-kit-unit-of-work]` (new): `SETUP.md` at focus-kit `e7607c58ad38e70e3496518a58d4237612e21ebc`, which states the unit of work, for chapters 6, 9 and 10.
  * `[^book-spec-driven-run]` (new): `https://github.com/JCKodel/focus-kit-book/commit/53109f372125e8aeda200bb2e5bbd1ad7bcc5d61`.
* Cases: the clinic; this book. No Ninjobs, no Case A or B.
* Exercises, on the clinic, by conversation with the agent, never by hand:
  * 10.1 Check out `book-v1/brainstorm` on a branch of your own, update the kit as in chapter 5, run `/propose skeleton` with the brief, and compare your page with the one in this chapter. Which differences are the agent's "your call" choices?
  * 10.2 Review your page with the questions of section 4 before any `/apply`. Ask the agent to cover each hole, and read the diff.
  * 10.3 Ask `/propose` for `book-appointment` and `cancel-appointment` as one delivery. Does it propose a split? Where does the second line go?
* Corrections to earlier chapters, both editions, same delivery. Both said the page and the build land in the same commit in all three git strategies, which is true only on trunk:
  * Chapter 6, "The two choices", the sentence "In every one, the page `/propose` writes and the build `/apply` makes land in the same commit, and the agent never commits or merges." becomes the unit of work: in every one the delivery reverts in one step, one commit on trunk, one merge of the branch otherwise, and the agent never commits or merges. The trunk, branch and worktree sentences stay.
  * Chapter 9, "The marks", the sentence "With trunk, a branch or a worktree, the page and the build land in the same commit, so `[>]` lives in the working tree between the two commands." becomes: on trunk the page and the build land in one commit, so `[>]` waits in the working tree; on a branch the page may be committed there, and the delivery reaches the main branch in one merge. Sentence 91 of chapter 9 (`two-choices` in one commit) is true on trunk and stays.
  * The quoted agent output of chapters 7 and 8 is a real artifact and is not changed.
  * The source is focus-kit `e7607c5`, already pushed. The kit was reinstalled at that commit during /propose: in this book (staged, the author's commit), in the clinic (`3f0b47c`) and in the CLAHub fork (`f72e964`, branch `book`), each a commit of its own, not yet pushed. /apply does not reinstall it again.
* Documents: docs/03 gained the term unit of work (/propose wrote it). docs/06 line `propose` kept its slug; /propose changed its description to "Chapter 10: /propose, one page, reading it before /apply, and splitting what does not fit". docs/00 §Contents already names chapter 10 "`/propose`, one page", unchanged. docs/03 unchanged. The page's What happened records the exercise answers for the `exercise-answers` appendix.

**Out of scope.**

* `/apply` on `skeleton` and the clinic's commit and tag: chapter 11.
* A branch or worktree per delivery: Part IV; the clinic is trunk.
* Changing the kit: the unit of work and "read the page before `/apply`" are written in the focus-kit repository by the author, before this /apply; this delivery only cites them.
* A usage measurement of the book's own runs: `/usage` as the author reads it is the source.
* The whole-milestone review: chapter 12.

**Done when.**

* [x] `usage.txt` saved (by /propose, from the author's file).
* [x] The kit reinstalled at `e7607c5` in the book, the clinic and the CLAHub fork.
* [x] Chapters 6, 9 and 10 cite focus-kit `e7607c5` for the unit of work.
* [x] The author pushed the clinic's `3f0b47c` before the run's commit is quoted, so the link check can open it.
* [x] Chapters 6 and 9 corrected in both editions; no other sentence of theirs changed.
* [x] Run recorded in `work/done/propose-run/`; every answer is a brief section word for word or its rule.
* [x] The author reviewed the page; every correction is a recorded turn; `skeleton.diff` matches `skeleton-first.md` against the clinic's `work/skeleton.md`.
* [x] The clinic holds `work/skeleton.md` and `skeleton` at `[>]`, uncommitted and unstaged; nothing else changed there.
* [x] Both editions written, same file name and heading structure, opening with the Objective in at most three sentences.
* [x] No filler and nothing useful cut; every number cites its source; no draft marker.
* [x] Every excerpt in the English edition matches its source byte for byte (brief, questions, first page, requests, diffs, `git show 53109f3 -- docs/06-Queue.md`); translated in Portuguese with the note.
* [ ] `make verify` green.
* [x] `make book` builds; both PDF paths given to the author.
* [x] docs/06 line `[x]`, page in `work/done/`, staged, commit message suggested.

The unticked item is the author's: `make verify` is red only on the four links to `work/done/propose-run/` on `main` (`README.md` and `usage.txt`, in both editions), which answer once this commit is pushed.

**What happened.**

The run, 2026-09-28: Claude Code 2.1.283, model `claude-opus-5-5`, one headless session of two turns in `acceptEdits`, no call denied; the review in a second session. Everything is in `propose-run/README.md`.

Diverged from the plan:

* The review did not run as a `--continue` turn of the run's session. /apply stopped after turn 2 and showed the author the page with a list of the holes it found against the clinic's documents; the author checked them, opened Claude Code in the clinic, interactive and in a fresh session, and typed `/propose skeleton` with the list after the slug. The author chose to record it as it ran (`review.md`, `turn-3.txt`), and the chapter says so in two sentences: it worked because `/propose` reads `work/` first; the fresh session lacked the first conversation's reasoning.
* Who found the holes: the agent running this /apply, not the author alone. The author chose to say it plainly, in the first person, in section 4.
* The interactive session offered a question form, so the agent asked the author about the manifest and the screenshot with options; the author took the recommended option in each. The chapter quotes the two chosen labels; the form itself is kept whole in `review.md` and `turn-3.txt`.
* The request carries no backticks, as the author pasted it; it is quoted as sent.
* The review took the manifest out of `skeleton` and added the line `install` to the clinic's milestone 2, so the clinic's docs/06 changed beyond the mark (`queue.diff`). The author chose one sentence in section 5 that points to it, after the `53109f3` example.
* The answer of turn 2 is the brief's rule alone: the agent read the slug from the command, and the brief answers none of its questions.
* The kit's new ending is quoted as a whole block of turn 2's reply, "Before `/apply`, read the page and question it", in section 3.
* Files added to the record beyond the Contract's list: `turn-3.txt` (the review's transcript) and `queue.diff`. `skeleton.diff` was made with `diff -u` and labels `a/work/skeleton.md` and `b/work/skeleton.md`; it matches `skeleton-first.md` against the clinic's `work/skeleton.md` after the review.
* The Portuguese edition translates every prose artifact (the brief, the round, the answer, the ending, the first page with its code kept, the request) with the note; the two diffs stay as they ran, each followed by a sentence giving its content in Portuguese. "your call" and "sem interface" stay as in chapters 7 and 8.
* `make book` printed the known warning `Ignored user-select: none`, as in earlier chapters.

After the first staging, the author's review of the chapter found section 2 unclear and asked it to answer six questions, as a teacher would: where the slugs come from, what if the line does not exist, why not do it all in one step, how the agent knows what to do, how you correct the page, and why not use the host's own plan mode. Section 2 now opens with what a delivery and a page are (the author's framing: one line of the queue, by its slug, becomes one page a person can review, holding what to do, what not to do and, after `/apply`, how it was done), then answers each question under its own H3, then keeps the Contract and the unit of work as the last two H3s. Sources: the answers come from `propose/SKILL.md` at `e7607c5` and the clinic's docs/05; plan mode is quoted from Claude Code's "Common workflows" page, a new note `[^claude-code-plan-mode]`, the one source outside the Contract's list, taken because a comparison with a tool must quote the tool. The chapter names only Claude Code's plan mode, since it is the host of the runs; it makes no claim about other hosts. The first key point now names the slug and the missing line. In both editions.

Proof: `make verify` green up to the link check, which fails only on the four links above; disclosure scan green alone. Every English excerpt was compared by script with its source: `brief.md`, turn 1 and the ending in `questions.md`, `skeleton-first.md`, the request in `review.md`, `skeleton.diff`, and `git show 53109f3 -- docs/06-Queue.md`.

Chapters 6 and 9: one sentence each replaced, in both editions, plus the note `[^focus-kit-unit-of-work]`; nothing else changed.

Exercise answers, for the `exercise-answers` appendix:

* 10.1: the pages will differ in wording and in the "your call" choices; in this run those were the health page with its three states, the migration runner and `schema_migration` in `skeleton`, a manifest with no service worker, the pixel baseline, Node 24, `npm run dev`, `Result` kept local, and `data/clinic.sqlite`.
* 10.2: the holes of this chapter's review are a model: a check with no error behind it, content nobody specified (the icons), a proof tied to one machine, and a Contract that leaves a test's input unstated.
* 10.3: `/propose` should say the two do not fit one page, write `book-appointment` only, and leave `cancel-appointment` as its own line after it, where the queue already has it.

