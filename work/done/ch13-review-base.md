# ch13-review-base

**Objective.** After chapter 13 the reader can tell whether a delivery review covered the whole delivery, including earlier branch commits and documents, and whether verification covers its final edits.

**Behaviour.**
* Given a delivery with staged and unstaged tracked changes, the read-only reviewer reads `git diff HEAD` restricted to its paths, not a bare diff that misses staged changes.
* Given a resumed delivery with partial commits on its branch, the reviewer also reads those delivery commits against its base; a clean working tree does not mean there is nothing to review.
* Given a new untracked file, the reviewer opens the file named by the writer; no tracked-file diff substitutes for reading it. Another delivery's files and queue lines remain outside this review.
* Given a changed schema or manual, apply updates its owning documents before review. The lending example lists its schema before its reviewer reads, rather than adding it after review.
* Given any later edit covered by verify, including a review correction or changed document, verify runs again before completion; the earlier green result is not treated as covering it.

**Contract.** Files: `book/en/13-apply.md` and `book/pt/13-apply.md`; delivery review, completion list, lending example and affected summary. Terms: delivery review, candidate, verify, manual, untracked file from docs/03. Source: focus-kit SETUP.md 2026.10.18.1's apply command and Delivery review slot, pinned by `work/kit-2026-10-18-1.md`. That migration owns docs/05 and installed commands. Preserve the distinction between a path-limited host review and a read-only agent's Git reading, and between whole-delivery coverage and milestone-wide review. No schema/API change.

**States.** Inapplicable: no new screen.

**Visual reference.** Inapplicable: existing layout.

**Out of scope.** Slow-test policy belongs to `ch05-13-slow-tests`; human use-first instructions to `apply-use-first`; no actual implementation review, new reviewer model, or private-case evidence.

**Decisions.** Definition proceeds under the user's exception using the migration's contract; apply still waits for `kit-2026-10-18-1`. Existing review outcomes stay in the lending example; only its ordering and coverage change. docs/04's ban on narrating a run remains in force.

**Done when.**
* [x] The prerequisite is `[x]` and updated docs/05 agrees with the page before apply starts.
* [x] Both editions answer all Behaviour scenarios with document updates before review and verify after later covered edits.
* [x] The chapter opens with its value, retains its evidenced gain, contains no filler or useful omissions, and every number and quoted artifact remains sourced.
* [x] `make verify` is green after the final covered edit; `make book` builds both editions; proof records both PDFs for author review, followed by delivery review and archival per docs/05.

**What happened.** Both editions of chapter 13 changed in "The delivery review", "Green is not done", the lending example, the staged review's questions and the key points.
The review now waits for the documents and manuals the delivery changes; the read-only agent reads `git diff HEAD` of the delivery's paths (a bare `git diff` misses what is staged), the commits a person made on a delivery branch from a blocked `/apply`'s staged partial work, none on trunk, and the files the delivery created; any edit verify covers after its last green run runs verify again.
The lending example adds the table `loan` to the schema document before the reviewer reads, and the reviewer reads that document in `git diff HEAD`; its two candidates and the commit message are unchanged.
The host's path-limited review and the milestone review keep their sentences.

**Divergences.** None. No Case A or Case B passage was added.

**Decisions.** The new sentence on branch commits names no chapter: chapter 19 does not teach committing partial work on a delivery branch, and the existing pointer at "When the work cannot go on" already stood before this delivery. The opening's list of what done means keeps its order, since it lists, not sequences.

**Delivery review.** A read-only agent on Opus read `git diff HEAD` of both chapter files (no created file, no shared document) against this page, docs/04, docs/05 §5 and the apply command. Candidates: (1) the branch sentence said a blocked `/apply` committed, against the chapter's never-commit rule: fixed, the person commits what it staged; (2) "a clean working folder means the work is in those commits" overclaimed: fixed to the page's form, it does not mean there is nothing to review; (3) chapter 19 does not teach the cited branch case: the new pointer dropped, the older one queued; (4) the Portuguese question read as if branch commits always exist: fixed with "tenha feito"; (5) and (6), the opening's order and the completion list's labels: judged fine, unchanged. Verify ran again after the fixes.

**Proof.** `make verify` green after the last edit; `make book` is run once by the batch driver for both PDFs, `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`, for the author's review.

```commit
docs(ch13-review-base): review the whole delivery after its documents

- Read git diff HEAD, the branch's delivery commits and created files
- Update documents and manuals before the delivery review
- Run verify again after any later covered edit
- List the lending schema before its reviewer reads

work/done/ch13-review-base.md
```
