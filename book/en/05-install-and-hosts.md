# Install, and the hosts

After this chapter you can install focus-kit in a repository with one sentence to your coding agent, update it by saying the same sentence again, and invoke its four commands in Claude Code, Codex or GitHub Copilot.
You can also explain why the method does not depend on the host.

## Install

Open your coding agent at the root of the repository and say:

```
Read https://raw.githubusercontent.com/JCKodel/focus-kit/main/SETUP.md and do what it says.
```

`SETUP.md` is focus-kit's setup file: one file of instructions that the agent reads and turns into the kit's files.[^focus-kit-setup]
If you prefer to read it first, download `SETUP.md` next to the repository and point the agent at the file.
Nothing is installed on your machine: the agent writes files into the repository, and that is all.

Your host asks before it downloads the file and before it writes into its own settings folder, `.claude/` in Claude Code: approve both.
A host's web fetch tool may hand the agent a summary of a page and not its text, and the setup file says every file must be copied byte for byte, so a careful agent asks to download the file instead; when I ran it, Claude Code did exactly that.[^claude-code-run]

The run this chapter shows was on the guided project, the scheduling app of a small clinic that you build through the rest of the book, in its public repository `JCKodel/focus-kit-clinic`.
Each chapter that changes it ends with a chapter tag, `book-v1/<chapter-slug>`, on the commit it quotes, so you can open the project as it was at any chapter.
The run started from the tag `book-v1/start`, where the repository holds three files: `README.md`, `LICENSE` and `LICENSE-TEXT`.
Claude Code read the setup file, wrote the files, and reported:[^claude-code-run]

```markdown
I've installed the focus-kit. I wrote all 36 files that SETUP.md lists, copying each one straight out of SETUP.md with a script. Where a file has a `<name>` placeholder, it was replaced with the command's name. I didn't touch any existing files and didn't stage or commit anything.

**Files written:**
- **Skills (18 files):** in each of `.claude/skills/`, `.agents/skills/` and `.windsurf/skills/`, there's a `SKILL.md` for `brainstorm`, `analyze`, `propose` and `apply`, plus `references/documents.md` under `brainstorm` and `analyze`.
- **Codex:** `.agents/skills/{brainstorm,analyze,propose,apply}/agents/openai.yaml`
- **Copilot:** `.github/prompts/{brainstorm,analyze,propose,apply}.prompt.md`
- **Cursor:** `.cursor/commands/{brainstorm,analyze,propose,apply}.md`
- **Gemini CLI:** `.gemini/commands/{brainstorm,analyze,propose,apply}.toml`, plus `GEMINI.md` (none existed before, so I created it)
- **Antigravity:** `.agents/rules/focus-kit.md`

I ran the checks from section 4 of SETUP.md, and they all pass. The file count is right, the only changes are the new files, and every `propose` and `apply` skill still contains `$ARGUMENTS`. There are no em dashes and no leftover `<name>` placeholders.

**Next step:** this repository has no code yet (just the README and licenses), so start a fresh session and run `/brainstorm`.
```

The report names every file it wrote, confirms the setup file's own checks, and ends with the next command: `/brainstorm`, because the repository has no code yet (a repository with code gets `/analyze`).

Then `git status --short` showed what appeared:[^claude-code-run]

```
?? .agents/
?? .claude/
?? .cursor/
?? .gemini/
?? .github/
?? .windsurf/
?? GEMINI.md
```

These lines hold 36 files (`git status --short --untracked-files=all` lists them one by one): the four commands once in each skills folder, `.claude/skills/`, `.agents/skills/` and `.windsurf/skills/`, and small pointer files for the hosts that need them.[^focus-kit-setup]
Every file came out of the setup file byte for byte.[^claude-code-run]
The install does not stage or commit; you review the files and commit them yourself.

## What the install never touches, and how to update

Running the setup file again replaces the kit's files and nothing else.[^focus-kit-setup]
`docs/`, `work/`, `AGENTS.md` and `CLAUDE.md` are the project's: the commands write them, and the setup file never touches them.
In the clinic, none of them exists yet; chapter 7 writes them.

To update the kit, say the same sentence again.
The agent writes the kit's files as the setup file holds them now, and `git diff` shows you what changed in the kit and nothing of your project.

## How a host finds the commands

Chapter 2 showed the rules file, `AGENTS.md`, which a host loads when a session starts.
A host also needs to find the commands, and to hand each one the slug you type after it: the name of the delivery, the `<slug>` of `work/<slug>.md`.
Each host below does it from files in the repository.

**Claude Code** reads `AGENTS.md` on its own; where it cannot, a `CLAUDE.md` holding the line `@AGENTS.md` imports it, and chapter 7 writes that file.[^claude-code-memory]
It reads a command from `.claude/skills/<name>/SKILL.md`.
You type `/propose <slug>`, and the slug reaches the command as `$ARGUMENTS`.[^claude-code-skills]

**Codex** reads `AGENTS.md` before doing any work.[^codex-agents-md]
It reads a command from `.agents/skills/<name>/SKILL.md`, and you type `$propose <slug>`.[^codex-skills]
Codex may also run a skill on its own when your message matches the skill's description; the `agents/openai.yaml` beside each skill turns that off, so a message that happens to say "apply" builds nothing you did not ask for.[^codex-skills]

**GitHub Copilot** reads `AGENTS.md` as its agent instructions.[^copilot-instructions]
It reads the kit's skills in `.agents/skills/`.[^copilot-skills]
The slash command comes from a prompt file, `.github/prompts/<name>.prompt.md`, which in the clinic only points to the skill, [`.github/prompts/propose.prompt.md`](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/install-and-hosts/.github/prompts/propose.prompt.md):

```markdown
---
agent: 'agent'
---
Read `.agents/skills/propose/SKILL.md` and follow it. `$ARGUMENTS` is `${input:slug}`.
```

You type `/propose`, and Copilot asks you for the slug, which `${input:slug}` stands for.[^copilot-prompt-files]
Prompt files work in VS Code, Visual Studio and JetBrains IDEs.[^copilot-prompt-files]

Cursor, Gemini CLI, Google Antigravity, Windsurf and others are in the table of [`SETUP.md` §1](https://github.com/JCKodel/focus-kit/blob/main/SETUP.md#1-what-to-do), with the vendor page each row was read from; the kit keeps that table current, and this book does not repeat it.

## Why the method does not depend on the host

The hosts differ in folders and in the character that starts a command, and they agree on three facts.
Each reads a rules file when a session starts, `AGENTS.md` directly or through a pointer; each loads a command from a file in the repository; and each hands the command the word you type after it.
The method lives in plain files, the rules file of chapter 2 and the project documents a fresh session reads, so switching hosts changes nothing in it.
Every install writes every host's files, whichever host ran it, so the repository opens ready in any of them.[^focus-kit-setup]

The kit also offers the FOCUS architecture and a git strategy, and imposes neither; Parts III and IV teach them.

## Key points

* One sentence to your agent installs focus-kit, and the same sentence updates it; nothing is installed on your machine.
* The install writes 36 files, the four commands once in each skills folder and pointer files for other hosts, and never touches `docs/`, `work/`, `AGENTS.md` or `CLAUDE.md`.
* Claude Code runs a command as `/propose <slug>`, Codex as `$propose <slug>`, and Copilot as `/propose`, which asks for the slug.
* Every host reads a rules file at session start, loads commands from files in the repository, and passes on the word typed after a command, so the method works the same in any of them.
* Other hosts are in the setup file's table, which the kit keeps current.

## Exercises

### Exercise 5.1

Clone `JCKodel/focus-kit-clinic`, check out `book-v1/start` on a branch of your own, and install the kit with your host.
Compare your file list with `git diff --stat book-v1/start book-v1/install-and-hosts`.

### Exercise 5.2

Say the install sentence again and read `git status`.
What did the update change, and what did it leave alone?

### Exercise 5.3

Find your host's row in `SETUP.md` §1, open its vendor page, and invoke `/propose` (or your host's equivalent) with a made-up slug.
The project has no documents yet for the command to read: what does the agent say, and why does that make chapters 6 and 7 come next?

[^focus-kit-setup]: J.C. Ködel, "focus-kit", `SETUP.md` at commit 26e5e1e4c8fcc6e059075a51db8cad5ed2028f2b. https://github.com/JCKodel/focus-kit/blob/26e5e1e4c8fcc6e059075a51db8cad5ed2028f2b/SETUP.md
[^claude-code-run]: This book's install of focus-kit on the guided project, 2026-09-25, with Claude Code 2.1.282, from `book-v1/start` to the chapter tag `book-v1/install-and-hosts`: the command, the report, the file list and the byte-for-byte check in the run's folder. https://github.com/JCKodel/focus-kit-book/blob/main/work/done/install-and-hosts-run/README.md
[^claude-code-memory]: Anthropic, "How Claude remembers your project", accessed 2026-09-25. https://code.claude.com/docs/en/memory
[^claude-code-skills]: Anthropic, "Extend Claude with skills", accessed 2026-09-25. https://code.claude.com/docs/en/skills
[^codex-agents-md]: OpenAI, "Custom instructions with AGENTS.md", accessed 2026-09-25. https://developers.openai.com/codex/guides/agents-md
[^codex-skills]: OpenAI, "Build skills", accessed 2026-09-25. https://developers.openai.com/codex/skills
[^copilot-instructions]: GitHub, "Adding repository custom instructions for GitHub Copilot", accessed 2026-09-25. https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions
[^copilot-skills]: GitHub, "About agent skills", accessed 2026-09-25. https://docs.github.com/en/copilot/concepts/agents/about-agent-skills
[^copilot-prompt-files]: GitHub, "Your first prompt file", accessed 2026-09-25. https://docs.github.com/en/copilot/tutorials/customization-library/prompt-files/your-first-prompt-file
