#!/usr/bin/env python3
"""Regenerate The EU AI Act Informer from posts/YYYY-MM-DD/post.md.

Python 3 standard library only. Reads each post's front matter and markdown
body, then writes index.html, archive/index.html, posts/YYYY-MM-DD/index.html,
posts/posts.json, and 404.html.
"""

from __future__ import annotations

import html
import json
import posixpath
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
POSTS_DIR = ROOT / "posts"
SITE_TITLE = "The EU AI Act Informer"
TAGLINE = "One key takeaway from the EU AI Act, every weekday."
FOOTER_NOTE = "Takeaways written by bot Ursula. Not legal advice."
EUR_LEX = "https://eur-lex.europa.eu/eli/reg/2024/1689/oj"
EUR_LEX_LABEL = "Regulation (EU) 2024/1689 on EUR-Lex"

_INLINE = re.compile(
    r"\[([^\]\n]+)\]\(([^)\s]+)\)"
    r"|\*\*([^*\n]+)\*\*"
    r"|\*([^*\n]+)\*"
    r"|_([^_\n]+)_"
)


def die(message: str) -> None:
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(1)


def rel_link(from_page: str, to_url: str) -> str:
    """Relative URL from an HTML page to another site path."""
    from_dir = posixpath.dirname(from_page)
    if from_dir in ("", "."):
        from_dir = "."
    trailing = to_url.endswith("/")
    rel = posixpath.relpath(to_url, from_dir)
    if trailing and rel != "." and not rel.endswith("/"):
        rel += "/"
    if rel == ".":
        return "./"
    return rel


def render_inline(text: str) -> str:
    """Convert bold, italic, and links. Everything else is escaped."""
    parts: list[str] = []
    pos = 0
    for match in _INLINE.finditer(text):
        parts.append(html.escape(text[pos : match.start()]))
        label, url, bold, italic_star, italic_under = match.groups()
        if label is not None:
            parts.append(
                f'<a href="{html.escape(url, quote=True)}">{html.escape(label)}</a>'
            )
        elif bold is not None:
            parts.append(f"<strong>{html.escape(bold)}</strong>")
        else:
            inner = italic_star if italic_star is not None else italic_under
            parts.append(f"<em>{html.escape(inner)}</em>")
        pos = match.end()
    parts.append(html.escape(text[pos:]))
    return "".join(parts)


def markdown_to_html(source: str) -> str:
    """Paragraphs separated by blank lines, plus inline markdown."""
    blocks = re.split(r"\n\s*\n", source.strip())
    paragraphs: list[str] = []
    for block in blocks:
        text = " ".join(line.strip() for line in block.splitlines() if line.strip())
        if text:
            paragraphs.append(f"<p>{render_inline(text)}</p>")
    return "\n".join(paragraphs)


def parse_front_matter(path: Path) -> tuple[dict[str, str], str]:
    raw = path.read_text(encoding="utf-8").lstrip("\ufeff")
    lines = raw.splitlines()
    if not lines or lines[0].strip() != "---":
        die(f"{path}: front matter must start with ---")
    try:
        end = lines.index("---", 1)
    except ValueError:
        die(f"{path}: front matter is not closed")
    meta: dict[str, str] = {}
    for line in lines[1:end]:
        if not line.strip():
            continue
        if ":" not in line:
            die(f"{path}: bad front matter line: {line}")
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]
        meta[key] = value
    body = "\n".join(lines[end + 1 :]).strip()
    return meta, body


def load_posts() -> list[dict[str, str]]:
    paths = sorted(POSTS_DIR.glob("*/post.md"))
    if not paths:
        die("no posts found at posts/YYYY-MM-DD/post.md")
    posts: list[dict[str, str]] = []
    for path in paths:
        meta, body = parse_front_matter(path)
        for key in ("date", "lens", "headline", "source"):
            if key not in meta:
                die(f"{path}: missing {key}")
        folder = path.parent.name
        if meta["date"] != folder:
            die(f"{path}: date {meta['date']} does not match folder {folder}")
        try:
            parsed = date.fromisoformat(meta["date"])
        except ValueError:
            die(f"{path}: date must be YYYY-MM-DD")
        if not meta["lens"].strip() or not meta["headline"].strip():
            die(f"{path}: lens and headline must not be empty")
        display = f"{parsed.strftime('%A')} {parsed.day} {parsed.strftime('%B %Y')}"
        posts.append(
            {
                "date": meta["date"],
                "lens": meta["lens"],
                "headline": meta["headline"],
                "source": meta["source"],
                "body": body,
                "display_date": display,
                "body_html": markdown_to_html(body),
                "path": f"posts/{meta['date']}/",
            }
        )
    posts.sort(key=lambda post: post["date"], reverse=True)
    return posts


def page_html(*, page: str, title: str, main: str) -> str:
    css = html.escape(rel_link(page, "styles.css"), quote=True)
    icon = html.escape(rel_link(page, "favicon.svg"), quote=True)
    home = html.escape(rel_link(page, "index.html"), quote=True)
    safe_title = html.escape(title)
    description = html.escape(TAGLINE)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{safe_title}</title>
  <meta name="description" content="{description}">
  <link rel="icon" href="{icon}" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&amp;display=swap">
  <link rel="stylesheet" href="{css}">
</head>
<body>
  <div class="wrap">
    <header>
      <a class="site-title" href="{home}">{html.escape(SITE_TITLE)}</a>
      <p class="tagline">{html.escape(TAGLINE)}</p>
    </header>
    <main id="main">
{main}
    </main>
    <footer>
      <p>{html.escape(FOOTER_NOTE)}</p>
      <p><a href="{html.escape(EUR_LEX, quote=True)}">{html.escape(EUR_LEX_LABEL)}</a></p>
    </footer>
  </div>
</body>
</html>
"""


def article_html(post: dict[str, str]) -> str:
    body = "\n".join(f"          {line}" for line in post["body_html"].split("\n"))
    source = ""
    if post["source"].strip():
        source = (
            '\n        <p class="source">Source: '
            + html.escape(post["source"])
            + "</p>"
        )
    return f"""      <article>
        <p class="kicker"><time datetime="{html.escape(post["date"])}">{html.escape(post["display_date"])}</time> <span class="pill">{html.escape(post["lens"])}</span></p>
        <h1>{html.escape(post["headline"])}</h1>
        <div class="body">
{body}
        </div>{source}
      </article>"""


def list_item_html(post: dict[str, str], from_page: str) -> str:
    href = html.escape(rel_link(from_page, post["path"]), quote=True)
    return f"""          <li>
            <a href="{href}">
              <span class="item-meta"><time datetime="{html.escape(post["date"])}">{html.escape(post["display_date"])}</time> <span class="pill">{html.escape(post["lens"])}</span></span>
              <span class="item-title">{html.escape(post["headline"])}</span>
            </a>
          </li>"""


def index_main(posts: list[dict[str, str]]) -> str:
    latest = posts[0]
    earlier = posts[1:6]
    blocks = [article_html(latest)]
    archive = html.escape(rel_link("index.html", "archive/"), quote=True)
    if earlier:
        items = "\n".join(list_item_html(post, "index.html") for post in earlier)
        earlier_html = f"""        <h2 id="earlier-heading">Earlier takeaways</h2>
        <ul class="takeaways">
{items}
        </ul>
"""
        labelled = ' aria-labelledby="earlier-heading"'
    else:
        earlier_html = ""
        labelled = ""
    blocks.append(
        f"""      <section class="earlier"{labelled}>
{earlier_html}        <p class="more"><a href="{archive}">Archive</a></p>
      </section>"""
    )
    return "\n".join(blocks)


def archive_main(posts: list[dict[str, str]]) -> str:
    items = "\n".join(list_item_html(post, "archive/index.html") for post in posts)
    return f"""      <h1>Archive</h1>
      <ul class="takeaways">
{items}
      </ul>"""


def post_main(post: dict[str, str], posts: list[dict[str, str]]) -> str:
    index = next(i for i, item in enumerate(posts) if item["date"] == post["date"])
    page = f"posts/{post['date']}/index.html"
    older = posts[index + 1] if index + 1 < len(posts) else None
    newer = posts[index - 1] if index > 0 else None
    chunks = [article_html(post), '      <nav class="pager" aria-label="Takeaways">']
    if older:
        href = html.escape(rel_link(page, older["path"]), quote=True)
        chunks.append(
            f"""        <a class="pager-prev" href="{href}">
          <span class="pager-dir">Previous</span>
          <span class="pager-title">{html.escape(older["headline"])}</span>
        </a>"""
        )
    home = html.escape(rel_link(page, "index.html"), quote=True)
    chunks.append(f'        <a class="pager-home" href="{home}">Home</a>')
    if newer:
        href = html.escape(rel_link(page, newer["path"]), quote=True)
        chunks.append(
            f"""        <a class="pager-next" href="{href}">
          <span class="pager-dir">Next</span>
          <span class="pager-title">{html.escape(newer["headline"])}</span>
        </a>"""
        )
    chunks.append("      </nav>")
    return "\n".join(chunks)


def not_found_main() -> str:
    return """      <h1>Page not found</h1>
      <p class="more"><a href="index.html">Home</a></p>"""


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text if text.endswith("\n") else text + "\n", encoding="utf-8")


def write_posts_json(posts: list[dict[str, str]]) -> None:
    payload = [
        {
            "date": post["date"],
            "lens": post["lens"],
            "headline": post["headline"],
            "source": post["source"],
            "path": post["path"],
            "body": post["body"],
        }
        for post in posts
    ]
    write_text(
        POSTS_DIR / "posts.json",
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
    )


def self_check() -> None:
    assert rel_link("index.html", "archive/") == "archive/"
    assert rel_link("index.html", "posts/2026-09-25/") == "posts/2026-09-25/"
    assert rel_link("index.html", "styles.css") == "styles.css"
    assert rel_link("archive/index.html", "index.html") == "../index.html"
    assert rel_link("archive/index.html", "posts/2026-09-25/") == "../posts/2026-09-25/"
    assert rel_link("posts/2026-09-25/index.html", "index.html") == "../../index.html"
    assert rel_link("posts/2026-09-25/index.html", "archive/") == "../../archive/"
    assert rel_link("posts/2026-09-25/index.html", "posts/2026-09-24/") == "../2026-09-24/"
    assert rel_link("posts/2026-09-25/index.html", "favicon.svg") == "../../favicon.svg"
    assert markdown_to_html("Hello") == "<p>Hello</p>"
    assert markdown_to_html("A\n\nB") == "<p>A</p>\n<p>B</p>"
    assert markdown_to_html("one\ntwo") == "<p>one two</p>"
    assert (
        markdown_to_html("Say **bold** and *italic* and _also_.")
        == "<p>Say <strong>bold</strong> and <em>italic</em> and <em>also</em>.</p>"
    )
    assert (
        markdown_to_html("See [the Act](https://example.com/a).")
        == '<p>See <a href="https://example.com/a">the Act</a>.</p>'
    )
    assert markdown_to_html("T&Cs <ok>") == "<p>T&amp;Cs &lt;ok&gt;</p>"
    shown = date(2026, 9, 25)
    assert f"{shown.strftime('%A')} {shown.day} {shown.strftime('%B %Y')}" == (
        "Friday 25 September 2026"
    )


def main() -> None:
    self_check()
    posts = load_posts()
    write_text(
        ROOT / "index.html",
        page_html(page="index.html", title=SITE_TITLE, main=index_main(posts)),
    )
    write_text(
        ROOT / "archive" / "index.html",
        page_html(
            page="archive/index.html",
            title=f"Archive — {SITE_TITLE}",
            main=archive_main(posts),
        ),
    )
    for post in posts:
        write_text(
            POSTS_DIR / post["date"] / "index.html",
            page_html(
                page=f"posts/{post['date']}/index.html",
                title=f"{post['headline']} — {SITE_TITLE}",
                main=post_main(post, posts),
            ),
        )
    write_text(
        ROOT / "404.html",
        page_html(
            page="404.html",
            title=f"Page not found — {SITE_TITLE}",
            main=not_found_main(),
        ),
    )
    write_posts_json(posts)
    print(f"built {len(posts)} takeaways")


if __name__ == "__main__":
    main()
