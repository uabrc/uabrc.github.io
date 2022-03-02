# Introduction to SLURM

All work on Cheaha must be submitted to the queueing system, Slurm. This doc gives a basic overview of Slurm and how to use it.

Slurm is software that gives researchers fair allocation of the cluster's resources. It schedules jobs based using resource requests such as number of CPUs, maximum memory (RAM) required per CPU, maximum run time, and more.

The main Slurm documentation can be found at [the Slurm site](https://slurm.schedmd.com/). The [Slurm Quickstart](https://slurm.schedmd.com/quickstart.html) can also be helpful for orienting researchers new to queueing systems on the cluster.

The basic workflow for non-interactive jobs follows:

1. Stage data to `$USER_DATA`, `$USER_SCRATCH`, or a project directory.
2. Research how to run your directives in 'batch' mode. In other words, how to run your analysis pipeline from the command line, with no GUIs or researcher input.
3. Identify the appropriate resources necessary to run the jobs (CPUs, time, memory, etc)
4. Write a job script specifying these parameters using Slurm directives.
5. Submit the job (`sbatch`)
6. Monitor the job (`squeue`)
7. Review the results, and modify/rerun if necessary (`sacct` and `seff`)
8. Remove data from `$USER_SCRATCH`
