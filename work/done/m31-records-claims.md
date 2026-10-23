# m31-records-claims

**Objective.** The author can read the records of `ch22-cache-service`, `m30-records-claims` and `m31-review`, and `ch22-cache-service`'s queue line, and find each claim held by what happened: `make book` with its commit and both PDF paths, the HEAD and `book/` it ran on said to be unrecorded; the Delivery review tick and paragraph saying what the agent read and that its report on the advisor is not recorded; every line number as it was; docs/03's header restated in its own words; the wrapped commit bullet named; the define commits that were not made named where the review planned them; and the queue line without docs/03's FOCUS term `service`. Findings C3 to C10 but C8' of `work/done/m31-review.md`.

**Behaviour.**

* Reading `work/done/ch22-cache-service.md`, the author finds its Proof (:72) naming `make book`'s two PDF paths and the commit it came before, `bc6fa75`, whose parent `9c65001` was committed 72 seconds earlier in the same tree, the build's HEAD and `git status --short book/` not recorded (C3).
* In the same page, the author finds the review item (:55) naming the agent, what it read and against what, and that whether it kept the session's advisor is not recorded; the review paragraph (:78) no longer saying the agent "keeps the session's advisor" but that it is not recorded; and Divergences (:74) naming both changes and that the page has no define commit (C4).
* In the same page, the author finds chapter 22's Claude Code sentence cited at :39, where it was at the base, in Behaviour (:14) and the Contract (:25) (C5); "Decided by this proposal" (:63) saying the line said "the service" and restating docs/03's header as it reads, the Portuguese term fixed, the Portuguese edition using it and no synonym (C10, C9); and the queue-line quote (:5) kept as it was read, followed by a sentence saying `m31-records-claims` reworded the line (C9).
* Reading `work/done/m30-records-claims.md`, the author finds Out of scope (:26) citing m30-review's two finding bullets at :181-182, not the blank :183 (C6); and Divergences (:63) saying the `commit` block, as `9c65001` carries it, wraps its second bullet onto two lines, against docs/05 §6's one-line bullets (C7).
* Reading `work/done/m31-review.md`, the author finds Base (:34) saying the range holds M30's fix round with no define commit for its lines or for this page, none having been made; Areas (:43) placing this page beside the range, read from the working tree; and Divergences (:192) naming End (:36) and Readers (:48) as what foresaw a define commit, no longer Behaviour, which did not, and the fix lines' pages first entering git with `9c65001` and `bc6fa75` (C8).
* Reading docs/06, the author finds `ch22-cache-service`'s line (:697) saying "the stored context is kept where the model runs and written again after a pause", no longer "the service keeps", with the rest of the line and its `[x]` as they were (C9).
* Edge: every other line of the three records reads as before: the Done when items stay ticked, `m31-review`'s End commit (:106), Inventory (:113) and candidate table, the `commit` blocks unchanged and last.
* Edge, the shared tree: `ch22-cache-route-host` (defined beside this line) edits chapter 22, docs/03's `cache lifetime` row and its own line of docs/06 in the same tree; this line's replacements are found by their quoted text, so its edits to docs/06 move no replacement, and its uncommitted chapter 22 shows in `git status --short book/` when this delivery runs `make book`, recorded as such.
* Fails: a replacement whose quoted text is not found exactly once; any other line of these files changed, or a line added or removed; a `commit` block changed; a Done when item of a record unticked; an em dash; a chapter, docs/03 or docs/05 touched; any line of docs/06 changed but :697's words and this line's own mark.

**Contract.** Exact replacements in three record pages and docs/06, found by the quoted text, not by line number (line numbers as the files are now: `ch22-cache-service` and docs/06 :697 unchanged since `bc6fa75`, `m30-records-claims` since `9c65001`, `m31-review` since `99d04a5`; none of the three records has an uncommitted edit, and docs/06's only uncommitted edits are the two marks at :708-709). Each quoted text was counted once in its file when this page was written. Each replacement stays on its line; the rest of each file is untouched. The forms are `m29-records-claims`': replacement 19 for an unrecorded HEAD, 24 for a review item, 23 for a review paragraph, 22 for the Divergences sentence; "`m31-records-claims` gave ..." names this line wherever it changes a record's words.

`work/done/ch22-cache-service.md`

1. (C9, :5) "This page answers it alone." becomes "This page answers it alone. `m31-records-claims` later gave the line, in place of "the service keeps the stored context and writes it again", this page's words, "the stored context is kept where the model runs and written again", `service` being docs/03's FOCUS term (Decided by this proposal); the quote above is the line as this page read it."
2. (C5, :14) "chooses the lifetime (:38)" becomes "chooses the lifetime (:39)".
3. (C5, :25) "* Same section, :38 (" becomes "* Same section, :39 (".
4. (C4, :55) "* [x] Delivery review as docs/05 §5 says." becomes "* [x] Delivery review by one read-only agent on Opus over `git diff HEAD` of the two chapter files and docs/03 and this line's hunk of docs/06, with both chapter files whole and the live source, against this page and docs/04 (Delivery review); whether it kept the session's advisor, as docs/05 §5 asks, is not recorded."
5. (C10, C9, :63) "The line says "the service"; docs/03 fixes `service` / `serviço` as the FOCUS piece (:63) and its header says the Portuguese term is used with no other meaning, so" becomes "The line said "the service"; docs/03 fixes `service` / `serviço` as the FOCUS piece (:63) and its header fixes the Portuguese term, the Portuguese edition using it and no synonym (:4), so".
6. (C3, :72) "`make verify` green after the last edit; `make book` builds both editions." becomes "`make verify` green after the last edit; `make book` builds both editions, `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`, before this delivery's commit `bc6fa75`, whose parent `9c65001` (`m30-records-claims`) was committed 72 seconds earlier, the two lanes sharing one tree; the build's HEAD and `git status --short book/` are not recorded."
7. (C4, :74) "so that note is cited 6 times per edition, the pricing note 4." becomes "so that note is cited 6 times per edition, the pricing note 4. The Done when's review item ticked the review "as docs/05 §5 says", and the review paragraph said the agent "keeps the session's advisor", the slot's words, not its report's, which this page does not record (Delivery review); the page has no define commit, its first commit being `bc6fa75`; `m31-records-claims` gave the item and the paragraph what is recorded."
8. (C4, :78) "A read-only agent on Opus, which keeps the session's advisor, read" becomes "A read-only agent on Opus read".
9. (C4, :78) "and checked the live source: no candidates." becomes "and checked the live source: no candidates. Whether it kept the session's advisor, as docs/05 §5 asks, is not recorded."

`work/done/m30-records-claims.md`

10. (C6, :26) "(:179, :183)." becomes "(:179, :181-182)."
11. (C7, :63) "its reply says it consulted none (Delivery review)." becomes "its reply says it consulted none (Delivery review). The `commit` block below, as `9c65001` carries it, wraps its second bullet onto two lines, against docs/05 §6's one-line bullets; `m31-records-claims` left it as committed."

`work/done/m31-review.md`

12. (C8, :34) "with their define commits, which get no second review (docs/05 §8), and this page's define commit;" becomes "which get no second review (docs/05 §8); no define commit was made for those lines or for this page, so none is in it (End commit);".
13. (C8, :43) "* **The documents:** `docs/` paths, `docs/06-Queue.md` and this page among them, and the records under `work/done/` of M30's fix round." becomes "* **The documents:** `docs/` paths, `docs/06-Queue.md` among them, and the records under `work/done/` of M30's fix round; this page, uncommitted, was read from the working tree beside the range (End commit)."
14. (C8, :192) "* Behaviour and End foresee this page's define commit before or after the base; neither happened (End commit, C8)." becomes "* End (:36) foresaw this page's define commit before or after the base, and Readers' second case (:48) a range holding it; neither happened, and no define commit was made for M30's fix lines either, whose pages first entered git with their own commits, `9c65001` and `bc6fa75` (End commit, C8); `m31-records-claims` gave Base (:34) and Areas (:43) what happened."

`docs/06-Queue.md`

15. (C9, :697) "say that the service keeps the stored context and writes it again after a pause" becomes "say that the stored context is kept where the model runs and written again after a pause".

Terms: record, Delivery review, Done when, define commit, as docs/03 and docs/05 have them; `service` as docs/03 :63 has it; no row added. No chapter, no case, no number, no code example.

**States.** Inapplicable: record pages and a queue line, no screen.

**Visual reference.** Inapplicable: no screen, no chapter.

**Out of scope.**

* C1 and C2: `ch22-cache-route-host`'s, chapter 22 and docs/03's row.
* C8', `[>]` uncommitted before /apply, and C11, docs/04 and the source note: weak, dropped on the author's word (`work/done/m31-review.md` :164).
* `m31-review`'s :36 and :48: a plan with two outcomes and a case not taken; Divergences name them, so their words stay as defined.
* The commits `9c65001`, `bc6fa75` and `99d04a5`: history, no rewrite; the records' `commit` blocks stay as the commits carry them.
* `work/done/m30-review.md` :191-195, which quotes `ch22-cache-service`'s line with "the service keeps": the line names three records, and that page quotes the line as m30-review wrote it.
* What `ch22-cache-service`'s review agent reported of the advisor, and the HEAD its `make book` ran on: no record or commit holds them, so the records say they are not recorded rather than reconstruct them.
* Chapter 22, docs/03, docs/05: `ch22-cache-route-host` owns chapter 22 and the row.

**Decisions from the documents.**

* The findings and their cites: `work/done/m31-review.md` :146-154 (C3 to C10), :162 (the line's candidates) and :175-182 (the line).
* Each cite checked against git: chapter 22 at `a961be3`, :38 blank and :39 "Claude Code chooses the lifetime per request, in two groups"; `work/done/m30-review.md` at `a961be3`, :181-182 the two finding bullets, :183 blank; docs/03 :4 "The Portuguese term is fixed: the Portuguese edition uses it and no synonym."; docs/05 §6 (:350) "body up to five one-line bullets", `9c65001`'s body wrapping its second bullet.
* No define commit: `git log --diff-filter=A` finds `work/ch22-cache-service.md`, `work/m30-records-claims.md` and `work/m31-review.md` never added, each page first committed under `work/done/` by `bc6fa75`, `9c65001` and `99d04a5`; `m31-review`'s Behaviour holds no define commit, so its Divergences' "Behaviour" is wrong.
* The PDF paths: docs/01 :70, `make book` writes `output/one-page-at-a-time.*` and `output/uma-pagina-de-cada-vez.*`.
* The forms: `work/done/m29-records-claims.md` replacements 19, 22, 23 and 24, after `m28-records-claims`; `m30-records-claims` for the page's shape.
* `make book` in Done when names HEAD and `git status --short book/`, as `m29-records-claims` and `m30-records-claims` did, because `ch22-cache-route-host` may have chapter 22 uncommitted in the same tree.

**Decisions taken alone.** The agent chose each of these; the author may correct them in review.

* C3: the build's HEAD and `book/` are said to be not recorded, though git narrows them (HEAD `a961be3` or `9c65001`, neither touching `book/`), because no record holds what the tree was at the build.
* C4: the review is said to be over the diff "against this page and docs/04", the paragraph listing both among what it read; "launched by this /apply" is not added, the paragraph not saying it.
* C7: the `commit` block keeps the wrap `9c65001` carries, Divergences naming it, as `m30-records-claims` kept `a4f2cb9`'s message; the line's "a commit body of one-line bullets" could be read as rewrapping the block, which would make it differ from the commit.
* C8: Base (:34) and Areas (:43), which state what the range holds, get what happened; End (:36) and Readers (:48), a plan and an untaken case, keep their words, Divergences naming them.
* C9: the queue line takes the record's own words; the record's quote of the line stays as it was read, a sentence after it naming the reword.
* The queue line keeps its wording.

**Neighbouring lines.** `ch22-cache-route-host` (`[>]`, chapter 22, docs/03's `cache lifetime` row and its own line of docs/06) beside this line under M31, another session's work in the same tree, touches no file of this line but docs/06, on another line.

**The token of this line.** `(PA)`: the definition takes nothing from `ch22-cache-route-host`'s page, and the build touches none of its files but docs/06, on separate lines; `after` names `m31-review`, `[x]`.

**Done when.**

* [x] Each quoted text counted once in its file before any edit; the fifteen replacements made word for word.
* [x] `git diff` of the three records shows only those replacements, none adding or removing a line: `ch22-cache-service` :5, :14, :25, :55, :63, :72, :74, :78; `m30-records-claims` :26, :63; `m31-review` :34, :43, :192; and of docs/06, this line's hunk holds :697's words and this line's mark (with :25's second cite, Divergences).
* [x] A search of `ch22-cache-service`'s record finds no review item reading "as docs/05 §5 says." and no paragraph saying the agent "keeps the session's advisor"; of docs/06 :697, no "service" (but the slug and :74's quote, Divergences).
* [x] Each record's last fenced block is `commit`, unchanged, and nothing follows it; no em dash; no Done when item of a record unticked.
* [x] `make verify` green after the last edit, its result in this page's Proof.
* [x] `make book` exit 0, the Proof naming HEAD, `git status --short book/` and both PDF paths, and its order beside the last verify.
* [x] Delivery review by one read-only Opus agent this lane launches, told to open docs/04 as a file, to list what it read and to say whether it consulted an advisor, over `git diff HEAD` of the three records and this page, with this line's hunk of docs/06, against this page and docs/04 (docs/05 §5); the tick and the paragraph record its reading and its answer on the advisor as given, and Divergences say so if it ran without the advisor docs/05 §5 asks. It read this page, docs/04 whole, docs/05 by lines, the three records' diff and lines, docs/03 :4 and :63, docs/06 :697 and :709 and the commits by `git show` and `git log`, and says it did not consult an advisor (Delivery review).

**Built.** The fifteen replacements of the Contract, each old text counted once in its file before any edit and replaced word for word by the Edit tool, and, after the review, :25's second ":38" of `ch22-cache-service`'s record made ":39" (Divergences); nothing else in the three records changed. docs/06: :697's words and this line's mark.

**Divergences.**

* The Contract's replacement 3 changed the first ":38" of `ch22-cache-service`'s :25 and left its second, ":38's Claude Code detail", the same sentence; the review found it against Behaviour's "cited at :39 ... in the Contract (:25)", and /apply made it ":39" on the same line.
* Done when's search finds "service" on docs/06 :697 in the slug `ch22-cache-service` alone, the word as docs/03's term gone; and "keeps the session's advisor" in `ch22-cache-service`'s record only in replacement 7's Divergences, quoting what the paragraph said, no paragraph saying it of the agent.
* The Delivery review ran without the session's advisor, which docs/05 §5 asks it to keep: its reply says it did not consult one. It was launched as a foreground Agent call with its model set to Opus, and the host ran it in the background, its report reaching this lane as its completion notice.

**Decisions taken by /apply.** The agent chose each of these.

* The review's weak candidate on replacement 1, that "the stored context is kept where the model runs and written again" joins the record's :23 and :24 rather than standing whole in it, is left as the Contract wrote it: both halves are the page's words, and the sentence cites where they are decided.
* `make book` ran once, after the first verify and before the review, as `m30-records-claims` did; the edits after it touch no file of `book/`.

**Delivery review.** One read-only Opus agent (an Explore agent with model opus), launched by this lane, told to open docs/04 as a file, to list what it read and to say whether it consulted an advisor, over `git diff HEAD` of the three records, with this line's own hunk of docs/06 written to a file, and this page, against this page and docs/04. It ran after the fifteen replacements, `make verify` and `make book`, before the :25 fix and these records. Its reply says it read this page, the two diff files and docs/04 whole; docs/05's headings, :345-355, :266 and :304; `ch22-cache-service`'s record at :1-6, :20-30, :44-58, :62-64 and :70-89; `m31-review`'s at :1-50, :100-116, :146-164 and :180-217 and every "define commit"; `m30-records-claims`' `commit` block; docs/03 :4 and :63 at HEAD and in the tree; docs/06 :697 and :709; `m29-records-claims` by search; and, by git, the commits' dates and parents, `git log --all --diff-filter=A` of the pages, chapter 22 and `m30-review` at `a961be3`, `9c65001`'s message; that it rebuilt the four files from HEAD and the Contract by script, identical to the tree but the marks; and that it did not consult an advisor tool. Its candidates: :25's second ":38" (fixed, Divergences); weak, replacement 1's "this page's words" (Decisions taken by /apply) and the two literal searches of Done when (Divergences).

**Proof.**

* Each of the fifteen old texts counted 1 in its file, on the line the Contract names, before any edit (a script over the four files).
* `git diff --numstat`: `ch22-cache-service` 8 and 8, hunks :5, :14, :25, :55, :63, :72, :74, :78; `m30-records-claims` 2 and 2, :26, :63; `m31-review` 3 and 3, :34, :43, :192; no line added or removed. This line's hunk of docs/06: :697 and :709.
* Search: no "as docs/05 §5 says." in `ch22-cache-service`'s record; no Done when item of the three records unticked; no em dash; each record's last fenced block is its `commit`, outside the diff, and nothing follows it.
* `make verify` exit 0 after the fifteen replacements; `make book` exit 0 right after it, on HEAD `99d04a5`, with `git status --short book/` printing ` M book/en/22-cost-and-where.md` and ` M book/pt/22-cost-and-where.md`, `ch22-cache-route-host`'s uncommitted chapter 22 in the same tree, before and after the build: `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`, with their EPUBs.
* `make verify` exit 0 again after the :25 fix, these records, this page's move to `work/done/` and the line's `[x]`, the last edit.

```commit
docs(m31-records-claims): make three records hold what happened

- ch22-cache-service: make book, review item and paragraph, line cites
- m30-records-claims: m30-review's bullets cited, its wrapped bullet named
- m31-review: no define commits in Base, Areas and Divergences
- docs/06: ch22-cache-service's line without docs/03's term service

work/done/m31-records-claims.md
```
