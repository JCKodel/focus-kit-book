# ch11-14-queue-tree

**Objective.** After chapters 11 to 14 the reader, developer or not, can ask what may run now and read the answer the kit gives: the queue tree that the kit's queue script draws from docs/06, the current milestone with each line under the last line it waits on and its state, ending with the lines free for `/apply` and for `/propose` together and the lines without a token, judged first; and knows that `/propose` and `/apply` typed with no slug show that tree and ask, that `/apply` ends with it, and that the free lines are offered as one command with several slugs, each slug one more agent costing as much as one session.

**Behaviour.** What the reader can do or explain after the four chapters:

* Asked "what may run now?", say that the agent runs the kit's queue script as one line, `git -c "alias.fq=!sh .agents/skills/propose/scripts/queue.sh" fq <strategy>`, the same alias trick and the same strategy word as the claim script of chapter 13, shows its tree and edits nothing; on trunk it reads the queue of the folder where the session runs.
* Read chapter 14's tree of the library's first milestone on one afternoon: `return-book` and `my-loans` drawn under `lend-book`, which they wait on, each saying `waits: after lend-book`; `lend-book` and `reservations` in flight, by the command their mark names; `due-reminder` blocked, with its reason and the command that resumes it; `search-catalog` free to build and `m1-review` free to define now; no `[x]` line shown; and the last lines: nothing free together, and `search-catalog` and `m1-review` listed to judge first, since neither carries a token.
* Judge those two as the kit says, from the page and docs/01, by the files each touches: `search-catalog` builds in `src/features/catalog/`, which no line in flight touches, so it can be built beside them; `m1-review`'s page takes every delivery of the milestone, clause by clause, so it waits until the lines above are defined, as a `-` in its token's first place would say.
* Say where a line with two pending lines in its `after` sits: under the lower of the two in the queue, with the other named after `+ after`.
* On chapter 14's four lines with tokens (`lend-book` `[*]`, `search-catalog (PA)` and `renew-loan (P-)` both `[ ]`), say that the tree ends with `free for /propose, together: search-catalog renew-loan`, and that the agent offers it as one command, `/propose search-catalog renew-loan`, saying each slug is one more agent and costs as much as one session.
* Say that `/propose` and `/apply` typed with no slug show the tree and ask which line to take; with a slug they run on that line as before.
* Say how `/apply` ends: its last next step is what may run next, the queue tree and its offer; in chapter 13's `lend-book` example, with `lend-book` `[x]`, `return-book` and `m1-review` are free for `/propose` and carry no token, the review is judged to wait, and the command given is `/propose return-book`, in a fresh session.
* In chapter 11, say that the queue script draws `return-book` under `lend-book` while `lend-book` is not `[x]`: the `· after` written with the line is what puts it there.
* Failure: asked "the tree says `m1-review` is `propose now`, so may I define it beside `reservations`?", answer no: a line with no token is judged first, and the review's page takes the pages of the lines above.
* Failure: asked "the tree shows `free for /propose, together: none`, so is nothing free?", answer no: lines without a token are never listed together; they are listed to judge first.
* Edge: a line `[x]` is not drawn, and the tree is of the current milestone only, the first with a line not `[x]`; chapter 13's `suspension-end`, under milestone 2, does not appear.
* In the Portuguese edition, read the same tree with the edition's slugs and milestone heading, the script's own words in English as it prints them, and the chapter saying so before the block.

**Contract.** Eight files: `book/en/` and `book/pt/` `11-queue-and-milestones.md`, `12-propose.md`, `13-apply.md`, `14-queue-states.md`. Line numbers are at HEAD `914fc75`, en, with pt where it differs; one sentence per line; each change replaces only the quoted words, the rest of each sentence staying. The English text below is the text to write; the Portuguese is its translation, with docs/03's Portuguese terms (`árvore da fila`, `linha livre`, `token de paralelismo`), the Portuguese edition's own slugs and folders (`emprestar-livro`, `devolver-livro`, `meus-emprestimos`, `buscar-catalogo`, `reservas`, `aviso-prazo`, `renovar-emprestimo`, `src/features/catalogo/` as the pt chapter already writes it), and every code block exact as given or as the script prints it.

The two trees are the real output of the installed `.agents/skills/propose/scripts/queue.sh trunk`, run by /apply in a scratch repository outside this one whose `docs/06-*.md` holds, under ch11's milestone heading (en :42, pt :44), chapter 14's nine lines (en :38-46, pt :39-47); /apply runs it once per edition and copies the output verbatim, the chapter saying the queue was written for it. When this page was written the output was, en:

```
milestone: Milestone 1: a librarian lends and takes back
[*] lend-book · in flight: apply
 └[ ] return-book · waits: after lend-book
 └[ ] my-loans · waits: after lend-book
[>] search-catalog · apply now, no token: judge
[~] reservations · in flight: propose
[?] due-reminder · blocked: what provider?, then propose
[ ] m1-review · propose now, no token: judge

free for /apply, together: none
free for /propose, together: none
judge first, no token: search-catalog m1-review
```

and pt:

```
milestone: Marco 1: um bibliotecário empresta e recebe de volta
[*] emprestar-livro · in flight: apply
 └[ ] devolver-livro · waits: after emprestar-livro
 └[ ] meus-emprestimos · waits: after emprestar-livro
[>] buscar-catalogo · apply now, no token: judge
[~] reservas · in flight: propose
[?] aviso-prazo · blocked: qual provedor?, then propose
[ ] m1-review · propose now, no token: judge

free for /apply, together: none
free for /propose, together: none
judge first, no token: buscar-catalogo m1-review
```

The quoted last line for the four token lines is the same script's output on chapter 14's four-line block (en :96-99, pt :97-100) under the same heading, both run when this page was written: en `free for /propose, together: search-catalog renew-loan`, pt `free for /propose, together: buscar-catalogo renovar-emprestimo`. Chapter 13's step 4 states what the script prints on ch11's milestone (en :49-54) with `lend-book` `[x]`: `return-book` and `m1-review` both `propose now, no token: judge`, nothing together.

* **`14-queue-states.md`**
  * **C1, the opening** (:3): "name the next delivery, and say which lines can run at the same time and read the two letters a line may carry that say it." becomes "name the next delivery, say which lines can run at the same time from the queue tree the kit's script draws, and read the two letters a line may carry that say it."
  * **C2, "The next line, and which run together"** (:70): "`lend-book`, `search-catalog` and `reservations` are free;" becomes "`lend-book`, `search-catalog`, `reservations` and `m1-review` are free;", since by the rule `m1-review`, with no `after`, is free, and the tree shows it so.
  * **C3, same section** (:84): "Asked what can run at the same time, you answer from the queue: the free lines, by their tokens where they carry one, else those that touch different files, judged from their pages and from docs/01, which says where each part of the code lives." becomes "Free lines can run at the same time when they touch different files, judged from their pages and from docs/01, which says where each part of the code lives." :85 and :86 stay; :88 onward reads on from it.
  * **C4, a new section after :120** ("[Chapter 19](19-worktrees.md) shows how two sessions run in one folder, and when they need two."), titled `## What may run now` / `## O que pode rodar agora`, before "## Waiting: `[?]`":
    * "Asked what may run now, the agent does not read every token and the end of every line for its `after`: it runs the kit's queue script, `propose/scripts/queue.sh`, in one line, `git -c "alias.fq=!sh .agents/skills/propose/scripts/queue.sh" fq <strategy>`, the same alias and the same strategy word as the claim script of [chapter 13](13-apply.md)."
    * "The script reads docs/06 and edits nothing: on trunk the queue of the folder where the session runs, and with a branch or a worktree per delivery each delivery's line where it lives, as the section above says ([chapter 19](19-worktrees.md))."
    * "It draws the current milestone, the first with a line not `[x]`, as a tree, the queue tree: each line not yet `[x]`, under the last line it waits on, the one furthest down the queue of the pending lines its `after` names, with the others named after `+ after`, and its state; then the lines free for `/apply` and for `/propose` together, and the lines without a token, to judge first."
    * "On the milestone at the top of this chapter, chapter 11's milestone 1 with the lines written for this chapter, it prints this, the milestone's heading first:" (pt adds, before the block, one sentence saying the script's words stay in English, as the kit prints them, as pt :36 says of the suffixes.)
    * the tree block, as above.
    * "The `└` draws a line under the one it waits on: `return-book` and `my-loans` wait on `lend-book`, and say so; `lend-book` and `reservations` are in flight, under the command their mark names; `due-reminder` is blocked, with its reason and the command that resumes it; `search-catalog` may be built now and `m1-review` defined now."
    * "Neither carries a token, so no line is offered together, and the last line lists both to judge first, from the page and docs/01, by the files each touches: `search-catalog` builds in `src/features/catalog/`, which no line in flight touches, so it can be built beside them; `m1-review`'s page takes every delivery of the milestone, clause by clause ([chapter 15](15-closing-a-milestone.md)), so it waits until the lines above are defined, as a `-` in its token's first place would say."
    * "On the four lines with tokens above, before `renewal-notice` was added, the script ends with `free for /propose, together: search-catalog renew-loan`, and the agent offers it as one command, `/propose search-catalog renew-loan`, saying each slug is one more agent and costs as much as one session ([chapter 12](12-propose.md))."
    * "`/propose` and `/apply` typed with no slug show the same tree and ask which line to take, and `/apply` ends with it."
  * **C5, "What the team gains"** (:213): "the free lines, their tokens and the files they touch answer it from the queue, without a meeting," becomes "the queue tree draws it from the queue, without a meeting, each line under what it waits on, and lists the lines to judge first,".
  * **C6, "Key points"**: a new bullet after the free-line bullet (:218): "* Asked what may run now, the agent runs the kit's queue script and shows its tree: the current milestone, each line not `[x]` under the last line it waits on with its state, then the lines free for `/apply` and for `/propose` together and the lines without a token, judged first by the files they touch; it offers the free lines as one command with several slugs, each slug one more agent costing as much as one session, and `/propose` and `/apply` typed with no slug show the tree and ask."
* **`13-apply.md`**
  * **C7, "What `/apply` does"**: a sentence after :21 (pt :21), ending that paragraph: "Typed with no slug, `/apply` shows what may run now, the queue tree of [chapter 14](14-queue-states.md), and asks which line to build."
  * **C8, "What it reads"** (:36): "and it names the next free line when it ends." becomes "and it ends with what may run next, the queue tree."
  * **C9, the last-words bullet** (:119): "and take the queue's next line, with its command written as your host invokes it, in a fresh session," becomes "and then what may run next: the queue tree, with its free lines offered as one command written as your host invokes it, for a fresh session,".
  * **C10, the `lend-book` next steps, item 4** (:168): "4. The queue's next free line is `return-book`; in a fresh session, run `/propose return-book` in Claude Code, or `$propose return-book` in Codex (chapter 8's table)." becomes "4. What may run next, from the queue tree: `return-book` and `m1-review` are free for `/propose`, and neither carries a token, so the agent judges them first; the review's page takes every delivery of the milestone, so it waits, and the command is `/propose return-book`, in a fresh session, in Claude Code, or `$propose return-book` in Codex (chapter 8's table)."
  * **C11, "Key points"**: the first bullet (:283) gains, after "`/apply a b` opens one subagent per slug, in the one folder on trunk or each sent to its worktree's path,", the clause "and `/apply` with no slug shows the queue tree and asks,"; the next-steps bullet (:287) "its last words are your next steps, using what it built first, each command written out," becomes "its last words are your next steps, using what it built first and what may run next last, the queue tree, each command written out,".
* **`12-propose.md`**
  * **C12, the opening** (:6): "and say what the command may let them decide alone or build." becomes "and say what each costs and what the command may let them decide alone or build."
  * **C13, "What `/propose` does"**: a sentence after :24: "Typed with no slug, it shows what may run now, the queue tree the kit's script draws from docs/06 ([chapter 14](14-queue-states.md)), and asks which line to define."
  * **C14, "Several lines in one command"**: two sentences after :154: "Each slug is one more agent, and each costs as much as one session of its own." and "Asked what may run now, or typed with no slug, the agent offers the free lines as one such command, and says so (chapter 14)."
  * **C15, "Key points"**: the `/propose` bullet (:191) gains, before "never writes code,", the clause "typed with no slug shows the queue tree and asks,"; the `/propose a b` bullet (:192) "`/propose a b` opens one subagent per slug," becomes "`/propose a b` opens one subagent per slug, each one more agent costing as much as one session, the free lines being offered as one such command,".
* **`11-queue-and-milestones.md`**
  * **C16, "Size and order"**: a sentence after :88 (pt :91), "That is an order, not a wait: ...": "The kit's queue script draws that order: while `lend-book` is not `[x]`, it shows `return-book` under `lend-book`, each line under the last line it waits on (chapter 14 reads the tree)."
* Unchanged, checked: ch14 :62, :72-73, ch12 :28 and ch13 :38 (reading the queue off trunk, `ch19-queue-branches`' subject; C4 only points to chapter 19); ch14 :105's "a line without one is judged from the pages, as above", which now points to C3; ch14 :107 (several slugs and tokens, still true); ch12 :34 (with a slug, `/propose` ends on its line); ch13 :145; ch11 :84 and the key points of ch11.
* Terms of docs/03: `queue tree` / `árvore da fila`, `free line`, `parallel token`, `subagent`; none new, no row changed. Sources: no new footnote; the script and its alias are the kit's installed files, docs/05 §4 :110-117 and docs/03's `queue tree` row. Cases: none; every example is the lending library's, written for the chapter. No number.

**States.** Inapplicable: chapters, no screen.

**Visual reference.** Inapplicable as a design; the tree's `└` (U+2514) is a character no chapter has shown before, so its rendering is proved as docs/05 §5 says (Done when).

**Out of scope.**

* Chapter 8, including :153's "`/apply` names the queue's next line", which this version makes stale: `ch08-update-2026-10-24`'s file.
* Chapter 19 and how the script reads branches off trunk, the default branch and "only on a branch": `ch19-queue-branches`.
* Chapter 17's "where are we?" answer (:68, :120-128): the AGENTS.md bullet, which the kit left unchanged, answers where things stand, not what may run now; its `m1-review` shown as next free agrees with C2.
* Chapter 10's quick guide: its steps name no next line of `/apply` and stay true.
* Giving `m1-review` an `after` in the library's blocks (ch11 :54, ch14 :46): the kit does not require one, and it would make chapters 15 and 17's blocks disagree.
* The changelog's story and numbers: the book teaches the kit as it is, with no numbers for a kit change (docs/04, "The kit as it is").
* docs/03, docs/05 and ADR-0018: already at 2026.10.24 by `kit-2026-10-24`.

**Done when.**

* [x] C1 to C16 read as the Contract says in both editions, each quoted text found once before its edit; the rest of the eight files unchanged.
* [x] Both trees are the installed script's output on the scratch queues the Contract names, copied verbatim, the scratch outside this repository; the four-line block's last line checked the same way; the output recorded on this page.
* [x] Both editions written, Portuguese names in the Portuguese edition, the script's words in English with the sentence before the pt block.
* [x] Each chapter still opens with its value; no filler and nothing useful cut; no number added; no private case; no em dash; no run narration, version, date or commit hash in chapter text.
* [x] Every new block keeps to 74 columns in both editions.
* [x] `make verify` green after the last edit.
* [x] The tree's `└` renders: screenshots of chapter 14's tree on the site in light and dark and in the PDF, both editions, saved as `work/done/ch11-14-queue-tree-<edition>-<what>.png`; if the glyph does not render, /apply stops and the line waits for a toolchain line, as docs/05 §6 says.
* [x] `make book` builds both editions after the last verify, both PDF paths recorded.
* [x] Delivery review by one read-only Opus agent that keeps the session's advisor, over `git diff HEAD` of the eight files and this page, against the page and docs/04, as docs/05 §5 says, what it read and what its report says of the advisor recorded; only this delivery's paths and its docs/06 line staged; the page moved to `work/done/` and its commit message suggested.

**Decisions from the documents.**

* What may run now is answered by running the script and showing its tree, a line without a token judged first by the files it touches, the free lines offered as one command with several slugs, each slug one more agent costing as much as one session: docs/05 §4 :110-117, in its words.
* `/propose` and `/apply` with no slug show what may run now and ask; `/apply` ends with what may run next: `.claude/skills/propose/SKILL.md` :13 and `.claude/skills/apply/SKILL.md` (slugs sentence and last paragraph).
* The tree's content, `+ after`, the current milestone only, `[x]` lines left out, the state words: the installed `queue.sh` and docs/03's `queue tree` row; the chapter's examples are its real output.
* The term is "queue tree" / "árvore da fila", chosen in `kit-2026-10-24`'s /propose (`work/done/kit-2026-10-24.md`).
* The script's words stay English in the Portuguese edition, and the library's names are translated: docs/04, Evidence ("Commands and their output stay as they are").
* `m1-review` stays without an `after`: docs/05 §8 and the brainstorm template plan the review as the milestone's last line with no `after`, and docs/05 §4 judges a line without a token from its page; the review's page takes every delivery's page (docs/05 §8), so judging it is the example of "judged first". Chapter 17 :127 already shows it next free while `return-book` is `[*]`, when every page above is defined, which this judgement agrees with.
* The book teaches the kit as it is, no before and after, no changelog numbers: docs/04, "The kit as it is".
* A new kind of content proves it renders, site light and dark and the PDF, both editions: docs/05 §5, Proof of a screen.
* Token `(PA)` stays: this definition takes nothing from `ch08-update-2026-10-24`'s or `ch19-queue-branches`' pages, and the build touches only chapters 11 to 14, none of their files (chapter 8 and chapter 19); its `after`, `kit-2026-10-24`, is `[x]`.

**Decisions taken alone.** The agent chose each of these; correct them in the review.

* The tree is taught once, in chapter 14, on the chapter's nine-line milestone, since it shows every state and the "judge first" line; chapter 14's four token lines give only the script's last line, for the offer; chapter 13 states the tree's answer in its step 4 in prose, with no second block, and chapter 11 gets one sentence where `after` is taught.
* The new chapter 14 section, "What may run now", follows the section on tokens, since the tree's words use tokens; C3 keeps the rule for lines without a token where it was.
* The English text is written on this page and the Portuguese left to /apply as its translation, with the Portuguese blocks, names and terms fixed here: eight files would double the page with no decision in the second half.
* No tree block in chapter 13, to keep one place that teaches the tree; the step names the command as before.
* No change to ch11's key points: the tree is chapter 14's lesson, and ch11's `after` key point stays true.

## What happened

**The trees.** A scratch repository per case, outside this one, in the session's scratch folder: `git init`, a `docs/06-Queue.md` holding ch11's milestone heading (en :42, pt :44) and the lines copied from the chapter at HEAD, one commit; then the installed `.agents/skills/propose/scripts/queue.sh trunk`, run in it. Five runs, each output equal byte for byte to the one this page quotes: chapter 14's nine lines, en (:38-46) and pt (:39-47), the two trees above, copied into the chapter verbatim; the four token lines, en (:96-99) and pt (:97-100), whose output is

```
milestone: Milestone 1: a librarian lends and takes back
[*] lend-book · in flight: apply
[ ] search-catalog (PA) · propose now
[ ] renew-loan (P-) · propose now

free for /apply, together: none
free for /propose, together: search-catalog renew-loan
```

and in pt the same with `emprestar-livro`, `buscar-catalogo (PA)`, `renovar-emprestimo (P-)` and `free for /propose, together: buscar-catalogo renovar-emprestimo`; and ch11's milestone (en :49-54) with `lend-book` `[x]`, which prints `return-book` and `m1-review` both `propose now, no token: judge`, `free for /propose, together: none` and `judge first, no token: return-book m1-review`, what C10 says in prose.

**The edits.** C1 to C16 in both editions, each quoted text counted once in its file before its edit. ch13's first key-point bullet, which the Contract places at :283, is at :284 at HEAD; the next-steps bullet is at :287, as the Contract says; the quoted texts were found once there. The Portuguese follows the Contract's names and docs/03's terms; the alias's placeholder is `<estratégia>`, as pt ch13 :24 already writes the claim script's; the sentence before the pt block says the script's words stay in English, as the kit prints them, like the suffixes (pt :36).

**The glyph.** `pandoc/fonts/IosevkaTerm-Regular.ttf`, the PDF's code font, maps U+2514, and the `└` renders in the tree and inline in the site, light and dark, and in the PDF, both editions: `work/done/ch11-14-queue-tree-<en|pt>-<site-light|site-dark|pdf>.png`. The site shots are of a copy of the built page in the scratch folder, served on a port of its own, with the sections before "What may run now" removed so the section opens the shot (headless Chrome renders blank when it scrolls to an anchor); the PDF shots are English page 152 and Portuguese page 161.

**Divergences.**

* C6 gives chapter 14 a sixth key point; docs/04's chapter shape says at most five. The page is followed, as its Contract is exact; the same rule is already passed by chapters 1 (seven), 12 (six before this delivery, the same six after), 21 and 24 (six each). Reported for the person: either docs/04's "at most five" changes or those chapters, 14 included, fold their key points; no line added, since the choice is the person's.
* Two sentences of the Contract's English, corrected after the review in both editions: C4's "the same alias" is "the same alias trick", since the claim script's alias is `fk` and the queue script's `fq` (the Behaviour's own words); C4's and C10's "`m1-review`'s page takes every delivery of the milestone" now says what chapter 15 and docs/05 §8 say, that the review's page takes the milestone's paragraph clause by clause and names the delivery that answers each (C10: "names the delivery that answers each clause of the milestone"), pt with chapter 15's "pega" and "atende".

**Decisions taken in /apply.**

* The pt alias placeholder is `<estratégia>`, as pt chapter 13 writes it for the claim script.
* The pt sentence before the block is its own sentence after "o título do marco primeiro.", so the en sentence keeps its colon and the pt block follows the note.
* No `[ ]` line for the review's docs/04 questions (key points, pointers): they ask the person to choose between the rule and the chapters, so they are reported, not queued as a fix.

**Delivery review.** One read-only Opus agent read this page, docs/04, docs/03's three rows, docs/05 §4 :105-120, this line's hunk of docs/06, `git diff HEAD` of the eight chapters with their context, chapter 15 :18 in both editions, the installed `queue.sh` and the skills (by grep), the check scripts, and the six screenshots; it reran the five scratch trees outside the repository, byte-equal, and the parity, em dash, prose and width checks, all green. Its report says it had the advisor and called it once before writing, which agreed the mechanical checks held and pointed it to the chapter 15 wording, the six key points, the pointer counts and the record's line numbers. No blocking finding. Fixed: "the same alias" (an error in the text), the review page's description against chapter 15 (in ch14 and ch13), and this record's ch13 line number. Left for the person, each following the Contract's text: ch14's sixth key point against docs/04's "at most five" (above); docs/04's "once per chapter for each target", which C4's second pointers to chapters 19 and 15 pass, as chapters 11 to 13 already do with chapter 14; wording only, ch13 :284's "and `/apply` with no slug shows the queue tree and asks, reads docs/00" making the subject of "reads" less clear, ch12 :192's added clauses, and ch14's "under the command their mark names" using the tree's word "under" in another sense. Out of scope, noted: how the script reads a delivery's line off trunk (`ch19-queue-branches`).

**Proof.** `make verify` green after C1 to C16, and again after the review's fixes, this page's move and the `[x]`, the last covered edits; `make book` after that last verify: `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`. Nothing acts outside git: reverting the commit undoes the delivery.

```commit
docs(ch11-14-queue-tree): teach the queue tree in chapters 11 to 14

- ch14: new section "What may run now", the script's real tree
- ch13 and ch12: no slug shows the tree; /apply ends with it
- ch12: each slug one more agent, as much as one session
- ch11: the script draws `after` as the tree's order
- both editions; the glyph proved on the site and in the PDF

work/done/ch11-14-queue-tree.md
```
