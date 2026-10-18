# ch14-back-to-open

**Objective.** After chapter 14 the reader can resume a waiting line in the phase recorded by the kit, preserving its draft when it returns to `[ ]`.

**Behaviour.**
* Given `due-reminder [?]` with `resume: propose` and a resolved provider question, the reader removes both waiting suffixes, returns the line to `[ ]` and keeps its draft for `/propose`.
* Given a resolved waiting line with `resume: apply`, the reader returns it to `[>]`; the chapter does not teach a separate route to `[ ]` merely because scope changed.
* While the reason remains unresolved, neither command proceeds; a recorded answer or the last prerequisite becoming `[x]` can resolve the reason under the existing rule, without inventing an additional mandatory approval.
* The description and affected key points agree on removing both `resume` and `blocked` suffixes and keeping any draft; the draft's existence never means its definition is complete.

**Contract.** Files: `book/en/14-queue-states.md` and `book/pt/14-queue-states.md`, the waiting/resumption section and affected key points. Terms: docs/03 (mark, draft page and fresh session); no new term. Intended source: focus-kit `SETUP.md` version 2026.10.18.1, template docs/05 §4, read from the local uncommitted source on 2026-10-18, with no commit claimed for that version. It maps `resume: propose` to `[ ]` and `resume: apply` to `[>]`. Current project docs/05 §4 additionally permits returning an apply-phase line to `[ ]` when scope becomes undecided; the chapter currently follows that extra rule. The owner document must be aligned first by `kit-2026-10-18-1`; this delivery cannot silently contradict it.

**States.** Inapplicable: prose, no new screen.

**Visual reference.** Inapplicable: existing layout.

**Out of scope.** Changing docs/05 belongs to the kit migration. Board column placement belongs to `ch14-blocked-column`; session interruption and cancelled deliveries belong to `ch14-ended-and-dropped`; the definition mark belongs to `ch11-14-defined-mark`. No new private-case evidence.

**Done when.**
* [x] Before implementation, the prerequisite is `[x]` and its owning rule matches the contract defined here; unexpected drift returns to definition rather than being silently resolved.
* [x] Both editions implement every Behaviour scenario and preserve the draft on the documented return to `[ ]`.
* [x] The chapter opens with its value, retains its evidenced team gain, has no filler and cuts nothing useful; every number and quoted artifact remains sourced, and terms follow docs/03.
* [x] Any changed Case A passage is listed and author-approved under docs/00 OD-3; no new private details or em dash enter the text.
* [x] `make verify` is green and `make book` builds both editions; results and both PDF review paths are recorded under docs/05 §5.

**Definition decision.** The author authorized defining dependent pages before implementation on 2026-10-18.
The complete contract of `kit-2026-10-18-1` settles the owning rule; retain `after kit-2026-10-18-1` as an implementation gate.
No further scope decision remains; the migration owns the process edit and this page owns the chapter explanation.

**Divergences and omissions.** None. The `[ ]` return for an apply-phase line whose scope became undecided, which the chapter still taught, is gone from both editions, and the stop on a `[?]` line no longer waits for the person's word alone: any of the three ways that resolve the reason frees it. The opening, the problem, the evidence and the team gain are untouched.

**Case A.** No Case A passage changed.

**Delivery review.** A read-only agent on Opus read `git diff HEAD` of both chapter files against this page, docs/03, docs/04 and docs/05 §4, and found no contradiction left in chapter 14. Three wording points, all fixed in both editions: the draft sentence named `[ ]` twice, now ending on its reason; "those three" pointed too far back, now naming the reason; the key point's "returns by that phase" read as a calque in Portuguese, now "volta conforme essa fase", and "returns as that phase says" in English.

**Proof.** `make verify` green after the last edit. `make book` is run once by the batch driver at the end, which records `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf` for review.

**Decisions taken alone.** The prerequisite `kit-2026-10-18-1` is `[x]` and docs/05 §4 matches this page's Contract, so implementation went ahead with no drift to return to definition.

```commit
docs(ch14-back-to-open): return a resolved line by its resume phase

- chapter 14: resume: propose returns to [ ] with its draft, apply to [>]
- drop the apply-phase return to [ ] on undecided scope, as the kit says
- a [?] line is freed by any of the three resolutions, not only by word
- both editions and the key point agree

work/done/ch14-back-to-open.md
```
