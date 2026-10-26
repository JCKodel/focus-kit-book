#!/bin/sh
# focus-kit: claim a queue line as docs/05 says. Run it through git, so it
# starts at the repository's top level on every host and shell:
#   git -c "alias.fk=!sh .agents/skills/propose/scripts/claim.sh" fk <slug> <strategy> [resume]
# <strategy> is the Git slot of docs/05: trunk | branch | worktree <hidden> <prefix>
# The branch is created on origin only if no one else has: a branch that
# is there and not here is another clone's, opened only with "resume".
# Prints key: value lines; exit 0 claimed, 2 refused. Edits no document.
set -eu

die() { printf 'error: %s\n' "$1"; exit 2; }

resume=0; last=
for a in "$@"; do last=$a; done
[ $# -gt 2 ] && [ "$last" = resume ] && resume=1
slug=${1:-}; strategy=${2:-}
[ -n "$slug" ] && [ -n "$strategy" ] || die "usage: claim.sh <slug> trunk | branch | worktree <hidden> <prefix> [resume]"
case $slug in -*|*[!a-zA-Z0-9._-]*) die "slug '$slug' holds a character a branch name cannot" ;; esac

top=$(git rev-parse --show-toplevel 2>/dev/null) || die "not inside a repository"
head=$(git symbolic-ref --quiet --short HEAD) || die "HEAD is detached; claim from the default branch"

draft() {
  if [ -f "$top/work/$slug.md" ]; then
    printf 'draft: work/%s.md at %s; bring it into the delivery\n' "$slug" "$top"
  else
    printf 'draft: none\n'
  fi
}

if [ "$strategy" = trunk ]; then
  printf 'claim: none, trunk\nbranch: %s\npath: %s\n' "$head" "$top"
  draft
  exit 0
fi

case $strategy in
  worktree)
    hidden=${3:-}; prefix=${4:-}
    [ -n "$hidden" ] && [ -n "$prefix" ] || die "worktree needs the hidden folder and the branch prefix: worktree .focus-kit focus-kit/"
    hidden=${hidden%/}
    branch="$prefix$slug"
    case $top in
      */"$hidden"/worktrees/"$slug")
        printf 'claim: here\nbranch: %s\npath: %s\n' "$branch" "$top"; draft; exit 0 ;;
      */"$hidden"/worktrees/*) die "run from main/, not from a worktree: $top" ;;
    esac
    case $head in "$prefix"*) die "run from main/; HEAD is $head, a delivery branch" ;; esac
    ;;
  branch)
    branch=$slug
    if [ "$head" = "$branch" ]; then printf 'claim: here\nbranch: %s\npath: %s\n' "$branch" "$top"; draft; exit 0; fi
    ;;
  *) die "unknown strategy '$strategy': trunk, branch or worktree <hidden> <prefix>" ;;
esac

git remote get-url origin >/dev/null 2>&1 || die "no remote origin; the claim needs one, or the Git slot says trunk"
git fetch -q origin || die "git fetch origin failed"

default=$(git symbolic-ref --quiet --short refs/remotes/origin/HEAD 2>/dev/null | sed 's|^origin/||') || true
[ -n "$default" ] || for b in main master; do
  if git show-ref --quiet "refs/remotes/origin/$b"; then default=$b; break; fi
done
[ -n "$default" ] || die "cannot tell the default branch; run git remote set-head origin -a"
[ "$head" = "$default" ] || die "on branch $head; claim from $default"

# The delivery starts from origin's default branch, which the fetch just
# read, so a clone that did not pull still starts from what is integrated.
base="refs/remotes/origin/$default"
behind=$(git rev-list --count "$head..$base" 2>/dev/null || echo 0)
ahead=$(git rev-list --count "$base..$head" 2>/dev/null || echo 0)
[ "$behind" -eq 0 ] || printf 'note: %s is behind origin by %s; the delivery starts from origin/%s\n' "$head" "$behind" "$default"
[ "$ahead" -eq 0 ] || printf 'note: %s is ahead of origin by %s; those commits are not in the delivery\n' "$head" "$ahead" "$default"

# ls-remote matches a pattern against the tail of a ref, so the full name is given.
if [ "$strategy" = worktree ] && git ls-remote --exit-code --heads origin "refs/heads/$slug" >/dev/null 2>&1; then
  printf "note: a branch %s without the prefix exists on origin; it is not the delivery's\\n" "$slug"
fi

if git ls-remote --exit-code --heads origin "refs/heads/$branch" >/dev/null 2>&1; then remote=1; else remote=0; fi
local=0; git show-ref --quiet "refs/heads/$branch" && local=1

# push_new <dir>: creates the branch on origin only if it is not there yet.
push_new() { git -C "$1" push -q -u origin "$branch" --force-with-lease="refs/heads/$branch:" 2>/dev/null; }

if [ "$strategy" = worktree ]; then
  path="$(dirname "$top")/$hidden/worktrees/$slug"
  if [ -d "$path" ]; then
    if [ "$remote" -eq 1 ]; then claim="existing"
    else
      push_new "$path" || die "push of $branch failed; the line is not claimed"
      claim="existing, branch pushed now"
    fi
  elif [ "$remote" -eq 1 ]; then
    [ "$local" -eq 1 ] || [ "$resume" -eq 1 ] || { printf 'claim: taken\nbranch: %s, on origin and not here: another clone'"'"'s; to open it here, add resume\n' "$branch"; exit 2; }
    if [ "$local" -eq 1 ]; then git worktree add -q "$path" "$branch"
    else git worktree add -q --track -b "$branch" "$path" "origin/$branch"; fi
    claim=$([ "$local" -eq 1 ] && echo existing || echo resumed)
  else
    git worktree add -q --no-track -b "$branch" "$path" "$base"
    if ! push_new "$path"; then
      git worktree remove --force "$path" >/dev/null 2>&1; git branch -q -D "$branch"
      printf 'claim: taken\nbranch: %s appeared on origin meanwhile: another clone claimed it first\n' "$branch"; exit 2
    fi
    claim="new"
  fi
  path=$(git -C "$path" rev-parse --show-toplevel)
else
  if [ "$remote" -eq 1 ]; then
    [ "$local" -eq 1 ] || [ "$resume" -eq 1 ] || { printf 'claim: taken\nbranch: %s, on origin and not here: another clone'"'"'s; to open it here, add resume\n' "$branch"; exit 2; }
    if [ "$local" -eq 1 ]; then git switch -q "$branch"; claim="existing"
    else git switch -q --track -c "$branch" "origin/$branch"; claim="resumed"; fi
  elif [ "$local" -eq 1 ]; then
    git switch -q "$branch"
    push_new "$top" || die "push of $branch failed; the line is not claimed"
    claim="existing, branch pushed now"
  else
    git switch -q --no-track -c "$branch" "$base"
    if ! push_new "$top"; then
      git switch -q "$default"; git branch -q -D "$branch"
      printf 'claim: taken\nbranch: %s appeared on origin meanwhile: another clone claimed it first\n' "$branch"; exit 2
    fi
    claim="new"
  fi
  path=$top
fi

printf 'claim: %s\nbranch: %s, on origin\npath: %s\n' "$claim" "$branch" "$path"
draft
