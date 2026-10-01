# author-review-1

**Objective.** A reader opens the PDF on its cover and, from the Prologue to chapter 5, meets no bare pointer, no unexplained organization or study, no footnote that only lists counts, and, in Portuguese, no code they need English to read.

**Behaviour.**

* `make book` writes each edition's PDF with its cover as the first page and each EPUB with its cover image; a missing pypdf or cover is a finding.
* The Prologue explains or rephrases every forward pointer as a sentence, links Ninjobs at its first mention, and says once that the private repositories' numbers were counted by the author; no chapter carries a private-case note.
* Chapter 1 says what METR and DORA are; chapter 2 says what Liu's paper and Chroma are, and its team gain says that every delivery's page (why, done when, what was done) is versioned with the code, so a newcomer asks the agent.
* Chapter 3 gives the original term (Spec-Driven Development, SDD) in Portuguese, defines behaviour in a note box, and says why one page is enough without calling it a price.
* Chapter 4 says what the U-2, the SR-71 and Johnson's rule were, and warns, in a note box before the team gain, that an agent grows a process the way it grows code, with this book's own review spiral as the case.
* Chapter 5 says why a pure, synchronous rule with an orchestrator beats Clean Architecture's async use case with injected repositories; makes the exhaustive switch the reason for a Result; says why an exception becomes a value (the library's domain against the application's, and the compiler's check); explains a throw as a broken return contract; and gains red-green as what "done" means for an agent.
* Chapter 6 names the .NET interface-for-everything habit and where it is ceremony.
* The Portuguese edition's code, file names, slugs, table columns, test names and messages are in Portuguese, chapters 4 to 23.

**Contract.**

* `scripts/build_book.py`: pypdf required; `with_cover` prepends `book/assets/cover-<edition>.pdf` (one page) to weasyprint's output; `--epub-cover-image book/assets/cover-<edition>.png`.
* Note box: a blockquote `> **Note.** ...` / `> **Nota.** ...` (`**Caution.**` / `**Cuidado.**`), styled in `site.css`, `pdf.css`, `epub.css`.
* Terms: behaviour (comportamento), note box (caixa de nota) in docs/03; the running example's Portuguese identifiers listed there.
* Documents: docs/01 (make book, files, errors), docs/03, docs/04 (Portuguese code, note box, introductions and pointers, private cases without notes), docs/06 (cover `[x]`, this line, m8-review reworded), AGENTS.md, both READMEs (pypdf), the release workflow.

**Out of scope.**

* Chapters 6 on beyond what the author's seven points named and the two book-wide rules (private-case notes, Portuguese code): the author is reading them and will send findings.
* docs/05 §8: the review rule stays as written; chapter 4's caution tells what happened without changing the process.
* `[^ninjobs-tokens]` in chapter 23 left with the other private-case notes; chapter 23's text already says how the tokens were counted.

**Done when.**

* [x] Both editions changed together; `make verify` green.
* [x] `make book` writes four files, each PDF opening on its cover, each EPUB with its cover image.
* [x] The author has both PDF paths to review.

## What happened

* The author's seven points, sent by conversation on 2026-09-30, are this page's Behaviour; two questions were asked and answered: the Portuguese edition's code is translated (not glossed), and the private-case notes leave the whole book (not only the Prologue).
* Point 7's "Dependências só onde existe um fake" is in chapter 6, not 5; the .NET paragraph went there. Its red-green request was "talvez"; the section was added to chapter 5, short, pointing to chapter 8 for the rest.
* Point 4's "linha 97" is the key points in the source; the addition went to the team gain and a key point (two key points merged to stay at five).
* The cover PDFs are 419.5 × 595 pt, A5 within a third of a point; no adjustment. pypdf 6.9.2, present in the author's Python, pinned in the release job.
* Every `[^ninjobs]`, `[^case-a]`, `[^case-b]` and `[^ninjobs-tokens]` reference and definition left, 63 references in 17 chapters per edition (counted on the staged diff); the sentences read without them, and chapter 3 keeps one parenthesis on how the 37,228 lines were counted.
* Chapter 13's queue template line, `[ ] <slug>  <what it delivers, one line>`, is still in English in the Portuguese edition; left for the author's reading of chapter 13.
* Portuguese identifiers follow docs/03's fixed words, without accents; `Result`, `ok`, `err`, library APIs and the log's field names stay, and chapter 4 says so once, chapter 23 for the log.
