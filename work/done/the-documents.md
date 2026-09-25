# the-documents

**Objective.** After chapter 6 the reader can say what each of the seven project documents, the ADRs and `AGENTS.md` hold, decide which one a new fact belongs in, and explain why an agent that reads them in a fresh session builds what was decided.

**Behaviour.**

* The reader can name the seven numbered documents and say in one sentence what each holds and who reads it.
* The reader can take a fact (a rule of the product, a term, a choice of stack, the verify command, a decision with its reason) and say which document owns it.
* The reader can explain one place per fact: a fact written in two places goes stale in one of them (chapter 4), and a fact written nowhere is gone in a fresh session (chapter 2).
* The reader can explain what an open decision is and why docs/00 lists them: so an agent never settles by assumption what belongs to a person.
* The reader can read an ADR and say why it is amended and never rewritten.
* The reader can explain why `AGENTS.md` only points: it is short, it names the documents to read, and no rule lives only there.
* The reader can explain why the commands hold no fact of the project and read docs/05's slots instead.
* The reader can explain living documents: a delivery that changes behaviour updates the document that owns it in the same delivery, and every later session follows the change without being told again.

**Contract.**

Chapter 6, `book/en/06-the-documents.md` and `book/pt/06-the-documents.md`:

* Title: "The documents" / "Os documentos".
* Voice: instruction to the reader as "you"; the living-document story in the first person, a few sentences.
* The chapter is one argument, "the documents do the work", and not a catalog. The seven documents are its middle. Sections, in order (headings may be reworded; both editions keep the same structure):
  1. Opening, at most three sentences: the Objective.
  2. One place per fact. Chapter 2's fresh session reads only files, and chapter 4's six places went stale. So each fact lives in one place, and the set has a fixed shape: seven numbered documents, `docs/adr/`, `AGENTS.md` and `work/`. The numbers are fixed because the commands cite them; the name after the number is in the documentation language.[^focus-kit-documents] No recap of chapters 2 and 4, only the link to them (docs/04, no filler).
  3. The seven documents, one short paragraph each: what it holds, who reads it and when.
     * **docs/00, the product.** Show this book's docs/00 §Product questions whole, then one sentence on what to see: every decision answers yes to all of them. Open decisions in two or three sentences, with this book's OD-3 described (the author approves the anonymized text of a private case), not quoted. This is the term's first use.
     * **docs/03, the domain.** The table is also the vocabulary every page, identifier and test uses; a new concept enters here first. Show one row of this book's table (the row `delivery`), with its header.
     * **docs/01, the architecture**; **docs/02, the backend**: the stack with the reason for each choice, how code is organized, how errors travel, what was removed on purpose; docs/02 only when a server holds rules, else "there is none" (this book's docs/02 is that one line). FOCUS and the git strategy are the two choices docs/01 and docs/05 record: one sentence, pointing to Parts III and IV.
     * **docs/04, the conventions.** One sentence; its excerpt comes in section 6.
     * **docs/05, the process.** The kit's template with this project's slots filled. Show two slots of this book's docs/05 §5 whole, **Verify** and **Git**, then one sentence: `/apply` reads the verify command here, so the command file holds none (chapter 4's later rule). §3 (the page) and §2 (the flow) are named and pointed to chapters 10 and 11.
     * **docs/06, the queue.** One or two sentences, pointing to chapter 9.
  4. ADRs. One file per decision: context, decision, consequences, date. Amended, never rewritten, so the reason survives the next change. Show ADR-0010 whole, then one sentence on what to see.
  5. `AGENTS.md`. Show the part of this book's `AGENTS.md` that chapter 2 did not: `## Non-negotiables`, `## Do not rebuild`, `## How to work`. Chapter 2 showed the lines up to `## Read before acting`, and this chapter shows the rest, never those lines again. Then say the kit's rules: sixty lines at most, everything points at a document, nothing in it is the only place a rule is written.[^focus-kit-documents] `CLAUDE.md` gets one clause at most, pointing to chapter 5.
  6. Living documents. The story: after chapter 3 the author found excerpts without context. The fix went into docs/04 as the rule "Context before an excerpt" (and "Teach, do not only show"), and chapter 5 was written following it without anyone repeating the request. Show docs/04's "Context before an excerpt" bullet whole. Then the rule: a delivery that changes behaviour updates the document that owns it, in the same delivery.[^focus-kit-documents]
  7. Key points, at most five.
  8. Exercises (below).
* Excerpts are English prose artifacts. The Portuguese edition says before each that the original is in English and shows it translated (docs/04 §Evidence), as chapter 2 did with `AGENTS.md`. Each excerpt is preceded by what it is and from where, and followed by one sentence on what to see (docs/04).
* Numbers, and only these: seven (numbered documents); sixty (lines, `AGENTS.md`'s limit), sourced to the kit.
* docs/03 terms used: project documents, rules file, ADR, open decision (new, added by this /propose), slot, verify, delivery, page, queue, fresh session, command, guided project, FOCUS, trunk. The Portuguese edition uses the fixed terms.
* Sources (`[^key]`, same keys in both editions):
  * `[^focus-kit-documents]`: focus-kit's `SETUP.md` §3.5, `references/documents.md`, at `26e5e1e4c8fcc6e059075a51db8cad5ed2028f2b` (as chapter 5). If `main` of focus-kit moved before /apply and §3.5 changed, /apply uses the new head and records it.
  * `[^book-docs]`: this book's repository at `6c2713b63af7397ee00142497287b8408a5651b1`, the source of the excerpts of docs/00, docs/03, docs/05, ADR-0010 and `AGENTS.md`. Each excerpt must match that commit byte for byte. docs/03 changes in this delivery, but not in the `delivery` row.
  * `[^book-docs-context]`: commit `297af60dedb088bad441555c8bc019a60ce4e612` of this book, which added "Context before an excerpt" to docs/04, and `work/done/install-and-hosts.md`, which cites it. Links on GitHub.
* Cases: none. No Ninjobs beyond pointing to chapter 4, no Case A or B. No OD-3 approval.
* Guided project: not changed, no chapter tag (docs/05 §5).
* Exercises, on the guided project (answers belong to the `exercise-answers` appendix, not here):
  * 6.1: at `book-v1/install-and-hosts`, open `.claude/skills/brainstorm/references/documents.md` in the clinic, the kit's own description of the documents. Which of the clinic's documents might read "there is none", and what would decide it?
  * 6.2: write by hand the clinic's docs/00 Purpose paragraph and three non-negotiables, and keep them to compare with what `/brainstorm` writes in chapter 7.
  * 6.3: in this book's `AGENTS.md`, find the document each line points at, and any line that is the only place its rule is written.

Chapter 2 fix, both editions: `book/en/02-how-agents-see.md:82` "Chapter 6 builds these documents for your project." and `book/pt/02-how-agents-see.md:84` become "Chapter 6 explains these documents, and chapter 7 writes them for your project." and its translation. Chapter 7 writes them (chapter 5 and docs/06 agree).

Files:

```
book/en/06-the-documents.md      chapter 6, no status: draft when done
book/pt/06-the-documents.md      chapter 6, no status: draft when done
book/en/02-how-agents-see.md     line 82, the chapter 6/7 sentence
book/pt/02-how-agents-see.md     line 84, the same
docs/03-Domain.md                open decision row (written by this /propose)
docs/06-Queue.md                 the-documents [x]
```

**Out of scope.**

* The queue's marks and milestones: chapter 9.
* The page and the flow of docs/05: chapters 10 and 11.
* FOCUS and the git strategies: Parts III and IV, one sentence here.
* Writing the clinic's documents: chapter 7, `/brainstorm`.
* Reproducing `documents.md` whole: it is the kit's file and it changes, as chapter 5 did not reproduce the hosts table.
* Ninjobs' or a private case's documents: nothing showable, and chapter 4 already told the story.
* The kit's `CLAUDE.md` wording (chapter 5's finding for focus-kit): another repository.

**Done when.**

* [x] Both editions written, same headings in the same order, no `status: draft`.
* [x] Opens with its value in at most three sentences; at most five key points; exercises 6.1 to 6.3.
* [x] No filler and nothing useful cut: every sentence read against docs/00 product question 2.
* [x] Every excerpt matches `[^book-docs]` byte for byte (English), translated in Portuguese with the note; each has context before it and one sentence after it.
* [x] Only the Contract's numbers, sourced.
* [x] Chapter 2 line fixed in both editions.
* [x] `make verify` green (build, parity, em dash, prose, links, disclosure). The links to this book's commits answer once the author has pushed. Any red link that only a push fixes is recorded here.
* [x] `make book` builds; both PDF paths given to the author.
* [x] docs/06 marked `[x]`; page moved to `work/done/the-documents.md` with what happened.

**What happened.**

* Diverged from the Contract, sources: a fifth key, `[^focus-kit-commands]` (`SETUP.md` §3.3 and §3.4 at the same commit), for which documents `/propose` and `/apply` read. Behaviour asks the reader to say who reads each document and when, and §3.5 alone does not say it.
* Diverged from the Contract, section 2: its text says "chapter 4's six places"; the numbers rule allows only seven and sixty, so the chapter says "several places" and links chapter 4.
* docs/02 is quoted whole, "There is none. The book is static; no server holds rules.", two sentences on one line; the Contract called it one line.
* Added beyond the Contract's sections, each for docs/04 (context before an excerpt, teach and not only show): where the excerpts come from and that chapter 7 writes the clinic's set; that the Portuguese term column exists because the book has two editions; that the slugs in the Verify slot are this book's deliveries; what "ADR" stands for; one parenthesis on what a worktree is, pointing to Part IV; that the AGENTS.md lines name the document that holds the rule. The living-document story says the fix went into docs/04 in the same commit as chapter 3's fix, and that chapter 5's delivery cited the rule (its page, "What happened", the two sentences introducing the guided project).
* The docs/05 excerpt is the Verify and Git bullets of §5, not contiguous in the file; the docs/03 excerpt is the header, the separator and the `delivery` row. The Portuguese edition names §5 "This project" in English with the translation in parentheses, since the file's heading is English, and rewraps the translated Verify slot.
* focus-kit's `main` was still at `26e5e1e4c8fcc6e059075a51db8cad5ed2028f2b` (`git ls-remote`, 2026-09-25), so the note cites it unchanged. The clinic path of exercise 6.1 was checked at `book-v1/install-and-hosts`.
* Proof. A script took every fenced block of the English chapter and compared it with `git show 6c2713b:<file>`: docs/00 §Product questions, ADR-0010, `AGENTS.md` from `## Non-negotiables` and the docs/04 bullet match as contiguous text; the docs/03 and docs/05 blocks match line by line. `make verify` green on the first run, links included: `origin/main` was already at `6c2713b` and `297af60` is its ancestor, so no link waits for a push. `make book` built both PDFs and EPUBs with the known `user-select` warnings; the chapter appears in both tables of contents and its chapter links render as text. No new kind of content, so no screenshots (docs/05 §5).
* Author's review, after the first /apply: "Living documents" gains a paragraph in both editions. The documents need no editing by hand: a conversation with the agent fills a gap, fixes a detail, adds, changes or removes, since the documents tell it where each fact lives. The person interprets, guides and validates, and never takes the agent's text on trust, because it reads as right even when it is wrong. Key point 5 says the same in one clause.
* Nothing dropped. No ADR. docs/03 got its `open decision` row from /propose; no other document changed.
