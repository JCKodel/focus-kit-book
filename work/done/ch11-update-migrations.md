# ch11-update-migrations

**Objective.** After chapter 11 a reader can update focus-kit knowing what the update writes and what it only reports: it replaces the kit's files and stops before overwriting one it did not ship, reports as migrations the rule changes that belong in docs/04, docs/05 and `AGENTS.md` and leaves those files as the team wrote them, which the team applies as a delivery after reading the changelog; and every command names the next one as the reader's host invokes it.

**Behaviour.**

* A reader on Claude Code updating from 2026.10.05 to 2026.10.13 expects the update to rewrite the kit's command files and then report, without writing them, the migrations for their project: for each, the path, the section and the proposed wording, such as the Manuals slot in docs/05 §5 and the `docs/manuals/` line in `AGENTS.md`'s Read before acting.
* A reader asked "the update finished, is my process on 2026.10.13?" answers no: the `metadata.version` in each `SKILL.md` says which kit is installed; the process changes only when the reported migrations are applied, and the reader adds them as a queue line and runs it through `/propose` and `/apply`.
* A reader who wants to know why a migration exists opens the kit's changelog, finds the entry for that version, newest first, and reads what changed, the problem that caused it and the `Migration:` item.
* A reader whose docs/05 §5 says "trunk, one session at a time" sees the update propose the two-sessions wording as a migration and keep the reader's choice until the team accepts it; the update never edits docs/05.
* Failure: a reader who edited `.claude/skills/apply/SKILL.md` by hand, or added a command of their own in a host's folder, sees the update show the diff against the kit's file and stop before writing any file; the reader decides whether to keep it or replace it.
* Failure: a reader who expects to run `/brainstorm` or `/analyze` again to update the process knows from the chapter that the update says no: on a documented project it reports the migrations, or says there are none.
* Edge: an update with no rule change for the project's documents (2026.10.08.2, the `commit` block shown in the conversation) reports no migration; the commands change and nothing else does.
* A reader on Codex sees each command end by naming the next one as `$apply lend-book`, and a reader on Claude Code as `/apply lend-book`; the reader knows, from chapter 11's table, that the form follows the host and not the kit.

**Contract.**

* **Chapter 11, both editions, file name kept; same headings in both.**
  1. Opening: "update it with the same sentence" gains that an update reports, as migrations, what it does not write in the project's documents.
  2. "What the install never touches, and how to update": keeps its text; gains that the update replaces a file only when it is one the kit shipped, in this or an earlier version, and that a custom command or an edit of the reader's stops it before it writes anything, with the diff, for the reader to decide (SETUP.md §1, step 1).
  3. A new section "What an update reports" (pt: "O que uma atualização relata") after it: docs/04, docs/05 and `AGENTS.md` belong to the project; when a kit version changes a rule they hold, the update compares them with its templates and reports each migration with the path, the section and the proposed wording in the documentation language, and keeps the project's choices; the installed version is not the process, an updated kit with migrations not applied still runs the old process; the team applies them as a delivery, a queue line through `/propose` and `/apply`; on a documented project the update reports the migrations first, or says there are none, and never asks for `/brainstorm` or `/analyze` again (SETUP.md §1, steps 4 and 5). Then the changelog: `CHANGELOG.md`, in Portuguese `CHANGELOG.pt.md`, newest first, one entry per version, the version being the `Version:` line of `SETUP.md` and the `metadata.version` in each `SKILL.md`; each entry says what changed and the problem that caused it, and a `Migration:` item names what to change in the project's documents. Example written for the chapter on the lending library, said so: the 2026.10.13 report naming docs/05 §5's Manuals slot and the line in `AGENTS.md`.
  4. "How each host finds the commands": a paragraph after the table: every command ends by naming the next one, written as the host running it invokes it, as the table's last column (the setup file names `/brainstorm` or `/analyze`, `/propose` names `/apply <slug>`, `/apply` the next line, chapter 15); one example on the lending library in two hosts.
  5. "What the team gains": two gains from the kit's changelog, paraphrased, named in plain words, no note (docs/04, as `ch10-12-manuals`): an update never rewrites the rules the team wrote, with the count of the versions from 2026.10.07, when the report came in, to 2026.10.13 whose entry changes a rule in the project's documents (five of six when this page was written, 2026.10.08.2 the one without; /apply recounts from the changelog at kit `96c0930`); and the next command in the host's form, from entry 2026.10.08.1: a Codex user was told to run `/propose`, which Codex does not recognize. The paragraph on plain files kept.
  6. Key points: the update point says it reports migrations and writes nothing in docs/04, docs/05 or `AGENTS.md`; new points on the changelog and on the next command in the host's form.
* **Terms:** setup file, host, delivery, queue line, slot, as docs/03 has them; **migration** and **changelog**, added to docs/03 by this page.
* **Sources:** the kit's `SETUP.md` §1 at 2026.10.13 and its `CHANGELOG.md` entries 2026.10.07 to 2026.10.13, named in plain words, no note (docs/04); the chapter's existing vendor notes unchanged.
* **Cases:** none; no Case A or B, no Ninjobs passage.
* **Code examples:** none; the migration report and the next command are written for the chapter on the lending library, said so; Portuguese names in the Portuguese edition (the slugs `lend-book` and `return-book` as chapter 15 has them, `emprestar-livro` and `devolver-livro` there).
* **Queue:** chapter 10's sentence on docs/04 and the commit format, assigned here by `ch15-apply-ends`, became the line `ch10-commit-format · after ch10-12-manuals` (author's choice: `ch10-12-manuals` is building chapter 10 now).

**Out of scope.**

* Chapter 10's sentence on the commit format: `ch10-commit-format`.
* The host table's new rows in the kit's `SETUP.md` (OpenCode, Zed and the hosts that only read `AGENTS.md`): no line asks for them; the chapter's last paragraph already covers hosts that read `AGENTS.md`.
* What each migration of 2026.10.13 teaches (manuals, two sessions, queue order, `/propose` deciding): the other M12 chapter lines.
* This book's own update as evidence: the milestone's paragraph names the changelog as the evidence (docs/06, M12).
* A full migration report or changelog entry quoted: the chapter names their parts.

**Done when.**

* [x] Chapter 11 changed in both editions, same headings; opens with its value; no filler and nothing useful cut.
* [x] No sentence in the book says an update writes or rewrites docs/04, docs/05 or `AGENTS.md`, or that an update is done once the kit's files are written.
* [x] The count of versions with a migration recounted from the changelog and said where it comes from; the changelog and `SETUP.md` named in plain words, no note.
* [x] `make verify` green; `make book` builds and both PDF paths are given to the author.
* [x] Page in `work/done/`, the line `[x]`, staged by its paths, its hunk of docs/06 and its rows of docs/03, the commit suggested in a `commit` block.

**Decisions taken from the documents.**

* The changelog is the evidence, not this book's own update: docs/06, M12's paragraph.
* Stopping on a custom command and never asking for `/brainstorm` again are taught here, since they are what makes an update safe to run: `SETUP.md` §1, steps 1 and 5.
* The next command in the host's form is taught after chapter 11's table, since `ch14-propose-decides` and `ch15-apply-ends` left it here (their pages' Out of scope).
* No note to the kit's files, the count included: docs/04 ("No note points to ... a file of focus-kit's repository"); the sentence names the changelog in plain words and says the count comes from it.
* Migrations applied as a delivery, a queue line through `/propose` and `/apply`: the kit says only to apply what the report identifies (`SETUP.md` §1 and the changelog's header); the delivery is how this book applied 2026.10.13 (`kit-2026-10-13`). The chapter says it as the method's way, not as the kit's words; correct here if you want it said otherwise.
* Chapter 10 moves to its own line (asked; author chose).

**What happened.**

* Tree at the start: index empty; docs/03 (the rows migration and changelog), docs/06 (this line `[>]`, the new line `ch10-commit-format`) and this page were this delivery's /propose output. During the build another session moved `ch10-commit-format` to `[>]` and `ch18-19-only-apply` to `[~]` in the same hunk of docs/06, and wrote `work/ch10-commit-format.md`: that session's work (docs/05 §4). Only this line's change is staged in docs/06; the `ch10-commit-format` line, added by this page's /propose, is now in the state the session building it gave it and goes with that delivery.
* Chapter 11, both editions, same headings: the opening gains what the update writes and what it only reports; "What the install never touches, and how to update" keeps its text and gains the ownership rule and the stop on a custom command or a hand edit, with the diff; the new section "What an update reports" / "O que uma atualização relata"; a paragraph after the host table on the next command in the host's form (`/apply lend-book`, `$apply lend-book`; `emprestar-livro` in Portuguese); two gains; key points.
* The count, recounted from the kit's changelog at `96c0930`: from 2026.10.07 to 2026.10.13 there are six versions (2026.10.07, 2026.10.08, 2026.10.08.1, 2026.10.08.2, 2026.10.08.3, 2026.10.13); five change a rule in docs/04, docs/05 or `AGENTS.md`; 2026.10.08.2 changes only the commands. The sentence says the count comes from the changelog, no note.
* The migration report is written for the chapter on the lending library and says so: docs/05 §5's Manuals slot and the line in `AGENTS.md`'s Read before acting, the latter in the kit's template wording ("what a person does by hand (publish, roll back): docs/manuals/"). In Portuguese the report is in Portuguese, the project's documentation language there, with the section names in English as chapter 10's Portuguese edition keeps them ("o slot Environments").
* Second Done when: searched both editions for the setup file, `SETUP.md`, update, `/brainstorm` and `/analyze` outside chapter 11; no sentence says an update writes docs/04, docs/05 or `AGENTS.md`, or that it is done once the kit's files are written.
* The queue line until kit-2026-10-16 said: chapter 11: updating reports migrations for docs/04, docs/05 and AGENTS.md and preserves them, the changelog as where to read what changed; each command names the next one as the host invokes it; both editions.

**Divergences.**

* Key points: the page asked for two new points on top of chapter 11's five, and docs/04 allows five. Install and update stay one point (now with the stop on a changed file); the update point says it reports migrations and writes nothing in docs/04, docs/05 or `AGENTS.md`; the changelog is its own point; the host forms and the next command share one point.
* No second pointer to chapter 15 or chapter 12 in the new text: chapter 11 already points to each once (docs/04, Chapter pointers).
* The changelog's `Migration:` item is named in Portuguese as the kit's Portuguese changelog writes it, `Migração:`.

**Proof.** `make verify` green (strict build, parity, em dash, prose rules, links, disclosure). `make book` built `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf` for the author to review; no new kind of content, so no screenshot (docs/05 §5).

**Environments.** Local: `make serve` and `make book` build. GitHub Pages publishes from `main` on the author's push; GitHub Release only on the author's tag (docs/05 §5).

```commit
docs(ch11-update-migrations): teach migrations, changelog and next command

- Chapter 11: an update replaces only the kit's own files, stops on yours
- New section: what an update reports, the installed kit vs the process
- The changelog: one entry per version, the problem and the Migration item
- Every command names the next one as the host invokes it
- docs/03: migration and changelog

work/done/ch11-update-migrations.md
```
