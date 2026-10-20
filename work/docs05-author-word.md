# docs05-author-word

**Objective.** A session that runs a milestone review finds in docs/05 §8 and docs/03's `milestone review` row what holds when the author's word gives the clause tests and the candidates' confirmation to the review's own session, so a page like m23-review's follows a rule instead of departing from one.

**Behaviour.**

* Asked, in a review's /apply, "the author will not read the PDFs: may the session answer the clauses?", the agent answers from docs/05 §8: only on the person's word, given in that review's session and quoted on its page; the session then answers each clause's test from its own reading of the passages the page names, in the PDF of both editions for a milestone of chapters, and the page records each answer as the review's, never the person's.
* With that word given for the confirmation too, the word is the person's confirmation of each candidate the checker marks seen, so each one is a finding with no further step, low ones included; latent and weak ones are dropped and listed on the page with their marks (docs/05 §8; docs/03 `finding`, "a candidate ... that the person confirms", still holds).
* With no such word on the page, nothing changes: the person tests each clause by hand and confirms each candidate before it is a finding, as §8 says today.
* The word covers the review whose page quotes it; the next milestone's review tests by hand again unless its own page quotes a new word.
* Asked what made M23's findings findings, the agent answers from `work/done/m23-review.md`'s Decisions (the author's word, "review and fixes directly") and from docs/05 §8 as this delivery leaves it.
* Fails if: a review page records a session's answer as the author's; a page skips the person's test or confirmation with no word quoted; the rule lets the word drop the checker, the PDFs of both editions, the fixed range or the `[?]` for paths not read; any chapter, skill file, other section of docs/05 or other row of docs/03 changes.

**Contract.** Two files, both English only (docs/05 §5, Documentation language); lines at HEAD `91461e3`.

1. `docs/05-Process.md` §8: a new paragraph after the paragraph at :389 to :391 ("For a milestone of chapters, testing by hand is the author reading, ..."), before :393 ("Each finding becomes a `[ ]` line ..."). No existing line moves or rewraps.

   After (new paragraph):

   ```
   On the person's word, given in the review's /apply session and quoted
   on its page, the review's session may take the tests and the
   confirmation: it answers each clause's test from its own reading of
   the passages the page names, in the PDF of both editions for a
   milestone of chapters, and the word is the person's confirmation of
   each candidate the checker marks seen, the latent and weak ones listed
   on the page as dropped. The page records those answers as the
   review's, never the person's. The word holds for the review whose page
   quotes it; the checker, the range and the `[?]` for paths not read
   stay as above.
   ```

2. `docs/03-Domain.md`, the `milestone review` row (:33), edited in place, Portuguese column and identifiers unchanged: after "each candidate the person confirms is a finding like the others." append " On the person's word, quoted on its page, the review's session may answer the clause tests from its own reading of the passages, and the word confirms each candidate the checker marks seen; the page records those answers as the review's, never the person's (docs/05 §8)." The row's closing `|` stays.

The `finding` (:35), `candidate` (:36) and `checker` (:37) rows and §5's Milestone review slot stay: the word is the person's confirmation, so "a candidate ... that the person confirms" and "once the person confirms it" still hold, and "before the person sees it" holds, since the person reads the page and commits it.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Out of scope.**

* docs/03's `finding`, `candidate` and `checker` rows, and docs/05 §§2 and 4: the queue line names §8 and the `milestone review` row; `kit-2026-10-20` (M24) edits §§2 and 4 and other docs/03 rows.
* The chapters, both editions: the book teaches the kit as it is today (`book-is-kit-today`), and this is the project's own wording in a kit section, not the kit's rule.
* The skills' `references/documents.md`: they carry the kit's template and change only by a reinstall (docs/05 §5).
* A proposal to focus-kit: the author's to raise, if wanted.
* `work/done/m23-review.md` :87 to :88: "replaces" and "departs from docs/05 §8" were true when written and stay, history kept honest.
* A new ADR: the rule is a review's procedure, owned by docs/05 §8, like the slot's model choice in `review-slot-models`.

**Done when.**

* [ ] docs/05 §8 and docs/03's `milestone review` row say what the Contract says; no other line of either file changes.
* [ ] No em dash in the changed text; `make verify` green after the last edit.
* [ ] Delivery review as docs/05 §5 says; only this delivery's paths and its hunk of docs/06 staged; the page moved to `work/done/` and its commit message suggested.

**Decisions from the documents.**

* The rule lives where the rule it qualifies lives: §8's "the person tests each clause by hand" and "a candidate the person confirms" (docs/05 §8), and the row that summarizes §8 (docs/03, `milestone review`).
* What the word gives is what m23-review's Decisions took (`work/done/m23-review.md` :87 to :88): the clause answers as the review's own, both PDFs, seen candidates as findings, latent and weak dropped and listed; nothing more (finding P4).
* docs/05 is English only, so no Portuguese text changes (docs/05 §5).

**Decisions taken alone** (the batch's driver asked for recommended answers; correct them in the review).

* The word is framed as the person's confirmation given in advance, not as a second way past it: so the `finding` and `candidate` rows, which say "the person confirms", stay true and the delivery keeps to the queue line's two places. The queue line keeps its wording. The `finding` row's "fails in the person's hands" reads loosely beside a session's test; it is left, as the line does not name it.
* §8 is kit template text (m21-review :57); the new paragraph is the project's wording, a recorded project choice this page holds, as `review-slot-models` is for §5's slot, so a later reinstall's step 4 reports it that way instead of migrating it out.
* A new paragraph, not an edit inside §8's sentences, so the template's lines stay byte for byte and the project's addition is one hunk.
* Neighbour on the same files: `kit-2026-10-20` (M24) edits docs/05 §§2 and 4 and docs/03's `free line` and `kanban board` and adds `claim` and `remote`; this line comes first in queue order, and its insertion at :392 shifts no line that page or another open page cites. Its page's "docs/05 §§3, 6 to 8 ... match since kit-2026-10-19-2; none" goes stale once this lands: its /apply should report §8's project paragraph as a recorded project choice. That page is M24's and is not edited here.
* The word is per review, not standing: m23-review's was given "for this batch", and a standing word would retire §8's by-hand test, which only the author can choose.
