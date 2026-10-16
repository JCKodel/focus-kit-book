# ch21-worktree-first

**Objective.** A reader of chapter 21 knows what a worktree is the first time the chapter names one, in both editions, and every later use of the word rests on a definition already given.

**Decided with the author.**
1. Gloss and reorder (the author's answer in this /propose): the opening defines the word where it first appears, and §What a worktree is moves before §When a worktree still pays.

**Decided from the documents.**
2. The gloss is docs/03's definition shortened, "a second working folder of the same repository, on its own branch" ("uma segunda pasta de trabalho do mesmo repositório, no seu próprio branch"); the opening stays at most three sentences (docs/04, `<opening>`).
3. The Portuguese gloss "(uma árvore de trabalho)", now at the end of §When a worktree still pays, moves with the first use, into the opening (docs/04 line 35: a tool is introduced in a few words the first time it is named).
4. §When a worktree still pays keeps its argument, branches alone and a second clone against a worktree, and loses only its reveal, "That is a worktree.", which becomes a sentence that names what the worktree, already defined, gives; nothing else in the chapter is cut or added (ADR-0015).
5. No pointer in the book or in docs/ links to an anchor of chapter 21, so moving the section breaks no link (checked with `grep "21-worktrees.md#"`).
6. Found from the review: the author's C2 in `m13-review` ("o capítulo explica o que é um worktree depois de mencionar ele no começo do capítulo").

**Behaviour.**

* A reader opens chapter 21 in English: the first sentence that says "worktree" also says what one is, a second working folder of the same repository on its own branch. The same in Portuguese, with "(uma árvore de trabalho)" there.
* Reading in order, the reader meets §What is and is not a conflict there (its "give one of them a worktree"), then §What a worktree is, then §When a worktree still pays, then §How it solves the problem; the sections between keep their order.
* §What a worktree is keeps all its content: the main worktree, the bare repository, `git worktree add`, shared history with separate files, `HEAD` and staging area, one branch per worktree, and its two quotes with their notes.
* §When a worktree still pays still says the two cases it pays in and why branches alone and a second clone fall short, and it no longer ends by revealing the word as if new.
* Searched for "worktree" in each edition, the first match in the chapter's body is the sentence that defines it; a first match without the definition fails the delivery.
* The reader who goes to the Key points and §Worktrees in the kit finds them unchanged.
* If, when /apply starts, `plain-numbers` is being built and is changing `book/*/21-worktrees.md`, /apply stops and reports (docs/05 §4: a file this page needs that the other delivery is changing).

**Contract.**

* Files: `book/en/21-worktrees.md`, `book/pt/21-worktrees.md`.
* Sections, in order after the change: opening; §The problem: one folder, two jobs; §Two sessions in one folder; §What is and is not a conflict there; §What a worktree is; §When a worktree still pays; §How it solves the problem; the rest as they are.
* Terms of docs/03: worktree, bare repository (already there; no new term). Sources: `[^git-worktree]`, `[^git-clone]`, unchanged; their notes keep their keys. Cases: none. Exercises: none (ADR-0017).
* docs/03, docs/04, docs/05: no change. docs/06: this line `[>]` now, `[*]` when /apply starts, `[x]` by /apply.

**Out of scope.**

* Other wording of chapter 21: the C2 finding is about order, not prose.
* Numbers in chapter 21 (§What the team gains): `plain-numbers`.
* Other chapters that say "worktree" (10, 20): the finding named chapter 21, and chapter 20 ends where 21 begins.

**Done when.**

* [x] Both editions written, same section order, the word defined at its first use.
* [x] Opens with its value, at most three sentences; no filler and nothing useful cut.
* [x] Every number sourced (none added).
* [x] `make verify` green, disclosure scan included.
* [x] `make book` run; both PDF paths given to the author.
* [x] Page in `work/done/`, the line `[x]`, staged, commit message suggested in a `commit` block.

## What happened

* Checked at start: `plain-numbers` was `[~]`, being defined, with no page in `work/` and no change to `book/*/21-worktrees.md`, so no conflict (docs/05 §4). Its `[~]` mark shares a hunk of docs/06 with this line; it is that session's work, left unstaged.
* Opening: the second sentence now reads "when it still pays to give each delivery a worktree, a second working folder of the same repository on its own branch" (pt: "quando ainda compensa dar a cada entrega um worktree (uma árvore de trabalho), uma segunda pasta de trabalho do mesmo repositório no seu próprio branch"); still two sentences.
* §What a worktree is moved, unchanged, before §When a worktree still pays.
* The reveal, two sentences, became one: "A worktree per delivery gives exactly that: several folders, each on its own branch, sharing one history." (pt: "Um worktree por entrega dá exatamente isso: ..."); the Portuguese gloss left it for the opening.
* Proof: `grep -n -i worktree` on each edition, the first match after the title is line 4, the sentence with the definition; headings 56, 74, 89, 102 in the order of the Contract in both editions. `make verify` green; `make book` built `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.
* Divergences: none. No document changed, as the Contract said.

```commit
docs(ch21-worktree-first): define worktree at its first use in ch 21

- opening glosses worktree where the chapter first names it; both editions
- What a worktree is now comes before When a worktree still pays
- the section's reveal becomes what a worktree per delivery gives

work/done/ch21-worktree-first.md
```
