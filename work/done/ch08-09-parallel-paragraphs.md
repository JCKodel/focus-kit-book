# ch08-09-parallel-paragraphs

Built before the author read it: the author asked for the whole queue to be run, each page decided alone and built in the same session (docs/05 §4, a command that says to decide alone and to build as well). Every choice the documents leave open is marked "decided by the agent, the author corrects it in the review".

**Objective.** After chapters 8 and 9 the reader knows that the command writing a project's documents puts docs/05 §4's two paragraphs on parallel work in only when the git strategy is a branch or a worktree per delivery or the person says sessions will run at the same time, and that an update leaves a docs/05 of one session at a time on trunk without them, as the team chose.

**Behaviour.** What the reader can do or explain afterwards:

* Say what the two paragraphs hold: two sessions in one working tree on free lines, and a command typed with several slugs.
* Say when they are written: the Git slot is a branch or a worktree per delivery, or the person says sessions will run at the same time; otherwise they are left out, and a later decision adds them.
* Say why: every `/apply` reads docs/05 §4, so a team working one session at a time would read about sessions it never runs on every delivery.
* Failure: asked "my docs/05 says trunk, one session at a time; will the update propose the paragraphs for two sessions in one folder?", answer no: the kit writes them only where sessions overlap, and the choice stays.
* Name a real case: this book's docs/05 keeps them, because its Git slot says two sessions may work in one tree on free lines.
* In the Portuguese edition, the same, with docs/03's Portuguese terms.

**Contract.** Four chapter files, line numbers en / pt at HEAD `47b35ee`; pt follows en sentence for sentence. The text is the agent's within these changes.

* **ch09** (`book/en/09-starting-a-project.md`, `book/pt/09-starting-a-project.md`)
  * C1, after "Each slot it writes in docs/05 ..." (:25 / :25): a short paragraph: the two paragraphs of §4 on parallel work, what they hold, when the command writes them (Git slot a branch or a worktree per delivery, pointer to chapter 20; or the person says sessions will run at the same time), left out otherwise and added by a later decision; why (every `/apply` reads §4); this book's docs/05 keeping them because its Git slot says two sessions may work in one tree. It says the docs/05 either command writes, since `/analyze` writes from the same template.
* **ch08** (`book/en/08-install-and-hosts.md`, `book/pt/08-install-and-hosts.md`)
  * C2, "Your choices stay" (:59 / :59): a docs/05 whose §5 says "trunk, one session at a time" keeps it, and the update proposes no paragraphs on parallel work for it, which the kit writes only where sessions will run at the same time (chapter 9); a migration the update does propose waits for the team to accept it.

Terms of docs/03: slot, migration, delivery, subagent (not named). No new term: "the paragraphs on parallel work" is a description, not a concept of the domain. Sources: the kit's `SETUP.md` at 2026.11.12 (step 4's §4 item, "The parallel paragraphs present only where sessions overlap"; `/brainstorm`'s first milestone, "When sessions will run at the same time, docs/05 §4 gets its parallel paragraphs") and `references/documents.md`'s docs/05 template, §4 ("Written when §5's Git slot is a branch or a worktree per delivery, or when the person says sessions will run at the same time: the two paragraphs below. Otherwise they are left out, and a later decision adds them"), installed here byte for byte in `.claude/skills/brainstorm/references/documents.md` and `.claude/skills/analyze/references/documents.md`; this repository's docs/05 §4 and §5's Git slot. No number. No source note: the kit is taught as it is (docs/04). Cases: none.

**States.** Inapplicable: chapters, no screen.

**Visual reference.** Inapplicable: no screen, and no new kind of content (prose).

**Out of scope.**

* Chapter 8's report excerpt without `None` and the medium findings in chapters 7, 8, 11, 13 and 14: `m33-fixes`.
* The changelog's story of why the paragraphs became conditional, and its numbers: the book teaches the kit as it is (docs/04).
* docs/05 of this repository: it keeps the paragraphs by its Git slot, as m33-review found; nothing to change.
* docs/03's retired parallel token row: history, true as written.

**Done when.**

* [x] C1 and C2 read as the Contract says in both editions; no passage left saying a trunk docs/05 of one session at a time sees the two-session wording proposed.
* [x] Both editions written; each chapter opens with its value; no filler and nothing useful cut; no number added; no em dash; no run narration.
* [x] `make verify` green after the last edit; the disclosure scan green.
* [x] `make book` builds both editions, both PDF paths recorded.
* [x] Delivery review by one read-only Opus agent, as docs/05 §5 says; only this delivery's paths and its docs/06 line staged; the page in `work/done/` and its commit message suggested.

**Decisions.**

* Decided by the agent, the author corrects it in the review: chapter 9 teaches the rule once, after `/brainstorm`'s six subjects, for the docs/05 either command writes, since `/analyze` writes from the same template; the line names `/brainstorm` only.
* Decided by the agent, the author corrects it in the review: chapter 8's example keeps the trunk docs/05 of one session at a time and turns it into the case it now is, a choice the update leaves alone, rather than replacing it with another example.
* Decided by the agent, the author corrects it in the review: the reason is given in the present (every `/apply` reads §4), without the changelog's observation of two trunk projects or its word counts, as the book teaches a kit change as it is now.
* From the documents: the condition and its wording (the kit's `SETUP.md` and the installed `references/documents.md`), the book's own case (docs/05 §5's Git slot), the finding (`m33-review`, G1).

## Outcome

* Built as the Contract says, C1 and C2, in both editions. Diverged: C1's pointer goes to chapter 18, which teaches the kit's three git strategies, not chapter 20 (pull requests, issues and boards), as the Contract said; C2 is two sentences, the choice kept and then the migration that waits, for a reader who is not a developer.
* Delivery review: one read-only agent on Opus (model set at launch, Explore type) read the page, docs/04, `AGENTS.md`, the diff of the four chapter files and this line's docs/06 hunk, the installed template, `/brainstorm`'s `SKILL.md`, the kit's `SETUP.md` step 4 and docs/05 §§4 and 5. Four candidates, all fixed:
  * 1, ch09 :27: the pointer to chapter 20 was wrong; fixed: chapter 18, both editions.
  * 2, ch09 :26: the new paragraph had no blank line before it and joined the slot paragraph; fixed, both editions.
  * 3, pt ch08 :60: "propõe" lost en's "does propose"; fixed: "de fato propõe".
  * 4, ch08 :59: one sentence held three claims; fixed: split in two, both editions.
* Proof: `make verify` green after the last edit, 12.4 seconds; `make book` built `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.
* No number added, no case used, no note for the review.

```commit
docs(ch08-09-parallel-paragraphs): fix ch8 and ch9 on §4's parallel work

- Chapter 9: §4's parallel paragraphs only where sessions overlap
- Chapter 8: a trunk docs/05 of one session keeps its choice
- Both editions

work/done/ch08-09-parallel-paragraphs.md
```
