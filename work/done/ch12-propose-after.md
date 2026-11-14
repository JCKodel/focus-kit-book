# ch12-propose-after

Defined by /propose on 2026-11-14 on the author's word for this run, given on 2026-11-13 and relayed by the driver session: "Precisamos fechar todas as linhas de docs/06-Queue.md sem minha supervisão", close every open line of docs/06 without supervision. So the agent decided alone (docs/05 §4): every choice below marked "decided by the agent" is the agent's recommendation taken as the answer, and the author corrects it in the review. This page was written, and will be built, before the person read it; the person reads the page and the diff at the end.

**Overlap, found while defining.** `work/ch14-after-never-waits.md`, already `[>]`, widened itself to chapter 12 and holds both passages this line exists for: its Behaviour line "From chapter 12: say that `/propose` marks `[?]` only on an unanswered question, and returns the line to `[ ]` with `· after <slug>` when another line must come first." and its Contract paragraph "Chapter 12: ..." on `:36` and the key point. Two builds must not touch the same file (docs/05 §4), and this page does not write a second wording of the same sentences. Decided by the agent: this line names `ch14-after-never-waits` in its `after`, so its /apply starts only once that line is integrated, and the page is written as the end state chapter 12 must reach: /apply writes only what chapter 12 does not yet say. If `ch14-after-never-waits` built its chapter 12 item, this delivery confirms it with the sweep below and changes no chapter text; if that item was struck from its page before the build, this delivery writes it. Not dropped (cancelling is the person's, docs/05 §4) and not `[?]` (none of the three cases).

**Objective.** After chapter 12 the reader can say what `/propose` does when, while defining, it finds that another line must be done first: it saves the page as far as it goes, adds `· after <slug>` and returns the line to `[ ]`, never `[?]`, which it keeps for an answer nobody has given yet.

**Behaviour.** What the reader of both editions can do or explain after chapter 12:

* B1. Given `/propose reservations` finding, while defining, that it needs `search-catalog` first, the reader writes the result: the draft page saved as far as it goes, the line `[ ] reservations ... · after search-catalog`, and nothing else; `/propose reservations` resumes from the draft once `search-catalog` is `[>]` or beyond, as `:28` already says.
* B2. Given `/propose reservations` finding a scope question nobody has answered, the reader writes `[?]` with `· resume: propose` and what it waits on, the draft kept.
* B3. Must fail: the reader does not write `[?] reservations ... · resume: propose · blocked: after search-catalog`; asked why, they point to chapter 14, which owns the reason (`ch14-after-never-waits`), and chapter 12 retells nothing of the 2026-11-13 error.
* B4. The key points say the same: `[?]` when the scope waits on an answer, `[ ]` with `· after <slug>` when another line must come first.

**Contract.**

Files: `book/en/12-propose.md` and `book/pt/12-propose.md`, nothing else. docs/03 needs no change: its rows dependency / dependência, waiting mark / marca de espera, blocked reason / motivo da espera and resume suffix / fase de retomada already say the 2026.11.13 rule (`kit-2026-11-13`); checked by the agent. The Portuguese edition uses those terms, and "travado", never "bloqueado".

Sources the text follows: the installed `.claude/skills/propose/SKILL.md` 2026.11.13, "If an answer is missing, save the draft and block it as docs/05 §4 says, with `resume: propose`. If another line must come first, save the draft and add its `after` as §4 says."; docs/05 §4, "A line that needs another line first is not waiting. It ends `· after <slug>` and keeps the mark that names its next command. [...] Found by work already started, [...] the session adds the suffix and returns the line to `[ ]` from `[~]`, keeping the draft, or to `[>]` from `[*]`." Decided by the agent: chapter 12 teaches `/propose`'s half, `[~]` back to `[ ]`; the `[>]` of the queue line's "`[ ]` or `[>]`" is `/apply`'s return from `[*]`, which chapter 13 (`ch13-apply-after`) and chapter 14 (`ch14-after-never-waits`) teach, so chapter 12 does not repeat it.

End state, quoted by sentence since `m38-fixes`, `ch14-after-never-waits` and the other M39 lines may move line numbers (line numbers as of `f28abd1`, en / pt); the wording follows `ch14-after-never-waits`'s Contract, so whichever line writes it, the chapter reads the same:

* C1. `## What /propose does`, `:36` / `:36`. EN today: "When it finds, while defining, that the scope waits on an answer nobody has given yet or on another line that must be done first, it writes the page as far as it goes and marks the line `[?]` instead, with `· resume: propose` and what it waits on." PT today: "Quando descobre, enquanto define, que o escopo espera uma resposta que ninguém deu ainda ou outra linha que precisa ser feita antes, ele escreve a página até onde ela vai e marca a linha como `[?]` no lugar, com `· resume: propose` e o que ela espera." End state, two sentences: EN "When it finds, while defining, that the scope waits on an answer nobody has given yet, it writes the page as far as it goes and marks the line `[?]` instead, with `· resume: propose` and what it waits on. When it finds that another line must be done first, the line is not waiting: it saves the page as far as it goes, adds `· after` and that line's slug, and returns the line to `[ ]`, never `[?]` (chapter 14)." PT "Quando descobre, enquanto define, que o escopo espera uma resposta que ninguém deu ainda, ele escreve a página até onde ela vai e marca a linha como `[?]` no lugar, com `· resume: propose` e o que ela espera. Quando descobre que outra linha precisa ser feita antes, a linha não está esperando: ele salva a página até onde ela vai, acrescenta `· after` e o slug daquela linha, e devolve a linha a `[ ]`, nunca `[?]` (capítulo 14)." If `ch14-after-never-waits` wrote it in other words saying the same, it stays as written.
* C2. Key point 1, `:196` / `:205`. EN today "... or `[?]` when the scope waits, typed with no slug ..."; PT "... ou `[?]` quando o escopo espera, digitado sem slug ...". End state: EN "or `[?]` when the scope waits on an answer, and `[ ]` with `· after <slug>` when another line must come first,"; PT "ou `[?]` quando o escopo espera uma resposta, e `[ ]` com `· after <slug>` quando outra linha precisa ser feita antes,".

Kept as they are, decided by the agent after reading chapter 12 whole: `:28` (a line already `[?]`; a line whose `after` is not yet `[>]` does not start) already agrees with the rule and C1 does not repeat it; `:34` and `:35` (`[~]` until the page is complete, then `[>]`) hold; `:157` / pt `:166` ("a line still waiting when the others end is reported to you, not waited for") is docs/05 §4's own wording for a line its `after` holds back and marks nothing `[?]`.

Terms of docs/03 introduced: none new; dependency, waiting mark and resume suffix are already taught (chapter 14 owns them).

Cases drawn on: none. No number is added, so no source note. The error of 2026-11-13 is `ch14-after-never-waits`'s, told once in chapter 14; chapter 12 points there.

**Out of scope.**

* Chapter 14's three cases of `[?]`, `after` read per command, `queue.sh`'s `waits` and the 2026-11-13 error: `ch14-after-never-waits`.
* `/apply` returning a line to `[>]` with `· after <slug>`: `ch13-apply-after`.
* A new slug joined to an `after` the line already has: chapters 13 and 14 (`ch13-apply-after`, `ch14-after-never-waits`).
* `:25`'s "the milestone's lines" in the queue tree: a note below, not this line's clause.
* An example run of `/propose` returning a line in `## The page`: the `lend-book` page is complete, and chapter 14 holds the queue example; a second would say the thing twice.
* docs/03: no row is wrong.

**Done when.**

* [x] C1 and C2 read as their end state in both editions, the Portuguese in docs/03's terms, English the source; the Outcome says which line wrote them.
* [x] A sweep of chapter 12 whole, both editions, for `[?]`, "blocked", "travad", "wait" and "esper" finds no sentence that marks a line `[?]` because another line must come first.
* [x] No "no longer", "instead of blocking" or other before-and-after wording of the kit (docs/04, "The kit as it is"); nothing of the 2026-11-13 error retold.
* [x] The chapter still opens with what the reader can do; no filler, nothing useful cut; no number added; no private case used, so no approval needed (docs/00 OD-3).
* [x] `make verify` green, with its time said.
* [x] `make book` run under the run's scratchpad lock and the paths of both PDFs given to the author (docs/05 §5, Proof of a screen), whether or not this delivery changed chapter text; the Outcome says which.

## Outcome

Built by /apply on 2026-11-14, in a fresh session on trunk, on the author's word for this run relayed by the driver session ("Precisamos fechar todas as linhas de docs/06-Queue.md sem minha supervisão"): every decision below is the agent's, taken alone (docs/05 §4), and the page was built before the person read it. The author authorized one commit per slug for this run; the driver session commits this delivery with the message below, and never pushes.

**Divergence: this line wrote chapter 12.** The page was defined believing `ch14-after-never-waits` also edits chapter 12. It does not: its page's Contract says "chapter 12's is `ch12-propose-after`'s", and its Out of scope leaves chapter 12's `[?]` sentence and key point to this line. So this delivery took the page's own way out, "if that item was struck from its page before the build, this delivery writes it", and wrote C1 and C2 itself, in the words of their end state above. The driver session removed `ch14-after-never-waits` from this line's `after` in docs/06 before the build; the line's remaining `after kit-2026-11-13` is integrated (`[x]` on trunk), and no in-flight build touches chapter 12 (`m38-fixes`, `[*]`, changes chapters 5, 10, 11, 13, 14, 15 and 21, docs/01, docs/03, `pandoc/` and the READMEs), so the line started.

**What changed.** `book/en/12-propose.md` and `book/pt/12-propose.md`, `## What /propose does`: the one sentence on `[?]` became two, C1's end state, the second ending "(chapter 14)" / "(capítulo 14)", the pointer the page's B3 needs. Key point 2 of the key points (the long `/propose` bullet): C2's end state. Nothing else in either edition; no docs/03 row and no other document changes, as the Contract says.

**Sweep** (both editions, `[?]`, blocked, travad, bloque, wait, esper, "no longer", "não mais"): en `:28` (a line already `[?]`; a line whose `after` is not yet `[>]` does not start), `:36` and `:37` (C1), `:158` (a line still waiting reported, docs/05 §4's wording), `:197` (C2); pt the same at `:28`, `:36`, `:37`, `:167`, `:206`, and `:155` ("o resultado esperado", unrelated). None marks a line `[?]` because another line must come first; no before-and-after wording of the kit; nothing of the 2026-11-13 error.

**Proof.** `make verify` green in 41 seconds (ceiling five minutes). `make book` run under the run's scratchpad lock, green, with chapter text changed by this delivery: `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf` (and their EPUBs); the build printed only weasyprint's `user-select` warnings.

**Delivery review** (docs/05 §5): one read-only agent on Opus read the diff of both chapter 12 files and this line of docs/06 against this page and docs/04. Nothing to fix: C1 and C2 match their end state word for word in both editions, the Portuguese in docs/03's terms ("não está esperando", no "bloqueado"), the rule as docs/05 §4 and the propose skill say it, no em dash, no before-and-after wording, nothing of the 2026-11-13 error, one sentence per line, and no sentence of chapter 12 left marking `[?]` for another line. Its notes on this delivery's text, each decided by the agent:

* The new "(chapter 14)" at `:37` is a fourth pointer to chapter 14, where docs/04 "Chapter pointers" allows one per target. Kept: C1 writes it and B3 relies on it; the three older pointers (`:28`, `:34`, en `:158` / pt `:167`) predate this delivery and are a note below.
* Key point 2 reads "or `[?]` when the scope waits on an answer, and `[ ]` with `· after <slug>` when another line must come first", the "and" after "or" reading as both results. Kept as C2's exact end state, which the page fixed; a note below for the author.
* Chapter 14 in the tree still teaches the `[?]` for another line until `ch14-after-never-waits` is integrated; with that line gone from this `after`, chapter 12 can land first and the book contradicts itself in between. Not a text flaw: an order of integration, reported to the driver.

No fix was made after the review, so verify and `make book` above stand for the final text.

## For the review

* `book/en/12-propose.md:25` / `book/pt/12-propose.md:25`: "Typed with no slug, it shows what may run now, the queue tree the kit's script draws from docs/06, the milestone's lines with their states and the lines free to run, and asks which line to define." At 2026.11.13 `queue.sh` draws one tree per open milestone and offers the free lines across them (docs/05 §4); a reader sees "the milestone's lines" and may expect one milestone. It is not false while one milestone is open, so the agent cannot say it is grave: a note. `ch14-queue-every-milestone` (being defined, its page not yet written) owns the subject for chapters 13 and 14 and may take this sentence too.
* `book/en/12-propose.md:193-200` / `book/pt/12-propose.md:202-209`: `## Key points` holds six bullets, where docs/04 "Chapter shape" says at most five; older than this delivery. A reader sees one bullet more than every other chapter allows.
* `book/en/12-propose.md:28`, `:34`, `:158` / `book/pt/12-propose.md:28`, `:34`, `:167`: three pointers to chapter 14 before this delivery's fourth at `:37`, where docs/04 "Chapter pointers" allows one per target; the author may keep only the one that names a term not yet taught.
* `book/en/12-propose.md:158` / `book/pt/12-propose.md:167`: "a line still waiting when the others end is reported to you, not waited for (chapter 14)" is docs/05 §4's own wording for a line its `after` holds back, while `:37` now says such a line "is not waiting"; `:28`'s "it says the same" leans the same way, milder. A reader may take a line held by `after` for a wait. The words are the kit's, so the fix starts in the kit's docs/05 wording.
* `book/en/12-propose.md:197` / `book/pt/12-propose.md:206`: "or `[?]` when the scope waits on an answer, and `[ ]` with `· after <slug>` when another line must come first" reads as both results at once; "or `[ ]` ..." would read cleaner. Written as this page's C2 fixed it.

```commit
docs(ch12-propose-after): /propose keeps a line needing another at [ ]

- Chapter 12: an unanswered question marks [?], another line first adds after and returns [ ]
- Key point on /propose says the same, both editions
- docs/06: ch12-propose-after done

work/done/ch12-propose-after.md
```
