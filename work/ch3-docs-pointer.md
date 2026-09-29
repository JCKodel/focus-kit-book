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

* [ ] Both editions changed, same meaning; no other paragraph touched.
* [ ] `make verify` green.
* [ ] `make book` run, and both PDF paths given to the author.
* [ ] Page in `work/done/`, `[x]` in docs/06, staged, commit message suggested.
