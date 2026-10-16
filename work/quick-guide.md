# quick-guide

**Objective.** After this chapter a reader takes a project, new or existing, from an empty host session to its first delivery committed, step by step, with no repository to open and one pointer per step to the chapter that teaches it.

**Behaviour.**

* A reader with an empty repository and Claude Code follows the "New project" column from top to bottom: install, `/brainstorm`, read and commit the documents, `/propose <first slug>`, read the page, `/apply <first slug>` in a fresh session, read the diff, commit. Each step is one line of what to type or do, one line of what they see when it worked, and a pointer to the chapter that explains it. They do not need to open any other chapter to finish.
* A reader with a repository that already has code follows the "Existing project" column: install, put what the code cannot say in `context/`, `/analyze`, check every observed statement against the code, commit the documents, then the same `/propose`, `/apply`, commit loop. The column says what the first delivery is when code already exists: there is no skeleton to build, so the first line is the smallest change the first milestone needs, and the verify command is the one `/analyze` observed.
* On an existing project the column answers, in one line each, what happens to the tests and CI already there (they are the verify command, or part of it, as `/analyze` records them), what happens to the backlog already there (it is read into the first milestone by `/analyze`, three to eight lines, and the rest waits in its tool), and that nothing else in the repository changes until a delivery touches it.
* The reader sees, before the first `/propose`, the git choice they have to make (trunk, a branch per delivery or a worktree per delivery), with the default `/brainstorm` and `/analyze` write for them, and a pointer to chapters 20 and 21; they are not taught git here.
* The reader finds the first commit named: after `/brainstorm` or `/analyze`, the documents, `AGENTS.md` and the host's files are the first commit, made by the person, with a one-line message the chapter gives as an example written for it.
* Failure: a reader who types `/apply` in the same session that ran `/propose` finds the step that says a fresh session, with its reason in five words and the pointer to chapter 15; the chapter never narrates what happens when they do not.
* Failure: a reader whose host is Codex or Windsurf finds the form of each command for their host in the same table chapter 11 gives, reduced to the "You type" column; the guide does not repeat the hosts' file layout.
* Edge: a reader who stops after the first commit of the documents has a project the kit can resume in any later session; the chapter says so in one sentence and nothing more about resuming.
* Edge: the chapter ends with when to stop a pilot, in one short section: the three signs the method is not paying on this project (the pages are written and not read, the queue is not the plan the team follows, "done" is still said without verify) and what to do with the documents when it stops (they stay; they are the project's documentation either way).
* Failure: a reader looking for why a step exists finds only the pointer; the guide explains nothing twice. Any sentence that explains a rule instead of giving the step is out of this chapter.
* A reader who has only read chapter 12 understands every term in the chapter: slug, page, line, mark, verify, fresh session are all introduced before it (chapters 10 to 12) or named with the chapter that introduces them (13 to 15).

**Contract.**

* **New chapter, both editions,** `book/en/12a-quick-guide.md` and `book/pt/12a-quick-guide.md` (title en: "12a. From zero to the first delivery"; pt: "12a. Do zero à primeira entrega"), placed after chapter 12 in Part II under a temporary number: no other chapter moves; `renumber-chapters` gives it its final number and closes the merges' gaps in one pass. docs/00's Contents lists it after chapter 12 with the temporary number; `work/done/` and earlier ADRs keep their numbers as history.
* **Shape** (docs/04 §Chapter shape): front matter `status: draft` until done; opening of at most three sentences; sections:
  1. `## Before you start`: what you need (a repository, a host from chapter 11's table, the kit installed with the one sentence chapter 11 gives), and the git choice stated as a default with the two chapters that teach the alternatives.
  2. `## A new project`: a numbered list of eight steps. Each step is three lines in the source: what to type or do, in the host's form; what you see when it worked; the pointer, as "chapter N" with the chapter's own words for the step. Steps: install; `/brainstorm`; read the documents against the checklist of chapter 12's "Review before you commit" and commit them (the example message, written for the chapter: `docs: the project's documents, by /brainstorm`); `/propose <slug>` for the queue's first line; read the page as chapter 14 says; `/apply <slug>` in a fresh session; read the diff and the suggested message; commit.
  3. `## An existing project`: the same list with the steps that differ: `context/` before `/analyze`; `/analyze`; check observed statements against the code; the first delivery when code exists (no skeleton; the smallest change the first milestone needs; the verify command is the observed one); what the existing tests, CI and backlog become; then the shared loop, pointed back to the list above and not repeated.
  4. `## The loop after the first delivery`: three lines: the next line is the first free line (chapter 13), each delivery is page, build, commit, and a milestone closes with its review (chapter 17); `renumber-chapters` moves these pointers with every other.
  5. `## When to stop a pilot`: the three signs and what stays, in at most six lines.
  6. `## What the team gains`: one sentence; there is no number for this chapter, and it says so as docs/04 allows.
  7. `## Key points`: at most five.
* **Host forms:** a two-column table, host and what you type for `/propose <slug>`, taken from chapter 11's table and kept to 74 columns; the chapter says the other three commands follow the same form. The install sentence is the one chapter 11 gives after `ch11-update-2026-10-16-2`, quoted once.
* **No repository, no run, no artifact quoted** except the one example commit message, said to be written for the chapter (ADR-0017, docs/04 §Evidence). No code.
* **Terms:** slug, page, queue line, mark, verify, fresh session, free line, milestone, review, manual, context folder, as docs/03 has them; docs/03 unchanged. "Pilot" is used as chapter 25 uses it, in plain words, and gets no row.
* **Sources:** none new. No note: every claim is the kit's rule, named by the chapter that teaches it. The kit's SETUP.md (Version 2026.10.16.2) and README are the source of what each command does and asks; the chapter names no version (docs/04 §The kit as it is).
* **Cases:** none. The lending library is named only where a slug is needed as an example (`lend-book`, as chapter 12's milestone has it; pt `emprestar-livro`).
* **Cross-references:** chapter 12's opening gains nothing; chapter 25 ("Adoption") gains one sentence pointing to this chapter for the steps, in the section that lists its five steps, and loses nothing else here (its cuts are `ch22-26-team-cut`).
* **docs/00:** the Contents table gains the chapter in Part II; docs/06's M15 paragraph already names it.

**Out of scope.**

* Teaching any step: each step points to its chapter; a reader who needs the why opens it.
* Git beyond naming the choice: chapters 20 and 21.
* Adoption in a company, roles and the pitch: chapter 25, cut in `ch22-26-team-cut`.
* Any renumbering: `renumber-chapters` numbers this chapter and closes the gaps the merges leave; this delivery moves no file but its own.
* A worked example repository or tags: ADR-0017.

**Done when.**

* [ ] Both editions written, same file name and headings; opens with its value; no step explains a rule, every step points to one chapter; no filler and nothing useful cut.
* [ ] A person following the "New project" column on an empty repository with Claude Code reaches a committed first delivery with no other chapter open (the author's own check, by reading, since the book narrates no run).
* [ ] No other chapter file moved; the chapter builds after chapter 12 on the site, in the PDF contents and in the EPUB under its temporary number; docs/00's Contents lists it; chapter 25's pointer added.
* [ ] Every host form matches chapter 11's table at the time of the build; the install sentence matches chapter 11.
* [ ] `make verify` green; `make book` builds, the PDF contents of both editions still fit on one page, and both PDF paths are given to the author.
* [ ] Page in `work/done/`, the line `[x]`, staged by its paths and its hunk of docs/06, the commit suggested in a `commit` block.

**Decisions taken from the documents.**

* Placed after chapter 12 as the queue line says; numbered by `renumber-chapters`, the one pass the author chose over the per-delivery renumbering `queue-states` did for chapter 16 (ADR-0017 amendment 2026-10-05).
* Steps carry pointers and no explanation: docs/04 §Chapter pointers allows a pointer back "where the pointers are the content, a map of where each step is taught", the case of chapter 9's rules and chapter 25's steps.
* No note and no number: docs/04 §Source notes and §A gain per chapter.
* The pilot's stop signs are placed here and not in chapter 25, because the reader who runs the first delivery is the one who decides whether to run the second; chapter 25 keeps the company's view.
* The first commit's example message follows docs/05 §6's form of this repository only in spirit; the chapter says the project's own docs/05 owns its format.

**Decisions in the review.**

* Numbering: the author chose one renumbering at the end. This delivery shifts no chapter: the file is `12a-quick-guide.md` in both editions, its H1 carries the temporary number "12a." so the site, the PDF contents and the EPUB order it after chapter 12, and `renumber-chapters` gives it its number with the merges' gaps. Chapter 25's pointer names it "the chapter after 12" until then. If a check of `make verify` rejects the temporary number, /apply reports it and the line waits as `[?]`.
* Title: "From zero to the first delivery", as recommended.
