# m33-fixes

Built before the author read it: the author asked for the whole queue to be run, each page decided alone and built in the same session (docs/05 §4, a command that says to decide alone and to build as well). Every choice the documents leave open is marked "decided by the agent, the author corrects it in the review".

**Objective.** After chapters 7, 8, 11, 13 and 14 the reader meets no contradiction with what the book teaches of focus-kit 2026.11.12 in the six places m33-review found: which findings become queue lines, a page with a screen and its Visual reference, the claim with `taken` and `resume`, a branch's mark on the mirror once pushed, `· after` read per command, and the update report's own wording.

**Behaviour.** What the reader can do or explain afterwards, one item per medium finding of `work/done/m33-review.md`:

* M1. From chapter 11 alone, say that only a grave finding becomes a queue line, that the review's medium findings the person picks share one line under it and the rest stay listed on its page, and that a flaw `/apply` finds outside what its delivery built becomes a line only when grave, a note on its page otherwise; never read there that every finding becomes a line.
* M2. Read chapter 11's `due-date-format` page, which changes the loan screen, and find a Visual reference naming the design, as chapter 9's Design slot asks of a screen; the sentence after it counts the sections that do not apply correctly.
* M3. From chapter 13 alone, say what `claim.sh` does when origin already has the slug's branch and this clone does not: `claim: taken`, nothing created, opened only with `resume` on the person's word; never read that it reuses another clone's branch.
* M4. From chapter 14 alone, say that the mirror shows a mark at once on trunk and, with a branch or a worktree per delivery, at the first refresh after the mark is pushed to its branch, as chapter 20 says.
* M5. From chapter 7, say that `· after` names a line another needs first and is read for each command, never that it holds a line until another is done.
* M6. Read chapter 8's report excerpt and its explanation and find only words the run record holds: a part that matches is listed as already in line with the template, a project choice as a choice to keep; no `None`.
* Failure: asked "does chapter 11 say every review finding gets a line?", the answer is no, in both editions.
* In the Portuguese edition, the same, with docs/03's Portuguese terms (achado, grave, médio, nota, linha de correções).

**Contract.** Ten chapter files, line numbers en / pt at HEAD `32d084f`; pt follows en sentence for sentence. The text is the agent's within these changes.

* **M1, ch11** (`book/{en,pt}/11-queue-and-milestones.md`)
  * :74 / :77: lines added while a milestone runs: a grave flaw a delivery finds outside what it built, the review's findings that become lines (below), a problem found trying the product.
  * :97 / :100: the review's findings stay in its milestone under the review line; each grave one, which breaks a clause of the paragraph for a person on its usual path, loses or exposes data, or leaves verify red, becomes a `[ ]` line; the medium ones the person picks share one line, `<milestone>-fixes`; the others stay listed on the review's page; no second review.
  * :176 / :181: during `/apply`, a flaw found outside what the delivery built becomes a `[ ]` line when grave and a note on the delivery's page for the milestone's review otherwise; only a fix the delivery needs first goes above it and makes it wait.
  * :195 / :200, key point: the review, whose grave findings and the medium ones the person picks become lines under it.
  * :80 / :83 and :182 / :187 read true beside these and stay.
* **M2, ch11**
  * :147 / :151: `**Visual reference.** The loan screen in the design file, at 390 and 1280 pixels wide.` (pt: the same in Portuguese), wrapped to the block as the page is.
  * :155 / :160: two sections, Contract and States, say only that they do not apply or take the defaults; the Visual reference names the screen the change touches.
  * :156 / :161: `/apply` also compares the screen it built with the design at both widths; the rest as it is.
* **M3, ch13** (`book/{en,pt}/13-apply.md`) :29: with a branch per delivery the script switches to the slug's branch, with a worktree per delivery it opens the slug's worktree, the `path` it prints; when origin has no branch for the slug it creates one from origin's main branch and pushes it at once; it reopens the branch or worktree this clone already has, pushing its branch when origin lacks it; a branch on origin this clone does not have is another clone's line: `claim: taken`, nothing created, unless the command ends with `resume`, which `/propose` adds on the person's word. Pointers to chapters 18 and 19 kept.
* **M4, ch14** (`book/{en,pt}/14-queue-states.md`) :65 / :66: the mirror shows the mark at once on trunk; with a branch or a worktree per delivery it pushes the queue read the same way, shows a mark at the first refresh after the mark is pushed to the delivery's branch, and each refresh carries every other delivery's mark pushed so far, never one branch's copy of the file.
* **M5, ch07** (`book/{en,pt}/07-the-documents.md`) :62 / :63: `· after`, which names a line another needs first and is read for each command, the definition waiting for that line's page and the build for its code. No pointer forward (docs/04, chapters 0 to 7).
* **M6, ch08** (`book/{en,pt}/08-install-and-hosts.md`)
  * Excerpt :69 to :70 / :70 to :71 and :79 to :80 / :80 to :81: the item order kept; `None` replaced by the record's own phrases: the section numbers "already in line with the template", §6 among the "project choices to keep".
  * :90 / :91, :92 / :93: the three outcomes said in the record's words: a part that matches is listed as already in line with the template; a project choice is listed among the choices to keep, the item naming it and asking for no change; :89 / :90 "ends in one of three outcomes" adjusted to match.

Terms of docs/03: finding, grave, note, fixes line, milestone review, claim, mirror, integrated. No new term. Sources: docs/05 §§4 and 8 at 2026.11.12 and docs/03's finding, note and fixes line rows (M1); chapter 9 :49 and chapter 12 :87, the lending library's design file (M2); `propose/scripts/claim.sh` at 2026.11.12 and chapter 19 :244 (M3); chapter 20 :62 to :63 (M4); docs/05 §4 (M5); the run record `work/done/ch08-update-2026-10-25-run/update.md`, its headings "Already in line with the template" and "Project choices to keep" (M6). No number added. No source note added. Cases: none.

**States.** Inapplicable: chapters, no screen.

**Visual reference.** Inapplicable: no screen, and no new kind of content (prose).

**Out of scope.**

* Chapter 15's "each finding becomes a line", the `· from <slug>` suffix, where a grave line goes and how the review grades: `ch15-review-grades` and `ch14-queue-findings` in M38.
* The small findings 7 to 32 of m33-review: not picked by the author.
* Chapter 12 :30's "reused when the definition resumes": the checker marked that half weak.
* Reordering chapter 8's excerpt to the record's grouping: it would rewrite :96's claim on what comes first, which the record does not source.

**Done when.**

* [x] M1 to M6 read as the Contract says in both editions; no passage of chapters 7, 8, 11, 13 or 14 left with the six contradictions.
* [x] Both editions written; each chapter opens with its value; no filler and nothing useful cut; no number added; no em dash; no run narration.
* [x] `make verify` green after the last edit; the disclosure scan green.
* [x] `make book` builds both editions, both PDF paths recorded.
* [x] Delivery review by one read-only Opus agent, as docs/05 §5 says; only this delivery's paths and its docs/06 line staged; the page in `work/done/` and its commit message suggested.

**Decisions.**

* Decided by the agent, the author corrects it in the review: chapter 11 says the grades in one sentence, with the definition of grave from docs/05 §4, since a reader cannot follow "only a grave one" without it; how the review grades, `· from` and placement wait for M38's lines, and no new pointer to chapter 15, which still says every finding becomes a line until `ch15-review-grades`.
* Decided by the agent, the author corrects it in the review: chapter 11's page takes the lending library's design file, the one chapter 12's `lend-book` page names, at the same two widths, rather than a design delivery, since the library already has a design file and a design delivery would add a line to the chapter's example.
* Decided by the agent, the author corrects it in the review: chapter 8's excerpt keeps its item order and swaps `None` for the record's phrases in place, the smallest change the record sources.
* From the documents: the finding rules (docs/05 §§4 and 8, docs/03), the Design slot (chapter 9, docs/05 §3), `claim.sh`'s behaviour (the script, chapter 19), the mirror (chapter 20), `after` per command (docs/05 §4), the report's wording (the run record); the six items and that they are one page (`work/done/m33-review.md`, the author's pick; docs/05 §8).

## Outcome

* Built as the Contract says, M1 to M6, in both editions, from HEAD `32d084f`. Diverged: chapter 11's review sentence is four short sentences, not one, and names the fixes line by docs/03's term and says what a medium finding is (docs/05 §8), so "medium" is not left undefined; it says a small finding stays listed unless the person picks one. Chapter 7's `· after` is its own sentence after the list, not an aside inside it. Chapter 13's claim is three sentences, one per case. Chapter 8's "ends in one of three outcomes" reads "has one of three outcomes".
* Delivery review: one read-only agent on Opus (model set at launch, Explore type), which keeps the session's advisor, read the page, the diff of the ten chapter files, this line's docs/06 hunk, docs/05 §§4 and 8, docs/03's finding, note and fixes line rows, `work/done/m33-review.md`, `claim.sh`, the run record `update.md`, and chapters 9, 12, 19 and 20 at the passages the page names; it did not open docs/04 or `AGENTS.md`, whose em dash and width rules it checked from the brief, and `make verify` holds them. Eight candidates, no contradiction with the sources:
  * 1, ch11 :98: one sentence with three facts, "medium" undefined, no "fixes line"; fixed: split, medium defined, the term used, both editions.
  * 2, ch11 :98: "the others stay listed" against §8's small one picked; fixed: "unless you pick one", both editions.
  * 3, ch11 key point: read as one line per picked medium finding; fixed: "a line each", the medium ones "share one", both editions.
  * 4, ch11 :179: three clauses and an ambiguous "it"; fixed: split, "above the delivery's line", both editions.
  * 5, ch07 :62: the `· after` aside inside the list; fixed: its own sentence, from the waiting line's side, both editions.
  * 6, ch13 :30: three cases in one sentence; fixed: one sentence each, both editions.
  * 7, ch14 :65: "every other delivery's" with no delivery to be other than; fixed: "each delivery's refresh", as chapter 20 says, both editions.
  * 8, ch08 :90: the record also has a "No change needed" heading, for documents the excerpt does not show; no change, the excerpt shows docs/05 only.
* Proof: `make verify` green after the last edit, 11 seconds, under the five-minute ceiling; `make book` at `32d084f` with this delivery's working tree built `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`. No slow tests (docs/05 §5).
* The sweep of both editions for the six phrases found them only where this page changes them, in chapter 15, held by `ch15-review-grades`, and in chapter 21, below.
* No number added, no case used, no new line.

## For the review

* book/en/21-beyond-software.md:103 (pt the same): the key point "Give every finding a line, or it gets lost." reads, beside chapter 11 and docs/05 §4, as if every kit finding became a queue line; the chapter's findings are those of an analysis outside software, so a person may read it either way.

```commit
docs(m33-fixes): fix M33's six medium findings in five chapters

- Chapter 11: which findings become lines; the page's Visual reference
- Chapter 13: the claim with taken and resume
- Chapter 14: the mirror shows a branch's mark once pushed
- Chapters 7 and 8: after read per command; the report's own words
- Both editions

work/done/m33-fixes.md
```
