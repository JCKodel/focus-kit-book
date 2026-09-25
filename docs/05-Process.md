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
built, `[x]` done. Edited by conversation in any session.

## 5. This project

* **Documentation language:** English. Identifiers in English. The book
  itself: English source, Brazilian Portuguese translation, same delivery.
* **Verify:** `make verify`, which runs the strict site build, edition
  parity, the em dash check, the prose rules, the link check and the
  disclosure scan. Green before anything is declared done. Created by
  `site-skeleton` (build, parity, em dash); `disclosure-scan`,
  `prose-rules` and `link-check` add their checks to it.
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
  deliveries, no screenshot: the proof is verify green. A chapter that
  brings a kind of content the build has not shown before (its first
  diagram, say) also proves it renders: screenshots of the site in light
  and dark and of the PDF, in both editions.
* **Disclosure:** the disclosure list lives outside the repository, at
  `~/.config/focus-kit-book/denylist.txt` or the path in `FKB_DENYLIST`;
  in Actions it comes from the secret `DISCLOSURE_DENYLIST`. No term of
  that list, no private path and no source folder name is ever written in
  this repository, its pages or its commit messages. Created by
  `disclosure-scan`.
* **Publish policy:** the agent never pushes, tags, releases or uploads.
  A chapter that is not done carries the draft marker, the line
  `status: draft` in its front matter, in both editions; the site shows a
  banner and a mark in the navigation, and the chapter's delivery removes
  the line when done. So the site can publish `main` at any time.
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

When a milestone closes, review the whole with what the host offers, and
each confirmed finding becomes a line in the queue, not a fix in the middle
of the next milestone.

For a milestone of chapters, the review reads the part end to end in both
editions and asks the product questions of docs/00, above all: does every
sentence carry value, and is anything the reader needs missing?
