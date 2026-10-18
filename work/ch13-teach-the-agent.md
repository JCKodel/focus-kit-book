# ch13-teach-the-agent

**Objective.** A reader of chapter 13, reviewing the staged change, asks the agent for each correction of taste as well as of fault, saying what they want instead and why, and knows that the preference lands in a project document, so the agent learns and makes the same mistake less often; both editions. From the author's reading of the book on 2026-10-18: "In 'Review the staged change', talk to the agent about problems: if you prefer the code a certain way, tell the agent and explain what you want instead of fixing it yourself. Many agents keep a memory that is updated by your corrections; some can change the kit's files, write new ADRs, and so on. Early in a project it is normal for agents to do things that do not suit the team's taste or needs; teaching the agent is the most efficient way for it to learn and make fewer mistakes later. Treat the agent as a member of the team."

**Decided without the author.** The batch had no one to answer; each choice is the recommended one.

1. *Five lines inserted, nothing replaced.* Chapter 13's "Review the staged change" already says "Ask the agent for each correction, in the same session, never by hand" and why (en 13:165-166, pt 13:165-166 at /propose); those two lines stay. What the chapter lacks is the draft's "so it learns": taste counts as a correction, where the preference lands, the author's experience and the colleague. That the next session follows a written rule without being told again is chapter 7's (en 07:130), so the line says where the preference goes and stops there. The five lines go right after en 13:166 / pt 13:166, before the automation-bias paragraph. Source: the draft; book/en/13-apply.md; docs/04 §Writing the book (nothing said twice, no filler).
2. *"Some can change the kit's files, write new ADRs" becomes: the preference goes into the document that owns it, a convention in docs/04 or a decision with its reason in an ADR, in the same delivery.* The kit's files are the skills the setup file writes, which the project does not edit (chapter 8, "What the install never touches"); what the kit lets the agent write is the project's documents, and `/apply` already "updates their owning documents and ADRs" (`.claude/skills/apply/SKILL.md`; en 13:85, "a new rule into the document that owns it, a decision into docs/adr/"). The words "kit's files" do not appear. Source: chapter 8; the apply skill; chapter 13.
3. *Host memory said host-neutrally, with no citation.* The draft's "many agents keep a memory" is true of some hosts and not shown for every row of chapter 8's table; one sentence says that whatever memory a host keeps of its own, the one every host and every colleague reads is the project's documents, which docs/03 calls "the project's memory". It names no host, so it needs no source note, and it reuses no footnote of chapter 8. Source: docs/03 row "project documents"; chapter 8's table; docs/04 §Evidence.
4. *The author's experience in the first person, with no project named and no number.* "In my experience, early in a project the agent often does things that do not suit the team's taste or needs." No count exists, so the line claims none, and naming no project keeps it clear of `pt-ninjobs-masculine`'s article change. Source: docs/04 §Voice and §Evidence; the draft.
5. *The colleague kept to one sentence.* "Treat the agent as a new member of the team: you explain once what the team wants, where it can read it again." Trust is not re-taught here: the prologue (en 00:53-54) and chapter 7 (en 07:135) hold it, and chapter 17's "The person is the brain" holds the three jobs. Source: those chapters; docs/04 (nothing said twice).
6. *The key point gains a few words; "What the team gains" stays.* The key point (en 13:231, pt 13:231) already says "ask for each correction in the same session"; it gains "saying what you want instead and why", so it carries the chapter's new idea. The gain section has no number for teaching the agent, and docs/04 §A gain per chapter allows the gain alone; the chapter's gain is unchanged. Source: docs/04.
7. *No chapter pointer added.* The lines lean on no detail of an earlier chapter worth reopening, and point forward to none. Source: docs/04 §Chapter pointers.
8. No new docs/03 term, no new queue line, no split.

**Behaviour.**

* The reader of chapter 13, in English, under "Review the staged change", after "The same session keeps the reasoning of the build: it knows why it made each choice, which a fresh session would have to guess.", reads, one sentence per line:
  * "That holds for taste as much as for faults: when the code works but you would have written it another way, say what you want instead and why, rather than rewriting it yourself."
  * "A preference that should hold beyond this delivery goes where the next session reads it, a convention in docs/04 or a decision with its reason in an ADR, written in this same delivery."
  * "Whatever memory your host keeps of its own, the memory every host and every colleague reads is the project's documents."
  * "In my experience, early in a project the agent often does things that do not suit the team's taste or needs; saying it once, so it lands in a document, cost me less than fixing the same thing by hand in every delivery."
  * "Treat the agent as a new member of the team: you explain once what the team wants, where it can read it again."
* The reader of the Portuguese edition, under "Revise a mudança em stage", after "A mesma sessão guarda o raciocínio da construção: ela sabe por que fez cada escolha, o que uma sessão nova teria de adivinhar.", reads:
  * "Isso vale para o gosto tanto quanto para os defeitos: quando o código funciona mas você o teria escrito de outro jeito, diga o que quer no lugar e por quê, em vez de reescrevê-lo você mesmo."
  * "Uma preferência que deve valer além desta entrega vai para onde a próxima sessão a lê, uma convenção no docs/04 ou uma decisão com o seu motivo em um ADR, escrita nesta mesma entrega."
  * "Seja qual for a memória que o seu host guarda por conta própria, a memória que todo host e todo colega leem são os documentos do projeto."
  * "Na minha experiência, no começo de um projeto o agente muitas vezes faz coisas que não combinam com o gosto ou as necessidades do time; dizer uma vez, para que vá parar em um documento, me custou menos do que corrigir a mesma coisa à mão em toda entrega."
  * "Trate o agente como um novo membro do time: você explica uma vez o que o time quer, em um lugar onde ele pode ler de novo."
* The key point, en: "* Review the staged change against the page, ask for each correction in the same session, saying what you want instead and why, and commit it yourself: that review is the defence against automation bias, the habit of trusting the agent after many good deliveries."; pt: "* Revise a mudança em stage contra a página, peça cada correção na mesma sessão, dizendo o que quer no lugar e por quê, e faça você o commit: essa revisão é a defesa contra o viés de automação, o hábito de confiar no agente depois de muitas entregas boas."
* The lines before and after them ("Ask the agent for each correction" and "A person who commits after many good deliveries", and their Portuguese) are unchanged.
* Checked at apply time:
  * `grep -n "That holds for taste\|Isso vale para o gosto" book/*/13-apply.md` prints one line per edition.
  * `grep -n "saying what you want instead and why\|dizendo o que quer no lugar e por quê" book/*/13-apply.md` prints one line per edition, the key point.
  * `grep -n "kit's files\|arquivos do kit" book/*/13-apply.md` prints nothing.
  * `git diff book/` shows only the five inserted lines and the key point per edition.
* Fails: en 13:165-166 or pt 13:165-166 changed or removed; a claim about one host's memory, or a host named in the new lines; the words "kit's files"; a number; Ninjobs or a private case named; a chapter pointer added; trust re-taught beyond the one sentence; any other line of chapter 13 changed; an em dash.

**Contract.**

* Files: `book/en/13-apply.md`, `book/pt/13-apply.md`; section "Review the staged change" / "Revise a mudança em stage" (insertion after en 13:166 / pt 13:166 at /propose) and the last key point (en 13:231, pt 13:231 at /propose).
* Terms of docs/03: none new; uses "host", "project documents", "ADR", "delivery". Sources: none added or removed. Cases: none; the author's experience, unnamed. Exercises: none (ADR-0017).
* docs/00 to docs/05: no change. docs/06: this line's marks only, set by the driver and by /apply; no new queue line.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Deliveries in flight on the same files.**

* `try-before-commit` (still a draft) names chapter 13's staged review as its first candidate, and its "small things fixed in conversation while the delivery is open" leans on this delivery's lines. The split: this page owns "correct by talking, so the agent learns"; `try-before-commit` owns "use the software before you commit". Whichever lands second edits the section as the first left it; the lines are found by their text, not their number. If it lands after, its sentence on small fixes can say "in conversation, as above" instead of saying again how to ask.
* `ch07-talk-not-edit` says the same idea for the documents in chapter 7 ("you talk to the agent to change them"); this delivery says it for the code in chapter 13. The two agree and neither edits the other's file.
* `pt-ninjobs-masculine` changes Ninjobs's article in pt 13:142, outside this section; the new lines name no Ninjobs, so no shared hunk.
* `early-no-forward-links` edits chapters 0 to 7 only; this delivery adds no pointer.

**Out of scope.**

* Using the software before committing: `try-before-commit`.
* The documents edited by conversation, chapter 7: `ch07-talk-not-edit`.
* A host's own memory, how it works or which hosts have one: the book teaches the project's documents, read by every host (decision 3).
* "What the team gains" of chapter 13: decision 6.

**Done when.**

* [ ] Both editions written: the five lines and the key point as Behaviour says.
* [ ] Chapter 13 still opens with its value, keeps its gain, no filler and nothing useful cut.
* [ ] Every number sourced: none added.
* [ ] `make verify` green: edition parity, prose rules, width, disclosure scan, no em dash.
* [ ] The author's approval of an anonymized passage: inapplicable, no private case (docs/00 OD-3).
* [ ] `make book` run; both PDF paths given to the author.
* [ ] Page in `work/done/`, the line `[x]`, staged by its paths and its hunk of docs/06, commit message in a `commit` block.
