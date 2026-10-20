# Release the book

## What it does and when

Publishes the PDF and the EPUB of both editions as a GitHub Release, under a new tag `vX.Y.Z`.
`make release` writes the new version and today's date to `VERSION`, builds the book on your machine, commits `VERSION`, and pushes `main` and the tag; the job `release` builds the four files and attaches them.
Each file's rights page, the page with the copyright line, says which version it is, when it was published, and where to look for a newer one.
The README sends readers to the Releases page, and `releases/latest/download/<file>` serves the newest one.
Release when `main` holds chapters you want readers to download; the site does not need a release (`publish-the-site.md`).

## What must be in place

* You are the author, with push rights to `JCKodel/focus-kit-book`; nobody else tags.
* On `main`, with no uncommitted change, and not behind `origin/main` (`git pull` first).
* At least one commit since the newest `vX.Y.Z` tag.
* `make verify` green; `make release` runs it again and refuses when it fails.
* `VERSION` naming the newest tag, as the last `make release` left it (`1.2.3 2026-10-16` for `v1.2.3`); edit it by hand only to fix that.
* pandoc, weasyprint and pypdf installed, since `make release` builds the book before it asks (`docs/manuals/build-the-book-from-a-clone.md`).
* The secret `DISCLOSURE_DENYLIST` set in the repository, because the job `release` runs only after `verify` is green in Actions (`set-up-the-disclosure-list.md`).

## Steps

1. `make release` for the next patch version (`v1.2.3` after `v1.2.2`).
   `make release BUMP=minor` (`v1.3.0`) or `make release BUMP=major` (`v2.0.0`) for a larger step.
2. Wait for `make verify` and the book build; on a build that fails, it prints the build's findings and refuses.
3. Read what it prints: the four files' paths in `output/`, the next tag, the newest one before it, and the commits between them. Open a PDF if you want to see the rights page before answering.
4. Answer `y` to commit `VERSION` as `chore(release): vX.Y.Z`, push `main`, tag that commit and push the tag; anything else restores `VERSION` and stops with nothing committed or pushed.
5. Open the Actions link it prints and follow the job `release`.

A refusal prints one line, `Makefile:1: release: <message>`, or `VERSION:1: release: <message>` for `VERSION`, says what to fix, and pushes nothing; a failed push of `main` after `y` also undoes the commit and restores `VERSION`.

## How to tell it worked

The job `release` ends green, and the Release page the command printed, `releases/tag/<tag>`, holds four files: `one-page-at-a-time.pdf`, `one-page-at-a-time.epub`, `uma-pagina-de-cada-vez.pdf`, `uma-pagina-de-cada-vez.epub`.
The third page of each PDF, and the rights of each EPUB, read "This is version X.Y.Z of the book, published on YYYY-MM-DD." (pt: "Esta é a versão X.Y.Z do livro, publicada em YYYY-MM-DD."), with no "not yet published"; so does `make book` on the tagged commit with a clean tree.
A tag with a `-` in it, such as `v2.0.0-rc1`, makes a pre-release, which `latest` does not serve.

## How to undo it

Delete the Release on its page on GitHub, then the tag, remotely and locally:

```
git push origin :refs/tags/vX.Y.Z
git tag -d vX.Y.Z
```

`main` stays pushed; that is a publish of the site, undone as `publish-the-site.md` says.
The commit `chore(release): vX.Y.Z` stays on `main` unless reverted; revert it with `git revert <its sha>` and push, so `VERSION` names the newest tag again and the next `make release` does not refuse.

## What breaks if a step is skipped

* Tagging by hand instead of `make release`: nothing checks that `main` is pushed, clean and green, the tag may name a commit Actions has not seen, and `VERSION` still names the previous release, so every book built from the tag says that version, with changes not yet published.
* Secret missing: the job `verify` fails, `release` never starts, and the tag exists with no Release; delete the tag as above, set the secret, release again.
* `make verify` red: `make release` refuses before pushing anything.
* `VERSION` edited by hand to another version: `make release` refuses, `VERSION:1: release: VERSION says <x> but the newest tag is <tag>`; set it back to the newest tag and its date.
* Network lost after `y`: when the push of `main` fails, `make release` undoes its commit and restores `VERSION`, and you run it again; when only the push of the tag fails, `main` is pushed and the tag exists locally, so push it with `git push origin vX.Y.Z`.
