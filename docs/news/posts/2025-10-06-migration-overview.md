---
date: 2025-10-06T12:00:00-05:00
categories:
    - Maintenance
---

# Cheaha Data Migration

## User Impact Summary

- All user and project data will be migrated to a new storage systems on a rolling basis over the coming weeks
- Users will receive two day notice before their account is migrated
- During migration, user accounts will be placed on hold preventing access. All queued and running jobs will be requeued and held
- The migration window is **2 days**. Please plan for your account to remain on hold for the duration. We hope to complete migrations prior to the end of this window and will remove account holds as soon as migrations are complete.
- Once migration is complete, account certification will be required through the [web portal](https://rc.uab.edu).
- Wait times for jobs are expected to increase during the migration. Please see our [expected impact](#effects-on-queue-times) for more details.

<!-- more -->

## Potential Sections of Interest

- [Migraton Procedure](#migration-procedure)
- [General Timeline](#general-timeline)
- [Summary of Available Compute During the Migration](#gpfs-5-compute-nodes)
- [Impact on Job Wait Times](#effects-on-queue-times)
- [Changes to Scratch](#scratch)

## Overview

Research Computing will be performing a data migration for all data on Cheaha from our current GPFS 4 storage system to our new GPFS 5 storage system over the coming weeks. This migration is necessary due to GPFS 4 reaching end-of-life, and the physical hardware and vendor support to increase storage capacity on GPFS 4 does not exist. The new GPFS 5 storage system will support future upgrades and planned growth for Cheaha. This is a large-scale migration covering 1.3 billion files and 4.7 petabytes of data. To facilitate a migration of this size, we developed a more flexible, phased process to avoid an extended cluster shutdown for all user simultaneously. This page is to provide you with technical information covering the migration plan, our rationale behind certain decisions, and how your account will be affected pre- and post-migration.

### Batching Accounts Into Communities

In order to reliably move user data during the migration, it's imperative that those data are unchanging. We have weighed the available options and decided against a whole-cluster shutdown due to estimate downtime. Instead, we have split the Cheaha userbase into a number of **communities** (batches) based on shared access to project spaces. This means for each project space, to the best of our ability, we will be migrating every member of that project at the same time. Our goal is to minimize both individual account downtime as well as overall migration time while making sure each researcher has access to the data they need pre- and post-migration.

<!-- markdownlint-disable MD046 -->
!!! important

    It was not possible to make sure all users were transferred with all of their projects while also keeping community sizes manageable. We have minimized the number of people this affects as much as possible. We will notify users if they are part of groups being migrated in a different community than their projects when that occurs.
<!-- markdownlint-enable MD046 -->

## Migration Procedure

Each community, or batch of user groups, should expect the following procedure when it is their turn to migrate.

1. **Notice of Pending Migration**
    1. Two days prior to migration, each user in a given community will receive a notification via email.
    1. The email will include the list of projects being migrated in that batch for each user's reference.

1. **Access Restriction During Migration**
    1. At 00:00 of the date specified in the notice email, all accounts in a batch will be placed on hold and access to Cheaha will be disabled
    1. All jobs for these accounts will be requeued if they are running and placed on hold.
        1. Requeued jobs are essentially cancelled and resubmitted to queue under the same Job ID. **These jobs start from the beginning of the submitted script**.
    1. After migration, each account will require certification by going to our [web portal](https://rc.uab.edu). You will not be able to access Cheaha until your account has been certified.

    <!--markdownlint-disable MD046 -->
    !!! note

        The certification step is part of a new annual process we are adopting to ensure cluster resources are associated only with active, valid accounts. This will improve system security and ensure compliance with expectations, responsibilities, and policies. Part of the review process is confirming each researcher intends to continue using RCS services
    <!--markdownlint-enable MD046 -->

1. **Migration Schedule**
    1. Plan to lose access to Cheaha for up to **2 days** during migration.
    1. Accounts will be immediately released from hold once migration completes, and the next community will receive their notice for pending migration.
        1. Due to potential for high variability in migration duration for each community, we cannot provide set dates for each community's migration. The migration will be performed as safely and quickly as possible.
    1. Migrations will continue as possible over all necessary weekends.

1. **Post-Migration Activity**
    1. After migration for a batch ends, held jobs will be released back into queue.
    1. Compute node availability differs between GPFS 4 and GPFS 5. See our [compute node](#gpfs-5-compute-nodes) section for more details.
        1. Compute availability will affect expected wait times for jobs during the migration, especially for GPU compute.

### General Timeline

As explained above, the migration can be thought of as a series of, at most, 4-day windows. Each window will see one or more community migration(s) performed from start to finish.

1. Day 0: Community members receive an email notifying them of their impending migration
1. Day 2: Community members are put on hold access to Cheaha suspended
1. Day 2-4: Access to Cheaha is restored post-migration
1. Repeat for the next community

Due to high variability in file structure and content across users and communities, it's not feasible to predict how long any given community's migration will take. Therefore, we cannot give expected dates for when a given group's migration will begin and end as it's solely dependent on migrations of prior groups. Here are some dates to remember though:

- **Tuesday, October 7**: Initial announcement concerning the migration is sent to the Cheaha userbase
- **Thursday, October 9**: Notification of impending migration sent to members of community 1
- **Saturday, October 11**: Migration for community 1 begins

The migration will proceed through our predefined communities continuously until finished. Beyond the dates given, we cannot predict when each community will be transferred. The full migration is expected to last through the end of October.

## GPFS 5 Data Tiering

To effectively manage growing storage needs while controlling the costs associated with high-performance storage, our upgrade to GPFS 5 introduces a new data tiering strategy. Tiering is not visible to the user and requires no adjustments to user workflows on Cheaha. These details on the tiering architecture are informational only and do not require any awareness or action by the user. GPFS will remain the parallel storage system for Cheaha continuing to provide high-performance access for all active files. Inactive files, defined as those not accessed within a set period (currently over one year since last access), will have their content transparently migrated to a backing storage tier provided by CephFS. This process reduces storage pressure on GPFS by freeing up capacity, while leaving a file stub containing all relevant metadata behind on GPFS. This stub makes the file appear to the user as if it's still on GPFS, and reading the file will automatically and transparently transfer the content back from CephFS to GPFS for active use. This flexible tiering approach allows for balanced storage use based on performance needs and application use cases.

### What GPFS Tiering IS NOT

1. **Tiering is NOT a replacement for LTS**.
    1. Data you know you will not use for an extended period of time should be moved to [LTS](../../data_management/lts/index.md).
    1. Storage quotas will be enforced regardless of a given file's storage tier. This means for a standard project quota, only 25 TiB can be stored in a project across both GPFS and Ceph.
1. **Tiering is NOT a backup**
    1. A file's data will only exist on one tier, CephFS or GPFS, **never on both**.
    1. If a file reaches the age limit, its data is automatically moved from GPFS to Ceph leaving behind a stub containing only file metadata.
    1. When reading a file stub on GPFS, its data is moved from Ceph to GPFS leaving nothing on Ceph.
1. **Tiering is NOT high performance storage for analysis**
    1. Ceph only stores data deemed to be inactive on Cheaha.
1. **Tiering is NOT something users will interact with**
    1. Users will never make direct contact with Ceph. All of this is purely informational and provides background to some changes and behavior explained below.
    1. All data transfer to and from Ceph is done transparently, without any direct action from the user. Do not change how you interact with Cheaha on account of this tiered storage.

<!-- markdownlint-disable MD046 -->
!!! critical

    It is imperative to understand that tiered storage does not equal a backup. We do not provide a traditional, automatic backup for data stored on Cheaha. All data are erasure-encoded in case of hardware failure, they are not backed up in case of user error. Please see information about [LTS](../../data_management/lts/index.md) for a potential backup solution.
<!-- markdownlint-enable MD046 -->

### What CephFS IS

1. Cost-efficient, expandable storage on Cheaha.
    1. Increasing GPFS storage capacity is cost-prohibitive and has severely limited our ability to grant increases to project space quotas.
    1. CephFS provides a **FUTURE** avenue for expandable storage. **This is not currently an option**. More details will be provided as these services develop.
1. Tunable data sink
    1. With Ceph, we are able to tune which files are offloaded from GPFS based on user behavior and activity without interfering with ongoing analysis or burdening the researcher with quickly moving data to another storage system.
    1. This allows us a powerful option to address potential GPFS storage constraints that has not been available previously.

### Tiered Storage Summary

In summary, **users should not take tiered storage into account when using Cheaha**.

- There will be no changes in user experience when traversing a directory tree. Active and inactive files will appear as ordinary files from the user's perspective.
- Slight delays when fetching old data should be expected as the data is migrated from Ceph to GPFS. See the section on [initial interaction with files](#initial-interaction-with-files)
- Tiered storage is NOT back-up storage
- Tiered storage IS a new tool to improve storage demands on Cheaha.
- See notes on [quotas](#quotas) below

## GPFS 5 Notes Post-Migration

### Initial Interaction With Files

After migration to GPFS 5, loading a given file may take longer than expected during the initial read but will return to normal for all subsequent reads. This is expected post-migration behavior of our new tiered file system compared to our GPFS 4 system. This may be especially evident during startup of interactive apps from the web portal and during activation and use of virtual environments such as `conda` due to the large number of files these tools use.

Please be patient when starting an app such as Jupyter Notebook or reading an especially large file for the first time post-migration due to the delay caused by initial file reads.

For workflows operating on existing, large files (i.e. >= 10 GiB) after migration, please [contact support](../../index.md#how-to-contact-us) for potential optimizations. This can include pre-migrating data to GPFS prior to starting these workflows.

### Jobs Requeued Prior to Migration

As mentioned in the [migration procedure](#migration-procedure), jobs running at the time accounts are put on hold will be requeued and held. This is not a pause, it is essentially a resubmission of that job under the same job ID. For most software, jobs restarting like this will not pose issues. The job will start from the beginning of the script and either perform the same tasks as previously until reaching the end or will continue from where it left off if the tool being used has that as an option and the script has accounted for it (rare across all software, see machine learning checkpointing as an example).

Some software have checks built-in to make sure previously generated data are not being overwritten accidentally. If these software detect some amount of standard outputs already exist, they may fail as opposed to overwriting the existing data. As example of this is the MRI analysis software FreeSurfer. This is a hazard when requeueing running jobs which will immediately cancel any command being run in the job and exit. Once you have been notified of your migration time, please be cognizant of potential effects of requeuing your planned jobs if you're not certain they will finish before the migration begins.

### GPFS 5 Compute Nodes

Compute nodes are only able to run jobs from one of GPFS 4 or GPFS 5 so compute power has been split between the two storage systems. Due to hardware configuration constraints, some changes were made to the partitions on GPFS 5 that could potentially impact jobs.

**Current GPFS 5 Compute Capacity Pre-Migration**:

| Partition | Available Nodes | Notes |
|---|---|---|
| mainline | 20 (2560 cores) | Include AMD CPUs. See the [list of changes](#changes-to-mainline-partitions) for details |
| pascalnodes | 0 | All pascalnodes will be moved during the 1st compute migration |
| amperenodes | 5 (10 A100s) | 10 amperenodes will be added during the 1st compute migration with the remaining 5 added once the migration completes |
| amperenodes-medium | 1 (2 A100s) | Nodes will be added to the amperenodes-medium partition during both compute migrations |
| largemem | 0 | largemem and largmem-long nodes will remain on GPFS 4 until the full migration completes. If you require access to the 1.5 TiB RAM nodes, contact support |

#### Changes to Mainline Partitions

On GPFS 4, all nodes in the interactive/express/short/medium/long (mainline) partitions have Intel processors while the `amd-hdr100` nodes have AMD processors. On GPFS 5, the mainline partitions use nodes that were previously migrated from the `amd-hdr100` partition and so now use AMD CPUs.

In rare cases, tools compiled on on Intel processor can cause `Illegal Instruction` errors when run on AMD CPUs. If your jobs were submitted to one of the mainline partitions and show this error after migration, please [contact support](../../index.md#how-to-contact-us). As the migration continues, the standard Intel nodes will also be migrated from GPFS 4 to GPFS 5 and added to the mainline partitions.

Once the migration is complete, the partitions will return to their current configuration separating AMD nodes into separate partitions from Intel nodes.

#### Compute Migration

To best accomodate workload for both migrated and not-yet-migrated users, compute capacity will be moved from GPFS4 to GPFS5 in two stages: at 50% and 100% user migration progress. Due to hardware networking and rack constraints, we have limited options as far as which nodes we can move at which times. See below for a list of which nodes will be migrated to GPFS 5 at which time.

**50% Migration Completion**:

- All pascalnodes (18 total nodes on GPFS 5, 72 available P100s)
- 10 amperenodes (15 total on GPFS 5, 30 available A100s)

**100% Migration Completion**:

- 5 amperenodes (20 total on GPFS 5)
- All largemem nodes (14 total on GPFS 5)

#### Effects on Queue Times

During the migration, be aware that job wait times are expected to increase based on when you are migrated relative to the [compute migration](#compute-migration). For instance, users migrated prior to the initial compute migration will experience longer wait times due to initially lower compute capacity on GPFS 5 while users still on GPFS 4 will experience somewhat reduced wait times due to fewer jobs competing for resources on that platform. This will flip after the initial compute migration where users on GPFS 5 will have reduced wait times from the influx of compute nodes, and users on GPFS 4 will have longer wait times.

**This will be especially apparent for jobs on pascalnodes and amperenodes.** Prior to the initial compute migration, there will be a 100%:0% split of pascalnodes and 75%:25% split of amperenodes on GPFS4 and GPFS 5, respectively. After the initial compute migration, the splits will be 0%:100% for pascalnodes and 25%:75% for amperenodes on GPFS 4 and GPFS 5, respectively. We understand this will have a large impact on job throughput for individual users and will endeavor to complete the migration swiftly to prevent undue burden on our community. Thank you for understanding.

### Quotas

Existing quotas on project spaces have not been altered as part of the migration in order to smoothly accommodate existing data. Quotas will be enforced as the sum of storage used across both GPFS and CephFS. Future changes to quotas will be communicated when appropriate.

### Scratch

Network scratch space (`/scratch`) will have a couple of major changes moving forward

1. Total `/scratch` capacity will be reduced from 800 TiB to **500 TiB** for all users. This is a consequence of a necessary reduction in total GPFS capacity.
1. Scratch policies regarding old data will be enforced. Files older than 30 days will be automatically offloaded for deletion.
1. Scratch does not obey the same tiered storage principles as explained in the [data tiering](#gpfs-5-data-tiering) section. Data offloaded from scratch due to age will be subject to deletion as opposed to indefinite storage on Ceph.

Please be cognizant of these changes moving forward and remember that `/scratch` is a shared storage space that is limited by total capacity. We will continue to adjust scratch policies based on application usage and performance requirements.
