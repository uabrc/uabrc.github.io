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

!!! note

<!-- markdownlint-disable-next-line -->
    It is suggested that at least 2 CPUs are requested for every GPU to begin with. The researcher should monitor and adjust the number of cores on subsequent job submissions if necessary. Look at [Managing Jobs](job_management.md#managing-jobs) for more information.

### Open OnDemand

When requesting an interactive job through `Open OnDemand`, selecting the `pascalnodes` partitions will automatically request access to one GPU as well. There is currently no way to change the number of GPUs for OOD interactive jobs.

## CUDA Toolkit

You will need to load a CUDA toolkit module for relevant commands to access the GPUs. Depending on which version of tensorflow, pytorch, or other similar software you are using, a different version of the CUDA toolkit may be required. For instance, tensorflow version 2.5.0 requires CUDA toolkit version 11.2.

Several CUDA toolkit versions have been installed as modules on Cheaha. To see which CUDA toolkits are available, use:

``` bash
module -r spider 'cuda.*toolkit'
```

If a specific version of the CUDA toolkit is needed but not installed,
send an install request to [support@listserv.uab.edu].
