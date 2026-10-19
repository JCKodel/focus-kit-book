# m21-git-slot-default

**Objective.** After chapters 6, 8, 13, 18 and 19 a reader meets no sentence that puts the person's reading before the commit as the only form: each such sentence says it is the default, so it stays true under the Git slot's commit form that chapters 7 and 13 teach (the agent commits by the slot's word, which counts as the asking; the person reviews the commit); both editions, the least change.

**Behaviour.**

* Reading chapter 6's rule "The agent stages and suggests the commit message", the reader learns that the check on the product is a person reading each change, by default before it enters the history (chapter 13).
* Reading chapter 8's install, the reader learns that the install does not commit and that they read and commit it themselves, as by default with every change the agent makes.
* Reading chapter 13's opening, the reader learns that by default they use what `/apply` built, review the staged change and then commit it, themselves or by asking the agent; reading "The delivery review", that with no delivery reviewer their own review stays the only one; reading "The commit is the human review", that by default they use the delivery, read the staged diff, then commit.
* Reading chapter 18's "Commits and the history", the reader learns that by default the agent stages and suggests the message, and that their use and reading before the commit are their review.
* Reading chapter 19, the reader learns that by default the commit comes after using the delivery and reading what is staged, in one folder, on a worktree's branch, after a partial commit and for each step they ask for.
* Every other sentence of the five chapters stays; no chapter gains a pointer to chapter 7 or repeats its paragraph on the slot.
* Fails if: a changed sentence is false under either form; "by default" lands on a sentence none of whose steps needs it (the never-on-its-own rule, chapter 19 line 194's push, conflict and worktree clause); a chapter names this repository's own Git choice; it says the form is new, a version or a date; it narrates a run; a title changes.

**Contract.**

The same sentences in both editions, `book/en/` and `book/pt/`; "by default" is "por padrão" in Portuguese, as chapter 13 line 165 and chapter 23 line 64 already write it. Wording is /apply's within the sense below; line numbers are both editions'.

Chapter 6, `06-birth-of-focus-kit.md`, "Each rule and its failure":

* Line 66 (G1): "a person reading each change before it enters the history (chapter 13)" becomes "a person reading each change, by default before it enters the history (chapter 13)".

Chapter 8, `08-install-and-hosts.md`, "Install":

* Line 30 (G5): "as with every change the agent makes (chapter 13)" becomes "as by default with every change the agent makes (chapter 13)". "commit it yourself" stays: the install comes before docs/05 and its Git slot exist.

Chapter 13, `13-apply.md` (G2):

* Opening, line 4: "You can then use what `/apply` built and review the staged change ..." becomes "You can then, by default, use what `/apply` built and review the staged change ..."; the rest stays.
* "The delivery review", line 72: "and your commit stays the only review" becomes "and your review stays the only one" (pt "e a sua revisão continua sendo a única"), true whether the person reviews before the commit or the commit after it.
* "The commit is the human review", line 217: "Once you have used the delivery, read the staged diff, then commit:" becomes "By default, once you have used the delivery, read the staged diff, then commit:".
* Stays: line 89 (every step it names still comes after the delivery review, under both forms), lines 164, 165, 210, 213, 215, as `ch13-19-commit-by-slot` wrote them.

Chapter 18, `18-git-essentials.md`, "Commits and the history":

* Line 65 (G3): "The agent stages that change and suggests the message; ..." opens with "By default"; the rest stays. Line 190 keeps the chapter's one pointer to chapter 7 and the slot's form.

Chapter 19, `19-worktrees.md` (K1, G4):

* "Two sessions in one folder", line 38: "after you have used it and read what it staged" becomes "by default after you have used it and read what it staged".
* "Worktrees in the kit", line 185: "You use the delivery, review and commit on the branch, ..." opens with "By default".
* Same section, line 189: "That commit is the one exception ..." opens with "By default", which covers both its clauses, the exception and "the commit that completes the delivery still comes after you use the whole of it".
* Same section, line 196: "Each step comes after your reading" opens with "By default", as K1 prescribes: the marker governs the commit and merge clauses; the push clause holds under both forms and is not made false by it.
* Stays: line 194, which names the slot's form for commit and merge and keeps push, the conflict and the worktree yours to ask for; line 195.

Terms of docs/03 used: slot, trunk, worktree; the Git slot's commit form as chapter 7 teaches it. No new docs/03 row. No number, no source, no case, no lending library example added.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no visual change.

**Out of scope.**

* Chapter 20's "reviews the staged diff and commits it" and "whoever merges is the reviewer": `ch20-roles-and-points` (G6, G7).
* Chapter 8's step 4 outcomes: `ch08-step4-outcomes`, after this line.
* Chapter 7's paragraph on the two forms and chapter 13's and 19's slot clauses: done (`ch07-review-git-slots`, `ch13-19-commit-by-slot`).
* Chapter 13 line 89, marked weak by the checker: it holds under both forms (Decisions).
* This repository's own Git choice: a project's answer, not what the chapters teach (`work/done/kit-2026-10-19.md`, ADR-0017).
* docs/03, docs/05, docs/06, AGENTS.md: no edit; the queue line is the driver's.

**Decisions from the documents.**

* Scope is exactly the sentences m21-review's K1 and G1 to G5 name, the author's confirmed findings (`work/done/m21-review.md`, Author's answers and Findings).
* "By default" / "por padrão" is the marker, as the queue line says and as chapter 13 line 165 and chapter 23 line 64 already use it (`work/done/ch13-19-commit-by-slot.md`, /apply decisions).
* No new pointer to chapter 7: each chapter that teaches the slot already has one, and chapters 6 and 8 point to chapter 13, which holds the clause (docs/04, "Chapter pointers"; `ch13-19-commit-by-slot`).
* No before/after, version or date (AGENTS.md; the driver's rules).

**Decisions taken alone.**

* Chapter 13 line 72 takes no "by default": it does not order reading and commit, it calls the commit the review; "your review stays the only one" is true under both forms and is the least change.
* Chapter 13 line 89 (the checker's weak mark) stays: its claim is that use, review and commit come after the delivery review, which holds when the agent commits by the slot's word too.
* Chapter 13 line 4 places "by default" after "You can then" rather than first, so the sentence still opens with what the reader can do.
* Chapter 8 line 30 keeps "commit it yourself": the install runs before any Git slot exists; only the comparison "as with every change" gains "by default".
* Chapter 18 line 65 and chapter 19 lines 185, 189 and 196 take "By default" at the sentence's head, one per sentence, rather than inside a clause; chapter 19 line 189's two clauses share it.
* Chapter 6's bullet is the kit's rule as SETUP.md §2 lists it today, so it is changed like any other sentence; `ch13-19-commit-by-slot` had left it as Ninjobs history, and the author's confirmation of G1 overrides that.

**Done when.**

* [x] Both editions written, the same sentences changed in each, Portuguese read as Portuguese; each chapter opens with its value as before, no filler and nothing useful cut; no number added.
* [x] Every sentence the Contract names reads true under both Git slot forms; every sentence it lists as staying is unchanged.
* [x] `grep -c -i "by default"` rises by exactly 1 in chapters 6, 8 and 18, 2 in chapter 13 and 4 in chapter 19 (en); `grep -c -i "por padrão"` by the same in pt.
* [x] `grep -n "your commit stays the only review" book/en/13-apply.md` and `grep -n "o seu commit continua sendo a única revisão" book/pt/13-apply.md` find nothing.
* [x] `grep -c "07-the-documents"` on the five chapter files, both editions, is unchanged.
* [x] No added line holds "no longer", "now offers", "não mais", "agora oferece", "2026.10" or an em dash; no narrated run.
* [x] Delivery review as docs/05 §5 says.
* [x] `make verify` green; `make book` builds both editions and both PDF paths are reported (the driver runs `make book` once for the batch).
* [x] Only this delivery's paths and its hunk of docs/06 staged (staging is the driver's); the page moved to `work/done/` and its commit message suggested.

**Proof.**

* `grep -c -i "by default"` (en) and `grep -c -i "por padrão"` (pt), before and after: chapter 6 0 to 1, chapter 8 0 to 1, chapter 13 1 to 3, chapter 18 0 to 1, chapter 19 1 to 5, the same in both editions.
* The two `grep -n` on chapter 13's old sentence find nothing in either edition.
* `grep -c "07-the-documents"`: 0, 0, 2, 1, 2 in chapters 6, 8, 13, 18, 19, before and after, both editions.
* `git diff HEAD` of the ten chapter files: one line changed per Contract sentence, 10 per edition, no title touched; no added line holds an em dash, "no longer", "now offers", "não mais", "agora oferece" or "2026.10".
* `make verify` green. `make book` is run once by the driver for the batch; staging and the docs/06 hunk are the driver's.

**Divergences.** None: every sentence takes the Contract's wording; the Portuguese ones are "por padrão" at the same place.

**Delivery review.** A read-only Opus agent read the diff of the ten chapter files against this page, docs/04 and chapter 7's two forms: nothing breaks the page or docs/04; counts, stayed lines and Portuguese confirmed. Three nits, left as the Contract wrote them: chapter 8 line 30 could set "by default" off with commas; chapter 19 line 189's head "By default" could be read as qualifying the exception itself; chapter 13 line 4 pairs "can" with "by default". Each follows a decision above, and none makes a sentence false.

```commit
docs(m21-git-slot-default): reading before the commit is the default

- chapters 6, 8, 18: the reading before the commit says "by default"
- chapter 13: opening and "The commit is the human review" say it too
- chapter 13: with no delivery reviewer, your review stays the only one
- chapter 19: one folder, the worktree's branch, the partial commit, each step

work/done/m21-git-slot-default.md
```
