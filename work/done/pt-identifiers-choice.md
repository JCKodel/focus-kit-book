# pt-identifiers-choice

**Objective.** A reader of the Portuguese edition, at the book's first code block, learns that its Portuguese identifiers are a teaching choice and not a recommendation, and that the team decides what suits its project and its people; the sentence listing which names are translated, which a glance at the code already shows, is gone. Found by the author's reading of the book on 2026-10-18: "pt 03:25 ('Nesta edição, os nomes que o código inventa ... ficam como são') is removed: a glance at the code says it. In its place, Portuguese edition only: the book uses Portuguese identifiers as a teaching choice, not a recommendation; the team decides what is best for the project and its members."

**Decided without the author.** The batch had no one to answer; each choice is the recommended one. Removing the sentence and the content of the new note are the author's decisions, not these.

1. *In place.* The new note replaces pt 03:25 on the same line, between "Os exemplos de código deste livro foram escritos para ele" (pt 03:24) and the first code block's lead-in (pt 03:26), so it stays where docs/04 §Writing the book puts it: once, at the book's first code block. Source: the author's draft ("In its place"), docs/04 §Writing the book, Evidence and the Code bullet.
2. *The wording.* One sentence, the author's two clauses and nothing else: "Nesta edição, os nomes do código estão em português por uma escolha didática, não como recomendação: cabe à equipe decidir o que é melhor para o projeto e para as pessoas dele." It keeps "Nesta edição", as the removed sentence opened, so the reader knows the English edition names things in English; it drops "sem acentos" and the list of words that stay in English, which the code shows. Source: the author's draft; ADR-0015 (as long as proving takes, no filler).
3. *The kit's names keep their sentences.* The sentences that say a name stays in English, pt 04:56 (`features/`), 07:17 (`docs/`, `work/` and the rest), 11:22 and 11:87 (`· after`, `<milestone>-review`), 14:29 (the queue's suffixes) and 22:88 (the log's fields), stay as they are. They say what a glance does not: that the reader's own project keeps those names in English, as the kit writes them or an external format fixes them, in an edition where every other name is Portuguese. The author's reason, "a glance at the code says it", is about the identifiers being Portuguese, which chapter 3 no longer explains. Source: the author's draft (names pt 03:25 only), docs/04 §Writing the book, Evidence ("the Portuguese edition says so once, where the reader first meets them (chapters 4, 7, 11, 14)").
4. *docs/04 changes in two places, both on chapter 3's note.* §Writing the book, Evidence: "Chapter 3, at the first code block, says once that the names are in Portuguese." becomes "Chapter 3, at the first code block, says once, in the Portuguese edition, that its Portuguese names are a teaching choice, not a recommendation, and that the team decides what suits its project and its people." The Code bullet: "(and, in Portuguese, that their names are in Portuguese)" becomes "(and, in Portuguese, that their Portuguese names are a teaching choice, not a recommendation)". §Languages (the Portuguese edition's example code has Portuguese names) and the Evidence rule on what is translated stay: they tell a writer what to translate, not what the reader is told. Source: the author's draft ("update it to the new note"), docs/05 §7 (a delivery that changes behaviour updates the document that owns it).
5. *English untouched.* The English edition's code is in English, the language its reader expects, and it has no sentence on names; the choice and the note exist only in Portuguese, so ADR-0004's "a change to both" is met as in `pt-ninjobs-article` decision 5. Source: the author's draft, ADR-0004, work/done/pt-ninjobs-article.md.
6. No new docs/03 term, no new queue line, no split.

**Behaviour.**

* A reader of the Portuguese edition, at chapter 3's first code block, reads: "Nesta edição, os nomes do código estão em português por uma escolha didática, não como recomendação: cabe à equipe decidir o que é melhor para o projeto e para as pessoas dele."
* The same reader no longer reads which names are translated, that identifiers have no accents, or that `function`, `return` and library names stay as they are.
* The reader of chapters 4, 7, 11, 14 and 22 still reads, where a kit name or a log field first appears, that it stays in English.
* A writer opening docs/04 §Writing the book finds chapter 3's note described as the new one, in Evidence and in the Code bullet, word for word as decision 4 quotes.
* Checked at apply time:
  * `grep -n "sem acentos" book/pt/03-simplicity-and-results.md` prints nothing.
  * `grep -n "escolha didática" book/pt/03-simplicity-and-results.md` prints one line, just before the first code block's lead-in.
  * `grep -rn "escolha didática" book/pt` prints that line only: the note is said once.
  * `grep -n "names are in Portuguese" docs/04-Conventions.md` prints nothing.
  * `git diff --stat book/en README.md README.pt.md` shows nothing changed by this delivery.
* Fails: the old sentence or part of it left in chapter 3; the note said twice or in another chapter; a kit-name sentence of chapters 4, 7, 11, 14 or 22 removed; any text of the English edition changed; docs/04 still describing the old note; an em dash.

**Contract.**

* Files: `book/pt/03-simplicity-and-results.md`, the one line at pt 03:25 at /propose; `docs/04-Conventions.md`, the Evidence line on chapter 3 (docs/04:28 at /propose) and the Code bullet's parenthesis (docs/04:50).
* Terms of docs/03: none. Sources: none added or removed. Cases: none. Exercises: none (ADR-0017).
* docs/00, docs/01, docs/02, docs/03, docs/05: no change. docs/06: this line's marks only, set by the driver and by /apply; no new queue line.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Deliveries in flight on the same files.** `ch03-literal-type-comment` edits chapter 3's refusal example (the section `Uma função pura`, pt 03:122) and `ch03-error-languages` edits the section `Exceção, recusa, erro` (pt 03:164); both edit both editions, far from pt 03:25. `early-no-forward-links` edits chapters 0 to 7 of both editions where a pointer to a later chapter stands; pt 03:25 holds no link, and if it rewrites a neighbouring line, whichever lands second edits the paragraph as the first left it. `pt-ninjobs-masculine` changes pt 03:7's heading, a hunk apart. `docs04-code-layout` edits the same Code bullet of docs/04 to add the rule on blank lines: this delivery changes only the parenthesis on chapter 3's note, and whichever lands second keeps the other's clause. No line order is needed; `m18-review` reads all of them after.

**Out of scope.**

* The English edition: decision 5.
* The kit-name sentences of chapters 4, 7, 11, 14 and 22: decision 3; the author can name any of them in a new line.
* The rule on which names the Portuguese code translates (docs/04 §Languages and Evidence): unchanged, decision 4.
* `work/done/`: the record of what was decided, not rewritten (`m16-review` decision 4).

**Done when.**

* [x] pt 03:25 replaced by Behaviour's sentence; Behaviour's checks give what it names.
* [x] docs/04's two places read as decision 4 quotes.
* [x] Chapter 3 still opens with its value, keeps its gain, no filler and nothing useful cut.
* [x] Every number sourced: no number added.
* [x] `make verify` green: edition parity, prose rules, width, disclosure scan, no em dash.
* [x] The author's approval of an anonymized passage: inapplicable, the change draws on no Case A or Case B passage (docs/00 OD-3).
* [x] `make book` run; both PDF paths given to the author.
* [x] Page in `work/done/`, the line `[x]`, staged by its paths and its hunks of docs/04 and docs/06, commit message in a `commit` block.

**Proof.**

* pt 03:25 now reads Behaviour's sentence, between pt 03:24 and the first code block's lead-in.
* `grep -n "sem acentos"` on chapter 3 and `grep -n "names are in Portuguese" docs/04-Conventions.md` print nothing; `grep -rn "escolha didática" book/pt` prints pt 03:25 only.
* `git diff --stat book/en README.md README.pt.md` showed nothing from this delivery; changes there belong to other deliveries in flight.
* `make verify` green: build, parity, em dash, prose, width, links, disclosure.

**Divergences.** None from Behaviour.

**Decisions taken in /apply.**

* Run in a batch of applies on one tree: the driver marks this line in docs/06, runs `make book` once at the end of the batch and gives both PDF paths, and stages and commits this delivery by its paths and hunks.

**Review.** One read-only agent on Opus read the hunks of `book/pt/03-simplicity-and-results.md` and `docs/04-Conventions.md` against this page and docs/04, and checked the kit-name sentences of pt 04, 07, 11, 14 and 22 and the English edition: no findings.

```commit
docs(pt-identifiers-choice): say pt names are a teaching choice

- Portuguese chapter 3: the note on translated names becomes one sentence: Portuguese names are a teaching choice, not a recommendation; the team decides
- docs/04: Evidence and the Code bullet describe the new note

work/done/pt-identifiers-choice.md
```
