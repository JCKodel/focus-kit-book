#!/bin/sh
# focus-kit: change the mark of one docs/06 line, as docs/05 §4 says. Run it
# through git, so it starts at the repository's top level on every host:
#   git -c "alias.fm=!sh .agents/skills/propose/scripts/mark.sh" fm <slug> "<mark>" [stage]
# <mark> is one of "[ ]" "[~]" "[>]" "[*]" "[x]" "[?]". A program that
# rewrites docs/06 whole can leave it empty; this one changes one byte. The
# file is written beside itself and renamed over it, only when the result
# keeps its size and differs in at most that byte. With "stage", the same
# line changes in the index and nothing else there does, so another
# session's staged lines stay as they are. A "[~]" goes only on a "[ ]" line
# and a "[*]" only on a "[>]" one, so two sessions that started one line
# cannot both mark it: the second is refused. Exit 0 marked, 2 refused.
set -eu

die() { printf 'error: %s\n' "$1"; exit 2; }

slug=${1:-}; mark=${2:-}; stage=${3:-}
[ -n "$slug" ] && [ -n "$mark" ] || die 'usage: mark.sh <slug> "[ ]" | "[~]" | "[>]" | "[*]" | "[x]" | "[?]" [stage]'
case $mark in '[ ]'|'[~]'|'[>]'|'[*]'|'[x]'|'[?]') ;; *) die "unknown mark '$mark'" ;; esac
case $stage in ''|stage) ;; *) die "unknown word '$stage'; the third is stage or nothing" ;; esac
case $slug in -*|*[!a-zA-Z0-9._-]*) die "slug '$slug' holds a character a slug cannot" ;; esac
command -v cmp >/dev/null 2>&1 || die "cmp is missing; it proves only the mark changed"

top=$(git rev-parse --show-toplevel 2>/dev/null) || die "not inside a repository"
queue=
for f in "$top"/docs/06-*.md; do
  [ -f "$f" ] || continue
  [ -z "$queue" ] || die "more than one docs/06-*.md in $top/docs"
  queue=$f
done
[ -n "$queue" ] || die "no docs/06-*.md in $top/docs"
rel="docs/${queue##*/}"

# The slug's line: a mark, whitespace, then the slug as a whole word.
# count prints how many lines are the slug's; put prints the input with
# the mark of that line replaced.
find='function mine(l,  r) {
    if (l !~ /^\[[ ~>*x?]\][ \t]/) return 0
    r = substr(l, 4); sub(/^[ \t]+/, "", r); sub(/\r$/, "", r)
    return r == slug || index(r, slug " ") == 1 || index(r, slug "\t") == 1
  }'
count="$find"' mine($0) { n++ } END { print n + 0 }'
put="$find"' mine($0) { $0 = mark substr($0, 4) } { print }'

tmp=$(mktemp "$queue.XXXXXX")
blob=; new=
trap 'rm -f "$tmp" ${blob:+"$blob"} ${new:+"$new"}' EXIT

# replace <source> <name> <target>: writes the source with the mark changed
# into the target, refusing unless the target keeps the source's size and
# differs from it in at most one byte.
replace() {
  n=$(awk -v slug="$slug" "$count" "$1")
  [ "$n" -eq 1 ] || die "$n lines of $2 are $slug's; expected 1"
  awk -v slug="$slug" -v mark="$mark" "$put" "$1" > "$3"
  [ "$(wc -c < "$1")" -eq "$(wc -c < "$3")" ] || die "the result of $2 would not keep its size (does it end without a newline?); nothing written"
  d=$(cmp -l "$1" "$3" 2>/dev/null | wc -l)
  [ "$d" -le 1 ] || die "the result of $2 would differ in $d bytes; nothing written"
}

cp -p "$queue" "$tmp"
replace "$queue" "$rel" "$tmp"
was=$(awk -v slug="$slug" "$find"' mine($0) { print substr($0, 1, 3) }' "$queue")
case $mark in '[~]') from='[ ]' ;; '[*]') from='[>]' ;; *) from=$was ;; esac
[ "$was" = "$from" ] || die "$slug is $was, not $from; docs/05 §4 says how it moves, and a [~] or [*] is another session's, resumed only on the person's word; nothing written"
mv "$tmp" "$queue"
printf 'marked: %s %s in %s\n' "$mark" "$slug" "$rel"

[ "$stage" = stage ] || exit 0
entry=$(git -C "$top" ls-files -s -- "$rel")
[ -n "$entry" ] || die "$rel is not in the index; stage it as docs/05 §6 says"
[ "$(printf '%s\n' "$entry" | wc -l)" -eq 1 ] || die "$rel has a merge conflict in the index"
mode=${entry%% *}
blob=$(mktemp); new=$(mktemp)
git cat-file blob ":$rel" > "$blob"
[ "$(awk -v slug="$slug" "$count" "$blob")" -ne 0 ] || die "$slug's line is not in the index yet; stage the line as docs/05 §6 says"
replace "$blob" "the index's $rel" "$new"
sha=$(git hash-object -w --no-filters "$new")
git -C "$top" update-index --cacheinfo "$mode,$sha,$rel"
printf 'staged: that line alone\n'
