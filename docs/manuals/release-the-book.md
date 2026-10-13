# Release the book

## What it does and when

Publishes the PDF and the EPUB of both editions as a GitHub Release, under a new tag `vX.Y.Z`.
`make release` pushes `main` and the tag; the job `release` builds the four files and attaches them.
The README sends readers to the Releases page, and `releases/latest/download/<file>` serves the newest one.
Release when `main` holds chapters you want readers to download; the site does not need a release (`publish-the-site.md`).

## What must be in place

* You are the author, with push rights to `JCKodel/focus-kit-book`; nobody else tags.
* On `main`, with no uncommitted change, and not behind `origin/main` (`git pull` first).
* At least one commit since the newest `vX.Y.Z` tag.
* `make verify` green; `make release` runs it again and refuses when it fails.
* The secret `DISCLOSURE_DENYLIST` set in the repository, because the job `release` runs only after `verify` is green in Actions (`set-up-the-disclosure-list.md`).

## Steps

1. `make release` for the next patch version (`v1.2.3` after `v1.2.2`).
   `make release BUMP=minor` (`v1.3.0`) or `make release BUMP=major` (`v2.0.0`) for a larger step.
2. Read what it prints: the next tag, the newest one before it, and the commits between them.
3. Answer `y` to push `main` and the tag, or anything else to stop with nothing pushed.
4. Open the Actions link it prints and follow the job `release`.

A refusal prints one line, `Makefile:1: release: <message>`, says what to fix, and pushes nothing.

## How to tell it worked

The job `release` ends green, and the Release page the command printed, `releases/tag/<tag>`, holds four files: `one-page-at-a-time.pdf`, `one-page-at-a-time.epub`, `uma-pagina-de-cada-vez.pdf`, `uma-pagina-de-cada-vez.epub`.
A tag with a `-` in it, such as `v2.0.0-rc1`, makes a pre-release, which `latest` does not serve.

## How to undo it

Delete the Release on its page on GitHub, then the tag, remotely and locally:

```
git push origin :refs/tags/vX.Y.Z
git tag -d vX.Y.Z
```

`main` stays pushed; that is a publish of the site, undone as `publish-the-site.md` says.

## What breaks if a step is skipped

* Tagging by hand instead of `make release`: nothing checks that `main` is pushed, clean and green, and the tag may name a commit Actions has not seen.
* Secret missing: the job `verify` fails, `release` never starts, and the tag exists with no Release; delete the tag as above, set the secret, release again.
* `make verify` red: `make release` refuses before pushing anything.
