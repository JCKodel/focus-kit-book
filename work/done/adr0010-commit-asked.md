# adr0010-commit-asked

**Objective.** A reader of ADR-0010 learns from an amendment that the agent commits or merges only when the person asks, and that `make release` makes one commit, `VERSION`, as docs/05 §§5 and 6 say, with the ADR's earlier text untouched.

**Behaviour.**

* ADR-0010 ends with a new section, `## Amendment, <date of /apply> (adr0010-commit-asked)`, after the amendment of 2026-10-13.
* The amendment says the agent never commits or merges on its own and, asked, takes the step the person names, after the person has reviewed the delivery, since `kit-2026-10-18-1` (docs/05 §5 Git, §6, AGENTS.md).
* The amendment says the one commit a script makes is `make release`'s: on the author's `y` it commits `VERSION` alone as `chore(release): vX.Y.Z` (docs/05 §6, `docs/manuals/release-the-book.md`), since `copyright-version`.
* The Context, the Decision ("the author reviews and commits"), the Consequences and the 2026-10-13 amendment are byte-unchanged: `git diff` on the file shows only added lines at its end.
* Nothing in the amendment says the agent may commit an unreviewed delivery or a batch on its own.

**Contract.** Appended to `docs/adr/ADR-0010-trunk.md`, after a blank line:

```
## Amendment, <date of /apply> (adr0010-commit-asked)

Since `kit-2026-10-18-1`, the agent never commits or merges on its own; asked, it takes the step the person names, once the person has reviewed the delivery (docs/05 §§5 and 6, AGENTS.md).
Since `copyright-version`, `make release` makes one commit: on the author's `y`, it commits `VERSION` alone as `chore(release): vX.Y.Z` (docs/05 §6, `docs/manuals/release-the-book.md`).
The decision stands: one delivery, one commit, on `main`, decided by the author.
```

`<date of /apply>` is the day /apply writes the section, in `YYYY-MM-DD`. No other file changes; English only (docs/adr's language).

**States.** Inapplicable: prose, no screen.

**Visual reference.** Inapplicable: prose, no screen.

**Out of scope.**

* Rewriting the Decision line "the author reviews and commits" or the 2026-10-13 amendment: an ADR's history is not rewritten; the amendment says what changed.
* docs/05, AGENTS.md and the chapters: they already say this (agent-commits-asked, kit-2026-10-18-1, copyright-version).
* The release script's refusal scope (D3 of m19-review): not confirmed by the author.

**Decisions taken alone.**

* The heading follows ADR-0002's and ADR-0016's form, the date then the slug in parentheses; the date is /apply's, as amendments carry the day they are written.
* The sources are named by delivery slug, as the 2026-10-13 amendment names `ch21-one-tree`, not by commit.
* The last sentence states that the decision itself still holds, so the amendment reads as a clarification of who types the commit, not a reversal.
* Written with no person available, on the author's batch authorisation; the `[~]` and `[>]` marks in docs/06 are the batch driver's.

**Done when.**

* [x] ADR-0010 ends with the Contract's section and every Behaviour line holds; `git diff docs/adr/ADR-0010-trunk.md` shows only added lines.
* [x] `make verify` green after the last edit.
* [x] The page is in `work/done/` and the line is `[x]`.

**Divergences.** None: the section is the Contract's, with `<date of /apply>` as 2026-10-19.

**Proof.** `git diff docs/adr/ADR-0010-trunk.md` shows only added lines at the file's end; docs/05 §6 and `docs/manuals/release-the-book.md` both name `chore(release): vX.Y.Z`; `make verify` green after the last edit.

**Delivery review:** skipped on the author's word (2026-10-19).

**Open questions taken alone.** None left open by the page.

```commit
docs(adr0010-commit-asked): amend ADR-0010 on who commits

- the agent commits or merges only when the person asks, after review
- make release commits VERSION alone as chore(release): vX.Y.Z
- the decision and its earlier amendment are unchanged

work/done/adr0010-commit-asked.md
```
