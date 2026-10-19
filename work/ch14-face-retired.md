# ch14-face-retired

**Objective.** After chapter 14's "The queue as a kanban board" the reader knows that a board can read the queue itself, with nothing to mirror, and how it reads it: docs/06 and the pages in `work/` by slug, from the folder's own files on trunk and from each slug's worktree or branch with a branch or a worktree per delivery, as the same chapter teaches. The section names no tool, and the book no longer names FACE nor links to it.

**Behaviour.** What the reader finds after the change, both editions:

* The section ends as before with the pointer to chapter 20's one-way mirror, then the sentence that a board can also read the queue itself, with nothing to mirror, then one sentence on how such a board reads: docs/06 and the pages in `work/` by slug, on trunk from the folder's own files, with a branch or a worktree per delivery from each slug's worktree or branch, its cards moving as the marks change while the agent works.
* On trunk, the board reads the one docs/06 and the pages in the folder's `work/`, and shows `reservations` as `[~]` from the first minute of its conversation, as the section's example already says.
* With a branch or a worktree per delivery, the board takes `lend-book`'s line and page from `lend-book`'s worktree or branch, not from the main branch's copy, agreeing with "At the moment the work changes" (en 61 to 63, pt 62 to 64) and the kanban key point (en 187, pt 188).
* Edge: no sentence names a tool, product, author's project, URL or footnote for this board; the sentence describes what any board that reads the queue does.
* Edge: the sentence promises no visibility beyond what "At the moment the work changes" states (a worktree's mark at once, a branch's once committed, a remote branch's once pushed); it says where the board reads, and that paragraph says when a mark is seen there.
* Edge: nothing else in the book names FACE or links to its site; `grep -rn "FACE\|face.kodel" book/` finds nothing after the change.

**Contract.** Two files, `book/en/14-queue-states.md` and `book/pt/14-queue-states.md`, same change in both, one sentence per line as the chapter is laid out:

* "The queue as a kanban board" / "A fila como quadro kanban": the line "A board can also read the queue itself, with nothing to mirror." (en 170) / "Um quadro também pode ler a própria fila, sem nada a espelhar." (pt 171) stays unchanged.
* The FACE line (en 171, pt 172) is replaced by one line:
  * en:

    ```
    It reads docs/06 and the pages in `work/` by slug, on trunk from the folder's own files and with a branch or a worktree per delivery from each slug's worktree or branch, and moves its cards as the marks change while the agent works.
    ```
  * pt:

    ```
    Ele lê o docs/06 e as páginas em `work/` pelo slug, no trunk nos arquivos da própria pasta e com um branch ou um worktree por entrega no worktree ou no branch de cada slug, e move os cartões conforme as marcas mudam enquanto o agente trabalha.
    ```
* The footnote definition `[^face]: J.C. Ködel, "FACE: agents write the code, your team keeps the thread", ...` (en 191, pt 192) is deleted; the notes `[^toyota-kanban]` and `[^azure-kanban]` stay as they are.
* Terms of docs/03, as the chapter already writes them: kanban board, trunk, branch, worktree, slug, mark; pt "quadro", "trunk", "branch", "worktree", "slug", "na própria pasta", "cartões". No new term.
* Sources: chapter 14's own "At the moment the work changes" (en 58 to 64, pt 59 to 65) and docs/03's `kanban board` row; no footnote, since the reader gains nothing to open.
* Cases: none. No number.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no visual change.

**Out of scope.**

* Every other line of chapter 14: the opening, "At the moment the work changes", the next-line section, the three-column illustration, the gain section and the key points stay as they are; all are true without FACE.
* Chapter 7's lending library Board slot (`npm run board` / `npm run quadro`): candidate 3, rejected by m22-review.
* Chapter 20's "Boards" section and its mirror: `ch20-merge-and-marks`.
* The pages in `work/` sitting on their branches off trunk as a kit note: `kit-note-work-in-flight`.
* docs/06's done line `ch14-face-prototype` and its history in `work/done/`: records, not the book; they stay.

**Decisions from the documents.**

* FACE and its note leave chapter 14, and the section keeps a board that reads the queue itself, docs/06 and `work/` by slug, naming no tool: the author's answer to candidate 9 in `work/done/m22-review.md` (Findings) and docs/06's line.
* The reading by slug is the one "At the moment the work changes" already teaches, so the new sentence restates where, not a new rule: chapter 14 en 60 to 62, docs/05 §4, docs/03 `kanban board`.
* Both editions in the same delivery, English the source: ADR-0004.
* No footnote for a board that names no source: docs/04 (a source note only where the reader gains something to open).
* The gain section stays true: it speaks of the marks and the queue, never of FACE (en 173 to 179, pt 174 to 180); the opening's "lay the queue out as a kanban board that shows the work while it happens" stays true too.

**Decisions taken alone** (the author chose recommended answers):

* One replacement line, not two: the visibility of a mark per place is already en 63 / pt 64, so the sentence says where the board reads and leaves when to that paragraph, rather than repeat it.
* The board is described in the present tense as what such a board does, not as something the author builds or offers: the line says "naming no tool", and a "prototype" or "free" clause would point back to a product.
* "the pages in `work/`" stays beside docs/06, read by slug like the lines: the line names `work/` and, off trunk, a delivery's page sits on its branch.
* No sibling sentence elsewhere is changed: `grep` finds FACE only in chapter 14's one line and one note per edition, and in docs/06's done line, which is a record.
* No docs/03 term needed: the sentence uses existing terms only.

**Done when.**

* [ ] Both editions changed in the same two places: the FACE line replaced by the Contract's line, the `[^face]` note deleted; nowhere else.
* [ ] `grep -rn "FACE\|face.kodel" book/` finds nothing; `[^toyota-kanban]` and `[^azure-kanban]` still resolve.
* [ ] The chapter still opens with its value; the gain section true; no filler, nothing useful cut; one sentence per line kept.
* [ ] No version, date, number, before and after, narration of a run or em dash; no private case touched.
* [ ] `make verify` green; `make book` builds both editions, and both PDF paths are reported (or the driver runs it for the batch, said on this page).
* [ ] Delivery review as docs/05 §5 says; only this delivery's paths staged, the page moved to `work/done/` and its commit message suggested; in this batch the driver stages and commits.
