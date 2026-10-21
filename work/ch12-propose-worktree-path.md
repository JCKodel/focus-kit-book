# ch12-propose-worktree-path

**Objective.** After chapter 12 the reader who works with a worktree per delivery knows, from the chapter on `/propose` itself, that the session stays in `main/` and writes the mark and the page in the delivery's worktree, and that `/propose` ends by giving that worktree's path, where `/apply`'s fresh session opens; so chapters 8, 12, 13 and 19 give one account of what `/propose` says last: the queue line always, and the worktree's path when there is one.

**Behaviour.** What the reader can do or explain after the chapter:

* Asked "where does `/propose return-book` run when the project gives each delivery a worktree?", answer from chapter 12: in `main/`, which it does not leave; it creates or reuses the worktree, writes the line's `[~]`, the page and later the `[>]` there, and the container's manual is what lets a session in `main/` edit it (chapter 19).
* Say how `/propose` ends: by showing the line's queue line and asking you to read and question the page, then to run `/apply` in a fresh session, opened in the delivery's worktree when there is one, whose path it writes out.
* Edge, trunk: the `lend-book` example keeps its ending, `[>] lend-book ...`, with no path, since on trunk no worktree exists and the fresh session opens in the folder where `/propose` ran; the new words say "when there is one" and the reader of chapter 8, whose example is on trunk, finds no contradiction.
* Edge, a branch per delivery: the session stays in its folder, on the branch `/propose` created; no worktree, no path, and no new sentence says otherwise.
* Edge, the key points: the bullet on `/propose` says the same two things, `main/` for the worktree case and the path at the end, without contradicting chapter 19 :214 ("one in `main/` for each `/propose`, one in each worktree for its `/apply`").
* Edge: no passage names a version, a date, a run or the kit change that brought the path.

**Contract.** One chapter, the same changes in both editions, against the files as they are now: `book/en/12-propose.md` has 177 lines and `book/pt/12-propose.md` 186; :28, :29, :32 and :36 are the same lines in both, and the key point is en :172, pt :181. One sentence per line, as the chapter is laid out. The new line shifts the later ones by one; every cite below is the line as it is now.

* `book/en/12-propose.md` and `book/pt/12-propose.md`:
  * New line after :29 ("Its first edit there marks the line `[~]`..." / "A primeira edição dele ali marca a linha como `[~]`..."), so that :29's "there" / "ali" keeps pointing at the branch or worktree :28 names:
    * en: "With a worktree per delivery the session itself does not move: `/propose` runs in `main/` and writes the mark and the page in the delivery's worktree, which the container's manual lets a session in `main/` edit ([chapter 19](19-worktrees.md))."
    * pt: "Com um worktree por entrega a própria sessão não se move: o `/propose` roda em `main/` e escreve a marca e a página no worktree da entrega, que o manual do contêiner deixa uma sessão em `main/` editar ([capítulo 19](19-worktrees.md))."
  * :32, en: "...and asking you to read and question the page, then to run `/apply` in a fresh session." becomes "...and asking you to read and question the page, then to run `/apply` in a fresh session, opened in the delivery's worktree when there is one, whose path it writes out."
  * :32, pt: "...e pedindo que você leia e questione a página, e depois rode o `/apply` em uma sessão nova." becomes "...e pedindo que você leia e questione a página, e depois rode o `/apply` em uma sessão nova, aberta no worktree da entrega quando há um, cujo caminho ele escreve por extenso."
  * :36, en: "`/apply` starts in a fresh session, with a clean context, and the page is all it takes..." becomes "`/apply` starts in a fresh session, with a clean context, opened in the delivery's worktree when there is one ([chapter 13](13-apply.md)), and the page is all it takes..."; the rest stays.
  * :36, pt: "O `/apply` começa em uma sessão nova, com o contexto limpo, e a página é tudo o que ele leva..." becomes "O `/apply` começa em uma sessão nova, com o contexto limpo, aberta no worktree da entrega quando há um ([capítulo 13](13-apply.md)), e a página é tudo o que ele leva..."; the rest stays.
  * Key point, en :172:
    * "starts in the delivery's branch or worktree, where the project's Git slot puts one," becomes "starts in the delivery's branch or worktree, where the project's Git slot puts one, a worktree written from a session that stays in `main/`,"
    * "...or `[?]` when the scope waits, and never writes code." becomes "...or `[?]` when the scope waits, never writes code, and ends by giving, with a worktree per delivery, the worktree's path, where `/apply`'s fresh session opens."
  * Key point, pt :181:
    * "começa no branch ou worktree da entrega, onde o slot Git do projeto põe um," becomes "começa no branch ou worktree da entrega, onde o slot Git do projeto põe um, um worktree escrito de uma sessão que fica em `main/`,"
    * "...ou `[?]` quando o escopo espera, e nunca escreve código." becomes "...ou `[?]` quando o escopo espera, nunca escreve código, e termina dando, com um worktree por entrega, o caminho do worktree, onde abre a sessão nova do `/apply`."
  * Nothing else in the chapter changes.
* Terms of docs/03: worktree (:94), container folder (:95), manual (:119). No new term and no row changed: "the container's manual" is a `manual` of a `container folder`, as `work/done/ch13-19-session-folder.md` reasoned.
* Sources: the installed `.claude/skills/propose/SKILL.md` at 2026.10.20.2, its last sentence ("then run `/apply <slug>` in a fresh session, written as this host invokes commands, opened in the delivery's worktree, if any, its path written out"); chapter 19 :135 ("since `/propose` runs there and writes the page in the delivery's worktree"), :197 ("`/propose` ends by giving that folder's path") and :214; chapter 13 :19, which holds the reason the session opens in the worktree. The first occurrence of the rule is chapter 19 (`ch13-19-session-folder`); chapter 12 points to chapters 19 and 13 instead of teaching the reason a third time.
* Cases: none. No number.
* Neighbouring lines: `ch08-worktree-slot-manual` (chapter 8) and `m26-records-claims` (records in `work/done/`), in flight beside this one, touch no file of this delivery. Later in queue order, M27's `ch12-14-18-several-slugs` edits chapter 12 and finds these sentences as this delivery leaves them.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no visual change.

**Out of scope.**

* :37, "`/propose` itself runs where you choose": it answers a different question, the conversation that asked for the change or a fresh session, not the folder; with the new line two lines above it, it still reads true in every Git strategy, so it stays.
* :28: it says where the definition starts, the branch or worktree named after the slug, as the propose skill words it ("start or resume the definition in the right branch or worktree"); the new line after :29 says the session stays in `main/`, so :28 keeps its words.
* :27: it already says the main branch's queue is "where it runs".
* The `lend-book` example and the example page: on trunk, with no path to give.
* Chapter 8: `ch08-worktree-slot-manual`'s. Chapters 13 and 19: they already hold the rule. Chapter 10: its steps assume trunk.
* docs/03: no row, as the Contract says.

**Decisions from the documents.**

* `/propose` in `main/`, writing in the worktree, and ending with the path: the installed propose skill and chapter 19 :135, :197 and :214, as the Sources quote them.
* The reason the fresh session opens in the worktree stays in chapters 13 and 19, where `ch13-19-session-folder` put it first; chapter 12 links to them (AGENTS.md, abstraction on the second occurrence).
* Every new clause is scoped to a worktree per delivery ("when there is one", "with a worktree per delivery"), as chapter 12 :28 already separates trunk, branch and worktree.
* Taught as the kit is today, with no version, date or "now" (AGENTS.md, the M21 rule).

**Decisions taken alone.** The agent chose each of these.

* The new sentence goes after :29, not after :28: inserted between them it would leave :29's "there" pointing at `main/`.
* :28 keeps its words rather than being rewritten: the skill says the definition starts "in the right branch or worktree", and the new line resolves the reading that the session moves into it.
* :32 and :36 both change, since the review cites both (C2, C16): :32 gives the path, :36 says where the fresh session opens and links to chapter 13, with no reason repeated.
* The key point keeps its single sentence, adding the `main/` qualifier beside "starts in the delivery's branch or worktree" (C17) and the path at its end (C2).
* The queue line keeps its wording.
* Token `(PA)`: the `after`, `m26-review`, is `[x]`; the lines beside it in flight, `ch08-worktree-slot-manual` and `m26-records-claims`, touch no file of this delivery and this page reads nothing from their pages, so both commands may run beside them.

**Done when.**

* [ ] Both editions changed as the Contract says, and nothing else in the chapter.
* [ ] `grep -c "main/" book/en/12-propose.md book/pt/12-propose.md` prints 2 for each edition (today 0): the new line and the key point.
* [ ] `grep -n "worktree da entrega quando há um\|delivery's worktree when there is one" book/*/12-propose.md` prints :32 and :36 (as they are after the new line, :33 and :37) in each edition.
* [ ] The chapter still opens with its value, no filler and nothing useful cut, no number added, no em dash, no run narration, no version or date in chapter text.
* [ ] `make verify` green.
* [ ] `make book`: left to the driver after the batch; the milestone review records the build.
* [ ] Delivery review by one read-only Opus agent over this page and `git diff HEAD` of the two chapter files, against docs/04 and AGENTS.md.
* [ ] Page moved to `work/done/`, covered by the last verify.
