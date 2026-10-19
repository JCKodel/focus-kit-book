# ch18-19-one-index

**Objective.** After chapters 18 and 19 the reader can say what the index is, the staged copy of the project a commit is made from, and that one working folder has one, shared by every session open in it, while each worktree has its own; so, on trunk, when the second session has staged before the first delivery is committed, the person sets the second's paths aside with `git restore --staged <paths>`, commits the first, and has them staged again. The reader can also say that with a branch or a worktree per delivery the line's marks are edits to docs/06 on the delivery's branch, so `main`'s queue shows the line as it was until the merge brings them in.

**Behaviour.** What the reader can do or explain after the two chapters:

* Name the index after chapter 18: `git add` writes a change to it, `git diff --cached` shows it, a plain `git commit` takes it whole; "the agent stages" means the agent writes to it, and the person's review reads it before the commit.
* Say, after chapter 18, that a working folder has one index, so two sessions in one folder stage into the same one, and find in chapter 19 what to do about it.
* In chapter 19's "Two sessions in one folder", read the reason before the steps it already teaches: one folder, one index, shared by both sessions, so a commit takes whatever either has staged; then the steps as they stand (order first, `git restore --staged <its paths>` when both are staged, docs/06 taken out whole when the lines are neighbours, this delivery's line staged again, commit, the other's entries staged again).
* Say that a worktree has its own index, the same fact seen from the other side: two sessions in two worktrees never share one, so there is nothing to set aside, and their changes meet only at the merge.
* Say where the mark lives under a branch or worktree per delivery: `/propose`'s `[~]` and every later mark of the line are edits to docs/06 on the delivery's branch, so `main/`'s queue shows the line as it was, and each worktree's queue shows its own branch's state, not a live view of all; the merge brings the marks in, and that is why the queue always meets at the merge, as chapter 19 already says. Where a board sees the mark is chapter 14's, by a pointer.
* Find both facts in the key points of each chapter.
* Edge: a reader on trunk reads nothing that suggests a mark waits for a merge; on trunk the mark is in the one folder at once.
* Edge: a reader who stages in one worktree and runs `git diff --cached` in `main/` sees nothing of it, as chapter 19 line 89 already says; no new sentence for it.

**Contract.** `book/en/18-git-essentials.md` and `book/pt/18-git-essentials.md`, same changes in both (line numbers as of today, equal in both editions):

* Opening (lines 3-4): the second sentence gains "say what the index holds and why a folder has one", or as close as reads well, beside "read a history of commits, branches and merges".
* "Commits and the history" (after line 65, "The agent stages that change and suggests the message"): two or three sentences defining the index: the staged copy of the project a commit is made from, also called the staging area; `git add <path>` writes a change to it, `git diff --cached` shows what it holds, and a plain `git commit` takes it whole, so staging is choosing what the commit holds. One working folder has one index, shared by every session open in it; [chapter 19](19-worktrees.md) says what two sessions do about it. The sentence on use and reading as review stays.
* "One delivery, one step to undo" (line 25, the branch per delivery sentence): one clause that the page and the line's marks are written on the branch, so `main`'s queue shows the line as it was until the merge; pointer to [chapter 14](14-queue-states.md) for where a board sees it. The rest of the sentence and the example stay.
* "Choosing", the Trunk bullet (line 181): "each session staging only its delivery" becomes "each session staging only its delivery in the folder's one index"; the rest stays.
* "Key points": the commit bullet (line 199) gains "the index is the staged copy a commit is made from, one per working folder"; the strategies bullet (line 201) keeps its wording, with "the marks live on the delivery's branch until its merge" beside the branch and worktree strategies if it reads in one clause, else left out.

`book/en/19-worktrees.md` and `book/pt/19-worktrees.md`, same changes in both:

* "Two sessions in one folder" (line 49): before "Then do not commit yet", one sentence: one folder has one index, which both sessions stage into, so a commit takes whatever either has staged (chapter 18). Lines 50-54, the `git restore --staged` steps, stay as they are: they already say what docs/05 §6 says.
* "What a worktree is" (line 88): "its own staging area" becomes "its own index", in Portuguese "o seu próprio índice", with the clause "where one folder has one index for every session in it" if it reads in one line.
* "Worktrees in the kit" (after line 178, "and writes the page there"): one or two sentences: the line's `[~]` and every later mark are written in the worktree, on its branch, so `main/`'s queue shows the line as it was and each worktree's queue shows its own branch's state; the merge brings the marks in, which is why the queue meets at every merge ("When the branches meet"). Pointer to chapter 14 for where a board sees it; nothing on `/propose`'s order of branch and mark beyond what chapter 12 says.
* "Key points": the commit bullet (line 346) opens "One folder has one index:" and keeps the rest; the worktree bullet (line 347) gains "each worktree has its own index, and the line's marks live on its branch until the merge".
* Line 298's parenthetical "(the staged copy a commit is made from)" stays: a reminder at the point of use.

docs/03, a new row after `stage` (the driver adds it before /apply; the `stage` row is unchanged):

`| index | índice | `git add`, `git diff --cached`, `git restore --staged` | The staged copy of the project a commit is made from, also called the staging area: `git add` writes a change to it, `git diff --cached` shows it, and a plain `git commit` takes it whole. One working folder has one, shared by every session open in it, and each worktree has its own; on trunk, when the second session has staged before the first delivery is committed, the person sets its paths aside with `git restore --staged <paths>`, commits the first, and stages them again (docs/05 §6). |`

* Terms of docs/03: index (new), stage, branch, worktree, trunk, merge, delivery; in Portuguese "índice", "colocar em stage", "pasta de trabalho", as chapters 13 and 19 already say. The English prose says "working folder", as chapters 13, 14 and 19 do, not "working tree".
* Sources: docs/05 §6 ("One working tree has one index, so when the second session has already staged, the person sets its paths aside with `git restore --staged <paths>`, commits the first, and stages them again") and §4 ("In worktrees, each worktree's queue shows that branch's state, not a global live view"; "with a branch or a worktree per delivery the mark lives on the delivery's branch"); the git-worktree documentation chapter 19 already cites for a worktree's own index. No new footnote: no number, and no git page the reader gains beyond those already cited.
* Cases: none. No number.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no visual change.

**Out of scope.**

* Where a board sees a mark, at once on trunk or at the merge: `ch14-where-a-board-sees`; this page says only where the mark lives in git.
* `/propose` creating the branch or worktree before it marks `[~]`: `ch12-branch-then-mark`; chapters 18 line 25 and 19 line 178 keep their wording on that order.
* Chapter 13 lines 230-231, which already point to chapter 19 for an index of one delivery.
* The `git restore --staged` steps of chapter 19 (lines 50-54), the batch section's patch with `git apply --cached`, the conflict sections and every other section of both chapters: they keep everything they say.
* The Git slot's option of the agent committing by the slot's word: `ch07-review-git-slots`.

**Decisions from the documents.**

* One working tree has one index, and the person sets the second session's paths aside with `git restore --staged`, commits the first, and stages them again: docs/05 §6 and `work/done/kit-2026-10-19.md`.
* With a branch or worktree per delivery the mark lives on the delivery's branch, and each worktree's queue shows that branch's state: docs/05 §4.
* The agent never unstages another session's entries; the person does: docs/05 §6 ("Do not unstage those entries yourself"), as chapter 19 already says.
* Taught as the kit is, with no version, date or "now": AGENTS.md and the M21 rule.
* The new concept enters docs/03 first, in both languages: docs/03's header and AGENTS.md; `work/done/kit-2026-10-19.md` left this row to this line.

**Decisions taken alone.**

* The index is defined in chapter 18, the git basics chapter, and chapter 19 builds on it: chapter 19 uses "the index" from line 49 while only line 298 glosses it, and chapter 18 never names it.
* The docs/03 Portuguese term is "índice", which chapters 13 and 19 already use; chapter 19 line 88 changes "staging area" / "área de stage" to "index" / "índice", since docs/03 fixes one Portuguese term and no synonym. English keeps "also called the staging area" once, in chapter 18's definition and in the docs/03 row, so a reader who meets git's other name knows it.
* The English prose keeps "working folder", the book's word, not docs/05's "working tree".
* Chapter 19's `git restore --staged` steps are not rewritten: they already match docs/05 §6; the delivery adds only the reason in front of them.
* Chapter 18's opening sentence gains the index, as a new thing the reader can do; chapter 19's opening stays, since it already promises committing each delivery alone.
* No footnote for git's glossary: the definition is plain, and chapter 19 already cites the git-worktree page for a worktree's own index.
* Line 298's parenthetical stays.

**Done when.**

* [x] The docs/03 `index` row is present, as the Contract writes it, before the first chapter edit (committed by the driver in c79bc37).
* [x] Both editions changed in the places the Contract names, and nowhere else in chapters 18 and 19.
* [x] Each chapter still opens with its value; no filler, nothing useful cut; one sentence per line kept.
* [x] No version, date, before/after or narration of a run in the text; no em dash.
* [x] Portuguese says "índice" for the index everywhere in chapters 18 and 19, and no "área de stage" is left; chapter 18's one gloss of git's other name gives it in English, "staging area", as the book does for a term git names in English.
* [x] Nothing in either chapter suggests a mark waits for a merge on trunk.
* [x] No number added, so none to source; no private case used, so no approval needed.
* [x] `make verify` green; `make book` and both PDF paths: run once by the driver at the end of the batch, as this run's rules say.
* [x] Delivery review as docs/05 §5 says; the page moved to `work/done/` and its commit message suggested; staging and the docs/06 hunk are the driver's, as this run's rules say.

## Proof

* `make verify` green before the first edit and after the last.
* `make book` and the two PDF paths: run once by the driver at the end of the batch.
* Chapter 18, both editions: the opening's second sentence, line 25's branch per delivery sentence, two new lines after line 65, the Trunk bullet, and the commit and strategies key points.
* Chapter 19, both editions: a new line before "Then do not commit yet", line 88, two new lines after line 178, and the commit and worktree key points.

## Divergences

* Chapter 18 line 25: the marks clause goes after "`/apply` builds on it", joined by semicolons, since `/apply` writes the later marks; the rest of the sentence and the example stay.
* Chapter 18's definition opens "To stage is to write to the index" / "Colocar em stage é escrever no índice", tying the agent's staging to the index as the Behaviour asks.
* Chapter 19's commit key point opens "One folder has one index, so commit from it ..." rather than "One folder has one index: ...", to avoid two colons in one sentence; the rest stays.
* Chapter 19 line 88's added clause reads "the one every session open in that folder stages into" / "aquele em que toda sessão aberta naquela pasta coloca em stage", so it states the same fact from the worktree's side instead of a contrast.
* Chapter 19's "Worktrees in the kit" refers to the conflict section as "the next section, on conflicts" / "a próxima seção, sobre conflitos", since the book links no in-page headings.

## Delivery review

A read-only agent on Opus read `git diff HEAD` of the four chapter files against this page, docs/03, docs/04 and AGENTS.md. No blocking findings; Contract places, parity, Portuguese terms, the trunk edge and git facts held. Three nits: line 88's "while" set up a false contrast, fixed (the divergence above); "`git diff --cached` shows what it holds" is the Contract's wording and kept; the new chapter 19 line 49 partly repeats the line before it, kept as the reason the Contract asks for.

## Decisions taken alone (apply)

* The author was not in the session; the review's nits were settled as above without asking.
* The strategies key point of chapter 18 takes the marks clause, since it reads in one clause attached to the branch and worktree strategies only.

```commit
docs(ch18-19-one-index): one index per folder, marks on the branch

- Define the index in ch 18, one per working folder
- Give the reason before ch 19's git restore --staged steps
- Each worktree has its own index; "área de stage" becomes "índice"
- Marks live on the delivery's branch until its merge, ch 18 and 19

work/done/ch18-19-one-index.md
```
