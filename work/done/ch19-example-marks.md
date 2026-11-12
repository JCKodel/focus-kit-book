# ch19-example-marks

**Objective.** After chapter 19 a reader of the worktree tree example sees `overdue-list` carry the token chapter 14 gives a line whose build shares `src/features/loans/` with a line above it, `(P-)`, waiting for `/apply` as the script prints, and knows how the example's marks reached origin before any delivery was committed: a commit and a push the person made, a step outside the default flow, in which a line shows as the main branch has it until the person commits on its branch and pushes; both editions. Findings R3-8 and R3-5 of `work/done/m32-review.md`.

This page was defined and built by the agent before the author read it, on the author's word that the agent runs the whole queue; the author reads the page and the diff at the end (docs/05 §4).

**Behaviour.**

* Reading chapter 19's tree example (en/pt :202 to :212), the reader finds `[>] overdue-list (P-) · waits: the lines above are done` (pt `lista-de-atrasos`) and `free for /apply, together: none`, where the chapter had `(PA) · apply now` and `overdue-list` free; the other lines of the block are as they were.
* Reading the sentences after it (:214), the reader learns that `overdue-list` is defined and waits, because its build shares `src/features/loans/` (pt `src/features/emprestimos/`) with `return-book`'s, as :97 says, and the `-` holds its `/apply` until every line above is `[x]`, which the script prints as `waits: the lines above are done`, so no line is free for `/apply`.
* Reading :200, the reader finds the example's state saying each mark was committed on its branch and pushed by the person, not "both branches pushed".
* Reading :223, the reader learns that by default no mark reaches origin before the person commits on the delivery's branch and pushes it: `/propose` and `/apply` write each mark in the worktree and commit nothing on their own, and after the claim only the person pushes, or asks for a push; so the example's marks are there by a step of the person's own, outside the default, and without it a line shows as the main branch has it, `[ ] · propose now`, from the claim until that commit and push. :224's claim sentence follows unchanged.
* Edge: :252's "the one exception" (a blocked `/apply`'s partial commit) stays true: the mark commit of the example is the person's own step, outside the default, not a second default exception.
* Edge: `[?]` stays out of the block: its rank against `[>]` is R3-7, dropped, and `ch19-claim-integration`'s (M33).
* Edge, the shared tree: another session may work in the same tree on another line; its files and its docs/06 line are its own (docs/05 §4).
* Fails: a block line not byte for byte the run below; a sentence changed in one edition and not the other; an em dash; a block wider than 74 columns; `make verify` red.

**Contract.**

Sources: `queue.sh` of focus-kit 2026.10.24, as installed in this repository at `914fc75` (`git show 914fc75:.agents/skills/propose/scripts/queue.sh`), with its `claim.sh`, decided by the agent: chapter 19 teaches the tokens of 2026.10.24 until M33's lines, so the installed 2026.11.12 script, which has no token, does not produce this chapter's block. The fixture is `ch19-queue-branches`' scratch repository (its page, Contract) with one change, `overdue-list`'s token `(P-)` instead of `(PA)` (pt `lista-de-atrasos`): a bare origin; on `main`, docs/06 under `## M2. Returns` (`## M2. Devoluções`) holding `[x] lend-book (PA)`, `[ ] return-book (PA) · after lend-book`, `[ ] overdue-list (P-) · after lend-book`, `[ ] m2-review · after return-book, overdue-list`, each with a description; both lines claimed with `claim.sh ... worktree .focus-kit focus-kit/`; `return-book`'s branch committed and pushed at `[*]` with `[ ] damaged-copy (PA)` added above `m2-review`; `overdue-list`'s at `[>]`; run from `main/` with `worktree .focus-kit focus-kit/`. Checked at /propose: the fixture with `(PA)` prints the chapter's present blocks byte for byte in both languages.

English block (:202 to :212), the run:

```
milestone: M2. Returns
[*] return-book (PA) · in flight: apply
[>] overdue-list (P-) · waits: the lines above are done
 └[ ] m2-review + after return-book · waits: after overdue-list

free for /apply, together: none
free for /propose, together: none
only on a branch:
  damaged-copy (return-book)
```

Portuguese block, the run; widest line 70 columns, line 3 59:

```
milestone: M2. Devoluções
[*] devolver-livro (PA) · in flight: apply
[>] lista-de-atrasos (P-) · waits: the lines above are done
 └[ ] m2-review + after devolver-livro · waits: after lista-de-atrasos

free for /apply, together: none
free for /propose, together: none
only on a branch:
  exemplar-danificado (devolver-livro)
```

Prose, `book/en/19-worktrees.md`, three replacements, each anchor once at HEAD `91fde28`:

1. :200 "both branches pushed," becomes "each mark committed on its branch and pushed by you,".
2. :214 "`overdue-list` is free for `/apply`, and" becomes "`overdue-list` is defined and waits, and"; then a new line after it: "`overdue-list` carries `(P-)`, since its build shares `src/features/loans/` with `return-book`'s: the `-` holds its `/apply` until every line above is `[x]`, which the script prints as `waits: the lines above are done`, so no line is free for `/apply`."
3. :223 becomes two lines: "And the tree shows the marks that reached origin, not claims, and by default no mark reaches origin before you commit on the delivery's branch and push it: `/propose` and `/apply` write each mark in the worktree and commit nothing on their own, and after the claim only you push, or ask for a push." and "The marks above reached origin because you committed each line's mark on its branch and pushed it, a step of your own outside the default; without it, from the claim until your commit and push, a line shows as the main branch has it, `[ ] · propose now`."

`book/pt/19-worktrees.md`, the same three:

1. :200 "os dois branches com push," becomes "cada marca com commit no seu branch e push feitos por você,".
2. :214 "`lista-de-atrasos` está livre para o `/apply`, e" becomes "`lista-de-atrasos` está definida e espera, e"; then a new line: "`lista-de-atrasos` leva `(P-)`, já que a construção dela divide `src/features/emprestimos/` com a de `devolver-livro`: o `-` segura o `/apply` dela até toda linha acima estar `[x]`, o que o script imprime como `waits: the lines above are done`, então nenhuma linha está livre para o `/apply`."
3. :223 becomes two lines: "E a árvore mostra as marcas que chegaram ao origin, não reivindicações, e por padrão nenhuma marca chega ao origin antes de você fazer o commit no branch da entrega e o push dele: o `/propose` e o `/apply` escrevem cada marca no worktree e não fazem commit de nada por conta própria, e depois da reivindicação só você faz push, ou pede um." and "As marcas acima chegaram ao origin porque você fez o commit da marca de cada linha no seu branch e o push dele, um passo seu fora do padrão; sem ele, da reivindicação até o seu commit e push, uma linha aparece como o branch principal a tem, `[ ] · propose now`."

Terms of docs/03: none new (parallel token, queue tree, claim). Cases: none. Sources cited: none new.

Decided by the agent, the author corrects it in the review: the token is `(P-)`, chapter 14's reading of the same folder (:98 to :103), not a change of the example's folders; the block comes from 2026.10.24's script at `914fc75`; R3-5 is answered by keeping the example's marks and saying the person committed and pushed them, rather than rebuilding the example on a state the default flow reaches (a `[?]` partial commit would bring R3-7 in).

**Out of scope.**

* :93, :97 to :101, :386 and the key points saying deliveries whose files meet build at once in worktrees, which 2026.10.24's `-` holds in worktrees too: a note for the review, since its fix reshapes the chapter's case for worktrees.
* The claim shown as `propose now` (R3-6) and the rank of `[?]` (R3-7): `ch19-claim-integration` (M33).
* The tokens elsewhere in the book and their removal: M33's lines.
* docs/03, docs/05, ADRs, the kit: unchanged.

**Done when.**

- [x] Both editions changed as the Contract says, nothing else in the chapter.
- [x] Both blocks byte for byte the run of `914fc75`'s `queue.sh` on the fixture, rerun in /apply, and the same fixture with no mark pushed prints both lines `[ ] · propose now`.
- [x] Opens with its value, no filler and nothing useful cut, every number sourced (none new).
- [x] No em dash; blocks within 74 columns.
- [x] `make verify` green; `make book` builds both PDFs, their paths given.
- [x] Delivery review by a read-only Opus agent (docs/05 §5).
- [x] Cases: none, so no approval is needed (docs/00 OD-3).

## Outcome

Built as defined, with two changes from the Delivery review, both in what this delivery wrote:

* :224's second sentence, en "The marks above reached origin because you committed each line's mark on its branch and pushed it, a step of your own outside the default; without it," became "The example's marks got there by that step, yours and outside the default; without it,", since :200 already says the marks were committed and pushed by you; pt "As marcas acima chegaram ao origin porque você fez o commit da marca de cada linha no seu branch e o push dele, um passo seu fora do padrão; sem ele," became "As marcas do exemplo chegaram lá por esse passo, seu e fora do padrão; sem ele,".
* pt :200 "no seu branch" became "no branch da linha", which cannot be read as the reader's branch.

**Proof.** On scratch repositories outside this one, the fixture of the Contract built with `914fc75`'s `queue.sh` and `claim.sh`: with `(PA)`, the run printed the chapter's former blocks byte for byte in both languages, so the fixture is `ch19-queue-branches`'; with `(P-)`, the run printed the chapter's new blocks byte for byte in both languages (`cmp`, after the edits); with no mark pushed, both lines printed `[ ] · propose now`, in both languages. `make verify` green after the last edit, 39.5 seconds wall time (the ceiling is five minutes). `make book` at HEAD `91fde28` with this delivery's changes in the tree built `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.

**Delivery review.** A read-only agent on Opus read the page, docs/04, `git diff HEAD` of both chapter files and the delivery's hunk of docs/06, the chapter around the change and chapter 14's token passage, and `914fc75`'s `queue.sh` lines 89 to 90 for the printed wording. It found the Contract made exactly, the blocks consistent, the Portuguese faithful, no em dash and nothing private; its two findings in this delivery's text are fixed above, and its other two are the note below and a confirmation that :252's "the one exception" holds.

**Decisions taken alone.** Those under Contract, for the author's review; and that the review's call for a line on the worktree tension is a note, since docs/05 §4 calls it grave only when it breaks a clause of the milestone's paragraph, which it does not.

## For the review

* book/en/19-worktrees.md :93, :97 to :101, :386 and the key points (pt the same lines): they say deliveries whose files meet build at once in worktrees, `return-book` and `overdue-list` on `src/features/loans/` "at the same time", while :215, now, shows the same pair waiting, since 2026.10.24's `-` holds `/apply` in worktrees too and 2026.10.25 makes the overlap a conflict before `/apply`'s first edit; a reader sees the chapter's case for worktrees and then the pair not built at once. The person may give it to `ch19-claim-integration` or a line of its own.

```commit
docs(ch19-example-marks): overdue-list (P-) waits; marks pushed by you

- the tree example: overdue-list (P-), waiting, nothing free for /apply
- the marks in origin by the person's commit and push, outside the default
- by default a line shows as main has it until that commit and push
- both blocks rerun with 2026.10.24's queue.sh; both editions

work/done/ch19-example-marks.md
```
