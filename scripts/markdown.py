"""The Markdown masking shared by the checks: what a reader does not read becomes spaces."""

import re


def blank(text):
    return " " * len(text)


def mask(text, keep_targets):
    """Return the lines of text with front matter, code and HTML comments as spaces.

    With keep_targets False, link and image targets `](…)` are blanked too.
    Line numbers and columns are those of the text.
    """
    lines = text.split("\n")
    out = []
    front = bool(lines) and lines[0].strip() == "---"
    fence = None
    comment = False
    for index, line in enumerate(lines):
        if front:
            out.append(blank(line))
            if index > 0 and line.strip() == "---":
                front = False
            continue
        if fence:
            out.append(blank(line))
            if line.lstrip().startswith(fence):
                fence = None
            continue
        if not comment:
            opening = re.match(r"\s*(`{3,}|~{3,})", line)
            if opening:
                fence = opening.group(1)
                out.append(blank(line))
                continue
        kept, comment = mask_inline(line, comment, keep_targets)
        out.append(kept)
    return out


def target_end(line, i):
    """Given `](` at i, return the index of the `)` that closes the target, or the last index."""
    depth, j = 0, i + 1
    while j < len(line):
        if line[j] == "(":
            depth += 1
        elif line[j] == ")":
            depth -= 1
            if depth == 0:
                break
        j += 1
    return j


def mask_inline(line, comment, keep_targets):
    """Blank inline code, link targets and HTML comments; return (line, still inside a comment)."""
    chars = list(line)
    i = 0
    while i < len(line):
        if comment:
            end = line.find("-->", i)
            stop = len(line) if end < 0 else end + 3
            chars[i:stop] = blank(line[i:stop])
            i = stop
            comment = end < 0
            continue
        if line.startswith("<!--", i):
            comment = True
            continue
        if line[i] == "`":
            run = re.match(r"`+", line[i:]).group(0)
            end = line.find(run, i + len(run))
            if end < 0:
                i += len(run)
                continue
            stop = end + len(run)
            chars[i:stop] = blank(line[i:stop])
            i = stop
            continue
        if line.startswith("](", i):
            j = target_end(line, i)
            if not keep_targets:
                chars[i + 1:j + 1] = blank(line[i + 1:j + 1])
            i = j + 1
            continue
        i += 1
    return "".join(chars), comment
