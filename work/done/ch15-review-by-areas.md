# ch15-review-by-areas

**Objective.** After chapter 15 a reader can run a milestone review's code reading as the kit does it in any host that runs agents: on the person's word, over `git diff <base>..HEAD` from the base the review's page names and never a bare commit, split into the areas docs/05's Milestone review slot names with one read-only agent each (one fresh session per area where the host runs no agents), every reader listing the paths it read and the review line waiting as `[?]` when they miss part of the range, and one checker marking each candidate seen, latent or weak before the person sees it; both editions.

**Decided without the author.**

1. *Which passages change.* Chapter 15 only, both editions: the opening's second sentence, §The review is a delivery from the base sentence's second clause to the line on where each delivery's code is read, §Read the whole code once from "The deep review is the host's command" to its end, the review line of the queue example, one sentence of the gain, and key point 3. The base sentence's first clause and the first-commit sentence `ch15-first-commit` wrote stay byte for byte (work/done/ch15-first-commit.md decisions 3 and 6, Delivery review item 4, which handed this line "The agent may say it is time, and never launches it.").
2. *Where the rule comes from.* docs/05 §8 as installed by `kit-2026-10-17`, which is the kit's template verbatim (`SETUP.md` §3 at 2026.10.17), and the Milestone review slot's template, "the areas a milestone's changes split into for the code reading of §8, one reader each, and the model its readers and checker run on, or the session's; or: none" (`.claude/skills/analyze/references/documents.md`). The chapter names them in plain words, docs/05 §8 and the Milestone review slot; no note points to the kit's repository (docs/04 "Source notes").
3. *Section title.* `## Read the whole code once` becomes `## Read the code since the base, by areas` (pt `## Leia o código desde a base, por áreas`): the section now teaches the range and the areas, and no link points to its anchor (`grep "15-closing-a-milestone.md#"` finds nothing). The hand-test blind-spot paragraph that opens it stays.
4. *The slot shown.* A Milestone review slot for the lending library, written for the chapter and said so: its areas from its feature folders as chapter 4 lays them out (`src/features/loans/`, `src/features/members/`, `src/features/catalog/`, and the documents and the rest), and "the session's model". Not this repository's slot (build, chapters, kit skills, documents, a named model and advisor): that is this project's answer, and how a project answers the slot belongs to `ch08-09-review-slot` (ch13-delivery-review decision 3, docs/04 "Context before an excerpt").
5. *An example of the checker's marks.* Yes, one short block of three candidates on the lending library, written for the chapter and said so, one per mark, because the three marks are the part a reader cannot picture from their names (docs/04 "Teach, do not only show"): seen, a candidate of one delivery against docs/01; latent, one delivery against another that nothing triggers today; weak, a claim the file does not bear out. Each candidate is one the delivery review of chapter 13 could not see, since it spans two deliveries or a delivery and a document; they hold to chapters 4 and 12 and leave chapter 14's due-date story alone (Behaviour names them).
6. *Both hosts.* "In any host" is taught as docs/05 §8's two branches: one read-only agent per area, in parallel, where the host runs agents; one fresh session per area, opened by the person, where it does not (M16's paragraph, docs/05 §8).
7. *The person's word.* The line "The agent may say it is time, and never launches it." becomes the rule docs/05 §8 states: the reading costs, so the session says when it is time and starts it only on the person's word. Its reason in the present: each reader reads its area with the whole repository open, so the reading costs a reader per area (docs/04 "The kit as it is").
8. *Why the range.* Said in the present as the error it prevents: a review given one commit reads what that commit changed, the milestone's last delivery, and the milestone is every change since the base; `git diff <base>..HEAD` shows them all, and the review's page lists, by the slot's areas, the paths `git diff --stat <base>..HEAD` shows, so the paths the readers read can be checked against it. `git diff` is explained in a few words where it appears; chapter 18 teaches it (docs/04 "Teach, do not only show").
9. *No measure, no history.* The kit's own account of why the rule exists (a cancelled cloud review, a launch with a bare commit, readers who read part of the chapters, a candidate that did not hold, 21 lines of rework) does not enter: it is a measure and a history of a kit change, which docs/04 "The kit as it is" forbids, and a run of this repository, which ADR-0017 keeps out. Each becomes its rule's reason, in the present.
10. *Models and hosts named.* None: no `/code-review`, no cloud review, no Opus, Fable or advisor. The slot's model is said as "the model its readers and checker run on, or the session's" (ch13-delivery-review decision 3).
11. *The slot set to none.* One clause: a project whose Milestone review slot says none has no code reading, and the hand test still runs (the slot template's "or: none"; ch13-delivery-review decision 8).
12. *Where each delivery's code is read.* The line on it names the delivery review before `/apply` ends beside the staged change, both in chapter 13, since `ch13-delivery-review` comes before this line in M16; the milestone's readers look for what those could not see: one delivery against another, a document against another, the whole against docs/01 (docs/05 §8).
13. *The queue example's review line.* `[x] m1-review  each clause of the paragraph tested by hand` becomes `[x] m1-review  the paragraph tested by hand, the code read` (pt `[x] m1-review            o parágrafo testado à mão, o código lido`), so the example matches the review it closes; within 74 columns (docs/04 "Width of a block").
14. *The gain.* One sentence added, no number: the checker spends the person's time on the candidates that hold, and the paths read make a part of the milestone left unread show on the page instead of passing as read (docs/04 "One gain", "A gain per chapter"; ch13-delivery-review decision 10).
15. *A docs/03 term.* Yes, `candidate` / `candidato`: docs/03's `milestone review`, `delivery review` and `finding` rows lean on it and no row defines it, and this chapter defines its three marks. Requested on the Contract for the driver session; docs/03's `milestone review` row already holds the readers, paths read and checker, so it needs no change.
16. *Portuguese words.* Fixed on the Contract, one rendering each, matching chapter 13 (`agente somente leitura`, `revisão da entrega`) and docs/03 (`revisão de marco`, `achado`, `sessão nova`) (docs/04 "Languages").
17. *Chapters 7, 11 and 23.* They still say a person launches a deep code review (chapter 7's slot list and its question 6, chapter 11's §The review, and its findings, chapter 23's "Who reviews the milestone"), and chapter 7 counts nine slots where docs/05 now has the Delivery review too. No M16 line owns them; this page does not widen to them and asks the driver for one new `[ ]` line after this one (Contract, docs/06).
18. *Trunk, nothing staged by this definition.* docs/05 §5 Git; the driver session sets the marks in docs/06 (this batch's instructions). Chapter 13's files, changed in the tree by another session, are not this page's.


**Decided in /apply, without the author** (this batch's rule: the recommended option, recorded here).

19. *The slot's wording.* The lending library's slot is shown as a three-line block in the edition's language, "by areas, one reader each: `src/features/loans/`, `src/features/members/`, `src/features/catalog/`, the documents and the rest; readers and checker on the session's model", followed by one sentence on why its areas are chapter 4's slices; the split-again rule's example is `loans/` into its lending and its `return/`.
20. *Where "candidate" is defined in the chapter.* At the first sentence that uses it in §Read the code since the base, by areas ("a candidate is what a reviewer reports before anyone acts on it"), matching the docs/03 row; the opening uses the word before it, as the opening's promise of what the chapter teaches.
21. *The example's line numbers* (12, 14, 18, 21) are invented for the block, which is said to be written for the chapter; the latent candidate names two files on two rows, so the block keeps its 74 columns in both editions.
22. *The sentence after the block* says what to see: the seen and the latent candidates each sit across two slices, which no delivery's review reads together, and the weak one, unchecked, would have spent the person's time (docs/04 "Teach, do not only show").
23. *docs/03's row.* The driver had not added it; this delivery adds the Contract's row verbatim after `finding`.

**Behaviour.**

* The opening's second sentence says the reader can say what the review reads: the paragraph by hand, and, on the person's word, the code changed since the milestone's base, by areas, one read-only agent each, with a checker before the person sees a candidate; and why its findings get no review of their own. The opening stays at most three sentences.
* §The review is a delivery: the base sentence keeps "Its page names the commit that closed the previous milestone, or the project's first commit" and its second clause says the page lists, by the areas of docs/05's Milestone review slot, the paths the range since that commit changed; the next line says the reading costs, so the session says when it is time and starts it only on the person's word; the first-commit sentence follows unchanged; the line on where each delivery's code is read names the delivery review and the staged change (chapter 13) and the pull request (chapter 20).
* Reading §Read the code since the base, by areas, a reader can explain:
  * why the range: the milestone is every change since the base, `git diff <base>..HEAD` shows them all, and a review given one commit reads only that commit, the last delivery;
  * what the slot holds: the areas a milestone's changes split into, one reader each, and the model the readers and the checker run on, or the session's; the lending library's slot is shown, written for the chapter and said so;
  * that an area too large for one careful reading splits again;
  * who reads, in any host: one read-only agent per area (the agent of chapter 13 that reads files and edits nothing), in parallel where the host runs agents, or one fresh session per area, opened by the person, where it does not;
  * what a reader looks for: what no delivery's own review could see, one delivery's work against another's, a document against another, the whole against docs/01; with the whole repository open, it reports candidates by file and line and the paths it read;
  * the paths read: the review's page compares them with the range's; when they miss some, the page says which and the review line waits as `[?]` with `· resume: apply` (chapter 14), because a reader that read part of its area reports the same way as one that read it all;
  * the checker: one, an agent or the review's session, opens each candidate's file and marks it seen, latent (nothing triggers it today) or weak (the claim does not hold as stated), before the person sees it, because a reader's candidate is a claim about a file and some do not hold once the file is opened;
  * the example block of three candidates on the lending library, written for the chapter and said so, each as file and line, the reader's claim and the checker's mark, within 74 columns, followed by one sentence on what to see in it; it holds to chapter 4's layout and chapter 12's table `loan` (`returned_at` null while the loan is open):
    * seen: `src/features/members/myLoans.server.ts` (pt `src/features/membros/meusEmprestimos.server.ts`), the query of `my-loans`, reads the table `loan` directly, where the library keeps loan code in `src/features/loans/` and other slices import it (chapter 4, docs/03 `vertical slice`): true today, and no hand test shows it;
    * latent: that file and `src/features/loans/return/repository.server.ts` (pt `src/features/emprestimos/devolucao/repositorio.server.ts`) each write their own condition for an open loan, `returned_at` null (pt `devolvido_em`): the same today, apart the day a loan gains another state; nothing triggers it;
    * weak: a reader says `return-book` records a return for a copy never lent; the file shows its update matches only an open loan and refuses otherwise.
  * that the readers and the checker fix nothing, a candidate becomes a finding only when the person confirms it, and a slot that says none means no code reading while the hand test still runs.
* §A line, and not a fix: the queue example's `m1-review` line reads as decision 13; the block stays within 74 columns.
* §What the team gains: its three sentences stay and one sentence is added, as decision 14.
* Key point 3: the person tests each clause by hand and, on the person's word, the session reads the range since the base by the slot's areas, one read-only agent each listing the paths it read, and a checker marks each candidate; a clause no delivery answers, one that fails in the person's hands, or a candidate the person confirms is a finding. Still five key points.
* The Ninjobs section, §Test each clause by hand, §No second review and key points 1, 2, 4 and 5 are unchanged.
* Edge: nothing in either edition names a kit version, cites the changelog, compares the kit with an earlier one or recounts how the rule came to be (decision 9).
* Edge: nothing names `/code-review`, a cloud review, Opus, Fable or an advisor; nothing names this repository's areas.
* Edge: the prose rules of docs/04 hold, `not-but` included, in the passages that say what a reader looks for and what the checker marks.
* Failure: a passage saying the readers or the checker fix anything, that the agent never starts the reading, that a host's command is the reading, that a single commit is read, that a candidate is a finding before the person confirms it, or that the line closes while the paths read miss part of the range, contradicts docs/05 §8 and this page.
* Failure: one edition changed and not the other, or the example block or the slot over 74 columns.

**Contract.**

* **Files.** `book/en/15-closing-a-milestone.md` and `book/pt/15-closing-a-milestone.md`, same changes; no other chapter. docs/03, the one `candidate` row below, only if the driver session has not added it.
* **Sections touched** (found by text): the opening; §The review is a delivery / §A revisão é uma entrega, from the base sentence's second clause ("when docs/05's Milestone review slot names a deep review" / "quando o slot Milestone review (revisão de marco) do docs/05 cita") through the line "Each delivery's code is still read" / "O código de cada entrega continua sendo lido", keeping the first-commit line; §Read the whole code once / §Leia o código inteiro uma vez, renamed (decision 3), its first paragraph kept; §A line, and not a fix, the `m1-review` line; §What the team gains; key point 3.
* **Terms of docs/03.** `milestone review`, `delivery review`, `finding`, `slot`, `host`, `fresh session`, `waiting mark`, `resume suffix` used as defined. One new row, asked of the driver session before /apply:
  `| candidate | candidato | none | What a reviewer reports, by file and line, before anyone acts on it: in the delivery review, fixed by /apply or turned into a `[ ]` line; in the milestone review, marked seen, latent (nothing triggers it today) or weak (the claim does not hold as stated) by the checker, and a finding only once the person confirms it. |`
  placed after `finding`.
* **Portuguese words.** reader: `leitor`; checker: `conferente`; area: `área`; candidate: `candidato`; seen, latent, weak: `visto`, `latente`, `fraco`; range: `intervalo`; the person's word: `a palavra da pessoa`; read-only agent: `agente somente leitura`; delivery review: `revisão da entrega`; milestone review: `revisão de marco`; fresh session: `sessão nova`. The slot keeps its name, `Milestone review`, as the chapter already writes it. In the pt example the feature folders are `src/features/emprestimos/`, `src/features/membros/`, `src/features/catalogo/` (chapter 4).
* **Sources.** None added or removed. Rules named in plain words: docs/05 §8 and the Milestone review slot.
* **Cases.** No private case added; the Ninjobs passage is unchanged.
* **Numbers.** None added.
* **docs/06.** This line's marks, set by the driver, and its suffix, asked of the driver: `· after kit-2026-10-17, ch13-delivery-review`, since this chapter points to chapter 13's delivery review and its read-only agent (decision 12), which only `ch13-delivery-review` writes. One new line asked of the driver, in M16 after `ch15-review-by-areas` and before `m16-review`, which then also waits on it:
  `[ ] ch07-11-23-review-words   chapters 7, 11 and 23: the milestone review's code reading by areas on the person's word, no deep review a person launches, and chapter 7's slots with the Delivery review; both editions · after ch15-review-by-areas`

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Out of scope.**

* Chapter 13's delivery review: `ch13-delivery-review`.
* Why the governor admits the reviews' readers and checker as its one specialized subagent: `ch16-review-agents`.
* How `/analyze` and `/brainstorm` ask for the slot's areas and model, and chapter 8's update report: `ch08-09-review-slot`.
* Batches of proposes and parallel applies: `batch-propose`.
* Chapters 7, 11 and 23's sentences on the milestone review: the new line asked above (decision 17).
* This repository's own slot, areas and models: a project choice (decision 4).
* Any measure or history of the rule (decision 9).

**Done when.**

* [x] Both editions written, same sections, the same headings renamed, parity green.
* [x] The chapter opens with its value, at most three sentences; no filler, nothing useful cut; still five key points.
* [x] Every Behaviour line reads as written in both editions; the slot and the example block are said to be written for the chapter and stay within 74 columns.
* [x] `grep -n "or the project's first commit" book/en/15-closing-a-milestone.md` still finds 2 lines and `grep -c "left part of the project unread"` 1; pt `"ou o primeiro commit do projeto"` 2 and `"deixaram parte do projeto sem ler"` 1.
* [x] `grep -n -i -E "2026\.|changelog|no longer|opus|fable|advisor|code-review|ultra|deep review|never launches" book/en/15-closing-a-milestone.md` finds nothing; `grep -n -i -E "2026\.|changelog|não mais|opus|fable|advisor|code-review|ultra|revisão profunda|nunca a lança" book/pt/15-closing-a-milestone.md` finds nothing.
* [x] The Portuguese uses the Contract's words and no synonym.
* [x] docs/03 holds the `candidate` row as the Contract writes it, added by the driver session or, if absent, by this delivery; no number added.
* [x] No em dash; `make verify` green, disclosure scan included.
* [x] The Delivery review ran on this delivery's paths as docs/05 §5 says, and the page records it.
* [x] The author's approval of an anonymized passage: inapplicable, no Case A or Case B passage.
* [x] `make book` builds, and the delivery ends giving the author both PDF paths to review.

**Proof.** `make verify` green (build, parity, em dash, prose, width, links, disclosure). `make book` builds `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`, the author's review of chapter 15 in both. The Done when greps give 2 and 1 (en), 2 and 1 (pt), and nothing for the forbidden words.

**Divergences.** None from the page. The driver had not added docs/03's `candidate` row; this delivery added it as the Contract writes it (decision 23).

**Delivery review** (docs/05 §5): a read-only agent on Opus read `git diff` and `git diff --cached` of this delivery's paths, of docs/06 only this line's hunk, against the page, docs/03, docs/04, docs/05 §8 and the installed skills. Nothing broke the page or docs/04. Its findings, and what became of them:

1. "each reader reads its area ..., a reader per area" used "reader" before the section defines it and said the idea twice: fixed, "each area gets a reader of its own, which reads it with the whole repository open" (pt to match).
2. "its update" in the weak candidate read as an ordinary noun, and in pt as an English word: fixed, `UPDATE`, the SQL keyword, in both editions.
3. The opening mixed "the person's word" with "before you see": fixed, "before the person sees a candidate" (pt to match), as the Behaviour line says.
4. Chapters 7, 11 and 23 still describe a deep review a person launches: already the line `ch07-11-23-review-words`; no new line.
5. Chapters 8 and 9 still name the deep review in the slot: already the line `ch08-09-review-slot`; no new line.
6. The gain's "The read of the whole code" sits loosely beside the renamed section: kept, since decision 14 keeps the gain's three sentences and the range is still the milestone's whole code; no line.

```commit
docs(ch15-review-by-areas): read the milestone by areas in chapter 15

- Read git diff <base>..HEAD, never a bare commit, split by areas
- One read-only reader per area in any host, on the person's word
- Paths read checked against the range; line waits as [?] if short
- A checker marks each candidate seen, latent or weak
- Add the candidate / candidato row to docs/03

work/done/ch15-review-by-areas.md
```
