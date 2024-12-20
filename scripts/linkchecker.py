import subprocess
from pathlib import Path, PurePath
from typing import Optional

import pandas as pd

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
    with open(LINKCHECKER_LOG, "wb", buffering=0) as f:
        subprocess.run("linkchecker --config=.linkcheckerrc docs", stdout=f)


def load_output() -> pd.DataFrame:
    df = pd.read_csv(LINKCHECKER_RAW_CSV)
    df = df[[RESULT, URLNAME, URL, PARENTNAME, LINE, COLUMN]]
    df = df.rename(
        columns={
            URLNAME: URL_IN_MARKDOWN,
            URL: URL_AFTER_REDIRECTION,
            PARENTNAME: MARKDOWN_FILE,
        },
    )
    return df


def replace_lines_containing(
    _s: pd.Series, _containing: str, _with: str, /, find_in: Optional[pd.Series] = None
) -> pd.Series:
    if find_in is None:
        find_in = _s

    contains = find_rows_containing(find_in, _containing)
    out = _s.copy()
    out[contains] = _with
    return out


def find_rows_containing(_s: pd.Series, _containing: str) -> pd.Series:
    return _s.str.contains(_containing)


def ignore_ok_with_no_redirects(_df: pd.DataFrame) -> pd.DataFrame:
    same_url = _df[URL_IN_MARKDOWN] == _df[URL_AFTER_REDIRECTION]
    result_ok = _df[RESULT].str.startswith("200")
    drop = same_url & result_ok
    out = _df[~drop]
    return out


def ignore_rows_containing(
    _df: pd.DataFrame,
    _in: str,
    _containing: str,
    /,
    if_result_code: Optional[str] = None,
) -> pd.DataFrame:
    find_in = _df[_in]
    contains = find_rows_containing(find_in, _containing)

    if if_result_code is not None:
        contains &= _df[RESULT].str.contains(if_result_code)

    out = _df[~contains]
    return out


if __name__ == "__main__":
    run_linkchecker()
    df = load_output()

    # drop good urls
    df = ignore_ok_with_no_redirects(df)

    # change 200 OK to 300 Redirect for human clarity
    df[RESULT] = replace_lines_containing(df[RESULT], "200 OK", "300 Redirect")

    # replace long error messages with short codes
    df[RESULT] = replace_lines_containing(df[RESULT], "ConnectTimeout", "408 Timeout")

    # special code for SSO urls
    df[RESULT] = replace_lines_containing(
        df[RESULT],
        "https://padlock.idm.uab.edu",
        "423 Locked",
        find_in=df[URL_AFTER_REDIRECTION],
    )

    # special ignore rules
    df = ignore_rows_containing(
        df, URL_IN_MARKDOWN, "https://doi.org", if_result_code="300"
    )  # doi.org always redirects, that's its purpose, so we ignore
    df = ignore_rows_containing(
        df, URL_IN_MARKDOWN, "https://anaconda.org", if_result_code="403"
    )  # if anaconda.org goes down we'll surely hear about it
    df = ignore_rows_containing(
        df, URL_AFTER_REDIRECTION, "https://padlock.idm.uab.edu", if_result_code="423"
    )

    # organize
    df = df.sort_values(by=[RESULT, URL_IN_MARKDOWN, MARKDOWN_FILE, LINE, COLUMN])

    # output
    df.to_csv(LINKCHECKER_OUT_CSV, index=False)
