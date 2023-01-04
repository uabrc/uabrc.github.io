# Getting Started

Cheaha is a High Performance Computing (HPC) resource intended primarily for batch processing of research computing software. We offer a user-friendly portal website Open OnDemand with graphical interfaces to the most common features, all in one place. Read on to learn more about our resources and how to access them.

## Getting Help

Please [Contact Us](../index.md#contact-us) with requests for support. Tips on getting effective support are [here](../help/support.md), and our frequently asked questions are [here](../help/faq.md).

## Account Creation

Please visit our [Account Creation page](../account_management/cheaha_account.md) for detailed instructions on creating a Cheaha account.

## Accessing Cheaha

The primary method for accessing Cheaha is through our online portal website, Open OnDemand. To login to our portal, navigate to our <https://rc.uab.edu>, which does not require an on-campus connection nor the UAB Campus VPN. You should be presented with UAB's Single Sign-on page, which will require use of [Duo 2FA](https://www.uab.edu/it/home/security/2-factor). Login using the appropriate credentials laid out at our [Account Creation page](../account_management/cheaha_account.md).

[SSH](../uab_cloud/remote_access.md#command-line-via-ssh) may be used to access Cheaha. Connect to host `cheaha.rc.uab.edu` on port `22`.

## Open OnDemand Features

The Open OnDemand portal features a [file browser](./open_ondemand/ood_files.md), [job composer](./open_ondemand/ood_jobs.md) and various [interactive applications](./open_ondemand/ood_interactive.md) including a remote desktop, Jupyter, RStudio and MATLAB, among others. There is also a [terminal](./open_ondemand/ood_main.md#shell-access) usable directly in the browser for very basic functions such as file management. More detailed documentation may be found on our [Open OnDemand page](./open_ondemand/ood_main.md).

## Hardware

A full list of the available hardware can be found on our [hardware page](./hardware.md).

### Storage

#### User Storage

Each user is allocated 5 TB of personal storage by default. This storage quota is shared between the `USER_DATA` (`/data/user/<blazerid>`) and the `HOME` (`/home/<blazerid>`) directories. More information on storage can be [found here](../data_management/storage.md).

#### Project Directories

In addition to personal storage, Primary Investigators may request additional shared storage for their lab personnel. This space is given a default size of 25 TB. Each PI may have one project space. To request project storage space, the PI should email support at support@listserv.uab.edu with the name of the project as well as the Blazer IDs of the researchers to give access to. Any future requests for giving or removing access must come from the PI.

<!-- markdownlint-disable MD046 -->
!!! danger

    Data on Cheaha are replicated for recovery in case of system failures; however, **data are not recoverable if deleted by the researcher**. Be very careful with commands such as `rm -r` and other tools that delete files making sure you are deleting only the files and folders you mean to. Backing up data onto external platforms is the sole responsiblity of the researcher. Make [backups](../data_management/storage.md#backups) of raw data places such as [RC Long-term Storage](https://uabrc.github.io/data_management/lts/lts/), AWS/Google Cloud/Azure data storage, local hard drives, or [UAB Box](https://www.box.com). Analysis scripts to places like [Github](https://www.github.com) or [UAB RC Gitlab](https://gitlab.rc.uab.edu).
<!-- markdownlint-enable MD046 -->

### Etiquette

[Quotas](hardware.md#quality-of-service-qos-limits) are in place to ensure any one user can't monopolize all resources.

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
