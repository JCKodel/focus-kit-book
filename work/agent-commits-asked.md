# agent-commits-asked

**Objective.** The reader can distinguish the person’s decision to commit or merge from the agent executing exactly the Git step explicitly requested.

**Behaviour.**

* After an ordinary apply, the agent stages and suggests a message, then stops without commit or merge.
* After using and reviewing one delivery, the person can ask the agent to commit that delivery or merge its named branch; the agent performs the named step and the person checks its result.
* A request to commit does not authorize a merge or push, and permission to execute the command does not replace the person’s review.
* In a batch, each delivery still receives its own use and review and an index containing only it; asking for a specific step is not permission for agents to commit an unreviewed batch autonomously.
* The adoption checklist assigns the commit/merge decision to a person without falsely requiring that person to type every Git command.

**Contract.** Edit both editions of `06-birth-of-focus-kit.md` (current kit rule, not historical outcomes), `18-git-essentials.md` (commit responsibility and strategy summaries), `19-worktrees.md` (requested Git assistance and batch limits), and `23-adoption.md` (responsibilities and key point).
Also correct only the contradictory git-strategy sentence in both editions of `07-the-documents.md`, currently an unconditional “never commits or merges”, and the unconditional commit-authority wording in both editions of `13-apply.md` (title, why it stops, human review and summaries).
Align docs/00’s contents entry with the revised chapter 13 title; no product behavior changes beyond the already approved commit-authority migration.
Source: SETUP.md §2, apply instructions and docs/05 template Git and Commit rules, as migrated by `kit-2026-10-18-1`.
Keep “on its own” explicit, retain human decision and review in every abbreviated version, and use docs/03’s commit, stage, branch, merge and unit-of-work terms.
Chapter 6’s revised rule must agree with `ch06-23-kit-rules`, applied sequentially because both touch it.
No new authority for publishing, releasing, tagging or altering unrelated staged entries.

**States.** Inapplicable: prose, no new screen.

**Visual reference.** Inapplicable: existing chapter layout.

**Out of scope.** No Git action is performed by this editorial delivery. Branch strategy, index mechanics and revert scope remain their existing queue lines; no change to measured Ninjobs history or private cases.

**Definition decision.** The author authorized defining this page before its dependency completes, using `work/kit-2026-10-18-1.md` as the contract.
The queue retains `after kit-2026-10-18-1` as an implementation gate; apply first checks the completed migration against this contract and reports any contradiction.
Source is the local working copy of focus-kit SETUP.md 2026.10.18.1, not its older HEAD; the installation page owns its fingerprint.
No implementation or staging occurs during this proposal.

**Done when.**

* [ ] Both editions pass every Behaviour check against the completed kit migration and use docs/03's terms.
* [ ] Every affected chapter keeps its opening value and evidenced team gain; no filler, no useful content cut, and every number and artifact has a checked source.
* [ ] `make verify` is green after the last covered edit, `make book` builds both editions, and the author receives both PDF paths for review.
* [ ] The independent delivery review, proof and decisions are recorded under docs/05; no private passage is added, so OD-3 approval is inapplicable.
