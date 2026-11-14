# ADR-0018: six marks

**Date:** 2026-10-05

## Context

Case A mirrored its queue, one way, to a kanban board its project manager followed, and the board showed two errors of the three marks.
A mark changed when a command ended, so a delivery reached Doing only once `/propose` had written its page, while the talk that defined it showed as To Do.
And a line blocked on the client's answers had no mark of its own: five such lines sat in Doing and read as work nobody had started; the project added `[?]` by hand.
This book had rejected `[?]` for itself (ADR-0013), on the ground that none of its lines waits on a person.
The error was not Case A's alone, so focus-kit took both answers in its version 2026.10.05: a mark for each moment the work changes, `[~]` being defined and `[*]` being built, and `[?]` for a line that waits, with its reason at the end of the line.

## Decision

The book follows the kit's six marks, `[ ]`, `[~]`, `[>]`, `[*]`, `[x]`, `[?]`, in its own queue and in docs/05 §4, and installs the kit 2026.10.05 for every host.

## Consequences

Chapter 16, "The queue while it happens", teaches the six marks; chapters 16 to 25 become 17 to 26 (ADR-0017, amendment).
Chapter 18, the governor, tells how a mark moved from one project to the kit; chapter 22 keeps question deliveries as Case A's customization and no longer calls `[?]` Case A's alone.
ADR-0013 is superseded.

## Amendment, 2026-10-13 (kit-2026-10-13)

Since `kit-2026-10-13` the book runs focus-kit 2026.10.13; the six marks are unchanged.

## Amendment, 2026-10-16 (kit-2026-10-16)

Since `kit-2026-10-16` the book runs focus-kit 2026.10.16, 2026.10.15 included with no migration, since its container folder applies only to a worktree per delivery and the book is on trunk (ADR-0010); the six marks are unchanged.

## Amendment, 2026-10-16 (kit-2026-10-16-2)

Since `kit-2026-10-16-2` the book runs focus-kit 2026.10.16.2, 2026.10.16.1 included; the six marks are unchanged.

## Amendment, 2026-10-17 (kit-2026-10-17)

Since `kit-2026-10-17` the book runs focus-kit 2026.10.17; the six marks are unchanged.

## Amendment, 2026-10-18 (kit-2026-10-18)

Since `kit-2026-10-18` the book runs focus-kit 2026.10.18; the six marks are unchanged, and `[?]` waits in a fourth case: a milestone review's code reading that missed part of its range (docs/05 §§4, 8).

## Amendment, 2026-10-18 (kit-2026-10-18-1)

Since `kit-2026-10-18-1` the book runs focus-kit 2026.10.18.1; the six marks are unchanged, and their states say three things more (docs/05 §4).
A `[~]` or `[*]` line whose session ended without blocking it keeps its mark and is resumed by its command on the person's word.
A delivery the person cancels ends `[x]` with `· dropped: <reason>`, and a line whose `after` names it is the person's to re-decide.
A resolved wait returns by its suffix alone, `resume: propose` to `[ ]` with its draft kept and `resume: apply` to `[>]`: the two returns the kit's template carried until it dropped them during 2026.10.16.1, kept here through later installations (a return to `[ ]` when scope became undecided and the recovery of a line blocked without `resume`), are retired.

## Amendment, 2026-10-19 (kit-2026-10-19)

Since `kit-2026-10-19` the book runs focus-kit 2026.10.19; the six marks are unchanged, and docs/05 §4 says where a board sees a mark: on trunk at once, with a branch or a worktree per delivery when that branch is merged.

## Amendment, 2026-10-19 (kit-2026-10-19-1)

Since `kit-2026-10-19-1` the book runs focus-kit 2026.10.19.1; the six marks are unchanged, and with a branch or a worktree per delivery a mark is read from the slug's own branch or worktree, the main branch showing the line as it was until the merge (docs/05 §4).

## Amendment, 2026-10-20 (kit-2026-10-19-2)

Since `kit-2026-10-19-2` the book runs focus-kit 2026.10.19.2; the six marks are unchanged, and running the product from a fresh clone is a manual always owed, named in docs/05 §5's Manuals slot: here `docs/manuals/build-the-book-from-a-clone.md`.

## Amendment, 2026-10-20 (kit-2026-10-20)

Since `kit-2026-10-20` the book runs focus-kit 2026.10.20; the six marks are unchanged, and with a branch or a worktree per delivery the delivery's branch, pushed by /propose when it creates it, is the claim of its line: after `git fetch` a line whose branch exists is taken, whatever the main branch's queue shows (docs/05 §4). The book stays on trunk, where no delivery branch is created and the agent never pushes (ADR-0010, docs/05 §5).

## Amendment, 2026-10-20 (kit-2026-10-20-1)

Since `kit-2026-10-20-1` the book runs focus-kit 2026.10.20.1; the six marks are unchanged, and a queue line may carry the `(PA)` token after its slug: `P` lets its /propose and `A` its /apply run while the lines above it are in flight, `-` waits for them to be `[>]` or beyond before /propose and `[x]` before /apply, and `after` holds for both (docs/05 §4). It applies on trunk as written, two sessions in one working tree being this queue's normal case; whoever changes the queue re-judges the tokens it affects, and a line without one is judged from the pages as before.

## Amendment, 2026-10-21 (kit-2026-10-20-2)

Since `kit-2026-10-20-2` the book runs focus-kit 2026.10.20.2; the six marks are unchanged, and with a worktree per delivery each session opens where it works: /propose in `main/`, ending with the worktree's path, and /apply in a fresh session opened in that worktree, stopping before any edit anywhere else, the container's manual letting `main/`'s session edit the worktrees. The book stays on trunk, where no worktree exists: /propose gives no path, /apply runs in the one working tree as before, and no manual is owed (ADR-0010, docs/05 §5).

## Amendment, 2026-10-21 (kit-2026-10-20-3)

Since `kit-2026-10-20-3` the book runs focus-kit 2026.10.20.3; the six marks are unchanged, and /propose or /apply typed with several slugs opens one subagent per slug, a subagent being a fresh session, opened at once where the `(PA)` tokens and `after` allow, a line still waiting reported, not waited for; the session edits nothing itself, asks the person each question a subagent reports and sends the answer back, and a command that says to decide alone or to build as well has the page record it (docs/05 §§2, 4 and 7). The skills keep disabling model invocation, since the command the person typed names every slug. It applies on trunk as written: with no worktree, each subagent works in the one working tree, two sessions in one working tree being this queue's normal case (ADR-0010).

## Amendment, 2026-10-21 (kit-2026-10-20-4)

Since `kit-2026-10-20-4` the book runs focus-kit 2026.10.20.4; the six marks are unchanged, and /propose claims its line by running the kit's script `claim.sh` through git's own shell, with the strategy docs/05 §5's Git slot names: with a branch or a worktree per delivery it checks the remote, creates or reuses the branch or worktree, pushes its branch only when the remote lacks it, and prints the path the /apply session opens in, and it edits no document, the mark `[~]` staying the agent's first edit. The rule stays in docs/05 §2. The propose skill may run git without Claude Code asking, a permission and no rule. The book stays on trunk, where the script creates, fetches and pushes nothing and prints the one working tree's path, so the Publish policy's "the agent never pushes" holds as before (ADR-0010, docs/05 §5).

## Amendment, 2026-10-21 (kit-2026-10-20-5)

Since `kit-2026-10-20-5` the book runs focus-kit 2026.10.20.5; the six marks are unchanged. docs/05 §4 says what `after` requires: neither /propose nor /apply starts until every line it names is `[x]`, whatever the `(PA)` token says, the rule it held before written out; and a page decided alone says the agent chose each answer, so the review finds it. Setup writes only into the repository the session works in and writes no `AGENTS.md` or docs/05, which /brainstorm and /analyze write. On trunk both rules apply as written (ADR-0010).

## Amendment, 2026-10-25 (kit-2026-10-24)

Since `kit-2026-10-24` the book runs focus-kit 2026.10.24; the six marks are unchanged. What may run now comes from the kit's script `queue.sh`, run through git's own shell like `claim.sh` with the strategy of docs/05 §5's Git slot: it draws docs/06's current milestone as a tree, each line under the last line it waits on with its state, and ends with the lines free for /apply and for /propose together, the lines without a token judged first by the files they touch; it edits nothing. /propose and /apply typed with no slug show it and ask, as propose's and apply's `SKILL.md` say, /apply ends with it, as apply's says, and the free lines are offered as one command with several slugs, each slug one more agent costing as much as one session (docs/05 §4). docs/06 does not change. On trunk the script reads the one working tree's queue and fetches no branch (ADR-0010).

## Amendment, 2026-10-26 (kit-2026-10-25)

Since `kit-2026-10-25` the book runs focus-kit 2026.10.25; the six marks are unchanged, and the `(PA)` token of `kit-2026-10-20-1` is gone: `after` is read per command, /propose starting when every line it names is `[>]` or beyond and /apply when every line it names is integrated, `[x]` on trunk, and the review line ends `· after all`. /apply checks the files its page touches against the builds in flight before its first edit; `claim.sh` creates the branch on origin or reopens this clone's, another clone's only with `resume`; with a branch or a worktree per delivery the branch's copy of a line is the current one until the merge. docs/05 gains the Design slot (ADR-0019) and the page's `## Outcome` heading, and docs/06 loses its tokens and ends every milestone review with `· after all` (docs/05 §§2, 3, 4, 5 and 8). On trunk the claim creates nothing and integration is the `[x]` itself (ADR-0010). Applied directly at the author's request on 2026-10-26, outside /propose and /apply.

## Amendment, 2026-10-26 (kit-2026-10-26)

Since `kit-2026-10-26` the book runs focus-kit 2026.10.26; the six marks are unchanged. A mark is changed by the kit's script `mark.sh`, one byte, staged with its line alone when /apply marks `[x]`; any other edit to docs/06 is the host's file edit on the lines it changes, never a program that writes the whole file (docs/05 §4). Applied directly at the author's request on 2026-10-26, outside /propose and /apply.

## Amendment, 2026-10-26 (kit-2026-10-27)

Since `kit-2026-10-27` the book runs focus-kit 2026.10.27; the six marks are unchanged, and `mark.sh` refuses a `[~]` on a line that is not `[ ]` and a `[*]` on one that is not `[>]`, so two sessions that start one line cannot both mark it. No document changes: the script alone does. Recorded at the author's request on 2026-10-26, outside /propose and /apply.

## Amendment, 2026-11-12 (kit-2026-10-27-1)

Since `kit-2026-10-27-1` the book runs focus-kit 2026.10.27.1; the six marks are unchanged. `· after all` leaves out the milestone's dropped lines, so a review waits on no line the person cancelled, while a line whose `after` names a dropped one still waits for the person to re-decide it (docs/05 §§4 and 8). Applied directly at the author's request on 2026-11-12, outside /propose and /apply.

## Amendment, 2026-11-12 (kit-2026-11-03)

Since `kit-2026-11-03` the book runs focus-kit 2026.11.03; the six marks are unchanged. /apply ends by telling the person each next step and by running `queue.sh` unasked, its `next:` written as the host invokes commands. No document changes: the skill alone does. Recorded at the author's request on 2026-11-12, outside /propose and /apply.

## Amendment, 2026-11-12 (kit-2026-11-12)

Since `kit-2026-11-12` the book runs focus-kit 2026.11.12; the six marks are unchanged. What /apply's review, proof or build finds wrong in what its delivery built or changed is fixed in that delivery. A flaw found in anything else is a finding: a grave one becomes a `[ ]` line ending `· from <slug>`, every other one a note under the page's `## For the review` heading, and a line for a test, a proof tool or a change to the process enters only on the person's word. The milestone review copies the notes and grades every confirmed finding, grave a line each, the medium ones the person picks on one `<milestone>-fixes` line, the small ones listed. The Verify slot names a ceiling of five minutes and its slow tests one line each, none here (docs/05 §§2, 3, 4, 5, 6 and 8; docs/06's four open M32 findings end `· from m32-review`). Applied directly at the author's request on 2026-11-12, outside /propose and /apply.

## Amendment, 2026-11-14 (kit-2026-11-13)

Since `kit-2026-11-13` the book runs focus-kit 2026.11.13; the six marks are unchanged. `[?]` waits in three cases and never on another line: a line that needs another first ends `· after <slug>` and keeps the mark that names its next command, whether the need is known when the line is added or found by work already started, which returns the line to `[ ]` from `[~]`, keeping the draft, or to `[>]` from `[*]`; `· blocked: after <slug>` is retired, and /apply no longer clears dependent lines at its end. A `[?]` blocks on the copy that put it, a line only a branch has sits under main's heading of its milestone, and `queue.sh` draws every open milestone, offering the free lines across them in the queue's order (docs/05 §§4 and 6; docs/03; docs/06 held no `[?]` line ending `· blocked: after`). Applied directly at the author's request of 2026-11-13, outside /propose and /apply.
