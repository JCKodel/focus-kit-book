# ch3-docs-pointer

**Objective.** A reader of chapter 3 can place focus-kit's edits to `docs/03` and `docs/06`, because the sentence names what the two documents are and points to chapter 6.

**Behaviour.**

* In §"The light row is not free", the sentence with "adding 6 lines and removing 3" names `docs/03` as the project's vocabulary and `docs/06` as its queue, the words the `AGENTS.md` of chapter 2 already uses for them.
* The same sentence, or the next, points to chapter 6, which describes every document.
* Both editions say the same.
* Finding F2 of the M3 review is settled.

**Contract.**

* Files: `book/en/03-spec-driven.md` (line 187 today) and `book/pt/03-spec-driven.md` (line 267 today), that paragraph only.
* Terms of docs/03: project documents, queue; the Portuguese uses "vocabulário" and "fila".
* Sources: the existing `[^spec-driven-run]` note; no new note. The link to chapter 6 is relative, `06-the-documents.md`.
* Cases: none. Exercises: unchanged.

**Out of scope.**

* Describing the other 15 files focus-kit wrote once per project: chapter 6.

**Done when.**

* [x] Both editions changed, same meaning; no other paragraph touched.
* [x] `make verify` green.
* [x] `make book` run, and both PDF paths given to the author.
* [x] Page in `work/done/`, `[x]` in docs/06, staged, commit message suggested.

**What happened.**

* English: the sentence with "adding 6 lines and removing 3" now reads "in `docs/03`, the project's vocabulary, and `docs/06`, its queue; [chapter 6](06-the-documents.md) describes every document." The words are the ones the `AGENTS.md` of chapter 2 uses ("the vocabulary", "queue").
* Portuguese: the same, "em `docs/03`, o vocabulário do projeto, e `docs/06`, a sua fila; o [capítulo 6](06-the-documents.md) descreve cada documento."
* The pointer joins the same sentence, after a semicolon, as chapter 1 did for chapter 3; the `[^spec-driven-run]` note stays at its end, no new note.
* Nothing diverged, nothing dropped. No document changed: docs/03 already holds both terms. Finding F2 of the M3 review is settled.
* Proof: `make verify` green; `make book` builds both editions, and the sentence reads in both PDFs as one line of thought, the edit, what the two files are, then chapter 6.
