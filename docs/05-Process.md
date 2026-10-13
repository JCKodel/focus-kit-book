# Process

How an idea becomes a chapter, or a piece of the toolchain, in *One Page at a Time*.

## 1. The rule

One delivery is one page, `work/<slug>.md`. If it does not fit one page,
it is two deliveries. The page is not a concision goal: it is the test that
the scope was understood. A scope that needs five pages has not been
decided yet.

A chapter is one delivery and includes both editions.

## 2. The flow

docs/06 `[ ]` → /propose <slug>, the line `[~]` → work/<slug>.md, the
line `[>]` → /apply <slug>, in a fresh session, the line `[*]` → verify
green, environments as §5 says → work/done/<slug>.md, the line `[x]`, and
git add → a person reviews and commits. Any line before `[x]` may wait as
`[?]` (§4).

/propose talks and writes the page, never code. /apply builds, proves,
updates the documents, stages and suggests the commit, never commits.
Code changes only inside /apply: a change asked anywhere else, however
small, becomes a `[ ]` line in docs/06 and the answer stops there.

Before /propose changes the queue or the page, use §5's git strategy:
create the branch or worktree named after the slug, or reuse its existing
one on resumption. Add a missing queue line where it belongs and say so.
Start defining with `[~]`; start building only a completely defined `[>]`
page, with `[*]`. Follow §4 for blocked lines and §6 before changing code
or staging. Keep project slots and rules current before using them; report
a missing process rule rather than falling back to a retired instruction.

## 3. The page

    # <slug>

    **Objective.** One sentence: what the user can do afterwards.

    **Behaviour.** Verifiable scenarios in user language, each an action
    with concrete input and the result the user sees. Include the cases
    that must fail and the edges the documents imply. Each line becomes a
    test or a manual check.

    **Contract.** Data, schema, API, message shapes, or "none". The only
    section that must be exact.

    **States.** Empty, loading, error, offline: one line each, or "the
    defaults". Only when there is a screen.

    **Visual reference.** Where the design is, and the viewports. Only when
    there is a screen.

    **Out of scope.** What does not enter, half a line of reason each.

    **Done when.** A mechanical checklist: tests X pass; verify green;
    screenshot matches Y.

After /apply the page also records what happened: what diverged, what was
dropped, what the proof found, the decisions taken. It ends with the commit
message /apply suggested, in a fenced block whose info string is `commit`.
There is one final block: a resumed /apply replaces the earlier suggestion.

A draft with unanswered scope questions is not ready for /apply, even
when its file exists. Before marking `[>]`, every section above is filled
or explicitly inapplicable and no scope decision remains open. Ask the
person to review the page: Behaviour is checkable, Contract exact, Out of
scope names what they assumed was included, and choices made on their
behalf are explicit. Corrections happen in the /propose conversation;
/apply starts in a fresh session afterwards.

For a chapter, the page reads this way: **Objective** is the "what you get"
sentence the chapter opens with; **Behaviour** lists what the reader can do
or explain afterwards; **Contract** lists the sections, the terms of docs/03
it introduces, the sources it cites, the cases it draws on and the
exercises; **Done when** always includes: both editions written, opens with
its value, no filler and nothing useful cut, every number sourced,
verify green, and, when a private case is used, the author's approval of
the anonymized text (docs/00 OD-3).

## 4. The queue

docs/06: one line per delivery, in order, under milestones. The order is
the priority: the next delivery is the first free line, and the person
reorders by conversation. A line that needs another done first ends with
`· after <slug>`, written when the line is added; it is free when every
line it names is `[x]`. Asked what can run at the same time, answer from
the queue: the free lines, and among them the ones that touch different
files, judged from their pages and docs/01. The line never
leaves the queue; it changes mark, at the moment the work changes, so the
queue shows what is happening while it happens:

| Mark | Means | Set by |
|---|---|---|
| `[ ]` | not defined | the conversation that adds the line |
| `[~]` | being defined | /propose, when it starts |
| `[>]` | completely defined, page ready for /apply | /propose, when §3 is complete |
| `[*]` | being built | /apply, when it starts |
| `[x]` | done, page in `work/done/` | /apply, with verify green |
| `[?]` | waiting | any session, in the three cases below |

A line waits when the person says it is blocked, when it needs an answer
that was asked and not given, or when work already started finds it needs
another line done first, such as a fix found in the middle of an /apply.
The reason goes at the end
of the line, `· blocked: <reason>` or `· blocked: after <slug>, <slug>`.
A dependency known when the line is added is `· after <slug>` alone,
without `[?]`: an order, not an interruption.
Before that reason, record the phase to resume: `· resume: propose` for
`[ ]` or `[~]`, and `· resume: apply` for `[>]` or `[*]`. A draft saved
by /propose always uses `resume: propose` until §3 is complete.
Any mark before `[x]` can become `[?]`. The line leaves `[?]` when the
reason is resolved: the person says so, the session that records the
answer clears it, or /apply clears it when it marks `[x]` the last line of
an `after`. Remove both suffixes and return `resume: propose` to `[ ]`,
keeping any draft for /propose to finish; return `resume: apply` to `[>]`
only when its page still satisfies §3. Existence alone is insufficient.
If scope became undecided, return `[ ]` and say what /propose must settle.
For an old blocked line without `resume`, recover the phase from its page
and history; if completeness cannot be established, return `[ ]`.
These are the marks of focus-kit 2026.10.05 (ADR-0018).

Two sessions in one working tree, on free lines that touch different
files, are the normal case of parallel work on trunk. Another line
changing mark, another delivery's page or files appearing in the tree,
and another session's index entries are that session's work, not a
conflict: do not stop for them, do not touch them, change only this
delivery's line and stage only this delivery's paths and hunks, including
its own hunk of docs/06. A conflict is the same hunk edited by both, or a
file this page needs that the other delivery is changing; then stop and
report. In worktrees, each worktree's queue shows that branch's state, not a
global live view. Change only the current delivery's line, its new findings
and the dependent lines this session can resolve. When branches are
integrated, reconcile docs/06 by slug: retain every delivery and finding,
and each owning branch's latest state. Do not replace the whole file with
one side or downgrade a completed line using a stale copy. Check the page
at the expected path and keep a dependency blocked until its completed
changes are available in the branch that needs them. A conflicting state
or scope is reported for resolution, never guessed. Apply the same care
to shared domain terms and ADRs.

Each milestone is planned with its review as the last line (§8). Edited by
conversation in any session.

## 5. This project

* **Documentation language:** English. Identifiers in English. The book
  itself: English source, Brazilian Portuguese translation, same delivery.
* **Verify:** `make verify`, which runs the strict site build, edition
  parity, the em dash check, the prose rules, the link check and the
  disclosure scan. Green before anything is declared done. Created by
  `site-skeleton` (build, parity, em dash); `disclosure-scan`,
  `prose-rules` and `link-check` add their checks to it; `commit-hooks`
  adds the commit messages and the hooks to the disclosure scan.
* **Environments:**
  * local: `make serve` for the site, `make book` for PDF and EPUB in
    `output/` (never committed). A delivery leaves both building.
  * GitHub Pages: the site from `main`, published by Actions on every
    push. A delivery leaves nothing to do: the author's push publishes
    (`docs/manuals/publish-the-site.md`).
  * GitHub Release: PDF and EPUB in both editions, built by Actions on a
    `v*` tag. Only the author tags, with `make release`
    (`docs/manuals/release-the-book.md`).
* **Proof of a screen:** for toolchain deliveries, a screenshot of the
  rendered site at 1280 and 390 pixels wide, in both editions, saved as
  `work/done/<slug>-<what>.png`; failures are captured too. For chapter
  deliveries, no screenshot: the proof is verify green, then `make book`,
  and the delivery ends by giving the author the paths of both PDFs to
  review. A chapter that
  brings a kind of content the build has not shown before (its first
  diagram, say) also proves it renders: screenshots of the site in light
  and dark and of the PDF, in both editions.
* **Case A and Case B:** every passage drawn from them is listed in the
  delivery's page for the author's approval before the chapter is done
  (docs/00 OD-3), and `make scan` is green.
* **Disclosure:** the disclosure list lives outside the repository, at
  `~/.config/focus-kit-book/denylist.txt` or the path in `FKB_DENYLIST`;
  in Actions it comes from the secret `DISCLOSURE_DENYLIST`. No term of
  that list, no private path and no source folder name is ever written in
  this repository, its pages or its commit messages. Created by
  `disclosure-scan`. `commit-hooks` adds the check of every commit
  message to `make verify` and the hooks, turned on with `make hooks`;
  `make verify` fails while they are off. Setting up the list, the hooks
  and the secret: `docs/manuals/set-up-the-disclosure-list.md`.
* **Publish policy:** the agent never pushes, tags, releases or uploads.
  A chapter that is not done carries the draft marker, the line
  `status: draft` in its front matter, in both editions; the site shows a
  banner and a mark in the navigation, and the chapter's delivery removes
  the line when done. So the site can publish `main` at any time.
* **Context:** `context/` is listed in `.gitignore`: the repository is
  public and what people said about the book's cases is private. The
  folder does not exist today: the sources stay in the author's folders
  outside the repository, named nowhere (ADR-0012), and the author's
  decisions arrive by conversation and go into the documents. A folder
  created later stays out of git; back it up elsewhere.
* **Guided project and brownfield project:** retired by `rewrite`
  (ADR-0017). The repositories `JCKodel/focus-kit-clinic` and
  `JCKodel/clahub` and their published tags stay as they are and no
  chapter cites them; the recorded runs in `work/done/*-run/` stay as the
  history of how the book's numbers were counted, and a chapter's note may
  point to one. The recipe of a recorded run that this section held is in
  the history of this file, at the commit before `rewrite`.
* **Manuals:** `docs/manuals/`, one file per thing a person does by hand
  outside a delivery (publish, roll back, rotate a secret, set up a
  service), named in the documentation language after what it does. Each
  stands alone for a person who has read nothing else: what it does and
  when, what must be in place, the commands in order, how to tell it
  worked, how to undo it, what breaks if a step is skipped. A slot that
  names such a command points to its manual instead of holding the steps;
  a delivery that changes one updates its manual.
  * `publish-the-site.md`: the site on GitHub Pages, from a push to `main`.
  * `release-the-book.md`: PDF and EPUB of both editions as a GitHub
    Release, with `make release`.
  * `set-up-the-disclosure-list.md`: the list, the hooks and the Actions
    secret, once per machine and once per clone.
* **Git:** trunk. A delivery's page and build are one change: one commit.
  Two sessions may work in one tree on free lines (§4). The agent stages;
  it never commits or merges.

## 6. Commit

This section owns the commit format; docs/04 points here. Before editing,
inspect git status, the staged and unstaged diffs, and untracked files.
Record which changes already belong to this delivery (its /propose page
and queue changes, or a previous partial /apply) and which are unrelated;
do not assume an existing edit belongs to it because it shares a path.
Another delivery's page, its files and its hunk of docs/06 belong to the
session building it (§4); they are unrelated here. Preserve unrelated
edits and the pre-existing index entries. If ownership of a change this
delivery must edit cannot be established, or changes overlap in the same
hunk, stop and report the affected paths before editing them or staging;
do not reset or stash them.

Stage only this delivery's files or hunks, including the page move and its
documentation changes. Use explicit paths for files wholly owned by it,
and selective staging for mixed files; never `git add -A` or `git add .`.
Inspect the staged diff afterwards and report any unrelated entries that
were already staged, so the person knows a plain commit would include
them. Do not unstage those entries yourself. A commit must contain only
this delivery for the one-change promise to hold: with two sessions on
trunk, the person commits one delivery at a time, naming its paths.

The agent suggests the message; the person commits after reviewing.
Imperative subject up to 72 characters, `<type>(<slug>): <subject>`, where
type is `feat`, `fix`, `docs` or `chore`; body up to five one-line bullets,
the highlights and not
the reasoning; last line points to the page's actual path, where the
reasoning lives: `work/done/<slug>.md` when done, `work/<slug>.md` when
blocked. A partial message says it is partial and names the blocker;
it must not imply verify passed or the delivery is done.

When blocked on trunk, keep the work uncommitted and do not add it to the
index; the `commit` block is a draft for the eventual whole delivery.
Resume with the same page and record the current verify result. If a
prerequisite must be implemented separately before resumption, move this
partial delivery to its own branch/worktree, preserving its edits and
index ownership, before starting the prerequisite; ask for help if safe
separation is not possible. Do not mix their commits on trunk.
On a delivery branch or worktree, partial changes may be staged and
suggested for the person to commit there. Keep the branch unmerged until
the delivery is complete, so one merge still contains the whole delivery.

## 7. What this process does not have

No formal spec, no spec delta, no change folder, no numbered tasks, no
gate before implementation, no review of a review, no specialized
subagent, no tool the deliveries did not ask for. When one of these is proposed, the question
is: which concrete error would it have caught? The answer names an error
that happened.

## 8. Closing a milestone

A milestone is planned with its review as its last line,
`<milestone>-review`, a delivery like the others: /propose writes its
page, /apply runs it. Its page takes the milestone's paragraph clause by
clause and writes, for each, which delivery answers it and how a person
tests it. It reviews no code and fixes nothing. The person tests each
clause by hand: a clause no delivery answers, or one that fails in the
person's hands, is a finding.

For a milestone of chapters, testing by hand is the author reading, in
the PDF of both editions, the passages the page names, and answering the
test the page wrote.

Each finding becomes a `[ ]` line in the same milestone, under the review
line, waiting for /propose. The milestone closes when those lines are
`[x]`. They get no second review: each one passes through its own page,
its proof and the person's commit, which is the review. A finding is
never a fix in the middle of the next milestone.

M3 and M4 were reviewed by a headless session whose findings opened `.1`
milestones, with a code review of the guided project beside them, and
both recipes are in the history of this file at the commit before
`m9-review`.
