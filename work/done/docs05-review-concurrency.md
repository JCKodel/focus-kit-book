# docs05-review-concurrency

**Objective.** A session running a milestone review reads in docs/05's Milestone review slot how many review agents run at once, at most two, instead of finding the limit only on earlier review pages.

**Decided without the author.** This page was written in a batch /propose with no question asked (the author's instruction for this run); each decision names its source, so the author corrects it in the review of this page.

1. The number is two, and the limit counts every agent of the review, readers and checker. Source: `work/done/m16-review.md`, Divergence: the five readers launched at once left three with no report after 600 seconds, and the author asked for at most two agents at a time; the three areas then ran two at a time and reported in full. `m17-review` decision 5 ran the same limit.
2. Only the slot changes. A slot says what and the command, in a few lines (docs/05 §5's opening); §8's "in parallel where the host runs agents" is the kit's text filled for this project and stays: the slot narrows it for this repository.
3. The reason goes in the slot in one clause, since the governor asks every rule for the error it would have caught (docs/05 §7), and the error happened in `m16-review`.
4. Kit: `kit:` optional; the author may tell the kit that §8's "in parallel where the host runs agents" could say that a project's slot may limit how many run at once.

**Behaviour.**

* A session that reads the Milestone review slot reads that at most two of the review's agents run at a time, and why.
* Edge: a review with more areas than two queues the rest, two at a time, as `m16-review` and `m17-review` did; the slot's "one per area" is unchanged.
* Edge: the delivery review, one agent, is untouched.
* Fails, and is fixed before done: a slot that names the limit for the readers and leaves the checker out, or that names a number other than two.

**Contract.**

docs/05 §5, Milestone review slot, lines 232 to 238, exact; /apply rewraps the bullet to the file's width. After "Each launch sets its model to Opus; no other model runs the review." add: "At most two of these agents run at a time: in `m16-review` five at once left three with no report."

No new term. No chapter changes: chapter 15 teaches the lending library's review, and this limit is this repository's.

Shared files and order: this applies after `conflict-same-lines` (docs/05:142-143, :252-254) and `docs05-fourth-case-version` (docs/05:134), and before `docs05-four-cases-sentence` (docs/05:115-118). Each is another hunk; an earlier one may still be staged and not committed when this runs, so /apply stages only this delivery's hunk of docs/05 with `git add -p`, and its own line of docs/06.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Out of scope.**

* docs/05 §8's wording: the kit's text (decision 2).
* Chapter 15: teaches the library, not this repository (Contract).
* docs/03's milestone review row: it says what a review is, not how this repository runs it.

**Done when.**

* [x] The slot holds the Contract's exact sentence.
* [x] `make verify` green.
* [x] The delivery review run as docs/05 §5 says, and recorded.
* [x] Page in `work/done/`, line `[x]`, staged by hunk as the Contract says, commit message in a `commit` block, `kit:` note for the author in the final report.

**Built.** docs/05 §5's Milestone review slot holds the Contract's exact sentence after "Each launch sets its model to Opus; no other model runs the review.", wrapped onto two lines with the bullet's indent; no other sentence changed.

**Decisions at apply time.** The Contract's line numbers (232 to 238) had moved to 236 to 242 after the earlier deliveries of this batch; the text edited is the one the Contract names. No Case A or Case B passage.

**Divergences and omissions.** None.

**Proof.** `make verify` green (build, parity, em dash, prose, width, links, disclosure).

**Delivery review.** One read-only agent on Opus read this delivery's hunk of docs/05 and its line of docs/06 against this page, docs/04 and `work/done/m16-review.md`. No finding: the sentence matches the Contract, "these agents" covers the area readers and the checker, no em dash, and the reason agrees with `m16-review`'s Divergence.

**Kit note for the author.** `kit:` optional: the kit's §8 "in parallel where the host runs agents" could say that a project's slot may limit how many run at once (decision 4).

```commit
docs(docs05-review-concurrency): run at most two review agents at a time

- docs/05's Milestone review slot limits the review to two agents at once
- The reason, from m16-review, in one clause

work/done/docs05-review-concurrency.md
```
