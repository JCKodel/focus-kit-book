# ch7-agents-fixed-lines

**Objective.** A reader of chapter 7 can take the clinic's `AGENTS.md` non-negotiables and say which six lines the conversation wrote for this project and which three the kit's template writes in every project. They can also say why the one project line with no document in parentheses, "An open decision in docs/00 is asked, never assumed.", still has its reason in a document.

**Behaviour.**

* The reader can say that the kit's template asks for three to six rules of the project's own and then writes three fixed lines, and can open that template at the chapter's tag to check it.
* The reader can split the excerpt: the six project lines run from "Every business rule is a pure use case" to "An open decision in docs/00 is asked, never assumed."; the three fixed lines are "One delivery = one page", "No em dash" and "The agent stages and suggests the commit message".
* The reader can say that five project lines name their document or ADR in parentheses, and that the sixth names docs/00 in its own words. That line makes the open decisions of docs/00, the list chapter 6 quoted a line of, something a session asks about and never settles alone.
* The booking code sentence still says the code comes from a "your call".
* Both editions say the same.
* Finding F4 of the M4.1 review is settled (`work/done/m4.1-review-run/findings.md:18`).

**Contract.**

Sentences are found by their quoted text. The line numbers are from commit `cad46ef`. No other page in flight touches chapter 7.

* `book/en/07-brainstorm.md` and `book/pt/07-brainstorm.md`, section "Purpose" (pt "Propósito"; the paragraph before and the paragraph after the `AGENTS.md` excerpt; the excerpt is not changed):
  * en:165: "Its non-negotiables are the kit's template with the project's own rules above the three fixed lines." becomes "Its non-negotiables follow the kit's [template](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/brainstorm/.claude/skills/brainstorm/references/documents.md), which asks for three to six rules of the project's own and then writes three fixed lines in every project: the clinic has six of its own, from "Every business rule" to "An open decision", and the three fixed lines from "One delivery" down."
  * pt:167: "Os inegociáveis dele são o modelo do kit com as regras do próprio projeto acima das três linhas fixas." becomes "Os inegociáveis dele seguem o [modelo](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/brainstorm/.claude/skills/brainstorm/references/documents.md) do kit, que pede de três a seis regras do próprio projeto e depois escreve três linhas fixas em todo projeto: a clínica tem seis dela, de "Toda regra de negócio" a "Uma decisão em aberto", e as três linhas fixas de "Uma entrega" para baixo." The quoted starts match the Portuguese excerpt as printed at pt:172-181.
  * en:184: "Each project line points at the document or ADR that holds its reason, and the booking code comes from a "your call": the agent's answer to how a client with no account proves an appointment is theirs." becomes "The first five project lines each point at the document or ADR that holds its reason. The sixth names docs/00 in its own words: it makes the open decisions of docs/00, the list chapter 6 quoted a line of, something a session asks about and never settles alone. The booking code comes from a "your call": the agent's answer to how a client with no account proves an appointment is theirs."
  * pt:187: "Cada linha do projeto aponta para o documento ou o ADR que guarda o seu motivo, e o código de agendamento vem de um "your call": a resposta do agente para como um cliente sem conta prova que um agendamento é dele." becomes "As cinco primeiras linhas do projeto apontam, cada uma, para o documento ou o ADR que guarda o seu motivo. A sexta nomeia o docs/00 no próprio texto: ela faz das decisões em aberto do docs/00, a lista de que o capítulo 6 citou uma linha, algo que uma sessão pergunta e nunca decide sozinha. O código de agendamento vem de um "your call": a resposta do agente para como um cliente sem conta prova que um agendamento é dele."
  * These are proposals for `/apply` to tighten; the facts they state do not change.
* The facts, checked when the page was proposed. At `book-v1/brainstorm` in `../focus-kit-clinic`, `.claude/skills/brainstorm/references/documents.md:221-227` holds the template's Non-negotiables: the placeholder "three to six rules that protect what the product is; from docs/00 and docs/01, one line each", then "One delivery = one page in work/<slug>.md", "No em dash in any text a user reads." and "The agent stages and suggests the commit message. It never commits." "Open decision" appears in no kit file at that tag. The line came from the conversation, which recorded open decisions "which no delivery may settle by assumption" (`work/done/brainstorm-run/questions.md:64`), and docs/00 §Open decisions opens "Nobody closes these alone. A delivery that needs one asks first." The tag is published, so the link check can open the new link.
* Terms of docs/03: none new. "Non-negotiables", "fixed line" and "open decision" are used as the chapter already uses them.
* Sources: the kit's template at the chapter's tag, linked in place, since the reader gains a file to open and check the split against. No footnote is added. `[^brainstorm-run]` is unchanged.
* Cases: none. Ninjobs is not used. Exercises: unchanged. Key points: unchanged, since none of them names the split.

**Out of scope.**

* The `AGENTS.md` excerpt and the clinic's `AGENTS.md`: both are real and already right.
* Chapter 6's `AGENTS.md` excerpt of this book: it names no split, so the finding does not reach it.
* Rewording the sixth line in the clinic to add "(docs/00)": the clinic's history is quoted as it is, and the chapter explains the line rather than changing it.
* The kit's `SETUP.md` template: it matches the tag, and the chapter links the tag, which never moves.

**Done when.**

* [x] Both editions written, with the two sentences replaced as the Contract says, and the excerpt untouched.
* [x] The chapter still opens with its value; no filler and nothing useful cut.
* [x] Every fact the new sentences state is checkable at the linked tag or in the excerpt.
* [x] `make verify` green, the link check opening the template link.
* [x] `make book`, and both PDF paths given to the author to review. Left for the batch driver, which builds once at the end of the loop. Done by the driver on 047d672: both editions build.
* [x] F4 marked settled on this page's record.

**What happened.**

* Revalidated against the tree: no commit since `cad46ef` touched chapter 7; the sentences were still at en:165, en:184, pt:167, pt:187, and the excerpt at pt:172-181. At `book-v1/brainstorm` the template's Non-negotiables still hold the placeholder and the three fixed lines, and "open decision" appears in no `.claude/` kit file. Chapter 6 still quotes a line of docs/00's open decisions (en:240, pt:244).
* Tightened alone (batch, no conversation): "the clinic has six of its own" became "the clinic's six run from" (pt "as seis da clínica vão de"); "The first five project lines each point at" gained "in parentheses" (pt "cada uma entre parênteses"), since that is what the sixth line lacks. The second replacement is three sentences on three lines, one sentence per line as the chapter writes.
* The template link returned 200; `make verify` green.
* F4 of the M4.1 review (`work/done/m4.1-review-run/findings.md:18`) is settled: the excerpt now splits into six project lines and three fixed lines, and the sixth line's reason is named.
* No document changed: no new term, rule or decision.
* `make book` not run here, by the batch's instruction.
