# Storage

Research Computing offers several data storage options to meet individual or shared needs of UAB researchers, depending on their requirement and use-cases. The types of storage available, procedures for requesting access, responsibilities, and usage guidelines are detailed in the following sections.

## What Type of Storage Do I Need?

There are multiple locations for data storage both on and off Cheaha each with a specific purpose. You can look at the table below to help determine the storage platform we provide that best matches your needed use-case. If you need additional assistance, please contact [Support](../help/support.md).

{{ read_csv('data_management/res/storage_overview.csv', keep_default_na=False) }}

## What Individual Storage Solutions are Available?

Every Cheaha user has personal directories found at `/home/$USER` (or `$HOME`) and `/data/user/$USER` (or `$USER_DATA`), which are created automatically during account registration. In addition, individual allocations on Long-Term Storage (LTS) are also available upon request. Please read more about [Long-Term Storage](./lts/index.md) and [User Data and Home Directories](#user-data-and-home-directories).

### How Do I Request Individual Long-Term Storage?

To request individual Long-Term Storage, please first read and understand how [Long-Term Storage](./lts/index.md) differs from traditional file systems, like GPFS on Cheaha. Decide if it is suitable for your needs. Then please feel free to contact [Support](../help/support.md).

## What Shared Storage Solutions are Available?

Shared Storage is available via two services. We have [Project Storage](#project-directory) (located in `/data/project` or Cheaha) and [Long-Term Storage (LTS)](./lts/index.md). The two offerings are suited to different sets of use-cases and are available upon request, so please read on to determine which may be most suitable.

[Project Storage](#project-directory) is best-suited for changing or dynamic data. Specifically::

- Data needing/undergoing analysis
- Exploratory data
- Temporary data needed longer than 30 days

In contrast, [Long-Term Storage](./lts/index.md) is best-suited for unchanging or static data. Specifically:

- Instrument-acquired data
- Completed analyses
- Hosting data for others to copy
- Hosting data for the public internet
- "Pick-up" and "drop-off" locations for data as part of a workflow

Shared Storage is available for labs headed by a PI _and_ for Core facilities headed by a director.

Shared Storage is allocated on a per-organization basis, not on a per-person basis. If an individual researcher manages both a lab and a Core, they may request independent storage allocations for each organization. Each organization may request both Project Storage and Long-Term Storage.

### How Do I Request Shared Storage?

To request shared Project Storage or Long-Term Storage, please contact [Support](../help/support.md). To ensure prompt allocation of Shared Storage, please follow the guidelines below:

- Requests must be made to <support@listserv.uab.edu> or via the [AskIT HelpDesk](https://www.uab.edu/it/home/).
- Requests must come from one of the proposed owners (a Lab PI, a Research Core director, or both).
- The role of Lab PI entitles a person to a project space for that lab.
- The role of Research Core director entitles a person to a project space for that core. If one person has both roles, they may have two shared Storage spaces, one for each role.
- All proposed owners must have created their [Research Computing accounts](../account_management/cheaha_account.md) at the time of the request.

Please provide the following information. Missing information can delay allocation of Shared Storage as we either look up the information, or ask followup questions.

- **Responsible Party/Owner:** The BlazerID of the person claiming responsibility for what happens and what is stored in the space. Typically this would be a Principal Investigator (PI) or a Core Director.
    - Multiple responsible parties are allowed.
    - We need one person declared as "primary" owner. This person will be the literal owner (in the Linux sense) for Project Storage.
- **Members:** A list of BlazerIDs of people to give access to the space. (Note: this only applies to Project Storage. LTS access controls are managed differently.)
- **Type of Organization:** Is the Shared Storage request for a lab, core, campus administrative group, or something else?
- **Name of Organization:** The _specific_ name of the organization the Shared Storage request is for.
- **Parent Organization:** The name of the parent organization for your organization. Please be as detailed as possible.
- **Purpose of Shared Storage:** The research purpose for the storage, how do you intend to use it? Please feel free to be as detailed as you like, but please limit to a few sentences at most.
- **Internal UAB Collaborator Organizations:** The name(s) of any other UAB organizations participating in the Shared Storage.
- **External Collaborator Organizations:** The name(s) of any external organizations participating in the Shared Storage.
- **Regulatory Requirements:** List any regulatory requirements or agencies affecting data to be stored in the space. Possibilities include, but are not limited to: IRB, EHR, HIPAA, PHI, FERPA.
- **Name of Shared Storage:** Please give us a generic name specific to your project/Lab.

    - For Labs, we recommend using the format `<PI_BlazerID>_lab`, where `<PI_BlazerID>` is the BlazerID or name of the Principal Investigator (PI). For example: `PI_BlazerID_lab`, `PI_name_lab`.
    - For Cores, we recommend using a shortened version of the Core name. For example: `core_facility_space`
    - For Project Storage, the name you choose will be used in the path `/data/project/<PI_BlazerID>_lab` on Cheaha. Also, this name,`<PI_BlazerID>_lab`, will be given to your shared LTS account.

    <!-- markdownlint-disable MD046 -->
    !!! Tip

        - Keep the name short, memorable, and relevant.
        - Use `underscores (_)` or `hyphen (-)` to separate words.
        - To serve future projects, consider names that are generic.
    <!-- markdownlint-disable MD046 -->

If some members have not created their accounts at the time of the request, we will proceed with allocating the Shared Storage. Additional members may be added at a later time in a new service request.

### How Do I Make Changes to Shared Storage Membership?

To request changes in Shared Storage membership, please contact [Support](../help/support.md). Please take note of the following guidelines to ensure changes can be made promptly.

- We must have written approval from an owner to make membership changes.
- The exact name of the Shared Storage. If it is Project Storage, the path to the storage location, i.e., `/data/project/...`.
- Please give BlazerIDs of members to add or remove.

### How Can I Get A Larger `/data/project/` (GPFS) Allocation?

At this time, due to constraints on total GPFS storage, we are not able to increase `/data/project/` allocations. Please consider batching your analyses by leveraging a combination of [LTS](./lts/index.md) to store raw and/or input data, and [User Scratch](#user-scratch) for temporary storage of up to 100 TB of data for use during analysis.

If you wish to have further discussion of options for expanding your GPFS allocation and other workarounds tailored to your workflow, please [Contact Support](../help/support.md). Please also note that project storage is not just for a single project only, it is meant as a storage for multiple projects.

### How Can I Get A Larger LTS Lab Allocation?

At this time, due to constraints on total [LTS](./lts/index.md) storage, increasing an LTS allocation requires purchasing additional hardware. Below are some facts about purchasing additional storage nodes.

- Allocation increases occur by purchasing whole storage nodes.
- Each node has 133 TB of usable storage.
- Nodes are purchased with researcher funds at vendor cost.
- No markups are added to the cost of nodes.
- Purchased nodes are racked with existing hardware in our data centers.
- Purchased nodes are maintained by Research Computing with the same level of service as other hardware.
- Purchased nodes are supported for 5 years from date of purchase, the industry standard for commercial datacenter hardware.
- Once an order is placed with the vendor, we can provide additional storage immediately _if_ free storage is available, regardless of lead-time.

If you have additional questions _or_ wish to discuss further, please [Contact Support](../help/support.md).

### If I Can't Get a Larger Allocation, What Alternatives Are There?

One alternative we recommend is breaking your dataset into batches. A generic, template workflow might be something like below.

- Copy a batch of data from LTS, or an internet source, to [User Scratch](#user-scratch).
- Perform analyses on copied data in User Scratch.
- Store intermediate or final results in `/data/project/` or LTS.
- Delete copied data from User Scratch.
- Start again with the next batch.

When all batches have been processed, begin processing or aggregating the resulting data.

If you wish to discuss other alternatives tailored to your workflow, please [Contact Support](../help/support.md).

## User Data and Home Directories

Every user of Cheaha are given a storage space to store general data and data that can be used during active analysis. While there are no data retention policies in place, these spaces are not intended for long-term storage of data that changes infrequently. Traditionally, `$HOME` is intended to store scripts, supporting files, software configuration files, and toolboxes such as Anaconda virtual environments or R packages. In contrast, `$USER_DATA` is intended to store datasets and results for individual research projects, with access granted only to the user of that directory. Since the quotas for these directories are limited to 5TB, you may consider using [scratch](#scratch) space and/or [project directories](#project-directory) for storing, moving, and analyzing data.

## Project Directory

The Project Directories are larger than home directories and serves as a storage solution accessible to Labs led by a PI and Core facilities led by a director. It is intended for sharing data and code within a group of researchers or among lab members and collaborators, located under `/data/project/<project>`.

The PI is the owner of the project directory, and when a directory `/data/project/<project>` is created, researchers permitted to collaborate on the project are added as members of this group, granting them access to the project directory. New members can be added or removed from the group upon PI approval. Currently, a project directory space is 25 TB, and this space is not designated for a single project only; it serves as storage for multiple projects.

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
- If you have issues with permissions, please contact [Support](../index.md#how-to-contact-us). We can guide you through [Managing Permissions](../workflow_solutions/shell.md#manage-permissions-of-files-and-directores-chmod) and [Managing Group Ownership](../workflow_solutions/shell.md#manage-group-ownership-chgrp).

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

Each compute node has a local scratch directory that is accessible via `/local/$SLURM_JOB_ID`. At this time, you will need to create the directory manually using `mkdir -p /local/$SLURM_JOB_ID`. If your job performs a lot of file I/O, the job should use `/local/$SLURM_JOB_ID` rather than `$USER_SCRATCH` to prevent bogging down the network scratch file system. It's important to recognize that most jobs run on the cluster do not fall under this category.

If you are using `amperenodes` and the A100 GPUs, then it is highly recommended to move your input files to `/local/$SLURM_JOB_ID` prior to running your workflow, to ensure adequate GPU performance. Using `$USER_SCRATCH`, or other network file locations, will starve the GPU of data, resulting in poor performance. For more information please see [Ensuring IO Performance With A100 GPUs](../cheaha/slurm/gpu.md#ensuring-io-performance-with-a100-gpus).

Be sure to clean up `/local/$SLURM_JOB_ID` after your job is complete! An example script to automate this process is shown below.

```bash
#!/bin/bash
#SBATCH ...

# LOAD MODULES
# module load ...

# CREATE TEMPORARY DIRECTORY
# WARNING! $TMPDIR will be deleted at the end of the script!
# Changing the following line can cause permanent, unintended deletion of important data.
TMPDIR="/local/$USER/$SLURM_JOB_ID"
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

    Using `/local/$SLURM_JOB_ID` with MPI jobs takes additional consideration. If you do not need MPI, please use the `#SBATCH --nodes=1` slurm directive to specify that all requested cores are on the same node. If you need the performance of `/local/$SLURM_JOB_ID` in an MPI job, please contact [Support](../help/support.md) and read about the Slurm commands `sbcast` and `sgather`.
<!-- markdownlint-enable MD046 -->

<!-- markdownlint-disable MD046 -->
!!! note

    By default the variable `$TMPDIR` points to `/scratch/local/` which in turn is a symbolic link to `/local/`. The variable `$LOCAL_SCRATCH` is identical to `$TMPDIR`.

    We recommend overwriting `$TMPDIR`, as above, because it will ensure that jobs always write to a safe location on the same node the work is being done.
<!-- markdownlint-enable MD046 -->

## Temporary Files (`/tmp/` directory)

Please do not use the directory `/tmp/` as storage for temporary files. The `/tmp/` directory is local to each node, and a full `/tmp/` directory harms compute performance on that node for all users. Instead, please use [`/local/$SLURM_JOB_ID`](#local-scratch) for fast access and [`$USER_SCRATCH`](#user-scratch) for larger space.

Some software defaults to using `/tmp/` without any warning or documentation, especially software designed for personal computers. We may reach out to inform you if your software fills `/tmp/`, as it can harm performance on that compute node. If that happens we will work with you to identify ways of redirecting temporary storage to one of the scratch spaces.

### Software Known to Use `/tmp/`

The following software are known to use `/tmp/` by default, and can be worked around by using the listed flags. See [Local Scratch](#local-scratch) for more information about creating a local temporary directory.

- [Java](https://docs.oracle.com/cd/E63231_01/doc/BIAIN/GUID-94C6B992-1488-4FC7-85EC-91E410D6E7D1.htm#BIAIN-GUID-94C6B992-1488-4FC7-85EC-91E410D6E7D1): `java * -Djava.io.tmpdir=/local/$SLURM_JOB_ID`
- [UMI Tools](https://umi-tools.readthedocs.io/en/latest/common_options.html): `umi_tools * --temp-dir=/local/$SLURM_JOB_ID`
- [Samtools Sort](http://www.htslib.org/doc/samtools-sort.html): `samtools sort * -T /local/$SLURM_JOB_ID`
- [GATK Tool](https://gatk.broadinstitute.org/hc/en-us/community/posts/360072269012--tmp-dir-option-user-error): `gatk --java-options * --tmp-dir /local/$SLURM_JOB_ID`
- [Parabricks](https://docs.nvidia.com/clara/parabricks/4.0.1/gettingstarted.html): `pbrun * --tmp-dir=/local/$SLURM_JOB_ID`
- [FastQC](https://home.cc.umanitoba.ca/~psgendb/doc/fastqc.help): `fastqc * -d /local/$SLURM_JOB_ID`
- [MACS2](https://manpages.org/macs2_callpeak): `macs2 callpeak * --tempdir /local/$SLURM_JOB_ID`

Software known to use `/tmp/` by default with no know workaround.

- [Keras](https://github.com/tensorflow/tensorflow/blob/5bb81b7b0dd140a4304b92530614502c0c61a150/tensorflow/python/keras/utils/data_utils.py#L205) has `/tmp/.keras` hardcoded as a fallback cache directory if `~/.keras` is inaccessible. See [here](https://github.com/tensorflow/tensorflow/issues/38831) for a discussion of the issue.

## How much space do I have left?

- **Individual Storage**: use the command `quota-report` to see usage in `/data/user/$USER` and `/scratch/$USER`.
- **Project Storage**: use the command `proj-quota-report <project>`. Replace `<project>` with the appropriate project directory name, i.e., `/data/project/<project>`. Be sure to _not_ use a trailing slash. Use `proj-quota-report mylab` not `proj-quota-report mylab/`.
- **Long-Term Storage**: please contact [Support](../help/support.md).

Quota reports are updated nightly, so they may be out of date if you move data around before running these commands.

<!-- markdownlint-disable MD046 -->
!!! tip

    Running out of space? Can't afford to remove any data? Please consider using our [Long Term Storage (LTS) system](lts/index.md).
<!-- markdownlint-enable MD046 -->

## Data Responsibilities and Procedures

### Archival

<!-- markdownlint-disable MD046 -->
!!! important

    Archival of data is the responsibility of researchers using Cheaha.
<!-- markdownlint-enable MD046 -->

At this time, Research Computing does not offer a method of archival. If you have need for archival, please feel free to contact [Support](../help/support.md) to start a conversation.

A possible external resource for archival is available through University of Oklahoma (OU) Supercomputing Center for Education and Research (OSCER). Please see the following link for details: <https://www.ou.edu/oscer/resources/ourrstore--ou---regional-research-store>.

### Backups

<!-- markdownlint-disable MD046 -->
!!! important

    Backups of data are the responsibility of researchers using Cheaha.
<!-- markdownlint-enable MD046 -->

A good practice for backing up data is to use the 3-2-1 rule, as [recommended by US-CERT](https://www.cisa.gov/sites/default/files/publications/data_backup_options.pdf):

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
- [S3 based long-term storage (LTS)](lts/index.md) can be used for short-term onsite backup.
- Crashplan licenses are available for automatic offsite backups, please contact [Support](../help/support.md) for more information.

### HIPAA Compliance

Cheaha is HIPAA compliant and can accept Protected Health Information (PHI) data. Currently, [long-term storage](lts/index.md) is NOT HIPAA compliant but will be in the future.

For UAB policies surrounding PHI data, please see the following URLs.

- [Data Classification](https://www.uab.edu/it/home/policies/data-classification/classification-overview)
- [Data Protection and Security Policy](https://secure4.compliancebridge.com/uab/portal/getdoc.php?file=302)
- [Data Access Policy](https://secure4.compliancebridge.com/uab/portal/getdoc.php?file=301)
- [HIPAA Data Policy](https://www.uab.edu/it/home/policies/compliance/hipaa)

<!-- markdownlint-disable MD046 -->
!!! important

    It is the responsibility of researchers to make sure PHI is accessible _only_ to people on the relevant IRB, with a demonstrated need to know. If PHI is stored in a project directory where some researchers are not on the IRB, their access to those files should be restricted using Access Control Lists (ACLs). Access control should be planned in advance of moving PHI data to Cheaha. If you need assistance setting up ACLs properly, please contact [Support](../help/support.md).
<!-- markdownlint-enable MD046 -->

Managing PHI data can be challenging. There are experts on Campus who can provide assistance. Please contact [Support](../help/support.md) if you intend to use Research Computing services in combination with PHI and PHI-derived data.

### Scratch Retention Policy

Data stored in `/scratch` is subject to two limited retention policies.

- Each user will have a quota of 50 TB of scratch storage.
- Files will be retained for a maximum of 30 days, after which they become eligible for deletion.
