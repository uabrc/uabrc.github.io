# Introduction to Slurm

All work on Cheaha must be submitted to our fair-share job queueing system, Slurm. Slurm is a collection of software packages enabling researchers to use resources on Cheaha. Researchers write job scripts that tell Slurm what commands to run and what resources are needed. Scripts submitted using the `sbatch` command are queued by Slurm. Resources are allocated when as they become available.

The official Slurm documentation can be found at [the Slurm website](https://slurm.schedmd.com/). The official [Slurm Quickstart](https://slurm.schedmd.com/quickstart.html) may help you get oriented.

## How Do I Use Slurm?

1. Understand how to run your software in 'batch' mode, purely from the command line. You may need to review the software documentation.
1. Stage data to [Cheaha storage](../../data_management/cheaha_storage_gpfs/index.md).
1. Figure out what resources are needed, such as CPUs, memory, GPUs, and time.
1. Write a [Slurm job script](./slurm_tutorial.md). Be sure to delete data from local scratch.
1. [Submit the job](./submitting_jobs.md) with the `sbatch` command.
1. [Monitor the job](./job_management.md#monitoring-queued-jobs-with-squeue) with the `squeue` command.
1. Review job information and efficiency with the [`sacct` command](./job_management.md#reviewing-past-jobs-with-sacct) and [`seff` command](../job_efficiency.md).
1. Remove unneeded data from network scratch.

## The Slurm Queue

When working on Cheaha and with Research Computing, you will often hear references to the Slurm Queue. By its name, you might think that the Slurm Queue is a first-in-first-out (FIFO) queue like when waiting in line at an event or place of business. And, some institutions use a FIFO queue, as it is the default configuration for Slurm.

At UAB Research Computing, we use a multifactor _priority_ queue, meaning that those users with top priority are first to receive service, regardless of when they entered the queue.

Slurm measures priority as a single number, and the highest value generally is first to receive service. Multiple factors play into the queue. The most important factors are given in the table below, in no particular order.

{{ read_csv("cheaha/slurm/res/priority_factor.csv") }}

The fastest way to queue a job is to request minimal resources and time, have a smaller share of total resources already used, and use the shortest partition possible.

Given two or more jobs with equal priority, the job on the partition with the largest "Priority Tier" value goes first.

The scheduler cannot predict the future. If a job enters the queue with a higher priority than yours, it will start before yours. This may lead to a situation where your job no longer fits on any of the nodes. If this happens your job will have to wait until sufficient space opens regardless of its priority value. A possible strategy to minimize the risk of preemption is to request fewer resources per node, to more readily fill available space.

A lot of intelligent people have worked very hard to design the Slurm scheduler to be both smart and fair. Please allow it to do its job. If you have workloads that are very large and want advice or are unsure of the best queueing strategy for your workflow, please [Contact Us](../../index.md#how-to-contact-us) for a consultation, we are happy to help.

<!-- markdownlint-disable MD046 -->
!!! important

    Please do not run `squeue`, or any other Slurm command, in a loop. All Slurm commands increase the load on the Slurm controller. Many commands in a short period of time can make Slurm unresponsive, unstable, or require a restart, which negatively impacts all researchers.

    Instead, please simply let the Slurm scheduler do its job of managing.
<!-- markdownlint-enable MD046 -->
