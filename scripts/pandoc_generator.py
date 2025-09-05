"""Adds pandoc generator to transform markdown files to docx and plaintext."""

import logging
from pathlib import PurePath
from typing import ClassVar, Literal

import mkdocs_gen_files
import pypandoc

log = logging.getLogger(f"mkdocs.plugins.{__name__}")


class Doc:
    """Class storing doc path and knowing how to convert."""

    def __init__(self, _path: PurePath) -> None:
        """Initialize a new Doc object."""
        self._input_path: PurePath = _path
        self._output_path: PurePath = _path

    def set_output_path(self, _path: PurePath) -> None:
        """Set output path."""
        self._output_path: PurePath = _path

    def to_docx(self) -> None:
        """Convert doc to docx format."""
        self._convert("docx")

    def to_plaintext(self) -> None:
        """Convert doc to plaintext format."""
        self._convert("plain")

    _FORMAT_SUFFIX_MAP: ClassVar[dict[str, str]] = {
        "docx": ".docx",
        "plain": ".txt",
    }

    def _convert(self, _format: Literal["docx", "plain"]) -> None:
        suffix = self._FORMAT_SUFFIX_MAP[_format]

        # Touch the file so mkdocs_gen_files is aware of what we intend. This
        # must be done because pypandoc can only write docx directly to disk.
        mkdocs_url_output_path = self._output_path.with_suffix(suffix)
        with mkdocs_gen_files.open(mkdocs_url_output_path, "w") as f:
            f.write("")

        # Clobber the touched file with the actual content.
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
    """Generate docs based on list supplied below."""
    doc = Doc(PurePath("grants") / "res" / "uab-rc-facilities.md")
    doc.to_plaintext()
    doc.to_docx()


# Do the thing.
generate()
