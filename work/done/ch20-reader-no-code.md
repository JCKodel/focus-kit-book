# ch20-reader-no-code

**Objective.** After chapter 20 the reader can also say what the kit assumes of a person on the team who does not read code: they take part in `/propose`, where the page is written in user language, test the delivery as its user, and ask any session where things stand or what a page decided; and can tell that person apart from the one a board serves, who opens neither the repository nor a session.

**Behaviour.** What the reader can do or explain after the chapter:

* Asked "our product owner does not read code; where do they fit in the kit?", the reader answers: in three places, each taught in its own chapter: in `/propose`, whose page is written in user language (chapter 12); using the delivery as its user before the commit (chapter 13); and asking any session where things stand or what a page decided (chapters 17 and 7).
* Asked "does that person need a code editor or a developer beside them?", the reader answers: no; the kit assumes they open a session of the host at the project's root and talk, as chapter 17's manager does, and the code stays the coder's to review.
* Asked "then who is the board for?", the reader answers: for the people who open neither the repository nor a session, such as a client or a manager who only follows progress; the board is the queue's one-way mirror, and the person who does not read code but opens a session asks the queue itself.
* Edge: the one-person sentence on line 8 stays the kit's assumption for the roles that read code (propose, use, review the staged diff, commit); the new sentence adds a person, it does not split those roles.
* Edge: chapter 17's manager section stays as it is; chapter 20 points to it and does not repeat its status example, its "no status command" line or its plan mode paragraph.
* Fails: the status answer of chapter 17 or a page section of chapter 12 repeated in chapter 20; a sentence saying the non-coder reviews the diff or commits; any version, date, "now", before/after or history of how the kit came to say this; a sentence on how Case A's manager or client took part; one edition changed and not the other.

**Contract.** Files `book/en/20-team-tools.md` and `book/pt/20-team-tools.md`, same changes in both, line numbers as of this page (same in both editions):

* Opening (line 3): one clause added, after "the reviewer the kit assumes": and what it assumes of a teammate who does not read code (pt: "e o que ele assume de quem no time não lê código"). The rest of line 3 and line 4 stay.
* `## The problem` / `## O problema`: one sentence inserted after line 8: a person who does not read code takes part in `/propose`, where the page is written in user language ([chapter 12](12-propose.md)), tests the delivery as its user ([chapter 13](13-apply.md)), and asks any session where things stand or what a page decided ([chapter 17](17-project-as-assistant.md)). Each pointer sits on the clause it supports; no fourth link to chapter 7 (chapter 17's section already leads there through the rules file, and one sentence holds three pointers at most). Portuguese from the kit's README.pt: "participa do `/propose`, onde a página é escrita em linguagem de usuário, testa a entrega como seu usuário e pergunta a qualquer sessão em que ponto as coisas estão ou o que uma página decidiu", with "em que pé" as chapter 17 writes it.
* Line 9: "a way for people who never open the repository, a manager or a client, to see progress" becomes "a way for people who open neither the repository nor a session, a client or a manager, to see progress" (pt: "um jeito de quem não abre nem o repositório nem uma sessão, um cliente ou um gerente, ver o progresso"), so the board's audience does not read as the person of the new sentence. Line 10 stays.
* `## Key points` / `## Pontos-chave`: one bullet added first, before the pull request bullet (line 83): the kit assumes one person who proposes, uses, reviews the staged diff and commits, and a teammate who does not read code takes part in `/propose`, tests the delivery as its user and asks a session where things stand or what a page decided; a board serves those who open neither. No other bullet changes.
* Nothing else: the pull request section, Issues, Boards (line 52 "rarely open a repository" stays: it is about a manager who follows a board), Question deliveries, the wiki section and What the team gains keep every byte.
* Wording: one sentence per line; no em dash; Portuguese "o kit assume" as line 8 already writes it, "linguagem de usuário", "sessão".
* Terms of docs/03: `delivery`, `page`, `trunk` already present. No new term; no docs/03 row.
* Sources: focus-kit README at 2026.10.19 ("A person who does not read code takes part in `/propose`, where the page is written in user language, tests the delivery as its user, and asks any session where things stand or what a page decided.") and README.pt.md (same passage); AGENTS.md of the kit's template, answering what a delivery decided from its page (taught in chapter 7, line 114). Named in prose as the kit's assumption; no footnote, since the reader gains nothing to open (docs/04).
* Cases: none. No number.

**States.** Inapplicable: prose, no screen.

**Visual reference.** Inapplicable: no visual change.

**Out of scope.**

* Chapter 17's manager section: it already teaches where things stand and the plan mode; chapter 20 points to it.
* Chapter 7's what-a-page-decided line and chapter 12's user-language Behaviour: already taught; pointed to, not repeated.
* The board, its slot and question deliveries: `ch20-one-person-assumed`, done.
* How Case A's manager or client took part: a private case's detail no document gives, and it would need OD-3 approval.
* The kit's history of this sentence: the book teaches the kit as it is (AGENTS.md, M21).

**Decisions from the documents.**

* The three things the person does are the kit's README sentence at 2026.10.19, in both languages; the Portuguese edition follows README.pt.md's verbs.
* Teaching the kit as it is today, no version or "now": AGENTS.md and the M21 rule.
* Each behaviour is already taught in its own chapter (12 line 42, 13 lines 107 and 172, 17 lines 113 to 137, 7 line 114), so chapter 20 states the assumption and points: AGENTS.md ("say each thing once" from `ch20-21-git-cut`).

**Decisions taken alone.**

* Home: chapter 20, as the line says. Chapter 17's manager session was considered, since it already teaches where things stand; it was not clearly better: it covers one of the three behaviours, while the README puts this sentence right after the one-person assumption that chapter 20 line 8 states, and chapter 20's problem already names the manager and the client. Chapter 17 is untouched and pointed to.
* The sentence goes right after line 8, mirroring the README's order.
* Line 9 changes so the board's audience is those who open neither the repository nor a session: without it, the paragraph would assume a non-coder who asks sessions and then build a board for people who "never open the repository", which reads as the same person.
* "a manager or a client" becomes "a client or a manager" on line 9, the client first, since chapter 17 already gives the manager a session.
* No pointer to chapter 7 in the new sentence; chapter 17 is the one place a non-coder's questions are taught.
* A new key point bullet rather than a clause on an existing one: no existing bullet is about the people the kit assumes; the bullet also carries line 8's assumption, which no key point says yet.

**Done when.**

* [x] Both editions changed in the same places (opening clause, the sentence after line 8, line 9, one key point bullet) and nowhere else; chapter 17 untouched.
* [x] The chapter still opens with its value; no filler, nothing useful cut; one sentence per line kept.
* [x] Every pointer sits inside a sentence that says something; nothing of chapters 7, 12, 13 or 17 repeated.
* [x] No version, date, "now", before/after or history; no em dash; no number, so none to source; no private case text, so no OD-3 approval.
* [x] Chapter 17's lines 113 to 137 and chapter 20's line 9 agree on who opens what: a session for the person who does not read code, the board for those who open neither.
* [x] `make verify` green; `make book` builds both editions and both PDF paths are reported (the driver runs it once, as for `ch20-one-person-assumed`).
* [x] Delivery review as docs/05 §5 says; only this delivery's paths and its hunk of docs/06 staged (the driver's, in this batch); the page moved to `work/done/` and its commit message suggested.

**Proof.** `make verify` green after the last edit. `make book` is run once by the driver at the end of the batch, which reports both PDF paths.

**Divergences.** One, from the review: the Portuguese opening clause reads "e o que o kit assume de quem no time não lê código" instead of the Contract's "e o que ele assume", since "ele" could read as "o revisor", the nearest masculine noun. The English "it" is unambiguous and stays.

**Omissions.** None.

**Delivery review.** A read-only Opus agent read `git diff HEAD` of both chapter files against this page, docs/04 and AGENTS.md. No must-fix finding. Two suggestions: the Portuguese "ele" ambiguity, fixed as above; and adding "who only follows progress" to line 9, declined because the page fixes that line's wording and the Behaviour already carries the distinction.

**Decisions taken alone during /apply.**

* The Portuguese key point bullet writes "quem no time não lê código", matching the opening clause, where the English says "a teammate".
* The review's Portuguese fix above, applied without the author, since it only removes an ambiguity in text this delivery wrote.

```commit
docs(ch20-reader-no-code): say what the kit assumes of a non-coder

- ch 20: a teammate who does not read code proposes, uses, asks
- ch 20: the board serves those who open neither repository nor session
- ch 20: key point on whom the kit assumes; both editions

work/done/ch20-reader-no-code.md
```
