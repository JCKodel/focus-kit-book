# kit-record-step4

**Objective.** The author can read on `work/done/kit-2026-10-19-2.md` a "Migration report (step 4)" that holds only what SETUP's step 4 checks, the project's other dispositions in a list of their own, agreeing with the page's Decisions on the Environments pointer, and a Behaviour that credits the kit's changelog only with what it says.

**Behaviour.**

* Reading `work/done/kit-2026-10-19-2.md`, "Migration report (step 4)", the author finds only the items SETUP.md's step 4 checks at `44132c4` (docs/05's section numbers, §§2 to 4, §5's slots and their shape, §§6 to 8, docs/04, docs/06, AGENTS.md): section numbers and §§2 to 4 none; the Manuals slot applied; every other slot none, Milestone review and Git as recorded project choices, the Git slot only reflowed; §§6 to 8, docs/04 and docs/06's header none; AGENTS.md's manuals line applied (m23-review R1).
* Below it, under "The project's other dispositions", the author finds what the project did that step 4 does not check: §4's provenance sentence untouched; the Environments local item's pointer to the new manual, which the step 4 report did not name, as the page's Decisions taken alone say (:46); the new manual in `docs/manuals/`; docs/01's row holding; docs/03's `manual` row; ADR-0018's amendment. The record no longer lists the Environments pointer under step 4 while :46 says the report does not name it (m23-review K3).
* Reading the Behaviour item that opens "The run's step 4 report", the author finds the changelog for 2026.10.19.2 credited only with the AGENTS.md echo, as its text says ("and the AGENTS.md template points to it"), and the manual in `docs/manuals/` named as the project's disposition of the Manuals migration (m23-review R2).
* Reading "Step 5", the author finds "the pending migrations" pointing to the step 4 report above, not to both lists.
* Chapter 8's excerpt, "What an update reports" in both editions, stays as it is and agrees item for item with the new step 4 list: Manuals, AGENTS.md, Milestone review as a project choice, and "the other items" covering §§2 to 4, the other slots of §5, §§6 to 8, docs/04 and docs/06 (m23-review marked C1 and K4 weak for this reason).
* Edges: no Done when item is unticked; no other section of the page changes, its Contract, commit block and the lines `m23-records-crossrefs` edits included; nothing claims the run printed what the record does not already say; `make verify` is green with the other sessions' uncommitted files in the tree, named as theirs if they fail it.

**Contract.** Exact replacements in `work/done/kit-2026-10-19-2.md`, line numbers at `ac44bea`, the file unchanged since `3cc90a8`; /apply matches the quoted text if they moved. The rest of the page is untouched.

1. Behaviour, line 9, the clause "with its echoes in AGENTS.md's manuals line and in docs/manuals/, as the kit's changelog for 2026.10.19.2 says." becomes:

   > with its echo in AGENTS.md's manuals line, as the kit's changelog for 2026.10.19.2 says ("and the AGENTS.md template points to it"); the new manual in docs/manuals/ is the project's disposition of that migration, which neither the changelog nor step 4 names.

   The line's next sentence, on Step 5, stays.

2. What happened, lines 76 to 87, the heading and its ten items, become:

   > **Migration report (step 4), by document and section.**
   >
   > * docs/05 section numbers, §§2 to 4: match since kit-2026-10-19-1; none.
   > * docs/05 §5, the Manuals slot: it did not name the manual of running it. Applied: the template's 2026.10.19.2 opening whole, and a new first item, `build-the-book-from-a-clone.md`; the three present items unchanged after it.
   > * docs/05 §5, every other slot: match since kit-2026-10-19-1; none. Milestone review (the kit's readers, `work/done/review-slot-models.md`) and Git (trunk; never commits or merges on its own, AGENTS.md): recorded project choices; none. The template's Git slot only reflowed; none.
   > * docs/05 §§6 to 8, docs/04, docs/06's header: match; none.
   > * AGENTS.md: the manuals line becomes the template's "running it, and what a person does by hand", the project's parenthesis kept. Applied.
   >
   > **The project's other dispositions**, which step 4 does not check.
   >
   > * docs/05 §4's provenance sentence: untouched, as the page decided.
   > * docs/05 §5, the Environments slot: the local item now ends with the pointer to the new manual, as the shape of a slot says; the step 4 report did not name it (Decisions taken alone).
   > * docs/manuals/: `build-the-book-from-a-clone.md`, new, with the six headings of `set-up-the-disclosure-list.md`, the manual the Manuals slot now names. Applied.
   > * docs/01: the `docs/manuals/` row still holds; none.
   > * docs/03: `manual` names running the book from a fresh clone. Applied, in place.
   > * ADR-0018: amendment `kit-2026-10-19-2`. Applied; history untouched.

3. Step 5, line 89, "The pending migrations are those above, now applied;" becomes:

   > The pending migrations are those of the step 4 report above, now applied;

   the rest of the sentence stays.

Neighbour: `m23-records-crossrefs` also edits this file, at lines 3 and 37, and is applied after this line in queue order; replacement 2 adds four lines after line 76, so lines 3 and 37 do not move. No docs/03 row, no chapter, no ADR, no docs/05 or docs/06 text.

**States.** Inapplicable: a record, no screen.

**Visual reference.** Inapplicable.

**Out of scope.**

* Chapter 8: its excerpt already agrees with the step 4 list (m23-review, C1 and K4 weak); its `Next:` is `ch08-next-free-line`'s.
* Lines 3 and 37 of the page: `m23-records-crossrefs` owns them.
* The page's Contract, line 15's "these dispositions of the step 4 report": the plan before the run, where a disposition is what the report led to, the Environments item included; the finding saw the record (Decisions taken alone).
* The commit block and the commit `3cc90a8`: they exist and do not change.
* Any rerun of the installation, the refusal case or the fresh clone: the record says what they did, and this line moves items between lists without adding output.
* A note on the record that it was edited: this page is that history, as `m22-batch-proof` left its three pages.

**Decisions from the documents.**

* What step 4 checks is SETUP.md's step 4 at `44132c4` (`git -C ~/Projects/focus-kit show 44132c4:SETUP.md`, lines 39 to 95): docs/05's section numbers, §§2 to 8 one by one, §5's slots and their shape, docs/04, docs/06 and AGENTS.md. docs/01, docs/03, ADR-0018 and the creation of a manual are not on that list.
* The kit's changelog for 2026.10.19.2 (`git show 44132c4:CHANGELOG.md`) names the Manuals slot, `/brainstorm`, `/analyze` and "the AGENTS.md template points to it"; it names no docs/manuals/ echo.
* The Environments pointer is the project's, as the record's own Decisions taken alone :46 say and chapter 8's excerpt, paraphrased from that record, shows by not listing it.
* Record pages in `work/done/` are corrected by exact replacements, the rest untouched, as `m22-batch-proof` did.

**Decisions taken alone** (the batch's driver asked for recommended answers; correct them in the review).

* The finding's "agreeing with its Decisions" is met by moving the Environments item out of the step 4 list, not by rewriting :46: the excerpt in chapter 8 and the run's step 4 check both support :46.
* §4's provenance sentence moves to the other dispositions: step 4 checks §4's content, and the decision not to touch that sentence is the page's.
* The second list's heading is "The project's other dispositions", the line's own words.
* Step 5's "those above" is changed as a sibling sentence that would go stale once the list splits; no other line touches it.
* The Contract's line 15 stays: it is the plan, and its "dispositions of the step 4 report" holds once a disposition is read as what the report led to.
* /apply, resumed in a fresh session after the first was stopped mid-run (docs/05 §4): the record's uncommitted hunks it found in the tree are this delivery's, checked against the Contract word for word, and kept as they were.

**Done when.**

* [x] The three replacements above made word for word, and `git diff` of `work/done/kit-2026-10-19-2.md` shows only those lines.
* [x] The new step 4 list matches chapter 8's excerpt item for item in both editions, which stay unchanged.
* [x] No Done when item of the record unticked; no em dash; no private case, so OD-3 approval is inapplicable.
* [x] `make verify` green after the last edit.
* [x] Delivery review by one read-only Opus agent this lane launched, over `git diff HEAD` of the record and this page against this page and docs/04 (Delivery review); whether it kept the session's advisor, as docs/05 §5 asks, is not recorded.
* [x] The page moved to `work/done/` and its commit message suggested; the staging and the queue's marks are the driver's in this batch.

**Divergences.** `make book` is not run: the batch's lane rules leave it to the driver, and no chapter changes. docs/06 is the driver's in this batch: it marks the line `[x]`. The staging and the commit are the driver's too: this session staged nothing.

**Proof.** `git diff HEAD -- work/done/kit-2026-10-19-2.md` shows two hunks, :9 and :75 to :96: replacement 1 in the Behaviour line, its Step 5 sentence kept; replacement 2, five items under step 4 and six under "The project's other dispositions"; replacement 3 in Step 5. Lines 3 and 37 are untouched. Chapter 8's excerpt, en :60 to :84 and pt likewise, is unchanged and names Manuals, AGENTS.md, Milestone review as a project choice and "the other items" for §§2 to 4, the other slots of §5, §§6 to 8, docs/04 and docs/06, the new step 4 list item for item. No em dash in the record or this page. `make verify` green after the last edit: build, parity, em dash, prose, width, examples, links and disclosure.

**Delivery review.** One read-only Opus agent, launched by this lane, read `git diff HEAD` of the record and this page against this page and docs/04, with SETUP.md and CHANGELOG.md at the kit's `44132c4` and chapter 8 in both editions. No findings: the three replacements word for word and nothing else, the step 4 list exactly what SETUP's step 4 checks, the changelog crediting only the AGENTS.md echo, chapter 8's excerpt agreeing item for item, and the record's :46 agreeing with the Environments item's new place. No new queue line.

```commit
docs(kit-record-step4): split the record's step 4 report from the rest

- kit-2026-10-19-2's step 4 report holds only what SETUP's step 4 checks
- the project's other dispositions, the Environments pointer included, apart
- the changelog credited only with the AGENTS.md echo; Step 5 points to step 4

work/done/kit-record-step4.md
```
