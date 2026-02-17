"""Grid Card macro definitions."""

from __future__ import annotations

from pathlib import Path, PurePath
from typing import TYPE_CHECKING, Callable

import yaml

from macros.util import normalize_page_link

from .card import CardNamespace
from .render import CardRenderer

if TYPE_CHECKING:
    from mkdocs.structure.pages import Page
    from mkdocs_macros.plugin import MacrosPlugin


def define_env(env: MacrosPlugin) -> None:
    """Define grid card macros for use in docs."""

    def render_j2() -> Callable[[str], str]:
        def fn(raw_md: str) -> str:
            template = env.env.from_string(raw_md)
            return template.render(env.variables)

        return fn

    def get_page() -> Callable[[], Page]:
        def fn() -> Page:
            return env.page

        return fn

    renderer = CardRenderer(
        render_j2(),
        get_page(),
    )

    cards_path = PurePath("res/grid_cards.yml")
    with Path(cards_path).open("r", encoding="utf-8") as f:
        content = yaml.safe_load(f)
    cards = CardNamespace.from_yaml("cards", content)

    env.variables["cards"] = cards
    env.variables["renderer"] = renderer

    @env.filter
    def normalize_link(link_target: str) -> str:
        return normalize_page_link(
            page_url=PurePath(env.page.url),
            link_target=link_target,
            page_is_index=env.page.is_index,
        )
