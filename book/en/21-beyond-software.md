# 21. Projects that are not software

After this chapter you can run a proposal, an analysis, a handover document, a data rule or a book as deliveries, each done only when every item of its page's Done when has its evidence and `/apply` has ticked it.
You can also say why a finding with no line in a queue gets lost.

## The problem

A proposal, an analysis or a handover has decisions, a scope and a moment when it is done, like code.
It is usually written with no process at all: a file in a shared folder, versions named "final" and "final 2", findings sent by email.
Nothing says what is still pending, and nothing checks that a decision taken on one version reached the next.

## A delivery is anything with value that fits a page

Chapter 12 defined a delivery as the smallest change that has value, and nothing in that definition says code.
The page format reads the same for a document:

* **Objective.** What the reader of the document can do after reading it.
* **Behaviour.** What the reader can do, one line each, every line a check a person makes by reading or by trying.
* **Contract.** The document's structure: its sections, its format, the facts it must carry.
* **Out of scope.** What the document does not cover, and where that lives instead.
* **Done when.** A checklist of the checks that prove it done, some run by a machine, some made by a person reading or trying; `/apply` ticks each one when its evidence is on the page.

A page for the lending library of Part I, written for this chapter:

```markdown
# librarian-guide

**Objective.** A new librarian lends and takes back a copy on the first
day, with this guide and no training.

**Behaviour.**
* A librarian who never used the system lends a copy by following the
  guide.
* A librarian finds, from the contents, what to tell a member who is
  refused.

**Contract.**
Sections: Lend, Take back, Refusals.
Refusals lists every member of LendRefusal with the message the member
sees.
Markdown in guide/, and a PDF built from it.

**Out of scope.**
* Managing members: its own guide, `admin-guide`.

**Done when.**
* [ ] Every member of LendRefusal appears in Refusals.
* [ ] A person who never used the system lends a copy with the guide
      alone.
* [ ] The PDF builds.
```

`/apply` writes the guide as it would write code: it follows the page and runs what can be checked by a machine (the PDF builds, every refusal is listed).
The second item is a manual check, and only a person can make it: someone who never used the system tries to lend a copy with the guide alone.
Until that happens the delivery is not done, however green the machine checks are, and `/apply` does not move the page with that item left for a later tick.
Until the report comes, `/apply` stops as [chapter 13](13-apply.md) says: the page stays in `work/` and the delivery's line in the queue waits as `[?]`, with `resume: apply` and the report it waits on.
When the person reports that a new librarian lent a copy with the guide alone, the resumed `/apply` writes that report on the page as the item's evidence, ticks it with the other two, and moves the page to `work/done/`.
If the librarian got stuck, the guide is wrong where they got stuck: the person says where, `/apply` corrects it, and the check is made again.

## Case A's documents

On Case A, a client project on a low-code platform, Microsoft Power Apps with Copilot Studio, the handover was a set of deliveries.
A solution design, an installation guide in three formats, a handover document and a presentation, an evidence pack indexed by the acceptance criteria, a repository readme and a work record each had a queue line and a page, and each went through `/propose` and `/apply` like code.
The evidence pack shows the Contract as structure: indexed by the acceptance criteria, it lets the client check the delivery criterion by criterion and find the proof of each.

Some deliveries produce nothing but a person's written answer.
A question delivery's page says what is asked, of whom, and what each possible answer unblocks, and it is done when the answer arrives (chapter 20).

This book runs on the kit too: one page per chapter in `work/`, a queue of milestones in docs/06, and `make verify`, which checks the parity of the two editions, the prose rules and a scan against the disclosure list.
A chapter is done when those checks are green and the author has approved every passage about a private case.

## Data work as deliveries

A database's security rules decide who may read or write which row, and they are work with value like a screen.
On Ninjobs, six of its 93 finished pages changed only database rules, and nothing else.
One of those rules stops the client from writing while an account deletion is pending; it lives in the database itself, as an access rule, and the project's test of the access rules proves it ([chapter 13](13-apply.md) tells what its build found).

A rule in the database holds for every client that will ever talk to it, and its test is the Done when that proves it.

## Case B, the contrast

Case B is a consultancy's proposal for a client's adoption program, and it did not run on the process.
An analysis of the proposal was written with one discipline of this book: every number carried its provenance, whether it came from the proposal, a measurement, an estimate or experience.
It found six faults.
Among them, the proposal named the wrong tool, a contract risk, and it fixed a scope without fixing how much work that scope covered, which left it open to growth nobody would pay for.

The findings had no queue line and no page to carry them.
Two days later, the next version of the proposal still held at least one of them.
The analysis was right, and being right was not enough: each finding needed a line, and a page whose Done when said "the next version names the right tool", so that the fault stayed open in plain sight until a person checked the next version and the item was ticked on that evidence.

## What the team gains

One process for every kind of work the team does, so the same queue, the same page and the same review carry code, documents, questions and data rules.
On Case A, about 16 of its 73 done lines were questions to people or documents, and each went through the same two commands as the project's code.

## Key points

* A delivery is anything with value that fits a page, code or not.
* For a document, Behaviour is what its reader can do, the Contract is its structure, and Done when is a checklist of machine checks and manual checks.
* A check only a person can make stays the person's; `/apply` records what they report and ticks every item, and never one without its evidence.
* A question to a person is a delivery too, done when the answer arrives.
* A database rule is a delivery with a test, enforced where every client meets it.
* Give every finding a line, or it gets lost.

