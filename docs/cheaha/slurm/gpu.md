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

To use GPUs with our [Open OnDemand MATLAB](../open_ondemand/ood_matlab.md) app, you may need to take a slightly different route than usual.

If you are using MATLAB R2022a or newer, then our `pascalnodes` P100 GPUs and `amperenodes` A100 GPUs should work without any additional steps.

If you are using R2021b and earlier, then follow the instructions below.

1. Start an [HPC Interactive Desktop Job](../open_ondemand/hpc_desktop.md) with appropriate resources. Be sure to use one of the `pascalnodes*` [Partitions](#scheduling-gpus).
1. Open a terminal.
1. Load the appropriate [CUDA Module](#cuda-modules).
    - Determine which CUDA Modules are compatible with your required version of MATLAB using the table at the [MathWorks Site](https://www.mathworks.com/help/releases/R2021b/parallel-computing/gpu-support-by-release.html).
    - Check the `Pascal (cc6.x)` column for the `pascalnodes` P100 GPUs and `Ampere (cc8.x)` column for the `amperenodes` A100 GPUs.
    - As of September, 2023, `module load CUDA/11.6.0` and newer should work fine with any version of MATLAB R2021b or older, with possible caveats for some functions.
1. Load the appropriate MATLAB [Module](../software/modules.md).
1. Start MATLAB by entering the command `matlab`.
1. When MATLAB loads, enter the command `gpuDevice` in the MATLAB Command Window to verify it can identify the GPU.

For more information and official MATLAB documentation please see this page: <https://www.mathworks.com/help/parallel-computing/gpu-computing-requirements.html>.

## CUDA Modules

You will need to load a CUDA module to make use of GPUs on Cheaha. Depending on which version of software you are using, different versions of CUDA module may be required. For instance, tensorflow version `2.13.0` requires the `CUDA/11.8.0` module. To see which versions are available on Cheaha, use the following command at the terminal.

``` bash
module -r spider 'CUDA/*'
```

If a specific version of CUDA is needed but not installed, please send an install request to <support@listserv.uab.edu>.

### cuDNN Modules

If working with deep neural networks (DNNs, CNNs, LSTMs, LLMs, etc.), you will need to load a `cuDNN` module as well. The `cuDNN` modules are built to be compatible with a sibling `CUDA` module and are named with the corresponding version. For example, if you are loading `CUDA/12.2.0`, you will also need to load `cuDNN/8.9.2.26-CUDA-12.2.0`.

### CUDA Compute Capability and Known Issues

GPU-based software requires a compatible [CUDA Compute Capability](../slurm/gpu.md/#available-devices) to function correctly. Each GPU card has a fixed CUDA Compute Capability version. For the software to run as expected, this version must be at least as large as the minimum CUDA Compute Capability required by the software; otherwise, the software will fail to run as expected, often resulting in runtime errors. Some of the known issues are reported in the [FAQ Entry](#frequently-asked-questions-faq-about-a100-gpus). For more information on CUDA Compute Capability, please refer [here](https://developer.nvidia.com/cuda-gpus).

<!-- markdownlint-disable MD046 -->
!!! note

    We recommend using the `amperenodes` partition for GPU software that requires a CUDA Compute Capability greater than 6.0 as the `pascalnodes` partition has a CUDA Compute Capability of 6.0.
<!-- markdownlint-disable MD046 -->

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

<!-- markdownlint-disable MD046 -->
!!! Note

     When loading modules, such as CUDA modules for jobs requiring one or more GPUs, always utilize `module reset` before loading modules, both at the terminal and within `sbatch` scripts. See [best practice for loading modules](../software/modules.md#best-practice-for-loading-modules) for more information.
<!-- markdownlint-disable MD046 -->

## Reviewing GPU Jobs

As with all jobs, use [`sacct`](job_management.md#reviewing-past-jobs-with-sacct) to review GPU jobs. Quantity of GPUs may be reviewed using the `reqtres` and `alloctres` [fields](job_management.md#sacct-fields).

## Frequently Asked Questions (FAQ) About A100 GPUs

- **I've been using the P100 GPUs on `pascalnodes` up until now, what is the easiest way to start using the A100 GPUs?**
    - If you are using an `sbatch` script...
        - Change `--partition=pascalnodes` to `--partition=amperenodes`, or change `--partition=pascalnodes-medium` to `--partition=amperenodes-medium`.
        - Also change `--gres=gpu:3` and `--gres=gpu:4` to `--gres=gpu:2`, as there are only two A100 GPUs per node.
    - If you are using an [Open OnDemand Interactive App](../open_ondemand/ood_layout.md#interactive-apps)...
        - Change the partition from "pascalnodes" to "amperenodes, or change "pascalnodes-medium" to "amperenodes-medium".
    - In all cases, be sure to read the section on [Ensuring IO Performance With A100 GPUs](#ensuring-io-performance-with-a100-gpus) to be sure disk read speed doesn't limit your performance gains.
- **How do I access the A100 GPUs?**
    You can access the A100 GPUs by request jobs in the appropriate partitions. Use `amperenodes` partition for up to 12 hours or `amperenodes-medium` partition for up to 48 hours.
- **How many GPUs can I request at once?**
    Up to four GPUs may be requested by any one researcher at once. However, there are only two GPUs per node, so requesting four GPUs will allocate two nodes. To make use of multiple nodes, your workflow software must know how to communicate between nodes using software like Horovod or OpenMPI. If you are new to GPUs and aren't sure you need multiple nodes, please limit your request to one or two gpus.
- **What performance improvements can I expect over the P100 GPUs?**
    Performance improvements depend on the software and algorithms being used. Determining optimal configuration will take some experimenting. Swapping a single P100 to a single A100, you can generally expect 3x to 20x improvement. For more information about possible performance improvements, please see the [Official NVIDIA A100 page](https://www.nvidia.com/en-us/data-center/a100/).
- **How can I make the most efficient use of the A100 GPUs?**
    A100s process data very rapidly compared with previous technology. Ideally, we want the A100 to be the bottleneck during processing, rather than CPUs or I/O operations. Here are two initial possibilities to consider for optimizing efficiency:
    - All researchers should copy their input data onto `/local/$SLURM_JOB_ID` (node-specific NVMe drives) before processing to avoid I/O bottlenecks reducing performance. See [Ensuring IO Performance With A100 GPUs](#ensuring-io-performance-with-a100-gpus).
    - Some researchers may benefit from using a larger number of CPU cores for data loading and preprocessing, compared with `pascalnodes`. Please consider experimenting with different numbers of CPU cores using the same dataset to find what is optimal for you. If you feel that performance should be higher, please contact [Support](../../help/support.md) so we can guide you toward an optimal CPU-to-GPU ratio for your application and workflow.
- **Where are the A100 nodes physically located, and will this impact my workflows?**
    The A100 nodes are located in the DC BLOX Data Center, west of UAB Campus. Because Cheaha storage (GPFS) is located on campus, there may be slightly higher latency when transferring data between the A100 nodes and GPFS. Impacts will only occur if very small amounts of data are transferred very frequently, which is unusual for most GPU workflows. We strongly recommend copying your input data onto `/local/$SLURM_JOB_ID` prior to processing, see [Ensuring IO Performance With A100 GPUs](#ensuring-io-performance-with-a100-gpus).
- **What will happen to the P100 GPUs?**
    We intend to retain all of the 18 existing P100 GPU nodes, of which  9 nodes are available now. The remaining 9 nodes have been temporarily taken offline as we reconfigure hardware, and will be reallocated based on demand and other factors.
- **What else should I be aware of?**
    - Please be sure to clean your data off of `/local/$SLURM_JOB_ID` as soon as you no longer need it, before the job finishes.
    - We have updated the CUDA and cuDNN modules to improve reliability and ease of use. Please see the section on [CUDA Modules](#cuda-modules) for more information.
    - GPU-based software, such as Parabricks, Triton, etc., requires a [CUDA Compute Capability](../slurm/gpu.md/#available-devices) greater than 6.0 for proper execution and should be run on the `amperenodes` partition. Some of the software that encountered runtime errors due to the underlying issues were,
        - [Parabricks](../../education/case_studies.md/#minimum-hardware-requirements-to-run-parabricks-on-cheaha-gpus)
        - [Triton](https://docs.nvidia.com/deeplearning/triton-inference-server/archives/triton_inference_server_1140/user-guide/docs/build.html#configure-triton-build)
