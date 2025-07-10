# Cheaha Storage (GPFS)

The Cheaha storage, also known as GPFS (General Parallel File System), is a distributed file system designed for managing dynamic data and serves as a storage solution on Cheaha. We provide the following Cheaha storage solutions.

## User Data and Home Directories

Every user of Cheaha are given a storage space to store general data and data that can be used during active analysis. While there are no data retention policies in place, these spaces are not intended for long-term storage of data that changes infrequently. Traditionally, `$HOME` is intended to store scripts, supporting files, software configuration files, and toolboxes such as Anaconda virtual environments or R packages. In contrast, `$USER_DATA` is intended to store datasets and results for individual research projects, with access granted only to the user of that directory. Since the quotas for these directories are limited to 5TB, you may consider using [scratch](#scratch) space and/or [project directories](#project-directory) for storing, moving, and analyzing data.

## Project Directory

The Project Directories are larger than user data directories and serve as a storage solution accessible to Labs led by a PI and Core facilities led by a director. It is intended for sharing data and code within a group of researchers or among lab members and collaborators, located under `/data/project/<project>`.

The PI is the owner of the project directory, and when a directory `/data/project/<project>` is created, researchers permitted to collaborate on the project are added as members of this group, granting them access to the project directory. New members can be added or removed from the group upon PI approval. Currently, a project directory space is 25 TB, and this space is not designated for a single project only; it serves as storage for multiple projects.

### Project Directory Permissions

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
    - Retaining source permissions in project directories is undesirable behavior and can create headaches for you, your colleagues, and your project directory administrators and PIs.

For PIs and project administrators:

- Please educate your staff and collaborators about the above permission setups, and any additional ACLs you may have in place, to minimize future challenges.
- If you have issues with permissions, please contact [Support](../../help/support.md). We can guide you through [Managing Permissions](../../workflow_solutions/shell.md#manage-permissions-of-files-and-directores-chmod) and [Managing Group Ownership](../../workflow_solutions/shell.md#manage-group-ownership-chgrp).

## Scratch

Two types of scratch space are provided for analyses currently being ran, network-mounted and local. These are spaces shared across users (though one user still cannot access another user's files without permission) and as such, data should be moved out of scratch when the analysis is finished.

<!-- markdownlint-disable MD046 -->
!!! important

    Starting January 2023, scratch data will have limited retention. See [Scratch Retention Policy](#scratch-retention-policy) for more information.
<!-- markdownlint-enable MD046 -->

### User Scratch

All users have access to a large, temporary, work-in-progress directory for storing data, called a scratch directory in `/scratch/$USER` or `$USER_SCRATCH`. Use this directory to store very large datasets or temporary pipeline intermediates for a short period of time while running your jobs. The maximum amount of data a single user can store in network scratch is 100 TB at once.

Network scratch is available on the login node and each compute node. This storage is a GPFS high performance file system providing roughly 1 PB of storage. If using scratch, this should be your jobs' primary working directory, unless the job would benefit from local scratch (see below).

<!-- markdownlint-disable MD046 -->
!!! warning

    Research Computing expects each user to keep their scratch areas clean. **The cluster scratch areas are not to be used for archiving data.** In order to keep scratch clear and usable for everyone, files older than 30 days will be eligible for deletion.
<!-- markdownlint-enable MD046 -->

### Local Scratch

Each compute node has a local scratch directory that is accessible via `/local/`. We recommend creating a subdirectory `/local/$USER/` to simplify data management avoid confusing your files for those of others working on the same node. You can further separate data needed for different jobs you are running with the subdirectory `/local/$USER/$SLURM_JOB_ID`.

If your job performs a lot of file I/O, the job should use local scratch rather than `$USER_SCRATCH` to ensure adequate performance and avoid impacting other users. When using local scratch, file reading and writing stays on the node doing the processing, freeing up network resources for other tasks. It's important to recognize that most jobs run on the cluster do not fall under this category. However, any work that requires frequent disk access or high-bandwidth disk access are good candidates for using local scratch.

At this time you will need to make local scratch subdirectories yourself with `mkdir -p /local/$USER` and `mkdir -p /local/$USER/$SLURM_JOB_ID`. Note that `$SLURM_JOB_ID` is only defined within a job context. If you need to keep files separated among jobs, use `/local/$USER/$SLURM_JOB_ID`. If you need to share files on one node among multiple jobs use `/local/$USER/` instead.

Some known examples of tasks benefiting from local scratch, not an exhaustive list:

- AI and deep learning training on [A100 GPUs](../../cheaha/slurm/gpu.md).
- Large-scale genome annotation.
- Reading/writing hundreds of thousands or more files in a single job.

If you are using `amperenodes` and the A100 GPUs, then you should use local scratch for your data to ensure adequate GPU performance. Using `$USER_SCRATCH`, or other network file locations, will starve the GPU of data, resulting in poor GPU performance. For more information please see [Ensuring IO Performance With A100 GPUs](../../cheaha/slurm/gpu.md#ensuring-io-performance-with-a100-gpus).

<!-- markdownlint-disable MD046 -->
!!! important

    Be sure to clean up `/local/$USER/$SLURM_JOB_ID` after your job is complete!
<!-- markdownlint-enable MD046 -->

An example script to automate this process is shown below. This example shows how you can wrap your workflow with deployment and cleanup of local scratch. The following sample script only applies if you are running a small number of jobs (less than one hundred). If you need to run many jobs all using the same data, such as with a large array using the `--array` flag, please [contact us](../../help/support.md) about preloading the data onto your desired nodes. This will avoid the per-job overhead of copying and deleting files.

```bash
#!/bin/bash
#SBATCH ...

# LOAD MODULES
# module load ...

# CREATE TEMPORARY DIRECTORY
# WARNING! $TMPDIR will be deleted at the end of the script!
# Changing the following line can cause permanent, unintended deletion of important data.
TMPDIR="/local/$USER/$SLURM_JOB_ID"
# The -p flag creates all parents of the `$SLURM_JOB_ID` subdirectory, i.e. `/local/$USER/`, if they don't already exist.
mkdir -p "$TMPDIR"

# COPY RESEARCH DATA TO LOCAL TEMPORARY DIRECTORY
# Replace $MY_DATA_DIR with the path to your data folder
cp -r "$MY_DATA_DIR" "$TMPDIR"

# YOUR ORIGINAL WORKFLOW GOES HERE
# be sure to load files from "$TMPDIR"!

# CLEAN UP TEMPORARY DIRECTORY
# WARNING!
# Changing the following line can cause permanent, unintended deletion of important data.
rm -rf "$TMPDIR"
```

<!-- markdownlint-disable MD046 -->
!!! important

    Using `/local/$USER/$SLURM_JOB_ID` with MPI jobs takes additional consideration. If you do not need MPI, please use the `#SBATCH --nodes=1` slurm directive to specify that all requested cores are on the same node. If you need the performance of `/local/$USER/$SLURM_JOB_ID` in an MPI job, please contact [Support](../../help/support.md) and read about the Slurm commands `sbcast` and `sgather`.
<!-- markdownlint-enable MD046 -->

<!-- markdownlint-disable MD046 -->
!!! note

    By default the variable `$TMPDIR` points to `/scratch/local/` which in turn is a symbolic link to `/local/`. The variable `$LOCAL_SCRATCH` is identical to `$TMPDIR`.

    We recommend overwriting `$TMPDIR`, as above, because it will ensure that jobs always write to a safe location on the same node the work is being done.
<!-- markdownlint-enable MD046 -->

#### What if My Data Won't Fit in Local Scratch?

Be sure that your files will fit in `/local/` before starting. You can determine disk size and current usage using `df -h | grep "local"`. Most nodes have 1.0 TB total capacity, while the `amperenodes` have 6.0 TB. If you data won't fit in the current usage, or on the drives, please [Contact Us](../../help/support.md). We can work with you to identify a solution.

#### What if I Have a Large Amount of Data for Local Scratch?

If you have a large amount of data but each job takes very little time to run, performance can be further improved by avoiding frequent data copies and deletions. In these cases, preloading the data onto local scratch only once and then reusing it makes more sense. If this is the case for you, or you think you might benefit, please [Contact Us](../../help/support.md) and we can discuss creating a temporary node reservation to allow one-time data preloading.

## Temporary Files (`/tmp/` Directory)

Please do not use the directory `/tmp/` as storage for temporary files. The `/tmp/` directory is local to each node, and a full `/tmp/` directory harms compute performance on that node for all users. Instead, please use [local scratch](#local-scratch) for fastest access and [`$USER_SCRATCH`](#user-scratch) for largest space.

Some software packages default to using `/tmp/` without any warning or documentation, especially software designed for personal computers. We may reach out to inform you if your software fills `/tmp/`, as it can harm performance on that compute node. If that happens we will work with you to identify ways of redirecting temporary storage to one of the scratch spaces.

### Software Known to Use `/tmp/`

The following software are known to use `/tmp/` by default, and can be worked around by using the listed flags. See [Local Scratch](#local-scratch) for more information about creating a local temporary directory. You may need to manually create (and clean) `/local/$USER/$SLURM_JOB_ID/`.

- [Java](https://docs.oracle.com/cd/E63231_01/doc/BIAIN/GUID-94C6B992-1488-4FC7-85EC-91E410D6E7D1.htm#BIAIN-GUID-94C6B992-1488-4FC7-85EC-91E410D6E7D1): `java * -Djava.io.tmpdir=/local/$USER/$SLURM_JOB_ID`
- [UMI Tools](https://umi-tools.readthedocs.io/en/latest/common_options.html): `umi_tools * --temp-dir=/local/$USER/SLURM_JOB_ID`
- [Samtools Sort](http://www.htslib.org/doc/samtools-sort.html): `samtools sort * -T /local/$USER/$SLURM_JOB_ID`
- [GATK Tool](https://gatk.broadinstitute.org/hc/en-us/community/posts/360072269012--tmp-dir-option-user-error): `gatk --java-options * --tmp-dir /local/$USER/$SLURM_JOB_ID`
- [NVIDIA Clara Parabricks](https://docs.nvidia.com/clara/parabricks/latest/gettingstarted.html): `pbrun * --tmp-dir=/local/$USER/$SLURM_JOB_ID`.
- [FastQC](https://home.cc.umanitoba.ca/~psgendb/doc/fastqc.help): `fastqc * -d /local/$USER/$SLURM_JOB_ID`
- [MACS2](https://manpages.org/macs2_callpeak): `macs2 callpeak * --tempdir /local/$USER/$SLURM_JOB_ID`

Software known to use `/tmp/` by default with no known workaround:

- [Keras](https://github.com/tensorflow/tensorflow/blob/5bb81b7b0dd140a4304b92530614502c0c61a150/tensorflow/python/keras/utils/data_utils.py#L205) has `/tmp/.keras` hardcoded as a fallback cache directory if `~/.keras` is inaccessible. See [this GitHub Keras issue](https://github.com/tensorflow/tensorflow/issues/38831) for a discussion of the issue.

## How Much Space Do I Have Left?

- **Individual Storage**: use the command `quota-report` to see usage in `/data/user/$USER` and `/scratch/$USER`.
- **Project Storage**: use the command `proj-quota-report <project>`. Replace `<project>` with the appropriate project directory name, i.e., `/data/project/<project>`. Be sure to _not_ use a trailing slash. Use `proj-quota-report mylab` not `proj-quota-report mylab/`.
- **Long-Term Storage**: please contact [Support](../../help/support.md).

Quota reports are updated nightly, so they may be out of date if you move data around before running these commands.

<!-- markdownlint-disable MD046 -->
!!! tip

    Running out of Cheaha Storage space? Can't afford to remove any data? Please consider using our [Long Term Storage (LTS) system](../lts/index.md).
<!-- markdownlint-enable MD046 -->

### Scratch Retention Policy

Data stored in `/scratch` is subject to two limited retention policies.

- Each user will have a quota of 100 TB of scratch storage.
- Files will be retained for a maximum of 30 days, after which they become eligible for deletion.
