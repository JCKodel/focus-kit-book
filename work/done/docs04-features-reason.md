# docs04-features-reason

**Objective.** A person writing or reviewing the Portuguese edition reads in docs/04 §Writing the book, Evidence, the same reason for keeping `features/` in English that chapter 4 gives the reader: it is the name this book gives the folder of the slices, kept as *feature* is kept, and not a name an external format fixes. Found by `ch04-features-folder`'s review (work/done/ch04-features-folder.md, Decisions taken in /apply, second note).

**Decided without the author.** The batch had no one to answer; each choice is the recommended one.

1. *Only the parenthesis that gives the wrong reason changes.* docs/04's Evidence paragraph, in its "Since `author-review-1`" sentence, lists `features/` among "names an external format fixes (a log's fields, `features/`)"; chapter 4 (pt line 54) now says `features/` stays because "é o nome que este livro dá à pasta das fatias, assim como ele diz *feature*". The sentence moves `features/` out of that parenthesis and gives it chapter 4's reason, citing docs/03, which keeps "feature" in English in both editions. Source: docs/04 as it stands, book/pt/04-focus.md line 54, docs/03 (`feature`, `vertical slice`).
2. *The rest of the paragraph stays.* "the text says so where such a name appears (chapter 22's log fields, chapter 4's `features/`)" still holds: chapter 4 says so. The later clause "the kit's own names (...) and `features/` stay" already sets `features/` apart from the kit's names, as `ch04-features-folder` decision 3 found. Source: docs/04.
3. *docs/03 stays.* Its running example row points to "docs/04 §Writing the book, Evidence" for `features/` and says only that the Portuguese code keeps it; the pointer stays right after this change. Source: docs/03.
4. *No chapter changes, so no edition changes.* This is a process document in English (AGENTS.md); ADR-0004's both-editions rule concerns the book, and neither chapter 4 file is touched. No new docs/03 term, no new queue line, no split.

**Behaviour.**

* A person reading docs/04 §Writing the book, Evidence, reads, in place of "`Result`, `ok`, `err` and their fields, and names an external format fixes (a log's fields, `features/`) stay as they are, and the text says so where such a name appears (chapter 22's log fields, chapter 4's `features/`).":
  "`Result`, `ok`, `err` and their fields, names an external format fixes (a log's fields) and `features/`, the name this book gives the folder of the slices, kept in English as *feature* is (docs/03), stay as they are, and the text says so where such a name appears (chapter 22's log fields, chapter 4's `features/`)."
* Checked on `docs/04-Conventions.md`: `grep -c "external format fixes (a log's fields, \`features/\`)"` gives 0; `grep -c "the name this book gives the folder of the slices"` gives 1; `grep -c "chapter 4's \`features/\`"` gives 1.
* `git diff --stat` of the delivery shows only `docs/04-Conventions.md`, one line, and this line's hunk of docs/06.
* Fails: `features/` still called a name an external format fixes; the log's fields losing their reason; the pointer to chapters 22 and 4 dropped; any other sentence of docs/04 changed; a chapter file changed; an em dash.

**Contract.**

* Files: `docs/04-Conventions.md`; no other file besides this page and this line's marks in docs/06.
* Section and line: §Writing the book, Evidence, the sentence beginning "Since `author-review-1`" (line 27 in the working tree of 2026-10-18); the text is the locator, the number a courtesy.
* Terms of docs/03: none new (`feature`, `vertical slice`, as they are). Sources: none added or removed. Cases: none. Exercises: none (ADR-0017).
* docs/00 to docs/03 and docs/05: no change. docs/06: this line's marks only, set by the driver and by /apply; no new queue line.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Deliveries in flight on the same file.** None: of the pages in `work/` on 2026-10-18 (`ch08-update-2026-10-18`, `ch11-blocking-fix`, `ch13-created-files`, `ch14-four-waits`, `ch15-review-base`, `pt-ninjobs-article`), none names `docs/04-Conventions.md` among its files.

**Out of scope.**

* Both editions of chapter 4: they already give the book's reason (`ch04-features-folder`).
* docs/03's running example row: its pointer stays right (decision 3).
* The other names the paragraph lists: their reasons are right as they are.

**Done when.**

* [x] docs/04 changed as Behaviour says; its greps give the results it names; no other file changed but this page and docs/06's line.
* [x] Chapter checks inapplicable: no chapter changes, so no edition, value, gain, number or anonymized passage to check (docs/00 OD-3 inapplicable).
* [x] `make verify` green: prose rules, disclosure scan, no em dash.
* [x] `make book` inapplicable: no chapter changes; both PDFs are untouched by docs/04.
* [x] Page in `work/done/`, the line `[x]`, staged by its paths and its hunk of docs/06, commit message in a `commit` block.

**Proof.** On `docs/04-Conventions.md`, `grep -c "external format fixes (a log's fields, \`features/\`)"` gives 0, `grep -c "the name this book gives the folder of the slices"` gives 1 and `grep -c "chapter 4's \`features/\`"` gives 1; `git diff --stat` shows only `docs/04-Conventions.md`, one line, besides this page and this line of docs/06. `make verify` green.

**Divergences.** None from Behaviour.

**Decisions taken in /apply.**

* The sentence keeps the page's exact wording, though the review noted that "names an external format fixes (a log's fields) and `features/`" could be read, for a moment, as the format fixing `features/` too; the clause that follows gives `features/` its own reason, and Behaviour quotes the sentence whole.
* The page's pointer to the Portuguese chapter 4 now says line 54, where the sentence is, in place of 56; the text stays the locator.

**Review.** One read-only agent on Opus read docs/04's diff, this line of docs/06 and this page against the page, docs/04, docs/03 and the Portuguese chapter 4: no findings that break the page or docs/04. Two optional notes, both recorded under Decisions taken in /apply.

```commit
docs(docs04-features-reason): give features/ the book's reason in docs/04

- docs/04 Evidence: `features/` is the book's name for the slices' folder

work/done/docs04-features-reason.md
```
