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

* [ ] docs/05 §4 reads as the Contract's After block; `grep -n "dependency blocked\|available in the branch" docs/05-Process.md` finds nothing.
* [ ] No other file changes but this page and its line in docs/06 (the driver's).
* [ ] `make verify` green after the last edit.
* [ ] Delivery review as docs/05 §5 says; only this delivery's paths and its hunk of docs/06 staged; the page moved to `work/done/` and its commit message suggested.
