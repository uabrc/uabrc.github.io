"""Grid Card macro definitions."""

import os
from pathlib import Path, PurePath
from typing import Callable

import yaml
from mkdocs_macros.plugin import MacrosPlugin

from .card import CardNamespace
from .render import CardRenderer


def define_env(env: MacrosPlugin) -> None:
    """Define grid card macros for use in docs."""

    def j2_renderer() -> Callable[[str], str]:
        def fn(_raw: str) -> str:
            template = env.env.from_string(_raw)
            return template.render(env.variables)

        return fn

    def page_url_getter() -> Callable[[], str]:
        def fn() -> str:
            return _get_page_url().as_posix()

        return fn

    renderer = CardRenderer(
        j2_renderer(),
        page_url_getter(),
    )

    cards_path = PurePath("res/grid_cards.yml")
    with Path(cards_path).open("r", encoding="utf-8") as f:
        content = yaml.safe_load(f)
    cards = CardNamespace.from_yaml("cards", content)

    env.variables["cards"] = cards
    env.variables["renderer"] = renderer
    env.macro(list, "__dummy")

    @env.macro
    def include(rel_url: str, *, indent: int = 0) -> str:
        mkdocs_url = to_docs_abs_url(rel_url)
        with Path(mkdocs_url).open("r") as f:
            lines = f.readlines()

        if not lines:
            return ""

        first = lines[0]
        lines = [" " * indent + line for line in lines[1:]]
        lines.insert(0, first)
        return "".join(lines)

    def to_docs_abs_url(rel_url: str) -> PurePath:
        link_url = PurePath(rel_url)
        page_url = _get_page_url()
        docs_dir = PurePath(env.conf["docs_dir"])
        return docs_dir / os.path.normpath(page_url / link_url)

    @env.filter
    def to_page_rel_url(docs_dir_url: str) -> str:
        docs_dir = PurePath(env.conf["docs_dir"])
        target_url = docs_dir / docs_dir_url
        page_url = docs_dir / _get_page_url()
        out = PurePath(os.path.relpath(target_url, page_url))
        return out.as_posix()

    def _get_page_url() -> PurePath:
        page = env.page
        url = PurePath(page.url)
        return url if page.is_index else url.parent
