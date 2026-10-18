# ch14-ended-and-dropped

**Objective.** After chapters 14 and 23 the reader can resume an interrupted session and record a cancelled delivery without confusing either with waiting or successful implementation.

**Behaviour.**
* Given `[~] reservations` after its session ends without recording a blocker, the mark stays `[~]`; on the person's word that the session ended, propose inspects the page, tree and index and resumes. A different session does not infer abandonment from the mark alone.
* Given `[*] lend-book` after a connection loss, apply follows the same explicit resumption rule, preserving the build and index ownership rather than resetting the line to undefined.
* Given a delivery the person cancels as impossible, refused or no longer wanted, it becomes `[x]` with `· dropped: <reason>`; its page in `work/done/` states what was built and undone, including when nothing was built.
* Given a dependent line whose `after` names a cancelled delivery, the person re-decides it; the dropped predecessor does not prove that its promised capability exists.
* Reading Case A's impossible request in chapter 23, the reader understands its documented closure and how the current kit represents cancellation, without being told that this exact current suffix appeared in the historical artifact.

**Contract.** Files: both editions of `14-queue-states.md` (marks, interruption, cancellation and key points) and `23-adoption.md` (impossible-request paragraph). Source: focus-kit SETUP.md 2026.10.18.1 template docs/05 §4, pinned in `work/kit-2026-10-18-1.md`; the migration owns docs/05, docs/03 and ADR alignment. The exact current suffix is `· dropped: <reason>` on `[x]`; retain the line and archive its page. Use lending-library illustrations explicitly written for the chapter. Case A remains a paraphrase of the already documented closure, not a quotation or claim about its original syntax. No new term beyond the migrated domain, data schema or API.

**States.** Inapplicable: prose explaining queue states, no new screen.

**Visual reference.** Inapplicable: existing layout.

**Out of scope.** Waiting resumption belongs to `ch14-back-to-open`; board projection to `ch14-blocked-column`; no cancelled real queue item, historical artifact rewrite or additional private evidence.

**Decisions.** The user authorized definition against the migration's contract before implementation; apply still waits for `kit-2026-10-18-1`. Distinguishing the historical event from the current rule avoids inventing source evidence. Author approval of the changed anonymized passage remains an apply acceptance check under docs/00 OD-3, not an unanswered scope decision.

**Done when.**
* [ ] The migration is `[x]` and its rules support these scenarios before apply starts.
* [ ] Both editions answer all Behaviour cases and distinguish cancelled `[x]` from built `[x]` in the marks explanation.
* [ ] The changed Case A paragraph is listed here and author-approved under OD-3, with no private identifiers, source paths or new historical claim.
* [ ] Both chapters open with their value, retain evidenced team gains, contain no filler or useful omissions, and every number/artifact remains sourced.
* [ ] `make verify` is green and `make book` builds both editions; proof records both PDF review paths, and delivery review and archival follow docs/05.
