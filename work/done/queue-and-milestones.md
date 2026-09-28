# queue-and-milestones

**Objective.** After chapter 9 the reader can read a queue, say what each mark means and which command changes it, write a milestone paragraph a person can check, order a milestone's lines, and add or change a line by conversation.

**Behaviour.**

* The reader can say what docs/06 holds: milestones, each with a paragraph saying what is true when it closes, and under each one line per delivery, in order: a mark, a slug, what it delivers in one line.
* The reader can say what the slug is for: the name of the delivery's page, `work/<slug>.md`, and of the command's argument, `/propose <slug>`.
* The reader can name the three marks and who moves each: `[ ]` not yet defined; `[>]` defined, `/propose` wrote the page; `[x]` done, `/apply` moved the page to `work/done/`. A line never leaves the queue; it changes mark, so the queue is also the history.
* The reader knows that the line is one line: the reasoning goes on the page, and a line that grows into a paragraph is a decision in the wrong place (the Ninjobs numbers).
* The reader can write a milestone paragraph as a test: sentences a person can check against the product, not a list of lines or a theme.
* The reader can size and order a milestone: three to eight deliveries; the first ones are the skeleton the others stand on (the clinic's `skeleton` creates `npm run verify`); then each line after the lines it needs.
* The reader knows no command owns the queue: a new idea becomes a line by conversation, in any session, where it belongs, and a milestone's paragraph or a line's description changes the same way, with the slug kept. The person reviews the diff, as with every document (chapter 6).

**Contract.**

Chapter 9, `book/en/09-queue-and-milestones.md` and `book/pt/09-queue-and-milestones.md`:

* Title: "The queue and milestones" / "A fila e os marcos".
* Voice: instruction to the reader as "you".
* Sections, in order (headings may be reworded; both editions keep the same structure):
  1. Opening, at most three sentences: the Objective.
  2. The line. What docs/06 holds and the shape of a line, `[ ] <slug>    <what it delivers, one line>`, from the kit. What the slug names. Point to the clinic's queue in chapter 7 and CLAHub's in chapter 8 by link (`07-brainstorm.md`, `08-analyze.md`, and the files at their chapter tags); no excerpt of them is repeated. Then the Ninjobs passage (below).
  3. The marks. The three marks, one line each, and who moves each: `[ ]` to `[>]` is `/propose` (chapter 10), `[>]` to `[x]` is `/apply` (chapter 11), one sentence each, no more. A line never leaves; the queue is the history. With a branch or a worktree per delivery, or here on trunk, the page and the build land in the same commit, so `[>]` lives in the working tree between the two commands: it is how a fresh session running `/apply` knows the page exists. Say it in one or two sentences, without teaching git (Part IV).
  4. Milestones. The paragraph says what is true when the milestone closes, in sentences a person can check; the clinic's milestone 1 paragraph, quoted in chapter 7, is the example, pointed to, not repeated. Size: three to eight deliveries (the kit's rule for the first milestone, and a good size for any). Order: the skeleton first, then each line after what it stands on. Closing a milestone is chapter 12, one sentence.
  5. Changing the queue. No command owns it; lines come from an idea in any session, from a milestone's review (chapter 12, one sentence) or from issues (chapter 8, one sentence). The example is this book's own queue: the diff of docs/06 at commit `59b5e10`, quoted whole (English in both editions, translated with a note in Portuguese, as chapter 6 does). Context before it: after chapters 7 and 8 were done, the author asked for the two choices to be defined in chapter 6, so both could point back. One sentence after it on what to see: the line `two-choices` entered in the middle of M3, where it belongs, already `[x]` because page and build landed in one commit; in the same commit, M4's paragraph and the `errors-and-slices` description changed their words and kept the slug. The change was asked of the agent, never made by hand.
  6. Key points, at most five.
  7. Exercises (below).
* The Ninjobs passage, in substance, word for word in meaning (the wording may be adjusted to the chapter's prose, not the framing): "The kit asks for one line, and the reasoning goes on the page. On Ninjobs the author let the lines grow: its queue held 102 deliveries in 1,711 lines, 1,052 of them continuations of a line, decisions that belonged on the pages." It says the author let it grow, not that the method failed. No Ninjobs slug, heading, milestone name or continuation text is quoted or paraphrased; only the three numbers.
* Numbers, and only these: three (marks); three to eight (deliveries in a milestone); 102, 1,711 and 1,052 (Ninjobs). Counted by the author for this page, in Ninjobs' docs/06 at its last change, commit `225c59e` of 2026-09-22: 1,711 lines by `wc -l`; 102 lines inside the code fences starting with a mark; 1,052 non-empty lines inside the fences that start with no mark. /apply cannot recount them and does not change them.
* docs/03 terms used: queue, mark, milestone, delivery, page, command, fresh session, verify, guided project, brownfield project. No new term.
* Sources (`[^key]`, same keys in both editions):
  * `[^focus-kit-documents]`: the existing note of chapter 6, `SETUP.md` at `26e5e1e4c8fcc6e059075a51db8cad5ed2028f2b`, for the shape of the queue, the marks, "a line never leaves" and "no command owns it". The queue text and "three to eight" are the same at `fa1450e`. Footnotes end their chapter, so chapter 9 repeats the note with the same key.
  * `[^focus-kit-brainstorm]` (new): `SETUP.md` at the same commit, §3.1 `/brainstorm`, item 6, for "three to eight deliveries" and "the first ones are the skeleton".
  * `[^ninjobs-queue]` (new): "Ninjobs, a private repository, its docs/06 at its last change, 2026-09-22, counted by the author: lines with `wc -l`, deliveries as the lines inside the code blocks that start with a mark, continuations as the other non-empty lines inside them." Written like chapter 4's `[^ninjobs-adr-0022]`.
  * `[^book-two-choices]` (new): `https://github.com/JCKodel/focus-kit-book/commit/59b5e10fb59bde04b2cd444b38efe50414733446`, on `origin/main`.
* Cases: Ninjobs, numbers only; this book. No Case A or B.
* Exercises, on the clinic at `book-v1/brainstorm`, by conversation with the agent, never by hand; the clinic gets no commit and no tag from this chapter:
  * 9.1 For each sentence of milestone 1's paragraph, name the line that makes it true. If a sentence has no line, or a line serves no sentence, ask the agent to fix the queue and review the diff.
  * 9.2 Bring one idea for the clinic that the brief does not exclude. Ask the agent to add it: a line in the milestone where it belongs, or a new milestone with its paragraph. Check the diff: one line, a new slug, `[ ]`, no reasoning in the line.
  * 9.3 Ask the agent to move `deploy` back to milestone 1, then read the paragraphs of both milestones: what else had to change, and did the agent change it?
* Documents: docs/00 §Contents already names chapter 9 "The queue and milestones", unchanged. docs/03 unchanged. /apply marks the line `[x]` and adds the exercise answers to what the `exercise-answers` appendix will need (the page's What happened records them).

**Out of scope.**

* The `[?]` mark and extra marks: ADR-0013 and chapter 21 (customizing).
* Splitting a delivery that does not fit one page: chapter 10.
* The whole-milestone review and its findings: chapter 12.
* Branches, worktrees and the commit: Part IV.
* A recorded run or a tag in the clinic: the chapter reads queues that exist; chapters 10 and 11 move marks for real.
* Re-quoting the clinic's or CLAHub's queue: chapters 7 and 8 show them.

**Done when.**

* [x] Both editions written, same file name and heading structure, opening with the Objective in at most three sentences.
* [x] No filler and nothing useful cut; every number cites its source; no draft marker.
* [x] The two-choices diff in the English edition matches `git show 59b5e10 -- docs/06-Queue.md` byte for byte (the hunks, from `diff --git` on).
* [x] No Ninjobs slug, heading or continuation text in either edition; `make scan` green.
* [x] The author approved the Ninjobs passage in both editions (the two-choices review struck a Ninjobs sentence that read as a flaw of the method).
* [x] `make verify` green.
* [x] `make book` builds; both PDF paths given to the author.
* [x] docs/06 line `[x]`, page in `work/done/`, staged, commit message suggested.

**What happened.**

* **The "what to see" sentence names three changes, not two.** The diff at `59b5e10` also changes the `four-pieces` description, which lost "(the Ninjobs lesson of chapter 4)". A sentence naming only M4's paragraph and `errors-and-slices` would be false about the artifact shown, so it reads "M4's paragraph and the descriptions of `errors-and-slices` and `four-pieces`"; the reason the parenthetical went is not told.
* **The diff in Portuguese.** It stays in English, as the page asks and as chapter 7 does with its diff, and a sentence before it translates the new line and the M4 changes. The English diff matches `git show 59b5e10 -- docs/06-Queue.md` from `diff --git` on, checked with `diff` (the Portuguese block is the same bytes).
* **Git sentence.** "With trunk, a branch or a worktree", one sentence, plus one pointing to Part IV.
* **Slug.** Defined in the chapter as the delivery's name, the name of its page and the commands' argument; docs/03 already carries it as the identifier of delivery and page, so no new row.
* **Ninjobs passage approved by the author in both editions**, as written: "On Ninjobs I let the lines grow", in the first person per docs/04 §Voice. Numbers as counted for the page, not recounted.
* **Proof.** `make verify` green; `make book` builds `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf` (the `user-select` warnings were already there).
* **Exercise answers**, for the `exercise-answers` appendix: 9.1, the paragraph's clauses map to `professionals` (register professionals), `weekly-hours` (their weekly hours), `book-appointment` (book a free slot), `cancel-appointment` (cancel up to 24 hours before); `skeleton` and `clinic-setup` serve no sentence: `skeleton` is what the others stand on, and `clinic-setup` (the owner signs in) is a sentence the paragraph could gain. 9.2, any idea the brief does not exclude; the diff holds one new line with a new slug and `[ ]`, or a new milestone with a checkable paragraph, and nothing else. 9.3, moving `deploy` to milestone 1 means M1's paragraph gains "the app runs outside the developer's machine with no paid service" and M2's loses it; the answer is whether the agent changed both paragraphs, or only moved the line.
* **Documents.** docs/00 and docs/03 unchanged; docs/06 marks the line `[x]`.
