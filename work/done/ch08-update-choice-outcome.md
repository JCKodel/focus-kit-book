# ch08-update-choice-outcome

**Objective.** After chapter 8's "What an update reports" the reader reads the excerpt and the three outcomes explained after it as one account: `None` is the report's word for "no migration", so an item that matches ends in it and so does an item that differs by a recorded project choice, as the excerpt's Git item does, and the reader no longer takes that item for a match.

**Behaviour.**

* Given the excerpt (en :59-73, pt :59-75), the reader finds the Git item unchanged: "a project choice, not a migration: trunk, ADR-0010, with the Publish policy, the agent never pushes. None." It is faithful to its source: the record `work/done/kit-2026-10-20-4.md` ends that item "a recorded project choice; none" (:27, :86).
* Given the three outcomes after it, the reader finds the third saying the item names the choice, asks for no change, and ends in `None` too, so the Git item is plainly the third outcome and the word it ends with is explained.
* The first outcome, "It matches and needs nothing, and says so: `None`", stays: it remains true, `None` now reading as the word both outcomes that ask nothing share.
* The claim matches SETUP §1 step 4 at focus-kit `ffbec72`: a divergence decided and recorded with a date or an ADR "is a project choice: report it as such, with what the kit says, not as a migration".
* Edge: en :84 / pt :86, "The report gives each item one of those three outcomes", still reads true and is not touched.
* Edge: en :55 / pt :55, the trunk docs/05 that keeps its own wording until the team accepts the change, is a pending migration, not this outcome, and stays.
* Fails: the excerpt changed; any other line of chapter 8 changed; a claim the record or SETUP does not make; an em dash; a commit hash; one edition changed without the other. /apply removes it before verify.

**Contract.** Both editions, same change; English is the source (ADR-0004). Line numbers as the files are now (HEAD `93a44e6`).

`book/en/08-install-and-hosts.md`, "What an update reports", en :78:

* "Or it differs by a choice the project made and recorded with a date or an ADR, as the book's Git slot does: the item names that choice and asks for no change." becomes

  "Or it differs by a choice the project made and recorded with a date or an ADR, as the book's Git slot does: the item names that choice, asks for no change, and ends in `None` too."

`book/pt/08-install-and-hosts.md`, "O que uma atualização relata", pt :80:

* "Ou ele difere por uma escolha que o projeto fez e registrou com uma data ou um ADR, como o slot Git do livro: o item cita essa escolha e não pede mudança." becomes

  "Ou ele difere por uma escolha que o projeto fez e registrou com uma data ou um ADR, como o slot Git do livro: o item cita essa escolha, não pede mudança e também termina em `Nenhuma`."

No term of docs/03 is introduced; no source note is added (the excerpt already names its record); no case is drawn on. No line in flight touches chapter 8: `m28-claim-wording` edits chapters 13 and 19, docs/03 and ADR-0018; `ch10-12-no-implicit-hosts` chapters 10 and 12; `ch13-16-several-slugs-sessions` chapters 13 and 16; `m28-records-claims` record pages in `work/done/`. M29's `ch08-update-2026-10-20-5` will edit chapter 8 later; it is `[ ]` and waits for `kit-2026-10-20-5`.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Out of scope.**

* The excerpt itself: it paraphrases the record, which ends the Git item "none".
* The third outcome's "with what the kit says" from SETUP step 4: the excerpt's Git item does not state the kit's alternative, and the review did not see it; not this finding.
* en :55 / pt :55 and en :84 / pt :86: true as written.
* Any record page in `work/done/`, `m28-records-claims`' lane.

**Decisions taken alone.** The agent chose each one, per the batch rules; the author may correct them in review.

* The explanation changes, not the excerpt: the excerpt is a paraphrase of a real record whose Git item ends "none", and AGENTS.md wants every quoted artifact real; ending it in another word would quote what the report never said.
* One sentence changes, the third outcome; the first outcome's `None` stays as written, since it is true and the third now says the same word ends it.
* Queue line wording: no change; it names the disagreement, and fixing the explanation makes the two agree.
* `(PA)` judged `(PA)`: the definition takes nothing from a line in flight (`m28-review` is `[x]`), and the build touches only chapter 8, which no line in flight edits.

**Divergences.** None: both sentences went in word for word as the Contract writes them, at en :78 and pt :80; no other line of chapter 8 moved.

**Decisions taken by /apply.** Nothing was open. The batch rules keep docs/06 out of this lane, so the queue line's mark is the driver's.

**Proof.**

* `make verify`: green, every check passed (build, parity, em dash, prose, width, examples, links, disclosure), exit 0, before the review and again after the page's records and its move to `work/done/`.
* `make book`: run after the last verify, exit 0, on HEAD `0ada2f1` with this delivery's two chapter lines and the other lanes' uncommitted edits in the tree; the PDFs to review are `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.

**Delivery review.** One read-only Opus agent, launched by this /apply over this delivery's paths only (`git diff HEAD` of both editions of chapter 8), against this page, docs/04 and `AGENTS.md`, with `work/done/kit-2026-10-20-4.md` :27, :86 and SETUP.md §1 step 4 at focus-kit `ffbec72` for the claim. Its prompt asked for no advisor, and its reply names none. Its reply: no finding. Each edition changes one line, en :78 and pt :80, word for word as the Contract asks, and nothing else in chapter 8; the excerpt is unchanged, its Git item still ending "None."/"Nenhuma.", which the new third outcome agrees with; the record (:27, :86, "recorded project choice(s); none") and SETUP step 4 ("is a project choice: report it as such ... not as a migration") support the claim; the Portuguese list reads naturally and means the same as the English; no em dash, commit hash, run narration or private case, no docs/03 term and no source note added. It ran neither verify nor the book, being read-only.

**Done when.**

* [x] Both editions of chapter 8 changed at en :78 / pt :80 as the Contract says, and nothing else in the chapter.
* [x] The chapter still opens with its value; no filler and nothing useful cut.
* [x] The claim traces to `work/done/kit-2026-10-20-4.md` :27, :86 and SETUP §1 step 4 at `ffbec72`.
* [x] No em dash, no commit hash, no run narration; disclosure scan green.
* [x] Delivery review as docs/05 §5 says, its record saying what the agent read and whether it consulted the advisor.
* [x] `make verify` green; `make book` run, with its HEAD and tree named, and both PDF paths given.

```commit
docs(ch08-update-choice-outcome): a recorded choice ends in None too

- chapter 8: the third outcome of an update report, a recorded project
  choice, ends in None as the excerpt's Git item does; both editions

work/done/ch08-update-choice-outcome.md
```
