# 10. From zero to the first delivery

After this chapter you can take a project, new or with code already in it, from an empty session of your host to its first delivery committed, step by step.
Each step says what to type or do, what you see when it worked, and the one chapter that teaches it, so you can follow it with no other chapter open.

## Before you start

You need a git repository, empty or with code, and a host from [chapter 8](08-install-and-hosts.md)'s table, the program that runs your coding agent.
The kit is installed with the one sentence that chapter gives, said to your agent at the root of the repository:

```
Read https://raw.githubusercontent.com/JCKodel/focus-kit/main/SETUP.md
and do what it says.
```

The steps are written for Claude Code.
In another host, a command takes the form of chapter 8's table:

| Host | You type |
|---|---|
| Claude Code | `/propose <slug>` |
| Codex | `$propose <slug>` |
| GitHub Copilot in VS Code | `/propose`, and it asks for the slug |
| GitHub Copilot CLI | `/propose` |
| Cursor | `/propose` |
| Gemini CLI | `/propose <slug>` |
| Google Antigravity | `/propose <slug>` |
| Devin Desktop, formerly Windsurf | `/propose` |
| OpenCode, Zed | by asking for the skill |
| Jules, Junie, Warp, Kiro, Roo Code, Cline | by asking in words for `.agents/skills/propose/SKILL.md` |

`/apply` takes the same form as `/propose`, with the slug of the delivery after it, or as the answer when the host asks for it, or, where neither works, in your message; `/brainstorm` and `/analyze` take it with no slug, `$brainstorm` in Codex.
In Claude Code, the GitHub Copilot CLI and Codex a command runs only when you name it: a message that happens to match what it does starts nothing.

One choice is yours before the first `/propose`: the git strategy, trunk, a branch per delivery or a worktree per delivery.
`/brainstorm` and `/analyze` ask it with a default and write your answer into docs/05: trunk for one person, and on a project with code, what the repository already does.
[Chapter 18](18-git-essentials.md) and [chapter 19](19-worktrees.md) teach the three; the steps below assume trunk.

## A new project

1. Open Claude Code at the root of the empty repository and say the sentence above.
   You see the kit's four commands in `.claude/skills/`, nothing staged or committed, and the agent naming `/brainstorm` as the next step, in a fresh session.
   Taught in [chapter 8](08-install-and-hosts.md), "Install".
2. Open a fresh session, not the one that ran the install, and type `/brainstorm`, then answer its questions, one subject at a time; "your call" keeps the agent's default.
   You see docs/00 to 06, `docs/adr/`, `AGENTS.md`, `CLAUDE.md` and `work/done/` written, the queue shown, and the agent naming `/propose <slug>` for the queue's first line.
   Taught in [chapter 9](09-starting-a-project.md), "`/brainstorm`: a new project".
3. Read the documents against chapter 9's checklist and ask the agent for every fix in the same session.
   Then stage by name only the files the install reported writing and the ones `/brainstorm` wrote; never `git add -A`, `git add .` or a whole folder such as `.claude/`, which would also take a note or an edit of yours lying beside them.
   A part of that list, to complete from the install's report and the files `/brainstorm` wrote, not to copy as it stands:

   ```
   git add AGENTS.md CLAUDE.md work/done/.gitkeep
   git add .claude/skills/propose/SKILL.md
   ```

   Read what is staged with `git diff --staged`, as step 7 does: a file neither the install nor `/brainstorm` wrote is not this commit's, even one staged before you began, and naming paths does not take it out; find out whose it is, and take it out with `git rm --cached <path>` once you know it can wait for its own commit, which leaves the file on disk; `git restore --staged`, which chapter 19 uses, needs a first commit to exist.
   Then `git commit -m "Add the kit and the documents from /brainstorm"`, a message written for this chapter, a subject alone, since there is no page yet for its last line.
   You see one commit in `git log` holding the documents, `AGENTS.md`, `CLAUDE.md` and the kit's files in the host's folders, and nothing else; from here, your docs/05 owns the format of every message.
   Taught in [chapter 9](09-starting-a-project.md), "Review before you commit".
4. In a fresh session, type `/propose <slug>`, with the slug of the queue's first line, and answer what the documents leave open.
   You see `work/<slug>.md` written, its line in docs/06 marked `[>]`, and the agent asking you to read the page, then to run `/apply <slug>` in a fresh session.
   Taught in [chapter 12](12-propose.md), "What `/propose` does".
5. Read the page with chapter 12's questions, and ask the agent for every correction in that same session.
   You see a page whose every Behaviour line can be checked, whose Out of scope names what you assumed was in, and no question left open.
   Taught in [chapter 12](12-propose.md), "Read the page before `/apply`".
6. Open a fresh session, never the one that ran `/propose`, because the page must stand alone, and type `/apply <slug>`.
   You see verify green, the page moved to `work/done/`, its line marked `[x]`, the delivery staged, the suggested message in a `commit` block, on the page and in the conversation, and your next steps, starting with using what the delivery changed; when the delivery is the first after which a person can run the product, such as the skeleton, also the manual of running it in `docs/manuals/`.
   Taught in [chapter 13](13-apply.md), "What `/apply` does".
7. Use what the delivery built as its user would, in the environment `/apply`'s last sentence names: for chapter 12's `lend-book`, lend a copy and try each refusal its page lists; for a document, open what it renders and read it, with no screen to invent.
   Then read the staged change with `git diff --staged` against the page, and ask the agent for every correction in the same session.
   You see the delivery do what its page says, only this delivery staged, every Behaviour line answered, and a message whose last line is `work/done/<slug>.md`.
   Taught in [chapter 13](13-apply.md), "Review the staged change".
8. Type `git commit` and paste the message from the `commit` block at the end of the page.
   You see one new commit in `git log`, holding the page in `work/done/` and its build.
   Taught in [chapter 13](13-apply.md), "The commit is the human review".

A project left after step 3 is ready for the kit: any later session reads its documents and starts at step 4.

## An existing project

1. Install as in the new project's step 1, at the root of the repository with code.
   You see the same kit files, no file of your code changed, and the agent naming `/analyze` as the next step, in a fresh session.
   Taught in [chapter 8](08-install-and-hosts.md), "What the install never touches, and how to update".
2. Put what the code cannot say in a folder `context/` at the root, as it is: proposals, contracts, emails, meeting transcripts, tickets.
   You see one folder beside the code, with nothing sorted or summarized.
   Taught in [chapter 17](17-project-as-assistant.md), "The context folder".
3. Open a fresh session, not the one that ran the install, and type `/analyze`, then answer its one round; each default is what the code already does.
   You see the change shown before it is written, then the documents of the new project's step 2, the manual of running the product from a fresh clone and one for each thing a person already does by hand, in `docs/manuals/`, every inferred statement marked observed, and the agent naming `/propose <slug>`.
   Taught in [chapter 9](09-starting-a-project.md), "`/analyze`: an existing project".
4. Check every observed statement against the code, opening the file it names, then review and commit them as in the new project's step 3, staging by name only what the install and `/analyze` wrote, from a tree with no change of yours, with `/analyze` in the message.
   You see one commit holding the documents, `AGENTS.md`, `CLAUDE.md` and the kit's files in the host's folders, and none of your code.
   Taught in [chapter 9](09-starting-a-project.md), "Review before you commit".
5. In a fresh session, type `/propose <slug>` for the queue's first line: with code already there, there is no skeleton to build, so it is the smallest change the first milestone needs.
   You see a page whose Done when runs the verify command `/analyze` observed, and the agent asking you to read it.
   Taught in [chapter 12](12-propose.md), "What `/propose` does".

From there, follow steps 5 to 8 of the new project, unchanged.

The tests and CI already there are the verify command, or part of it, as `/analyze` recorded them in docs/05.
The backlog already there is read into the first milestone by `/analyze`, three to eight lines, and the rest waits in its tool.
Nothing else in the repository changes until a delivery touches it.

## The loop after the first delivery

The next delivery is the queue's first free line ([chapter 11](11-queue-and-milestones.md)).
Each delivery is a page, a build and a commit, steps 4 to 8 of the new project.
A milestone closes with its review, its last line, a delivery like the others ([chapter 15](15-closing-a-milestone.md)).

## When to stop a pilot

A pilot, one milestone run on the method to see whether it pays ([chapter 23](23-adoption.md)), is not paying when one of three signs shows:

* the pages are written and nobody reads them before `/apply`;
* the queue is not the plan the team follows;
* "done" is still said without verify green.

When it stops, the documents stay: they are the project's documentation either way.

## What the team gains

Anyone on the team, developer or not, goes from an empty session to a first delivery committed by one list, each step one link from its reason.

## Key points

* Before the first `/propose` you need a repository, a host, the kit installed with one sentence, and an answer to the git question; trunk fits one person.
* A new project: install, `/brainstorm` in a fresh session, review and commit the documents, `/propose` the first line, read the page, `/apply` in a fresh session, use what it built, read the staged change, commit.
* An existing project: `context/` first, then `/analyze` in a fresh session, every observed statement checked against the code; the first delivery is the smallest change the first milestone needs, checked by the verify command `/analyze` observed.
* The documents are the project's first commit, and a project stopped there is ready for any later session.
* A pilot stops when the pages go unread, the queue is not the plan or "done" is said without verify; the documents stay.
