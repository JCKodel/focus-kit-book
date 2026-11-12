# ch14-key-points-pointers

**Objective.** The author reads chapter 14 and finds five key points, as docs/04's chapter shape says, and reads chapters 8, 12, 13 and 14 and finds none of the forward pointers M32 added beside a pointer to the same chapter that was already there; both editions. Findings R1-3 and R1-5 of `work/done/m32-review.md`.

This page was defined and built by the agent before the author read it, on the author's word that the agent runs the whole queue; the author reads the page and the diff at the end (docs/05 §4).

**Behaviour.**

* Reading chapter 14's `## Key points` (en :242, pt :244), the author counts five bullets in each edition, where there were six; the bullet on a session that ended and a cancelled delivery is now the second half of the first bullet, the six marks, which already said who sets `[x]` with `· dropped: <reason>`; nothing the six bullets said is lost.
* Reading chapter 8, the author finds "the scripts the commands run (chapter 13)" at :24 and "the queue tree, the milestone's lines with their states and the lines free to run" at en :151 / pt :153, with no pointer to chapter 14 in either; the one pointer to chapter 14 left is :102 / :104, there before M32.
* Reading chapter 12, the author finds the queue tree at :25 described in a few words, with no link to chapter 14, and "and says so." at en :157 / pt :166 with no "(chapter 14)"; the pointers to chapter 14 there before M32 stay.
* Reading chapter 13 at :22, the author finds "`/apply` shows what may run now, the same queue tree as `/propose`, and asks which line to build", with no link to chapter 14.
* Reading chapter 14, the author finds no link to chapter 19 at en :125 / pt :126 ("as the section above says" stays, and :120 / :121 still points to chapter 19) and no link to chapter 15 at en :145 / pt :147 (:156 / :158 still points to chapter 15).
* Edge: a pointer back (chapter 14's to chapters 12 and 13 added by M32) is untouched; so is every forward pointer that was there before M32 (Out of scope, and a note for the review).
* Edge: "(PA)" and "local or remote" in chapter 14's key points stay as they are; `ch11-14-after` and `kit-2026-10-25` own them (docs/06, M33).
* Edge, the shared tree: `ch19-example-marks` may run in the same tree on chapter 19; its files and its docs/06 line are its own.
* Fails: an anchor below not found exactly once in its file; a sentence changed in one edition and not the other; a Case A or Case B sentence touched (ch12 :188, ch14 :238); an em dash; `make verify` red.

**Contract.** Sixteen exact replacements, eight per edition, numbered the same in both, each anchor counted once in its file at HEAD `4459d5b`; the rest of each file untouched.

`book/en/08-install-and-hosts.md`:

1. :24 "the scripts the commands run (chapters 13 and 14) go through it" becomes "the scripts the commands run (chapter 13) go through it".
2. :151 "and `/apply` names what may run next, the queue tree ([chapter 14](14-queue-states.md))." becomes "and `/apply` names what may run next, the queue tree, the milestone's lines with their states and the lines free to run."

`book/pt/08-install-and-hosts.md`:

1. :24 "os scripts que os comandos rodam (capítulos 13 e 14) passam por ele" becomes "os scripts que os comandos rodam (capítulo 13) passam por ele".
2. :153 "e o `/apply` cita o que pode rodar a seguir, a árvore da fila ([capítulo 14](14-queue-states.md))." becomes "e o `/apply` cita o que pode rodar a seguir, a árvore da fila, as linhas do marco com os seus estados e as linhas livres para rodar."

`book/en/12-propose.md`:

3. :25 "the queue tree the kit's script draws from docs/06 ([chapter 14](14-queue-states.md)), and asks which line to define." becomes "the queue tree the kit's script draws from docs/06, the milestone's lines with their states and the lines free to run, and asks which line to define."
4. :157 "as one such command, and says so (chapter 14)." becomes "as one such command, and says so."

`book/pt/12-propose.md`:

3. :25 "a árvore da fila que o script do kit desenha a partir do docs/06 ([capítulo 14](14-queue-states.md)), e pergunta qual linha definir." becomes "a árvore da fila que o script do kit desenha a partir do docs/06, as linhas do marco com os seus estados e as linhas livres para rodar, e pergunta qual linha definir."
4. :166 "como um comando assim, e diz isso (capítulo 14)." becomes "como um comando assim, e diz isso."

`book/en/13-apply.md`:

5. :22 "the queue tree of [chapter 14](14-queue-states.md), and asks which line to build." becomes "the same queue tree as `/propose`, and asks which line to build."

`book/pt/13-apply.md`:

5. :22 "a árvore da fila do [capítulo 14](14-queue-states.md), e pergunta qual linha construir." becomes "a mesma árvore da fila do `/propose`, e pergunta qual linha construir."

`book/en/14-queue-states.md`:

6. :125 "as the section above says ([chapter 19](19-worktrees.md))." becomes "as the section above says."
7. :145 "names the delivery that answers each ([chapter 15](15-closing-a-milestone.md)), so it waits" becomes "names the delivery that answers each, so it waits".
8. Key points: the fourth bullet (:247) is removed and the first (:244), which ends "any session sets `[?]`.", ends instead "any session sets `[?]`; a line whose session ended keeps its mark, and its command resumes it on the person's word, inspecting the page, the folder and the index first, and a cancelled delivery's page in `work/done/` says what was built and undone."

`book/pt/14-queue-states.md`:

6. :126 "como diz a seção acima ([capítulo 19](19-worktrees.md))." becomes "como diz a seção acima."
7. :147 "nomeia a entrega que atende cada uma ([capítulo 15](15-closing-a-milestone.md)), então ela espera" becomes "nomeia a entrega que atende cada uma, então ela espera".
8. Pontos-chave: the fourth bullet (:249) is removed and the first (:246), which ends "qualquer sessão põe `[?]`.", ends instead "qualquer sessão põe `[?]`; uma linha cuja sessão terminou mantém a sua marca, e o seu comando a retoma com a palavra da pessoa, inspecionando antes a página, a pasta e o índice, e a página de uma entrega cancelada em `work/done/` diz o que foi construído e desfeito."

Sources: docs/04 :43 ("A pointer forward names a term the reader has not been taught, once per chapter for each target") and :133 ("at most five bullets; every chapter"); `work/done/m32-review.md`, R1-3 and R1-5; `git diff 99d04a5 HEAD` of the eight files, `99d04a5` being m31-review's commit, M32's base, which shows these pointers as M32's (`7d8a0e7` for chapter 8, `0cc0caa` for chapters 12 to 14). No number, no case, no code example.

Terms: queue tree, as docs/03 has it; no row added.

**States.** Inapplicable: a chapter, no screen.

**Visual reference.** Inapplicable: a chapter has no screen (docs/05 §5, Design).

**Out of scope.**

* Forward pointers there before M32 that repeat a target in the same chapter (en counts after this delivery: chapter 8, three to chapter 9 and two to 13; chapter 12, six to 14, four to 19, two to 13; chapter 13, five to 14, nine to 19, two to 15, two to 18; pt the same): older than M32, a note for the review, not this line.
* Pointers back, chapter 14's to chapters 12 and 13: docs/04's rule for them is another.
* Chapters 1, 12, 21 and 24, which also hold more than five key points (`work/done/ch11-14-queue-tree.md`): older than M32 and not named by this line, a note for the review.
* docs/04's two rules: they stay; restating them is the author's (decision 1).
* "(PA)" and "local or remote" in chapter 14: M33's lines.

**Decisions taken by the agent.** Decided by the agent, the author corrects them in the review.

1. Question: fold the chapters, or restate docs/04's rule? Answer: fold the chapters; docs/04 stays. Why: the rule has its history in docs/04 (`author-review-2`, the shape at :133) and only the author restates a rule; the line names that option as the author's.
2. Question: which pointers? Answer: only the forward pointers M32 added to a chapter that already pointed to the same target before M32, by `git diff 99d04a5 HEAD`; a target is the chapter pointed to, linked or in parentheses. This is R1-5's list plus en ch12 :157 / pt :166 ("(chapter 14)", added by `0cc0caa` beside :155's), which the line's words hold. The older repeats are a note.
3. Question: which pointer goes when M32's is the first in its chapter (ch08 :24 and :151 against :102, ch12 :25 against :28)? Answer: M32's, so the chapter reads as it did before M32 for that target; where it was the first naming of the queue tree (ch08 :151, ch12 :25), a few words say what the tree is, as docs/04's "Teach, do not only show" asks; ch13 :22 says it is the same tree as `/propose`'s, which chapter 12 just described.
4. Question: which key points fold? Answer: the fourth into the first; the first already says the person sets `[x]` with `· dropped: <reason>`, so only the resume rule and the cancelled page's content move.

**Done when.**

* [x] Both editions changed as the Contract says, each anchor found once; no other line of the eight chapters changed (two wordings refined after the review, under Outcome).
* [x] Chapter 14 has five key points in each edition.
* [x] Forward pointers per target, rerun after the change, per edition: chapter 8 one to 14 (from three); chapter 12 six to 14 (from eight); chapter 13 five to 14 (from six); chapter 14 one to 15 and one to 19.
* [x] Opens with its value, no filler and nothing useful cut; every number sourced (none added); no private case touched, so no approval needed.
* [x] `make verify` green, with its time.
* [x] `make book` builds both PDFs; their paths given to the author.
* [x] Delivery review by one read-only Opus agent, as docs/05 §5 says, recorded on this page.
* [x] Only this delivery's paths and its docs/06 line staged; page in `work/done/`; commit message suggested.

## Outcome

Built as the Contract says, in both editions, then two wordings refined after the review (below). Chapter 14 has five key points in each edition; the forward pointers per target in chapters 8, 12, 13 and 14 are again what they were at `99d04a5`, M32's base: chapter 8 one to 14 (from three), chapter 12 six to 14 (from eight), chapter 13 five to 14 (from six), chapter 14 one to 15 and one to 19 (from two each); pt the same, counted by a script over both editions.

**Divergences.** Two, both from the Delivery review, in what this delivery built:

* ch08 :24, both editions: "the scripts the commands run (chapter 13)" sent a reader to chapter 13 for scripts of which only the claim script is there. It reads "the scripts the commands run, such as the claim script of chapter 13, go through it" (pt "os scripts que os comandos rodam, como o script de reivindicação do capítulo 13, passam por ele"), still the one pointer to chapter 13 at that place and none to 14.
* pt ch13 :22: "a mesma árvore da fila do `/propose`" could be read as the tree of `/propose`'s queue; it reads "a mesma árvore da fila que o `/propose` mostra".

**Proof.** `make verify` green, 28 seconds (2026-11-12), and green again, 15 seconds, after the review's fixes and the page's move. `make book` at HEAD `4459d5b` with this delivery's changes in the tree built `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.

**Delivery review.** One read-only agent launched with its model set to Opus read the page, docs/04 :38 to :43 and :133, AGENTS.md's rules, `git diff HEAD` of the eight chapters and this line's hunk of docs/06, the context of every changed line in both editions, `git diff 99d04a5 HEAD` and `git log` of the eight files, `work/done/m32-review.md` R1-3 and R1-5, docs/03 :121 and the key-point counts of every chapter; it applied the Contract's anchors to HEAD by script and matched the tree, counted the pointers at the base, at HEAD and in the tree, and ran `make verify`, green, leaving the tree as it was. Its report says it had the advisor and called it once. No blocking finding. Fixed: ch08 :24's pointer for "the scripts" and pt ch13 :22's wording (above), and this page's Out of scope counts, which mixed HEAD and after-delivery bases. Left as they are, judged acceptable by the review: the glosses at ch08 :151 and ch12 :25 stacking one description on the tree, and the length of chapter 14's first key point.

**Decisions.** The four under "Decisions taken by the agent", unchanged by the build; the page was defined and built before the author read it.

## For the review

* ch08 en :36, :42, :120 (pt :122), ch12 en :28 to :155 (pt :28 to :164), ch13 :19 to :252: forward pointers there before M32 repeat a target in the same chapter (counts under Out of scope), which docs/04 :43's "once per chapter for each target" does not allow; a reader meets "(chapter 14)" six times in chapter 12 and "chapter 19" nine times in chapter 13. The author may cut them to one per target or restate the rule.
* Chapters 1 (seven), 12, 21 and 24 (six each), both editions: more key points than docs/04's chapter shape allows (at most five); a reader sees the longer list. The author may fold them or restate the rule.

```commit
docs(ch14-key-points-pointers): five key points, M32's pointers once

- Chapter 14 folds its fourth key point into the first: five, both editions
- Cut the forward pointers M32 added beside one to the same chapter
- Chapters 8, 12 and 13 say what the queue tree is where the link was
- Notes for the review: older repeated pointers, other long key points

work/done/ch14-key-points-pointers.md
```
