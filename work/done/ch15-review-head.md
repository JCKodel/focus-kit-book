# ch15-review-head

**Objective.** After chapter 15 the reader can define and check a milestone review's fixed range even if new commits arrive while its readers work.

**Behaviour.**
* Given the previous milestone's review commit, the review page records it as base and records the commit HEAD points to when the reading starts as its fixed endpoint; every area's path inventory and diff use those same endpoints.
* Given a new commit after reading starts, an area reader does not silently include it by re-evaluating HEAD; all readers retain the recorded endpoint.
* Given a first milestone, the base remains its first commit, whose own additions are not in the range; fixing the endpoint does not change that exclusion.
* Given a reader's reported paths missing an area of the fixed inventory, the review waits with `resume: apply` and what was read as its reason; checking coverage against a later moving HEAD would be incorrect.

**Contract.** Files: `book/en/15-closing-a-milestone.md` and `book/pt/15-closing-a-milestone.md`; review definition, code-range explanation, path-coverage check and affected key points. Source: focus-kit SETUP.md 2026.10.18.1 template docs/05 §8, pinned in `work/kit-2026-10-18-1.md`. Terms: milestone review, base, HEAD, candidate and checker use docs/03; no new term. The page records actual endpoints when apply runs the review, not during propose. In teaching prose use placeholders such as `<base>` and `<review-head>` consistently, explaining the latter as the recorded starting HEAD; no actual commit hash or narrated run. The migration owns docs/05 and the domain definition.

**States.** Inapplicable: no new screen.

**Visual reference.** Inapplicable: existing layout.

**Out of scope.** No milestone review is executed here, no change to human authorization, reviewer model, checker labels or findings placement; slow tests belong to `ch05-13-slow-tests`.

**Decisions.** Definition uses the migration's contract under the user's exception; apply remains gated by `after kit-2026-10-18-1`. Preserve the chapter's existing base and first-commit caveats; the fixed endpoint solves only a moving reading range, not all concurrency.

**Done when.**
* [x] The migration is `[x]` and its owning rule agrees before apply starts.
* [x] Both editions answer all Behaviour scenarios and use one recorded endpoint consistently for inventory and reading, without literal historical hashes.
* [x] The chapter opens with its value, retains its evidenced gain, contains no filler or useful omissions, and every number/artifact remains sourced; no private-case changes.
* [x] `make verify` is green and `make book` builds both editions; proof records both PDF paths for author review, followed by delivery review and archival per docs/05.

**What happened.** Both editions of chapter 15 changed in the opening, "The review is a delivery", "Read the code since the base, by areas", the path-coverage check, "What the team gains" and the key points.
The review's page names as its end the commit `HEAD` was when the reading started, written `<review-head>` in the English edition and `<head-da-revisao>` in the Portuguese one; `git diff <base>..<review-head>` and its `--stat` give every area's list and diff, every reader takes those two commits from the page and never `HEAD`, which moves when a free line of the next milestone commits during the reading, and the coverage check compares the paths read with the list from `<base>..<review-head>`, never with a moved `HEAD`.
The first-milestone caveat keeps the first commit's exclusion and says recording the end changes only where the range stops.

**Divergences.** None. No Case A or Case B passage was added or changed.

**Decisions.** The placeholder is translated in the Portuguese edition, as docs/04 says of a placeholder a chapter writes. The chapter claims only that the list and the diff are fixed: readers still open files in the working repository and the checker marks what is true in the file today. It says nothing of where a commit made between `<review-head>` and the review's own commit is read, since docs/05 §8 does not say.

**Delivery review.** A read-only agent on Opus read `git diff HEAD` of both chapter files (no created file, no shared document) against this page, docs/04 and docs/05 §8. Points: (1) "every area's reading comes from the same range" overclaimed: fixed to the diff; (2) `<review-head>` left in English in the Portuguese edition against docs/04: translated to `<head-da-revisao>`; (3) "the list it wrote from `<review-head>`" read as one commit: fixed to `<base>..<review-head>`; (4) a key point whose verb attached to the placeholder: split in two; (5) a detached modifier in the next key point: reordered; (6) "not that" with no antecedent: "not that exclusion"; (7) "the commit it points to" after defining `HEAD` as a commit: "that commit"; (8) the opening's long second sentence: split, the fixed range in its own sentence. Verify ran again after the fixes.

**Proof.** `make verify` green after the last edit; `make book` is run once by the batch driver for both PDFs, `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`, for the author's review.

```commit
docs(ch15-review-head): fix the milestone review's range at its start

- Record the commit HEAD was when the reading started as the range's end
- Every reader's list and diff use <base>..<review-head>, never HEAD
- Check coverage against the recorded list, not a moved HEAD
- Keep the first commit's exclusion for a first milestone

work/done/ch15-review-head.md
```
