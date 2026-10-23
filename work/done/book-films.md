# book-films

**Objective.** A reader of either edition finds the two films that show focus-kit at work in the edition's language, on the repository's README, on the site's home page and in chapter 8 where the kit is installed, with the other language's playlist one link away on the README and the home.

**Behaviour.**
* A reader opens `README.md` on GitHub: under "Read", after the site and the Releases, one bullet links the English engineering film and the English business film, each named by what it shows, and one bullet links the Portuguese playlist; each link opens on YouTube.
* A reader opens `README.pt.md`: under "Ler", the same two bullets in Portuguese link the Portuguese films and the English playlist.
* A reader opens the English site home (`/focus-kit-book/`): below "Free, in English and Portuguese.", a short paragraph links the two English films and the Portuguese playlist.
* A reader opens the Portuguese site home (`/focus-kit-book/pt/`): the same paragraph in Portuguese links the two Portuguese films and the English playlist.
* A reader of chapter 8, §Install (pt: §Instalação), reads, in a paragraph of its own right after the one that ends "approve both." (pt: "aprove os dois."), one sentence saying a film shows this install and the four commands at work, with a source note whose address opens the edition's engineering film; in the PDF and the EPUB the note prints the address.
* Nowhere does a reader find a description of the project the films show, of its client, of the company on screen or of what the films run: each film is named by one phrase, the engineering film showing the install and the four commands, the business film the method on a project's documents without code (docs/00 §Cases, ADR-0017, docs/04 **No runs**).
* Edge: no link of an edition points to a film of the other language; the only cross link is the other language's playlist, on the README and the home, named by its language, never by its YouTube title (the English playlist is titled after the engineering film, the Portuguese one after the business film).
* Edge: chapter 8's sentence carries no number from the film (no length, no count), so it needs no source beyond the note.
* Edge: a film removed or made private: YouTube still answers 200 for a removed video, so `links` stays green; the author learns it from the channel or the kit's README, not from verify (Out of scope).
* Failure: a link mistyped, or a playlist id cut short, answers 404 or a host failure and `make verify` fails at `file:line: links: <url>: <reason>`.
* Failure: a heading added to one README and not the other fails parity; this delivery adds no heading, only bullets in the existing "Read"/"Ler" section.
* Failure: the note cited in one edition of chapter 8 and not the other fails parity.

**Contract.**
* Links, checked on 2026-10-23 (each answered 200; the playlists hold exactly the two films of their language):

| What | Edition | URL |
|---|---|---|
| engineering film, 21 min | en | https://youtu.be/Ywp1iUtEVyY |
| business film, 13 min | en | https://youtu.be/4cqpi5CfnVc |
| engineering film, 20 min | pt | https://youtu.be/r0fk_yVHgO4 |
| business film, 12 min | pt | https://youtu.be/gnLcNYOI2MU |
| English playlist | linked from pt | https://youtube.com/playlist?list=PLCoT-CR09np8 |
| Portuguese playlist | linked from en | https://youtube.com/playlist?list=PLd13b_CIAdxo |

* Files: `README.md`, `README.pt.md` (bullets inside "Read"/"Ler", no new heading, so parity of headings holds, docs/04 §Tests); `book/en/index.md`, `book/pt/index.md` (one paragraph after the last line, same shape in both); `book/en/08-install-and-hosts.md`, `book/pt/08-install-and-hosts.md` (one paragraph in §Install and one note definition at the end of the file); `docs/00-Product.md` §Mechanics, Cases, already written by this /propose (below).
* Chapter 8's sentence, to be fitted by /apply to the prose rules and approved by the author:
  * en: `A film shows this install and the four commands at work.[^focus-kit-film]`
  * pt: `Um vídeo mostra esta instalação e os quatro comandos em uso.[^focus-kit-film]`
* Chapter 8's note, key `focus-kit-film` in both editions, in the form of docs/04 §Chapter shape, Source notes, the title in the film's own language:
  * en: `[^focus-kit-film]: J.C. Ködel, "focus-kit in practice: coding agents with a process (engineering)", 2026. <https://youtu.be/Ywp1iUtEVyY>`
  * pt: `[^focus-kit-film]: J.C. Ködel, "focus-kit na prática: agentes de código com processo (engenharia)", 2026. <https://youtu.be/r0fk_yVHgO4>`
* Form: plain Markdown links, no YouTube thumbnails, in the READMEs and on the homes. The agent chose it: docs/04 §Files keeps the book's images in `book/assets/` with no text inside, and the covers carry text; a remote image would also be fetched from YouTube on every view of the home.
* Words: English "film" (the kit's README says "Two films"), Portuguese "vídeo" (the kit's README.pt says "Dois vídeos"); each film named by what it shows, engineering / engenharia and business / negócio, as the kit's READMEs name them. Not a docs/03 term: the glossary holds the book's concepts, and no chapter teaches the films; the agent chose to keep it out, and the words are fixed here.
* Cases: the author's answers (OD-3, relayed by the opening session on 2026-10-23): the films are linked from the README, the site home and chapter 8; the client project they show is not Case A nor Case B but another project, outside the book's cases, and the text does not describe it, only links. docs/00 §Mechanics, Cases now says so in one sentence, written by this /propose. The text of this delivery describes no project, so it draws on no case and docs/05 §5's Case A and Case B slot does not apply.
* Terms of docs/03: none introduced. Sources cited: the four films and two playlists above. Cases drawn on: none.
* Token: `(PA)` stands. Nothing in flight touches the READMEs, `index.md`, chapter 8 or docs/00 (M30's line changes chapter 22).

**Out of scope.**
* Thumbnails or embedded players: images stay in `book/assets/` (docs/04 §Files), and an embed does not render in the PDF or the EPUB.
* The business film or the playlists in chapter 8: the author asked for the edition's engineering film there, the one that opens with the install.
* A description of the project, the client or the company the films show: the author's answer, and docs/00 §Cases.
* Chapters other than 8 (17 or 21 for the business film): not asked; a new line if the author wants them.
* Catching a removed film: YouTube answers 200 for it, and a check for that would answer an error that has not happened (docs/05 §7).
* Changing the films, their titles or the playlists: they live on YouTube and in the kit's repository, the author's.

**Done when.**
* [x] Both READMEs carry the two bullets in "Read"/"Ler", with the links of the Contract for their language.
* [x] Both site homes carry the paragraph, with the links of the Contract for their language.
* [x] Chapter 8 in both editions carries the sentence and the note; the chapter still opens with its value, no filler, nothing useful cut, its one new claim sourced by the note.
* [x] The author approves chapter 8's sentence in both editions (docs/00 OD-3).
* [x] docs/00 §Mechanics, Cases carries the sentence on the films (written by /propose; /apply checks it still reads true of what it built).
* [x] `make verify` green: build, parity, em dash, prose, width, links (the six URLs), disclosure scan.
* [x] Screenshot of the site home in both editions at 1280 and 390 pixels wide (docs/05 §5, Proof of a screen), saved as `work/done/book-films-home-<edition>-<width>.png`.
* [x] `make book`, and both PDF paths given to the author, the note's address printed under chapter 8's install.
* [x] Nothing acts outside git: one revert undoes the delivery.

## Decisions

* OD-3, answered by the author (relayed by the opening session, 2026-10-23): option B, the films are linked from the README, the site home and chapter 8, one sentence after the install with a source note to the edition's engineering film, nothing describing the project or what the film runs.
* The client project the films show is not Case A: another project, outside the book's cases (the author's answer).
* Chosen by the agent, for the author's review: text links without thumbnails; "film" / "vídeo" kept out of docs/03; chapter 8's paragraph placed after the one that ends "approve both."; the sentence's draft wording above.

## What /apply did

**Built.** `README.md` §Read and `README.pt.md` §Ler: two bullets each after the Releases, the edition's engineering and business films, each named by what it shows, then the other language's playlist named by its language. `book/en/index.md` and `book/pt/index.md`: one paragraph after the last line, the same two films and the playlist. Chapter 8, both editions: one paragraph after the one that ends "approve both." / "aprove os dois.", the Contract's sentence word for word, and the `[^focus-kit-film]` definition at the end of the file, word for word. docs/00 §Mechanics, Cases, written by /propose, still reads true of what was built: the films are linked from the READMEs, the home and chapter 8, and nothing describes the project or what they run.

**Divergences.** None from the Contract. docs/00's sentence, written by /propose, was corrected after the review: it said "an anonymized client project", a word the author's answer does not hold, and read as if chapter 8 linked both films; it now says "a client project" and that chapter 8 links the engineering film.

**Decisions taken by /apply.** The agent chose these alone: the wording of the README bullets and of the home's paragraph, each film's description in parentheses after its link, "the kit's four commands" (pt: "os quatro comandos do kit"), since neither page has chapter 8 around it; the note definition placed last among the chapter's notes, as the page says, so the site numbers it 11 at §Install while the PDF numbers it 1 (the chapter's notes were already grouped by vendor, not in mention order).

**Proof.** `make verify` green (exit 0, no finding) after the edits, the link check reaching the six URLs; the YouTube oEmbed of the four films on 2026-10-23 gives the titles the notes quote. `make book` built `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf` and both EPUBs; in each PDF chapter 8's note is number 1 and prints its address at the foot of the page of §Install. Screenshots of the home with `make serve` and headless Chrome: `work/done/book-films-home-en-1280.png`, `-en-390.png`, `-pt-1280.png`, `-pt-390.png`. Headless Chrome keeps a window wider than 390 pixels, so the first 390 shots cropped the page; the 390 shots were taken again through an iframe 390 pixels wide and cropped to it, and show the paragraph wrapped with no horizontal overflow.

**Delivery review.** One read-only Opus agent, launched by this /apply, that wrote none of it, read the page, docs/04, AGENTS.md, docs/00 §Mechanics, `git diff HEAD` of the two READMEs, both homes, both chapter 8s and docs/00, this line's block of docs/06, the four screenshots and the built site's chapter 8, and fetched the oEmbed of the four films and two playlists (all 200, titles matching the notes); it said it did not consult an advisor. No candidate broke the page or docs/04. Five candidates: docs/00 said "anonymized", which the page does not hold (fixed: cut); docs/00 read as if both films were in chapter 8 (fixed); the README and home sentences, all commas, could parse a description and the next link as one list (fixed: each description in parentheses, both editions, the 390 and 1280 screenshots taken again); the README said "the four commands" and the home "the kit's four commands" (fixed: "the kit's" in both, both editions); the new note is defined last, so the site numbers it 11 at its first mention (kept: the page places it at the end of the file, docs/04 sets no order, and the chapter's notes were out of mention order before). After the fixes, `make verify` and `make book` were run again.

**Author approval.** The author's answer, relayed by the opening session on 2026-10-23: chapter 8's sentence and note are approved as they are, in both editions (docs/00 OD-3).

```commit
docs(book-films): link the films of focus-kit at work

- README and README.pt: the edition's engineering and business films
  and the other language's playlist, under Read / Ler
- site home, both editions: the same links in one paragraph
- chapter 8, after the install: one sentence and a note to the
  edition's engineering film
- docs/00 Cases: the films show a project outside the book's cases

work/done/book-films.md
```
