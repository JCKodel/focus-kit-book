#!/bin/sh
# focus-kit: draw docs/06's current milestone as a tree of what waits on
# what, and say what may run now, as docs/05 §4 says. Run it through git:
#   git -c "alias.fq=!sh .agents/skills/propose/scripts/queue.sh" fq <strategy>
# <strategy> is the Git slot of docs/05: trunk | branch | worktree <hidden> <prefix>
# With a branch or worktree per delivery, each delivery's line is read from
# its branch on origin, which is its own copy until the delivery is
# integrated; a branch on origin is a claim; a [?] on any copy blocks. A
# line goes under the last line it waits on; "+ after" names the others.
# A wrapped line is read whole. Edits nothing.
set -eu

die() { printf 'error: %s\n' "$1"; exit 2; }

strategy=${1:-}
case $strategy in
  trunk) prefix= ; hidden= ;;
  branch) prefix= ; hidden= ;;
  worktree) hidden=${2:-}; prefix=${3:-}; [ -n "$hidden" ] && [ -n "$prefix" ] || die "worktree needs the hidden folder and the branch prefix: worktree .focus-kit focus-kit/"; hidden=${hidden%/} ;;
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

# join: a physical line that starts with whitespace, after a queue line, is
# the rest of that line. Everything else passes through, CR removed.
join='{ sub(/\r$/, "") }
  /^[ \t]+[^ \t]/ && held != "" { sub(/^[ \t]+/, " "); held = held $0; next }
  { if (held != "") print held; held = "" }
  /^\[[ ~>*x?]\][ \t]+[^ \t]/ { held = $0; next }
  { print }
  END { if (held != "") print held }'

# tag: records "src \t milestone \t line" for the awk below.
tag='/^## / { ms = substr($0, 4); next } { print s "\t" ms "\t" $0 }'

overlay=$(mktemp)
trap 'rm -f "$overlay"' EXIT
# here: the slug whose own copy the local file is, when run in its worktree
# or on its branch; empty in main/ and on trunk.
here=
if [ "$strategy" != trunk ] && git remote get-url origin >/dev/null 2>&1; then
  git fetch -q origin 2>/dev/null || printf 'note: git fetch origin failed; branches as last fetched\n'
  default=$(git symbolic-ref --quiet --short refs/remotes/origin/HEAD 2>/dev/null | sed 's|^origin/||') || true
  [ -n "$default" ] || for b in main master; do
    if git show-ref --quiet "refs/remotes/origin/$b"; then default=$b; break; fi
  done
  head=$(git symbolic-ref --quiet --short HEAD 2>/dev/null || true)
  case $strategy in
    worktree) case $top in */"$hidden"/worktrees/*) here=${top##*/} ;; esac ;;
    branch) [ "$head" = "$default" ] || here=$head ;;
  esac
  case $here in ''|*[!a-zA-Z0-9._-]*) here= ;; esac
  git for-each-ref --format='%(refname)' refs/remotes/origin | while read -r ref; do
    name=${ref#refs/remotes/origin/}
    if [ "$name" = "$default" ]; then slug='*'
    else
      case $name in HEAD) continue ;; "$prefix"*) ;; *) continue ;; esac
      slug=${name#"$prefix"}
      case $slug in ''|*[!a-zA-Z0-9._-]*) continue ;; esac
      printf '%s\t@claimed\t\n' "$slug" >> "$overlay"
      if [ -n "$default" ] && git merge-base --is-ancestor "$ref" "refs/remotes/origin/$default" 2>/dev/null; then
        printf '%s\t@integrated\t\n' "$slug" >> "$overlay"
      fi
    fi
    git show "$ref:$rel" 2>/dev/null | awk "$join" | awk -v s="$slug" "$tag" >> "$overlay" || true
  done
fi

awk "$join" "$queue" | awk -F '\t' -v strategy="$strategy" -v here="$here" '
# Copies of a line, by slug: the base is origin'"'"'s default branch (in a
# worktree or on a branch) or the local file (in main/, on trunk); a
# delivery branch on origin holds its own slug'"'"'s copy, and the local file
# is the own copy of the slug whose worktree or branch this is. The own copy
# wins for its slug until the delivery is integrated, then the base wins.
# Any copy at [?] shows the line blocked unless the winner is [x]. A branch
# on origin whose winning copy is still [ ] is claimed, progress unknown.
function sl(line,   s) { s = line; sub(/^\[.\][ \t]+/, "", s); sub(/[ \t].*/, "", s); return s }
function isline(s) { return s ~ /^\[[ ~>*x?]\][ \t]+[^ \t]/ }
function parse(line, k,   rest, n, parts, i, p, deps, j, m) {
  mark[k] = substr(line, 2, 1)
  rest = substr(line, 4); sub(/^[ \t]+/, "", rest)
  slug[k] = rest; sub(/[ \t].*/, "", slug[k])
  rest = substr(rest, length(slug[k]) + 1); sub(/^[ \t]+/, "", rest)
  nafter[k] = 0; resume[k] = ""; blocked[k] = ""; dropped[k] = 0; all[k] = 0
  n = split(rest, parts, " \302\267 ")
  for (i = 2; i <= n; i++) {
    p = parts[i]
    if (p ~ /^after /) {
      sub(/^after /, "", p)
      if (p == "all") { all[k] = 1; continue }
      m = split(p, deps, /, */)
      for (j = 1; j <= m; j++) if (deps[j] != "") after[k, ++nafter[k]] = deps[j]
    } else if (p ~ /^resume: /) { sub(/^resume: /, "", p); resume[k] = p }
    else if (p ~ /^blocked: /) { sub(/^blocked: /, "", p); blocked[k] = p }
    else if (p ~ /^dropped: /) dropped[k] = 1
  }
}
function add(s, line, ms, src,   k) {
  k = ++nq; parse(line, k); at[s] = k; mstone[k] = ms; from[k] = src
  if (s in blockedcopy && mark[k] != "x") { parse(blockedcopy[s], k); mstone[k] = ms }
  if (strategy == "trunk") integrated[k] = (mark[k] == "x")
  else integrated[k] = ((s in basemark) && basemark[s] == "x") || (s in integ)
  if (mark[k] == "x" && !integrated[k]) built[k] = 1
  if (mark[k] == " " && (s in claimed)) claimedk[k] = 1
}
function defined(k) { return mark[k] ~ /[>*x]/ || (mark[k] == "?" && resume[k] == "apply") }
function done(k) { return mark[k] == "x" && integrated[k] }
function deps(k, i,   j, n) {
  n = 0
  for (j = 1; j <= nafter[k]; j++) dep[k, ++n] = after[k, j]
  if (all[k]) for (j = 1; j < k; j++) if (mstone[j] == mstone[k]) dep[k, ++n] = slug[j]
  ndep[k] = n
}
function few(list, n, what) { return ((n <= 3) ? list : list " and " (n - 3) " more") (what == "" ? "" : " " what) }
function state(k,   i, s, d, why, sep, ok, nd, dl, ds, nb, bl, bs, nw, wl, ws) {
  if (mark[k] == "~") return "in flight: propose"
  if (mark[k] == "*") return "in flight: apply"
  if (mark[k] == "?") return "blocked: " blocked[k] (resume[k] != "" ? ", then " resume[k] : "")
  if (built[k]) return "built, awaiting integration"
  if (claimedk[k]) return "claimed, progress unknown: propose in flight"
  cmd[k] = (mark[k] == ">") ? "apply" : "propose"
  why = ""; sep = ""; nd = 0; dl = ""; ds = ""; nb = 0; bl = ""; bs = ""; nw = 0; wl = ""; ws = ""
  for (i = 1; i <= ndep[k]; i++) {
    s = dep[k, i]
    if (s == slug[k]) { why = why sep "after itself"; sep = "; "; continue }
    if (!(s in at)) { why = why sep s " is not in the queue"; sep = "; "; continue }
    d = at[s]
    if (dropped[d]) { why = why sep "after " s ", dropped: re-decide"; sep = "; "; continue }
    if (cmd[k] == "propose") ok = defined(d); else ok = done(d)
    if (ok) continue
    if (cmd[k] == "apply" && mark[d] == "x") { nb++; if (nb <= 3) { bl = bl bs s; bs = ", " } }
    else if (cmd[k] == "apply") { nw++; if (nw <= 3) { wl = wl ws s; ws = ", " } }
    else { nd++; if (nd <= 3) { dl = dl ds s; ds = ", " } }
  }
  if (nw > 0) { why = why sep "after " few(wl, nw, "") ; sep = "; " }
  if (nb > 0) { why = why sep few(bl, nb, "built, not integrated"); sep = "; " }
  if (nd > 0) { why = why sep few(dl, nd, "not defined"); sep = "; " }
  if (why != "") { cmd[k] = ""; return "waits: " why }
  return cmd[k] " now"
}
function show(k, depth,   pad, i, c, extra, sep, line, n) {
  seen[k] = 1
  pad = ""; for (i = 1; i < 2 * depth; i++) pad = pad " "
  if (depth > 0) pad = pad "\342\224\224"
  extra = ""; sep = ""; n = 0
  for (i = 1; i <= ndep[k]; i++) {
    c = dep[k, i]
    if (c != lastdep[k] && c in at && !done(at[c])) { n++; if (n <= 3) { extra = extra sep c; sep = ", " } }
  }
  if (n > 3) extra = extra " and " (n - 3) " more"
  line = pad "[" mark[k] "] " slug[k]
  if (extra != "") line = line " + after " extra
  if (from[k] != "") line = line " (only on branch " from[k] ")"
  print line " \302\267 " st[k]
  for (i = 1; i <= nkid[k]; i++) { c = kid[k, i]; if (!(c in seen)) show(c, depth + 1) }
}
function cycle(k, start,   i, s, d) {
  if (visiting[k]) return (k == start)
  visiting[k] = 1
  for (i = 1; i <= ndep[k]; i++) { s = dep[k, i]; if (s in at) { d = at[s]; if (d != k && cycle(d, start)) { visiting[k] = 0; return 1 } } }
  visiting[k] = 0
  return 0
}
FILENAME == ARGV[1] {
  b = $1; ms = $2; l = $3
  if (ms == "@claimed") { claimed[b] = 1; next }
  if (ms == "@integrated") { integ[b] = 1; next }
  if (!isline(l)) next
  s = sl(l)
  if (b == "*") { obase[s] = l; obasems[s] = ms }
  else if (s == b) { own[s] = l; ownms[s] = ms }
  else if (!(s in other)) { other[s] = l; otherms[s] = ms; otherfrom[s] = b }
  if (substr(l, 2, 1) == "?" && !(s in blockedcopy)) blockedcopy[s] = l
  next
}
/^## / { lms = substr($0, 4); next }
isline($0) {
  s = sl($0)
  if (s in local) { nerr++; err[nerr] = s " appears twice; the second line is ignored"; next }
  local[s] = $0; localms[s] = lms; lorder[++nl] = s
  if (substr($0, 2, 1) == "?" && !(s in blockedcopy)) blockedcopy[s] = $0
}
END {
  # The base copy of every slug, then the order of the lines.
  if (here != "") { for (s in obase) { basemark[s] = substr(obase[s], 2, 1); base[s] = obase[s]; basems[s] = obasems[s] } }
  else { for (s in local) { basemark[s] = substr(local[s], 2, 1); base[s] = local[s]; basems[s] = localms[s] } }
  if (here != "" && (here in local)) { own[here] = local[here]; ownms[here] = localms[here] }
  for (i = 1; i <= nl; i++) order[++no] = lorder[i]
  if (here != "") for (s in obase) if (!(s in local)) order[++no] = s
  for (i = 1; i <= no; i++) {
    s = order[i]
    if ((s in own) && !(s in integ)) { line = own[s]; ms = ownms[s] }
    else if (s in base) { line = base[s]; ms = basems[s] }
    else { line = own[s]; ms = ownms[s] }
    if (ms == "" && (s in base)) ms = basems[s]
    add(s, line, ms, "")
  }
  for (s in other) if (!(s in at)) { add(s, other[s], otherms[s], otherfrom[s]); xtra[nq] = 1 }
  # A line only a branch has goes at the end of its milestone.
  n = 0
  for (k = 1; k <= nq; k++) if (!(k in xtra)) ord[++n] = k
  for (k = 1; k <= nq; k++) if (k in xtra) {
    pos = n
    for (i = n; i >= 1; i--) if (mstone[ord[i]] == mstone[k]) { pos = i; break }
    for (i = n; i > pos; i--) ord[i + 1] = ord[i]
    ord[pos + 1] = k; n++
  }
  for (i = 1; i <= n; i++) { k = ord[i]; nm[k] = i }
  for (k = 1; k <= nq; k++) at[slug[k]] = k
  cur = ""
  for (i = 1; i <= n; i++) { k = ord[i]; if (!done(k)) { cur = mstone[k]; break } }
  if (cur == "" && nq > 0) { print "milestone: none open; every line is [x]"; exit }
  for (i = 1; i <= n; i++) {
    k = ord[i]
    if (done(k)) continue
    deps(k, i)
    lastdep[k] = ""; best = 0
    for (j = 1; j <= ndep[k]; j++) {
      s = dep[k, j]
      if ((s in at) && !done(at[s]) && nm[at[s]] > best && at[s] != k) { best = nm[at[s]]; lastdep[k] = s }
    }
    if (best > 0 && best < i && mstone[ord[best]] == mstone[k]) kid[ord[best], ++nkid[ord[best]]] = k
    else root[k] = 1
  }
  print "milestone: " cur
  for (i = 1; i <= n; i++) { k = ord[i]; if (!done(k) && mstone[k] == cur) st[k] = state(k) }
  for (i = 1; i <= n; i++) { k = ord[i]; if (!done(k) && mstone[k] == cur && root[k] && !(k in seen)) show(k, 0) }
  for (i = 1; i <= n; i++) { k = ord[i]; if (!done(k) && mstone[k] == cur && !(k in seen)) show(k, 0) }
  np = ""; na = ""; next_slug = ""
  for (i = 1; i <= n; i++) {
    k = ord[i]
    if (mstone[k] != cur || done(k) || st[k] !~ / now$/) continue
    if (cmd[k] == "propose") np = np " " slug[k]; else na = na " " slug[k]
    if (next_slug == "") next_slug = "/" cmd[k] " " slug[k]
  }
  print ""
  print "free for /apply, in order:" (na == "" ? " none" : na)
  print "free for /propose, in order:" (np == "" ? " none" : np)
  print "next: " (next_slug == "" ? "none" : next_slug)
  for (i = 1; i <= n; i++) {
    k = ord[i]
    if (done(k) || mstone[k] != cur) continue
    for (j = 1; j <= ndep[k]; j++) {
      s = dep[k, j]
      if (s == slug[k]) { nerr++; err[nerr] = slug[k] " waits on itself" }
      else if (!(s in at)) { nerr++; err[nerr] = slug[k] " waits on " s ", which is not in the queue" }
    }
    if (cycle(k, k)) { nerr++; err[nerr] = slug[k] " is in a cycle of after" }
  }
  if (nerr > 0) { print "errors:"; for (i = 1; i <= nerr; i++) print "  " err[i] }
}
' "$overlay" -
