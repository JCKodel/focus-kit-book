# ch19-adjacent-mark-staging

**Objective.** A reader of chapter 19 knows that the session, not the person, stages a batch's mark when it sits in one hunk of docs/06 with the marks of other lines, and how it stages only its own line without an editor: a patch with only that line's change, applied to the index with `git apply --cached`.

**Decided without the author.** This page was written in a batch /propose with no question asked (the author's instruction for this run); each decision names its source, so the author corrects it in the review of this page.

1. Who stages: the session that owns the line. Sources: docs/05 §4:140-142 and §6:257-259 (the session stages its own paths and hunks), §5 Git ("The agent stages"), chapter 19:34 and :174. The person never stages a delivery's mark; the person commits.
2. How, without an editor: `git add -p` splits a hunk with `s` only where an unchanged line separates two changes, and its `e` opens an editor, which a session does not drive. The session writes the hunk as a patch holding only its own line's change and gives it to `git apply --cached`, which applies a patch to the index alone and leaves the folder as it is (git's documentation of `git apply`, option `--cached`). Checked in a throwaway repository with git 2.56.0: two adjacent marks changed in the folder, a patch holding one of them applied with `--cached`, `git diff --cached` showed that line only and `git diff` the other.
3. The patch keeps the line's `-` and `+` next to each other, with the other lines as they stand in the index, unchanged, as context, in the file's order. Reason, found in the same check: the hunk git shows for adjacent marks lists both old lines, then both new ones; deleting the other line's `+` and turning its `-` into a space, as chapter 19:272 now says to do in the editor, leaves the own line's new text after the other line, and the index then holds the two lines swapped. So the chapter's present `e` recipe is wrong as well as manual, and the paragraph drops it.
4. The check before each commit stays (19:273) and says what to look for: `git diff --cached docs/06-Queue.md` shows one `-` and one `+` line, next to each other, for that line alone.
5. Source notes: `[^git-add]` stays for the `s` claim, its sections narrowed to "Interactive mode" since "Editing patches" is no longer cited; a new `[^git-apply]`, "Git, "git-apply", the documentation, option "--cached", accessed <the date /apply reads it>. <https://git-scm.com/docs/git-apply>", in both editions with the same key (docs/04 §Chapter shape, Source notes). /apply reads the online page and keeps the claim to what it says.
6. Not touched: the person's own unstaging of another session's entries, 19:55 (`git restore --staged -p docs/06-Queue.md`), which meets the same limit of `-p` for adjacent marks. It is outside this line's finding (R3-4 names 19:272), and these lines get no widening (docs/05 §8); the author may add it as a line.
7. Kit: `kit:` the author may tell the kit that its apply text says "selective staging for mixed files" and names no way to stage one of two adjacent lines; this repository's docs/05 §6 keeps saying what, and the chapter teaches how (docs/05 §5: a slot says what, steps go elsewhere). Nothing in docs/05 changes here.

**Behaviour.**

* A reader of chapter 19 §Proposing in a batch reads, after the sentence that the shared hunk holds no conflict, that the session staging its mark is the one that stages, and that the person does not.
* The reader learns why `git add -p` cannot do it here: `s` splits only at an unchanged line, and `e` needs an editor.
* The reader learns the way the session does it: it writes the hunk as a patch with only its own line's `-` and `+`, next to each other, the other lines unchanged as context, and runs `git apply --cached` on it, which changes the index and not the folder.
* The reader can say what to check before each commit: `git diff --cached docs/06-Queue.md` shows only that line's `-` and `+`, side by side.
* Edge: the other line's mark is already staged by its own session. The context is the index as it stands, so the other line appears with its staged mark as context, and the patch still applies (decision 3).
* Edge: a patch whose context does not match the index. `git apply --cached` refuses it and changes nothing; the session writes the patch again from `git diff docs/06-Queue.md`, which compares the folder with the index.
* No text says the person stages a mark, and no text keeps the `e` recipe, in either edition.
* The paragraph shows no run, transcript, diff or `git status` output (docs/04 §Writing the book, No runs): it names the commands and what they do.

**Contract.**

Chapter 19, `book/en/19-worktrees.md` and `book/pt/19-worktrees.md`, §Proposing in a batch, lines 272 and 273, in both editions; the Portuguese says "colocar em stage" as the chapter does, and keeps the commands as they are:
* line 272 is replaced by sentences that say, in this order: the session stages its own mark, never the person; `git add -p` splits a hunk with `s` only where an unchanged line separates two changes, and its `e` opens an editor; so the session writes the hunk as a patch with only its own line's change, its `-` and `+` together and the other lines as they stand, unchanged, and gives it to `git apply --cached`, which applies the patch to the index and leaves the folder alone.
* line 273 keeps `git diff --cached docs/06-Queue.md` before each commit and says it shows that line's `-` and `+`, side by side, and nothing else.
* Notes: `[^git-add]` cited at the `s` claim, its definition naming the section "Interactive mode" only; `[^git-apply]` cited at the `--cached` claim, defined as decision 5 says, after `[^git-add]` at the end of the file. Parity: each note cited as many times in both editions.
* No new docs/03 term: stage, hunk as the chapter defines it (19:28), queue, mark.
* No case is drawn on.

Shared files and order: `conflict-same-lines` applies first and edits the line before, 271, in both editions; this page keeps 271 as that page leaves it. `pt-librarian-masculine` (another agent) edits `book/pt/19-worktrees.md` after this one. /apply stages this delivery's hunks of both chapter files with `git add -p`, and its own line of docs/06.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Out of scope.**

* The person's unstaging at 19:55 (decision 6): not this finding.
* docs/05 §6's staging rule: says what, not how (decision 7).
* Chapter 13's staging bullets: they hold for lines far apart, the common case.
* The conflict's definition: `conflict-same-lines`.

**Done when.**

* [x] Chapter 19 lines 272 and 273 rewritten in both editions as the Contract says, `[^git-apply]` added and `[^git-add]` narrowed, in both.
* [x] The recipe checked once more in a throwaway repository outside this one at /apply: one of two adjacent changed marks staged with `git apply --cached`, the index in the file's order (`git show :<file>`).
* [x] `[^git-apply]`'s claim matches the online documentation, read at /apply.
* [x] `make verify` green, links included.
* [x] `make book`, and the paths of both PDFs given to the author.
* [x] The delivery review run as docs/05 §5 says, and recorded.
* [x] Page in `work/done/`, line `[x]`, staged by hunk as the Contract says, commit message in a `commit` block, `kit:` note for the author in the final report.

**Built.** Chapter 19 §Proposing in a batch, lines 272 and 273 of both editions, now 272 to 276: the session that owns a line stages its mark, never the person; why `git add -p` cannot (`s`, `e`); the patch holding only the own line's `-` and `+` with the other lines as context from the index; `git apply --cached`; the check before each commit. `[^git-add]` names "Interactive mode" only; `[^git-apply]` added after it; each cited once per edition. English first.

**Decisions at apply time.**

* "patch" and "index" appear in the chapter for the first time in this paragraph, so each gets a gloss at the word: the text `git diff` prints for a change; the staged copy a commit is made from (docs/04, Teach, do not only show; the index gloss from the review).
* Line 276 says "no other change" in place of the Contract's "nothing else", since `git diff --cached` also prints the unchanged context lines the patch carries (review finding).
* The Behaviour's two edges are the session's conduct, not reader text: the online `--cached` text says nothing of a refused patch, so the chapter does not claim it. Both edges were checked in the throwaway repository (below).
* Staging: the driver changed the run so that parallel sessions share the tree; this session stages nothing and the driver commits each delivery from its own index. `make book` is run once by the driver at the end, not here.
* No Case A or Case B passage.

**Divergences and omissions.** `make book` not run in this session (driver's instruction); the driver gives the PDF paths, `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.

**Proof.** Throwaway repository with git 2.56.0: three adjacent marks changed in one hunk; a hand-written patch holding only the middle line's `-` and `+`, the others as context, applied with `git apply --cached`; `git diff --cached` showed that line only, `git diff` the other two, and `git show :q.md` held the lines in the file's order. Edge 1: a second patch for another line, with the first line's staged mark as context, applied. Edge 2: the first patch, now stale, was refused ("patch does not apply") and the index stayed as it was. The online git-apply page, option `--cached`, read 2026-10-18: "Apply the patch to just the index, without touching the working tree." `make verify` green.

**Delivery review.** One read-only agent on Opus read both chapter diffs and this line of docs/06 against this page and docs/04. Three findings, fixed: "index" used without a gloss (now glossed in both editions); the Portuguese "o seu `e`" read as the reader's (now "o `e` dele"); "nothing else" contradicted the context lines (now "no other change" / "nenhuma outra mudança"). Verify run again, green. Outside this delivery: the Portuguese key point at 19:321 says "a partir do stage" where chapter 13 and the new paragraph say "índice", now the line `pt-ch19-index-word`; 19:55 is decision 6.

**Kit note for the author.** `kit:` the kit's apply text says "selective staging for mixed files" and names no way to stage one of two adjacent lines; a session can do it with a patch holding only its line and `git apply --cached` (decision 7).

```commit
docs(ch19-adjacent-mark-staging): stage one adjacent mark with git apply

- Chapter 19 says the session stages its own mark, never the person
- It drops the editor recipe and teaches a patch with `git apply --cached`
- New note git-apply; git-add narrowed to "Interactive mode"
- Both editions

work/done/ch19-adjacent-mark-staging.md
```
