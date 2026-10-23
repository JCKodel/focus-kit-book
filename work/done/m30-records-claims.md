# m30-records-claims

**Objective.** The author can read the record of `ch08-other-items-claude-md` and find its Delivery review held by what happened: the Done when's review item saying what its agent read, narrower than docs/05 §5 because docs/04 was not opened, and that it consulted no advisor; and Divergences saying the review ran without docs/04 and without the session's advisor. Finding C13 of `work/done/m30-review.md`.

**Behaviour.**

* Reading `work/done/ch08-other-items-claude-md.md`, the author finds its review item (:118) no longer saying "as docs/05 §5 says", but naming the agent, what it read, that docs/04 was not opened, and that it consulted no advisor, which docs/05 §5 asks it to keep, as the review paragraph (:110) records.
* In the same page, the author finds Divergences (:97) saying "None from the Contract", the Portuguese-split sentence as it was, and a new sentence saying the review ran without the session's advisor and without docs/04, while the item, as defined at `f443055`, ticked it "as docs/05 §5 says", and that `m30-records-claims` gave the item the paragraph's words.
* Edge: the review paragraph (:110), the Proof, the other Done when items, "Decisions taken by /apply" and the `commit` block read as before; every Done when item stays ticked.
* Fails: a replacement whose quoted text is not found exactly once; any other line of the record changed, or a line added or removed; the `commit` block changed; a Done when item unticked; an em dash; a chapter, docs/03, docs/05 or docs/06 touched beyond this line's own hunk.

**Contract.** Exact replacements in `work/done/ch08-other-items-claude-md.md`, found by the quoted text, not by line number (line numbers as the file is now, unchanged since its commit `a4f2cb9`, no uncommitted edit). Each quoted text was counted once in the file when this page was written. Each replacement stays on its line; the rest of the file is untouched. The forms are `m29-records-claims`': replacements 17 and 21 for "None from the Contract", 27 and 33 for the Divergences sentence, 29 and 35 for the review item, "consulted no advisor" because the paragraph says the agent said it called none.

1. (C13, :97) "**Divergences.** None. The Portuguese split" becomes "**Divergences.** None from the Contract. The Portuguese split".
2. (C13, :97) "the Contract's numbers are as the files were before it." becomes "the Contract's numbers are as the files were before it. The Delivery review ran without the session's advisor, which docs/05 §5 asks it to keep: its agent said it did not call any advisor tool; and it did not open docs/04, against which docs/05 §5 has it read, using the conventions the brief and the page state, while its Done when item, as defined at `f443055`, ticked it "as docs/05 §5 says" (Delivery review); `m30-records-claims` gave the item the paragraph's words."
3. (C13, :118) "* [x] Delivery review as docs/05 §5 says, its record saying what the agent read and what its reply says of the advisor." becomes "* [x] Delivery review by one read-only Opus agent, launched by this /apply, over `git diff HEAD` of both chapter 8 files and this page (Delivery review): narrower than docs/05 §5, which has it read against docs/04, here not opened; it read this page, the record's lines 85 to 90, SETUP.md at `cc16f4e` and chapter 8 by line, and consulted no advisor, which docs/05 §5 asks it to keep."

Terms: record, Delivery review, Done when, as docs/03 and docs/05 have them; no row added. No chapter, no case, no number, no code example.

**States.** Inapplicable: a record page, no screen.

**Visual reference.** Inapplicable: no screen, no chapter.

**Out of scope.**

* C14, the verify item at :119 against the Proof at :107, and every other candidate of `work/done/m30-review.md`: the author confirmed only C1 and C13 (:179, :181-182).
* The review paragraph (:110): it says what happened, and the finding cites it as evidence, not as a line to change; its "did not run `make verify`" is a read-only reader's, which docs/05 §5 does not ask to run it.
* "Decisions taken alone" (:89), which already says the agent chose, and "Decisions taken by /apply" (:99), which says nothing was open: no choice to attribute.
* The `commit` block (:121 to :131): the message `a4f2cb9` carries.
* Chapter 8, docs/03, docs/05, docs/06 beyond this line, `work/done/m30-review.md`: `ch22-cache-service` owns chapter 22 and docs/03.

**Decisions from the documents.**

* The finding and its cites: `work/done/m30-review.md` :151 (C13, :118 against :110 and :97), :182 and the line at :196 to :200.
* The Delivery review slot: docs/05 §5 :265 to :272, a read-only agent on Opus that keeps the session's advisor, against the page and docs/04.
* The forms: `work/done/m29-records-claims.md` replacements 17, 21, 27, 29, 33 and 35, after `m28-records-claims`.
* The item was ticked as defined, not reworded in /apply: `git show f443055:work/ch08-other-items-claude-md.md` :103 holds the same words as `a4f2cb9`'s :118, so Divergences say "as defined at `f443055`", with no "/apply gave the item" sentence.
* What the agent read and said of the advisor: the review paragraph (:110) is the only source; the commits do not carry the agent's report.
* `make book` in Done when: docs/05 §5 Environments, a delivery leaves both building; its Proof names HEAD and `git status --short book/`, as `m29-records-claims` did, because `ch22-cache-service` may have chapter edits uncommitted in the same tree.

**Decisions taken alone.** The agent chose each of these; the author may correct them in review.

* The paragraph at :110 stays as it is, the queue line naming only the tick and Divergences.
* The new item lists what the agent read in short ("chapter 8 by line"), the paragraph keeping the line numbers.
* The queue line keeps its wording.

**Neighbouring lines.** `ch22-cache-service` (`[~]`, chapter 22 and docs/03) beside this line under M30, and `m31-review` (M31), each another session's work in the same tree, touch no file of this line.

**The token of this line.** `(PA)`: the definition takes nothing from `ch22-cache-service`'s page, and the build touches none of its files; `after` names `m30-review`, `[x]`.

**Done when.**

* [x] Each quoted text counted once in the record before any edit; the three replacements made word for word.
* [x] `git diff` of the record shows only those replacements: two lines changed, :97 and :118, none added or removed.
* [x] A search of the record finds no ticked review item reading "as docs/05 §5 says", and Divergences no longer reading "None." alone.
* [x] The record's last fenced block is `commit`, unchanged, and nothing follows it; no em dash; no Done when item unticked.
* [x] `make verify` green after the last edit, its result in this page's Proof.
* [x] `make book` exit 0, the Proof naming HEAD, `git status --short book/` and both PDF paths, and its order beside the last verify.
* [x] Delivery review by one read-only Opus agent this lane launches, told to open docs/04 as a file, to list what it read and to say whether it consulted an advisor, over `git diff HEAD` of the record and this page, against this page and docs/04; the tick and the paragraph record its reading and its answer on the advisor as given, and Divergences say so if it ran without the advisor docs/05 §5 asks.

**Built.** The three replacements of the Contract in `work/done/ch08-other-items-claude-md.md`, each old text counted once in the file before any edit and replaced word for word by the Edit tool; nothing else in the record changed.

**Divergences.** None from the Contract. The Delivery review ran without the session's advisor, which docs/05 §5 asks it to keep: its reply says it consulted none (Delivery review). The `commit` block below, as `9c65001` carries it, wraps its second bullet onto two lines, against docs/05 §6's one-line bullets; `m31-records-claims` left it as committed.

**Decisions taken by /apply.** None: the Contract left nothing open. The review's one observation, that the item states "consulted no advisor" as fact where the record's :110 gives it as the agent's word, is the form Contract chose and the Divergences sentence keeps the attributed words; no change and no queue line comes of it.

**Delivery review.** One read-only Opus agent (an Explore agent with model opus), launched by this lane, told to open docs/04 as a file, to list what it read and to say whether it consulted an advisor, over `git diff HEAD` of the record and this page, with this line's own hunk of docs/06, against this page and docs/04. It ran after the three replacements, `make verify` and `make book`, before these records. Its reply says it read this page and docs/04 whole, docs/05 :255-279, the record's diff and its lines 84 to 132, `work/done/m30-review.md` :145-200, `f443055`'s :100-105, `a4f2cb9`'s :118 and the record's log, `work/done/m29-records-claims.md` at replacements 17, 21, 27, 29, 33 and 35, and docs/06 :698; that it rebuilt the record from HEAD and the Contract by script, byte-identical to the working tree; and that it consulted no advisor. Its verdict: "No findings." Its one observation is in Decisions taken by /apply.

**Proof.**

* Each of the three old texts counted 1 in the record before any edit (`grep -cF` and `grep -oF`).
* `git diff --numstat` of the record: 2 insertions and 2 deletions, hunks `@@ -97 +97 @@` and `@@ -118 +118 @@` only; the record still has 131 lines.
* Search of the record: no line reading "as docs/05 §5 says, its record", no Divergences reading "None." alone, no `[ ]`, no em dash; its last fenced block opens at :121 as `commit`, untouched by the diff, and nothing follows it.
* `make verify` exit 0 after the three replacements, every check passed, the external link included; and again after these records, this page's move to `work/done/` and the queue's `[x]`, the last edit.
* `make book` exit 0 after the first of those verifies, on HEAD `a961be3` with `git status --short book/` empty: `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.

```commit
docs(m30-records-claims): make ch08's record hold its review as it ran

- the review item names its agent, what it read, no docs/04, no advisor
- Divergences: none from the Contract, the review without docs/04
  or the session's advisor

work/done/m30-records-claims.md
```
