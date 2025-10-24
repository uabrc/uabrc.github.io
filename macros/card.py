"""Grid Card definitions.

Derives from CardElement for shared elements.

Leaves of a tree structure.
"""

from __future__ import annotations

import enum
from dataclasses import dataclass, field
from types import SimpleNamespace
from typing import Literal, Self, overload

from macros.base import CardElement


class EmojiSizesCss(enum.Enum):
    """CSS Emoji Sizes."""

    standard = ""
    large = ".lg"
    xlarge = ".xlg"
    xxlarge = ".xxlg"
    xxxlarge = ".xxxlg"

    @classmethod
    def default(cls) -> EmojiSizesCss:
        """Return default."""
        return cls.large


class EmojiVerticalAlignmentCss(enum.Enum):
    """CSS Emoji Vertical Alignments."""

    standard = ""
    middle = ".middle"

    @classmethod
    def default(cls) -> EmojiVerticalAlignmentCss:
        """Return default."""
        return cls.middle


@dataclass
class Card(CardElement):
    """Representation of a grid card."""

    title_text: str
    title_url: str | None = None

    icon_name: str | None = None
    icon_color: str | None = None
    icon_size: EmojiSizesCss | None = None
    icon_vertical_alignment: EmojiVerticalAlignmentCss | None = None
    content: str | None = None

    link_url: str | None = None
    link_text: str | None = None
    link_icon_name: str | None = None

    def __post_init__(self) -> None:
        """Validate title text."""
        super().__post_init__()
        if not self.title_text:
            msg = "Card must have non-empty title."
            raise ValueError(msg)

    @classmethod
    def from_yaml(cls, name: str, content: dict) -> Self:
        """Build card from YAML representation."""
        return cls(
            name=name,
            title_text=content["title_text"],
            title_url=content.get("title_url"),
            icon_name=content.get("icon_name"),
            icon_color=content.get("icon_color"),
            icon_size=content.get("icon_size"),
            icon_vertical_alignment=content.get("icon_vertical_alignment"),
            content=content.get("content"),
            link_url=content.get("link_url"),
            link_text=content.get("link_text"),
            link_icon_name=content.get("link_icon_name"),
        )


@dataclass
class CardNamespace(CardElement, SimpleNamespace):
    """Namespace of grid card collection."""

    def __setattr__(self, name: str, value: CardNamespace | Card) -> None:
        """Override setattr() and dot operator."""
        if name.startswith("_") or name in ("name", "parent"):
            object.__setattr__(self, name, value)
            return
        if isinstance(value, (Card, CardNamespace)):
            if hasattr(self, name):
                path = self.get_path()
                path = f"{path}.{name}" if path else name
                msg = f"duplicate namespace or card found: {path}"
                raise KeyError(msg)
            value.parent = self
            self._children.append(value)
            object.__setattr__(self, name, value)
            return
        msg = "CardNamespace may only hold CardNamespace or Card."
        raise TypeError(msg)

    @overload
    def get_children(
        self,
        *,
        recursive: bool = ...,
        cards_only: Literal[False],
    ) -> list[Card | CardNamespace]: ...

    @overload
    def get_children(
        self,
        *,
        recursive: bool = ...,
        cards_only: Literal[True] = True,
    ) -> list[Card]: ...

    def get_children(
        self,
        *,
        recursive: bool = False,
        cards_only: bool = True,
    ) -> list[Card | CardNamespace] | list[Card]:
        """Get all cards that are children of this card.

        If recursive is True, children of children, etc., are also returned,
        depth first.
        """
        children: list[Card | CardNamespace] = []
        for child in self._children:
            if not cards_only or isinstance(child, Card):
                children.append(child)
            if isinstance(child, CardNamespace) and recursive:
                children.extend(
                    child.get_children(recursive=recursive, cards_only=cards_only),
                )
        return children

    def to_dict(
        self,
        *,
        cards_only: bool = True,
    ) -> dict[str, Card | CardNamespace] | dict[str, Card]:
        """Children as dict of (path, Card).

        If cards_only is False, also returns CardNamespaces.
        """
        return {
            c.get_path(): c
            for c in self.get_children(recursive=True, cards_only=cards_only)
        }

    @classmethod
    def from_yaml(cls, name: str, content: dict) -> Self:
        """Build from YAML."""
        namespace = cls(name)
        for child_name, child_content in content.items():
            child_type = Card if "title_text" in child_content else cls
            child = child_type.from_yaml(child_name, child_content)
            setattr(namespace, child_name, child)
        return namespace

    _children: list[CardNamespace | Card] = field(default_factory=list)
