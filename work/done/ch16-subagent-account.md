# ch16-subagent-account

**Objective.** After chapter 16 the reader gives the one account of subagents that docs/05 §7 gives: the process has no subagent beyond a command's one per slug and the reviews' readers and checker; three steps launch agents of their own; the one a command opens per slug is not specialized and runs no step the command typed alone would not, and the readers and checker are the one specialized kind, each let in by the governor on an error that happened.

**Behaviour.** What the reader can do or explain after the chapter, in each edition:

* Asked which subagents the process admits, answer from the list of what the process does not have, in §7's words: none beyond a command's one per slug and the reviews' readers and checker (chapter 16's list item, docs/05 §7).
* Asked which steps launch agents of their own, name three: a command typed with several slugs (chapter 12), the delivery review where the host has none (chapter 13), and the milestone review (chapter 15).
* Say why a command's subagent is not specialized: it runs the whole command on its own line, as a fresh session the person opened would, so each delivery still has one agent that reads, plans and builds, and runs no step the command typed alone would not run.
* Say why the readers and the checker are specialized, and that the governor let them in, not the per-slug subagents, each on an error that happened in this book's repository.
* Edge: the list still holds eight things, as §7 does, and the chapter's footnote on subagents still opens Claude Code's page.
* Edge: a subagent launched only to plan, build or fix still has to name its error; no sentence implies the per-slug subagents opened that door, nor that a command's subagent running `/apply` is such a builder.
* Edge: the opener (:4) promises the specialized kind, the readers and checker, and stays true beside the plural heading and the key point that give both kinds.
* Edge: no passage names a kit version, a date of change, a run or a commit hash.

**Contract.** One chapter, the same changes in both editions, against the files as they are now (117 lines in en, 118 in pt with a trailing blank; line numbers match). One sentence per line, as the chapter is laid out. Lines shift after the insert; every cite is the line as it is now. No other line in flight touches chapter 16: `ch08-update-other-edits` is chapter 8, `ch12-13-19-several-slugs-paths` chapters 12, 13 and 19, `m27-records-claims` records only.

* :67, the list item, replaced whole:
  * en: "* **No subagent beyond a command's one per slug and the reviews' readers and checker**, a subagent being an agent that another agent launches, and a specialized one an agent launched for one narrow role with its own instructions, such as a planner or a reviewer:[^claude-code-subagents] each delivery has one agent that reads the documents, plans and builds, the one a command opens for each of its slugs included, and the reviews' readers and checker are the one specialized kind, which the next section explains."
  * pt: "* **Nenhum subagente além do que um comando abre por slug e dos leitores e do conferente das revisões**, sendo um subagente um agente que outro agente lança, e um especializado um agente lançado para um papel estreito com as suas próprias instruções, como um planejador ou um revisor:[^claude-code-subagents] cada entrega tem um agente só, que lê os documentos, planeja e constrói, o que um comando abre para cada um dos seus slugs incluído, e os leitores e o conferente das revisões são o único tipo especializado, que a próxima seção explica."
* :70, the heading: en "## The subagent it admits" becomes "## The subagents it admits"; pt "## O subagente que ele admite" becomes "## Os subagentes que ele admite". No link in the book points at the heading's anchor (grep).
* :72: en "Two steps of the process can launch agents of their own." becomes "Three steps of the process can launch agents of their own."; pt "Dois passos do processo podem lançar agentes próprios." becomes "Três passos do processo podem lançar agentes próprios."
* New line after :72, before the delivery review's sentence (:73), taking :87's place:
  * en: "A command typed with several slugs ([chapter 12](12-propose.md)) opens one subagent per slug, and none of them is specialized: each runs the whole command on its own line, as a fresh session you opened would, so each delivery still has one agent that reads, plans and builds, and runs no step the command typed alone would not run."
  * pt: "Um comando digitado com vários slugs ([capítulo 12](12-propose.md)) abre um subagente por slug, e nenhum deles é especializado: cada um roda o comando inteiro na sua própria linha, como uma sessão nova aberta por você rodaria, então cada entrega ainda tem um agente só, que lê, planeja e constrói, e não roda nenhum passo que o comando digitado sozinho não rodaria."
* :73 to :75 unchanged (the delivery review, the milestone review, "These readers, and the checker when an agent does that job, are specialized subagents in this chapter's sense"), :75 still pointing at :67's definition of a specialized one.
* :77: en "The governor let them in the way it lets in anything," becomes "The governor let the readers and the checker in the way it lets in anything,"; pt "O regulador os deixou entrar do jeito que deixa entrar qualquer coisa," becomes "O regulador deixou entrar os leitores e o conferente do jeito que deixa entrar qualquer coisa,". The rest of each line stays.
* :87 removed (en "A command typed with several slugs opens one subagent per slug ([chapter 12](12-propose.md)), and none of them is specialized: ..."; pt "Um comando digitado com vários slugs abre um subagente por slug ([capítulo 12](12-propose.md)), e nenhum deles é especializado: ..."), its content now in the line after :72.
* :86, which now ends the paragraph, names the specialized kind it keeps out, so it does not read against a command's subagent running `/apply` (the reason `work/done/ch12-14-18-several-slugs.md` placed :87 after it):
  * en: "The exception opens nothing else: a planner, a builder or a fixer subagent still has to name its error, and until one does, it stays out." becomes "The exception opens nothing else: a subagent launched only to plan, build or fix still has to name its error, and until one does, it stays out."
  * pt: "A exceção não abre mais nada: um subagente planejador, construtor ou corretor ainda precisa nomear o seu erro, e até um nomear, fica de fora." becomes "A exceção não abre mais nada: um subagente lançado só para planejar, construir ou corrigir ainda precisa nomear o seu erro, e até um nomear, fica de fora."
* :113, the key point, after "and the governor itself;" / "e o próprio regulador;":
  * en: "the reviews' readers and checker are the one specialized subagent it admits, each on an error that happened." becomes "the subagents it admits are a command's one per slug, each that one agent on its own line, and the reviews' readers and checker, the one specialized kind, each on an error that happened."
  * pt: "os leitores e o conferente das revisões são o único subagente especializado que ele admite, cada um com um erro que aconteceu." becomes "os subagentes que ele admite são o que um comando abre por slug, cada um aquele agente só na sua própria linha, e os leitores e o conferente das revisões, o único tipo especializado, cada um com um erro que aconteceu."
* Unchanged, checked: :4 (the readers and checker "the one specialized subagent it admits", still true), :58 ("eight things", §7 still lists eight), :106 ("The one exception", the specialized kind), the footnotes.
* Terms of docs/03: `subagent` / `subagente` (its row already gives both kinds, "the one specialized kind" among them), fresh session, slug. No row added or changed.
* Sources: docs/05 §7 ("no subagent beyond a command's one per slug (§4) and the reviews' readers and checker (§5's Delivery review, §8)"), §4's paragraph on a command typed with several slugs; its "each following the command's file with one slug", which chapter 12 :153 / pt :162 teaches as "as `/propose renew-loan` typed alone would"; the finding, `work/done/m27-review.md` C15. No new footnote.

**Out of scope.**

* Chapters 12, 13 and 19's several-slugs details: `ch12-13-19-several-slugs-paths`.
* docs/05 and docs/03: they already say this; nothing in them moves.
* The m27-review record, which cites the heading as it was: records hold what happened.
* An error that justified the per-slug subagents: none is recorded, so the chapter says why they add no step instead of naming one.

**Done when.**

* [x] Both editions changed as the Contract says, and nothing else in the chapter.
* [x] `grep -n "No subagent beyond a command's one per slug and the reviews' readers and checker" book/en/16-the-governor.md` and `grep -n "Nenhum subagente além do que um comando abre por slug" book/pt/16-the-governor.md` print one line each, in the list.
* [x] `grep -n "specialized subagent beyond\|subagente especializado além" book/*/16-the-governor.md` prints nothing.
* [x] `grep -n "Three steps\|Três passos" book/*/16-the-governor.md` prints one line per edition; `grep -n "Two steps\|Dois passos" book/*/16-the-governor.md` prints nothing.
* [x] `grep -c "none of them is specialized" book/en/16-the-governor.md` and `grep -c "nenhum deles é especializado" book/pt/16-the-governor.md` print 1, the line right after "Three steps" / "Três passos".
* [x] `grep -n "launched only to plan, build or fix" book/en/16-the-governor.md` and `grep -n "lançado só para planejar, construir ou corrigir" book/pt/16-the-governor.md` print one line each, and `grep -n "planner, a builder or a fixer subagent\|planejador, construtor ou corretor" book/*/16-the-governor.md` prints nothing.
* [x] "eight things" / "oito coisas" still at :58 and the list still has eight items in each edition.
* [x] Opens with its value, no filler and nothing useful cut, every number sourced; no em dash in an added line.
* [x] `make verify` green; `make book` run, both PDF paths given.

**Decisions taken alone.** The agent chose each one.

* The list item quotes §7's clause as its bold words, and keeps "specialized" as the chapter's own definition after it, since :75, :86, :106 and docs/03's row use it.
* The per-slug sentence moves from :87 to right after :72, so the count of three steps names each step where it is counted, instead of a fourth sentence after the exception; since `work/done/ch12-14-18-several-slugs.md` placed it after :86 so that :86's builder would not read against a subagent running `/apply`, :86 now names the kind it keeps out, "launched only to plan, build or fix", and /apply keeps both edits together.
* Siblings that would go stale and belong to no other line, fixed here: the heading goes plural, and :77's "them" names the readers and the checker, so the governor is not said to have let the per-slug subagents in on an error.
* Why the governor needs no error for the per-slug subagents is said as "runs no step the command typed alone would not run", from docs/05 §4's "each following the command's file with one slug" and chapter 12's "typed alone"; no error is invented.
* :4 stays: it speaks of the specialized kind, and is still true.
* Token: `(PA)`, chapter 16 alone and no line above in flight touches it. The queue line's wording stays.

**Divergences.** None: every change is in both editions with the wording the Contract gives.

**Omissions.** None.

**Decisions taken alone in /apply.**

* The review's three points are all optional and none breaks the page, docs/04 or the text this delivery wrote, so none is changed. Points 2 and 3 are the Contract's own wording, which reads correctly in its place.
* Point 1, the second subagent per slug that a command told to build as well opens to run `/apply`, gets no queue line: it is also one the command opens for the slug, running a whole command, so §7's "a command's one per slug" and the chapter's "runs the whole command on its own line" cover it, and "launched only to plan, build or fix" does not read against it; the book teaches the kit as it is, and chapter 12 already teaches the build-as-well subagent.

**Delivery review.** One read-only Opus agent, launched by this lane, over this page and `git diff HEAD` of `book/en/16-the-governor.md` and `book/pt/16-the-governor.md`, given docs/04, AGENTS.md, docs/05 §4 and §7 and docs/03's `subagent` row. Its reply, as returned:

> **Verdict:** the delivery passes. Every Contract change is in both editions with the wording given, nothing else in the chapter changed, and nothing needs fixing.
>
> **What I read**
> - /Volumes/Data/Projects/focus-kit-book/work/ch16-subagent-account.md, the whole page.
> - `git diff HEAD` on book/en/16-the-governor.md and book/pt/16-the-governor.md: 14 lines added and 14 removed in each, in four hunks per edition.
> - book/en/16-the-governor.md lines 1-12 and 55-120.
> - book/pt/16-the-governor.md lines 1-6, 72-80 and 98-118.
> - docs/05-Process.md lines 188-206 (§4, a command typed with several slugs) and 360-376 (§7).
> - docs/03-Domain.md line 39 (the `subagent` row).
> - A grep of book/ for links to the old heading's anchor and for cross-references to chapter 16's subagent text: neither found anything.
> - An em dash grep over the added lines: zero.
>
> **Contract, both editions**
> - **:67, the list item:** replaced word for word, and it matches §7's clause.
> - **:70, the heading:** now plural ("The subagents it admits", "Os subagentes que ele admite"). No link points at the old anchor.
> - **:72:** now "Three steps" / "Três passos", and the per-slug sentence follows it. Line 74 still says "specialized subagents in this chapter's sense", which still points back to :67's definition.
> - **:77:** "them" now names the readers and the checker, in both editions.
> - **The old :87:** removed. It is now :86, the new per-slug sentence just after "Three steps".
> - **The old :86:** reworded to "launched only to plan, build or fix" / "lançado só para planejar, construir ou corrigir", and it now ends the paragraph.
> - **The key point (now :113):** rewritten as the Contract gives it.
> - **Lines left unchanged:**
>   - The opener :4 (en and pt) still speaks only of the specialized kind, which is still true.
>   - :58 still says "eight things", and the list still has eight items.
>   - "The one exception" (now :107) still means the specialized kind.
>   - The footnotes are unchanged.
>
> **Rules (docs/04, AGENTS.md)**
> - No em dash, and one sentence per line.
> - No run narration, and no version, date or commit hash added.
> - No Case B passage touched.
> - The claims agree with docs/05 §4 and §7 and with docs/03's row.
>
> **Findings, all optional**
> 1. **book/en/16-the-governor.md:86, pt:86.** docs/05 §4 lets a command that says to decide alone and also build open a second subagent per slug to run `/apply`. The chapter's "one subagent per slug" and the reworded "a subagent launched only to plan, build or fix" both leave that subagent out. It runs a whole command, so it is not "only" a builder, and the text is not false. But the chapter does not account for it, and §7's own "a command's one per slug" has the same gap. If the author wants that case covered, it needs a new queue line, because it touches docs/05 §7 and is outside this page.
> 2. **en:113, pt:113.** "each that one agent on its own line" / "cada um aquele agente só na sua própria linha" relies on the reader linking "that one agent" back to "one agent" earlier in the same sentence. It reads as compressed, and "each one runs that whole command on its own line" would be clearer. It is the Contract's own wording, so changing it would mean changing the page.
> 3. **en:67, pt:67.** "the one a command opens for each of its slugs included" / "...incluído" is heavy, though the chapter uses the same trailing "included" construction elsewhere. Natural enough; no change needed.
>
> Nothing breaks the page, docs/04 or the text this delivery wrote. The only candidate for a new queue line is finding 1, the `/apply` subagent of a command that also builds, which would be a docs/05 §7 matter.

No fix and no new queue line, as the decisions above say. The line numbers in the reply are the reviewer's; rechecked, the per-slug sentence is :73 in both editions, the line that ends the paragraph ("launched only to plan, build or fix") :87, "specialized subagents in this chapter's sense" :76, the governor's line :78 and "The one exception" :106.

**Proof.** `make verify` was run after the chapter edits, again with the review recorded and the page moved to `work/done/`, and once more after this Proof was written: exit 0 each time, every check passed, the link check included. The Done when greps find each phrase once per edition: the list item :67, "Three steps" / "Três passos" :72, "none of them is specialized" / "nenhum deles é especializado" :73, "launched only to plan, build or fix" / "lançado só para planejar, construir ou corrigir" :87; the three "prints nothing" greps print nothing; "eight things" / "oito coisas" is still :58 and the list still has eight items; no added line holds an em dash. This lane ran `make book` after the second verify, exit 0, both editions: `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`. Nothing pushed; no environment changes.

```commit
docs(ch16-subagent-account): give chapter 16 §7's subagent account

- list item quotes §7: no subagent beyond a command's one per slug
- heading plural; three steps launch agents, per-slug one named first
- the exception keeps out a subagent launched only to plan, build or fix
- key point names both kinds; both editions

work/done/ch16-subagent-account.md
```
