# LYMDLUT.github.io

Personal homepage for 刘祎铭 / Yiming Liu. Static HTML, no runtime dependencies.

## Editing

All content lives in [`data/site.yml`](data/site.yml) — profile, timeline chapters,
publications, open-source entries. Prose fields are authored as HTML, so inline
`<a>`, `<strong>`, and `<code>` are allowed.

Any `{en: ..., zh: ...}` map is collapsed by `build.py` to the language it is rendering,
which keeps both languages next to each other instead of in two drifting files. Keep each
Chinese paragraph on a single line: a newline inside CJK text renders as a stray space.

After editing, regenerate both pages:

```sh
python3 build.py        # needs PyYAML + Jinja2 → index.html and zh/index.html
python3 -m http.server  # preview at http://localhost:8000
```

The generated pages are committed so GitHub Pages can serve them directly;
`.nojekyll` keeps Pages from trying to build the repo itself.

## Adding a paper

Append an entry to `publications:` in `data/site.yml`:

```yaml
  - title: "Paper Title"
    authors: [First Author, Yiming Liu, Last Author]   # your name gets bolded
    venue: ICLR                                        # or "arXiv preprint"
    year: 2026
    note: Poster                                       # optional badge
    topic: Evaluation &amp; Benchmarks
    links: { OpenReview: "...", PDF: "...", Code: "..." }
    bib: |
      @inproceedings{...}
```

Suffix a name with `*` for equal contribution.

## Publishing

```sh
git remote add origin git@github.com:LYMDLUT/LYMDLUT.github.io.git
git push -u origin main
```

GitHub Pages serves a repo named `<user>.github.io` from its default branch at
`https://LYMDLUT.github.io` — enable it under *Settings → Pages → Deploy from a branch*.

## Résumé

The LaTeX source of both résumés lives in [`resume/`](resume/), fonts included, so they
build anywhere with XeLaTeX. The English page links to the English PDF and the Chinese page
to the Chinese one. After editing, rebuild and copy them into `assets/cv/`:

```sh
cd resume && make publish
```
