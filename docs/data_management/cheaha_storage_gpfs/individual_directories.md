# User Directories

Every user of Cheaha are given a storage space to store general data and data that can be used during active analysis. While there are no data retention policies in place, these spaces are not intended for long-term storage of data that changes infrequently.

## User Data and Home Directories

Home directory is the directory the your are landed when you first login to the Cheaha. The `$HOME` directory is intended to store scripts, supporting files, software configuration files, and toolboxes such as Anaconda virtual environments or R packages. In contrast, `$USER_DATA` is intended to store datasets and results for individual research projects, with access granted only to the user of that directory. Since the quotas for these directories are limited to 5TB, you may consider using [scratch](./scratch.md) space and/or [project directories](./project_directory.md) for storing, moving, and analyzing data.

## How Much Space Do I Have Left?

Use the command `quota-report` to see usage in `/data/user/$USER` and `/scratch/$USER`.

Quota reports are updated nightly, so they may be out of date if you move data around before running these commands.

<!-- markdownlint-disable MD046 -->
!!! tip

    Running out of Cheaha Storage space? Can't afford to remove any data? Please consider using our [Long Term Storage (LTS) system](../lts/index.md).
<!-- markdownlint-enable MD046 -->

## Policies & Expectations
