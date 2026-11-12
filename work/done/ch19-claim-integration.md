# ch19-claim-integration

**Objective.** After chapter 19 a reader with a worktree per delivery knows what the kit's claim script answers, `new`, `existing`, `existing, branch pushed now`, `taken`, `resumed` or `here`, that it creates a delivery's branch on origin only when no clone has it and cuts the worktree from origin's main branch, and reads the queue tree as the kit's queue script draws it from the branches on origin: a branch is a claim, a branch's copy of its line is the current one until the merge, a `[?]` on any copy blocks, a `[x]` not merged is built and awaiting integration, a line only a branch has stands in its milestone, and two builds that touch the same files run one after the other in worktrees as in one folder; both editions.

This page was defined and built by the agent before the author read it, on the author's word that the agent runs the whole queue; the author reads the page and the diff at the end (docs/05 §4).

**Behaviour.**

* Reading the section "Worktrees in the kit", the reader learns that `/propose` claims the line with the claim script, which fetches origin, creates the worktree from origin's main branch as just fetched, so a clone that did not pull still starts from what is integrated, and pushes the branch only when no clone has it.
* Reading the paragraph on the queue script, the reader learns the copy rule: a branch on origin is the claim; while the branch's copy still says `[ ]` the tree shows `claimed, progress unknown: propose in flight`; the branch's copy of its slug's line is the current one until the branch is merged into the main branch on origin, the main branch's after it; a `[?]` on any copy shows the line blocked until it is `[x]`; a `[x]` not merged shows `built, awaiting integration`, and a line whose `after` names it waits with `<slug> built, not integrated`.
* Reading the tree example, the reader sees the block below, `overdue-list` free for `/apply` and named by `next:`, and learns that the script reads marks and `after`, not files: `/apply overdue-list` in its worktree finds `src/features/loans/` in `return-book`'s build too, stops before its first edit, and builds once `return-book` is merged, as chapter 14 says of one folder.
* Reading the same passage, the reader finds `damaged-copy` (pt `exemplar-danificado`) shown at the end of its milestone with `(only on branch return-book)` and offered for `/propose`, not listed apart.
* Reading the passage after the merge, the reader learns that in `overdue-list`'s worktree the main branch's copy on origin is the current one for `return-book` once merged, `[x]`, so the line leaves the tree; with `trunk` in that worktree the script reads only the folder's copy and offers `return-book` as `propose now`.
* Reading the passage on what reaches origin, the reader learns that without the person's commit and push a claimed line shows `[ ] overdue-list · claimed, progress unknown: propose in flight`, not `propose now`, and that another clone's `/propose` of that slug gets `claim: taken`.
* Reading the paragraph on the claim script's refusals and output, the reader learns: in the slug's own worktree it answers `claim: here` with that folder's path and creates nothing; in another slug's worktree or on a delivery branch it refuses; it notes when `main` is behind or ahead of origin, the delivery starting from origin's main branch all the same; a branch on origin of which this clone has nothing is another clone's, `claim: taken`, exit 2, opened only when the command ends with `resume`, on the person's word, printing `claim: resumed`; a branch that appears on origin between the check and the push makes it remove what it made and answer `claim: taken`.
* Reading the worktree passages (:81, :93, :97 to :101, :386 to :388, key points 2, 4 and 5), the reader finds no claim that two builds on the same files run at once in worktrees, nor that a worktree lifts a file conflict: `/apply`'s file check holds in either form, as chapters 13 and 14 say, and a worktree per delivery keeps each delivery on its own branch until its merge.
* Edge: :252 to :257, the blocked `/apply` in a worktree, stay as they are; the `[?]` rule is said once, in the queue script's paragraph.
* Edge, the shared tree: another session may work in the same tree on another M33 line; its files and its docs/06 line are its own (docs/05 §4).
* Fails: a block line not byte for byte the run; a sentence about a script that a run on the installed scripts does not show; a sentence changed in one edition and not the other; an em dash; a block wider than 74 columns; more than five key points; `make verify` red.

**Contract.**

Sources: the installed `claim.sh` and `queue.sh` (`.agents/skills/propose/scripts/`, focus-kit 2026.11.12) and the kit's `CHANGELOG.md`, section 2026.10.25. The fixture is `ch19-example-marks`' with the kit as it is now: a bare origin; on `main`, docs/06 under `## M2. Returns` (`## M2. Devoluções`) holding `[x] lend-book`, `[ ] return-book · after lend-book`, `[ ] overdue-list · after lend-book`, `[ ] m2-review · after all`, each with a description, no token; a container with `main/` and `.focus-kit/`; both lines claimed with `claim.sh ... worktree .focus-kit focus-kit/`; `return-book`'s branch committed and pushed at `[*]` with `[ ] damaged-copy` added above `m2-review`; `overdue-list`'s committed and pushed at `[>]`; run from `main/` with `worktree .focus-kit focus-kit/`. Checked at /propose: it prints the blocks below; with `overdue-list` not committed it prints `[ ] overdue-list · claimed, progress unknown: propose in flight`.

English block, the run, widest line 59 columns:

```
milestone: M2. Returns
[*] return-book · in flight: apply
[>] overdue-list · apply now
 └[ ] m2-review + after return-book · propose now
[ ] damaged-copy (only on branch return-book) · propose now

free for /apply, in order: overdue-list
free for /propose, in order: m2-review damaged-copy
next: /apply overdue-list
```

Portuguese block, the run, widest line 69 columns:

```
milestone: M2. Devoluções
[*] devolver-livro · in flight: apply
[>] lista-de-atrasos · apply now
 └[ ] m2-review + after devolver-livro · propose now
[ ] exemplar-danificado (only on branch devolver-livro) · propose now

free for /apply, in order: lista-de-atrasos
free for /propose, in order: m2-review exemplar-danificado
next: /apply lista-de-atrasos
```

Passages of `book/en/19-worktrees.md` at HEAD `8ff514d`, and the same lines of `book/pt/19-worktrees.md`, each rewritten to say what Behaviour lists and nothing else: :81 (the conflict's remedy, `· after` only); :93 (when a worktree pays, the second case one build at a time); :97 to :101 (the example pair, `overdue-list` defined meanwhile and built after `return-book`'s merge); :192 (the claim); :199 (the copy rule, the claim, `[?]`, built and awaiting integration); the block :202 to :212; :214 to :216 (what the block shows, the file check, `damaged-copy`); :218 to :219 (the current copy after the merge); :224 to :226 (the claimed line without a push, `claim: taken`); :238 to :240 and :250 (the claim script's refusals, notes, `taken`, `resume`, `here`, its values); :387 to :388 (files both change); key points :412, :414, :415. No section added or removed; one sentence per line.

docs/03: the rows claim and queue tree say what the scripts do now (create-only, `taken`, `resume`, `here`, origin's main; the claim, the current copy, `[?]` on any copy, built and awaiting integration, the line only a branch has in its milestone), since this chapter teaches those terms and the rows still say the further mark and a list apart. No new term. Cases: none. Sources cited: none new; the chapter's examples stay "written for this chapter".

Decided by the agent, the author corrects it in the review:

1. The worktree passages of the note in `work/done/ch19-example-marks.md` (:93, :97 to :101, :386, key points) are this line's, with :81 and key points 2 and 5, which say the same: rerunning the block with the installed script makes `overdue-list` free for `/apply`, and the chapter must then say what `/apply` does with the shared folder, which chapters 13 (:45) and 14 (:95, :107) already teach with no strategy excepted. The alternative, a line of its own under M33, would leave chapter 19 contradicting chapters 13 and 14 until it ran.
2. The block is the fixture with `overdue-list`'s `[>]` pushed: with it unpushed, the Portuguese review row prints 76 columns, past docs/04's 74; the claimed state is quoted in a sentence instead.
3. The tokens' removal from chapter 19 (the note in `work/done/ch11-14-after.md`) is this line's: the block is the installed script's run.
4. docs/03's two rows change in this delivery rather than becoming a note, since the chapter would otherwise contradict them.
5. The worktree's second case in :93 stays, as focus-kit's `SETUP.md` Git slot still names it, with the file check said beside it.

**Out of scope.**

* Chapters 12 (:30) and 13 (:29) describing the claim as reusing or creating a branch: the note of `ch11-14-after`, not this line's.
* Chapters 8, 9, 17 and 20: their M33 lines.
* The kit itself (`SETUP.md`'s Git slot, the scripts): read, not changed.
* docs/05, ADRs, the manuals: unchanged.

**Done when.**

- [x] Both editions changed as the Contract says, and nothing else in the chapter.
- [x] Both blocks byte for byte a rerun of the installed `queue.sh` on the fixture; each changed sentence about a script matched by a run on scratch repositories, recorded under Outcome.
- [x] Opens with its value, no filler and nothing useful cut, every number sourced (none new).
- [x] No em dash; blocks within 74 columns; at most five key points.
- [x] docs/03's two rows changed.
- [x] `make verify` green; `make book` builds both PDFs, their paths given.
- [x] Delivery review by a read-only Opus agent (docs/05 §5).
- [x] Cases: none, so no approval is needed (docs/00 OD-3).

## Outcome

Built as defined, with these divergences:

* The race sentence of Behaviour (a branch that appears on origin between the check and the push) is not in the chapter: on a scratch run where both clones cut the branch from the same commit of origin's main, the create-only push is a no-op and both get `claim: new`; the script removes what it made only when the other branch has moved (`claim: taken ... appeared on origin meanwhile`). The chapter says "only when origin has no such branch", which holds.
* Added from the runs: a clone made with `git clone --bare` after a line's claim holds that branch as its own, so the script answers `existing`, not `taken` (en/pt :245).
* From the Delivery review: :229 "never free in the tree" became "never free for `/propose`", since a claimed line at `[>]` is free for `/apply`; :198 and :200 say the main branch's copy is `main/`'s own queue when run from `main/`, so pull there after a merge (a merged line read from an unpulled `main/` shows claimed); :192 and key point 4 say "origin has no such branch" for "no clone has it"; pt :192 and :245 reworded; docs/03's claim row says "reopens a branch of this clone that the remote lacks" and its queue tree row names `main/`'s own file.

**Proof.** On scratch repositories outside this one, with the installed `claim.sh` and `queue.sh`: the Contract's fixture printed both blocks byte for byte (`cmp`, after the edits), en and pt; with `overdue-list` uncommitted it printed `[ ] overdue-list · claimed, progress unknown: propose in flight` (pt `lista-de-atrasos`); `[?]` on `return-book`'s branch copy, and on main's copy with the branch at `[*]`, each printed the line blocked; `[x]` pushed and unmerged printed `built, awaiting integration` and `waits: return-book built, not integrated`; after the merge, from `overdue-list`'s worktree, `return-book` left the tree, and with `trunk` there it printed `[ ] return-book · propose now`; a failed fetch printed the note; `claim.sh` printed `claim: taken` (exit 2) and `claim: resumed` from a clone made before the claim, `claim: existing` from one made after it, `claim: here` in the slug's own worktree, `error: run from main/, not from a worktree` in another's, and the behind and ahead notes. `make verify` green after the last edit, 13.5 seconds wall time (ceiling five minutes). `make book` built `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.

**Delivery review.** A read-only agent on Opus read the page, docs/04, `git diff HEAD` of both chapter files and docs/03, this delivery's line of docs/06, both scripts, chapters 13 and 14 around the file check and docs/05 §4; it reran the English block and the states on scratch fixtures and consulted its advisor. Its findings 1 to 4 and the two Portuguese wording points are fixed above; its point on the worktree's second case is decision 5, left for the author; the rest are the notes below.

**Decisions taken alone.** Those under Contract, for the author's review, and the divergences above.

## For the review

* book/en/19-worktrees.md:93 and key point 4 (pt the same): the worktree's second case, one person whose deliveries touch the same files, stays as focus-kit's `SETUP.md` Git slot names it, beside the file check that builds them one after the other; a reader may not see its gain. The author may name it (each delivery defined and committed on its own branch) or drop it.
* Kit, `claim.sh`: the "ahead" note prints twice, the second garbled (`by ;`), its `printf` given three arguments for two `%s`.
* Kit, `claim.sh`: two clones that claim one slug at once from the same commit of origin's main both get `claim: new`, the create-only push being a no-op on an equal commit.
* Kit, `claim.sh`: a clone made with `git clone --bare` after a claim answers `existing` for it, not `taken`.
* Kit, `claim.sh`: a local branch with no worktree and not on origin makes it stop with git's `fatal: a branch named ... already exists`, exit 255, not `error:` and exit 2; book/en/19-worktrees.md:255 says `existing` for "this clone's worktree or branch".
* Kit, `queue.sh`: a line only a branch has goes after the review line, so `m2-review` is `propose now` with `damaged-copy` undefined (book/en/19-worktrees.md:217, pt the same), as the chapter prints and does not explain.

```commit
docs(ch19-claim-integration): teach the claim and the current copy

- claim.sh: create-only from origin's main; taken, resume, here
- queue.sh: a branch is a claim; the branch's copy current until merge
- a [?] on any copy blocks; built, awaiting integration; branch-only lines
- worktrees build shared files one after the other; tree block rerun
- docs/03 claim and queue tree rows; both editions

work/done/ch19-claim-integration.md
```
