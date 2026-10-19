# m22-batch-proof

**Objective.** The author can read on the pages of `ch08-update-2026-10-19-1`, `ch12-free-lines-branches` and `ch14-20-read-branches` a Done when that ticks only what their Proof records, and find where the whole `make verify` run and the `make book` run that hold their chapters are recorded.

**Behaviour.**

* Reading `work/done/ch08-update-2026-10-19-1.md`, the author finds the `make verify` item saying what ran: every check but the link check after the last covered edit, failing only on external timeouts outside chapter 8, and the whole run green after `m22-review`'s last edit, with chapter 8 unchanged; the `make book` item points to the build `work/done/m22-review.md` records, with both PDF paths. The Proof and the Decision that deferred both to the driver point to the same record (m22-review candidate 22).
* Reading `work/done/ch12-free-lines-branches.md`, the author finds the same for chapter 12: the item, the Proof's last sentence on `make book` and the Divergence "to rerun when those sites answer" all point to the whole run and the build `work/done/m22-review.md` records.
* Reading `work/done/ch14-20-read-branches.md`, the author finds `make verify` green as its Proof already says, and the `make book` item, the Proof sentence and the Divergence pointing to the build `work/done/m22-review.md` records instead of "the driver's in this batch".
* Edges: no item is unticked and no other item, decision, review or commit block of the three pages changes; nothing claims these sessions ran what they did not; `work/done/m22-review.md`, docs/05, docs/06 and every chapter stay as they are.

**Contract.** The record the three pages point to, checked at define time:

* `work/done/m22-review.md`, Mechanical checks: the PDFs at `output/one-page-at-a-time.pdf` (17:06) and `output/uma-pagina-de-cada-vez.pdf` (17:07) contain the text of `abb988a`; its Proof: `make verify` green after that page's last edit.
* `git diff --stat abb988a 838f737 -- book/` is empty; chapter 8 last changed at `1e0159b` and chapter 12 at `fac1518`, both ancestors of `abb988a`, so that build and that verify hold all three deliveries' chapters as they left them.

Exact replacements, one line each, the rest of each page untouched:

1. `work/done/ch08-update-2026-10-19-1.md`, Done when, line 51, from `* [x] \`make verify\` green after the last covered edit; ...` to:

   > * [x] `make verify` green: after the last covered edit every check passed but the link check, which failed only on external timeouts outside chapter 8 (Proof), and the whole run passed after `m22-review`'s last edit, with this chapter unchanged; `make book` built both editions from `abb988a`'s `book/`, which holds this chapter, and both PDF paths are in `work/done/m22-review.md`.

2. Same page, Decisions taken alone in /apply, line 66, to:

   > * `make book` is not run in this session: the build `work/done/m22-review.md` records made both PDFs from `abb988a`'s `book/`, which holds this chapter, and gives their paths.

3. Same page, Proof, line 74: its last sentence, "The driver reruns `make verify` before committing.", becomes:

   > A whole run passed after `m22-review`'s last edit, with chapter 8 as this delivery left it (`work/done/m22-review.md`, Proof); the driver runs it again before the release.

4. `work/done/ch12-free-lines-branches.md`, Done when, line 65, to:

   > * [x] `make verify` green: in this session every check passed but the link check, which failed only on external timeouts outside chapter 12 (Proof), and the whole run passed after `m22-review`'s last edit, with this chapter unchanged; `make book` built both editions from `abb988a`'s `book/`, which holds this chapter, and both PDF paths are in `work/done/m22-review.md`.

5. Same page, Proof, line 73: its last sentence, "`make book` is run once by the driver for the batch.", becomes:

   > The whole run passed after `m22-review`'s last edit, with chapter 12 as this delivery left it, and `make book` built both PDFs from `abb988a`'s `book/`: `work/done/m22-review.md` records both, with the PDF paths.

6. Same page, Divergences, line 76, to:

   > **Divergences.** The link check's external timeouts above, outside this delivery; the whole run passed after `m22-review`'s last edit (Proof).

7. `work/done/ch14-20-read-branches.md`, Done when, line 76, to:

   > * [x] `make verify` green; `make book` built both editions from `abb988a`, this delivery's commit, and both PDF paths are in `work/done/m22-review.md`.

8. Same page, Proof, line 85: its last sentence, "`make book` is run once by the driver for the batch, so this lane reports no PDF paths.", becomes:

   > `make book` built both PDFs from `abb988a`, this delivery's commit; `work/done/m22-review.md` records them with their paths, so this lane reports none.

9. Same page, Divergences, line 92, to:

   > * Done when's `make book` item is met by the build `work/done/m22-review.md` records, not by this session.

No docs/03 row, no chapter, no ADR, no docs/05 or docs/06 text.

**States.** Inapplicable: records, no screen.

**Visual reference.** Inapplicable.

**Out of scope.**

* The other M22 pages whose Done when say the driver may run `make book`: candidate 22 calls that part weak, and m22-review's Findings table names only these three pages for this line.
* A docs/05 sentence on where a batch driver records its runs: the finding's other branch; the author chose the pages (m22-review, Findings).
* A new `make verify` or `make book` run recorded on the three pages: the build and the whole run already recorded hold their chapters; the release's rerun is the driver's, as m22-review says.
* The commit blocks and messages of the three pages: their commits exist and do not change (candidate 24's reason).
* Chapters 8, 12, 14 and 20: other M22 lines edit them.

**Decisions from the documents.**

* The pages point to `work/done/m22-review.md` rather than to a new run: its Mechanical checks and Proof hold the build and the green verify for `abb988a`'s `book/`, unchanged at `838f737` (git, above), which is "where the pages point" in the finding.
* The driver's rerun before the release is named once, on the page whose Proof promised a rerun before committing (item 3): m22-review, Findings.
* Records only: m22-review's Findings table, `m22-batch-proof`'s row.

**Decisions taken alone** (the author chose recommended answers):

* The finding's first branch (record on the pages), not a docs/05 sentence: the author's Findings paragraph says the three pages' Proof and Done when must agree.
* Items stay ticked and are reworded to what holds, rather than unticked: each criterion is met by the record they now name.
* Siblings included, since the finding covers them in the same files: ch08's Decision line 66 ("ticked on that understanding"), ch12's Divergence line 76 ("to rerun when those sites answer") and ch14-20's Divergence line 92; each repeats the deferral the finding names.
* The line numbers are those at `838f737`; /apply matches the quoted text if they moved.

**Done when.**

* [x] The nine replacements above made word for word, and nothing else in the three pages changed (`git diff` of each page shows only those lines).
* [x] `git diff --stat abb988a 838f737 -- book/` rechecked empty at /apply; later edits by other M22 lines do not touch these records, which speak of the runs at that state.
* [x] No em dash; no private case, so OD-3 approval is inapplicable.
* [x] `make verify` green after the last edit; only this delivery's paths and its hunk of docs/06 staged as docs/05 §6 says (the driver's in this batch), the page moved to `work/done/` and its commit message suggested.

## What happened

**Built.** The nine replacements, word for word, matched by their quoted text: the line numbers at `838f737` still held. `git diff HEAD` of the three pages shows 9 lines out and 9 in, nothing else; no item unticked.

**Checked.** `git diff --stat abb988a 838f737 -- book/` empty again at /apply; `1e0159b` (chapter 8) and `fac1518` (chapter 12) are ancestors of `abb988a`. `work/done/m22-review.md` holds both PDF paths under Mechanical checks and `make verify` green in its Proof. No em dash in the three pages.

**Divergences.** None.

**Decisions taken alone in /apply.**

* Staging and the commit are the driver's in this batch, from its own index: this session stages nothing.
* The Delivery review ran as a headless Opus session in plan mode, read-only, since this session could not start an agent of its own.

**Delivery review.** A read-only Opus context read `git diff HEAD` of the three pages and this line of docs/06 against this page, docs/04, AGENTS.md and `work/done/m22-review.md`: every replacement word for word, nothing else changed, no em dash, no claim that a session ran what it did not, the records named exist, the `book/` diff empty. No findings.

**Proof.** `make verify` green after the nine replacements, and again after the last edit of this page, its move and the queue's `[x]`.

```commit
docs(m22-batch-proof): three pages point to m22-review's runs

- ch08, ch12, ch14-20 pages: make verify and make book items say what ran
- Proof and Divergences point to the build and run m22-review records

work/done/m22-batch-proof.md
```
