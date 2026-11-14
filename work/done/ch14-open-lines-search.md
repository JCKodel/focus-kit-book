# ch14-open-lines-search

Defined by /propose on 2026-11-14 on the author's word for this run, given on 2026-11-13 and relayed by the driver session: "Precisamos fechar todas as linhas de docs/06-Queue.md sem minha supervisão", close every open line of docs/06 without supervision. So the agent decided alone (docs/05 §4): every question below is answered by the agent's recommendation, and says the agent chose it. This page was written, and will be built, before the person read it; the person reads the page and the diff at the end.

The request is the author's own, of 2026-11-14, in their words: "Adicione onde for melhor no livro: uma dica para visualizar tudo o que está em aberto no documento 06 é pesquisar via regex: `^\[[^x]\]`. Este regex verifica todas as entradas `[ ]` que estão no começo da linha que contenham qualquer caractere exceto `x` (que é o símbolo de concluído), mostrando assim todas as tarefas em aberto, sendo propostas, aplicadas ou bloqueadas." (Add, wherever it fits best in the book, a tip: to see everything open in document 06, search it with the regex `^\[[^x]\]`, which matches every bracketed entry at the start of a line holding any character but `x`, the done mark, so it shows every open task, proposed, applied or blocked.)

**Objective.** After chapter 14 the reader can list every open line of a queue at once, with one search for the regular expression `^\[[^x]\]` in an editor or with `grep`, and say why that list does not tell what may run now.

**Behaviour.** What the reader can do or explain after the chapter, both editions:

* B1. The reader writes the expression and reads it piece by piece: `^` the start of a line, `\[` and `\]` the brackets themselves, `[^x]` any one character but `x`; so it matches a line that starts with any mark but `[x]`.
* B2. Given the nine lines of the chapter's `## Six marks` example, the reader says the search lists seven, every line but `catalog` and `members`: not defined, being defined, defined, being built and waiting, `[?] due-reminder` included.
* B3. Edge, a cancelled line: given `[x] print-card ... · dropped: no printer driver`, the reader says the search leaves it out, as it leaves out a done line, since it starts `[x]`; and that `reprint-card`, `[ ]` with `· after print-card`, is listed.
* B4. Edge, a mark not at the start of a line (a sentence of docs/06 that mentions `[ ]`, a line indented): not listed, since `^` anchors the match to the line's first character, and every queue line starts with its mark.
* B5. The reader runs it two ways: an editor's search with regular expressions turned on, or `grep -nE '^\[[^x]\]' docs/06-Queue.md` in a terminal, which prints each open line with its line number.
* B6. Must fail: asked for the next delivery, the reader does not take the first line the search lists. On the `## Six marks` example the first listed is `lend-book`, already being built, and `return-book` is listed though its build waits on `lend-book`; the search reads no `after` and no session, and the queue tree of `## What may run now` stays the answer to what may run now.
* B7. Edge, a branch or a worktree per delivery: the search reads only the copy of docs/06 in front of the reader, so a line claimed on another branch reads as this copy has it; the queue tree reads each line where it lives (`## At the moment the work changes`).

**Contract.**

Files: `book/en/14-queue-states.md` and `book/pt/14-queue-states.md`, nothing else. Same files as `ch14-after-never-waits`, `ch14-queue-every-milestone` and `m38-fixes`: by docs/05 §4 the builds run one after another, and this page names its passages by sentence, so it builds after any of them.

Where it goes, decided by the agent, the author corrects it in the review: chapter 14, at the end of `## Six marks`, right after the paragraph under the nine-line example, EN "Anyone reading it knows, without asking, that a session is building `lend-book`, ..." (:49 as of `f28abd1`), PT "Quem a lê sabe, sem perguntar, que uma sessão está construindo `emprestar-livro`, ..." (:50). Why there: that section teaches the marks and reading a line's state, and the search is a way of reading marks; the nine-line example above it holds every mark, so the tip is shown on lines the reader has just read, with no new block; and it touches none of the passages the other three chapter 14 builds change (the table row of the waiting mark, `## What may run now`, `## Waiting: [?]`, `## A line from a finding`). Chapter 11 (the queue file) was weighed and left: it has not taught the marks yet, and the tip needs all six.

The passages:

* C1. The tip, a note box as docs/04 defines it ("A note box is a blockquote whose first words are bold, `> **Note.** ...` (pt: `> **Nota.**` ...), one paragraph, one sentence per line"), the kind chapters 2 and 3 already use, so no new kind of content and no render proof (docs/05 §5). It says, in this order and no more: the search and the expression, and what a regular expression is, a pattern a search matches against each line (first use in the book); the expression read piece by piece (B1); the marks it finds and that a cancelled line, `[x]` with `· dropped:`, is left out like a done one (B3); how to run it, an editor's search with regular expressions turned on, or `grep -nE '^\[[^x]\]' docs/06-Queue.md`, saying in a clause what `grep` is, the command-line program, on every Unix-like system and in Git for Windows' shell, that prints the lines of a file matching a pattern (first use in the book), and that `-n` adds each line's number; on the nine lines above, it finds seven, all but `catalog` and `members` (B2); the evidence, this book's own queue (C3); and that the search reads neither `after` nor another branch's copy, so what may run now stays the queue tree's answer, below (B6, B7). The expression is always in a code span, never bare: a bare `[^x]` is footnote syntax in Markdown.
* C2. The opening, EN :3, "After this chapter you can read any queue line's state among focus-kit's six marks, say who sets each one, ...", becomes "After this chapter you can read any queue line's state among focus-kit's six marks and list every open line of a queue with one search, say who sets each one, ..."; PT :3, "Depois deste capítulo você consegue ler o estado de qualquer linha da fila entre as seis marcas do focus-kit, dizer quem põe cada uma, ...", becomes "... entre as seis marcas do focus-kit e listar toda linha aberta de uma fila com uma busca, dizer quem põe cada uma, ...". Decided by the agent: the chapter opens with what the reader can do (AGENTS.md), and this is something new the reader can do.
* C3. The evidence, one sentence in C1: on 2026-11-14 this book's own queue, docs/06 of its repository, held 515 lines, 509 of them done, and the search showed the other six. Counted by the agent on the committed docs/06 at `f28abd1` (`git show f28abd1:docs/06-Queue.md`; `grep -cE '^\[.\] '` 515, `grep -cE '^\[x\]'` 509, `grep -cE '^\[[^x]\]'` 6); the date is that commit's (`git log -1 --format=%cs f28abd1`, 2026-11-14). No commit hash in the text (AGENTS.md). Precedent for the book's own making as evidence: chapter 3's Caution, "While this book was being written, the agent proposed ...". No source note: the count says where it comes from, and the link would show a queue that has moved on. Decided by the agent; if the author prefers the tip without a number, C3 is dropped and nothing else changes.

Proposed English text for C1, which /apply may tighten but not lengthen:

> **Note.** To see every open line of a queue at once, search docs/06 for the regular expression `^\[[^x]\]`, a pattern that a search matches against each line.
> `^` is the start of a line, `\[` and `\]` are the brackets themselves, and `[^x]` is any one character but `x`, so it finds every line that starts with a mark other than `[x]`: not defined, being defined, defined, being built and waiting; a cancelled line ends `[x]` with `· dropped:`, and is left out like a done one.
> Turn on regular expressions in an editor's search, or run `grep -nE '^\[[^x]\]' docs/06-Queue.md` in a terminal: `grep`, on every Unix-like system and in Git for Windows' shell, prints the lines of a file that match a pattern, and `-n` adds each line's number.
> On the nine lines above it finds seven, all but `catalog` and `members`; on 2026-11-14 this book's own queue held 515 lines, 509 of them done, and the search showed the other six.
> The search reads no `after` and only the copy of the file in front of you, so what may run now is still the queue tree's answer (below).

The Portuguese says the same in docs/03's terms (marca, linha, fila, árvore da fila, dependência for `after`), "expressão regular" for regular expression, and its own example's slugs: seven of nine, all but `catalogo` and `membros`. The expression and the command are the same in both editions.

Reproduction, since the scratchpad can vanish: write the chapter's nine-line example into a `docs/06-Queue.md` inside a fenced block under a milestone heading, in a scratch folder, and run `grep -nE '^\[[^x]\]' docs/06-Queue.md`: seven lines, `lend-book` to `m1-review` (pt: `emprestar-livro` to `m1-review`). With `[x] print-card ... · dropped: no printer driver` and `[ ] reprint-card ... · after print-card` added, it prints eight: `reprint-card` listed, `print-card` not. Run by the agent on 2026-11-14 with the system's `grep`. No output block goes into the chapter: with `-n` four of the English and Portuguese lines pass 74 columns (docs/04, Width of a block), and without it the block would repeat seven lines the reader has just read.

Terms of docs/03 introduced: none. "Regular expression" and `grep` are general tools, explained where first used, not the book's vocabulary.

Cases drawn on: none. No private case; the only number is the book's own queue (C3).

**Out of scope.**

* An output block of the search: past 74 columns with `-n`, a repeat without it (above).
* Key points: the tip is a convenience, not a rule; the opening names it, and key point 1 keeps the marks' rules.
* `## What the team gains`: the evidence stands in the tip, where it proves something; said once.
* The queue tree, `queue.sh` and what may run now: `ch14-queue-every-milestone` and `ch14-after-never-waits` own them; the tip points to the tree and changes nothing there.
* The table row of the waiting mark, "in the four cases below": `ch14-after-never-waits`.
* A search for one mark (`^\[\?\]` for waiting lines and the like): the author asked for one search, and each mark's variant is the same idea.
* Other chapters, docs/03, the kit: nothing changes there.

**Done when.**

* [x] C1 and C2 written in both editions, English the source, the Portuguese in docs/03's terms; C3 inside C1.
* [x] The note box follows docs/04: one paragraph, one sentence per line, `**Note.**` / `**Nota.**`.
* [x] The expression and the command in code spans everywhere, and both PDFs show `^\[[^x]\]` intact, backslashes and brackets included.
* [x] The seven of nine re-counted by /apply on the `## Six marks` example as it stands when built, since three builds touch chapter 14 first; the sentence follows the count.
* [x] The chapter still opens with its value; no filler and nothing useful cut; nothing of the other three chapter 14 lines' passages changed.
* [x] Every number sourced (C3); no private case, so no approval (docs/00 OD-3).
* [x] `make verify` green, with its time said.
* [x] `make book` run under the scratchpad lock, and the paths of both PDFs given to the author.

## Outcome

Built on 2026-11-14 by /apply, on trunk, before the person read the page (the author's word for this run, quoted above). The author authorized one commit per slug for this run; the driver session commits this delivery with the message below, and never pushes.

* Built as the page says: C1, the note box, at the end of `## Six marks`, right after the paragraph "Anyone reading it knows, without asking, that a session is building `lend-book`, ..." (EN :51-55, PT :52-56); C2 in the opening; C3 inside C1. Only `book/en/14-queue-states.md` and `book/pt/14-queue-states.md` changed, and the line's mark in docs/06.
* Re-count on the example as it stands after `m38-fixes` and `ch14-after-never-waits` (the nine lines did not change): `grep -nE '^\[[^x]\]'` on a scratch `docs/06-Queue.md` holding the first block of each edition prints seven lines, `lend-book` to `m1-review` (pt: `emprestar-livro` to `m1-review`); with `[x] print-card ... · dropped: no printer driver` and `[ ] reprint-card ... · after print-card` added, eight, `reprint-card` listed and `print-card` not. The sentence stands: seven of nine, all but `catalog` and `members` (pt: `catalogo`, `membros`).
* Divergence, C3: the page's "509 of them done" is not true: at `f28abd1` 3 of the 509 `[x]` lines end `· dropped:`, cancelled, and the note itself tells a cancelled line from a done one. Written "509 of them `[x]`" (pt: "509 delas `[x]`"); 515, 509, 6 and the date kept as the page fixed them, recounted with the page's commands.
* Divergence, C1 wording, decided by the agent: "a cancelled line ends `[x]`" became "is `[x]`" (the note teaches `^` as the start of a line, so "ends" would mislead); "in Git for Windows' shell" became "in the shell Git for Windows installs", the wording of chapters 8 and 13.
* Divergence, C2, from the review: the new clause placed after "six marks" made "say who sets each one" point to the open lines; it moved after "name the next delivery" in both editions: "..., name the next delivery, list every open line of a queue with one search, say which lines can run at the same time ..." (pt: "..., dizer qual é a próxima entrega, listar toda linha aberta de uma fila com uma busca, dizer quais linhas ...").
* Delivery review (docs/05 §5): one read-only agent on Opus, given the diff of both chapter files, this line of docs/06, the page and docs/04. No must-fix. Should-fix: the C2 placement above, fixed. Nits fixed in the Portuguese: "um caractere qualquer, menos `x`" (the English "any one"), "como uma linha feita", "a própria fila deste livro", "não lê o `after`". Nit left: the note explains `-n` and not `-E`; the page fixes the command with `-E` (B5) and asks the text not to grow, and the expression works the same either way. It also confirmed the regex reading, BSD and GNU grep behaviour, `^` as the start of a line in common editors' regex search, and that no passage of the other chapter 14 lines changed.
* Proof: `make verify` green, 40 seconds after the review's fixes (51 seconds on the first run; ceiling five minutes). `make book` under the scratchpad lock, exit 0; both PDFs show `^\[[^x]\]` intact, backslashes and brackets included, inside the note box (EN p. 158, PT p. 164, read as text and rendered). In the English PDF the code span of the `grep` command breaks after `'^\` at a line end, as long code spans do in the PDF; nothing is lost.
* Environments: local, both PDFs and EPUBs built in `output/`; GitHub Pages and the Release unchanged until the author's push and tag.

```commit
docs(ch14-open-lines-search): one search lists every open queue line

- chapter 14: a note box under the six marks' example, both editions
- teaches the expression ^\[[^x]\] piece by piece and grep -nE to run it
- seven of the example's nine; this book's queue: 515 lines, six open
- says the search reads no after, so the queue tree still says what runs
- opening adds listing every open line with one search

work/done/ch14-open-lines-search.md
```
