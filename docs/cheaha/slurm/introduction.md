# Introduction to Slurm

All work on Cheaha must be submitted to the queueing system, Slurm. This doc gives a basic overview of Slurm and how to use it.

Slurm is software that gives researchers fair allocation of the cluster's resources. It schedules jobs based using resource requests such as number of CPUs, maximum memory (RAM) required per CPU, maximum run time, and more.

The main Slurm documentation can be found at [the Slurm site](https://slurm.schedmd.com/). The [Slurm Quickstart](https://slurm.schedmd.com/quickstart.html) can also be helpful for orienting researchers new to queueing systems on the cluster.

## Batch Job Workflow

1. Stage data to `$USER_DATA`, `$USER_SCRATCH`, or a `/data/project/...` directory.
2. Research how to run your directives in 'batch' mode. In other words, how to run your analysis pipeline from the command line, with no GUIs or researcher input.
3. Identify the appropriate resources necessary to run the jobs (CPUs, time, memory, etc)
4. Write a job script specifying these parameters using Slurm directives.
5. Submit the job (`sbatch`)
6. Monitor the job (`squeue`)
7. Review the results, and modify/rerun if necessary (`sacct` and `seff`)
8. Remove data from `$USER_SCRATCH`

For more details, please see [Submitting Jobs](submitting_jobs.md).

For details on managing and reviewing jobs, please see [Job Management](job_management.md).

## The Slurm Queue

When working on Cheaha and with Research Computing, you will often hear references to the Slurm Queue. By its name, you might think that the Slurm Queue is a first-in-first-out (FIFO) queue like when waiting in line at an event or place of business. And, some institutions use a FIFO queue, as it is the default configuration for Slurm.

At UAB Research Computing, we use a multifactor _priority_ queue, meaning that those users with top priority are first to receive service, regardless of when they entered the queue.

Slurm measures priority as a single number, and the highest value generally is first to receive service. Multiple factors play into the queue. The most important factors are given in the table below, in no particular order.

{{ read_csv("cheaha/slurm/res/priority_factor.csv") }}

The fastest way to queue a job is to request minimal resources and time, have a smaller share of total resources already used, and use the shortest partition possible.

Given two or more jobs with equal priority, the job on the partition with the largest "Priority Tier" value goes first.

The scheduler cannot predict the future. If a job enters the queue with a higher priority than yours, it will start before yours. This may lead to a situation where your job no longer fits on any of the nodes. If this happens your job will have to wait until sufficient space opens regardless of its priority value. A possible strategy to minimize the risk of preemption is to request fewer resources per node, to more readily fill available space.

If you are unsure of the best queueing strategy for your workflow, please [Contact Us](../../index.md#contact-us) for a consultation, we are happy to help.
