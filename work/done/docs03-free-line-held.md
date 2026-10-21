# docs03-free-line-held

**Objective.** A reader of docs/03's `free line` row learns that the next delivery is the first free line no session holds, as chapter 14 :185 says, not a free line another session is already defining or building.

**Behaviour.** What a reader of docs/03 can say afterwards:

* Read the `free line` row and say that the next delivery is the first free line in the queue that no session holds.
* Given a queue whose first free line is `[~]` in another session, and a `[ ]` line below it, say the next delivery is the `[ ]` line, as chapter 14 :71 teaches with `lend-book`, `reservations` and `search-catalog`.
* Edge: a `[~]` or `[*]` line stays free by the row's first clause (not `[x]`, not `[?]`, its `after` lines `[x]`); the row does not redefine free, it only says which free line is next.
* Edge: with a branch or a worktree per delivery, the row's last clause still says a line whose branch exists after `git fetch` is taken, not free; the two clauses agree.
* Edge: docs/03's row and chapter 14 :185 (en) and :186 (pt) say the same next delivery.

**Contract.** One row of `docs/03-Domain.md`, against the file as it is today; the term, its pt name and its code column unchanged.

* `docs/03-Domain.md` :115, in the definition: "the first one in the queue is the next delivery," becomes "the first one in the queue that no session holds is the next delivery,". The rest of the row is unchanged, so it reads: "A line not `[x]` and not `[?]` whose `after` lines are all `[x]`; the first one in the queue that no session holds is the next delivery, and free lines that touch different files may run at the same time; with a branch or a worktree per delivery, a line whose branch exists after `git fetch` is taken, not free, whatever the main branch shows (docs/05 §4)."
* No new term; no other row changes.
* Neighbouring line on the same file: `kit-2026-10-20-1` (M25, `[>]`, `work/kit-2026-10-20-1.md`) rewrites this same row whole at its :29, quoting the row as it is today plus the `(PA)` token. It comes later in queue order, so it applies after this line. Composed, the row reads: "A line not `[x]` and not `[?]` whose `after` lines are all `[x]`; the first one in the queue that no session holds is the next delivery, and free lines may run at the same time as their `(PA)` tokens say, or, without one, when they touch different files; with a branch or a worktree per delivery, a line whose branch exists after `git fetch` is taken, not free, whatever the main branch shows (docs/05 §4)." That page's quote at :29 still holds the old clause: handed to the driver, so its /apply writes the composed row and does not undo this one, as m24-review handed P8 to that page.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no visual change.

**Out of scope.**

* docs/05 §4 :93, "the next delivery is the first free line": the template's text, changed only by a reinstall (ADR-0018), and `kit-2026-10-20-1` takes the new template paragraph whole.
* The installed skills' `references/documents.md`: the kit's files, not this project's.
* Chapters 8 :109, 10 :104 and 17 :131, which say "first free line": not what P6 saw, and chapter 8 lies with `ch08-23-fetch-taken`.
* Chapter 14: it already says "no session holds" (en :71, :185; pt :72, :186).
* A definition of "holds": docs/05 §4 already says a `[~]` or `[*]` line keeps its mark while its session works on it or until the person's word resumes it.
* `work/done/m24-review.md`: it names P6 as this line already; no edit.

**Decisions from the documents.**

* Finding P6 of `work/done/m24-review.md` :150: docs/03 :115 "the first one ... is the next delivery" also counts a free line another session holds; chapter 14 :185 says "no session holds".
* The wording is chapter 14's: "the first free line no session holds" (en :71, :185).
* A finding of M24's own review stays in M24 (docs/05 §8); docs/03 is not in the book, so no edition pair applies (ADR-0004 covers the book).

**Decisions taken alone.**

* The clause takes chapter 14's words and no definition of "holds", keeping the row one clause longer and nothing more.
* No sibling sentence widens the scope: no other docs/03 row says which line is next.
* Composition with `kit-2026-10-20-1` is written here and handed to the driver; its page is not edited by this delivery.
* The queue line keeps its wording.

**Done when.**

* [x] docs/03 :115 reads as the Contract says, and no other row changes.
* [x] The row agrees with chapter 14 en :185 and pt :186 on the next delivery.
* [x] No em dash; no version, date or before/after in the row.
* [x] `make verify` green after the last edit, its result recorded in this page's Proof.
* [x] Delivery review by one read-only Opus agent, over `git diff HEAD -- docs/03-Domain.md` against this page, docs/04 and chapter 14 (Delivery review); whether it kept the session's advisor, as docs/05 §5 asks, is not recorded.

**Proof.**

* `git diff HEAD -- docs/03-Domain.md`: one line changed, :115, the clause "the first one in the queue that no session holds is the next delivery,"; the rest of the row as the Contract quotes it.
* Chapter 14 en :71 and :185 say "the first free line no session holds"; pt :72 and :186 say "a primeira linha livre que nenhuma sessão pegou": the row names the same next delivery.
* `make verify` after the last edit: exit 0 (build, parity, em dash, prose, width, examples, links, disclosure).
* `make book` after the last verify: exit 0; `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.

**Divergences.**

* The commit subject the page proposed ran 86 characters; it is shortened to fit 72, same meaning.

**Delivery review.**

One read-only Opus agent read `git diff HEAD -- docs/03-Domain.md` against this page, docs/04 and chapter 14 en :71, :185 and pt :72, :186. Verdict: clean, no findings. It confirmed the only change is :115, the term, pt name and code column unchanged, no other row changed, the row agrees with chapter 14 on the next delivery, and no em dash, version, date or before/after.

```commit
docs(docs03-free-line-held): a held free line is not the next delivery

- docs/03: `free line` says the next delivery is the first free line no
  session holds, as chapter 14 says

work/done/docs03-free-line-held.md
```
