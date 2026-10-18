# m20-review

**Objective.** The author can determine whether M20's technical claims match their examples and evidence in both editions, and whether the new executable-example check catches the demonstrated failures.

**Behaviour.**

* After every prerequisite is complete, the author receives both current PDFs, the clause checks below and their PDF page numbers, then records holds or fails for each.
* The runtime and compilation demonstrations recorded by the chapter deliveries are inspected against the printed examples; the example check is rerun with its documented failure demonstrations, not accepted solely because a page was marked done.
* On the author's word, area readers and a checker inspect a fixed range; missing paths or unavailable mandated reviewers leave `resume: apply` waiting with the actual reason.
* Missing evidence or an unanswered author check remains open; new commits do not move the endpoint, and each confirmed fault becomes a new `[ ]` line below this review in M20 without being fixed here.

**Contract.** Checks from docs/06's M20 paragraph, including its prevention and board lines:

| Promise | Delivery and passages | Author's check |
|---|---|---|
| Query behavior matches the claim | `ch03-query-catch`; chapter 3 boundary | Does recognized driver failure become a value while a bug/control object escapes, synchronously and asynchronously? |
| Exhaustiveness has an explicit check | `ch03-exhaustive-switch`; chapter 3 Result and handling sections | Which omitted case fails Record or never checking, and why is a bare switch insufficient? |
| Isolation is a goal | `ch04-isolation-claims`; chapter 4 | Can the reader identify affected consumers and explain why server decisions remain authoritative? |
| Recovery after compaction | `ch01-recovery-not-immunity`; chapter 1 | Can the reader recover by rereading the page/documents without expecting automatic persistence in every call? |
| Each scenario has appropriate proof | `ch12-scenario-levels`; chapter 12 example | Does each observable have the right check, including the real constraint race and exact column types? |
| Protocol has phase boundaries | `ch24-protocol-phase`; chapter 24 protocol | Does a missing agreed requirement stay in the delivery while a new capability becomes a line? |
| Historical totals disclose coverage limits | `ch22-cost-method`; chapter 22 measurement, gain and key points | Are unmatched per-delivery averages absent, limitations explicit, and new measurements taught with matching populations? |
| Prevention has evidence | `ch16-prevention-evidence`; chapter 16 | Can an actual error elsewhere justify proportionate prevention without hypothetical bureaucracy? |
| Waiting has no remembered board column | `ch14-blocked-column`; chapter 14 | Does resumption use the suffix and mark consistently, including a line blocked during definition and one blocked during implementation? |
| Verify executes printed examples | `verify-examples`; Makefile, checker, docs/01 and docs/04 | Does each edition's actual code run, and does an injected failure identify its source line and fail verify? |

Resolve the base as the commit that completed `work/done/m19-review.md`, not the last M19 finding fix; record its exact hash before any reading.
It does not exist at definition time; implementation waits for m19-review to be completed and committed so the base is unambiguous and available.
At apply start freeze HEAD as endpoint, record `git diff --name-only <base>..<endpoint>` and its stat, and assign every changed path to build, chapters, kit skills or documents (delivery records included).
Every exclusion needs an explicit reason; split large areas and account for all reviewed paths.
Read-only Opus readers plus checker, at most two concurrently, follow docs/05 §5 and §8, with seen/latent/weak labels and author confirmation; no substitute model.
Run `make verify` and any slow suite named in the active Verify slot.
Only this page, its final archive move and its queue mark/findings change; no API, schema or book edit.

**States.** Inapplicable: review, no screen.

**Visual reference.** Existing PDFs in both editions; apply adds page numbers to the named sections.

**Out of scope.** Fixing findings, revising the Ninjobs measurement, reviewing previous milestone clauses again, or inferring permission to launch readers from this definition.

**Decision.** Early definition was authorized by the author; all original dependencies remain and `after m19-review` is added because its completed commit supplies this review's base.
M20's cost clause follows the author's decision to preserve token totals and remove unmatched per-delivery averages.
The range's hashes and path inventory are execution inputs fixed before reading, with the selection rule fully defined here.

**Done when.**

* [ ] All clauses have recorded author answers; the runtime/checker evidence and actual printed examples agree.
* [ ] The exact base and endpoint, path inventory, complete reader coverage, slow-suite outcomes and checked candidates are recorded.
* [ ] Every confirmed failure becomes an M20 finding, with no fixes made during the review.
* [ ] `make verify` is green after final edits, both PDFs were built for the author, and this review alone is staged and archived with its suggested commit message.
