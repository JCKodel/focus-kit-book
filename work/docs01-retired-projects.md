# docs01-retired-projects

**Objective.** After this delivery docs/01 and `AGENTS.md` present no guided project, brownfield project or chapter tag as live, give the "no playground server" rule the reason that is true today, and docs/01's tree names every path `.gitignore` ignores.

**Behaviour.** What a reader of the two documents finds.

* docs/01 "How the repository is organized" no longer holds the two sentences saying the guided project's code lives in `JCKodel/focus-kit-clinic` and the brownfield project's in the fork `JCKodel/clahub`, quoted at chapter tags. The sentence on chapter file names stays.
* docs/01 "Tried and removed on purpose" gains the retired projects in one line: a guided project and a brownfield project, each in its own repository with a tag per chapter (ADR-0008, ADR-0009, retired by ADR-0017; the repositories and tags stay, cited by no chapter, docs/05 §5).
* The "no playground server" lines say why today: the code examples are short TypeScript written for the chapter and shown in it (ADR-0017), so there is nothing for a shortener or a playground to open. docs/01: "A link shortener or playground server for code snippets: the examples are short, written for the chapter and shown in it (ADR-0017)." `AGENTS.md`: "A link shortener or playground server for snippets: the examples are short and live in the chapter (ADR-0017)."
* docs/01's tree gains the two ignored paths it left out, `context/` ("not created; listed in `.gitignore` so private notes never enter, docs/05 §5") and `.DS_Store` ("macOS folder metadata, in any folder; ignored"), each in the tree's column format, next to `.venv/`, `site/`, `output/` and `__pycache__/`.
* Failure: every line of `.gitignore` (`.venv/`, `site/`, `output/`, `context/`, `__pycache__/`, `**/.DS_Store`) has a line in the tree; a reader finds no word "guided", "brownfield", "clahub", "clinic" or "chapter tag" in docs/01 outside "Tried and removed on purpose", and none in `AGENTS.md` outside "Do not rebuild".
* Edge: `AGENTS.md` line 29 ("A guided project, a brownfield project, chapter tags or exercises (ADR-0017)") already says retired in "Do not rebuild" and stays.

**Contract.** Text only. docs/01: lines 72 and 73 deleted; the bullet at line 102 reworded as above; one bullet added under "Tried and removed on purpose"; two tree lines added. `AGENTS.md`: the bullet at line 28 reworded as above. Re-checked at the start: all of these lines hold the stale text (D2) and `.gitignore` lists `context/` and `**/.DS_Store`, absent from the tree (D8); nothing else in docs/01 or `AGENTS.md` names the retired projects.

**Out of scope.**

* docs/03's `tag` row naming the book's chapter tags as live (D6): `docs03-current-rows`.
* docs/04's "Teach, do not report", which still says "a run of the guided project or a case is evidence": noticed here, not in the M14 review; a line for the author to add (it is docs/04's own `docs04-gain-number` file, but not that line's finding).
* docs/05 §5, which already retires the projects, and its history paragraph on M3 and M4: unchanged.
* The tree's other omissions that `.gitignore` does not list (`AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, the hosts' hidden folders): not a finding of the review.
* The repositories `focus-kit-clinic` and `clahub` and their tags: stay (docs/05 §5).

**Done when.**

* [ ] The five changes above made, no other line of docs/01 or `AGENTS.md` changed; each ignored path of `.gitignore` found in the tree, checked line by line.
* [ ] `grep -in "guided\|brownfield\|clahub\|clinic\|chapter tag"` over docs/01 and `AGENTS.md` finds only "Tried and removed on purpose" and "Do not rebuild".
* [ ] `make verify` green; page in `work/done/`, the line `[x]`, staged by its paths and its hunks of docs/01, `AGENTS.md` and docs/06, the commit suggested in a `commit` block.

**Decisions taken from the documents.**

* The reason for "no playground server" is ADR-0017's: examples written for the chapter, shown in it; the tags that did the job are retired, docs/05 §5.
* The retired projects move to "Tried and removed on purpose", where docs/01 keeps what the book decided not to rebuild.

**Decisions in the review.**

* The two sentences at lines 72 and 73 are deleted, not rewritten as history: chosen alone, since docs/05 §5 and ADR-0017 already hold the history and docs/01 says how the repository is organized today.
* `.DS_Store` and `context/` get tree lines, as the review's D8 says; the other unlisted files are left out: chosen alone, matching the queue line's "every ignored path".
* Overlap: `venv-failed-install` edits docs/01 too (the `.venv` target row and the tree line `.venv/`), different lines near the tree; stage by hunk and run them one after the other. No page of M15 touches docs/01, `AGENTS.md` or this text (`renumber-chapters` says docs/01 is unchanged). No docs/03 term is needed.
