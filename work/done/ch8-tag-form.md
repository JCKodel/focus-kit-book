# ch8-tag-form

**Objective.** A reader of chapter 8 knows why the brownfield project's chapter tag is `book-v1-analyze`, with a hyphen, and not the `book-v1/<chapter-slug>` form chapter 5 taught for the guided project.

**Behaviour.**

* Where chapter 8 first names the chapter tag in its text, the sentence "The excerpts below are quoted at the chapter tag `book-v1-analyze`, as committed." (EN line 166, PT line 167), one sentence follows it: the fork already holds the tag `book-v1`, the frozen upstream, and git refuses a tag `book-v1/analyze` beside it, so the brownfield project's chapter tags take a hyphen where the guided project's take a slash (chapter 5).
* The reason given is git's, not a style choice: with a tag `book-v1`, `git tag -a book-v1/analyze` fails with "cannot lock ref 'refs/tags/book-v1/analyze': 'refs/tags/book-v1' exists" (checked with git 2.55.0 while writing this page). The chapter paraphrases it; it does not quote the error.
* The Portuguese says the same after its line 167, keeping the term "tag do capítulo".
* Nothing else in chapter 8 changes: line 64 still introduces `book-v1`, the exercises and the note `analyze-run` keep their tags.
* Finding F9 of the M3 review is settled.

**Contract.**

* Files: `book/en/08-analyze.md` and `book/pt/08-analyze.md`, one sentence added after line 166 (EN) and 167 (PT).
* Terms of docs/03: chapter tag, brownfield project, guided project. No new term; docs/03's row for chapter tag already lists both forms.
* Sources: none added; the fact is git's behaviour, which the reader can repeat, and docs/05 §5 "Brownfield project" already records it. No source note.
* Cases: none. Exercises: unchanged.

**Out of scope.**

* Chapter 5's sentence on `book-v1/<chapter-slug>`: it describes the guided project and is right as it stands.
* Renaming the fork's tags: a published tag never moves (docs/05 §5).
* `ch8-accept-edits`, the other chapter 8 finding: its own delivery.

**Done when.**

* [x] Both editions changed, same meaning; the reason is git's refusal, named in plain words.
* [x] `make verify` green.
* [x] `make book` run, and both PDF paths given to the author.
* [x] Page in `work/done/`, `[x]` in docs/06, staged, commit message suggested.

**What happened.**

* Chapter 8, English line 167: "The brownfield project's chapter tags take a hyphen where the guided project's take a slash (chapter 5) because the fork already holds the tag `book-v1`, the frozen upstream, and git refuses to create a tag `book-v1/analyze` beside it."
* Chapter 8, Portuguese line 168: "As tags do capítulo do projeto brownfield levam hífen onde as do projeto guiado levam barra (capítulo 5) porque o fork já tem a tag `book-v1`, o upstream congelado, e o git se recusa a criar uma tag `book-v1/analyze` ao lado dela."
* The refusal was checked again in a scratch repository with git 2.55.0: `git tag -a book-v1/analyze` beside `book-v1` fails with "cannot lock ref". The chapter paraphrases it and quotes no error.
* Nothing dropped, nothing diverged from the plan; no document changed, docs/03 and docs/05 §5 already held both forms. Finding F9 of the M3 review is settled.
* Proof: `make verify` green; `make book` builds both editions, `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.
