# ch16-ceiling-moves

**Objective.** After chapter 16 a reader can say how the kit puts the governor to work on its own text: each command is short enough to read whole, and since a full command sends its words somewhere else, the files they go to, `SETUP.md` §1, the docs/05 template and `documents.md`, have ceilings too, and a change that would pass one removes as much as it adds. The reader can also do the same in their own project: when they cap the size of a step, they cap where its words go; both editions.

**Behaviour.**

* Asked how long a kit command may be, the reader answers from the kit's rules: its body is at most thirty lines of prose for `/propose` and fifty for `/apply`, not counting frontmatter and blank lines, and it says which documents to read, what to do and what never to do; a project's own details go in a slot of docs/05.
* Asked what happens to the words a full command cannot hold, the reader says they go to the files around it: `SETUP.md` §1, the steps an agent follows to install and update the kit (chapter 8); the docs/05 template; and `documents.md`, the reference `/brainstorm` and `/analyze` read, which describes each document and holds that template. The reader then says the ceilings: §1 at most 160 lines, the docs/05 template at most 260 non-blank lines, `documents.md` at most 450.
* Asked what a change does when it would pass one of those ceilings, the reader says it removes as much as it adds.
* Asked which error let those ceilings in, the reader names it as the governor asks: a step of §1 had grown into one long sentence that an agent running it could not hold in mind and rewrote as a list for itself. The chapter tells it with no date, no version and no line count of the old text.
* The reader carries the pattern to their own project: a cap on one file (a rules file, a prompt, a command) moves the growth to the files next to it unless they have a cap too, and every cap still answers the governor's question with an error that happened.
* Edge: the reader knows these ceilings are rules of the kit's own repository, binding whoever changes the kit; installing the kit does not put them in a project's docs/05.
* Fails if: the chapter says "no longer", "since", a kit version or a date for the ceilings, gives the old step's line count, compares before and after, narrates a run of either repository, or gives a ceiling number with no source note.

**Contract.**

Chapter `book/en/16-the-governor.md` and `book/pt/16-the-governor.md`, the same passages in both:

* Opening, second sentence (line 4): gains, at its end or as a third sentence, that the reader can cap where a step's words go when they cap the step's size. The first sentence stays.
* A new section after `## It works both ways` and before `## What the process does not have`: `## A ceiling, and where the words go` (pt `## Um teto, e para onde vão as palavras`). It says, in this order:
  * the kit asks the governor's question of its own files: a command is read whole by the agent on every run, so its body stays at most thirty lines of prose for `/propose` and fifty for `/apply`, frontmatter and blank lines aside, with what is specific to one project in a slot of docs/05 ([chapter 7](07-the-documents.md));
  * a full command does not stop the words; they go to the files around it, `SETUP.md` §1 (chapter 8's install and update steps), the docs/05 template and `documents.md` (each named in a few words, as above), so the same ceiling watches them: 160 lines, 260 non-blank lines and 450 lines, and a change that would pass one removes as much as it adds;
  * the error that let them in, said once and with no date, version or count: a step of §1 written as one long sentence, which an agent running it could not hold in mind and rewrote as a list for itself;
  * for the reader's project, one or two sentences: a cap on one file moves the growth next door, so the cap goes where the words go, and each cap names its error like any other step.
  * One source note, `[^kit-rules]`, at the first ceiling number, covering the five numbers and the error: J.C. Ködel, "CLAUDE.md", focus-kit, the rules of the kit's repository, accessed 2026-10-19, <https://github.com/JCKodel/focus-kit/blob/main/CLAUDE.md>; the Portuguese note in the edition's form ("acesso em 2026-10-19"). The kit's prose is English; a quoted phrase, if any, is translated in pt with the note docs/04 asks for, but the passage paraphrases by default.
* `## What the team gains`: unchanged.
* `## Key points`: one new bullet, after the third: the commands stay short enough to read whole, and the files a full command sends its words to have ceilings of their own; a change that would pass one removes as much as it adds. No number in it (docs/04 "Numbers that prove", "One gain").
* Every other section, footnote and sentence stays.

Terms of docs/03 used: governor, slot, command, docs/05. "Ceiling" (pt "teto") is said in plain words, as the kit's rule says it, and needs no docs/03 row: it is used in one chapter only. Sources: focus-kit `CLAUDE.md` §Rules at commit `fd1aa75`, read for this page; its `CHANGELOG.md` entry for 2026.10.19, read only to confirm the error, never cited (docs/04 "The kit as it is"); `SETUP.md` §§1, 3.5 for what §1, `documents.md` and the template are. No private case, no lending library code.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no visual change.

**Out of scope.**

* The governor's other sections (the question, both ways, the eight things, the subagent, the mark, the gain): untouched.
* Chapter 8's account of `SETUP.md` §1's step 4 as a list: `ch08-update-2026-10-19`.
* Chapter 6 and other chapters naming command sizes: none do today; nothing added there.
* The kit repository and its `CLAUDE.md`: read-only.
* docs/03, docs/05, docs/06: no change.

**Decisions from the documents.**

* The ceilings and the error are the kit's, from focus-kit `CLAUDE.md` §Rules (fd1aa75): "Commands stay short enough to read whole ... The same ceiling watches where the words go when a command is full: `SETUP.md` §1 at most 160 lines, the docs/05 template at most 260 non-blank lines, `documents.md` at most 450. A change that would pass one removes as much as it adds."
* The error is told without its date, the old line count or the version: docs/04 "The kit as it is" (no version as a date, no before and after; a rule's reason is the error it prevents) and the driver's rule of no numbers measuring a kit change.
* A source note points to the kit's file, since it gives the reader something to open and carries every number: docs/04 "Evidence" and "Source notes".
* The key point carries no number: docs/04 "Numbers that prove" and "One gain".
* The gain section stays: the new passage applies the governor already summed there (docs/04 "One gain").

**Decisions taken alone.**

* A section of its own, placed after "It works both ways", because the ceiling is the governor deciding what enters the kit's own text; one paragraph inside that section would bury the files and their numbers.
* The error is told in the past as an error that happened, as the governor requires and as the chapter tells its other errors, while keeping docs/04's limits: no date, version, count or old wording. An alternative the author may prefer: say it in the present only ("a step written as one long sentence is one an agent cannot hold in mind and rewrites as a list"), which drops "happened".
* The source note links the kit's `CLAUDE.md` on `main`, as chapter 8 links `SETUP.md` on `main` and the book links its own records on `main`, not a commit hash (ADR-0017).
* "Ceiling" gets no docs/03 row: one chapter uses it, and docs/03 adds a term on its second use.
* The opening gains a clause rather than a new sentence when it reads as well; /apply decides.

**Done when.**

* [ ] Both editions written, the same passages changed in each, Portuguese read as Portuguese.
* [ ] The chapter still opens with what the reader can do after it, now including capping where a step's words go; no filler and nothing useful cut.
* [ ] The five ceilings and the rule "removes as much as it adds" agree word for word in meaning with focus-kit `CLAUDE.md` §Rules, each under the `[^kit-rules]` note.
* [ ] `grep -n -i -E "no longer|since (its|version)|2026\.10\.1|45|before and after" book/en/16-the-governor.md` and `grep -n -i -E "não mais|desde a versão|2026\.10\.1|45|antes e depois" book/pt/16-the-governor.md` find nothing new; no narrated run, no em dash.
* [ ] Every link resolves; every number sourced.
* [ ] Delivery review as docs/05 §5 says.
* [ ] `make verify` green; `make book` builds both editions, and the two PDF paths are reported.
* [ ] Only this delivery's paths and its hunks of docs/06 staged; the page moved to `work/done/` and its commit message suggested.
