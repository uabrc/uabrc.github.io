import logging
from pathlib import Path, PurePath
from typing import Literal

import mkdocs_gen_files
import pypandoc

log = logging.getLogger(f"mkdocs.plugins.{__name__}")


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

    _FORMAT_SUFFIX_MAP = {
        "docx": ".docx",
        "plain": ".txt",
    }

    def _convert(self, _format: Literal["docx", "plain"]) -> None:
        suffix = self._FORMAT_SUFFIX_MAP[_format]

        # touch the file so mkdocs_gen_files is aware of what we intend
        # must do this because pypandoc can only write docx directly to disk
        mkdocs_url_output_path = self._output_path.with_suffix(suffix)
        with mkdocs_gen_files.open(mkdocs_url_output_path, "w") as f:
            f.write("")

        # clobber with the actual content
        pandoc_disk_output_path = (
            PurePath(mkdocs_gen_files.directory) / mkdocs_url_output_path
        )
        pypandoc.convert_file(
            str(PurePath("docs") / self._input_path),
            to=_format,
            extra_args=["--wrap=preserve"],
            outputfile=str(pandoc_disk_output_path),
        )


def generate() -> None:
    doc = Doc(PurePath("grants") / "res" / "uab-rc-facilities.md")
    doc.to_plaintext()
    doc.to_docx()


generate()
