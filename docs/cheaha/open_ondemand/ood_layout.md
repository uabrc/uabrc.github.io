# Navigating Open OnDemand

After creating your Cheaha account, going to [rc.uab.edu](https://rc.uab.edu) will take you to the Open OnDemand (OOD) homepage:

![!Landing page for Open OnDemand.](./images/ood_homepage.png)

The landing page contains information about current updates to the system, a message of the day with links to our support email and documenation, as well as a helpful [partition table](../getting_started.md#partitions) to help you determine which partition to submit your jobs to. You can access all of the different features of OOD using the navigation tabs at the top of the screen. The most commonly used features are covered below.

## File Browser

You can open a file browser in a new tab by clicking the `Files` dropdown and selecting which default directory you would like to access from `HOME`, `USER_DATA`, or `USER_SCRATCH`.

<!-- markdownlint-disable MD046 -->
!!! note

    `USER_SCRATCH` is shown as both `/scratch` and `/data/scratch`. `/data/scratch` is just a symbolic link to `/scratch`. You can use either, but `/scratch` is preferred since it's an actual folder instead of a symlink.
<!-- markdownlint-enable MD046 -->

![!Basic file browser for OOD.](./images/file_browser.png)

You can see the current working directory at the top (green) along with its file and folder list (black). There are also control bars for both working with files (blue) as well as the file browser itself (orange).

### OOD Command Menu

#### Uploading Data

Data can be uploaded from your local machine using this interface. Use the `Upload` button in the OOD Command Menu at the top right to select files from your local browser.

<!-- markdownlint-disable MD046 -->
!!! important

    This should be limited to small files only (< 1 MB). For large files or datasets, please use [Globus](../../data_management/transfer/globus.md) instead.
<!-- markdownlint-enable MD046 -->

#### Opening a Terminal

You can also open a bash terminal in the current directory using the `>_Open in Terminal` command. This should only be used for small tasks since the terminal is running on the login node. For compute-intensive tasks, either request an interactive session in the terminal or request an HPC Desktop session through the Interactive Apps and use the terminal there.

#### Show Dotfiles

Selecting the `Show Dotfiles` option will show the hidden files (those beginning with `.`) in the current folder.

#### Show Owner

Selecting the `Show Owner/Mode` option will show the permissions for the files in the working directory. These permissions (`mode`) can be used to investigate permission issues in shared spaces like `/data/project` directories. The `owner` column shows the Unix ID for the user who owns the file or directory. There is not a known way to change it to the username so its use is limited.

## Interactive Apps

There are two tabs used to interact with applications in OOD, the Interactive Apps dropdown, used to select resources and start jobs, and the My Interactive Sessions tab, used to view currently running interactive apps. The Interactive Apps dropdown has a list of specific software setup to run on Cheaha that you can interact with through a browser window such as RStudio, MATLAB, and Jupyter. There is also an HPC Desktop app that provides a general VNC desktop to run all available software on Cheaha. See the [quickstart](index.md#quickstart) for how to create an example HPC Desktop job. Below, you can see a general form for selecting job resources.

![!A general form for selecting interactive job resources](images/ood_general_resources_form.png)

The interactive apps have the following fields to customize the resources for your job:

1. Number of Hours: the maxmimum number of hours the job will run for. Interactive apps will stay allocated for this amount of time unless the job is manually deleted or crashes. The selected number of hours should be less than or equal to the max runtime for your selected partition.
2. Partition: the partition the job will be allocated in. See [here](../getting_started.md#partitions) for more information about which partition to choose for your job.
3. Number of GPUs: Total number of GPUs to request (max of 4 on pascalnodes or 2 on amperenodes)
4. Numer of CPUs: Total number of CPUs to request
5. Memory Per CPU (GB): GB of memory multiplied by the requested number of CPUs.

Every interactive app has resources only allocated on a single node, so make sure the amount of memory you request is less than or equal to the max amount per node for the partition you choose. You can find a table with the memory values per node in a partition in our [hardware page](../hardware.md#cheaha-hpc-cluster)

### Environment Setup Window

In addition to requesting general resources, for some apps you will have the option to add commands to be run during job startup in an Environment Setup Window. See below for an example showing how to load CUDA into a Jupyter job so it can use a GPU.

![! Example environment setup window showing how to load CUDA into a Jupyter job](./images/ood_environment_setup_window.png)

For jobs such as RStudio and Jupyter, some modules like CUDA need to be loaded beforehand so the application has access to it. This can also include loading compiler modules such as CMake and GCC for compiling package installations or editing your `$PATH` specifically for the interactive app without needing to edit your `.bashrc`. See the software specific pages for more examples on how to use the Environment Setup.

### Debugging OOD Job Failures

On occasion, interactive jobs created in OOD will crash on startup and cause the job card to disappear. Most of these failures are caused by improper environment setup prior to job creation. If you experiencing OOD job failures, retrieve the OOD job info using the following steps:

1. Create a new job with the same setup as the job that failed.
2. When the job is in queue, click the link in the `Session ID` field in the job card before the job fails (see the image below for an example). This will open a file browser in a new tab.

    ![!Example Session ID Link](images/example_session_id_link.png)

3. Wait for the job to fail. Afterwards, refresh the file browser, select all of the files (do not include the `desktops` or `..` folders), and click `Download`.
4. Take all of the files that were downloaded, put them in a new folder, and zip the folder.

[Submit a ticket](../../index.md#how-to-contact-us) to us explaining the issue with the zip folder created in Step 4 attached to the email, and we will be happy to assist. If you would like to inspect the log yourself for debugging, the `output.log` typically will contain the relevant error messages.