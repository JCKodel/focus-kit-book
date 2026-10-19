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
