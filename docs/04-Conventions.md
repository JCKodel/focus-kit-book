# Conventions

## Languages

* Process documents (`docs/`, `work/`, ADRs, commit messages): English.
* Identifiers, file names and slugs of this repository: English. The Portuguese edition's example code has Portuguese names (§Writing the book, Evidence).
* The book: English is the source (`book/en/`), Portuguese the translation (`book/pt/`, Brazilian Portuguese).
  A change to one edition is a change to both, in the same delivery (ADR-0004).
* The Portuguese edition uses the Portuguese term of docs/03, and no synonym.
* The README exists in both languages, `README.md` and `README.pt.md`, with the same sections in the same order; a change to one is a change to both, in the same delivery.

## Writing the book

* **Value first.** The chapter's first paragraph says what the reader can do after it.
* **Teach, do not report.** A chapter is a lesson, not the log of a run: it starts from the reader's problem, says what the tool or practice is, why it exists and how it solves that problem, and only then how to use it. A run of the guided project or a case is evidence at the point it proves something (a real output, a number), never the thread of the chapter: who ran what, in which order, with which flags stays in the run's record (first: `worktrees`, rewritten at the author's request).
* **No filler.** Cut every sentence that does not carry information: no recap of the previous chapter, no announcement of the next. Never cut useful content, and never pad, to reach a length; there is no length target.
* **Voice.** The author tells stories in the first person ("when Ninjobs stalled, I..."); instruction speaks to the reader as "you".
* **One sentence per line** in the Markdown source.
* **No em dash** in any text a reader reads, in either edition. Use a comma, a colon, parentheses or a new sentence.
* **Anti-AI prose rules**: the patterns that make text read as machine-written, in §Prose rules, checked by `make verify`.
* **No runs.** No chapter narrates a run: no brief, no transcript of an agent's turns, no diff, no `git status`, no headless flag, no commit hash as evidence (ADR-0017).
  The record of how a number was counted stays in `work/done/`, and the note points to it.
* **Evidence.** Every number says where it comes from: a primary publication, a record of this book's runs, or, for a private case, how the author counted it.
  Every quoted artifact (a page, a queue line, a rules file, a command's output) is real; a page or a queue written for the chapter as an example says so where it appears.
  The Portuguese edition shows an English prose artifact (a rules file, a page) translated, and says before it that the original is in English.
  Since `author-review-1`, the Portuguese edition's code speaks Portuguese too: every name the code invents (functions, types, variables, fields, files, folders, slugs, table columns, test names, string messages, comments) is translated, identifiers without accents (`emprestar`, `RecusaDeEmprestimo`, `TemLivrosEmAtraso`), and the vocabulary of docs/03 §running example gives the words; the language's own words (`function`, `return`), library APIs (`describe`, `it`, `expect`, `new Date`), `Result`, `ok`, `err` and their fields, and names an external format fixes (a log's fields, `features/`) stay as they are, and the text says so where such a name appears (chapter 23's log fields). Commands and their output stay as they are.
  Chapter 4, at the first code block, says once that the names are in Portuguese.
* **Context before an excerpt.** A reader who has read only the previous chapters understands every artifact shown without opening anything else (docs/00 product question 5).
  Before it, the text gives what the artifact is about: the project, the problem it answers, where it comes from.
  An excerpt is a whole unit that means something on its own (a page's section, a queue's milestone), never a loose line that leans on the lines around it.
* **Teach, do not only show.** After an artifact, one sentence says what the reader should see in it; a term, a name or a choice the reader has not met yet is explained where it appears, or the text says which chapter explains it.
  An organization, a study or a tool is introduced in a few words the first time it is named (METR, DORA, Chroma, Liu's paper in chapters 1 and 2).
  No sentence is only a pointer to a later chapter ("A project writes its product in docs/00 (chapter 10)." said nothing the reader could use yet): a forward pointer follows a sentence that already says something, as a parenthesis or as "chapter 10 shows that document"; first occurrence, the prologue in `author-review-1`.
* **Say it where the doubt is born.** What a thing is for, and what the team gets from it, is said where the thing is introduced, never saved for `## What the team gains`, which sums up and gives the evidence (first: chapter 7's orchestrator, whose reason, one test per event, was said only in the gain, `author-review-2`).
* **Chapter pointers** (since `author-review-2`, which cut 65 of 179 per edition). A pointer forward names a term the reader has not been taught, once per chapter for each target. A pointer back stays only where the sentence leans on a specific detail worth reopening (chapter 5's red and green cycle), where it names a term of chapters 4 to 8 for the reader who skipped them (docs/00 §Audience), or where the pointers are the content, a map of where each step is taught (chapter 9's rules, chapter 24's roles and steps); a pointer back that only repeats what a reader in order has just read is cut. A chapter is found by the number in its title; in the PDF and the EPUB a chapter link prints in the text's color, and on the site it stays a link.
* **Width of a block.** A text or Markdown artifact in a code block, a table, a queue, a folder layout, a log, keeps to 74 columns, what an A5 page holds at the PDF's code size, so no row wraps (first: chapter 18's work record, which the PDF broke). TypeScript may wrap.
* **A note box** is a blockquote whose first words are bold, `> **Note.** ...` (pt: `> **Nota.**`; `**Caution.**` / `**Cuidado.**` for a warning), one paragraph, one sentence per line; the site, the PDF and the EPUB style it as a box (`site.css`, `pdf.css`, `epub.css`).
  It holds a definition or a warning the reader needs at that point and the section's flow does not carry: first, chapter 3's behaviour; second, chapter 4's caution on an agent that grows the process.
  It is the one box syntax pandoc and MkDocs both render; `!!!` and `:::` each break in one output.
* **A gain per chapter.** Every chapter has the section `## What the team gains` (pt: `## O que o time ganha`) before its key points: what a team or a project gains, with a number or a sourced claim, or one sentence saying the gain has no number (docs/00 product question 7).
* **Code** is TypeScript only, written for the chapter, short (as a rule under 25 lines a block), tab-indented, on the book's running example, the lending library (docs/03); chapter 4, at the book's first code block, says once that the examples are written for the book (and, in Portuguese, that their names are in Portuguese), and chapter 2's rules file, the one prose artifact before it, says so itself.
  Code is never presented as the output of a run.
* **Private cases** appear only as Case A and Case B; docs/03 §Entities and invariants says what may never appear.
  Case B did not run on the process, and every passage that uses it says so or reads so.

## Prose rules

A reader who spots one of these patterns stops trusting the sentence around it, because it reads as written by a machine and not checked by a person.
`scripts/check_prose.py` reads this section and nothing else: each `### <id>` is a rule, its first line is the message a finding prints, and each backtick span on a `* en:`, `* pt:` or `* both:` line is one entry.
A plain entry matches as a whole word, regardless of case; `re:<pattern>` is a Python regular expression, also regardless of case.
`'` and `’` are both apostrophes, so the entries that hold one accept either.
It checks `book/en/` and `README.md` with the `en` and `both` entries, `book/pt/` and `README.pt.md` with the `pt` and `both` entries; code, link targets, HTML comments and the front matter are not checked.
Adding an entry here is enough to make the check use it.

### filler

say it; do not announce, recap or clear your throat

* en: `re:in this chapter,? (we|you) will`, `as we saw`, `as we have seen`, `as mentioned`, `it is worth noting`, `re:it(’|')s worth noting`, `it is important to note`, `re:let(’|')s dive`, `without further ado`, `in conclusion`, `in summary`, `to sum up`
* pt: `re:neste capítulo,? (vamos|você vai)`, `como vimos`, `como mencionado`, `vale ressaltar`, `vale notar`, `vale destacar`, `re:é importante (notar|destacar|ressaltar)`, `sem mais delongas`, `em conclusão`, `em resumo`, `resumindo`

### inflated

use the plain word

* en: `re:\bdelv(e|es|ed|ing)\b`, `tapestry`, `testament to`, `re:\bseamless(ly)?\b`, `re:\bleverag(e|es|ed|ing)\b`, `re:\bunlock(s|ed|ing)?\b`, `re:\bempower(s|ed|ing|ment)?\b`, `pivotal`, `game-changer`, `game changer`, `ever-evolving`, `fast-paced`, `cutting-edge`, `realm`
* pt: `re:\bmergulh(ar|amos|e|o)\b`, `tapeçaria`, `re:\balavanc(ar|a|am|ando)\b`, `re:\bpotencializ\w*`, `re:\bempoder\w*`, `divisor de águas`, `em constante evolução`, `de ponta`

### not-but

say what it is; do not set it against what it is not

* en: `re:\bnot (just|only|merely)\b.*\bbut\b`, `re:\bit(’|')?s not\b.*\bit(’|')?s\b`, `re:\b(is|are)n(’|')?t (just|only|merely)\b`
* pt: `re:\bnão (é |são )?(apenas|só|somente|simplesmente)\b.*\b(mas|é|são)\b`

### reveal

state the point; do not stage it with a question or a teaser

A line that is only a question of up to three words ("Why?", "The result?") is a teaser.

* en: `re:^[a-z]\w*(\s\w+){0,2}\?$`, `re:here(’|')s (the thing|why|how|what)`, `here is the thing`
* pt: `re:^[a-zà-ú]\w*(\s\w+){0,2}\?$`, `eis o segredo`, `eis por que`, `eis o porquê`

### intensifier

cut the intensifier; the fact carries the weight

* en: `truly`, `incredibly`, `absolutely`, `genuinely`
* pt: `verdadeiramente`, `incrivelmente`, `absolutamente`, `genuinamente`

### exclamation

end with a full stop

The entry skips `![` (an image), `!!!` (an admonition) and `<!--` (a comment).

* both: `re:(?<![!<])!(?![!\[-])`

### emoji

remove the emoji

* both: `re:[\U0001F300-\U0001FAFF☀-➿]`

## Chapter shape

Every chapter, in both editions, has this shape (terms from docs/03); the prologue and every chapter, starting at chapter 1, follow it:

```
---
status: draft            only while the chapter is not done; the delivery removes the line (docs/05 §5)
---

# <N>. <Title>           H1, the chapter's number and title (`# 7. FOCUS: the four pieces`); the prologue is `# Prologue: <Title>` (pt: `# Prólogo: <Título>`); the navigation and the table of contents show it, so "chapter 7" in the text can be found

<opening>                first paragraph, no heading, at most three sentences: what the reader can do after it

## <Section>             the content, in H2 sections (H3 inside when needed); as many as the value takes

## What the team gains   pt: ## O que o time ganha; one short section; every chapter

## Key points            pt: ## Pontos-chave; at most five bullets; every chapter

[^<key>]: <source>       source notes, at the end of the file
```

There are no exercises (ADR-0017).

* One sentence per line in the source: a convention, not a check (no error it would have caught has happened, docs/05 §7).
* Source notes: a note only where the reader gains something to open (a publication, a tool's documentation, a file of this book's repository or its runs) or a count to repeat. Every number and every quoted claim from such a source carries `[^<key>]` at the claim; a source cited again in the chapter reuses the key, and the PDF and the EPUB print its note once.
  No note points to a commit, a diff or a file of focus-kit's repository: where the text quotes or states a rule of the kit, the sentence names the file in plain words (`SETUP.md` §3.4, the file of `/apply`).
  A private case has no note (since `author-review-1`; before it, each chapter carried a `[^ninjobs]`, `[^case-a]` or `[^case-b]` listing how every number was counted, and the author found them noise): the prologue says once, at the first mention of Ninjobs and of Case A, that their repositories are private and that every number about them was counted by the author.
  A chapter adds a parenthesis in the text only where the method matters to a reader repeating a count on their own project (chapter 3's `wc -l` over the tool's folder), and a reason or a story a chapter needs goes in the text or a note box, never in a note.
  The key is lowercase `[a-z0-9-]+`, the same in both editions (`[^metr-2025]`).
  The definition is `[^<key>]: <Author or organization>, "<Title>", <year>. <URL>`, with the title in its original language in both editions; the URL is written in angle brackets, `<https://...>`, so the site, the PDF and the EPUB make it a link.
  A publication without a date carries `accessed YYYY-MM-DD` in place of `<year>` (pt: `acesso em YYYY-MM-DD`).
  A tool cited at a tag or a release carries its version in place of `<year>` (`[^spec-kit]: GitHub, "Spec Kit", v1.0.11. <URL>`).
  A quotation is in quotation marks and italic, `"*...*"`.
  The English edition keeps the publication's words; the Portuguese edition gives only their translation, and the original is at the source in the note.
* `mkdocs.yml` enables the `footnotes` Markdown extension so the site renders them; pandoc reads the same syntax for PDF and EPUB.
* Appendices (`A<n>-`) are out of this shape until the first appendix delivery fixes theirs.

## Files

* Chapters: `book/<edition>/NN-<slug>.md`; appendices `A<n>-<slug>.md`.
* The prologue is `00-<slug>.md`: the prefix only sorts it first, the text calls it the prologue, and it is never called chapter 0.
* Images: `book/assets/NN-<what>.png|svg`, with no text inside, so one image serves both editions.
  A diagram, whose labels are words, is an SVG written by hand, one per edition, `book/assets/NN-<what>.<edition>.svg`, with an opaque light background so it reads in the dark theme and fonts that fall back to a generic family; each edition links its own, `![<alt>](../assets/NN-<what>.<edition>.svg)`, with the alt text in the edition's language, written as a caption, since the PDF and the EPUB print it under the image.
  The stylesheets (`book/assets/site.css`, `pandoc/pdf.css`, `pandoc/epub.css`) give every PNG a thin border and a reduced width; since `rewrite` the chapters show no screenshot.

## Tests

There is no product code to test.
The checks are the tests: site build (strict), edition parity, em dash, prose rules, links, disclosure scan.
Each lives in `scripts/` and runs from `make verify`.
The strict build catches a broken internal link; `links` catches an external URL in either edition, either README or `mkdocs.yml` that answers 404, 410, another 4xx or a 5xx, whose host or connection fails, or that times out. 401, 403 and 429 pass, since the server exists; URLs in code, HTML comments and the front matter, under `site_url`, on `localhost`, `127.0.0.1` and `example.*` are not fetched.
The disclosure scan also reads every commit message in the history, and the hooks of `make hooks` run it on each commit's staged files and message before the commit exists: a commit message once carried a term of the list, which a scan of the files cannot see.
The em dash check skips `work/done/*-run/`, the folders of a recorded run: they keep the tools' and the agent's output byte for byte as a chapter's evidence (Spec Kit, OpenSpec and focus-kit for chapter 3, the first; the host's messages in chapter 7's `/brainstorm` run, the second), and no reader of the book reads it there; the disclosure scan still covers them.
A new check enters only when it names the error it would have caught (docs/05 §7).

## Commit messages

Imperative subject up to 72 characters, `<type>(<slug>): <subject>`, where type is `feat`, `fix`, `docs` or `chore`.
Body up to five one-line bullets.
Last line: `work/done/<slug>.md`.
