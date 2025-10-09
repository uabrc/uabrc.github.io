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

    def page_url_getter(env: MacrosPlugin) -> Callable[[], str]:
        def fn() -> str:
            return env.page.url

        return fn

    renderer = CardRenderer(page_url_getter(env))  # replace with macros fix_url()

    cards_path = PurePath("res/grid_cards.yml")
    with Path(cards_path).open("r") as f:
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
        page_url = PurePath(env.page.url).parent
        docs_dir = PurePath(env.conf["docs_dir"])
        return docs_dir / os.path.normpath(page_url / link_url)
