"""Base definitions for Grid Card objects."""

from __future__ import annotations

import abc
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Self

if TYPE_CHECKING:
    from macros.card import CardNamespace


@dataclass
class CardElement:
    """Base CardElement."""

    name: str
    parent: CardNamespace | None = field(default=None, init=False)

    def __post_init__(self) -> None:
        """Validate card element name."""
        if not self.name.isidentifier():
            msg = "CardElement name must be a valid identifier."
            raise ValueError(msg)

    def get_path(self) -> str:
        """Get path of this namespace down to root."""
        parts: list[str] = []
        element = self

        while element.parent:
            parts.append(element.name)
            element = element.parent

        return ".".join(reversed(parts))

    @classmethod
    @abc.abstractmethod
    def from_yaml(cls, name: str, content: dict) -> Self:
        """Build from YAML."""
