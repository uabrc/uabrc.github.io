"""Model rendering."""

from __future__ import annotations

import os
import textwrap
from pathlib import PurePath
from typing import Callable

from macros.card import Card, CardNamespace, EmojiSizesCss, EmojiVerticalAlignmentCss


class CardRenderer:
    """Handles rendering of cards."""

    def __init__(
        self,
        j2_renderer: Callable[[str], str],
        get_page_url_fn: Callable[[], str],
        *,
        indent: int = 4,
    ) -> None:
        """Initialize new object."""
        self._j2_renderer: Callable[[str], str] = j2_renderer
        self._get_page_url: Callable[[], str] = get_page_url_fn
        self._indent: int = indent

    def render_cards(self, *cards: Card) -> str:
        """Render input to markdown string.

        Intended for use with mkdocs-material grid cards.
        """
        parts = [self._div_open]
        extractors = [
            _CardExtractor(self._get_page_url(), card, self._indent) for card in cards
        ]
        card_parts = [ex.extract() for ex in extractors]
        card_parts = [part for cards in card_parts for part in cards]
        parts.extend(card_parts)
        parts.append(self._div_close)

        template_raw = "\n\n" + "\n\n".join(parts) + "\n\n"
        return self._j2_renderer(template_raw)

    def render_namespace(
        self,
        namespace: CardNamespace,
        *,
        recursive: bool = False,
    ) -> str:
        """Render input namespaceto markdown string.

        Intended for use with mkdocs-material grid cards.
        """
        cards = namespace.get_children(recursive=recursive, cards_only=True)
        return self.render_cards(*cards)

    _div_open = r'<div class="grid cards" markdown>'
    _div_close = r"</div>"


class _CardExtractor:
    def __init__(self, page_url: str, card: Card, indent: int) -> None:
        self._page_url: str = page_url
        self._card: Card = card
        self._indent: int = indent

    def extract(self) -> list[str]:
        indented_block = []
        content = self._content_part()
        if content:
            indented_block.append(content)
        link = self._link_part()
        if link:
            indented_block.append(link)
        if indented_block:
            indented_block.insert(0, self._hr)

        parts = [self._title_part()]
        parts.extend([self._clean_and_indent(part) for part in indented_block])
        return parts

    #### DEFAULTS
    _DEFAULT_ICON_COLOR = ".icon-color-uab-green"
    _DEFAULT_ICON_SIZE = EmojiSizesCss.large
    _DEFAULT_ICON_VERTICAL_ALIGNMENT = EmojiVerticalAlignmentCss.middle
    _DEFAULT_LINK_TEXT = "Read more"
    _DEFAULT_LINK_ICON_NAME = ":octicons-arrow-right-24:"

    #### DEFINITIONS
    _ul = "-"
    _hr = "---"

    #### TITLE PART
    def _title_part(self) -> str:
        parts = [self._ul]
        icon = self._icon()
        if icon:
            parts.append(icon)
        parts.append(self._title())
        return " ".join(parts)

    ## TITLE
    def _title(self) -> str:
        text = self._title_text()
        url = self._title_url()
        return self._to_md_internal_link(text, url) if url else text

    def _title_text(self) -> str:
        return f"**{self._card.title_text}**"

    def _title_url(self) -> str | None:
        url = self._card.title_url
        return self._to_url_relative_to_page(url) if url else None

    ## ICON
    def _icon(self) -> str | None:
        name = self._icon_name()
        css = self._icon_css()
        if name and css:
            return name + css
        if name:
            return name
        return None

    def _icon_name(self) -> str | None:
        return self._card.icon_name

    def _icon_css(self) -> str | None:
        css_classes = [
            self._icon_size(),
            self._icon_vertical_alignment(),
            self._icon_color(),
        ]
        return "{ " + " ".join(css_classes) + " }" if css_classes else None

    def _icon_size(self) -> str:
        size = self._card.icon_size
        return size.value if size else EmojiSizesCss.default().value

    def _icon_vertical_alignment(self) -> str:
        va = self._card.icon_vertical_alignment
        return va.value if va else EmojiVerticalAlignmentCss.default().value

    def _icon_color(self) -> str:
        color = self._card.icon_color
        return color if color else self._DEFAULT_ICON_COLOR

    #### CONTENT PART
    def _content_part(self) -> str | None:
        return self._card.content

    #### LINK PART
    def _link_part(self) -> str | None:
        text = f"{self._link_text()} {self._link_icon()}"
        url = self._link_url()
        return self._to_md_internal_link(text, url) if url else None

    def _link_text(self) -> str:
        text = self._card.link_text
        return text if text else self._DEFAULT_LINK_TEXT

    def _link_icon(self) -> str:
        name = self._card.link_icon_name
        return name if name else self._DEFAULT_LINK_ICON_NAME

    def _link_url(self) -> str | None:
        url = self._card.link_url
        return self._to_url_relative_to_page(url) if url else None

    #### HELPERS
    def _clean_and_indent(self, s: str) -> str:
        out = s
        out = textwrap.dedent(out)
        out = out.strip()
        return textwrap.indent(out, " " * self._indent)

    def _to_url_relative_to_page(self, start_url: str) -> str:
        root = PurePath("/root/")

        link = root / start_url
        page = root / self._page_url

        return PurePath(os.path.relpath(link, page)).as_posix()

    def _to_md_internal_link(self, text: str, url: str) -> str:
        return f"[{text}]({url})"
