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
* [x] A reader can classify a missing agreed requirement and a new capability correctly in both editions; the prompt to add what is worthwhile has an adjacent scope boundary.
* [x] The four experimental messages and numerical results are unchanged; if any private-case passage must change, list it here and obtain the author's approval under docs/00 OD-3 before completion.

* [x] Both editions say the same thing, using docs/03's terms and Portuguese example names.
* [x] The opening states the reader's value and the gain is supported; no filler added or useful explanation cut; every number and quoted artifact has its source (docs/00 and docs/04).
* [x] `make verify` and `make book` pass; the author receives `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf` for the passage checks (docs/05 §5).

**Built.** Both editions of chapter 24. The opening adds that the reader can say in which phase of a delivery each turn may change something, so the protocol never widens what the page agreed. Right after the copyable block of the four turns, a new paragraph, The phase decides what a turn may change: once `/propose` has written the page and before `/apply` runs, what the turns find goes into the page, which the person reviews, and no turn authorizes code (chapter 12); after `/apply`'s first result, a requirement the page holds and the result missed is a fix of this delivery, with verify and the proof run again and the page recording it; a new capability, reservations proposed by turn 4 on `lend-book` (`emprestar-livro`, `reservas`), whose page puts it out of scope (chapter 12), becomes a `[ ]` line with a draft page, `/propose` and a fresh `/apply` (chapter 13); a change turn 2's test uncovers outside the agreed result follows the same rule. Turn 4's explanation adds that inside a delivery what is worth adding now is what the page already asks for. Key points: a new bullet for the phase rule.

**Divergences.** None. The four quoted messages, the experiment's numbers and the Case A card story are unchanged; no private-case passage changed, so OD-3 approval is not needed.

**Decisions.** The boundary is prose beside the block, not a fifth line in it, so the messages stay as measured. The example uses chapter 14's existing `reservations` / `reservas` line names. The Portuguese "a verificação e a prova rodam de novo e a página a registra" repeats chapter 13's wording.

**Proof.** `git diff` of both chapter files shows the code block, the Case A section and every number untouched. `make verify` green after the last edit; `make book` is run once by the batch driver for `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`, for the author's passage checks.

**Delivery review.** A read-only agent on Opus read `git diff HEAD` of both chapter files against this page, docs/03, docs/04 and AGENTS.md; nothing blocking. Points: (1) "while `/propose` defines a delivery, send it after the agent writes the page" contradicted chapter 12, where `/propose` ends with the page written: now "once `/propose` has written the page, and before `/apply` runs, send it in that session". (2) pt "classifique ... pela página" read awkwardly: "compare com a página". (3) "is proved" left out chapter 13's record: verify and the proof run again and the page records it. (4) The reservations sentence was long and its out-of-scope claim had no source: split, with chapter 12 cited. (5) The key point left out the turn 2 rule: added. Verify ran again after the fixes.

```commit
docs(ch24-protocol-phase): say in which phase the protocol runs

- Beside the four turns: what a turn may change in each phase
- Before /apply, the turns' findings go into the page; no code
- After /apply's first result, a missed page requirement is fixed
- A new capability, like reservations, becomes a queue line

work/done/ch24-protocol-phase.md
```
