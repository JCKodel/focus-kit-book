# ch15-waiting-reason

**Objective.** A reader of chapter 15 sees the review line wait with both suffixes docs/05 §8 gives it, `· resume: apply` and `· blocked: <what was read>`, in both editions. Added by `ch14-four-waits`'s delivery review (work/done/ch14-four-waits.md).

**Decided without the author.** The batch had no one to answer; each choice is the recommended one.

1. The line is answered by `ch15-review-base`, applied after it was added: the driver had folded the same gap into that page at propose time (work/done/ch15-review-base.md, Behaviour and Contract), and its delivery wrote the suffix in both editions. This page records that and changes no chapter, so the line does not wait on a second edit of the same sentence.
2. No new term, no new queue line.

**Behaviour.**

* `grep -n 'blocked: <what was read>' book/en/15-closing-a-milestone.md` finds line 74, after `· resume: apply`.
* `grep -n 'blocked: <o que foi lido>' book/pt/15-closing-a-milestone.md` finds line 75, after `· resume: apply`.
* Fails: a chapter 15 review line with `· resume: apply` and no `· blocked:` reason.

**Contract.** None: chapter 15 already holds the text since `ch15-review-base`'s commit.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Out of scope.**

* Any rewording of chapter 15: `ch15-review-base` owns it and was reviewed.

**Done when.**

- [x] Both greps above find the line, in both editions.
- [x] verify green.
- [x] Both editions already written by `ch15-review-base`; no number, no private case.

## What happened

The proof is the two greps, run after `ch15-review-base` was committed: both found the line. No chapter changed, so no delivery review had text of this delivery to read beyond this page; `make verify` was green.

```commit
docs(ch15-waiting-reason): record chapter 15's waiting reason as answered

- ch15-review-base already wrote blocked: <what was read>; both editions

work/done/ch15-waiting-reason.md
```
