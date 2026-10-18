# ch07-11-23-review-words

**Objective.** After chapters 7, 11 and 23 a reader who meets the milestone review there reads it as chapter 15 teaches it: started on the person's word, never launched by hand as a host's review, the review's session has read the code changed since the milestone's base by the areas docs/05's Milestone review slot names, one read-only agent each, and a checker marks each candidate before anyone sees it; and chapter 7 counts docs/05's ten slots, the Delivery review among them; both editions.

**Decided without the author.**

1. *Which passages change.* Six sentences, found by text, the same in both editions: chapter 7's slot enumeration in §The seven documents ("whose entries are its nine slots" / "cujos itens são os seus nove slots") and its question 6 in §Where a new fact goes; chapter 11's second sentence of §The review, and its findings ("It fixes nothing:" / "Ela não corrige nada:"); chapter 23's bullet "Who reviews the milestone" / "Quem revisa o marco". A grep of the three chapters for the deep review and the nine slots finds only these (the queue line, docs/05 §8).
2. *The slot count and order.* Ten, in the order of the kit's template of docs/05 §5 (`.claude/skills/analyze/references/documents.md`): documentation language, verify, environments, proof of a screen, publish policy, context, delivery review, manuals, milestone review, git. This repository's extra slots (Case A and Case B, Disclosure, Guided project) are its own and chapter 7 never counted them. The Delivery review goes between `context/` and the manuals, as the template orders it. Said as the count it is, never as "now ten" or "one more" (docs/04 "The kit as it is").
3. *What the two review slots are called in chapter 7.* By what they hold, as the template's bullets say: who reviews a delivery's changes before `/apply` ends (the Delivery review), and the areas the milestone review's code reading splits into with the model its readers and checker run on (the Milestone review); followed by "(chapters 13 and 15)", in chapter 7's plain-reference style. No host, model or command named (ch13-delivery-review decision 3, ch15-review-by-areas decision 10).
4. *Question 6.* "the milestone review's command" becomes "how a delivery and a milestone are reviewed", since the Milestone review slot holds areas and a model, not a command, and the Delivery review is a fact the commands read too (the template). The sentence above it, "A slot says what and the command", stays: docs/05 §5 still opens with it.
5. *How much chapters 11 and 23 say.* One clause each and the link to chapter 15 they already carry, no retelling: chapter 15 teaches the range, the areas, the paths read and the checker's marks (the batch's instructions, docs/04 "Teach, do not only show" applied in chapter 15, not here).
6. *Chapter 23's framing.* Kept as a role: the team tests the paragraph on the running product and gives the word; the session has the code read; the team confirms which candidates are findings. That is who does what, the chapter's subject (docs/05 §8).
7. *The slot set to none.* Said once where the slot is named in chapters 11 and 23, as "when it names areas" / "quando cita áreas"; chapter 7 already says a slot may hold no answer only through chapter 9, so it adds nothing (the template's "or: none"; ch15-review-by-areas decision 11).
8. *The `m1-review` example line in chapter 11.* `[ ] m1-review     the milestone checked against its paragraph` stays: chapter 14 prints the identical line, it is a line not yet defined, still true of the review, and chapter 15 shows the closed line with the code read (ch15-review-by-areas decision 13). The queue line names no example.
9. *The gain sections.* Unchanged in the three chapters: they point to the rule, and chapters 13 and 15 teach it and carry its gain (docs/04 "One gain").
10. *Portuguese words.* The ones ch15-review-by-areas fixed on its Contract, so the book uses one rendering: `com a palavra da pessoa`, `agente somente leitura`, `revisão de marco`, `revisão da entrega`, `conferente`, `candidato`, `área` (docs/04 "Languages").
11. *docs/03 and docs/06.* No new term: `candidate` / `candidato` is already asked of the driver by ch15-review-by-areas, and this page relies on it. No new queue line; this line's `· after ch15-review-by-areas` already holds the order. The driver sets the marks (this batch's instructions).
12. *Neighbouring passages left to their owners.* Chapter 9's "deep code review you will launch" (en and pt lines 21 and 79) belongs to `ch08-09-review-slot`; chapter 15's own text belongs to `ch15-review-by-areas`, applied in this tree now and assumed done by this line's `after`.

**Behaviour.**

* Chapter 7, §The seven documents, the slot sentence reads, in substance: "One section is filled in by the project, "This project", whose entries are its ten slots: the documentation language, the command that verifies a delivery, the environments, how a screen is proved, when anything is published, whether `context/` is committed, who reviews a delivery's changes before `/apply` ends, the manuals, the areas the milestone review's code reading splits into and the model its readers and checker run on, and the git strategy (chapters 13 and 15)." pt: "... cujos itens são os seus dez slots: ..., se a pasta `context/` entra no commit, quem revisa as mudanças de uma entrega antes de o `/apply` terminar, os manuais, as áreas em que a leitura do código da revisão de marco se divide e o modelo em que os seus leitores e o conferente rodam, e a estratégia de git (capítulos 13 e 15)."
* Chapter 7, question 6 reads: "Is it a fact of this project that the commands read: the verify command, the environments, whether `context/` is committed, how a delivery and a milestone are reviewed, git?" pt: "É um fato deste projeto que os comandos leem: o comando de verificação, os ambientes, se a pasta `context/` entra no commit, como uma entrega e um marco são revisados, o git?" Its answer line is unchanged.
* Chapter 11, §The review, and its findings, the second sentence reads, in substance: "It fixes nothing: a person tests each clause by hand and, on the person's word, the session has the code changed since the milestone's base read by the areas the project's docs/05 names, when it names areas, one read-only agent each, and a checker marks each candidate before the person sees it." pt: "Ela não corrige nada: uma pessoa testa cada cláusula à mão e, com a palavra da pessoa, a sessão faz ler o código alterado desde a base do marco pelas áreas que o docs/05 do projeto cita, quando cita áreas, um agente somente leitura em cada uma, e um conferente marca cada candidato antes que a pessoa o veja." The first and third sentences and the link to chapter 15 stay.
* Chapter 23, §Roles in a team, the bullet reads, in substance: "**Who reviews the milestone:** the team, on the running product, against the milestone's paragraph; on its word, the session has the code changed since the milestone's base read by the areas docs/05 names, when it names areas, one read-only agent each, and a checker marks each candidate before the team confirms which are findings ([chapter 15](15-closing-a-milestone.md))." pt: "**Quem revisa o marco:** o time, no produto rodando, contra o parágrafo do marco; com a palavra dele, a sessão faz ler o código alterado desde a base do marco pelas áreas que o docs/05 cita, quando cita áreas, um agente somente leitura em cada uma, e um conferente marca cada candidato antes que o time confirme quais são achados ([capítulo 15](15-closing-a-milestone.md))."
* A reader of any of the three chapters can say who starts the code reading (the session, on the person's or team's word), what it reads (the code since the base, by areas), who reads (read-only agents) and that a checker stands between a reader's candidate and the person; chapter 7's reader can name the ten slots.
* Every other sentence of the three chapters, their openings, gains and key points, is unchanged.
* Edge: nothing in the six files names a deep review, a host's review command, `/code-review`, Opus, Fable, an advisor, a kit version or the changelog, or compares the kit with an earlier one.
* Edge: the prose rules of docs/04 hold in the new sentences, `not-but` included.
* Failure: a passage saying a person launches the review, that the agent starts it unasked, that a host's command is the reading, that a single commit is read, or that a candidate is a finding before the person confirms it contradicts docs/05 §8 and chapter 15.
* Failure: one edition changed and not the other, or a count other than ten in chapter 7.

**Contract.**

* **Files.** `book/en/07-the-documents.md`, `book/pt/07-the-documents.md`, `book/en/11-queue-and-milestones.md`, `book/pt/11-queue-and-milestones.md`, `book/en/23-adoption.md`, `book/pt/23-adoption.md`; no other file but this page.
* **Sections touched** (found by text): chapter 7, §The seven documents / §Os sete documentos, the slot sentence; §Where a new fact goes / §Para onde vai um fato novo, question 6; chapter 11, §The review, and its findings / §A revisão, e os seus achados, second sentence; chapter 23, §Roles in a team / §Papéis num time, the bullet "Who reviews the milestone" / "Quem revisa o marco".
* **Terms of docs/03.** `slot`, `delivery review`, `milestone review`, `finding`, `candidate` (the row ch15-review-by-areas asks of the driver) used as defined. No new row.
* **Portuguese words.** As decision 10; no synonym.
* **Sources.** None added or removed.
* **Cases.** None added; no Ninjobs, Case A or Case B passage changes.
* **Numbers.** One count changed, nine to ten slots, sourced by the kit's template of docs/05 §5 (decision 2); no other number.
* **docs/06.** None asked; the driver sets this line's marks.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Out of scope.**

* Chapter 15's teaching of the review by areas: `ch15-review-by-areas`.
* Chapter 13's delivery review: done in `ch13-delivery-review`.
* Chapters 8 and 9's slot questions and update example, chapter 9's "deep code review" included: `ch08-09-review-slot`.
* Chapters 8 and 10's hosts: `ch08-10-devin-desktop`.
* The governor's admission of the reviews' readers: `ch16-review-agents`.
* Chapter 11's `m1-review` example line and chapter 14's copy of it (decision 8).
* Any gain, measure or history of the rule (decision 9).

**Done when.**

* [x] Both editions changed in the same six passages; parity green.
* [x] Every Behaviour line reads as written in both editions; openings, gains and key points of the three chapters unchanged, so each still opens with its value; no filler, nothing useful cut.
* [x] `grep -n -i -E "deep (code )?review|nine slots|launch|review's command" book/en/07-the-documents.md book/en/11-queue-and-milestones.md book/en/23-adoption.md` finds nothing; `grep -n -i -E "revisão profunda|nove slots|lança|comando da revisão" book/pt/07-the-documents.md book/pt/11-queue-and-milestones.md book/pt/23-adoption.md` finds nothing.
* [x] `grep -c "ten slots" book/en/07-the-documents.md` is 1 and `grep -c "dez slots" book/pt/07-the-documents.md` is 1.
* [x] The links to chapter 15 survive: `grep -c "15-closing-a-milestone.md"` is 1 in each edition of chapter 11 and 2 in each edition of chapter 23.
* [x] `grep -n -i -E "2026\.|changelog|no longer|não mais|opus|fable|advisor|code-review"` over the six files finds no line this delivery wrote.
* [x] The Portuguese uses decision 10's words and no synonym.
* [x] No em dash; `make verify` green, disclosure scan included.
* [x] The Delivery review ran on this delivery's paths as docs/05 §5 says, and the page records it.
* [x] The author's approval of an anonymized passage: inapplicable, no Case A or Case B passage.
* [x] `make book` builds, and the delivery ends giving the author both PDF paths to review.

**Divergences.**

* Chapter 7's slot sentence: the Behaviour line put "(chapters 13 and 15)" / "(capítulos 13 e 15)" after the git strategy, where it read as if git were taught there (chapter 7 teaches it). The built text names each chapter after its slot: "before `/apply` ends (chapter 13)" and "checker run on (chapter 15)", the same in both editions. Same slots, same order, same count.

**Decisions taken in /apply (batch, recommended option).**

13. *The Delivery review's suggestions left as written.* "has the code ... read by the areas" (en), "a sessão faz ler" (pt) and "one read-only agent each" without the fresh-session path follow the Behaviour lines word for word, break neither docs/04 nor the page, and chapter 15, linked from both passages, teaches the rest (decision 5). No queue line: the author may smooth the wording when reading the PDFs.

**Proof.** `make verify` green (build, parity, em dash, prose, width, links, disclosure). The Done-when greps: no deep review, nine slots, launch or review's command in either edition; "ten slots" and "dez slots" once each; the links to chapter 15 count 1 in chapter 11 and 2 in chapter 23 in each edition; no line this delivery wrote matches the version, changelog, model or host pattern. `make book` built `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.

**Delivery review.** A read-only agent on Opus, keeping the session's advisor, read `git diff` and `git diff --cached` of the six chapters and this line's hunk of docs/06 against this page and docs/04. It found the six passages in both editions with the same meaning, decision 10's words, no em dash, the ten slots in the template's order, and the text true to docs/05 §8 and chapter 15. Candidates: (1) the chapter reference after the git strategy, fixed (Divergences); (2) to (4) wording suggestions, left as written (decision 13). No new queue line.

```commit
docs(ch07-11-23-review-words): say the review by areas in 7, 11 and 23

- Chapter 7 counts docs/05's ten slots, the Delivery review among them
- Chapter 7's question 6 asks how a delivery and a milestone are reviewed
- Chapters 11 and 23: code read by areas on the person's word, a checker
- No deep review a person launches; both editions

work/done/ch07-11-23-review-words.md
```
