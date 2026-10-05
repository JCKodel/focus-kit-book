# critique-fixes

**Objective.** A reader who doubts the method on one of three points finds the answer where the doubt comes up. Chapter 14: you explore a problem you do not understand yet by talking to the agent before any page. Chapter 10: the page, the queue, verify and the commit work the same with or without FOCUS. Chapter 15: the review of the staged change is the defence against automation bias. Both editions.

**Decided by the author.**
1. A new milestone, M11, with its review as its last line.
2. Exploring is not a new mark, a new command or a new kind of delivery. It is talking to the agent: an AI is a language model you converse with, not a button with fixed commands. The conversation reads the project's documents and ends in one of three ways: a new line in the queue, an opinion on how to solve the problem that the person accepts, or a `/propose` in the same session, with the exploration already in its context. On the author's projects this was rarely needed, and talking was always enough.
3. The sentence on working without FOCUS goes in chapter 10, §The two choices.
4. Chapter 15 gets no new mechanism: `/apply` already writes on the page what diverged and the decisions it took (chapter 15, §What `/apply` does). The chapter names the bias and shows that the review it already teaches is the defence.

**Behaviour.**

* A reader of chapter 14 who does not know yet what the delivery is can say what to do: talk to the agent in any session, and end with a line, a decision written where it belongs, or a `/propose` in the same session. They can also say why nothing new is needed for that.
* A reader of chapter 10 whose project will not use FOCUS can say what in the method still works for them (the page, the queue, the documents, verify, the commit) and what FOCUS would add.
* A reader of chapter 15 can say what automation bias is, where the book measures it (chapter 26), and how each part of the review counters it.
* The rest of chapters 10, 14 and 15 reads as before. The Portuguese edition says the same things in the same places.

**Contract.**

`book/en` and `book/pt`, files `10-the-documents.md`, `14-propose.md` and `15-apply.md`. The wording below is the English intent; /apply writes the final sentences and the Portuguese.

* **Chapter 14, opening.** The "After this chapter" sentence adds: explore a problem you do not understand yet by talking to the agent, before there is a page.
* **Chapter 14, a new section after §When it does not fit**, "When you do not know yet" (pt "Quando você ainda não sabe"), in a few lines:
  * A scope that does not fit a page because nobody knows the answer yet, such as how an unfamiliar API behaves or which of two approaches holds, is explored first, in what other methods call a spike.
  * The exploration is a conversation. The agent is a language model to talk with, not a button that runs a fixed command. It reads the documents, so its suggestions follow the project.
  * The conversation ends in one of three ways: a new line in the queue (chapter 13); a decision the person accepts, written in the document that owns it (chapter 10); or `/propose` in the same session, which starts with the exploration already in its context.
  * The evidence: on the author's projects this was rarely needed, and the conversation was always enough, with no mark or command added. That is the governor of chapter 18.
* **Chapter 14, Key points.** One bullet with the same idea.
* **Chapter 10, §The two choices**, after "or neither, the project's own conventions.": one or two sentences. With any of the three answers, the page, the queue, the documents, verify and the commit work the same. FOCUS adds code an agent reads one slice at a time (chapter 6) and a test per piece (chapter 8). /apply checks that chapters 6 and 8 say this and cites only what they say.
* **Chapter 10, Key points.** The bullet on the two choices adds that the method works under any of them.
* **Chapter 15, §Review the staged change**, a short paragraph after the list:
  * A person who commits after many good deliveries stops checking. That is automation bias, defined and measured in chapter 26.
  * The review counters it in four ways. It is a set of questions answered against a page you already read, not a glance. The page's record of what happened shows where the agent decided alone. One page keeps the diff small. Verify and the proof ran before you look, so your attention goes where no check reaches.
  * No new numbers; chapter 26 holds them and their notes.
* **Chapter 15, Key points.** One bullet: the review is the defence against automation bias.
* Terms: none added to docs/03 ("spike" is only another method's name, given once). Sources: none new; chapter links only. Cases: no Case A or Case B passage, so OD-3 does not apply; Ninjobs is not cited.

**Out of scope.**

* A spike mark, command or delivery type: decision 2, and the governor of chapter 18.
* Friction mechanisms at commit time (a terminal that waits for an answer, comments planted in the code): they name no error that happened, and the review already counters the bias.
* Any change to focus-kit's commands: `/apply` already records its decisions.
* Moving chapters 4 to 8 to an appendix, or making FOCUS secondary: the rewrite put the base before the method (ADR-0017).
* Chapter 12's strangler fig: decision 3 puts the sentence in chapter 10.
* Case A's question deliveries (chapters 22 and 23): unchanged.

**Done when.**

* [x] Chapters 14, 10 and 15 as Contract, in both editions.
* [x] No other line of the three chapters changed beyond the Contract.
* [x] Each change opens with its value, has no filler and cuts nothing useful; no em dash.
* [x] `make verify` green, disclosure scan included.
* [x] `make book` run; both PDF paths given to the author, with the pages where chapters 10, 14 and 15 start.
* [x] Page in `work/done/`, `critique-fixes` `[x]`, staged, commit message suggested.

**What happened.**

* Chapter 10: the Contract said FOCUS adds "code an agent reads one slice at a time (chapter 6)". Chapter 6 teaches vertical slices, which the two-principles answer also has, so the sentence says the two principles give that too, and only the test for each of the four pieces (chapter 8) is FOCUS whole alone. Both chapters say exactly this.
* Chapter 14: the evidence line names no mark, command or kind of delivery added, and ties it to the governor of chapter 18 (none would name an error it caught). "Spike" appears once, as another method's name; docs/03 unchanged.
* Chapter 15: the paragraph goes at the end of §Review the staged change, after the three lines that follow the list, not right after the list, so "the page's record of what happened" comes after the line that asks the reader to read what happened. No number; chapter 26 holds them.
* The chapter 14 Key points bullet sits after the bullet on reading the page, in the chapter's order.
* Proof: `make verify` green, disclosure scan included; `make book` built both editions. PDF pages where the chapters start: English 71 (10), 96 (14), 103 (15); Portuguese 75 (10), 100 (14), 108 (15).
* No document changed: no term, rule or decision is new.
