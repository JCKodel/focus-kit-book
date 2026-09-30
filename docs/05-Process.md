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
* **Case A and Case B:** every passage drawn from them is listed in the
  delivery's page for the author's approval before the chapter is done
  (docs/00 OD-3), and `make scan` is green.
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
* **Guided project and brownfield project:** retired by `rewrite`
  (ADR-0017). The repositories `JCKodel/focus-kit-clinic` and
  `JCKodel/clahub` and their published tags stay as they are and no
  chapter cites them; the recorded runs in `work/done/*-run/` stay as the
  history of how the book's numbers were counted, and a chapter's note may
  point to one. The recipe of a recorded run that this section held is in
  the history of this file, at the commit before `rewrite`.
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

A milestone that also changed the guided project got a code review of
its own, `m<n>-code-review`, a separate delivery placed right after its
review, whose findings joined the same `M<n>.1`. Since `rewrite` the book
has no guided project (ADR-0017), so no milestone has a code review; its
recipe is in the history of this file, at the commit before `rewrite`.
