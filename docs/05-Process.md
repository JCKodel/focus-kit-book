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
green, environments as §5 says → work/done/<slug>.md, git add, and the
line `[x]` → a person uses it, reviews and commits. Any line before `[x]`
may wait as `[?]` (§4).

/propose talks and writes the page, never code. /apply builds, proves,
updates the documents, stages and suggests the commit, never commits on
its own. Code changes only inside /apply: a change asked anywhere else,
however small, becomes a `[ ]` line in docs/06; what was said that the
line cannot hold goes into a draft `work/<slug>.md`. The answer stops
there and names `/propose <slug>`, as this host invokes commands; the
person runs it in this session, whose conversation the draft already
holds, or in a fresh one. /apply always starts in a fresh session, a
subagent being one: it has only what the page says.

Before /propose changes the queue or the page, claim the line as §5's
Git slot says: `claim.sh` creates the branch or worktree on origin, or
reopens the one this clone already has; one another clone created opens
only on the person's word, with `resume`. Bring into it any draft left
for the slug. Add a missing queue line where it belongs and say so; a
flaw found on the way is a finding, and §4 says whether it is a line.
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
    section that must be exact: a wrong screen is fixed in a session, a
    wrong column is a migration, and a wrong access rule has already
    leaked.

    **States.** Empty, loading, error, offline: one line each, or "the
    defaults". Only when there is a screen.

    **Visual reference.** Where the design is, and the viewports. Only when
    there is a screen. A screen whose reference does not exist yet gets
    one as §5's Design slot says, before this page is `[>]`.

    **Out of scope.** What does not enter, half a line of reason each.

    **Done when.** A mechanical checklist: tests X pass; verify green;
    screenshot matches Y.

After /apply the page also records what happened, under a heading
`## Outcome` below Done when, so the definition above stays as it was
read: what diverged, what was dropped, what the proof found, the
decisions taken. It ends with the commit message /apply suggested, in a fenced block whose info string is `commit`.
There is one final block: a resumed /apply replaces the earlier suggestion.
Above that block a page may hold a heading `## For the review`: the
notes §4 defines, one line each, written by the command that found them.

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
it introduces, the sources it cites and the cases it draws on; **Done when**
always includes: both editions written, opens with its value, no filler
and nothing useful cut, every number sourced, verify green, and, when a
private case is used, the author's approval of the anonymized text
(docs/00 OD-3).

## 4. The queue

docs/06: one line per delivery, in order, under milestones, edited by
conversation in any session. The order is the priority: the next
delivery is the first free line, and the person reorders by
conversation. A line is the mark, the slug, one sentence and its
suffixes, on one line; what happened goes on the page, because /propose
reads the whole queue. A line that needs another first ends with
`· after <slug>`, or `· after all`,
every line above it in its milestone but the dropped ones, which is how
the review is written. `after` is read per command: /propose starts when every line
it names is `[>]` or beyond, because the definition needs their pages;
/apply starts when every line it names is integrated, because the build
needs their code. Integrated is `[x]` on trunk; with a branch or a
worktree per delivery it is the delivery merged into the main branch,
and a `[x]` on its branch is built, awaiting integration. A line that
no clause of the current milestone's paragraph needs, whoever adds it,
goes under the next milestone, created when missing with a paragraph
that line answers and its review last; a finding of the milestone's own
review stays in it (§8), and so does a grave finding, below.

What /apply's review, proof or build discovers in what its delivery
built or changed is fixed in that delivery, as /apply says, and is no
finding here. A finding is a flaw a command discovers in anything else,
/propose while it defines included. A flaw older than the delivery is
one, even in a file the delivery edits. A finding is grave when it
breaks a clause of the milestone's paragraph for a person on its usual
path, loses or exposes data, or leaves verify red. So is a fix a
delivery in flight cannot go on without. A grave finding becomes a `[ ]`
line ending `· from <slug>`, the delivery that found it. The line goes
above the open planned lines only when verify is red or one of them
needs it. Otherwise it goes below them, above the review, or under the
review once it ran. Every other finding is a note on the page of the
delivery that found it, under `## For the review` (§3): the file and
line, and what a person would see. A note is not a line and waits for
the next milestone review to run (§8). A finding nobody can say is grave
is a note. A flaw in what a delivery built, whose fix would widen its
page or needs a decision no document answers, is a note too, with what
the person may do. When that flaw is grave, or leaves a Done when item
unticked, the line waits for the person's answer instead, the second
case below. A line that delivers a test, a proof tool or a change to
this process, and is not a grave finding, enters only on the person's
word; without it, it is a note.

Asked what may run now, run
`git -c "alias.fq=!sh .agents/skills/propose/scripts/queue.sh" fq <strategy>`,
the strategy as for the claim, and show its trees, one per open
milestone: each line under the last line it waits on, with its state.
Then come the lines free for /apply and for /propose, in the queue's
order across the milestones, and the next one. Offer the free lines as
one command with several slugs, saying each slug is one more agent and
costs as much as one session. Two builds must not touch the same files:
before its first edit, /apply compares the files its page touches with
the in-flight and unintegrated builds (§6), and an overlap is a
conflict, below. The line never leaves the queue; it changes mark as the
work changes, so the queue shows what is happening while it happens:

| Mark | Means | Set by |
|---|---|---|
| `[ ]` | not defined | the conversation that adds the line |
| `[~]` | being defined | /propose, when it starts |
| `[>]` | completely defined, page ready for /apply | /propose, when §3 is complete |
| `[*]` | being built | /apply, when it starts |
| `[x]` | done, page in `work/done/`; on a branch, built until merged; with `· dropped:`, cancelled | /apply, with verify green; the person, when cancelling |
| `[?]` | waiting, never on another line | any session, in the three cases below |

A board may read the queue, and people pull work from it, so a mark
changes at once: `[~]` is /propose's first edit, `[*]` is /apply's first,
`[x]` is /apply's last. A mark is changed by running
`git -c "alias.fm=!sh .agents/skills/propose/scripts/mark.sh" fm <slug> "<mark>"`,
adding `stage` at the end when the line goes into the index, as /apply's
`[x]` does. Any other edit to docs/06 is the host's file edit on the lines
it changes, never a program that writes the whole file. On trunk the
board sees a new mark at once. With a branch or a worktree per delivery
the mark lives on the delivery's branch, which /propose creates on
origin as the claim, and the main branch shows the line as it was until
the merge. A line whose branch exists on origin is taken, whatever its
copies say. The branch's copy of the line is the current one for its
slug until the merge, main's after it. A `[?]` blocks on the copy that
put it. A branch's blocks when the branch changed the line after it left
main: the line differs from the one at their merge-base, or was not
there. Main's blocks unless the line's own branch changed the line. None
blocks a line whose current copy is `[x]`. A line only a branch has
belongs to its milestone, under main's wording of the heading when the
branch reworded it. `queue.sh` reads them
so; whoever reads by hand, a board or a session, reads the same way
after `git fetch`.

A line waits in three cases, never on another line: the person says it
is blocked; it needs an answer that was asked and not given; or a
milestone review's code reading missed part of its range, and its
reason says what was read (§8).
The reason goes at the end
of the line, `· blocked: <reason>`.
Before that reason, record the phase to resume: `· resume: propose` for
`[ ]` or `[~]`, and `· resume: apply` for `[>]` or `[*]`. A draft saved
by /propose always uses `resume: propose` until §3 is complete.
Any mark before `[x]` can become `[?]`. The line leaves `[?]` when the
reason is resolved: the person says so, or the session that records the
answer clears it. Remove both suffixes: `resume: propose` returns to `[ ]`,
keeping any draft, and `resume: apply` to `[>]`.

A line that needs another line first is not waiting. It ends
`· after <slug>` and keeps the mark that names its next command. Known
when the line is added, the suffix is written then. Found by work
already started, such as a fix in the middle of an /apply, the session
adds the suffix and returns the line to `[ ]` from `[~]`, keeping the
draft, or to `[>]` from `[*]`. Its page says what was built and what it
waits on, and /apply continues from there.

A `[~]` or `[*]` line whose session ended without blocking it (the host
closed, the connection or its limit) keeps its mark; its command resumes
it on the person's word, inspecting the page, the tree and the index
before editing. A delivery the person cancels, because it is impossible,
refused or no longer wanted, ends `[x]` with `· dropped: <reason>` at the
end of the line, its page in `work/done/` saying what was built and
undone; a line whose `after` names it is the person's to re-decide.
`after all` names none and leaves it out.
These are the marks of focus-kit 2026.10.05, a line waiting on a review's
partial reading is that of 2026.10.18, and the ended and dropped lines are
those of 2026.10.18.1, where a board sees a mark is that of 2026.10.19,
how the queue is read with a branch or a worktree per delivery is that
of 2026.10.19.1, the branch as the claim of its line is that of
2026.10.20, the `(PA)` token on queue lines was that of 2026.10.20.1
until 2026.10.25 removed it, a command typed with several slugs is that
of 2026.10.20.3, a page decided alone saying the agent chose is that of
2026.10.20.5, what may run now answered by `queue.sh` is that of
2026.10.24, `after` read per command, `after all`, integration, the
claim by `claim.sh` and the current copy of a line are those of
2026.10.25, a mark changed by `mark.sh` and docs/06 edited line by line
are those of 2026.10.26, `mark.sh` refusing a second start of one
line is that of 2026.10.27, `after all` leaving out the dropped lines is
that of 2026.10.27.1, and a flaw fixed in the delivery that built it,
the grave finding as a line ending `· from <slug>` and every other
finding a note are those of 2026.11.12, and the three cases a line
waits in, a line that needs another ending `· after <slug>` and never
`[?]`, a `[?]` blocking on the copy that put it, a branch's line under
main's heading and the trees, one per open milestone, are those of
2026.11.13 (ADR-0018 and its amendments
`kit-2026-10-18`, `kit-2026-10-18-1`, `kit-2026-10-19`,
`kit-2026-10-19-1`, `kit-2026-10-20`, `kit-2026-10-20-1`,
`kit-2026-10-20-3`, `kit-2026-10-20-5`, `kit-2026-10-24`,
`kit-2026-10-25`, `kit-2026-10-26`, `kit-2026-10-27`,
`kit-2026-10-27-1`, `kit-2026-11-12` and `kit-2026-11-13`).

Two sessions in one working tree, on free lines that touch different
files, are the normal case of parallel work on trunk. Another line
changing mark, another delivery's page or files appearing in the tree,
and another session's index entries are that session's work, not a
conflict: do not stop for them, do not touch them, change only this
delivery's line and stage only this delivery's paths and hunks, including
its own hunk of docs/06. A conflict is a line edited by both, or a file
this page needs that the other delivery is changing; then stop and
report. Two deliveries' edits in one hunk, each on its own line, as two
neighbouring queue lines are, conflict in nothing: they are split when
staged, each session staging only its own line. In worktrees, change
only this delivery's line; when branches are integrated, reconcile
docs/06 by slug, keeping every line at its latest state, never one
side's whole file.

A command typed with several slugs opens one subagent per slug, each
following the command's file with one slug, sent to the slug's worktree
where §5's Git slot has one (/propose creates it). The subagents `after`
lets run at once are opened at once, not one after another; a line still waiting when the others end is reported, not waited
for. The session edits nothing itself. A subagent cannot ask the person:
it reports the question with the context to answer it and stops; the
session asks and sends the answer back, resuming it where the host can,
else opening it again on the slug, whose `[~]` or `[*]` it resumes on the
command's word. A command that says to decide alone has each question
answered by its recommendation, written on the page as the agent's
answer, saying the agent chose it, so the review finds it; one that says
to build as well has a new subagent run /apply when a page reaches
`[>]`, the page saying it was built before the person read it, who reads
the pages and the diffs at the end.

## 5. This project

A slot says what and the command, in a few lines: /apply reads it every
time. Steps go in a manual, and what a command prints stays in its help.
The project may add slots of its own; a slot that names /propose or
/apply is followed by that command, with no edit to the skill.

* **Documentation language:** English. Identifiers in English. The book
  itself: English source, Brazilian Portuguese translation, same delivery.
* **Verify:** `make verify`, which runs the strict site build, edition
  parity, the em dash check, the prose rules, the block width check, the
  examples check (chapter 3's database-boundary examples run by Node.js
  26.12.0 or later), the link check and the disclosure scan, commit
  messages and hooks included, fast enough to run on every delivery.
  Green before anything is declared done. Its ceiling: five minutes; it
  took 11 seconds on 2026-11-12. /apply says how long verify took. Over
  the ceiling, that is a note for the review (§4). The review says which
  tests go to the slow ones. Slow tests, one line each, the command and
  what it covers: none. The milestone review runs them all (§8). /apply
  runs the ones that cover what its delivery changed, and only those,
  before the delivery ends.
* **Environments:**
  * local: `make serve` for the site, `make book` for PDF and EPUB in
    `output/` (never committed). A delivery leaves both building
    (`docs/manuals/build-the-book-from-a-clone.md`).
  * GitHub Pages: the site from `main`, published by Actions on every
    push. A delivery leaves nothing to do: the author's push publishes
    (`docs/manuals/publish-the-site.md`).
  * GitHub Release: PDF and EPUB in both editions, built by Actions on a
    `v*` tag. Only the author tags, with `make release`
    (`docs/manuals/release-the-book.md`).
* **Design:** prototype, no reference, by choice: the site's look is
  MkDocs Material's theme (docs/01), and a toolchain delivery that
  changes what the site shows is proved by Proof of a screen; a chapter
  has no screen (ADR-0019).
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
  this repository, its pages or its commit messages. The hooks are turned
  on with `make hooks`; `make verify` fails while they are off. Setting
  up the list, the hooks and the secret:
  `docs/manuals/set-up-the-disclosure-list.md`.
* **Publish policy:** the agent never pushes, tags, releases or uploads.
  A chapter that is not done carries the draft marker, the line
  `status: draft` in its front matter, in both editions; the site shows a
  banner and a mark in the navigation, and the chapter's delivery removes
  the line when done. So the site can publish `main` at any time.
  Whatever it is, /apply's last words say which environment is at which
  version.
* **Context:** `context/` is listed in `.gitignore` and not created: the
  repository is public and what people said about the cases is private.
* **Delivery review:** before /apply ends, a read-only agent on Opus,
  which keeps the session's advisor, reads the whole delivery against its
  base: `git diff HEAD` of the delivery's paths, staged and unstaged, of
  docs/06 only its own hunk; the commits a blocked delivery already made
  on its branch, none on trunk, where blocked work stays uncommitted
  (§6); and the files the delivery created, which no diff shows until
  they are staged; all against the delivery's page and docs/04. Another
  session's files are not this review's. No other model runs it.
* **Guided project and brownfield project:** retired by `rewrite`
  (ADR-0017). The repositories `JCKodel/focus-kit-clinic` and
  `JCKodel/clahub` and their tags stay as they are, cited by no chapter;
  the recorded runs in `work/done/*-run/` are the history of the book's
  numbers.
* **Manuals:** `docs/manuals/`, one file per action that takes more than
  one command, named after what it does: running the product from a fresh
  clone, what a person does by hand outside a delivery (publish, roll
  back, rotate a secret, set up a service) and a proof /apply runs on
  another machine. Each stands alone for whoever runs it, having read
  nothing else: what it does and when, what must be in place, the commands
  in order, how to tell it worked, how to undo it, what breaks if a step
  is skipped. A slot that names such a command points to its manual
  instead of holding the steps; a delivery that changes one updates its
  manual.
  * `build-the-book-from-a-clone.md`: running the book from a fresh
    clone, from installing what it needs to the site at
    `http://127.0.0.1:8000/`, the PDF and EPUB in `output/` and `make
    verify` green; owed since the book could be built, written by
    `kit-2026-10-19-2`, updated by every delivery that changes a step.
  * `publish-the-site.md`: the site on GitHub Pages, from a push to `main`.
  * `release-the-book.md`: PDF and EPUB of both editions as a GitHub
    Release, with `make release`.
  * `set-up-the-disclosure-list.md`: the list, the hooks and the Actions
    secret, once per machine and once per clone.
* **Milestone review:** the kit's readers: on the author's word in the
  review's /apply session, read-only agents on Opus read
  `git diff <base>..<end>`, the two commits the review's page names, its
  base and the commit HEAD was when the reading started, one per area it
  touches: the build, the chapters, the kit's skills, the documents. One
  more read-only agent on Opus checks each candidate against the file
  before the author sees it. Every agent keeps the session's advisor,
  Fable. Each launch sets its model to Opus; no other model runs the
  review. At most two of these agents run at a time: in `m16-review`
  five at once left three with no report.
* **Git:** trunk. A delivery's page and build are one change: one commit.
  Reverting it undoes what git holds; a delivery that acts outside git
  (a migration run, a message sent) says in its Done when how that is
  undone, or that it is not. Two sessions may work in one tree on free
  lines (§4). The agent stages; it never commits or merges on its own,
  and asked, it takes the step the person names.

## 6. Commit

This section owns the commit format; docs/04 points here. Before editing,
inspect git status, the staged and unstaged diffs, and untracked files.
Record which changes already belong to this delivery (its /propose page
and queue changes, or a previous partial /apply) and which are unrelated;
do not assume an existing edit belongs to it because it shares a path.
Another delivery's page, its files and its hunk of docs/06 belong to the
session building it (§4); they are unrelated here. Preserve unrelated
edits and the pre-existing index entries. If ownership of a change this
delivery must edit cannot be established, or this delivery and another
changed the same lines, stop and report the affected paths before editing
them or staging; do not reset or stash them.

Stage only this delivery's files or hunks, including the page move and its
documentation changes. Use explicit paths for files wholly owned by it,
and selective staging for mixed files; never `git add -A` or `git add .`.
Inspect the staged diff afterwards and report any unrelated entries that
were already staged, so the person knows a plain commit would include
them. Do not unstage those entries yourself. A commit must contain only
this delivery for the one-change promise to hold: with two sessions on
trunk, the person commits each delivery as its session ends, from an
index that holds only it, never by naming paths on `git commit`, which
takes each named file whole from the working tree and carries the other
session's hunk of it, staged or not. One working tree has one index, so
when the second session has already staged, the person sets its paths
aside with `git restore --staged <paths>`, commits the first, and stages
them again.

The agent suggests the message; the person commits after reviewing, or
asks the agent to.
The one commit a script makes is the release's: `make release`, on the
author's `y`, commits `VERSION` alone as `chore(release): vX.Y.Z`, with no
page and no body (`docs/manuals/release-the-book.md`).
Imperative subject up to 72 characters, `<type>(<slug>): <subject>`, where
type is `feat`, `fix`, `docs` or `chore`; body up to five one-line bullets,
the highlights and not
the reasoning; last line points to the page's actual path, where the
reasoning lives: `work/done/<slug>.md` when done, `work/<slug>.md` when
blocked. A partial message says it is partial and names the blocker;
it must not imply verify passed or the delivery is done.

When blocked on trunk, keep the work uncommitted and do not add it to the
index; the `commit` block is a draft for the eventual whole delivery.
Resume with the same page and record the current verify result. A
prerequisite that must be built first becomes a `[ ]` line above this
one, ending `· from <slug>` (§4), and this line returns to `[>]` ending
`· after <slug>` (§4). The partial work stays in the tree, uncommitted and out of
the index, while the prerequisite is built and staged alone; when the two
change the same lines, the prerequisite's session stops and reports, as
this section says. Do not mix their commits on trunk.
On a delivery branch or worktree, partial changes may be staged and
suggested for the person to commit there. Keep the branch unmerged until
the delivery is complete, so one merge still contains the whole delivery.

## 7. What this process does not have

No formal spec, no spec delta, no change folder, no numbered tasks, no
gate before implementation beyond a complete page, no review of a review,
no subagent beyond a command's one per slug (§4) and the reviews' readers
and checker (§5's Delivery review, §8), no tool the deliveries did not ask
for. When one of these is proposed, the question
is: which concrete error would it have caught? The answer names an error
that happened.

## 8. Closing a milestone

A milestone is planned with its review as its last line,
`<milestone>-review · after all`, a delivery like the others: /propose
writes its page when every line above but the dropped ones is defined,
/apply runs it when every one of those is integrated. Its page takes the milestone's paragraph clause by
clause and writes, for each, which delivery answers it and how a person
tests it. It fixes nothing. It runs §5's slow tests, when the slot names
them; a failing one is a finding. The person tests each
clause by hand: a clause no delivery answers, or one that fails in the
person's hands, is a finding.

The review also reads the code, the one look at the whole instead of a
delivery: every page can be right and the whole wrong. Its page names as
the base the commit of the previous milestone's review, so the range
holds the fixes of its findings, which get no second review, or the
first commit for a first milestone, or, where no earlier review exists,
the commit the page names and why; and the commit HEAD was when the
reading started, so the range stays fixed while readers work; and it
lists the paths `git diff --stat <base>..<that commit>` shows: always
the range, since a bare commit reads that one commit. It costs, so the
session says it is time and starts it only on the person's word. §5's
Milestone review slot says who reads: the host's deep review, which the
person launches over that range; or the kit's readers, one read-only
agent per area of the slot, in parallel where the host runs agents, or
one fresh session per area, opened by the person, where it does not;
an area too large for one careful reading splits again. Each reader has
the whole repository open and reads its area's changes for what no
delivery's own review could see, one delivery's work against another's,
a document against another, the whole against docs/01, and reports
candidates by file and line and the paths it read. Either way, one
checker, an agent or the review's session, opens each candidate's file
and marks it seen (true in the file today), latent (nothing triggers it
today) or weak (the claim does not hold as stated) before the person
sees it. They fix nothing. When the paths read miss some of the range's,
the page says which and the line waits as `[?]` with `· resume: apply`
and `· blocked: <what was read>` (§4). A candidate the person confirms
is a finding like the others.

For a milestone of chapters, testing by hand is the author reading, in
the PDF of both editions, the passages the page names, and answering the
test the page wrote.

On the person's word, given for the review, in its session or relayed
to it, and quoted on its page, the review's session may take the tests and the
confirmation: it answers each clause's test from its own reading of
the passages the page names, in the PDF of both editions for a
milestone of chapters, and the word is the person's confirmation of
each candidate the checker marks seen, the latent and weak ones listed
on the page as dropped. The page records those answers as the
review's, never the person's. The word holds for the review whose page
quotes it; the checker, the range and the `[?]` for paths not read
stay as above.

The review opens by copying onto its page the notes left since the
previous review, from the `## For the review` heading of every page the
range delivered (§4). The checker marks each as it marks a candidate.
The review grades every confirmed finding. A grave one, as §4 defines
it, becomes a `[ ]` line, one each. The others stay listed on the
review's page. First come the medium ones, which a person meets in
ordinary use while the clause still holds. Then come the small ones: a
rare case, a latent or weak candidate, a cost nobody measured. The
person says which medium ones enter the milestone's one line,
`<milestone>-fixes`, each an item of its page. That page is their list
and is not split, whatever its length. A small one becomes a line only when
the person picks it. These lines end `· from <milestone>-review`, sit
under the review line and wait for /propose; the milestone closes when
they are `[x]`. They get no second review: each passes through its own
page, its proof and the person's commit, which is the review; a finding
is never a fix in the middle of the next milestone.

M3 and M4 were reviewed by a headless session whose findings opened `.1`
milestones, with a code review of the guided project beside them, and
both recipes are in the history of this file at the commit before
`m9-review`.
