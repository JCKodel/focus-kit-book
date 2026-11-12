# ch11-14-after

Built before the author read it: the author asked for the whole queue to be run, each page decided alone and built in the same session (docs/05 §4, a command that says to decide alone and to build as well). Every choice the documents leave open is marked "decided by the agent, the author corrects it in the review".

**Objective.** After chapters 11 to 14 the reader, developer or not, writes a queue line with no token, knows that `· after` is read per command (`/propose` once every line it names is `[>]` or beyond, `/apply` once every one is integrated, `[x]` on trunk, merged with a branch or a worktree per delivery) and that the review line is written `· after all`, knows that `/apply` checks its page's files against the builds in flight and not yet integrated before its first edit, reads the queue tree with its states, its two free lists and its `next:`, and knows that, off trunk, each slug's line is read from its branch on origin after `git fetch`.

**Behaviour.** What the reader can do or explain after the four chapters:

* Write a line as the mark, the slug, one sentence and its suffixes; no two letters follow the slug.
* In chapter 11's milestone (`lend-book` `[>]`, `return-book · after lend-book` `[ ]`), say that `/propose return-book` may start now, since `lend-book`'s page is complete, and that `/apply return-book` waits until `lend-book` is integrated.
* Say that a milestone's review line ends `· after all`, every line above it in its milestone but the cancelled ones: its `/propose` starts when they are all defined, its `/apply` when they are all integrated.
* In chapter 14's nine-line milestone (`lend-book` `[*]`), say that `return-book` and `my-loans` are free for `/propose` and not for `/apply`; that `search-catalog` is free for `/apply`; that `m1-review` waits; that the next delivery is `/propose return-book`, the first free line down the queue, whichever command it takes; and that the tree lists `free for /propose, in order: return-book my-loans`, offered as one command.
* Failure: asked "`return-book` is `[>]`, `lend-book` is `[*]`; may I build `return-book`?", answer no: its `after` names a line not integrated, and `/apply` says what it waits on and leaves the mark as it is.
* Failure: with `lend-book` `[*]` and `renew-loan` `[>]`, both changing `src/features/loans/`, say that `/apply renew-loan` stops before its first edit, naming `lend-book` and the folder, leaving the mark as it is, though the queue lists it free for `/apply`; `/apply search-catalog renew-loan` builds `search-catalog` and reports `renew-loan`.
* Edge: off trunk, a `[x]` on a delivery's branch not yet merged is built, awaiting integration, and frees no build; `return-book`'s `after` is read from `lend-book`'s branch on origin after `git fetch`.
* Read chapter 14's six-line tree: `lend-book` in flight, `return-book` under it `waits: after lend-book`, `search-catalog` `apply now`, `m1-review` under `search-catalog` with `+ after lend-book, return-book` and `propose now`; then `free for /apply, in order: search-catalog`, `free for /propose, in order: m1-review`, `next: /apply search-catalog`.
* Name the states a row can show: in flight by the command its mark names, `propose now`, `apply now`, `waits:` with what it waits on, `blocked:` with its reason and the command that resumes it.
* In chapter 13's `lend-book` ending (`lend-book` `[x]`), say that the tree ends `next: /propose return-book` and that `m1-review` waits until `return-book` is defined.
* In the Portuguese edition, the same with its slugs, the script's words in English as it prints them.

**Contract.** Eight files: `book/en/` and `book/pt/` `11-queue-and-milestones.md`, `12-propose.md`, `13-apply.md`, `14-queue-states.md`. Line numbers are en at HEAD `3370f69`; pt follows en sentence for sentence, with docs/03's Portuguese terms and the pt slugs. The text is the agent's within these changes; every block exact as given.

* **ch14**
  * C1, opening (:3-4): "read the two letters a line may carry that say it" becomes saying why `/apply` stops on a line whose files another build is changing; "`· after`" read for each command.
  * C2 (:32): `/apply` builds once every line its `after` names is integrated; no token.
  * C3, the nine-line block (:46): `[ ] m1-review       the milestone against its paragraph · after all` (pt `[ ] m1-review         o marco contra o parágrafo dele · after all`).
  * C4 (:61-62, :232, key point :248): each slug's line read from its branch on origin after `git fetch`, the branch's copy current until the merge and the main branch's after it, with the lines only a branch has; "local or remote" and "latest state" go.
  * C5, "The next line, and which run together" (:69-118): a line free for a command when not `[x]` nor `[?]` and its `after` lets that command start; `after` read per command, with the reason (pages, code); integrated defined; `· after all` with its one clause on cancelled lines; the nine lines read so (Behaviour); the next delivery `/propose return-book`; off trunk, `return-book`'s build waits for `lend-book`'s merge; `/apply my-loans` once `[>]` waits on `lend-book`; the token paragraphs, the four-line token block and `renewal-notice` go; the file check before `/apply`'s first edit, on four lines written for the chapter (`members` `[x]`, `lend-book` `[*]`, `search-catalog` `[>]`, `renew-loan` `[>]`), with several slugs; :80's re-judging of tokens goes.
  * C6 (:168): a `[?]` leaves when the last line its `after` names is integrated, on trunk when `/apply` marks it `[x]`.
  * C7, "What may run now" (:124-147): the states named; the free lists "in order" and `next:`; the six-line milestone written for the chapter, earlier that week, before `reservations`, `my-loans` and `due-reminder` were added, and its tree, both below; `free for /propose, in order: return-book my-loans` quoted for the nine lines.
  * C8, team gain (:240) and key points (:245-246): no token; per command, integration, the file check, the tree's ending.
* **ch13**
  * C9 (:20): several slugs build at once where `after` lets them and their files do not overlap.
  * C10 (:37, :39, :44-45): `after` lines integrated before it starts, integration off trunk; each slug's line from its branch on origin after `git fetch`; the file check before the `[*]` edit, an overlap a conflict: it stops, names the line and the files, leaves the mark; no token.
  * C11, next steps item 4 (:169): the tree ends `next: /propose return-book`; `m1-review`, `· after all`, waits until `return-book` is defined; no token.
  * C12, key point (:286): `after` integrated and files free.
* **ch12**
  * C13 (:28-29): `/propose` starts when every line its `after` names is `[>]` or beyond; read off trunk from each slug's branch on origin after `git fetch`; no token, no "local or remote".
  * C14 (:34): the token sentence goes.
  * C15 (:155): subagents opened at once where `after` lets their lines start.
  * C16, key points (:194-195): no token.
* **ch11**
  * C17 (:16-19): the line without the token; the format block `[ ] <slug>  <what it delivers, one sentence> · after <slug>`.
  * C18, the milestone blocks (:54, :117): review lines end `· after all`, en `the milestone against its paragraph`, pt `o marco contra o parágrafo dele`.
  * C19 (:88-89): `after` read per command, on `return-book` with `lend-book` `[>]`: `/propose return-book` may start now, `/apply return-book` once `lend-book` is integrated, `[x]` on trunk.
  * C20 (:94): the review line `<milestone>-review · after all`, waiting for the lines above it.
  * C21 (:180, key point :192): no token.

Chapter 14's six-line queue, en:

```
[x] catalog         the librarian registers books and their copies
[x] members         the librarian registers and suspends members
[*] lend-book       the librarian lends a copy, or a rule refuses
[>] return-book     records a return · after lend-book
[>] search-catalog  a member searches the catalog
[ ] m1-review       the milestone against its paragraph · after all
```

Its tree, the installed `queue.sh trunk` run in a scratch repository outside this one under ch11's milestone heading (output when this page was written; /apply reruns it on the final blocks, both editions, and copies it verbatim):

```
milestone: Milestone 1: a librarian lends and takes back
[*] lend-book · in flight: apply
 └[>] return-book · waits: after lend-book
[>] search-catalog · apply now
 └[ ] m1-review + after lend-book, return-book · propose now

free for /apply, in order: search-catalog
free for /propose, in order: m1-review
next: /apply search-catalog
```

pt, the same queue with `catalogo`, `membros`, `emprestar-livro`, `devolver-livro`, `buscar-catalogo`, `m1-review`, prints `└[ ] m1-review + after emprestar-livro, devolver-livro · propose now`, 69 columns, and `next: /apply buscar-catalogo`.

Terms of docs/03: dependency, free line, queue tree, claim, kanban board; none new, no row changed (they already say what the chapters will). Sources: no new note; docs/05 §4 :98-176, docs/03's rows, the installed `queue.sh`. Cases: none. No number.

**States.** Inapplicable: chapters, no screen.

**Visual reference.** Inapplicable: no new kind of content (the tree's `└` was proved by `ch11-14-queue-tree`).

**Out of scope.**

* `mark.sh` and its refusal (M34, M35); `after all` leaving out a cancelled line taught with its case (`ch14-15-after-all-dropped`): C5 gives it one clause only.
* `/apply` naming each next step and running `queue.sh` unasked (`ch13-apply-next`); findings, `· from`, `findings:` (M38): no example line carries `· from`.
* Chapter 19's tree with `together:` and `(P-)`, the claim's `taken` and `resume`: `ch19-claim-integration`. Chapters 8, 9, 17 and 20: their M33 lines.
* The changelog's story and numbers of 2026-10-25: the book teaches the kit as it is (docs/04).

**Done when.**

* [x] C1 to C21 read as the Contract says in both editions; no `(PA)`, `(P-)`, `(-A)`, `(--)`, "token" or "local or remote" left in the eight files.
* [x] The tree blocks are the installed script's output on the final queue blocks, both editions, copied verbatim.
* [x] Both editions written; each chapter opens with its value; no filler and nothing useful cut; no number added; no private case; no em dash; no run narration.
* [x] Every block keeps to 74 columns.
* [x] `make verify` green after the last edit.
* [x] `make book` builds both editions, both PDF paths recorded.
* [x] Delivery review by one read-only Opus agent, as docs/05 §5 says; only this delivery's paths and its docs/06 line staged; the page in `work/done/` and its commit message suggested.

**Decisions.**

* Decided by the agent, the author corrects it in the review: the tree is drawn on a six-line milestone, earlier that week, because the nine-line milestone's review row prints 141 columns in en and more in pt, past docs/04's 74, and the real output cannot be cut; the nine lines keep the marks and the board.
* Decided by the agent, the author corrects it in the review: the review lines in the library's blocks end `· after all` (docs/05 §8 writes it so) and their description is shortened to fit 74 columns.
* Decided by the agent, the author corrects it in the review: `after all` gets one clause on cancelled lines in chapter 14, so the chapter is true of the kit as it is, and its worked case stays `ch14-15-after-all-dropped`'s.
* From the documents: per command, integration, the file check, the copy rule (docs/05 §4 :103-115, :145-149, :168-176); the tree's words (the installed `queue.sh`).

## Outcome

**Divergences.** C7's six-line milestone is not "earlier that week, before `reservations`, `my-loans` and `due-reminder` were added", as the Contract says: in it `return-book` is `[>]`, and in the nine lines it is `[ ]`, and a mark never goes back. The text calls it milestone 1 in six lines, written for the chapter like the four-line block, with `return-book` already defined (en ch14 :121, pt :123); decided by the agent, the author corrects it in the review. The Delivery review's fixes went beyond the Contract's line list where this delivery's per-command reading made an unchanged sentence false: ch14 :64 (a mark seen once pushed to origin and fetched), ch14 :199 (`reprint-card`'s build), ch13 :117 (lines already integrated), ch11 :4 (the line "it needs first"); all in both editions.

**Proof.** The installed `queue.sh trunk`, run in scratch repositories outside this one under ch11's milestone heading, on the final blocks: the six-line tree, en and pt, byte-equal to the chapter; on the nine lines `free for /propose, in order: return-book my-loans` (pt `devolver-livro meus-emprestimos`) and `next: /propose return-book`; on ch11's milestone as written, `return-book · propose now` under `lend-book`; with `lend-book` `[x]`, `next: /propose return-book` and `m1-review · waits: return-book not defined` (pt the same with its slugs). `make verify` green, 15 seconds, after the last edit. `make book` at HEAD `3370f69` with this delivery uncommitted: `output/one-page-at-a-time.pdf`, `output/uma-pagina-de-cada-vez.pdf` (and the two EPUBs).

**Delivery review.** One read-only agent on Opus read this page, the diff of the eight chapters, this line's hunk of docs/06, docs/05 :90-180, the installed `queue.sh` and docs/04's rules, reproduced every tree in a scratch folder (all equal) and ran the width, parity, em dash and prose checks (green); it did not read docs/03's rows. Its report says it had the advisor and called it once. Fixed: "a state is one of five" (off trunk the script prints two more states), now "on trunk, a state is one of these"; ch13's step 4 "now that `lend-book` is `[x]`", which taught the old rule; ch14 :64's reading by local or remote branch; ch14 :77's "so", which did not follow; three pt wordings (ch13 :44's double "com", ch14's "num", ch14 :71's "dela"); and the four sentences under Divergences.

**Decisions** are those above the heading, each written as the agent's.

## For the review

* book/en/14-queue-states.md:46, pt :47: on the nine-line milestone the review's tree row prints 141 columns (en), past docs/04's 74, so a realistic milestone's tree cannot be shown whole; the chapter draws it on six lines.
* book/en/12-propose.md and pt, Key points: six bullets against docs/04's five, older than this delivery.
* book/en/12-propose.md:30, book/en/13-apply.md:29, and pt: the claim described as reusing or creating a branch; `claim.sh` is create-only and opens another clone's branch only with `resume`; `ch19-claim-integration` covers chapter 19 only.
* book/en/15-closing-a-milestone.md:123, pt :126: `[x] m1-review` without `· after all`, which chapters 11 and 14 now write.
* book/en/19-worktrees.md:205-215, pt: the tree still prints `together:` and `(P-)`, which the installed script no longer does.

```commit
docs(ch11-14-after): teach after per command and the file check

- Remove the parallel token from chapters 11 to 14
- Read after per command; integration frees a build; after all
- /apply checks its files against other builds before editing
- Tree with its states, free lists in order and next:
- Read each slug's line from its branch on origin after git fetch

work/done/ch11-14-after.md
```
