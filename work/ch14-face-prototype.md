# ch14-face-prototype

**Objective.** A reader of chapter 14's "The queue as a kanban board" learns, in one short paragraph, that a board can read the queue straight from the repository, with no mirror, and where to open one: FACE, the author's prototype, at <https://face.kodel.com.br>. Both editions. From the author's reading of the book on 2026-10-18: "show briefly <https://face.kodel.com.br>, the author's prototype that operates on focus-kit. Brief: what it is and that it reads the queue; no more than the section needs. Check the URL answers (the link check runs on it)."

**What the page shows** (fetched 2026-10-18, HTTP 200, English at the root, Portuguese at `/pt/`): FACE, "Focus Agentic Code Environment", is a free program, one binary for macOS, Linux and Windows, run in the folder that holds a person's projects; it plants focus-kit in each project, talks to the coding agent the person already uses, and shows in the browser "the queue, the pages, the sessions, the cost and the diff". Its board is "the queue in five lanes, one milestone at a time", and "marks move while the agent works, not after". "Board, pages, progress and cost are projections of your repository." No account. Version 2026.10.14.1, "without warranty".

**Decided without the author.** The batch had no one to answer; each choice is the recommended one.

1. *"Prototype" stays, as the author's word.* The page does not call FACE a prototype: it shows a dated version, installers and six languages. The draft and the queue line both say "the author's prototype", and the author is the one who can say what state their own program is in, so the chapter says "a free prototype the author is building". If the author now reads it as released, the review changes one word per edition. Source: the draft; docs/06's line; the page.
2. *A source note, not a bare URL in the text.* The section already cites by note (`[^toyota-kanban]`, `[^azure-kanban]`), and a tool the reader can open is what a note is for. Key `face`, in the existing format: en `[^face]: J.C. Ködel, "FACE: agents write the code, your team keeps the thread", accessed 2026-10-18. <https://face.kodel.com.br>`; pt the same with `acesso em 2026-10-18`. The author's name already signs notes in chapters 19 and 24. Source: docs/04 §Source notes (lines 140 and 146); book/pt/19-worktrees.md:332.
3. *One URL, the root, in both editions.* The existing notes of the section use one URL in both editions, and the root is the site's `x-default`; the site offers its own language switch. Source: book/*/14-queue-states.md notes; the page's `hreflang` links.
4. *Placed after the pointer to chapter 20, as a contrast to it.* The section ends on Case A's error and "Chapter 20 shows how a script mirrors the queue to a team's own board, one way." FACE is the other way to the same board: it reads docs/06 itself, so there is nothing to mirror. The new paragraph goes right after en 14:120 / pt 14:121 (at /propose), and says nothing of Case A's board or chapter 20's script, which those lines already say. Source: book/en/14-queue-states.md:119-120; book/en/20-team-tools.md:55; the brief's "avoid saying a thing twice".
5. *No lane count.* The page says five lanes and lists six marks without the mapping; the chapter teaches six columns, or three folded. A number the text cannot explain raises a question it does not answer, so the line says "as a board" and stops. Source: the page; book/en/14-queue-states.md:105-107.
6. *Nothing from the page beyond what FACE is.* The page also tells Ninjobs's stack and a consulting engagement's counts; none enters the chapter: Case A's numbers are the author's count (the prologue) and Ninjobs's infrastructure stays out. No install line, no terminal output, no screenshot. Source: AGENTS.md non-negotiables; docs/03 line 131; ADR-0017.
7. *What it is, said for a reader who does not program.* A free program, run on the person's own machine in the folder of their projects, that reads docs/06 and the pages in `work/` and shows the queue in the browser, its marks moving while the agent works. That is the whole mention. Source: the draft ("what it is and that it reads the queue"); the author's rule to explain the basics first.
8. *The gain section and the key points unchanged.* FACE is a way to read the queue the chapter already teaches; it brings no number and no gain of its own, and the book teaches the kit as it is, without a before and after. Source: docs/04 §The kit as it is (line 29); ADR-0015.
9. *ADR-0005 does not apply.* It forbids the author's earlier books; FACE is a program, and docs/00 and docs/03 already name the author's own product (Ninjobs) where it serves the reader. Source: ADR-0005; docs/00 line 27.
10. No new docs/03 term (FACE is named once, not a concept of the method), no new queue line, no split.

**Behaviour.**

* The reader of chapter 14, in English, under "The queue as a kanban board", after the line "Chapter 20 shows how a script mirrors the queue to a team's own board, one way.", reads a new paragraph:
  * "A board can also read the queue itself, with nothing to mirror."
  * "FACE, a free prototype the author is building, runs on your machine in the folder of your projects, reads docs/06 and the pages in `work/`, and shows the queue as a board in the browser, its marks moving while the agent works.[^face]"
* The reader of the Portuguese edition, under "A fila como quadro kanban", after "O capítulo 20 mostra como um script espelha a fila no quadro do próprio time, numa só direção.", reads:
  * "Um quadro também pode ler a própria fila, sem nada a espelhar."
  * "O FACE, um protótipo gratuito que o autor está construindo, roda na sua máquina na pasta dos seus projetos, lê o docs/06 e as páginas em `work/`, e mostra a fila como um quadro no navegador, com as marcas andando enquanto o agente trabalha.[^face]"
* Each edition ends with the note of decision 2, after `[^azure-kanban]`.
* Checked at apply time:
  * `grep -n "face.kodel.com.br" book/*/14-queue-states.md` prints one note line per edition.
  * `grep -c "\[\^face\]" book/*/14-queue-states.md` prints 2 per edition (mention and definition).
  * `git diff book/` shows, per edition, only the new paragraph and its note.
  * `make verify`'s link check reaches <https://face.kodel.com.br> (200 at /propose).
* Fails: a lane count; a number, a case, a stack or a client detail taken from the FACE page; an install line, a command or terminal output; Case A's board or chapter 20's script said again; the gain section or the key points changed; a `/pt/` URL in one edition only; an em dash.

**Contract.**

* Files: `book/en/14-queue-states.md`, `book/pt/14-queue-states.md`; section "The queue as a kanban board" / "A fila como quadro kanban", new paragraph after en 14:120 / pt 14:121, and the note after `[^azure-kanban]` (lines at /propose; found by their text).
* Terms of docs/03: none new. Sources: one added, `[^face]`, the FACE site, accessed 2026-10-18. Cases: none. Exercises: none (ADR-0017).
* docs/00 to docs/05: no change. docs/06: this line's marks only, set by the driver and by /apply; no new queue line.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Deliveries in flight on the same files.**

* No other M18 page or draft edits chapter 14. `early-no-forward-links` names chapter 14 only as the target of a pointer from chapter 7 (its page, line 28); it does not edit chapter 14, and the new paragraph adds no pointer.
* `ch19-agent-does-git`, `try-before-commit` and the chapter 19 and 21 pages touch other chapters; chapter 21's `.face/` folder names are not explained here (Out of scope).
* Whichever lands first shifts line numbers; the lines are found by their text, not their number.

**Out of scope.**

* What FACE's board, delivery and commit screens do in detail, its cost per delivery, its install: the section needs only that a board can read the queue (the draft: "no more than the section needs").
* Chapter 20's team tools: it teaches the one-way mirror; FACE is named once, where the board is taught.
* The `.face/` and `face/` defaults of chapters 19 and 21: no kit document ties them to FACE in the book, and none is invented here.

**Done when.**

* [ ] Both editions written: the paragraph and the note as Behaviour says.
* [ ] Chapter 14 still opens with its value, keeps its gain, no filler and nothing useful cut.
* [ ] Every number sourced: none added.
* [ ] `make verify` green: edition parity, prose rules, width, links (the FACE URL answers), disclosure scan, no em dash.
* [ ] The author's approval of an anonymized passage: inapplicable, no private case (docs/00 OD-3).
* [ ] `make book` run; both PDF paths given to the author.
* [ ] Page in `work/done/`, the line `[x]`, staged by its paths and its hunk of docs/06, commit message in a `commit` block.
