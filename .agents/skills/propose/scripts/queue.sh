#!/bin/sh
# focus-kit: draw docs/06's current milestone as a tree of what waits on
# what, and say what may run now, as docs/05 §4 says. Run it through git:
#   git -c "alias.fq=!sh .agents/skills/propose/scripts/queue.sh" fq <strategy>
# <strategy> is the Git slot of docs/05: trunk | branch | worktree <hidden> <prefix>
# With a branch or worktree per delivery, each delivery's line is read from
# its branch on origin, and lines only a branch has are listed. A line goes
# under the last line it waits on; "+ after" names the others. Edits nothing.
set -eu

die() { printf 'error: %s\n' "$1"; exit 2; }

strategy=${1:-}
case $strategy in
  trunk) prefix= ;;
  branch) prefix= ;;
  worktree) prefix=${3:-}; [ -n "$prefix" ] || die "worktree needs the hidden folder and the branch prefix: worktree .focus-kit focus-kit/" ;;
  *) die "usage: queue.sh trunk | branch | worktree <hidden> <prefix>" ;;
esac

top=$(git rev-parse --show-toplevel 2>/dev/null) || die "not inside a repository"
queue=
for f in "$top"/docs/06-*.md; do
  [ -f "$f" ] || continue
  [ -z "$queue" ] || die "more than one docs/06-*.md in $top/docs"
  queue=$f
done
[ -n "$queue" ] || die "no docs/06-*.md in $top/docs"
rel="docs/${queue##*/}"

overlay=$(mktemp)
trap 'rm -f "$overlay"' EXIT
if [ "$strategy" != trunk ] && git remote get-url origin >/dev/null 2>&1; then
  git fetch -q origin 2>/dev/null || printf 'note: git fetch origin failed; branches as last fetched\n'
  default=$(git symbolic-ref --quiet --short refs/remotes/origin/HEAD 2>/dev/null | sed 's|^origin/||') || true
  [ -n "$default" ] || for b in main master; do
    if git show-ref --quiet "refs/remotes/origin/$b"; then default=$b; break; fi
  done
  git for-each-ref --format='%(refname)' refs/remotes/origin | while read -r ref; do
    name=${ref#refs/remotes/origin/}
    # The default branch gives every line; a delivery branch, its own.
    if [ "$name" = "$default" ]; then slug='*'
    else
      case $name in HEAD) continue ;; "$prefix"*) ;; *) continue ;; esac
      slug=${name#"$prefix"}
      case $slug in ''|*[!a-zA-Z0-9._-]*) continue ;; esac
    fi
    git show "$ref:$rel" 2>/dev/null | awk -v s="$slug" '{ print s "\t" $0 }' >> "$overlay" || true
  done
fi

awk -F '\t' '
function parse(line, k,   rest, n, parts, i, p, deps, j, m) {
  mark[k] = substr(line, 2, 1)
  rest = substr(line, 4); sub(/^[ \t]+/, "", rest)
  slug[k] = rest; sub(/[ \t].*/, "", slug[k])
  rest = substr(rest, length(slug[k]) + 1); sub(/^[ \t]+/, "", rest)
  tokp[k] = ""; toka[k] = ""
  if (rest ~ /^\([P-][A-]\)/) { tokp[k] = substr(rest, 2, 1); toka[k] = substr(rest, 3, 1) }
  nafter[k] = 0; resume[k] = ""; blocked[k] = ""; dropped[k] = 0
  n = split(rest, parts, " \302\267 ")
  for (i = 2; i <= n; i++) {
    p = parts[i]
    if (p ~ /^after /) {
      sub(/^after /, "", p); m = split(p, deps, /, */)
      for (j = 1; j <= m; j++) if (deps[j] != "") after[k, ++nafter[k]] = deps[j]
    } else if (p ~ /^resume: /) { sub(/^resume: /, "", p); resume[k] = p }
    else if (p ~ /^blocked: /) { sub(/^blocked: /, "", p); blocked[k] = p }
    else if (p ~ /^dropped: /) dropped[k] = 1
  }
}
function rank(m) { return index(" ~?>*x", m) }
function isline(s) { return s ~ /^\[[ ~>*x?]\][ \t]+[^ \t]/ }
function defined(k) { return mark[k] ~ /[>*x]/ || (mark[k] == "?" && resume[k] == "apply") }
function pending(s) { return !(s in at) || mark[at[s]] != "x" }
function state(k,   i, s, why, sep) {
  if (mark[k] == "~") return "in flight: propose"
  if (mark[k] == "*") return "in flight: apply"
  if (mark[k] == "?") return "blocked: " blocked[k] (resume[k] != "" ? ", then " resume[k] : "")
  cmd[k] = (mark[k] == ">") ? "apply" : "propose"
  why = ""; sep = ""
  for (i = 1; i <= nafter[k]; i++) {
    s = after[k, i]
    if (!(s in at)) { why = why sep s " is not in the queue"; sep = "; " }
    else if (dropped[at[s]]) { why = why sep "after " s ", dropped: re-decide"; sep = "; " }
  }
  if (lastdep[k] != "") { why = why sep "after " lastdep[k]; sep = "; " }
  if (cmd[k] == "propose" && tokp[k] == "-") for (i = 1; i < k; i++) if (!defined(i)) { why = why sep "the lines above are defined"; sep = "; "; break }
  if (cmd[k] == "apply" && toka[k] == "-") for (i = 1; i < k; i++) if (mark[i] != "x") { why = why sep "the lines above are done"; sep = "; "; break }
  if (why != "") { cmd[k] = ""; return "waits: " why }
  if (tokp[k] == "") { judge[++nj] = slug[k]; return cmd[k] " now, no token: judge" }
  return cmd[k] " now"
}
function show(k, depth,   pad, i, c, extra, sep, line, n) {
  seen[k] = 1
  pad = ""; for (i = 1; i < 2 * depth; i++) pad = pad " "
  if (depth > 0) pad = pad "\342\224\224"
  extra = ""; sep = ""
  for (i = 1; i <= nafter[k]; i++) {
    c = after[k, i]
    if (c != lastdep[k] && c in at && pending(c)) { n++; if (n <= 3) { extra = extra sep c; sep = ", " } }
  }
  if (n > 3) extra = extra " and " (n - 3) " more"
  line = pad "[" mark[k] "] " slug[k] (tokp[k] != "" ? " (" tokp[k] toka[k] ")" : "")
  if (extra != "") line = line " + after " extra
  print line " \302\267 " st[k]
  for (i = 1; i <= nkid[k]; i++) { c = kid[k, i]; if (!(c in seen)) show(c, depth + 1) }
}
{ sub(/\r$/, "") }
FILENAME == ARGV[1] {
  b = $1; l = substr($0, length($1) + 2)
  if (!isline(l)) next
  s = l; sub(/^\[.\][ \t]+/, "", s); sub(/[ \t].*/, "", s)
  if (b == "*") base[s] = l
  else if (s == b) own[b] = l
  if (!(s in other)) { other[s] = l; from[s] = (b == "*") ? "the default branch" : b }
  next
}
/^## / { ms = substr($0, 4); next }
isline($0) {
  k = ++nq; parse($0, k); at[slug[k]] = k; mstone[k] = ms
  if (slug[k] in base && rank(substr(base[slug[k]], 2, 1)) > rank(mark[k])) parse(base[slug[k]], k)
  if (slug[k] in own && rank(substr(own[slug[k]], 2, 1)) > rank(mark[k])) parse(own[slug[k]], k)
}
END {
  for (s in other) if (!(s in at)) { k = ++nq; parse(other[s], k); at[s] = k; mstone[k] = "only on a branch: " from[s] }
  cur = ""
  for (k = 1; k <= nq; k++) if (mark[k] != "x") { cur = mstone[k]; break }
  if (cur == "" && nq > 0 && mark[nq] == "x") { print "milestone: none open; every line is [x]"; exit }
  for (k = 1; k <= nq; k++) {
    if (mark[k] == "x") continue
    lastdep[k] = ""; best = 0
    for (i = 1; i <= nafter[k]; i++) {
      s = after[k, i]
      if ((s in at) && pending(s) && at[s] > best && at[s] != k) { best = at[s]; lastdep[k] = s }
    }
    if (best > 0 && mstone[best] == mstone[k] && best < k) kid[best, ++nkid[best]] = k
    else root[k] = 1
  }
  print "milestone: " cur
  for (k = 1; k <= nq; k++) if (mark[k] != "x" && mstone[k] == cur) st[k] = state(k)
  for (k = 1; k <= nq; k++) if (mark[k] != "x" && mstone[k] == cur && root[k] && !(k in seen)) show(k, 0)
  for (k = 1; k <= nq; k++) if (mark[k] != "x" && mstone[k] == cur && !(k in seen)) show(k, 0)
  np = ""; na = ""
  for (k = 1; k <= nq; k++) {
    if (mstone[k] != cur || mark[k] == "x" || tokp[k] == "" || st[k] !~ / now$/) continue
    if (cmd[k] == "propose") np = np " " slug[k]; else na = na " " slug[k]
  }
  print ""
  print "free for /apply, together:" (na == "" ? " none" : na)
  print "free for /propose, together:" (np == "" ? " none" : np)
  if (nj > 0) { printf "judge first, no token:"; for (i = 1; i <= nj; i++) printf " %s", judge[i]; print "" }
  for (k = 1; k <= nq; k++) if (mstone[k] ~ /^only on a branch/) { if (!h++) print "only on a branch:"; print "  " slug[k] " (" substr(mstone[k], 19) ")" }
}
' "$overlay" "$queue"
