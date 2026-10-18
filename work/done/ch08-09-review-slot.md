# ch08-09-review-slot

**Objective.** After chapters 8 and 9 a reader can read the report of an update to focus-kit 2026.10.17 and say what each of its four migrations asks of the project's documents, the Delivery review slot, the Milestone review slot turned into areas and a model, docs/05 §7's exception and §8's code reading by areas, and what the update removed from `.windsurf/skills/`; and, starting a project with `/brainstorm` or `/analyze`, can answer the two questions on review, who reviews a delivery's changes before `/apply` ends and how the milestone review's code reading splits and on which model, or keep their defaults knowingly; both editions.

**Decided without the author.**

1. *The lending library's state before the update.* It ran 2026.10.16.2 and applied the eight migrations chapter 8 shows today, so its docs/05 holds a Milestone review slot that names a command a person launches and §8's short "The review also reads the code" paragraph, and has no Delivery review slot. A rerun at 2026.10.17 then reports four migrations: the missing Delivery review slot, the Milestone review slot that names a command, §7's wording, §8's paragraph (`SETUP.md` §1 step 4 at 2026.10.17, read in the kit's repository; the template in `.claude/skills/analyze/references/documents.md`). AGENTS.md's template and docs/04's pointer did not change, so nothing for them (work/done/kit-2026-10-17.md, Contract "AGENTS.md").
2. *The report keeps its shape.* Installed line, count, numbered items by document and section, closing line, as chapter 8 prints it today; versions stay, since they are the command's output (docs/04 "The kit as it is", its chapter 8 sentence). It is said to be written for the chapter, as today (docs/04 "Evidence").
3. *A `Removed:` line.* Yes, one line: the kit's six files in `.windsurf/skills/` (four `SKILL.md`, two `references/documents.md`), nothing else there, since every version before 2026.10.17 wrote them and the update removes them (`SETUP.md` §1 step 3; kit-2026-10-17 "What happened" counted the same six). One self-contained clause after the block explains it with no pointer to the hosts section, because `ch08-10-devin-desktop` may land after this line and today's table still has a Windsurf row; the clause says only what holds either way: the folder is one the setup file does not write, and a file of the reader's own there is reported and left.
4. *Item 1's proposed wording: a read-only agent on the session's model.* It matches chapter 13's `lend-book` example, which shows a read-only agent because it claims no feature of any host (work/done/ch13-delivery-review.md decision 2), and the slot template's "else a read-only agent on the session's model reading `git diff` of those paths". No Opus, advisor or host name. The sentence after the block says why, in chapter 13's words: it claims no feature of any host, while chapter 9 gives the default a project starts from.
5. *Item 2 does not quote the old slot.* It says "the slot names a command a person launches", which is what `SETUP.md` §1 step 4 tests, and keeps `/code-review` and `ultra` out of the book, as chapters 13 and 15 keep them (ch13-delivery-review Behaviour "Edge", ch15-review-by-areas decision 10). Its proposed areas and model are chapter 15's lending library slot word for word, in each edition (ch15-review-by-areas decisions 4 and 19), so the reader meets the same slot twice; it ends with the kit's question, whether the command still runs too.
6. *Item 4 prints §8's new paragraph whole.* The kit reports "the proposed wording" (`SETUP.md` §1 step 4) and this batch asks for the report as the kit prints it; a shortened quote would be output the kit does not print. The block grows to 44 rows, each within 74 columns in both editions; the paragraph is the template's verbatim in English and, in Portuguese, the Contract's translation with chapter 15's words.
7. *The sentences after the block.* Every item changes a rule, so the old split into rule items and word items goes. Item 1 is said in plain words with no pointer, since chapter 8 already points to chapter 13 once (its §Install) and docs/04 "Chapter pointers" allows one per target; items 2 and 4 point to chapter 15 once; item 3 is said in plain words with no pointer to chapter 16, which today still lists no exception (`ch16-review-agents` is `[ ]`; ch13-delivery-review divergences). One sentence says what item 2 teaches beyond its rule: the report proposes the areas and asks about the command, so the team's choice stays, matching the section's "Your choices stay". The old pointers to chapters 11 and 14 leave with the items they served.
8. *The changelog paragraph.* The 2026.10.17 entry has no item starting with `Migration:` (kit `CHANGELOG.md`), so "Every item of the report above comes from such an item" is no longer true and is rewritten: an entry may have a `Migration:` item; what a rerun compares is the setup file's own step, and the report lists only what the documents still lack, on the lending library the four above. Key point 3 says the same. Nothing of the entry's history or measures (rework counts, a cancelled review, cloud limits, Cascade, dates) enters (docs/04 "The kit as it is").
9. *Chapter 9: both questions, each with its default and one reason.* Brainstorm's subject 5 and analyze's list name the delivery review and the milestone review as the installed skills ask them (`.claude/skills/brainstorm/SKILL.md` subject 5, `.claude/skills/analyze/SKILL.md` §Ask), and the chapter's rule that every question carries a default holds. One short paragraph after "Each slot it writes in docs/05" says what each slot decides and why its default, in the present: the host's own review only when it can be kept to the delivery's paths, since another session may work in the same folder; else a read-only agent; docs/01's modules as areas, since a module's changes are read together; the session's model unless the project names another (docs/04 "Teach, do not only show", "Say it where the doubt is born"). Chapter 9 has no pointer to chapters 13 or 15 yet, so it gets one each there.
10. *Analyze's round grows to seven subjects.* The delivery review and the milestone review become two numbered questions, 5 and 6; the first milestone becomes 7; "One round, of six subjects only" becomes seven (pt "sete assuntos"). Key point 4 says "asks one round" with no count and stays.
11. *This repository's slot answers are not shown.* ch13-delivery-review decision 3 and ch16-review-agents decision 9 left "how a project answers the slots" to this line; it answers by teaching the questions, their defaults and their reasons on the lending library. This book's own slot (a named model and advisor, its areas) is a project choice, not the kit's rule, and naming models would date the book (docs/04 "The kit as it is", "Context before an excerpt").
12. *The gains and the other key points.* Chapter 8's and chapter 9's `## What the team gains` are unchanged: an update that keeps the team's rules and a default for every question still sum each chapter, and a new review changes neither gain (docs/04 "One gain").
13. *No docs/03 term.* `delivery review`, `milestone review`, `candidate`, `slot`, `host`, `fresh session` exist and are used as defined.
14. *Ordering with `ch08-10-devin-desktop`.* No `after` asked: decision 3 keeps this line independent of it; both lines edit `book/*/08-install-and-hosts.md` in different sections, so when both are in the tree they stage by hunk (docs/05 §4, as that page says).
15. *Trunk, nothing staged by this definition.* docs/05 §5 Git; the driver session sets the marks in docs/06 (this batch's instructions). The tree's other changes (`docs/06-Queue.md`, `.claude/settings.json`, the other pages in `work/`) are other lines' work and are not this page's.

**Behaviour.**

* Reading chapter 8's "What an update reports", a reader finds the lending library's report at `focus-kit 2026.10.17`: one `Removed:` line, four pending migrations and the closing line, as the Contract writes it, every row within 74 columns.
* A reader can say what each item asks: item 1 adds the Delivery review slot, a read-only agent reading the delivery's changes before `/apply` ends; item 2 turns the Milestone review slot into areas from docs/01 and the session's model, and asks whether the command the slot named still runs; item 3 lets docs/05 §7 admit the reviews' readers and checker; item 4 replaces §8's short paragraph with the code reading over the range by areas, on the person's word, with the paths read and a checker (chapter 15).
* A reader whose old Milestone review slot names a command can say what happens to it: the report proposes the areas and asks; nothing changes until the team applies the migration as a delivery.
* A reader who sees `.windsurf/skills/` gone from the diff after an update can say why: the kit's own files there were removed, the folder is one the setup file does not write, and a file of their own there would have been reported and left.
* Reading the changelog paragraph, a reader learns the changelog says what changed and why for each version, that an entry may carry a `Migration:` item, and that the report lists only what their documents still lack.
* Reading chapter 9's `/brainstorm` list, subject 5 names who reviews a delivery's changes before `/apply` ends and how the milestone review's code reading splits; the paragraph after it gives each slot's default and its reason.
* Reading chapter 9's `/analyze` questions, a reader finds seven: 5, the delivery review, default the host's own review when it can be kept to a delivery's paths, else a read-only agent; 6, the milestone review's areas and model, default docs/01's modules and the session's model; 7, the first milestone.
* Edge: a reader answering "your call" to both questions can say what they get: the host's review kept to the delivery's paths, or a read-only agent, and docs/01's modules read on the session's model.
* Edge: a reader on a host whose own review cannot be kept to one delivery's paths knows the default falls to a read-only agent, and why: another session's files in the same folder are not that delivery's.
* The Portuguese edition reads the same in the same places, with the Contract's words and the lending library's Portuguese folders.
* Failure: a passage naming `/code-review`, `ultra`, a cloud review, Opus, Fable or an advisor, saying "no longer", naming 2026.10.16 or recounting why the kit changed, contradicts docs/04 "The kit as it is" and this page; the review catches it.
* Failure: chapter 9 still saying a person launches a deep code review, or "six subjects" for `/analyze`, contradicts the installed skills.
* Failure: a row of either block over 74 columns, or one edition changed and not the other.

**Contract.**

* **Chapter 8, both editions** (`book/en/08-install-and-hosts.md`, `book/pt/08-install-and-hosts.md`), section "What an update reports" (pt "O que uma atualização relata") only, found by text:
  * the fenced block after "Here is the report of an update on the lending library" (pt "Este é o relatório de uma atualização na biblioteca de empréstimos") becomes, in English:

    ```
    Installed: focus-kit 2026.10.17, in every SKILL.md.
    Removed: the kit's 6 files in .windsurf/skills/; nothing else there.
    Pending process migrations: 4.

    1. docs/05, §5 This project: add the Delivery review slot after
       Context: "Delivery review: a read-only agent on the session's
       model reads git diff of the delivery's paths against its page and
       docs/04."
    2. docs/05, §5 Milestone review: the slot names a command a person
       launches. Proposed, its areas from docs/01's modules: "by areas,
       one reader each: src/features/loans/, src/features/members/,
       src/features/catalog/, the documents and the rest; readers and
       checker on the session's model." Say whether the command still
       runs too.
    3. docs/05, §7: "no specialized subagent" becomes "no specialized
       subagent beyond the reviews' readers and checker (§5's Delivery
       review, §8)".
    4. docs/05, §8 Closing a milestone: replace "The review also reads
       the code: its page names the commit that closed the previous
       milestone, or the first commit, and the person launches §5's
       Milestone review against it." with "The review also reads the
       code, the one look at the whole instead of a delivery: every page
       can be right and the whole wrong. Its page names the commit that
       closed the previous milestone, or the first commit, as the base,
       and lists, by §5's areas, the paths git diff --stat <base>..HEAD
       shows: always the range, since a bare commit reads that one
       commit. An area too large for one careful reading splits again.
       It costs, so the session says it is time and starts it only on
       the person's word: one read-only agent per area, in parallel
       where the host runs agents, or one fresh session per area, opened
       by the person, where it does not. Each reader has the whole
       repository open and reads its area's changes for what no
       delivery's own review could see, one delivery's work against
       another's, a document against another, the whole against docs/01,
       and reports candidates by file and line and the paths it read.
       One checker, an agent or the review's session, opens each
       candidate's file and marks it seen, latent (nothing triggers it
       today) or weak (the claim does not hold as stated) before the
       person sees it. They fix nothing. When the paths read miss some
       of the range's, the page says which and the line waits as [?]
       with · resume: apply (§4). A candidate the person confirms is a
       finding like the others."

    docs/ and AGENTS.md were not changed.
    ```

    and in Portuguese:

    ```
    Instalado: focus-kit 2026.10.17, em cada SKILL.md.
    Removidos: os 6 arquivos do kit em .windsurf/skills/; nada mais ali.
    Migrações de processo pendentes: 4.

    1. docs/05, §5 This project: acrescentar o slot Delivery review
       depois do Context: "Delivery review: um agente somente leitura no
       modelo da sessão lê o git diff dos caminhos da entrega contra a
       página dela e o docs/04."
    2. docs/05, §5 Milestone review: o slot cita um comando que uma
       pessoa lança. Proposto, com as áreas tiradas dos módulos do
       docs/01: "por áreas, um leitor cada: src/features/emprestimos/,
       src/features/membros/, src/features/catalogo/, os documentos e o
       resto; leitores e conferente no modelo da sessão." Diga se o
       comando também continua rodando.
    3. docs/05, §7: "nenhum subagente especializado" vira "nenhum
       subagente especializado além dos leitores e do conferente das
       revisões (Delivery review do §5, §8)".
    4. docs/05, §8 Closing a milestone: trocar "A revisão também lê o
       código: a sua página cita o commit que fechou o marco anterior, ou
       o primeiro commit, e a pessoa lança o Milestone review do §5
       contra ele." por "A revisão também lê o código, o único olhar
       sobre o todo em vez de uma entrega: cada página pode estar certa e
       o todo errado. A sua página cita como base o commit que fechou o
       marco anterior, ou o primeiro commit, e lista, pelas áreas do §5,
       os caminhos que git diff --stat <base>..HEAD mostra: sempre o
       intervalo, já que um commit solto lê só aquele commit. Uma área
       grande demais para uma leitura cuidadosa se divide de novo. Ela
       custa, então a sessão diz que é hora e só a começa com a palavra
       da pessoa: um agente somente leitura por área, em paralelo onde o
       host roda agentes, ou uma sessão nova por área, aberta pela
       pessoa, onde não roda. Cada leitor tem o repositório inteiro
       aberto e lê as mudanças da sua área atrás do que a revisão de
       nenhuma entrega podia ver, o trabalho de uma entrega contra o de
       outra, um documento contra outro, o todo contra o docs/01, e
       relata candidatos por arquivo e linha e os caminhos que leu. Um
       conferente, um agente ou a sessão da revisão, abre o arquivo de
       cada candidato e o marca visto, latente (nada o dispara hoje) ou
       fraco (a afirmação não se sustenta como foi dita) antes de a
       pessoa vê-lo. Eles não corrigem nada. Quando os caminhos lidos não
       cobrem parte dos do intervalo, a página diz quais e a linha espera
       como [?] com · resume: apply (§4). Um candidato que a pessoa
       confirma é um achado como os outros."

    docs/ e AGENTS.md não foram alterados.
    ```

  * the two lines after the block, "Items 1, 3, 4 and 7 change a rule ..." and "Items 2, 5, 6 and 8 change only words ..." (pt "Os itens 1, 3, 4 e 7 mudam uma regra ..." and "Os itens 2, 5, 6 e 8 mudam só palavras ..."), become, one sentence per line:
    "Every item changes a rule."
    "Item 1 has each delivery's own changes read before `/apply` ends, by a reader that did not write them, here a read-only agent, which claims no feature of any host; items 2 and 4 have the milestone review read every change since the milestone's base, split into areas, one read-only reader each, with a checker before the person sees what they report ([chapter 15](15-closing-a-milestone.md)); item 3 lets docs/05 §7, which lists what the process does not have, admit those readers and their checker."
    "Item 2 also keeps a choice: the slot named a command the person launches, and the report proposes the areas beside it and asks whether it still runs, so the team decides."
    "`Removed` lists the kit's own files the update deleted from `.windsurf/skills/`, a folder the setup file does not write; a file of yours there would have been reported and left."
    (pt: "Todo item muda uma regra." / "O item 1 faz as mudanças de cada entrega serem lidas antes de o `/apply` terminar, por um leitor que não as escreveu, aqui um agente somente leitura, que não depende de recurso de nenhum host; os itens 2 e 4 fazem a revisão de marco ler toda mudança desde a base do marco, dividida em áreas, um leitor somente leitura cada, com um conferente antes de a pessoa ver o que relatam ([capítulo 15](15-closing-a-milestone.md)); o item 3 deixa o §7 do docs/05, que lista o que o processo não tem, admitir esses leitores e o seu conferente." / "O item 2 também mantém uma escolha: o slot citava um comando que a pessoa lança, e o relatório propõe as áreas ao lado dele e pergunta se ele continua rodando, para que o time decida." / "`Removidos` lista os arquivos do próprio kit que a atualização apagou de `.windsurf/skills/`, uma pasta que o arquivo de setup não escreve; um arquivo seu ali teria sido relatado e deixado.")
  * in the changelog paragraph, "Each entry says what changed and the problem that caused it, and an item that starts with `Migration:` names what to change in the project's documents." becomes "Each entry says what changed and the problem that caused it, and an entry may carry an item that starts with `Migration:`, naming what to change in the project's documents."; "Every item of the report above comes from such an item, which says that the report checks ..." to its end becomes "What a rerun compares is the setup file's own step, which names the sections of docs/05, the slots and the lines of `AGENTS.md` it checks; the report lists only what your documents still lack, on the lending library the four items above." (pt to match: "e uma entrada pode trazer um item que começa com `Migration:`, citando o que mudar nos documentos do projeto"; "O que uma nova execução compara é o próprio passo do arquivo de setup, que cita as seções do docs/05, os slots e as linhas do `AGENTS.md` que confere; o relatório lista só o que os seus documentos ainda não têm, na biblioteca de empréstimos os quatro itens acima.")
  * key point 3: "and in a `Migration:` item what to change in the project's documents" becomes "and, in an item that starts with `Migration:` when the entry has one, what to change in the project's documents" (pt to match).
  Every other section of chapter 8 is unchanged, "How each host finds the commands" and key point 4 above all (`ch08-10-devin-desktop`).
* **Chapter 9, both editions** (`book/en/09-starting-a-project.md`, `book/pt/09-starting-a-project.md`), found by text:
  * `/brainstorm` subject 5: "and the deep code review you will launch when a milestone closes" becomes "who reviews a delivery's changes before `/apply` ends, and how the milestone review's code reading splits" (pt "quem revisa as mudanças de uma entrega antes de o `/apply` terminar, e como se divide a leitura do código da revisão de marco").
  * after the line "Each slot it writes in docs/05 says what and the command ...", one paragraph, one sentence per line:
    "Two of those slots say who reviews."
    "The Delivery review slot names who reads a delivery's changes before `/apply` ends, a context that did not write them ([chapter 13](13-apply.md)): the default is the host's own review, a skill or a command the agent can run, when it can be kept to the delivery's paths, since another session may be working in the same folder; otherwise a read-only agent, one that reads files and edits none."
    "The Milestone review slot says how the code reading at a milestone's close splits ([chapter 15](15-closing-a-milestone.md)): the default areas are docs/01's modules, one reader each, because a module's changes are read together, and the readers run on the session's model, the one you already work with, unless you name another."
    (pt: "Dois desses slots dizem quem revisa." / "O slot Delivery review cita quem lê as mudanças de uma entrega antes de o `/apply` terminar, um contexto que não as escreveu ([capítulo 13](13-apply.md)): o padrão é a revisão do próprio host, uma skill ou um comando que o agente consegue rodar, quando ela pode ficar restrita aos caminhos da entrega, já que outra sessão pode estar trabalhando na mesma pasta; senão, um agente somente leitura, que lê arquivos e não edita nenhum." / "O slot Milestone review diz como se divide a leitura do código ao fechar um marco ([capítulo 15](15-closing-a-milestone.md)): as áreas padrão são os módulos do docs/01, um leitor cada, porque as mudanças de um módulo se leem juntas, e os leitores rodam no modelo da sessão, o que você já usa, a menos que você cite outro.")
  * `/analyze` §What it asks: "One round, of six subjects only:" becomes "One round, of seven subjects only:" (pt "Uma rodada, de sete assuntos apenas:"); item 5 is replaced by two and the first milestone becomes 7:
    "5. The delivery review: who reads a delivery's changes before `/apply` ends. Default: the host's own review, when it can be kept to the delivery's paths; otherwise a read-only agent."
    "6. The milestone review: the areas its code reading splits into and the model its readers run on. Default: docs/01's modules and the session's model."
    (pt: "5. A revisão da entrega: quem lê as mudanças de uma entrega antes de o `/apply` terminar. Padrão: a revisão do próprio host, quando ela pode ficar restrita aos caminhos da entrega; senão, um agente somente leitura." / "6. A revisão de marco: as áreas em que a leitura do código se divide e o modelo em que os leitores rodam. Padrão: os módulos do docs/01 e o modelo da sessão.")
  Every other section of chapter 9 is unchanged, key points and `## What the team gains` included.
* **Portuguese words.** delivery review: `revisão da entrega`; milestone review: `revisão de marco`; read-only agent: `agente somente leitura`; reader: `leitor`; checker: `conferente`; area: `área`; range: `intervalo`; candidate: `candidato`; seen, latent, weak: `visto`, `latente`, `fraco`; fresh session: `sessão nova`; the person's word: `a palavra da pessoa`; the session's model: `o modelo da sessão`. Slot names stay in English (`Delivery review`, `Milestone review`), and so do docs/05's section titles inside the report (`This project`, `Closing a milestone`), as chapters 8 and 15 already write them. The lending library's folders in pt: `src/features/emprestimos/`, `src/features/membros/`, `src/features/catalogo/` (chapter 4).
* **Terms of docs/03.** `delivery review`, `milestone review`, `candidate`, `slot`, `host`, `fresh session` used as defined. No new term, no docs/03 change.
* **Sources.** None added or removed. The kit's setup file and changelog are named in plain words, as chapter 8 already names them; no note points to focus-kit's repository (docs/04 "Source notes").
* **Cases.** No private case; no number beyond the report's own (a version, a count of six files, four migrations), in an artifact said to be written for the chapter.
* **docs/06.** None from this page beyond its own line's marks, set by the driver.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Out of scope.**

* Chapter 8's host table, its paragraph, the `.windsurf/skills/` sentence of that section and key point 4: `ch08-10-devin-desktop`.
* Chapter 13's delivery review and chapter 15's code reading by areas: done (`ch13-delivery-review`, `ch15-review-by-areas`); this line only points to them.
* Chapter 16's exception for the reviews' readers: `ch16-review-agents`; no pointer to it here (decision 7).
* Chapter 7's slot list: already names both reviews (`ch07-11-23-review-words`).
* This repository's own slot answers, models and advisor: a project choice (decision 11).
* The changelog's measures and history of the 2026.10.17 changes (decision 8).
* Batches of proposes: `batch-propose`.

**Done when.**

* [x] Both editions written in the places the Contract names, the English first; parity green.
* [x] Both report blocks read as the Contract writes them, every row within 74 columns (`check_width.py` green).
* [x] `grep -n -i -E "no longer|code-review|ultra|deep|opus|fable|advisor|cloud|2026\.10\.16" book/en/08-install-and-hosts.md book/en/09-starting-a-project.md` finds nothing; `grep -n -i -E "não mais|code-review|ultra|profunda|opus|fable|advisor|nuvem|2026\.10\.16" book/pt/08-install-and-hosts.md book/pt/09-starting-a-project.md` finds nothing; `grep -n -i "launch"` in the English chapter 8 finds only the report's items 2 and 4 and the sentence on item 2, and nothing in chapter 9 (pt `lança`, the same places).
* [x] `grep -c "seven subjects" book/en/09-starting-a-project.md` gives 1; pt `sete assuntos` 1; no `six subjects` / `seis assuntos` left beside `/analyze`.
* [x] Chapters 8 and 9 still open with their value; no filler, nothing useful cut; still five key points each; chapter 8 points to chapter 13 once and to chapter 15 once.
* [x] The Portuguese uses the Contract's words and no synonym.
* [x] No em dash; `make verify` green (build, parity, em dash, prose, width, links, disclosure).
* [x] The Delivery review ran on this delivery's paths (docs/05 §5) and the page records it.
* [x] The author's approval of an anonymized passage: inapplicable, no Case A or Case B passage.
* [x] `make book` builds; the delivery ends with the paths of both PDFs for the author's review.
* [x] Page moved to `work/done/`, the line `[x]`, staged by explicit paths, by hunk in chapter 8 when `ch08-10-devin-desktop`'s changes are also in the tree (key points 3 and 4 are adjacent lines, so where both changed that hunk is split by hand), and this line's hunk of docs/06; the commit message suggested, `docs(ch08-09-review-slot): ...`.

**What happened.**

* Built as defined: chapter 8's report at 2026.10.17 in both editions, word for word from the Contract (widest row 68 columns in English, 69 in Portuguese), the four sentences after it, the changelog paragraph and key point 3; chapter 9's `/brainstorm` subject 5, the paragraph on the two review slots with one pointer each to chapters 13 and 15, and `/analyze`'s seven subjects. The English first. Nothing dropped.
* Adapted to `ch08-10-devin-desktop` (commit fec4118), which landed first: its table row, its `.windsurf/skills/` sentence and key point 4 are kept as they are. The `Removed` sentence after the block stays as the Contract writes it (decision 3): it now repeats the hosts section's sentence without contradicting it, and it explains the report's line where the reader meets it.
* Divergence, justified: the Portuguese `Removed` sentence ends "relatado e mantido", not the Contract's "relatado e deixado", so it uses the same words as the hosts section's sentence of the same chapter.
* Divergence, justified: the sentence on item 1 adds "while chapter 9 gives the default a project starts from" (pt "enquanto o capítulo 9 dá o padrão de que um projeto parte"), as decision 4 asks and the Contract's sentence had left out, so a reader does not take item 1's read-only agent and chapter 9's default as a contradiction. Plain words, no link: chapter 8 already names chapter 9 so.
* Decided by the agent, no author present (rule of this batch: the recommended option): the two divergences above; the Portuguese key point 3 keeps its existing "num item de migração" and adds "quando a entrada tem um".
* Proof: `make verify` green; `make book` builds both editions; the Done when greps find nothing; "launch" / `lança` only in the report's items 2 and 4 and the sentence on item 2; "seven subjects" / `sete assuntos` once each; five key points in each chapter.
* Delivery review (docs/05 §5), a read-only agent on Opus over this delivery's staged and unstaged diff against this page, docs/04 and the installed brainstorm and analyze skills: no finding breaks the page or docs/04. Four optional points: "deixado" against "mantido" in the Portuguese, taken; the `Removed` sentence repeating the hosts sentence, left as above; item 1 against chapter 9's default, taken; the Portuguese key point 3 saying "item de migração", older than this delivery, left. Verify green again. No finding left for the queue.

```commit
docs(ch08-09-review-slot): update chapter 8's report and 9's review asks

- Chapter 8's report at 2026.10.17: Removed line and four migrations
- Delivery review, milestone review by areas, §7 exception, §8 reading
- Changelog paragraph: an entry may carry a Migration: item
- Chapter 9: who reviews, its defaults, /analyze asks seven subjects
- Both editions

work/done/ch08-09-review-slot.md
```
