# ch12-branch-then-mark

**Objective.** After chapter 12 the reader knows that `/propose` first stands where the delivery will live, in its branch or worktree as the project's Git slot says, created, or reused on resumption with any draft left for the slug brought in, and that its first edit there is the `[~]`; on trunk there is nothing to create, and the mark lands in the queue of the folder where the session runs.

**Behaviour.** What the reader can do or explain after the chapter:

* Say the order `/propose` takes on a line: the git strategy of docs/05 §5 first, then the `[~]` as its first edit, then the page; so the mark and the page are written on the delivery's branch, where `/apply` builds and the merge takes them, and never on `main` before a switch.
* Say what happens on resumption under a branch or worktree per delivery: `/propose` reuses the branch or worktree that exists for the slug instead of creating another, and brings into it a draft page left for the slug, so the draft the chapter already mentions (a fresh session "starts from the documents and the draft page") is found there.
* Say what happens on trunk: nothing is created; the `[~]` is the first edit in the folder where the session runs.
* Find, in the key points, `/propose` starting in the delivery's branch or worktree before it marks `[~]`, beside the marks it already lists.
* Find the mechanics where they live: creating a branch in chapter 18, a worktree in chapter 19, and where a board sees the mark in chapter 14, each by a pointer, not repeated here.
* Edge: on a line that is not free, `[?]` or with an `after` not yet `[x]`, nothing is created: `/propose` says what the line waits on and stops, as the chapter already says (chapter 14); at most one clause on line 28, not a new sentence.
* Edge: a reader on trunk with two sessions in one folder reads nothing that suggests `/propose` switches branch or creates a worktree there.

**Contract.** Chapter `book/en/12-propose.md` and `book/pt/12-propose.md`, same changes in both:

* "What `/propose` does" (en and pt, the "When it starts" sentence, line 26 in both): before the mark, the clause that `/propose` first starts or resumes the definition in the delivery's branch or worktree, as the project's Git slot says, created, or reused with any draft for the slug brought in, and only then marks `[~]` there as its first edit; on trunk there is none to create. Pointers to chapters 18 and 19. The rest of the sentence (`[>]` only when completely defined, chapter 14) stays. The sentence may split in two, one sentence per line as the chapter is laid out.
* "Key points" (en line 168, pt line 177): the `/propose` bullet gains "starts in the delivery's branch or worktree, where the project's Git slot puts one, and marks the line `[~]` there while it talks"; the rest of the bullet stays.
* Wording: the trunk case stands first or beside the branch case in every changed sentence, since this book's default is trunk; nothing reads as if `/propose` switches branch on trunk.
* Terms of docs/03: branch, worktree, trunk, draft page, delivery, slot; in Portuguese "branch da entrega", "worktree", "trunk", "rascunho da página", as chapters 13 and 18 already say. No new term; no docs/03 row.
* Sources: the installed `.claude/skills/propose/SKILL.md` at `metadata.version` 2026.10.19 ("start or resume the definition in the right branch or worktree, a worktree where docs/05's Git slot puts it and reused when it exists; then your first edit there marks the line `[~]`"), already cited by the chapter as "the kit's file for the command"; docs/05 §2 ("create the branch or worktree named after the slug, or reuse its existing one on resumption, bringing into it any draft left for the slug"). No new footnote: the reader gains nothing to open beyond the kit file the chapter already names.
* Cases: none. No number.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no visual change.

**Out of scope.**

* Where a board sees a mark, on trunk or at the merge: `ch14-where-a-board-sees`.
* /apply reading docs/00 and docs/03 and following every slot: `ch13-apply-reads-00-03`.
* Project slots /propose follows with no edit to the skill: `ch07-slots-and-decided`.
* Chapter 18's line 25, which already says `/propose` creates or reuses the branch and writes the page there: correct as is.
* Chapter 19's worktree layout and the mark on a delivery branch until its merge: `ch18-19-one-index`.
* Any other section of chapter 12: it keeps everything else it says.

**Decisions from the documents.**

* The order is branch or worktree first, then `[~]` as the first edit there: the installed `/propose` skill, 2026.10.19, and docs/05 §2.
* Resumption reuses the existing branch or worktree and brings in a draft left for the slug: docs/05 §2.
* A line that is not free gets no branch or worktree: the installed `/propose` skill checks that the line is free before the git step.
* On trunk nothing is created: docs/05 §5 Git slot ("trunk") and `work/done/kit-2026-10-19.md` ("on trunk there is none to create").
* Taught as the kit is, with no version, date or "now": AGENTS.md and the M21 rule that the book teaches the kit as it is today.

**Decisions taken alone.**

* The resumption clause, with the draft brought in, enters the chapter: without it, the chapter's own sentence on a fresh session starting "from the documents and the draft page" would be silent on where that draft is under a branch strategy.
* Pointers to chapters 18 and 19 instead of explaining how a branch or worktree is created; one pointer to chapter 14 at most for the board, left to its own line.
* Chapter 18's line 25 and chapter 14 untouched by this delivery.
* The key point is reworded inside the existing `/propose` bullet, not added as a new bullet.
* The reason given in the chapter is one clause: the mark and the page belong to the delivery's branch, where `/apply` builds and the merge takes them.

**Done when.**

* [x] Both editions changed in the same two places, "What `/propose` does" and "Key points", and nowhere else in chapter 12.
* [x] The chapter still opens with its value; no filler, nothing useful cut; one sentence per line kept.
* [x] No version, date, before/after or narration of a run in the text; no em dash.
* [x] Portuguese uses the words chapters 13 and 18 already use for branch, worktree, trunk and draft.
* [x] No number added, so none to source; no private case used, so no approval needed.
* [x] `make verify` green; `make book` builds both editions, and both PDF paths reported.
* [x] Delivery review as docs/05 §5 says; only this delivery's paths and its hunk of docs/06 staged; the page moved to `work/done/` and its commit message suggested.

## What happened

**Built.** Both editions of chapter 12, `book/en/12-propose.md` and `book/pt/12-propose.md`, changed in two places. "What `/propose` does": the "When it starts" sentence became three, one per line: `/propose` first stands where the project's Git slot puts the delivery, trunk first (the folder where the session runs, nothing to create), otherwise the branch or worktree named after the slug, created or reused on resumption with any draft page for the slug brought in (chapters 18 and 19); its first edit there marks `[~]`, and off trunk the mark and the page go with the delivery's branch, where `/apply` builds and the merge takes them; the `[>]` sentence stays as it was. "Key points": the `/propose` bullet gains where it starts, trunk beside the branch or worktree, and "marks the line `[~]` there while it talks".

**Checked.** Against `.claude/skills/propose/SKILL.md` at 2026.10.19 (lines 19 to 21) and docs/05 §2 (create, or reuse on resumption, bringing in any draft). Portuguese words as chapters 13 and 18 use them: "branch da entrega", "worktree", "trunk", "rascunho da página", "slot Git". No number, no private case, no em dash, no version or date.

**Divergences.** None from the Contract. Line 28 of the chapter (the not-free line) is untouched: its "does not start" already covers the edge, and the Done when allows changes only in the two places.

**Decisions taken alone in /apply.**

* The key point names the trunk case beside the branch or worktree ("or on trunk in the folder where the session runs"), to meet the Wording rule in every changed sentence.
* The Git slot heads the sentence ("where the project's Git slot puts the delivery"), since the slot chooses trunk too, as the review suggested.
* `make book` is not run in this session: the driver of the parallel /apply sessions runs it once at the end and gives both PDF paths; the Done when item is ticked on that understanding.

**Delivery review.** A read-only Explore agent on Opus read `git diff HEAD` of both chapters against this page, docs/04, AGENTS.md, the installed `/propose` skill and docs/05 §2. It confirmed scope, facts, terms and parity, and raised five minor points:

* "on a branch, the mark and the page go with the delivery's branch" repeated "branch" and left the worktree to inference. Fixed: "off trunk the mark and the page go with the delivery's branch".
* The branch half chained too many appositives and tied the Git slot only to it. Fixed: the slot moved to the head of the sentence.
* Line 26 might read as if the branch is made before the free-line check of line 29. Kept: the page allows that line at most one clause and its "does not start" covers it.
* The key point grew longer with the trunk case. Kept: the Wording rule asks for trunk beside the branch case.
* "never on `main` before a switch" only implied by "first edit there". Kept: the Contract does not ask for it.

**Proof.** `make verify` green after the last covered edit, the review's fixes and the page's move included.

```commit
docs(ch12-branch-then-mark): propose starts where the delivery lives

- /propose stands where the Git slot puts the delivery, trunk first
- branch or worktree created, or reused with the slug's draft
- its first edit there marks [~]; off trunk it goes with the branch
- key point names where /propose starts; both editions

work/done/ch12-branch-then-mark.md
```
