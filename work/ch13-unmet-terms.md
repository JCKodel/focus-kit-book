# ch13-unmet-terms

**Objective.** A reader of chapter 13 sees what job "spec delta" and "specialized subagent" would do, because each is said in a few words where it appears, so the list of what the process does not have can show that nothing is missing.

**Behaviour.**

* In §"What the process does not have", the "Spec delta" item first says what one is: in OpenSpec, the file of a change that lists only the requirements it adds, changes or removes, merged into the specs when the change is archived; then, as today, what does that job in focus-kit.
* The item can point to chapter 3's run, whose OpenSpec change wrote two such files, each titled "Spec Delta".
* The "Specialized subagent" item first says what one is: an agent that another agent launches for one narrow role, with its own instructions, such as a planner or a reviewer; then, as today, what does that job.
* Both editions say the same; the Portuguese keeps "Delta de spec" and "Subagente especializado".
* Finding F19 of the M3 review is settled.

**Contract.**

* Files: `book/en/13-the-governor.md` and `book/pt/13-the-governor.md`, lines 49 and 53 today.
* Sources: for the spec delta, the run already cited as `[^spec-driven-run]` in chapter 3 (the files are `work/done/spec-driven-run/openspec/feature/openspec/changes/add-client-cancellation/specs/*/spec.md`); /apply checks OpenSpec's own documentation for "merged when archived" and cites it only if the reader gains a page to open. For subagents, a host's documentation of them (Claude Code's subagents page), cited once, if /apply finds a stable URL; otherwise the gloss stands without a note.
* Terms of docs/03: none new; both stay outside the glossary, since the process does not have them.
* Cases, exercises: unchanged.

**Out of scope.**

* Explaining the other five items: the review found them met in earlier chapters.
* The two paragraphs after the list (the gate and the second agent): `headless-runs` covers the second agent.

**Done when.**

* [ ] Both items explained in both editions, same meaning.
* [ ] Every new source note gives the reader something to open (docs/04).
* [ ] `make verify` green, the link check included.
* [ ] `make book` run, and both PDF paths given to the author.
* [ ] Page in `work/done/`, `[x]` in docs/06, staged, commit message suggested.
