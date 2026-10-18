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
* [ ] The migration is `[x]` and its owning rule agrees before apply starts.
* [ ] Both editions answer all Behaviour scenarios and use one recorded endpoint consistently for inventory and reading, without literal historical hashes.
* [ ] The chapter opens with its value, retains its evidenced gain, contains no filler or useful omissions, and every number/artifact remains sourced; no private-case changes.
* [ ] `make verify` is green and `make book` builds both editions; proof records both PDF paths for author review, followed by delivery review and archival per docs/05.
