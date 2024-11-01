import os
from pathlib import Path, PurePath
from typing import Literal

import pypandoc
from mkdocs.plugins import get_plugin_logger

log = get_plugin_logger(__name__)


class Doc:
    def __init__(self, _path: PurePath) -> None:
        self._input_path: PurePath = _path
        self._output_path: PurePath = _path

    def set_output_path(self, _path: PurePath) -> None:
        self._output_path: PurePath = _path

    def to_docx(self) -> None:
        self._convert("docx")

    def to_plaintext(self) -> None:
        self._convert("plain")

    def clean(self) -> None:
        """
        Deletes the same path with other suffixes from the filesystem.
        """
        suffix = self._output_path.suffix
        parent = self._output_path.parent
        stem = self._output_path.stem

        files = [f for f in Path(parent).glob(f"{stem}.*") if f.suffix != suffix]

        for f in files:
            # log.info(f"Deleting {f}")
            os.remove(f)

    _FORMAT_SUFFIX_MAP = {
        "docx": ".docx",
        "plain": ".txt",
    }

    def _convert(self, _format: Literal["docx", "plain"]) -> None:
        suffix = self._FORMAT_SUFFIX_MAP[_format]
        pypandoc.convert_file(
            str(self._input_path),
            to=_format,
            outputfile=str(self._output_path.with_suffix(suffix)),
        )


def on_pre_build(config) -> None:
    DOCS = PurePath("docs")

    GRANTS_RES = PurePath("grants") / "res"
    UAB_RC_FACILITIES_MD = "uab-rc-facilities.md"

    subfolder = GRANTS_RES
    doc_file = UAB_RC_FACILITIES_MD
    location = subfolder / doc_file

    doc = Doc(DOCS / location)
    doc.to_plaintext()
    doc.to_docx()


def on_post_build(config) -> None:
    DOCS = PurePath("docs")

    GRANTS_RES = PurePath("grants") / "res"
    UAB_RC_FACILITIES_MD = "uab-rc-facilities.md"

    subfolder = GRANTS_RES
    doc_file = UAB_RC_FACILITIES_MD
    location = subfolder / doc_file

    doc = Doc(DOCS / location)
    doc.clean()
