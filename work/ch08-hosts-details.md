# ch08-hosts-details

**Objective.** The reader can invoke the kit on each listed host without mistaking an optional pointer for a requirement or attaching a delivery slug to a project-start command.

**Behaviour.**

* Reading the Antigravity row, the reader sees that it reads `AGENTS.md` directly and that `.agents/rules/focus-kit.md` is an always-on pointer, not the only way rules reach it.
* Using Jules, Junie, Warp, Kiro, Roo Code or Cline, the reader finds a row in both chapters and asks in words to follow `.agents/skills/<name>/SKILL.md`; the text promises neither automatic skill discovery nor a slash command for that group.
* Starting a project, the reader invokes `/brainstorm` or `/analyze` in the host's form without a slug; defining or building `lend-book`, the reader supplies that slug to `/propose` or `/apply`, or answers the host wrapper's question.
* In Claude Code, a matching skill description alone does not authorize a run: its `disable-model-invocation: true` means the person names it; the prose does not attribute equivalent enforcement to all hosts.

**Contract.** Edit `book/en/08-install-and-hosts.md`, `book/pt/08-install-and-hosts.md`, `book/en/10-quick-guide.md` and `book/pt/10-quick-guide.md`, the host tables and their explanatory paragraphs.
Primary source: focus-kit SETUP.md §1's table, invocation-policy paragraph and §§3.1 to 3.4, version 2026.10.18.1 read in the kit's working tree; public source <https://github.com/JCKodel/focus-kit/blob/main/SETUP.md>.
The four facts above are already explicit in that source; make no additional claim about current vendor behavior without checking the vendor page named by it.
Keep the existing Claude Code skills note as the policy source, checking <https://code.claude.com/docs/en/skills> during application; name SETUP.md §1 in prose for the grouped row, without a source note linking to a kit file, as docs/04 requires.
Use docs/03's host, command, rules file and delivery terms; no new concept.
Choose a prose explanation of which commands take a slug rather than expanding both tables into a reference manual, per docs/00's non-goals.

**States.** Inapplicable: prose, no screen.

**Visual reference.** Inapplicable: existing tables and chapter layout.

**Out of scope.** Claude Code's fallback when no `CLAUDE.md` exists belongs to `ch08-update-2026-10-18-1`; fresh-session instructions belong to `ch08-10-fresh-start`; no host or skill configuration changes.

**Done when.**

* [ ] Both editions pass the four Behaviour checks, and chapters 8 and 10 give the same invocations and host grouping.
* [ ] Each chapter keeps its opening value and evidenced team gain, with no filler or useful content cut; every number and artifact retains a checked source.
* [ ] Source notes and headings stay in edition parity; no private case is added, so OD-3 approval is inapplicable.
* [ ] `make verify` and `make book` pass, and both PDFs are given to the author to review the table layout.
