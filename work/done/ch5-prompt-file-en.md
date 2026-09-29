# ch5-prompt-file-en

**Objective.** The English reader of chapter 5 gets the same explanation of the Copilot prompt file as the Portuguese reader: what its last line tells the agent.

**Behaviour.**

* After the prompt file's code block, the English gains the sentence the Portuguese already has (`book/pt/05-install-and-hosts.md:113`): the last line tells the agent to read the skill and follow it, and that `$ARGUMENTS` is the value you type.
* The next sentence, on `${input:slug}`, follows it unchanged.
* The Portuguese is unchanged; English is the source again and says what the translation says.
* Finding F5 of the M3 review is settled.

**Contract.**

* Files: `book/en/05-install-and-hosts.md`, one sentence added after line 93 today. `book/pt/05-install-and-hosts.md` unchanged.
* Terms of docs/03: host, command. No new term.
* Sources: none new; the prompt file is already linked at its tag.
* Cases: none. Exercises: unchanged. The guided project: unchanged, no tag.

**Out of scope.**

* A sweep of chapter 5 for other English and Portuguese differences: the review found only this one.

**Done when.**

* [x] English sentence added; its meaning is the Portuguese sentence's.
* [x] `make verify` green.
* [x] `make book` run, and both PDF paths given to the author.
* [x] Page in `work/done/`, `[x]` in docs/06, staged, commit message suggested.

**What happened.**

* `book/en/05-install-and-hosts.md:95`, after the prompt file's code block: "The last line tells the agent to read the skill and follow it, and that `$ARGUMENTS` is the value you type." It says what `book/pt/05-install-and-hosts.md:113` says, clause for clause; the sentence on `${input:slug}` follows it unchanged.
* The Portuguese is unchanged. Nothing dropped, nothing diverged from the plan. No document changed: host and command are already in docs/03. Finding F5 of the M3 review is settled.
* Proof: `make verify` green; `make book` builds both editions, `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.
