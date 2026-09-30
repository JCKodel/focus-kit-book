# Process

How an idea becomes a chapter, or a piece of the toolchain, in *One Page at a Time*.

## 1. The rule

One delivery is one page, `work/<slug>.md`. If it does not fit one page,
it is two deliveries. The page is not a concision goal: it is the test that
the scope was understood. A scope that needs five pages has not been
decided yet.

A chapter is one delivery and includes both editions.

## 2. The flow

docs/06 → /propose <slug> → work/<slug>.md → /apply <slug>, in a fresh
session → verify green, environments as §5 says → work/done/<slug>.md and
git add → a person reviews and commits.

/propose talks and writes the page, never code. /apply builds, proves,
updates the documents, stages and suggests the commit, never commits.

## 3. The page

    # <slug>

    **Objective.** One sentence: what the user can do afterwards.

    **Behaviour.** Verifiable scenarios in user language. Each line becomes
    a test or a manual check.

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
dropped, what the proof found, the decisions taken.

For a chapter, the page reads this way: **Objective** is the "what you get"
sentence the chapter opens with; **Behaviour** lists what the reader can do
or explain afterwards; **Contract** lists the sections, the terms of docs/03
it introduces, the sources it cites, the cases it draws on and the
exercises; **Done when** always includes: both editions written, opens with
its value, no filler and nothing useful cut, every number sourced,
verify green, and, when a private case is used, the author's approval of
the anonymized text (docs/00 OD-3).

## 4. The queue

docs/06: one line per delivery, in order, under milestones. The line never
leaves the queue; it changes mark: `[ ]` not defined, `[>]` defined and not
built, `[x]` done. The last line of each milestone is its review (§8). Edited by
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
    push. A delivery leaves nothing to do: the author's push publishes.
  * GitHub Release: PDF and EPUB in both editions, built by Actions on a
    `v*` tag. Only the author tags, and uploads the files to
    books.kodel.com.br.
* **Proof of a screen:** for toolchain deliveries, a screenshot of the
  rendered site at 1280 and 390 pixels wide, in both editions, saved as
  `work/done/<slug>-<what>.png`; failures are captured too. For chapter
  deliveries, no screenshot: the proof is verify green, then `make book`,
  and the delivery ends by giving the author the paths of both PDFs to
  review. A chapter that
  brings a kind of content the build has not shown before (its first
  diagram, say) also proves it renders: screenshots of the site in light
  and dark and of the PDF, in both editions.
* **Disclosure:** the disclosure list lives outside the repository, at
  `~/.config/focus-kit-book/denylist.txt` or the path in `FKB_DENYLIST`;
  in Actions it comes from the secret `DISCLOSURE_DENYLIST`. No term of
  that list, no private path and no source folder name is ever written in
  this repository, its pages or its commit messages. Created by
  `disclosure-scan`. `commit-hooks` adds the check of every commit
  message to `make verify` and the hooks: a clone that has the list runs
  `make hooks` once, and from then on a commit whose staged files or
  message match the list is refused before it exists; `make verify`
  fails while they are off.
* **Publish policy:** the agent never pushes, tags, releases or uploads.
  A chapter that is not done carries the draft marker, the line
  `status: draft` in its front matter, in both editions; the site shows a
  banner and a mark in the navigation, and the chapter's delivery removes
  the line when done. So the site can publish `main` at any time.
* **Guided project:** `JCKodel/focus-kit-clinic`, worked on locally in the
  sibling directory `../focus-kit-clinic`. A chapter that changes it ends
  with the annotated tag `book-v1/<chapter-slug>` on the commit it quotes
  (message "One Page at a Time, chapter <slug>"); a chapter that changes
  nothing has no tag. `book-v1/start` is the empty starting point. A
  published tag never moves. The agent stages there too and never commits,
  tags or pushes. Order: the author commits and pushes the chapter's tag
  first, then the chapter's `make verify` can go green, because the link
  check opens every tag URL the chapter cites. A delivery of this book
  that is not a chapter may advance the guided project (the first is
  `clinic-milestone-1`); the author commits each of its deliveries with
  the kit's message and no tag, and the next chapter tag includes those
  commits.
  * **A recorded clinic run** (the first is `clinic-milestone-1`, the
    second `clinic-orchestrator-tests`): each clinic delivery takes five
    steps, run from the clinic's root, one turn at a time.
    1. `/propose`, headless, fresh: `claude -p "/propose <slug>"` with the
       common flags. Every round of questions is answered with
       `--continue` and `Your call. Say what you chose and why.`, unless
       the delivery's page gives a brief.
    2. Page review: the author decides which holes to send; each request
       goes to the same session with `--continue`, word for word as the
       author approved it. "None" is a valid review. The page is never
       edited by hand.
    3. `/apply`, headless, fresh: `claude -p "/apply <slug>"` with the
       common flags and `--allowedTools "Bash(npm *)" "Bash(npx *)"
       "Bash(node *)" "Bash(mkdir *)" "Bash(cp *)" "Bash(git add *)"
       "Bash(git status *)" "Bash(git diff *)"` `--disallowedTools
       "Bash(npm run dev*)"`.
    4. Staged review: as step 2, to the `/apply` session. Nothing in the
       clinic is edited by hand.
    5. The author commits with the kit's message, no tag, and pushes.

    Common flags: `--model claude-opus-5-5 --setting-sources project
    --strict-mcp-config --permission-mode acceptEdits --permission-prompts
    none --output-format stream-json --verbose`.

    Exits: a denied call is recorded, never retried by another route; a
    run that cannot finish or a verify that stays red stops the delivery,
    and the author decides on a second run; a line `/propose` splits off
    is built in the same delivery only if the page says so; a note the
    host writes outside the repository is deleted after each delivery.

    The record, `work/done/<slug>-run/`: `README.md` with host version,
    model, the clinic's first and last commit, the flags and the
    allowlist, then per clinic delivery the commands, the answers, the
    author's requests word for word (or "none"), the denied calls, what
    diverged and the commit; `<clinic slug>/turn-N.txt`, every turn, text
    blocks byte for byte and tool calls as `[tool <name>] <path or
    command>`; `verify.txt`, `npm run verify` on the clinic's last commit.
    Paths are relative to the clinic's root; session ids are left out.
* **Brownfield project:** the fork `JCKodel/clahub`, worked on locally in
  the sibling directory `../clahub`, on the branch `book` created from
  `book-v1`, the frozen upstream (ADR-0009). A chapter that changes it ends
  with the annotated tag `book-v1-<chapter-slug>` on the commit it quotes
  (a hyphen, since git refuses `book-v1/<slug>` beside the tag `book-v1`),
  with the same message and the same order as the guided project. The
  agent stages there too and never commits, tags or pushes. A delivery of
  this book that is not a chapter may change the fork too (the first were
  the kit's installs); the author commits it on `book` with the fork's
  message style and no tag.
* **Git:** trunk. The agent stages; it never commits or merges.

## 6. Commit

The agent stages and suggests the message; the person commits after
reviewing. Imperative subject up to 72 characters, scope in parentheses
when it helps; body up to five one-line bullets, the highlights and not
the reasoning; last line points to `work/done/<slug>.md`, where the
reasoning lives.

## 7. What this process does not have

No formal spec, no spec delta, no change folder, no numbered tasks, no
gate before implementation, no specialized subagent, no tool the
deliveries did not ask for. When one of these is proposed, the question
is: which concrete error would it have caught? The answer names an error
that happened.

## 8. Closing a milestone

The last line of every milestone but a `.1` is its review,
`<milestone>-review`, a delivery like the others: /propose writes its page, /apply runs it. It
checks the milestone's paragraph clause by clause against what the
deliveries built, and reviews the code with what the host offers. A clause
no delivery answers is a finding. The review fixes nothing; the person
decides each finding, confirmed or rejected, with a reason.

Each confirmed finding becomes a `[ ]` line in a new milestone placed
right after the reviewed one, numbered with `.1` (M3 is followed by M3.1),
with its own paragraph, so the lines wait for /propose and nothing
renumbers. No confirmed finding, no new milestone. A finding is never a
fix in the middle of the next milestone.

A milestone has at most one round of fixes: `.1` is the last. A `.1`
has no review of its own: it closes when its lines are `[x]` with their
proof, and whatever it missed is found by the review of the next
milestone. (Rule written after M4, whose `.1` review opened M4.2:
`m4.2-review` was the last review run under the old rule, and the author
rejected its four findings to close M4.)

For a milestone of chapters, the review is a fresh session that reads the
book from its start to the end of the part, in both editions, and asks the
product questions of docs/00, above all: does every sentence carry value,
and is anything the reader needs missing? It checks the milestone's
paragraph clause by clause against the chapters that teach it, and its
findings may fall in any chapter it read.

**The recipe of a milestone review** (the first is `m3-review`, the second
`m4-review`, which wrote it down). The delivery is `m<n>-review`; its page
names the model, the last chapter and the paragraph.

1. Before the run: `main` with only the review's own `/propose` changes
   uncommitted; `make verify` green.
2. What the review reads, in order: docs/00 (audience, values, product
   questions), docs/04 §"Writing the book" and §"Prose rules", then the
   chapters from `00-` to the last chapter of the part, each chapter
   English then Portuguese. The milestone's paragraph is quoted in the
   request. Nothing else from docs/, work/ or scripts/; the guided
   project's tags only as the links the chapters print.
3. Turn 1, the review, headless, detached, from the repository's root:
   `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1 nohup claude -p "<request>" --model
   <model> --setting-sources project --strict-mcp-config --permission-mode
   default --permission-prompts none --output-format stream-json --verbose
   --allowedTools "Read" "Glob" "Grep"`. Auto-memory is off because a
   reader does not have the host's notes on this project.
4. The request, in English, recorded word for word, says: read as a reader
   who has only the earlier chapters; edit nothing; each finding names
   where it is (file and line, one or both editions), the product question
   or the paragraph it fails, what is wrong and what the reader loses; a
   finding may fall in any chapter read; do not report what `make verify`
   guards; spend attention on value, on what is missing, on whether each
   chapter can be followed from the earlier ones alone, on whether the
   code a chapter prints can be followed from what it says, and on whether
   the Portuguese means what the English means; check the paragraph clause
   by clause. It asks for this shape: `### F<n>. <summary>` with the bullets
   Where, Question, What, Reader; then `## Paragraph`, one line per clause,
   `<clause>: <chapter §section> · <tag or "no tag">` or
   `<clause>: FINDING F<n>`.
5. The book's `/apply` session checks each finding against the text and
   gives its assessment; the author decides each one,
   `F<n>: confirmed|rejected, <reason>`, in one sentence. Nothing is fixed.
6. Turn 2, with `--resume <the review's session id>`, never `--continue`,
   which takes the directory's most recent conversation (in `m3-review` it
   reached the `/apply` session): the decisions, word for word as the
   author approved them, and the request to write the confirmed findings
   into docs/06 as `## M<n>.1. What the review of M<n> found`, after the
   milestone and before the next, with a paragraph "When this milestone
   closes, …", one `[ ]` line per finding and no review line,
   and to stage it. A finding an
   existing line covers adds no line; that line gains words only if the
   finding adds something. Flags as turn 1, with `--permission-mode
   acceptEdits --allowedTools "Read" "Edit" "Bash(git add
   docs/06-Queue.md)" "Bash(git diff *)" "Bash(git status *)"`.
   Corrections are further turns to the same session, recorded. docs/06
   is not edited by hand for these lines.
7. No confirmed finding: no new milestone; the record says so.
8. A denied call is recorded, never retried by another route. Notes the
   host writes outside the repository are deleted after the run. Session
   ids and absolute paths are left out of the record.
9. The record, `work/done/<slug>-run/`: `README.md` (date,
   `claude --version`, model, the book's commit, commands, allowlists, the
   paragraph check one line per clause, counts read, confirmed, rejected
   and already queued, denied calls, what diverged); `turn-N.txt` (text
   blocks byte for byte, tool calls as `[tool <name>] <relative path or
   command>`); `findings.md` (as reported, byte for byte); `decisions.md`
   (each request, word for word); `queue.diff` (docs/06 before and after
   the lines).

A milestone that also changed the guided project gets a code review of
its own, `m<n>-code-review`, a separate delivery placed right after its
review, whose findings join the same `M<n>.1`.

**The recipe of a milestone's code review** (the first is
`closing-a-milestone`, chapter 12's review of the clinic's milestone 1;
the second `m4-code-review`, which wrote it down). The delivery is
`m<n>-code-review`; its page names the model and the range.

1. The range: from the previous milestone's last chapter tag to this
   milestone's last chapter tag, three dots, `<from>...<to>`, the form of
   Claude Code's documentation. When the milestone's last change to the
   guided project has no chapter tag, the range ends at that commit, by
   its short hash. A commit at the start of the range that touches only
   the kit's files, as a kit update does, is left out by starting the
   range on it, and the README names it. The README says how many commits
   the range holds, names any commit of the milestone past its end, and
   says whether it is reviewed and why. (The untagged end and the kit
   commit left out: first `m4.1-code-review`.)
2. Before the run: the book as step 1 of the recipe above; the guided
   project on `main`, clean, equal to `origin/main`, with nothing in
   `src/` past the range's end.
3. Turn 1, the review, headless, detached, from the guided project's
   root: `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1 nohup claude -p "/code-review
   high <range>" --model <model> --setting-sources project
   --strict-mcp-config --permission-mode default --permission-prompts none
   --output-format stream-json --verbose --allowedTools "Bash(git diff *)"
   "Bash(git log *)" "Bash(git show *)" "Bash(git status *)" "Bash(npm *)"
   "Bash(npx *)"`. The review edits nothing.
4. The book's `/apply` session checks each finding against the guided
   project's code and documents and gives its assessment; the author
   decides each one, `<n>: confirmed|rejected, <reason>`, in one sentence,
   and approves the request word for word before it is sent. Nothing is
   fixed.
5. Turn 2, with `--resume <turn 1's session id>`, from the guided
   project's root, flags as turn 1 plus `--add-dir ../focus-kit-book`,
   with `--permission-mode acceptEdits --allowedTools "Read" "Edit"
   "Bash(git -C ../focus-kit-book add docs/06-Queue.md)" "Bash(git -C
   ../focus-kit-book diff *)" "Bash(git -C ../focus-kit-book status *)"`:
   the decisions, word for word, and the request to write each confirmed
   finding as `[ ] clinic-<slug>  <what the code does afterwards>, by a
   recorded run` in the book's `M<n>.1`, after its book lines (the
   milestone the review opened: after M4.1 it is M4.2), with one
   clause in its paragraph, and to stage it. Findings that one change
   settles may share one line, as the author decides (first
   `m4-code-review`, second `m4.1-code-review`). If the milestone review
   found nothing and `M<n>.1` does not exist, turn 2 creates it as step 6
   above says. A finding a line of the guided project's own queue covers
   still gets its line, which names that line and what the finding adds;
   the guided project's queue is never touched. Corrections are further
   turns to the same session, recorded.
6. If `--add-dir` does not allow turn 2, or the session cannot or will not
   write the lines, a fresh interactive session in the book gets the same
   request, recorded as a turn. "Already queued" in either queue, denied
   calls, notes of the host (in both repositories' memory folders) and the
   record follow steps 6 to 9 above; the README adds the range, the target
   form and the `--add-dir` check.
