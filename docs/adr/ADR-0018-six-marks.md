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
