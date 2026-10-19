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

* [x] Both editions pass every Behaviour check against the completed kit migration and use docs/03's terms.
* [x] Every affected chapter keeps its opening value and evidenced team gain; no filler, no useful content cut, and every number and artifact has a checked source.
* [x] `make verify` is green after the last covered edit, `make book` builds both editions, and the author receives both PDF paths for review.
* [x] The independent delivery review, proof and decisions are recorded under docs/05; no private passage is added, so OD-3 approval is inapplicable.

**What happened.** Both editions of chapters 8, 10, 11, 12, 13 and 17 changed where they say `/propose` runs.
Chapter 11's due-date-format example now names `/propose` without sending it to a fresh session, offers the two choices (this session, whose conversation the draft holds, or a fresh one), turns "define it now" into the first choice, and says the page must hold every decision the build needs, including what only that conversation supplied, because `/apply` starts fresh; the line still stays `[ ]` with its draft, and the key point says the same.
Chapter 12 gains one line on where `/propose` runs and where the page is read and corrected, its exploration ending names both choices, and its key point says the page is read in the session that wrote it.
Chapter 13 says `/apply` always starts fresh even when `/propose` ran in the asking conversation; chapter 17's manager answer names `/propose` for that session, out of plan mode, or a fresh one; chapter 8 keeps the Claude Code and Codex forms and adds that `/apply` starts fresh in every host.
Chapter 10's step 2 no longer says the agent names `/propose` "in a fresh session", which the brainstorm command does not say.

**Contradiction check.** The completed kit-2026-10-18-1 migration agrees with this page: docs/05 §2, docs/03's draft page row and AGENTS.md all allow `/propose` in the asking session or a fresh one and keep `/apply` fresh. Nothing contradicts the Contract.

**Divergences.** Chapter 9's handoff and chapter 10's steps 4 (new project) and 5 (existing project) keep `/propose` in a fresh session. The Contract asked to revise them, but the source allows the same session only for the session that asked for a change outside `/apply`; the `/brainstorm` or `/analyze` session asked for none, and the kit's brainstorm and analyze commands name `/propose` with no session rule. Revising them to "this session or a fresh one" would teach a rule the source does not hold, so only the step 2 wording that contradicted the command changed. Chapter 13's "in a fresh session, run `/propose return-book`" stays: the `/apply` session did not ask for that line.

**Decisions.** The open question of chapters 9 and 10 took the sourced reading above (the author may widen it). Chapter 1's rationale and the brainstorm and analyze boundary were not touched, as the page says.

**Delivery review.** A read-only agent on Opus read `git diff HEAD` of the fourteen chapter files against this page, docs/04, docs/05 §2 and docs/03. Points: (1) chapters 9 and 10 offered the same session after `/brainstorm` or `/analyze` without a source: reverted to a fresh session (Divergences). (2) chapter 12's fresh session started "from the draft page" when there may be none: now "the documents and the draft page, when there is one". (3) chapter 11 described the fresh choice twice and said `/apply` starts fresh three times: cut to once each. (4, 5) a dangling "Choosing a fresh session" in both editions: now "If you choose" / "Se você escolher", and "pergunta" for "questão". (6) "the first session" with no second session: dropped. (7) a double "e" in the Portuguese key point: fixed. (8) chapter 17's manager session may be in plan mode: "out of plan mode" added. (9) chapter 8's long sentence: split. No passage outside the Contract still sends `/propose` to a fresh session only. Verify ran again after the fixes.

**Proof.** `make verify` green after the last edit; `make book` is run once by the batch driver for both PDFs, `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`, for the author's review. No Case A or Case B passage was added or changed.

```commit
docs(propose-same-session): let /propose run where the change was asked

- Chapter 11 offers /propose in the asking session or a fresh one
- The page holds every decision, since /apply always starts fresh
- Chapters 8, 10, 12, 13 and 17 follow; brainstorm and analyze stay fresh

work/done/propose-same-session.md
```
