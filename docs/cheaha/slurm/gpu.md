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

### Making the Most of GPUs

#### Ensuring IO Performance With A100 GPUs

If you are using `amperenodes` and the A100 GPUs, then it is highly recommended to move your input files to the [local scratch](../../data_management/cheaha_storage_gpfs/index.md#local-scratch) at `/local/$USER/$SLURM_JOB_ID` prior to running your workflow, to ensure adequate GPU performance. Network file mounts, such as `$USER_SCRATCH`, `/scratch/`, `/data/user/` and `/data/project/`, do not have sufficient bandwidth to keep the GPU busy. So, your processing pipeline will slow down to network speeds, instead of GPU speeds.

Please see our [Local Scratch Storage section](../../data_management/cheaha_storage_gpfs/index.md#local-scratch) for more details and an example script.

#### Using Multiple GPUs

<!-- markdownlint-disable MD046 -->
!!! note

    To effectively use multiple GPUs per node, you'll need to get in the mindset of doing some light unit canceling, multiplication, and division. Please be mindful.
<!-- markdownlint-enable MD046 -->

When using multiple GPUs on the `amperenodes*` or `pascalnodes*` partitions, an additional Slurm directive is required to ensure the GPUs can all be put to use by your research software: `--ntasks-per-socket`. You will need to explicitly set the `--ntasks` directive to an integer multiple of the number of GPUs in `--gres=gpu`, then set `--ntasks-per-socket` to the multiplier.

Most researchers, in most scenarios, should find the following examples to be sufficient. It is very important to note that `--ntasks-per-socket` times `--gres=gpu` equals `--ntasks` (1 times 3 equals 3). You will need to supply other directives, as usual, remembering that total CPUs is equal to `--cpus-per-task` times `--ntasks`, and that the total number of CPUs per node cannot exceed the actual number of physical cores on the node, and cannot exceed any quotas for the partition. See [Hardware](../hardware.md#cheaha-hpc-cluster) for more information about hardware and quota limits on Cheaha.

Pascalnodes:

```bash
#SBATCH --partition=pascalnodes   # up to 28 cpus per node
#SBATCH --ntasks-per-socket=1
#SBATCH --gres=gpu:4
#SBATCH --ntasks=4
#SBATCH --cpus-per-task=7         # 7 cpus-per-task times 4 tasks = 28 cpus
```

Amperenodes:

```bash
#SBATCH --partition=amperenodes   # up to 64 cpus per job
#SBATCH --ntasks-per-socket=1
#SBATCH --gres=gpu:2
#SBATCH --ntasks=2
#SBATCH --cpus-per-task=32        # 32 cpus-per-task times 2 tasks = 64 cpus
```

If `--ntasks-per-socket` is not used, or used incorrectly, it is possible that some of the GPUs requested may go unused, reducing performance and increasing job runtimes. For more information, please read the [GPU-Core Affinity Details](#gpu-core-affinity-details) below.

##### GPU-Core Affinity Details

Important terminology:

- **[node](https://en.wikipedia.org/wiki/Node_(networking)#Distributed_systems)**: A single computer in a cluster.
- **[mainboard](https://en.wikipedia.org/wiki/Motherboard)**: The central circuit board of a computer, where the components of the node all integrate.
- **[CPU](https://en.wikipedia.org/wiki/Central_processing_unit)**: Central Processing Unit, where general calculations are performed during operation of the node. Often contains multiple cores. Sometimes conflated with "core". We use the term "CPU die" in this section to avoid ambiguity.
- **[socket](https://en.wikipedia.org/wiki/CPU_socket)**: A connector on the mainboard for electrical connection to a CPU die. Some mainboards have a single socket, others have multiple sockets.
- **[core](https://en.wikipedia.org/wiki/Processor_core)**: A single physical processor of computer instructions. One core can carry out one computation at a time. Part of a CPU. Also called "processor core". Sometimes conflated with "CPU".
- **[GPU](https://en.wikipedia.org/wiki/Graphics_processing_unit)**: Graphics Processing Unit, trades off generalized computing for faster computation with a limited set of operations. Often used for AI processing. Contains many, specialied cores. Increasingly called "accelerator" in the context of clusters and high-performance computing (HPC).

Nodes in both the `amperenodes*` and `*pascalnodes` partition are configured as follows:

- Each node has a single mainboard.
- Each mainboard has two sockets.
- Each socket has a single CPU die.
- Each CPU die has multiple cores:
    - `amperenodes*`: 128 cores per CPU die
    - `pascalnodes*`: 28 cores per CPU die
- Each socket is connected with a subset of the GPUs:
    - `amperenodes*`: 1 GPU per socket (2 per mainboard)
    - `pascalnodes*`: 2 GPUs per socket (4 per mainboard)

Communication between each socket and its connected GPUs is relatively very fast. Communication between GPUs connected to different sockets is much slower, so we want to make sure that the Slurm knows which cores in each socket are associated with each GPU to allow for optimal performance of applications. The association between cores and GPUs is called "GPU-core affinity". Slurm is made explicitly aware of GPU-core affinity in the file located at `/etc/slurm/gres.conf`.

When a researcher submits an sbatch script, the use of `--ntasks-per-socket` informs slurm that tasks should be distributed across sockets, rather than the default behavior of "first available". Often, the default behavior results in all cores being allocated from a single socket, leaving some of the GPUs unavailable to your software, or with lower than expected performance.

To ensure the capability for optimal performance, ensure use of the `--ntasks-per-socket`.

### Open OnDemand

When requesting an interactive job through `Open OnDemand`, selecting the `pascalnodes` partitions will automatically request access to one GPU as well. There is currently no way to change the number of GPUs for OOD interactive jobs.

#### MATLAB

To use GPUs with our [Open OnDemand MATLAB](../open_ondemand/ood_matlab.md) app, you may need to take a slightly different route than usual.

If you are using MATLAB R2022a or newer, then our `pascalnodes` P100 GPUs and `amperenodes` A100 GPUs should work without any additional steps.

If you are using R2021b and earlier, then follow the instructions below.

1. Start an [HPC Interactive Desktop Job](../open_ondemand/hpc_desktop.md) with appropriate resources. Be sure to use one of the `pascalnodes*` [Partitions](#scheduling-gpus).
1. Open a terminal.
1. Load the appropriate [CUDA Module](#cuda-and-cudnn-modules).
    - Determine which CUDA Modules are compatible with your required version of MATLAB using the table at the [MathWorks Site](https://www.mathworks.com/help/releases/R2021b/parallel-computing/gpu-support-by-release.html).
    - Check the `Pascal (cc6.x)` column for the `pascalnodes` P100 GPUs and `Ampere (cc8.x)` column for the `amperenodes` A100 GPUs.
    - As of September, 2023, `module load CUDA/11.6.0` and newer should work fine with any version of MATLAB R2021b or older, with possible caveats for some functions.
1. Load the appropriate MATLAB [Module](../software/modules.md).
1. Start MATLAB by entering the command `matlab`.
1. When MATLAB loads, enter the command `gpuDevice` in the MATLAB Command Window to verify it can identify the GPU.

For more information and official MATLAB documentation please see this page: <https://www.mathworks.com/help/parallel-computing/gpu-computing-requirements.html>.

## CUDA and cuDNN Modules

You will need to load a CUDA module to make use of GPUs on Cheaha. Depending on which version of software you are using, different versions of CUDA module may be required. For instance, tensorflow version `2.13.0` requires the `CUDA/11.8.0` module. To see which versions are available on Cheaha, use the following command at the terminal.

``` bash
module -r spider 'CUDA/*'
```

As of 2025-02-25, we offer CUDA modules up to version `12.6.0`. If you need a newer version, please use [Conda](../software/software.md#anaconda-on-cheaha) to install CUDA software from the `conda-forge` channel. The packages and relevant commands to install into your newly created [environment](../../workflow_solutions/using_anaconda.md#create-an-environment) are available at the URLs in the following table. Note that you should use different packages depending on the CUDA version you need for your software!

{{ read_csv('cheaha/slurm/res/cuda_conda_package_versions.csv', keep_default_na=False) }}

If you are working with deep neural networks (DNNs, CNNs, LSTMs, LLMs, AI, etc.), you will also need to load a `cuDNN`. The `cuDNN` modules are built to be compatible with a sibling `CUDA` module and are named with the corresponding `CUDA` version. For example, if you are loading `CUDA/12.2.0`, you will also need to load `cuDNN/8.9.2.26-CUDA-12.2.0`. Note the trailing `12.2.0`.

As of 2025-02-25, we offer cuDNN modules for CUDA up to `12.3.0`. If you need a newer version, please use [Conda](../software/software.md#anaconda-on-cheaha) to install cuDNN software from the `conda-forge` channel. More details on how to install `CUDA` and `cuDNN` into your [environment](../../workflow_solutions/using_anaconda.md#create-an-environment) are available at <https://anaconda.org/conda-forge/cudnn>.

### CUDA Compute Capability and Known Issues

GPU-based software requires a compatible [CUDA Compute Capability](../slurm/gpu.md#available-devices) to function correctly. Each GPU card has a fixed CUDA Compute Capability version. For the software to run as expected, this version must be at least as large as the minimum CUDA Compute Capability required by the software; otherwise, the software will fail to run as expected, often resulting in runtime errors. Some of the known issues are reported in the [FAQ Entry](#frequently-asked-questions-faq-about-a100-gpus). For more information on CUDA Compute Capability please see the [official documentation](https://developer.nvidia.com/cuda-gpus).

<!-- markdownlint-disable MD046 -->
!!! note

    We recommend using the `amperenodes` partition for GPU software that requires a CUDA Compute Capability greater than 6.0 as the `pascalnodes` partition has a CUDA Compute Capability of 6.0.
<!-- markdownlint-disable MD046 -->

### Tensorflow Compatibility

To check which CUDA Module version is required for your version of Tensorflow, see the toolkit requirements chart here <https://www.tensorflow.org/install/source#gpu>.

<!-- markdownlint-disable MD046 -->
!!! note

    The latest CUDA and cuDNN are now available from [Conda](#cuda-and-cudnn-modules).
<!-- markdownlint-enable MD046 -->

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

<!-- markdownlint-disable MD046 -->
!!! note

    The latest CUDA and cuDNN are now available from [Conda](#cuda-and-cudnn-modules).
<!-- markdownlint-enable MD046 -->

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
    - All researchers should copy their input data onto `/local/$USER/$SLURM_JOB_ID` (node-specific NVMe drives) before processing to avoid I/O bottlenecks reducing performance. See [Ensuring IO Performance With A100 GPUs](#ensuring-io-performance-with-a100-gpus).
    - Some researchers may benefit from using a larger number of CPU cores for data loading and preprocessing, compared with `pascalnodes`. Please consider experimenting with different numbers of CPU cores using the same dataset to find what is optimal for you. If you feel that performance should be higher, please contact [Support](../../help/support.md) so we can guide you toward an optimal CPU-to-GPU ratio for your application and workflow.
- **Where are the A100 nodes physically located, and will this impact my workflows?**
    The A100 nodes are located in the DC BLOX Data Center, west of UAB Campus. Because Cheaha storage (GPFS) is located on campus, there may be slightly higher latency when transferring data between the A100 nodes and GPFS. Impacts will only occur if very small amounts of data are transferred very frequently, which is unusual for most GPU workflows. We strongly recommend copying your input data onto `/local/$USER/$SLURM_JOB_ID` prior to processing, see [Ensuring IO Performance With A100 GPUs](#ensuring-io-performance-with-a100-gpus).
- **What will happen to the P100 GPUs?**
    We intend to retain all of the 18 existing P100 GPU nodes, of which  9 nodes are available now. The remaining 9 nodes have been temporarily taken offline as we reconfigure hardware, and will be reallocated based on demand and other factors.
- **What else should I be aware of?**
    - Please be sure to clean your data off of `/local/$USER/$SLURM_JOB_ID` as soon as you no longer need it, before the job finishes.
    - We have updated the CUDA and cuDNN modules to improve reliability and ease of use. Please see the section on [CUDA Modules](#cuda-and-cudnn-modules) for more information.
    - GPU-based software, such as NVIDIA Clara Parabricks, Triton, etc., requires a [CUDA Compute Capability](../slurm/gpu.md#available-devices) greater than 6.0 for proper execution and should be run on the `amperenodes` partition. Some of the software that encountered runtime errors due to the underlying issues were,
        - [NVIDIA Clara Parabricks](../../education/case_studies.md#minimum-hardware-requirements-to-run-parabricks-on-cheaha-gpus)
        - [Triton](https://docs.nvidia.com/deeplearning/triton-inference-server/archives/triton_inference_server_1140/user-guide/docs/build.html#configure-triton-build)
