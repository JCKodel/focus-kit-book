# Conventions

## Languages

* Process documents (`docs/`, `work/`, ADRs, commit messages): English.
* Identifiers, file names and slugs: English.
* The book: English is the source (`book/en/`), Portuguese the translation (`book/pt/`, Brazilian Portuguese).
  A change to one edition is a change to both, in the same delivery (ADR-0004).
* The Portuguese edition uses the Portuguese term of docs/03, and no synonym.
* The README exists in both languages, `README.md` and `README.pt.md`, with the same sections in the same order; a change to one is a change to both, in the same delivery.

## Writing the book

* **Value first.** The chapter's first paragraph says what the reader can do after it.
* **No filler.** Cut every sentence that does not carry information: no recap of the previous chapter, no announcement of the next. Never cut useful content, and never pad, to reach a length; there is no length target.
* **Voice.** The author tells stories in the first person ("when Ninjobs stalled, I..."); instruction speaks to the reader as "you".
* **One sentence per line** in the Markdown source.
* **No em dash** in any text a reader reads, in either edition. Use a comma, a colon, parentheses or a new sentence.
* **Anti-AI prose rules**: the patterns that make text read as machine-written, in §Prose rules, checked by `make verify`.
* **Evidence.** Every number cites its source: a primary publication, or the case's recorded artifact.
  Every artifact shown (a page, a queue, a command output) comes from a real run.
* **Code** is TypeScript only, quoted from a tag of the guided project's repository with its path.
* **Private cases** appear only as Case A and Case B; docs/03 §Entities and invariants says what may never appear.

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

Every chapter, in both editions, has this shape (terms from docs/03); chapter 1 is the first to follow it:

```
---
status: draft            only while the chapter is not done; the delivery removes the line (docs/05 §5)
---

# <Title>                H1, the chapter title; the navigation shows it

<opening>                first paragraph, no heading, at most three sentences: what the reader can do after it

## <Section>             the content, in H2 sections (H3 inside when needed); as many as the value takes

## Key points            pt: ## Pontos-chave; at most five bullets; every chapter

## Exercises             pt: ## Exercícios; Part II on only; absent in Part I
### Exercise N.M         pt: ### Exercício N.M; N the chapter number, M from 1

[^<key>]: <source>       source notes, at the end of the file
```

* One sentence per line in the source: a convention, not a check (no error it would have caught has happened, docs/05 §7).
* Source notes: every number and every quoted claim from a publication carries `[^<key>]` at the claim.
  The key is lowercase `[a-z0-9-]+`, the same in both editions (`[^metr-2025]`).
  The definition is `[^<key>]: <Author or organization>, "<Title>", <year>. <URL>`, with the title in its original language in both editions.
  A publication without a date carries `accessed YYYY-MM-DD` in place of `<year>` (pt: `acesso em YYYY-MM-DD`).
  A quotation keeps the publication's words; the Portuguese edition quotes an English source in English and follows it with its translation in parentheses.
  For a case, whose repository the reader cannot open, the definition says it is private and how each number was obtained, so the reader knows what is claimed and can repeat the count on their own project; it names no private path: `[^ninjobs-adr-0022]: Ninjobs, a private repository, counted by the author over its history up to 2026-08-29, when its ADR-0022 dropped OpenSpec: ...`
* `mkdocs.yml` enables the `footnotes` Markdown extension so the site renders them; pandoc reads the same syntax for PDF and EPUB.
* Appendices (`A<n>-`) are out of this shape until the first appendix delivery fixes theirs.

## Files

* Chapters: `book/<edition>/NN-<slug>.md`; appendices `A<n>-<slug>.md`.
* Images: `book/assets/NN-<what>.png|svg`, with no text inside, so one image serves both editions.
  A diagram, whose labels are words, is an SVG written by hand, one per edition, `book/assets/NN-<what>.<edition>.svg`, with an opaque light background so it reads in the dark theme and fonts that fall back to a generic family; each edition links its own, `![<alt>](../assets/NN-<what>.<edition>.svg)`, with the alt text in the edition's language, written as a caption, since the PDF and the EPUB print it under the image.

## Tests

There is no product code to test.
The checks are the tests: site build (strict), edition parity, em dash, prose rules, links, disclosure scan.
Each lives in `scripts/` and runs from `make verify`.
The strict build catches a broken internal link; `links` catches an external URL in either edition, either README or `mkdocs.yml` that answers 404, 410, another 4xx or a 5xx, whose host or connection fails, or that times out. 401, 403 and 429 pass, since the server exists; URLs in code, HTML comments and the front matter, under `site_url`, on `localhost`, `127.0.0.1` and `example.*` are not fetched.
A new check enters only when it names the error it would have caught (docs/05 §7).

## Commit messages

Imperative subject up to 72 characters, `<type>(<slug>): <subject>`, where type is `feat`, `fix`, `docs` or `chore`.
Body up to five one-line bullets.
Last line: `work/done/<slug>.md`.
