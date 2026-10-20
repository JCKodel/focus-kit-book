# m22-records-commits

**Objective.** The author can read on the pages of `ch08-13-17-next-line`, `ch20-merge-and-marks` and `ch08-13-20-default-review` which commit holds each of `ch08-13-20-default-review`'s chapter sentences, with each page's numbers and staging items true of the commit that holds its lines, and chapter 8 :30 placed under the section it sits in, "Install" / "Instalação".

**Behaviour.**

* Reading the Proof of `work/done/ch08-13-17-next-line.md`, the author finds that its commit `d740cbb` also holds `ch08-13-20-default-review`'s sentences in chapter 8 (:30) and chapter 13 (:259), one replaced line each per edition, so the commit's stat of the eight chapter files is 14 insertions and 8 deletions against this delivery's 10 and 4 (m23-review S1).
* Reading its Divergences, the author finds "nothing else in the four chapters changed" said of this delivery's text, with the two sentences its commit also carries named as `ch08-13-20-default-review`'s (S1).
* Reading the Proof of `work/done/ch20-merge-and-marks.md`, the author finds, after its three hunks, that its commit `9c2e490` holds four hunks per edition: `ch08-13-20-default-review`'s :35 is the fourth, and its :11 and :86 sit inside the first and last; 7 insertions and 6 deletions per edition (S1).
* Reading the Proof of `work/done/ch08-13-20-default-review.md`, the author finds that its commit `53a82de` holds only this page and its docs/06 hunk, its chapter 8 and 13 sentences being in `d740cbb` and its chapter 20 sentences in `9c2e490`, both editions (S1).
* Reading that page's Contract item 1, the author finds chapter 8 :30 under "Install" / "Instalação", the section it sits in (both editions, :12 to :34), not "What the install never touches, and how to update" (S7).
* Reading the staging items of `ch08-13-17-next-line` and `ch08-13-20-default-review`, the author finds what each commit staged, not "only this delivery's paths".
* Edges: each new sentence says only what `git show` of the named commit shows, never why the lines landed there nor that the Proof knew it at the time. No item is unticked. No Objective, Behaviour, Contract wording (but item 1's section name) or ```commit block changes. Nothing else on the three pages changes, and no chapter.

**Contract.** The commits, checked at define time:

* `git show d740cbb --format= --shortstat -- book/`: 8 files, 14 insertions, 8 deletions; per edition 2 and 1 in chapters 8, 13 and 17, 1 and 1 in chapter 23. The lines beyond this delivery's are the chapter 8 sentence "By default you read what it wrote and then commit it, ..." / "Por padrão você lê o que ela escreveu e então faz o commit, ..." and the chapter 13 sentence "... a person reads the change, by default the diff ..." / "... uma pessoa lê a mudança, por padrão o diff ...".
* `git show 9c2e490 --format= --shortstat -- book/`: 2 files, 14 insertions, 12 deletions; four `@@` hunks per edition (starting at :5, :32, :58, :83 on the new side). `ch08-13-20-default-review`'s lines: "a second person who reviews, by default before the merge" (:11, first hunk), "By default the reviewer the kit assumes is whoever decides the merge" (:35, second hunk), the pull request key point's "whoever decides the merge" (:86, last hunk); pt the same.
* `git show 53a82de --format= --stat`: 2 files, `docs/06-Queue.md` (its `[x]`) and `work/done/ch08-13-20-default-review.md`; no chapter.
* Chapter 8's headings, both editions: `## Install` / `## Instalação` at :12, the next at :35.

Exact replacements, each found by its section and quoted text (line numbers are today's, at `aa828d6`, and only a guide); the rest of each page untouched:

1. `work/done/ch08-13-17-next-line.md`, Done when, :73, "Only this delivery's paths staged (the driver's in this batch); the page moved to `work/done/` and its commit message suggested.", to:

   > * [x] This delivery's paths staged by the batch's driver, whose commit `d740cbb` also holds `ch08-13-20-default-review`'s sentences in chapters 8 and 13 (Proof); the page moved to `work/done/` and its commit message suggested.

2. Same page, Proof, :78, after "; 10 insertions and 4 deletions in all.", add:

   > Its commit `d740cbb` also holds `ch08-13-20-default-review`'s sentences in chapter 8 (:30) and chapter 13 (:259), one replaced line in each per edition, so the commit's stat of the eight files reads 2 insertions and 1 deletion in each of chapters 8 and 13, per edition, 14 insertions and 8 deletions in all.

3. Same page, Divergences, :82, "None: the Contract's wording is in place word for word, and nothing else in the four chapters changed.", to:

   > **Divergences.** None in this delivery's text: the Contract's wording is in place word for word, and this delivery changed nothing else in the four chapters. Its commit also carries `ch08-13-20-default-review`'s sentences in chapters 8 and 13, which are that delivery's (Proof).

4. `work/done/ch20-merge-and-marks.md`, Proof, :67, after "the board key point (line 87), same lines in both editions.", add:

   > Its commit `9c2e490` holds four hunks per edition, 7 insertions and 6 deletions each: these three and `ch08-13-20-default-review`'s sentence at :35 as the fourth, with that delivery's :11 and :86 inside the first and last.

5. `work/done/ch08-13-20-default-review.md`, Contract, item 1, :16, "section \"What the install never touches, and how to update\" / \"O que a instalação nunca toca, e como atualizar\"" becomes "section \"Install\" / \"Instalação\""; the rest of the item stays.

6. Same page, Done when, :70, "Only this delivery's paths staged; the page moved to `work/done/` and its commit message suggested.", to:

   > * [x] The page moved to `work/done/` and its commit message suggested; its commit `53a82de` holds the page and its docs/06 hunk, and its chapter sentences were committed with `d740cbb` and `9c2e490` (Proof).

7. Same page, Proof, after its first bullet (:74, "The five sentences, found by their words, ..."), a new bullet:

   > * The commit `53a82de` holds only this page and its docs/06 hunk: the sentences in chapters 8 and 13 are in `d740cbb` (`ch08-13-17-next-line`), those in chapter 20 in `9c2e490` (`ch20-merge-and-marks`), both editions.

* **Terms:** delivery, record, Proof, as docs/03 has them; no new term, no docs/03 row.
* **Sources:** m23-review's candidates S1 and S7 (`work/done/m23-review.md`, Findings table); `git show` of `d740cbb`, `9c2e490`, `53a82de`.
* **Cases, code examples:** none. No chapter changes.
* **Neighbour:** `m23-records-proof` (`[>]`, before this line in the queue) edits `work/done/ch20-merge-and-marks.md` first, at Done when :47 and :48, Proof :71, Divergences :75 and :76 and Decisions :83; it leaves :67, so replacement 4's anchor holds after it. `m23-records-crossrefs` touches none of the three pages.

**States.** Inapplicable: record pages, no screen.

**Visual reference.** Inapplicable: no screen, no chapter.

**Out of scope.**

* The ```commit blocks of the three pages, and the messages of `d740cbb`, `9c2e490` and `53a82de`: each block is the suggestion its /apply made (docs/05 §3), and history keeps the messages; the Proofs now say what each commit holds.
* `ch08-13-17-next-line` Done when :67 and :69 and `ch08-13-20-default-review` Done when :66: claims about the delivery's own diff, true as written.
* `ch08-13-20-default-review`'s Proof line numbers (:260, :11, :35, :86): true of the chapters when it ran.
* `ch20-merge-and-marks` Done when :48, Proof :71 and the rest `m23-records-proof` rewrites; its new "only this delivery's files staged" is true at file level and is that line's.
* S7's `docs05-dependency-merged` half: the review marked it weak.
* Any chapter, docs/03, docs/05, docs/06.

**Decisions from the documents.**

* Scope is S1 and S7 as `work/done/m23-review.md` gives them, the places they cite and each page's Proof, which the queue line names.
* Items stay ticked and are reworded to what is recorded: `m22-batch-proof`'s precedent, followed by `m23-records-proof`.
* Records edited in place, the change named here, not in them: the batch rule that a delivery naming a record may edit it.
* No chapter is touched, so the book's Done when items are inapplicable (docs/05 §3).

**Decisions taken alone** (the batch's driver asked for recommended answers; correct them in the review).

* The new sentences are added after what each Proof recorded, not rewritten into it: the Proofs were true of the working tree they measured, and the commit facts come after.
* Siblings included, the staging items that would go stale and that no other line edits: `ch08-13-17-next-line` :73 and `ch08-13-20-default-review` :70.
* Commit hashes go in the records, which already cite them; no chapter gets one.
* The queue line's wording needs no change.

**Done when.**

* [ ] The 7 replacements above made word for word, each found by its section and quoted text, and nothing else in the three pages changed (`git diff` of each shows only those lines).
* [ ] The Contract's git checks rechecked at /apply: the three `--shortstat`/`--stat` results and chapter 8's headings as given.
* [ ] A search of the three pages finds no "What the install never touches" and no "Only this delivery's paths staged"; `ch20-merge-and-marks`'s Proof still says "three hunks" for its own.
* [ ] No em dash; no private case, so OD-3 approval is inapplicable.
* [ ] `make verify` green after the last edit.
* [ ] Delivery review as docs/05 §5 says: a read-only Opus agent with the session's advisor reads the diff of the three pages and this page against this page, docs/04 and the three commits; its findings fixed or recorded.
* [ ] Page in `work/done/`, the commit suggested in a `commit` block; the line's `[x]` and the staging are the batch driver's steps.
