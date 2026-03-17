"""Utilities for macros module."""

from __future__ import annotations

import os
import re
from pathlib import PurePath


def normalize_page_link(
    page_url: PurePath,
    link_target: str,
    *,
    page_is_index: bool,
) -> str:
    """Return normalized link in page.

    - [text](name@domain.com) -> name@domain.com
    - [text](https://domain.com) -> https://domain.com
    - [text](path/to/file.md) -> ../rel/to/page/file.md
    """
    # external
    if _is_email(link_target):
        return f"mailto:{link_target}"

    if _is_uri(link_target):
        return link_target

    # internal
    page_url = page_url if page_is_index else page_url.parent
    out = _to_rel_url(page_url, PurePath(link_target))

    return out.as_posix()


def _to_rel_url(
    source_sub_path: PurePath,
    target_sub_path: PurePath,
) -> PurePath:
    """Return relative url between source_sub_path and target_sub_path."""
    root = PurePath()
    target_abs_url = root / target_sub_path
    source_abs_url = root / source_sub_path
    return PurePath(os.path.relpath(target_abs_url, source_abs_url))


_J2_DELIMITERS = (
    ("{{", "}}"),
    ("{%", "%}"),
    ("{#", "#}"),
)


def _is_template(link_target: str) -> bool:
    """Return true if Jinja template.

    - {{ ... }}
    - {% ... %}
    - {# ... #}
    """
    return any(
        link_target.startswith(start) and link_target.endswith(end)
        for start, end in _J2_DELIMITERS
    )


def _is_email(link_target: str) -> bool:
    return "@" in link_target


def _is_uri(link_target: str) -> bool:
    return bool(re.fullmatch(r"^.*://.*$", link_target))


if __name__ == "__main__":
    cases = (
        ("a@b.c", "a@b.c"),
        ("s://a.b/", "s://a.b/"),
        ("a.md", "a.md"),
        ("index.md", "index.md"),
        ("a/b.md", "a/b.md"),
        ("a/index.md", "a/index.md"),
        ("../index.md", "../index.md"),
        ("../a.md", "../a.md"),
    )
    expected = (
        "name@domain.com",
        "",
    )
