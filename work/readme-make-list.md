# readme-make-list

**Objective.** A person reading "Build locally" in either README learns that `make` alone lists its commands, without the bullet claiming that the bullets below are that list (m22-review, candidate 26).

**Behaviour.** Manual checks (docs/04 §Tests: no check reads the READMEs' bullets, as `make-help` decided).

* README.md, "Build locally": the first bullet reads "`make` lists its commands, one line each."; with "these" gone it no longer introduces the five bullets below as the list, so read beside `make`'s eight lines (`help`, `serve`, `build`, `verify`, `scan`, `hooks`, `book`, `release`) it is true although `help`, `build` and `scan` have no bullet of their own.
* README.pt.md, "Gerar localmente": the same bullet in Portuguese, "`make` lista os seus comandos, uma linha cada.", in the same place.
* The bullet stays true when a target is added or removed later: it names no count and no list.
* Nothing else in either README changes: the other bullets, their order and the headings stay as they are (parity counts headings).
* Fails if: the bullet still points at the bullets below as the list, or one edition changes without the other (ADR-0004).

**Contract.** Text only, one line in each README.

README.md, line 20, from:

```
* `make` lists these commands, one line each.
```

to:

```
* `make` lists its commands, one line each.
```

README.pt.md, line 20, from:

```
* `make` lista estes comandos, uma linha cada.
```

to:

```
* `make` lista os seus comandos, uma linha cada.
```

"Commands" stays: the target/command clash is candidate 26's weak part, which m22-review rejected with every weak candidate. No docs/03 term is needed, and no other document changes.

**States.** No screen.

**Visual reference.** No screen.

**Out of scope.**

* Bullets for `make help`, `make build` and `make scan`: the reworded first bullet answers the finding, and `make` prints what each does.
* "Target" for "command": candidate 26's weak part, rejected by m22-review.
* Reordering the bullets to match `make`'s order: not what the finding names.
* The Makefile, docs/01 and the help output: `make-help` and m22-review's mechanical check found them right.

**Done when.**

* [ ] README.md line 20 and README.pt.md line 20 read exactly as the Contract says; no other line of either changes.
* [ ] Read by hand beside `make`'s output: the bullet is true in both editions.
* [ ] `make verify` green; page in `work/done/`, the line `[x]`, staged by its paths and its hunk of docs/06, the commit suggested in a `commit` block.

**Decisions taken from the documents.**

* No check and no test: docs/04 §Tests, as `make-help` decided for the same bullet.
* "Commands" kept: m22-review's Findings reject every weak candidate, the target/command part of 26 among them.
* Both editions in the same delivery: ADR-0004.

**Decisions made alone** (the author asked for recommended answers; correct them in the review):

* Reword the bullet rather than add bullets for `build` and `scan`, the first of the two ways m22-review's proposed line names: one demonstrative replaced per edition, and true whatever targets are added later.
* No count in the bullet ("its commands", not "eight"): a count would go stale with the next target.
* No sibling sentence covered by the finding was found in the same files: the READMEs' other bullets each describe one target and stay true.
