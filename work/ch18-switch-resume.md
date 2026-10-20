# ch18-switch-resume

**Objective.** After chapter 18 the reader can say, from the `lend-book` example, that `/propose` switches to an existing branch only when the definition resumes, as the chapter's sentence two lines above and chapter 12 :28 say.

**Behaviour.** What the reader can do or explain after the chapter:

* Read chapter 18 :27 and say that `git switch lend-book` replaces the example's first two lines when the definition resumes, and only then.
* Read :25 and :27 together and find the same condition in the same words: "when the definition resumes", "quando a definição é retomada".
* Follow chapter 12 :28 and find the same sense: a branch already there means the line is taken, unless the definition resumes.
* Edge: no sentence of chapter 18 reads as if an existing branch were reused whatever the line's state.
* Edge: chapter 19 :179, as ch18-19-fetch-resume left it, keeps agreeing with chapter 18.

**Contract.** One chapter, same change in both editions, against the files as they are today (en and pt line numbers match). One sentence per line, as the chapter is laid out; nothing else in chapter 18 changes, and no line is added or removed.

* `book/en/18-git-essentials.md` :27: "`git switch lend-book` instead when the branch exists," becomes "`git switch lend-book` instead when the definition resumes,". The rest of the sentence stays.
* `book/pt/18-git-essentials.md` :27: "`git switch emprestar-livro` no lugar delas quando o branch existe," becomes "`git switch emprestar-livro` no lugar delas quando a definição é retomada,". The rest of the sentence stays.
* Terms of docs/03: branch, claim, remote. No new term; no docs/03 row.
* Sources: the finding, `work/done/ch18-19-fetch-resume.md` (Delivery review, finding 1); chapter 18 en/pt :25 ("reuses it when the definition resumes", "o reutiliza quando a definição é retomada"); chapter 12 en/pt :28 ("reused when the definition resumes", "reutilizado quando a definição é retomada"). No footnote: the reader gains nothing to open.
* Cases: none. No number.
* Neighbouring lines on the same file: M27's `ch12-14-18-several-slugs` (chapters 12, 13, 14 and 18), later in queue order, finds :27 as this delivery leaves it. The lines proposed beside this one under m24-review (`ch07-review-merge`, `docs03-free-line-held`, `m24-records-proof`, `m24-records-crossrefs`) do not touch chapter 18.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no visual change.

**Out of scope.**

* Chapter 18 :25 and chapter 19 :179: already carry the resume condition (ch18-19-fetch-resume).
* Chapter 12 :28: the source of the condition; no edit.
* The record page `work/done/ch18-19-fetch-resume.md`: its finding already says a new queue line was to be added; no edit.

**Decisions from the documents.**

* Finding 1 of `work/done/ch18-19-fetch-resume.md`'s Delivery review: chapter 18 :27 carries no resume condition.
* The wording is chapter 18 :25's and chapter 12 :28's: "when the definition resumes", "quando a definição é retomada" (the author's brief for this line).
* Taught as the kit is today, with no version or "now": AGENTS.md.

**Decisions taken alone.**

* "when the branch exists" is replaced, not kept beside the new condition: the definition resumes only on a branch that exists (:25, "reuses it"), and `git switch` without `-c` already shows the branch is there; keeping both would lengthen a long sentence for no gain.
* No sibling sentence widens the scope: chapter 18 has no other sentence on reusing a branch.
* The queue line keeps its wording.

**Done when.**

* [ ] Both editions changed in the clause the Contract names, and nowhere else in chapter 18.
* [ ] `grep -n "instead when the branch exists\|no lugar delas quando o branch existe" book/*/18-git-essentials.md` prints nothing.
* [ ] No sentence of chapter 18 reads as if an existing branch were reused whatever the line's state.
* [ ] The chapter still opens with its value; no filler, nothing useful cut; one sentence per line kept.
* [ ] No version, date, before/after or narration of a run in the text; no em dash; no number added, no private case used.
* [ ] `make verify` green after the last edit, its result recorded in this page's Proof.
* [ ] `make book` built both PDFs, its run and both PDF paths recorded in this page's Proof; when a batch's driver runs it instead, this item is ticked only on that run as the Proof records it.
* [ ] The Delivery review as docs/05 §5 says, recorded on this page with who read what.

**Proof.**

**Divergences.**

**Delivery review.**

```commit
docs(ch18-switch-resume): switch to the branch only when the definition resumes

- ch 18: the lend-book example's git switch says when the definition resumes
- both editions

work/done/ch18-switch-resume.md
```
