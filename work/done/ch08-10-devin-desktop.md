# ch08-10-devin-desktop

**Objective.** After chapters 8 and 10 a reader who works in Devin Desktop, the host formerly called Windsurf, knows that it reads the rules from `AGENTS.md` and the commands from `.agents/skills/`, invokes them as `/propose`, naming the delivery in the message when the slug does not reach the command, and why the kit leaves no copy of a command in `.windsurf/skills/`; both editions, and docs/03's `host` row names `devin-desktop`.

**Decided without the author.**

1. *The form you type: `/propose`, not `/propose <slug>`.* The queue line says "its `/propose <slug>`", but `SETUP.md` §1's host table, the kit as it is today, gives Devin Desktop "`/<name>`; whether a slug typed after it reaches the command is not documented", and the vendor's skills page says only that a skill is invoked as `/skill-name`. The book follows the kit and the vendor (docs/04 "The kit as it is", "Evidence"): the "You type" cell is `/propose`, the same as Cursor's, whose caveat is the same.
2. *The Cursor sentence becomes the shared caveat.* "For Cursor, the vendor's documentation does not say whether a slug typed after a command reaches it" becomes "For Cursor and Devin Desktop, ...". AGENTS.md "Abstraction on the second concrete occurrence": Cursor was the first, Devin Desktop is the second, and one sentence now covers both.
3. *The folder in the table: `.agents/skills/` alone.* `SETUP.md` §1 says Devin Desktop also reads `.claude/skills/`, and that what a host reading two folders does with the same name in both the kit has not tested. The table names the folder the kit writes the host's commands for, as its "Reads the commands from" column does; it already leaves out that Copilot reads `.claude/skills/` too, and an untested overlap gives the reader nothing to do (docs/04 "Numbers that prove", "No filler").
4. *`.windsurf/skills/` taught in the present.* One sentence after the table's paragraphs: Devin Desktop also reads `.windsurf/skills/`, the folder of its former name; the setup file writes nothing there and, on an update, removes the kit's own files there, so the host never finds an older copy of a command beside the current one; a file of yours there is reported and left (`SETUP.md` §1 step 3; kit `CHANGELOG.md` 2026.10.17 for the reason, not cited). No "no longer", no version, no Cascade, no `@` form: docs/04 "The kit as it is" keeps a rule's reason in the present and cites no changelog entry. The vendor's skills page lists `.windsurf/skills/` among the project folders it reads, so the claim carries `[^devin-skills]`.
5. *`AGENTS.md` read on its own.* "Codex and Copilot read `AGENTS.md` on their own" becomes "Codex, Copilot and Devin Desktop read ...", with `[^devin-rules]` beside the existing notes (vendor rules page: "Devin CLI reads this file automatically"). Devin Desktop needs no pointer file, as `SETUP.md` §1's table says.
6. *Source notes.* Two, the same keys in both editions, with the vendor's titles in English (docs/04 "Source notes"): `[^devin-skills]`, Cognition, "Skills Overview", Devin Docs, accessed 2026-10-17, <https://docs.devin.ai/cli/extensibility/skills/overview>; `[^devin-rules]`, Cognition, "Rules & AGENTS.md", Devin Docs, accessed 2026-10-17, <https://docs.devin.ai/cli/extensibility/rules>. They are the two pages `SETUP.md` §1 cites for this row. The pages are written for Devin's command line, so the notes sit on the claims those pages state (the folders, `/skill-name`, `AGENTS.md` read on its own); that these facts hold for Devin Desktop is the kit's table, named in plain words, with no note (docs/04: no note points to a file of focus-kit's repository). Cognition is the organization whose links the pages carry; the docs' index lists "Devin Desktop (Windsurf)" releases, which supports "formerly Windsurf".
7. *Introducing the host.* In the row and at its first mention in the text: "Devin Desktop, formerly Windsurf" (pt "Devin Desktop, antes Windsurf"), so a reader who knows the old name finds it (docs/04 "Teach, do not only show": a tool is introduced in a few words the first time it is named). Nothing more: the other hosts in the table get no description either, and the chapter's definition of host covers it.
8. *The row's place.* Where the Windsurf row is, in both tables (chapter 8's and chapter 10's), so the order the reader knows does not change.
9. *Key point 4.* "Windsurf as `@propose <slug>`" becomes "Devin Desktop as `/propose`"; still five key points, no number (docs/04 "Chapter shape", "One gain").
10. *The gain.* `## What the team gains` is unchanged: its sentence about Codex's `$` still holds, and a host renamed changes no gain (docs/04 "A gain per chapter").
11. *docs/03.* The queue line names docs/03: the `host` row's last value `windsurf` becomes `devin-desktop`. No new term. `kit-2026-10-17` left this row to this line (its Out of scope).
12. *Trunk, nothing staged by this definition.* docs/05 §5 Git; the driver session sets the marks in docs/06 (this batch's instructions). The tree's other changes (chapters 7, 11 and 23, docs/06, `work/batch-propose.md`, `work/ch07-11-23-review-words.md`, `work/ch16-review-agents.md`) are other lines' work and are not this page's.

**Behaviour.**

* Reading chapter 8's table "How each host finds the commands", a reader finds the row `Devin Desktop, formerly Windsurf` | `AGENTS.md` | `.agents/skills/` | `/propose`, in the place of the Windsurf row; no row names `.windsurf/skills/` or `@propose`.
* Reading the paragraph under the table, a reader finds that Codex, Copilot and Devin Desktop read `AGENTS.md` on their own, and that for Cursor and Devin Desktop the vendor's documentation does not say whether a slug typed after a command reaches it, so they name the delivery in their message if it does not.
* A reader who opens a repository in Devin Desktop and finds its old commands under `.windsurf/skills/` can say what the update does there: it removes the kit's own files, so the host does not find an older copy of `/apply` beside the current one in `.agents/skills/`, and it reports and leaves a file of their own.
* Edge: a reader who types `/propose lend-book` in Devin Desktop and sees the command ask what to define, or start without the slug, knows from the chapter to name the delivery in the message.
* Edge: a reader who knows the editor as Windsurf finds it under that name in the row, and does not look for `@propose`.
* Reading chapter 8's key points, a reader finds Devin Desktop running a command as `/propose`.
* Reading chapter 10's table, a reader finds `Devin Desktop, formerly Windsurf` | `/propose` in the Windsurf row's place.
* The Portuguese edition reads the same in the same places: "Devin Desktop, antes Windsurf", the same two notes with `acesso em 2026-10-17`, `emprestar-livro` where the lending library's slug appears.
* Reading docs/03, a person finds the `host` row's values ending in `devin-desktop`, and no `windsurf`.
* Failure: a sentence saying the kit "no longer" writes `.windsurf/skills/`, naming a kit version or Cascade, or citing the changelog fails docs/04 "The kit as it is"; the review catches it.
* Failure: a cell saying `/propose <slug>` for Devin Desktop states what the vendor does not document; the review catches it.

**Contract.**

* **Chapter 8, both editions** (`book/en/08-install-and-hosts.md`, `book/pt/08-install-and-hosts.md`), section "How each host finds the commands" (pt "Como cada host encontra os comandos") only:
  * the table row found by `| Windsurf |` becomes `| Devin Desktop, formerly Windsurf | \`AGENTS.md\` | \`.agents/skills/\` | \`/propose\` |` (pt `| Devin Desktop, antes Windsurf | ... | \`/propose\` |`);
  * the sentence starting "Codex and Copilot read `AGENTS.md` on their own" (pt "O Codex e o Copilot leem o `AGENTS.md` sozinhos") names Devin Desktop too and gains `[^devin-rules]`;
  * the sentence starting "For Cursor, the vendor's documentation" (pt "Para o Cursor, a documentação do fornecedor") covers Cursor and Devin Desktop;
  * one new sentence after it, on `.windsurf/skills/` as decision 4 says, with `[^devin-skills]`;
  * key point 4 as decision 9 says;
  * two note definitions after `[^copilot-prompt-files]`, as decision 6 writes them (pt `acesso em 2026-10-17`).
  Every other section of chapter 8 is unchanged, the update report block and "What an update reports" above all (`ch08-09-review-slot`).
* **Chapter 10, both editions** (`book/en/10-quick-guide.md`, `book/pt/10-quick-guide.md`): the row found by `| Windsurf |` becomes `| Devin Desktop, formerly Windsurf | \`/propose\` |` (pt `| Devin Desktop, antes Windsurf | \`/propose\` |`). Nothing else.
* **docs/03** (`docs/03-Domain.md`): the `host` row's code values end `..., \`antigravity\`, \`devin-desktop\``; its definition unchanged. No new term.
* **Sources:** `SETUP.md` §1's host table and step 3 (kit, named in plain words); the two Devin Docs pages of decision 6. No private case; no number.
* **docs/06:** none from this page beyond its own line's marks, set by the driver.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Out of scope.**

* Chapter 8's update example, its report at 2026.10.17 and chapters 8 and 9's slot questions: `ch08-09-review-slot`. Both lines edit `book/*/08-install-and-hosts.md` in different sections; when both are in the tree, stage by hunk (docs/05 §4).
* That Devin Desktop and Copilot also read `.claude/skills/`: an overlap the kit has not tested, nothing the reader acts on (decision 3).
* Codex's footnotes at their 2026-09-30 addresses: the kit's changelog moved its own citation; the book's notes record what was read that day, and no queue line asks for it.
* Chapters 7, 11 and 23: `ch07-11-23-review-words`, in flight in this tree.
* `work/done/` pages naming `.windsurf/`: history, not edited.
* README and README.pt: they name no host folder.

**Done when.**

* [x] Both editions written in the places the Contract names, the English first; parity green.
* [x] `grep -rn -i "windsurf" book/` finds only "formerly Windsurf" / "antes Windsurf" in the two tables of each edition and the `.windsurf/skills/` sentence of chapter 8; `grep -rn "@propose" book/` finds nothing.
* [x] `grep -n -i windsurf docs/03-Domain.md` finds nothing.
* [x] Chapter 8 still opens with its value; no filler and nothing useful cut; every claim on Devin Desktop carries its note or names `SETUP.md` in plain words; no "no longer", version, Cascade or changelog in the new text.
* [x] `make verify` green (build, parity, em dash, prose, width, links, disclosure).
* [x] `make book` builds; the delivery ends with the paths of both PDFs for the author's review.
* [x] The Delivery review ran on this delivery's paths (docs/05 §5) and the page records it.
* [x] Page moved to `work/done/`, the line `[x]`, staged by explicit paths and this line's hunk of docs/06, and the commit message suggested, `docs(ch08-10-devin-desktop): ...`.

**What happened.**

* Built as defined: chapter 8's row, the `AGENTS.md` sentence with `[^devin-rules]`, the shared Cursor and Devin Desktop caveat, the `.windsurf/skills/` sentence with `[^devin-skills]`, key point 4 and the two notes; chapter 10's row; docs/03's `host` row ending in `devin-desktop`. Both editions, the English first. Nothing dropped.
* Divergence, justified: the Done when grep for "windsurf" also finds "formerly Windsurf" / "antes Windsurf" in the `AGENTS.md` sentence of chapter 8, the host's first mention in the text, as decision 7 asks.
* Resumed after a stalled session: its staged edits were checked against Behaviour and Contract and kept.
* Decided by the agent, no author present (rule of this batch: the recommended option): the caveat reads "neither vendor's documentation says" (pt "nenhum dos dois fornecedores diz na documentação"), so two vendors are not behind one singular "vendor's".
* Proof: `make verify` green; `make book` builds both editions; `@propose` found nowhere in `book/`; `windsurf` nowhere in docs/03.
* Delivery review (docs/05 §5), a read-only agent on Opus over this delivery's staged and unstaged diff against this page and docs/04: no finding breaks the page or docs/04. Two optional points: the singular "vendor's" for two vendors, taken as above, verify green again; the queue line's text still says `/propose <slug>` and `.windsurf/skills/`, left as decision 1 explains and the Contract allows only the marks there. No finding left for the queue.

```commit
docs(ch08-10-devin-desktop): name Devin Desktop in chapters 8 and 10

- Windsurf row becomes Devin Desktop, formerly Windsurf, with /propose
- It reads AGENTS.md on its own; slug caveat shared with Cursor
- Update removes the kit's files from .windsurf/skills/, keeps yours
- Two Devin Docs source notes; docs/03 host value devin-desktop
- Both editions

work/done/ch08-10-devin-desktop.md
```
