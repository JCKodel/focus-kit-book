# ch17-20-branch-on-origin

**Objective.** After chapters 17 and 20 a reader with a branch or a worktree per delivery knows that a session asked where things stand, and a board's mirror, run `git fetch` and read each slug's line from its branch on origin, the branch's copy being the current one until the merge and the main branch's after it, with the lines only a branch has, so both see a mark once its commit is pushed to the delivery's branch, while on trunk the board sees it at once; both editions.

This page was defined and built by the agent before the author read it, on the author's word that the agent runs the whole queue; the author reads the page and the diff at the end (docs/05 §4).

**Behaviour.**

* Reading chapter 17's paragraph after the "where are we?" answer, the reader learns that with a branch or a worktree per delivery the session runs `git fetch`, counts a line whose branch exists on origin as taken even before any of its marks is pushed, and takes each slug's line from its branch on origin, the current copy until the merge, the main branch's after it, with the lines only a branch has; and that the answer's `return-book [*]` is seen once that mark is pushed.
* Reading chapter 17's last key point, the reader finds the same: each slug's branch on origin, after `git fetch`.
* Reading chapter 20's step 4 of a pull request, the reader learns that a `[~]` or `[*]` set on a branch is read by a board or a session once it is pushed.
* Reading chapter 20's Boards section, the reader learns that on trunk the board shows a mark at once, since the push runs inside the command that changed it; that with a branch or a worktree per delivery the command that pushes runs `git fetch` and reads each slug's line from its branch on origin, with the same copy rule and the lines only a branch has; and that the board sees a mark once its commit is pushed to the delivery's branch, by default by the person, each refresh carrying every other delivery's mark pushed so far.
* Reading chapter 20's board key point, the reader finds the board read from each slug's branch on origin after `git fetch`, seeing a mark once it is pushed.
* Edge: a mark committed on a local branch and not pushed is seen by no board and no other session; neither chapter says "local or remote", nor that a local commit is enough.
* Edge: chapter 17 :119 quotes the rules file's line, which the kit's `SETUP.md` writes "from the delivery branches after `git fetch`" and this repository's `AGENTS.md` :37 keeps; it stays as it is.
* Edge, Case A: chapter 20 :59 to :60 and :82 and chapter 17's gain section are not touched.
* Edge, the shared tree: another session may work in this tree on another M33 line; its files and its docs/06 line are its own (docs/05 §4).
* Fails: "local or remote" (pt "local ou remoto") left in either chapter; a sentence that says the board sees a branch's mark at once; a version or "no longer" in the text (docs/04, The kit as it is); a sentence changed in one edition and not the other; an em dash; `make verify` red.

**Contract.**

Sources: docs/05 §4 :161 to :176 and focus-kit's `SETUP.md` §4 (its board paragraph), the kit's `CHANGELOG.md`, section 2026.10.25 (the copy rule, which displaces "local or remote"); chapters 14 :61 to :64 and 19 :198 to :229 as the book already says them. No number.

Passages of `book/en/17-project-as-assistant.md` and `book/en/20-team-tools.md` at HEAD `9335b2d`, and the same lines of `book/pt/`, each rewritten to say what Behaviour lists and nothing else:

* Chapter 17 :132, the reading with a branch or a worktree per delivery; :151, the last key point.
* Chapter 20 :27, step 4's last clause; :62, the board's refresh, which may become two sentences, one per line; :89, the board key point.

No section added or removed; one sentence per line. Terms of docs/03: kanban board, claim, queue tree, free line; none new, no row changed (the kanban board row already reads each slug's own branch on origin after `git fetch`). Cases: none changed; chapter 20's Case A passages stay byte for byte. Sources cited: no new note.

Decided by the agent, the author corrects it in the review:

1. The parallel token: neither chapter 17 nor chapter 20 carries `(PA)`, `(P-)`, `(-A)`, `(--)` or the word token at HEAD `9335b2d`, in either edition, so this line removes nothing; `work/done/kit-2026-10-25.md` :20 lists both chapters as still teaching it, which is a note below.
2. Chapter 17 :119 stays: it is the rules file's line, written as focus-kit's `SETUP.md` and `AGENTS.md` :37 write it; :132 right after it says how the branches are read.
3. Chapter 17 :151 changes with :132, to "each slug's branch on origin", so the key point and the passage agree.
4. Chapter 20 :27 and :89 change with :62: the line's sentence names the board seeing a mark once it is pushed, and both clauses would otherwise say the board reads a branch with no word on origin or the push.

**Out of scope.**

* Chapter 8 :102 (pt :104), "local or remote" in the update: `ch08-update-2026-10-25`'s line.
* Chapter 20's Case A passages and question deliveries: unchanged, so no approval is asked.
* docs/03, docs/05, ADRs, `AGENTS.md`, the manuals: they already say this.

**Done when.**

- [x] Both editions changed as the Contract says, and nothing else in the chapters.
- [x] No "local or remote" (pt "local ou remoto") in chapters 17 and 20.
- [x] Opens with its value, no filler and nothing useful cut, every number sourced (none new).
- [x] No em dash; at most five key points.
- [x] `make verify` green; `make book` builds both PDFs, their paths given.
- [x] Delivery review by a read-only Opus agent (docs/05 §5).
- [x] Cases: none changed, so no approval is needed (docs/00 OD-3).

## Outcome

Built as defined. Chapter 20 :62 became two sentences, one per line, so its key point is :90 now, not :89; no other line moved.

**Proof.** `grep` finds no "local or remote" nor "local ou remoto" in chapters 17 and 20 of either edition; chapter 20 :59 to :60 and :83 (Case A) and chapter 17's gain section unchanged. `make verify` green after the last edit, 19 seconds wall time (ceiling five minutes). `make book` built `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.

**Delivery review.** A read-only agent on Opus, not given this session's conclusions, read the page, docs/04, `git diff HEAD` of the four chapter files, this delivery's hunk of docs/06, docs/05 §4, docs/03's rows, chapters 14 and 19 around the rule, and the kit's `SETUP.md` and `CHANGELOG.md` 2026.10.25. It found the rule right in both editions, the scope and Case A held, and seven wording candidates, all fixed: 20 :27 "once the mark's commit is pushed" (the "it" read as the branch); 20 :63 "a push that is yours by default, since the commands commit nothing on their own (chapter 19)"; 20 :63 "at the first refresh after its commit is pushed", since the board refreshes only when a command changes a mark; pt 20 :63 "as marcas já enviadas de cada outra entrega" ("enviada" agreed with "entrega"); en 20 :90 "once that mark is pushed"; 17 :132 and 20 :63 "which holds the current copy" (pt "que guarda"), as chapter 14 :62 says; 17 :151 "exists on origin". Its eighth candidate, in chapter 14, is a note below.

**Decisions taken alone.** Those under Contract, for the author's review.

## For the review

* work/done/kit-2026-10-25.md:20: lists chapters 17 and 20 among those that "still teach the token"; neither carried it at `9335b2d` (decision 1 above).
* book/en/14-queue-states.md:66 (pt the same): the project's mirror "shows the mark at once", with no "on trunk", and "every delivery's mark"; chapter 20 :62 to :63 now say at once on trunk and, with a branch, at the first refresh after the push, with "every other delivery's"; a reader may see the two as contradicting.

```commit
docs(ch17-20-branch-on-origin): read each line from its branch on origin

- Chapter 17: the status read from each slug's branch on origin
- Chapter 20: the board sees a branch's mark once it is pushed
- On trunk the board still shows a mark at once; both editions

work/done/ch17-20-branch-on-origin.md
```
