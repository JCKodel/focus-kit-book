# spec-driven

**Objective.** After chapter 3 the reader can say what Spec-Driven Development is and how far a tool takes the spec (spec-first, spec-anchored, spec-as-source), name what Spec Kit and OpenSpec got right, and show, with the numbers of one recorded run, where they weigh more than the feature needs.

**Behaviour.**

* The reader can define a spec and Spec-Driven Development in one sentence each, and place a tool on Böckeler's three levels.
* The reader can say what the two tools got right: the decision written before code, in files the agent reads at the start of a session (chapter 2); a project-wide file written once (Spec Kit's constitution); a question asked before writing, as OpenSpec asked about the slots the brief assumed and the code did not have.
* The reader can read the run's table: what each tool installs, writes once per project and writes per feature, for the same brief, and knows it is one run, one model, one day.
* The reader can say where the weight is: per feature, Spec Kit wrote 8 files and 756 lines, OpenSpec 6 and 180, the page of chapter 4 1 and 82; the one 24-hour rule is restated in 8 of Spec Kit's 8 files and in 4 of OpenSpec's 6; every one of those files is something a person has to review.
* The reader sees that the light row is not free: focus-kit writes the most once per project (17 files, 277 lines), and its `/propose` also edited two of those files.
* The reader can check every number in the run's folder and repeat the run.

**Contract.**

Chapter 3, `book/en/03-spec-driven.md` and `book/pt/03-spec-driven.md`:

* Title: "Spec-Driven Development" / "Desenvolvimento Guiado por Especificação". "What Spec Kit and OpenSpec got right and where they weighed too much" is the opening's job, not the title's.
* Sections, in order (headings may be reworded in the writing; both editions keep the same structure):
  1. Opening, at most three sentences: the Objective.
  2. What a spec is: Böckeler's definition of a spec and of SDD; the three levels; Kiro in one sentence (the lightest of her three, mostly spec-first), Tessl in one (the only one aiming at spec-anchored and exploring spec-as-source), both through her article. Spec Kit and OpenSpec introduced by what they are, at the versions the run pinned.
  3. One feature, three tools: the run in a paragraph (the same four-file TypeScript project, the same brief, each tool's default path, stopped before code, 2026-09-25, `claude-opus-5-5`), then the full table of the run's README, the three rows of each tool. focus-kit is labelled as the method of this book, taught from chapter 4; the chapter does not explain it.
  4. What they got right: the points of Behaviour's second bullet, each shown from the run. Spec Kit asked nothing and wrote its assumptions into the spec; the chapter says the optional `clarify`, which exists to ask, was not run.
  5. Where they weighed too much: the per-feature row; the rule count; the three excerpts below; Böckeler's finding that Spec Kit's files were "repetitive, both with each other, and with the code that already existed" and "very verbose and tedious to review". Then the honest line: focus-kit's once row is the largest and its `/propose` added 6 lines and removed 3 in docs/03 and docs/06; the trade is to decide once per project and write one page per feature. The run says what each tool writes, not which one builds better software.
  6. Key points. No exercises (Part I).
* Voice: "you" throughout; no case story. Ninjobs stays out (chapter 4; chapter 1 already gave its OpenSpec numbers).
* docs/03 terms introduced: `spec` (new), `spec-first`, `spec-anchored`, `spec-as-source` (new, written by /propose), `Spec-Driven Development`. The Portuguese edition uses "especificação" for spec, keeps the three levels in English and puts the Portuguese of docs/03 in parentheses on first use.
* The name is "Spec Kit", as the tool's README writes it; the run folder's `speckit/` and its README stay as recorded.
* Sources, each checked on 2026-09-25:
  * `[^bockeler-2025]`: Birgitta Böckeler, "Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl", 2025. https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html. Confirmed (dated 15 October 2025): the definition of a spec ("a structured, behavior-oriented artifact [...] written in natural language that expresses software functionality and serves as guidance to AI coding agents"); the three levels; "All SDD approaches and definitions I've found are spec-first, but not all strive to be spec-anchored or spec-as-source"; Kiro "the simplest (or most lightweight)", "mostly spec-first"; Tessl "the only one of these three tools that explicitly aspires to a spec-anchored approach, and is even exploring the spec-as-source level"; spec-kit "created a LOT of markdown files for me to review. They were repetitive, both with each other, and with the code that already existed", "very verbose and tedious to review". Her own caveat, that the tools change fast, goes into the chapter.
  * `[^spec-kit]`: GitHub, Spec Kit, v1.0.11. https://github.com/github/spec-kit/tree/v1.0.11. The chapter describes the tool at this tag, not at `main`, whose README now offers three processes.
  * `[^openspec]`: Fission AI, OpenSpec, 1.13.2. https://github.com/Fission-AI/OpenSpec/tree/v1.13.2 (the npm page answers the link check with 403).
  * `[^spec-driven-run]`: this book's run, 2026-09-25. https://github.com/JCKodel/focus-kit-book/blob/53109f372125e8aeda200bb2e5bbd1ad7bcc5d61/work/done/spec-driven-run/README.md. Every count of the table comes from it.
  * `[^rule-count]`: counted in that folder with `grep -rliE '24 ?h|24-hour|24 hours' <tool>/feature | wc -l`, against the per-feature file count: Spec Kit 8 of 8, OpenSpec 4 of 6, focus-kit 1 of 1.
* The only numbers in the chapter are the table's, the rule count, the 6 and 3 lines of the diff, and 2025 as Böckeler's year.
* Excerpts, the same rule (a cancellation exactly 24 hours before is accepted) as each tool wrote it, copied byte for byte from the run folder, in English in both editions, each followed by one sentence in the edition's language saying what it says:
  * Spec Kit: `speckit/feature/specs/001-cancel-appointment/spec.md`, lines 30 to 32.
  * OpenSpec: `openspec/feature/openspec/changes/add-client-cancellation/specs/appointment-cancellation/spec.md`, lines 16 to 18.
  * focus-kit: `focus-kit/feature/work/cancel.md`, line 16.
  None of those lines holds an em dash today; /apply checks before copying, since the em dash exemption covers only the run folder.
* Cases: none; no OD-3 approval.

Files:

```
book/en/03-spec-driven.md   chapter 3, no status: draft when done
book/pt/03-spec-driven.md   chapter 3, no status: draft when done
docs/00-Product.md          §Contents: chapter 3's title, and "Spec Kit"
docs/06-Queue.md            "SpecKit" becomes "Spec Kit" in the two M2 lines; spec-driven [x]
docs/03-Domain.md           spec, spec-first, spec-anchored, spec-as-source (written by /propose)
```

**Out of scope.**

* Cost and time of each run: the figures stayed in the scratch folder, so they have no source a reader can check.
* The permission modes the run needed, focus-kit's install in `bypassPermissions` above all: a fact about installing, for chapter 5.
* Ninjobs and how focus-kit was born: chapter 4.
* How focus-kit works: chapters 4 to 13.
* OpenSpec's archive and spec merge, and Spec Kit's other processes and extensions: the run did not exercise them, and the chapter makes no claim it cannot source.
* Kiro and Tessl beyond one sentence each: not run.
* A second run or model: one run, said plainly.

**Done when.**

* [x] Both editions of chapter 3 written, same headings in the same order, `status: draft` absent from both.
* [x] Opens with its value in at most three sentences; ends with at most five key points; no exercises.
* [x] No filler and nothing useful cut: every sentence read against docs/00 product question 2.
* [x] Every number and quoted claim carries a source note whose text was found in the publication or the run folder; any not found is dropped and recorded here.
* [x] The table matches the run's README; the rule count repeats with the command of `[^rule-count]`.
* [x] The three excerpts match their files byte for byte.
* [x] The Portuguese edition uses "especificação" and the three levels as docs/03 says, and no synonym.
* [x] docs/00 and docs/06 say "Spec Kit".
* [x] `make verify` green (build, parity, em dash, prose, links including the source URLs, disclosure).
* [x] `make book` builds; both PDF paths given to the author for review.
* [x] docs/06 line marked `[x]`; page moved to `work/done/spec-driven.md` with what happened.

**What happened.**

* Both editions written with the Contract's six sections; `status: draft` never added. The opening is two sentences, key points five, no exercises.
* Diverged from the Contract, `[^spec-kit]`: the page said the tag describes one process and `main` "now offers three". The README at `v1.0.11` (tag `8147943`) already offers three processes, Spec-Driven Development in core and the other two as extensions. The chapter introduces Spec Kit as that README does, a toolkit of processes of which the run used SDD, and quotes the SDD line "Constitution once per project; specify → plan → tasks → implement → converge per feature".
* Diverged from docs/04: it said the Portuguese edition translates an English prose artifact; the page keeps the three excerpts in English in both editions so they match their files byte for byte. docs/04 §Evidence now says so: an excerpt shown as evidence of how a tool worded something stays as written, followed by one sentence in the edition's language.
* Widened: docs/04 §Chapter shape knew only `<year>` or `accessed YYYY-MM-DD` in a source note; it now says a tool cited at a tag or release carries its version there, as the page's `[^spec-kit]` and `[^openspec]` do.
* Widened by one word: docs/04 §Tests said "SpecKit"; it says "Spec Kit" now, with docs/00 and docs/06. The run folder keeps its spelling. docs/00 §Contents gives chapter 3's title alone, like its neighbours.
* Sources, all checked on 2026-09-25: Böckeler's article (dated 15 October 2025, title from its `<h1>`) holds every quotation used, the SDD definition included; her definition of a spec has "- or a set of related artifacts -" in the middle, cut with `[...]` as the page asked. OpenSpec's line is from its README at `v1.13.2`; its tagline and bullets carry em dashes and were not used. The OpenSpec question and Spec Kit's "Assumptions" come from the run folder (`openspec/questions.md`, `speckit/.../spec.md`); `[^spec-driven-run]` names the folder's `questions.md` files. Spec Kit's clarification step is sourced from its README ("when you need extra quality gates"). Nothing was dropped.
* The rule count repeats: `grep -rliE '24 ?h|24-hour|24 hours' <tool>/feature | wc -l` gives 8 of 8, 4 of 6, 1 of 1. The +6/-3 matches `focus-kit/propose-docs.diff`.
* Numbers used beyond the page's list: none counted; the run's date, the versions and the model are identifiers of the run, which the Contract asked for.
* Proof: `make verify` green. The three excerpts, taken from each edition's fenced blocks, compared as lines with the file lines the page names: identical in both editions; none holds an em dash. `make book` builds; weasyprint's two `user-select` warnings are the known ones of chapter 2. The chapter brings the book's first table, so docs/05 §5 asked for screens: `work/done/spec-driven-<en|pt>-site-<light|dark>.png` (headless Chrome, 1280 by 4200, over the built site) and `work/done/spec-driven-<en|pt>-pdf-<table|excerpts>.png` (`pdftoppm`, table on page 13 of both PDFs, excerpts on page 15 in English, 15 and 16 in Portuguese as `-excerpts-1` and `-excerpts-2`). The table fits the A5 page. Seen and left: the Spec Kit and OpenSpec excerpt lines run to about 100 characters, so the site scrolls them sideways and the PDF wraps them with a hanging indent; rewrapping would break byte for byte.
