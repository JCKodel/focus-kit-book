# ch15-first-commit-base

**Objective.** A reader of chapter 15 knows what a first milestone's range, from the project's first commit, leaves out: the first commit's own content, which no diff of the range shows; both editions. Finding R2-2 of `m17-review` (work/done/m17-review.md).

**Decided without the author.** A batch /propose with no question asked; each choice below is the recommended one and names its source.

1. The fault: chapter 15 says "The first commit, the base of a first milestone, makes the review read the whole project." `git diff <first>..HEAD` holds every change made after the first commit and none of what the first commit itself added, as the chapter's own explanation of `<base>..HEAD` says ("every change made after the base"). docs/05 §8's rule, the first commit as a first milestone's base, is right and unchanged.
2. What the first commit holds is said from chapter 10: on a new project, it holds the kit's files and the documents `/brainstorm` wrote (chapter 10, new project step 3 and its key point "The documents are the project's first commit"). The text names it with "on a new project" and a pointer to chapter 10, which is the specific detail it leans on (docs/04, Chapter pointers).
3. The text says how that content is still seen: the readers read their areas with the whole repository open (the chapter's own sentence just before), and the person reviewed the documents before committing them (chapter 10, step 3). No pointer to chapter 9 as well: one pointer per detail is enough, and chapter 10's step itself points to chapter 9.
4. A project documented with `/analyze`, whose first commit is its old code's, is not described: the finding is the new sentence's claim, and the chapter's example is the lending library from its first commit (docs/05 §8: no widening).
5. Files other slugs touch, and the order: `book/en/15-closing-a-milestone.md` and `book/pt/15-closing-a-milestone.md` are edited by `ch15-review-range-order` two lines above (the sentence after "Its page names as the base"), one hunk with this one. In the batch's order that slug applies first: this /apply starts only after its commit, and if its change is still uncommitted in the tree, this /apply follows docs/05 §4 and §6 as they read then (`conflict-same-lines`, applied first, may change them; today: stop and report). In pt, `docs03-checker-pt` (another agent's, applied later) may edit the line between, "A leitura custa"; it follows this commit. Line numbers shift as these land; /apply finds the passage by its text.
6. No new docs/03 term, no queue line, no change to docs/05, no `kit:` note: the kit's text names the first commit as a base and claims nothing about the whole project.

**Behaviour.**

* A reader of chapter 15, §The review is a delivery, can say what `<first>..HEAD` holds for a first milestone: every change after the first commit, not the commit itself.
* The same reader can say what that leaves out on a new project, the kit's files and the documents of the first commit, and where they are still seen: in the repository each reader reads its area against, and in the person's review before that commit.
* Fails: `grep -n "the whole project" book/en/15-closing-a-milestone.md` or `grep -n "projeto inteiro" book/pt/15-closing-a-milestone.md` finds a line.
* Edge: the key point "or the project's first commit for a first milestone" (pt "ou o primeiro commit do projeto para um primeiro marco") stays: it names the base and claims no coverage.

**Contract.** The sentences, as /apply writes them (one sentence per line, docs/04), replacing the line "The first commit, the base of a first milestone, makes the review read the whole project." and its pt line "O primeiro commit, a base de um primeiro marco, faz a revisão ler o projeto inteiro.", in place.

`book/en/15-closing-a-milestone.md`:

```
A first milestone's range, from the project's first commit, holds every change made after that commit and not the commit itself.
What the first commit added, on a new project the kit's files and the documents (chapter 10), is in no diff of the range: the readers see it only as the repository they read their areas against, and the person read the documents before committing them.
```

`book/pt/15-closing-a-milestone.md`:

```
O intervalo de um primeiro marco, a partir do primeiro commit do projeto, guarda toda mudança feita depois desse commit, e não o próprio commit.
O que o primeiro commit acrescentou, num projeto novo os arquivos do kit e os documentos (capítulo 10), não está em nenhum diff do intervalo: os leitores só o veem como o repositório contra o qual leem as suas áreas, e a pessoa leu os documentos antes de fazer o commit deles.
```

Terms: milestone (marco), range (intervalo, as chapter 15 uses it), commit, docs/03; no new term.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Out of scope.**

* A base that holds the first commit's content (an empty tree as base, say): the rule is docs/05 §8's, and the finding is the chapter's claim.
* A project started with `/analyze`: decision 4.
* Line 21's range order: `ch15-review-range-order`.

**Done when.**

* [x] Chapter 15 carries the Contract's text, in both editions.
* [x] The Behaviour's greps find nothing.
* [x] No number, no private case, no em dash, no narrated run in the new text.
* [x] `make verify` green.
* [x] The delivery review run as docs/05 §5 says, on this delivery's hunk of both files and this page.
* [x] `make book`, and the paths of both PDFs given to the author (docs/05 §5, Proof of a screen).
* [x] Page in `work/done/`, line `[x]`, staged by hunk where the files hold other deliveries' changes (decision 5), commit message in a `commit` block.

Queue line, as it stands in docs/06:

```
[~] ch15-first-commit-base   chapter 15 says what a first milestone's range leaves out of the first commit, instead of "the whole project"; both editions
```

**Built.** Chapter 15, §The review is a delivery, both editions: the line "The first commit, the base of a first milestone, makes the review read the whole project." (pt "O primeiro commit, a base de um primeiro marco, faz a revisão ler o projeto inteiro.") is replaced, in place, by the Contract's two sentences. The Behaviour's greps find nothing.

**Decisions at apply time.** The Contract's last clause read "and the person read it before committing it" (pt "e a pessoa o leu antes de fazer o commit dele"), where "it" is the kit's files and the documents; chapter 10, step 3, has the person read only the documents, as decision 3 says. The clause now names the documents, "and the person read the documents before committing them" (pt "e a pessoa leu os documentos antes de fazer o commit deles"), and the Contract above carries the corrected text. `make book` is run once by the batch driver at the end of the parallel run; staging is the driver's, from the paths this delivery reports. No Case A or Case B passage.

**Divergences and omissions.** None.

**Proof.** `make verify` green (build, parity, em dash, prose, width, links, disclosure).

**Delivery review.** One read-only agent on Opus read this delivery's hunk of both chapter files against this page and docs/04. One finding, fixed: the last clause claimed the person read the kit's files too, more than chapter 10 and decision 3 support; both editions and the Contract now name the documents, and verify ran again, green. Everything else held: the Portuguese mirrors the English, one sentence per line, the pointer to chapter 10 leans on a specific detail, the first sentence matches the chapter's reading of `<base>..HEAD`.

```commit
docs(ch15-first-commit-base): say what a first milestone's range leaves out

- Chapter 15: a first milestone's range holds the changes after the first commit, not the commit
- Chapter 15: the first commit's files are seen as the repository, the documents by the person
- Both editions

work/done/ch15-first-commit-base.md
```
