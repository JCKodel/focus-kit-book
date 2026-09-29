# ch4-adr-docs05

**Objective.** A reader of chapter 4 can picture the ADRs among the six places a Ninjobs decision lived, and docs/05 as the home of the rule that came later, because each is said in a few words where it first appears, with a pointer to chapter 6.

**Behaviour.**

* In §"How it was", the first "ADRs" gains a few words: an architecture decision record, one file per decision (docs/03's meaning).
* In §"Where it went", in the paragraph that begins "One rule came later", "docs/05" gains a few words: the process document, whose "This project" section holds the facts the commands read.
* One of the two, the later one, points to chapter 6, where every document is described.
* §"What went wrong" keeps its list of six places as it is; the first mention already explained the ADRs.
* Both editions say the same; the Portuguese uses docs/03's "registro de decisão de arquitetura".
* Finding F4 of the M3 review is settled.

**Contract.**

* Files: `book/en/04-birth-of-focus-kit.md` and `book/pt/04-birth-of-focus-kit.md`, lines 9 and 37 today.
* Terms of docs/03: ADR, project documents, slot (named in words, not as the term, unless the sentence stays shorter with it). No new term.
* Sources: no new note; the pointer to chapter 6 is a relative link, `06-the-documents.md`.
* Cases: Ninjobs, unchanged. Exercises: none; chapter 4 has none.

**Out of scope.**

* The failure behind each rule: `ch4-rule-failures`, its own delivery, in the same chapter.
* Explaining the documents, specs, changes and outline of the six places: the documents and specs are met in chapter 3; the outline stays a word.

**Done when.**

* [ ] Both editions changed, same meaning; lines 16 and 25 to 30 untouched.
* [ ] `make verify` green.
* [ ] `make book` run, and both PDF paths given to the author.
* [ ] Page in `work/done/`, `[x]` in docs/06, staged, commit message suggested.
