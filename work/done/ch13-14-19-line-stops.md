# ch13-14-19-line-stops

**Objective.** After chapter 13 a reader knows that a code change asked outside `/apply` becomes a `[ ]` line, that what the line cannot hold goes into a draft `work/<slug>.md`, and that the answer stops there naming `/propose <slug>` for a fresh session, which starts from that draft; chapters 14 and 19 say the same where they reach that moment.

**Behaviour.**

* A reader asks the agent, in an ordinary session, for the due date as day/month/year, and adds how it should look on a narrow screen and that the catalog keeps the ISO form. From chapter 13 they expect: the line `[ ] due-date-format   the loan screen shows the due date as day/month/year` added above `m1-review`; a draft `work/due-date-format.md` holding the narrow-screen rule and the catalog exception; and the answer ending with `/propose due-date-format`, written as their host invokes it, for a fresh session. No file of the app changes.
* Without detail beyond the sentence, the line alone is enough: no draft is written for a request the line holds whole.
* A reader who then opens `/propose due-date-format` in a fresh session expects it to start from the draft, bringing it into the branch or worktree it creates, and to write the page from it; nothing they said is asked twice.
* Failure: a reader who says "define it now" in the ordinary session and expects the page written there. Chapter 13 answers: the draft takes what was said, and the page is `/propose`'s, in a fresh session, because the skill is a command the host runs and the agent cannot invoke on its own; a page written without it has nothing of what `/propose` reads.
* Failure: an agent that writes the narrow-screen rule and the catalog exception into the queue line. The reader knows the line is one sentence and the detail belongs to the draft.
* A reader of chapter 14's "When you do not know yet" finds that an exploration ends in one of three ways: a line in the queue, with a draft when the line cannot hold what was found; a decision written in its document; or nothing, and no fourth way that continues as `/propose` in the same session.
* A reader of chapter 19 finds the manager's code change becoming a line, with a draft for the detail, and `/propose` named for a fresh session.

**Contract.**

* **Chapter 13, both editions, file name, title and headings kept.**
  1. Opening, second sentence: "and turn a code change asked outside `/apply` into a line, or continue it as `/propose` in the same session" becomes "and turn a code change asked outside `/apply` into a line and a draft for its page".
  2. "Changing the queue": the sentence "A change to it asked in any other session, however small, becomes a `[ ]` line: the agent writes the line, says so, and the answer stops there, with no file of the app changed." gains the draft: what was said that the line cannot hold goes into a draft `work/due-date-format.md`, and the answer stops there, naming `/propose due-date-format` for a fresh session, written as the host invokes it. The paragraph "When you want the change defined now, say so: the conversation continues as `/propose due-date-format` in the same session, the line goes `[~]`, and what you said becomes the page instead of a longer line (chapter 14 shows `/propose`)." is replaced by: the draft is where the detail waits; `/propose`, in a fresh session, starts from it and writes the page (chapter 14), so nothing said in the first session is said twice; the reason, in the present: the agent cannot run `/propose` on its own, it is a command the host runs, and a page written without it starts without what `/propose` reads. The sentences after it in the paragraph stay.
  3. "What the team gains": "with one sentence, the detail goes to a page, in the same session if the person wants it" becomes "with one sentence, the detail goes to the page, or to its draft until `/propose` writes it". The rest of the paragraph and its numbers stay.
  4. Key points: the last point's "or continues as `/propose` in the same session when you want it defined now" becomes "with a draft page for what the line cannot hold, and `/propose` in a fresh session".
* **Chapter 14, both editions**, "When you do not know yet": "or `/propose` in the same session, which starts with the exploration already in its context" becomes: or a line with a draft page holding what the exploration found, which `/propose` starts from in a fresh session. The sentence after it (no mark, command or kind of delivery added) stays.
* **Chapter 19, both editions**, the sentence "A change to the code, however small, becomes a line as well (chapter 13), and the answer stops there, or continues as `/propose` in the same session when the manager wants it defined now." becomes: becomes a line as well, with a draft page for the detail, and the answer stops there naming `/propose` for a fresh session (chapter 13).
* **Portuguese:** `formato-devolucao` as chapters 13 and 19 have it; "rascunho" for draft, as docs/03 will have it after `kit-2026-10-16-2` adds the term; "sessão nova" for fresh session, as chapter 15 already says it.
* **Terms:** `draft page` (pt `rascunho da página`): a `work/<slug>.md` written for a `[ ]` line, holding what the line cannot, that `/propose` starts from. Added to docs/03 by `kit-2026-10-16-2`; this delivery uses it. If that line is not `[x]` first, this delivery adds the row.
* **Sources:** docs/05 §2 and the AGENTS.md template as SETUP.md writes them; the kit's changelog paraphrased with no note, present tense, no version: the agent cannot invoke the skill, and a request not defined now needs a place for its detail.
* **Cases:** none new.
* **Code examples:** the `due-date-format` line already in chapter 13; the draft is described, not shown (one sentence says what it holds), since a draft is a page in the making and chapter 14 shows the page.

**Out of scope.**

* docs/05 §2, AGENTS.md's line and docs/03's new row in this repository: `kit-2026-10-16-2`.
* Chapter 14's account of what `/propose` reads and brings into its worktree: unchanged; the draft is one more thing it reads, said in chapter 13.
* Chapter 16's `[?]` with `resume: propose` keeping its draft: unchanged; it already says a draft stays.
* The kit's AGENTS.md line of this book's repository: `kit-2026-10-16-2`.
* A transcript of the ordinary session: told in prose (ADR-0017).

**Done when.**

* [x] Chapters 13, 14 and 19 changed in both editions, same headings; chapter 13 still opens with its value; no filler and nothing useful cut.
* [x] No sentence in the book says a request continues as `/propose` in the same session; `grep -rn "same session\|mesma sessão" book/` shows only chapter 15's "ask for each correction in the same session", which is `/apply`'s own session and stays.
* [x] The rule's wording matches docs/05 §2 as `kit-2026-10-16-2` leaves it.
* [x] `make verify` green; `make book` builds and both PDF paths are given to the author.
* [x] Page in `work/done/`, the line `[x]`, staged by its paths and its hunk of docs/06, the commit suggested in a `commit` block.

**Decisions taken from the documents.**

* Trunk, no branch: docs/05 §5 Git.
* The rule's wording, "a `[ ]` line, with a draft page for what the line cannot hold, and the answer stops there, naming /propose for a fresh session": SETUP.md's docs/05 §2 and AGENTS.md template.
* The reason said in the present (the agent cannot invoke the skill; the detail needs a place): docs/04, the kit as it is; the changelog gives both.
* Chapters 14 and 19 changed here so no chapter contradicts chapter 13: precedent `ch13-short-lines`.
* The draft described and not shown: docs/04, no runs; chapter 14 already shows a page.

**Decisions in the review.**

* Chapter 13 describes the draft in one sentence and shows no block, as recommended.

**What happened.**

* Built: chapter 13's opening, "Changing the queue" (the draft in the rule's sentence, the example request with its narrow-screen rule and catalog exception, the draft that holds them, the answer naming `/propose due-date-format` for a fresh session, and the reason "define it now" changes nothing), its gain sentence and its last key point; chapter 14's "When you do not know yet" and its last key point; chapter 19's code-change sentence; both editions, headings unchanged.
* docs/03: the row `draft page | rascunho da página | work/<slug>.md` added after `page`. The page expected `kit-2026-10-16-2` to have added it; that line is `[x]` without it, so, as the page's fallback says and the author confirmed in this session, this delivery adds it.
* Rule's wording checked against docs/05 §2 and `AGENTS.md`: a `[ ]` line, a draft `work/<slug>.md` for what the line cannot hold, the answer stops there naming `/propose <slug>` for a fresh session, as the host invokes commands.

**Divergences.**

* Chapter 14's last key point also said "`/propose` in the same session"; the Contract named only the section's sentence, and Done when asks that no sentence say it, so the key point changed with it.
* Chapter 14's three endings follow Behaviour: a line, with a draft when the line cannot hold what was found; a decision; or nothing. The Contract's literal wording would have made two of the three a line, so the draft joins the first ending.
* `grep -rn "same session\|mesma sessão" book/` still shows, besides chapter 15's three sentences on `/apply`'s own session (the correction and its reasoning, and the key point): chapter 12's "ask the agent for the fix in the same session", the setup session's own fix, not a request continuing as `/propose`, which stays; and chapter 11's update report, which quotes the 2026.10.16 migration and is replaced by `ch11-update-2026-10-16-2`.

**Proof.** `make verify` green; `make book` built `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf` for the author's review of chapters 13, 14 and 19.

```commit
docs(ch13-14-19-line-stops): a request outside /apply stops at the line

- chapter 13: a draft page holds what the line cannot hold
- chapter 13: /propose starts from the draft in a fresh session
- chapters 14 and 19: no request continues as /propose in the same session
- docs/03: the term draft page
work/done/ch13-14-19-line-stops.md
```
