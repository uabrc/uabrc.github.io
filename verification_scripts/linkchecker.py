"""Runs linkchecker on docs and produces human-readable output."""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path, PurePath

import pandas as pd
import yaml

"""
How to use:

python ./scripts/linkchecker.py
"""

# Cleans up output of linkchecker

OUTPUT = PurePath("out")
Path(OUTPUT).mkdir(exist_ok=True)

# FILE PATHS
LINKCHECKER_LOG = OUTPUT / "linkchecker.log"
LINKCHECKER_RAW_CSV = OUTPUT / "linkchecker-raw.csv"
LINKCHECKER_OUT_CSV = OUTPUT / "linkchecker-out.csv"
LINKCHECKER_OUT_YAML = OUTPUT / "linkchecker-out.yml"

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


def run_linkchecker() -> None:
    """Run the linkchecker application."""
    with Path(LINKCHECKER_LOG).open("wb", buffering=0) as f:
        subprocess.run(  # noqa: S603
            [_get_linkchecker_path(), "--config", ".linkcheckerrc", "docs"],
            stdout=f,
            check=False,
        )


def load_output() -> pd.DataFrame:
    """Load the raw linkchecker output dataframe."""
    raw_linkchecker_data = pd.read_csv(LINKCHECKER_RAW_CSV)
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


def replace_rows(
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


def drop_ok_with_no_redirects(_df: pd.DataFrame) -> pd.DataFrame:
    """Drop rows with OK code (200) if there is no redirection."""
    same_url = _df[URL_IN_MARKDOWN] == _df[URL_AFTER_REDIRECTION]
    result_ok = _df[RESULT].str.startswith("200")
    drop = same_url & result_ok
    return _df[~drop]


def drop_rows(
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


def modify_file_uris(_s: pd.Series) -> pd.Series:
    """Modify file URIs to a normalized format.

    Example:
    file:///D|/repos/uabrc.github.io/dir/file.md -> dir/file.md

    """
    keep = _s.str.startswith("file:") & _s.str.contains("repos/uabrc.github.io")
    splits = _s.str.split("repos/uabrc.github.io", expand=True)

    fixes = splits.iloc[:, -1][keep]
    fixes = fixes.apply(lambda x: PurePath(x))  # pyright: ignore[reportCallIssue,reportArgumentType]
    fixes = fixes.astype(str)
    fixes = fixes.str.lstrip(os.sep)

    out = _s.copy()
    out[keep] = fixes
    return out


def _find_rows_containing(_s: pd.Series, _containing: str) -> pd.Series:
    """Find rows containing the supplied string in the supplied series."""
    return _s.str.contains(_containing)


def _get_linkchecker_path() -> PurePath:
    return PurePath(sys.executable).parent / "Scripts" / "linkchecker"


if __name__ == "__main__":
    run_linkchecker()
    results = load_output()

    ### drop good urls
    results = drop_ok_with_no_redirects(results)

    ### replace unhelpful error messages
    # change 200 OK to 300 Redirect for human clarity
    results[RESULT] = replace_rows(results[RESULT], "200 OK", "300 Redirect")
    # replace long error messages with short codes
    results[RESULT] = replace_rows(results[RESULT], "ConnectTimeout", "408 Timeout")
    # special code for SSO urls
    results[RESULT] = replace_rows(
        results[RESULT],
        "https://padlock.idm.uab.edu",
        "423 Locked",
        find_in=results[URL_AFTER_REDIRECTION],
    )

    ### special url ignore rules
    # doi.org always redirects, that's its purpose, so we ignore
    results = drop_rows(
        results,
        URL_IN_MARKDOWN,
        "https://doi.org",
        if_result_code="300",
    )
    # if anaconda.org goes down we'll surely hear about it
    results = drop_rows(
        results,
        URL_IN_MARKDOWN,
        "https://anaconda.org",
        if_result_code="403",
    )
    # UAB specific requiring login
    results = drop_rows(
        results,
        URL_IN_MARKDOWN,
        "https://idm.uab.edu/cgi-cas/xrmi/sites",
        if_result_code="423",
    )

    ### modify file uris to improve readability
    results[MARKDOWN_FILE] = modify_file_uris(results[MARKDOWN_FILE])

    ### organize
    results = results.sort_values(
        by=[RESULT, URL_IN_MARKDOWN, MARKDOWN_FILE, LINE, COLUMN],
    )

    ### output
    # csv
    results.to_csv(LINKCHECKER_OUT_CSV, index=False)

    # yml
    records = results.to_dict(orient="records")
    with Path(LINKCHECKER_OUT_YAML).open("w") as f:
        yaml.safe_dump(records, f, sort_keys=False)
