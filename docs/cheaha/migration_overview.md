# Cheaha Data Migration

## User Impact Summary

- All user and project data will be migrated on a rolling basis over the coming weeks
- Users will receive two day notice before their account is migrated
- During migration, access to Cheaha will be revoked and all jobs will be requeued and held
- Plan to lose access to Cheaha for up to **2 days**
- Once migration is complete, account certification will be required through the [web portal](https://rc.uab.edu)

## Overview

Research Computing will be performing a cluster migration for all data on Cheaha from our current GPFS 4 storage system to our new GPFS 5 storage system over the coming weeks. This migration is necessary due to GPFS 4 reaching end-of-life and losing vendor support as well as allowing us to perform further, necessary upgrades to Cheaha over the coming months and years. This is a large scale migration covering [INSERT NUMBER OF FILES] files and [INSERT NUMBER OF PiB] petabytes of data, and so to facilitate a migration of this size, a more intricate process was necessary beyond a whole-cluster shutdown and move. This page is to provide you with information covering the migration plan, our rationale behind certain decisions, and how your account will be affected pre- and post-migration.

### Batching Accounts into Communities

In order to reliably replicate user data during the migration, it's imperative that those data are quiescent. While a whole-cluster shutdown would address that, the estimated downtime would be overly burdensome to all researchers. Instead, we have split the Cheaha userbase into a number of communities (batches) based on shared access to project spaces. This means for each project space, to the best of our ability, we will be migrating every member of that project at the same time. Our goal is to minimize both individual account downtime as well as overall migration time while making sure each researcher has access to the data they need pre- and post-migration.

<!-- markdownlint-disable MD046 -->
!!! important
    It was not possible to make sure all users were transferred with all of their projects while also keeping community sizes manageable. We have minimized the number of people this affects as much as possible. We will notify users if they are part of groups being migrated in a different community when that occurs.
<!-- markdownlint-enable MD046 -->

## Migration Procedure

The following procedure is performed on a **per-community** basis.

1. **Notice of Pending Migration**
    1. Two days prior to migration, each user in a given community will receive a notification via email.
    1. The email will include the list of projects being migrated in that batch for each user's reference.

1. **Access Restriction During Migration**
    1. At 00:00 of the date specified in the notice email, all accounts in a batch will be placed on hold and access to Cheaha will be revoked
    1. All jobs for these accounts will be requeued if they are running and placed on hold.
        1. Requeued jobs are essentially cancelled and resubmitted to queue under the same Job ID. **These jobs start from the beginning of the submitted script**.
    1. After migration, each account will require certification by going to our [web portal](https://rc.uab.edu). You will not be able to access Cheaha until your account has been certified.

1. **Migration Schedule**
    1. Plan to lose access to Cheaha for up to **2 days** during migration.
    1. If migration for a community completes earlier than expected, the next community will immediately receive a notice for pending migration starting their 2 day premigration clock.
        1. Due to potential for high variability in migration duration for each community, we cannot provide set dates for each community's migration. The migration will be performed as safely and quickly as possible.
    1. Migrations will continue as possible over all necessary weekends.

1. **Post-Migration Cleanup**
    1. After migration for a batch ends, held jobs will be released.
    1. Compute node availability differs between GPFS 4 and GPFS 5. See below for more details.

## GPFS 5 Notes Post-Migration

### Initial Interaction with Files

After migration to GPFS 5, loading a given file will be slow during the initial read but will return to normal for all subsequent reads. This is an expected behavior of our new tiered file system compared to our GPFS 4 system. This will be especially evident during startup of interactive apps from the web portal and during activation and use of virtual environments such as `conda` due to the large number of files these tools use. Please be patient when starting an app such as Jupyter Notebook or reading an especially large file for the first time post-migration due to the delay caused by initial file reads.

### GPFS 5 Compute Nodes

Compute nodes are only able to run jobs from one of GPFS 4 or GPFS 5 so compute power has been split between the two storage systems. Due to hardware configuration constraints, some changes were made to the partitions on GPFS 5 that could potentially impact jobs.

| Partition | Available Nodes | Notes |
|---|---|---|
| mainline | 20 (2560 cores) | Include AMD CPUs. See [below](#changes-to-mainline-partitions) for details |
| pascalnodes | 0 | All pascalnodes will be moved during the 1st compute migration |
| amperenodes | 5 (10 A100s) | 10 amperenodes will be added during the 1st compute migration with the remaining 5 added once the migration completes |
| amperenodes-medium | 1 (2 A100s) | Nodes will be added to the amperenodes-medium partition during both compute migrations |
| largemem | 0 | largemem and largmem-long nodes will remain on GPFS 4 until the full migration completes. If you require access to the 1.5 TiB RAM nodes, contact support |

#### Changes to Mainline Partitions

On GPFS 4, all nodes in the interactive/express/short/medium/long (mainline) partitions have Intel processors while the `amd-hdr100` nodes have AMD processors. On GPFS 5, the mainline partitions use nodes that were previously migrated from the `amd-hdr100` partition and so now use AMD CPUs.

In rare cases, tools compiled on on Intel processor can cause `Illegal Instruction` errors when run on AMD CPUs. If your jobs were submitted to one of the mainline partitions and show this error after migration, please [contact support](../index.md#how-to-contact-us). As the migration continues, the standard Intel nodes will also be migrated from GPFS 4 to GPFS 5 and added to the mainline partitions.

#### Compute Migration

To best accommodate workloads on both clusters during data migration, compute nodes will be migrated in two stages: at 50% and 100% data migration. Due to hardware networking and rack constraints, we have limited options as far as which nodes we can move at which times. See below for a list of which nodes will be migrated to GPFS 5 at which time.

**50% Migration Completion**:

- All pascalnodes (18 total nodes on GPFS 5, 72 available P100s)
- 10 amperenodes (15 total on GPFS 5, 30 available A100s)

**100% Migration Completion**:

- 5 amperenodes (20 total on GPFS 5)
- All largemem nodes (14 total on GPFS 5)

### Directory Paths

We have reorganized our GPFS 5 filesets to improve file access performance specifically for our network scratch space. As part of this, we have changed the `/data` drive to `/gpfs` and have brought `/scratch` under it.

**Path conversions from GPFS 4 to GPFS 5**:

- `/data/user` -> `/gpfs/user`
- `/data/user/home` -> `/gpfs/user/home`
- `/data/project` -> `/gpfs/project`
- `/scratch` -> `/gpfs/scratch`

In order to smooth the transition to GPFS 5, we have provided symlinks that mimic the GPFS 4 directory structure:

**GPFS 5 symlinks**:

- `/data` -> `/gpfs`
- `/scratch` -> `/gpfs/scratch`
- `/home` -> `/gpfs/user/home`

<!-- markdownlint-disable MD046 -->
!!! critical
    It is **not** necessary to immediately make changes to your paths in your scripts. The provided symlinks ensure backwards compatibility with GPFS 4 path structure in existing scripts in 99% of cases. Requeued and pending jobs submitted using GPFS 4 paths will not be impacted by these path changes.
<!-- markdownlint-enable MD046 -->

As you use GPFS 5, we suggest switching to the new path structure in your scripts as the symlinks will eventually be deprecated.
