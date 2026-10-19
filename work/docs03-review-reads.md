# docs03-review-reads

**Objective.** After this delivery a person or agent who looks up `milestone review` in docs/03 reads who reads the milestone's code as docs/05 §8 and chapter 15 say it: on the person's word, whoever the Milestone review slot names, the host's deep review that the person launches over the range, or the kit's readers by area, or nobody when the slot says none, and a checker either way; not "the session reads".

**Behaviour.**

* Reading docs/03's `milestone review` row, a person finds that on the person's word the code in `git diff <base>..<end>` is read, and that who reads is the Milestone review slot's choice: the host's deep review, which the person launches over the range; the kit's readers, one read-only reader per area, each listing the paths it read; or none.
* The row no longer names "the session" as the reader of the range; nothing in it says the session launches or runs the deep review.
* Whoever reads, the row keeps one checker that marks each candidate seen, latent or weak before the person sees it, as docs/05 §8 ("Either way, one checker") and chapter 15 say.
* Edge, none: the slot set to none (the kit's slot template, `or: none`, and chapter 15, "or none") is in the row: no code is read, and the hand test and the slow tests still run, as the row's first clauses already say.
* Edge, the range: the base (previous review's commit, the first commit for a first milestone, or the commit the page names and why), the end (the commit HEAD was when the reading started) and "so the range stays fixed while readers work" stay word for word.
* Every other clause of the row, its Term, Portuguese, Identifier columns, and every other row of docs/03 are unchanged.
* The `checker` row is checked and stays: "comes after the area readers or the host's deep review: an agent or the review's own session" agrees with docs/05 §8 and chapter 15. The `candidate`, `finding`, `waiting mark` (fourth case), `delivery review` and `slot` rows are checked and stay: none names who reads the range.
* Fails if: the row still says the session reads the range, has the session launch the deep review, drops the checker for either answer, leaves out none, names a host command, a model or a kit version, or tells how the review was read before.

**Contract.**

* **Files.** `docs/03-Domain.md` (the file docs/01 names for docs/03), the `milestone review` row only; and this page. No chapter, no other document; docs/06 is the driver's.
* **The row's Meaning, exact** (the other three columns unchanged):

  > The last line every milestone is planned with: its page takes the milestone's paragraph clause by clause and writes which delivery answers each and how a person tests it; it fixes nothing; it runs the slow tests the Verify slot names, when it names any, and a failing one is a finding; the person tests each clause by hand, and on the person's word the range `git diff <base>..<end>` is read, between the two commits the page names, its base, the previous review's commit, the first commit for a first milestone or, where no earlier review exists, the commit the page names and why, and the commit HEAD was when the reading started, so the range stays fixed while readers work; it is read by whoever the Milestone review slot names: the host's deep review, which the person launches over the range, or the kit's readers, one read-only reader per area, each listing the paths it read; a slot that says none reads no code; whoever reads, one checker marks each candidate seen, latent or weak before the person sees it; each candidate the person confirms is a finding like the others.

  /apply may tune punctuation to docs/04, keeping every element: the person's word, the range and its two commits, the slot's choice with its three answers in docs/05 §8's order and the person launching the deep review, the paths each reader lists, the checker whoever reads, and the person confirming.
* **Terms of docs/03.** `milestone review`, `slot`, `checker`, `candidate`, `finding`, as defined. No new row.
* **Sources.** None; no number; no private case.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no visual change.

**Out of scope.**

* Chapter 15 (`ch15-who-reads`), chapters 11 and 23 (`ch11-23-who-reads`), chapter 7 (`ch07-review-git-slots`): already teach who reads.
* docs/05 §5's Milestone review slot and §8: they already say it; this row follows them.
* The `checker` row and the other rows named in Behaviour: they already agree (checked, unchanged).
* The book's chapters: no script or Makefile target renders docs/03 into an edition, so no edition changes and no `make book`.

**Decisions from the documents.**

* Who reads is the slot's choice, the host's deep review the person launches over the range or the kit's readers by area: docs/05 §8; chapter 15, §Read the code since the base.
* The slot may say none: the kit's slot template in SETUP.md (`or: none`), chapter 15 ("or none"), `work/done/ch11-23-who-reads.md` ("when it names anyone").
* Passive "is read" in place of "the session reads", as `ch11-23-who-reads` did for chapters 11 and 23 for the same reason: docs/05 §8, where the person launches the deep review.
* The checker either way: docs/05 §8; docs/03's `checker` row.
* The book teaches the kit as it is, no before/after or version: docs/04, ADR-0017; the row says none either.

**Decisions taken alone.**

* none is written into the row ("a slot that says none reads no code"), although docs/05 §8 lists only the two answers; the slot template and chapter 15 carry it, and a glossary row that omits it would read as if a code reading were always made. Alternative the author may take: the minimal fix, the passive "is read" and "which the person launches", with no clause on none. If none stays, docs/05 §8 names two answers and docs/03 three; that is left to the author, not made here.
* "before the person sees it" is added to the checker clause, from docs/05 §8 and the `checker` row, so the row says why the checker comes first.
* The `checker` row stays as it is: "after the area readers or the host's deep review" already matches; with none there is no candidate and so no checker.

**Done when.**

* [ ] docs/03's `milestone review` row reads as Contract gives it; no other row changed.
* [ ] `grep -n "the session reads" docs/03-Domain.md` finds nothing.
* [ ] The row agrees with docs/05 §8 and chapter 15 on who reads, who launches the deep review, none, and the checker.
* [ ] No em dash; no host command, model or kit version in the row.
* [ ] Delivery review as docs/05 §5 says.
* [ ] `make verify` green.
* [ ] Only this delivery's paths and its hunks of docs/06 staged; the page moved to `work/done/` and its commit message suggested.
