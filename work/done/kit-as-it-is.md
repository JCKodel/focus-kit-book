# kit-as-it-is

**Objective.** A reader of either edition meets focus-kit as it is today: what each rule is, how it works and what the team gains, with no changelog entry, no version as a date, no "before that rule" and no measure taken before and after a kit change; docs/04 holds the rule so later deliveries keep it.

**Decided.**
1. The rule is wider than the queue line: "O livro descreve o processo, como ele funciona, o que ele traz de valor, não changelog do focus-kit." (the author, in this /propose). So the book cites no changelog entry as its reason or its number, not only none that compares versions.
2. A rule's reason stays, said in the present as the error the rule prevents ("without it, a second session would stop on a changed queue"), with no entry, no version and no "a user" (decision 1).
3. A number whose only source is a changelog entry leaves with the entry (4.7 KB, about 180 KB, 80 KB, about 120 lines, six of the eight versions).
4. Case A's `[?]` story stays as Case A's: its idle-looking lines, the mark it added by hand, the governor deciding in that project. What goes is the kit adopting it in a version; the kit's six marks are described as they are (the author's answer here).
5. Chapter 11's update report and its versions stay: they are what the update command prints today (`m13-review` decision 4); so does `metadata.version` and the `Version:` line.
6. Chosen on the author's behalf, to question in review: chapter 11 lines 90 to 92 and key point 152 keep teaching the changelog as a file of the kit, where to read why a migration exists, because that describes the kit as it is; line 93 keeps its link from the changelog's `Migration:` item to the report, without naming the version.
7. `plain-numbers` touches the same gain sections (11, 13, 21), a file conflict (docs/05 §4): its line gets `· after kit-as-it-is` in this delivery.

**Behaviour.**

* A reader of chapters 10, 13, 14, 15, 16, 19, 21 and 22 finds each rule's reason said as the error it prevents, in the present, and no "the kit's changelog", no entry number, no "a user ran".
* A reader of chapter 16 learns the six marks with no "since its version" and no "this chapter follows the kit's version"; `SETUP.md` holding docs/05, whose §4 is the queue, stays. §At the moment the work changes says why a mark set when a command ends is wrong without "under three marks".
* A reader of chapter 18 §the Case A passage learns: the governor decides in each project; Case A's five idle-looking lines were the error that earned Case A its mark; the kit's six marks answer the same error for any team that reads its queue as a board (chapter 16). Line 55's "an error one project proves can change the kit every project installs", line 56's "the kit's three marks", lines 62 to 63 and key point 77 lose the adoption.
* A reader of chapter 22 reads Case A's mark for waiting and that the kit has its own `[?]` (chapter 16), without "took that mark in its version" or "is now the kit's".
* A reader of chapter 17 §When the findings became one delivery reads that the kit's milestone review reads no code, since each delivery's code is read before its commit, without "no longer".
* A reader of chapter 11 reads "a version that changes only the commands reports no migration" without naming 2026.10.08.2 or 2026.10.15; §What the team gains says what an update gives (a list of what to change and where, the team's rules in place; the next command in the host's form, because a host may not recognize another's form) with no count of versions and no sizes.
* A reader of chapter 13 §What the team gains finds the order, code only inside `/apply` and one sentence per line explained as what each prevents, without this book's queue sizes before and after; the M12 `· after` example stays, saying each line needs the update `kit-2026-10-13` done first, not "brings chapters to the kit's version".
* Checks, both editions: `grep -nE "20[0-9]{2}\.[0-9]{2}\.[0-9]{2}" book/*/[0-9]*.md` matches only in chapter 11 §What an update reports and the slug `kit-2026-10-13` in chapter 13; `grep -niE "changelog"` matches only chapter 11 §What an update reports and its key points; in chapters 10 to 22, `since its version`, `in its version`, `before that rule`, `since then`, `took (it|that mark)` (pt `desde a sua versão`, `na sua versão`, `antes dessa regra`, `desde então`, `adotou`) find nothing.
* Fails: a sentence outside chapter 11 that keeps "the kit's changelog"; a note pointing to a changelog entry or a before-and-after count of a kit change; a note definition left with no reference (`[^short-lines]`, `[^adr-0018]` go with their sentences).

**Contract.**

Sections touched (en lines at the start; pt the same sections, chapter 13 offset by 2):
10 §What the team gains (144 to 149, manuals' reason). 11 §What an update reports (87, 88, 93), §What the team gains (141, 143, 146). 13 §What the team gains (127 to 134), `[^short-lines]` removed. 14 §What the team gains (148 to 150). 15 §What the team gains (183 to 186). 16 §The problem (15, 16), §At the moment the work changes (47), §What the team gains (126). 17 §When the findings became one delivery (69). 18 the Case A passage (55 to 63), key point 77, `[^adr-0018]` removed. 19 §The manager's session (117). 21 §What is and is not a conflict there (65), §Worktrees in the kit (197), §What the team gains (281, 282). 22 §A mark for waiting (66), key point 88.

docs/04 §Writing the book, after **Evidence**, a new bullet: **The kit as it is.** The book describes focus-kit as it is today: what each rule is, how it works, what the team gains. It cites no changelog entry, names no version as a date ("since its version", "no longer", "before that rule") and shows no measure taken before and after a kit change; a rule's reason is the error it prevents, said in the present. Chapter 11's update report keeps its versions, which are the command's output, and teaches the changelog as a file of the kit (first: `kit-as-it-is`, from `m13-review`).

docs/06: this line `[>]`, `[*]`, `[x]`; `plain-numbers` gets `· after kit-as-it-is`. docs/03: no new term.

Case A sentences rewritten, for the author's approval (docs/00 OD-3): 16 lines 15 and 16; 18 lines 55 to 63 and key point 77; 22 line 66 and key point 88.

**Out of scope.**

* Chapter 9's birth story: it sets the kit against OpenSpec, not against an earlier kit.
* Chapter 21 line 277's parallel-build measure and every Ninjobs or Case A number in a gain: not a kit change; `plain-numbers` decides them.
* docs/03's waiting mark history ("the kit took it in 2026.10.05") and ADR-0018: process documents, not the book.
* Naming which kit version the book portrays: chapter 11's report already shows it.
* A prose rule for this: `check_prose.py` has no per-chapter exemption and chapter 11 must keep its versions.

**Done when.**

* [x] Both editions changed in every section of Contract; the checks of Behaviour hold in `book/en` and `book/pt`.
* [x] docs/04 holds the rule; `plain-numbers` carries `· after kit-as-it-is`.
* [x] Each chapter touched still opens with its value, keeps its gain section, no filler and nothing useful cut.
* [x] The rewritten Case A sentences listed under What happened and approved by the author.
* [x] `make verify` green, disclosure scan included.
* [x] `make book` run; both PDF paths given to the author.
* [x] Page in `work/done/`, line `[x]`, staged, commit message in a `commit` block.

## What happened

**Tree before editing (docs/05 §6).** `M docs/06-Queue.md` (this line `[>]` and `plain-numbers`' `· after kit-as-it-is`, both from this delivery's /propose) and `?? work/kit-as-it-is.md`; nothing staged, nothing unrelated.

**Built.** Every section of Contract, in both editions. Each rule's reason is now the error it prevents, in the present, with no entry, version or "a user": chapters 10 (manuals), 13 (order, code only inside `/apply`, one sentence per line), 14, 15, 16 (which lines run together), 19 (no status command) and 21 (what is not a conflict, one worktree shape). Chapter 11 says what a version with no migration is without naming one, links items 5 and 6 of its report to "such an item" of the changelog, and its gain keeps the list of what to change and the host's form, with no count of versions and no sizes. `[^short-lines]` and `[^adr-0018]` left with their sentences. docs/04 §Writing the book holds **The kit as it is**.

**Divergences.**
* Chapter 18's heading "From one project to the kit" (pt "De um projeto para o kit") was the claim the passage lost; it became "The error that earned a mark" (pt "O erro que rendeu uma marca"). No link pointed to its anchor. Approved by the author with the Case A sentences.
* Three "now" outside the listed lines carried the same before and after and went with their neighbours: chapter 10 "Now the slot holds" (line 149), chapter 16 "now answer it" (line 128, merged into 126), chapter 18 "the ones the kit's `SETUP.md` now lists" (line 68, en and pt).
* Chapter 15 line 10, "which documents no longer say the truth", matches `no longer` and stays: it speaks of a project's documents, not of the kit.

**Proof.**
* `grep -nE "20[0-9]{2}\.[0-9]{2}\.[0-9]{2}" book/*/[0-9]*.md`: only chapter 11 lines 49 and 52, in §What an update reports, both editions (the slug `kit-2026-10-13` in chapter 13 has no dots and does not match).
* `grep -niE changelog book/*/[0-9]*.md`: only chapter 11 lines 90 and 92 (pt; en 90), in §What an update reports, and key point 149.
* The phrase checks of Behaviour, in chapters 10 to 22 of both editions: nothing but chapter 15 line 10 above.
* `make verify` green, disclosure scan included; `make book` built `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.

**Case A sentences, approved by the author (docs/00 OD-3), both editions.**
* 16 §The problem: "focus-kit answers both with six marks, each set at the moment the work changes. Its file `SETUP.md` holds the process document, docs/05, and that document's §4 is the queue."
* 18, heading "The error that earned a mark"; "The question is asked in each project, and the governor decides there, with an error that project met."; "the board showed what Case A's three marks hid (chapter 16)"; "five idle-looking lines were the error that earned Case A its mark, and the mark named it."; "The error is not Case A's alone: any team that reads its queue as a board meets it the day a line waits, or a delivery is being defined. The kit's six marks answer the same error for every such team, with `[?]` among them (chapter 16)."; key point: "The governor decides in each project: Case A's idle-looking lines earned Case A its `[?]`, and the kit's six marks answer the same error for every team that reads its queue as a board."
* 22 §A mark for waiting: "The kit has its own `[?]`, with the two other reasons a line waits (chapter 16)."; key point: "`[?]` was Case A's mark for lines waiting on a person, and the kit has its own (chapter 16); question deliveries, which close on the answer, stay Case A's customization."

**Decisions.** Decision 6 of the page held as chosen (chapter 11 lines 90 to 92 and key point 149 teach the changelog as a file of the kit). `plain-numbers` keeps `· after kit-as-it-is` and is free now that this line is `[x]`.

```commit
docs(kit-as-it-is): teach the kit as it is, with no changelog
- chapters 10, 13 to 19, 21, 22: each rule's reason is the error it prevents
- chapter 11: no version named outside the update report, no sizes
- chapters 16, 18, 22: Case A's [?] stays Case A's; the kit has six marks
- docs/04: the kit as it is, a rule of writing the book
work/done/kit-as-it-is.md
```
