# renumber-chapters

**Objective.** After this delivery the book's chapters are numbered 1 to N with no gap in both editions, every file, H1, link, mention, contents table, parts map and PDF contents agree, and the merges and the inserted chapter leave no trace of the old numbers in anything a reader reads.

**Behaviour.**

* A reader of either edition finds the chapters numbered without a gap: the prologue, then chapter 1 "How an agent sees your project", 2 "Spec-Driven Development", 3 "Simplicity and results", 4 "FOCUS", 5 "A test for each piece", 6 "How focus-kit was born", and so on through the method, the quick guide, git, beyond code and asking for more; the final map is written on this page before the move.
* A reader who follows any "chapter N" in the text, any link, the site's navigation, the PDF's contents page or the EPUB's table of contents lands on the chapter whose H1 carries that number.
* Failure: a "chapter N" that still means the old number anywhere in `book/`, docs/00, docs/03, docs/04 or the prologue's parts map is a finding; the list of every mention before the move is on this page and each is checked after it.
* Edge: `work/done/`, docs/06 and the ADRs keep old numbers as history, as `queue-states` decided; ADR-0017 gains one amendment line naming the new map and this delivery.
* Edge: `book/assets/` files named by chapter number (`NN-<what>`) are renamed with their chapters, and each edition's link to its diagram follows.
* Edge: the PDF contents of both editions still fit on one page, with the chapter number no larger than the page number (`pdf-contents-one-page`).
* Edge: an external link to a chapter's old site URL is not preserved: the site has no redirects, and the book has not been released at these numbers since `rewrite`; the README's links, if any name a chapter file, are updated.

**Contract.**

* **Both editions:** `git mv` of every chapter file whose number changes, the H1 number with it; H1 titles otherwise unchanged. The map, old to new, written on this page by /apply before the first move, from the files present then (the merges leave 01, 05 and 07 absent; `12a-quick-guide.md` sits between 12 and 13 and takes the number 13, so 13 to 26 become 14 to 27 before the gaps close).
* **Mentions:** every `](NN-<slug>.md` link (`12a-quick-guide.md` included, and chapter 25's "the chapter after 12" becomes its number) and every "chapter N" / "capítulo N" in `book/`, docs/00 (Contents and Audience), docs/03, docs/04 and the prologue's parts map moved by one script, as `queue-states` did; docs/00's Contents, which has bare numbers, by hand. Never in `work/`, `docs/adr/` or docs/06.
* **Assets:** `book/assets/NN-*` renamed with their chapter, links in both editions updated.
* **ADR-0017:** one amendment line: the chapters were renumbered when the prologue absorbed chapter 1, chapters 4 and 5 and 6 and 7 merged, and the quick guide was inserted; the map in `work/done/renumber-chapters.md`.
* **docs/01:** unchanged (the navigation comes from the file names).
* **README and README.pt:** any chapter link updated; sections unchanged.
* **Terms:** none; docs/03's rows that name a chapter follow the script.

**Out of scope.**

* Any change of text beyond numbers and links.
* Redirects on the site: not built; a decision of its own if a release had been made at the old numbers.
* docs/06's lines and `work/done/` pages: history.

**Done when.**

* [x] Files, H1s, links and mentions renumbered in both editions; the map and the list of every mention before the move on this page, each checked after it at its new number.
* [x] docs/00, docs/03, docs/04, the parts map, assets, README links and ADR-0017 follow.
* [x] `make verify` green (strict build, parity by file name, links); `make book` builds, both PDF contents fit on one page, and both PDF paths are given to the author.
* [x] Page in `work/done/`, the line `[x]`, staged by its paths and its hunk of docs/06, the commit suggested in a `commit` block.

**Decisions taken from the documents.**

* One renumbering at the end rather than one per merge: docs/05 §1, the page is the test that the scope was understood; three cascading renumberings are three chances to miss a mention, and `queue-states` shows one scripted pass is checkable.
* The merges leave gaps until this runs: the site orders by file name and tolerates gaps (docs/01), and the PDF numbers chapters from the H1, so a draft between deliveries builds; the gap is visible only until this line closes it.
* History keeps old numbers: ADR-0017 amendment 2026-10-05.
* Script, not hand edits: the precedent's list of 97 mentions was checked one by one after the move; the same check applies.

**Decisions in the review.**

* The author chose one renumbering here: `quick-guide` enters as `12a-quick-guide.md` with the temporary number "12a." in its H1 and in docs/00's Contents, moves nothing, and this delivery gives it its number along with the merges' gaps. The map on this page starts from that file. The `· after` lines in docs/06 stay as written: `prologue-and-why`, `simplicity-and-results`, `focus-and-slices`, `quick-guide`.

**The map, old to new** (written by /apply before the first move, from the files present then; the same names in `book/pt/`; old 1, 5 and 7 were absent, removed by the merges):

| Old | Old file | New | New file | Title |
|---|---|---|---|---|
| prologue | `00-product-people-process.md` | prologue | unchanged | Product, people and process |
| 2 | `02-how-agents-see.md` | 1 | `01-how-agents-see.md` | How an agent sees your project |
| 3 | `03-spec-driven.md` | 2 | `02-spec-driven.md` | Spec-Driven Development |
| 4 | `04-simplicity-and-results.md` | 3 | `03-simplicity-and-results.md` | Simplicity and results: KISS, YAGNI, DRY and exceptions as values |
| 6 | `06-focus.md` | 4 | `04-focus.md` | FOCUS: features, not layers, and the four pieces |
| 8 | `08-testing-each-piece.md` | 5 | `05-testing-each-piece.md` | A test for each piece |
| 9 | `09-birth-of-focus-kit.md` | 6 | `06-birth-of-focus-kit.md` | How focus-kit was born |
| 10 | `10-the-documents.md` | 7 | `07-the-documents.md` | The documents: one place per fact |
| 11 | `11-install-and-hosts.md` | 8 | `08-install-and-hosts.md` | Install, and the hosts |
| 12 | `12-starting-a-project.md` | 9 | `09-starting-a-project.md` | Starting: `/brainstorm` and `/analyze` |
| 12a | `12a-quick-guide.md` | 10 | `10-quick-guide.md` | From zero to the first delivery |
| 13 | `13-queue-and-milestones.md` | 11 | `11-queue-and-milestones.md` | The queue and milestones |
| 14 | `14-propose.md` | 12 | `12-propose.md` | `/propose`: one page |
| 15 | `15-apply.md` | 13 | `13-apply.md` | `/apply`: build, verify, prove, never commit |
| 16 | `16-queue-states.md` | 14 | `14-queue-states.md` | The queue while it happens |
| 17 | `17-closing-a-milestone.md` | 15 | `15-closing-a-milestone.md` | Closing a milestone |
| 18 | `18-the-governor.md` | 16 | `16-the-governor.md` | The governor |
| 19 | `19-project-as-assistant.md` | 17 | `17-project-as-assistant.md` | The project as the team's assistant |
| 20 | `20-git-essentials.md` | 18 | `18-git-essentials.md` | Git essentials |
| 21 | `21-worktrees.md` | 19 | `19-worktrees.md` | Worktrees and parallel agents |
| 22 | `22-team-tools.md` | 20 | `20-team-tools.md` | The team's tools: pull requests, issues and boards |
| 23 | `23-beyond-software.md` | 21 | `21-beyond-software.md` | Projects that are not software |
| 24 | `24-cost-and-where.md` | 22 | `22-cost-and-where.md` | What agents cost, and where they pay |
| 25 | `25-adoption.md` | 23 | `23-adoption.md` | Adoption in teams and companies |
| 26 | `26-asking-for-more.md` | 24 | `24-asking-for-more.md` | Asking for more |

Assets: `book/assets/02-context-window.en.svg` and `.pt.svg` become `01-context-window.en.svg` and `.pt.svg`.

**Mentions before the move** (file, line, old number to new; 381 mentions of "chapter N" or "capítulo N" that change, written before the move; the 48 H1s and the 175 links `](NN-<slug>.md` and `NN-<what>.svg` moved with them by the same script; each line was checked after the move to hold its new number):

* `book/en/00-product-people-process.md`: 37 10→7; 45 2→1; 55 26→24; 61 18→16; 62 3→2; 62 9→6; 66 19→17; 95 14→12; 97 15→13; 106 19→17.
* `book/en/02-how-agents-see.md`: 69 4→3; 82 10→7; 88 14→12; 88 15→13.
* `book/en/03-spec-driven.md`: 20 14→12; 59 10→7; 67 9→6.
* `book/en/04-simplicity-and-results.md`: 14 9→6; 99 6→4; 134 6→4; 220 8→5; 250 18→16.
* `book/en/06-focus.md`: 51 4→3; 54 8→5; 82 4→3; 138 4→3; 188 8→5; 222 4→3.
* `book/en/08-testing-each-piece.md`: 11 4→3; 15 6→4; 56 4→3; 60 14→12; 87 6→4; 142 15→13.
* `book/en/09-birth-of-focus-kit.md`: 8 3→2; 9 10→7; 24 6→4; 25 4→3; 43 18→16; 58 14→12; 62 10→7; 64 13→11; 66 15→13; 68 18→16; 74 12→9.
* `book/en/10-the-documents.md`: 15 14→12; 17 12→9; 36 15→13; 41 13→11; 51 6→4; 51 4→3; 54 6→4; 54 8→5; 61 20 and 21→18 and 19; 84 15→13; 89 2→1; 90 11→8.
* `book/en/11-install-and-hosts.md`: 29 15→13; 34 12→9; 93 13→11; 93 16→14; 93 17→15; 94 14→12; 94 15→13; 94 18→16; 104 21→19; 115 14→12.
* `book/en/12-starting-a-project.md`: 24 10→7; 56 14→12; 77 13→11; 127 6→4; 139 19→17.
* `book/en/12a-quick-guide.md`: 8 11→8; 16 11→8; 33 20→18; 33 21→19; 39 11→8; 42 12→9; 43 12→9; 45 12→9; 48 14→12; 49 14→12; 51 14→12; 54 15→13; 57 15→13; 60 15→13; 68 11→8; 71 12→9; 74 12→9; 77 12→9; 80 14→12; 90 13→11; 92 17→15; 96 25→23.
* `book/en/13-queue-and-milestones.md`: 21 14→12; 36 15→13; 39 16→14; 43 20→18; 81 16→14; 87 16→14; 91 17→15; 100 15→13; 110 14→12; 114 16→14; 127 19→17; 127 22→20.
* `book/en/14-propose.md`: 30 16→14; 139 13→11; 139 10→7; 140 18→16; 146 23→21.
* `book/en/15-apply.md`: 16 14→12; 23 13→11; 30 4→3; 42 16→14; 45 21→19; 62 10→7; 64 16→14; 74 14→12; 76 8→5; 77 4→3; 87 21→19; 107 11→8; 135 26→24; 147 20→18; 160 21→19.
* `book/en/16-queue-states.md`: 51 20→18; 69 21→19; 118 22→20.
* `book/en/17-closing-a-milestone.md`: 22 15→13; 22 22→20.
* `book/en/18-the-governor.md`: 37 4→3; 57 16→14; 62 16→14.
* `book/en/19-project-as-assistant.md`: 18 16→14; 21 20→18; 128 11→8; 132 14→12; 134 13→11.
* `book/en/20-git-essentials.md`: 72 22→20; 150 21→19; 167 21→19; 195 22→20; 196 21→19.
* `book/en/21-worktrees.md`: 16 20→18; 23 16→14; 141 10→7; 248 20→18.
* `book/en/22-team-tools.md`: 10 20→18; 24 16→14; 59 16→14; 66 16→14; 88 16→14.
* `book/en/23-beyond-software.md`: 14 14→12; 59 22→20.
* `book/en/24-cost-and-where.md`: 14 2→1; 59 2→1; 63 13→11; 90 4→3.
* `book/en/25-adoption.md`: 21 24→22; 24 18→16; 30 11→8; 62 14→12; 63 21→19; 65 15→13; 66 17→15; 67 19→17; 74 11→8; 75 12→9; 76 13→11; 78 17→15; 82 24→22; 102 23→21.
* `book/en/26-asking-for-more.md`: 9 19→17; 105 2→1; 105 24→22; 135 24→22.
* `book/pt/00-product-people-process.md`: 37 10→7; 45 2→1; 55 26→24; 61 18→16; 62 3→2; 62 9→6; 66 19→17; 95 14→12; 97 15→13; 106 19→17.
* `book/pt/02-how-agents-see.md`: 69 4→3; 82 10→7; 88 14→12; 88 15→13.
* `book/pt/03-spec-driven.md`: 20 14→12; 59 10→7; 67 9→6.
* `book/pt/04-simplicity-and-results.md`: 14 9→6; 100 6→4; 135 6→4; 221 8→5; 251 18→16.
* `book/pt/06-focus.md`: 52 4→3; 55 8→5; 83 4→3; 139 4→3; 189 8→5; 223 4→3.
* `book/pt/08-testing-each-piece.md`: 11 4→3; 15 6→4; 56 4→3; 60 14→12; 87 6→4; 142 15→13.
* `book/pt/09-birth-of-focus-kit.md`: 8 3→2; 9 10→7; 24 6→4; 25 4→3; 43 18→16; 58 14→12; 62 10→7; 64 13→11; 66 15→13; 68 18→16; 74 12→9.
* `book/pt/10-the-documents.md`: 15 14→12; 17 12→9; 36 15→13; 41 13→11; 51 6→4; 51 4→3; 54 6→4; 54 8→5; 61 20 e 21→18 e 19; 84 15→13; 89 2→1; 90 11→8.
* `book/pt/11-install-and-hosts.md`: 29 15→13; 34 12→9; 96 13→11; 96 16→14; 96 17→15; 97 14→12; 97 15→13; 97 18→16; 107 21→19; 118 14→12.
* `book/pt/12-starting-a-project.md`: 24 10→7; 56 14→12; 77 13→11; 127 6→4; 139 19→17.
* `book/pt/12a-quick-guide.md`: 8 11→8; 16 11→8; 33 20→18; 33 21→19; 39 11→8; 42 12→9; 43 12→9; 45 12→9; 48 14→12; 49 14→12; 51 14→12; 54 15→13; 57 15→13; 60 15→13; 68 11→8; 71 12→9; 74 12→9; 77 12→9; 80 14→12; 90 13→11; 92 17→15; 96 25→23.
* `book/pt/13-queue-and-milestones.md`: 21 16→14; 23 14→12; 38 15→13; 41 16→14; 45 20→18; 83 16→14; 89 16→14; 93 17→15; 102 15→13; 112 14→12; 116 16→14; 129 19→17; 129 22→20.
* `book/pt/14-propose.md`: 30 16→14; 146 13→11; 146 10→7; 147 18→16; 153 23→21.
* `book/pt/15-apply.md`: 16 14→12; 23 13→11; 30 4→3; 42 16→14; 45 21→19; 62 10→7; 64 16→14; 74 14→12; 76 8→5; 77 4→3; 87 21→19; 107 11→8; 135 26→24; 147 20→18; 160 21→19.
* `book/pt/16-queue-states.md`: 52 20→18; 70 21→19; 119 22→20.
* `book/pt/17-closing-a-milestone.md`: 22 15→13; 22 22→20.
* `book/pt/18-the-governor.md`: 37 4→3; 57 16→14; 62 16→14.
* `book/pt/19-project-as-assistant.md`: 18 16→14; 21 20→18; 128 11→8; 132 14→12; 134 13→11.
* `book/pt/20-git-essentials.md`: 72 22→20; 150 21→19; 167 21→19; 195 22→20; 196 21→19.
* `book/pt/21-worktrees.md`: 16 20→18; 23 16→14; 141 10→7; 248 20→18.
* `book/pt/22-team-tools.md`: 10 20→18; 24 16→14; 59 16→14; 66 16→14; 88 16→14.
* `book/pt/23-beyond-software.md`: 14 14→12; 59 22→20.
* `book/pt/24-cost-and-where.md`: 14 2→1; 59 2→1; 63 13→11; 90 4→3.
* `book/pt/25-adoption.md`: 21 24→22; 24 18→16; 30 11→8; 62 14→12; 63 21→19; 65 15→13; 66 17→15; 67 19→17; 74 11→8; 75 12→9; 76 13→11; 78 17→15; 82 24→22; 102 23→21.
* `book/pt/26-asking-for-more.md`: 9 19→17; 105 2→1; 105 24→22; 135 24→22.
* `docs/03-Domain.md`: 11 3→2; 11 14→12; 43 26→24; 44 26→24; 48 26→24; 127 26→24.
* `docs/04-Conventions.md`: 26 24→22; 27 4→3; 30 11→8; 37 2→1; 38 10→7; 38 10→7; 39 6→4; 40 8→5; 40 4 to 8→3 to 5; 40 9→6; 40 25→23; 41 19→17; 43 3→2; 43 4→3; 46 4→3; 46 2→1; 120 6→4; 139 3→2; 166 3→2.
* `docs/00-Product.md`: 15 2 and 3→1 and 2.

**What happened.**

* Both editions: 24 chapter files per edition moved with `git mv` by the map above, the prologue unchanged; the two diagrams `02-context-window.<edition>.svg` became `01-context-window.<edition>.svg` and each edition's link followed.
* One script rewrote every mention, link and H1 in `book/`, docs/00's Audience, docs/03 and docs/04, never in `work/`, `docs/adr/` or docs/06; it skipped the Toyota note of chapter 14 (old 16), whose "Chapter 1" is the cited work's own, and docs/00's Open decisions. Every entry it recorded before the move (381 changing mentions, 175 links, 48 H1s) was checked after it at its new path and line: 607 checked, 0 failures.
* By hand: docs/00's Contents, bare numbers 1 to 24, with the quick guide's "(a temporary number, until `renumber-chapters`)" removed; chapter 23's "The chapter after 12" / "O capítulo depois do 12" became "Chapter 10" / "O capítulo 10"; docs/04's example H1 became `# 4. FOCUS: ...`; docs/04's three mentions with no new number (below).
* The prologue's parts map names no chapter number (only parts), so nothing moved there; its one mention, chapter 26 in Part V, became 24 with the script.
* The README and README.pt link no chapter file; unchanged.
* ADR-0017 gained the amendment `2026-10-16 (renumber-chapters)`.
* Proof: `make verify` green (strict build, parity by file name, em dash, prose, links, disclosure); `make book` built both editions, each contents page on one page, chapters 1 to 24 in order after the prologue (read from the rendered PDFs), with no warning but the known `user-select` one.

**Decisions in /apply** (taken alone, as the batch rules ask):

* docs/04's "first: the orchestrator of chapter 7, now chapter 6 after `focus-and-slices`" keeps the old 7 as history and reads "now chapter 4 after `focus-and-slices` and `renumber-chapters`", so the sentence stays true.
* docs/04's em dash paragraph named "chapter 7's `/brainstorm` run", a number from before `rewrite` that no map covers; it now names chapter 9, the chapter that teaches `/brainstorm`, so the line holds no stale number beside the renumbered "chapter 2".
* docs/04's "it is never called chapter 0" is the rule about the prologue, not a mention; unchanged.
* docs/00's OD-4 bullet is unchanged: it quotes what the kit says today, chapter 7 and `.../07-four-pieces/`, and the kit still says it. The repointing the author must make in the focus-kit repository (README, README.pt and `SETUP.md` §3): FOCUS is now chapter 4, `book/<edition>/04-focus.md`, on the site `.../04-focus/` (and `.../pt/04-focus/`).
* `scripts/build_book.py` keeps the letter after the two digits (`12a-`), and docs/01 and docs/04 keep the convention: it is a general rule for the next chapter placed between two numbers, docs/01 is unchanged by this page's Contract, and no chapter uses a letter now.
* `book/assets/11-skeleton-390x844.png` is not renamed: no file in the repository references it (`git grep`), and its number is that of the `/apply` chapter before `rewrite`; renaming it to `08-` would credit it to the install chapter. Its removal is the author's call, for a line of its own.

**Old to new, for the pages written with the old numbers** (`method-said-once`, `small-delivery-example`, `ch20-21-git-cut`, `ch22-26-team-cut`, `one-gain-section`, `m15-review`): read the map above; in short, 2→1, 3→2, 4→3, 6→4, 8→5, 9→6, 10→7, 11→8, 12→9, 12a→10, and 13 to 26 become 11 to 24 (N→N−2). So "chapters 9 to 19" are now 6 to 17 (the quick guide, 10, among them), "chapter 13" is 11, "chapters 20 and 21" are 18 and 19, "chapters 22 to 26" are 20 to 24, and "every chapter 1 to 26" is every chapter 1 to 24.

```commit
docs(renumber-chapters): chapters numbered 1 to 24 with no gap

- both editions: 24 chapter files moved, H1s, links and mentions by one script
- the quick guide is chapter 10; the context window diagrams are 01-
- docs/00 Contents and Audience, docs/03 and docs/04 follow
- ADR-0017 amendment names the map, old to new

work/done/renumber-chapters.md
```
