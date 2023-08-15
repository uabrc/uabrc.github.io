# GPUs

## Available Devices

Currently, the Cheaha cluster has 18 nodes dedicated to GPU use under the `pascalnodes` partition family. Each node contains 4 individual NVIDIA P100 GPUs. These GPUs have the following specifications:

|                              |                                          |
| ---------------------------- | ---------------------------------------- |
| GPU Architecture             | **NVIDIA Pascal**                        |
| NVIDIA CUDA Cores            | **3584**                                 |
| GPU Memory                   | **16GB CoWoS HBM2 at 732 GB/s**          |
| Double-Precision Performance | **4.7 TeraFLOPS**                        |
| Single-Precision Performance | **9.3 TeraFLOPS**                        |
| Compute APIs                 | **CUDA, DirectCompute, OpenCL, OpenACC** |

For more information on these nodes, see `Detailed Hardware Information`.

## Scheduling GPUs

To successfully request access to GPUs, you will need to set the partition to one of the `pascalnodes` family of partitions depending on how much time you need for the job.

| Partition          | Time Limit |
| ------------------ | ---------- |
| pascalnodes        | 12 hours   |
| pascalnodes-medium | 50 hours   |

Additionally, when requesting a job using `sbatch`, you will need to include a SLURM directive `--gres=gpu:#` where `#` is the number of GPUs you need.

<!-- markdownlint-disable MD046 -->
!!! note

    It is suggested that at least 2 CPUs are requested for every GPU to begin with. The user should monitor and adjust the number of cores on subsequent job submissions if necessary. Look at [Managing Jobs](./job_management.md#managing-jobs) for more information.
<!-- markdownlint-enable MD046 -->

### Open OnDemand

When requesting an interactive job through `Open OnDemand`, selecting the `pascalnodes` partitions will automatically request access to one GPU as well. There is currently no way to change the number of GPUs for OOD interactive jobs.

#### MATLAB

To use GPUs with our [Open OnDemand](../open_ondemand/ood_interactive.md) MATLAB, you'll need to take a slightly different route than usual.

1. Determine which CUDA Toolkits are compatible with your required version of MATLAB using the table at the [MathWorks Site](https://www.mathworks.com/help/releases/R2021b/parallel-computing/gpu-support-by-release.html). The column `Pascal (cc6.x)` is relevant for our system.
2. Start an [HPC Interactive Desktop Job](../open_ondemand/ood_interactive.md) with appropriate resources. Be sure to use one of the `pascalnodes*` [Partitions](#scheduling-gpus).
3. Open a terminal.
4. Load the appropriate [CUDA Toolkit Module](#cuda-toolkit).
5. Load the appropriate MATLAB [Module](../software/modules.md).
6. Start MATLAB by entering the command `matlab`.
7. When MATLAB loads, enter the command `gpuDevice` in the MATLAB Command Window to verify it can identify the GPU.

For more information and official MATLAB documentation please see this page: <https://www.mathworks.com/help/parallel-computing/gpu-computing-requirements.html>.

## CUDA Toolkit

You will need to load a CUDA toolkit module for relevant commands to access the GPUs. Depending on which version of tensorflow, pytorch, or other similar software you are using, a different version of the CUDA toolkit may be required. For instance, tensorflow version 2.5.0 requires CUDA toolkit version 11.2.

Several CUDA toolkit versions have been installed as modules on Cheaha. To see which CUDA toolkits are available, use:

``` bash
module -r spider 'cuda.*toolkit'
```

If a specific version of the CUDA toolkit is needed but not installed, send an install request to <support@listserv.uab.edu>.

### cuDNN

NVIDIA drivers for their deep neural net toolbox are available in the cuDNN modules. Be aware that versions of cuDNN are not compatible with all installed versions of the CUDA toolkit, and no default version of the toolkit is loaded when loading a cuDNN module. The cuDNN module names have a CUDA version listed in the module name, i.e. `cuDNN/8.2.1.32-CUDA-11.3.1`. Please load the toolkit version matching the CUDA version in the cuDNN name, in this case `cuda11.3/toolkit`.

### Tensorflow Compatibility

To check which CUDA Toolkit module version is required for your version of Tensorflow, see the toolkit requirements chart here <https://www.tensorflow.org/install/source#gpu>.

### PyTorch Compatibility

PyTorch does not maintain a simple compatibility table for CUDA Toolkit versions. Instead, please manually check their ["get started" page](https://pytorch.org/get-started/locally/#start-locally) for the latest PyTorch version compatibility, and their ["previous versions" page](https://pytorch.org/get-started/previous-versions/) for older PyTorch version compatibility. Assume that a CUDA Toolkit version is not compatible if it is not listed for a specific PyTorch version.

To use GPUs prior to PyTorch version 1.13 you _must_ select a `cudatoolkit` version from the pytorch channel when you install PyTorch using Anaconda. It is how PyTorch knows to install a GPU compatible flavor, as opposed to the CPU only flavor. See below for templates of CPU and GPU installs for PyTorch versions prior to 1.13. Be sure to check the compatibility links above for your selected version. Note `torchaudio` is also available for signal processing.

- CPU Version: `conda install pytorch==... torchvision==... -c pytorch`
- GPU Version: `conda install pytorch==... torchvision==... cudatoolkit=... -c pytorch`

For versions of PyTorch 1.13 and newer, use the following template instead.

- CPU Version: `conda install pytorch==... torchvision==... cpuonly -c pytorch`
- GPU Version: `conda install pytorch==... torchvision==... pytorch-cuda=... -c pytorch -c nvidia`

## Reviewing GPU Jobs

As with all jobs, use [`sacct`](job_management.md#reviewing-past-jobs-with-sacct) to review GPU jobs. Quantity of GPUs may be reviewed using the `reqtres` and `alloctres` [fields](job_management.md#sacct-fields).
