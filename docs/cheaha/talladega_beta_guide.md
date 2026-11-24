# Cheaha beta (Talladega) user guide

Changes from Cheaha for closed beta testers | 17 November 2026

> **Tidbit:** The Talladega Mountain Range contains Cheaha Mountain as well as Hernandez Peak, the two tallest locations in the state of Alabama.

<!-- markdownlint-disable MD046 -->
!!! important
    This document refers to the beta deployment of UAB’s HPC as **Talladega** and to the live production deployment as **Cheaha**. Once the beta period ends and the full user migration takes place, UAB’s HPC will reassume the Cheaha name.
<!-- markdownlint-enable MD046 -->

<!-- markdownlint-disable MD046 -->
!!! important
    This document will be updated throughout the beta as the configuration changes and we progress towards full production. While we will send out periodic notices regarding imminent breaking changes, this document will be updated to reflect the current state of Talladega during beta development.
<!-- markdownlint-enable MD046 -->

This guide covers the experience available when the Talladega beta opens. Continue using your existing Slurm workflows, with the script changes listed in [section 2](#2-update-existing-job-scripts). You will retain access to Cheaha throughout the beta.

## Contents

- [1. Cluster access and hardware](#1-cluster-access-and-hardware)
- [2. Update existing job scripts](#2-update-existing-job-scripts)
- [3. Software](#3-software)
- [4. Service](#4-service)

## 1. Cluster Access and Hardware

### Connect Through SSH

<!-- markdownlint-disable MD046 -->
!!! note
    Talladega access is through SSH only during the initial beta phase. Access through the web portal will be added in the next beta phase. Your username and SSH keys stay the same.
<!-- markdownlint-enable MD046 -->

Talladega is accessible from the UAB Campus Network as well as from Cheaha. Please follow the [UAB VPN instructions](https://www.uab.edu/it/home/tech-solutions/network/vpn) to connect to the UAB network from off-campus.

- **Talladega address:** `164.111.161.61`
- **Talladega hostname:** `talladega.rc.uab.edu`

The hostname for Talladega's login node is `login007`. Please make sure you're connected to the correct login node when trying to use either Talladega or Cheaha.

#### Example Connection From Local Machine

```bash
[username@local-machine ~]$ ssh blazerid@talladega.rc.uab.edu
```

#### Example Connection From Cheaha

```bash
# Initial connection to Cheaha
[username@local-machine ~]$ ssh blazerid@cheaha.rc.uab.edu

# Secondary connection to Talladega
[blazerid@login006 ~]$ ssh $USER@talladega.rc.uab.edu
```

### Interactive Jobs and Graphical Interfaces

Support for Open OnDemand (OOD) and interactive graphical (GUI) software will be provided in a future update.

All interactive jobs should be submitted using `srun --pty /bin/bash` along with the corresponding `srun` parameters. Submit batch jobs with `sbatch` as usual after making the modifications detailed in [section 2](#2-update-existing-job-scripts).

### The GPFS Filesystem Is Shared

GPFS paths are identical on both clusters. Both systems access the same filesystem, so file changes made through Talladega are immediately reflected on Cheaha, and vice versa. No data copy is needed between the two clusters for files already on GPFS.

This includes shared job scripts and environment files. Keep beta-specific copies where changes should not affect your Cheaha workflow.

For jobs that write temporary files, explicitly set the expected scratch location even though it remains the default:

```bash
export TMPDIR=/scratch/local
```

Node-local scratch is separate from shared GPFS storage. Continue using GPFS paths for data that needs to be accessible from both clusters.

### Current Beta Hardware

| Node class | Nodes | Cores per node | RAM per node | GPUs per node          |
| ---------- | ----- | -------------- | ------------ | ---------------------- |
| CPU only   | 9     | 128            | 512 GiB      | None                   |
| A100       | 1     | 128            | 512 GiB      | 2 × A100, 80 GiB each  |
| H200       | 4     | 192            | 1.5 TiB      | 8 × H200, 140 GiB each |

### Provisional Per-User Resource Limits

| Resource  | Total across your Talladega jobs |
| --------- | -------------------------------- |
| CPU cores | 264                              |
| Host RAM  | 3 TiB                            |
| H200 GPUs | 8                                |

These are provisional limits at the start of beta and will likely change before full migration. These limits apply only to Talladega. Cheaha and Talladega jobs do not count toward each other’s limits. Actual allocation also depends on available hardware.

## 2. Update Existing Job Scripts

Due to changes in our Slurm configuration, some updates to job scripts and Slurm commands may be necessary.

### Partition Automatically Assigned

To reduce complexity of job submissions, we have removed the need to specify a partition at job submission. Instead, the partition will be automatically determined by the resource request. Remove all partition specifications from your job script. Currently, jobs specifying a partition are rejected at submission time.

### Typed GPU Requests

Use either request style below, replacing `TYPE` with `a100` or `h200` and `COUNT` with the number of GPUs:

```bash
--gres=gpu:TYPE:COUNT  # GPUs per node
--gpus=TYPE:COUNT      # GPUs for the whole job
```

**Examples**:

- `--gres=gpu:a100:1` requests one A100 per node
- `--gpus=h200:2` requests two H200 GPUs across the job
    - Specify the node count in the job submission (i.e., `--nodes=1`) when using this parameter.

### Summary Table: Job Submission Changes

| Setting in your script or command       | Required beta change                                                                                                                                                        |
| --------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Partition selection                     | Remove `--partition`, `-p` and `#SBATCH` partition directives for every job. A supplied partition will be rejected at submission.                                           |
| Account selection                       | Remove `--account`, `-A` and `#SBATCH` account directives. The account is assigned automatically.                                                                           |
| GPU requests                            | Specify `a100` or `h200` and a count. Replace `pascal`, `ampere` and untyped GPU requests.                                                                                  |
| Hardware constraints and node selection | Remove old `--constraint`, `--nodelist` and `--exclude` settings. In particular, remove `--constraint=intel`; Talladega has no Intel CPUs and those jobs will not schedule. |
| Wall time                               | Set `--time` within the CPU or GPU maximum below.                                                                                                                           |

### Job Duration and Array Size

| Job type or setting       | Beta limit                                                            |
| ------------------------- | --------------------------------------------------------------------- |
| CPU job maximum wall time | 150 hours: `--time=6-06:00:00`                                        |
| GPU job maximum wall time | 48 hours: `--time=2-00:00:00`                                         |
| Array size setting        | Retained from Cheaha: `MaxArraySize=10001`, allowing indexes 0–10000. |

Max allowable walltime is now 150 hours (equivalent to Cheaha’s long partition) for all CPU-only jobs and 48 hours for all GPU jobs. Job priority will be affected by the requested time limit with shorter jobs receiving higher priority.

Please continue making realistic CPU, memory, and time requests.

## 3. Software

### Operating System Upgrade

Talladega runs Rocky Linux 9 instead of CentOS 7. The newer GLIBC allows native software installations that were blocked by the older GLIBC on Cheaha. If existing self-installed software has compatibility problems, its environment may need to be recreated.

### Software and Containers

Modules will not be available during the initial beta. Anaconda and Apptainer will be available by default on all compute nodes. Remove `module load` commands that depend on the Cheaha module system and use your existing Anaconda environment or container workflow.

Talladega now uses Apptainer as a drop-in replacement for Cheaha's SingularityCE. These software are closely related forks and share much if not all of the same functionality. The `singularity` command remains available as a symlink to the `apptainer` binary so existing container commands should continue to work. Existing Singularity images and Anaconda environments are expected to work as-is. Report unexpected container behavior; recreate a self-installed environment if compatibility issues require it.

### Queue and Accounting Output

All users will belong to the base account `users`. The `Account` field in `squeue` or `sacct` will show `users` instead of your username; update any filters or scripts that depend on that field to `User`.

You will be able to see all jobs in the queue. Cheaha job history will not be available from Talladega during beta; query the Cheaha cluster for its historical jobs.

## 4. Service

### Service Interruptions and Support

This is a closed beta. Expect occasional service interruptions while configuration is finalized. The team will keep interruptions to a minimum. If planned work will affect pending or running jobs, we will notify all beta participants in advance with enough time to adjust any pending or planned jobs. Slurm policies and resource limits may change during beta; follow the current beta notices.

Report problems to [support@listserv.uab.edu](mailto:support@listserv.uab.edu). Include `[Talladega]` in the subject line, along with the job ID, relevant script or command, environment details and error output.
