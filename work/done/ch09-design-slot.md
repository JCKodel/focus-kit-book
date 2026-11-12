# ch09-design-slot

Built before the author read it: the author asked for the whole queue to be run, each page decided alone and built in the same session (docs/05 §4, a command that says to decide alone and to build as well). Every choice the documents leave open is marked "decided by the agent, the author corrects it in the review".

**Objective.** After chapter 9 the reader, developer or not, says where each screen's design comes from before anyone builds it: the person's design tool, a design delivery whose static HTML or SVG mock they approve, or a prototype by choice, as the project's Design slot says; knows that a page with a screen and no reference is not `[>]` unless the slot says prototype, and that `/apply` compares what it built with the reference; writes a first milestone with `· after` and its review `· after all`, with no token; and knows, from chapters 12 and 13, that what `/apply` records on a page goes under `## Outcome`, below Done when.

**Behaviour.** What the reader can do or explain afterwards:

* Name the Design slot's three forms (the person's design tool and its export; a design delivery, a queue line before the screen's line whose deliverable is a static HTML or SVG mock the person opens and approves, kept in `docs/ui/` unless the slot says otherwise; a prototype, no reference, by choice), and "no screens" for a project without any.
* Say the defaults: `/brainstorm` asks it inside the subject of the process slots, default a design delivery for a product and a prototype for a tool; `/analyze` asks it as one of seven subjects, default what exists, named.
* Failure: asked "the lending screen has no design yet and the Design slot says design delivery; may `/propose lend-book` mark the page `[>]`?", answer no: the screen gets its reference first, as the slot says; with "prototype, by choice" in the slot, yes.
* Say why: an agent asked for a screen with nothing to follow builds a plausible one and approves its own choices; on Ninjobs, whose process said from its first day that a screen with no design is designed first, never improvised, a delivery that compared the screens with their designs caught phone layouts stretched across a desktop window.
* Say what `/apply` does with a reference: it compares what it built with it and corrects or justifies each divergence on the page.
* Write `/brainstorm`'s first milestone as the kit asks: one line each, `· after` on a line that needs another first, then the review, `· after all`; no two letters after the slug.
* Count the kit's slots in docs/05 §5 as eleven, the Design slot among them (chapter 7).
* Say where `/apply` writes what happened on a page: under a heading `## Outcome` below Done when, so the definition above stays as it was read (chapters 12 and 13).
* In the Portuguese edition, the same, with docs/03's Portuguese terms and the slot names in English, as "o slot Delivery review" already is.

**Contract.** Eight chapter files and one document, line numbers en at HEAD `e8e5673`; pt follows en sentence for sentence. The text is the agent's within these changes.

* **ch09** (`book/en/09-starting-a-project.md`, `book/pt/09-starting-a-project.md`)
  * C1, opening (:3-4): the reader also says where each screen's design comes from before anyone builds it.
  * C2, subject 5 (:22): how a screen is proven and where its design comes from.
  * C3, subject 6 (:23): `· after` on a line that needs another first, then its review, `· after all`; the parallel token's clause and its pointer go (handed to this line by `ch11-14-after`'s Out of scope, "Chapters 8, 9, 17 and 20: their M33 lines").
  * C4, a new subsection `### Where a screen's design comes from` after the review question (:31): why (the agent approving its own plausible screen); the Design slot's three forms and "no screens"; `docs/ui/`; the defaults; a page with a screen and no reference not `[>]` unless the slot says prototype, the page's Visual reference naming it; `/apply` comparing, correcting or justifying each divergence; Ninjobs' rule and the delivery that caught phone layouts stretched across a desktop window, as the error the rule prevents; this book's own slot, prototype by choice (ADR-0019), as a real example.
  * C5, `/analyze`'s round (:81-88): seven subjects; a new sixth, where a screen's reference comes from, default what exists, named; the milestone, seventh, with `· after` and `· after all`.
  * C6, the team gain (:133-134): one sentence, no screen built from nothing.
  * C7, key point 1 (:138): the screen's design before its page is complete. Still five key points (docs/04).
* **ch07** (`07-the-documents.md`, both editions)
  * C8 (:45, :50, :178): eleven slots, "where a screen's design comes from" listed before how a screen is proved; pt "onze".
* **ch12** (`12-propose.md`, both editions)
  * C9 (:49): Visual reference: a screen whose design does not exist yet gets one as the Design slot says, before the page is `[>]`, with a pointer to chapter 9 (the first in ch12).
  * C10 (after the list, :51): what `/apply` records goes under `## Outcome` below Done when, so the definition above stays as it was read.
* **ch13** (`13-apply.md`, both editions)
  * C11 (:112): "writes into the page what happened, under a heading `## Outcome` below Done when, ...".
* **docs/03**: a new row, design delivery, entrega de design, `docs/ui/` (added by this /propose, as the skill says).

Terms of docs/03: slot, page, delivery, mark, queue line; new: design delivery. Sources: the kit's `SETUP.md` at 2026.11.12 (Design slot, `/brainstorm` subject 5 and 6, `/analyze`'s round, docs/05 §3's Visual reference and Outcome), the kit's `CHANGELOG.md` 2026.10.25, Design bullet, for the Ninjobs rule and the delivery that caught the stretched layouts; this repository's ADR-0019. No source note: the kit is taught as it is, and Ninjobs is a private case (docs/04). Cases: Ninjobs only, paraphrased from the changelog; no number.

**States.** Inapplicable: chapters, no screen.

**Visual reference.** Inapplicable: no screen, and no new kind of content (a bulleted list and prose); the Design slot of this repository says prototype, by choice (ADR-0019).

**Out of scope.**

* The changelog's story of how the rule left and came back: the book teaches the kit as it is (docs/04).
* Chapter 8's update example and the numbering map line: `ch08-update-2026-10-25`.
* Chapter 13's lend-book walk-through at :148 and chapter 12's gain at :188: they say "what happened" and stay true; C10 and C11 say where it goes.
* The rest of `/brainstorm`'s subject 5 as the kit writes it now (the verify ceiling, the publish policy): not this line's subject.

**Done when.**

* [x] C1 to C11 read as the Contract says in both editions; no "token" or two letters left in ch09.
* [x] Both editions written; each chapter opens with its value; no filler and nothing useful cut; no number added; no em dash; no run narration.
* [x] Ninjobs paraphrased from the changelog only: no slug, path, file or number of its repository; the disclosure scan green.
* [x] `make verify` green after the last edit.
* [x] `make book` builds both editions, both PDF paths recorded.
* [x] Delivery review by one read-only Opus agent, as docs/05 §5 says; only this delivery's paths and its docs/06 line staged; the page in `work/done/` and its commit message suggested.

**Decisions.**

* Decided by the agent, the author corrects it in the review: the `## Outcome` heading is taught in chapters 12 (the page's format) and 13 (what `/apply` writes), where the page and its record are taught, though the line says chapter 9, which teaches neither.
* Decided by the agent, the author corrects it in the review: chapter 7's count of slots, ten, becomes eleven in this delivery, since the Design slot is this line's subject and the count is wrong without it.
* Decided by the agent, the author corrects it in the review: the delivery that caught the stretched layouts is told without its slug, `chassi-desktop`, as chapters 12, 13 and 15 tell Ninjobs' deliveries; the slug is Portuguese and says nothing to the English reader.
* Decided by the agent, the author corrects it in the review: the Ninjobs passage holds only what the kit's changelog says of it (the rule from its first day; a delivery catching phone layouts stretched across a desktop window), no number and no detail of the delivery's page.
* From the documents: the slot's forms and defaults (the kit's `SETUP.md`), the token's removal in ch09 (`ch11-14-after`'s Out of scope), the book's own slot (ADR-0019).

## Outcome

* Built as the Contract says, C1 to C11, in both editions, with the docs/03 row added by /propose; the Design subsection sits in ch09 after the review question, `/analyze` asks seven subjects, chapter 7 counts eleven slots.
* Diverged from Behaviour: the reason the chapter gives is that a screen built with nothing to follow is the agent's guess, which its proof can only compare with itself, not that the agent "approves its own choices", a wording that came from no source the page names; the Ninjobs passage keeps to the changelog's words (the rule from its first day, a delivery catching phone layouts stretched across a desktop window), with no "never improvised" and no detail of the comparison.
* Delivery review: one read-only agent on Opus (model set at launch, Explore type) read the page, docs/04, `AGENTS.md`, the diff of the nine paths and this line's docs/06 hunk, the kit's `SETUP.md` and `CHANGELOG.md` 2026.10.25, and ADR-0019; its report says it consulted the advisor once. Nine candidates:
  * 1, ch09 :44: "whatever the form ... unless prototype" contradicted itself; fixed: "Unless the slot says prototype, a delivery's page ...".
  * 2, ch09 :44: Visual reference and `[>]` not taught before chapter 9; fixed: `[>]` glossed "ready to build", the chapter's one pointer to chapter 12 moved from :81 to the Visual reference.
  * 3, ch09 :46-47: the Ninjobs passage said more than the changelog; fixed as above.
  * 4, pt ch09 :46: "dizia" implied the rule had ended; fixed: "diz", en "has said".
  * 5, ch09 :35: the reason not in the sources; fixed as above.
  * 6, ch09 :152, :156: prototype listed as where a design comes from; fixed: the gain says "unless the team chose to prototype", the key point "from your tool or a design delivery ..., unless the slot says prototype".
  * 7, pt ch09 :39: "produto" for deliverable; fixed: "resultado".
  * 8, docs/03 :25: the page's row ended at Done when; fixed: "after /apply, what happened under `## Outcome` below it" (in what this delivery changes: the Outcome heading).
  * 9, pre-existing double pointers in ch09: a note below.
* Proof: `make verify` green, 13.6 seconds on 2026-11-12; `make book` at HEAD `e8e5673` with this delivery's changes in the tree: `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`. No slow tests (docs/05 §5).
* Environments: local builds both; GitHub Pages and the Release unchanged until the author pushes or tags.

## For the review

* book/en/09-starting-a-project.md:30 and :103 (pt the same lines) both point to chapter 15, and pt :128 points to chapter 17 where en :128 does not: a reader meets the same pointer twice, and the editions differ (docs/04, Chapter pointers). Older than this delivery.

```commit
docs(ch09-design-slot): teach the Design slot and the Outcome heading

- ch09: the Design slot's three forms, the design delivery, a page
  with a screen not [>] without a reference, Ninjobs' rule
- ch09: /analyze asks seven subjects; the first milestone with after
  and after all, no token
- ch07: eleven slots; ch12 and ch13: Visual reference and ## Outcome
- docs/03: the design delivery row; the page row with its Outcome

work/done/ch09-design-slot.md
```
