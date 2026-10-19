# ch04-remove-slice

**Objective.** After chapter 4 the reader knows that removing a feature removes its folder and the imports other slices hold of it, as the member's page that imports from `loans/` shows.

**Behaviour.**

* Reading "Vertical slices", the reader says that removing loans from the product removes `loans/` (pt `emprestimos/`) and changes every slice that imports from it, not one folder alone.
* Asked what else changes, the reader names the member's page that lists their loans, which imports from `loans/`, the example of "Where shared code lives" (pt "Onde mora o código compartilhado"), and says the imports of `loans/` name every such place.
* The reader keeps the rest of the sentence: a change to how lending works touches `loans/`.
* The claim agrees with "Scalable" (`ch04-isolation-claims`): the coupling between slices is what one imports from another, and those imports name where a change reaches.

**Contract.** Files: `book/en/04-focus.md` and `book/pt/04-focus.md`, section "Vertical slices" / "Fatias verticais", one sentence, located by content: en "A change to how lending works touches `loans/`, and removing loans from the product removes one folder." / pt "Uma mudança em como o empréstimo funciona mexe em `emprestimos/`, e tirar os empréstimos do produto tira uma pasta." Its second clause says removal takes the folder and the imports other slices hold of it, such as the member's page that lists their loans (pt "a página de um membro que lista os empréstimos dele"), with the folder names of each edition. The example is the chapter's TypeScript lending library, written for the chapter. Sources: the chapter's own sentence that a member's page imports from `loans/`, and Bogard's coupling rule, already cited as `bogard-vertical-slice`. Terms of docs/03: vertical slice, feature; no new term, no number, no private case.

**States.** Inapplicable: prose, no screen.

**Visual reference.** Inapplicable: existing chapter layout.

**Out of scope.** The Key points' slice bullet: it says a slice keeps what one feature needs in one folder, which stays true. A claim about what the compiler reports for a removed import: it would need a source the chapter does not have. No other chapter claims removal takes one folder (grep of both editions for "removes one folder" and "tira uma pasta").

**Decisions from the documents.** The member's page is the example because the chapter already names it as an importer of `loans/` (docs/06's line), so no new example enters.

**Done when.**

* [ ] Both editions written, same hunks, Portuguese folder names in the Portuguese edition; each Behaviour line checked against both.
* [ ] The chapter opens with its value and keeps its evidenced team gain; no filler and nothing useful cut; terms follow docs/03; no em dash.
* [ ] No Case A or Case B passage changed or added, so the author's OD-3 approval is inapplicable.
* [ ] `make verify` green after the last edit, chapter examples included; `make book` builds both editions and the page gives `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf` for the author's review.
* [ ] Delivery review by a read-only Opus agent per docs/05 §5, its candidates answered on this page; page archived and commit message suggested.
