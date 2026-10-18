# docs04-width-rule

**Objective.** Whoever reads docs/04 finds the block width check among the tests `make verify` runs, and reads the same set of unmeasured info strings that `scripts/check_width.py` skips. Found by `m16-review` (work/done/m16-review.md, build-1 seen: "docs/04:165, the Tests list leaves out the width check that `Makefile:20`, docs/01:66 and docs/05:165 name"; build-2 latent: "docs/04:45 says every block but `ts` is measured; `scripts/check_width.py:20` also skips `typescript`, which no block uses").

**Decided without the author.** The batch had no one to answer; each choice is the recommended one.

1. docs/04 follows the script, and the script does not change. The rule is about a language, not a spelling: docs/04 **Width of a block** says "TypeScript may wrap", docs/01's `check_width.py` row says "every fenced block but TypeScript", and the script's own docstring names both `ts` and `typescript`. Removing `typescript` from the script would make a future TypeScript block fail a rule that lets TypeScript wrap. So `UNMEASURED` and its lower-cased comparison stay, and `check_width.py` is left to `width-comment-fence` alone. Source: docs/04 **Width of a block**; docs/01:31; scripts/check_width.py:5 and :20, :39.
2. The rule says what the script compares: the first word of the info string, in any case. The script reads `opening.group(2).split()[0].lower()`, so `TS` is skipped and `tsx` is measured; docs/04 says exactly that, so the two cannot drift on a spelling again. Source: scripts/check_width.py:38-39.
3. The Tests list names the check in `make verify`'s order, between prose rules and links, and points at **Width of a block** instead of restating it, as the list does for no other check that has its own bullet. Source: Makefile:20; docs/01:66 (the `make verify` row: "prose, then width, then links"); docs/05 §5 Verify ("the block width check").
4. No docs/03 term, no new queue line, no split: two sentences of one document. Source: docs/03; docs/05 §1.

**Behaviour.**

* After the delivery, docs/04 §Tests lists the checks as: site build (strict), edition parity, em dash, prose rules, block width, links, disclosure scan, the order `make verify` runs them, and says where the width rule is written.
* docs/04 **Width of a block** says every fenced block is measured but one whose info string's first word is `ts` or `typescript`, whatever its case.
* Agreement check, run by /apply on scratch text through `check_width.check` (no file in the tree changes for it), each result as docs/04 now says:
  * a 90-column row in a `typescript` block: nothing;
  * a 90-column row in a `TS` block: nothing;
  * a 75-column row in a `tsx` block: one finding, `<path>:<n>: width: 75 columns; a code block keeps to 74 (docs/04)`;
  * a 75-column row in a `text` block: the same finding.
* Edge: `scripts/check_width.py`, docs/01, docs/05 and both editions do not change.
* Fails: a docs/04 that names `ts` alone, or a Tests list whose order differs from `make verify`'s.

**Contract.** docs/04, two edits, one sentence per line kept.

§Tests, the second line becomes:

```
The checks are the tests: site build (strict), edition parity, em dash, prose rules, block width (**Width of a block**), links, disclosure scan.
```

**Width of a block**, its second line becomes:

```
  `make verify` holds it (rule `width`): every fenced block is measured but one whose info string's first word is `ts` or `typescript`, whatever its case, a column being a character and a tab running to the next multiple of 8, as in the PDF.
```

No new term; no new queue line.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Out of scope.**

* `scripts/check_width.py`: it already does what docs/04 will say (decision 1); its comment rule is `width-comment-fence`.
* docs/01's rows on the width check and markdown.py: `width-comment-fence`, `fence-commonmark` and `docs01-helpers`.
* A fuller description of the width check in §Tests: **Width of a block** owns it.

**Order with the other slugs of this batch.** This page is first. It is the only one of the seven that edits docs/04; `width-comment-fence`, which comes next, edits `check_width.py` and docs/01 and leaves docs/04 as this page writes it.

**Done when.**

* [x] docs/04 holds the Contract's two lines, byte for byte, and nothing else in docs/04 changes.
* [x] Each agreement check of Behaviour run and its output recorded on this page; no scratch file left in the tree.
* [x] `make verify` green; no em dash on this page or in docs/04.
* [x] No screenshot: no rendered change (docs/05 §5 Proof of a screen; `code-width` the precedent).
* [x] Page in `work/done/`, line `[x]`, staged by its paths and its own hunk of docs/06 (docs/05 §6), other sessions' changes left unstaged; commit message in a `commit` block.

**Proof.** The agreement checks ran on scratch text passed straight to `check_width.check` from `scripts/`, with no file written:

* a 90-column row in a `typescript` block: nothing;
* a 90-column row in a `TS` block: nothing;
* a 75-column row in a `tsx` block: `scratch.md:2: width: 75 columns; a code block keeps to 74 (docs/04)`;
* a 75-column row in a `text` block: `scratch.md:2: width: 75 columns; a code block keeps to 74 (docs/04)`.

`grep -xF` finds each Contract line in docs/04 once, at lines 45 and 165, and `git diff --stat docs/04-Conventions.md` shows two lines changed. `make verify` is green (build, parity, em dash, prose, width, links, disclosure), before and after the review's fix.

**Divergences.** The Contract's width line said "in any case", which the review found can read as "anyway"; it now says "whatever its case", in the Contract, in Behaviour and in docs/04, so docs/04 still holds the Contract byte for byte.

**Omissions.** None.

**Decisions taken in /apply.** The wording fix above, taken alone as the recommended resolution, since the batch had no one to ask.

**Review.** Delivery review by a read-only Opus agent on docs/04's diff, this delivery's line of docs/06 and this page, against docs/04, `scripts/check_width.py` and the Makefile: both Contract lines match byte for byte, the text matches what the script compares (an empty info string measured, `~~~` fences covered), and the Tests list follows `make verify`'s order. One finding, the "in any case" wording, fixed as above. It also noted, out of scope, that the script's docstring gives no first-word or case detail and that a fence inside an HTML comment is still measured; both belong to `width-comment-fence`, which edits `check_width.py`, so no new line.

```commit
docs(docs04-width-rule): name the width check among docs/04's tests

- docs/04 Tests lists block width in make verify's order
- Width of a block: ts or typescript, first word, any case, unmeasured

work/done/docs04-width-rule.md
```
