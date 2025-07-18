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

This section outlines key storage policies and exceptions, including access control, data management, and conditions for administrative access or quota increases in user data and home directories.

- Storage Entitlement: All users receive a 5TB of default quota upon creating a Cheaha account.
- Quota Increase: At this time, we do not provide a quota increase in user data and home directories. If you require more storage for your work, please consider using [shared project allocation](./project_directory.md) or an [LTS](../../data_management/lts/index.md).
- Data Management: Users are responsible for organizing, cleaning, and backing up their data in their user data and home directory.
- Permission and Access Control Management: Access in user data and home directories can be managed using Access Control Lists (ACLs). Where third-party access is required, a security exception may apply. Please refer to the [Security Exception](../../data_management/research_data_responsibilities.md#security-exceptions-for-accessing-former-uab-personnel-data) page for more details.
- HIPAA Compliance: Users data and home directories are HIPAA compliant and can accept Protected Health Information (PHI) data. For HIPAA Compliance and UAB policies surrounding PHI data, please refer the [HIPAA Compliance](../../data_management/index.md#hipaa-compliance)page.
