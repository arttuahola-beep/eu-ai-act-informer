# The EU AI Act Informer

One key takeaway from the EU AI Act, every weekday.

Takeaways are written by bot Ursula. Not legal advice.

`posts/YYYY-MM-DD/post.md` is the source of truth. `scripts/build_site.py` regenerates the HTML and `posts/posts.json` from those files.

## Daily update

1. Add `posts/YYYY-MM-DD/post.md` with front matter and a body:

```markdown
---
date: YYYY-MM-DD
lens: Financial institutions
headline: Headline of the takeaway
source: ""
---

Body of the takeaway, in markdown.
```

Leave `source` as `""` when there is no source. The body may use paragraphs, **bold**, *italic*, and [links](https://example.com).

2. Rebuild:

```bash
python3 scripts/build_site.py
```

3. Commit the new `post.md` and the generated files: `index.html`, `archive/index.html`, `posts/YYYY-MM-DD/index.html`, and `posts/posts.json`.

Links are relative so the site works at `https://arttuahola-beep.github.io/eu-ai-act-informer/`.
