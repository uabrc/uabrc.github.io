# Open OnDemand

Open OnDemand (OOD) is web portal to access Cheaha. On it, you can submit interactive jobs in easy to use forms. These jobs include a generic desktop as well as specific apps such as RStudio or MATLAB. There is also access to a basic file manager for viewing and moving files.

The web portal can be accessed at [https://rc.uab.edu](https://rc.uab.edu) and is available both on and off campus.

## Quickstart

To start a generic desktop job where any piece of software can run, do the following:

1. Go to [Cheaha's web portal](https://rc.uab.edu)
2. Click Interactive Apps > HPC Desktop at the top.
3. Select the resources you will need for the job (number of CPUs, amount of memory, job runtime, and partition).
      1. As an example, a generic desktop job could use 1 CPU and 8 GB of RAM.
      2. See our [partition table](https://docs.rc.uab.edu/cheaha/hardware/#summary) for to determine which partition fits your job. The requested amount of time should not exceed the partition limit.
4. Click Launch at the bottom. This will take you to the My Interactive Sessions page and a job card will be created for your interactive job.
5. When the job card is created, the job is in queue. It will remain gray while in queue but will turn green when the job has been allocated resources and is running. Click the `Launch Desktop in new tab` button to open the interactive job.

Every interactive job requested in OOD is already set on a compute node. This bypasses the login node and is the preferred method for running interactive jobs on Cheaha.

### Choosing Resources

Resources requested for an interactive job are shared amongst all processes run in that job. This means if you are planning on running multiple analyses in the same interactive session at the same time, you will need to request adequate resources for all processes.

Be sure to select a reasonable partition for your job. For a quick breakdown of partition use cases see [Cheaha's Getting Started](../getting_started.md#partitions). For a more complete overview of the partitions, see our [hardware page](../hardware.md#cheaha-hpc-cluster).

## Debugging OOD Job Failures

On occasion, interactive jobs created in OOD will crash on startup and cause the job card to disappear. Most of these failures are caused by improper environment setup prior to job creation. If you experiencing OOD job failures, retrieve the OOD job info using the following steps:

1. Create a new job with the same setup as the job that failed.
2. When the job is in queue, click the link in the `Session ID` field in the job card before the job fails (see the image below for an example). This will open a file browser in a new tab.

    ![!Example Session ID Link](images/example_session_id_link.png)

3. Wait for the job to fail. Afterwards, refresh the file browser, select all of the files (do not include the `desktops` or `..` folders), and click `Download`.
4. Take all of the files that were downloaded, put them in a new folder, and zip the folder.

[Submit a ticket](../../index.md#how-to-contact-us) to us explaining the issue with the zip folder created in Step 4 attached to the email, and we will be happy to assist. If you would like to inspect the log yourself for debugging, the `output.log` typically will contain the relevant error messages.
