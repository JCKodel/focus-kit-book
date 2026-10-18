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
* [ ] Before implementation, the prerequisite is `[x]` and its owning rule matches the contract defined here; unexpected drift returns to definition rather than being silently resolved.
* [ ] Both editions implement every Behaviour scenario and preserve the draft on the documented return to `[ ]`.
* [ ] The chapter opens with its value, retains its evidenced team gain, has no filler and cuts nothing useful; every number and quoted artifact remains sourced, and terms follow docs/03.
* [ ] Any changed Case A passage is listed and author-approved under docs/00 OD-3; no new private details or em dash enter the text.
* [ ] `make verify` is green and `make book` builds both editions; results and both PDF review paths are recorded under docs/05 §5.

**Definition decision.** The author authorized defining dependent pages before implementation on 2026-10-18.
The complete contract of `kit-2026-10-18-1` settles the owning rule; retain `after kit-2026-10-18-1` as an implementation gate.
No further scope decision remains; the migration owns the process edit and this page owns the chapter explanation.
