# docs05-review-checker

**Objective.** Whoever reads docs/05 §5's Milestone review slot learns that the readers and the checker of the deep review are read-only agents on Opus, each keeping the session's advisor, Fable, as the author runs it, and no longer an agent on Fable. Found by `m15-review` (work/done/m15-review.md, K3: "the slot names a checker on Fable; the author runs the review on Opus with the host's advisor on Fable. Seen.").

**Decided without the author.** The batch had no one to answer; each choice is the recommended one.

1. Whether the finding still holds after `kit-2026-10-17`: yes. That delivery added the Delivery review slot and rewrote §7 and §8, but left the Milestone review slot whole and gave its checker wording to this line (work/done/kit-2026-10-17.md, Contract and Out of scope). docs/05:233-235 still reads "An agent on Fable checks each candidate ... Each launch sets its model". So what remains is the slot's last two sentences; its first sentence (word, range, base, areas, Opus readers) stays. Source: docs/05 §5 as it stands, the kit page.
2. What the slot says about the advisor: the author's own words of m15-review (work/done/m15-review.md:75), "Opus running with the host's advisor set to Fable ... an Opus agent launched from this session has the advisor tool", in the Delivery review slot's phrasing, "which keeps the session's advisor" (docs/05 §5), so the two review slots read alike. Fable is named once, because the queue line asks the slot to name it and the review's model is a decision the author recorded, unlike the Delivery review's, which names no advisor model. Known author preference: never a `model: "fable"` agent, never Sonnet. Source: docs/06 line, m15-review, docs/05 §5 Delivery review.
3. The checker is one more read-only agent on Opus, not the review's session. docs/05 §8 allows either ("One checker, an agent or the review's session"); m15-review ran it as an Opus agent with that advisor, and an agent keeps the checking out of the context that will record the findings. Source: docs/05 §8, work/done/m15-review.md:75.
4. "Each launch sets its model; no other model runs the review." becomes "Each launch sets its model to Opus; no other model runs the review.": the rule stays (no substitute model, `review-slot-models` decision 2's "each launch sets its model by name"), and only the name changes. The advisor is the session's and is not set per launch. Source: work/done/review-slot-models.md, Behaviour; docs/05 §5 Delivery review ("No other model runs it").
5. No other document changes. docs/03's `milestone review` row says "one checker" with no model, still true. docs/05 §7 ("the reviews' readers and checker") and §8 name no model. No chapter names Fable or the advisor (`grep -rn -i -e fable -e advisor book` finds nothing), so the both-editions rule does not apply; chapter 15's slot is the lending library's and chapter 8's quotes the kit's update report (`review-slot-models` decision 7). Source: docs/03, docs/05 §§7-8, the grep.
6. When the advisor is missing: the review does not start and the line waits as `[?]` with `· resume: apply · blocked: deep review advisor unavailable`, the shape of `review-slot-models`' "deep review models unavailable" (work/done/review-slot-models.md, Behaviour). No agent can see from inside which advisor the session has, so the author confirms it before giving the word; that Behaviour line is the author's manual check, not a test. Source: docs/05 §4, `review-slot-models`.
7. docs/03 and docs/06: no new term ("advisor" is a host setting, like "Opus", not the book's vocabulary, as `review-slot-models` decision 7 said of the models; the Delivery review slot already uses the word with no row) and no split: one slot, one page.

**Behaviour.**

* Reading docs/05 §5 after this delivery, the Milestone review slot reads exactly the Contract's text: the readers on Opus, one per area; one more read-only agent on Opus as the checker; every agent keeping the session's advisor, Fable; each launch setting its model to Opus.
* `grep -n "Fable" docs/05-Process.md` finds one line, inside the Milestone review slot, and it names Fable as the session's advisor, not as an agent's model; `grep -n "An agent on" docs/05-Process.md` finds nothing.
* Every other slot of §5, the Delivery review included, and §§7 and 8 read byte for byte as before.
* In the next milestone review's /apply, on the author's word, the session launches the readers and then the checker, each with its model set to Opus, from a session whose advisor is Fable; no agent is launched with Fable or any other model as its model.
* Fails: the session's advisor is not Fable, or a launched agent has no advisor tool: no agent runs on a substitute, the review does not start, and the review line waits as `[?]` with `· resume: apply · blocked: deep review advisor unavailable` (docs/05 §4; the same shape `review-slot-models` gave a refused model).
* Fails: a slot that still names "an agent on Fable" or a launch whose model is Fable.
* Edge: no file under `book/`, no chapter, docs/03, docs/05 §§7 and 8, and no kit file changes.

**Contract.** docs/05 §5, the Milestone review slot, from `* **Milestone review:**` to the line before `* **Git:**`, replaced by:

```
* **Milestone review:** on the author's word in the review's /apply
  session, read-only agents on Opus read `git diff <base>..HEAD`
  against the commit the review's page names, one per area it touches:
  the build, the chapters, the kit's skills, the documents. One more
  read-only agent on Opus checks each candidate against the file before
  the author sees it. Every agent keeps the session's advisor, Fable.
  Each launch sets its model to Opus; no other model runs the review.
```

No docs/03 term and no queue line to add.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Out of scope.**

* The Delivery review slot: already Opus with the session's advisor (`kit-2026-10-17`).
* docs/05 §§7 and 8, and the kit's slot template: the kit's text; they name no model.
* docs/03: decisions 5 and 7.
* Chapters, both editions: none names the checker's model; `ch15-review-by-areas` and `ch16-review-agents` teach the review as the kit has it.
* `work/done/review-slot-models.md` and `work/done/m15-review.md`: history, not edited.

**Done when.**

* [x] docs/05 §5's Milestone review slot equals the Contract's fenced block, byte for byte (`cmp` of the block extracted from this page and the slot extracted from docs/05).
* [x] `grep -n "Fable" docs/05-Process.md` finds only the slot's advisor sentence; `grep -n "An agent on" docs/05-Process.md` finds nothing.
* [x] `git diff --cached --stat` holds only docs/05, this page's move to `work/done/` and this line's hunk of docs/06 (docs/05 §6).
* [x] The Delivery review ran on this delivery's paths, as docs/05 §5 says, and the page records it.
* [x] `make verify` green; no em dash on this page or in the slot.
* [x] Page in `work/done/`, line `[x]`, staged by its paths and its hunk of docs/06; commit message in a `commit` block.

**Divergences.** None.

**Decisions taken in /apply.**

1. The review's first finding, that the slot does not say the review does not start when the advisor is missing, needs no change and no line: the Contract fixes the slot byte for byte, decision 6 makes it the author's manual check, and docs/05 §4's `blocked:` form already holds the waiting line, as it does for `review-slot-models`' refused model. Recommended option, no question asked (batch run).

**Proof.**

* `cmp` of the Contract's fenced block and the slot extracted from docs/05 (from `* **Milestone review:**` to the line before `* **Git:**`): identical.
* `grep -n "Fable" docs/05-Process.md`: line 235 only, "Every agent keeps the session's advisor, Fable."; `grep -n "An agent on" docs/05-Process.md`: nothing.
* `git diff --cached docs/05-Process.md`: the slot's last three lines become four; the Delivery review slot and §§7 and 8 unchanged.
* `make verify`: green (build, parity, em dash, prose, links, disclosure).
* No file under `book/` changed, so no `make book`.

**Review.** A read-only Opus agent read this delivery's diffs against the page and docs/04 (docs/05 §5). Nothing breaks the page or docs/04: the slot matches the Contract byte for byte, Fable appears only as the session's advisor, and the slot agrees with the Delivery review slot, §§7 and 8 and docs/03's `milestone review` row. One low finding, the missing "does not start" clause, is answered by decision 1 above. Two notes, both handled: the Done when items were ticked at the end, and only this line's hunk of docs/06 is staged. No new queue line.

```commit
docs(docs05-review-checker): name the milestone review checker on Opus

- the checker is one more read-only agent on Opus, no longer on Fable
- every review agent keeps the session's advisor, Fable
- each launch sets its model to Opus; no other model runs the review
work/done/docs05-review-checker.md
```
