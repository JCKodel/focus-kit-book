# The team's tools: pull requests, issues and boards

After this chapter you can land a delivery through a pull request whose review reads the page before the diff, and keep issues and a board in step with the queue without making either of them the source of truth.
You can also say why a project's documents live in docs/ and never in a wiki.

## The problem

One person working on trunk reviews the staged change and commits it (chapter 15).
A team needs two more things: a second person who reviews before the merge, and a way for people who never open the repository, a manager or a client, to see progress.
The git strategies of chapter 19 stop at the merge: they shape the history, and say nothing about who reviewed a change or who is watching the work.

## The pull request as the team's review

A pull request is a request, made on a code host such as GitHub, to merge one branch into another.
It gathers the description, the commits, the automated checks and the diff in one place, where reviewers comment and approve: in GitHub's words, "*A pull request brings together the context reviewers need to understand a change*".[^gh-prs]
GitLab calls the same thing a merge request.

With focus-kit, a pull request carries one delivery:

1. **A branch per delivery**, named by its slug (chapter 19).
2. **The page first.** The first commit on the branch is `work/<slug>.md`, written by `/propose`.
   Open the pull request as soon as it is pushed, and the page can be reviewed before any code exists (chapter 14).
3. **The build after.** `/apply` builds on the same branch; the page moves to `work/done/` and the queue line becomes `[x]` in the same change.
4. **One merge.** The delivery reaches the main branch whole, with its page, its code, its tests, its proof and its mark, so the queue on the main branch is always true.

The reviewer reads the page, then the diff against it.
Every Behaviour line has its test or its manual check; the Contract matches the code down to the names; nothing listed in Out of scope was built; every item of Done when is ticked with its proof.
A change in the diff that the page does not ask for is the first finding, whatever its quality.

The first reviewer can be an agent: the host's own review command, or GitHub Copilot code review, which reads the repository's custom and agent instructions from the branch under review, so it knows the same rules as the agent that built the change.[^copilot-review]
GitHub's documentation gives the limit itself: "*Always validate Copilot's feedback carefully. Supplement Copilot's feedback with a human review.*"[^copilot-review]
The agent's review finds what a tired person skims; the person decides what is a finding, and approves the merge.

## Issues

An issue is GitHub's record for "*ideas, feedback, tasks, or bugs*", opened on the web by anyone with access, including people outside the team.[^gh-issues]
That makes it a good door for a user's bug report.

A queue line may mirror an issue, and the slug names both: the issue's title starts with the slug, and the line ends with the issue's number.

```text
[ ] fix-due-date      due date one day early at the end of a month (#42)
```

The pull request says "Fixes #42", and GitHub closes the issue when it merges.[^gh-issues]
The queue stays the source of truth, because the agent reads the repository and never a web page: an issue with no line in the queue does not exist for `/propose`.
So an issue becomes a line by conversation (chapter 13), and from there it is a delivery like any other.

## Boards

A board shows work as cards in columns, one column per stage.
Azure DevOps, Microsoft's product for planning and building software, describes its kanban board this way: "*team members drag cards across columns to update status*".[^azure-kanban]
A manager opens a board; they rarely open a repository.
A board whose cards are moved by hand, though, is a second queue, and it drifts from the first the day someone forgets to drag a card.

The answer is a mirror in one direction, from the queue to the board.
On Case A, a client project on a low-code platform, a customization recorded in its docs/05 did this: a script and a pipeline pushed the queue, one way, to the project's Azure DevOps kanban board, so the project manager followed progress in the portal without asking a developer.
`/propose` and `/apply` refreshed the board whenever they changed a mark, and said so whenever they could not, so a stale board was never silent.
The mirror goes one way because the queue is the only place the agent reads: a card moved on the board changes nothing in the repository, and a sync in both directions would make two sources of truth.
One piece was still unproven when the project closed: the write permission of the pipeline's identity on the board.

### A mark for waiting

Case A's queue also lacked a word.
The mark `[>]` reads as "defined, waiting to be built", and five lines blocked on the client showed as work nobody had started.
Case A added a fourth mark to its queue, `[?]`, "waiting on a person".
Its question deliveries, whose only output is a written answer from someone outside the project, close on the answer, not on the send, because a session once marked one done when the email went out.

`[?]` is Case A's mark, never the kit's.
This book rejected it for itself: its only outside answer is the author's approval of the private cases' text, and that is a line of a chapter page's Done when, so none of its lines ever waits on a person.
The governor of chapter 17 decides per project, with its one question, which concrete error would the mark have caught: on Case A, five lines read as idle; here, none.

## Why the wiki is not docs/

GitHub gives every repository a wiki, and it looks like the natural home for a project's documents.
It is a second repository, edited on the web, with no pull requests and no build.
The agent in the project's folder does not read it, and no delivery changes it, so it drifts from the code with the first delivery that forgets it.
docs/ changes in the same commit as the code it describes, and is reviewed in the same pull request.
This book took the same decision for itself: no wiki, written or mirrored; one source builds the website and the PDF.

## What the team gains

The manager sees progress without asking a developer, and the review reads a page before it reads a diff, so a change nobody asked for is found by the first question.
There is no measured number for this gain: Case A's board ran on one project, and its write permission was never proven.

## Key points

* A pull request carries one delivery: a branch named by the slug, the page first, the build after, one merge with the page, the code and the mark.
* The reviewer reads the page, then the diff against it; an agent may review first, and a person decides.
* An issue mirrors a queue line through the slug, and the queue stays the source of truth, because the agent reads the repository.
* A board is a one-way mirror of the queue, refreshed when a mark changes, and never silent when it cannot be.
* `[?]` was Case A's mark for lines waiting on a person; the governor decides per project, and this book did not need it.

[^gh-prs]: GitHub Docs, "Pull requests", section "Working with pull requests", accessed 2026-09-30. <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests>
[^copilot-review]: GitHub Docs, "About GitHub Copilot code review", sections "Agent skills" and "Validating Copilot code reviews", accessed 2026-09-30. <https://docs.github.com/en/copilot/concepts/agents/code-review>
[^gh-issues]: GitHub Docs, "About issues", accessed 2026-09-30. <https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues>
[^azure-kanban]: Microsoft Learn, "About Kanban boards", Azure Boards, accessed 2026-09-30. <https://learn.microsoft.com/en-us/azure/devops/boards/boards/kanban-overview>
