# ch11-23-who-reads

**Objective.** After chapters 11 and 23 a reader who meets the milestone review's code reading there reads it as chapter 15 teaches it: on the person's or the team's word, the code changed since the milestone's base is read by whoever docs/05's Milestone review slot names, when it names anyone, the host's deep review or one read-only agent per area, and either way a checker marks each candidate before the person, or the team, sees it; both editions.

**Behaviour.**

* Chapter 11, §The review, and its findings, the second sentence reads, in substance: "It fixes nothing: a person tests each clause by hand and, on the person's word, the code changed since the milestone's base is read by whoever the Milestone review slot of the project's docs/05 names, when it names anyone, the host's deep review or one read-only agent per area, and either way a checker marks each candidate before the person sees it." pt: "Ela não corrige nada: uma pessoa testa cada cláusula à mão e, com a palavra da pessoa, o código alterado desde a base do marco é lido por quem o slot Milestone review do docs/05 do projeto cita, quando cita alguém, a revisão profunda do host ou um agente somente leitura por área, e nos dois casos um conferente marca cada candidato antes que a pessoa o veja." The first and third sentences and the link to chapter 15 stay.
* Chapter 23, §Roles in a team, the bullet reads, in substance: "**Who reviews the milestone:** the team, on the running product, against the milestone's paragraph; on its word, the code changed since the milestone's base is read by whoever docs/05's Milestone review slot names, when it names anyone, the host's deep review or one read-only agent per area, and either way a checker marks each candidate before the team confirms which are findings ([chapter 15](15-closing-a-milestone.md))." pt: "**Quem revisa o marco:** o time, no produto rodando, contra o parágrafo do marco; com a palavra dele, o código alterado desde a base do marco é lido por quem o slot Milestone review do docs/05 cita, quando cita alguém, a revisão profunda do host ou um agente somente leitura por área, e nos dois casos um conferente marca cada candidato antes que o time confirme quais são achados ([capítulo 15](15-closing-a-milestone.md))."
* Asked in either chapter who reads a milestone's code, the reader answers: the slot's choice, the host's deep review or the kit's readers by area, or nobody when the slot says none; a checker stands between any candidate and the person; chapter 15 says how.
* Edge, none: "when it names anyone" / "quando cita alguém" keeps the slot set to none true without a sentence of its own; the hand test still runs, as the first half of each sentence says.
* Edge: neither chapter says who launches the deep review, the range's two commits, the paths read, the three marks or the base where no earlier review exists; chapter 15 teaches them and the link already points there.
* Every other sentence of the two chapters, their openings, gains and key points, is unchanged.
* Fails if: a passage names the code reading only by areas, has the session launch the deep review, sends a candidate to the person unchecked, calls a candidate a finding before the person confirms it, names a host command, a model, a cloud or a kit version, tells how the kit chose before, narrates a run of this repository, or changes one edition and not the other.

**Contract.**

* **Files.** `book/en/11-queue-and-milestones.md`, `book/pt/11-queue-and-milestones.md`, `book/en/23-adoption.md`, `book/pt/23-adoption.md`; no other file but this page.
* **Sections touched**, found by text, the same in both editions:
  * chapter 11, §The review, and its findings / §A revisão, e os seus achados: the second sentence ("It fixes nothing:" / "Ela não corrige nada:") only;
  * chapter 23, §Roles in a team / §Papéis num time: the bullet "Who reviews the milestone" / "Quem revisa o marco" only.
* **Wording.** The sentences of Behaviour, in substance; /apply may tune the prose to docs/04, keeping each element: the person's or team's word, the code since the milestone's base, whoever the Milestone review slot names when it names anyone, the two answers in chapter 15's order (the host's deep review, then one read-only agent per area), the checker either way, and who confirms.
* **Terms of docs/03.** `milestone review`, `slot`, `checker`, `candidate`, `finding`, as defined; "host's deep review" / "revisão profunda do host" as docs/03's `milestone review` and `checker` rows and chapter 15 say it. No new row.
* **Sources.** None added or removed; no number, no footnote, no private case.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no visual change.

**Out of scope.**

* Chapter 15, which teaches who reads: done in `ch15-who-reads`.
* Chapter 7's slot list: `ch07-review-git-slots`. Chapter 9's question on a second pair of eyes: `ch09-second-pair-of-eyes`.
* Chapter 11's `m1-review` and `m2-review` example lines, its key points and its gain section: they do not say who reads (ch07-11-23-review-words decision 8).
* Chapter 23's key point "the team reviews the milestone" and its pilot list ("Close it with its review"): true either way.
* This repository's own choice of the kit's readers (`work/done/kit-2026-10-19.md`, `work/done/review-slot-models.md`): a run of this repository (ADR-0017).
* docs/03, docs/05, docs/06: no change; `kit-2026-10-19` wrote them.

**Decisions from the documents.**

* Who reads is the Milestone review slot's choice, the host's deep review or the kit's readers by area, or none: docs/05 §8 and §5's slot template, as installed by `kit-2026-10-19`, and docs/03's `milestone review` row.
* The checker marks every candidate either way: docs/05 §8 ("Either way, one checker") and docs/03's `checker` row.
* The reading starts only on the person's word; the person launches the deep review, so the sentences drop "the session has ... read" for a passive "is read", which holds for both answers: docs/05 §8, chapter 15 (`work/done/ch15-who-reads.md`, Divergences).
* Chapters 11 and 23 agree in one clause and point to chapter 15, no retelling: ch07-11-23-review-words decision 5, and this line's instruction that chapter 15 is the place the book teaches who reads.
* Portuguese words: `revisão profunda do host`, `agente somente leitura`, `conferente`, `candidato`, `com a palavra da pessoa`, as chapter 15 uses them (ch15-who-reads decision on Portuguese; ch07-11-23-review-words decision 10).
* The book teaches the kit as it is: no before/after, no version (docs/04 "The kit as it is", ADR-0017).

**Decisions taken alone.**

* The slot set to none is said as "when it names anyone" / "quando cita alguém", replacing "when it names areas", which no longer covers the deep review; no separate sentence on none. Alternative the author may prefer, since the deep review is a command and not a someone: "when it names one" / "quando cita uma".
* Order of the two answers: the host's deep review first, then the readers per area, as chapter 15's opening and docs/05 §8 order them.
* "the kit's readers" is not named as such in chapters 11 and 23; "one read-only agent per area" says what they are without a term the reader meets first in chapter 15.
* The gain sections of both chapters are not touched: they point to the rule and chapter 15 carries its gain (ch07-11-23-review-words decision 9).

**Done when.**

* [ ] Both editions written, the same two passages changed in each, Portuguese read as Portuguese.
* [ ] Each sentence holds every element of Contract's Wording and agrees with chapter 15 and docs/05 §8.
* [ ] `grep -n -E "by the areas|names areas" book/en/11-queue-and-milestones.md book/en/23-adoption.md` and `grep -n -E "pelas áreas|cita áreas" book/pt/11-queue-and-milestones.md book/pt/23-adoption.md` find nothing.
* [ ] `grep -n -i -E "code-review|ultra|opus|fable|advisor|cloud|no longer|2026\.10" book/en/11-queue-and-milestones.md book/en/23-adoption.md` and `grep -n -i -E "code-review|ultra|opus|fable|advisor|nuvem|não mais|2026\.10" book/pt/11-queue-and-milestones.md book/pt/23-adoption.md` find nothing, as before the delivery; no before/after, no narrated run, no em dash.
* [ ] Every link resolves; no number added, so none to source.
* [ ] Delivery review as docs/05 §5 says.
* [ ] `make verify` green; `make book` builds both editions, and the two PDF paths are reported.
* [ ] Only this delivery's paths and its hunks of docs/06 staged; the page moved to `work/done/` and its commit message suggested.
