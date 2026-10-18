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

* [x] Both editions pass every Behaviour check against the completed kit migration and use docs/03's terms.
* [x] Every affected chapter keeps its opening value and evidenced team gain; no filler, no useful content cut, and every number and artifact has a checked source.
* [x] `make verify` is green after the last covered edit, `make book` builds both editions, and the author receives both PDF paths for review.
* [x] The independent delivery review, proof and decisions are recorded under docs/05; no private passage is added, so OD-3 approval is inapplicable.

## What happened

**Contract check.** The completed migration agrees with this page: docs/05 §2 ("never commits on its own"), §5 Git ("it never commits or merges on its own, and asked, it takes the step the person names") and §6 ("the person commits after reviewing, or asks the agent to") say what the Behaviour asks; no contradiction.

**Built.**

* Chapter 6: already states the rule as SETUP.md §2 does, after ch06-23-kit-rules; checked, unchanged.
* Chapter 7: the git-strategy sentence gains "on its own; asked, it takes the step the person names", as chapter 6 words it.
* Chapter 13: title "never commit on its own", and docs/00's contents entry with it; the opening, the problem, "Why it stops at the stage" (the docs/05 quote now verbatim), "The commit is the human review" (asking the agent to commit, a commit asked is not a merge or a push, host permission does not replace the reading, `git show --stat HEAD` to check) and the key point.
* Chapter 18: the review is the reading before the commit; trunk and the key point say the person decides each commit and merge.
* Chapter 19: the commit stays the person's decision; the batch passage separates asking one reviewed delivery's session to commit it, from an index holding only it, from agents committing a batch on their own; checking a merge the agent made; the reading, gain and key points say "decide".
* Chapter 23: "Who decides each commit and merge", with the agent taking the one step asked; the key point follows.

**Decisions taken alone.** The new title is the old one plus "on its own" / "por conta própria", the phrase chapter 6 already uses; it is longer, so the PDF contents row for chapter 13 may wrap and the driver's `make book` should look at it. Chapter 13's next-steps bullet was left to `apply-use-first`, which owns it.

**Delivery review.** A read-only Opus agent read `git diff HEAD` of this delivery's paths and the docs/00 patch against this page and docs/04. It found every Behaviour line held in both editions, the docs/05 quote verbatim and chapter 6 agreeing. Candidates and answers:

* Chapter 13's pointer "the next section" named the wrong section: fixed.
* Chapter 19's opening, the reading under "You", the gain and a key point still said the person commits or merges unconditionally: each now says the person decides.
* Chapter 13's opening let "which is the human review" attach to a commit the agent made: reordered so the review is the reading.
* Chapter 23's key point dropped the merge: added.
* A merge the agent made had no check: one line on `git log --oneline --graph -3` added to chapter 19.
* Portuguese: "O ponto está no *por conta própria*" and "permite que ele digite" taken. The suggested rewording of "quando pedem" in chapters 6 and 7 was not taken: chapter 6 belongs to ch06-23-kit-rules, and the two stay worded alike.

**Proof.** `make verify` green after the last edit. `make book` and staging are the batch driver's; no Git action was taken. No private passage was added.

```commit
docs(agent-commits-asked): the agent commits only when the person asks

- chapters 6, 7, 13, 18, 19 and 23: never on its own; asked, the step named
- chapter 13 retitled "never commit on its own", docs/00 with it
- a commit asked is not a merge or push; permission is not review
- a batch: each delivery used, reviewed and committed from its own index
- chapter 23: a person decides each commit and merge

work/done/agent-commits-asked.md
```
