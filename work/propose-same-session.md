# propose-same-session

**Objective.** The reader can invoke propose in the conversation that requested a change or in a fresh session, then invoke apply in a fresh session from a complete page.

**Behaviour.**

* After requesting due-date-format outside apply, the person gets its queue line, optional draft and the host-specific propose command; the first answer still stops without implementation.
* Naming propose in that same conversation is allowed; its page captures every decision the later apply needs, including what only the conversation supplied.
* Choosing a fresh proposal session instead uses the saved draft and documents without repeating settled questions; neither choice makes a draft a completed proposal.
* Reading and correcting the page happens in the proposal conversation; apply always starts fresh, after the page is complete and the person has read it.
* Installing the kit still leads to brainstorm or analyze in a fresh session; allowing same-session propose does not change that distinct boundary.

**Contract.** Edit both editions of `08-install-and-hosts.md`, `09-starting-a-project.md`, `10-quick-guide.md`, `11-queue-and-milestones.md`, `12-propose.md`, `13-apply.md` and `17-project-as-assistant.md`, only their proposal-session instructions and corresponding summaries.
Source: SETUP.md docs/05 template §2 and propose/apply templates; dependency migrates docs/05 and docs/03’s draft-page definition.
Replace chapter 11’s explicit rejection of “define it now” with the two allowed choices and the requirement to persist decisions; revise quick-guide proposal steps, chapter 9’s handoff and chapters 12/17’s exploratory-conversation handoffs.
Keep chapter 8’s host-specific command forms and clarify that its existing fresh apply example remains mandatory.
Use docs/03’s fresh session and draft page terms; no new concept or schema.

**States.** Inapplicable: prose, no new screen.

**Visual reference.** Inapplicable: existing chapter layout.

**Out of scope.** No automatic skill invocation, immediate implementation after an ordinary request, changes to brainstorm/analyze session rules, or changes to chapter 1’s rationale for separating deciding from building.

**Definition decision.** The author authorized defining this page before its dependency completes, using `work/kit-2026-10-18-1.md` as the contract.
The queue retains `after kit-2026-10-18-1` as an implementation gate; apply first checks the completed migration against this contract and reports any contradiction.
Source is the local working copy of focus-kit SETUP.md 2026.10.18.1, not its older HEAD; the installation page owns its fingerprint.
No implementation or staging occurs during this proposal.

**Done when.**

* [ ] Both editions pass every Behaviour check against the completed kit migration and use docs/03's terms.
* [ ] Every affected chapter keeps its opening value and evidenced team gain; no filler, no useful content cut, and every number and artifact has a checked source.
* [ ] `make verify` is green after the last covered edit, `make book` builds both editions, and the author receives both PDF paths for review.
* [ ] The independent delivery review, proof and decisions are recorded under docs/05; no private passage is added, so OD-3 approval is inapplicable.
