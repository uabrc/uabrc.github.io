# Access Permissions in Cheaha Project Allocation

In this tutorial, we will guide you through how to manage access to files and directories in your Cheaha project allocation. We  will cover different methods of granting access, use cases and best practices for permission settings, and how various data transfer tools/methods affect permissions.

## Prerequisites

To get up to speed, you should have a basic understanding of how to use the shell/terminal, project directory structure, Linux permissions (`chmod`, `chgrp`), Access Control Lists (ACLs) (`setfacl`, `getfacl`), and data transfer tools/methods (`cp`, `scp`, `rsync`, `rclone`, Globus).

If you are not familiar with these concepts, we recommend checking out our learning resources on:

- [Basic shell usage](../../workflow_solutions/shell.md).
- Project Directory Structure.
- [File permissions and access control](../../workflow_solutions/shell.md#manage-permissions-of-files-and-directores-chmod).
- [Access Control Lists (ACLs)](../../workflow_solutions/shell.md#manage-researcher-access-to-files-and-directories-getfacl-setfacl).
- [Data transfer tools](../../data_management/transfer/index.md).

## Granting Access to a User

There are two options to grant access for new members:

1. Group Membership

    - Adding new members to the group associated with your Cheaha project directory automatically grants them access to all files and directories.

1. ACLs for Specific Directories

    - If you need to provide temporary or limited access, use ACLs to grant permissions on a directory that you would like to share with.

There are two common scenarios where file and directory access needs to be managed:

- Granting access for users to copy data from a project directory.
- Granting access for users to read/write data within the directory.

 Group membership is the simplest and most effective way to manage access in Cheaha project directory. Once a user has access via group membership or ACLs, they can also manage ACLs for files they own. This means everyone (including the project owner, lab members, and users granted access via ACLs) shares the responsibility of overseeing and managing permissions for the files and directories they work with.

## Understanding File Permissions and ACLs

Permissions in a project directory are affected by:

- Parent directory permissions
- ACLs
- Tools/methods used to move/copy data

Different data transfer tools/methods and their effect on file permissions and ACLs is shown in the table below.

{{ read_csv('data_management/res/transfer_tool_properties.csv', keep_default_na=False) }}

Therefore,  we recommend users to consider the below points when moving and copying files and directories in shared allocations.

- Avoid `cp -a`, `cp -p`, `scp`, and `mv` for preserving ACLs.
- Use `rclone`, and Globus  to copy/transferring data, as they respects ACLs.

<!-- markdownlint-disable MD046 -->
!!! note

    Before making permission changes, ensure that there are no special cases that need to be preserved within a directory and its files.
<!-- markdownlint-enable MD046 -->
