# Proposals for focus-kit

Not a delivery of this repository: suggestions from the author's reading on 2026-10-18, for the author to take to focus-kit's own repository. The book teaches the kit as it is; when a kit version carries one of these, an update milestone teaches it.

Taken to focus-kit 2026.10.18.1, taught by M19 in docs/06:

1. **Test time** (from ch05-test-time). Verify stays fast on every delivery; the Verify slot names the slow tests kept out of it, the milestone review runs them, and /apply says when a test is too slow for verify.
2. **A mark for "if there is time"** (from ch11-queue-grows). No new mark: a line no clause of the current milestone needs goes under the next milestone; a review's finding stays in its own.
3. **A broken link** (found by ch04-focus-optional's /propose). FOCUS is chapter 4, at `04-focus`, in SETUP.md and both READMEs.
4. **/propose in the asking session** (from ch11-agent-runs-propose, decision 4). /propose runs there or in a fresh session; /apply always fresh; the skills still disable model invocation.
5. **Use the product before committing** (from try-before-commit, decision 7). /apply's next steps start with using what the delivery changed.
6. **The Claude Code row** (from install-and-hosts). It reads `AGENTS.md` alone only where no `CLAUDE.md` exists, from v2.1.277; the kit still writes `CLAUDE.md` with `@AGENTS.md`.
7. **The agent's git rule** (from ch19-agent-does-git, decision 3). It never commits or merges on its own; asked, it takes the step the person names.
8. **"exceptions as values"**, the book's term, replaces "errors as values" in SETUP.md and both READMEs.
For the next focus-kit version:

9. **Ninjobs in two phases** (from ch07-ninjobs-focus). Ninjobs required FOCUS whole on every feature until its restart on 2026-08-29, and after it kept the two principles, vertical slices and exceptions as values, without the four pieces on every feature (ADR-0016's amendment ch07-ninjobs-focus; chapters 4, 6 and 7). 2026.10.18.1 took the earlier phase alone, with no date: SETUP.md §3.5's "FOCUS whole" answer ends "Ninjobs chose this", README.md says "Ninjobs took it whole." and README.pt.md "O Ninjobs adotou inteira."; the next version says both phases in all three. The copies the kit installs in this repository follow that version and are not edited here.

10. **Who reads, or none** (from m21-review, K2). SETUP.md §8 at `fd1aa75` names two answers to who reads the milestone's code, the host's deep review or the kit's readers, while its Milestone review slot template ends "or: none". The next version names the third in §8 as the slot does: a slot that says none reads no code, and the person still tests each clause.

11. **The base after a dropped review** (from m21-review, O3). §8 names as the base the previous milestone's review, the first commit for a first milestone, or, where no earlier review exists, the commit the page names and why. None fits a milestone whose previous review was dropped while an earlier one exists, as M21 after M20. The next version names the last review's commit, as this repository's docs/03 row says "the previous review's commit".

12. **The reviewer under the commit form** (from m21-review, G6 and G7). README.md's "reviews the staged diff and commits" and "On a team, whoever commits is that reviewer" (README.pt.md: "revisa o diff em stage e commita", "quem commita é esse revisor") hold for the Git slot's default. Under its other form, where the agent commits by the slot's word, the person reviews the commit. The next version says both in both READMEs.

13. **The pages in flight off trunk** (from ch12-free-lines-branches and m22-review, candidates 2 and 18). The /propose skill in SETUP.md §3 reads "the deliveries in flight in `work/`", which holds on trunk. With a branch or a worktree per delivery each page in flight is written and marked on its own branch, so the main branch's `work/`, where /propose starts, lacks every page not yet merged. The next version says /propose reads the pages in flight where it reads each slug's line: from that slug's worktree or branch, local or remote, reconciled by slug, as docs/05 §4 says since 2026.10.19.1. Chapters 12 and 19 keep the kit's words until then.
