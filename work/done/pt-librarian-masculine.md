# pt-librarian-masculine

**Objective.** A reader of the Portuguese edition meets the lending library's librarian as "o bibliotecário" in every chapter, as docs/03 fixes the word, never "a bibliotecária" in some chapters and "o bibliotecário" in others.

**Decided without the author** (batch rule of this run: the recommended answer, no question asked).

1. *The word and its gender.* docs/03's running example row fixes "bibliotecário", a masculine noun, and chapters 1, 12, 15 and 21 already write it with masculine articles. The finding (`m17-review`, R3-5) is that chapters 4, 5, 11, 14, 17 and 19 write the feminine. Every feminine form becomes the masculine with the same number: "uma bibliotecária" to "um bibliotecário", "a bibliotecária" to "o bibliotecário", "duas bibliotecárias" to "dois bibliotecários". docs/03 is not changed: it already says the word.
2. *Only the Portuguese edition changes.* English "librarian" has no gender, so the English edition has nothing to change; ADR-0004's "a change to one edition is a change to both" is met with nothing to change in English, as for `pt-ninjobs-article`.
3. *Pronouns stay.* The "ela" of chapter 5:85 ("e ela é testada") refers to "Essa parte", and no pronoun near the other passages refers to the librarian; none changes.
4. *"a diretora da biblioteca" stays.* Chapter 14's second waiting case names the library's director, another person and not a docs/03 term.
5. *Chapter 11's heading and chapter 17's answer change together.* Chapter 17's "Marco 1, uma bibliotecária empresta e recebe de volta" names chapter 11's milestone heading, so both read "um bibliotecário".
6. *No reflow.* "o bibliotecário" has the length of "a bibliotecária", and "um bibliotecário" is one character shorter than "uma bibliotecária", so no fenced line grows and no wrapped paragraph in a block is rewrapped (docs/04 **Width of a block**).
7. *No new check.* A check for the feminine would be a widening of this finding; none is added (docs/05 §8, no widening in this batch).
8. *Trunk; nothing staged by this definition; the driver sets docs/06's marks* (docs/05 §5 Git, this batch's rules).

**Behaviour.**

* Reading the Portuguese chapters 4, 5, 11, 14, 17 and 19, a reader meets "o bibliotecário", "um bibliotecário" or "dois bibliotecários", and never "bibliotecária" or "bibliotecárias".
* The milestone heading of chapter 11 and the answer of chapter 17 name the same milestone in the same words: "um bibliotecário empresta e recebe de volta".
* Every queue and code block in those chapters keeps its columns: no line passes 74 columns.
* Edge: chapters 1, 12, 15 and 21, already masculine, are not changed; "a diretora da biblioteca" in chapter 14 stays.
* Failure: any "bibliotecária" left in `book/pt/` or `README.pt.md`, a line of `book/en/` changed, a sentence changed beyond its article, numeral and noun, or a block line that grows.

**Contract.** Each replacement found by text, in `book/pt/` only:

* `04-focus.md`: "quando uma bibliotecária empresta este exemplar" to "quando um bibliotecário empresta este exemplar"; "Uma bibliotecária empresta um exemplar a um membro." to "Um bibliotecário empresta um exemplar a um membro."
* `05-testing-each-piece.md`: "já que duas bibliotecárias podem apertar" to "já que dois bibliotecários podem apertar".
* `11-queue-and-milestones.md`, in the ````markdown block: "## Marco 1: uma bibliotecária empresta e recebe de volta" to "## Marco 1: um bibliotecário empresta e recebe de volta"; "Quando ele fecha, uma bibliotecária consegue cadastrar livros, seus" to "Quando ele fecha, um bibliotecário consegue cadastrar livros, seus"; the three queue lines "a bibliotecária cadastra livros e seus exemplares", "a bibliotecária cadastra, suspende e reativa membros", "a bibliotecária empresta, e as regras podem recusar" to "o bibliotecário ..." with the rest unchanged. In the prose: "\"uma bibliotecária consegue emprestar um exemplar a um membro por 21 dias\"" to "\"um bibliotecário consegue emprestar um exemplar a um membro por 21 dias\""; "uma bibliotecária não consegue emprestar um exemplar" to "um bibliotecário não consegue emprestar um exemplar".
* `14-queue-states.md`: the queue lines "a bibliotecária cadastra livros e exemplares", "a bibliotecária cadastra e suspende membros", "a bibliotecária empresta um exemplar ou a regra nega" to "o bibliotecário ..."; "então a bibliotecária pede para segurar" to "então o bibliotecário pede para segurar".
* `17-project-as-assistant.md`: "Marco 1, uma bibliotecária empresta e recebe de volta: 4 de 7 feitas." to "Marco 1, um bibliotecário empresta e recebe de volta: 4 de 7 feitas."
* `19-worktrees.md`, in the conflict block, four lines: "a bibliotecária registra que um exemplar voltou" (twice) and "a bibliotecária vê os empréstimos vencidos" (twice) to "o bibliotecário ..."; in the list of decisions: "já que a bibliotecária cobra primeiro o" to "já que o bibliotecário cobra primeiro o".
* **Terms of docs/03.** `running example`'s fixed word "bibliotecário"; no new term, no docs/03 change.
* **Sources.** None added or removed. **Cases.** None: the lending library, already said to be written for the book.
* **Shared files.** `book/pt/19-worktrees.md` is also changed by `conflict-same-lines` and `ch19-adjacent-mark-staging` (other sessions, around the passage on a batch's adjacent marks, near lines 270 and 317); this page's lines are 195 to 199 and 251, so stage this delivery by hunk. `book/pt/14-queue-states.md` is also changed by `ch14-m1-return-book`, which applies after this page (batch order) and writes its new line with no word for the librarian; if this delivery is not yet committed when that one applies, its hunk is staged against the index, which already holds these lines.
* **docs/06.** None from this page; the driver sets its line's marks.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Out of scope.**

* Chapters 1, 12, 15 and 21: already masculine.
* The English edition: "librarian" has no gender.
* A check that rejects the feminine: not this finding (decision 7).
* "a diretora da biblioteca": another person (decision 4).

**Done when.**

* [x] Every replacement of the Contract made, and no other change: `git diff --stat book/en` empty, and each changed line of `book/pt/` differs only in its article, numeral and noun.
* [x] `grep -rn "bibliotecária" book/pt README.pt.md` finds nothing; `grep -c "bibliotecári"` on each file of `book/pt/` gives the same count as before the delivery (30 lines in all).
* [x] Every chapter still opens with its value; no filler, nothing useful cut.
* [x] No em dash; `make verify` green (build, parity, em dash, prose, width, links, disclosure).
* [x] The Delivery review ran on this delivery's paths and the files it created (docs/05 §5), and the page records it.
* [x] The author's approval of an anonymized passage: inapplicable, no Case A or Case B passage.
* [x] `make book` builds; the delivery ends with the paths of both PDFs for the author's review.
* [x] Page moved to `work/done/`, the line `[x]`, staged by explicit paths, by hunk for `book/pt/19-worktrees.md` and this line's hunk of docs/06; the commit message suggested, `docs(pt-librarian-masculine): ...`.

**Divergences.** The page counted 31 lines with "bibliotecári" in `book/pt/`; the real count is 30, before and after the delivery (01:1, 04:2, 05:1, 11:7, 12:2, 14:4, 15:4, 17:1, 19:5, 21:3). The Done when item now says 30.

**Proof.** `git diff --stat book/en` empty; 20 lines of `book/pt/` changed, each only in its article, numeral and noun (12 "a" to "o", 6 "uma" to "um", 1 "duas bibliotecárias" to "dois bibliotecários"); `grep -rn "bibliotecária" book/pt README.pt.md` finds nothing; `make verify` green; `make book` builds `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.

**Delivery review.** One read-only agent on Opus read this delivery's diff of `book/pt/` and its line of docs/06 against this page and docs/04. It found the changed text right (Contract complete, agreement kept, block columns kept, no em dash, `book/en` untouched) and one error on the page: the count of 31, fixed above.

**Decisions.** None beyond the page's.

```commit
docs(pt-librarian-masculine): say "o bibliotecário" throughout pt

- pt chapters 4, 5, 11, 14, 17 and 19 write the masculine, as docs/03
- chapter 11's milestone heading and chapter 17's answer match

work/done/pt-librarian-masculine.md
```
