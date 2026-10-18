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

* [ ] Both editions pass each Behaviour check; the list and its cross-reference agree with SETUP.md §2.
* [ ] Each chapter still opens with its value and keeps its evidenced team gain, with no filler or useful material cut; all retained numbers and artifacts keep their provenance.
* [ ] Existing Ninjobs observations are preserved without exposing implementation details; no private-case passage is introduced, so OD-3 approval is inapplicable.
* [ ] `make verify` and `make book` pass; both PDFs are given to the author for review, as docs/05 §5 requires.
