# ch11-commit-command

**Objective.** The reader of chapter 11 can commit the staged change with the suggested message themselves: they know the command, what git does when they run it, and how to choose the editor it opens.

**Behaviour.**

* Where the chapter says "Then I committed the staged tree with the suggested message", the reader sees the command the author ran, `git commit`, in a code block.
* It says what happens: with no `-m`, git opens an editor; the author pasted the suggested message, subject, blank line and bullets as the agent gave them, saved and closed, and the commit exists when the editor closes.
* It says in one sentence that git opens the editor named in `core.editor` (usually vi when none is set), and that `git config --global core.editor nano`, or `"code --wait"` for VS Code, chooses another.
* It says that chapter 17 teaches the rest of git. Tagging and pushing stay as they are, as what the author did; the reader is not told to do either.
* Exercise 8.1, which asks the reader to commit the kit before chapter 11, points forward to chapter 11 for how.
* The Portuguese says the same in the same places.
* Finding F16 of the M3 review is settled.

**Contract.**

* Files: `book/en/11-apply.md`, at line 346 today ("Then I committed the staged tree…"); `book/pt/11-apply.md`, at line 353 today ("Depois fiz o commit da árvore no stage…").
* `book/en/08-analyze.md` line 346 today: "install the kit (chapter 5), commit it" becomes "install the kit (chapter 5), commit it (chapter 11 shows how)"; `book/pt/08-analyze.md` line 349 today: "faça o commit" gains "(o capítulo 11 mostra como)". Nothing else in chapter 8 changes.
* One code block holding `git commit`, and a few sentences around it. No new section, heading or list. The paragraph on why the agent never commits (en 349 to 351) and the key points stay as they are.
* Fact it rests on: the author ran `git commit` with no `-m` in the clinic, git opened nano, and the message was pasted there; the commit is `d5b5c03` at `book-v1/apply`, whose message is the suggested one, already quoted at en 214 to 223.
* Sources: no new note. Terms of docs/03, cases: unchanged.
* Exercises: Exercise 11.2 unchanged in wording; the command it needs is now in the chapter.

**Out of scope.**

* `git commit -m` and `git commit -F`: one command is enough here, and `-m` with line breaks depends on the shell; chapter 17 teaches the rest.
* Tagging and pushing for the reader: the chapter tag is the book's, and the reader's clinic may have no remote; chapter 17.
* Checking the commit afterwards (`git log`, `git show`): chapter 17.
* Chapters 7, 9 and 10: none asks the reader to commit (Exercise 9 says to commit nothing); chapter 8's one request gets only the pointer above.

**Done when.**

* [x] Both editions show `git commit` in a code block where the author commits, with what git does and the editor sentence.
* [x] Exercise 8.1 points to chapter 11 in both editions.
* [x] The "never commits" paragraph, the key points and Exercise 11.2 unchanged in both editions.
* [x] `make verify` green.
* [x] `make book` run, and both PDF paths given to the author.
* [x] Page in `work/done/`, `[x]` in docs/06, staged, commit message suggested.

**What happened.**

* Built as planned: in both editions, the sentence "Then I committed the staged tree with the suggested message" now ends with a colon and a code block holding `git commit`, followed by four sentences: what git does with no `-m` (the author's editor, nano, the message pasted as given, the commit existing when the editor closes), the `core.editor` sentence with the nano and VS Code commands, the pointer to chapter 17, and the tagging and pushing, which were split off the committing sentence and stay as what the author did.
* Exercise 8.1 gains "(chapter 11 shows how)" and "(o capítulo 11 mostra como)"; nothing else in chapter 8 changed.
* Diverged: the VS Code option is written as the whole command, `git config --global core.editor "code --wait"`, rather than only `"code --wait"`, so the reader does not have to assemble it. Chapter 17 is named in plain text, without a link, as the book does for chapters not yet written.
* The "never commits" paragraph, the key points and Exercise 11.2 are untouched in both editions. No note, term, case or document other than the chapters and docs/06 changed; no ADR.
* Proof: `make verify` green; `make book` built both PDFs.
* Finding F16 of the M3 review is settled.
