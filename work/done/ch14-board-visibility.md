# ch14-board-visibility

**Objective.** After chapter 14 the reader can say what a board fed from the queue shows with a branch or a worktree per delivery: each delivery's mark as far as the reader of the queue can see it, never more, its cards moving as each mark becomes visible.

**Behaviour.** What the reader can do or explain after the chapter:

* Say what one refresh of a project's one-way mirror carries with a branch or a worktree per delivery: every delivery's mark as far as the pushing command can see it (a worktree's the moment it changes, a branch's once committed on it, a remote branch's once pushed), not its own branch's copy, and not every delivery's latest mark.
* Say when a board that reads the queue itself moves a card: when that card's mark becomes visible to it, by the same ladder, not the moment the mark changes on a branch nobody committed.
* Read chapter 14 and chapter 20 as one rule: chapter 14's mirror sentence and chapter 20's push say "as far as it can see it" alike, in both editions.
* Edge: on trunk, nothing changes; the board still sees the mark at once.
* Edge: no sentence reads as if a board sees a mark on a branch before it is committed, or on a remote branch before it is pushed.

**Contract.** Chapter `book/en/14-queue-states.md` and `book/pt/14-queue-states.md`, same changes in both, against the files as they are today:

* "At the moment the work changes", the mirror sentence (en :64, pt :65): "so each refresh carries every delivery's latest mark, not its own branch's copy" becomes "so each refresh carries every delivery's mark as far as it can see it, not its own branch's copy". Portuguese: "então cada atualização leva a marca de cada entrega até onde consegue vê-la, não a cópia do próprio branch", the phrase of chapter 20 pt :61. The rest of the sentence stays. The sentence above it (en :63, pt :64) already says how far each place lets a reader see; the fix leans on it and does not restate it.
* "The queue as a kanban board", the board that reads the queue itself (en :171, pt :172): "and moves its cards as the marks change while the agent works" becomes "and moves its cards as each mark becomes visible to it while the agent works"; Portuguese "e move os cartões conforme cada marca fica visível para ele enquanto o agente trabalha". The rest of the sentence stays.
* No line number in chapter prose; one sentence per line, as the chapter is laid out.
* Terms of docs/03: kanban board, board mirror, trunk, branch, worktree. No new term; no docs/03 row.
* Sources: chapter 20 :61 ("as far as it can see it"), chapter 14 :63, docs/05 §4 and docs/03's `kanban board` row. No footnote: the reader gains nothing to open.
* Cases: none. No number.
* Neighbouring lines: no other M23 line edits chapter 14 (ch17-next-free-line only cites chapter 14 :78). M24's `ch12-14-17-20-branch-claim` and M25's `ch12-14-parallel-token` edit chapter 14 later, in queue order, and will find these two sentences as this delivery leaves them.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no visual change.

**Out of scope.**

* The key points' kanban bullet (en :187, pt :188): the review read it and marked nothing; it already bounds itself with "until the merge".
* S5, a board reading the pages in `work/`: dropped weak by the review; nothing to fix.
* en :59 to :63 (pt :60 to :64): already right, the ladder this fix points to.
* Chapter 20 :61: the source of the wording, not a target.
* The 2026.10.20 branch claim: M24's `ch12-14-17-20-branch-claim`; this delivery teaches the installed kit, 2026.10.19.2.
* Any version, date or history of the kit's change.

**Decisions from the documents.**

* A reader of the queue sees a worktree's mark at once, a branch's once committed, a remote branch's once pushed: chapter 14 :63, chapter 20 :61, docs/05 §4.
* The mirror's push reads each slug's line where it lives and carries every mark "as far as it can see it": chapter 20 :61 and docs/03 `board mirror`.
* Finding ids D1, S3 and D4, seen, low: `work/done/m23-review.md`.
* Taught as the kit is today, with no version or "now": AGENTS.md and the M21 rule.

**Decisions taken alone.**

* The Portuguese mirror sentence reuses chapter 20's "até onde consegue vê-la" word for word, so the two chapters say one thing one way.
* "while the agent works" stays in the :171 sentence: it says when the board is useful, and is true once the visibility clause bounds it.
* No back reference such as "as said above" is added: the ladder is the sentence just before the mirror sentence, and the kanban section's sentence names where the board reads, which is enough.
* The queue line keeps its wording; its ":63" is a pointer for the page, not text for the chapter.
* /apply, resumed in a fresh session after the first was stopped mid-run (docs/05 §4): the two chapter hunks it found in the tree are this delivery's, checked against the Contract word for word, and kept as they were; nothing else of this delivery had been written.

**Done when.**

* [x] Both editions changed in the same two sentences, the mirror sentence and the board that reads the queue itself, and nowhere else in chapter 14.
* [x] No sentence reads as if a board sees a branch's mark before it is committed or a remote branch's before it is pushed; on trunk nothing changes.
* [x] The chapter still opens with its value; no filler, nothing useful cut; one sentence per line kept.
* [x] No version, date, before/after or narration of a run in the text; no em dash; no number added, no private case used.
* [x] `make verify` green after the last edit, and `make book` built both PDFs, its run and both PDF paths recorded in this page's Proof by /apply.
* [x] The Delivery review as docs/05 §5 says, recorded on this page.

**Divergences.** `make book` is not run by this /apply: the batch's lane rules leave it to the driver, who runs it once for the batch and gives the author both PDF paths, `output/` English and Portuguese; the Done when item on it is ticked on that word. docs/06 is the driver's in this batch: it marks the line `[x]`. The staging and the commit are the driver's too: this session staged nothing.

**Proof.** `git diff HEAD` of both chapter files shows two hunks per edition, en :64 and :171, pt :65 and :172, each the Contract's sentence with only the named clause changed; no other line of chapter 14 moved. Neither edition holds "latest mark", "marca mais recente", "as the marks change" or "conforme as marcas" any more. The new mirror clause reads as chapter 20 :61 does, "as far as it can see it" and "até onde consegue vê-la", so the two chapters say it one way. On trunk the text is unchanged: the sentence above (en :63, pt :64) and the kanban sentence's trunk clause stand as they were. `make verify` green after the last edit: build, parity, em dash, prose, width, examples, links and disclosure.

**Delivery review.** One read-only Opus agent read `git diff HEAD` of both chapter files and of this page against the page, docs/04 and AGENTS.md, with chapter 20 :61 and chapter 14's two sections whole in both editions. It found one: the review's Done when item was ticked before this paragraph existed; fixed by this paragraph. It confirmed both edits word for word against the Contract and nothing else changed, one phrase with chapter 20 :61 in both editions, the old wording gone, the Portuguese "para ele" and "vê-la" agreeing with "quadro" and "a marca", no em dash, number, version or private case, and that en :62 and :145 (pt :63 and :146) read as no board seeing a mark before it is visible. No new queue line.

```commit
docs(ch14-board-visibility): board sees each mark as far as it can

- chapter 14's mirror carries every delivery's mark as far as it can see it
- a board reading the queue moves a card as each mark becomes visible
- one phrase with chapter 20 :61; both editions

work/done/ch14-board-visibility.md
```
