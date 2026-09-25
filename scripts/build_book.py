#!/usr/bin/env python3
"""Build the PDF and the EPUB of both editions into output/, with pandoc and weasyprint.

Prints the path of each file it writes.
An error prints as `file:line: book: message`, or `Makefile:1: book: message` when it names no file, and exits 1.
"""

import html
import re
import shutil
import subprocess
import sys
import tempfile
from html.parser import HTMLParser
from pathlib import Path

from markdown import front_matter, mask

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "output"
PANDOC = ROOT / "pandoc"
EDITIONS = {
    "en": {"lang": "en", "name": "one-page-at-a-time"},
    "pt": {"lang": "pt-BR", "name": "uma-pagina-de-cada-vez"},
}
READ = ["-f", "markdown-tex_math_dollars", "--file-scope", "--toc"]

YAML_FIELD = re.compile(r"^(\s*)(site_author|copyright|draft_banner):\s*(.*)$")
LOCALE = re.compile(r"^(\s*)- locale:\s*(\S+)")
CHAPTER_LINK = re.compile(r"\]\(((?:[0-9]{2}|A[0-9]+)-[^)#\s]+\.md)(\s+\"[^\"]*\")?\)")
PANDOC_PLACE = re.compile(r"\"([^\"]+)\" \(line (\d+), column \d+\)")
CHAPTER_START = re.compile(r"(?=<h1[ >])")
NOTES = re.compile(r'<aside id="footnotes[^"]*" class="footnotes[^"]*"[^>]*>.*?<ol[^>]*>\n?(.*?)</ol>\s*</aside>\n?', re.S)
NOTE_NUMBER = re.compile(r'(<a\s+href="#fn\d+"\s+class="footnote-ref"[^>]*><sup>)\d+(</sup>)')


class Failed(Exception):
    pass


def unquote(value):
    if value[:1] == "'" and value[-1:] == "'":
        return value[1:-1].replace("''", "'")
    if value[:1] == '"' and value[-1:] == '"':
        return value[1:-1].replace('\\"', '"')
    return value


def site_values():
    """Read site_author, copyright and draft_banner from mkdocs.yml, per edition.

    The standard library has no YAML reader, so this reads the three keys by indentation:
    top level for English, under `- locale: pt` of the i18n plugin for Portuguese.
    """
    values = {"en": {}, "pt": {}}
    locale, indent = None, 0
    for line in (ROOT / "mkdocs.yml").read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        depth = len(line) - len(line.lstrip())
        match = LOCALE.match(line)
        if match:
            locale, indent = match.group(2), len(match.group(1))
            continue
        if locale and depth <= indent:
            locale = None
        match = YAML_FIELD.match(line)
        if match:
            target = "en" if locale is None else locale
            if target in values:
                values[target].setdefault(match.group(2), unquote(match.group(3).strip()))
    values["pt"].setdefault("site_author", values["en"].get("site_author"))
    for edition, found in values.items():
        for key in ("site_author", "copyright", "draft_banner"):
            if not found.get(key):
                raise Failed(f"mkdocs.yml:1: book: no {key} for edition {edition}")
    return values


class TextWithURLs(HTMLParser):
    """HTML turned into text, each link followed by its URL in parentheses."""

    def __init__(self):
        super().__init__()
        self.parts, self.hrefs = [], []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            self.hrefs.append(dict(attrs).get("href"))

    def handle_endtag(self, tag):
        if tag == "a" and self.hrefs:
            href = self.hrefs.pop()
            if href:
                self.parts.append(f" ({href})")

    def handle_data(self, data):
        self.parts.append(data)


def html_to_text(markup):
    parser = TextWithURLs()
    parser.feed(markup)
    parser.close()
    return "".join(parser.parts).strip()


def index_values(edition):
    """Return (title, subtitle) of book/<edition>/index.md: its H1 and its first **...** line."""
    path = Path("book") / edition / "index.md"
    _, body = front_matter((ROOT / path).read_text(encoding="utf-8"))
    title = next((line[2:].strip() for line in body if line.startswith("# ")), None)
    subtitle = next(
        (line.strip()[2:-2] for line in body if re.fullmatch(r"\*\*[^*].*\*\*", line.strip())), None
    )
    if not title or not subtitle:
        raise Failed(f"{path}:1: book: needs an H1 and a **subtitle** line")
    return title, subtitle


def chapters(edition):
    folder = ROOT / "book" / edition
    numbered = sorted(folder.glob("[0-9][0-9]-*.md"))
    appendices = sorted(folder.glob("A[0-9]*-*.md"))
    return numbered + appendices


def anchor(name):
    """The id the H1 of a chapter gets, the target of a link to the chapter without #anchor."""
    return "chapter-" + Path(name).stem


def prepare(source, names, banner):
    """Return (lines, source line of each line) of a chapter as pandoc reads it.

    The front matter goes; a draft gets the banner after its H1; the H1 gets the id `anchor`;
    a link to another chapter of the book without #anchor points to that id.
    """
    text = source.read_text(encoding="utf-8")
    fields, body = front_matter(text)
    first = len(text.splitlines()) - len(body) + 1
    masked = mask("\n".join(body), keep_targets=True)
    lines, where = [], []
    heading_done = False
    for offset, (line, seen) in enumerate(zip(body, masked)):
        number = first + offset
        for match in reversed(list(CHAPTER_LINK.finditer(seen))):
            if match.group(1) in names:
                end = match.end(1)
                line = line[:end] + "#" + anchor(match.group(1)) + line[end:]
        if not heading_done and re.match(r"# \S", seen):
            heading_done = True
            if not line.rstrip().endswith("}"):
                line = line.rstrip() + " {#" + anchor(source.name) + "}"
            lines.append(line)
            where.append(number)
            if fields.get("status") == "draft":
                for extra in ["", "::: draft-banner", banner, ":::"]:
                    lines.append(extra)
                    where.append(number)
            continue
        lines.append(line)
        where.append(number)
    return lines, where


def notes_at_chapter_end(page):
    """Move the notes of each chapter of pandoc's HTML to the chapter's end, numbered from 1.

    pandoc's --reference-location=section ends the notes at the end of the innermost section,
    an H2, and numbers them through the whole book; the PDF wants them at the end of the chapter.
    """
    end = page.rfind("</body>")
    parts = CHAPTER_START.split(page[:end])
    for index, part in enumerate(parts):
        items = "".join(NOTES.findall(part))
        if not items:
            continue
        numbers = iter(range(1, part.count("footnote-ref") + 1))
        part = NOTE_NUMBER.sub(lambda match: f"{match.group(1)}{next(numbers)}{match.group(2)}", NOTES.sub("", part))
        parts[index] = (
            part + '<aside class="footnotes" role="doc-endnotes">\n<hr />\n<ol>\n' + items + "</ol>\n</aside>\n"
        )
    return "".join(parts) + page[end:]


def run(command, places, cwd=ROOT):
    """Run pandoc or weasyprint; print its warnings as findings, and on failure raise Failed with one finding."""
    done = subprocess.run(command, cwd=cwd, capture_output=True, text=True)
    messages = [line.strip() for line in done.stderr.splitlines() if line.strip()]
    if done.returncode != 0:
        message = " ".join(messages) or f"{command[0]} exited with {done.returncode}"
        raise Failed(finding(message, places))
    for message in messages:
        print(finding(message, places))


def finding(message, places):
    """`file:line: book: message` when the message names a chapter, `Makefile:1: book: message` otherwise.

    pandoc names the copy it read; the line becomes the line of the chapter in book/.
    """
    match = PANDOC_PLACE.search(message)
    if match and Path(match.group(1)).name in places:
        source, where = places[Path(match.group(1)).name]
        line = min(int(match.group(2)), len(where))
        number = where[line - 1] if line else 1
        text = (message[:match.start()].rstrip().removesuffix(" at") + message[match.end():]).strip()
        return f"{source}:{number}: book: {text}"
    return f"Makefile:1: book: {message}"


def build(edition, site, work):
    settings = EDITIONS[edition]
    title, subtitle = index_values(edition)
    author = site[edition]["site_author"]
    rights = html_to_text(site[edition]["copyright"])
    sources = chapters(edition)
    names = {source.name for source in sources}
    places = {}
    inputs = []
    for source in sources:
        lines, where = prepare(source, names, site[edition]["draft_banner"])
        copy = work / source.name
        copy.write_text("\n".join(lines) + "\n", encoding="utf-8")
        places[source.name] = (source.relative_to(ROOT), where)
        inputs.append(source.name)
    common = READ + [
        f"--resource-path={ROOT / 'book' / edition}:{ROOT / 'book'}",
        "-M", f"lang={settings['lang']}",
    ]

    front = work / "front.html"
    front.write_text(
        '<section class="title-page">\n'
        f'<h1 class="title">{html.escape(title)}</h1>\n'
        f'<p class="subtitle">{html.escape(subtitle)}</p>\n'
        f'<p class="author">{html.escape(author)}</p>\n'
        "</section>\n"
        f'<section class="rights-page">\n<p>{html.escape(rights)}</p>\n</section>\n',
        encoding="utf-8",
    )
    page = work / "book.html"
    run(
        ["pandoc", *inputs, *common, "--reference-location=section", "-s", "-t", "html5",
         "--css", (PANDOC / "pdf.css").as_uri(),
         "-M", f"pagetitle={title}",
         "--include-before-body", str(front), "-o", str(page)],
        places, work,
    )
    # The return arrow of a note comes with U+FE0E, which no font of the book has.
    text = notes_at_chapter_end(page.read_text(encoding="utf-8")).replace("\ufe0e", "")
    page.write_text(text, encoding="utf-8")
    pdf = OUTPUT / f"{settings['name']}.pdf"
    run(["weasyprint", "--base-url", str(ROOT / "book" / edition) + "/", str(page), str(pdf)], places)

    epub = OUTPUT / f"{settings['name']}.epub"
    run(
        ["pandoc", *inputs, *common, "-t", "epub3",
         "--css", str(PANDOC / "epub.css"),
         "-M", f"title={title}", "-M", f"subtitle={subtitle}",
         "-M", f"author={author}", "-M", f"rights={rights}",
         "-o", str(epub)],
        places, work,
    )
    return [pdf, epub]


def main():
    for tool in ("pandoc", "weasyprint"):
        if shutil.which(tool) is None:
            print(f"Makefile:1: book: {tool} not found; install it (see README)")
            return 1
    try:
        site = site_values()
        OUTPUT.mkdir(exist_ok=True)
        written = []
        for edition in EDITIONS:
            with tempfile.TemporaryDirectory() as work:
                written += build(edition, site, Path(work))
    except Failed as failure:
        print(failure)
        return 1
    for path in written:
        print(path.relative_to(ROOT))
    return 0


if __name__ == "__main__":
    sys.exit(main())
