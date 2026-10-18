# ch14-resume-moment

**Objective.** After chapter 14 a reader can say why a milestone review's line that waits on a code reading that missed part of its range resumes by `apply`: the review was being built, in the middle of its `/apply`, when the readers' paths showed the gap; both editions.

**Decided without the author** (batch rule of this run: the recommended answer, no question asked).

1. *Where the moment is said.* Inside the fourth bullet of "Waiting: `[?]`" (pt "Esperando: `[?]`"), as the third bullet already says its own, "In the middle of `/apply my-loans`" (pt "No meio de `/apply meus-emprestimos`"). The same phrase, "in the middle of `/apply m1-review`", says the review was being built, and the paragraph after the bullets already maps a line that was `[>]` or `[*]` to `· resume: apply`, so the reader derives the phase the same way for both bullets. No new sentence and no rule repeated (docs/04 "No filler"; finding of `ch14-four-waits`'s Delivery review).
2. *A clause, not a second sentence.* The bullet stays one sentence on one line (docs/04 "One sentence per line"); the review of `ch14-four-waits` judged it dense and correct, and the clause adds six words. "its readers" becomes "the review's readers", so "its" cannot be read as the `/apply`'s.
3. *The phrase is true to chapter 15.* The review's readers start on the person's word in the review's `/apply` session (docs/05 §5 Milestone review, §8), so the line is `[*]` when the gap is found.
4. *Nothing else in chapter 14 changes.* Key point 4, the mark table, the leaving paragraph and the example queue already hold for this case (`ch14-four-waits` decisions 5 and 10).
5. *No docs/03 change.* The `waiting mark` row already says the four cases and the resume phases.
6. *Trunk; nothing staged by this definition; the driver sets docs/06's marks.* docs/05 §5 Git, and this batch's instructions. Chapter 15, which `ch15-review-base` is building in this tree, and the Portuguese article sweep of `pt-ninjobs-article` are not touched; that page applies last and re-reads `book/pt/` as it is then.

**Behaviour.**

* Reading the fourth bullet of "Waiting: `[?]`", a reader finds that the gap was found in the middle of `/apply m1-review`, while the review was being built.
* A reader can say why the line carries `· resume: apply`: the line was `[*]`, and a line that was `[>]` or `[*]` resumes by `apply`, as the paragraph after the bullets says and as the third bullet's `my-loans` does.
* Edge: a reader does not take the review's line for one that waits before its definition: it does not resume by `propose`, and leaves `[?]` when the reason is resolved, the person says so, going back to `[>]` for `/apply m1-review` to read what is missing.
* The Portuguese edition reads the same in the same place, with the Contract's words.
* Failure: the bullet split into two lines, its suffixes or its reason changed, any other sentence of chapter 14 changed, or one edition changed and not the other.

**Contract.**

* **Chapter 14, both editions** (`book/en/14-queue-states.md`, `book/pt/14-queue-states.md`), found by text, in the fourth bullet of "Waiting: `[?]`" (pt "Esperando: `[?]`"), one replacement each:
  * en "so when `m1-review`'s readers list no path of `src/features/catalog/`, the line waits" becomes "so when, in the middle of `/apply m1-review`, the review's readers list no path of `src/features/catalog/`, the line waits".
  * pt "então quando os leitores de `m1-review` não listam nenhum caminho de `src/features/catalogo/`, a linha espera" becomes "então quando, no meio de `/apply m1-review`, os leitores da revisão não listam nenhum caminho de `src/features/catalogo/`, a linha espera".
  The rest of the bullet, its suffixes `· resume: apply · blocked: read all but catalog/` (pt `· resume: apply · blocked: lidos todos menos catalogo/`) included, and every other line of chapter 14 are unchanged.
* **Portuguese words.** in the middle of: `no meio de`, as the third bullet writes it; reader: `leitor`; review: `revisão`. `/apply` and `m1-review` stay in English, as chapter 14 writes them.
* **Terms of docs/03.** `waiting mark`, `milestone review`, `resume` suffixes used as defined. No new term, no docs/03 change.
* **Sources.** None added or removed.
* **Cases.** No private case added; the example is the lending library's, already said to be written for the chapter.
* **docs/06.** None from this page; the driver sets its line's marks.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Out of scope.**

* Chapter 15's review line and its reason: `ch15-review-base` and `ch15-waiting-reason`.
* Key point 4 and the rest of "Waiting: `[?]`": already true for this case (decision 4).
* The Portuguese edition's article for Ninjobs: `pt-ninjobs-article`.
* A rewrite of the fourth bullet into shorter sentences: judged correct by `ch14-four-waits`'s review; not this line's finding.

**Done when.**

* [x] Both editions written in the place the Contract names, the English first; parity green.
* [x] ``grep -c "in the middle of `/apply m1-review`" book/en/14-queue-states.md`` gives 1, and ``grep -c "no meio de `/apply m1-review`" book/pt/14-queue-states.md`` gives 1.
* [x] `git diff book/en/14-queue-states.md book/pt/14-queue-states.md` shows one changed line per edition, the fourth bullet.
* [x] Chapter 14 still opens with its value; no filler, nothing useful cut; still four bullets in "Waiting" and five key points.
* [x] The Portuguese uses the Contract's words and no synonym.
* [x] No em dash; `make verify` green (build, parity, em dash, prose, width, links, disclosure).
* [x] The Delivery review ran on this delivery's paths and the files it created (docs/05 §5), and the page records it.
* [x] The author's approval of an anonymized passage: inapplicable, no new Case A or Case B passage.
* [x] `make book` builds; the delivery ends with the paths of both PDFs for the author's review.
* [x] Page moved to `work/done/`, the line `[x]`, staged by explicit paths and this line's hunk of docs/06; the commit message suggested, `docs(ch14-resume-moment): ...`.

**Proof.** `make verify` green (build, parity, em dash, prose, width, links, disclosure). ``grep -c "in the middle of `/apply m1-review`"`` gives 1 in English and ``grep -c "no meio de `/apply m1-review`"`` gives 1 in Portuguese; `git diff --numstat` shows one line changed per edition, the fourth bullet of "Waiting: `[?]`" (pt "Esperando: `[?]`"); still four bullets there and five key points. `make book` builds:

* `output/one-page-at-a-time.pdf`
* `output/uma-pagina-de-cada-vez.pdf`

**Divergences.** None: both replacements are the Contract's, word for word.

**Delivery review** (docs/05 §5, one read-only agent on Opus, on both chapter diffs, this line's hunk of docs/06 and this page; the delivery created no file). No findings: the clause matches the Contract in both editions, the suffixes are unchanged, the Portuguese uses `no meio de`, `leitores` and `revisão`, the bullet is still one sentence on one line, and the phrase is true to chapter 15, whose readers start on the person's word in the review's `/apply` session, so the line was `[*]` and resumes by `apply`.

**Decisions taken in /apply.** None beyond the page's.

```commit
docs(ch14-resume-moment): say chapter 14's review line waits mid-apply

- the fourth waiting case finds the gap in the middle of
  /apply m1-review, so the line resumes by apply; both editions

work/done/ch14-resume-moment.md
```
