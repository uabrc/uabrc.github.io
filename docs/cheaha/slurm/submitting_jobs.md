# Submitting Jobs with Slurm

Slurm is simple to use to submit batch jobs. Scripts should be written in an available shell language on Cheaha, typically bash, and should include the appropriate Slurm directives at the top of the script telling the scheduler the requested resources. Common Slurm directives can be seen below along with simple examples for both single batch jobs and array batch jobs.

<!-- markdownlint-disable MD046 -->
!!! tip

    Please see our page on [Job Efficiency](../job_efficiency.md) for more information on making the best use of cluster resources and minimizing queue wait times.
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

## Slurm Flags

Slurm has many flags a researcher can use when creating a job, but a short list of the most important ones are listed here. It is highly recommended to explicitly use all of these flags in every job you submit.

1. `--job-name`: The name of your job to be stored in job accounting records and visible in `squeue`.
2. `--nodes`: The number of nodes a job needs. If your job does not require MPI, set this to `1`.
3. `--ntasks`: The number of tasks you plan to execute on each node, used mostly for bookkeeping and computing total cpus for each node. If unsure, set to `1`.
4. `--cpus-per-task`: The number of cores to request for each task. Total cpus fore each node equals `ntasks` times `cpus-per-task`.
5. `--partition`: The partition to submit the job to. Partition details can be seen below.
6. `--time`: Amount of time the job is estimated to run for. Acceptable time formats include `mm`, `mm:ss`, `hh:mm:ss`, `d-hh`, `d-hh:mm` and `d-hh:mm:ss`.
7. `--mem`: Amount of RAM in MB needed per node. Can specify 16 GB with either 16000 or 16G.
8. `--output`: Path to a file storing the text output of the job commands.
9. `--error`: Path to an output file if the script errors.
10. `--array`: A comma-separated list of array tasks to run. We will explain in more detail further down.

For batch jobs, directives are typically included as comments at the top of the script. See examples below. All batch jobs should be submitted using the `sbatch` command. All flags and more information on how to submit jobs can be seen using `man sbatch`. For a complete list, see [Slurm sbatch Documentation](https://slurm.schedmd.com/sbatch.html).

The `--output` and `--error` flags can use other information as part of the name:

- `%j` is the Job ID, equal to `$SLURM_JOB_ID`.
- `%A` is the main Array Job ID, equal to `$SLURM_ARRAY_JOB_ID`.
- `%a` is the Array job index number, equal to `$SLURM_ARRAY_TASK_ID`.
- `%x` is the `--job-name`, equal to `$SLURM_JOB_NAME`.

## Available Partitions for `--partition`

Please see [Partitions](../hardware.md#partitions) page for more information. Remember, the smaller your resource request, the sooner your job will get through the queue.

## A Batch Job with `sbatch`

Below is an example batch job script. To test it, copy and paste it into a plain text file `testjob.sh` in your [Home Directory](../../data_management/storage.md#home-directory) on Cheaha. Run it at the terminal by navigating to your home directory by entering `cd ~` and then entering `sbatch testjob.sh`. Momentarily, two text files with `.out` and `.err` suffixes will be produced in your home directory.

``` bash
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
2. Lines 3-11 are the [`sbatch` flags](#slurm-flags) which tell the scheduler what resources you need and how to manage your job.

    - Line 3: The job name is `test`.
    - Lines 4-7: The job will have 1 node, with 1 core and 1 GB of memory.
    - Line 8: The job will be on the express partition.
    - Line 9: The job will be no longer than 10 minutes, and will be terminated if it runs over.
    - Line 10: Any standard output (`stdout`) will be written to the file `test_$SLURM_JOB_ID.out` in the same directory as the script, whatever the `$SLURM_JOB_ID` happens to be when the job is submitted. The name comes from `%x` equal to `test`, the `--job-name`, and `%j` equal to the Job ID.
    - Line 11: Any error output (`stderr`) will be written to a different file `test_$SLURM_JOB_ID.err` in the same directory.

3. Lines 13 and 14 are the payload, or tasks to be run. They will be executed in order from top to bottom just like any shell script. In this case, it is simply writing "Hello World" to the `--output` file and "Hello Error" to the `--error` file. The `1>&2` Means redirect a copy (`>&`) of `stdout` to `stderr`.

## An Array Job with `sbatch`

Building on the job script above, below is an array job. Array jobs are useful when you need to perform the same analysis on slightly different inputs with no interaction between those analyses. We call this situation "pleasingly parallel". We can take advantage of an array job using the variable `$SLURM_ARRAY_TASK_ID`, which will have an integer in the set of values we give to the `--array` flag.

To test the script below, copy and paste it into a plain text file `testarrayjob.sh` in your [Home Directory](../../data_management/storage.md#home-directory) on Cheaha. Run it at the terminal by navigating to your home directory by entering `cd ~` and then entering `sbatch testarrayjob.sh`. Momentarily, 16 text files with `.out` and `.err` suffixes will be produced in your home directory.


``` bash
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
#SBATCH --array=0-5,7,9

echo "My SLURM_ARRAY_TASK_ID: " $SLURM_ARRAY_TASK_ID
```

This script is very similar to the one above, but will submit 8 jobs to the scheduler that all do slightly different things. Each of the 8 jobs will have the same amount and type of resources allocated, and can run in parallel. The 8 jobs come from `--array=0-7`. The output of each job will be one of the numbers in the set `{0, 1, 2, 3, 4, 5, 6, 7}`, depending on which job is running. The output files will look like `test_$(SLURM_ARRAY_JOB_ID)_$(SLURM_ARRAY_TASK_ID).out` or `.err`. The value of `$(SLURM_ARRAY_JOB_ID)` is the main Job ID given to the entire array submission.

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

## Interactive Jobs with `srun` at the Terminal

To interact with a job at the terminal, use the following `srun` command with the `--pty /bin/bash` flag. The other [flags](#slurm-flags) should be substituted in place of `$FLAGS`.

``` bash
srun $FLAGS --pty /bin/bash
```

For more details on using `srun` please see the [official documentation](https://slurm.schedmd.com/srun.html).

## Graphical Interactive Jobs

It is highly recommended to use the [Open OnDemand](../open_ondemand/ood_main.md) web portal for [interactive apps](../open_ondemand/ood_interactive.md). Interactive sessions for certain software such as MATLAB and RStudio can be created directly from the browser while an HPC Desktop is available to access all of the other software on Cheaha. A terminal is also available through Open OnDemand.

It is possible to use other remote desktop software, such as VNC, to start and interact with jobs. These methods are not officially supported and we do not have the capacity to help with remote desktop connections. Instead, please consider switching your workflow to use the [Open OnDemand HPC Desktop](../open_ondemand/ood_interactive.md#my-interactive-sessions). If you are unable to use this method, please contact [Support](../../help/support.md).

## Estimating Compute Resources

Being able to estimate how many resources a job will need is critical. Requesting many more resources than necessary bottlenecks the cluster by reserving unused resources for an inefficient job preventing other jobs from using them. However, requesting too few resources will slow down the job or cause it to error.

Questions to ask yourself when requesting job resources:

1. Can my scripts take advantage of multiple CPUs?
    1. For instance, RStudio generally works on a single thread. Requesting more than 1 CPU here would not improve performance.
2. How large is the data I'm working with?
3. Do my pipelines keep large amounts of data in memory?
4. How long should my job take?
    1. For example, do not request 50 hours time for a 15 hour process. Have a reasonable buffer included to account for unexpected processing delays, but do not request the maximum time on a partition if that's unnecessary.

<!-- markdownlint-disable MD046 -->
!!! note

    Reasonable overestimation of resources is better than underestimation. However, gross overestimation may cause admins to contact you about adjusting resources for future jobs.
<!-- markdownlint-enable MD046 -->

To get the most out of your Cheaha experience and ensure your jobs get through the queue as fast as possible, please read about [Job Efficiency](../job_efficiency.md).
