# 20. The team's tools: pull requests, issues and boards

After this chapter you can land a delivery through a pull request whose review reads the page before the diff, knowing who on the team is the reviewer the kit assumes and what it assumes of a teammate who does not read code, and keep issues and a board in step with the queue without making either of them the source of truth, refreshing the board through a slot of docs/05 rather than an edit to the commands.
You can also say why a project's documents live in docs/ and never in a wiki.

## The problem

The kit assumes one person who proposes a delivery, uses it and reviews it: by default the staged diff, before committing it, or, when the Git slot's word lets the agent commit, the commit, after it lands. The kit splits those roles no further; how a team splits them is the team's own practice.
A person who does not read code takes part in `/propose`, where the page is written in user language ([chapter 12](12-propose.md)), tests the delivery as its user ([chapter 13](13-apply.md)), and asks any session where things stand or what a page decided ([chapter 17](17-project-as-assistant.md)).
A team needs two more things: a second person who reviews before the merge, and a way for people who open neither the repository nor a session, a client or a manager, to see progress.
The git strategies of chapter 18 stop at the merge: they shape the history, and say nothing about who reviewed a change or who is watching the work.

## The pull request as the team's review

A pull request is a request, made on a code host such as GitHub, to merge one branch into another.
It gathers the description, the commits, the automated checks and the diff in one place, where reviewers comment and approve: in GitHub's words, "*A pull request brings together the context reviewers need to understand a change*".[^gh-prs]
GitLab calls the same thing a merge request.

With focus-kit, a pull request carries one delivery:

1. **A branch per delivery**, named by its slug.
2. **The page first.** The first commit on the branch is `work/<slug>.md`, written by `/propose`.
   Open the pull request as soon as it is pushed, and the page can be reviewed before any code exists.
3. **The build after.** `/apply` builds on the same branch; the page moves to `work/done/` and the queue line becomes `[x]` in the same change.
4. **One merge.** The delivery reaches the main branch whole, with its page, its code, its tests, its proof and its mark, so the queue on the main branch holds what has landed; a `[~]` or `[*]` set on a branch shows there only (chapter 14).

The reviewer reads the page, then the diff against it.
Every Behaviour line has its test or its manual check; the Contract matches the code down to the names; nothing listed in Out of scope was built; every item of Done when is ticked with its proof.
A change in the diff that the page does not ask for is the first finding, whatever its quality.

The first reviewer can be an agent: the host's own review command, or GitHub Copilot code review, which reads the repository's custom and agent instructions from the branch under review, so it knows the same rules as the agent that built the change.[^copilot-review]
GitHub's documentation gives the limit itself: "*Always validate Copilot's feedback carefully. Supplement Copilot's feedback with a human review.*"[^copilot-review]
The agent's review finds what a tired person skims; the person decides what is a finding, and approves the merge.
By default whoever merges is the reviewer the kit assumes: on a branch the merge is the delivery's one change, as the commit is on trunk; when the Git slot's word lets the agent merge, the reviewer is the person who reviews the merge after it lands.

## Issues

An issue is GitHub's record for "*ideas, feedback, tasks, or bugs*", opened on the web by anyone with access, including people outside the team.[^gh-issues]
That makes it a good door for a user's bug report.

A queue line may mirror an issue, and the slug names both: the issue's title starts with the slug, and the line ends with the issue's number.

```text
[ ] fix-due-date      due date one day early at the end of a month (#42)
```

The pull request says "Fixes #42", and GitHub closes the issue when it merges.[^gh-issues]
The queue stays the source of truth, because the agent reads the repository and never a web page: an issue with no line in the queue does not exist for `/propose`.
So an issue becomes a line by conversation, and from there it is a delivery like any other.

## Boards

A manager opens a board; they rarely open a repository.
A board whose cards are moved by hand, though, is a second queue, and it drifts from the first the day someone forgets to drag a card.

The answer is a mirror in one direction, from the queue to the board.
On Case A, a client project on a low-code platform, a customization recorded in its docs/05 did this: a script and a pipeline pushed the queue, one way, to the project's Azure DevOps kanban board, so the project manager followed progress in the portal without asking a developer.
`/propose` and `/apply` refreshed the board whenever they changed a mark, and said so whenever they could not, so a stale board was never silent.
A project gives its board this refresh with a slot of its own in docs/05 §5 that names `/propose`, `/apply` and the command that pushes the queue, as in the lending library's docs/05 of [chapter 7](07-the-documents.md); the commands follow it as they follow the kit's slots, with no edit to their files, which the kit's installation writes.
Since the push runs inside the command that changed the mark, the board shows the mark at once, on any branch the delivery is on.
With the kit's six marks, a mirror places each card by its line's mark, in the column where [chapter 14](14-queue-states.md) folds them onto a board's columns.
The mirror goes one way because the queue is the only place the agent reads: a card moved on the board changes nothing in the repository, and a sync in both directions would make two sources of truth.

### Question deliveries

Case A recorded one more customization: question deliveries, whose only output is a written answer from someone outside the project.
They close on the answer, not on the send, because a session once marked one done when the email went out.

## Why the wiki is not docs/

GitHub gives every repository a wiki, and it looks like the natural home for a project's documents.
It is a second repository, edited on the web, with no pull requests and no build.
The agent in the project's folder does not read it, and no delivery changes it, so it drifts from the code with the first delivery that forgets it.
docs/ changes in the same commit as the code it describes, and is reviewed in the same pull request.
This book took the same decision for itself: no wiki, written or mirrored; one source builds the website and the PDF.

## What the team gains

The manager sees progress without asking a developer, and the review reads a page before it reads a diff, so a change nobody asked for is found by the first question.
Case A's board ran on one project, and its write permission was never proven.

## Key points

* The kit assumes one person who proposes, uses and reviews, by default the staged diff before committing, or the commit the Git slot's word let the agent make, and a team splits those roles as its own practice; a teammate who does not read code takes part in `/propose`, tests the delivery as its user and asks a session where things stand or what a page decided, and a board serves those who open neither the repository nor a session.
* A pull request carries one delivery: a branch named by the slug, the page first, the build after, one merge with the page, the code and the mark; its reviewer reads the page, then the diff against it; an agent may review first, a person decides, and the reviewer the kit assumes is, by default, whoever merges, or, by the Git slot's word, the person who reviews the merge the agent made.
* An issue mirrors a queue line through the slug, and the queue stays the source of truth, because the agent reads the repository.
* A board is a one-way mirror of the queue, refreshed, when a mark changes, by a slot of docs/05 that the commands follow, not by an edit to them, and never silent when it cannot be.
* A question delivery, Case A's own customization, closes on the answer, not on the send.

[^gh-prs]: GitHub Docs, "Pull requests", section "Working with pull requests", accessed 2026-09-30. <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests>
[^copilot-review]: GitHub Docs, "About GitHub Copilot code review", sections "Agent skills" and "Validating Copilot code reviews", accessed 2026-09-30. <https://docs.github.com/en/copilot/concepts/agents/code-review>
[^gh-issues]: GitHub Docs, "About issues", accessed 2026-09-30. <https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues>
