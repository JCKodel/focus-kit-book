# ch13-apply-reads-00-03

**Objective.** After chapter 13 the reader can say which documents `/apply` reads before it builds, docs/00, docs/01, docs/03, docs/04 and docs/05 besides the page, `AGENTS.md` and docs/06, and what each gives the build: docs/00 the product's rules and open decisions a page may contradict, docs/03 the identifiers the code is written with; and that `/apply` follows every slot of docs/05 §5 literally, the project's own slots included.

**Behaviour.** What the reader can do or explain after the chapter:

* Name the five project documents `/apply` reads, in number order, and why each: docs/00 so it sees when the page contradicts the product and stops at an open decision; docs/01 for where each piece goes and how errors travel; docs/03 for the vocabulary, each term with the identifier the code gives it; docs/04 for the tests; docs/05 for the process and its slots.
* Say why the build uses docs/03's identifiers: the word the page, the tests and the code use is the one the table names, so `loan` in docs/03 is `loan` in the migration and the function, never a synonym the agent picks; a new term enters docs/03 first, as the chapter's "Green is not done" list already says.
* Say which slots `/apply` follows: every slot of docs/05 §5, literally, the ones the kit writes and any the project added of its own; the list the chapter gives (verify, environments, proof of a screen, delivery review, publish policy, git) stays as examples, not as the whole set.
* In the `lend-book` example, see the agent read docs/00 and docs/03 with the other three: docs/00 for the rules a member meets and the open decisions, docs/03 for the names the build uses, `loan`, `lend` and `AlreadyLent`, the same names the next sentence already writes. The paragraph "If docs/00 said a loan lasts 14 days..." then follows from a document the agent was said to read, instead of one it was never said to open.
* Find, in the key points, `/apply` reading docs/00 and docs/03 with the rest, building with docs/03's identifiers and following every slot of docs/05 §5, the project's own included.
* Edge: a reader who has not read chapter 7's project slots still understands "the project's own slots": the clause says what they are in a few words (slots the project added to docs/05 §5 beside the kit's), with no example and no pointer forward or back that only repeats chapter 7.
* Edge: docs/02 and docs/06 are not added to or removed from the list; docs/06 keeps its own sentence (read whole, for the `after` and the next free line).
* Fails: no sentence says `/apply` "now" or "also" reads docs/00 and docs/03, gives a kit version or date, or compares with what it read before (AGENTS.md, M21's rule that the book teaches the kit as it is). No run narrated. No number added.
* Both editions say the same, paragraph for paragraph; `make verify`'s parity check passes.

**Contract.** Files `book/en/13-apply.md` and `book/pt/13-apply.md`, the same changes in both, only these places:

* "What it reads" / "O que ele lê", line 22 (en and pt): "three of the project documents" (pt "três dos documentos do projeto") becomes five, in number order: docs/00, the product, whose rules and open decisions a page must not contradict; docs/01, the architecture, as now; docs/03, the domain, whose table gives each term the identifier the code uses; docs/04, the conventions, as now; docs/05, the process. The sentence may split in two, one sentence per line, as the chapter is laid out; its shape echoes chapter 12's line 25 ("docs/00 for the product and its rules, docs/03 for the words the page must use"), so the two commands read alike.
* Same section, line 23: "docs/05 holds the project's slots, and `/apply` follows them literally: ..." becomes that `/apply` follows every slot of docs/05 §5 literally, the project's own included, slots a project adds beside the kit's, with the current list kept as examples ("among them" / "entre eles"). One sentence, or two at most.
* "`lend-book`, built" / "`emprestar-livro`, construída", line 113: the agent reads the page, then docs/00 for the rules a member meets and the open decisions, docs/01 as now, docs/03 for the names the build uses, `loan`, `lend` and the refusal `AlreadyLent` (pt `emprestimo`, `emprestar`, `JaEmprestado`, as docs/03's `running example` row fixes them), docs/04 and docs/05 as now. No number in the docs/00 clause: line 118 keeps its hypothetical 14 days, and the 21 days stay where the chapter already has them.
* "Key points" / "Pontos-chave", line 264, first bullet: "follows docs/05 literally" (pt "segue o docs/05 ao pé da letra") becomes reading docs/00 and docs/03 with the rest, building with docs/03's identifiers and following every slot of docs/05 §5 literally, the project's own included; the rest of the bullet stays.
* Terms of docs/03: `slot`, whose row already says a project may add one that /propose or /apply follows; page, delivery, line. Identifier in Portuguese is "identificador", as chapter 7 (pt lines 40 to 43) already writes; "the project's own" is "do próprio projeto", as chapters 6 and 7 already write. No new term; no docs/03 row.
* Sources: the installed `.claude/skills/apply/SKILL.md` at `metadata.version` 2026.10.19 ("Read the page, `AGENTS.md`, docs/00 (product), docs/01 (architecture), docs/03 (domain), docs/04 (conventions), docs/05 (process) and docs/06 (queue). Follow every slot of docs/05 §5 literally, the project's own slots included." and "Build where docs/01 says, with its error convention and docs/03's identifiers."), which the chapter already cites as "the kit's file for the command"; docs/05 §5's intro and docs/03's `slot` row for the project's own slots. No new footnote: the reader gains nothing to open beyond the kit file the chapter already names.
* Cases: none. No number. The lending library only, its examples already marked as written for the chapter.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no visual change.

**Out of scope.**

* Teaching how a project adds a slot, and the Board example: `ch07-slots-and-decided`.
* The opening (lines 3 to 5): it lists what "done" means and how `/apply` ends, not what it reads; unchanged.
* "When the page contradicts a document" and line 118's 14-day hypothetical: unchanged, since reading docs/00 is what they already assume.
* The removed skill sentence on another session's delivery not being a conflict; line 133 stays correct under docs/05 §§4 and 6: `ch18-19-one-index` owns the one index.
* Chapter 12's reading list (line 25) and every other chapter: no other chapter repeats `/apply`'s reading list (searched both editions).
* Any other section of chapter 13: it keeps everything else it says.

**Decisions from the documents.**

* The five documents and docs/06, and "every slot of docs/05 §5 literally, the project's own slots included": the installed `/apply` skill, 2026.10.19.
* Building with docs/03's identifiers: the same skill, and docs/03 itself ("Identifier" column) as chapter 7 teaches it.
* A project slot is followed by the command it names, with no edit to the skill: docs/05 §5 intro and docs/03 `slot`.
* Taught as the kit is, with no version, date or "now": AGENTS.md and M21's paragraph in docs/06.
* Portuguese identifiers of the example: docs/03 `running example` row.

**Decisions taken alone.**

* The five documents are listed in number order, each with one clause of what it gives the build, rather than adding docs/00 and docs/03 at the end.
* The slot list of line 23 stays, as examples: it tells a reader of Part II what a slot looks like, and dropping it would cut something useful.
* No pointer to chapter 7 for project slots: docs/04's pointer rule keeps a pointer back only where a specific detail is worth reopening, and one clause defines the project's own slots in place.
* The opening stays unchanged: it states what the reader can do after the chapter, and reading two more documents is part of what `/apply` does, not a new capability of the reader.
* `## What the team gains` unchanged: no evidence beyond what it already gives belongs to this change.
* In the `lend-book` example, docs/00's clause names the rules and open decisions but no number, so the 21 days are not attributed to a document here, where chapters 7 and 12 attribute them differently; that difference is not this line's to settle.

**Done when.**

* [ ] Both editions changed in the same three places, "What it reads" (lines 22 and 23), the `lend-book` example (line 113) and "Key points" (line 264), and nowhere else in chapter 13.
* [ ] The chapter still opens with its value; no filler, nothing useful cut; one sentence per line kept.
* [ ] No version, date, "now", before/after or narration of a run in the text; no em dash.
* [ ] Portuguese uses "identificador", "do próprio projeto" and docs/03's identifiers for the example.
* [ ] No number added, so none to source; no private case used, so no approval needed.
* [ ] `make verify` green; `make book` builds both editions, and both PDF paths reported.
* [ ] Delivery review as docs/05 §5 says; only this delivery's paths and its hunk of docs/06 staged; the page moved to `work/done/` and its commit message suggested.
