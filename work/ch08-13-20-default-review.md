# ch08-13-20-default-review

**Objective.** A reader of chapters 8, 13 and 20 finds every sentence that puts a person's review before the commit or the merge marked as the default, and learns that the reviewer the kit assumes is whoever decides the merge, typing it or asking the agent for it; both editions, least change.

**Behaviour.**

* Reading chapter 8's "The install does not stage or commit", the reader learns that by default they read what the install wrote and then commit it, themselves or by asking the agent, as with every change the agent makes.
* Reading chapter 13's "What the team gains", the reader learns a person reads the change, by default the diff before it exists in the history, or, by the Git slot's word, the commit once it lands; the gain still holds: nothing ships without a check and a person.
* Reading chapter 20's "The problem", the reader learns the team's second person reviews, by default before the merge.
* Reading chapter 20's pull request section and its Key points, the reader learns the reviewer the kit assumes is, by default, whoever decides the merge, merging or asking the agent to, or, by the Git slot's word, the person who reviews the merge the agent made.
* Every other sentence reads as it does.
* Fails if: a sentence below still puts a person's review before the commit or the merge with no "by default" (pt "por padrão") or no Git slot alternative; chapter 20 still says "whoever merges is the reviewer" (pt "quem faz o merge é o revisor") or "is, by default, whoever merges" (pt "é, por padrão, quem faz o merge"); a sentence not named here changes; the chapter says how it read before or narrates a run; the two editions differ in sense.

**Contract.** Five sentences in six files. Line numbers are as of this page; this line runs after `ch08-13-17-next-line` and `ch20-merge-and-marks`, which edit the same files, so /apply finds each sentence by its words. Wording is /apply's within the sense given.

1. `book/{en,pt}/08-install-and-hosts.md`:30, section "What the install never touches, and how to update" / "O que a instalação nunca toca, e como atualizar" (candidate 16):
   * en "You read what it wrote and commit it yourself, as by default with every change the agent makes (chapter 13)." becomes "By default you read what it wrote and then commit it, yourself or by asking the agent, as with every change the agent makes (chapter 13)."
   * pt "Você lê o que ela escreveu e faz o commit você mesmo, como por padrão em toda mudança que o agente faz (capítulo 13)." becomes "Por padrão você lê o que ela escreveu e então faz o commit, você mesmo ou pedindo ao agente, como em toda mudança que o agente faz (capítulo 13)."
2. `book/{en,pt}/13-apply.md`:259, section "What the team gains" / "O que o time ganha" (candidate 4):
   * en "Nothing ships without a check and a person: verify and the proof check the build, and a person reads the diff before it exists in the history." becomes "Nothing ships without a check and a person: verify and the proof check the build, and a person reads the change, by default the diff before it exists in the history, or, by the Git slot's word, the commit once it lands."
   * pt "Nada é publicado sem uma checagem e uma pessoa: a verificação e a prova conferem a construção, e uma pessoa lê o diff antes de ele existir no histórico." becomes "Nada é publicado sem uma checagem e uma pessoa: a verificação e a prova conferem a construção, e uma pessoa lê a mudança, por padrão o diff antes de ele existir no histórico, ou, pela palavra do slot Git, o commit depois que ele entra."
3. `book/{en,pt}/20-team-tools.md`:10, section "The problem" / "O problema" (candidate 14, :10):
   * en "a second person who reviews before the merge," becomes "a second person who reviews, by default before the merge,"; the rest of the sentence stays.
   * pt "uma segunda pessoa que revisa antes do merge," becomes "uma segunda pessoa que revisa, por padrão antes do merge,"; the rest stays.
4. `book/{en,pt}/20-team-tools.md`:34, section "The pull request as the team's review" / "O pull request como a revisão do time" (candidate 15):
   * en "By default whoever merges is the reviewer the kit assumes: on a branch ..." becomes "By default the reviewer the kit assumes is whoever decides the merge, merging or asking the agent to: on a branch ..."; from "on a branch" to the end the sentence stays.
   * pt "Por padrão quem faz o merge é o revisor que o kit assume: em um branch ..." becomes "Por padrão o revisor que o kit assume é quem decide o merge, fazendo-o ou pedindo-o ao agente: em um branch ..."; from "em um branch" the sentence stays.
5. `book/{en,pt}/20-team-tools.md`:85, Key points / Pontos-chave (candidate 15):
   * en "is, by default, whoever merges, or, by the Git slot's word," becomes "is, by default, whoever decides the merge, or, by the Git slot's word,"; the rest stays.
   * pt "é, por padrão, quem faz o merge, ou, pela palavra do slot Git," becomes "é, por padrão, quem decide o merge, ou, pela palavra do slot Git,"; the rest stays.

Stays, read and already true: chapter 13:4, :165, :167, :217 and Key point :270, which say "by default" or give the Git slot's alternative; :107 and the example's step 2 (:154), which give `/apply`'s next steps in the kit's words under the default; chapter 20:8 and Key point :84, which say "by default"; chapter 20:33 ("approves the merge"), candidate 14's weak half, rejected by the review; chapter 8:42, :91 and :96, which put no review before a commit.

Terms of docs/03 used: delivery, slot (the Git slot, as the chapters already name it); none new. No number, source note or private case added.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no visual change.

**Out of scope.**

* Chapter 20:33 and chapter 13:4: weak candidates the review rejected (14's :33, 17).
* The next free line, the `after` reading and the board's push in the same files: `ch08-13-17-next-line` and `ch20-merge-and-marks`.
* Chapter 20:8's two sentences on one source line: `ch20-merge-and-marks` (candidate 13).
* docs/03, docs/06 and any other chapter: no edit; the queue line is the driver's.

**Decisions from the documents.**

* The candidates and their files are `work/done/m22-review.md`'s Findings row for this line: 4, 14, 15, 16.
* The default is commit or ask the agent: chapter 13:4, chapter 18 and chapter 23 as the review cites them, and AGENTS.md ("asked, it takes the step the person names").
* "Whoever decides the merge" is the queue line's own wording (docs/06, M22).
* Least change and no before/after: the driver and AGENTS.md.

**Decisions taken alone.**

* Candidate 14's :33 is left as it is: the review marked it weak, and the Findings reject every weak candidate.
* Chapter 13:107 and :154 are left: they repeat the kit's `/apply` next steps (`.claude/skills/apply/SKILL.md`: "review the staged diff; commit") and describe the default run of the lending library example, not a rule for every project.
* Chapter 8:30 moves "by default" to the start of the sentence and names both ways to commit, rather than adding a clause, so the sentence keeps one subject.
* Chapter 13:259 keeps "Nothing ships without a check and a person": with the Git slot's word the person still reads the commit, so the gain stays true with the alternative named.
* The pt uses "quem decide o merge" and "fazendo-o ou pedindo-o ao agente", matching chapter 13's "pedindo ao agente".

**Done when.**

* [ ] Both editions written, the five sentences changed in each pair of files, Portuguese read as Portuguese; each chapter opens as it did and its gain section stays true.
* [ ] `grep -n "whoever merges\|quem faz o merge é\|por padrão, quem faz o merge\|commit it yourself, as by default\|faz o commit você mesmo, como por padrão" book/{en,pt}/{08-install-and-hosts,20-team-tools}.md` finds nothing.
* [ ] `git diff` of this delivery touches only those sentences.
* [ ] No em dash; no "no longer", "now", "não mais", "agora" added; no narrated run.
* [ ] Delivery review as docs/05 §5 says.
* [ ] `make verify` green; `make book` builds both editions and both PDF paths are reported (the driver may run it once for the batch).
* [ ] Only this delivery's paths staged; the page moved to `work/done/` and its commit message suggested.
