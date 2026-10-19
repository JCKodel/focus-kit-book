# ch13-19-commit-by-slot

**Objective.** After chapters 13, 18, 19 and 23 a reader can say that the agent never commits or merges on its own in any git strategy, that a Git slot which says it commits, and merges, by the slot's word is the asking, the person then reading and reviewing the commit after it lands, and why a person still answers for every delivery under either form; every sentence on who commits stays true under both forms with the least change, both editions.

**Behaviour.**

* Reading chapter 13's "Why it stops at the stage", the reader learns that `/apply` never commits or merges on its own in any git strategy, and that a Git slot saying the agent commits by its word counts as the asking, the person then reviewing the commit (chapter 7).
* Reading chapter 13's "The commit is the human review", the reader learns that the person decides the commit by asking for it or once, in the Git slot, and that under the slot's form the person reads the commit after it lands and reverts it in one step when it is wrong, so no delivery stands unread by a person either way; an agent that commits on its own still skips that reader.
* Reading chapter 18's rule for the three strategies and its Key point, the reader learns that the person decides each commit and merge, by asking or once in the Git slot, and never the agent on its own.
* Reading chapter 19, the reader learns the same for commit and merge, while push, resolving a conflict and removing a worktree stay the person's to ask for in every case; and that agents committing a batch before the person read it costs the same four things whether they did it on their own, which leaves the method, or by the Git slot's word.
* Reading chapter 23's roles, the reader learns that a person always decides each commit and merge, by asking or by the Git slot's word, and reviews the delivery before the commit or the commit after it lands.
* Chapter 7 is pointed to at most once per chapter; no chapter repeats chapter 7's paragraph; every other sentence of the four chapters stays.
* Fails if: a changed sentence is false under either form; "whatever the git strategy" or "as in every git strategy" remains the reason no commit happens without a person; the slot's word covers push, conflict resolution or worktree removal; a chapter names this repository's own Git choice; it says the form is new, a version, a date or how the slot read before; it names a host's command; it narrates a run; it points to chapter 7 twice; a title changes.

**Contract.**

The same passages in both editions, `book/en/` and `book/pt/`. Wording is /apply's within the sense below; the Portuguese reuses chapter 7's "pela palavra do slot, que vale como o pedido; a pessoa revisa o commit".

Chapter 13, `13-apply.md`:

* §"Why it stops at the stage", line 164: "never commits and never merges on its own" stays, in every git strategy, and gains one clause: a Git slot that says the agent commits, and merges, by the slot's word is the asking, and the person reviews the commit ([chapter 7](07-the-documents.md)), the chapter's one pointer to chapter 7. Line 165 stays and reads as the default; /apply may put the clause there instead.
* §"The commit is the human review", line 211: "the person uses the delivery, reads the diff and decides the commit" gains the other form in a clause: or, by the Git slot's word, the agent commits and the person uses the delivery and reads the commit after it.
* Same section, line 213, the first reason: reframed. The bold lead no longer says nothing reaches the history unread; it says no delivery stands unread by a person (pt "Nenhuma entrega fica sem ser lida por uma pessoa"), and the reason gives both forms: a commit the person makes says they read the change and accept it; under the slot's form the person reads the commit after it lands and reverts it in one step if it is wrong; an agent that commits on its own skips the only reader who can say the build is what was wanted.
* Same section, line 215: "the commit, whoever types it, is where that answer is given" becomes the commit or, under the slot's form, the review of the commit.
* Key points, line 270: "and then commit it, yourself or by asking the agent" gains "or review the commit the Git slot let it make".
* Stays: the title ("never commit on its own" holds, the slot's word being the asking), the opening (lines 3 and 4, which describe the reader's default steps), "The problem" (line 13), the kit quote (line 166, still exact against the kit's process document), line 167, the automation bias paragraph (lines 201 to 207, true under both forms), line 214.

Chapter 18, `18-git-essentials.md`:

* Line 190: "the person decides each commit and merge, never the agent on its own" gains: by asking, or once in the Git slot, whose word is the asking ([chapter 7](07-the-documents.md)).
* Key point, line 203: "the agent takes one of those steps only when the person names it" gains: or when the Git slot says it commits by its word.

Chapter 19, `19-worktrees.md`:

* Line 194: the list stays; one clause limited to commit and merge: a Git slot that says the agent commits, and merges, by its word is the asking for those two, and you review the commit ([chapter 7](07-the-documents.md)); push, the conflict and the worktree stay yours to ask for. "as in every git strategy" stays only if the sentence stays true with it.
* Line 308: "Letting the agents commit a batch of applies on their own, before you have read them, leaves the method, and it costs four things." becomes: agents committing a batch before you have read it costs four things, whether they do it on their own, which leaves the method, or by the Git slot's word. The four costs (lines 309 to 312) stay: each holds under both forms.
* Key point, line 351: "every commit stays your decision, made by you or asked of the agent after your review" gains: or given once in the Git slot, its commit reviewed after it lands.
* Stays: the opening (line 5, "every commit stays your decision", true under both forms), lines 195 and 196, line 189 (the partial commit), lines 306 and 307.

Chapter 23, `23-adoption.md`:

* Line 63: "a person, always" stays and gains: by asking, or once in the Git slot, whose word is the asking.
* Line 64: "then commits or asks the agent to take that one step, and checks what it did" gains the third case: or the agent commits by the Git slot's word and the person reviews the commit; "the review is the human one either way" becomes "in every case". Its pointer to chapter 13 stays; chapter 23 does not point to chapter 7.
* Line 112, the Key point: "a person always decides each commit and merge after using the delivery and reviewing it" gains: or, by the Git slot's word, reviewing the commit after it lands.

Terms of docs/03 used: slot, trunk, worktree, conflict, automation bias as chapter 24 defines it; the Git slot's commit form is the kit's slot template (`.claude/skills/analyze/references/documents.md`, Git) as chapter 7 teaches it. No new docs/03 row. No number, no footnote, no private case, no lending library example added. Sources cited: none new.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no visual change.

**Out of scope.**

* Chapter 7's explanation of the two forms: done (`work/done/ch07-review-git-slots.md`).
* Chapter 6 line 65: a quoted Ninjobs rule, history (driver).
* Chapter 8 line 30: the install, before docs/05 exists (driver).
* Chapter 20 line 8: states the kit's assumption, true either way; its file is in flight (driver).
* When a team should pick the slot's form: no repository document gives a rule (`work/done/ch07-review-git-slots.md`).
* This repository's own Git choice (it keeps "never commits or merges on its own", `work/done/kit-2026-10-19.md`): a project's answer, not what the chapters teach (ADR-0017).
* docs/03, docs/05, docs/06, AGENTS.md: no edit; `kit-2026-10-19` already wrote them; the queue line is the driver's.

**Decisions from the documents.**

* Scope widened to chapters 13, 18, 19 and 23 with the listed sentences, and chapters 6, 8 and 20 left: the driver's decision, in this delivery and under this slug.
* "Never commits or merges on its own" stays true under the slot's form, because the slot's word is the asking: the kit's slot template (`documents.md`, Git: "by this slot's word, which is the asking; the person reviews the commit").
* The slot's form covers commit and merge only, so chapter 19's push, conflict and worktree stay the person's: the same template names only "commits, and merges".
* Under the slot's form the person reads the commit after it lands, so chapter 13 line 213 is reframed: the driver, from the same template's "the person reviews the commit".
* At most one pointer back to chapter 7 per chapter, and none where a chapter already points to the chapter that holds the detail: the driver; docs/04, "Chapter pointers".
* Portuguese wording from chapter 7: `work/done/ch07-review-git-slots.md`.
* No before/after, version or date, and no host command: AGENTS.md, `work/done/kit-as-it-is.md`, `work/ch15-who-reads.md` decision 1.

**Decisions taken alone.**

* The driver's "194-ish" for chapter 13 is read as the section around line 211 ("The commit is the human review"), lines 211 and 215 beside 213; the automation bias paragraph (lines 201 to 207) stays, true under both forms.
* Chapter 13's Key point (line 270) is added, as the same kind of sentence as chapter 19's line 351, which the driver named; chapter 13's opening (lines 3 and 4) stays, as the reader's default steps.
* Chapter 19's line 308 keeps "leaves the method" for the agents' own commits only, and the four costs are said to hold under the slot's form too: the costs (the index, automation bias, the revert) do not depend on who gave the word.
* Chapter 23 points to no chapter 7: its line 64 already points to chapter 13, which holds the clause and the pointer.
* The page still fits one page: about ten sentences per edition, each a clause or a reframed reason.
* (/apply) "At most once per chapter" is read as at most one new pointer, as the Done when's grep measures: chapters 13 and 19 already pointed to chapter 7 once, for the manuals (13 line 100, 19 line 132), a different detail; each now has two, chapter 18 one, chapter 23 none.
* (/apply) Chapter 13 line 165 and chapter 23 line 64 open with "By default" (pt "Por padrão"), which the Contract allows for 165: without it, "the decision to commit is yours, and it comes after your review" and "`/apply` stages and stops" read false one line after the slot's form is named.
* (/apply) Chapter 13 line 213 drops "in one step" from the revert, which the next bullet's lead already says; "the slot's form" is not used in the text: the chapters say "the slot's word", chapter 7's term.
* (/apply) Chapter 19 line 196 ("Each step comes after your reading") stays, as the Contract lists it: it follows "Ask, and it takes any of them", so it reads as the asked steps; a "By default" there is a proposed queue line, not this page's.

**Proof.** `make verify` green after the last edit. The Done when greps: "Nothing reaches the history unread" and "Nada chega ao histórico sem ser lido" find nothing; "whatever the git strategy" and "qualquer que seja a estratégia de git" remain only on chapter 13 line 164, in the sentence that names the slot's word as the asking; `07-the-documents` counts go 13: 1 to 2, 18: 0 to 1, 19: 1 to 2, 23: 0 to 0, in both editions; no added line holds "no longer", "now offers", "não mais", "agora oferece", "2026.10", "code-review", "ultra" or an em dash. `make book` is the driver's, once for the batch.

**Delivery review.** A read-only agent on Opus read `git diff HEAD` of the eight chapter files against this page and docs/04: nothing on the Fails if list tripped. Fixed: "its word" read as the agent's word (18 line 203, 19 line 194), now "the slot's word"; "o agente os dá" now "os faz"; chapter 23 line 64's "`/apply` stages and stops" false under the slot's form, now "By default"; chapter 23 line 112 put the decision after a review that, under the slot, follows the commit, now split by form; chapter 13 lines 164, 165, 210, 213, 215, 270 reworded for clarity (repeated subject, "the slot's form", a broken subject, "which counts as the asking" as in chapter 7); chapter 19 line 308's agreement and the pt "os" with no plural antecedent; 351's "its" and the pt "dado" now "dada". Left: chapter 19 line 196, as decided above.

**Done when.**

* [x] Both editions written, the same passages changed in each, Portuguese read as Portuguese; each chapter opens as it did, no filler and nothing useful cut.
* [x] Every sentence the Contract names reads true under both Git slot forms; every sentence it lists as staying is unchanged.
* [x] `grep -n -E "whatever the git strategy" book/en/13-apply.md` and `grep -n -E "qualquer que seja a estratégia de git" book/pt/13-apply.md` find nothing, or only inside a sentence that now names the slot's word as the asking; `grep -n "Nothing reaches the history unread" book/en/13-apply.md` and `grep -n "Nada chega ao histórico sem ser lido" book/pt/13-apply.md` find nothing.
* [x] `grep -c "07-the-documents" ` on each of the four chapter files, both editions, rises by at most one for 13, 18 and 19 and not for 23.
* [x] `grep -n -i -E "no longer|now offers|2026\.10|code-review|ultra"` on the four en files and `grep -n -i -E "não mais|agora oferece|2026\.10|code-review|ultra"` on the four pt files find nothing new; no em dash; no narrated run.
* [x] Delivery review as docs/05 §5 says.
* [x] `make verify` green; `make book` builds both editions and both PDF paths are reported (the driver runs `make book` once for the batch).
* [x] Only this delivery's paths and its hunk of docs/06 staged (staging is the driver's); the page moved to `work/done/` and its commit message suggested.

```commit
docs(ch13-19-commit-by-slot): the Git slot's word is the asking

- ch13: never on its own stays; the slot's word is the asking
- ch13: no delivery stands unread, the commit reviewed after it lands
- ch18, ch23: each commit and merge decided by asking or in the slot
- ch19: slot covers commit and merge only; the four costs hold both ways

work/done/ch13-19-commit-by-slot.md
```
