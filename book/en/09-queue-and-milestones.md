# The queue and milestones

After this chapter you can read a queue, say what each mark means and which command changes it, and write a milestone paragraph a person can check.
You can also order a milestone's lines, and add or change a line by conversation.

## The line

As the kit's `references/documents.md` sets it, docs/06 holds the project's milestones, each with a paragraph saying what is true when it closes, and under each one line per delivery, in order.
A line has three parts, a mark, a slug and what the delivery gives, in one line:

```
[ ] <slug>    <what it delivers, one line>
```

The slug is the delivery's name, in lowercase words joined by hyphens.
It names the delivery's page, `work/<slug>.md`, and it is the argument of the commands, `/propose <slug>`, so the line, the page and the command all point at the same delivery.
You have read two queues already: the clinic's, which `/brainstorm` wrote in [chapter 7](07-brainstorm.md), at [`book-v1/brainstorm`](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/brainstorm/docs/06-Queue.md), and CLAHub's, which `/analyze` wrote in [chapter 8](08-analyze.md), at [`book-v1-analyze`](https://github.com/JCKodel/clahub/blob/book-v1-analyze/docs/06-Queue.md).

The kit asks for one line, and the reasoning goes on the page.
On Ninjobs I let the lines grow: its queue held 102 deliveries in 1,711 lines, 1,052 of them continuations of a line, decisions that belonged on the pages.[^ninjobs]
A line that grows into a paragraph is a decision in the wrong place: the page is where the next session looks for it.

## The marks

A line has one of three marks:

* `[ ]` not yet defined: the delivery has a line and no page.
* `[>]` defined: `/propose` wrote the page, `work/<slug>.md`.
* `[x]` done: `/apply` built it and moved the page to `work/done/`.

`/propose` turns `[ ]` into `[>]` when it writes the page (chapter 10).
`/apply` turns `[>]` into `[x]` when it moves the page to `work/done/` (chapter 11).
A line never leaves the queue; it changes mark, so the queue is also the history of what was delivered.

On trunk the page and the build land in one commit, so `[>]` waits in the working tree between the two commands; on a branch the page may be committed there, and the delivery reaches the main branch in one merge.
It is how a fresh session running `/apply` knows the page exists; Part IV teaches the git side.

## Milestones

A milestone's paragraph says what is true when the milestone closes, in sentences a person can check against the product.
It is a test, not a list of the lines under it and not a theme: "the owner can register professionals" can be checked, "professionals" cannot.
The clinic's milestone 1 paragraph, quoted in [chapter 7](07-brainstorm.md), is the example: each sentence is something the owner or a client can do.

A milestone holds three to eight deliveries, the rule of the kit's `brainstorm/SKILL.md` for the first milestone and a good size for any.
The first ones are the skeleton the others stand on; the clinic's first line, `skeleton`, creates `npm run verify`, which every later delivery runs.
Then each line comes after the lines it needs: a client cannot book before the owner has set a professional's hours.
Closing a milestone, and reviewing the whole, is chapter 12.

## Changing the queue

No command owns the queue.
A new idea becomes a line by conversation, in any session: you tell the agent, and it writes the line in the milestone where it belongs, with a new slug and `[ ]`.
A milestone's paragraph or a line's description changes the same way, and the slug stays, since a page or a commit may already use it.
Lines also come from a milestone's review (chapter 12) and, on an existing project, from its issues (chapter 8).
You review the diff, as with every document ([chapter 6](06-the-documents.md)).

This book's queue is an example.
After chapters 7 and 8 were done, I asked the agent to define the kit's [two choices](06-the-documents.md#the-two-choices) in chapter 6, so both chapters could point back to them.
This is the diff of docs/06 in that commit:

````diff
diff --git a/docs/06-Queue.md b/docs/06-Queue.md
index 52ea9aa..d9ddd9f 100644
--- a/docs/06-Queue.md
+++ b/docs/06-Queue.md
@@ -41,6 +41,7 @@ When this milestone closes, a reader can install the kit, document a new or an e
 [x] the-documents          Chapter 6: docs/00 to 06, ADRs, AGENTS.md, and why documents do the work
 [x] brainstorm             Chapter 7: /brainstorm on the guided project, and choosing a stack by what the agent knows (the Ninjobs lesson of chapter 4)
 [x] analyze                Chapter 8: /analyze on the brownfield project
+[x] two-choices            Chapter 6 gains "The two choices": FOCUS (four pieces, whole / two principles / neither) and git (trunk / branch / worktree) in a paragraph each, so chapters 7 and 8 point back to them; Parts III and IV still teach them
 [ ] queue-and-milestones   Chapter 9: the queue, the marks, milestones and their paragraphs
 [ ] propose                Chapter 10: /propose, one page, and splitting what does not fit
 [ ] apply                  Chapter 11: /apply, verify, proof, documents, stage, never commit
@@ -50,11 +51,11 @@ When this milestone closes, a reader can install the kit, document a new or an e
 
 ## M4. Part III, FOCUS architecture
 
-When this milestone closes, a reader can organize code by feature with errors as values, and knows when the four pieces pay their way and when they do not.
+When this milestone closes, a reader can organize code by feature with exceptions as values, and knows when the four pieces pay their way and when they do not.
 
 ```
-[ ] errors-and-slices      Chapter 14: errors as values and vertical slices, the two principles that stand alone
-[ ] four-pieces            Chapter 15: View, Orchestrator, Use Case, Repository, one table and one flow, and when the four pieces pay their way (the Ninjobs lesson of chapter 4)
+[ ] errors-and-slices      Chapter 14: exceptions as values and vertical slices, the two principles that stand alone
+[ ] four-pieces            Chapter 15: View, Orchestrator, Use Case, Repository, one table and one flow, and when the four pieces pay their way
 [ ] testing-and-agents     Chapter 16: testing each piece, and how the architecture helps an agent
 ```
 
````

The line `two-choices` entered in the middle of M3, where it belongs, already `[x]` because its page and its build landed in one commit; in the same commit, M4's paragraph and the descriptions of `errors-and-slices` and `four-pieces` changed their words and kept their slugs.
I asked the agent for the change and reviewed the diff; nobody edited the queue by hand.

## Key points

* docs/06 holds milestones, each with a paragraph, and one line per delivery under it: a mark, a slug and what it delivers, in one line; the reasoning goes on the page.
* The slug names the page, `work/<slug>.md`, and is the argument of `/propose` and `/apply`.
* Three marks: `[ ]` not defined, `[>]` the page exists (`/propose`), `[x]` done (`/apply`); a line never leaves, so the queue is also the history.
* A milestone paragraph is a test a person can check against the product; three to eight deliveries, the skeleton first, then each line after the lines it needs.
* No command owns the queue: lines and paragraphs change by conversation, in any session, with the slug kept, and you review the diff.

## Exercises

These exercises use the clinic at `book-v1/brainstorm`, by conversation with the agent, never by hand; commit nothing, since chapters 10 and 11 move the marks for real.

### Exercise 9.1

For each sentence of milestone 1's paragraph, name the line that makes it true.
If a sentence has no line, or a line serves no sentence, ask the agent to fix the queue and review the diff.

### Exercise 9.2

Bring one idea for the clinic that the brief of chapter 7 does not exclude, and ask the agent to add it: a line in the milestone where it belongs, or a new milestone with its paragraph.
Check the diff: one line, a new slug, `[ ]`, and no reasoning in the line.

### Exercise 9.3

Ask the agent to move `deploy` back to milestone 1, then read the paragraphs of both milestones.
What else had to change, and did the agent change it?

[^ninjobs]: Ninjobs, a private repository, its docs/06 at its last change, 2026-09-22, counted by the author: lines with `wc -l`, deliveries as the lines inside the code blocks that start with a mark, continuations as the other non-empty lines inside them.
