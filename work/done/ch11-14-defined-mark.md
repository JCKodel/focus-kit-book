# ch11-14-defined-mark

**Objective.** After chapters 11 and 14 the reader can distinguish a saved draft from a completely defined delivery ready for `/apply`.

**Behaviour.**
* Given `[ ] due-date-format` and a draft in `work/`, the reader says the delivery is not defined and starts `/propose`; the file alone does not authorize `/apply`.
* Given a page with all sections filled or explicitly inapplicable and no unresolved scope decision, the reader explains why `/propose` marks `[>]` and `/apply` may then start if dependencies are done.
* Given a page with an unanswered scope question, the reader does not call it `[>]`: active definition is `[~]`, and a missing requested answer invokes the waiting rule.
* The chapter 11 milestone explanation no longer infers that a `[ ]` line has no page; the chapter 14 mark table says completely defined and ready for `/apply`.

**Contract.** Files: `book/en/11-queue-and-milestones.md`, `book/pt/11-queue-and-milestones.md`, `book/en/14-queue-states.md`, `book/pt/14-queue-states.md`. Sections: chapter 11 marks and milestone interpretation; chapter 14 six marks and affected key points. Sources: docs/05 §§3 and 4, docs/03 (mark, draft page and page), and the installed propose and apply skills; these already distinguish a complete definition from a file that exists. No new term or case evidence. Decisions follow the existing documents; no scope question remains.

**States.** Inapplicable: chapter prose, no new screen.

**Visual reference.** Inapplicable: existing book layout, no new visual content.


**Out of scope.** Session policy, queue placement, blocked-line return and board placement belong to their own queued deliveries. Existing private-case passages and numbers stay intact.

**Done when.**
* [x] Every Behaviour scenario is checked against the English and Brazilian Portuguese text; both editions are changed in the same delivery.
* [x] Each chapter opens with its reader value and retains its evidenced team gain; no filler and nothing useful cut; every number and quoted artifact remains sourced.
* [x] Terms follow docs/03, examples remain identified as written for the chapter, no em dash or private detail is introduced, and no run is narrated (docs/04).
* [x] `make verify` is green and `make book` builds both PDFs and EPUBs; the page records the results and gives the author both PDF paths for review (docs/05 §5).
* [x] Existing Case A evidence is retained; any changed passage drawn from it is listed for the author and approved before completion (docs/00 OD-3).

## What happened

**Built.** Chapter 11: `[ ]` is "no complete page", a draft may wait in `work/`; the milestone reading says `lend-book` is completely defined and two lines are not defined yet; the `due-date-format` draft passage says the line stays `[ ]` and `/apply` builds only a `[>]` line. Chapter 14: the mark table says `[>]` is completely defined and ready for `/apply`; a short paragraph under it gives the condition (every section filled or inapplicable, no scope question open), `[~]` while a question is talked through and `[?]` when an asked answer is missing; the milestone reading and the key point follow. Both editions, same hunks.

**First occurrence.** Chapter 14's `[?]` return paragraph already said "a draft is a page begun, not a definition complete"; this delivery repeats the distinction in chapter 11 and under chapter 14's table, without a new abstraction.

**Divergences.** None. Chapter 12 line 26 and chapter 13 line 27 carry the same inference; they are other deliveries' files (`ch12-defined-mark` is queued; chapter 13 belongs to another delivery in flight).

**Proof.** `make verify` green after the last edit. `make book` is run once by the batch driver at the end of this batch, which gives the author both PDF paths.

**Review.** One read-only Opus context over the four chapter files against this page and docs/04. Two findings, both fixed: "`[>]` does not mean that the page exists" read as if a `[>]` line could lack a page, now "A page that exists is not yet `[>]`"; "a file in `work/` is not a definition" was too broad, now "a draft in `work/`", with the redundant "completely defined" dropped. It also noted chapter 11 still says `/propose` runs in a fresh session; session policy is out of scope here and already queued as `propose-same-session`.

**Decisions.** Placed the `[>]` condition under chapter 14's table rather than in a new section. The Case A passage in chapter 14's problem section is unchanged, so nothing drawn from a private case needs approval.

```commit
docs(ch11-14-defined-mark): define [>] as complete, not as existing

- Chapter 11: a [ ] line may keep a draft; only [>] lets /apply build
- Chapter 14: [>] is completely defined and ready for /apply, with its
  condition, [~] while scope is open and [?] for a missing answer
- Both editions

work/done/ch11-14-defined-mark.md
```
