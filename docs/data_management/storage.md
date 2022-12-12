# Storage

<!-- markdownlint-disable MD046 -->
!!! announcement

    Please note upcoming changes!

    - December 13, 2022: Clean up of `temp-scratch` must be completed by all researchers.
    - December 16, 2022: Access to `temp-scratch` will be removed for all researchers.
    - January 16, 2023: New `$SCRATCH` storage limited-retention policies will start.
    - To Be Determined: `$USER_SCRATCH` will point to `/scratch/$USER`
<!-- markdownlint-enable MD046 -->

## What Type of Storage Do I Need?

There are multiple locations for data storage both on and off Cheaha each with a specific purpose. You can look at the table below to find the storage platform we provide that best matches your needed use-case.

{{ read_csv('data_management/res/storage_overview.csv', keep_default_na=False) }}

## User Space

Each user has personal directories found at `/home/$USER` (or `$HOME`) and `/data/user/$USER` (or `$USER_DATA`). These two locations are meant to store general data long-term and can be used during active analysis or for archiving small projects. Traditionally, `$HOME` is meant to store scripts and supporting files and toolboxes such as Anaconda virtual environments or R packages while `$USER_DATA` can store datasets and results for a user's projects.

The owner (`$USER`) of both directories can read, write/delete, and list files. No other users or groups have permissions to this directory. While it is possible to share files in your personal space with other users, a more practical solution may be to use a [project directory](#project-directory) instead.

A user is limited to 5 TB of data across both `$HOME` and `$USER_DATA` combined.

<!-- markdownlint-disable MD046 -->
!!! note

    The home and user data directories are mirrored across storage locations to allow for emergency backup in case some of the drives fail. This is not meant to be a long-term backup solution as any data deleted by a user is deleted on the main drive and the mirrored drive.
<!-- markdownlint-enable MD046 -->

## Project Directory

Shared data can be stored in a `/data/project/<project_name>` directory. The default storage size for a new project is 50TB. If you need less than 5TB or your need for shared space is short term, please request a [Sloss space](#sloss) instead. Project storage can be helpful for teams of researchers who need access to the same data.

All project spaces must be owned by a principal investigator (PI) who is an employee of UAB with a legitimate research interest. The PI takes responsibility for data in the space, as well as access control of all files and directories under the parent directory. As with all data on Cheaha, backups and archival services are not provided, and are the responsibility of the respective data owners.

The PI and all members with access to the project directory can read, write/delete, and list files within the top-level directory, and all other subdirectories by default. Other people on the system have no ability to access the project space. Access control for directories and files within the project space can be implemented via access control lists. Please see the bash commands [setfacl](https://linux.die.net/man/1/setfacl) and [getfacl](https://linux.die.net/man/1/getfacl)) for more information. Access control within the project directory are the responsibility of the project owner. However, we respect that access control lists can be tricky, so please feel free to [contact us](../index.md#contact-us) for assistance.

To create a project directory, or change access to or ownership of a project directory, the PI should follow the instructions at [How Do I Request Or Change A Project Space?](../help/support.md#how-do-i-request-or-change-a-project-space)

### Sloss

A special location under `/data/project/sloss` to store projects that are at most 5 TB. In keeping with the name [Sloss](https://www.slossfurnaces.com/), these spaces are intended as a foundry for experimental or temporary project spaces that have potential to grow. Otherwise, they are treated like any other project space.

### Project Directory Permissions

Every project directory has a group that is unique system-wide, and not used anywhere else on the filesystem. The unique project group will be referred to as `<grp>` and generally has the same name as the top level project directory.

<!-- markdownlint-disable MD046 -->
!!! note

    Some early group names may not match their project directory, but should be reasonably close.
<!-- markdownlint-enable MD046 -->

Members of the project directory group have permissions to access that project directory. Adding and removing members from the project directory group is how Research Computing controls access to, and ownership of, project directories. We do not use access control lists (ACLs) to manage permissions ourselves, but use of ACLs is allowed and encouraged for PIs and project administrators who want more fine-grained control. Please see our [section on ACLs](../workflow_solutions/shell.md#manage-researcher-access-to-files-and-directories-getfacl-setfacl) for more information.

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
    - Retaining source permissions in project directories is undesirable behavior and can create headaches for you, your colleagues, and your project directory administrators and PIs.

For PIs and project administrators:

- Please educate your staff and collaborators about the above permission setups, and any additional ACLs you may have in place, to minimize future challenges.
- If you have issues with permissions, please contact [Support](../help/support.md#contact-us). We can guide you through [Managing Permissions](../workflow_solutions/shell.md#manage-permissions-of-files-and-directores-chmod) and [Managing Group Ownership](../workflow_solutions/shell.md#manage-group-ownership-chgrp).

## Scratch

Two types of scratch space are provided for analyses currently being ran, network-mounted and local. These are spaces shared across users (though one user still cannot access another user's files without permission) and as such, data should be moved out of scratch when the analysis is finished.

<!-- markdownlint-disable MD046 -->
!!! important

    Starting January 2023, scratch data will have limited retention. See [Scratch Retention Policy](#scratch-retention-policy) for more information.
<!-- markdownlint-enable MD046 -->

### User Scratch

All users have access to a large, temporary, work-in-progress directory for storing data, called a scratch directory in `/data/scratch/$USER` or `$USER_SCRATCH`. Use this directory to store very large datasets or temporary pipeline intermediates for a short period of time while running your jobs. The maximum amount of data a single user can store in network scratch is 100 TB at once.

Network scratch is available on the login node and each compute node. This storage is a GPFS high performance file system providing roughly 1 PB of storage. If using scratch, this should be your jobs' primary working directory, unless the job would benefit from local scratch (see below).

<!-- markdownlint-disable MD046 -->
!!! warning

    Research Computing expects each user to keep their scratch areas clean. **The cluster scratch areas are not to be used for archiving data.** In order to keep scratch clear and usable for everyone, files older than 30 days will be automatically deleted.
<!-- markdownlint-enable MD046 -->

### Local Scratch

Each compute node has a local scratch directory that is accessible via the variable `$LOCAL_SCRATCH`. If your job performs a lot of file I/O, the job should use `$LOCAL_SCRATCH` rather than `$USER_SCRATCH` to prevent bogging down the network scratch file system. It's important to recognize that most jobs run on the cluster do not fall under this category.

<!-- markdownlint-disable MD046 -->
!!! important

    `$LOCAL_SCRATCH` is only useful for jobs in which all processes run on the same compute node, so MPI jobs are not candidates for this solution. Use the `#SBATCH --nodes=1` slurm directive to specify that all requested cores are on the same node.
<!-- markdownlint-enable MD046 -->

## Temporary Files (`tmp`)

Please do not use the directory `tmp` as storage for temporary files. The `tmp` directory is local to each node, and a full `tmp` directory harms compute performance on that node for all users. Instead, please use [`$LOCAL_SCRATCH`](#local-scratch) for fast access and [`$USER_SCRATCH`](#user-scratch) for larger space.

Some software defaults to using `tmp` without any warning or documentation, especially software designed for personal computers. We may reach out to inform you if your software fills `tmp`, as it can harm performance on that compute node. If that happens we will work with you to identify ways of redirecting temporary storage to one of the scratch spaces.

### Software Known to Use `tmp`

The following software are known to use `tmp` by default, and can be worked around by using the listed flags.

- Java: `java * -Djava.io.tmpdir=$LOCAL_SCRATCH`
- UMI Tools: `umi_tools * --temp-dir=$LOCAL_SCRATCH`

## How much space do I have left?

- **Personal**: use the command `quota-report` to see usage in `/data/user/$USER` and `/scratch/$USER`.
- **Project**: use the command `proj-quota-report <project>`. Replace `<project>` with the appropriate project directory name, i.e., `/data/project/<project>`. Be sure to _not_ use a trailing slash. Use `proj-quota-report mylab` not `proj-quota-report mylab/`.

Both quota reports are updated nightly, so they may be out of date if you move data around before running these commands.

<!-- markdownlint-disable MD046 -->
!!! tip

    Running out of space? Can't afford to remove any data? Please consider using our [Long Term Storage (LTS) system](lts/lts.md).
<!-- markdownlint-enable MD046 -->

## Data Policies

### Replication

Data on GPFS are replicated using a RAID configuration which is intended to decrease the risk of data loss in the event of disk failures. This is standard good practice for researcher computing data centers.

### Backups

<!-- markdownlint-disable MD046 -->
!!! important

    Backups of data are the responsibility of researchers using Cheaha.
<!-- markdownlint-enable MD046 -->

A good practice for backing up data is to use the 3-2-1 rule, as [recommended by US-CERT](https://www.cisa.gov/uscert/security-publications/data-backup-options):

- **3**: Keep **3** copies of important data. 1 primary copy for use, 2 backup copies.
- **2**: Store backup copies on **2** different media types to protect from media-specific hazards.
- **1**: Store **1** backup copy offsite, located geographically distant from the primary copy.

What hazards can cause data loss?

- Accidental file deletion.
    - Example: mistakenly deleting the wrong files when using the [shell command](../workflow_solutions/shell.md#delete-files-and-directories-rm-rmdir) `rm`.
    - Files deleted with `rm` or any similar command can not be recovered by us under any circumstances.
    - Please restore from a backup.
- Natural disasters.
    - Examples: tornado; hurricane.
    - All of our data sits in one geographical location at the UAB Technology Innovation Center (TIC).
    - Plans to add geographical data redundancy are being considered.
    - Please restore from an offsite backup.
- Unusable backups.
    - Examples: backup software bug; media destroyed; natural disaster at offsite location.
    - Regularly test data restoration from all backups.

How can I ensure data integrity?

- Regularly back up your (and your lab's) data in an offsite location.
- [S3 based long-term storage (LTS)](lts/lts.md) can be used for short-term onsite backup.
- Crashplan licenses are available for automatic offsite backups, please contact [Support](../help/support.md) for more information.

### HIPAA Compliance

As of December 2019, Cheaha is HIPAA compliant and so PHI can be stored on it. Currently, long-term storage is NOT HIPAA compliant but will be in the future.

<!-- markdownlint-disable MD046 -->
!!! important

    It is the responsibility of the user to make sure PHI is only accessible by researchers on the IRB. If PHI is being stored in a project folder and some researchers are not on an IRB, their access to those files should be restricted using Access Control Lists (ACLs). If you need assistance setting up ACLs properly, please [contact us](../index.md#contact-us).
<!-- markdownlint-enable MD046 -->

### Scratch Retention Policy

Starting January 2023, data stored in `/scratch` will be subject to two limited retention policies.

- Each user will have a quota of 50 TB of scratch storage.
- Files will be retained for 30 days.

## Directory Permissions

Default file permissions are described for each directory above.
Additional background on Linux file system permissions can be found
here:

- <https://its.unc.edu/research-computing/techdocs/how-to-use-unix-and-linux-file-permissions/>
- <https://www.rc.fas.harvard.edu/resources/documentation/linux/unix-permissions/>
- <https://hpc.nih.gov/storage/permissions.html>
