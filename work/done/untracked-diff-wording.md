# untracked-diff-wording

**Objective.** A reader of chapter 8, and of docs/03's untracked file row, knows that a new file never shows in plain `git diff` and shows in `git diff --cached` once it is staged, instead of reading that `git diff` shows it once staged; both editions. Finding R4-2 of `m17-review` (work/done/m17-review.md).

**Decided without the author.** A batch /propose with no question asked; each choice below is the recommended one and names its source.

1. The fault: chapter 8's sentence on item 2 and docs/03's untracked file row say "`git diff` shows nothing of it until it is staged", which reads as if plain `git diff` showed it after. Plain `git diff` compares the working folder with what is staged, so a new file is in it neither before nor after staging; `git diff --cached` compares what is staged with the last commit, and holds the new file once it is staged.
2. `--cached` is not taught before chapter 8 (its first use is chapter 19), so the sentence says in a few words what it shows, "the diff of what is staged" (docs/04, Teach, do not only show).
3. "Never" is the queue line's word. It holds for every command the book teaches; `git add -N`, which makes plain `git diff` show a new file, is taught nowhere in the book and is not mentioned.
4. Chapter 13's sentence on the delivery review, which uses the same words, stays: there "`git diff`" is the subject's "their `git diff`, staged and unstaged", so it already means both diffs, and the reader and the checker marked it safe (work/done/m17-review.md, R4-2). `ch13-four-waits`, another agent's, edits chapter 13.
5. The kit's text is right ("which no diff shows before they are staged"), and so are docs/05 §5's Delivery review slot and docs/03's delivery review row ("no diff shows them until they are staged"): no `kit:` note, no change there.
6. Files other slugs touch, and the order (docs/05 §4 and §6 as they read when /apply runs, since `conflict-same-lines`, applied first, may change how a shared hunk is treated):
   * `book/en/08-install-and-hosts.md` and `book/pt/08-install-and-hosts.md`: `ch15-review-range-order` edits the next sentence, on item 3, in the same hunk; it applies first in the batch's order, so this /apply starts only after its commit, and if its change is still uncommitted in the tree, this /apply follows docs/05 §4 and §6 (today: stop and report). `ch08-report-item-one` (the report block) and `pt-ch08-migration-label` (the pt key point) touch other hunks: stage by hunk if they are in the tree.
   * `docs/03-Domain.md`: this slug edits the untracked file row; `conflict-same-lines` edits the conflict row, `docs03-checker-pt` the candidate and milestone review rows or rows near them, and `docs05-fourth-case-version` the waiting mark row, other agents' slugs, each far enough from this row to be its own hunk: stage this row's hunk alone. If one of them lands in the same hunk, stop and report.
   Line numbers shift as these land; /apply finds each passage by its text.
7. No new docs/03 term, no queue line.

**Behaviour.**

* A reader of chapter 8, §What an update reports, can say which command shows a delivery's new file once it is staged, `git diff --cached`, and that plain `git diff` never does.
* docs/03's untracked file row says the same, and keeps its second half on the delivery review.
* Fails: `grep -n "shows nothing of it until it is staged" book/en/08-install-and-hosts.md docs/03-Domain.md` or `grep -n "não mostra nada dele até ele entrar em stage" book/pt/08-install-and-hosts.md` finds a line.
* Edge: chapter 13 still holds its sentence (decision 4); the Behaviour's greps do not read it.

**Contract.**

`book/en/08-install-and-hosts.md`, the sentence on item 2, whole:

```
Item 2 has the delivery review read the files the delivery created as well as its `git diff`: a new file is untracked, one git does not hold yet, so plain `git diff` never shows it, and `git diff --cached`, the diff of what is staged, holds it only once it is staged, and `/apply` stages after the review.
```

`book/pt/08-install-and-hosts.md`, the sentence on item 2, whole:

```
O item 2 faz a revisão da entrega ler os arquivos que a entrega criou, além do seu `git diff`: um arquivo novo é não rastreado, um que o git ainda não guarda, então o `git diff` sem opções nunca o mostra, e o `git diff --cached`, o diff do que está em stage, só o traz depois que ele entra em stage, e o `/apply` põe em stage depois da revisão.
```

`docs/03-Domain.md`, the untracked file row, whole:

```
| untracked file | arquivo não rastreado | `git status`, `??` | A file in the working folder that git does not hold yet: no commit has it, plain `git diff` never shows it, and `git diff --cached` shows it only once it is staged; a delivery's new files are untracked while its delivery review runs, so the review opens them. |
```

Terms: untracked file (arquivo não rastreado), stage (stage), delivery review (revisão da entrega), docs/03.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Out of scope.**

* Chapter 13's sentence: decision 4.
* `git add -N`: decision 3.
* The report block's item 2 ("which no diff shows until they are staged"), docs/05 §5 and docs/03's delivery review row: true as written (decision 5).

**Done when.**

* [x] Chapter 8, in both editions, and docs/03's row carry the Contract's text.
* [x] The Behaviour's greps find nothing.
* [x] No number, no private case, no em dash, no narrated run in the new text.
* [x] `make verify` green.
* [x] The delivery review run as docs/05 §5 says, on this delivery's hunks of the three files and this page.
* [x] `make book`, and the paths of both PDFs given to the author (docs/05 §5, Proof of a screen).
* [x] Page in `work/done/`, line `[x]`, staged by hunk where the files hold other deliveries' changes (decision 6), commit message in a `commit` block.

Queue line, as it stands in docs/06:

```
[~] untracked-diff-wording   chapter 8 and docs/03's untracked file row say a new file shows in `git diff --cached` once staged and never in plain `git diff`; both editions
```

**Built.** Chapter 8, §What an update reports, both editions: the sentence on item 2 is the Contract's, saying plain `git diff` never shows a new file and `git diff --cached`, glossed as the diff of what is staged, holds it once it is staged. docs/03's untracked file row is the Contract's, its second half on the delivery review kept. Chapter 13 unchanged (decision 4). The Behaviour's greps find nothing.

**Decisions at apply time.** `ch15-review-range-order` and `ch08-report-item-one` were committed before this /apply began, so the shared hunk held no other delivery's change. `make book` is run once by the batch driver at the end of the parallel run; staging is the driver's, from the paths this delivery reports. No Case A or Case B passage.

**Divergences and omissions.** None.

**Proof.** `make verify` green (build, parity, em dash, prose, width, links, disclosure).

**Delivery review.** One read-only agent on Opus read this delivery's hunks of the three files against this page and docs/04. No finding breaks the page or docs/04: the text matches the Contract in both editions and docs/03, the git is right, `--cached` is glossed where it first appears, the Portuguese reads naturally with the chapter's terms. Two nits left as they are: the sentence's three "and" clauses (the Contract fixes the text), and a staged new file edited again showing its later edits in plain `git diff` (the sentence's "it" is the untracked file, the same edge as decision 3).

```commit
docs(untracked-diff-wording): say a new file shows only in git diff --cached

- Chapter 8's item 2 sentence and docs/03's untracked file row say plain `git diff` never shows a new file and `git diff --cached` shows it once it is staged
- Both editions

work/done/untracked-diff-wording.md
```
