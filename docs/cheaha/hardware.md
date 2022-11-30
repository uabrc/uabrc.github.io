# Hardware Information

The following hardware summaries may be useful for grant proposal writing. If any information is missing that would be helpful to you, please be sure to [contact us](../index.md#contact-us) or create an issue on our [tracker](https://github.com/uabrc/uabrc.github.io/issues).

<!-- markdownlint-disable MD046 -->
!!! tip

    The tables in this section are wide and can be scrolled horizontally to display more information.
<!-- markdownlint-enable MD046 -->

## Cheaha HPC Cluster

The HPC cluster is comprised of 8192 compute cores connected by low-latency Fourteen Data Rate (FDR) and Enhanced Data Rate (EDR) InfiniBand networks. In addition to the basic compute cores, there are also 72 NVIDIA Tesla P100 GPUs available. There is a total of just under 49 TB of memory across the cluster. A description of the available hardware generations are summarized in the following table.

{{ read_csv('cheaha/res/hardware_short_hpc.csv', keep_default_na=False) }}

The full table can be downloaded [here](./res/hardware_short_hpc.csv).

The table below is a theoretical analysis of FLOPS (floating point operations per second) based on processor instructions and core counts, and is not a reflection of efficiency in practice.

{{ read_csv('cheaha/res/flops_hpc.csv', keep_default_na=False) }}

The full table can be downloaded [here](./res/flops_hpc.csv).

For information on using Cheaha, see our dedicated [section](index.md).

### Partitions

{{ read_csv('cheaha/res/partitions.csv', keep_default_na=False) }}

The full table can be downloaded [here](./res/partitions.csv).

### Quality of Service (QoS) Limits

Quality of Service (QoS) allows us to balance usage across the cluster, so that no single researcher can consume all of the resources. Each set of QoS limits is applied to one or more partitions according to the table below. Each limit is applied to every researcher on Cheaha. The partitions within a group all share the same limits, so that a researcher can use 1.5 TB on both `express` and `short`, but can't use 2 TB on both at the same time.

{{ read_csv('cheaha/res/qos.csv', keep_default_na=False) }}

The full table can be downloaded [here](./res/qos.csv).

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

## Full Hardware Details

Detailed hardware information including processor and GPU makes and models, core clock frequencies, and other information for current hardware are in the table below.

{{ read_csv('cheaha/res/hardware_full_all.csv', keep_default_na=False) }}

The full table can be downloaded [here](./res/hardware_full_all.csv).
