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

* [ ] Files, H1s, links and mentions renumbered in both editions; the map and the list of every mention before the move on this page, each checked after it at its new number.
* [ ] docs/00, docs/03, docs/04, the parts map, assets, README links and ADR-0017 follow.
* [ ] `make verify` green (strict build, parity by file name, links); `make book` builds, both PDF contents fit on one page, and both PDF paths are given to the author.
* [ ] Page in `work/done/`, the line `[x]`, staged by its paths and its hunk of docs/06, the commit suggested in a `commit` block.

**Decisions taken from the documents.**

* One renumbering at the end rather than one per merge: docs/05 §1, the page is the test that the scope was understood; three cascading renumberings are three chances to miss a mention, and `queue-states` shows one scripted pass is checkable.
* The merges leave gaps until this runs: the site orders by file name and tolerates gaps (docs/01), and the PDF numbers chapters from the H1, so a draft between deliveries builds; the gap is visible only until this line closes it.
* History keeps old numbers: ADR-0017 amendment 2026-10-05.
* Script, not hand edits: the precedent's list of 97 mentions was checked one by one after the move; the same check applies.

**Decisions in the review.**

* The author chose one renumbering here: `quick-guide` enters as `12a-quick-guide.md` with the temporary number "12a." in its H1 and in docs/00's Contents, moves nothing, and this delivery gives it its number along with the merges' gaps. The map on this page starts from that file. The `· after` lines in docs/06 stay as written: `prologue-and-why`, `simplicity-and-results`, `focus-and-slices`, `quick-guide`.
