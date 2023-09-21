# GPUs

## Available Devices

Cheaha has GPUs available with the following statistics, broken out by [Slurm Partition](../slurm/introduction.md). For more information on all available partitions, see our [Hardware Summary](../hardware.md#summary).

{{ read_csv('cheaha/slurm/res/gpu_devices.csv', keep_default_na=False) }}

For more information on these nodes, see `Detailed Hardware Information`.

## Scheduling GPUs

To submit a job with one or more GPUs, you will need to set the partition to `pascalnodes` or `amperenodes` family of partitions for P100 GPUs or `amperenodes` family for A100 GPUs.

When requesting a job using `sbatch`, you will need to include the Slurm flag `--gres=gpu:#`. Replace `#` with the number of GPUs you need. Quotas and constraints are available on our [Hardware Summary](../hardware.md#summary)

<!-- markdownlint-disable MD046 -->
!!! note

    It is suggested that at least 2 CPUs are requested for every GPU to begin with. The user should monitor and adjust the number of cores on subsequent job submissions if necessary. Look at [Managing Jobs](./job_management.md#managing-jobs) for more information.
<!-- markdownlint-enable MD046 -->

## Ensuring IO Performance With A100 GPUs

If you are using `amperenodes` and the A100 GPUs, then it is highly recommended to move your input files to `/local/$SLURM_JOB_ID` prior to running your workflow, to ensure adequate GPU performance. Using `$USER_SCRATCH`, or other network file locations, will starve the GPU of data, resulting in poor performance.

The following script can be used to wrap your existing workflows. It will automatically create a temporary directory `$TMPDIR` and delete it when your workflow is finished. You'll need to supply the original source of your data as `$MY_DATA_DIR`. The script is not guaranteed to delete the temporary directory if the job ends before it reaches the final line, so please be mindful and periodically check for any extra temporary directories and delete them as needed.

```bash
#!/bin/bash
#SBATCH ...
#SBATCH --partition=amperenodes
#SBATCH --gres=gpu:1

# LOAD CUDA MODULES
module load CUDA/12.1.1
module load cuDNN/12.1.1

# CREATE TEMPORARY DIRECTORY
# WARNING! $TMPDIR will be deleted at the end of the script!
# Changing the following line can cause permanent, unintended deletion of important data.
TMPDIR="/local/$USER/$SLURM_JOB_ID"
mkdir -p "$TMPDIR"

# COPY RESEARCH DATA TO LOCAL TEMPORARY DIRECTORY
# Replace $MY_DATA_DIR with the path to your data folder
cp -r "$MY_DATA_DIR" "$TMPDIR"

# YOUR ORIGINAL WORKFLOW GOES HERE
# be sure to load files from "$TMPDIR"!

# CLEAN UP TEMPORARY DIRECTORY
# WARNING!
# Changing the following line can cause permanent, unintended deletion of important data.
rm -rf "$TMPDIR"
```

### Open OnDemand

When requesting an interactive job through `Open OnDemand`, selecting the `pascalnodes` partitions will automatically request access to one GPU as well. There is currently no way to change the number of GPUs for OOD interactive jobs.

#### MATLAB

To use GPUs with our [Open OnDemand](../open_ondemand/ood_interactive.md) MATLAB app, you may need to take a slightly different route than usual.

If you are using MATLAB R2022a or newer, then our `pascalnodes` P100 GPUs and `amperenodes` A100 GPUs should work without any additional steps.

If you are using R2021b and earlier, then follow the instructions below.

1. Start an [HPC Interactive Desktop Job](../open_ondemand/ood_interactive.md) with appropriate resources. Be sure to use one of the `pascalnodes*` [Partitions](#scheduling-gpus).
2. Open a terminal.
3. Load the appropriate [CUDA Module](#cuda-modules).
    - Determine which CUDA Modules are compatible with your required version of MATLAB using the table at the [MathWorks Site](https://www.mathworks.com/help/releases/R2021b/parallel-computing/gpu-support-by-release.html).
    - Check the `Pascal (cc6.x)` column for the `pascalnodes` P100 GPUs and `Ampere (cc8.x)` column for the `amperenodes` A100 GPUs.
    - As of September, 2023, `module load CUDA/11.6.0` and newer should work fine with any version of MATLAB R2021b or older, with possible caveats for some functions.
4. Load the appropriate MATLAB [Module](../software/modules.md).
5. Start MATLAB by entering the command `matlab`.
6. When MATLAB loads, enter the command `gpuDevice` in the MATLAB Command Window to verify it can identify the GPU.

For more information and official MATLAB documentation please see this page: <https://www.mathworks.com/help/parallel-computing/gpu-computing-requirements.html>.

## CUDA Modules

You will need to load a CUDA module to make use of GPUs on Cheaha. Depending on which version of software you are using, different versions of CUDA module may be required. For instance, tensorflow version `2.13.0` requires the `CUDA/11.8.0` module. To see which versions are available on Cheaha, use the following command at the terminal.

``` bash
module -r spider 'CUDA/*'
```

If a specific version of CUDA is needed but not installed, please send an install request to <support@listserv.uab.edu>.

### cuDNN Modules

If working with deep neural networks (DNNs, CNNs, LSTMs, LLMs, etc.), you will need to load a `cuDNN` module as well. The `cuDNN` modules are built to be compatible with a sibling `CUDA` module and are named with the corresponding version. For example, if you are loading `CUDA/12.2.0`, you will also need to load `cuDNN/8.9.2.26-CUDA-12.2.0`.

### Tensorflow Compatibility

To check which CUDA Module version is required for your version of Tensorflow, see the toolkit requirements chart here <https://www.tensorflow.org/install/source#gpu>.

### PyTorch Compatibility

PyTorch does not maintain a simple compatibility table for CUDA versions. Instead, please manually check their ["get started" page](https://pytorch.org/get-started/locally/#start-locally) for the latest PyTorch version compatibility, and their ["previous versions" page](https://pytorch.org/get-started/previous-versions/) for older PyTorch version compatibility. Assume that a CUDA version is not compatible if it is not listed for a specific PyTorch version.

To use GPUs prior to PyTorch version 1.13 you _must_ select a `cudatoolkit` version from the PyTorch channel when you install PyTorch using Anaconda. It is how PyTorch knows to install a GPU compatible flavor, as opposed to the CPU only flavor. See below for templates of CPU and GPU installs for PyTorch versions prior to 1.13. Be sure to check the compatibility links above for your selected version. Note `torchaudio` is also available for signal processing.

- CPU Version: `conda install pytorch==... torchvision==... -c pytorch`
- GPU Version: `conda install pytorch==... torchvision==... cudatoolkit=... -c pytorch`

For versions of PyTorch 1.13 and newer, use the following template instead.

- CPU Version: `conda install pytorch==... torchvision==... cpuonly -c pytorch`
- GPU Version: `conda install pytorch==... torchvision==... pytorch-cuda=... -c pytorch -c nvidia`

## Reviewing GPU Jobs

As with all jobs, use [`sacct`](job_management.md#reviewing-past-jobs-with-sacct) to review GPU jobs. Quantity of GPUs may be reviewed using the `reqtres` and `alloctres` [fields](job_management.md#sacct-fields).
