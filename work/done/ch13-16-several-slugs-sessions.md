# ch13-16-several-slugs-sessions

**Objective.** After chapters 16 and 13, the reader counts what a command typed with several slugs opens, one `/propose` subagent per slug and, when the command says to build as well, a second per slug that runs `/apply` once the page is `[>]`, and knows that with a worktree per delivery the session typing `/apply a b` in `main/` edits nothing and sends each subagent to its worktree, so it is not the session that stops anywhere but the delivery's worktree.

**Behaviour.** What the reader can do or explain afterwards:

* Asked how many subagents `/propose a b` told to build as well opens, answer from chapter 16: one per slug for `/propose`, then, for each slug whose page reaches `[>]`, a new one that runs `/apply` on it, sent to the delivery's worktree's path when there is one (chapter 12 en :164 / pt :173, docs/05 §4 :202-204).
* Asked why neither needs an error to be admitted, answer from chapter 16: each runs one whole command on its own line, as a fresh session in which you typed that command would; the `/apply` one reads, plans, builds, proves and documents, so it is not the "subagent launched only to plan, build or fix" that :86 keeps out.
* Asked where to type `/apply a b` with a worktree per delivery, answer from chapter 13 :21, unchanged: in a session in `main/`.
* Asked whether that session refuses, since chapter 13 says a session outside the delivery's worktree, `main/` included, refuses, answer from chapter 13's refusal sentence: no; the refusal is for `/apply <slug>` typed in a session outside the slug's worktree and for a subagent not sent to its path; the session that typed `/apply a b` edits nothing itself and sends each subagent to its slug's worktree.
* Fails: chapter 16 still says, of the per-slug subagents, "runs no step the command typed alone would not run" / "não roda nenhum passo que o comando digitado sozinho não rodaria"; chapter 16 :113 counts only "a command's one per slug"; chapter 13's refusal sentence still opens with "a session opened, with a worktree per delivery, in any folder but the delivery's worktree, `main/` included".
* Edge: chapter 16 :72's "Three steps of the process" stays three: the command typed with several slugs is one step whether it opens one or two subagents per slug.
* Edge: no em dash, no run narration, no version, date or commit hash in chapter text, nothing implying Case B ran on the process.

**Contract.** Two chapters in both editions, against the working tree as it is now, which already carries `m28-claim-wording`'s chapter 13 :28 (the line above, `[*]`, applied before this one; it touches no other sentence of chapter 13). Line counts: chapter 13 291/291, chapter 16 117/118; no line added or removed. One sentence per line; anchors are quoted clauses.

* `book/en/16-the-governor.md` and `book/pt/16-the-governor.md`:
  * :73, "The subagents it admits", replaced whole:
    * en: "A command typed with several slugs ([chapter 12](12-propose.md)) opens one subagent per slug, and when your `/propose a b` says to build as well, each slug gets a second once its page reaches `[>]`, a new subagent that runs `/apply` on it, sent to the delivery's worktree's path when there is one; none of them is specialized: each runs one whole command on its own line, the `/propose` or the `/apply` your command calls for, as a fresh session in which you typed that command would, so each delivery is still built by one agent that reads, plans and builds, and none runs a step its command typed alone would not run."
    * pt: "Um comando digitado com vários slugs ([capítulo 12](12-propose.md)) abre um subagente por slug, e quando o seu `/propose a b` diz para construir também, cada slug ganha um segundo assim que a sua página chega a `[>]`, um novo subagente que roda o `/apply` nela, mandado para o caminho do worktree da entrega quando há um; nenhum deles é especializado: cada um roda um comando inteiro na sua própria linha, o `/propose` ou o `/apply` que o seu comando pede, como rodaria uma sessão nova em que você digitasse esse comando, então cada entrega ainda é construída por um agente só, que lê, planeja e constrói, e nenhum roda um passo que o seu comando digitado sozinho não rodaria."
  * :113, the key point: en "the subagents it admits are a command's one per slug, each that one agent on its own line," becomes "the subagents it admits are a command's one per slug, `/propose`'s and, when it says to build as well, `/apply`'s, each that one agent on its own line,"; pt "os subagentes que ele admite são o que um comando abre por slug, cada um aquele agente só na sua própria linha," becomes "os subagentes que ele admite são o que um comando abre por slug, o do `/propose` e, quando ele diz para construir também, o do `/apply`, cada um aquele agente só na sua própria linha,"; the rest of each line stays.
  * Unchanged, checked: :4 (speaks of the specialized kind only); :67 (its bold words quote docs/05 §7, and "the one a command opens for each of its slugs" reads per command, `/propose`'s and `/apply`'s); :72 ("Three steps"); :75; :77; :86 ("a subagent launched only to plan, build or fix", which the new :73 does not contradict, since the `/apply` subagent runs the whole command).
* `book/en/13-apply.md` and `book/pt/13-apply.md`, "What it reads", the sentence that begins "The same holds for a session opened, with a worktree per delivery," (en :42) / "O mesmo vale para uma sessão aberta, com um worktree por entrega," (pt :42), replaced whole:
  * en: "The same holds, with a worktree per delivery, for `/apply <slug>` typed in a session in any folder but the delivery's worktree, `main/` included, and for a subagent not sent to that worktree's path: it refuses the same way, edits nothing, leaves the mark as it is, and gives the worktree's path, where you open the fresh session again, or where the session that typed `/apply a b`, on your command's word, sends a subagent on the slug again; that session, in `main/`, does not refuse, since it edits nothing itself and sends each subagent to its slug's worktree."
  * pt: "O mesmo vale, com um worktree por entrega, para `/apply <slug>` digitado em uma sessão em qualquer pasta que não o worktree da entrega, `main/` incluída, e para um subagente não mandado para o caminho desse worktree: recusa do mesmo jeito, não edita nada, deixa a marca como está, e dá o caminho do worktree, onde você abre a sessão nova de novo, ou para onde a sessão que digitou `/apply a b`, pela palavra do seu comando, manda de novo um subagente no slug; essa sessão, em `main/`, não recusa, já que ela mesma não edita nada e manda cada subagente para o worktree do seu slug."
  * :21 unchanged: it already says the session in `main/` edits nothing and sends each subagent to its slug's worktree. Nothing else in the chapter changes.
* Terms of docs/03: `subagent`, fresh session, slug, worktree; no row added or changed. Sources: chapter 12 en :164 / pt :173, docs/05 §4 :191-204, `.claude/skills/apply/SKILL.md` :11-23 (several slugs, one subagent per slug; with a worktree, only a session opened in it or a subagent sent to its path builds); the finding, `work/done/m28-review.md` C34, C35. No new footnote. Cases: none.
* Neighbouring lines: `m28-claim-wording` (`[*]`, above) touches chapter 13 :28 and chapter 19, docs/03, ADR-0018, and is applied first; `ch10-12-no-implicit-hosts` (chapters 10, 12) and `ch08-update-choice-outcome` (chapter 8) touch none of this page's files; `m28-records-claims` touches `work/done/` pages only.

**Out of scope.**

* "One subagent per slug" in docs/05 §4 :191 and §7 :370, docs/03 :39, ADR-0018 :76, docs/06 :645, chapter 8 :88, chapter 12 :153 and :192: each speaks of what one command opens, and docs/05 §4 :202-204 and chapter 12 :164 already say the build-as-well subagent beside it; true as written, not cited by the review.
* Chapter 19 :200 ("Opened in any other folder, `main/` included, `/apply` stops"): :198 makes it `/apply return-book`, one slug, and :230 already shows the `main/` session sending a subagent to each worktree; not cited by the review, and chapter 19 is `m28-claim-wording`'s file.
* The kit's own wording of /apply with several slugs: the kit's text, not edited.

**Decisions from the documents.**

* The build-as-well subagent is opened when a page reaches `[>]` and sent to the worktree's path when there is one: docs/05 §4 :202-204, chapter 12 en :164.
* A session in `main/` with several slugs does not build, so the "elsewhere, stop before any edit" rule is a single slug's session or a subagent at the wrong path: `.claude/skills/apply/SKILL.md` :11-23; chapter 13 :21 says the same of the session.
* "A command's one per slug" is read per command, `/propose`'s and `/apply`'s, so the documents above stay true and :73 is written to read with them.
* Taught as the kit is today, no version, date or run (AGENTS.md, docs/04).

**Decisions taken alone.** The agent chose each of these.

* :73 keeps "none runs a step its command typed alone would not run", now said of each subagent's own command, since that is why the governor admits them without an error; the `/apply` one is said to read, plan and build, so it does not read as :86's builder.
* :113 names both of a command's per-slug subagents, `/propose`'s and `/apply`'s, in one clause and keeps its structure; :67 stays, as its bold words quote docs/05 §7.
* Chapter 13's fix is at :42, narrowed to `/apply <slug>` typed outside the worktree, with a closing clause saying the `main/` session does not refuse; :21 stays word for word.
* Chapter 19 :200 left out (see Out of scope), so the queue line's wording stays: it names what the page changes.
* Token `(P-)`, as the line has it: chapter 13 is shared with `m28-claim-wording`, `[*]` above, so /apply waits for every line above to be `[x]`; chapter 16 is shared with no line in flight.

**Divergences.** Two, from the delivery review, both in chapter 16 and both editions; the Contract above now carries the new wording and the fourth Done-when grep matches it. :113's clause first read "a command's one per slug, and the `/apply` one each slug gets after it when the command says to build as well" / "o que um comando abre por slug, e o do `/apply` que cada slug ganha depois dele quando o comando diz para construir também", which set the `/apply` subagent apart from "a command's one per slug", the words :67 uses to admit it, and whose "it" / "dele" could point to the command; it now reads "a command's one per slug, `/propose`'s and, when it says to build as well, `/apply`'s" / "o que um comando abre por slug, o do `/propose` e, quando ele diz para construir também, o do `/apply`", so :67 stays true as written. :73's "the `/propose` or the `/apply` your command names" / "que o seu comando nomeia" now reads "calls for" / "pede", since `/propose a b` told to build as well never types `/apply`. Every other sentence went in word for word as the Contract writes it; the chapters keep 291/291 and 117/118 lines.

**Decisions taken by /apply.** The three review findings fixed now, as recommended, since each is in text this delivery wrote; nothing else was open, and the queue line stands unchanged (docs/06 is the driver's in this batch).

**Proof.**

* Each Contract sentence, as it now reads, found once as one whole line of its file, by a script over the page and the four chapters.
* The five Done-when greps print 1 and 1, nothing, 1 per edition, 1 per edition and nothing, after the review's fixes.
* `git diff HEAD` of the four files: 6 lines in, 6 out; no em dash in the added lines; no number, version, date, run or hash added.
* `make verify`: green, every check passed, exit 0, after the edits, again after the review's fixes and the page's move to `work/done/`, and once more after these two lines.
* `make book`: exit 0, after that verify; `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.

**Delivery review.** One read-only Opus agent, launched by this /apply over this page and `git diff HEAD` of the four files, against the Contract, docs/04, docs/05 §§2 and 3, AGENTS.md and `.claude/skills/apply/SKILL.md`. It read the page, chapter 13 en :15-45 and pt :15-22 and :42, chapter 16 en and pt :60-90 and :113, chapter 12 en :164 and pt :173, docs/05 :188-206 with grep hits in §2 and :370, docs/03 :39, docs/04 by grep for the em dash and run-narration rules, and SKILL.md :1-30; AGENTS.md only from its context. It ran the diff, line counts, a check that each Contract sentence is one whole line, the Done-when greps and an em-dash grep; it ran neither `make verify` nor `make book`, and consulted no advisor. Its reply: no blocking finding; every Contract sentence in word for word, nothing else changed, the greps hold, :42 agrees with :21, :73 does not contradict :86, :72's three steps hold, the Portuguese reads naturally and agrees, nothing banned. Three minor findings: :113's new clause lists the `/apply` subagent apart from "a command's one per slug", which on that reading :67 would exclude, suggesting "a command's one per slug, `/propose`'s and, when it says to build as well, `/apply`'s"; :73's "names" is loose, since the command only says to build as well, suggesting "calls for" / "pede"; :113's "after it" / "depois dele" could point to the command. All three fixed as Divergences says.

**Done when.**

* [x] Both editions changed as the Contract says in chapters 13 and 16, nothing else in them; line counts unchanged (291/291, 117/118).
* [x] `grep -c "each slug gets a second once its page reaches" book/en/16-the-governor.md` and `grep -c "cada slug ganha um segundo assim que a sua página chega" book/pt/16-the-governor.md` print 1.
* [x] `grep -n "runs no step the command typed alone would not run\|não roda nenhum passo que o comando digitado sozinho" book/*/16-the-governor.md` prints nothing.
* [x] `grep -c "\`/propose\`'s and, when it says to build as well, \`/apply\`'s\|o do \`/propose\` e, quando ele diz para construir também, o do \`/apply\`" book/*/16-the-governor.md` prints 1 per edition.
* [x] `grep -c "for \`/apply <slug>\` typed in a session in any folder but\|para \`/apply <slug>\` digitado em uma sessão em qualquer pasta" book/*/13-apply.md` prints 1 per edition, and `grep -n "for a session opened, with a worktree per delivery, in any folder\|para uma sessão aberta, com um worktree por entrega, em qualquer pasta" book/*/13-apply.md` prints nothing.
* [x] Each chapter still opens with its value, no filler and nothing useful cut, no number added, no em dash, no run narration, no version, date or commit hash in chapter text, nothing implying Case B ran on the process.
* [x] `make verify` green.
* [x] `make book` run, both PDF paths recorded.
* [x] Delivery review by one read-only Opus agent over this page and `git diff HEAD` of the four files, against docs/04, docs/05 §§2 and 3, AGENTS.md and `.claude/skills/apply/SKILL.md`; what it read and whether an advisor was consulted recorded as they were.
* [x] Page moved to `work/done/`, covered by the last verify.

```commit
docs(ch13-16-several-slugs-sessions): count the build-as-well subagent

- chapter 16: a command typed with several slugs opens one subagent per
  slug and, told to build as well, a second per slug that runs /apply
  once the page is [>]; the key point names both; both editions
- chapter 13: the refusal is for /apply <slug> typed outside the
  slug's worktree and for a subagent not sent there; the session in
  main/ that typed /apply a b does not refuse; both editions

work/done/ch13-16-several-slugs-sessions.md
```
