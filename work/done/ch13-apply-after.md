# ch13-apply-after

Defined by /propose on 2026-11-14 on the author's word for this run, given on 2026-11-13 and relayed by the driver session: "Precisamos fechar todas as linhas de docs/06-Queue.md sem minha supervisão", close every open line of docs/06 without supervision. So the agent decided alone (docs/05 §4): every question below is answered by the agent's recommendation, and says the agent chose it. This page was written, and will be built, before the person read it; the person reads the page and the diff at the end.

**Objective.** After chapter 13 the reader can say what `/apply` does when its build finds that another line must be done first: the line takes that line as its `after` and goes back to `[>]`, its page saying what was built, while `[?]` is kept for a stop on an answer, the person's word or a review's partial reading; and that a finished `/apply` frees the lines that name it without touching them, because each command reads its `after` itself.

**Behaviour.** What the reader can do or explain after the chapter, both editions:

* B1. Given a build of `return-book` that finds, in the middle, a fix it cannot do inside its page, the reader says what `/apply` writes: the fix as a `[ ]` line above `return-book`, ending `· from return-book`; `return-book` back to `[>]`, ending `· after <the fix's slug>`, through the mark script; the page saying what was built and what it waits on, and a partial `commit` block, shown in the conversation too; on trunk nothing staged.
* B2. The reader says why that line is `[>]` and not `[?]`: it waits on no answer; the mark names its next command, `/apply`, and the `after` says when it may run (integrated, as `:50` already says), so whoever reads docs/06 sees both without a second suffix.
* B3. The reader says how the build resumes: once the fix is integrated, `/apply return-book` in a fresh session starts on the `[>]` line like any other, inspects the page, the tree and the index first, and continues from what the page says was built, the partial work still uncommitted in the tree on trunk (docs/05 §§4 and 6).
* B4. Edge, a line that already has an `after`: the reader says the new slug joins the slugs the suffix already names, and the line waits for all of them.
* B5. Edge, another line that already exists in the queue, not a fix found by this build: the same, its slug becomes the `after`, and no `· from` line is added, since nothing new was found.
* B6. Must fail: the reader does not mark a line `[?]` because another line must come first; given `[?] return-book ... · blocked: after fix-x`, the reader says it is written wrong and how it is written instead.
* B7. The three stops that do mark `[?]`, with `· resume: apply` and the reason: an answer nobody has given yet; the person says it is blocked; a milestone review's reading that left part of its range unread. A flaw in what the build made that it cannot fix, when grave or leaving a Done when item unticked, is the second of these, as chapter 13 already says.
* B8. The reader says what the end of `/apply` does for the lines that name it: nothing. Moving the page to `work/done/` and marking `[x]` is all; a line whose `after` names this one is freed by its own command's reading, `/propose` when the named line is `[>]` or beyond, `/apply` when it is integrated (chapter 14). The chapter says this as the kit is today: no "no longer", no before and after (docs/04, "The kit as it is").

**Contract.**

Files: `book/en/13-apply.md` and `book/pt/13-apply.md`, nothing else. docs/03 needs no change: its rows waiting mark / marca de espera, blocked reason / motivo da espera, dependency / dependência and resume suffix / fase de retomada already say the 2026.11.13 rule, migrated by `kit-2026-11-13`; the agent checked them and chose to leave them. The Portuguese edition uses those terms: dependência for `after`, marca de espera, travado (never "bloqueado"), fase de retomada.

Sources the text follows: the installed `.claude/skills/apply/SKILL.md` 2026.11.13, "When work cannot go on, record what was built and what it waits on and leave the page in `work/`. A line that waits on another takes it as its `after` and returns to `[>]`, as docs/05 §4 says; any other is blocked with `resume: apply`. A prerequisite fix becomes a `[ ]` line above this one, ending `· from <slug>`.", and "Tick every Done when item and move the page to `work/done/`."; docs/05 §4's paragraph "A line that needs another line first is not waiting. It ends `· after <slug>` and keeps the mark that names its next command. [...] Its page says what was built and what it waits on, and /apply continues from there."; docs/05 §6, "A prerequisite that must be built first becomes a `[ ]` line above this one, ending `· from <slug>` (§4), and this line returns to `[>]` ending `· after <slug>` (§4). The partial work stays in the tree, uncommitted and out of the index, while the prerequisite is built and staged alone".

Passages changed, quoted by sentence since `m38-fixes` and `ch14-queue-every-milestone` build chapter 13 first and move its lines (line numbers as of `f28abd1`, en / pt):

* C1. `### When the work cannot go on`, :72 / :72. EN "It stops when the build needs an answer nobody has given yet, when another line must be done first (a fix it found becomes a `[ ]` line above this one, ending `· from` and this delivery's slug, a suffix chapter 14 explains), when you say it is blocked, or, in a milestone's review, when the reading of the code changed since the milestone's base left part of it unread." PT "Ele para quando a construção precisa de uma resposta que ninguém deu ainda, quando outra linha precisa ser feita antes (...), quando você diz que ela está travada, ou, na revisão de um marco, ...". Becomes two stops: (a) waiting, `[?]`, in the three cases (answer, your word, a review's partial reading), with C2's flaw sentence kept; (b) another line first: a fix it found becomes a `[ ]` line above this one ending `· from` and this delivery's slug (chapter 14 explains the suffix), or a line already queued is named; this line takes that slug as its `after`, added to any it has, and goes back to `[>]` through the mark script; it is not waiting: the mark names the next command and the `after` says when (B1, B2, B4, B5).
* C2. Same section, :73-74 / :73-74. EN "A flaw in what it built that it cannot fix without widening the page, or without a decision no document answers, waits for your answer the same way when it is grave or leaves an item of Done when unticked." stays. EN "It writes on the page what was built and what it waits on, leaves the page in `work/`, marks the line `[?]` with that reason at its end (chapter 14)." PT "Ele escreve na página o que foi construído e o que ela espera, deixa a página em `work/`, marca a linha como `[?]` com esse motivo no fim dela (capítulo 14)." Becomes: in both stops it writes on the page what was built and what it waits on and leaves the page in `work/`; the waiting line is marked `[?]` with `· resume: apply` and its reason, the other keeps `[>]` with its `after`. The next two sentences (partial `commit` block; on trunk nothing staged, on a delivery branch partial staging) stay and hold for both.
* C3. Same section, one new sentence after those (B3): when the line it waits on is integrated, `/apply <slug>` in a fresh session starts on the `[>]` line as `:50` and `:52` say, and continues from what the page says was built, the partial work found in the tree.
* C4. `### Green is not done`, :135 / :135. EN "It moves the page to `work/done/`; a `[?]` line that waits only on this one, or on lines already integrated, goes back by its resume phase ([chapter 14](14-queue-states.md))." PT "Move a página para `work/done/`; uma linha `[?]` que espera só por esta, ou por linhas já integradas, volta pela fase de retomada ([capítulo 14](14-queue-states.md))." Becomes: it moves the page to `work/done/`; a line whose `after` names this one needs nothing from it, since its own command reads the `after` (chapter 14) (B8). Said in the present, as docs/04 asks.
* C5. Key point 2, :334 / :334. EN "...`[x]` with its last, once the rest is staged, with `stage`, so that line alone goes into the index, and `[?]`, with what it waits on, when it must stop." PT "... e `[?]`, com o que ela espera, quando precisa parar." Becomes: `[?]` with its reason when it stops on an answer, your word or a partial reading, and back to `[>]` ending `· after <slug>` when another line must be done first.

Kept as they are, decided by the agent: `:48` (a refusal before any build is no stop, and the line is not `[?]`) and `:50` (an `after` is an order, not a wait) already agree with the rule and C1 points to them rather than repeat them; `:54` (a `[?]` line resumes by its phase) holds for the three cases; `:103`, `:139`, `:318-319` and `:336` say "blocked" of an `/apply` that stopped, as the installed skill ("done or blocked") and docs/05 §6 ("When blocked on trunk") do, so the word stays for any stop and the chapter does not invent a second one.

Terms of docs/03 introduced: none new; dependency, waiting mark, blocked reason, resume suffix and finding line are already taught (chapter 14 owns them).

Cases drawn on: none. The error that makes this rule worth teaching, the two `[?]` lines of 2026-11-13, is `ch14-after-never-waits`'s and is told once, in chapter 14; chapter 13 points there and retells nothing. No number is added, so no source note.

**Out of scope.**

* Chapter 14's three cases, `after` read per command and what it costs, `queue.sh`'s `waits`, and the 2026-11-13 error: `ch14-after-never-waits`.
* Chapter 13's example queue tree (:201 to :213) and the `### Green is not done` bullet on the tree (:141): `ch14-queue-every-milestone`.
* Chapter 13's three tests of grave (:116), the marks in the example's last message and key point 4: `m38-fixes`.
* Chapter 12's `/propose` passage (:36) that still marks `[?]` for another line: a finding, under `## For the review`, not this page's chapter.
* An example run of a returned line in `## lend-book, built`: the example ends done, and chapter 14 holds the queue example of a line with a `· from` fix above it; a second example would say the thing twice.
* docs/03: no row is wrong.

**Done when.**

* [x] C1 to C5 written in both editions, the Portuguese in docs/03's terms, English the source.
* [x] The chapter still opens with what the reader can do, and its opening (:3) still holds; no filler, nothing useful cut.
* [x] No "no longer", "instead of blocking" or other before-and-after wording of the kit in the chapter (docs/04).
* [x] Nothing of chapter 14's error retold; nothing of m38-fixes' or ch14-queue-every-milestone's passages changed.
* [x] No number added; no private case used, so no approval needed (docs/00 OD-3).
* [x] `make verify` green, with its time said.
* [x] `make book` run under the scratchpad lock, and the paths of both PDFs given to the author.

## Outcome

Built by /apply on 2026-11-14, before the person read the page, on the author's word for this run (docs/05 §4): every decision below is the agent's, and says so. The author authorized one commit per slug for this run; the driver session commits this delivery with the message below, and never pushes.

**What was built.** `book/en/13-apply.md` and `book/pt/13-apply.md`, nothing else; the line `[>]` to `[*]` to `[x]` through `mark.sh`. Every passage was found by its quoted sentence: `m38-fixes` (`296089e`) had changed only :116, :139 and key point 4, outside this page's passages, so C1 to C5 sat at the page's line numbers.

* C1, C2: `### When the work cannot go on` now gives the three stops that wait, `[?]` with `· resume: apply` and the reason, with the flaw sentence kept right after them so "the same way" still reads as a wait; then the stop for another line first: either a line already in the queue, which adds no line, or a fix found, which becomes a `[ ]` line above ending `· from` and the slug; the line takes that slug as its `after`, beside any it names, goes back to `[>]` through the mark script, and gets no `[?]`. "Whichever the stop" the page says what was built and what it waits on; the partial `commit` block and the staging sentences stay for both.
* C3: one sentence after the staging sentences: when every line its `after` names is integrated, `/apply <slug>` in a fresh session starts on the `[>]` line, inspects the page, the folder and the index, and continues from the partial work, in the folder on trunk or staged or committed on the delivery's branch (so it agrees with the delivery-branch sentence and with the review section's commits of a blocked `/apply`).
* C4: the `work/done/` bullet says a line whose `after` names this one needs nothing more from `/apply`, since that line's own command reads its `after` when it starts, with the chapter 14 link kept.
* C5: key point 2 gives `[?]` with its reason for the three stops and `[>]` ending `· after <slug>` for another line first, still five key points.
* Checked before writing, by the agent: `mark.sh` moves `[*]` back to `[>]` (only `[~]` and `[*]` are guarded), so "through the mark script" holds; several slugs in one `after` are a comma list in docs/06 and `queue.sh`, and the chapter shows no syntax for them, only "beside any slug its `after` already names".
* The chapter never says "dependency" for `after`, so the Portuguese keeps `after` too and does not write "dependência", which the chapter already uses for a package (:61, :247). Agent's choice.

**Proof.** `make verify` green, 13 seconds before the review, 10 seconds after its fixes, and once more after this page was written and moved to `work/done/` (ceiling five minutes; the last run's time is in /apply's last message). `make book` run under the scratchpad lock after the last edit to the chapters: `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`. Another session (`ch14-after-never-waits`) was editing chapters 8, 14 and 19 in the same tree; verify was green with its edits present.

**Delivery review.** One read-only agent on Opus read `git diff HEAD` of both chapters, this page and docs/04, and found B1 to B8 and C1 to C5 answered, parity kept, no docs/04 violation and no passage of m38-fixes or of `ch14-queue-every-milestone` touched. Its candidates and what became of each:

* "it marks the line `[?]`" read as the line marking itself: fixed, "`/apply` marks it `[?]`" (pt "o `/apply` a marca").
* "so it is never `[?]`" overstated, since any mark before `[x]` can become `[?]` on your word: fixed, "this stop puts no `[?]` on it".
* The long comma chain on `[>]` and `after` split into three sentences.
* The resume sentence said "the line it needs", singular, after the text allowed several: fixed, "every line its `after` names"; this also removed the Portuguese ele/ela referent mismatch.
* B5 left implicit that a queued line adds no `· from` line: fixed, "when the line it needs is already in the queue, no line is added"; the two alternatives now come first, the suffix pointer in parentheses.
* "In both stops" after four listed situations: fixed, "Whichever the stop".
* Key point 2's "stops on an answer" could read as on receiving one: fixed, "stops for an answer not given" (pt "à espera de uma resposta não dada").
* :48 called the refusal "not the stop" the section describes, now that the section describes two: fixed, "none of the stops" (pt "nenhuma das paradas"), the page's "kept as they are" for :48 being otherwise held.
* Portuguese "já nomeia" set to the subjunctive "já nomeie"; the doubled "quando" removed by the split.
* "blocked" for an `/apply` that stopped on another line, in passages this delivery kept: not changed, a note below.
* The page's B7 calls the flaw case "the second" of its list, which in B7's own order is "the person says it is blocked"; the chapter follows docs/05 §4, where the flaw "waits for the person's answer instead, the second case below", the answer asked and not given. The definition stays as it was read; the chapter is right.
* :77's restatement of :50 (an `after` is an order, not a wait): kept, C1 asked for it.

No test: the book has no product code, and its checks are verify (docs/04 §Tests).

**The chapter 12 finding.** The page's `## For the review` item on `book/en/12-propose.md:36` was judged grave by /propose and reported to the driver session, which added it as `ch12-propose-after · from ch13-apply-after`; it is `[x]` at `46e961a`. It is no longer a note, so it moves here and the milestone review has nothing of it to copy.

## For the review

* `book/en/13-apply.md:110`, `:111`, `:146`, `:325` and `:343` (and the same lines in `book/pt/13-apply.md`, "travado") call an `/apply` that stopped "blocked", now also the stop that returns its line to `[>]` with an `after`, while docs/03's row blocked / travado says the word of a `[?]` line and of an `/apply` that stopped on one. The installed skill ("done or blocked") and docs/05 §6 ("When blocked on trunk", which covers the prerequisite) use it the same way, so the page kept it; a reader may meet "a blocked `/apply`" right after reading that the line is not waiting. The person may widen docs/03's row to any stopped `/apply`, or ask for another word in chapter 13.

```commit
docs(ch13-apply-after): /apply returns a line needing another to [>]

- Teach the three stops that mark [?] with resume: apply and a reason
- Teach another line first: the after, back to [>], no [?]
- Say how /apply resumes once every line its after names is integrated
- A line naming this one in after needs nothing at its end
- Key point 2 gives both marks; both editions

work/done/ch13-apply-after.md
```
