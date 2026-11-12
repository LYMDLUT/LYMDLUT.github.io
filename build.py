#!/usr/bin/env python3
"""Render the English and Chinese homepages from data/site.yml."""

from __future__ import annotations

import datetime as dt
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader, StrictUndefined

ROOT = Path(__file__).parent
LANGUAGES = {"en": "", "zh": "zh/"}  # language code -> path prefix of its page


def load_site() -> dict:
    return yaml.safe_load((ROOT / "data" / "site.yml").read_text(encoding="utf-8"))


def localize(node, lang: str):
    """Collapse every {en: ..., zh: ...} map in the tree to one language."""
    if isinstance(node, dict):
        if node and node.keys() <= LANGUAGES.keys():
            return node.get(lang, node["en"])
        return {key: localize(value, lang) for key, value in node.items()}
    if isinstance(node, list):
        return [localize(item, lang) for item in node]
    return node


def navigation(ui: dict, profile: dict) -> list[dict]:
    cv = next(link["url"] for link in profile["links"] if link["kind"] == "cv")
    return [
        {"label": ui["nav_about"], "url": "#main"},
        {"label": ui["nav_timeline"], "url": "#timeline"},
        {"label": ui["nav_publications"], "url": "#publications"},
        {"label": ui["nav_cv"], "url": cv},
    ]


def is_site_relative(url: str) -> bool:
    return not url.startswith(("http://", "https://", "mailto:", "/", "#"))


def main() -> None:
    data = load_site()
    env = Environment(
        loader=FileSystemLoader(ROOT / "templates"),
        undefined=StrictUndefined,
        autoescape=False,  # content in site.yml is authored as HTML
        trim_blocks=True,
        lstrip_blocks=True,
    )
    template = env.get_template("index.html")
    today = dt.date.today()

    for lang, prefix in LANGUAGES.items():
        page = localize(data, lang)
        root = "../" * prefix.count("/")  # how to reach the site root from this page
        other = next(code for code in LANGUAGES if code != lang)
        portrait = page["profile"]["portrait"]
        for link in page["profile"]["links"]:
            if is_site_relative(link["url"]):
                link["url"] = root + link["url"]
        page["profile"]["portrait"] = root + portrait
        html = template.render(
            lang=lang,
            root=root,
            portrait_url=f"{data['site']['url']}/{portrait}",
            alternates={code: f"{data['site']['url']}/{path}" for code, path in LANGUAGES.items()},
            switch_url=f"{root}{LANGUAGES[other]}",
            canonical=f"{data['site']['url']}/{prefix}",
            site=page["site"],
            ui=page["ui"],
            profile=page["profile"],
            timeline=page["timeline"],
            publications=page["publications"] or [],
            open_source=page["open_source"],
            nav=navigation(page["ui"], page["profile"]),
            year=today.year,
            built=today.strftime("%b %Y") if lang == "en" else today.strftime("%Y 年 %-m 月"),
        )
        target = ROOT / prefix / "index.html"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(html, encoding="utf-8")
        print(f"wrote {target.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
