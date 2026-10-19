# docs-m21-tidy

**Objective.** The author can read in docs/06 where the rule for the next milestone lives and which clause of M21 each of its lines answers, read docs/05's Milestone review slot at its neighbours' width, read on m21-review's page the base case that fits it, and take three confirmed notes to focus-kit's next version.

**Behaviour.**

* Opening docs/06, the author reads in its header that docs/05 §4 also owns the next milestone: where a line no clause of the current milestone needs goes, and that a review's finding stays in its own (m21-review O10).
* Reading M21's paragraph, the author finds a clause for chapter 6 (Ninjobs' 91 deliveries ran on its own two commands, the kit arriving after the beta) and one for chapter 16 (where the words go when a command is full, with the kit's three ceilings), so `ch06-kit-after-ninjobs` and `ch16-ceiling-moves` each answer a clause, as m21-review's "No clause as written" row already tested them (O11).
* Opening docs/05 §5, the author finds the Milestone review slot with no line wider than 72 columns, the code span `git diff <base>..<end>` whole on one line, and the same words in the same order as before (O17, as `kit-2026-10-19` recorded it).
* Reading m21-review's Base paragraph, the author finds right after it a short correction: the base is m19-review's commit as "the previous review's commit" in docs/03's `milestone review` row, the last review that exists, since `m20-review` was dropped; not the case "where no earlier review exists" the paragraph invoked (O3).
* Opening `work/kit-proposals.md`, the author finds under "For the next focus-kit version:" three new items, 10 to 12, in item 9's style: §8 naming "or none" as the slot template does (K2); §8 naming the base when the previous milestone's review was dropped (O3); the README's reviewer sentence under the Git slot's commit form (G6, G7).
* Edges: no queue line changes mark, slug, sentence or `after` in this delivery's edit of docs/06 (its own `[x]` is the driver's or /apply's last step); m21-review's Base paragraph, Findings and commit block keep their text; no chapter, README, docs/03 row, ADR or installed kit copy changes.

**Contract.** This /apply edits docs/06's header and M21's paragraph itself, not only its own mark: the driver runs it alone, with no other session's hunk in docs/06. It stages only these hunks and its own line, and the paths below.

1. `docs/06-Queue.md`, line 3, becomes:

   > The marks, the suffixes (`· after`, `· resume:`, `· blocked:`, `· dropped:`), the order as priority, the next milestone and what may run at the same time are docs/05 §4, written once there.

2. `docs/06-Queue.md`, M21's paragraph: after "...SETUP.md §1's step 4 as a list, and what the kit assumes of one person, a team and a reader who does not read code." one sentence is appended to the same paragraph:

   > It also says that Ninjobs' 91 deliveries ran on its own two commands, the kit planted there after the beta, and where the words go when a command is full, with the kit's three ceilings.

   The lines below the paragraph are not touched.

3. `docs/05-Process.md`, §5, the Milestone review slot (today lines 259 to 268), rewrapped with the words unchanged:

   ```
   * **Milestone review:** the kit's readers: on the author's word in the
     review's /apply session, read-only agents on Opus read
     `git diff <base>..<end>`, the two commits the review's page names, its
     base and the commit HEAD was when the reading started, one per area it
     touches: the build, the chapters, the kit's skills, the documents. One
     more read-only agent on Opus checks each candidate against the file
     before the author sees it. Every agent keeps the session's advisor,
     Fable. Each launch sets its model to Opus; no other model runs the
     review. At most two of these agents run at a time: in `m16-review`
     five at once left three with no report.
   ```

4. `work/done/m21-review.md`: one paragraph inserted right after the **Base.** paragraph, before **End.**:

   > **Correction** (`docs-m21-tidy`). The base case that fits is "the previous review's commit", as docs/03's `milestone review` row words it: m19-review is the last review that exists, since `m20-review` was dropped as already read. The paragraph above invokes "where no earlier review exists", which does not hold; docs/05 §8, the kit's text, names the previous milestone's review and has no case for a dropped one, a note for focus-kit in `work/kit-proposals.md`. The base itself does not change.

5. `work/kit-proposals.md`: after item 9, three items in its style:

   > 10. **Who reads, or none** (from m21-review, K2). SETUP.md §8 at `fd1aa75` names two answers to who reads the milestone's code, the host's deep review or the kit's readers, while its Milestone review slot template ends "or: none". The next version names the third in §8 as the slot does: a slot that says none reads no code, and the person still tests each clause.
   >
   > 11. **The base after a dropped review** (from m21-review, O3). §8 names as the base the previous milestone's review, the first commit for a first milestone, or, where no earlier review exists, the commit the page names and why. None fits a milestone whose previous review was dropped while an earlier one exists, as M21 after M20. The next version names the last review's commit, as this repository's docs/03 row says "the previous review's commit".
   >
   > 12. **The reviewer under the commit form** (from m21-review, G6 and G7). README.md's "reviews the staged diff and commits" and "On a team, whoever commits is that reviewer" (README.pt.md: "revisa o diff em stage e commita", "quem commita é esse revisor") hold for the Git slot's default. Under its other form, where the agent commits by the slot's word, the person reviews the commit. The next version says both in both READMEs.

No docs/03 row, no chapter, no ADR.

**States.** Inapplicable: documents, no screen.

**Visual reference.** Inapplicable.

**Out of scope.**

* Editing docs/05 §8 itself for K2 or O3: it is the kit's text; the author confirmed both as notes for focus-kit.
* The blank line before "For the next focus-kit version:" and item 9's version (O12, O13): not confirmed.
* docs/05's other lines past 72 columns (249, 254 and others): not O17, which names line 260.
* M20's paragraph (O16): not confirmed.
* Any other finding of m21-review: each has its own line.

**Decisions.**

* The header names "the next milestone" between the order and what may run, matching docs/05 §4's order of rules (order, next milestone, parallel work) (docs/05 §4).
* The two clauses are one appended sentence, not entries in the colon list, because that list names what 2026.10.19 brought and chapters 6 and 16 teach no change of it; the wording follows m21-review's "No clause as written" row and the two queue lines (m21-review, Contract and Decisions; docs/06).
* The rewrap keeps the code span on one line and stays within 72 columns, the width the neighbouring slots mostly keep (`kit-2026-10-19`, Delivery review: "Rewrapped").
* The correction is a new paragraph after Base, leaving the recorded text as it was, so the page still shows what the review read (docs/05 §3: the page records what happened).
* docs/03's row already fits the case; it is not edited (m21-review, O3: "docs/03:33's wording weak: it fits").
* The kit notes cite SETUP.md and the READMEs at `fd1aa75`, the version this repository runs (`kit-2026-10-19`).

**Done when.**

* [x] docs/06's header and M21's paragraph read as Contract 1 and 2; no queue line changed but this delivery's own mark.
* [x] docs/05's Milestone review slot reads as Contract 3, its words equal before and after (compared with whitespace collapsed), no line past 72 columns.
* [x] `work/done/m21-review.md` carries the correction of Contract 4 and nothing else changes on it.
* [x] `work/kit-proposals.md` carries items 10 to 12 of Contract 5.
* [x] No em dash added; `make verify` green after the last edit.
* [x] Only this delivery's paths and hunks staged (docs/05 §6), with its suggested commit message.

**Proof.**

* `git diff -U0 HEAD -- docs/06-Queue.md`: three hunks, line 3 (Contract 1), line 517 (Contract 2, the sentence appended to M21's paragraph) and line 544, this delivery's own mark, the driver's; no other queue line.
* docs/05 lines 259 to 268: widths 70, 56, 72, 72, 72, 69, 69, 68, 68, 41; the slot's words at HEAD and now are equal with whitespace collapsed; `git diff <base>..<end>` whole on line 261.
* `work/done/m21-review.md`: one added paragraph between **Base.** and **End.**; nothing else on the page changed.
* `work/kit-proposals.md`: items 10 to 12 appended after item 9, as Contract 5.
* No em dash added. `make verify` green after the last edit.
* Staging and the `[x]` mark are the driver's in this run.

**Divergences.** None.

**Delivery review.** A read-only Opus agent read this delivery's hunks against this page, docs/04 and AGENTS.md: no finding. It checked the facts the notes cite: docs/03:33 says "the previous review's commit"; m21-review's findings K2, O3, G6 and G7 say what items 10 to 12 say; the README sentences quoted in item 12 and SETUP.md §8's two answers and base cases are in the kit at `fd1aa75`.

```commit
docs(docs-m21-tidy): M21's clauses, a rewrap and three kit notes

- docs/06: the header names the next milestone in docs/05 §4
- docs/06: M21's paragraph names what chapters 6 and 16 answer
- docs/05: the Milestone review slot rewrapped within 72 columns
- m21-review: a correction names the base case that fits
- kit-proposals: items 10 to 12 for the next focus-kit version

work/done/docs-m21-tidy.md
```
