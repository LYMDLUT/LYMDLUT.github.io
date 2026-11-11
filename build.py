#!/usr/bin/env python3
"""Render index.html from data/site.yml."""

from __future__ import annotations

import datetime as dt
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader, StrictUndefined

ROOT = Path(__file__).parent
NAV = [
    {"label": "About", "url": "#main"},
    {"label": "Timeline", "url": "#timeline"},
    {"label": "Publications", "url": "#publications"},
    {"label": "CV", "url": "assets/cv/Yiming_Liu_CV.pdf"},
]


def load_site() -> dict:
    return yaml.safe_load((ROOT / "data" / "site.yml").read_text(encoding="utf-8"))


def main() -> None:
    data = load_site()
    env = Environment(
        loader=FileSystemLoader(ROOT / "templates"),
        undefined=StrictUndefined,
        autoescape=False,  # content in site.yml is authored as HTML
        trim_blocks=True,
        lstrip_blocks=True,
    )
    today = dt.date.today()
    html = env.get_template("index.html").render(
        site=data["site"],
        profile=data["profile"],
        timeline=data["timeline"],
        publications=data["publications"] or [],
        open_source=data["open_source"],
        nav=NAV,
        year=today.year,
        built=today.strftime("%b %Y"),
    )
    (ROOT / "index.html").write_text(html, encoding="utf-8")
    print("wrote index.html")


if __name__ == "__main__":
    main()
