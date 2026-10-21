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

* [ ] Both editions changed as the Contract says in chapters 12, 13 and 19, and nothing else in them.
* [ ] `grep -n` finds, in both editions: chapter 12 "or reuses when it exists" / "ou reutiliza quando já existe", "You read and correct each page there too" / "Você também lê e corrige cada página ali", "sent to the delivery's worktree's path when there is one" / "mandado para o caminho do worktree da entrega quando há um"; chapter 13 "you type `/apply a b` in a session in `main/`" / "você digita `/apply a b` em uma sessão em `main/`", "sends a subagent on the slug again" / "manda de novo um subagente no slug"; chapter 19 "or one in `main/` for an `/apply a b`" / "ou uma em `main/` para um `/apply a b`", "which carries the correction to a subagent" / "que leva a correção a um subagente".
* [ ] `grep -n "correct one of them in its conversation\|corrige uma delas na sua conversa" book/*/19-worktrees.md` prints nothing.
* [ ] Each chapter still opens with its value, no filler and nothing useful cut, no number added, no em dash, no run narration, no version, date or commit hash in chapter text, nothing implying Case B ran on the process.
* [ ] `make verify` green.
* [ ] `make book` run, both PDF paths recorded.
* [ ] Delivery review by a read-only Opus agent over this page and `git diff HEAD` of the six chapter files, against docs/04 and AGENTS.md; the record names the agent's model and whether it kept the session's advisor, and the tick says the same.
* [ ] Page moved to `work/done/`, covered by the last verify.
