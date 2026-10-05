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
leaves the queue; it changes mark, at the moment the work changes, so the
queue shows what is happening while it happens:

| Mark | Means | Set by |
|---|---|---|
| `[ ]` | not defined | the conversation that adds the line |
| `[~]` | being defined | /propose, when it starts |
| `[>]` | defined, `work/<slug>.md` exists | /propose, when the page is written |
| `[*]` | being built | /apply, when it starts |
| `[x]` | done, page in `work/done/` | /apply, with verify green |
| `[?]` | waiting | any session, in the three cases below |

A line waits when the person says it is blocked, when it needs an answer
that was asked and not given, or when it needs another line done first,
such as a fix found in the middle of an /apply. The reason goes at the end
of the line, `· blocked: <reason>` or `· blocked: after <slug>, <slug>`.
Any mark before `[x]` can become `[?]`. The line leaves `[?]` when the
reason is resolved: the person says so, the session that records the
answer clears it, or /apply clears it when it marks `[x]` the last line of
an `after`. It goes back to `[>]` when its page exists and `[ ]`
otherwise, and the next command marks it again. These are the marks of
focus-kit 2026.10.05 (ADR-0018).

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
    push. A delivery leaves nothing to do: the author's push publishes.
  * GitHub Release: PDF and EPUB in both editions, built by Actions on a
    `v*` tag. Only the author tags.
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
* **Git:** trunk. The agent stages; it never commits or merges.

## 6. Commit

The agent stages and suggests the message; the person commits after
reviewing. Imperative subject up to 72 characters, scope in parentheses
when it helps; body up to five one-line bullets, the highlights and not
the reasoning; last line points to `work/done/<slug>.md`, where the
reasoning lives.

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
