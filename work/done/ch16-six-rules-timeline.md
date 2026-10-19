# ch16-six-rules-timeline

**Objective.** After chapter 16 the reader learns what Ninjobs opened on as chapter 6 tells it: one page per delivery, two commands, one queue line per delivery, two checks and the governor, not the six rules the kit's `SETUP.md` lists, which came with the kit after the opening.

**Behaviour.**

* Reading "What the team gains", the reader finds Ninjobs' public opening reached on one page per delivery, two commands, one queue line per delivery, two checks and the governor's question, after the old checks had gone with it through fifteen days that built four screens.
* The reader no longer reads that the opening ran on the six rules of `SETUP.md`: chapter 6 dates the kit, and with it its list of rules, to 2026-09-21, after the opening on 2026-09-10, and names the drift found then as the cause of the slots rule.
* The next sentence, "The governor keeps a process that small...", still reads as following from the one before.
* Chapter 6 and chapter 16 agree on what held at the opening, word for word in the list.

**Contract.** Files: `book/en/16-the-governor.md` and `book/pt/16-the-governor.md`, section "What the team gains" / "O que o time ganha", one sentence, located by content: en "Ninjobs reached its public opening on a process of six rules, the ones the kit's `SETUP.md` lists for every project, and two checks, after the old checks had gone with it through fifteen days that built four screens." / pt "O Ninjobs chegou à abertura ao público com um processo de seis regras, as que o `SETUP.md` do kit lista para todo projeto, e duas verificações, depois de as verificações antigas o terem acompanhado por quinze dias que construíram quatro telas."
The list it gets is chapter 6's key point, en "one page per delivery, two commands, one queue line per delivery, two checks and the governor's question", pt "uma página por entrega, dois comandos, uma linha de fila por entrega, duas verificações e a pergunta do regulador", with a pointer to chapter 6. The fifteen days and four screens stay; they are chapter 6's numbers, sourced there. Ninjobs stays paraphrased; no Case A or Case B passage. Terms of docs/03: delivery, page, command, queue, governor; no new term.

Chapter 16 was being edited by another session while this page was written (`ch16-prevention-evidence`); /apply locates the sentence by its text, not by a line number, and reports a conflict if that sentence is the other delivery's.

**States.** Inapplicable: prose, no screen.

**Visual reference.** Inapplicable: existing chapter layout.

**Out of scope.** Chapter 6's rule map and chapter 23's six rules: they describe the kit as it is now and are true (`ch06-23-kit-rules`). No other chapter claims the opening ran on the six rules (grep of both editions).

**Decisions from the documents.** The queue line lists "one page, two commands, two checks and the governor"; the page adds "one queue line per delivery", because chapter 6 lists it among what held on Ninjobs (its restart section and key point), and the two chapters should name the same list.

**Done when.**

* [x] Both editions written, same hunks; each Behaviour line checked against both and against chapter 6.
* [x] The chapter opens with its value and keeps its evidenced team gain; no filler and nothing useful cut; every number keeps its source; no em dash.
* [x] The Ninjobs passage stays paraphrased, exposing no infrastructure or plan; no Case A or Case B passage changed or added, so the author's OD-3 approval is inapplicable.
* [x] `make verify` green after the last edit; `make book` builds both editions and the page gives `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf` for the author's review. Under the batch, the driver runs `make book` once at the end.
* [x] Delivery review by a read-only Opus agent per docs/05 §5, its candidates answered on this page; page archived and commit message suggested.

**Built.** Chapter 16's sentence in "What the team gains" / "O que o time ganha" now says Ninjobs reached its public opening on a process of one page per delivery, two commands, one queue line per delivery, two checks and the governor's question, with a pointer to chapter 6, which tells the story; the six rules and `SETUP.md` are gone from it. The fifteen days and four screens stay. The list is chapter 6's key point word for word in each edition.

**Divergences.** The sentence keeps "a process of" / "um processo de" before the list, so the next sentence's "a process that small" / "um processo desse tamanho" still points back to a process (the delivery review's point).

**Decisions.** The pointer reads "([chapter 6](06-birth-of-focus-kit.md) tells the story)" / "(o [capítulo 6](06-birth-of-focus-kit.md) conta a história)", the form chapter 16 already uses for chapter 14. `ch16-prevention-evidence` was committed; the sentence was found by its text and was not that delivery's, so no conflict. Under the batch, the driver sets this line's mark, stages and runs `make book`.

**Proof.** `git diff HEAD` of both chapter files shows one line changed in each, the same hunk. `make verify` green after the last edit.

**Delivery review.** A read-only agent on Opus read both chapters' diff against this page, docs/04 and chapter 6. Every Behaviour line holds in both editions; the list matches chapter 6 line 87 word for word; the dates fit (kit 2026-09-21, opening 2026-09-10); the numbers keep their source in chapter 6; no em dash; the Portuguese reads naturally. Point: (1) dropping "a process" weakened the link to the next sentence's "a process that small": fixed, "a process of" / "um processo de" restored before the list, which stays word for word.

```commit
docs(ch16-six-rules-timeline): say what Ninjobs opened on, per chapter 6

- chapter 16 lists what held at the opening, chapter 6's key point
- it no longer says the opening ran on SETUP.md's six rules
- both editions

work/done/ch16-six-rules-timeline.md
```
