# 8. Install, and the hosts

After this chapter you can install focus-kit in a repository with one sentence to your coding agent, update it with the same sentence, knowing what the update writes and what it only reports to you, and invoke its commands in the host you use.
You can also say why the method does not depend on the host.

## The problem

A method tied to one tool lasts as long as the team keeps that tool, and a team rarely agrees on one.
One person works in Claude Code, another in Copilot inside their editor, a third tries Codex, and each host, the program that runs the coding agent, looks for its rules and its commands in folders of its own.
The kit has to open ready in all of them, and install without asking anyone to install anything.

## Install

Open your coding agent at the root of the repository and say:

```
Read https://raw.githubusercontent.com/JCKodel/focus-kit/main/SETUP.md
and do what it says.
```

The address is the file itself, not the page GitHub draws around it, so the agent gets the whole text.
That file is the kit's setup file: one file of instructions that the agent reads and turns into the kit's files, the four commands and a few small pointer files for the hosts that need them.
Nothing is installed on your machine; the agent writes files into the repository, and that is all.
Your host may ask before it downloads the file and before it writes into its own folder inside the repository, `.claude/` in Claude Code: approve both.

The setup file tells the agent to copy every file byte for byte.
Some hosts fetch a web page through a tool that hands the agent a summary of the page instead of its text; if yours does, ask the agent to download the file and read it whole.

The install does not stage or commit.
By default you read what it wrote and then commit it, yourself or by asking the agent, as with every change the agent makes (chapter 13).

The agent ends a first install by naming what comes next: on a repository without code, open a fresh session and type `/brainstorm`; on a repository with code, open a fresh session and type `/analyze` (chapter 9).
It writes the command as your host invokes it, with no slug, since these two take none: in Codex, `$brainstorm` or `$analyze`, and Copilot asks for no slug.

## What the install never touches, and how to update

The setup file writes the kit's files and nothing else.
`docs/`, `work/`, `AGENTS.md` and `CLAUDE.md` belong to the project: the commands write them, starting with `/brainstorm` or `/analyze` (chapter 9), and the setup file never touches them.
A `GEMINI.md` that already holds the project's own text keeps it; the kit only adds one line at its top.

To update the kit, say the same sentence again.
The agent writes the kit's files as the setup file holds them now, and the change you review is the kit's alone, with nothing of your project in it.
It replaces a file only when that file matches one the kit shipped, in this version or an earlier one, and the earlier one is established from the kit's history, `git show <commit>:SETUP.md` in the kit's repository, or, without that history at hand, by your word that the file was never edited; a familiar name or a `metadata.version` line alone does not prove it.
A command of your own in a host's folder, or an edit you made by hand to one of the kit's files, a line you added to `.claude/skills/propose/SKILL.md` say, stops the update before it writes or removes any file.
The agent shows your edit as a diff against the kit file it was made on, and the kit's own change to that file since then apart and in short; it still reports the migrations and the next command, and you decide whether to keep your edit or replace it, knowing that a rule your edit added to a command can become a slot of docs/05 §5, which the commands follow (chapter 7).
This check was tried on a copy of the book's kit files, made outside the book's repository: a line appended to `.agents/skills/brainstorm/references/documents.md` stopped the update to focus-kit 2026.10.20.3 this way, and every file of the copy was unchanged afterwards.

## What an update reports

docs/04, docs/05, docs/06 and `AGENTS.md` belong to the project: the team wrote its rules there, its choices with them, such as the verify command or working on trunk, and its queue.
When a new kit version changes what those files should hold, the setup file does not write it.
It compares the files with its own templates and reports each migration, a change your documents still need: the path, the section or the line, and the wording it proposes, in the project's documentation language.
A migration may name a rule, a queue line or a slot.
Your choices stay: a docs/05 whose §5 says "trunk, one session at a time" sees the wording for two sessions in one folder proposed, and keeps its own until the team accepts the change.

Here is part of the report the update to focus-kit 2026.10.20.3 gave on this book's own repository, shortened and paraphrased from the record of that update, `work/done/kit-2026-10-20-3.md` in the book's repository:

```
Installed: focus-kit 2026.10.20.3, in every SKILL.md.
Pending process migrations, by document and section, shortened:

* docs/05, section numbers: match the template (§4 the queue,
  §5 the slots, §6 commit, §8 closing a milestone). None.
* docs/05 §2, /apply in a fresh session: lacks the subagent.
  Proposed: "/apply always starts in a fresh session, a subagent
  being one: it has only what the page says."
* docs/05 §4, a command typed with several slugs: lacks it.
  Proposed: the template's paragraph that closes §4, whole, which
  begins: "A command typed with several slugs opens one subagent per
  slug, each following the command's file with one slug, sent to the
  slug's worktree where §5's Git slot has one (/propose creates it)."
  On trunk, each subagent works in the one working tree.
* docs/05 §5, Git: a project choice, not a migration: trunk, ADR-0010,
  with the Publish policy, the agent never pushes. None.

The other items cover docs/05 §3, the other slots of §5, §§6 to 8,
docs/04, docs/06 and AGENTS.md.
Next: /propose ch08-update-2026-10-20-3, once kit-2026-10-20-3 is [x].
```

Each item names a document and a section, and ends in one of three outcomes.
It matches and needs nothing, and says so: `None`.
It lacks something, and the item gives the wording the template proposes and where it goes, as for docs/05 §2 and §4.
Or it differs by a choice the project made and recorded with a date or an ADR, as the book's Git slot does: the item names that choice and asks for no change.
Every item is reported, never done: the update writes none of these documents.

Section numbers come first because the commands cite docs/05 by the template's numbers, §4 for the queue, §6 for the commit, and read by number; a docs/05 numbered otherwise would send every command to the wrong section, so that migration comes before any other, whatever an ADR says.
Applying the migrations keeps the team's choices: verify stays `make verify` with its checks, the reviewer stays the one the slot names, Git stays trunk, and the Milestone review keeps the kit's readers.

The report gives each item one of those three outcomes; it compares the documents with the current templates, never one version of the kit with another.

The kit's version is the `metadata.version` in each `SKILL.md`; the process is what docs/04, docs/05 and `AGENTS.md` say, because every command reads them, so an updated kit whose migrations are not applied still runs the old process.
The update is done when the migrations are applied, as any change is: a queue line, defined with `/propose` and built with `/apply`, so the change to your rules or your queue gets a page, verify and your review.
Applying them can need an edit no item names, when a migration's wording contradicts a sentence the report does not check: on the book's repository at 2026.10.20.3, docs/05 §7 admitted no specialized subagent beyond the reviews' readers and checker, which the §4 paragraph the report proposed, on a command typed with several slugs, contradicted, so the line that applied §2 and §4 edited §7 too, and §7 now admits a command's one subagent per slug with the reviews' readers and checker.

On a documented project the update reports the migrations first, or says there are none.
It never asks you to run `/brainstorm` or `/analyze` again: those write a project's documents from nothing, and yours exist.
It names instead the command docs/06's first free line wants, in your host's form: `/propose` and its slug for a `[ ]` line, `/apply` and its slug for a `[>]` one.
On trunk that line is read in the queue of the folder; with a branch or a worktree per delivery the main branch shows each line as it was until its merge, so the update runs `git fetch` first, counts a line whose branch exists as taken even before any of its marks is pushed, whatever the main branch shows, and reads each slug's line from its branch, local or remote, and the lines only a branch has, reconciling them by slug ([chapter 14](14-queue-states.md)).
A version that asks nothing of your documents reports no migration: a version that changes only the commands, such as `/apply` showing its commit message in the conversation too, changes nothing else.
A check that concerns a choice the project did not make asks nothing of it either: the manual letting a session in `main/` edit the worktrees is asked of a worktree Git slot, not of a trunk project such as the book's.
A docs/05 whose Git slot chose a worktree per delivery and names no folder has a folder proposed only when the project already works in a container, the folder [chapter 19](19-worktrees.md) lays out with the checkout and a hidden folder for the history and the worktrees, and that hidden folder holds `repo.git/`.
The report then proposes writing in that folder's name and the prefix the delivery branches already use, so nothing moves.
With no container yet, the slot means the kit's default, which that chapter names, and the report proposes no folder.
Whatever the folder, a worktree Git slot whose project has no manual letting a session in `main/`, where `/propose` runs, edit the worktrees is reported as lacking it.

To know why a migration exists, read the kit's changelog, `CHANGELOG.md` in its repository, `CHANGELOG.pt.md` in Portuguese.
It has one entry per version, newest first; the version is the `Version:` line of `SETUP.md`, the same value as the `metadata.version` in each `SKILL.md`.
Each entry says what changed and the problem that caused it, and an entry may carry an item that starts with `Migration:`, naming what to change in the project's documents.
What a rerun compares is the setup file's own step 4, a list by document and section, which names the sections of docs/05, the slots and the lines of `AGENTS.md` it checks; each item is reported, never done, with one of the three outcomes.

## How each host finds the commands

A host needs two things from the repository: the rules file, `AGENTS.md`, and the commands, `/propose` and `/apply` each with the slug you type after it, the name of the delivery in `work/<slug>.md` (chapter 12).
`/brainstorm` and `/analyze` start a project, not a delivery, so they take no slug; to define or build `lend-book`, you type `/propose lend-book` or `/apply lend-book`, or, where the host asks for the slug, you answer `lend-book`.
The setup file writes what every host below needs:

| Host | Reads the rules from | Reads the commands from | You type |
|---|---|---|---|
| Claude Code | `CLAUDE.md`, which imports `AGENTS.md`; `AGENTS.md` alone only where no `CLAUDE.md` exists, from version 2.1.277 | `.claude/skills/` | `/propose <slug>` |
| Codex | `AGENTS.md` | `.agents/skills/` | `$propose <slug>` |
| GitHub Copilot | `AGENTS.md` | `.agents/skills/`, through a prompt file in `.github/prompts/` | `/propose`, and it asks for the slug |
| Cursor | `AGENTS.md` | `.agents/skills/`, through a command file in `.cursor/commands/` | `/propose` |
| Gemini CLI | `AGENTS.md`, through `GEMINI.md` | `.agents/skills/`, through a command file in `.gemini/commands/` | `/propose <slug>` |
| Google Antigravity | `AGENTS.md` directly; `.agents/rules/focus-kit.md` is an always-on pointer | `.agents/skills/` | `/propose <slug>` |
| Devin Desktop, formerly Windsurf | `AGENTS.md` | `.agents/skills/` | `/propose` |
| OpenCode, Zed | `AGENTS.md` | `.agents/skills/` | by asking for the skill |
| Jules, Junie, Warp, Kiro, Roo Code, Cline | `AGENTS.md` | none | by asking in words for `.agents/skills/propose/SKILL.md` |

Each command is a skill, a folder with a `SKILL.md` file of instructions the host loads when you invoke it.[^claude-code-skills][^codex-skills][^copilot-skills]
Claude Code reads `CLAUDE.md` at the start of a session, and a line `@AGENTS.md` in it imports the rules file; from version 2.1.277 it reads `AGENTS.md` alone, but only in a repository with no `CLAUDE.md`, so the kit writes `CLAUDE.md` with the import, which every version reads.[^claude-code-memory]
Codex, Copilot and Devin Desktop, formerly Windsurf, read `AGENTS.md` on their own.[^codex-agents-md][^copilot-instructions][^devin-rules]
Antigravity reads `AGENTS.md` directly too; the rule the kit writes in `.agents/rules/focus-kit.md` is a pointer that is always on and holds no rule of its own, an extra path to `AGENTS.md`, not the only one.
Copilot's slash command comes from a prompt file that only tells the agent to read the skill and follow it, and asks you for the slug when you type the command.[^copilot-prompt-files]
Codex may run a skill on its own when a message matches its description; a small file beside each skill turns that off, so a message that happens to say "apply" builds nothing you did not ask for.[^codex-skills]
Claude Code's skills carry `disable-model-invocation: true`, which keeps Claude from running one on its own: a message that matches a skill's description is not enough, and the command runs only when you name it.[^claude-code-skills]
On the other hosts, invoke the commands yourself; the kit does not claim that each host enforces the same.
For Cursor and Devin Desktop, neither vendor's documentation says whether a slug typed after a command reaches it, so name the delivery in your message if it does not.
Copilot reads both skills folders, and its CLI reference says what happens to a skill with the same name in both: `.agents/skills/` comes before `.claude/skills/` and the first found wins; the kit writes the same file in both, so either copy is the same command.[^copilot-cli-reference]
Devin Desktop also reads `.windsurf/skills/`, the folder of its former name;[^devin-skills] the setup file writes nothing there and, on an update, removes the kit's own files from it, so the host never finds an older copy of a command beside the current one in `.agents/skills/`, and a file of yours there is reported and left.

Every command ends by naming the next one, written as the host running it invokes it, the table's last column.
The setup file names `/brainstorm` or `/analyze`, to run in a fresh session, `/propose` names `/apply` with the page's slug, and `/apply` names the queue's next line.
On the lending library, after `/propose lend-book`, Claude Code tells you to run `/apply lend-book` in a fresh session, and Codex tells you to run `$apply lend-book`, in a fresh session too.
`/propose` may run in the conversation that asked for the change; `/apply` always starts in a fresh session, in every host (chapter 11).
The kit's files are the same in both; the form follows the host that runs them.

The kit's setup file keeps this table current, with the vendor page each row was read from, and adds a host only with its documentation in hand.
The last row comes from §1 of the setup file: Jules, Junie, Warp, Kiro, Roo Code and Cline read `AGENTS.md`, and the kit relies on no skills folder and no slash command of theirs, so you ask in words, "read `.agents/skills/propose/SKILL.md` and follow it for `lend-book`", and the host reads the file you point it at.

## Why the method does not depend on the host

The hosts differ in folders and in the character that starts a command, and they share three facts.
Each reads a rules file at the start of a session, `AGENTS.md` directly or through a pointer.
Each reads the files you point it at.
Each can write files.

The method needs nothing more.
It lives in plain files: the rules file, the project documents a fresh session reads, the pages in `work/` and the commands, which only say which documents to read and what never to do.
The setup file writes every host's files, whichever host runs it, so the repository opens ready in any of them, and a person who switches hosts finds the same documents, the same queue and the same commands.

## What the team gains

One repository opens ready in any host, so each person keeps the host they prefer and the team still shares one process, and switching hosts changes nothing in the project.

An update never rewrites the rules the team wrote.
A version that asks for a change in the project's documents reaches the project as a list of what to change and where, with the team's own rules still in place, and the team applies it as it applies any change.
An edit the team made to a kit file is shown apart from the kit's own change, so the team can tell which is which, and a choice it recorded is reported as its own.

And the next command arrives in the form your host recognizes, because a host may not recognize another's form: Codex does not recognize `/propose`, since Codex invokes skills with `$`.

## Key points

* One sentence to your agent installs focus-kit, and the same sentence updates it; nothing is installed on your machine, nothing is staged or committed, and a kit file you changed stops the update before it writes, with your edit shown as a diff against the kit file it was made on.
* The setup file writes only the kit's files and never touches `docs/`, `work/`, `AGENTS.md` or `CLAUDE.md`; a change docs/04, docs/05, docs/06 or `AGENTS.md` needs, a rule, a queue line or a slot, comes as a migration in its report, a list by document and section where a choice the project recorded is reported as that choice, and until the team applies it as a delivery the process is the old one.
* The kit's changelog, newest first, says for each version what changed, the problem that caused it, and, in an item that starts with `Migration:` when the entry has one, what to change in the project's documents.
* Each host finds the rules and the commands in its own folders: Claude Code runs a command as `/propose <slug>`, Codex as `$propose <slug>`, Copilot as `/propose`, which asks for the slug, Devin Desktop as `/propose`, and Jules, Junie, Warp, Kiro, Roo Code and Cline by asking in words for the skill's file; `/brainstorm` and `/analyze` take no slug; every command names the next one in that form; Copilot takes a skill from `.agents/skills/` before `.claude/skills/`, the same file in both.
* Every host reads a rules file at the start, reads the files you point it at and writes files, and the method needs nothing more.

[^claude-code-memory]: Anthropic, "How Claude remembers your project", Claude Code documentation, accessed 2026-10-18. <https://code.claude.com/docs/en/memory>
[^claude-code-skills]: Anthropic, "Extend Claude with skills", Claude Code documentation, accessed 2026-10-18. <https://code.claude.com/docs/en/skills>
[^codex-agents-md]: OpenAI, "Custom instructions with AGENTS.md", Codex documentation, accessed 2026-09-30. <https://developers.openai.com/codex/guides/agents-md>
[^codex-skills]: OpenAI, "Build skills", Codex documentation, accessed 2026-09-30. <https://developers.openai.com/codex/skills>
[^copilot-instructions]: GitHub, "Adding repository custom instructions for GitHub Copilot", GitHub Docs, accessed 2026-09-30. <https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions>
[^copilot-skills]: GitHub, "About agent skills", GitHub Docs, accessed 2026-09-30. <https://docs.github.com/en/copilot/concepts/agents/about-agent-skills>
[^copilot-cli-reference]: GitHub, "GitHub Copilot CLI command reference", GitHub Docs, accessed 2026-10-19. <https://docs.github.com/en/copilot/reference/cli-command-reference>
[^copilot-prompt-files]: GitHub, "Your first prompt file", GitHub Docs, accessed 2026-09-30. <https://docs.github.com/en/copilot/tutorials/customization-library/prompt-files/your-first-prompt-file>
[^devin-skills]: Cognition, "Skills Overview", Devin Docs, accessed 2026-10-17. <https://docs.devin.ai/cli/extensibility/skills/overview>
[^devin-rules]: Cognition, "Rules & AGENTS.md", Devin Docs, accessed 2026-10-17. <https://docs.devin.ai/cli/extensibility/rules>
