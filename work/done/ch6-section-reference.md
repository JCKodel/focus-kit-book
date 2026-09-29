# ch6-section-reference

**Objective.** A reader of chapter 6 finds the rule of docs/04 the chapter promises, because the sentence names the chapter's section "Living documents" and links to it, instead of "section 6".

**Behaviour.**

* In §"The seven documents", the docs/04 description ends by naming [Living documents](#living-documents) below as where one of docs/04's rules is shown, not "section 6".
* The Portuguese names "Documentos vivos" and links to its own anchor.
* Clicking the link on the site lands on that section in both editions.
* Finding F7 of the M3 review is settled.

**Contract.**

* Files: `book/en/06-the-documents.md` (line 72 today) and `book/pt/06-the-documents.md` (line 73 today), that sentence only.
* Anchors: `#living-documents` in English, `#documentos-vivos` in Portuguese, as the site generates them; /apply confirms both in the built site.
* Terms, sources, cases, exercises: unchanged.

**Out of scope.**

* Other "section N" references in the book: the review found none that misleads.

**Done when.**

* [x] Both editions changed; each link reaches its section in the built site.
* [x] `make verify` green (the strict build fails on a broken internal anchor).
* [x] `make book` run, and both PDF paths given to the author.
* [x] Page in `work/done/`, `[x]` in docs/06, staged, commit message suggested.

**What happened.**

* `book/en/06-the-documents.md:72` ends "[Living documents](#living-documents), below, shows one of its rules."; `book/pt/06-the-documents.md:73` ends "[Documentos vivos](#documentos-vivos), mais adiante, mostra uma das regras dele." "Below" was added so the reader knows the section is later in this chapter.
* The built site has `id="living-documents"` in `site/06-the-documents/index.html` and `id="documentos-vivos"` in `site/pt/06-the-documents/index.html`, each target of the new link; the strict build passes.
* Nothing dropped, nothing diverged from the plan. No document changed. Finding F7 of the M3 review is settled.
* Proof: `make verify` green; `make book` builds both editions, `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.
