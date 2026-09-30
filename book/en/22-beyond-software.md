# Projects that are not software

After this chapter you can run a proposal, an analysis, a handover document, a data rule or a book as deliveries, each on a page whose Done when a person can tick.
You can also say why a finding with no line in a queue gets lost.

## The problem

A proposal, an analysis or a handover has decisions, a scope and a moment when it is done, like code.
It is usually written with no process at all: a file in a shared folder, versions named "final" and "final 2", findings sent by email.
Nothing says what is still pending, and nothing checks that a decision taken on one version reached the next.

## A delivery is anything with value that fits a page

Chapter 14 defined a delivery as the smallest change that has value, and nothing in that definition says code.
The page format reads the same for a document:

* **Objective.** What the reader of the document can do after reading it.
* **Behaviour.** What the reader can do, one line each, every line a check a person makes by reading or by trying.
* **Contract.** The document's structure: its sections, its format, the facts it must carry.
* **Out of scope.** What the document does not cover, and where that lives instead.
* **Done when.** A checklist a person ticks.

States and Visual reference are usually "none", or the template the document follows.
A page for the lending library of Part I, written for this chapter:

```markdown
# librarian-guide

**Objective.** A new librarian lends and takes back a copy on the first
day, with this guide and no training.

**Behaviour.**
* A librarian who never used the system lends a copy by following the guide.
* A librarian finds, from the contents, what to tell a member who is refused.

**Contract.**
Sections: Lend, Take back, Refusals.
Refusals lists every member of LendRefusal with the message the member sees.
Markdown in guide/, and a PDF built from it.

**Out of scope.**
* Managing members: its own guide, `admin-guide`.

**Done when.**
* [ ] Every member of LendRefusal appears in Refusals.
* [ ] A person who never used the system lends a copy with the guide alone.
* [ ] The PDF builds.
```

`/apply` writes the guide as it would write code: it follows the page, runs what can be checked by a machine (the PDF builds, every refusal is listed), and leaves the rest of Done when for the person to tick.

## Case A's documents

On Case A, a client project on a low-code platform, the handover was a set of deliveries.[^case-a]
A solution design, an installation guide in three formats, a handover document and a presentation, an evidence pack indexed by the acceptance criteria, a repository readme and a work record each had a queue line and a page, and each went through `/propose` and `/apply` like code.
The evidence pack shows the Contract as structure: indexed by the acceptance criteria, it lets the client check the delivery criterion by criterion and find the proof of each.

Some deliveries produce nothing but a person's written answer.
A question delivery's page says what is asked, of whom, and what each possible answer unblocks, and it is done when the answer arrives (chapter 21).
Of Case A's 73 done lines, 8 were questions to people and about eight were documents.[^case-a]

## Data work as deliveries

A database's security rules decide who may read or write which row, and they are work with value like a screen.
On Ninjobs, six of its 93 finished pages changed only database rules, and nothing else.[^ninjobs]
One of them was the rule "no writes while a deletion is pending": it was enforced in the database itself, by an access rule, and proven by the project's test of the access rules.[^ninjobs]
The build found that a blanket rule would also block the database's own functions, so the rule became "no write path reachable from the client", and the page recorded why.

A rule in the database holds for every client that will ever talk to it, and its test is the Done when that proves it.

## This book

This book is written with the kit: one page per chapter in `work/`, a queue of milestones in docs/06, and `make verify` as its verify command.
Its checks are the parity of its two editions, its prose rules and a scan against its disclosure list, so a chapter is done when they are green and the author has approved every passage about a private case.

## Case B, the contrast

Case B is a consultancy's proposal for a client's adoption program, and it did not run on the process.[^case-b]
An analysis of the proposal was written with one discipline of this book: every number carried its provenance, whether it came from the proposal, a measurement, an estimate or experience.
It found six faults.
Among them, the proposal named the wrong tool, a contract risk, and it fixed a scope without fixing how much work that scope covered, which left it open to growth nobody would pay for.

The findings had no queue line and no page to carry them.
Two days later, the next version of the proposal still held at least one of them.[^case-b]
The analysis was right, and being right was not enough: each finding needed a line, and a page whose Done when said "the next version names the right tool", so that the fault stayed open in plain sight until a person ticked it.

## What the team gains

One process for every kind of work the team does, so the same queue, the same page and the same review carry code, documents, questions and data rules.
On Case A, about 16 of its 73 done lines were questions or documents, and on Ninjobs six of 93 pages were database rules, all through the same two commands.[^case-a][^ninjobs]

## Key points

* A delivery is anything with value that fits a page, code or not.
* For a document, Behaviour is what its reader can do, the Contract is its structure, and Done when is a checklist a person ticks.
* A question to a person is a delivery too, done when the answer arrives.
* A database rule is a delivery with a test, enforced where every client meets it.
* A finding with no line gets lost: Case B's analysis was right, and at least one of its faults survived into the next version.

[^case-a]: Case A, a client project on a low-code platform, a private repository, counted by the author in its queue in docs/06 and its pages: 73 done lines, 8 of them question deliveries and about 8 document deliveries, the handover set named here. Its owner, its client and its business are not disclosed.
[^case-b]: Case B, a consultancy's proposal for a client's adoption program, private files read by the author: three versions of the proposal, a deck, an internal note and an analysis; the proposal did not run on the process. Its owner and its client are not disclosed.
[^ninjobs]: Ninjobs, the author's product, a private repository, counted by the author in its `work/done/`: 93 finished pages up to 2026-09-23, 6 of them changing only database rules; the pending-deletion rule and its test read in its page.
