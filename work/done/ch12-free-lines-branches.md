# ch12-free-lines-branches

**Objective.** After chapter 12's "What `/propose` does" a reader can say that, with a branch or a worktree per delivery, `/propose` judges whether its line is free, its own mark and the line each `after` names, from each slug's own worktree or branch, local or remote, because the main branch's queue, where it runs and whose `HEAD` the delivery's worktree starts from, shows each line as it was until its merge; on trunk it reads the one queue of the folder, at once; both editions, least change.

**Behaviour.** What the reader can do or explain after the chapter:

* Say where `/propose` reads the marks it checks before it starts: on trunk, the queue of the folder where the session runs, which every session sees at once; with a branch or a worktree per delivery, each slug's line from that slug's own worktree's file or branch, local or remote, reconciled by slug (chapter 14).
* Say why: the main branch's queue shows each line as it was until its delivery's branch is merged, so a line it shows `[ ]` may be `[~]`, `[*]` or `[?]` on its own branch, and `/propose` and the worktree it creates, from the main branch's `HEAD`, start from that stale view.
* Meet that reading inside the check that comes first: the reader still meets the refusal on a `[?]` line and on an unmet `after`, then where `/propose` stands (trunk, branch or worktree), then the first-edit `[~]`, in that order.
* Find, in the Key points, the `/propose` bullet saying that off trunk its line and its `after` are judged from each slug's own branch or worktree.
* Edge: a reader on trunk with two sessions in one folder reads nothing that sends them to a branch: the per-branch reading is said only for a branch or a worktree per delivery, and trunk stands first or beside it.
* Fails if: the chapter says or implies that a line marked `[x]` only on a branch not yet merged meets an `after` (docs/05 §4 keeps a dependency blocked until its completed changes reach the branch that needs it; how that reads is chapter 14's, `ch14-20-read-branches`); `/propose` creates or reuses a branch or worktree, or marks `[~]`, before it refuses a `[?]` line or an unmet `after`; the text gives a number, a count of worktrees or lines, a version, a date, "now", "no longer" or how the kit read before; it narrates a run; it names a path inside the container folder for the queue; the 21-day lines (en 59, 114, 137; pt as they stand) change; a title changes; the editions differ in order or sense.

**Contract.** The same changes in `book/en/12-propose.md` and `book/pt/12-propose.md`, nowhere else in the chapter:

* "What `/propose` does" (`## O que o \`/propose\` faz`), right after line 26 (the `[?]` / unmet `after` sentence, "... and does not start (chapter 14)." / "... e não começa (capítulo 14).") and before line 27 ("On a line it may start, ..." / "Em uma linha que ele pode começar, ..."): one new line, one sentence, in this sense, wording /apply's within it:
  * en: "On trunk it reads those marks in the queue of the folder where the session runs; with a branch or a worktree per delivery the main branch's queue, where it runs and whose `HEAD` the delivery's worktree starts from, shows each line as it was until its merge, so it reads its own line and each line its `after` names from that slug's worktree or branch, local or remote, reconciled by slug (chapter 14)."
  * pt: "No trunk ele lê essas marcas na fila da pasta onde a sessão roda; com um branch ou um worktree por entrega, a fila do branch principal, onde ele roda e de cujo `HEAD` parte o worktree da entrega, mostra cada linha como estava até o merge dela, então ele lê a própria linha e cada linha que o seu `after` nomeia no worktree ou no branch daquele slug, local ou remoto, reconciliadas pelo slug (capítulo 14)."
  * If the sentence reads long, /apply may split it in two lines at the semicolon, trunk first; no other sentence of the section moves or changes.
* "Key points" (en line 170, pt line 179), the `/propose` bullet: after "recommendation first," / "com a recomendação primeiro,", the clause "judges its line and its `after` off trunk from each slug's own branch or worktree," (pt "julga a própria linha e o seu `after`, fora do trunk, pelo branch ou worktree de cada slug,"); the rest of the bullet stays.
* Stays: lines 1 to 26 and 27 onward of the section in their words and order, the page example, the 21-day lines, "What the team gains" (still true: nothing it says depends on where a mark is read), every other section.
* Terms of docs/03: queue, mark, `after` (dependency), free line, trunk, branch, worktree, slug, main branch; in Portuguese "fila", "marca", "linha livre", "trunk", "branch", "worktree", "branch principal", "local ou remoto", "como estava", as chapters 18 and 19 already write them. No new term.
* Sources: docs/05 §4 as migrated by `kit-2026-10-19-1` (the board paragraph: "the main branch shows the line as it was until the merge, so whoever reads the queue there, a board or a session picking free lines or resolving an `after`, takes each slug's line from its worktree's file, or from its branch, local or remote, ... reconciled by slug"); the kit's SETUP.md at 2026.10.19.1, worktree per delivery ("`/propose` creates the slug's worktree there, from the main branch's HEAD"). No footnote: the chapter already names the kit's file for the command, and the changelog's numbers stay out (AGENTS.md, the book teaches the kit as it is today).
* Cases: none. No number. No lending library example: the sentence reads without one, and the page example below it is untouched.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no visual change.

**Out of scope.**

* Whether an `after` whose line is `[x]` only on an unmerged branch is met, and how a board or a session reads and reconciles the lines only a branch has: chapters 14 and 20, `ch14-20-read-branches`; chapter 12 points to chapter 14 and states neither.
* Chapter 8's update example at 2026.10.19.1: `ch08-update-2026-10-19-1`.
* Chapter 19's worktree section (line 179 already says the worktree starts from the main branch's `HEAD`; lines 180 and 350 say the main branch's queue shows the line as it was): true as it stands.
* Chapter 18, lines 25 and 203: true as they stand.
* The `[~]`-resume rule (a `[~]` line resumed only on the person's word): left out by `ch12-refuse-first`, still another line if wanted.
* Line 25's "`work/` for the deliveries in flight", whose pages also live on their branches under these strategies: the kit says nothing of it; a note for `work/kit-proposals.md`, not this chapter.
* docs/03, docs/05, docs/06: no edit; the queue line's marks are the driver's.

**Decisions from the documents.**

* The reading is per slug from its own worktree or branch, local or remote, reconciled by slug: docs/05 §4 as migrated (`work/done/kit-2026-10-19-1.md`), the board paragraph quoted in the Contract.
* The reason names the main branch's `HEAD` as where the delivery's worktree starts: SETUP.md 2026.10.19.1, worktree per delivery, and chapter 19 line 179.
* Branch and worktree both, though the queue line names the worktree: docs/05 §4 says "a branch or a worktree per delivery", and chapter 12 line 27 already names both.
* The reading sits inside the refusal step, before where `/propose` stands: the installed `/propose` skill checks the line and its `after` before it starts or resumes the definition (docs/05 §4; `work/done/ch12-refuse-first.md`).
* Trunk first or beside in every changed sentence: `work/done/ch12-branch-then-mark.md`'s wording rule; this repository is on trunk (ADR-0010).
* No number, version or before/after: AGENTS.md and the M21 rule that the book teaches the kit as it is today.

**Decisions taken alone.**

* One new line after line 26 rather than rewriting line 26: the refusal sentence keeps the words `ch12-refuse-first` gave it, and the reading follows it as "those marks".
* The chapter states the reading and its reason, and points to chapter 14 for the reconciliation and the unmerged `[x]`; it does not say that an `[x]` on an unmerged branch still leaves the `after` unmet, so chapter 12 cannot contradict what `ch14-20-read-branches` writes. The Fails if line forbids the opposite.
* No lending library example: one sentence with its reason teaches the rule, and an example would need a second worktree the chapter does not set up.
* The Key points clause goes inside the existing `/propose` bullet, as `ch12-branch-then-mark` did, not as a new bullet.
* The `HEAD` clause names the worktree, as SETUP.md does; it is not widened to the branch, which SETUP does not source. The branch per delivery is covered by "the main branch's queue, where it runs".
* "Lines only a branch has" is left to chapter 14: `/propose` on one line needs its own line and its `after`, and a line only a branch has is the board's and the reconciler's case.

**Done when.**

* [x] Both editions changed in the same two places, "What `/propose` does" and "Key points", and nowhere else in chapter 12; Portuguese read as Portuguese, with the words chapters 18 and 19 use.
* [x] In both editions, `grep -n` shows the `[?]` / `after` sentence, then the new reading sentence, then "first stands where" / "primeiro se coloca onde", in that line order.
* [x] `git diff` of the two chapter files touches only those two places; the 21-day lines unchanged.
* [x] No em dash; no number, version, date, "now", "no longer", "agora", "não mais" added; no narrated run; no path inside the container folder.
* [x] Delivery review as docs/05 §5 says, including that nothing implies an unmerged `[x]` meets an `after`.
* [x] `make verify` green: in this session every check passed but the link check, which failed only on external timeouts outside chapter 12 (Proof), and the whole run passed after `m22-review`'s last edit, with this chapter unchanged; `make book` built both editions from `abb988a`'s `book/`, which holds this chapter, and both PDF paths are in `work/done/m22-review.md`.
* [x] Only this delivery's paths and its hunk of docs/06 staged (the driver's in this batch); the page moved to `work/done/` and its commit message suggested.

**Proof.**

* `grep -n` on each file: the `[?]` / `after` sentence is line 26, the new reading sentence line 27, and the "first stands where" / "primeiro se coloca onde" sentence line 28, in both editions.
* `git diff HEAD` of the two chapters: 2 insertions and 1 deletion per file, the new line in "What `/propose` does" and the clause in the Key points' `/propose` bullet; the 21-day lines unchanged.
* The sentence kept whole on one line, trunk first, in the Contract's wording; the Key points clause as the Contract gives it.
* `make verify`: build, parity, em dash, prose, width, examples and disclosure green; the link check reported only timeouts on external sites (martinfowler.com, web.archive.org) that did not answer from this machine, none in chapter 12. The whole run passed after `m22-review`'s last edit, with chapter 12 as this delivery left it, and `make book` built both PDFs from `abb988a`'s `book/`: `work/done/m22-review.md` records both, with the PDF paths.
* Staging and the docs/06 hunk are the driver's in this batch.

**Divergences.** The link check's external timeouts above, outside this delivery; the whole run passed after `m22-review`'s last edit (Proof).

**Delivery review.** A read-only Opus agent read the diff of both chapters against this page, docs/04 and AGENTS.md: no findings.

**Decisions taken in /apply.**

* The sentence stays one line, not split at the semicolon: the section's other lines are as long, and one line keeps the order check to three lines.

```commit
docs(ch12-free-lines-branches): /propose reads marks off trunk per slug

- off trunk, /propose reads its line and its after from each slug's branch
- the Key points /propose bullet says the same, in both editions

work/done/ch12-free-lines-branches.md
```
