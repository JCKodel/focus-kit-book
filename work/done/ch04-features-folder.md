# ch04-features-folder

**Objective.** A reader of the Portuguese chapter 4 §Vertical slices learns that `features/` stays in English because it is the name this book gives the folder of the slices, as it keeps *feature* untranslated, and is no longer told the kit writes that folder, which it does not. Found by `m16-review` (work/done/m16-review.md, chA-1: "pt 04:56 says the kit writes `features/`; the kit writes no such folder." Seen).

**Decided without the author.** The batch had no one to answer; each choice is the recommended one.

1. *Only the Portuguese edition changes.* The sentence exists only there: docs/04 §Writing the book, Evidence, asks the Portuguese edition to say where `features/` stays in English ("the text says so where such a name appears (... chapter 4's `features/`)"), and the English edition has nothing to translate. ADR-0004's rule, a change to one edition is a change to both, is met: the English edition holds no counterpart, and edition parity compares status, headings and notes, none of which change. Source: docs/04, ADR-0004, chapter 4 en 49 to 58.
2. *The reason given is the book's.* docs/03 fixes `features/<name>/` as the identifier of the vertical slice and keeps "feature" in English in both editions ("never 'funcionalidade'"); the folder is FOCUS's, the book's optional architecture (ADR-0016), and the kit's installed files create no `features/` (`grep -rln "features/" .claude/skills .agents/skills` finds no file on 2026-10-18). The sentence keeps its second half, the Portuguese names of the slices. Source: docs/03 (`vertical slice`, `feature`), ADR-0016.
3. *docs/04 stays.* Its Evidence paragraph lists `features/` beside the kit's own names but apart from them ("the kit's own names (...) and `features/` stay"), so it does not say the kit writes it. Source: docs/04 as it stands.
4. No docs/03 term, no new queue line, no split.

**Behaviour.**

* A reader of the Portuguese chapter 4 §Fatias verticais reads, in place of "A pasta `features/` fica em inglês, como o kit a escreve e assim como este livro diz *feature*, sem traduzir; cada fatia dentro dela tem um nome em português, da biblioteca de empréstimos: `emprestimos/`, `membros/`, `catalogo/`.":
  "A pasta `features/` fica em inglês, porque é o nome que este livro dá à pasta das fatias, assim como ele diz *feature*, sem traduzir; cada fatia dentro dela tem um nome em português, da biblioteca de empréstimos: `emprestimos/`, `membros/`, `catalogo/`."
* Checked on `book/pt/04-focus.md`: `grep -c "como o kit a escreve"` gives 0; `grep -c "o nome que este livro dá à pasta das fatias"` gives 1. `grep -rn "features/" book/pt book/en | grep -i "kit"` finds nothing.
* `book/en/04-focus.md` is unchanged.
* Fails: the sentence still saying or implying the kit writes `features/`; the slices' Portuguese names dropped; any other line of chapter 4 changed; the English file changed; an em dash.

**Contract.**

* Files: `book/pt/04-focus.md`; no other file.
* Section and line: §Fatias verticais (the section the English edition calls §Vertical slices), the sentence at pt line 56 in the working tree of 2026-10-18; the text is the locator, the number a courtesy.
* Terms of docs/03: none new (`feature`, `vertical slice` / `fatia vertical`, as they are). Sources: none added or removed. Cases: none. Exercises: none (ADR-0017).
* docs/00 to docs/05: no change. docs/06: this line's marks only, set by the driver and by /apply; no new queue line.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Deliveries in flight on the same chapter.** `pt-ninjobs-article`, applied last, may touch `book/pt/04-focus.md`; chapter 4 already writes "Na Ninjobs", the feminine that page recommends, so no hunk is shared.

**Out of scope.**

* The English edition: decision 1.
* docs/04's Evidence paragraph: decision 3.
* Other English names kept in the Portuguese edition: right as they are, and each said where it first appears (docs/04).

**Done when.**

* [x] The Portuguese edition changed as Behaviour says; its greps give the results it names; the English file unchanged.
* [x] Chapter 4 still opens with its value, keeps its gain, no filler and nothing useful cut.
* [x] Every number sourced: no number added.
* [x] `make verify` green: edition parity, prose rules, disclosure scan, no em dash.
* [x] The author's approval of an anonymized passage: inapplicable, the change draws on no Case A or Case B passage (docs/00 OD-3).
* [x] `make book` run; both PDF paths given to the author.
* [x] Page in `work/done/`, the line `[x]`, staged by its paths and its hunk of docs/06, commit message in a `commit` block.

**Proof.** On `book/pt/04-focus.md`, `grep -c "como o kit a escreve"` gives 0 and `grep -c "o nome que este livro dá à pasta das fatias"` gives 1; `grep -rn "features/" book/pt book/en | grep -i "kit"` finds nothing; `git diff --stat book/` shows only `book/pt/04-focus.md`, one line. `grep -rln "features/" .claude/skills .agents/skills` finds no file, as decision 2 says. `make verify` green; `make book` built `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.

**Divergences.** None from Behaviour.

**Decisions taken in /apply.**

* The sentence keeps the page's exact wording, "assim como ele diz *feature*" included, though the review found "assim como diz" smoother: Behaviour quotes the sentence whole.
* The review's second note became a queue line, not a fix here: docs/04's Evidence paragraph calls `features/` "a name an external format fixes", while chapter 4 now gives it as the book's name; decision 3 leaves docs/04 out of this page, so `docs04-features-reason` under M16 aligns it.

**Review.** One read-only agent on Opus read the chapter's diff and this line of docs/06 against this page, docs/04 and AGENTS.md: no findings. Two optional notes, both recorded under Decisions taken in /apply.

```commit
docs(ch04-features-folder): give features/ as the book's folder name

- Portuguese chapter 4: `features/` is the book's name, not the kit's

work/done/ch04-features-folder.md
```
