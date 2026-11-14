#!/bin/sh
# focus-kit: draw every open milestone of docs/06 as a tree of what waits
# on what, and say what may run now, as docs/05 §4 says. Run it through git:
#   git -c "alias.fq=!sh .agents/skills/propose/scripts/queue.sh" fq <strategy>
# <strategy> is the Git slot of docs/05: trunk | branch | worktree <hidden> <prefix>
# With a branch or worktree per delivery, each delivery's line is read from
# its branch on origin, which is its own copy until the delivery is
# integrated; a branch on origin is a claim.
# A [?] blocks on the copy that put it, as docs/05 §4 says. A branch's or
# a worktree's blocks when that copy changed the line since it left the
# default branch: the line differs from the one at their merge-base, or
# was not there. With no merge-base, every line counts as changed. The
# default branch's blocks unless the copy of the line's own slug changed
# the line. None blocks a winning [x]. When several hold, the reason shown
# is the default branch's, then the other branches' by name, then the own
# copy's.
# A milestone is the base's heading. A line only a branch or a worktree
# has takes the base's heading of the lines that share its heading in
# that copy, so a copy that rewords a heading keeps its lines in place.
# A line goes under the last line it waits on; "+ after" names the others.
# "after all" leaves out the milestone's dropped lines; a line that
# names a dropped one waits for the person to re-decide.
# "findings:" counts the milestone's lines that end "from <slug>", and a
# warning names the open ones that stand ahead of an open planned line,
# but not one an open line names in its "after" or "blocked: after".
# A line only the local file has, as a fix written in a delivery's
# worktree, is read from it.
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
      # The queue where the branch left the default branch, tagged "^slug";
      # the local tree stands for the branch of its own slug, below.
      if [ -n "$default" ] && [ "$slug" != "$here" ]; then
        mb=$(git merge-base "$ref" "refs/remotes/origin/$default" 2>/dev/null) || mb=
        if [ -n "$mb" ]; then
          git show "$mb:$rel" 2>/dev/null | awk "$join" | awk -v s="^$slug" "$tag" >> "$overlay" || true
        fi
      fi
    fi
    git show "$ref:$rel" 2>/dev/null | awk "$join" | awk -v s="$slug" "$tag" >> "$overlay" || true
  done
  # In a worktree or on a branch, the local tree is the own copy: its
  # queue where HEAD left the default branch.
  if [ -n "$here" ] && [ -n "$default" ]; then
    mb=$(git merge-base HEAD "refs/remotes/origin/$default" 2>/dev/null) || mb=
    if [ -n "$mb" ]; then
      git show "$mb:$rel" 2>/dev/null | awk "$join" | awk -v s="^$here" "$tag" >> "$overlay" || true
    fi
  fi
fi

awk "$join" "$queue" | awk -F '\t' -v strategy="$strategy" -v here="$here" '
# Copies of a line, by slug: the base is origin'"'"'s default branch (in a
# worktree or on a branch) or the local file (in main/, on trunk); a
# delivery branch on origin holds its own slug'"'"'s copy, and the local file
# is the own copy of the slug whose worktree or branch this is. The own copy
# wins for its slug until the delivery is integrated, then the base wins.
# A branch still where the claim created it is an ancestor of the base
# without being integrated: there the local copy wins until the base says
# [x], and its own [x] is built, awaiting integration.
# A [?] shows the line blocked unless the winner is [x], when the copy that
# holds it put it there (docs/05 §4; see blocking() below). A branch
# on origin whose winning copy is still [ ] is claimed, progress unknown,
# once nothing in its after is left to wait on.
function sl(line,   s) { s = line; sub(/^\[.\][ \t]+/, "", s); sub(/[ \t].*/, "", s); return s }
function isline(s) { return s ~ /^\[[ ~>*x?]\][ \t]+[^ \t]/ }
function parse(line, k,   rest, n, parts, i, p, deps, j, m) {
  mark[k] = substr(line, 2, 1)
  rest = substr(line, 4); sub(/^[ \t]+/, "", rest)
  slug[k] = rest; sub(/[ \t].*/, "", slug[k])
  rest = substr(rest, length(slug[k]) + 1); sub(/^[ \t]+/, "", rest)
  nafter[k] = 0; resume[k] = ""; blocked[k] = ""; dropped[k] = 0; all[k] = 0; found[k] = 0
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
    else if (p ~ /^from [a-zA-Z0-9._-]+[ \t]*$/) found[k] = 1
  }
}
function add(s, line, ms, src,   k) {
  k = ++nq; parse(line, k); at[s] = k; mstone[k] = ms; from[k] = src
  if (s in blockedcopy && mark[k] != "x") { parse(blockedcopy[s], k); mstone[k] = ms }
  if (strategy == "trunk") integrated[k] = (mark[k] == "x")
  else integrated[k] = ((s in basemark) && basemark[s] == "x") || ((s in integ) && s != here)
  if (mark[k] == "x" && !integrated[k]) built[k] = 1
  if (mark[k] == " " && (s in claimed)) claimedk[k] = 1
}
# A copy changed a line when its mark or its text after the slug differs
# from the line at the copy'"'"'s merge-base, or the line was not there.
function key(l,   r) { r = l; sub(/^\[.\][ \t]+[^ \t]+[ \t]*/, "", r); return substr(l, 2, 1) " " r }
function asks(l) { return substr(l, 2, 1) == "?" }
function lineof(c, s) {
  if (here != "" && c == here) return (s in local) ? local[s] : ""
  return ((c, s) in copyl) ? copyl[c, s] : ""
}
# A copy may reword a milestone'"'"'s heading, as a branch that moved its
# dates did: a line the base lacks takes the base'"'"'s heading of the lines
# that share its heading in that copy.
function home(c, t) { return ((c, t) in tr) ? tr[c, t] : t }
function changed(c, s, l) { return !((c, s) in mb) || mb[c, s] != key(l) }
# The [?] that blocks slug s, or "": the default branch'"'"'s (the local file
# too, in main/ and on trunk) unless the own copy changed the line; then
# each other copy that changed it, by branch name; then the own copy.
function blocking(s,   o, ownc, i, c, l) {
  o = (s in iscopy) ? lineof(s, s) : ""
  ownc = (o != "") && changed(s, s, o)
  if (!ownc) {
    if (here == "" && (s in local) && asks(local[s])) return local[s]
    if ((s in obase) && asks(obase[s])) return obase[s]
  }
  for (i = 1; i <= ncopy; i++) {
    c = copies[i]
    if (c == s) continue
    l = lineof(c, s)
    if (l != "" && asks(l) && changed(c, s, l)) return l
  }
  if (ownc && asks(o)) return o
  return ""
}
function defined(k) { return mark[k] ~ /[>*x]/ || (mark[k] == "?" && resume[k] == "apply") }
function done(k) { return mark[k] == "x" && integrated[k] }
function deps(k, i,   j, n) {
  n = 0
  for (j = 1; j <= nafter[k]; j++) dep[k, ++n] = after[k, j]
  if (all[k]) for (j = 1; j < k; j++) if (mstone[j] == mstone[k] && !dropped[j]) dep[k, ++n] = slug[j]
  ndep[k] = n
}
function few(list, n, what) { return ((n <= 3) ? list : list " and " (n - 3) " more") (what == "" ? "" : " " what) }
function state(k,   i, s, d, why, sep, ok, nd, dl, ds, nb, bl, bs, nw, wl, ws) {
  if (mark[k] == "~") return "in flight: propose"
  if (mark[k] == "*") return "in flight: apply"
  if (mark[k] == "?") return "blocked: " blocked[k] (resume[k] != "" ? ", then " resume[k] : "")
  if (built[k]) return "built, awaiting integration"
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
  if (claimedk[k]) { cmd[k] = ""; return "claimed, progress unknown: propose in flight" }
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
  if (substr(b, 1, 1) == "^") { mb[substr(b, 2), s] = key(l); next }
  if (b == "*") { obase[s] = l; obasems[s] = ms }
  else if (s == b) { own[s] = l; ownms[s] = ms }
  else if (!(s in other)) { other[s] = l; otherms[s] = ms; otherfrom[s] = b }
  if (b != "*") {
    if (!(b in iscopy)) { iscopy[b] = 1; copies[++ncopy] = b }
    copyl[b, s] = l
    cq[++ncq] = b; sq[ncq] = s; mq[ncq] = ms
  }
  slugs[s] = 1
  next
}
/^## / { lms = substr($0, 4); next }
isline($0) {
  s = sl($0)
  if (s in local) { nerr++; err[nerr] = s " appears twice; the second line is ignored"; next }
  local[s] = $0; localms[s] = lms; lorder[++nl] = s
  slugs[s] = 1
}
END {
  # The local tree is the copy of the branch whose worktree this is.
  if (here != "" && !(here in iscopy)) { iscopy[here] = 1; copies[++ncopy] = here }
  for (s in slugs) { l = blocking(s); if (l != "") blockedcopy[s] = l }
  # The base copy of every slug, then the order of the lines.
  if (here != "") { for (s in obase) { basemark[s] = substr(obase[s], 2, 1); base[s] = obase[s]; basems[s] = obasems[s] } }
  else { for (s in local) { basemark[s] = substr(local[s], 2, 1); base[s] = local[s]; basems[s] = localms[s] } }
  if (here != "" && (here in local)) { own[here] = local[here]; ownms[here] = localms[here] }
  if (here != "") for (i = 1; i <= nl; i++) { cq[++ncq] = here; sq[ncq] = lorder[i]; mq[ncq] = localms[lorder[i]] }
  for (i = 1; i <= ncq; i++) {
    s = sq[i]
    if (!(s in base)) continue
    v = ++vote[cq[i], mq[i], basems[s]]
    if (v > top[cq[i], mq[i]]) { top[cq[i], mq[i]] = v; tr[cq[i], mq[i]] = basems[s] }
  }
  for (i = 1; i <= nl; i++) order[++no] = lorder[i]
  if (here != "") for (s in obase) if (!(s in local)) order[++no] = s
  for (i = 1; i <= no; i++) {
    s = order[i]
    if ((s in own) && (!(s in integ) || (s == here && basemark[s] != "x"))) { line = own[s]; ms = home(s, ownms[s]) }
    else if (s in base) line = base[s]
    else if (s in own) { line = own[s]; ms = home(s, ownms[s]) }
    else { line = local[s]; ms = home(here, localms[s]) }
    if (s in base) ms = basems[s]
    add(s, line, ms, "")
  }
  for (s in other) if (!(s in at)) { add(s, other[s], home(otherfrom[s], otherms[s]), otherfrom[s]); xtra[nq] = 1 }
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
  # The open milestones, in order.
  nms = 0
  for (i = 1; i <= n; i++) { k = ord[i]; if (!done(k) && !(mstone[k] in isopen)) { isopen[mstone[k]] = 1; msl[++nms] = mstone[k] } }
  if (nms == 0 && nq > 0) { print "milestone: none open; every line is [x]"; exit }
  if (nms == 0) msl[++nms] = ""
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
    for (j = 1; j <= nafter[k]; j++) wanted[after[k, j]] = 1
    if (blocked[k] ~ /^after /) {
      w = blocked[k]; sub(/^after /, "", w)
      nw = split(w, wl, /, */)
      for (j = 1; j <= nw; j++) wanted[wl[j]] = 1
    }
  }
  # Every open milestone is drawn, so a blocked one hides no free line.
  np = ""; na = ""; next_slug = ""
  for (m = 1; m <= nms; m++) {
    cur = msl[m]
    if (m > 1) print ""
    print "milestone: " cur
    nf = 0; nfo = 0; npo = 0; last = 0; above = 0; al = ""; asep = ""
    for (i = 1; i <= n; i++) {
      k = ord[i]
      if (mstone[k] != cur || dropped[k]) continue
      if (found[k]) { nf++; if (!done(k)) nfo++ }
      else if (!done(k) && !all[k]) { npo++; last = i }
    }
    for (i = 1; i < last; i++) {
      k = ord[i]
      if (mstone[k] != cur || !found[k] || dropped[k] || done(k) || (slug[k] in wanted)) continue
      above++; if (above <= 3) { al = al asep slug[k]; asep = ", " }
    }
    if (nf > 0) print "findings: " nfo " open of " nf " from a finding \302\267 " npo " planned open"
    if (above > 0) print "\342\232\240\357\270\217 ahead of planned lines: " few(al, above, "")
    for (i = 1; i <= n; i++) { k = ord[i]; if (!done(k) && mstone[k] == cur) st[k] = state(k) }
    for (i = 1; i <= n; i++) { k = ord[i]; if (!done(k) && mstone[k] == cur && root[k] && !(k in seen)) show(k, 0) }
    for (i = 1; i <= n; i++) { k = ord[i]; if (!done(k) && mstone[k] == cur && !(k in seen)) show(k, 0) }
    for (i = 1; i <= n; i++) {
      k = ord[i]
      if (mstone[k] != cur || done(k) || st[k] !~ / now$/) continue
      if (cmd[k] == "propose") np = np " " slug[k]; else na = na " " slug[k]
      if (next_slug == "") next_slug = "/" cmd[k] " " slug[k]
    }
  }
  print ""
  print "free for /apply, in order:" (na == "" ? " none" : na)
  print "free for /propose, in order:" (np == "" ? " none" : np)
  print "next: " (next_slug == "" ? "none" : next_slug)
  for (i = 1; i <= n; i++) {
    k = ord[i]
    if (done(k)) continue
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
