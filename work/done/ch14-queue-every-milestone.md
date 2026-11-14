# ch14-queue-every-milestone

Defined by /propose on 2026-11-14 on the author's word for this run, given on 2026-11-13 and relayed by the driver session: "Precisamos fechar todas as linhas de docs/06-Queue.md sem minha supervisão", close every open line of docs/06 without supervision. So the agent decided alone (docs/05 §4): every choice below is the agent's recommendation and says the agent chose it. This page was written, and will be built, before the person read it; the person reads the page and the diff at the end.

**Objective.** After chapters 13, 14 and 19 the reader can read a queue tree that draws every open milestone, each under its own `milestone:` line, with the free lines and `next:` running across them in the queue's order, so a milestone that waits hides no free line of the next; and, with a worktree per delivery, say that the script reads a delivery's own line from that worktree's file, keeps a branch's line under the main branch's heading, and lets a `[?]` block only on the copy that put it.

**Behaviour.** What the reader can do or explain afterwards, both editions:

* B1. Given chapter 14's new example (C5), the reader says why `next:` is `/propose due-date-format`: milestone 1's only open line, `m1-review`, waits as `[?]` on the person, and the script draws milestone 2 under its own `milestone:` line and offers its first free line.
* B2. The reader says where a later milestone's free line stands among the free lines: after every free line of the milestones above it, in the queue's order, so a line parked under the next milestone is offered, and offered last (chapter 14's "A milestone's end sets priority, not whether a line is free", unchanged).
* B3. The reader tells the error the drawing prevents: in one project, on 2026-11-13, a tree of the first open milestone alone answered `next: none` over a review waiting as `[?]` on an acceptance outside the team, while seven lines of the next milestone were free for `/propose`.
* B4. Given chapter 13's tree after `lend-book` (C2), the reader says why `m2-review` is offered beside `return-book`: chapter 11's milestone 2 is open, its `due-date-format` is `[x]`, so its review may be defined; the two are offered as one command, `/propose return-book m2-review`, and `next:` is `/propose return-book`, the first.
* B5. Given a delivery's own worktree whose session has marked its line `[>]` and committed nothing, the reader says what the script run there shows for that line: `[>]`, read from the folder's own file; and that an `[x]` read there is built, not integrated. Run from `main/`, the same line shows the branch's copy (chapter 19's `claimed, progress unknown` sentence, unchanged here).
* B6. Given a branch that rewords its milestone's heading, moving a date in it, say, and adds a line there, the reader says where the tree shows that line: under the main branch's heading, at the end of that milestone, with the branch named in brackets, not under a heading of its own.
* B7. Given a `[?]` the main branch cleared after a delivery's branch left it, the reader says the line is not blocked: a `[?]` blocks on the copy that put it, a branch's when the branch changed the line after it left the main branch, the main branch's unless the line's own branch changed it, and none once the current copy is `[x]`; with the error of 2026-11-09, a branch opened before the main branch cleared answered questions kept their old `[?]`, and the tree showed two lines waiting on questions already answered.
* B8. Must fail: asked "the first milestone holds only a waiting review, so nothing may run?", the reader answers from chapter 14 that the next milestone's free lines may run, and names the first.
* B9. Must fail: asked "a `[?]` on any copy blocks?", the reader finds no such sentence in chapter 19 and answers with B7.

**Contract.**

Files, decided by the agent: `book/en/13-apply.md`, `book/pt/13-apply.md`, `book/en/14-queue-states.md`, `book/pt/14-queue-states.md`, `book/en/19-worktrees.md`, `book/pt/19-worktrees.md`. The page is widened to chapter 19, as the driver allowed: chapter 19 teaches the worktrees and the reading of lines from branches, holds the one sentence that is now false ("a `[?]` on any copy ... shows the line blocked"), and holds the example of a line only a branch has; the worktree's own line, main's heading and which copy's `[?]` blocks are told once, there, and chapter 14 points to it from its sentence on how the script reads the queue (C4). `ch14-after-never-waits`'s page names this split too (its Out of scope, "Chapter 19's ... is that subject too ... left to it").

Passages are quoted by sentence, since `m38-fixes`, `ch13-apply-after`, `ch14-after-never-waits` and `ch14-open-lines-search` build these files first and move line numbers; line numbers are as of `f28abd1`.

Chapter 13, `## lend-book, built`:

* C1. en :201 "Then, though you did not ask, it runs the queue script and shows its tree, drawn from chapter 11's milestone 1 with `lend-book` now `[x]`, in an example written for this chapter:" / pt :201 "..., desenhada a partir do marco 1 do capítulo 11 com `emprestar-livro` já `[x]`, ...": "chapter 11's milestone 1" becomes "chapter 11's queue, its two milestones," / "da fila do capítulo 11, os seus dois marcos,". The rest stays.
* C2. The tree block under it (en and pt :203 to :211) becomes the run below, byte for byte.
* C3. en :213 "`return-book` is free for `/propose`, as it has been since `lend-book` was `[>]`, and `m1-review`, written `· after all`, waits until `return-book` is defined; the command is `/propose return-book`, in a fresh session, in Claude Code, or `$propose return-book` in Codex (chapter 8's table)." / pt :213 the same sentence: its first part stays up to "is defined"; then: `m2-review`, milestone 2's review, is free for `/propose` too, since `due-date-format` is `[x]`, because the script draws every open milestone and offers its free lines after milestone 1's (chapter 14); so the free lines come as one command, `/propose return-book m2-review`, each slug one more agent, and `next:` names the first, `/propose return-book`, in a fresh session, in Claude Code, or `$propose return-book` in Codex (chapter 8's table). /apply may split it in two sentences, one per line.
* Kept, checked by the agent: the `### Green is not done` bullet "Then, though no one asked, it runs the kit's queue script and shows its tree (chapter 14), what may run next, with its free lines offered as one command ..." (en :141) already says what C3 shows. `ch13-apply-after`'s page leaves the tree and that bullet to this page.

Run for C2, by the agent on 2026-11-14 with the installed `.agents/skills/propose/scripts/queue.sh` (2026.11.13), `fq trunk`, in a fresh `git init` folder in the scratchpad whose `docs/06-Queue.md` held chapter 11's two milestones (en :42 to :54 and :115 to :123, pt :44 to :57 and :118 to :126) with `lend-book` / `emprestar-livro` `[x]` and `due-date-format` / `formato-devolucao` `[x]` (chapter 11 en :174, built there). /apply runs it again and copies its output.

```
milestone: Milestone 1: a librarian lends and takes back
[ ] return-book · propose now
 └[ ] m1-review · waits: return-book not defined

milestone: Milestone 2: loan dates read at a glance
[ ] m2-review · propose now

free for /apply, in order: none
free for /propose, in order: return-book m2-review
next: /propose return-book
```

```
milestone: Marco 1: um bibliotecário empresta e recebe de volta
[ ] devolver-livro · propose now
 └[ ] m1-review · waits: devolver-livro not defined

milestone: Marco 2: datas de empréstimo lidas de relance
[ ] m2-review · propose now

free for /apply, in order: none
free for /propose, in order: devolver-livro m2-review
next: /propose devolver-livro
```

Chapter 14:

* C4. `## What may run now`, en :136 "It draws the current milestone, the first with a line not `[x]`, as a tree, the queue tree: each line not yet `[x]`, ..." / pt :137 "Ele desenha o marco atual, o primeiro com uma linha que não está `[x]`, como uma árvore, ...": it draws every milestone with a line not `[x]`, each under its own `milestone:` line, as a tree, the queue tree / cada marco com uma linha que não está `[x]`, cada um sob a sua própria linha `milestone:`; the rest stays. en :138 / pt :140 "When the milestone holds a line from a finding, two more lines may come between the heading and the tree" becomes "When a milestone holds ..., between its heading and its tree" / "Quando um marco tem ..., entre o título dele e a árvore dele". en :139 / pt :141 "each list in queue order" becomes "each list in queue order across the milestones" / "cada lista na ordem da fila, de um marco ao outro". en :135 "The script reads docs/06 and edits nothing: on trunk the queue of the folder where the session runs, and with a branch or a worktree per delivery, after `git fetch`, each delivery's line from its branch on origin, as the section above says." / pt :136: ends instead "..., as the section above says, and [chapter 19](19-worktrees.md) says which copy counts in a delivery's own worktree, under a heading a branch reworded, and for a `[?]`." / pt "..., como diz a seção acima, e o [capítulo 19](19-worktrees.md) diz qual cópia vale no worktree da própria entrega, sob um título que um branch reescreveu, e para um `[?]`."
* C5. Same section, a new paragraph after en :170 / pt :172 ("`/propose` and `/apply` typed with no slug show the same tree and ask which line to take, and `/apply` ends with it."): a milestone that waits hides no free line of the next one. On the library, with milestone 1's lines integrated, the director wants to try the product before its review is built, so `m1-review` waits as `[?]` with `· resume: apply · blocked: the director tries it on Monday`, the person saying it is blocked; milestone 2, chapter 11's, holds `due-date-format`, not yet defined, and its review. The queue is told in prose, not shown as a block: its `[?]` line does not fit 74 columns, and a queue line is written on one line (docs/05 §4, docs/04's Width of a block). Then the run below, "in an example written for this chapter"; then B1 and B2 in a sentence each; then the error of B3 as evidence, worded so the kit is not compared with an earlier version of itself: "A tree of the first open milestone alone would end at its waiting review: in one project, on 2026-11-13, a tree drawn that way answered `next: none` over a review waiting as `[?]` on an acceptance outside the team, while seven lines of the next milestone were free for `/propose`."
* C6. Key point 3, en "* Asked what may run now, the agent runs the kit's queue script and shows its tree: the current milestone, with `findings:` and its `⚠️` warning under the heading when the milestone holds a line from a finding, each line not `[x]` under the last line it waits on with its state, then the lines free for `/apply` and for `/propose`, in order, and `next:`, the command for the first; ..." / pt :339 the same: "the current milestone, with ... under the heading when the milestone holds" becomes "every open milestone under its own `milestone:` line, with ... under a milestone's heading when it holds"; "in order" becomes "in the queue's order across the milestones, so a milestone that waits hides no free line of the next". The rest stays.
* C7. Opening, first paragraph (en :3 / pt :3): "name the next delivery" becomes "name the next delivery, even past a milestone that waits" / "dizer qual é a próxima entrega, mesmo depois de um marco que espera". Its second paragraph is `ch14-after-never-waits`'s item 1, untouched here.
* C8. `## What the team gains`: one sentence on a line of its own after en :330 "The tree also says how much of the milestone came from findings ..." / pt :332 "A árvore também diz quanto do marco veio de achados ...": "And it draws every open milestone, so a milestone waiting on someone outside the team hides none of the work after it." / "E ela desenha cada marco aberto, então um marco que espera alguém de fora do time não esconde nada do trabalho depois dele." No number: the gain is the next free line named; the count of seven stays in the body, as docs/04 asks of a gain with no figure that sums the chapter. `ch14-after-never-waits`'s item 9 adds its sentence after the line before this one, a different line.

Run for C5, by the agent on 2026-11-14, same script and `fq trunk`, in a fresh `git init` folder each, whose `docs/06-Queue.md` held: under "## Milestone 1: a librarian lends and takes back", `[x] lend-book ...`, `[x] return-book ... · after lend-book` and `[?] m1-review the milestone against its paragraph · after all · resume: apply · blocked: the director tries it on Monday`; under "## Milestone 2: loan dates read at a glance", `[ ] due-date-format the screen shows the due date as day/month/year` and `[ ] m2-review the milestone against its paragraph · after all`. pt: chapter 11's pt heading and slugs (`emprestar-livro`, `devolver-livro`, `formato-devolucao`), and `· blocked: a diretora testa na segunda`. Every printed row is within 74 columns (longest 69).

```
milestone: Milestone 1: a librarian lends and takes back
[?] m1-review · blocked: the director tries it on Monday, then apply

milestone: Milestone 2: loan dates read at a glance
[ ] due-date-format · propose now
 └[ ] m2-review · waits: due-date-format not defined

free for /apply, in order: none
free for /propose, in order: due-date-format
next: /propose due-date-format
```

```
milestone: Marco 1: um bibliotecário empresta e recebe de volta
[?] m1-review · blocked: a diretora testa na segunda, then apply

milestone: Marco 2: datas de empréstimo lidas de relance
[ ] formato-devolucao · propose now
 └[ ] m2-review · waits: formato-devolucao not defined

free for /apply, in order: none
free for /propose, in order: formato-devolucao
next: /propose formato-devolucao
```

Chapter 19, `## Worktrees in the kit`:

* C9. en :200 "The branch's copy of its slug's line is the current one until the branch is merged into the main branch on origin, and the main branch's copy after it, so in `main/` pull after a merge; a `[?]` on any copy, the main branch's or a branch's, shows the line blocked until it is `[x]`." / pt :200 "...; um `[?]` em qualquer cópia, a do branch principal ou a de um branch, mostra a linha travada até ela estar `[x]`.": its last clause becomes B7's rule, a `[?]` blocking on the copy that put it, in the three parts docs/05 §4 gives; then one sentence of evidence: "In one project, on 2026-11-09, a branch opened before the main branch cleared answered questions kept the old `[?]`, and a tree that read a `[?]` on any copy showed two lines waiting on questions already answered." / pt the same, with travada and marca de espera as docs/03 has them. The only count is the changelog's "two lines".
* C10. en :219 "`damaged-copy` is a line `return-book`'s session added on its branch, in no queue of `main/` yet: the script shows it at the end of its milestone, naming in brackets a branch that holds it, and offers it like any other line." / pt :219 (`exemplar-danificado`): one sentence after it, B6: its milestone is the one the main branch's heading names, so a branch that rewords that heading, `M2. Returns, by Friday` say, keeps its lines under `M2. Returns` in the same tree.
* C11. After en :228 "The example's marks got there by that step, yours and outside the default; without it, from the claim until your commit and push, the tree reads the branch alone and prints `[ ] overdue-list · claimed, progress unknown: propose in flight`, free for no command." / pt :228: one sentence, B5: run in the delivery's own worktree, the script reads that delivery's line from the folder's own file, so the session there sees its own marks before any commit or push, and an `[x]` it reads there is built, not integrated. That sentence itself is `ch14-after-never-waits`'s only if it rewrites it; this page adds a new line after it and edits nothing of it. And en :198 "It fetches origin, reads every line from the main branch's copy, `main/`'s own queue when run from `main/` and the default branch on origin when run in a worktree, and each delivery's line from `origin/<prefix><slug>`, and edits nothing." / pt :198 gains, before "and edits nothing", the exception where it stands: "but, in a delivery's own worktree, that delivery's line from the folder's own file" / "mas, no worktree da própria entrega, a linha dela do arquivo da própria pasta", so the two sentences agree.
* C12. Key point 4, en "... reads a branch on origin as the claim and each delivery's line from its branch until the merge, the main branch's copy after it, a `[?]` on any copy blocking, and shows a line only a branch has in its milestone, though it sees no mark not yet pushed; ..." / pt :418 the same: "a `[?]` on any copy blocking" becomes "a `[?]` blocking on the copy that put it, a delivery's own line read from its worktree's file there"; "in its milestone" becomes "in its milestone, under the main branch's heading". The rest stays.
* Kept, checked by the agent: the tree block en and pt :204 to :214, rerun on 2026-11-14 with the installed script, `fq worktree .focus-kit focus-kit/` from `main/` of a scratch container (a bare origin, `main` with `M1. Loans` all `[x]` and `M2. Returns` holding `return-book`, `overdue-list` and `m2-review · after all` at `[ ]`, `focus-kit/return-book` with `[*] return-book` and the added `damaged-copy`, `focus-kit/overdue-list` with `[>] overdue-list`, each pushed), printed byte for byte what the chapter shows. :199's `claimed, progress unknown` sentence is `ch14-after-never-waits`'s (its chapter 19 item).

Checks the agent ran for B5 to B7 on that container, for /apply to rely on and run again: in a worktree `.focus-kit/worktrees/m2-review` on `focus-kit/m2-review`, created from origin's `main` and pushed with nothing committed, a local `[>] m2-review` printed `└[>] m2-review + after return-book · waits: after return-book, overdue-list`, while `main/` printed the same line `claimed, progress unknown: propose in flight`; `focus-kit/overdue-list` rewording `## M2. Returns` to `## M2. Returns, by Friday` and adding `[ ] overdue-email`, `main/` printed `[ ] overdue-email (only on branch overdue-list) · propose now` under `milestone: M2. Returns`; a `M3. Fines` whose `[?] fines` main cleared after `focus-kit/fine-receipt` left it printed `[ ] fines · propose now`.

Terms of docs/03: queue tree (árvore da fila), milestone (marco), waiting mark (marca de espera), blocked reason (motivo da espera), dependency (dependência), worktree, main branch (branch principal), integrated (integrada), as the chapters already use them. No new term. docs/03's queue tree row already says every open milestone under its own `milestone:` line, the free lines across them, the delivery's own line read in its worktree, the `[?]` on the copy that put it and main's heading; the agent checked it and leaves docs/03 as it is.

Sources the text follows: docs/05 §4 :142 to :145 ("show its trees, one per open milestone ... Then come the lines free for /apply and for /propose, in the queue's order across the milestones, and the next one") and :174 to :180 ("A `[?]` blocks on the copy that put it. ... A line only a branch has belongs to its milestone, under main's wording of the heading when the branch reworded it."); the installed `queue.sh`'s header comment; the kit's `CHANGELOG.md` under `## 2026.11.13`, its `queue.sh` entries, for the two errors, told as it words them, with no project named, no place and no business detail (the author's word for this run). No source note: the reader has nothing to open for them, as chapter 14's other dated errors.

Cases drawn on: none; the two errors are the kit's, not Case A or Case B, so docs/05 §5's Case A and Case B slot asks nothing. No number is added but the "seven" of the 2026-11-13 error, from that changelog entry.

**Out of scope.**

* Chapter 14's waiting section, `after` read per command, `queue.sh`'s `waits` for a claimed line (chapter 14 and chapter 19 :199), the opening's second paragraph, key point 4 and the gains sentence on `after`: `ch14-after-never-waits`.
* Chapter 13's `/apply` returning a line to `[>]` with `· after`: `ch13-apply-after`.
* Chapter 12's "the milestone's lines" (en and pt :25): a note on `ch12-propose-after`'s page already; not repeated here.
* The open-lines search tip: `ch14-open-lines-search`.
* Chapter 13's three tests of grave, the marks in its last message and key point 4, chapter 14's `fix-suspended`: `m38-fixes`.
* The `suspension-end` line of `ch13-apply-next`'s note: gone since `ch13-apply-findings` made that flaw a note (its page's decisions); the note's request, the tree run again on the chapter's own queue, is C1 to C3, on chapter 11's two milestones.
* A new output block in chapter 19: the three behaviours are one sentence each, and the chapter's example stays true.
* docs/03: no row is wrong.

**Done when.**

* [x] C1 to C12 written in both editions, English the source, the Portuguese in docs/03's terms.
* [x] The two trees of C2 and C5 run again at /apply with the installed script on scratch queues as this page records, en and pt, and copied byte for byte; every block within 74 columns.
* [x] Chapter 19's tree block rerun as recorded above and still equal to the chapter, or updated from the run.
* [x] No sentence in chapters 13, 14 or 19 says the script draws the current milestone, or that a `[?]` on any copy blocks.
* [x] No "no longer", no version named as a date, no before and after of the kit (docs/04, The kit as it is); the two errors told as evidence, with no project named.
* [x] Each chapter still opens with what the reader can do, and says what the team gains; no filler, nothing useful cut.
* [x] Nothing of `m38-fixes`', `ch13-apply-after`'s, `ch14-after-never-waits`' or `ch14-open-lines-search`'s passages changed; this build runs after theirs, never beside another build of chapters 13, 14 or 19.
* [x] No private case used, so no approval needed (docs/00 OD-3).
* [x] `make verify` green, with its time said.
* [x] `make book` run under the scratchpad lock, and the paths of both PDFs given to the author.

Decided by the agent, the author corrects it in the review:

* The page is widened to chapter 19, where the worktree's own line, main's heading and the `[?]` copy rule are told, and chapter 14 points there.
* Chapter 13's tree is run on chapter 11's whole queue, both milestones, since that is the library's queue at that moment; with milestone 1 alone the tree would print as it does, and would not be what the script prints on the chapter's own queue.
* Chapter 14's new example shows the output only and tells the queue in prose, since a `[?]` line with its suffixes does not fit 74 columns on one line.
* The 2026-11-13 error goes in chapter 14's body, not its gains, which get one sentence with no number.
* Chapter 19's `claimed, progress unknown` sentence is left to `ch14-after-never-waits`, which names it.
* C5 follows chapter 14's own frame, where chapter 11's `due-date-format` is open and free (en :104), not chapter 11's ending, where it is built; C2 follows chapter 13's moment, right after `lend-book`, with chapter 11's ending. The two are different moments of the library, each written for its chapter.

## Outcome

Built by /apply on 2026-11-14 in a fresh session, on trunk, on the author's word for this run ("Precisamos fechar todas as linhas de docs/06-Queue.md sem minha supervisão"), so every decision below is the agent's, and the person reads this page and the diff at the end. The author authorized one commit per slug for this run; the driver session commits this delivery with the message below, and never pushes.

Before the build: the line was `[>]`, its `after kit-2026-11-13` integrated; the driver's rewording of the line to "chapters 13, 14 and 19", as this page widened it, was in the working tree and is part of this delivery. `m38-fixes`, `ch13-apply-after`, `ch14-after-never-waits` and `ch14-open-lines-search` had changed the three chapters since the page was written; every passage was found again by its quoted sentence, and none of their passages was changed. No other build was in flight.

What was built, both editions: C1 to C12 as the Contract says, with the review's fixes below.

Proof, all with the installed `queue.sh` (2026.11.13), each output compared with the chapter's block by `diff`, not by eye:

* C2 (chapter 13) and C5 (chapter 14), en and pt, rerun on fresh scratch queues as the Contract records them: byte for byte the page's runs, and now the chapters'. Widest rows: 56, 64, 69 and 65 columns.
* Chapter 19's tree, rerun in both editions on fresh scratch containers (`fq worktree .focus-kit focus-kit/` from `main/`): equal to the chapter, unchanged.
* B5 to B7, rerun on the container: in `.focus-kit/worktrees/m2-review`, pushed with nothing committed, a local `[>] m2-review` printed `└[>] m2-review + after return-book · waits: after return-book, overdue-list`, while `main/` printed `claimed, progress unknown: propose in flight`; `focus-kit/overdue-list` rewording `## M2. Returns` to `## M2. Returns, by Friday` and adding `overdue-email` printed `[ ] overdue-email (only on branch overdue-list) · propose now` under `milestone: M2. Returns`; `[?] fines` under `M3. Fines`, cleared on main after `focus-kit/fine-receipt` left it, printed `[?] fines · blocked: ...` before the clearing and `[ ] fines · propose now` after it.
* A search of the six files for "current milestone", "marco atual", "any copy" and "qualquer cópia" finds only chapter 19's evidence sentence, which tells the error.
* `make verify` green, 15 seconds before the review's fixes, and green again after them and after this page moved to `work/done/`, in 12 seconds; `make book` built both editions under the scratchpad lock.

Delivery review (docs/05 §5): one read-only agent on Opus, given the six chapters' diff, this line's hunk of docs/06, this page and docs/04. It found nothing wrong; of its four unclear and three style candidates, all in what this delivery wrote, the agent fixed six:

* Chapter 14's new example said only `lend-book` and `return-book` were integrated, while the chapter's own milestone 1 holds more lines; it now says every other line of milestone 1 is integrated and the review is defined, `[>]`, which its `resume: apply` implies.
* C4's sentence linked chapter 19 a second time, five lines after the section's link, against docs/04's once-per-target rule, and said "which copy" for a heading; it now names chapter 19 in plain text and says "which heading counts when a branch rewords one". A divergence from C4's wording, decided by the agent.
* Chapter 19's new B5 sentence read as contradicting the sentence before it, `ch14-after-never-waits`'s, which names no folder; the new sentence now opens "That is the tree from `main/` or another worktree;", leaving that sentence untouched.
* Chapter 13's C3 sentence stacked two reasons; split in two.
* Chapter 19's 2026-11-09 sentence ("cleared answered questions") read twice; now "took the `[?]` off lines whose questions were answered".
* C8's gain sentence began "And" right before another "And"; now "Every open milestone is drawn, ...".

The seventh, chapter 13's library a moment ahead of chapter 14's, is the page's own decision and is left to the author, below.

Divergences: C4's pointer and wording, above. Nothing dropped. docs/03 unchanged, as the page decided: its queue tree row already says all of it.

## For the review

* `book/en/14-queue-states.md:104` / `book/pt/14-queue-states.md:105`: "Chapter 11's `due-date-format` sits under milestone 2, below `m1-review`, and names no `after`: it is free, and does not wait for `m1-review`." Chapter 11 (en :174, pt :179) ends with that line `[x]`, built; a reader who follows the library from chapter 11 reads a built line called free. The person may add "a line like" or move the sentence to a line still open.
* `book/en/08-install-and-hosts.md:159` / `book/pt/08-install-and-hosts.md:160`: "the queue tree, the milestone's lines with their states and the lines free to run" / "a árvore da fila, as linhas do marco com os seus estados e as linhas livres para rodar": the tree holds every open milestone's lines; a reader of chapter 8 expects one milestone. Not grave: chapter 14 says it whole. Same as chapter 12's :25, noted on `ch12-propose-after`'s page.
* `book/en/13-apply.md:224` against `book/en/14-queue-states.md:110` and `:179` (pt :224, :111, :181): chapter 13's tree has `due-date-format` `[x]` right after `lend-book` is built, while chapter 14, the next chapter, has it free and not yet defined, with milestone 1 further on; a reader going from 13 to 14 sees the library move back. The page decided the two are different moments, each written for its chapter (Decided by the agent); the person may keep it, or tell chapter 14's two examples as a line like `due-date-format`.

```commit
docs(ch14-queue-every-milestone): the tree draws every open milestone

- chapter 13's tree after lend-book run again on chapter 11's two milestones
- chapter 14: every open milestone drawn, free lines across them, next: none of 2026-11-13
- chapter 19: own worktree's line, main's heading, a [?] blocks on its copy
- the 2026-11-09 inherited [?] told as the error; both editions

work/done/ch14-queue-every-milestone.md
```
