# ch21-container

**Objective.** After chapter 21 a reader who chooses a worktree per delivery lays it out as focus-kit 2026.10.15 shapes it: a container folder whose `main/` is the checkout, the bare repository in its hidden folder, each delivery's worktree in `<hidden>/worktrees/<slug>/` on the branch `<prefix>/<slug>`, `.face/` and `face/` when docs/05's Git slot names neither, and knows why one shape for every tool and person.

**Behaviour.**

* A reader setting up the lending library for a worktree per delivery runs, once, from an empty folder `library/`: `git clone --bare <url> .face/repo.git`, the fetch line in `.face/repo.git`, then `git worktree add ../../main main` from inside it; `git worktree list` then shows `library/.face/repo.git (bare)` and `library/main [main]`.
* Asked where the history lives, the reader answers: in the bare repository, `.face/repo.git/`; `main/` is a worktree like the others, its `.git` a file that points there.
* Failure: a reader who skips the fetch line finds that `git fetch` in `main/` brings no `origin/main`, and knows why from the chapter (a bare clone creates no remote-tracking branches, git-clone `--bare`).
* From `main/`, `git worktree add ../.face/worktrees/return-book -b face/return-book main` creates the delivery's folder inside the container, hidden from `main/`'s files; the reader works there, merges from `main/` with `git merge --no-ff face/return-book`, then `git worktree remove ../.face/worktrees/return-book` and `git branch -d face/return-book`.
* Edge: a reader who runs `git worktree add` from another folder knows the path is relative to where they stand, so they run the cycle from `main/` as the chapter does.
* A reader whose docs/05 Git slot says "a worktree per delivery" and names no hidden folder and no prefix expects `/propose return-book` to create or reuse `.face/worktrees/return-book/` on `face/return-book`, from the main branch's HEAD, and write the page there; a slot that names `.wt/` and `wt/` gives `.wt/worktrees/return-book/` on `wt/return-book`.
* Failure: a reader who already has a branch `return-book`, without the prefix, knows `/propose` does not take it as the delivery's: it is someone else's.
* A reader asked why one shape answers with the kit's changelog, entry 2026.10.15: a `/propose` running in the background entered a worktree its host had made on its own, in the host's folder, and the person copied the page to the main branch by hand, because nothing said where a delivery's worktree belongs.
* A reader of the conflict example sees the incoming branch as `face/overdue-list` in the marker line.
* Edge: chapter 11 already says 2026.10.15 brought no migration; chapter 21 teaches the shape as it is now, with no "before" layout and no number for it.

**Contract.**

* **Chapter 21, both editions, file name and title kept**, headings kept, no new section.
  1. Opening, second sentence: the reader can also lay out a worktree per delivery as the kit shapes it, a container folder with `main/` and a hidden folder.
  2. "What a worktree is": the paragraph "The folder you cloned is the main worktree. It holds the `.git` folder" keeps that as the common case and adds the bare repository: a repository with no files of its own, only the history (git-clone `--bare`), so that every working folder, `main/` included, is a worktree of it. The rest stays.
  3. "How it solves the problem": the two bullets use `library/.face/worktrees/return-book` on `face/return-book` and `.../overdue-list` on `face/overdue-list` (pt `biblioteca/.face/worktrees/devolver-livro`, `face/devolver-livro`, `lista-de-atrasos`); "from the main folder" becomes "from `main/`".
  4. "The life of a worktree": first, once per clone, the container: the three setup commands above, each explained, with the fetch line `git config remote.origin.fetch '+refs/heads/*:refs/remotes/origin/*'` and why, quoting git-clone `--bare`; a project that chooses this writes those steps in a manual of `docs/manuals/` (chapter 10). Then the six steps, run from `main/`, with the paths and branches of the Behaviour; the sentence on installing dependencies in each worktree stays.
  5. "Worktrees in the kit": the Git slot may name the hidden folder and the prefix, and one that names neither means `.face/` and `face/`; `/propose <slug>` creates the worktree at `<hidden>/worktrees/<slug>/` on `<prefix>/<slug>`, from the main branch's HEAD, or reuses the one that exists, and writes the page there; a branch `<slug>` without the prefix is not the delivery's; the person makes the container once, the kit makes each worktree; "one in the main folder for each `/propose`" becomes "one in `main/`". The changelog story, paraphrased, as why one shape.
  6. "When the branches meet": `>>>>>>> overdue-list` becomes `>>>>>>> face/overdue-list` (pt `face/lista-de-atrasos`).
  7. "What the team gains": one sentence, the error the shape removes (the background `/propose` and the page copied by hand), from the changelog, no number; the run's numbers stay as they are.
  8. Key points: the worktree point names the container, `main/`, `<hidden>/worktrees/<slug>/` and `<prefix>/<slug>`, `.face/` and `face/` by default.
* **docs/03, new rows** (docs/03 says a new concept enters there first): `container folder` | `pasta contêiner` | `.face/`, `face/` | The folder of a project with a worktree per delivery whose `main/` is the checkout; it keeps the bare repository in a hidden folder (`<hidden>/repo.git/`) and each delivery's worktree in `<hidden>/worktrees/<slug>/`, on the branch `<prefix>/<slug>`; docs/05's Git slot may name the hidden folder and the prefix, and one that names neither means `.face/` and `face/`. `bare repository` | `repositório bare` | `git clone --bare` | A repository with the history and no working files of its own; in a container folder every working folder is a worktree of it. Portuguese terms from the kit's CHANGELOG.pt.md, entry 2026.10.15.
* **docs/03, `worktree` row:** "it shares the history with the main folder" becomes "it shares the history with every other worktree of the repository".
* **Sources:** the kit's CHANGELOG, entry 2026.10.15, paraphrased with no note (docs/04; the `ch21-one-tree` precedent for 2026.10.08.3). New note `[^git-clone]`: Git, "git-clone", the documentation, option `--bare`, accessed on the day written; quoted: "When this option is used, neither remote-tracking branches nor the related configuration variables are created." Existing notes kept.
* **Cases:** none. **Code examples:** the commands, the slugs and the paths are written for the chapter on the lending library, and said so; no transcript of a run (ADR-0017).
* **Git:** trunk, no branch (docs/05 §5). docs/06 also holds `ch13-short-lines`'s blocked hunk: /apply stages only this line's hunk.

**Out of scope.**

* Chapters 10 and 20: "a second working folder on its own branch" and "its own folder" stay true in a container.
* Chapter 11: it already says 2026.10.15 brought no migration.
* docs/05's Git slot and this repository's layout: trunk is the project's choice (`kit-2026-10-16`).
* A manual in this repository: the book does not use the container; the chapter tells the reader's project to write one.
* Turning an existing clone with uncommitted work into a container: the chapter starts from the remote; moving work in progress is a git lesson of its own.
* A new run or number (ADR-0017; memory: the book teaches the kit as it is now).

**Done when.**

* [x] Chapter 21 changed in both editions, same headings; opens with its value; no filler and nothing useful cut.
* [x] Every command of the chapter run again on a scratch repository in /apply, git version recorded; the git-clone quote checked word for word.
* [x] No `../library-`, `../biblioteca-`, `../<project>-<slug>` or unprefixed worktree branch left in the book (`grep`).
* [x] Changelog entry 2026.10.15 paraphrased and checked against the kit's CHANGELOG and CHANGELOG.pt.
* [x] docs/03 reads as the Contract says.
* [x] `make verify` green; `make book` builds and both PDF paths are given to the author.
* [x] Page in `work/done/`, the line `[x]`, staged by its paths and its hunk of docs/06, the commit suggested in a `commit` block.

**Decisions taken from the documents.**

* The shape, the defaults and `/propose`'s part: the kit's SETUP.md at `029cee6`, the a-worktree-per-delivery paragraph and the Git slot template; CHANGELOG entry 2026.10.15.
* The fetch line: checked during /propose on a scratch repository (git 2.56.0): without it `git fetch` in `main/` creates no `origin/main`; with it, it does. The full cycle (setup, add, commit, merge `--no-ff`, remove, branch `-d`) ran there.
* Running `git worktree add` with `-C .face/repo.git` and a path `./worktrees/<slug>` put the worktree inside `repo.git/worktrees/`, git's own admin folder: the chapter runs the cycle from `main/` with `../.face/worktrees/<slug>`.
* Changelog paraphrased with no note, git's documentation with one: docs/04, as `ch21-one-tree` did.
* `pasta contêiner`, `repositório bare`, `pasta oculta`, `prefixo`: the kit's CHANGELOG.pt.md.
* Teaching the one-time container setup in a few lines, with the fetch line and the manual: asked; the author chose it.

## What happened

**Proof.** Every command of the chapter ran again on a scratch repository with git 2.56.0, from a bare `origin.git`: without the fetch line, `git fetch` in `main/` left `git branch -r` empty; with it, `origin/main` appeared. `git worktree list` printed `.../library/.face/repo.git (bare)` and `.../library/main 0b166f7 [main]`, and `main/.git` is a file whose `gitdir:` points into `.face/repo.git/worktrees/main`. From `main/`, `git worktree add ../.face/worktrees/return-book -b face/return-book main` and the same for `overdue-list`; `git status` in `main/` showed nothing of them. Each branch marked its own queue line and committed; `git merge --no-ff face/return-book` went in, `face/overdue-list` conflicted with the marker line `>>>>>>> face/overdue-list`; `git merge --abort`, `git worktree remove`, `git branch -d face/return-book` all worked. The git-clone quote matches the online documentation and the 2.56.0 man page word for word. The changelog paraphrase was checked against CHANGELOG.md and CHANGELOG.pt.md, entry 2026.10.15, at the kit's `029cee6`. `grep` over `book/` finds no `../library-`, `../biblioteca-`, `<project>-<slug>`, `-b return-book` or unprefixed worktree branch. `make verify` green; `make book` built both editions.

**Decisions.**

* The first worktree command is split with `\` in both editions: the Portuguese one is 78 columns on one line, past docs/04's 74; English follows so the editions stay parallel.
* "What a worktree is": besides the contract's sentences, "points back to the main one" became "points back to where the history lives", since in a container no worktree is the main one; and "That is the common case." keeps the `.git` folder as the usual layout.
* "How it solves the problem" names `library/` and its `main/` in one clause with a pointer to the next section, since the bullets use paths the reader meets there.
* `origin/main` is explained in a clause (the remote-tracking branch, git's local record of where the remote's branch is): chapter 20 does not teach it, and the fetch line means nothing without it.
* `git worktree list` is described in prose ("one ending in ..."), not shown as output, since its real output prints absolute paths.
* The Portuguese edition writes the placeholders `<oculta>` and `<prefixo>`, the kit's CHANGELOG.pt.md words, and keeps "worktree" and "branch" masculine as docs/03 and the rest of the book do (the kit's Portuguese uses the feminine).

**Divergences.** None from the Contract. **Omissions.** None.

```commit
docs(ch21-container): teach a worktree per delivery in a container

- chapter 21, both editions: main/, .face/repo.git and the fetch line
- worktrees in .face/worktrees/<slug>/ on face/<slug>, slot defaults
- the 2026.10.15 changelog story as the reason for one shape
- docs/03: container folder, bare repository; worktree row reworded
- note [^git-clone], option --bare, quoted

work/done/ch21-container.md
```
