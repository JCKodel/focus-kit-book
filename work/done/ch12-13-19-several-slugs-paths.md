# ch12-13-19-several-slugs-paths

**Objective.** After chapters 12, 13 and 19 the reader of a command typed with several slugs knows where each part of it happens: a page a subagent wrote is read and corrected in the session that typed the command, which carries the correction to a subagent on the slug; `/propose`'s subagent creates its slug's worktree or reuses it; building as well sends `/apply`'s subagent to the worktree's path; and with a worktree per delivery the session typing `/propose a b` or `/apply a b` opens in `main/`.

**Behaviour.** What the reader can do or explain afterwards:

* Asked "where do I correct `renew-loan`'s page after `/propose search-catalog renew-loan`?", answer from chapter 12: in the session that typed the command; it edits nothing itself and sends the correction to a subagent on that slug the way it sends an answer, and the fix, on the page and in any document it touches, is that subagent's work.
* Say, from chapter 12's opening section, its "Read the page" section and its key point, that a single `/propose` is corrected in the session that wrote the page, and a command typed with several slugs in that command's session.
* Say that with a worktree per delivery each `/propose` subagent creates its slug's worktree from `main/`, or reuses it when it exists, as a `/propose` typed alone does.
* Say that a command told to build as well has its new `/apply` subagent sent to the delivery's worktree's path when there is one.
* Say where to type `/apply a b` with a worktree per delivery: in a session in `main/`, as `/propose` runs there; that session edits nothing itself and sends each subagent to its slug's worktree.
* Edge, refusal (chapter 13): a session opened outside the delivery's worktree gives the path, where you open the fresh session again; a subagent not sent to that path gives it too, and the session that typed `/apply a b` sends a subagent on the slug there again.
* Using chapter 19, say which sessions run two deliveries at once in worktrees: one in `main/` for each `/propose` or one for a `/propose a b` naming both, one in each worktree for its `/apply` or one in `main/` for an `/apply a b`, and none in the container.
* Using chapter 19's batch, say where a batch page is corrected, the decisions list included, and where two pages that settled one question two ways are reconciled: in the session that typed the command, as chapter 12 says.
* Edge, one slug: `/propose lend-book` and `/apply lend-book` read as before, their sessions where they were.
* Edge: no passage implies the session decides on its own to reopen a subagent, or that a correction changes a line's mark; no version, date, run or commit hash; nothing implies Case B ran on the process.

**Contract.** Three chapters, the same changes in both editions, against the files as they are now (en/pt: chapter 12, 196/205 lines; chapter 13, 282/282; chapter 19, 377/377); one sentence per line, as the chapters are laid out; anchors are quoted clauses, since lines move. The neighbouring lines in flight, `ch08-update-other-edits` (chapter 8) and `ch16-subagent-account` (chapter 16), touch none of these files; M28's `ch13-19-claim-script` touches chapters 13 and 19 later, after this line.

* `book/en/12-propose.md` and `book/pt/12-propose.md`:
  * C3, en :39: "and you read and correct the page in the session that wrote it, before `/apply`." becomes "and you read and correct the page in the session that wrote it, or, when one command defined several lines, in the session that typed it (below), before `/apply`."
  * C3, pt :39: "e você lê e corrige a página na sessão que a escreveu, antes do `/apply`." becomes "e você lê e corrige a página na sessão que a escreveu, ou, quando um comando definiu várias linhas, na sessão que o digitou (abaixo), antes do `/apply`."
  * C3, en :139: "You ask for every correction in the same conversation, and the agent writes the fix:" becomes "You ask for every correction in the same conversation, or, for a page of a command typed with several slugs, in that command's session (below), and the agent writes the fix:"; the rest stays.
  * C3, pt :148: "Você pede cada correção na mesma conversa, e o agente escreve a correção:" becomes "Você pede cada correção na mesma conversa, ou, para uma página de um comando digitado com vários slugs, na sessão desse comando (abaixo), e o agente escreve a correção:"; the rest stays.
  * C2, en :155: "which it creates from `main/`, as a `/propose` typed alone does" becomes "which it creates from `main/`, or reuses when it exists, as a `/propose` typed alone does"; the rest stays.
  * C2, pt :164: "que ele cria a partir de `main/`, como faz um `/propose` digitado sozinho" becomes "que ele cria a partir de `main/`, ou reutiliza quando já existe, como faz um `/propose` digitado sozinho"; the rest stays.
  * C3, new line after "A subagent cannot ask you: ..." (en :157) / "Um subagente não consegue perguntar a você: ..." (pt :166):
    * en: "You read and correct each page there too: you ask in the session that typed the command, and it sends your correction to a subagent on the slug the way it sends an answer, the fix on the page and in any document it touches being that subagent's work."
    * pt: "Você também lê e corrige cada página ali: pede na sessão que digitou o comando, e ela manda a sua correção para um subagente no slug do jeito que manda uma resposta, e a correção na página e em qualquer documento que ela toque é trabalho desse subagente."
  * C4, en :163: "a new subagent runs `/apply` on it, and the page says" becomes "a new subagent runs `/apply` on it, sent to the delivery's worktree's path when there is one, and the page says"; the rest stays.
  * C4, pt :172: "um novo subagente roda o `/apply` nela, e a página diz" becomes "um novo subagente roda o `/apply` nela, mandado para o caminho do worktree da entrega quando há um, e a página diz"; the rest stays.
  * C3, key point en :191: "the session edits nothing and relays each subagent's questions to you;" becomes "the session edits nothing and relays each subagent's questions to you and your corrections to a subagent on the slug;"; pt :200: "a sessão não edita nada e repassa a você as perguntas de cada subagente;" becomes "a sessão não edita nada e repassa a você as perguntas de cada subagente e as suas correções a um subagente no slug;".
  * C3, key point en :193: "you read the page before `/apply`, in the session that wrote it, and correct it" becomes "you read the page before `/apply`, in the session that wrote it or, for a command typed with several slugs, in that command's session, and correct it"; pt :202: "você lê a página antes do `/apply`, na sessão que a escreveu, e a corrige" becomes "você lê a página antes do `/apply`, na sessão que a escreveu ou, para um comando digitado com vários slugs, na sessão desse comando, e a corrige".
  * Nothing else in the chapter changes.
* `book/en/13-apply.md` and `book/pt/13-apply.md`:
  * C17, new line after "Typed with several slugs, `/apply a b` opens one subagent per slug ..." (en :20) / "Digitado com vários slugs, `/apply a b` abre um subagente por slug ..." (pt :20):
    * en: "With a worktree per delivery, you type `/apply a b` in a session in `main/`, as `/propose` runs there: the session edits nothing itself and sends each subagent to its slug's worktree ([chapter 19](19-worktrees.md))."
    * pt: "Com um worktree por entrega, você digita `/apply a b` em uma sessão em `main/`, como o `/propose` roda ali: a sessão não edita nada ela mesma e manda cada subagente para o worktree do seu slug ([capítulo 19](19-worktrees.md))."
  * C17, en :34: "and gives the worktree's path, where you open the fresh session again." becomes "and gives the worktree's path, where you open the fresh session again, or the session that typed `/apply a b` sends a subagent on the slug again."
  * C17, pt :34: "e dá o caminho do worktree, onde você abre a sessão nova de novo." becomes "e dá o caminho do worktree, onde você abre a sessão nova de novo, ou para onde a sessão que digitou `/apply a b` manda de novo um subagente no slug."
  * Nothing else in the chapter changes; the key point at :276 ("each sent to its worktree's path") stays true.
* `book/en/19-worktrees.md` and `book/pt/19-worktrees.md`:
  * C5 and C17, en :214: "one in `main/` for each `/propose`, one in each worktree for its `/apply`, and none in the container." becomes "one in `main/` for each `/propose`, or one for a `/propose a b` naming both, whose subagents write in each worktree, one in each worktree for its `/apply`, or one in `main/` for an `/apply a b`, which sends a subagent to each worktree's path, and none in the container."
  * C5 and C17, pt :214: "uma em `main/` para cada `/propose`, uma em cada worktree para o seu `/apply`, e nenhuma no contêiner." becomes "uma em `main/` para cada `/propose`, ou uma para um `/propose a b` que nomeia as duas, cujos subagentes escrevem em cada worktree, uma em cada worktree para o seu `/apply`, ou uma em `main/` para um `/apply a b`, que manda um subagente para o caminho de cada worktree, e nenhuma no contêiner."
  * C16, en :296: "correct each one in the session that typed the command (chapter 12);" becomes "correct each one in the session that typed the command, which carries the correction to a subagent on its slug (chapter 12);"; pt :296: "corrija cada uma na sessão que digitou o comando (capítulo 12);" becomes "corrija cada uma na sessão que digitou o comando, que leva a correção a um subagente no slug dela (capítulo 12);"; the rest stays.
  * C16, en :304: "and you correct one of them in its conversation." becomes "and you correct one of them in the session that typed the command, as above."; pt :304: "e corrige uma delas na sua conversa." becomes "e corrige uma delas na sessão que digitou o comando, como acima."
  * C17, key point en :365: "`/propose` in `main/`, which edits the worktrees by the container's manual, and `/apply` in a fresh session" becomes "`/propose` in `main/`, which edits the worktrees by the container's manual, a command typed with several slugs there too, its subagents writing in, or sent to, each worktree, and `/apply` in a fresh session"; pt :365: "o `/propose` em `main/`, que edita os worktrees pelo manual do contêiner, e o `/apply` em uma sessão nova" becomes "o `/propose` em `main/`, que edita os worktrees pelo manual do contêiner, um comando digitado com vários slugs ali também, os subagentes dele escrevendo em cada worktree, ou mandados para ele, e o `/apply` em uma sessão nova"; the rest stays.
  * Nothing else in the chapter changes.
* Terms of docs/03: none new; `subagent`, `worktree` and `slug` are there. Sources: none new. Cases: none.

**Out of scope.**

* Chapters 8 and 16: `ch08-update-other-edits`' and `ch16-subagent-account`'s.
* The claim script in chapters 13 and 19: M28's `ch13-19-claim-script`.
* docs/05 §4's "(/propose creates it)" and the kit's silence on where a correction of a subagent's page goes and where `/apply a b`'s session opens: the kit's text, installed by `kit-2026-10-20-3`; a kit proposal is not this delivery's.
* The record `work/done/ch12-14-18-several-slugs.md`, whose decision left the correction's path unsaid: records hold what happened, and that decision was taken.
* Chapter 13's key point, chapter 12's :29 and :31, and chapter 19 :200 ("Opened in any other folder, `main/` included, `/apply` stops before any edit"), which sits in `/apply return-book`'s paragraph and is said of the single command: already true as they stand.

**Decisions from the documents.**

* Created or reused: the propose skill ("a worktree where docs/05's Git slot puts it, reused when it exists") and chapter 12 :29 for the single command.
* `/apply`'s subagent sent to the worktree's path, every file and command there: the apply skill and chapter 13 :20.
* Corrections happen in the `/propose` conversation: docs/05 §3; the session edits nothing and relays the person's words to a subagent on the slug: docs/05 §4.
* Taught as the kit is today, with no version, date or run (AGENTS.md).

**Decisions taken alone.** The agent chose each of these.

* Where a correction goes: in the session that typed the command, which carries it to a subagent on the slug as it carries an answer. docs/05 §3 puts corrections in the `/propose` conversation and §4 says the session edits nothing; §4 names the relay only for a question's answer, and the book reads a correction as the same path. The sentence says the session sends your correction, so the person's word is what moves it, and says nothing of marks, since the kit does not say a correction changes one.
* Where the session typing `/apply a b` opens with a worktree per delivery: `main/`, as `/propose`'s session. The kit does not name the folder; this session edits nothing (docs/05 §4), reads the main branch's queue after `git fetch` (chapter 13 :30), sends each subagent to its path (the apply skill), and chapter 19 :216 gives every tool one shape. The apply skill's "elsewhere, stop before any edit" does not reach a session that edits nothing; the new line after chapter 13 :20 says it edits nothing, and :34 is left about the single session and the subagent.
* The remedy for a refused subagent: the session that typed `/apply a b` sends a subagent on the slug to the path again. The kit says only that the refusal gives the path; sending subagents is the session's part under docs/05 §4 ("else opening it again on the slug ... on the command's word"), and the book reads the refusal's path as what it sends the new one to.
* Chapter 12 is the home of the correction's path (one new line in "Several lines in one command"); its :39, :139 and both key points point there, and chapter 19 :296 and :304 point to chapter 12, as C16 asked ("neither chapter 12's").
* Chapter 12's key point on `/propose a b` (en :191, pt :200) gains the corrections: a sibling clause that would read incomplete beside the new line and that no other line owns.
* Queue line: no wording change; it already names the four points.
* Token `(PA)` holds: the `after`, `m27-review`, is `[x]`; this page takes nothing from `ch08-update-other-edits`' or `ch16-subagent-account`'s pages, and its files, chapters 12, 13 and 19, are none of theirs.

**Done when.**

* [x] Both editions changed as the Contract says in chapters 12, 13 and 19, and nothing else in them, with the review's wording fixes in Divergences.
* [x] `grep -n` finds, in both editions: chapter 12 "or reuses when it exists" / "ou reutiliza quando já existe", "You read and correct each page there too" / "Você também lê e corrige cada página ali", "sent to the delivery's worktree's path when there is one" / "mandado para o caminho do worktree da entrega quando há um"; chapter 13 "you type `/apply a b` in a session in `main/`" / "você digita `/apply a b` em uma sessão em `main/`", "sends a subagent on the slug again" / "manda de novo um subagente no slug"; chapter 19 "or one in `main/` for an `/apply a b`" / "ou uma em `main/` para um `/apply a b`", "which carries the correction to a subagent" / "que leva a correção a um subagente".
* [x] `grep -n "correct one of them in its conversation\|corrige uma delas na sua conversa" book/*/19-worktrees.md` prints nothing.
* [x] Each chapter still opens with its value, no filler and nothing useful cut, no number added, no em dash, no run narration, no version, date or commit hash in chapter text, nothing implying Case B ran on the process.
* [x] `make verify` green.
* [x] `make book` run, both PDF paths recorded.
* [x] Delivery review by one read-only Opus agent over this page and `git diff HEAD` of the six chapter files, against docs/04, docs/05 §§3 and 4 and the kit skills, as its reply lists, which does not name AGENTS.md; it did not keep the session's advisor.
* [x] Page moved to `work/done/`, covered by the last verify.

**Built.** The Contract's changes, in both editions: chapter 12 en :39, :139, :155, the new :158, :164, :192 and :194 (pt :39, :148, :164, the new :167, :173, :201 and :203); chapter 13 the new :21 and :35; chapter 19 :214, :296, :304 and :365. `git diff --stat HEAD` on the six files, before the review's fixes: 26 insertions and 22 deletions, one line added in chapter 12 and one in chapter 13 per edition, nothing else changed; the files now have 197/206, 283/283 and 377/377 lines.

**Divergences.** The delivery review's five findings, all on text this delivery wrote, were fixed; the Contract above keeps the wording as defined, and the chapters read:

* Chapter 13 :35: en "or where the session that typed `/apply a b`, on your command's word, sends a subagent on the slug again."; pt "ou para onde a sessão que digitou `/apply a b`, pela palavra do seu comando, manda de novo um subagente no slug.", so the reopening is tied to the person's command, as the page's Edge asks, and both editions say where it is sent.
* Chapter 13 :21: en opens "With several slugs and a worktree per delivery," and says "the session itself edits nothing"; pt opens "Com vários slugs e um worktree por entrega," and says "a própria sessão não edita nada", so the line does not read against :19, which is about the single command.
* Chapter 12 pt :167: "e corrigir a página e qualquer documento que a correção toque é trabalho desse subagente."
* Chapter 19 :214, both editions: the three folders separated by semicolons; pt :365 "ou mandados para cada um".

**Omissions.** None.

**Proof.**

* The Done when greps print each phrase once per edition, at the lines in Built; the grep for the old chapter 19 :304 wording prints nothing; a grep for the em dash counts 0 in the six files.
* `make verify`: exit 0, all checks passed (the d-nb.info link included), after the chapters' last edit and again after this page's last edit and its move.
* `make book`: exit 0, after the last verify; both editions built, `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf` (with their EPUBs).

**Delivery review.** One read-only Opus agent (a general-purpose subagent with model opus); it did not keep the session's advisor, since a subagent opened this way has none. It read this page and `git diff HEAD` of the six chapter files, chapter 13 en :18 to :30 and chapter 19 en :270 to :305, docs/05 §4, the apply skill and grep hits in docs/05 §3, the propose skill and docs/04. Its reply, as returned:

> Five findings, all low or medium. The Contract is applied exactly in both editions, and nothing else in the six files changed.
>
> **What I read:** the page `work/ch12-13-19-several-slugs-paths.md` and `git diff HEAD` of the six chapter files. For context I read chapter 13 lines 18-30 and chapter 19 lines 270-305 (en), docs/05 §4, the apply skill lines 18-26, and grep hits in docs/05 §3, the propose skill and docs/04.
>
> **Contract and rules**
> - Every Contract change is present word for word in en and pt, in the right places. The diff stat matches: 26 additions and 22 deletions over the six files.
> - The added lines contain no em dash. There is no run narration, version, date or commit hash, nothing about Case B, and no new number. Each new sentence is on its own line.
> - The changes agree with docs/05 §3 ("Corrections happen in the /propose conversation"), docs/05 §4 (the session edits nothing; a subagent is reopened on the command's word), the propose skill ("reused when it exists") and the apply skill ("a subagent sent to its path ... elsewhere, stop before any edit and give the path").
> - The paragraph changed at chapter 19 :304 sits in the batch section, so "as above" points to :296 as intended.
>
> **Findings**
>
> 1. **`book/en/13-apply.md:35` and `book/pt/13-apply.md:35`. Severity: text this delivery wrote (medium).**
>    - The new clause "or the session that typed `/apply a b` sends a subagent on the slug again" names no trigger. It reads as if the session reopens a subagent by itself, which the page's Edge forbids. Chapter 12 ties the same reopening to "the word of your command", and docs/05 §4 to "the command's word".
>    - The two editions also differ. The pt says where the subagent goes ("para onde ... manda"). The en has no "there" and leans on the earlier "where".
>    - Suggested fix (en): "or where the session that typed `/apply a b`, on your command's word, sends a subagent on the slug again".
>    - Suggested fix (pt): "ou para onde a sessão que digitou `/apply a b`, pela palavra do seu comando, manda de novo um subagente no slug".
>
> 2. **`book/en/13-apply.md:21` and `book/pt/13-apply.md:21`. Severity: text this delivery wrote (low).**
>    - The new line opens "With a worktree per delivery, ...", the same words as line 19, which says the fresh session opens in the delivery's worktree. Read quickly, the two lines contradict each other.
>    - Line 35 then says a session in `main/` refuses. The page's "Decisions taken alone" covers that, but the repeated opening makes the clash worse.
>    - Suggested fix: anchor the line to the command, e.g. "Typed this way with a worktree per delivery, `/apply a b` runs from a session in `main/`, as `/propose` does: ...". The pt would match.
>
> 3. **`book/pt/13-apply.md:21`. Severity: text this delivery wrote (low, Portuguese naturalness).**
>    - "a sessão não edita nada ela mesma" is awkward Portuguese.
>    - Chapter 12 pt :172 already says "A própria sessão não edita nada".
>    - Suggested fix: "a própria sessão não edita nada e manda cada subagente para o worktree do seu slug".
>
> 4. **`book/pt/12-propose.md:167`. Severity: text this delivery wrote (low, Portuguese naturalness).**
>    - The sentence says "correção" twice.
>    - "que ela toque" could refer to the session or to the correction.
>    - Suggested fix: "..., e corrigir a página e qualquer documento que a correção toque é trabalho desse subagente."
>
> 5. **`book/en/19-worktrees.md:214` and `book/pt/19-worktrees.md:214`. Severity: text this delivery wrote (low, readability).**
>    - The list now nests commas inside items that are themselves separated by commas. It is hard to tell where the `main/` part ends and the worktree part begins.
>    - Suggested fix: separate the three folders with semicolons, e.g. "one in `main/` for each `/propose`, or one for a `/propose a b` naming both, whose subagents write in each worktree; one in each worktree for its `/apply`, or one in `main/` for an `/apply a b`, which sends a subagent to each worktree's path; and none in the container." The pt would match.
>    - Smaller point, pt :365 only: "ou mandados para ele" is awkward, since "ele" has to stand for "cada worktree". "ou mandados para cada um" reads better.
>
> If you take findings 1, 2 or 5, the page's Contract text needs the same edit so the page and the chapters stay identical.

What was done with it: findings 1, 3, 4 and 5 fixed as suggested; finding 2 fixed by opening the line "With several slugs and a worktree per delivery," which keeps the Done when grep's "you type `/apply a b` in a session in `main/`"; the Contract keeps the wording as defined, and Divergences gives the chapters' text. No new queue line.

**Decisions at build.** Taken alone, by the batch rule to take the recommended option: every review finding fixed, finding 2 in the wording that keeps the Done when grep; the Contract left as defined, with the fixes in Divergences, since records hold what happened.

```commit
docs(ch12-13-19-several-slugs-paths): where several-slug parts happen

- chapter 12: a subagent's page is corrected in the command's session
- chapter 12: worktree created or reused; /apply subagent sent there
- chapter 13: /apply a b runs in main/ with a worktree per delivery
- chapter 19: the sessions for several slugs, and where pages are fixed

work/done/ch12-13-19-several-slugs-paths.md
```
