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

* [x] Both editions pass the four Behaviour checks, and chapters 8 and 10 give the same invocations and host grouping.
* [x] Each chapter keeps its opening value and evidenced team gain, with no filler or useful content cut; every number and artifact retains a checked source.
* [x] Source notes and headings stay in edition parity; no private case is added, so OD-3 approval is inapplicable.
* [x] `make verify` and `make book` pass, and both PDFs are given to the author to review the table layout.

**Build.** Chapter 8, both editions: the Antigravity cell says it reads `AGENTS.md` directly and that `.agents/rules/focus-kit.md` is an always-on pointer, with a sentence after the table; a last row for Jules, Junie, Warp, Kiro, Roo Code and Cline, asking in words for `.agents/skills/propose/SKILL.md`, and the sentence under the table names SETUP.md §1 as its origin, promising no skills folder or slash command; a sentence after the commands paragraph says `/brainstorm` and `/analyze` take no slug and `/propose lend-book` or `/apply lend-book` take one, or answer the host's question; Claude Code's `disable-model-invocation: true` is attributed to Claude Code alone, other hosts invoked explicitly with no claim of equal enforcement; the key point names the grouped row and the no-slug commands. Chapter 10, both editions: the same grouped row in its table, the slug rule and one sentence that in Claude Code a command runs only when named.

**Proof.** SETUP.md 2026.10.18.1 §1 table, the invocation-policy paragraph and §§3.1 to 3.4 (`disable-model-invocation: true`, `argument-hint` only on propose and apply) and §3.10; <https://code.claude.com/docs/en/skills> checked on 2026-10-18 ("Add `disable-model-invocation: true` to prevent Claude from triggering it automatically"), so the skills note's access date moved to 2026-10-18 in both editions. No vendor claim beyond the source; no Antigravity vendor note added.

**Review.** One read-only Opus agent over `git diff HEAD` of the four chapter files, against this page and docs/04. Points: (1) chapter 10's slug sentence omitted naming the delivery in the message where neither a typed slug nor a host question works, as chapter 8 says for Cursor and Devin Desktop: fixed in both editions. (2) "The last row is §1" misstated the relation: now "comes from §1", both editions. (3) Optional Antigravity source note: declined, since the vendor page was not checked in this delivery and the Contract allows no vendor claim without checking it; the facts come from SETUP.md, named in prose. `make verify` green after the fixes.

**Decisions.** The concrete `propose` skill file in the grouped row rather than `<name>`, matching the other rows' `/propose` example. `make book` and the PDFs are run once by the batch driver, which gives both PDF paths to the author.
