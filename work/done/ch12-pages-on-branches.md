# ch12-pages-on-branches

Defined by /propose on 2026-11-14 on the author's word for this run, relayed by the driver session: "Vamos rodá-la de ponta a ponta automaticamente, sem pausas para concluir o milestone." So the agent decided alone (docs/05 §4): every choice below marked "decided by the agent" is the agent's recommendation taken as the answer, and the author corrects it in the review. This page was written, and will be built, before the person read it.

**Objective.** After chapters 12 and 19 the reader can say which pages `/propose` reads before it asks: the page of each delivery in flight, in `work/` or on its own branch, since with a branch or a worktree per delivery the main branch's `work/` lacks every page not yet merged.

**Behaviour.** What the reader of both editions can do or explain afterwards:

* B1. Given a project with a worktree per delivery, `return-book` in flight on its branch and not yet merged, and `/propose overdue-list` typed in `main/`, the reader says `/propose` reads `return-book`'s page from its branch, though `main/`'s `work/` does not hold it.
* B2. On trunk, the reader says the pages in flight are all in the folder's `work/`, and `/propose` reads them there.
* B3. Must fail: the reader does not say `/propose` reads only `work/` in a worktree layout; no sentence of chapter 12 or 19 says it.
* B4. Edge, chapter 19's batch: two pages written at the same time still do not read each other, on trunk or on branches, since a page being written is on neither yet when the other starts.
* B5. A resumed `/propose` keeps its line's mark: the reader says the first edit marks a `[ ]` line `[~]`, and a line already `[~]` whose session ended keeps it when a new session resumes it on the person's word.

**Contract.**

Files: `book/en/12-propose.md`, `book/pt/12-propose.md`, `book/en/19-worktrees.md`, `book/pt/19-worktrees.md`, nothing else.

Sources the text follows: the installed `.claude/skills/propose/SKILL.md` 2026.11.14, "the page of each delivery in flight, in `work/` or on its own branch", and "Your first edit there marks a `[ ]` line `[~]` as docs/05 §4 says. A resumed line keeps its mark."; the kit's CHANGELOG 2026.11.14, "With a branch or a worktree per delivery, the main branch's `work/` lacks every page not yet merged."

End state (line numbers as of `6a91138`, en / pt):

* C1. Chapter 12, `## What /propose does`, `:27` / `:27`. EN today: "..., docs/06 for what comes before and after the line, `work/` for the deliveries in flight, and docs/01 ...". End state: "..., docs/06 for what comes before and after the line, the page of each delivery in flight, in `work/` or on its own branch, since with a branch or a worktree per delivery the main branch's `work/` lacks every page not yet merged, and docs/01 ...". PT today: "..., o docs/06 para o que vem antes e depois da linha, `work/` para as entregas em andamento, e o docs/01 ...". End state: "..., o docs/06 para o que vem antes e depois da linha, a página de cada entrega em andamento, em `work/` ou no seu próprio branch, já que com um branch ou um worktree por entrega o `work/` do branch principal não tem nenhuma página ainda sem merge, e o docs/01 ...".
* C2. Chapter 19, `## Proposing in a batch`, `:360` / `:360`. EN today: "`/propose` reads the deliveries in flight in `work/` when it starts, and a page being written ...". End state: "`/propose` reads the page of each delivery in flight, in `work/` or on its own branch, when it starts, and a page being written ...". PT today: "O `/propose` lê as entregas em andamento em `work/` quando começa, e uma página ...". End state: "O `/propose` lê a página de cada entrega em andamento, em `work/` ou no seu próprio branch, quando começa, e uma página ...". The rest of the sentence holds on a branch too: a page being written is not yet committed there (B4).
* C3. The resumed mark, in scope on the driver's word: checked, no change. Chapter 12 `:31` / `:31` already says "Its first edit there marks the `[ ]` line `[~]`" / "A primeira edição dele ali marca a linha `[ ]` como `[~]`", and `:32` / `:32` "a new session resumes it on your word, the line keeps its `[~]`, and nothing marks it `[~]` again". Chapter 19's `[~]` sentences (`:68`, `:193`, `:199`) say where the mark is written and read, never that a resumed `/propose` marks it. The kit's "your first edit there marks it `[~]`" is not taught in either chapter, in either edition.

Decided by the agent: no mechanism (fetch, origin) is added to C1 or C2; `:29` of chapter 12 already says how the session reads a branch on origin after `git fetch`, and the skill names none for pages. No dated error is told: the line names none, and the book teaches the kit as it is (docs/04). No new chapter pointer: chapter 12 already points to chapter 19 at `:30` and `:33`.

Terms of docs/03 introduced: none new.

Cases drawn on: none. No number is added, so no source note.

**Out of scope.**

* Chapter 15's base of a review's range: `ch15-base-last-end`, another lane.
* Chapter 19's key point (`:421`): it says nothing of which pages `/propose` reads, so nothing there is false.
* docs/03: no row is wrong.

**Done when.**

* [x] C1 and C2 read as their end state in both editions, English the source, Portuguese Brazilian.
* [x] C3 checked by a sweep of both chapters, both editions, for `[~]` and "first edit" / "primeira edição": no sentence says a resumed `/propose` marks its line again.
* [x] No "no longer", "now" or other before-and-after wording of the kit; no em dash.
* [x] The chapters still open with what the reader can do; no filler, nothing useful cut; no number added; no private case used, so no approval needed (docs/00 OD-3).
* [x] `make verify` green, with its time said.
* [x] Delivery review by a context that did not write the change (docs/05 §5).
* [x] `make book` and the paths of both PDFs: run once by the driver session for the whole milestone run, not by this delivery (driver's word).

## Outcome

Built by /apply on 2026-11-14 on trunk, on the same word of the author relayed by the driver session: every decision is the agent's, taken alone (docs/05 §4), and the page was built before the person read it. The driver session stages and commits.

**What changed.** Chapter 12 `:27` and chapter 19 `:360`, both editions, one sentence each; nothing else in the four files. No document, ADR or docs/03 row changes.

**Divergence from C1 and C2, from the review.** Two fixes to what this delivery built, decided by the agent:

* Portuguese "no seu próprio branch" became "no branch dela" in both chapters: with `/propose` as the subject, "seu" read as the command's branch, not the delivery's.
* C1's reason was shortened in both editions to "since the main branch's `work/` lacks every page not yet merged" / "já que o `work/` do branch principal não tem nenhuma página ainda sem merge": "with a branch or a worktree per delivery" is implied by "on its own branch", and `:29` already says how the main branch shows a line until its merge.

**C3.** Checked, no change: chapter 12 `:31` and `:32` already teach that the first edit marks a `[ ]` line `[~]` and a resumed line keeps its mark; chapter 19 never says a resumed `/propose` marks its line. The sweep's other "first edit" / "primeira edição" hits (chapter 19 `:100`, `:218`, `:394`) are `/apply`'s.

**Proof.** `make verify` green in 46 seconds, and again in 44 after the review's fixes (ceiling five minutes). `make book` is left to the driver session, which builds once for the run.

**Delivery review** (docs/05 §5): one read-only agent on Opus read the diff of the four chapter files against this page, docs/04 and the installed propose skill. It found C1 and C2 word for word, both chapters true to the skill, C2's batch sentence still true on a branch (the page is uncommitted in its worktree when the other starts), no em dash and no before-and-after wording. Its one fix (the Portuguese "seu") and one optional shortening were both taken, above; its third, "on its branch" for "on its own branch" in chapter 19, was not, since the English follows the skill's words.

```commit
docs(ch12-pages-on-branches): /propose reads pages on their branch

- Chapter 12: /propose reads the page of each delivery in flight, in
  work/ or on its own branch, since main's work/ lacks unmerged pages
- Chapter 19: pages written at once, the same reading, both editions
- Resumed /propose keeping its mark: already taught, checked
- docs/06: ch12-pages-on-branches done

work/done/ch12-pages-on-branches.md
```
