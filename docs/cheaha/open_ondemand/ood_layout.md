# Navigating Open OnDemand

After creating your Cheaha account, going to [rc.uab.edu](https://rc.uab.edu) will take you to the Open OnDemand (OOD) homepage.

![Screenshot of the Open OnDemand homepage.](./images/ood_homepage.png)

The Open OnDemand homepage contains information about the main navigation tabs located at the top of the page, current updates to the system and a message of the day with links to our support email and documentation. The homepage also includes a [partition table](../getting_started.md#partitions) that helps you to determine the appropriate partition when submitting your jobs.

You can access all Open OnDemand features using the navigation tabs at the top of the page. The features most commonly used by researchers are described in the following sections.

## File Browser

The file browser allows you to view and manage files stored on the Cheaha system. To open the file browser, select `Files` from the navigation bar to open the dropdown menu, and then choose one of the available directories such as the [Home Directory](../../data_management/storage/cheaha_storage_gpfs/individual_directories.md), [Data directory](../../data_management/storage/cheaha_storage_gpfs/individual_directories.md) (`/data/user/$USER`), or [scratch directory](../../data_management/storage/cheaha_storage_gpfs/network_scratch.md) (`/scratch/$USER`). Selecting one of these directories from the dropdown menu opens the file browser for that directory.

![Screenshot of the Open OnDemand file browser.](./images/file_browser.png)

The following items describe groups of controls shown in the image. Each group is numbered in keyboard navigation order, matching the labels in the screenshot.

1. **Operations Control Buttons**: The operations control button group provides options for managing files and directories. The  buttons included in this group are: <!-- markdownlint-disable-next-line MD033 -->
    1. **<span id="terminal" tabindex="-1">Opening in Terminal</span>**: Click the `>_Open in Terminal` button to open a bash terminal in the current directory. This should only be used for small tasks since the terminal is running on the login node. For compute-intensive work, request an interactive session in the terminal or HPC Desktop session through [Interactive Apps](#interactive-apps).
    1. **Create a New File**: Click `New File` button to create a new file in the current directory.
    1. **Create a New Directory**: Click  `New Directory` button to create a new folder in the current directory.
    1. **Uploading Data**: Click the `Upload` button to select and upload files from your local machine.

        <!-- markdownlint-disable MD046 -->
        !!! important

            This button should be used only to upload small files (< 1 MB). For large files or datasets, please use [Globus](../../data_management/transfer/globus/index.md) instead.
        <!-- markdownlint-enable MD046 -->

    1. **Download**: Select files by clicking the checkbox immediately to the left of the file name in the first, unlabeled column of the [File and Folders Table](#file-table), then click the `Download` button to save them to your local machine..
    1. **Copy/Move**: Select files by clicking the checkbox immediately to the left of the file name in the first, unlabeled column of the [File and Folders Table](#file-table), then click the `Copy/Move` button to copy or move them to another directory.
    1. **Delete**: Select files by clicking the checkbox immediately to the left of the file name in the first, unlabeled column of the [File and Folders Table](#file-table), then click `Delete` button to remove them from the current directory.

1. **Quick Access Directories**: The quick access directories links provide one click navigation to your most common work spaces which include:
    1. **Home Directory**: Click the `Home Directory` link to quickly navigate to your personal home folder.
    1. **Data Directory** (`/data/user/$USER`): Click the `Data` link to navigate to your main working data space.
    1. **Scratch Directory** (`/scratch/$USER`): Click the `/scratch/$USER` link to navigate to your scratch directory.
1. **Path Control Buttons**: The path control buttons display your current directory path and allow you to navigate or copy paths. The buttons in this group include:
    1. **Change Directory**: Click `Change Directory` button to jump to any other directories.
    1. **Copy Path**: Click `Copy Path` button to copy the currently displayed path as text.
1. **Custom view and metadata Controls**: The custom view and metadata controls group consists of checkboxes and a text field that allow you to adjust how files and folders are displayed. The control includes:
    1. **Show Owner/Mode**: Select `Show Owner/Mode` checkbox to display file modification dates, file permissions (mode), and file/directory owner (owner) Unix IDs. The permissions (`mode`) can be used to investigate permission issues in shared spaces like `/data/project` directories.
    1. **Show Dotfiles**: Select `Show Dotfiles` checkbox to display hidden files (those beginning with `.`) in the current directory.
    1. **Filter Text Field**: Enter a keyword in the text field to filter the displayed files and folders. <!-- markdownlint-disable-next-line MD033 -->
1. **<span id="file-table" tabindex="-1">File and Folders Table</span>**: This table displays the folders and files in the current directory and allows you to select items. For each file or folder, you can view, edit, rename, download, or delete it using the Actions menu.

    1. **Rename a File**: Click the three-dot menu next to the file name in the unlabeled Actions column, select `Rename` from the dropdown options, and enter the new name.
    1. **Other options Actions**: To view, edit, download, or delete a file, click the three-dot menu next to the file name in the unlabeled Actions column and select your preferred action.

## Clusters

The "Cheaha Shell Access" option is available under the "Clusters" menu in OOD. Cheaha Shell Access provides browser-based terminal access to the Cheaha cluster. It allows users to run commands, manage files, submit jobs, and troubleshoot workflows directly from the web interface without requiring a local SSH client.

![Screenshot of the OOD “Clusters” menu showing Cheaha Shell Access](images/ood_clusters.png)

!!! imporatant
    Note that Cheaha shell prompt to a login node. Do not run heavy-load jobs on the login node, instead you will have to use a [compute node](../../cheaha/getting_started.md#login-vs-compute-nodes). You will not typically be prompted for a password. If you are prompted, refer to [Enabling SSH Key Authentication on Cheaha](../../cheaha/getting_started.md/#enabling-ssh-key-authentication-on-cheaha).

## Interactive Apps

There are two tabs used to interact with applications in OOD, the Interactive Apps dropdown, used to select resources and start jobs, and the My Interactive Sessions tab, used to view currently running interactive apps. As shown below. ![!An image showing the Interactive App dropdown options on Cheaha](images/ood_menu_options.png)

### Creating an Interactive Job

The Interactive Apps dropdown has a list of specific software setup to run on Cheaha that you can interact with through a browser window such as RStudio, MATLAB, and Jupyter. There is also an HPC Desktop app that provides a general VNC desktop to run all available software on Cheaha. See the [quickstart](index.md#quickstart) for how to create an example HPC Desktop job. Below, you can see a general form for selecting job resources.

![!A general form for selecting interactive job resources](images/ood_general_resources_form.png)

The interactive apps have the following fields to customize the resources for your job:

1. Number of Hours: the maximum number of hours the job will run for. Interactive apps will stay allocated for this amount of time unless the job is manually deleted or crashes. The selected number of hours should be less than or equal to the max runtime for your selected partition.
1. Partition: the partition the job will be allocated in. See our [Partitions](../getting_started.md#partitions) section for more information about which partition to choose for your job.
1. Number of GPUs: Total number of GPUs to request (max of 4 on pascalnodes or 2 on amperenodes)
1. Numer of CPUs: Total number of CPUs to request
1. Memory Per CPU (GB): GB of memory multiplied by the requested number of CPUs.

<!-- markdownlint-disable MD046 -->
!!! note

    The "number of GPUs" field is ignored if a partition is selected that has no GPUs.
<!-- markdownlint-enable MD046 -->

<!-- markdownlint-disable MD046 -->
!!! tip

    You can decrease wait time in the queue by choosing resources carefully. The closer your request is to actual usage, the more optimal your wait time will be. Please see our section on [Job Efficiency](../job_efficiency.md) for more information.
<!-- markdownlint-enable MD046 -->

Every interactive app has resources only allocated on a single node, and resources are shared among all processes running in the app. Make sure the amount of memory you request is less than or equal to the max amount per node for the partition you choose. We have a table with [memory available per node](../hardware.md#cheaha-hpc-cluster) for each partition.

For more information on GPU efficiency please see [Making the Most of GPUs](../slurm/gpu.md#making-the-most-of-gpus).

<!-- markdownlint-disable MD046 -->
!!! important

    April 21, 2025: Currently, GPU-core affinity is not considered for GPU jobs on interactive apps. This may mean selecting multiple GPUs results in some GPUs not being used.
<!-- markdownlint-enable MD046 -->

#### Environment Setup Window

In addition to requesting general resources, for some apps you will have the option to add commands to be run during job startup in an Environment Setup Window. See below for an example showing how to load CUDA into a Jupyter job so it can use a GPU.

![! Example environment setup window showing how to load CUDA into a Jupyter job](./images/ood_environment_setup_window.png)

For jobs such as RStudio and Jupyter, some modules like CUDA need to be loaded beforehand so the application has access to it. This can also include loading compiler modules such as CMake and GCC for compiling package installations or editing your `$PATH` specifically for the interactive app without needing to edit your `.bashrc`. See the software specific pages for more examples on how to use the Environment Setup.

<!-- markdownlint-disable MD046 -->
!!! Note

    In the OOD session, the module is automatically reset at the beginning of every session by default. Therefore, avoid using `module reset` in the 'Environment Setup' box. See [best practice for loading modules](../software/modules.md#best-practice-for-loading-modules) for more information.
<!-- markdownlint-disable MD046 -->

<!-- markdownlint-disable MD046 -->
!!! note

    The latest CUDA and cuDNN are now available from [Conda](../slurm/gpu.md#cuda-and-cudnn-modules).
<!-- markdownlint-enable MD046 -->

#### Launching Interactive Sessions

Once you have completed the form fields with the necessary parameter for the job, click on the blue `Launch` button. The interactive session will be initiated and placed into the scheduling queue, changing the job state to `Queued`.

![!desktop session in queued state](./images/ood_desktop_queue.png)

Depending on the resources requested, you may need to wait for some time. After the resources are allocated, the job state will change to `Starting`.

![!desktop session in Starting state](./images/ood_desktop_starting.png)

Once the job is launched on the compute nodes, the state will switch to `Running`. You will then see the option `Launch Desktop in new tab` button. Click this button to open the interactive VNC session in a new tab. Alternatively, you can also click the blue button in the `Host` field to open a terminal directly. This terminal is opened on the compute node and so can run any commands you need.

![!desktop session in Running state](./images/ood_desktop_running.png)

### My Interactive Sessions

The My Interactive Sessions page lists the available apps and your current interactive sessions. If you are logged out, disconnected, or lose track of an interactive application (because of a closed tab or computer shutdown) you can reconnect to running applications on this page. The My Interactive Sessions page looks like:

![!List of interactive sessions shown as job cards.](./images/ood_interactive_sessions_II.png)

For each job running via Open OnDemand, there will be a card listed on this page:

1. **Job ID**: The jobID assigned by the Slurm scheduler for this specific job.
1. **Host**: The node on which the job is currently running.
1. **Time Remaining**: The amount of time remaining from the total requested time.
1. **Session ID**: This is the unique ID for the OOD session for this job, which can be clicked to access the OOD log directory for troubleshooting.
1. **Node, Cores and State**: Information about the number of node, cores assignment, and state of the job.
1. **Launch Desktop in new tab**: Click this button to open your interactive VNC session.
1. **Delete**: Click this button if you want to cancel/stop a running job, and/or delete the session if the job has already ended.
1. **View Only (Share-able Link)**: Click this button to share the URL of your job with someone. It allows them to watch as you interact with the program and assist you. However, they can only view and cannot control or enter any data.

The Job ID and Session ID are important for diagnosing issues you may encounter on Cheaha while using Open OnDemand. These interactive jobs can be stopped early by clicking the `Delete` button on the job card.

<!-- markdownlint-disable MD046 -->
!!! bug

    If your job fails to launch, see [debugging OOD jobs](#debugging-ood-job-failures) for instructions on how to access OOD job data and submit a support ticket.
<!-- markdownlint-enable MD046 -->

#### Debugging OOD Job Failures

On occasion, interactive jobs created in OOD will crash on startup and cause the job card to disappear. Most of these failures are caused by improper environment setup prior to job creation. To troubleshoot OOD applications, retrieving logs from failed jobs is essential. These logs are stored in `/data/user/$USER/ondemand/batch_connect/sys`, but each log directory is named using a hash value rather than a recognizable `JobID`, making it difficult to identify logs for a specific job after it has ended. To retrieve the correct log directory, use the following command:

`sacct -j <jobid> -o jobid,workdir --parsable`

This command retrieves the job's working directory, where the logs are stored. Replace `<jobid>` with the failed job ID when running the command. Then, you can download the logs, zip them, and attach the ZIP file to a support ticket for our review. If you are unable to run the `sacct` command, please email <support@listserv.uab.edu>, and we will provide you with the necessary download link.

Alternatively, you can create a new job and follow the steps below to retrieve and submit the log files.

1. Create a new job with the same setup as the job that failed.
1. When the job is in queue, click the link in the `Session ID` field in the job card before the job fails (see the image below for an example). This will open a file browser in a new tab.

    ![!Example Session ID Link](images/example_session_id_link.png)

1. Wait for the job to fail. Afterwards, refresh the file browser, select all of the files (do not include the `desktops` or `..` folders), and click `Download`.

    ![!Files to be downloaded and attached to the email](images/ood_failed_job.png)

1. Take all of the files that were downloaded, put them in a new folder, and zip the folder.

[Submit a ticket](../../index.md#how-to-contact-us) to us explaining the issue with the zip folder created in Step 4 attached to the email, and we will be happy to assist. If you would like to inspect the log yourself for debugging, the `output.log` typically will contain the relevant error messages.
