import subprocess
from pathlib import Path, PurePath

import pandas as pd

# Cleans up output of linkchecker

OUTPUT = PurePath("out")
Path(OUTPUT).mkdir(exist_ok=True)

LINKCHECKER_LOG = OUTPUT / "linkchecker.log"
LINKCHECKER_CSV = OUTPUT / "linkchecker-out.csv"


if __name__ == "__main__":
    with open(LINKCHECKER_LOG, "wb", buffering=0) as f:
        subprocess.run("linkchecker --config=.linkcheckerrc docs", stdout=f)
    df = pd.read_csv(LINKCHECKER_CSV)
    df = df[["result", "urlname", "parentname", "line", "column", "url"]]

    # drop good urls
    same_url = df["urlname"] == df["url"]
    result_ok = df["result"].str.startswith("200")
    drop = same_url & result_ok
    df = df[~drop]

    # output
    df.to_csv(LINKCHECKER_CSV, index=False)
