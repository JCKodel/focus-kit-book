# 25. Adoption in teams and companies

After this chapter you can take the method to a team or a company, answer the usual resistance with evidence, and give each role its part.
You can also run one milestone as a pilot that measures itself, and shape the pitch for your own company.

## The problem

In most teams each person already uses AI, each in their own way: one chats in a browser, one lets an agent edit the whole repository, one refuses to touch it.
Each pays their own cost, in tokens and in rework, and nobody sees it, because there is no shared standard to measure against.
When the team discusses it, the loudest opinion wins, and the [prologue](00-product-people-process.md) named that failure: opinion in place of evidence.

## The resistance, and its answer

Three objections come up in every team.
Each has an answer that asks for evidence rather than for faith.

**"My way works."**
It may.
The prologue's rule applies to it as to everything else: a claim carries its source.
Ask what it produced, measured how: how many deliveries, how many came back, what they cost.
A way that works can show it, and the method gives it the means to, with a page per delivery and a count of tokens per delivery ([chapter 24](24-cost-and-where.md)).

**"Too much process."**
The method has a governor for that ([chapter 18](18-the-governor.md)): every step must name the concrete error it would have caught, or it leaves.
What survives is six rules and two checks.
A team that finds a step that catches nothing removes it, and the method expects it to.

**"We already have a tool."**
The method is documents, and a tool is where you run them.
The documents, the queue and the pages are Markdown files in the repository, and any host that reads files can follow them ([chapter 11](11-install-and-hosts.md)).
The team keeps its host, its editor and its board.

## What the process caught on a real project

The strongest answer to "what would this have given us?" is a project that ran on it.
Case A, a client project on a low-code platform, ran on the method, and four of the things its process caught answer that question.

**The signed baseline did not match the build.**
The document the client had signed described something other than what had been built.
A question delivery, a queue line whose only purpose is a written answer, asked the client which of the two the acceptance would be measured against, and the answer came back in writing before any work depended on it.

**A request that could not be built was closed, not absorbed.**
One request had been accepted, and the work on it proved it technically impossible.
It was closed in the queue with the reason, without being built, where it could otherwise have been dropped in silence or bent into something nobody asked for.

**A clean install found what the development environment hid.**
An install on a clean environment failed on a permission that the development environment already had.
It became three lines in the queue and a fix in the installation guide.

**A secret was caught before it shipped.**
A secret sat in the package and would have shipped with it.
It was scrubbed first, and a scan was built so that the next package could not carry one.

None of the four is a bug in the code.
Each was caught because the work was written as lines and pages that a person read.

## Roles in a team

The method gives each step to whoever owns it.

* **Who proposes:** whoever owns the decision.
  A developer proposes a technical delivery, an analyst a rule, a manager a question to the client; `/propose` is a conversation, and it needs someone who can answer ([chapter 14](14-propose.md)).
* **Who applies:** a developer's session, or several at once in worktrees, each on its own delivery ([chapter 21](21-worktrees.md)).
* **Who commits and merges:** a person, always.
  `/apply` stages and stops; the commit is the human review ([chapter 15](15-apply.md)).
* **Who reviews the milestone:** the team, on the running product, against the milestone's paragraph ([chapter 17](17-closing-a-milestone.md)).
* **The manager** asks the project: what is pending, how it is going, who owes an answer ([chapter 19](19-project-as-assistant.md)).

## One milestone as the pilot

Do not adopt the method for a company in one decision.
Run it on one milestone of one project, and let the milestone decide.

1. Install the kit in an existing repository ([chapter 11](11-install-and-hosts.md)).
2. Run `/analyze`, so the documents describe what is already there, and review them ([chapter 12](12-starting-a-project.md)).
3. Write one milestone of three to eight lines, each a delivery the team needs anyway ([chapter 13](13-queue-and-milestones.md)).
4. Build it with `/propose` and `/apply`, one page per line.
5. Close it with its review ([chapter 17](17-closing-a-milestone.md)).

Measure two things: the tokens per delivery ([chapter 24](24-cost-and-where.md)), and what the review and the pages caught that would otherwise have shipped.
Then decide with those numbers on the table, and the next milestone becomes the comparison.

## The shape of a pitch

To take the method to a company, start from its problems, and map each one to the part of the method that answers it.
Case B, a consultancy's proposal for a client's adoption program, had an internal note that did exactly that.
In outline, and in my words, the mapping was this:

| The client's problem | The part of the method |
|---|---|
| Knowledge lives in a few heads | The documents |
| Scope is unclear | The page |
| Nobody sees how the work is going | The queue |
| Each person works their own way | The commands |

Use that shape for your own company: list its problems in its own words, and put beside each one the document, the command, the page or the queue that answers it.
A problem with nothing beside it is one the method does not solve, and saying so makes the rest credible.

The proposal itself did not run on the process.
It had no queue and no page, and [chapter 23](23-beyond-software.md) tells what that cost it.

## What the team gains

The whole team on one process, where each person knows which part is theirs and every decision is on a page anyone can read.
And a pilot that measures itself: one milestone gives a token count per delivery and a list of what was caught.
On Case A the process caught four problems outside the code: a baseline that did not match the build, an impossible request, a permission failure on a clean install, and a secret in the package.
There is no outside number to compare adoption against; the pilot's own milestone is the baseline.

## Key points

* Without a shared process each person uses AI their own way, at a cost nobody sees, and the loudest opinion decides.
* Answer "my way works" by asking for its evidence, "too much process" with the governor, and "we already have a tool" with the fact that the method is documents any host reads.
* On Case A the process caught a baseline that did not match the build, an impossible request, a failure hidden by the development environment, and a secret in the package.
* Whoever owns the decision proposes, a developer's session applies, a person always commits, and the team reviews the milestone.
* Start with one milestone of three to eight lines, measure tokens per delivery and what was caught, then decide.

