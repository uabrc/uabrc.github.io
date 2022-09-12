# Storage

<!-- markdownlint-disable MD046 -->
!!! warning

    The information on this page is under construction and some of it may be obsolete. If you need additional clarifications in the meantime, please [contact us](../index.md#contact-us).
<!-- markdownlint-enable MD046 -->

## What Type of Storage Do I Need?

There are multiple locations for data storage both on and off Cheaha each with a specific purpose. You can look at the table below to find the storage platform we provide that best matches your needed use-case.

{{ read_csv('data_management/storage_overview.csv', keep_default_na=False) }}

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

## Scratch

Two types of scratch space are provided for analyses currently being ran, network-mounted and local. These are spaces shared across users (though one user still cannot access another user's files without permission) and as such, data should be moved out of scratch when the analysis is finished.

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

## How much space do I have left?

To check how much space you have left in `/data/user/$USER` and `/scratch/$USER` please enter the command `quota-report`. This report is automatically displayed each time you log in.

For space in `/data/project/<project>` please enter the command `proj-quota-report <project>`. Replace `<project>` with the appropriate project directory name.

Both quota reports are updated nightly.

## Data Policies

### Backups

**It is the responsibility of the user to maintain proper backups of their data.**

Data on Cheaha are replicated from a main drive to an emergency backup drive each time a file is created, altered, or destroyed. This emergency backup drive is only used when there is a cluster failure and does not function as a traditional backup. If you delete data from the cluster, it is gone forever.

### HIPAA Compliance

As of December 2019, Cheaha is HIPAA compliant and so PHI can be stored on it. Currently, long-term storage is NOT HIPAA compliant but will be in the future.

<!-- markdownlint-disable MD046 -->
!!! important

    It is the responsibility of the user to make sure PHI is only accessible by researchers on the IRB. If PHI is being stored in a project folder and some researchers are not on an IRB, their access to those files should be restricted using Access Control Lists (ACLs). If you need assistance setting up ACLs properly, please [contact us](../index.md#contact-us).
<!-- markdownlint-enable MD046 -->

## Directory Permissions

Default file permissions are described for each directory above.
Additional background on Linux file system permissions can be found
here:

- <https://its.unc.edu/research-computing/techdocs/how-to-use-unix-and-linux-file-permissions/>
- <https://www.rc.fas.harvard.edu/resources/documentation/linux/unix-permissions/>
- <https://hpc.nih.gov/storage/permissions.html>
