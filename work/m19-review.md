# m19-review

**Objective.** The author can decide whether each promise of M19 holds in both editions and the installed process, with every confirmed failure recorded as a new finding in M19.

**Behaviour.**

* With every prerequisite completed, the author receives current PDFs and the clause checks below, with their starting pages in both editions; each answer is recorded as holds or fails with the observed fault.
* The review compares installed commands and active project documents with the kit version specified by the installation page, then checks the book's explanations against those rules.
* On the author's word, read-only area readers inspect one fixed commit range; a checker tests each candidate against that same snapshot and labels it seen, latent or weak before the author decides which become findings.
* A missing clause answer, unavailable required reviewer or incomplete path coverage leaves this review waiting with `resume: apply` and its actual reason; a passing partial reading never closes it.
* A new commit during reading does not move the fixed endpoint; later changes are identified as outside that reading. Confirmed findings become `[ ]` lines below this review in M19, with no fixes made here.

**Contract.** Clause checks from docs/06's M19 paragraph, each performed against the named delivery's completed page and the cited chapter passages in both PDFs:

| Promise | Deliveries and passages | Author's check |
|---|---|---|
| Installed kit and matching process | `kit-2026-10-18-1`, `ch08-update-2026-10-18-1`; installed files, docs/04 and docs/05, chapter 8 update example | Do the installed version and recorded migration report agree with the active rules and real example? |
| Fast verify and named slow tests | `ch05-13-slow-tests`; chapters 5, 7, 13 and 15 | Can the reader locate each suite and explain when it runs and how a slow failure is recorded? |
| Milestone placement | `ch11-next-milestone`; chapters 11, 14 and 15 | Where does unrelated work go, and where does a review's finding stay? |
| Proposal sessions and use before commit | `propose-same-session`, `apply-use-first`; affected passages in chapters 8 to 13, 17 to 19, 22 and 23 | Can a reader choose either proposal session, start apply fresh, use the result and request corrections before committing? |
| Git authority and isolation | `agent-commits-asked`, `ch19-commit-by-index`, `ch18-kit-branches`, `ch18-revert-scope`, `ch19-batch-staging`, `ch10-explicit-staging`; chapters 6, 7, 10, 13, 18, 19 and 23 | Is explicit authority distinct from autonomous action, does the index contain one delivery, and are external effects distinguished from git undo? |
| Queue and review lifecycle | `ch11-14-defined-mark`, `ch14-back-to-open`, `ch13-refuse-incomplete`, `ch14-ended-and-dropped`, `ch13-review-base`, `ch15-review-head`; chapters 11, 13 to 15 and 23 | Given draft, interrupted, blocked, cancelled and staged cases, can the reader select the mark, resumption and exact review input? |
| Remaining comparison corrections | `ch21-done-when`, `ch17-context-read`, `ch08-10-fresh-start`, `ch06-23-kit-rules`, `ch08-hosts-details`, `ch09-empty-repo`, `ch02-93-moment`, `ch07-ninjobs-focus`; their bounded Contract passages | Does each Behaviour scenario in these completed pages hold when read alongside the other chapters, including the two phases of Ninjobs and distinct count moments? |

Base: `1ac62f67b2f5462d7b49c53e395cb3a6b71156ef`, the commit of m18-review.
At apply start, after prerequisites are available, record the exact HEAD as endpoint and inventory `git diff --name-only <base>..<endpoint>` and its stat before launching readers.
Partition every changed path among build, chapters, kit skills and documents, assigning delivery records to documents; record every exclusion with its reason instead of silently omitting paths.
Split large areas into manageable path groups; use docs/05's Opus readers and checker, at most two concurrently, with no substitute model.
Run any slow tests actually named by the Verify slot; none is invented for the review.
Only this page, its final archive move, and its own queue mark/findings change; no schema, API or book content change.

**States.** Inapplicable: review, no screen.

**Visual reference.** Existing English and Portuguese PDFs, chapter sections above; apply records current PDF page numbers.

**Out of scope.** Fixing findings, re-reviewing previous milestone clauses, changing review models, or assuming the author waived PDF reading or authorized readers merely by approving this definition.

**Decision.** The author authorized early definition before prerequisites complete; their `after` gate remains.
The endpoint and concrete path inventory are execution inputs fixed before reading, not unsettled review scope (docs/05 §8 and `ch15-review-head`).

**Done when.**

* [ ] Every clause has the author's answer, and every named prerequisite is completed and available.
* [ ] Base, endpoint, area inventory, slow-suite outcomes, reader coverage and checked candidates are recorded; required approvals are recorded.
* [ ] Every confirmed failure is a separate queue finding in M19; no fix is silently made.
* [ ] `make verify` is green after final edits, both PDFs were built for the author's reading, and this review alone is staged and archived with its suggested commit message.
