# Open OnDemand

Open OnDemand (OOD) is web portal to access Cheaha. On it, you can submit interactive jobs in easy to use forms. These jobs include a generic desktop as well as specific apps such as RStudio or MATLAB. There is also access to a basic file manager for viewing and moving files.

The web portal can be accessed at <https://rc.uab.edu> and is available both on and off campus.

## Quickstart

To start a generic desktop job where any piece of software can run, do the following:

1. Go to [Cheaha's web portal](https://rc.uab.edu)
1. Click Interactive Apps > HPC Desktop at the top.
1. Select the resources you will need for the job (number of CPUs, amount of memory, job runtime, and partition).
      1. As an example, a generic desktop job could use 1 CPU and 8 GB of RAM.
      1. See our [partition table](https://docs.rc.uab.edu/cheaha/hardware#summary) for to determine which partition fits your job. The requested amount of time should not exceed the partition limit.
1. Click Launch at the bottom. This will take you to the My Interactive Sessions page and a job card will be created for your interactive job.
1. When the job card is created, the job is in queue. It will remain gray while in queue but will turn green when the job has been allocated resources and is running. Click the `Launch Desktop in new tab` button to open the interactive job.

Every interactive job requested in OOD is already set on a compute node. This bypasses the login node and is the preferred method for running interactive jobs on Cheaha.

### Choosing Resources

For a more complete description of how to select resources, please see our [Creating an Interactive Job](ood_layout.md#creating-an-interactive-job) section.

## Debugging OOD Job Failures

If your OOD job cards are disappearing after being allocated or during the job, see our [documentation](ood_layout.md#debugging-ood-job-failures) for instructions on how to retrieve the logs and submit a ticket to Research Computing support.
