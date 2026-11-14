# m39-fixes

Defined before the author read it: the author's word for this run, relayed by the session that runs the queue on the author's behalf on 2026-11-13, is "Precisamos fechar todas as linhas de docs/06-Queue.md sem minha supervisão" (close every open line of docs/06 without supervision), and for the reviews "Todas, médios entram" (every medium finding enters the one fixes line). So each question the documents leave open is answered by the agent's recommendation, marked "decided by the agent, the author corrects it in the review" (docs/05 §4, a command that says to decide alone).

**Objective.** After this delivery a reader who follows the lending library from chapter 11 to chapter 14 reads one story of `due-date-format`; chapters 8 and 12 say that the tree shows every open milestone; chapters 12, 14 and 19 never say that a line held by `after` waits, beside the rule that it is not waiting; the English PDF prints chapter 14's `grep` command whole, ready to copy; and chapter 21's opening promises what its body and key point teach.

**Behaviour.** What the reader can do or explain afterwards, one group per medium finding of `work/done/m39-review.md` (its numbering, M1 to M5):

* M1 (`due-date-format`). Reading chapters 11, 13 and 14 in order, the reader meets `due-date-format` built in chapter 11 and `[x]` in chapter 13's tree and in chapter 14; no sentence or tree of chapter 14 calls it free or not yet defined.
* M1: from chapter 14's "A milestone's end sets priority" paragraph alone, the reader says that chapter 11's `m2-review` is free for `/propose` whatever `m1-review`'s mark, because its `after all` names only the lines above it in milestone 2.
* M1: chapter 14's every-milestone example still shows a milestone that waits hiding no free line of the next: `m1-review` `[?]`, milestone 2 drawn under its own `milestone:` line, `next: /propose m2-review`, the tree being the installed `queue.sh`'s real output on the queue this page records.
* M1, edge: chapters 11 and 13 are unchanged; chapter 13's offer `/propose return-book m2-review` reads forward into chapter 14's example, where `return-book` is integrated and `m2-review` is still not defined.
* M2 (the trees). From chapter 8 or chapter 12 alone, the reader says that `/apply` ends with, and `/propose` typed with no slug shows, every open milestone's lines with their states, not one milestone's.
* M3 (`after` is not a wait). In chapters 12, 14 and 19, both editions, no sentence makes a line held by `after` the subject of waiting ("waits", "still waiting", "keeps ... waiting", "espera", "faz ... esperar"); such a line comes after another, is not free yet, or shows the tree's `waits:`, which chapter 14 names as the tree's word.
* M3, kept: "wait" stays for a `[?]` line and its reason, for a command, a build, a commit, the session or a person that waits, inside the script's output blocks, in the dated errors told as the kit's changelog words them, and in chapter 14's Case A passage (:383 to :384), which is not changed.
* M3, the kit's half: `work/kit-proposals.md` holds entry 15 under "For the next focus-kit version", naming the kit's own sentences that say the same, so the author can take it to the kit; the kit's files, docs/05 and docs/03 are unchanged.
* M4 (the `grep` command). Open the English PDF at chapter 14's note box: `grep -nE '^\[[^x]\]' docs/06-Queue.md` stands on one line, in a code block under the box, and a copy from the PDF runs as printed; the Portuguese PDF the same.
* M4, failure: the expression `^\[[^x]\]`, still inline in the box's first sentence, is drawn whole in both PDFs; if a break falls inside it, /apply rewords that sentence so the expression stays whole (Contract).
* M5 (chapter 21). Chapter 21's opening promises that the reader can say why a finding nothing carries, no line and no note on a page, gets lost, which its Case B story (:87 to :89) and its last key point teach.
* Small 9, met in passing: chapter 21 has five key points.
* In the Portuguese edition, the same, with docs/03's terms (dependência, marca de espera, travada, árvore da fila, achado, nota).

**Contract.** Line numbers en / pt at HEAD `b3afef0`, which for `book/` and `pandoc/` equals m39-review's end `8d5d063` (`git diff 8d5d063 HEAD -- book/ pandoc/` is empty). Each change quotes what it replaces, so a drift is found by the sentence; pt follows en sentence for sentence. The wording below is the agent's proposal; /apply may word it otherwise within what each item says, as long as each sentence stays true against the passages Behaviour names.

*M1, one story of `due-date-format`.* Chapter 11 ends with `[x] due-date-format` (en :174 / pt :179) and chapter 13's tree frees `m2-review` "since `due-date-format` is `[x]`" (:224 / :224); chapter 14 is changed to agree, chapters 11 and 13 are not.

* `book/{en,pt}/14-queue-states.md` en :110 / pt :111.
  * Replaced: "Chapter 11's `due-date-format` sits under milestone 2, below `m1-review`, and names no `after`: it is free, and does not wait for `m1-review`." / "A `formato-devolucao` do capítulo 11 fica sob o marco 2, abaixo de `m1-review`, e não nomeia nenhum `after`: ela está livre, e não espera `m1-review`."
  * Proposed: "Chapter 11's `m2-review` sits under milestone 2, below `m1-review`, and its `after all` names only the lines above it in milestone 2, `due-date-format`, built in that chapter: it is free for `/propose`, whatever `m1-review`'s mark." / "A `m2-review` do capítulo 11 fica sob o marco 2, abaixo de `m1-review`, e o seu `after all` nomeia só as linhas acima dela no marco 2, `formato-devolucao`, construída naquele capítulo: ela está livre para o `/propose`, qualquer que seja a marca de `m1-review`."
  * :111 / :112 ("But the next delivery is the first free line counting down the queue, ...") stays: it holds for `m2-review` as it did for `due-date-format`.
* `book/{en,pt}/14-queue-states.md` en :179 / pt :181, the clause after the `[?]` line's suffix.
  * Replaced: "milestone 2, chapter 11's, holds `due-date-format`, not yet defined, and its review, `· after all`." / "o marco 2, o do capítulo 11, tem `formato-devolucao`, ainda não definida, e a sua revisão, `· after all`."
  * Proposed: "milestone 2, chapter 11's, holds `due-date-format`, built in that chapter, and its review, `· after all`, not yet defined." / "o marco 2, o do capítulo 11, tem `formato-devolucao`, construída naquele capítulo, e a sua revisão, `· after all`, ainda não definida."
* The tree block en :183 to :193 / pt :185 to :195 becomes the installed script's output, run by the agent on 2026-11-14 with `.agents/skills/propose/scripts/queue.sh` (2026.11.13), `fq trunk`, in a fresh `git init` folder in the session's scratchpad whose `docs/06-Queue.md` held chapter 11's two milestones (en :42 to :54 and :115 to :123, pt :44 to :57 and :118 to :126) with every milestone 1 line `[x]` but `[?] m1-review ... · after all · resume: apply · blocked: the director tries it on Monday` (pt `a diretora testa na segunda`) and `due-date-format` / `formato-devolucao` `[x]`. /apply runs it again, en and pt, and copies its output byte for byte. En:

```
milestone: Milestone 1: a librarian lends and takes back
[?] m1-review · blocked: the director tries it on Monday, then apply

milestone: Milestone 2: loan dates read at a glance
[ ] m2-review · propose now

free for /apply, in order: none
free for /propose, in order: m2-review
next: /propose m2-review
```

  Pt: the same with `Marco 1: um bibliotecário empresta e recebe de volta`, `a diretora testa na segunda` and `Marco 2: datas de empréstimo lidas de relance`; the slugs and the script's words unchanged.
* `book/{en,pt}/14-queue-states.md` en :195 / pt :197.
  * Replaced: "`next:` is `/propose due-date-format`." / "o `next:` é `/propose formato-devolucao`."
  * Proposed: "`next:` is `/propose m2-review`." / "o `next:` é `/propose m2-review`." The rest of the sentence stays.
* Checked and kept: :196 / :198 ("A free line of a later milestone comes after every free line ..."), :197 / :199 (the 2026-11-13 error), key point 3 :396 / :398 and the gain :389 / :391 stay true of the new tree; `book/` holds no other "`due-date-format` ... free" or "not defined" (grep at HEAD: chapter 14 :110, :179, :187 to :192, :195 only).

*M2, the trees, one per open milestone.*

* `book/{en,pt}/12-propose.md` :25 / :25.
  * Replaced: "the milestone's lines with their states" / "as linhas do marco com os seus estados".
  * Proposed: "every open milestone's lines with their states" / "as linhas de cada marco aberto com os seus estados".
* `book/{en,pt}/08-install-and-hosts.md` en :159 / pt :160: the same replacement, in "and `/apply` names what may run next, the queue tree, the milestone's lines with their states and the lines free to run." / "e o `/apply` cita o que pode rodar a seguir, a árvore da fila, as linhas do marco com os seus estados e as linhas livres para rodar."
* Kept: chapter 14 :306 / :308 (`findings:` counts one milestone's lines) and chapter 15 :165 / :169 (one milestone's lines at its end): each means one milestone.

*M3, a line held by `after` never told as waiting.* The rule /apply applies, in chapters 12, 14 and 19, both editions: a line held by `after`, or its `after`, is never the subject of "wait" / "esperar", "still waiting" / "ainda espera", or "keeps ... waiting" / "faz ... esperar"; it comes after the other line, is not free yet, or shows the tree's `waits:`. Kept, each with its reason: a `[?]` line, its reason and its card; a command, a build, a commit, the session, a person or a note that waits; the script's output blocks; the dated errors told as the kit's changelog words them (author's word, "Sim, como o changelog"); chapter 14 :383 to :384 / :385 to :386, a Case A passage, whose change would need the author's approval (docs/00 OD-3); chapter 14 :250 / :252, which names `waits:` as the tree's word.

Changed, en / pt, the replaced words and the proposal:

* `12-propose.md` :28 / :28: "it says the same and does not start, since the definition needs those pages, while their code is what `/apply` waits for" / "ele diz o mesmo e não começa, já que a definição precisa dessas páginas, enquanto o código delas é o que o `/apply` espera" → "it names that line and does not start, since the definition needs those pages, while their code is what `/apply` needs" / "ele nomeia essa linha e não começa, já que a definição precisa dessas páginas, enquanto o código delas é o que o `/apply` precisa". The first half, on a `[?]` line, stays.
* `12-propose.md` :158 / :167: "and a line still waiting when the others end is reported to you, not waited for" / "e uma linha que ainda espera quando os outros terminam é relatada a você, não esperada" → "and a line whose `after` does not let it start yet is reported to you when the others end, not waited for" / "e uma linha cujo `after` ainda não a deixa começar é relatada a você quando os outros terminam, não esperada".
* `14-queue-states.md` :5 / :5, the opening: "nor keeps the milestone's review waiting" / "nem faça a revisão do marco esperar" → "nor holds back the milestone's review" / "nem segure a revisão do marco".
* `14-queue-states.md` :102 / :103: "`m1-review` waits, with four lines above it not yet defined" / "`m1-review` espera, com quatro linhas acima dela ainda não definidas" → "`m1-review` is free for neither command, with four lines above it not yet defined" / "`m1-review` não está livre para nenhum dos dois comandos, com quatro linhas acima dela ainda não definidas". "`due-reminder` waits on its reason" stays (`[?]`).
* `14-queue-states.md` :110 / :111: M1's sentence, which drops "does not wait for".
* `14-queue-states.md` :114 / :115: "it says what the line waits on" / "ele diz o que a linha espera" → "it names the line its `after` still needs" / "ele nomeia a linha de que o `after` dela ainda precisa".
* `14-queue-states.md` :142 / :143: "under the last line it waits on, the one furthest down the queue of the pending lines its `after` names" / "sob a última linha que ela espera, a que está mais abaixo na fila entre as linhas pendentes que o `after` dela nomeia" → "under the last pending line its `after` names, the one furthest down the queue" / "sob a última linha pendente que o `after` dela nomeia, a que está mais abaixo na fila"; the rest of each sentence stays, and /apply keeps it reading whole.
* `14-queue-states.md` :143 / :145: "`waits:`, with what it waits on" / "`waits:`, com o que ela espera" → "`waits:`, with what its `after` still needs" / "`waits:`, com o que o seu `after` ainda pede".
* `14-queue-states.md` :171 / :173: "The `└` draws a line under the one it waits on." / "O `└` desenha uma linha sob aquela que ela espera." → "The `└` draws a line under the one it comes after." / "O `└` desenha uma linha sob aquela depois da qual ela vem."
* `14-queue-states.md` :224 / :226: "with its page saying what was built and what it waits on" / "com a página dizendo o que foi construído e o que ela espera" → "with its page saying what was built and which line it needs first" / "com a página dizendo o que foi construído e de qual linha ela precisa antes".
* `14-queue-states.md` :254 / :256: "for as long as its `after` waits" / "enquanto o `after` dela espera" → "for as long as its `after` does not let its next command start" / "enquanto o `after` dela não deixa o próximo comando começar".
* `14-queue-states.md` :325 / :327: "and `reprint-card`, added after it, waits on it" / "e `reimprimir-cartao`, acrescentada depois dela, espera por ela" → "and `reprint-card`, added after it, names it in its `after`" / "e `reimprimir-cartao`, acrescentada depois dela, a nomeia no seu `after`".
* `14-queue-states.md` :338 / :340: "would name the cancelled one too and wait, as `reprint-card` does, on a line only the person's decision clears" / "nomearia também a cancelada e esperaria, como `reimprimir-cartao` espera, por uma linha que só a decisão da pessoa libera" → "would name the cancelled one too and, like `reprint-card`, never be free until the person decides again" / "nomearia também a cancelada e, como `reimprimir-cartao`, nunca ficaria livre até a pessoa decidir de novo".
* `14-queue-states.md` :342 / :344: "so the cancelled line never keeps the review waiting" / "então a linha cancelada nunca faz a revisão esperar" → "so the cancelled line never holds back the review" / "então a linha cancelada nunca segura a revisão".
* `14-queue-states.md` :343 / :345: "and the review waits with it until the person re-decides `reprint-card`" / "e a revisão espera com ela até a pessoa redecidir `reimprimir-cartao`" → "and the review is not free either until the person re-decides `reprint-card`" / "e a revisão também não fica livre até a pessoa redecidir `reimprimir-cartao`".
* `14-queue-states.md` :344 / :346: "the review waits for it like any other line" / "a revisão espera por ela como por qualquer outra linha" → "the review comes after it like after any other line" / "a revisão vem depois dela como de qualquer outra linha".
* `14-queue-states.md` :367 / :369: "they wait their turn, not on anyone" / "esperam a sua vez, não por alguém" → "their `after` is an order, not a wait" / "o `after` delas é uma ordem, não uma espera".
* `14-queue-states.md` :386 / :388, the gain: "each line under what it waits on" / "cada linha sob o que ela espera" → "each line under the one it comes after" / "cada linha sob aquela depois da qual ela vem".
* `14-queue-states.md` :396 / :398, key point 3: "each line not `[x]` under the last line it waits on with its state" / "cada linha que não está `[x]` sob a última linha que ela espera com o seu estado" → "each line not `[x]` under the last line its `after` names, with its state" / "cada linha que não está `[x]` sob a última linha que o seu `after` nomeia, com o seu estado". "so a milestone that waits hides no free line" stays (a `[?]` review).
* `19-worktrees.md` :81 / :81: "on the one that must wait for the other" / "na que precisa esperar a outra" → "on the one that must come after the other" / "na que precisa vir depois da outra".
* `19-worktrees.md` :199 / :199: "once nothing in its `after` is left to wait on, and before that `waits:` with what it waits on" / "quando nada no `after` dela resta a esperar, e antes disso `waits:` com o que ela espera" → "once its `after` lets `/propose` start, and before that `waits:`, the tree's word for an `after` not yet met, with what it still needs" / "quando o `after` dela deixa o `/propose` começar, e antes disso `waits:`, a palavra da árvore para um `after` ainda não cumprido, com o que ela ainda pede".
* `19-worktrees.md` :202 / :202: "and a line whose `after` names it waits with `return-book built, not integrated`, say" / "e uma linha cujo `after` o nomeia espera com `devolver-livro built, not integrated`, por exemplo" → "and a line whose `after` names it shows `waits: return-book built, not integrated`, say" / "e uma linha cujo `after` o nomeia aparece com `waits: devolver-livro built, not integrated`, por exemplo"; /apply checks the state's exact words against the installed `queue.sh` and copies them.

Kept, by the rule above, the other hits of a grep for `wait` (en) and `esper` (pt) at HEAD: chapter 12 :36 / :36 (`[?]`), :37 / :37 (the rule), :197 / :206 (`/propose`, a command); chapter 14 :3 to :4, :13, :15, :27, :33, :49 / :50, :52 / :53, :178 to :179 and :195 / :180 to :181 and :197, :201 to :217 / :203 to :219, :355 / :357, key points 1, 4 and 5 (`[?]`), :97 / :98 (awaiting integration), :101 / :102, :104 / :105, :134 / :135, :172 to :173 / :174 to :175 (a command or a build), :197 / :199 and :339 / :341 (dated errors), :222 / :224 (the rule), :250 / :252 (the tree's word named), :260 / :262 and :285 / :287 (features), :281 / :283 and :388 / :390 (a note), :317 / :319, :382 / :384 and :389 / :391 (`[?]`), :383 to :384 / :385 to :386 (Case A), the output blocks; chapter 19 :9, :50, :261, :375, :378, :394, :420 (a person, a commit, a delivery, a build), :24 (not `[?]`), :201 (the 2026-11-09 error), :356 and pt :260 (`[?]`), pt :267; chapter 12 pt :155 ("esperado", expected). A hit /apply finds that this list does not name is classed by the rule and said in the Outcome.

The kit's half, `work/kit-proposals.md`, a new entry after 14, in that file's form:

> 15. **A line held by `after`, told as waiting** (from m39-review, medium 3). focus-kit 2026.11.13 says "A line that needs another line first is not waiting." (docs/05 §4 of `SETUP.md`'s template) and keeps sentences that say such a line waits: "each line under the last line it waits on, with its state" (the trees), "what it waits on" (a returned line's page), "a line still waiting when the others end is reported, not waited for" (a command typed with several slugs), "the lines that wait on it" (integration, Git slot), and `apply/SKILL.md`'s "A line that waits on another takes it as its `after`". The next version says, in each, that the line comes after the other, or that its `after` does not let its next command start yet, and keeps "wait" for a `[?]` line and `waits:` as the tree's word. docs/05 §4 here keeps the template's words until then, and the copies the kit installs are not edited here; chapters 12, 14 and 19 already word it so (`m39-fixes`).

/apply checks each quoted sentence against the installed `.agents/skills/analyze/references/documents.md` (:170, :313, :371, :404 at HEAD) and `.agents/skills/apply/SKILL.md` (:38 to :39) before writing the entry.

*M4, the `grep` command whole in the PDF.*

* The cause, found by the agent on 2026-11-14 in a `git archive HEAD` copy built in the session's scratchpad under the run's lock (272 / 284 pages, as m39-review's build): weasyprint 69.0 breaks a line at every break opportunity Pango's line breaking (UAX #14) finds, and inside `'^\[[^x]\]'` it finds two, between `\` and `[` and between `]` and `\`; `pandoc/pdf.css` sets no `white-space` on inline `code`, so the en line ended after `'^\` and pt's line did not reach it. A probe with the command in a 1pt-wide paragraph broke it, as `pdftotext` printed the fragments, into `grep`, `-nE`, `'^\`, `[[^x]`, `\]'`, `docs/` and `06Queue.md` (a break after `06-`, its hyphen joined by `pdftotext`), the same with `word-break: keep-all` and with `line-break: strict` on `code`; only `white-space: nowrap` kept it whole. `nowrap` on every inline `code` would push the book's longest spans past the line (chapter 19 :197's queue script command, 95 characters, where a code block holds 74 columns), so no `pandoc/pdf.css` rule fixes this one span alone; a code block does, since `pre` wraps only a line longer than the page.
* `book/{en,pt}/14-queue-states.md` en :52 / pt :54, in the note box.
  * Replaced: "or run `grep -nE '^\[[^x]\]' docs/06-Queue.md` in a terminal:" / "ou rode `grep -nE '^\[[^x]\]' docs/06-Queue.md` num terminal:".
  * Proposed: "or run the command under this note in a terminal:" / "ou rode num terminal o comando abaixo desta nota:".
* After the box (en :54 / pt :56), a blank line and a fenced block, no info string, the same in both editions (commands stay as they are, docs/04):

```
grep -nE '^\[[^x]\]' docs/06-Queue.md
```

* The scratch build with these two changes alone set the command whole on one line, in a code block under the box, en p. 158 / pt p. 164, with the same page counts; seen as a page image.
* The box's last sentence keeps "(below)" / "(abaixo)", which points to the queue tree's section; /apply rewords it only if the block makes it read as pointing to the command.
* The box's first sentence keeps `^\[[^x]\]` inline: it is read piece by piece, not copied as a command. If at /apply's build a break falls inside it in either PDF, /apply moves the break by wording within that sentence and says so.
* No toolchain change: `pandoc/`, `scripts/` and docs/01 stay as they are, so docs/05 §5's Proof of a screen does not apply; the chapter's proof is verify, `make book` and both PDF paths.

*M5, chapter 21's opening.*

* `book/{en,pt}/21-beyond-software.md` :4 / :4.
  * Replaced: "You can also say why a finding with no line in a queue gets lost." / "Você também consegue dizer por que um achado sem linha numa fila se perde."
  * Proposed: "You can also say why a finding that nothing carries, no line and no note on a page, gets lost." / "Você também consegue dizer por que um achado que nada carrega, nem linha nem nota numa página, se perde."
  * It agrees with :87 ("The findings had no queue line and no page to carry them.") and the last key point :103; :89, a Case B passage, stays word for word. The opening stays two sentences.
* Small 9, met in passing: `book/{en,pt}/21-beyond-software.md` :101 and :102 / :101 and :102 become one key point.
  * Replaced: "* A question to a person is a delivery too, done when the answer arrives." and "* A database rule is a delivery with a test, enforced where every client meets it." / "* Uma pergunta a uma pessoa também é uma entrega, pronta quando a resposta chega." and "* Uma regra do banco de dados é uma entrega com um teste, garantida onde todo cliente a encontra."
  * Proposed: "* A question to a person is a delivery too, done when the answer arrives, and so is a database rule, with a test, enforced where every client meets it." / "* Uma pergunta a uma pessoa também é uma entrega, pronta quando a resposta chega, e uma regra do banco de dados também, com um teste, garantida onde todo cliente a encontra."

Terms of docs/03: dependency (dependência), waiting mark (marca de espera), blocked (travado), queue tree (árvore da fila), free line (linha livre), milestone review (revisão de marco), finding (achado), note (nota), key points (pontos-chave), opening (abertura). No new term. Sources: `work/done/m39-review.md`'s findings M1 to M5 and small 9; docs/05 §4 (`after all`, the trees, "A line that needs another line first is not waiting."); the installed `queue.sh` for the tree; the scratch build above for M4. No number added; no source note added. Cases: none changed; chapter 14's Case A passage and chapter 21's Case B passage untouched, so docs/05 §5's Case A and Case B slot asks nothing.

**States.** Inapplicable: chapters, no screen.

**Visual reference.** Inapplicable: no screen (docs/05 §5, Design). The PDF of both editions is read as page images for M4.

**Out of scope.**

* Chapters 11 and 13: they already tell `due-date-format` built; chapter 14 is brought to them.
* docs/05 §4 and the kit's installed files: their text is the kit's template, kept equal to it (m39-review's K2); M3's kit half is entry 15 of `work/kit-proposals.md`.
* docs/03 :121 and :124: :121 already says "an order, not a wait"; :124 describes the tree's output, `waits:` included, in the kit's terms, so it follows the kit's next version with docs/05.
* The same wording in chapters 11, 13 and 15 (the note below): M3 stops at the three chapters the finding names, and chapters 11 and 13 stay as M1 keeps them.
* Chapter 14 :383 to :384 / :385 to :386: a Case A passage; a change would wait on the author's approval (docs/00 OD-3), and "keeps no review waiting" there is about a dropped line, read with :342's rewording.
* A `pandoc/pdf.css` rule, or a build step marking short inline code unbreakable: no CSS rule fixes the one span without overflowing the long ones (Contract, M4); a build step is a toolchain change no finding asked for.
* Small 14 (chapter 13 :225's `/propose return-book m2-review` broken after the slash in the en PDF): the same cause, not picked; a code block there would change chapter 13's paragraph, which M1 leaves untouched.
* m39-review's other small findings (6 to 8, 10 to 13, 15 to 31) and the dropped ones: not picked by the author's word; small 9 is met in passing by choice (Decisions).
* No further line: a fix page opens none (docs/05 §8).

**Overlap with the work in flight.** None: M39 holds no other open line, and `queue.sh trunk` shows only this one (`[~] m39-fixes · in flight: propose`, `next: none`).

**Done when.**

* [x] M1 to M5 and small 9 read as the Contract says, in both editions.
* [x] Chapter 14's every-milestone tree run again with the installed `queue.sh` on the scratch queues this page records, en and pt, and copied byte for byte; every block within 74 columns.
* [x] A grep of `book/` finds no "`due-date-format` ... free", "not yet defined" said of it, "the milestone's lines" in chapters 8 and 12, nor their pt twins.
* [x] A grep for `wait` (en) and `esper` (pt) over chapters 12, 14 and 19 finds every hit changed or kept as the Contract's M3 rule says, each new hit classed in the Outcome; the two editions agree hit for hit.
* [x] `work/kit-proposals.md` holds entry 15 as the Contract gives it, each quoted kit sentence checked against the installed files.
* [x] `make book` under the run's lock builds both editions, each contents on one page, page counts recorded; the PDF pages of chapter 14's note box, en and pt, rendered to images in the session's scratchpad and opened: the command whole on one line in its code block, and every `^\[[^x]\]` drawn whole; the paths of both PDFs given to the author.
* [x] Both editions written; opens with its value; no filler and nothing useful cut; no number added; no em dash; no run narration; no source note added; chapter 21 :89 (Case B) and chapter 14 :383 to :384 (Case A) untouched; chapter 21 with five key points.
* [x] `make verify` green after the last edit, with its time against the five-minute ceiling; the disclosure scan green.
* [x] Delivery review by one read-only Opus agent, as docs/05 §5 says, over this delivery's paths and this line's docs/06 hunk; only those staged; the page in `work/done/` and its commit message suggested. The author authorized one commit per slug for this run; the driver session commits this delivery with the message /apply writes, and never pushes.

**Decisions.**

* Decided by the agent, the author corrects it in the review: M1 brings chapter 14 to chapters 11 and 13, not the other way, and swaps the free line of its examples for `m2-review`, whose `after all` reaches only milestone 2; so the library reads in one order (built in 11, `m2-review` offered in 13, still undefined in 14), and the sentence also teaches that `after all` stops at its milestone. Telling chapter 14's line as "a line like `due-date-format`" (the review's other option) was dropped: it keeps a second, undefined twin of a built line beside it.
* Decided by the agent, the author corrects it in the review: M3 is applied as a rule over every sentence of chapters 12, 14 and 19, not only the review's list, since the review's list named examples of one wording and a residue would leave the finding met in part; the sentences that only describe the tree (:142, :143, :171, key point 3, the gain :386) are reworded too, the tree's `waits:` kept as its word, which :250 names.
* Decided by the agent, the author corrects it in the review: the dated errors keep their words (:339 "waited on a line the person had dropped", the kit's `CHANGELOG.md` :224's own words, pt `CHANGELOG.pt.md` :234 "esperava"), by the author's word that they are told as the kit's changelog words them.
* Decided by the agent, the author corrects it in the review: M4 is fixed in the chapter, a code block under the note box, not in `pandoc/pdf.css`, since the scratch probe showed no CSS rule keeps the one span whole without pushing the book's 95-character inline commands past the line. The note box stays one paragraph, as docs/04 defines it; the block follows it, and no sentence follows the block, since the box says before it what the command does and what it finds (docs/04's sentence after an artifact).
* Decided by the agent, the author corrects it in the review: M5 rewords only the opening's promise, to what :87 and the last key point teach, and leaves :89 (Case B) as it is, so nothing waits on the author's approval (docs/00 OD-3).
* Decided by the agent, the author corrects it in the review: small 9 is met in passing, two key points of one kind (a delivery that is not code) joined into one, as the review allowed and `m38-fixes` did with its smalls; small 14 is not, since its cure, a code block, would change chapter 13, which M1 keeps as it is.
* From the documents: the five items and that they are one page (`work/done/m39-review.md`, the author's word; docs/05 §8); `after all` and "A line that needs another line first is not waiting." (docs/05 §4); the note box's form and the commands kept as they are (docs/04); the kit's files and docs/05 left as the kit has them, the note in `work/kit-proposals.md` (m39-review, M3 and Out of scope); Proof of a screen only for a toolchain change (docs/05 §5).

## Outcome

Built on 2026-11-14 before the author read it, on the author's word for this run ("Precisamos fechar todas as linhas de docs/06-Queue.md sem minha supervisão"); every choice below not named by the Contract was decided by the agent, the author corrects it in the review. The author authorized one commit per slug for this run; the driver session commits this delivery with the message below, and never pushes.

*What was built.* M1 to M5 and small 9 as the Contract says, in both editions: chapter 14 (en / pt), chapters 8 and 12 (M2, and M3 in 12), chapter 19 (M3), chapter 21 (M5, small 9), and entry 15 of `work/kit-proposals.md`.

*Divergences from the Contract's wording, each within what its item allows.*

* Chapter 12 pt :28: "aquilo de que o `/apply` precisa" instead of "o que o `/apply` precisa", which drops the preposition "precisar de" asks for.
* Chapter 14 :114 / :115 (M1): "names only the one line above it in milestone 2" / "nomeia só a linha acima dela no marco 2", not "the lines", since milestone 2 holds one line above its review (delivery review, nit 4).
* Chapter 14 :341 / :343 (M3): "not be free until the person decides again" / "não ficaria livre até a pessoa decidir de novo", not "never ... until", which read as a contradiction (delivery review, finding 2).
* Chapter 14 en :347 (M3): "comes after it as after any other line", not "like after" (delivery review, nit 3); pt unchanged.
* Chapter 21 pt :4 (M5): "um achado sem nada que o carregue, nem linha nem nota numa página", not "um achado que nada carrega", which a Portuguese reader takes first as "a finding that carries nothing" (delivery review, finding 1); it echoes the chapter's last key point, "Dê a cada achado algo que o carregue".

*Checks.*

* The every-milestone tree run again by the agent on 2026-11-14 with the installed `.agents/skills/propose/scripts/queue.sh` (2026.11.13), `fq trunk`, in two fresh `git init` folders of the session's scratchpad holding chapter 11's two milestones as the Contract says (milestone 1 all `[x]` but `[?] m1-review ... · after all · resume: apply · blocked: the director tries it on Monday`, pt `a diretora testa na segunda`; `due-date-format` / `formato-devolucao` `[x]`); its output equals the Contract's block byte for byte and was copied into both editions; widest row 65 columns.
* Chapter 19 :202: `waits: return-book built, not integrated` checked against `queue.sh`'s `state()`, which prints `waits: ` and the slug followed by `built, not integrated`.
* Entry 15's quotes checked against the installed `documents.md` (:170, :313, :365, :370 to :371, :403 to :404) and `apply/SKILL.md` (:38 to :39).
* M1 and M2 greps: no "`due-date-format` ... free", no "not yet defined" said of it, no "the milestone's lines" in chapters 8 and 12, nor the pt twins; chapter 13 :224 / :224 still frees `m2-review` "since `due-date-format` is `[x]`", which chapter 14 now agrees with.
* M3 grep, case-insensitive, `wait` (en) and `esper` (pt) over chapters 12, 14 and 19: every hit is changed or kept as the rule says, and the editions agree hit for hit. Hits the Contract's kept list did not name, each classed by the rule: chapter 14 en :202 / pt :204 (the heading "Waiting: `[?]`"), en :356 and :401 / pt :358 and :403 (the board's Waiting column, a `[?]` card), pt :96 ("pôr uma linha em espera", a `[?]` line, which en :95 says as "on hold" with no "wait"); chapter 19 pt :200 and :201 ("marca de espera", docs/03's term for `[?]`, where en says `[?]` with no "wait"); all kept, `[?]`. The grep was read occurrence by occurrence, not line by line, so no hit past a long line's start was missed.
* Kept untouched: chapter 14's Case A passage (en :386 to :387 / pt :388 to :389), chapter 21 :89 (Case B), the dated errors, chapters 11 and 13.
* Chapter 21 has five key points in both editions; its opening stays two sentences.

*Proof.* `make verify` green, disclosure scan included, run after the last edit to `book/` and again after this page's last edit, 12.1 seconds against the five-minute ceiling. `make book` under the run's lock built both editions, each contents on one page: 273 pages en (272 at m39-review's build) and 284 pt; built again after the review's fixes, with the same counts and the command still whole in both. Chapter 14's note box, en p. 158 and pt p. 164, rendered to PNG in the session's scratchpad and opened: `grep -nE '^\[[^x]\]' docs/06-Queue.md` stands whole on one line in its code block under the box, `pdftotext` gives it back byte for byte, and the inline `^\[[^x]\]` of the box's first sentence is drawn whole in both PDFs, so that sentence was not reworded. The box's last sentence keeps "(below)" / "(abaixo)": it names "the queue tree's answer", so it does not read as pointing to the command. PDFs: `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.

*Delivery review.* One read-only agent on Opus over this delivery's paths, this line's docs/06 hunk, this page and docs/04: no must-fix finding; two should-fix wordings (chapter 21 pt :4; chapter 14 :341 / :343) and two nits (chapter 14 en :347; :114 / :115) fixed as above; its nit 5, the box's "(below)" now above a code block, kept for the reason above. It confirmed the Contract met in both editions, the tree's state words against `queue.sh`, entry 15's quotes, the docs/04 rules, and the command whole in both PDFs.

*Environments.* local: `make verify` green and `make book` building both editions; GitHub Pages and GitHub Release unchanged until the author pushes and tags.

## For the review

* `book/en/13-apply.md:223` ("`m1-review`, written `· after all`, waits until `return-book` is defined."), `:50` and `:80` ("what it waits on" for a `[>]` line its `after` holds), `book/en/11-queue-and-milestones.md:90` ("each line under the last line it waits on") and `:95` (the review "waits for the lines above it"), `book/en/15-closing-a-milestone.md:3` ("never keeps it waiting"), `:26` ("does not wait for the review") and `:181` ("As a line it waits its turn"), with their pt twins ("espera"): the wording M3 removes from chapters 12, 14 and 19, found by this /propose's grep; a reader of those chapters meets a line held by `after` told as waiting beside chapter 13 :77's "It is not waiting". Not grave: no sentence puts a `[?]` on a line for another line. The person may apply M3's rule to them in a later delivery.

```commit
docs(m39-fixes): one due-date-format story, after never told as a wait

- Chapter 14 agrees with chapters 11 and 13: due-date-format built, m2-review free
- Chapters 8 and 12 name every open milestone's lines in the trees
- Chapters 12, 14 and 19 tell a line held by after as coming after, not waiting
- Chapter 14's grep command in a code block, whole in both PDFs
- Chapter 21's opening promises what it teaches; entry 15 in kit-proposals

work/done/m39-fixes.md
```
