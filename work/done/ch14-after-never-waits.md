# ch14-after-never-waits

**Objective.** After chapter 14, the reader can mark a line that needs another first with `· after <slug>` at `[ ]` or `[>]`, whether the need is known when the line is added or found by work already started, never with `[?]`; say the three cases a line waits in; say what reading `after` per command costs; and read the queue tree showing such a line as `waits`.

Defined alone on the author's word for this run, relayed by the driver session: "Precisamos fechar todas as linhas de docs/06-Queue.md sem minha supervisão" (2026-11-13), close every open line of docs/06 without supervision. Every choice below is the agent's, marked "decided by the agent", and the author corrects it in the review (docs/05 §4). Source of the rules: focus-kit `CHANGELOG.md` `## 2026.11.13`, first three entries and the fourth's first sentence; docs/05 §4 (current since `kit-2026-11-13`); the installed `.agents/skills/propose/scripts/queue.sh`.

**Behaviour.** The reader of both editions can:

* Say why a line that needs another is not waiting: it ends `· after <slug>` and keeps the mark that names its next command, so the mark alone says whether `/propose` or `/apply` comes next.
* Given `/apply my-loans` finding mid-build that `lend-book` sets a month-end due date one day early, write the result: `fix-due-date` a `[ ]` line above it ending `· from my-loans`, and `my-loans` back at `[>]` ending `· after lend-book, fix-due-date`, its page saying what was built and what it waits on. Failure: answering `[?] ... · resume: apply · blocked: after fix-due-date` is wrong.
* Given `/propose reservations` finding it needs `search-catalog` first, write `[ ] reservations ... · after search-catalog`, the draft kept.
* Say the three cases of `[?]`: the person says it is blocked; an answer was asked and not given; a milestone review's code reading missed part of its range. Edge: asked "can `· blocked:` name a slug?", the reader answers no, the reason is words, never another line.
* Say the two ways out of `[?]`: the person says so, or the session that records the answer clears it. Failure: "cleared when the last line its `after` names is integrated" is not a way out.
* Read the trunk tree below: `my-loans · waits: after fix-due-date` under `fix-due-date`, `next: /propose fix-due-date`, and `reservations · propose now` under `search-catalog`.
* Say the cost: `after` is read per command, so `reservations` is free for `/propose` as soon as `search-catalog`'s page is complete, not once its code is integrated; where a definition needs the other line built, the project's docs/05 says so, and the queue script does not know it.
* Off trunk (chapter 19): say that a claimed line still `[ ]` on its branch shows `waits:` while its `after` waits, and `claimed, progress unknown: propose in flight` only once nothing is left to wait on.
* On a three-column board, place the returned `my-loans` in Doing with no tag.

**Contract.** Files: `book/{en,pt}/14-queue-states.md`, `book/{en,pt}/19-worktrees.md`, `book/{en,pt}/08-install-and-hosts.md`. The page is widened past chapter 14 to chapters 19 and 8, which also teach the old wait (decided by the agent, as the driver asked); chapter 12's is `ch12-propose-after`'s. Sentences are quoted, since `m38-fixes` and the other M39 lines move line numbers; pt edits the same sentence, in docs/03's Portuguese terms (`dependência`, `marca de espera`, `motivo da espera`, `fase de retomada`).

Chapter 14:

1. Value, second paragraph: "You can also tell an order written with a line, `· after`, read for each command, from a wait found on the way, `[?]`, mark a line that waits with its reason and the phase to resume, and take it out again;" becomes "You can also write that a line needs another first, `· after`, whenever the need is found, read for each command and never a wait, mark a line that waits, `[?]`, in its three cases, with its reason and the phase to resume, and take it out again;".
2. Table: "| `[?]` | waiting | any session, in the four cases below |" becomes "| `[?]` | waiting, never on another line | any session, in the three cases below |" (pt "esperando, nunca outra linha", "nos três casos abaixo").
3. Waiting section: "A line waits in four cases:" becomes "A line waits in three cases, never on another line:"; the bullet "**Another line must be done first, found after work started.** ..." is cut (its story moves to item 5). "The reason goes at the end of the line, in words, `· blocked: <reason>`, or as the lines that must be `[x]` first, `· blocked: after <slug>, <slug>`." becomes "... in words, `· blocked: <reason>`, never another line." The paragraph "`· after` and `· blocked: after` look alike and say different things." and its three sentences are cut (replaced by item 5).
4. Way out: in "The person says so; or the session that records the answer clears it, ...; or it is cleared once the last line its `after` names is integrated, which on trunk is when `/apply` marks that line `[x]`." the last clause is cut; "in one of those three ways" becomes "in one of those two ways".
5. New section after the waiting section, `## A line that needs another` (pt `## Uma linha que precisa de outra`): a line that needs another first is not waiting, ends `· after <slug>` and keeps its mark; known when added, written then (`my-loans` · after `lend-book`); found by work already started, the session adds the slug and returns the line, `[~]` to `[ ]` with the draft kept, `[*]` to `[>]` with its page saying what was built and what it waits on (chapter 13 says what happens to the built files): two edits, the mark by the script, the suffix by the file edit. The two examples of Behaviour. Why not `[?]`, the error as the kit's changelog words it, no project named: "In one project, on 2026-11-13, a session that found two lines needed another first left both at `[?]`, ending `· after <slug> · resume: propose · blocked: after <slug>`: reading the queue, the person could not tell from the mark whether `/propose` or `/apply` came next, and each line said "after" in two ways; another project's queue held four such lines." The tree below, introduced as the library's milestone 1 at that moment, written for this chapter, `lend-book` integrated; one sentence on what to see; the cost; one sentence that off trunk the returned line's branch is still its claim and the tree shows it `waits` (chapter 19). Present tense only (docs/04 "The kit as it is"): no "no longer", no comparison with `blocked: after`, no version.
6. Findings section: "which names it in its `blocked: after`" becomes "which names it in its `after`"; "in its `after` or `blocked: after`" becomes "in its `after`".
7. Board: "`my-loans`, waiting on `fix-due-date` in the middle of its build, would stay in Doing by its `resume: apply`, tagged blocked; resolved, it stays in Doing as `[>]`, not as a `[*]` that no session is building." becomes "`my-loans`, back at `[>]` when its build found it needs `fix-due-date`, stays in Doing with no tag, as `[>]` and not as a `[*]` no session is building: it waits its turn, not on anyone."; it moves below "Either way, resolving the reason removes both suffixes and the tag with them.", which becomes "Resolving the reason removes both suffixes and the tag with them."
8. Key point 4, its part before "a grave finding is a `[ ]` line": `· after` is an order written with the line or by the work that finds the need, `[~]` back to `[ ]` with the draft kept, `[*]` back to `[>]`, never `[?]`, read per command, with docs/05 saying where a definition needs the other line built; a line waits in three cases, the reason in words, `· resume: propose · blocked: what provider?`; then its text from "when the reason is resolved" on, unchanged.
9. Gains: one sentence after "The queue also says which lines can run together: ...": a line that needs another keeps the mark of its next command, so the queue shows no blocked line where nothing went wrong. The Case A sentences stay byte for byte; no Case A passage changes, so docs/05 §5's Case A slot asks nothing.

The tree, run with the installed `queue.sh trunk` on a scratch queue of docs/06 (en: `[x]` catalog, members, lend-book; `[ ] fix-due-date    a month-end due date · from my-loans`; `[>] my-loans        a member's loans · after lend-book, fix-due-date`; `[>] search-catalog`; `[ ] reservations    a member reserves a copy · after search-catalog`; pt the same, docs/03's names). The input is not shown in the chapter: pt's `meus-emprestimos` line runs past 74 columns (decided by the agent). Output en, then pt:

```
milestone: Milestone 1: a librarian lends and takes back
findings: 1 open of 1 from a finding · 3 planned open
[ ] fix-due-date · propose now
 └[>] my-loans · waits: after fix-due-date
[>] search-catalog · apply now
 └[ ] reservations · propose now

free for /apply, in order: search-catalog
free for /propose, in order: fix-due-date reservations
next: /propose fix-due-date
```

```
milestone: Marco 1: um bibliotecário empresta e recebe de volta
findings: 1 open of 1 from a finding · 3 planned open
[ ] corrigir-devolucao · propose now
 └[>] meus-emprestimos · waits: after corrigir-devolucao
[>] buscar-catalogo · apply now
 └[ ] reservas · propose now

free for /apply, in order: buscar-catalogo
free for /propose, in order: corrigir-devolucao reservas
next: /propose corrigir-devolucao
```

Chapter 19: "A branch on origin is the claim: a line whose branch exists is taken, and while the branch's copy still says `[ ]`, since the `[~]` need never be committed, the tree shows it `claimed, progress unknown: propose in flight`." gains: once nothing in its `after` is left to wait on, and `waits:` with what it waits on before that. Proof, run with `queue.sh worktree .focus-kit focus-kit/` from `main/` of a scratch container (bare origin; `return-book` and `overdue-list` claimed, both `[ ]` on their branches, `overdue-list` · after `return-book`): `[ ] overdue-list · waits: return-book not defined`; with `return-book` `[>]` on its branch, `[ ] overdue-list · claimed, progress unknown: propose in flight`; pt the same with `devolver-livro` and `lista-de-atrasos`. Prose only, no new block (decided by the agent).

Chapter 8: "as the book's docs/05 §4 kept its sentence on the four cases a line waits in" becomes "... on the cases a line waits in": docs/05 §4 now says three.

docs/03: no change; its waiting mark, blocked reason, dependency and queue tree rows already say 2026.11.13, and the queue tree row keeps `blocked: after` because the script still reads it in an older queue.

**Out of scope.**

* Chapter 13's stop, `[?]` and dependent-line sentences: `ch13-apply-after`'s.
* Chapter 14's "draws the current milestone", every open milestone, the worktree's own line, main's heading, which copy's `[?]` blocks: `ch14-queue-every-milestone`'s. Chapter 19's "a `[?]` on any copy, the main branch's or a branch's, shows the line blocked until it is `[x]`" is that subject too, though its line names chapters 13 and 14 only; left to it, and reported to the driver.
* Chapter 12's `/propose` marking `[?]` for another line first, and its key point: `ch12-propose-after`'s, `[~]` while this page was written.
* The open-lines search tip: `ch14-open-lines-search`'s.
* `fix-suspended` and chapter 14's other `m38-fixes` items: that page's.
* Chapters 15, 17 and 21's `[?]` passages: each waits on a reason in words, still true.

**Done when.**

* Both editions written, every item above, opening with its value, no filler and nothing useful cut.
* The two trees and the two chapter 19 states rerun at /apply with the installed script and match the chapter byte for byte; every block within 74 columns.
* `grep -rn "blocked: after" book/` finds only the 2026-11-13 error sentence, once per edition; `grep -rn "four cases\|quatro casos" book/` finds nothing.
* Every number sourced: 2026-11-13, two lines and four lines, from the kit's changelog.
* `make verify` green, with its time; `make book` under the run's lock; both PDF paths given.
* Builds of chapter 14 run one at a time: after `m38-fixes`, never beside `ch14-queue-every-milestone` or `ch14-open-lines-search`; chapters 8 and 19 also only here, but chapter 19 may meet `ch14-queue-every-milestone` if it widens.

## Outcome

Built on 2026-11-14 by /apply in a fresh subagent session, on trunk, before the author read the page, on the author's word relayed by the driver session: "Precisamos fechar todas as linhas de docs/06-Queue.md sem minha supervisão" (2026-11-13). Every choice below marked "decided by the agent" is the agent's, for the author to correct in the review. The author authorized one commit per slug for this run; the driver session commits this delivery with the message below, and never pushes.

Base: `296089e` (after `m38-fixes` and `ch12-propose-after`). `git diff f28abd1 HEAD` showed only `m38-fixes`' sentence on `fix-suspended` in chapter 14, which this delivery left as it was; chapter 12's new sentence points to chapter 14 for the reason, which the new section gives. `ch13-apply-after` was being built in the same tree at the same time, on chapter 13 only: no shared file.

What was built, every Contract item, both editions:

* Chapter 14: the opening's second paragraph; the table's `[?]` row; the waiting section with three cases, the reason in words and never another line, the two ways out; the new section `## A line that needs another` (`## Uma linha que precisa de outra`) with the two library examples, the error of 2026-11-13, the tree, one sentence on what to see, the cost and the off-trunk sentence; the findings section's two `after`; the board's `my-loans` with no tag, below "Resolving the reason..."; key point 4; one sentence in the gains. The Case A sentences are byte for byte as they were, so docs/05 §5's Case A slot asks nothing.
* Chapter 19: the claim sentence gains `waits:` before the claim shows `claimed, progress unknown`.
* Chapter 8: "the four cases" becomes "the cases".

Divergences, each decided by the agent:

* The error sentence says "a single line said "after" in two ways" (pt "uma mesma linha dizia"), as the changelog says "one line", where the page wrote "each line".
* The off-trunk sentence in the new section names no "(chapter 19)": chapter 14 already points to chapter 19 once, and docs/04 allows one forward pointer per target per chapter.
* Chapter 19's clause quotes the script's word, `waits: return-book not defined` (pt `devolver-livro`), as a general case "for a line whose `after` names a `return-book` still `[ ]`", since the chapter's own example `overdue-list` names no `after`. Prose only, no new block, as the page said.
* After the tree, one sentence says that `waits:` is the tree's word for an `after` not yet satisfied and that a `[?]` shows `blocked:`, so the tree does not contradict "is not waiting".
* The board's `my-loans` ends "it is queued, not stuck" (pt "ela está na fila, não travada") in place of the page's "it waits its turn, not on anyone", which said "waits" of a line the chapter says is not waiting (from the review).
* pt table row "esperando, nunca por outra linha", not the page's "nunca outra linha", which read as "never another line" (from the review).

Proof:

* The two trees, rerun with the installed `.agents/skills/propose/scripts/queue.sh trunk` on scratch repositories holding the page's queues (en and pt), print the page's blocks byte for byte, and the chapter shows them so.
* Chapter 19's states, rerun with `queue.sh worktree .focus-kit focus-kit/` from `main/` of a scratch clone of a bare origin, `return-book` and `overdue-list` claimed, `overdue-list · after return-book`: both `[ ]` on their branches, `[ ] overdue-list · waits: return-book not defined`; with `return-book` `[>]` on its branch, `[ ] overdue-list · claimed, progress unknown: propose in flight`; pt the same with `devolver-livro` and `lista-de-atrasos`.
* `grep -rn "blocked: after" book/` finds en 14:205 and pt 14:207 only, the error sentence; `grep -rn "four cases\|quatro casos" book/` finds nothing.
* `make verify` green: 14 s before the review, 34 s after its fixes (under the five-minute ceiling).
* `make book` under the run's lock, after the fixes: `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.

Delivery review (docs/05 §5): one read-only agent on Opus read `git diff HEAD` of the six chapter files, this line of docs/06, the page and docs/04, with docs/05 §4, docs/03 and the changelog for the facts. It found no grave flaw, the Contract done, the trees matching and the pointers sound, and six small candidates plus one ambiguity, all in what this delivery changed. Fixed: the tree's lead-in "at that moment" read as the other project's moment, now "once both lines went back" (pt "depois que as duas linhas voltaram"); two sentences after the tree, the `reservations` one cut, since the cost paragraph says it ("as here"); pt table row; pt "isso / disso" repeated; pt "quando quer que" stiff, now "em qualquer momento em que"; the board's "waits"; "a `[ ]` line above it" ambiguous, now naming `my-loans` (pt `meus-emprestimos`). Verify and `make book` ran again after them.

Reported to the driver, not changed: chapter 19's "a `[?]` on any copy, the main branch's or a branch's, shows the line blocked until it is `[x]`" is `ch14-queue-every-milestone`'s subject, though its line names chapters 13 and 14 only.

Done when:

* [x] Both editions written, every item above, opening with its value, no filler and nothing useful cut.
* [x] The two trees and the two chapter 19 states rerun at /apply with the installed script and match the chapter byte for byte; every block within 74 columns.
* [x] `grep -rn "blocked: after" book/` finds only the 2026-11-13 error sentence, once per edition; `grep -rn "four cases\|quatro casos" book/` finds nothing.
* [x] Every number sourced: 2026-11-13, two lines and four lines, from the kit's changelog.
* [x] `make verify` green, with its time; `make book` under the run's lock; both PDF paths given.
* [x] Builds of chapter 14 run one at a time: after `m38-fixes`, beside neither `ch14-queue-every-milestone` nor `ch14-open-lines-search`.

```commit
docs(ch14-after-never-waits): a line needing another keeps its mark

- Chapter 14: [?] in three cases, never on another line
- New section: after added whenever the need is found, its cost, the tree
- Chapter 19: a claimed [ ] line shows waits while its after waits
- Chapter 8: the cases a line waits in, no count
- docs/06: ch14-after-never-waits done

work/done/ch14-after-never-waits.md
```
