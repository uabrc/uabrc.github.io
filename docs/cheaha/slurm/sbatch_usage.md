# Submitting Jobs with Slurm

Slurm is simple to use to submit batch jobs. Scripts should be written
in an available shell language on Cheaha, typically bash, and should
include the appropriate Slurm directives at the top of the script
telling the scheduler the requested resources. Common Slurm directives
can be seen below along with simple examples for both single batch jobs
and array batch jobs

## Common Slurm Terminology

- Node: A subdivision of the cluster that contains multiple cores.
  - Login nodes: Controls user access to Cheaha. Low count and shared among all users. DO NOT RUN JOBS ON THE LOGIN NODE
  - Compute nodes: Dedicated nodes for running user jobs.
- Core: A single CPU
- Partition: A job queue to submit your job to. Different partitions have different resource limits and priority.
- Job: Any single or combination of commands that require computational resources to perform. Can be interactive or submitted to the scheduler.
- Batch jobs: Scripts to submit to the SLURM scheduler. Should run with no user input or graphical user interface (GUI). Replicates commands in an order you would run them on the command line.

## Basic Slurm Directives

Slurm has many directives a researcher can use when creating a job, but
a short list of the very common ones are listed here:

1. `--job-name`: The name of the job that appears when using `squeue`
2. `--ntasks`: The number of nodes a job needs
3. `--cpus-per-task`: The number of cores to request for each task (default:1)
4. `--partition`: The partition to submit the job to. Partition details
    can be seen below
5. `--time`: Amount of time the job is estimated to run for. Acceptable time formats include "minutes", "minutes:seconds", "hours:minutes:seconds", "days-hours", "days-hours:minutes" and "days-hours:minutes:seconds"
6. `--mem-per-cpu`: Amount of RAM (in MB) needed per CPU. Can specify 4 GB with either 4000 or 4G. `--mem` can be used to specify the total RAM across all CPUs instead. Requested memory is shared across all CPUs.
7. `--output`: Path to a file storing the text output of the job commands.
8. `--error`: Path to an output file if the script errors.

For batch jobs, directives are typically included as comments at the top of the script. See examples below. All batch jobs should be submitted using the `sbatch` command. All directives and more information on how to submit jobs can be seen using `man sbatch`.

## Slurm Partitions

{{ read_csv('cheaha/slurm/partitions.csv') }}

Notes:

- Express jobs are highest priority in scheduling meaning they will be scheduled faster
- Most partitions have a max amount of requestable memory per node at 175 GB. Largemem has a maximum memory limit of 1.5 TB.
- Pascalnodes are specifically used for access to GPUs
- Each user has a maximum amount of requestable resources across all jobs. Submitted jobs beyond this resource limit will be kept in the queue until a user's prior jobs have completed. This will appear as `QOSMaxResourceLimit` in your `squeue` list.
- If a script finishes executing before the requested time limit, the job will automatically close and resources will be released. However requesting the max amount of time will cause scheduler priority to decrease.

## Estimating Compute Resources

Being able to estimate how many resources a job will need is critical. Requesting many more resources than necessary bottlenecks the cluster by reserving unused resources for an inefficient job preventing other jobs from using them. However, requesting too few resources will slow down the job or cause it to error.

Questions to ask yourself when requesting job resources:

1. Can my scripts take advantage of multiple CPUs?
    1. For instance, RStudio only works on a single thread (outside of very specific cases). Requesting more than 1 CPU here would not improve performance.
2. How large is the data I'm working with?
3. Do my pipelines keep large amounts of data in memory?
4. How long should my job take?
    1. For example, do not request 50 hours time for a 15 hour process. Have a reasonable buffer included to account for unexpected processing delays, but do not request the maximum time on a partition if that's unnecessary.

!!! note

    Reasonable overestimation of resources is better than underestimation. However, gross overestimation may cause admins to contact you about adjusting resources for future jobs.

After a job is completed, look at how well resources were used using `seff`. For more information, read `job-efficiency`.

## Single Batch Job

An example script using some of the listed directives can be seen below:

``` bash
#!/bin/bash
#
#SBATCH --job-name=test
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --partition=express
#SBATCH --time=10:00
#SBATCH --mem-per-cpu=1G
#SBATCH --output=test.out

echo "Hello World"
```

This script requests 1 core on 1 node with 1 GB of RAM on the express partition for 10 minutes. The output of the commands in the script, the `echo` command here, can be seen in the `test.out` file that will be created when the script executes.

If the script is saved as `$HOME/example.sh`, it can be submitted using the following command from the command line:

``` bash
sbatch $HOME/example.sh
```

## Array Jobs

For some analyses, you will want to perform the same operations on different inputs. However, instead of creating individual scripts for each different input, you can create an array job instead. These array jobs duplicate the SBATCH parameters as well as the commands of the script and apply them to different inputs specified by the user.

Array jobs can use a Slurm environmental variable, `$SLURM_ARRAY_TASK_ID`, as an index for inputs. For example, if we have a script that looks like:

``` bash
#!/bin/bash
#
#SBATCH --job-name=array
#SBATCH --output=array_%A_%a.out
#SBATCH --time=10:00
#SBATCH --partition=express
#SBATCH --ntasks=1
#SBATCH --mem=1G

# Print the task id.
echo "My SLURM_ARRAY_TASK_ID: " $SLURM_ARRAY_TASK_ID
```

In this script, the %A and %a values in the output file name refer to the overall job ID and array task ID, respectively. We can submit the script (named array.sh) using the following command:

``` bash
sbatch --array=0-15 array.sh
```

!!! note

    It is crucial to note that arrays use 0-based indexing. Array number 0 corresponds to the first job you're running. The `SLURM_ARRAY_TASK_ID` variable will also be 0 in this case.

This will cause 16 jobs to be created with array IDs from 0 to 15. Each job will write out the line "My SLURM_ARRAY_TASK_ID: " followed by the ID number. Scripts can be written to take advantage of this indexing environmental variable. For example, a project could have a list of participants that should be processed in the same way, and the analysis script uses the array task ID as an index to say which participant is processed in each individual job. Bash, python, MATLAB, and most languages have specific ways of interacting with environmental variables.

If you do not want to submit a full array, the `--array` directive can take a variety of inputs:

``` bash
# submit jobs with index 0, 3, and 7
sbatch --array=0,3,7 array.sh

# submit jobs with index 0, 2, 4, and 6
sbatch --array=0-6:2 array.sh
```

Additionally, the `--array` directive can be included with the rest of the SBATCH options in the script itself, although this adds another step if different subsets of the array job need to be run over time.

## Interactive Jobs

Batch jobs are meant to be submitted and not interacted with during execution. However, some jobs need user input during execution or need to use a GUI. Interactive jobs are meant to be used for these situations.

It is highly suggested to use the Cheaha `Open OnDemand` web portal for interactive jobs. Interactive sessions for certain software such as MATLAB and RStudio can be created directly from the browser while an HPC Desktop is available to access all of the other software on Cheaha.

If you choose to use a standard ssh connection and VNC for your interactive job, you will need to request resources for your job from the command line after opening the VNC. You can do this using the following command:

``` bash
srun --ntasks=1 --cpus-per-task=1 --mem-per-cpu=4G --time=1:00:00 --partition=express --pty /bin/bash
```

Resources should be changed to fit the job's needs. An interactive job will then start on a compute node. You can tell if you are on a compute node by looking at the command line. It should have the form: `[blazerid@c0XXX ~]` where XXX is a number.

!!! warning

    If your terminal says `[blazerid@loginXXX ~]`, you are on the login node. NO COMPUTE JOBS SHOULD BE RUN ON THE LOGIN NODE. If jobs are being run on the login node, they will be deleted and the user will be warned. Multiple warnings will result in account suspension.
