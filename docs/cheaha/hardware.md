# Hardware Information

The following hardware summaries may be useful for selecting partitions for workflows and for grant proposal writing. If any information is missing that would be helpful to you, please be sure to [contact us](../index.md#contact-us) or create an issue on our [tracker](https://github.com/uabrc/uabrc.github.io/issues).

<!-- markdownlint-disable MD046 -->
!!! tip

    The tables in this section are wide and can be scrolled horizontally to display more information.
<!-- markdownlint-enable MD046 -->

## Cheaha HPC Cluster

### Summary

The table below contains a summary of the computational resources available on Cheaha and relevant Quality of Service (QoS) Limits. QoS limits allow us to balance usage and ensure fairness for all researchers using the cluster. QoS limits are not a guarantee of resource availability.

In the table, [Slurm](./slurm/introduction.md) partitions are grouped by shared QoS limits on cores, memory, and GPUs. Node limits are applied to partitions independently. All limits are applied to researchers independently.

Examples of how to make use of the table:

- You submit 30 jobs to the "express" partition, requesting 10 cores each. If the first 26 jobs start, then 260 out of 264 core limit will be in use. The remaining 4 jobs will be held in queue, because starting one more would go beyond the QoS limit (270 > 264).
- You submit 5 jobs to the "medium" partition and 5 to the "long" partition. It is possible that all 10 jobs may start, because partition node limits are separate. If all 5 jobs start, jobs on the "medium" partition.
- You submit jobs to the "amperenodes" and "amperenodes-medium" partitions totaling 10 GPUs, and the "pascalnodes" partition totaling 4 GPUs. Jobs totaling 8 or fewer GPUs on the "gpu: ampere" group, and all jobs on "gpu: pascal", can start at the same time.

<!-- markdownlint-disable MD046 -->
!!! announcement

    Physical A100 nodes are slated for a future release on Cheaha. Information related to `amperenodes` and the A100 GPUs should be considered tentative information. The `amperenodes` hardware is not yet available as of 2023-08-22. Release date to be determined (TBD).
<!-- markdownlint-enable MD046 -->

{{ read_csv('cheaha/res/hardware_summary_cheaha.csv', keep_default_na=False) }}
<!-- fix headers -->

The full table can be downloaded [here](./res/hardware_summary_cheaha.csv).

### Details

Detailed hardware information, including processor and GPU makes and models, core clock frequencies, and other information for current hardware are in the table below.

{{ read_csv('cheaha/res/hardware_full_all.csv', keep_default_na=False) }}

The full table can be downloaded [here](./res/hardware_full_all.csv).

The table below is a theoretical analysis of FLOPS (floating point operations per second) based on processor instructions and core counts, and is not a reflection of efficiency in practice.

{{ read_csv('cheaha/res/flops_hpc.csv', keep_default_na=False) }}

The full table can be downloaded [here](./res/flops_hpc.csv).

For information on using Cheaha, see our dedicated [section](./getting_started.md).

## Cloud Service at cloud.rc

The Cloud service hardware consists of 5 Intel nodes and 4 DGX-A100 nodes. A description of the available hardware are summarized in the following table.

{{ read_csv('cheaha/res/hardware_short_cloud.csv', keep_default_na=False) }}

The full table can be downloaded [here](./res/hardware_short_cloud.csv).

The table below is a theoretical analysis of FLOPS (floating point operations per second) based on processor instructions and core counts, and is not a reflection of efficiency in practice.

{{ read_csv('cheaha/res/flops_cloud.csv', keep_default_na=False) }}

The full table can be downloaded [here](./res/flops_cloud.csv).

For information on using our Cloud service at cloud.rc, see our dedicated [section](../uab_cloud/index.md).

## Kubernetes Container Service

<!-- markdownlint-disable MD046 -->
!!! important

    The Kubernetes fabric is still in deployment and not ready for researcher use. We will be sure to inform you when the service is ready. The following information is planned hardware.
<!-- markdownlint-enable MD046 -->

The Kubernetes container service hardware consists of 5 Intel nodes and 4 DGX-A100 nodes. A description of the available hardware are summarized in the following table.

{{ read_csv('cheaha/res/hardware_short_container.csv', keep_default_na=False) }}

The full table can be downloaded [here](./res/hardware_short_container.csv).

The table below is a theoretical analysis of FLOPS (floating point operations per second) based on processor instructions and core counts, and is not a reflection of efficiency in practice.

{{ read_csv('cheaha/res/flops_container.csv', keep_default_na=False) }}

The full table can be downloaded [here](./res/flops_container.csv).
