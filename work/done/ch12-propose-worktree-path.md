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

* [x] Both editions changed as the Contract says, and nothing else in the chapter.
* [x] `grep -c "main/" book/en/12-propose.md book/pt/12-propose.md` prints 2 for each edition (today 0): the new line and the key point.
* [x] `grep -n "worktree da entrega quando há um\|delivery's worktree when there is one" book/*/12-propose.md` prints :32 and :36 (as they are after the new line, :33 and :37) in each edition.
* [x] The chapter still opens with its value, no filler and nothing useful cut, no number added, no em dash, no run narration, no version or date in chapter text.
* [x] `make verify` green.
* [x] `make book` exit 0, run by this lane after the second of its three verifies, with both PDF paths (Proof); the definition left it to the driver (Divergences).
* [x] Delivery review by one read-only Opus agent, launched by this lane, over this page and `git diff HEAD` of the two chapter files, given docs/04 and AGENTS.md, which its reply does not name among what it read (Divergences); whether it kept the session's advisor, as docs/05 §5 asks, is not recorded.
* [x] Page moved to `work/done/`, covered by the last verify.

**Divergences.**

* `make book`: the Done when item, as defined, left it to the driver; the batch's rules had this lane run it after the second of its three verifies, and the Proof records it. `m27-records-claims` gave the item the Proof's words.
* The delivery review: its reply lists the diff, this page, the propose skill and lines of chapters 13 and 19 as what it read, and does not name docs/04 or AGENTS.md among them, though its prompt gave both and it checked docs/04's prose rules; nor does it say whether the agent kept the session's advisor. `m27-records-claims` gave the item these words.

**Omissions.** None: every change of the Contract is in both editions, with the wording it gives.

**Decisions taken alone in /apply.**

* The links `([chapter 19](19-worktrees.md))` and `([chapter 13](13-apply.md))` are written as the Contract gives them, though chapter 12's own cross-references are plain "(chapter 14)": linked references are the book's form elsewhere (chapters 8 and 9), and the page names them.
* The review's one observation, that the key point's appositive asks for a careful reading, is left as the Contract words it: the reviewer judged it grammatical and acceptable, so no fix and no queue line.

**Delivery review.** One read-only Opus agent, launched by this lane, over `git diff HEAD` of `book/en/12-propose.md` and `book/pt/12-propose.md` and this page; whether it kept the session's advisor, as docs/05 §5 asks, is not recorded. Its reply, as returned:

> I found nothing to fix in `ch12-propose-worktree-path`.
>
> **What I read**
> - The diff of `book/en/12-propose.md` and `book/pt/12-propose.md` against `HEAD`, and the delivery page.
> - The end of `.claude/skills/propose/SKILL.md`.
> - Chapter 13 at :18, :19, :33 and :274.
> - Chapter 19 at :130 to :137, :195 to :199, :212 to :216 and :366, plus the Portuguese twin's use of "contêiner".
> - Every mention of `main/` and "fresh session" / "sessão nova" in chapter 12, in both editions.
>
> **Findings:** no findings.
>
> - **Matches the Contract:** each edition has 4 lines changed and 1 added, and nothing else changed. Both editions have the same changes. Line counts are now 178 (en) and 187 (pt), and `grep -c "main/"` gives 2 in each, as the Done-when expects.
> - **True against the sources:**
>   - The new line :30 matches the skill's last sentence ("opened in the delivery's worktree, if any, its path written out") and chapter 19 :135, :197 and :214.
>   - :33 and :37 match chapter 13 :19 and :274.
>   - The key point agrees with chapter 19 :214 ("one in `main/` for each `/propose`, one in each worktree for its `/apply`") and with chapter 19 :366.
> - **No conflict elsewhere in chapter 12:**
>   - The new line comes after the "Its first edit there" line, so that line's "there" / "ali" still points at the branch or worktree from :28.
>   - :28 still reads correctly: "stands where... the worktree" is narrowed by :30.
>   - :38's choice between the same conversation and a fresh session still holds.
>   - The trunk `lend-book` ending is kept as it was, and the new clause starts with "when there is one".
> - **Scoped to a worktree per delivery:** every new clause carries "when there is one", "with a worktree per delivery" or `main/`. Nothing new speaks for the branch-per-delivery case.
> - **Grammar:** the key-point sentence still reads correctly after both insertions, in both editions.
> - **Links:** `19-worktrees.md` and `13-apply.md` exist in both editions.
> - **Prose rules:** no em dash in either file, and no version, date, run narration or "now" in the new text.
> - **Portuguese:** reads naturally. "manual do contêiner" matches chapter 19's own term, and "cujo caminho ele escreve por extenso" is idiomatic.
>
> **Observations, no fix needed**
> - In the key point, the appositive "a worktree written from a session that stays in `main/`" / "um worktree escrito de uma sessão que fica em `main/`" is grammatical but asks for a careful reading. It sits right after "puts one", in an already long sentence. It is acceptable as the Contract states it.
> - I did not run `make verify`, because this review was read-only; it is still open on the Done-when list.

No new queue line.

**Proof.** `make verify` was run after the chapter edits, again with the review recorded and the page moved to `work/done/`, and once more after this Proof was written: exit 0 each time, every check passed, the link check included. The Done when greps print 2 `main/` lines per edition (:30, the new line, and :173 en, :182 pt, the key point) and the "when there is one" clause at :33 and :37 in each edition; the chapter has 178 lines in English and 187 in Portuguese. This lane ran `make book` after the second verify, before its commit `818011e`; the tree's HEAD and what it held of the other lanes' files are not recorded. Exit 0, both editions: `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`. Nothing pushed; no environment changes.

```commit
docs(ch12-propose-worktree-path): /propose stays in main/, gives path

- ch12: with a worktree per delivery, /propose writes it from main/
- ch12: /propose ends with the worktree's path for /apply's session
- ch12: key point says both; links to chapters 13 and 19
- both editions

work/done/ch12-propose-worktree-path.md
```
