# Conventions

## Languages

* Process documents (`docs/`, `work/`, ADRs, commit messages): English.
* Identifiers, file names and slugs: English.
* The book: English is the source (`book/en/`), Portuguese the translation (`book/pt/`, Brazilian Portuguese).
  A change to one edition is a change to both, in the same delivery (ADR-0004).
* The Portuguese edition uses the Portuguese term of docs/03, and no synonym.
* The README exists in both languages, `README.md` and `README.pt.md`, with the same sections in the same order; a change to one is a change to both, in the same delivery.

## Writing the book

* **Value first.** The chapter's first paragraph says what the reader can do after it.
* **No filler.** Cut every sentence that does not carry information: no recap of the previous chapter, no announcement of the next. Never cut useful content, and never pad, to reach a length; there is no length target.
* **Voice.** The author tells stories in the first person ("when Ninjobs stalled, I..."); instruction speaks to the reader as "you".
* **One sentence per line** in the Markdown source.
* **No em dash** in any text a reader reads, in either edition. Use a comma, a colon, parentheses or a new sentence.
* **Anti-AI prose rules**: a short list of patterns that make text read as machine-written, checked by `make verify`; written by `prose-rules`.
* **Evidence.** Every number cites its source: a primary publication, or the case's recorded artifact.
  Every artifact shown (a page, a queue, a command output) comes from a real run.
* **Code** is TypeScript only, quoted from a tag of the guided project's repository with its path.
* **Private cases** appear only as Case A and Case B; docs/03 §Entities and invariants says what may never appear.

## Chapter shape

Fixed by `chapter-template`; until then:

1. Title.
2. What you get: at most three sentences.
3. The content, in sections.
4. Key points: at most five bullets.
5. Exercises (Part II onwards), numbered `N.M`, on the guided project.

## Files

* Chapters: `book/<edition>/NN-<slug>.md`; appendices `A<n>-<slug>.md`.
* Images: `book/assets/NN-<what>.png|svg`; text inside an image is avoided, so one image serves both editions.

## Tests

There is no product code to test.
The checks are the tests: site build (strict), edition parity, em dash, prose rules, links, disclosure scan.
Each lives in `scripts/` and runs from `make verify`.
A new check enters only when it names the error it would have caught (docs/05 §7).

## Commit messages

Imperative subject up to 72 characters, `<type>(<slug>): <subject>`, where type is `feat`, `fix`, `docs` or `chore`.
Body up to five one-line bullets.
Last line: `work/done/<slug>.md`.
