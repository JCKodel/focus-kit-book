# pt-stage-term

**Objective.** The Portuguese reader meets one term for git's stage from chapter 4 on, "stage", said with `git add` the first time, so "the agent stages, the person commits" reads as the same step in every chapter.

**Behaviour.**

* docs/03 gains the term first: stage, Portuguese "stage", identifier `git add`, meaning: to mark changes for the next commit; the agent stages and the person commits.
* Chapter 4, both editions: the rule "The agent never commits" says the agent stages the work with `git add`. The English gains "with `git add`", which the Portuguese already has, so both editions say the same.
* Every Portuguese "prepara" or "preparei" that means git's stage becomes a form of "colocar em stage" (or "pôr no stage"), as chapters 7 to 12 already say: chapter 4 line 29, chapter 5 lines 46 and 77, chapter 6 lines 88, 144 and 168.
* The lines of chapter 6 that quote the project's own documents (docs/05 §5 and §6, AGENTS.md) read, in Portuguese, the same as chapter 7's quote of the clinic's AGENTS.md: "O agente coloca em stage e sugere a mensagem de commit. Ele nunca faz commit."
* No "prepara" in the Portuguese edition means stage afterwards; a search for "prepar" finds only other meanings.
* Finding F8 of the M3 review is settled.

**Contract.**

* docs/03, one new row after "unit of work" or beside the trunk rows, as it fits the table:

      | stage | stage | `git add` | To mark changes for the next commit; the agent stages, the person reviews and commits. |

* Files: docs/03-Domain.md; `book/en/04-birth-of-focus-kit.md` line 29; `book/pt/04-birth-of-focus-kit.md` line 29; `book/pt/05-install-and-hosts.md` lines 46 and 77; `book/pt/06-the-documents.md` lines 88, 144 and 168. Line numbers are today's.
* Chapter 5 line 46 is the Portuguese translation of the agent's English reply at line 28; the translation changes, the English reply does not.
* Sources, cases, exercises: unchanged.

**Out of scope.**

* A glossary entry in the book: the glossary appendix is generated from docs/03 in M7.
* The English edition beyond chapter 4: it already says "stage" throughout.
* `ch4-adr-docs05` and `ch4-rule-failures`, in the same chapter: their own deliveries; whichever is applied later works on the tree this one leaves.

**Done when.**

* [x] docs/03 has the row, in both languages.
* [x] Every listed line changed; `grep -n "prepar" book/pt/*.md` shows no git meaning left.
* [x] `make verify` green.
* [x] `make book` run, and both PDF paths given to the author.
* [x] Page in `work/done/`, `[x]` in docs/06, staged, commit message suggested.

**What happened.**

* docs/03 has the row "stage", identifier `git add`, just before "trunk", with the other git terms.
* Chapter 4: the English reads "It stages the work with `git add`"; the Portuguese "Ele coloca o trabalho em stage com `git add`".
* Chapter 5, Portuguese: line 46 "não coloquei nada em stage nem fiz commit" (the English reply at line 28 unchanged); line 77 "A instalação não coloca nada em stage nem faz commit", the same form as chapter 7 line 210.
* Chapter 6, Portuguese: line 88 "O agente coloca em stage; ele nunca faz commit nem merge."; line 144 "O agente coloca em stage e sugere a mensagem; o autor revisa e faz o commit."; line 168 reads exactly as chapter 7 line 181.
* `grep -n "prepar" book/pt/*.md` finds nothing: no other meaning of "prepar" was in the edition either.
* Nothing dropped, nothing diverged from the plan. Finding F8 of the M3 review is settled.
* Proof: `make verify` green; `make book` builds both editions, `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.
