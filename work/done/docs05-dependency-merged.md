# docs05-dependency-merged

**Objective.** A session that reads docs/05 §4 finds one rule for when an `after` is met with a branch or a worktree per delivery, the kit's reading by slug, and no sentence calling a dependency "blocked".

**Behaviour.**

* Asked, with a branch per delivery, whether `return-book` is free once `lend-book` reads `[x]` on `lend-book`'s branch, not yet merged, the agent answers from docs/05 §4's board paragraph: yes, an `after` is read from each slug's own branch or worktree, as chapter 14 teaches (en :71 to 73); docs/05 holds no other sentence that says otherwise.
* Asked whether a line with `· after lend-book` is blocked, the agent answers from docs/05 §4 and docs/03's `dependency` row: it is an order, not a wait, and the line keeps its mark; docs/05 no longer says "keep a dependency blocked".
* On trunk nothing changes: the one docs/06 of the tree is read at once (this repository, docs/05 §5 Git, ADR-0010).
* The worktree paragraph keeps everything else it says: each worktree's queue shows that branch's state, the reconciliation by slug, no stale downgrade, checking the page at its expected path, a conflicting state or scope reported, the same care for domain terms and ADRs.
* Fails if: any text of docs/05 still says a dependency is kept blocked or waits for a merge; a new rule on merging before an `after` is met is invented; another section, chapter, document or record changes.

**Contract.** One edit, `docs/05-Process.md` §4, the worktree paragraph, lines 176 to 179 at `838f737`. docs/05 is English only (docs/05 §5, Documentation language), so there is no Portuguese text to change; no chapter teaches this sentence (m22-review, candidate 5; `grep` over `book/` finds none), so neither edition changes.

Today:

```
Check the page at the expected path and keep a dependency blocked until
its completed changes are available in the branch that needs them. A
conflicting state or scope is reported for resolution, never guessed.
Apply the same care to shared domain terms and ADRs.
```

After:

```
Check the page at the expected path. A conflicting state or scope is
reported for resolution, never guessed. Apply the same care to shared
domain terms and ADRs.
```

Only these four lines are rewrapped; no other line of docs/05 moves. No docs/03 term is added or changed: `dependency`, `free line` and `blocked` already say what the paragraph now agrees with.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Out of scope.**

* Writing a rule that a dependency's changes must be merged before the line that needs them starts: it would contradict the kit's reading by slug (docs/05 §4's board paragraph, focus-kit 2026.10.19.1) and chapter 14; a proposal for focus-kit, if ever wanted, is the author's to raise.
* The records that quoted the sentence (`work/done/kit-2026-10-19-1.md`:17, `work/done/ch12-free-lines-branches.md`:12, 32, `work/done/ch14-20-read-branches.md`:42): history, not changed.
* docs/03's `dependency` and `free line` rows (m22-review candidate 12, rejected), and every other finding of m22-review: their own lines.
* The rest of the worktree paragraph and §4's provenance sentence: unchanged.

**Decisions.** Taken alone on the author's recommended answers; each can be corrected in review.

* Drop the clause rather than rewrite it (the line allows "agrees ... or leaves"). Recommended because docs/05 §4's board paragraph, the kit's 2026.10.19.1 text, already says how an `after` is read off trunk, so any agreeing sentence would repeat it, and any sentence that waits for a merge would contradict it. The clause was the kit's own text once (focus-kit `1ae0aaa`) and the kit dropped it (`36a853d`); this repository kept it from `kit-2026-10-13` (`f67255a`). Source: SETUP.md at the kit's `35bdc9a`, docs/05 §4, m22-review candidates 5 and 6.
* Keep "Check the page at the expected path.": it is not part of the finding and still holds for integrating branches.
* Fixes candidate 6's wording with candidate 5 by the same cut: no "blocked" is said of a dependency anywhere in docs/05 afterwards (docs/03 `dependency`, `blocked`; docs/05 §4 "an order, not an interruption").
* Latent for this repository (on trunk, ADR-0010): the edit changes what docs/05 says for a project with branches, not how this repository works.

**Done when.**

* [x] docs/05 §4 reads as the Contract's After block; `grep -n "dependency blocked\|available in the branch" docs/05-Process.md` finds nothing.
* [x] No other file changes but this page and its line in docs/06 (the driver's).
* [x] `make verify` green after the last edit.
* [x] Delivery review by the session's advisor, not by the read-only Opus agent docs/05 §5 asks (Divergences); only this delivery's paths and its hunk of docs/06 staged, by the batch's driver from its own index; the page moved to `work/done/` and its commit message suggested.

**Proof.**

* `git diff HEAD -- docs/05-Process.md`: one hunk, §4's worktree paragraph, the four lines of Today replaced by the three lines of After, word for word; no other line of docs/05 moves.
* `grep -n "dependency blocked\|available in the branch" docs/05-Process.md` finds nothing; the same search over `book/` and `docs/` outside docs/06 finds nothing.
* `grep -n -i dependenc docs/05-Process.md` finds only §4's "A dependency known when the line is added is `· after <slug>` alone, without `[?]`: an order, not an interruption.", which agrees with docs/03.
* `make verify` green after the last edit (exit 0).

**Divergences.**

* Staging and the commit are the driver's in this batch: it commits each delivery from its own index, so the Done when item on staging is ticked on that basis.
* The delivery review did not run in a separate read-only agent: this lane had no tool to start one, so it went through the session's advisor, as earlier lanes of this batch did; no review by a read-only agent, as docs/05 §5 says, is recorded for it.

**Delivery review.** The session's advisor read this delivery's hunk of docs/05 and its hunk of docs/06 against this page and docs/04: one hunk in docs/05, three lines replacing four, matching the Contract's After block exactly; no "blocked" said of a dependency remains in docs/05, whose only `dependenc` match is §4's "an order, not an interruption"; no other file, section, record or edition changed. Fixed on this page: this paragraph, first written before the review ran, now says what it found; the Proof's verify claim, rerun after the page's last edit; the commit's second bullet, which gave reasoning, now states the highlight. The chapter, docs/06 and work/ changes in the tree belong to other lanes (`ch08-13-17-next-line`, `ch14-face-retired`, `ch20-merge-and-marks`, `ch08-13-20-default-review`) and were not read as this delivery's.

**Decisions taken alone in /apply.**

* The review went through the session's advisor, since no agent could be started from this lane.
* `docs06-m21-opening`, whose `after` names this slug, keeps its line as it is: an `after` is an order, and its other slugs are not all done.

```commit
docs(docs05-dependency-merged): drop the blocked-dependency clause

- docs/05 §4: the worktree paragraph no longer keeps a dependency blocked
- docs/05 §4: `after` stays an order read by slug, nothing new on merging

work/done/docs05-dependency-merged.md
```
