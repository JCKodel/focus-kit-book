# ch12-refuse-first

**Objective.** After chapter 12's "What `/propose` does" a reader can say that `/propose` checks a line's mark and its `after` before anything else, and only on a line it may start does it stand where the Git slot puts the delivery and mark it `[~]`, as the kit's command does; both editions, least change.

**Behaviour.**

* Reading "What `/propose` does", the reader meets the refusal on a `[?]` line (says what it waits on, goes on only on the person's word that it is resolved) and on an unmet `after` (says the same, does not start) before the sentence on where it stands (trunk, branch or worktree) and the first-edit `[~]` mark.
* The sentence on where it stands reads as the step after those checks: on a line it may start, it first stands where the Git slot puts the delivery.
* Every other sentence of the section keeps its words and its order; the `[?]`-while-defining sentence (line 31) stays after the `[>]` and ending sentences.
* Fails if: any passage still has `/propose` create or reuse a branch or worktree, or mark `[~]`, before it refuses a `[?]` line or an unmet `after`; the chapter adds the `[~]`-resume rule or any other check the queue line does not name; it says the order is new, a version or how the chapter read before; it narrates a run; the 21-day loan passage (lines 59, 114; pt 59, 123) changes; a title changes; the two editions differ in order.

**Contract.**

The same passage in both editions, `book/en/12-propose.md` and `book/pt/12-propose.md`, section "What `/propose` does" (`## O que o \`/propose\` faz`):

* Line 30 ("On a line already `[?]`, ... does not start (chapter 14).", pt "Em uma linha que já está `[?]`, ... e não começa (capítulo 14).") moves, unchanged in its words, to stand before line 26.
* Line 26 ("When it starts, it first stands where ...", pt "Quando começa, ele primeiro se coloca onde ...") gains the condition that ties it to the check, e.g. "On a line it may start, it first stands where ..." (pt "Em uma linha que ele pode começar, ele primeiro se coloca onde ..."). Wording is /apply's within that sense; the rest of the sentence stays.
* Stays: lines 22 to 25, 27 to 29, 31 onward, the Key points (line 170 says where it starts, true as it stands), every other section.

Terms of docs/03 used: queue, mark, `after`, slot, trunk, worktree; none new. No number, no footnote, no private case, no lending library example added. Sources cited: none new.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no visual change.

**Out of scope.**

* The 21-day loan period's source (lines 59, 114; pt 59, 123): `ch07-12-loan-days`, after this line.
* The command's rule that a `[~]` line is resumed only on the person's word that its session ended: the queue line and finding O5 name only the order; another line if wanted.
* Chapter 14's account of the marks and the refusal (its line 108 says both commands stop on `[?]`, true as it stands).
* docs/03, docs/05, docs/06: no edit; the queue line is the driver's.

**Decisions from the documents.**

* The order is refuse first, then branch or worktree, then `[~]`: the installed command, `.claude/skills/propose/SKILL.md` ("Do not start a blocked line ... nor a line whose `after` is not done ... Otherwise follow docs/05 §§2, 4 and 5 first: start or resume the definition in the right branch or worktree"), finding O5 of `work/done/m21-review.md`.
* Least change, by moving the existing sentence rather than rewriting the section: the queue line and the driver ("Least change").
* No before/after or version in the text: AGENTS.md, `work/done/kit-2026-10-19.md`, the driver.

**Decisions taken alone.**

* The fix moves line 30 up instead of adding "before it creates anything" to line 30 in place: a reader then meets the steps in the order the command takes them, with one conditional clause on line 26 to join them.
* The `[?]`-while-defining sentence (line 31) stays where it is: it happens during definition, after the `[~]` mark, so its place is already right.
* The `[~]`-resume rule is left out: not in the finding, and adding it widens the section.

**Done when.**

* [ ] Both editions written, the same sentence moved and the same clause added in each, Portuguese read as Portuguese; the chapter opens as it did, no filler and nothing useful cut.
* [ ] In both editions the `[?]` / `after` sentence's line number is lower than the "first stands where" / "primeiro se coloca onde" sentence's (`grep -n` on each file).
* [ ] `git diff` of the two chapter files touches only that section; the 21-day lines are unchanged.
* [ ] No em dash; no "no longer", "now", "não mais", "agora", "2026.10" added; no narrated run.
* [ ] Delivery review as docs/05 §5 says.
* [ ] `make verify` green; `make book` builds both editions and both PDF paths are reported (the driver may run it once for the batch).
* [ ] Only this delivery's paths and its hunk of docs/06 staged; the page moved to `work/done/` and its commit message suggested.
