# Project Directory

The Project Directory is larger than home and user data directories and serves as a storage solution accessible to Labs led by a Principal Investigator (PI) and Core facilities led by a director. It is intended for sharing data and code within a group of researchers or among lab members and collaborators, located under `/data/project/<project>`.

The PI is the owner of the project directory, and when a directory `/data/project/<project>` is created, researchers permitted to collaborate on the project are added as members of this group, granting them access to the project directory. New members can be added or removed from the group upon PI approval. Currently, a project directory space is 25 TB, and this space is not designated for a single project only; it serves as storage for multiple projects.

## Project Directory Permissions

Every project directory has a group that is unique system-wide, and not used anywhere else on the filesystem. The unique project group will be referred to as `<grp>` and generally has the same name as the top level project directory.

<!-- markdownlint-disable MD046 -->
!!! note

    Some early group names may not match their project directory, but should be reasonably close.
<!-- markdownlint-enable MD046 -->

Members of the project directory group have permissions to access that project directory. Adding and removing members from the project directory group is how Research Computing controls access to, and ownership of, project directories. We do not use access control lists (ACLs) to manage permissions ourselves, but use of ACLs is allowed and encouraged for PIs and project administrators who want more fine-grained control. Please see our [section on ACLs](../../workflow_solutions/shell.md#manage-researcher-access-to-files-and-directories-getfacl-setfacl) for more information.

Be default, project space permissions are set up in the following way:

{{ read_csv('data_management/res/project_space_permissions.csv', keep_default_na=False) }}

Having `setgid` enabled on directories means new files and directories created within will inherit group ownership and the `setgid` bit. The `setgid` bit is reflected by the `2` in the numeric permissions and the `s` in the symbolic permissions. The `setgid` bit and per-directory project groups is how Research Computing controls access to each project directory.

There are some known issues surrounding project directory permissions when files are put into the project directory. Different commands have different behaviors. The following list describes the behaviors of various commands used to move and copy data, as well as good practices.

- `mv` maintains all permissions and ownerships of the source file or directory.
    - For files and directories created outside the project directory, avoid using `mv`, prefer `cp` or similar instead. See below for alternatives.
    - For files and directories created within the project directory, `mv` may work, but be sure the file has correct permissions and group ownership.
- `cp`, `tar -x`, `rsync`, `rclone`, `sftp` and Globus all behave as though creating a new file at the target location, by default. Prefer these commands when it is sensible to do so.
    - Avoid using the `-p` flag with `cp`, `tar`, `rsync` and `sftp`.
    - When using the `-p` flag, files and directories will retain their source permissions.
    - Retaining source permissions in project directories is undesirable behavior and can create headaches for you, your colleagues,s and your project directory administrators and PIs.

For PIs and project administrators:

- Please educate your staff and collaborators about the above permission setups, and any additional ACLs you may have in place, to minimize future challenges.
- If you have issues with permissions, please contact [Support](../../help/support.md). We can guide you through [Managing Permissions](../../workflow_solutions/shell.md#manage-permissions-of-files-and-directores-chmod) and [Managing Group Ownership](../../workflow_solutions/shell.md#manage-group-ownership-chgrp).

## Project Directory Organization

Effective research data management starts with a well organized directory structure, especially for researchers working on multiple projects under shared allocations. A well organized project directory structure ensures scalability, simplifies collaboration, and makes it easier to manage permissions.

To maintain long-term organization, create a new subdirectory each time your group begins a distinct project. Assign [permissions](#permissions-and-access-control) based on access needs to ensure security while allowing collaboration.

Below is a recommended directory structure to help keep project files, shared research data, and software environments organized within shared allocations on Cheaha.

1. Top-Level Directory

    Suppose the top-level directory is your lab Cheaha project directory, `/data/project/mylab/`.

1. Projects' Directory

    Each project gets its own subdirectory. This keeps things organized and isolated from one another, making it easier to manage and avoid confusion.

    Example:

    ```bash
    /data/project/mylab/project/
    |-- project-1/
    |-- project-2/
    |-- project-3/
    ```

1. Repositories

    If your projects rely on code or software tools that are used across multiple efforts, you can set up a repository directory for shared scripts, tools, or utilities.

    Example:

    ```bash
    /data/project/mylab/repository/
    |-- common-software-tool-1/
    |-- common-software-tool-2/
    ```

1. Shared Research Data

    Having a separate directory for research data that is common across projects helps prevent duplication and ensures that everyone is working with the same dataset.

    Example:

    ```bash
    /data/project/mylab/common-data/
    |-- some-data-used-by-multiple-projects/
    |-- other-shared-data/
    ```

1. Environments

    For projects that require specific software environments (e.g., Conda environments), you can centralize these in a separate directory. This way, you ensure that everyone is using the right tools.

    Example:

    ```bash
    /data/project/mylab/environments/
    |-- shared-conda-env-1.yml
    |-- shared-conda-env-2.yml
    ```

To provide a clearer picture, here is how all the components fit together in the overall structure:

```bash
/data/project/mylab/
|-- project/
|   |-- project-1/
|   |-- ...
|-- repository/
|   |-- common-software-tool-1/
|   |-- ...
|-- common-data/
|   |-- some-data-used-by-multiple-projects/
|   |-- ...
|-- environments/
|   |-- shared-conda-env-1.yml
|   |-- ...
```

## Permissions and Access Control

Permissions for each directory can be managed by either being a member of the group associated with the top-level project directory or by using [Linux permissions](../cheaha_storage_gpfs/project_directories.md#project-directory-permissions) or [Access Control Lists (ACLs)](../../workflow_solutions/shell.md#manage-researcher-access-to-files-and-directories-getfacl-setfacl). Managing proper permissions ensures that team members can access only the resources they need, while protecting sensitive data.

If you plan managing multiple projects and would like assistance with organizing your project directories or managing permissions, please send us a [support ticket](../../help/support.md#how-do-i-create-a-support-ticket).

## How Much Space Do I Have Left?

To check the storage space left from your project directory, use the command `proj-quota-report <project>`. Replace `<project>` with the appropriate project directory name, i.e., `/data/project/<project>`. Be sure to _not_ use a trailing slash. Use `proj-quota-report mylab` not `proj-quota-report mylab/`.

## Policies & Expectations

This section outlines key storage policies and exceptions, including access control and data management, conditions for administrative access or quota increases in Project directory.

- Storage Entitlement: A shared project allocation of 25 TB is available to research labs led by a PI and to Core Facilities headed by a Director. A shared project allocation is intended to support active research and collaboration.
- Quota Increase: At this time, we do not provide additional quota increase for shared project allocation. If you require more storage for your work, please consider requesting and using an [LTS](../../data_management/lts/index.md).
- Data Management: The owner the shared Project allocation is responsible for organizing, cleaning, and backing up their data in their shared Project allocation.
- Permission and Access Control Management: Access to shared project allocation can be managed using Access Control Lists (ACLs). New members can be added to or removed from the group access based on PI approval.
- HIPAA Compliance: Shared project allocation is HIPAA compliant and can accept Protected Health Information (PHI) data. For HIPAA Compliance and UAB policies surrounding PHI data, please refer the [HIPAA Compliance](../../data_management/index.md#hipaa-compliance)page.
