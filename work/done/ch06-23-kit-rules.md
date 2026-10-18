# ch06-23-kit-rules

**Objective.** The reader can name the kit's rules and the failure each prevents, and distinguish them from the project's own checks.

**Behaviour.**

* Reading chapter 6's rule map, the reader finds the six rules of SETUP.md §2: one page, separate deciding and doing, staging and the person's authority over commits, project slots, living documents, and the governor.
* Given a delivery that changes a behaviour documented elsewhere, the reader says its owning document changes in that delivery; the list no longer substitutes a one-line queue for this rule.
* Given a verify command repeated inside a skill, the reader explains why the command reads the project's slot instead; the existing drift story supports that rule without inventing a new incident.
* Reading chapter 23's answer to "Too much process", the reader reaches the same six rules in chapter 6 and does not count the queue as an extra universal rule or treat every project check as mandatory in the kit.

**Contract.** Edit `book/en/06-birth-of-focus-kit.md`, `book/pt/06-birth-of-focus-kit.md`, `book/en/23-adoption.md` and `book/pt/23-adoption.md`: chapter 6's rule map and matching key point, chapter 23's resistance answer and its pointer.
Source: focus-kit `SETUP.md` §2, version 2026.10.18.1 read in the kit's working tree, not a claimed published commit; public source is <https://github.com/JCKodel/focus-kit/blob/main/SETUP.md>.
Keep the queue's useful explanation as supporting prose, rather than one of the six listed rules, and explain living documents through the existing six-places failure.
The commit rule states the source's distinction between acting on its own and acting when asked; `agent-commits-asked` owns the broader treatment across chapters, so those applications must not edit chapter 6 concurrently.
Terms are the existing delivery, page, slot, queue and governor of docs/03; no new concept.
These choices follow docs/00's useful content rule and docs/04's kit-as-it-is rule; no changelog narrative or invented historical cause.
Ninjobs evidence already in chapter 6 stays paraphrased; no Case A or Case B passage is changed or added.

**States.** Inapplicable: prose, no screen.

**Visual reference.** Inapplicable: existing chapter layout.

**Out of scope.** Kit installation and process migrations belong to `kit-2026-10-18-1`; the broader commit guidance belongs to `agent-commits-asked`; Case A and Case B evidence is unchanged.

**Done when.**

* [x] Both editions pass each Behaviour check; the list and its cross-reference agree with SETUP.md §2.
* [x] Each chapter still opens with its value and keeps its evidenced team gain, with no filler or useful material cut; all retained numbers and artifacts keep their provenance.
* [x] Existing Ninjobs observations are preserved without exposing implementation details; no private-case passage is introduced, so OD-3 approval is inapplicable.
* [x] `make verify` and `make book` pass; both PDFs are given to the author for review, as docs/05 §5 requires.

**What was built.** Chapter 6's rule map lists SETUP.md §2's six rules in its order: one delivery is one page (answering the change folder), deciding and doing in separate sessions (now with `/propose` writes no code and `/apply` widens no scope), the agent stages and suggests the commit message and never commits or merges on its own, asked it takes the step the person names (answering the 29 checks), project specifics are slots in docs/05 (answering the drift), documents are living (answering the six places), and the governor. An opening sentence names the source and says any other check is the project's own. The queue keeps its chapter 11 explanation as prose after the list, serving the rules without being one. The third key point lists the six failures in the same order. Chapter 23's "Too much process" answer says the six rules are the same in every project and every check beyond them is the project's own, so the kit imposes none. Both editions.

**Divergences and omissions.** None. Key point 2 keeps the queue line, since it lists what held on Ninjobs, not the kit's rules.

**Proof.** Prose: each Behaviour bullet reread against both editions and against SETUP.md §2; Ninjobs evidence unchanged; no Case A or Case B passage touched; `make verify` green after the last edit. `make book` and the PDF paths are the batch driver's, run once at the end.

**Delivery review.** One read-only Opus agent over `git diff HEAD` of the four chapter paths, against this page, docs/03, docs/04 and SETUP.md §2. Candidates and answers: the separate-sessions rule left out `/propose` writes no code and `/apply` widens no scope, added; the governor rule dropped "concrete", added; "or merges" has no evidence of its own, left, since it is the source's rule and the evidence is the person's reading; chapter 16 says Ninjobs opened on the six rules SETUP.md lists, while chapter 6 dates the drift that pulled facts out of the commands after the opening, outside this page and already so before it: a new queue line.

**Decisions.** Recommended answers taken under the batch: the queue explanation sits right after the list; one page answers the change folder and living documents answer the six places; `agent-commits-asked` was not editing chapter 6 or 23 during this delivery.
