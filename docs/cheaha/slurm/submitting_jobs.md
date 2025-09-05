# Submitting Jobs With Slurm

Processing computational tasks with Cheaha at the terminal requires submitting jobs to the Slurm scheduler. Slurm offers two commands to submit jobs: `sbatch` and `srun`. Always use `sbatch` to submit jobs to the scheduler, unless you need an [interactive terminal](#interactive-jobs-with-srun). Otherwise only use `srun` within `sbatch` for submitting job steps within an [`sbatch` script](#batch-jobs-with-sbatch) context.

The command `sbatch` accepts script files as input. Scripts should be written in an available shell language on Cheaha, typically bash, and should include the appropriate Slurm directives at the top of the script telling the scheduler the requested resources. Read on to learn more about how to use Slurm effectively.

<!-- markdownlint-disable MD046 -->
!!! important

    Much of the information and examples on this page require a working knowledge of terminal commands and the shell. If you are unfamiliar with the terminal then please see our [Shell page](../../workflow_solutions/shell.md) for more information and educational resources.
<!-- markdownlint-enable MD046 -->

## Common Slurm Terminology

- Node: A self-contained computing devices, forming the basic unit of the cluster. A node has multiple CPUs, memory, and some have GPUs. Jobs requiring multiple nodes must use a protocol such as MPI to communicate between them.
    - Login nodes: Gateway for reseacher access to computing resources, shared among all users. **DO NOT** run research computation tasks on the login node.
    - Compute nodes: Dedicated nodes for running research computation tasks.
- Core: A single unit of computational processing, not to be confused with a CPU, which may have many cores.
- Partition: A logical subset of nodes sharing computational features. Different partitions have different resource limits, priorities, and hardware.
- Job: A collection of commands that require computational resources to perform. Can be interactive with `srun` or submitted to the scheduler with `srun` or `sbatch`.
- Batch Job: An array of jobs which all have the same plan for execution, but may vary in terms of input and output. Only available in non-interactive batch mode via `sbatch`
- Job ID: The unique number representing the job, returned by `srun` and `sbatch`. Stored in `$SLURM_JOB_ID` within a job.
- Job Index Number: For array jobs, the index of the currently running job within the array. Stored in `$SLURM_ARRAY_TASK_ID` within a job.

## Slurm Flags and Environment Variables

Slurm has many flags a researcher can use when creating a job, but a short list of the most important ones for are described below. It is highly recommended to be as explicit as possible with flags and not rely on system defaults. Explicitly using the flags below makes your scripts more portable, shareable and reproducible.

{{ read_csv('cheaha/res/job_submit_flags.csv', keep_default_na=False) }}

### Available Partitions for `--partition`

Please see [Cheaha Hardware](../hardware.md#summary) for more information. Remember, the smaller your resource request, the sooner your job will get through the queue.

### Requesting GPUs

Please see the [GPUs page](gpu.md) for more information. Take note that you'll need to take special care of how you submit GPU jobs to maximize performance. See our [Making the Most of GPUs Section](./gpu.md#making-the-most-of-gpus)

See our [GPU Jobs Tutorial](./slurm_tutorial.md#example-6-gpu-jobs) for an introduction.

### Dynamic `--output` and `--error` File Names

The `--output` and `--error` flags can use dynamic job information as part of the name:

- `%j` is the Job ID, equal to `$SLURM_JOB_ID`.
- `%A` is the main Array Job ID, equal to `$SLURM_ARRAY_JOB_ID`.
- `%a` is the Array job index number, equal to `$SLURM_ARRAY_TASK_ID`.
- `%x` is the `--job-name`, equal to `$SLURM_JOB_NAME`.

For example if using `--job-name=my-job`, then to create an output file like `my-job-12345678` use `--output=%x-%j`.

If also using `--array=0-4`, then to create an output file like `my-job-12345678-0` use `--output=%x-%A-%a`.

## Batch Jobs With `sbatch`

<!-- markdownlint-disable MD046 -->
!!! important

    The following examples assume familiarity with the Linux terminal. If you are unfamiliar with the terminal then please see our [Shell page](../../workflow_solutions/shell.md) for more information and educational resources.
<!-- markdownlint-enable MD046 -->

Batch jobs are typically submitted using scripts with `sbatch`. Using `sbatch` this way is the preferred method for submitting jobs to Slurm on Cheaha. It is more portable, shareable, reproducible and scripts can be version controlled using [Git](../../workflow_solutions/git_collaboration.md).

For batch jobs, flags are typically included as directive comments at the top of the script like `#SBATCH --job-name=my-job`. Read on to see examples of batch jobs using `sbatch`.

### A Simple Batch Job

Below is an example batch job script. To test it, copy and paste it into a plain text file `testjob.sh` in your [Home Directory](../../data_management/cheaha_storage_gpfs/individual_directories.md#home-and-user-data-directories) on Cheaha. Run it at the terminal by navigating to your home directory by entering `cd ~` and then entering `sbatch testjob.sh`. Momentarily, two text files with `.out` and `.err` suffixes will be produced in your home directory.

```bash linenums="1"
#!/bin/bash
#
#SBATCH --job-name=test
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=1G
#SBATCH --partition=express
#SBATCH --time=00:10:00
#SBATCH --output=%x_%j.out
#SBATCH --error=%x_%j.err

echo "Hello World"
echo "Hello Error" 1>&2
```

There is a lot going on in the above script, so let's break it down. There are three main chunks of this script:

1. Line 1 is the interpreter directive: `#!/bin/bash`. This tells the shell what application to use to execute this script. All `sbatch` scripts on Cheaha should start with this line.
1. Lines 3-11 are the [`sbatch` flags](#slurm-flags-and-environment-variables) which tell the scheduler what resources you need and how to manage your job.

    - Line 3: The job name is `test`.
    - Lines 4-7: The job will have 1 node, with 1 core and 1 GB of memory.
    - Line 8: The job will be on the express partition.
    - Line 9: The job will be no longer than 10 minutes, and will be terminated if it runs over.
    - Line 10: Any standard output (`stdout`) will be written to the file `test_$SLURM_JOB_ID.out` in the same directory as the script, whatever the `$SLURM_JOB_ID` happens to be when the job is submitted. The name comes from `%x` equal to `test`, the `--job-name`, and `%j` equal to the Job ID.
    - Line 11: Any error output (`stderr`) will be written to a different file `test_$SLURM_JOB_ID.err` in the same directory.

1. Lines 13 and 14 are the payload, or tasks to be run. They will be executed in order from top to bottom just like any shell script. In this case, it is simply writing "Hello World" to the `--output` file and "Hello Error" to the `--error` file. The `1>&2` Means redirect a copy (`>&`) of `stdout` to `stderr`.

### Batch Array Jobs With Known Indices

Building on the job script above, below is an array job. Array jobs are useful when you need to perform the same analysis on slightly different inputs with no interaction between those analyses. We call this situation "pleasingly parallel". We can take advantage of an array job using the variable `$SLURM_ARRAY_TASK_ID`, which will have an integer in the set of values we give to the `--array` flag.

To test the script below, copy and paste it into a plain text file `testarrayjob.sh` in your [Home Directory](../../data_management/cheaha_storage_gpfs/individual_directories.md#home-and-user-data-directories) on Cheaha. Run it at the terminal by navigating to your home directory by entering `cd ~` and then entering `sbatch testarrayjob.sh`. Momentarily, 16 text files with `.out` and `.err` suffixes will be produced in your home directory.

```bash linenums="1"
#!/bin/bash
#
#SBATCH --job-name=test
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=1G
#SBATCH --partition=express
#SBATCH --time=00:10:00
#SBATCH --output=%x_%A_%a.out
#SBATCH --error=%x_%A_%a.err
#SBATCH --array=0-9

echo "My SLURM_ARRAY_TASK_ID: " $SLURM_ARRAY_TASK_ID
```

This script is very similar to the one above, but will submit 10 jobs to the scheduler that all do slightly different things. Each of the 10 jobs will have the same amount and type of resources allocated, and can run in parallel. The 10 jobs come from `--array=0-9`. The output of each job will be one of the numbers in the set `{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}`, depending on which job is running. The output files will look like `test_$(SLURM_ARRAY_JOB_ID)_$(SLURM_ARRAY_TASK_ID).out` or `.err`. The value of `$(SLURM_ARRAY_JOB_ID)` is the main Job ID given to the entire array submission.

Scripts can be written to take advantage of the `$SLURM_ARRAY_TASK_ID` variable indexing variable. For example, a project could have a list of participants that should be processed in the same way, and the analysis script uses the array task ID as an index to pull out one entry from that list for each job. Many common programming languages can interact with shell variables like `$SLURM_ARRAY_TASK_ID`, or the values can be passed to a program as an argument.

You can override the `--array` flag stored in the script when you call `sbatch`. To do so, pass another `--array` flag along with the script name like below. This allows you to rerun only subsets of your array script.

``` bash
# submit jobs with index 0, 3, and 7
sbatch --array=0,3,7 array.sh

# submit jobs with index 0, 2, 4, and 6
sbatch --array=0-6:2 array.sh
```

For more details on using `sbatch` please see the [official documentation](https://slurm.schedmd.com/sbatch.html).

<!-- markdownlint-disable MD046 -->
!!! note

    If you are using bash or shell arrays, it is crucial to note they use 0-based indexing. Plan your `--array` flag indices accordingly.
<!-- markdownlint-enable MD046 -->

#### Throttling in Slurm Array Jobs

Throttling in Slurm array jobs refers to limiting the number of concurrent jobs that can run simultaneously. This approach prevents the overloading of computing resources and ensures fair distribution of resources among users. From a performance perspective, throttling helps optimize overall job performance by reducing resource contention across the Cheaha cluster. When too many jobs run at the same time, they may compete for CPU, memory, or I/O, which can negatively impact performance. Please [contact us](../../index.md#how-to-contact-us) if your research needs exceed our capacity.

To limit the number of concurrent jobs in a Slurm array, you can use the `%` separator. Here’s how to use it in the above example:

```bash
sbatch --array=0-9%4 job.sh
```

In this example, only 4 jobs will run concurrently, regardless of the total number of jobs (10) in the array.

### Batch Array Jobs With Dynamic or Computed Indices

For a practical example with dynamic indices, please visit our [Practical `sbatch` Examples](practical_sbatch.md)

## Interactive Jobs With `srun`

Jobs should be submitted to the Slurm job scheduler either using a [batch job](#batch-jobs-with-sbatch) or an [Open OnDemand (OOD) interactive job](../open_ondemand/index.md).

You can use `srun` for working on short interactive tasks such as [creating an Anaconda environment](../../workflow_solutions/using_anaconda.md) and running [parallel tasks](#srun-for-running-parallel-jobs) within an sbatch script.

<!-- markdownlint-disable MD046 -->
!!! warning

    The limitations of `srun` is that the jobs/execution die if the internet connection is down, and you may have to rerun the job again.

    We recommend against using `srun` for any scientific or research computing or data analysis. Use a [batch job](#batch-jobs-with-sbatch) or an [Open OnDemand (OOD) interactive job](../open_ondemand/index.md) instead.
<!-- markdownlint-disable MD046 -->

Let us see how to acquire a compute node quickly using `srun`. You can run interactive job using `srun` command with the `--pty /bin/bash` flag. Here is an example,

```bash
$srun --ntasks=2 --time=01:00:00 --mem-per-cpu=8G --partition=medium --job-name=test_srun --pty /bin/bash

srun: job 21648044 queued and waiting for resources
srun: job 21648044 has been allocated resources
```

The above example allocates a compute node with a 8GB of RAM on a `medium` partition with `--ntasks=2` to run short tasks.

### `srun` for Running Parallel Jobs

`srun` is used to run executables in parallel, and is used within `sbatch` script. Let us see an example where `srun` is used to launch multiple (parallel) instances of a job.

```bash
#!/bin/bash
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=1
#SBATCH --job-name=srun_test
#SBATCH --partition=long
#SBATCH --time=05:00
#SBATCH --mem=4G

srun hostname
```

In the script above, we have asked for two nodes --nodes=2, and each node will run a single instance of a `hostname` as we requested --ntasks-per-node=1. The output for the above script is,

```bash
c0187
c0188
```

Here is another example of running different independent programs simultaneously on different resources within a batch job. Multiple `srun` can execute simultaneously as long as they do not exceed the resources reserved for that job i.e., step 1 executes in node 1 with --ntasks=4, and step 2 executes in node 2 with --ntasks=4 simultaneously. Note that `--nodes=1 -r1` in step 2 defines the number of nodes and their relative node position within the resources assigned to the job.

```bash
#!/bin/bash
#SBATCH --nodes=2
#SBATCH --ntasks=8
#SBATCH --ntasks-per-node=4
#SBATCH --cpus-per-task=1
#SBATCH --partition=amd-hdr100
#SBATCH --time=05:00
#SBATCH --mem-per-cpu=1G

#Partioning of resources for two different tasks
#STEP 1
srun --nodes=1 --ntasks=4 hostname
#STEP 2
srun --nodes=1 -r1 --ntasks=4 uname -a
```

Here is the output for running multiple `srun` in a single job, i.e., executing the `hostname` and `uname -a` tasks simultaneously but on different nodes.

```bash
c0203
c0203
c0203
c0203
Linux c0204 3.10.0-1160.24.1.el7.x86_64 #1 SMP Thu Mar 25 21:21:56 UTC 2021 x86_64 x86_64 x86_64 GNU/Linux
Linux c0204 3.10.0-1160.24.1.el7.x86_64 #1 SMP Thu Mar 25 21:21:56 UTC 2021 x86_64 x86_64 x86_64 GNU/Linux
Linux c0204 3.10.0-1160.24.1.el7.x86_64 #1 SMP Thu Mar 25 21:21:56 UTC 2021 x86_64 x86_64 x86_64 GNU/Linux
Linux c0204 3.10.0-1160.24.1.el7.x86_64 #1 SMP Thu Mar 25 21:21:56 UTC 2021 x86_64 x86_64 x86_64 GNU/Linux
```

Alternatively, `srun` can also run MPI, OpenMP, hybrid MPI/OpenMP, and many more parallel jobs. For more details on using `srun`, please see the [official documentation](https://slurm.schedmd.com/srun.html).

<!-- markdownlint-disable MD046 -->
!!! important

    `srun` has been disabled for use with MPI. We have removed this functionality due to an open vulnerability: <https://nvd.nist.gov/vuln/detail/CVE-2023-41915>. The vulnerability could allow an attacker to escalate privileges to root and/or access data they do not have permissions for.

    Instead of `srun`, please load one of the `OpenMPI` modules with an appropriate version. Please contact [Support](../../help/support.md) with any questions or concerns.
<!-- markdownlint-enable MD046 -->

## Environment Setup and Module Usage in Job Submission

Before submitting a job using `sbatch`, it's crucial to establish a tailored environment, including software installations and loading necessary modules containing the required software packages. We highly recommend the practice of putting `module reset` before any `module load` calls in job scripts. The module system modifies the environment whenever the module list changes, and Slurm jobs inherit the environment from whatever called `sbatch` or `srun`. The module reset command normalizes the initial environment for the script, improving repeatability and minimizing the risk of hard-to-diagnose module conflicts. For examples and further information, please see [best practice for loading modules](../software/modules.md#best-practice-for-loading-modules).

## Graphical Interactive Jobs

It is highly recommended to use the [Open OnDemand](../open_ondemand/index.md) web portal for [interactive apps](../open_ondemand/ood_layout.md#interactive-apps). Interactive sessions for certain software such as MATLAB and RStudio can be created directly from the browser while an HPC Desktop is available to access all of the other software on Cheaha. A terminal is also available through Open OnDemand.

It is possible to use other remote desktop software, such as VNC, to start and interact with jobs. These methods are not officially supported and we do not have the capacity to help with remote desktop connections. Instead, please consider switching your workflow to use the [Open OnDemand HPC Desktop](../open_ondemand/hpc_desktop.md). If you are unable to use this method, please contact [Support](../../help/support.md).

## Estimating Compute Resources

Being able to estimate how many resources a job will need is critical. Requesting many more resources than necessary bottlenecks the cluster by reserving unused resources for an inefficient job preventing other jobs from using them. However, requesting too few resources will slow down the job or cause it to error.

Questions to ask yourself when requesting job resources:

1. Can my scripts take advantage of multiple CPUs?
    1. For instance, RStudio generally works on a single thread. Requesting more than 1 CPU here would not improve performance.
1. How large is the data I'm working with?
1. Do my pipelines keep large amounts of data in memory?
1. How long should my job take?
    1. For example, do not request 50 hours time for a 15 hour process. Have a reasonable buffer included to account for unexpected processing delays, but do not request the maximum time on a partition if that's unnecessary.

<!-- markdownlint-disable MD046 -->
!!! note

    Reasonable overestimation of resources is better than underestimation. However, gross overestimation may cause admins to contact you about adjusting resources for future jobs.
<!-- markdownlint-enable MD046 -->

To get the most out of your Cheaha experience and ensure your jobs get through the queue as fast as possible, please read about [Job Efficiency](../job_efficiency.md).

## Faster Queuing With Job Efficiency

Please see our page on [Job Efficiency](../job_efficiency.md) for more information on making the best use of cluster resources to minimize your queue wait times.
