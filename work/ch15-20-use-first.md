# ch15-20-use-first

**Objective.** After chapters 15 and 20 the reader meets the same sequence as in chapter 13: use the delivery, review the staged change, then commit.

**Behaviour.**

* Reading chapter 15's problem, the reader finds that each delivery was used and its staged change reviewed before its commit, not only reviewed.
* Reading chapter 15's "No second review" and its key point, the reader finds that a finding line passes through its own page, its proof, and the person's use, review and commit, not the commit alone.
* Reading chapter 20's problem, the reader finds that one person on trunk uses the delivery, reviews the staged change and commits it.
* The pull request's reviewer in chapter 20 still reads the page and then the diff: use first is the building person's step before the change leaves, not a new step for the reviewer.
* No number or measurement of either chapter changes.

**Contract.** Files: `book/en/15-closing-a-milestone.md`, `book/pt/15-closing-a-milestone.md`, `book/en/20-team-tools.md`, `book/pt/20-team-tools.md`. Sentences, located by content:

* Chapter 15, "The problem": en "Each page of a milestone was read before `/apply` built it, and each staged change was reviewed before its commit." / pt "Cada página de um marco foi lida antes de o `/apply` construí-la, e cada mudança em stage foi revisada antes do seu commit." The second clause names the use before the review.
* Chapter 15, "No second review": en "Each one passes through its own page, its proof and the person's commit, which is the review." / pt "Cada uma passa pela sua própria página, pela sua prova e pelo commit da pessoa, que é a revisão." It names the person's use and review before the commit.
* Chapter 15, Key points: en "each passes through its own page, its proof and the person's commit." / pt "cada uma passa pela sua própria página, pela sua prova e pelo commit da pessoa." Same change.
* Chapter 20, "The problem": en "One person working on trunk reviews the staged change and commits it." / pt "Uma pessoa trabalhando no trunk revisa a mudança em stage e faz o commit." It names the use first.

Source: docs/05 §2 ("a person uses it, reviews and commits"), the installed apply skill's next steps, chapter 13's "Review the staged change", which stays the main passage (`apply-use-first`). Terms of docs/03: delivery, stage, commit, finding; no new term, no private case.

**States.** Inapplicable: prose, no screen.

**Visual reference.** Inapplicable: existing chapter layout.

**Out of scope.** Chapter 15's code-reading sentence ("by the delivery review before `/apply` ends and in the staged change before its commit"): it says where code is read, not the person's sequence. Chapter 20's pull request steps and reviewer paragraph: the reviewer reads, the builder already used it before pushing. Chapters 10, 13, 18, 19, 22, 23: done by `apply-use-first`.

**Decisions from the documents.** The two sentences above stay as they are, for the reasons in Out of scope; the change is limited to the person's own sequence, which is what docs/05 §2 orders.

**Done when.**

* [ ] Both editions of both chapters written, same hunks; each Behaviour line checked against them.
* [ ] Each chapter opens with its value and keeps its evidenced team gain; no filler and nothing useful cut; every number keeps its source; terms follow docs/03; no em dash.
* [ ] No Case A or Case B passage changed or added, so the author's OD-3 approval is inapplicable.
* [ ] `make verify` green after the last edit; `make book` builds both editions and the page gives `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf` for the author's review.
* [ ] Delivery review by a read-only Opus agent per docs/05 §5, its candidates answered on this page; page archived and commit message suggested.
