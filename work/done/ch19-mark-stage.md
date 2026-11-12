# ch19-mark-stage

Built before the author read it: the author asked for the whole queue to be run, each page decided alone and built in the same session (docs/05 §4, a command that says to decide alone and to build as well). Every choice the documents leave open is marked "decided by the agent, the author corrects it in the review".

**Objective.** After chapter 19 the reader knows that each `/apply` stages its line of docs/06 with the kit's mark script's `stage`, which changes that line in the index and nothing else there, in one folder and in a batch's shared hunk alike, so two sessions' neighbouring lines never ride into one commit.

**Behaviour.** What the reader can do or explain afterwards:

* Say how a session stages its own line of the queue when the other session's line is its neighbour: with the mark script's `stage`, its `[x]` being its last edit; the script changes that line's mark in the index, one byte, and leaves every other line there as it was.
* Say why `git add -p` does not do it in that case: it splits a hunk with `s` only where an unchanged line separates two changes, and its `e` opens an editor a session does not drive.
* In one folder, after `git restore --staged docs/06-Queue.md` took the whole queue out of the index, say how this delivery's line goes back in: its session stages it again with the mark script's `stage`.
* Failure: asked "may the session write a patch of its line and give it to `git apply --cached`?", answer no: the chapter teaches no patch; the line is staged by the mark script, as chapter 14 says every mark changes.
* Edge: asked "`return-book` and `overdue-list` are neighbours, and `overdue-list`'s `/apply` already staged its `[x]`; how does `return-book`'s `/apply` stage its own?", answer: with the mark script's `stage`, and `git diff --cached docs/06-Queue.md` then shows both lines, each staged by its own session, so the commit waits until the index holds one delivery, as the chapter already says.
* Find the script's `stage` in chapter 19 where the hunk is first explained, in the one-folder sorting of the index, in the batch's section, in "When parallel stops paying" and in key point 1; find no patch and no `git apply` anywhere in the chapter.
* In the Portuguese edition, the same, with docs/03's term "script de marca".

**Contract.** Two chapter files; line numbers en at HEAD `daf31d8`; pt follows en sentence for sentence. The text is the agent's within these changes.

* **ch19** (`book/en/19-worktrees.md`, `book/pt/19-worktrees.md`)
  * C1 (:29): each session stages its own line alone with the kit's mark script's `stage`, which changes that line in the index and nothing else there (chapter 14), in place of "(the section on the batch shows how)".
  * C2 (:54): this delivery's session stages its own line again with the mark script's `stage`.
  * C3 (:369-371): the patch and `git apply --cached` removed; the `git add -p` sentence kept as the reason; the session stages its `[x]`, its last edit, with the mark script's `stage`, which changes that line's mark in the index and leaves the other lines there as they were.
  * C4 (:388): each `/apply` stages that line alone with the mark script's `stage`.
  * C5, key point 1 (:416): its line of the queue staged with the mark script's `stage`. Still five key points.
  * C6: the source note `[^git-apply]` removed, as no sentence cites it.

Terms of docs/03: mark script, stage, index, queue line; the word hunk as chapter 19 already explains it, which docs/03 holds in no row of its own. Sources: this repository's docs/05 §4 (a mark changed by `mark.sh`, `stage` when the line goes into the index), the installed `.agents/skills/propose/scripts/mark.sh` (what `stage` does), the git documentation already cited for `git add -p`. No new number, no new source note. Cases: none.

**States.** Inapplicable: a chapter, no screen.

**Visual reference.** Inapplicable: no screen, and no new kind of content; the Design slot says prototype, by choice (ADR-0019).

**Out of scope.**

* `mark.sh` refusing a second `[~]` or `[*]`: `ch12-14-mark-refused`, M35.
* A line a delivery adds to docs/06, which `stage` cannot stage since the index does not hold it yet: chapter 19 teaches no added line; docs/05 §6's selective staging covers it.
* The error of the emptied queue and the rule's reason: chapter 14 teaches them; chapter 19 points to it.
* Chapter 19's other passages on the index and the commit: they already agree with docs/05 §6.

**Done when.**

* [x] C1 to C6 read as the Contract says in both editions.
* [x] Both editions written; the chapter still opens with its value; no filler and nothing useful cut; no new number; no em dash; no run narration; no patch or `git apply` left in the chapter.
* [x] The disclosure scan green.
* [x] `make verify` green after the last edit.
* [x] `make book` builds both editions, both PDF paths recorded.
* [x] Delivery review by one read-only Opus agent, as docs/05 §5 says; only this delivery's paths and its docs/06 line staged; the page in `work/done/` and its commit message suggested.

**Decisions.**

* Decided by the agent, the author corrects it in the review: the `git add -p` sentence and its source note stay in the batch's section, as the reason a session needs the script for a shared hunk, said in the present (docs/04 "The kit as it is").
* Decided by the agent, the author corrects it in the review: chapter 19 names chapter 14 once, at the first mention of the script's `stage`, for what the script is and why; it does not retell the error.
* Decided by the agent, the author corrects it in the review: the one-folder sorting of the index (:54) is changed too, though the line names only "one folder" and the batch, since it is the other place the chapter has a session stage its line.
* From the documents: the rule (docs/05 §4), the script's `stage` (the installed `mark.sh`), the term (docs/03 `mark script`), the kit taught as it is with no word on the patch it replaces (docs/04).

## Outcome

* Built as the Contract says, C1 to C6, in both editions: chapter 19 stages a session's line with the mark script's `stage` at the hunk's first explanation (:29, with the link to chapter 14), in the one-folder sorting of the index (:54), in the batch's section (:370, the patch and `git apply --cached` removed), in "When parallel stops paying" (:387) and in key point 1 (:415); the `[^git-apply]` source note removed in both editions.
* Diverged: none.
* Proof: `make verify` green after the last edit, 13 seconds on 2026-11-12, under the five-minute ceiling; `make book` built `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`, with their EPUBs, after the review's fixes. No slow tests: the Verify slot names none.
* Delivery review: one read-only agent on Opus (model set at launch, Explore type) read this page, `AGENTS.md`, docs/04, docs/05 §§4 and 6, docs/03's rows, the installed `mark.sh`, chapter 14's "How a mark changes" and `git diff HEAD` of both chapter files with this line's hunk of docs/06. It confirmed `stage` run again after `git restore --staged docs/06-Queue.md` works and that "one byte" holds for the index's `[ ]`. Four candidates:
  * 1, en :29: "the kit's mark script's `stage`", a double possessive; fixed: "the `stage` of the kit's mark script".
  * 2, pt :370: the apposition between "em stage" and "com"; fixed: "coloca em stage o seu `[x]`, a sua última edição, com".
  * 3, en and pt :370: "one byte" is zero when the index already holds `[x]`; left: the sentence is the batch's first stage, where it is one byte.
  * 4, outside this delivery: chapter 19 :55 and docs/05 §6 differ on who stages the other delivery's paths again; a note below.
* Verify ran again after the fixes: green.

## For the review

* book/en/19-worktrees.md:55 and docs/05-Process.md §6 ("commits the first, and stages them again"): the chapter has the other session stage its entries again, §6 has the person do it, and a queue line goes back into the index only through the mark script's `stage`, which a session runs; the person may align §6 with §4 and the chapter in the kit or by ADR.

```commit
docs(ch19-mark-stage): stage a queue line with mark.sh in chapter 19

- ch19: each session stages its line with the mark script's stage
- ch19: the patch given to git apply --cached removed, and its note

work/done/ch19-mark-stage.md
```
