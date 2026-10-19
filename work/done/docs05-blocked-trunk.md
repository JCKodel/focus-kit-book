# docs05-blocked-trunk

**Objective.** An agent whose /apply blocks on trunk reads in docs/05 §6 that the work stays uncommitted and out of the index, and that a prerequisite becomes a `[ ]` line above it, with no move to a branch or worktree, as the kit's template, ADR-0010 and the trunk Git slot say.

**Behaviour.**

* An /apply blocked on trunk: docs/05 §6 says the work stays uncommitted and out of the index, and the `commit` block is a draft for the whole delivery, as the kit's template §6 says (`.claude/skills/brainstorm/references/documents.md`).
* An /apply blocked on trunk because another fix must be built first: §6 says the fix becomes a `[ ]` line above this one and this line waits `[?]` with `· resume: apply · blocked: after <slug>`, as `.claude/skills/apply/SKILL.md` and docs/05 §4 say; the partial work stays in the tree while the prerequisite is built and committed from an index holding only it.
* The prerequisite's session and the blocked work change the same lines: §6's existing rule holds, that session stops and reports the paths; nothing is reset or stashed.
* §6 no longer says "move this partial delivery to its own branch/worktree" nor "ask for help if safe separation is not possible"; a search of `book/`, `docs/` and `.claude/` for "branch/worktree" finds nothing.
* An /apply blocked on a delivery branch or worktree: §6's sentences on staging partial changes there and keeping the branch unmerged read as before.
* "Resume with the same page and record the current verify result" and "Do not mix their commits on trunk" stay.

**Contract.** docs/05-Process.md §6, the paragraph that today runs from "When blocked on trunk" to "Do not mix their commits on trunk." (lines 308 to 315), becomes:

```
When blocked on trunk, keep the work uncommitted and do not add it to the
index; the `commit` block is a draft for the eventual whole delivery.
Resume with the same page and record the current verify result. A
prerequisite that must be built first becomes a `[ ]` line above this
one, and this line waits `[?]` with `· resume: apply · blocked: after
<slug>` (§4). The partial work stays in the tree, uncommitted and out of
the index, while the prerequisite is built and staged alone; when the two
change the same lines, the prerequisite's session stops and reports, as
this section says. Do not mix their commits on trunk.
```

The next two sentences, "On a delivery branch or worktree, ..." to "... one merge still contains the whole delivery.", are unchanged. No other file changes: the line is one document, English only (docs/05's documentation language).

**States.** Inapplicable: prose, no screen.

**Visual reference.** Inapplicable: prose, no screen.

**Out of scope.**

* The delivery-branch sentences: they agree with the template and chapter 19 cites them (ch19-partial-branch-commits).
* "Resume with the same page and record the current verify result": a project addition the template lacks, consistent with §4; kept.
* ADR-0010 and the trunk Git slot: they already say no worktree; ADR-0010's amendment is adr0010-commit-asked's.
* The book: no chapter carries the removed sentence (searched `book/`, `docs/`, `.claude/`).
* The kit's template and skills: already say this; nothing to send the kit.

**Decisions taken alone.**

* The queue line says the prerequisite clause comes from "the kit's template"; the template's §6 holds only the uncommitted and out-of-index rule, while "a prerequisite fix becomes a `[ ]` line above this one" is `.claude/skills/apply/SKILL.md`'s, and the `blocked: after <slug>` form is docs/05 §4's. The paragraph cites §4; the page names all three.
* The removed "ask for help if safe separation is not possible" is replaced by §6's own stop-and-report rule for shared lines, so no case loses its answer.
* Written with no person available, on the author's batch authorisation; the `[~]` and `[>]` marks in docs/06 are the batch driver's.

**Done when.**

* [x] docs/05 §6 reads as the Contract, and every Behaviour line holds.
* [x] `make verify` green after the last edit.
* [x] The page is in `work/done/` and the line is `[x]`.

**Divergences.** None: docs/05 §6 reads as the Contract, word for word; the delivery-branch sentences are unchanged.

**Proof.** `grep -rn "branch/worktree" book docs .claude` finds nothing; §6's stop-and-report rule for shared lines (line 281) is the one the new paragraph points to; `make verify` green after the last edit.

**Delivery review:** skipped on the author's word (2026-10-19).

**Open questions taken alone.** None left open by the page.

```commit
docs(docs05-blocked-trunk): keep blocked trunk work in the tree

- docs/05 §6: a prerequisite becomes a [ ] line above, this one waits [?]
- the partial work stays uncommitted and out of the index, no worktree
- shared lines: the prerequisite's session stops and reports

work/done/docs05-blocked-trunk.md
```
