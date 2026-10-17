# review-slot-models

**Objective.** The author and the next review's session read in docs/05 §5 how this repository's deep review runs and on which models, as the author decided after M14, so `m15-review` follows the slot and repeats no unrecorded exception.

**Decided from the documents.**

1. The slot names the agent review, not `/code-review ultra <base>` and not both. Ultra alone writes a slot the author does not run: in M14 the author cancelled it for cost and speed (`work/done/m14-review.md`, Divergences). Both leaves the choice to `m15-review`, the failure the code review of `m14-review` found; the queue line asks for how the review runs, one way. Made on the author's behalf, from the author's words after that finding: "Forget about sonnet. All must be done with opus and fable as advisor."
2. The models are the author's choice, offered both readings of "fable as advisor": "an Opus agent writes, then a separate Fable agent reviews it, both models set explicitly", over the host's built-in advisor, whose model cannot be chosen. So Opus agents read, and one Fable agent checks their candidates against the files before the author sees them; each launch sets its model by name. Checking candidates is part of the one review, not the "review of a review" that docs/05 §7 and §8 rule out, which is a second review of the findings' fixes.
3. Who launches it: the session, on the author's word in the review's /apply session; asked by no one, it says it is time and stops.
4. Kit text. docs/05 §7 lists "no specialized subagent", and chapter 16 defines one as "an agent that another agent launches for one narrow role with its own instructions, such as a planner or a reviewer"; these agents are that. §7's own test admits them: "which concrete error would it have caught? The answer names an error that happened", and M14's read-only agents found errors that happened, such as B1, `scripts/repo_files.py` dropping a file with a non-ASCII name from every check, the disclosure scan included (`repo-files-any-name`). docs/05 §8 and chapter 15 say the agent "never launches it"; here the session launches the agents on the author's word, a divergence from §8's letter. §7, §8 and the kit's slot template, "the command a person launches ... or: none", are the kit's text (focus-kit 2026.10.16.2) and stay as they are; the divergence and the template's shape are reported as a note for the kit, not edited (docs/05 §2, report a missing process rule).
5. What the agents read: the changes since `<base>`, as ultra read them ("the changes on your branch since that commit", Claude Code's documentation) and as chapter 15 teaches ("the whole code changed since a base commit"); the ranged form `<base>..HEAD`, since a bare SHA read only one commit in M14's `/code-review high 0c50f1b`. Nothing on this page compares that run with the agents'.
6. The areas, M14's four, one agent each: the build (`scripts/`, `Makefile`, `mkdocs.yml`, `pandoc/`, `overrides/`, `.github/`, `.githooks/`), the chapters (`book/`, both editions), the kit's skills (`.claude/`, `.agents/`, `.windsurf/` and the other hosts' folders), and the documents (every other file). The slot names them; this list is the session's brief, kept here, not in a manual: a manual is for an action a person runs by hand outside a delivery (docs/05 §5, Manuals).
7. docs/03 is unchanged: its "milestone review" row says the person "launches the Milestone review slot's deep code review against the commit the page names", and it still reads true, since the review starts only on the author's word; who runs the agents the row does not say. "Opus", "Fable" and the agents are this repository's settings, not the book's vocabulary: no new term.

**Behaviour.**

* Reading docs/05 §5 after this delivery, the Milestone review slot reads exactly the Contract's text, and `grep -n "ultra" docs/05-Process.md` finds nothing.
* In `m15-review`'s /apply the author writes "run the deep review against <the commit that closed M14>": the session launches one read-only agent per area that `git diff <base>..HEAD` touches, each with its model set to Opus; an area the diff does not touch gets no agent.
* Each agent reports candidates with file and line; the session launches one Fable agent, model set to Fable, which opens each file and marks each candidate seen, latent or weak, as M14's page did; the session shows the author those marks; the author confirms which count, and each confirmed one is a finding (docs/05 §8).
* Fails: the session reaches the deep review and the author has not asked: it says it is time and stops; no agent runs.
* Fails: a launch with Opus or Fable named as its model is refused by the host, or runs on another model: no agent runs on a substitute and no `/code-review ultra` runs in its place; the review line waits as `[?]` with `· resume: apply · blocked: deep review models unavailable`.
* Fails: an agent proposes or makes an edit: agents are read-only and a candidate is never a fix (docs/05 §8, "It fixes nothing").
* Edge: no file under `book/`, no chapter, docs/03 and docs/05 §7 and §8 change; chapter 15's slot is the lending library's and chapter 8's is the kit's update report.

**Contract.** docs/05 §5, the Milestone review slot replaced by:

```
* **Milestone review:** on the author's word in the review's /apply
  session, read-only agents on Opus read `git diff <base>..HEAD`
  against the commit the review's page names, one per area it touches:
  the build, the chapters, the kit's skills, the documents. An agent on
  Fable checks each candidate against the file before the author sees
  it. Each launch sets its model; no other model runs the review.
```

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Out of scope.**

* Whether every /propose, /apply and other agent work in this repository runs as Opus writing and Fable reviewing: a separate decision the driver takes to the author; this line is the review's slot.
* docs/05 §7, §8 and the kit's slot template: the kit's text (docs/04, the book teaches the kit as it is); the divergence is reported, not edited.
* docs/03 and any chapter: decision 7; chapter 15's example is the lending library's, chapter 8's is the kit's report.
* `work/m15-review.md`: another delivery's page; its "the slot's command" wording is the driver's to revise.
* `work/done/m14-review.md`: its divergence stays as history.

**Done when.**

* [x] docs/05 §5's Milestone review slot equals the Contract's text, byte for byte.
* [x] `grep -n "ultra" docs/05-Process.md` finds nothing; `git diff --cached --stat` holds only docs/05, this page's move to `work/done/` and this line's hunk of docs/06 (docs/05 §6).
* [x] /apply's last words report, as a note for the kit, the divergence from §8's "never launches it" and the slot template's "the command a person launches" (decision 4).
* [x] `make verify` green; no em dash on this page.
* [x] Page in `work/done/`, line `[x]`, staged by its paths and its hunk of docs/06, commit message in a `commit` block.

**Divergences.** None from the page. Decision 4's divergence stands as the page records it: docs/05 §8 still says the agent "may say it is time and never launches it" and §7 still lists "no specialized subagent", both the kit's text as installed (`.claude/skills/analyze/references/documents.md`, §§7 and 8 of its template), so §5 now names agents the session launches on the author's word while §8's letter says the person launches. Reported to the author as a note for the kit, with the template's slot shape, "the command a person launches for a deep review ... or: none", which has no place for a review run by agents.

**Omissions.** No tests: the delivery changes one slot of a document; its Behaviour lines are exercised by `m15-review`'s /apply, the first review to run on this slot. Chapter 8's quotation of "Milestone review: Claude Code's /code-review ultra <base>" is the kit's update report of 2026.10.16.2, as decision 7 and the Edge say, and stays.

**Proof.**

* The Contract's fenced block, extracted from this page, and docs/05 §5 from `* **Milestone review:**` to the line before `* **Git:**` compare byte-identical (`cmp`).
* `grep -n "ultra" docs/05-Process.md` finds nothing (exit 1).
* `make verify` green: strict build, parity, em dash, prose, links, disclosure.

**Decisions.** `m15-review`, `[?]` with `resume: apply · blocked: after review-slot-models`, returns to `[>]` with both suffixes removed (docs/05 §4), so docs/06's net change is this line alone. `work/m15-review.md`'s revision in the tree is that delivery's and is not staged here.

```commit
docs(review-slot-models): milestone review runs on Opus agents

- docs/05 §5: the Milestone review slot names read-only Opus agents per area over git diff <base>..HEAD, a Fable agent checking each candidate
- the slot no longer names /code-review ultra
- m15-review returns to [>]

work/done/review-slot-models.md
```
