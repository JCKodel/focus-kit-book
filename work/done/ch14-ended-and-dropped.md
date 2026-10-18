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
* [x] The migration is `[x]` and its rules support these scenarios before apply starts.
* [x] Both editions answer all Behaviour cases and distinguish cancelled `[x]` from built `[x]` in the marks explanation.
* [x] The changed Case A paragraph is listed here and author-approved under OD-3, with no private identifiers, source paths or new historical claim.
* [x] Both chapters open with their value, retain evidenced team gains, contain no filler or useful omissions, and every number/artifact remains sourced.
* [x] `make verify` is green and `make book` builds both editions; proof records both PDF review paths, and delivery review and archival follow docs/05.

**Built.** Chapter 14, both editions: the opening gains a third sentence (resume an ended session, record a cancelled delivery); the `[x]` row of the marks table follows docs/05 §4 ("with `· dropped:`, cancelled"; "the person, when cancelling"), with a sentence that `· dropped:` is a suffix, not a seventh mark; the free rule points to the cancelled-`after` exception; a new section, "A session that ended, a delivery cancelled" (pt: "Uma sessão que terminou, uma entrega cancelada"), before the board, teaches the `[~] reservations` and `[*] lend-book` resumption on the person's word with page, folder and index inspected, the cancellation of `print-card` (pt `imprimir-cartao`), written for the chapter, as `[x] · dropped: no printer driver`, built `[x]` against cancelled `[x]`, and the dependent `reprint-card` the person re-decides; the gain section gains one sentence on Case A's impossible request; the key points stay five (the ended/dropped bullet added, `· after` merged into the waiting bullet). The PT note on suffixes kept in English adds `· dropped:`. Chapter 23, both editions: the impossible-request paragraph.

**Case A paragraph for author approval (OD-3).** Chapter 23, "A request that could not be built was closed, not absorbed". Before: "It was closed in the queue with the reason, without being built, where it could otherwise have been dropped in silence or bent into something nobody asked for." After: "It was closed in the queue with the reason, without being built, where it could otherwise have been left in silence or bent into something nobody asked for. The kit writes such a closure as `[x]` with `· dropped: <reason>` at the end of the line, its page in `work/done/` saying what was built and undone ([chapter 14](14-queue-states.md))." The Portuguese edition the same ("largado" became "deixado"). The new sentence states the kit's present rule, not the historical line's syntax; no private identifier or new historical claim. Chapter 14's gain sentence reuses the same documented fact. Under the batch the approval itself is the author's, asked in the lane's report.

**Proof.** `make verify` green after the last edit. `make book` and the two PDF review paths are the batch driver's, which builds once at the end.

**Delivery review.** A read-only Opus agent read `git diff HEAD` of the four chapter files, the page, docs/04, docs/05 §4 and AGENTS.md. Points and answers:
* The cancellation example did not say it was written for the chapter: fixed in both editions.
* "`· dropped:` is how the queue writes that closure" could read as Case A's queue using the suffix: rewritten as "the kit writes such a closure as ..." in both.
* "By the rule above" clashed with the free rule that already names the exception: now "By the free rule alone".
* The opening said "the team cancels" where the rule says the person: fixed.
* Awkward key point and PT "é da pessoa redecidir": reworded.
* The long merged waiting bullet, a longer PT reason and a gain line for resumption: optional, left; the bullet holds the rule whole, the PT reason fits, and resumption has no evidence for a gain line.

**Decisions taken alone.** The slugs `print-card`/`reprint-card` (pt `imprimir-cartao`/`reimprimir-cartao`) for the cancelled example; the new section placed before the board; "dropped in silence" reworded to "left in silence" so the suffix's word keeps one sense; board projection of a dropped card left to `ch14-blocked-column`.

```commit
docs(ch14-ended-and-dropped): teach ended sessions and dropped lines

- ch14: resume a [~] or [*] line on the person's word
- ch14: cancelled delivery ends [x] · dropped: <reason>
- ch14: a dependent of a dropped line is the person's to re-decide
- ch23: the impossible request and how the kit writes it
work/done/ch14-ended-and-dropped.md
```
