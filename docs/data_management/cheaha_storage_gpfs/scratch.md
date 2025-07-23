# Scratch Directories

Scratch directories provide temporary, high-performance storage for data used in active computations. There are two types of scratch space:

- User Scratch: is available on login nod and also shared across compute nodes.
- Local scratch: is available only on individual compute nodes.

Scratch Directories are meant for short-term storage of intermediate or in progress data and should not be used for long-term retention.

<!-- markdownlint-disable MD046 -->
!!! important

    Starting January 2023, scratch data will have limited retention. See [Scratch Retention Policy](#policies-and-expectations) for more information.
<!-- markdownlint-enable MD046 -->

## User Scratch

All users have access to a large, temporary, work-in-progress directory for storing data, called a scratch directory in `/scratch/$USER` or `$USER_SCRATCH`. Use this directory to store very large datasets or temporary pipeline intermediates for a short period of time while running your jobs. The maximum amount of data a single user can store in network scratch is 100 TB at once.

Network scratch is available on the login node and each compute node. This storage is a GPFS high performance file system providing roughly 1 PB of storage. If using scratch, this should be your jobs' primary working directory, unless the job would benefit from local scratch (see below).

<!-- markdownlint-disable MD046 -->
!!! warning

    Research Computing expects each user to keep their scratch areas clean. **The cluster scratch areas are not to be used for archiving data.** In order to keep scratch clear and usable for everyone, files older than 30 days will be eligible for deletion.
<!-- markdownlint-enable MD046 -->

## Local Scratch

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

### What if My Data Won't Fit in Local Scratch?

Be sure that your files will fit in `/local/` before starting. You can determine disk size and current usage using `df -h | grep "local"`. Most nodes have 1.0 TB total capacity, while the `amperenodes` have 6.0 TB. If you data won't fit in the current usage, or on the drives, please [Contact Us](../../help/support.md). We can work with you to identify a solution.

### What if I Have a Large Amount of Data for Local Scratch?

If you have a large amount of data but each job takes very little time to run, performance can be further improved by avoiding frequent data copies and deletions. In these cases, preloading the data onto local scratch only once and then reusing it makes more sense. If this is the case for you, or you think you might benefit, please [Contact Us](../../help/support.md) and we can discuss creating a temporary node reservation to allow one-time data preloading.

## Policies and Expectations

Data stored in `/scratch` is subject to two limited retention policies.

- Each user will have a quota of 100 TB of scratch storage.
- Files will be retained for a maximum of 30 days, after which they become eligible for deletion.
