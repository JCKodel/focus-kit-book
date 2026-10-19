# ch08-13-17-next-line

**Objective.** After chapters 8, 13, 17 and 23 a reader can say that, with a branch or a worktree per delivery, the update's next command, `/apply`'s `after` and next free line, and the manager's "where are we" take each slug's line from its worktree or branch, local or remote, reconciled by slug, because the main branch shows each line as it was until its merge; on trunk they read the one queue of the folder; both editions, least change. This answers m22-review's candidates 1, 7 and 8 (`work/done/m22-review.md`, Findings).

**Behaviour.** What the reader can do or explain after each chapter:

* Chapter 8, "What an update reports": say where the update reads the first free line whose command it names: on trunk, the queue of the folder; with a branch or a worktree per delivery, each slug's line from its worktree or branch, reconciled by slug (chapter 14).
* Chapter 13, "What `/apply` does": say where `/apply` reads the lines its `after` names before it starts and the lines it weighs for the next free line when it ends, the same way, trunk first.
* Chapter 17, "The manager's session": say why the answer to "where are we?" reads each slug's line where it lives off trunk, with the lending library's `return-book` / `devolver-livro` as the example already in the section: from the main branch's copy alone it would read `[ ]`, and "In flight" / "Em andamento" would miss the build under way. The Key points' manager bullet says the same in a clause.
* Chapter 23, "Roles in a team": the manager's bullet says the queue it asks is read on trunk in its one file and with a branch or a worktree per delivery from each slug's worktree or branch.
* Edge: a reader on trunk reads nothing that sends them to a branch: every changed sentence puts trunk first.
* Fails if: a sentence says or implies that an `[x]` only on an unmerged branch meets an `after` (chapter 14's to say; these chapters point to it, as chapter 12 does); a sentence names a branch per delivery without the worktree; the text gives a number, version, date, "now", "no longer", "agora" or "não mais", or how the kit read before; it narrates a run; chapter 8's update report (en :70 to :81, pt as it stands), a real report of this repository on trunk, changes; a title changes; the editions differ in order or sense.

**Contract.** Exact wording, both editions, nowhere else in the four chapters. Line numbers are at `838f737`.

* `book/{en,pt}/08-install-and-hosts.md`, "What an update reports" / "O que uma atualização relata": one new line right after en :100 / pt :102 ("It names instead the command docs/06's first free line wants, ..." / "Ela cita em vez disso o comando que a primeira linha livre do docs/06 pede, ..."), before "A version that asks nothing ..." / "Uma versão que não pede nada ...":
  * en: "On trunk that line is read in the queue of the folder; with a branch or a worktree per delivery the main branch shows each line as it was until its merge, so the update reads each slug's line from its worktree or branch, local or remote, and reconciles them by slug ([chapter 14](14-queue-states.md))."
  * pt: "No trunk essa linha é lida na fila da pasta; com um branch ou um worktree por entrega, o branch principal mostra cada linha como estava até o merge dela, então a atualização lê a linha de cada slug no worktree ou no branch dele, local ou remoto, e as reconcilia pelo slug ([capítulo 14](14-queue-states.md))."
* `book/{en,pt}/13-apply.md`, "What `/apply` does" / "O que o `/apply` faz": one new line right after :27 ("So every word on a line is read by every build ... (chapter 11)." / "Por isso, cada palavra de uma linha ... (capítulo 11)."), before :28 ("A file in `work/` does not make a page ready ..." / "Um arquivo em `work/` não deixa ..."); :26 and :27 keep their words, so :27's "So" still follows :26:
  * en: "On trunk it reads the queue of the folder where the session runs; with a branch or a worktree per delivery the main branch shows each line as it was until its merge, so it reads each line its `after` names, and each line it weighs for the next free line, from that slug's worktree or branch, local or remote, and reconciles them by slug (chapter 14)."
  * pt: "No trunk ele lê a fila da pasta onde a sessão roda; com um branch ou um worktree por entrega, o branch principal mostra cada linha como estava até o merge dela, então ele lê cada linha que o seu `after` nomeia, e cada linha que pesa para a próxima linha livre, no worktree ou no branch daquele slug, local ou remoto, e as reconcilia pelo slug (capítulo 14)."
* `book/{en,pt}/17-project-as-assistant.md`:
  * "The manager's session" / "A sessão do gerente", one new line right after :131 ("Every part of it is read from docs/06: ..." / "Cada parte dela é lida do docs/06: ..."), before :132 ("A `[?]` line would appear ..." / "Uma linha `[?]` apareceria ..."):
    * en: "On trunk that is the queue of the folder where the session runs; with a branch or a worktree per delivery the main branch shows each line as it was until its merge, so the session takes each slug's line from its worktree or branch, local or remote, and reconciles them by slug (chapter 14): from the main branch's copy alone, `return-book` would read `[ ]`, and "In flight" would miss the build under way."
    * pt: "No trunk essa é a fila da pasta onde a sessão roda; com um branch ou um worktree por entrega, o branch principal mostra cada linha como estava até o merge dela, então a sessão pega a linha de cada slug no worktree ou no branch dele, local ou remoto, e as reconcilia pelo slug (capítulo 14): só pela cópia do branch principal, `devolver-livro` leria `[ ]`, e "Em andamento" perderia a construção em curso."
  * "Key points" / "Pontos-chave", :150, the manager bullet: "it answers from the queue with the next command" / "ele responde a partir da fila com o próximo comando" becomes:
    * en: "it answers from the queue, read on trunk in its one file and with a branch or a worktree per delivery from each slug's worktree or branch, with the next command"
    * pt: "ele responde a partir da fila, lida no trunk no arquivo único dela e com um branch ou um worktree por entrega no worktree ou no branch de cada slug, com o próximo comando"
    * the rest of the bullet stays.
* `book/{en,pt}/23-adoption.md`, "Roles in a team" / "Papéis num time", :66, the whole bullet becomes:
  * en: "* **The manager** asks the project: what is pending and how it is going, read from the queue, on trunk its one file and with a branch or a worktree per delivery each slug's line from its worktree or branch, and who owes an answer ([chapter 17](17-project-as-assistant.md))."
  * pt: "* **O gerente** pergunta ao projeto: o que está pendente e como está indo, lido da fila, no trunk o arquivo único dela e com um branch ou um worktree por entrega a linha de cada slug no worktree ou no branch dele, e quem deve uma resposta ([capítulo 17](17-project-as-assistant.md))."
* Stays, in both editions: chapter 8's update report (en :70 to :81) and :142; chapter 13 :26, :31, :32, :103, :106, :107, :133, :156 and the Key points (the reading :26 names, which the new line places, is what :31's `after`, :103's `[?]` lines and :107's "the queue's next line" use; :32 and :106 write the delivery's own line, whose place chapter 14 :60 gives); chapter 17 :18, :24 to :25 (they define the states, not where a line is read), :68, :119 (the rules file's own line, as AGENTS.md writes it), the example at :123 to :128 (the library's Git strategy is not stated); every "What the team gains" section, still true since none depends on where a mark is read; every other section and title.
* Terms of docs/03: queue, mark, free line, `after` (dependency), slug, trunk, branch, worktree, main branch; in Portuguese "fila", "marca", "linha livre", "trunk", "branch", "worktree", "branch principal", "local ou remoto", "como estava até o merge", as chapters 12 and 14 write them. No new term.
* Sources: docs/05 §4's board paragraph ("the main branch shows the line as it was until the merge, so whoever reads the queue there, a board or a session picking free lines or resolving an `after`, takes each slug's line from its worktree's file, or from its branch, local or remote, ... reconciled by slug"); chapter 14 en :58 to :64 and :71 to :72 (pt :59 to :65, :72 to :73); chapter 12 :27's sentence, whose shape these follow. No footnote: chapter 14 is the reference, and no number enters.
* Cases: none. Example: the lending library's `return-book` / `devolver-livro`, already in chapter 17's answer, written for that chapter.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no visual change.

**Out of scope.**

* Where `work/` pages in flight sit off trunk: `kit-note-work-in-flight`; the chapters keep the kit's words.
* Whether an `[x]` on an unmerged branch meets an `after`, and the lines only a branch has: chapter 14's, pointed to.
* The review-before-commit sentences, chapter 8 :30 and chapter 13 :210, :213, :259: `ch08-13-20-default-review`, which runs after this line on the same files.
* Chapter 20 (`ch20-merge-and-marks`), chapter 14 (`ch14-face-retired`), chapter 12 (true as `ch12-free-lines-branches` left it).
* docs/03, docs/05, docs/06: no edit; the queue line's marks are the driver's.

**Decisions from the documents.**

* The reading by slug, its reason and its words: docs/05 §4's board paragraph and chapter 14 :58 to :64.
* Trunk first in every changed sentence, and "a branch or a worktree per delivery", never the branch alone: `ch12-free-lines-branches`'s wording rule; this repository is on trunk (ADR-0010).
* A new line after the cited sentence, not a rewrite of it: the precedent of chapter 12 :27 (`ch12-free-lines-branches`).
* No number, version or before/after: AGENTS.md, the book teaches the kit as it is today.

**Decisions taken alone** (the author chose recommended answers):

* Chapter 13's new line goes after :27, not :26, so :27's "So" still follows the sentence it continues; it covers both halves of :26, the `after` at start and the next free line at the end, and :31, :103, :107 stay.
* Chapter 17 gets the reason with the section's own example (`return-book` read `[ ]` from the main branch), as chapter 14 :72 does with `lend-book`; :24 to :25 and :119 stay.
* Chapter 23 gets a clause in the manager bullet, since the queue line names it and the author confirmed candidate 8 with it; the alternative, leaving it true through its pointer to chapter 17, was set aside. "Who owes an answer" stays last, since it comes from the work record, not the queue.
* Chapter 8's report example stays: it is this repository's report, on trunk, and its "first free line" is true there.
* Chapter 13's Key points gain nothing: none of its bullets says where the queue is read.

**Done when.**

* [ ] Both editions changed in the places the Contract names, and nowhere else in the four chapters; Portuguese read as Portuguese, with chapters 12 and 14's words.
* [ ] `grep -n` in each edition shows each new line right after its anchor: ch8 after "first free line wants" / "primeira linha livre do docs/06 pede"; ch13 after the "(chapter 11)" / "(capítulo 11)" line of "What it reads"; ch17 after "Every part of it is read from docs/06" / "Cada parte dela é lida do docs/06".
* [ ] `git diff` of the eight files: 1 insertion in each of chapters 8 and 13, 2 insertions and 1 deletion in chapter 17, 1 insertion and 1 deletion in chapter 23, per edition.
* [ ] Every chapter still opens with its value, its gain section still true, no filler and nothing useful cut; no em dash; no number, version, date, "now", "no longer", "agora", "não mais"; no narrated run.
* [ ] Delivery review as docs/05 §5 says, including that nothing implies an unmerged `[x]` meets an `after`.
* [ ] `make verify` green; `make book` builds both editions and both PDF paths are reported (the driver may run it once for the batch).
* [ ] Only this delivery's paths staged (the driver's in this batch); the page moved to `work/done/` and its commit message suggested.
