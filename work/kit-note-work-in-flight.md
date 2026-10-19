# kit-note-work-in-flight

**Objective.** After this delivery the author, taking `work/kit-proposals.md` to focus-kit's repository, reads in item 13 that the kit's /propose reads "the deliveries in flight in `work/`" while, with a branch or a worktree per delivery, those pages sit on their branches and not in the main branch's `work/`, and what the next version says instead. Found by `m22-review` (work/done/m22-review.md, findings table: candidate 2, "`work/` for the deliveries in flight", while off trunk their pages sit on their branches, chapter 12 line 25 and chapter 19 line 288, the kit's propose skill having the same words; candidate 18, `work/done/ch12-free-lines-branches.md` line 37 sends chapter 12's line 25 to "a note for `work/kit-proposals.md`" and no such note exists).

**Behaviour.**

* Opening `work/kit-proposals.md`, the author finds item 13 under "For the next focus-kit version:", after item 12, in the style of items 9 to 12.
* Item 13 quotes the kit's passage, the /propose skill's "the deliveries in flight in `work/`" (SETUP.md §3, installed as `.claude/skills/propose/SKILL.md` and its `.agents` copy), and says it holds on trunk.
* Item 13 says that with a branch or a worktree per delivery each page in flight is written and marked on its own branch, so the main branch's `work/`, where /propose starts, lacks the pages not yet merged; and that the next version says /propose reads those pages where it already reads each slug's line, from that slug's worktree or branch, local or remote, reconciled by slug (docs/05 §4 as migrated by `kit-2026-10-19-1`).
* Item 13 says the book's chapters 12 and 19 keep the kit's words until a kit version carries this, as the file's opening paragraph says for every item.
* Fails: items 1 to 12 or the opening paragraph change; the item names a local path of this machine or of the kit's repository, or a line number of the kit's files; a chapter, docs/03, docs/05 or docs/06 changes.

**Contract.** File: `work/kit-proposals.md` only, English only (a process file, not a chapter: no Portuguese edition). Items 1 to 12 and the opening paragraph stay. Appended after item 12, with one blank line before it, exactly:

    13. **The pages in flight off trunk** (from ch12-free-lines-branches and m22-review, candidates 2 and 18). The /propose skill in SETUP.md §3 reads "the deliveries in flight in `work/`", which holds on trunk. With a branch or a worktree per delivery each page in flight is written and marked on its own branch, so the main branch's `work/`, where /propose starts, lacks every page not yet merged. The next version says /propose reads the pages in flight where it reads each slug's line: from that slug's worktree or branch, local or remote, reconciled by slug, as docs/05 §4 says since 2026.10.19.1. Chapters 12 and 19 keep the kit's words until then.

/apply may polish the wording within these limits. Sources: the installed /propose skill (line "the deliveries in flight in `work/`"), docs/05 §4's board paragraph as migrated by `kit-2026-10-19-1`, chapter 12 "What `/propose` does" (line 29, the reading by slug), work/done/m22-review.md candidates 2 and 18. No term of docs/03 is new: "delivery", "queue line", "Git slot" and the reading by slug are already its words.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Out of scope.**

* Chapters 12 (line 25) and 19 (line 288), both editions: the book teaches the kit as it is, and the finding's line says the chapters keep the kit's words.
* The installed skills and their `.agents` copies: they change with the next kit update, never by hand.
* `work/done/ch12-free-lines-branches.md` line 37: a record; once item 13 exists its pointer holds, and that page's other edits belong to `m22-batch-proof`.
* /apply's own reading of `work/`: the apply skill reads only its own page, `work/<slug>.md`, on the delivery's branch; no finding names it.
* Editing focus-kit's repository: the file is for the author to take there.
* docs/03, docs/05, docs/06: no edit; the queue line's marks are the driver's.

**Decisions taken alone** (recommended answer taken, as the driver asked).

1. A new item 13 under "For the next focus-kit version:", not a sentence added to item 4 or another earlier item: items 1 to 8 are taken, and 9 to 12 each hold one concern (`kit-proposals-ninjobs-phases`, `docs-m21-tidy`).
2. The item proposes the reading by slug the kit already teaches for marks since 2026.10.19.1, not a new mechanism: docs/05 §4 as migrated; least change for the kit.
3. Both findings answered by the one item: candidate 18 asks only that the note promised exist; the record's line 37 is not edited (records are past, and `m22-batch-proof` owns that page's other changes).
4. The kit's passage is named by skill and SETUP.md section and quoted, never by line number or path, as `kit-proposals-ninjobs-phases` decision 3 did.
5. Chapter 19 line 288 is named beside chapter 12 line 25 as following the kit's words, since the finding names both; neither changes.

**Done when.**

* [ ] `work/kit-proposals.md` carries item 13 as the Contract says, nothing else changed (`git diff work/kit-proposals.md` shows only the appended lines).
* [ ] Each Behaviour line checked; no local path, no line number of the kit's files, no em dash in the item or this page; the disclosure scan green.
* [ ] No chapter changed, so no edition and no `make book` apply.
* [ ] `make verify` green after the last edit.
* [ ] Page archived to `work/done/` and commit message suggested.
