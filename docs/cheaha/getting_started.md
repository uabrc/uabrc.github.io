# Getting Started

Cheaha is a High Performance Computing (HPC) resource intended primarily for batch processing of research computing software. We offer a user-friendly portal website Open OnDemand with graphical interfaces to the most common features, all in one place. Read on to learn more about our resources and how to access them.

## Getting Help

Please [Contact Us](../index.md#contact-us) with requests for support. Tips on getting effective support are [here](../help/support.md), and our frequently asked questions are [here](../help/faq.md).

## Account Creation

Please visit our [Account Creation page](../account_management/cheaha_account.md) for detailed instructions on creating a Cheaha account.

## Accessing Cheaha

The primary method for accessing Cheaha is through our online portal website, Open OnDemand. To login to our portal, navigate to our <https://rc.uab.edu>, which does not require an on-campus connection nor the UAB Campus VPN. You should be presented with UAB's Single Sign-on page, which will require use of [Duo 2FA](https://www.uab.edu/it/home/security/2-factor). Login using the appropriate credentials laid out at our [Account Creation page](../account_management/cheaha_account.md).

[SSH](../uab_cloud/remote_access.md#command-line-via-ssh) may be used to access Cheaha. Connect to host `cheaha.rc.uab.edu` on port `22`.

### With VSCode

An alternative method suited for developers using VSCode, is to use the "Remote - Tunnels" extension to connect to an [HPC Desktop Interactive Job](./open_ondemand/ood_interactive.md#hpc-desktop). More details on this process are available in the [VSCode Tunnel](./open_ondemand/ood_interactive.md#visual-studio-code-remote-tunnel) section.

<!-- markdownlint-disable MD046 -->
!!! important

    Please do not use VSCode "Remote - SSH" to connect to Cheaha. All processes happen on the login node. Use the link above to use "Remote - Tunnel" instead.
<!-- markdownlint-enable MD046 -->

## Open OnDemand Features

The Open OnDemand portal features a [file browser](./open_ondemand/ood_files.md), [job composer](./open_ondemand/ood_jobs.md) and various [interactive applications](./open_ondemand/ood_interactive.md) including a remote desktop, Jupyter, RStudio and MATLAB, among others. There is also a [terminal](./open_ondemand/ood_main.md#shell-access) usable directly in the browser for very basic functions such as file management. More detailed documentation may be found on our [Open OnDemand page](./open_ondemand/ood_main.md).

## Hardware

A full list of the available hardware can be found on our [hardware page](./hardware.md).

### Storage

All researchers are granted 5 TB of individual storage when they [create their Research Computing account](../account_management/cheaha_account.md).

Shared storage is available to all Lab Groups and Core Facilities on campus. Shared storage is also available to UAB Administration groups.

Please visit our [Storage page](../data_management/storage.md) for detailed information about our individual and shared storage options.

### Partitions

Compute nodes are divided into groups called partitions each with specific qualities suitable for different kinds of workflows or software. In order to submit a compute job, a partition must be chosen in the Slurm options. The partitions can be roughly grouped as such:

|  Use | Partition Names | Notes |
|---|---|---|
| GPU Processing | pascalnodes, pascalnodes-medium, amperenodes, amperenodes-medium  | These are the only partitions with GPUs |
| All Purpose | amd-hdr100 | Runs AMD CPUs compared to all other CPU partitions running Intel. [Contact us](../index.md#how-to-contact-us) with issues running on this partition |
| Shorter time  | express, short, intel-dcb  |  |
| Medium-long time  | medium, long  |  |
| Very large memory | largemem, largemem-long |  |

Please visit our [hardware](hardware.md#cheaha-hpc-cluster) for more details about the partitions.

### Etiquette

[Quality-of-Service (QoS) limits](hardware.md#quality-of-service-qos-limits) are in place to ensure any one user can't monopolize all resources.

#### Running Tasks on Compute Nodes

There two main node types on Cheaha for researchers, the login node and many compute nodes. All expensive compute tasks must be run on compute nodes. Tasks running on the login node slow down processes for everyone, and in extreme cases can cause service outages affecting your work and the work of many of your colleagues. We will contact you if we find processes on the login node to help move your tasks to compute nodes.

You are on compute nodes if:

- using Open OnDemand Interactive Apps
- using Open OnDemand Job Composer
- terminal prompt looks like `[<blazerid>@c0001 ~]$`

You are on the login node if:

- terminal prompt looks like `[<blazerid>@login001 ~]$`

<!-- markdownlint-disable MD046 -->
!!! important

    If you are doing more than minor file management, you will need to use a compute node. Please request an interactive session at [https://rc.uab.edu](https://rc.uab.edu) or through a job submitted using [Slurm](./slurm/introduction.md).
<!-- markdownlint-enable MD046 -->

## Slurm

Slurm is our job queueing software used for submitting any number of job scripts to run on the cluster. We have documentation on how to set up job scripts and submit them [further in](./slurm/introduction.md). More complete documentation is available at <https://slurm.schedmd.com/>.

## Software

A large variety of software is available on Cheaha as modules. To view and use these modules see [the following documentation](./software/modules.md).

For new software installation, please try searching [Anaconda](../workflow_solutions/using_anaconda.md) for packages first. If you still need help, please [send a support ticket](../help/support.md)

### Conda Packages

A significant amount of open-source software is distributed as Anaconda or Python libraries. These libraries can be installed by the user without permission from Research Computing using Anaconda environments. To read more about using Anaconda virtual environments see our [Anaconda page](./software/software.md#anaconda-on-cheaha).

If the software installation instructions tell you to use either `conda install` or `pip install` commands, the software and its dependencies can be installed using a virtual environment.
