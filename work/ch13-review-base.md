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
* [ ] The prerequisite is `[x]` and updated docs/05 agrees with the page before apply starts.
* [ ] Both editions answer all Behaviour scenarios with document updates before review and verify after later covered edits.
* [ ] The chapter opens with its value, retains its evidenced gain, contains no filler or useful omissions, and every number and quoted artifact remains sourced.
* [ ] `make verify` is green after the final covered edit; `make book` builds both editions; proof records both PDFs for author review, followed by delivery review and archival per docs/05.
