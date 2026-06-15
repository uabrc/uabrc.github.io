"""Runs linkchecker on docs and produces human-readable output.

Install with `pip install -r requirements-dev.txt`.

Use with `python ./verification_scripts/linkchecker.py`.
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path, PurePath

import pandas as pd
import yaml
from attrs import define

# COLUMNS
## ORIGINAL
RESULT = "result"
URLNAME = "urlname"
URL = "url"
PARENTNAME = "parentname"
LINE = "line"
COLUMN = "column"
## RENAMED
URL_IN_MARKDOWN = "document-url"
URL_AFTER_REDIRECTION = "url-after-redirection"
MARKDOWN_FILE = "document"


# READ
def _run_linkchecker(path: PurePath) -> None:
    """Run the linkchecker application."""
    with Path(path).open("wb", buffering=0) as f:
        subprocess.run(  # noqa: S603
            [_get_linkchecker_path(), "--config", ".linkcheckerrc", "docs"],
            stdout=f,
            check=False,
        )


def _get_linkchecker_path() -> PurePath:
    return PurePath(sys.executable).parent / "Scripts" / "linkchecker"


# PROCESS
def _load_results(path: PurePath) -> pd.DataFrame:
    """Load the raw linkchecker output dataframe."""
    raw_linkchecker_data = pd.read_csv(path)
    raw_linkchecker_data = raw_linkchecker_data[
        [RESULT, URLNAME, URL, PARENTNAME, LINE, COLUMN]
    ]
    return raw_linkchecker_data.rename(
        columns={
            URLNAME: URL_IN_MARKDOWN,
            URL: URL_AFTER_REDIRECTION,
            PARENTNAME: MARKDOWN_FILE,
        },
    )


def _drop_ok_with_no_redirects(_df: pd.DataFrame) -> pd.DataFrame:
    """Drop rows with OK code (200) if there is no redirection."""
    same_url = _df[URL_IN_MARKDOWN] == _df[URL_AFTER_REDIRECTION]
    result_ok = _df[RESULT].str.startswith("200")
    drop = same_url & result_ok
    return _df[~drop]


@define
class Drop:
    """Information about rows to drop from linkchecker output."""

    url: str
    code: str


@define
class Replace:
    """Information about rows to replace in linkchecker output."""

    find: str
    replace: str
    where: str


@define
class Cases:
    """All special case information."""

    drops: list[Drop]
    replacements: list[Replace]


def _read_special_cases() -> Cases:
    with Path(".linkcheckerrc-special.yaml").open("r") as f:
        data = yaml.safe_load(f)

    drops = [Drop(url, str(code)) for url, code in data["drop"].items()]
    replaces = [Replace(pattern, v[0], v[1]) for pattern, v in data["replace"].items()]
    return Cases(drops, replaces)


def _file_uris_to_paths(_s: pd.Series) -> pd.Series:
    """Modify file URIs to a normalized format.

    Example:
    file:///D|/repos/uabrc.github.io/dir/file.md -> dir/file.md

    """
    if _s.empty:
        return _s

    keep = _s.str.startswith("file:") & _s.str.contains("repos/uabrc.github.io")
    splits = _s.str.split("repos/uabrc.github.io", expand=True)

    fixes = splits.iloc[:, -1][keep]
    fixes = fixes.apply(PurePath)  # type: ignore[reportCallIssue,reportArgumentType]
    fixes = fixes.astype(str)
    fixes = fixes.str.lstrip(os.sep)

    out = _s.copy()
    out[keep] = fixes
    return out


def _find_rows_containing(_s: pd.Series, _containing: str) -> pd.Series:
    """Find rows containing the supplied string in the supplied series."""
    return _s.str.contains(_containing)


def _replace_rows(
    _s: pd.Series,
    _containing: str,
    _with: str,
    /,
    find_in: pd.Series | None = None,
) -> pd.Series:
    """Replace entries in series.

    If _containing is found in an entry, then the entry is replaced with _with.
    Optionally, look for matches in "find_in" and replace in _s.
    """
    if find_in is None:
        find_in = _s

    contains = _find_rows_containing(find_in, _containing)
    out = _s.copy()
    out[contains] = _with
    return out


def _drop_rows(
    _df: pd.DataFrame,
    _in: str,
    _containing: str,
    /,
    if_result_code: str | None = None,
) -> pd.DataFrame:
    """Drop rows containing supplied string if found in _in column.

    Allows optional refinement conditional on result code.
    """
    find_in = _df[_in]
    contains = _find_rows_containing(find_in, _containing)

    if if_result_code is not None:
        contains &= _df[RESULT].str.contains(if_result_code)

    return _df[~contains]


def _handle_special_cases(results: pd.DataFrame) -> pd.DataFrame:
    cases = _read_special_cases()
    for replace in cases.replacements:
        results[RESULT] = _replace_rows(
            results[RESULT],
            replace.find,
            replace.replace,
            find_in=results[replace.where],
        )

    for drop in cases.drops:
        results = _drop_rows(results, URL_IN_MARKDOWN, drop.url, drop.code)

    return results


# WRITE
def _to_csv(results: pd.DataFrame, path: PurePath) -> None:
    results.to_csv(path, index=False)


def _to_yaml(results: pd.DataFrame, path: PurePath) -> None:
    records = results.to_dict(orient="records") if not results.empty else ""
    with Path(path).open("w") as f:
        yaml.safe_dump(records, f, sort_keys=False)


# ENTRY POINT
def main() -> None:
    """Primary entrypoint."""
    # config
    output_path = PurePath("out")
    Path(output_path).mkdir(exist_ok=True)

    # generate input
    _run_linkchecker(output_path / "linkchecker.log")
    results = _load_results(output_path / "linkchecker-raw.csv")

    # process
    results = _drop_ok_with_no_redirects(results)
    results = _handle_special_cases(results)
    results[MARKDOWN_FILE] = _file_uris_to_paths(results[MARKDOWN_FILE])
    results = results.sort_values(by=[RESULT, MARKDOWN_FILE, LINE, COLUMN])

    # write output
    _to_csv(results, output_path / "linkchecker-out.csv")
    _to_yaml(results, output_path / "linkchecker-out.yml")


if __name__ == "__main__":
    main()
