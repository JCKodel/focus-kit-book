# ch24-protocol-phase

**Objective.** A reader can apply the challenge protocol in the right phase without expanding an implementation beyond its agreed page.

**Behaviour.**
* While defining a delivery, the protocol's questions and proposed improvements go into the page for review; no protocol turn authorizes code before `/apply`.
* After `/apply` produces its first result, a missed requirement already on the page is corrected in that delivery and proved before it closes.
* If turn 4 suggests a new capability, such as reservations added to lending, it becomes a queue line with a draft when needed; it follows `/propose` and a fresh `/apply`, rather than being silently built into the open delivery.
* A challenge to a claimed limit stays a check of the agreed result; any discovered change outside that result follows the same new-line rule.

**Contract.** `book/en/24-asking-for-more.md` and `book/pt/24-asking-for-more.md`, The challenge protocol, explanations of turns 1 to 4 and matching opening/key points.
Keep the experiment's four quoted turns verbatim and its measured results unchanged: they are historical evidence, not permission to bypass the delivery scope.
Place the phase instruction immediately beside the reusable protocol so a reader copying it sees the boundary.
Sources: docs/05 §§2 to 4, chapters 12 and 13, and `work/done/ask-for-more-experiment.md` with `work/done/ask-for-more-experiment-run/` for the protocol as measured.
Decision from docs/06: improvements that satisfy the page stay; new capabilities become lines.
No new concept; the existing Case A opening remains unchanged.

**States.** Inapplicable: chapter prose, no new screen.

**Visual reference.** Inapplicable: the existing book layout.

**Out of scope.** Repeating or rewriting the experiment, changing its quoted prompts, and altering the Case A story: scope is the protocol's phase and authority.

**Done when.**
* [ ] A reader can classify a missing agreed requirement and a new capability correctly in both editions; the prompt to add what is worthwhile has an adjacent scope boundary.
* [ ] The four experimental messages and numerical results are unchanged; if any private-case passage must change, list it here and obtain the author's approval under docs/00 OD-3 before completion.

* [ ] Both editions say the same thing, using docs/03's terms and Portuguese example names.
* [ ] The opening states the reader's value and the gain is supported; no filler added or useful explanation cut; every number and quoted artifact has its source (docs/00 and docs/04).
* [ ] `make verify` and `make book` pass; the author receives `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf` for the passage checks (docs/05 §5).
