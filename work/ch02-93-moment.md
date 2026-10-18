# ch02-93-moment

**Objective.** The reader can distinguish the number of Ninjobs deliveries at its public opening from the later count of its finished pages.

**Behaviour.**

* Reading chapter 2's gain alongside chapter 6, the reader understands that 91 deliveries were complete at the public opening and that the count of 93 finished pages, totaling 22,650 lines, was taken afterwards.
* Reading chapter 2 alone, the reader does not infer that 93 pages were already complete when the product opened.
* The correction does not manufacture a precise date for the later count, recompute the historical total from today's files, or imply that line counts prove a controlled improvement in software quality.

**Contract.** Edit `book/en/02-spec-driven.md` and `book/pt/02-spec-driven.md`, the final sentence of "What the team gains" and its immediate connection to the preceding sentence if needed.
Keep 93 and 22,650 together as the later sample, qualifying it as counted after the opening; chapter 6 already owns the opening's 91, so chapter 2 need not repeat that additional count.
Sources: the author's explicit correction recorded by `ch02-93-moment` in docs/06 M19; chapter 6's opening count; the existing historical pair recorded in `work/done/ch03-restated-rule.md` and `work/done/ch02-gain-less-to-read.md`.
The current prologue explains that the author counted Ninjobs' artifacts; preserve that provenance and paraphrase the observation, without adding a private artifact, source path or invented count date.
No new term or source note: docs/03 and docs/04 already govern these terms and the treatment of counted case evidence.
Choosing a relative time rather than an unsupported exact date follows docs/00's real-numbers requirement and docs/04's numbers-that-prove rule.

**States.** Inapplicable: prose, no screen.

**Visual reference.** Inapplicable: existing chapter layout.

**Out of scope.** Recounting Ninjobs, revising chapter 6's historical opening, or changing the tool comparison and its recorded experiment would change the measurement rather than clarify it.

**Done when.**

* [ ] Both editions distinguish the later 93-page sample from the opening, and still pair it with 22,650 lines (22.650 in Portuguese).
* [ ] The opening value and evidenced team gain remain, with no filler or useful information cut; all numbers retain their recorded provenance and no exact later date is invented.
* [ ] No Case A or Case B passage is used, so OD-3 approval is inapplicable; Ninjobs stays within the disclosure rules.
* [ ] `make verify` and `make book` pass, and both PDFs are given to the author to review.
