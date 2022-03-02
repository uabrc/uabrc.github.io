# Cheaha

Cheaha is a High Performance Computing (HPC) resource intended primarily for batch processing. We offer a researcher-friendly portal website [Open OnDemand](#open-ondemand) with graphical interfaces to the most common features, all in one place.

## Etiquette

[Quotas](slurm/sbatch_usage.md#slurm-partitions) are in place to ensure any one researcher can't monopolize all resources.

All expensive compute tasks must be run on compute nodes. Tasks running on the login node slow down processes for everyone, and in extreme cases can cause service outages, affecting your work and the work of many of your colleagues. We will contact you if we find processes on the login node. Don't worry, we're happy to help get your tasks running in the right place with the most efficient resources.

### You are on compute nodes if

- using Open OnDemand Interactive Apps
- using Open OnDemand Job Composer
- terminal prompt contains something like `c0001`

### You are on the login node if

- terminal prompt contains something like `login001`

### When do I use need a compute node? If my task

- takes longer than 60 seconds
- uses more than one core
- uses more than 4 GB ram
- runs multiple times
- affects more than a few files
- transfers more than 1 GB over the internet

## Open OnDemand

Our online portal website, Open OnDemand, is available at <https://rc.uab.edu>. We have more detailed documentation on using Open OnDemand located [further in](open_ondemand/ood_main.md).

The portal features a [file browser](open_ondemand/ood_files.md), [job composer](open_ondemand/ood_jobs.md) and various [interactive applications](open_ondemand/ood_interactive.md) including a remote desktop, Jupyter, RStudio and MATLAB, among others. There is also a [terminal](open_ondemand/ood_main.md#shell-access) usable directly in the browser.

## Slurm

Slurm is our job queueing software, and we have documentation [further in](slurm/introduction.md). More complete documentation is available at <https://slurm.schedmd.com/>.

!!! important

<!-- markdownlint-disable-next-line -->
    Expensive compute tasks  should only be run on compute nodes. If your task will take longer than

    For more information please see our [Sbatch Documentation](slurm/sbatch_usage.md).
