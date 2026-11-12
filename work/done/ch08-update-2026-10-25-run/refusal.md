The kit is not updated, and nothing in the repository was written or removed. Setup stopped at step 1 because one file the kit owns has a hand edit, and the file says I may not write anything until you decide what happens to it. This is the point where I would have asked you.

## 1. The edit that stopped setup

`.claude/skills/apply/SKILL.md` matches no version of the kit. It was made on the kit's 2026.10.27 `apply/SKILL.md` (commit 94f8bfb), which the untouched `.agents/skills/apply/SKILL.md` still holds byte for byte. Your edit against that file:

```diff
@@ -70,3 +70,4 @@
 says. Then what may run next, as docs/05 §4 says. End saying which
 environment is at which version and the command that updates the
 others; never end silent.
+A line the person added by hand.
```

What the kit itself changed in that file since 2026.10.27:
- **2026.11.03:** `/apply` ends by running `queue.sh` even though no one asked, and shows its `next:` command.
- **2026.11.12:**
  - Fixing what the delivery built does not count as widening the page. What its review, proof or build finds wrong in its own work is fixed in the delivery.
  - What it cannot fix is a note on the page, not a new line, unless docs/05 §4 calls it grave.
  - A prerequisite line ends `· from <slug>`.
  - It writes tests only for what the page says and for each flaw it fixes.
  - The last message opens with an alarm, warning or check-mark sign.
  - The version becomes 2026.11.12.

You decide whether to keep the added line or replace it. If it is a rule for `/apply`, it can become a project slot in docs/05 §5 naming /apply, which /apply already follows, and the kit file can then be replaced.

Every other kit file is the kit's own:
- **Already current (19):**
  - in both skills folders: `claim.sh` and `mark.sh`
  - `.agents/rules/focus-kit.md`
  - the four `openai.yaml` files
  - the four prompt files, four Cursor commands and four Gemini commands
  - `GEMINI.md`, which already holds exactly one pointer line
- **Unedited kit 2026.10.27, ready to replace on a rerun (16):**
  - in both folders: the other three `SKILL.md` files, both `documents.md` and `queue.sh`
  - `.agents/skills/apply/SKILL.md`
- **`.windsurf/skills/`:** does not exist.

Installed skill version: 2026.10.27. That is separate from the process migrations below, which an updated skill would not do for you.

## 2. Process migrations still pending (reported, not done)

All of these are wording changes in `docs/05-Process.md`.

**§2, after "Add a missing queue line where it belongs and say so":**
> ; a flaw found on the way is a finding, and §4 says whether it is a line.

**§3, at the end of the paragraph on `## Outcome`:**
> Above that block a page may hold a heading `## For the review`: the notes §4 defines, one line each, written by the command that found them.

**§4:**
- "every line above it in its milestone" becomes "every line above it in its milestone but the dropped ones".
- The dropped-line paragraph ends with "`after all` names none and leaves it out."
- "a finding of the milestone's own review stays in it (§8)" gains ", and so does a grave finding, below."
- Insert the template's paragraph that begins "What /apply's review, proof or build discovers in what its delivery built or changed is fixed in that delivery…". It says:
  - what a finding is, and what makes one grave
  - a grave finding is a `[ ]` line ending `· from <slug>`, and where it goes
  - every other finding is a note under `## For the review`
  - a flaw the delivery cannot fix is a note, or a wait for your answer
  - a test, proof-tool or process line enters only on your word
- §6's sentence "A prerequisite that must be built first becomes a `[ ]` line above this one" should also say "ending `· from <slug>`".

**§5 Verify:** replace "Slow tests: none." with:
> Its ceiling: five minutes. /apply says how long verify took. Over the ceiling, that is a note for the review (§4). The review says which tests go to the slow ones. Slow tests, one line each: none. The milestone review runs them all (§8). /apply runs the ones that cover what its delivery changed, and only those, before the delivery ends.

Five minutes is the kit's default; you may name another ceiling.

**§8:**
- "every line above is defined / … integrated" gains "but the dropped ones".
- Add "The review opens by copying onto its page the notes left since the previous review, from the `## For the review` heading of every page the range delivered (§4). The checker marks each as it marks a candidate."
- Replace "Each finding becomes a `[ ]` line in the same milestone, under the review line…" with the template's grading: a grave finding is one line each; the medium ones you pick go on one `<milestone>-fixes` line; the rest stay listed on the review's page.
- Your paragraph letting the review's session take the tests on your word is a project addition the kit does not contradict. It stays.

**§5, the shape of a slot:** the hand-added line above is the case of "a rule added to a command's file". No other slot needs reshaping.

**`docs/06-Queue.md`:**
- No line is wrapped, and none carries a `(PA)` token. Lines 622 and 683 only mention `(PA)` as chapter content.
- Every milestone review line ends `· after all`. Lines 95 and 125 are done code-review lines sitting under M4's and M4.1's reviews, not the review line itself.
- No line says in prose which delivery found it, so no `· from` is owed.
- One line carries history: `ch03-query-catch`, line 501. Its page already holds the audit. Rewritten:
  > `[x] ch03-query-catch         chapter 3: `query` turns only the driver's failures into a value and rethrows the rest, and an async variant awaits inside the try, each case tested; both editions`

**No migration** in `docs/04-Conventions.md` (it points to §6 and lists tests by level) or `AGENTS.md`.

## 3. What comes next

1. Decide what happens to the line added in `.claude/skills/apply/SKILL.md`, then run this setup again. It will write the kit's 2026.11.12 files.
2. Apply the docs/05 §4 and §8 migration before any command. Until §4 says what a finding is and §8 collects the notes, the new `/apply` would leave every finding as a note nobody reads. Your queue already plans this as `kit-2026-11-12` (M38), with `kit-2026-10-27-1` (M36) for the dropped-line sentences and `kit-2026-11-03` (M37). They sit behind M32 to M37, so they would need to move up.
3. After that, the first free line is `m32-records-claims`, together with the other three open M32 lines: `/propose m32-records-claims`, in a fresh session.
