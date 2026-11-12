I updated the kit's command files to focus-kit 2026.11.12. Your project documents are still at 2026.10.27 and need several changes, listed below. I changed none of them, as the setup file says. Your edited files were safe: every file I replaced matched a version the kit shipped. Nothing was staged or committed, and there was no `git init`.

## Files written

I wrote all 36 kit files at their paths. All 36 match the eighteen-file count and the other checks in section 4 of the setup file.

**14 had new contents** (versions 2026.10.27 to 2026.11.12):
- `.claude/skills/` and `.agents/skills/`: `brainstorm/SKILL.md`, `analyze/SKILL.md`, `propose/SKILL.md`, `apply/SKILL.md`
- the same two folders: `brainstorm/references/documents.md`, `analyze/references/documents.md`
- `propose/scripts/queue.sh` in both folders

**22 were rewritten with the same bytes they already had:**
- `propose/scripts/claim.sh` and `propose/scripts/mark.sh`, in both skill folders
- `.agents/skills/{brainstorm,analyze,propose,apply}/agents/openai.yaml`
- `.github/prompts/{brainstorm,analyze,propose,apply}.prompt.md`
- `.cursor/commands/{brainstorm,analyze,propose,apply}.md`
- `.gemini/commands/{brainstorm,analyze,propose,apply}.toml`
- `.agents/rules/focus-kit.md`
- `GEMINI.md`, which keeps exactly one pointer line

Nothing was removed. There is no `.windsurf/skills/`.

## Installed version

The skills are now at 2026.11.12; before this run they were at 2026.10.27. That does not update your process: `docs/05` still follows 2026.10.27. It lacks what 2026.10.27.1 added (dropped lines left out of `after all`) and what 2026.11.12 added (findings, notes, grading). The changes below are still pending.

## Pending changes

### docs/05-Process.md

1. **§2, "Add a missing queue line where it belongs and say so."** Replace with: "Add a missing queue line where it belongs and say so; a flaw found on the way is a finding, and §4 says whether it is a line."

2. **§3, after "There is one final block: a resumed /apply replaces the earlier suggestion."** Add: "Above that block a page may hold a heading `## For the review`: the notes §4 defines, one line each, written by the command that found them."

3. **§4, first paragraph, about `after all`.**
   - "every line above it in its milestone, which is how the review is written" becomes "every line above it in its milestone but the dropped ones, which is how the review is written".
   - At the end of the dropped-line paragraph, after "a line whose `after` names it is the person's to re-decide.", add: "`after all` names none and leaves it out."

4. **§4, "a finding of the milestone's own review stays in it (§8). Asked what may run now, run".** This is the change that blocks the commands.
   - Replace the first sentence with: "a finding of the milestone's own review stays in it (§8), and so does a grave finding, below."
   - Start "Asked what may run now" as a new paragraph.
   - Between them, add the template's paragraph as it is: "What /apply's review, proof or build discovers in what its delivery built or changed is fixed in that delivery, as /apply says, and is no finding here. A finding is a flaw a command discovers in anything else, /propose while it defines included. A flaw older than the delivery is one, even in a file the delivery edits. A finding is grave when it breaks a clause of the milestone's paragraph for a person on its usual path, loses or exposes data, or leaves verify red. So is a fix a delivery in flight cannot go on without. A grave finding becomes a `[ ]` line ending `· from <slug>`, the delivery that found it. The line goes above the open planned lines only when verify is red or one of them needs it. Otherwise it goes below them, above the review, or under the review once it ran. Every other finding is a note on the page of the delivery that found it, under `## For the review` (§3): the file and line, and what a person would see. A note is not a line and waits for the next milestone review to run (§8). A finding nobody can say is grave is a note. A flaw in what a delivery built, whose fix would widen its page or needs a decision no document answers, is a note too, with what the person may do. When that flaw is grave, or leaves a Done when item unticked, the line waits for the person's answer instead, the second case below. A line that delivers a test, a proof tool or a change to this process, and is not a grave finding, enters only on the person's word; without it, it is a note."

5. **§5, Verify slot, "Green before anything is declared done. Slow tests: none."** Replace with: "Green before anything is declared done. Its ceiling: five minutes. /apply says how long verify took. Over the ceiling, that is a note for the review (§4). The review says which tests go to the slow ones. Slow tests, one line each, with what each covers: none. The milestone review runs them all (§8). /apply runs the ones that cover what its delivery changed, and only those, before the delivery ends."
   - The setup file would have me ask you for the ceiling. I couldn't, so I proposed its default of five minutes.

6. **§8, first paragraph, "/propose writes its page when every line above is defined, /apply runs it when every line above is integrated."** Replace with: "/propose writes its page when every line above but the dropped ones is defined, /apply runs it when every one of those is integrated."

7. **§8, the paragraph "Each finding becomes a `[ ]` line in the same milestone, under the review line, waiting for /propose. ... never a fix in the middle of the next milestone."** Replace it with the template's text: "The review opens by copying onto its page the notes left since the previous review, from the `## For the review` heading of every page the range delivered (§4). The checker marks each as it marks a candidate. The review grades every confirmed finding. A grave one, as §4 defines it, becomes a `[ ]` line, one each. The others stay listed on the review's page. First come the medium ones, which a person meets in ordinary use while the clause still holds. Then come the small ones: a rare case, a latent or weak candidate, a cost nobody measured. The person says which medium ones enter the milestone's one line, `<milestone>-fixes`, each an item of its page. That page is their list and is not split, whatever its length. A small one becomes a line only when the person picks it. These lines end `· from <milestone>-review`, sit under the review line and wait for /propose; the milestone closes when they are `[x]`. They get no second review: each passes through its own page, its proof and the person's commit, which is the review; a finding is never a fix in the middle of the next milestone."
   - **A question I would have asked you:** your §8 lets the author's word (from the `docs05-author-word` delivery) confirm candidates and list latent and weak ones as dropped. The new text has the person pick the medium findings for the `-fixes` line. Does that word also cover the pick? My default: no, the confirmation stays as recorded and the pick stays yours.

8. **§4, the sentence that records versions** ("These are the marks of focus-kit 2026.10.05 ... `kit-2026-10-27`)"). This one is not required by the kit; it is your own practice, backed by ADR-0018's amendments.
   - Before "(ADR-0018 and its amendments", add: ", `after all` leaving out the dropped lines is that of 2026.10.27.1, and a flaw a delivery built fixed in it, what a finding is, a grave one as a line ending `· from` and the others as notes for the review are those of 2026.11.12".
   - Add `kit-2026-10-27-1` and `kit-2026-11-12` to the list of amendments, with new ADR-0018 amendments to match.

**Already in line with the template:**
- Section numbers: §4 queue, §5 slots, §6 commit, §8 closing a milestone.
- §2's other rules.
- §3's Contract, Behaviour, Visual reference, Outcome and `commit` block.
- §4's marks, resumption, `queue.sh`, `mark.sh`, file check, next milestone, the four waiting cases, ended and dropped lines, the claim and current copy. The parallel paragraphs are rightly present, since the Git slot lets two sessions share a tree.
- §5's Design, Publish policy, Context, Delivery review (`git diff HEAD`, branch commits, created files), Manuals (with the run manual), Milestone review and Git slots. The slots point to manuals rather than narrating steps.
- §6, including the single index and never naming paths.
- §7's exception for the reviews' agents.
- §8's slow tests, range, who reads, the checker and paths read.

**Project choices to keep, with what the kit says:**
- §6: "the person commits after reviewing, or asks the agent to", the release commit by `make release`, and the `<type>(<slug>):` subject (ADR-0010, amendment of 2026-10-19). The kit says the agent never commits on its own and, asked, takes the step you name. The release commit is your own addition.
- Delivery review and Milestone review on Opus only, at most two agents at a time (the `review-slot-models` and `m16-review` deliveries). The kit says the session's model.
- §8's paragraph on a milestone of chapters, the author's-word paragraph (`docs05-author-word`), and the note on M3 and M4.
- §1's "a chapter is one delivery" and §3's reading of a chapter's page.

### docs/06-Queue.md

1. **Line 3.** The suffix list should end "`· dropped:`, `· from`)" instead of "`· dropped:`)".
2. **Lines 722 to 725.** The four open lines under `m32-review` are its findings, so they need `· from m32-review` at the end. Example for line 723: `[ ] queue-tree-row-source docs/03's `queue tree` row and ADR-0018's `kit-2026-10-24` amendment cite for the no-slug rule and /apply's ending the skills that hold them, not docs/05 §4 · after m32-review · from m32-review`
3. **Closed lines with history.** No open line carries history. Three closed lines carry commit hashes their pages already hold: lines 92, 125 and 611. Example for line 125: `[x] m4.1-code-review       /code-review of the clinic's code that M4.1 changed` (the range `a3e2470...6edc9ad` is in `work/done/m4.1-code-review.md`).

**No change needed:**
- The closed lines under earlier reviews keep their form; `queue.sh` counts findings only in the current milestone.
- The closed review lines 92, 95 and 125 predate `· after all` and have no effect on what may run.
- `(PA)` on lines 622 and 683 is a chapter's subject, not a token.
- No line is wrapped.

### Outside the setup file's list

`docs/03-Domain.md`, the `finding` row (line 35), says every finding "becomes a `[ ]` line in the same milestone". The `milestone review` row (line 33) also lacks the notes and the grading. Both should change with the §4 and §8 migration, in the same delivery.

### No change needed

- **docs/04-Conventions.md:** it points to docs/05 §6 for commits and gives its tests by level.
- **AGENTS.md:** it has every process rule, the docs/manuals line, and the em dash and abstraction lines pointing at docs/04 and docs/01.

## Next step

**The next step is the docs/05 change, not a command.** Until §4 says what a finding is and §8 collects the notes, the new `/apply` leaves every finding as a note nobody reads. Your queue already holds this work as `kit-2026-10-27-1` (M36) and `kit-2026-11-12` (M38). They wait behind `m35-review` and `m37-review`, and this run has now done their reinstall step, as it has for `kit-2026-11-03`. I would have asked whether to bring that change forward. My recommendation: apply the docs/05 and docs/06 items above, plus the docs/03 rows, before the next command.

After that, the first free line is `m32-records-claims`, which is `[ ]` with `m32-review` at `[x]`; no line is at `[>]`. In a fresh session, run:

```
/propose m32-records-claims
```

I read this from docs/06 by hand: the folder has no git repository, so `queue.sh` could not run.
