---
toc_depth: 3
---

# Getting Started

Cheaha is a High Performance Computing (HPC) resource intended primarily for batch processing of research computing software. We offer a user-friendly portal website Open OnDemand with graphical interfaces to the most common features, all in one place. Read on to learn more about our resources and how to access them.

## What if I Need Help?

Please [Contact Us](../index.md#how-to-contact-us) with requests for support. Please read our [Tips on Getting Effective Support](../help/support.md), and our [Frequently Asked Questions](../help/faq.md).

## Account Creation

Please visit our [Account Creation page](../account_management/cheaha_account.md) for detailed instructions on creating a Cheaha account.

## Accessing Cheaha

The primary method for accessing Cheaha is through our online portal website, Open OnDemand. To login to our portal, navigate to our <https://rc.uab.edu>, which does not require an on-campus connection nor the UAB Campus VPN. You should be presented with UAB's Single Sign-on page, which will require use of [Duo 2FA](https://www.uab.edu/it/home/security/2-factor). Login using the appropriate credentials laid out at our [Account Creation page](../account_management/cheaha_account.md).

[SSH](../uab_cloud/remote_access.md#command-line-via-ssh) may be used to access Cheaha. Connect to host `cheaha.rc.uab.edu` on port `22`.

### With VSCode

An alternative method suited for developers using VSCode, is to use the "Remote - Tunnels" extension to connect to an [HPC Desktop Interactive Job](./open_ondemand/hpc_desktop.md). More details on this process are available in the [VSCode Tunnel](./open_ondemand/hpc_desktop.md#visual-studio-code-remote-tunnel) section.

<!-- markdownlint-disable MD046 -->
!!! important

    Please do not use VSCode "Remote - SSH" to connect to Cheaha. All processes happen on the login node. Use the link above to use "Remote - Tunnel" instead.
<!-- markdownlint-enable MD046 -->

## Open OnDemand Features

The Open OnDemand portal features a [terminal](./open_ondemand/ood_layout.md#opening-a-terminal) usable directly in the browser for basic functions such as file management.

Interactive apps are available directly in your browser, including the following.

- [File Browser](./open_ondemand/ood_layout.md#file-browser)
- [Remote Desktop](./open_ondemand/hpc_desktop.md)
- [Jupyter Notebook](./open_ondemand/ood_jupyter_notebook.md)
- [Jupyter Lab](./open_ondemand/ood_jupyterlab.md)
- [RStudio](./open_ondemand/ood_rstudio.md)
- [MATLAB](./open_ondemand/ood_matlab.md)

More detailed documentation can be found on our [Open OnDemand page](./open_ondemand/index.md).

## Hardware

A full list of the available hardware can be found on our [hardware page](./hardware.md).

### Storage

All researchers are granted 5 TB of individual storage when they [create their Research Computing account](../account_management/cheaha_account.md).

Shared storage is available to all Lab Groups and Core Facilities on campus. Shared storage is also available to UAB Administration groups.

Please visit our [Storage page](../data_management/index.md) for detailed information about our individual and shared storage options.

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

[Quality-of-Service (QoS) limits](hardware.md#summary) are in place to ensure any one user can't monopolize all resources.

#### Why You Should Avoid Running Jobs on Login Nodes

To effectively manage and provide high-performance computing (HPC) resources to the University community provided via the clusters, kindly use the terminal from compute nodes in created jobs rather than the terminal from login nodes. Our clusters are essential for conducting this large and complex scientific computations that often times require a significant amount of computing power. These clusters are shared environments, where multiple users execute their research and computing tasks simultaneously. It is important to utilize the structure of these environments properly for efficient and respectful use of the shared resources, so everyone gets a fair chance at using these resources.

##### Login vs. Compute Nodes

Like with most HPC clusters, cheaha nodes are divided into two, the login node and compute nodes. The login node acts as the gateway for users to access the cluster, submit jobs, and manage files. Compute nodes, on the other hand, are like the engines of the cluster, designed to perform the heavy lifting of data processing and computation.

The Login node can be accessed from the Cheaha landing page or through the `$HOME` directory. You can see in the images below, how to identify if you’re within a login node or compute node.

You are on the login node if:

- terminal prompt looks like `[$USER@login004 ~]$`

![!login node terminal prompt shows username@login004](images/login_node.png)

You are on compute nodes if:

- using [Open OnDemand Interactive Apps](../cheaha/open_ondemand/ood_layout.md#interactive-apps)
- using [Interactive Jobs with `srun`](../cheaha/slurm/submitting_jobs.md#interactive-jobs-with-srun)
- terminal prompt looks like `[$USER@c0112 ~]$`

![!compute node terminal prompt shows username@c0112](images/comp_node.png)

<!-- markdownlint-disable MD046 -->
!!! important

    If the terminal prompt appears as `bash-4.2$` instead of the user prompt `[$USER@login004]`, please refer to the [FAQ](#how-to-restore-default-terminal-prompt-from-bash-42-to-userlogin004) below to resolve the issue.
<!-- markdownlint-disable MD046 -->

##### How to Restore Default Terminal Prompt From `bash-4.2$` to `$USER@login004`?

There might be scenarios where you see the terminal prompt display `bash-4.2$` like below, instead of the user prompt `[$USER@login004]`.

```bash
bash-4.2$
```

The `bash-4.2$` prompt indicates that the files `$HOME/.bashrc` and/or `$HOME/.bash_profile` are missing or corrupted. To resolve this issue, we recommend following these steps:

(i) If you have made any changes to these files earlier, it's advisable to create backups. For instance, you can rename `.bashrc` to `.bashrc.backup`, and you can verify if the backed-up files are listed.

```bash
bash-4.2$ mv $HOME/.bashrc $HOME/.bashrc.backup
bash-4.2$ mv $HOME/.bash_profile $HOME/.bash_profile.backup

bash-4.2$ ls .bash*
.bash_profile.backup  .bashrc.backup
```

(ii) After you have taken the backup of those files, run the following command to copy the default versions from `/etc/skel` to `$HOME`. Doing this will clobber, or remove, any changes you may have made, so be sure to make a backup first, as shown in the step (ii), if you wish to keep any changes. You will see the copied files listed in the directory.

```bash
bash-4.2$ cp /etc/skel/.bash* $HOME

bash-4.2$ ls .bash*
.bash_profile  .bash_profile.backup  .bashrc  .bashrc.backup
```

(iii) You can exit the terminal or source your files using the commands below to apply the changes, after which you will see the user prompt.

```bash
bash-4.2$ source ~/.bashrc
[$USER@login004 ~]$
```

##### Slurm and Slurm Jobs

Slurm Workload Manager is a widely used open-source job scheduler that manages the queue of jobs submitted to the compute nodes. It ensures efficient use of the cluster by allocating resources to jobs, prioritizing tasks, and managing queues of pending jobs. Starting Slurm jobs can be done in two primary ways: using Open OnDemand (OOD) or through the terminal. For more details on how to use Slurm on cheaha, please see our [slurm docs](../cheaha/slurm/introduction.md).

##### What Should Run in Jobs?

Ideally, only non-intensive tasks like editing files, or managing job submissions should be performed on the login node. Compute-intensive tasks, large data analyses, and simulations should be submitted as Slurm jobs to compute nodes. This approach ensures that the login node remains responsive and available for all users to manage their tasks and submissions. Submitting compute-intensive tasks as Slurm jobs to compute nodes helps to prevent overloading the login node, ensuring a smoother experience for all users of the cluster.

##### How to Start Slurm Jobs?

There are two straightforward ways to start Slurm jobs on cheaha, and they are detailed below.

###### Open OnDemand (OOD)

UAB uses the OOD platform, a web-based interface for providing access to cluster resources without the need for command-line tools. Users can easily submit jobs, manage files, and even use interactive applications directly from their browsers. One of the standout features of OOD is the ability to launch interactive applications, such as a virtual desktop environment. This feature allows users to work within the cluster as if they were on a local desktop, providing a user-friendly interface for managing tasks and running applications. For an overview of how the page works, and to read more details see our docs on [Navigating Open OnDemand](../cheaha/open_ondemand/index.md). After logging into OOD, users can access various applications designed for job management, file editing, and more.

###### Terminal (`sbatch` Jobs)

For users comfortable with the command line, submitting jobs via scripts using `sbatch` is a straightforward process. An `sbatch` script contains the job specifications, such as the number of nodes, execution time, and the command to run. This method provides flexibility and control over job submission and management. For more information on this, please see our docs on [Submitting Jobs with Slurm](../cheaha/slurm/submitting_jobs.md).

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
