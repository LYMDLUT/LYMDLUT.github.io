# LYMDLUT.github.io

Personal homepage for 刘祎铭 / Yiming Liu. Static HTML, no runtime dependencies.

## Editing

All content lives in [`data/site.yml`](data/site.yml) — profile, timeline chapters,
publications, open-source entries. Prose fields are authored as HTML, so inline
`<a>`, `<strong>`, and `<code>` are allowed.

After editing, regenerate `index.html`:

```sh
python3 build.py        # needs PyYAML + Jinja2
python3 -m http.server  # preview at http://localhost:8000
```

The generated `index.html` is committed so GitHub Pages can serve it directly;
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

The LaTeX source of the Chinese résumé lives in [`resume/`](resume/), fonts included, so it
builds anywhere with XeLaTeX. After editing it, rebuild and refresh the copy the `CV` nav
link points at:

```sh
cd resume && make zh_CN && cp resume-zh_CN.pdf ../assets/cv/Yiming_Liu_CV.pdf
```

## Notes

- `assets/cv/Yiming_Liu_CV.pdf` is the Chinese résumé; add an English CV if you want the
  `CV` nav link to be readable to international visitors.
