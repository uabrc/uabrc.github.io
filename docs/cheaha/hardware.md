# Hardware Information

The following hardware summaries may be useful for selecting partitions for workflows and for grant proposal writing. If any information is missing that would be helpful to you, please be sure to [contact us](../index.md#how-to-contact-us) or create an issue on our [tracker](https://github.com/uabrc/uabrc.github.io/issues).

<!-- markdownlint-disable MD046 -->
!!! tip

    The tables in this section are wide and can be scrolled horizontally to display more information.
<!-- markdownlint-enable MD046 -->

## Cheaha HPC Cluster

### Summary

The table below contains a summary of the computational resources available on Cheaha and relevant Quality of Service (QoS) Limits. QoS limits allow us to balance usage and ensure fairness for all researchers using the cluster. QoS limits are not a guarantee of resource availability.

In the table, [Slurm](./slurm/introduction.md) partitions are grouped by shared QoS limits on cores, memory, and GPUs. Node limits are applied to partitions independently. All limits are applied to researchers independently.

Examples of how to make use of the table:

- Suppose you submit 30 jobs to the "express" partition, and suppose each job needs 10 cores each. Hypothetically, in order for all of the jobs to start at once, 300 cores would be required. The QoS limit on cores is 264 on the "express" partition, so at most 26 jobs (260 cores) can start at once. The remaining 4 jobs will be held in queue, because starting one more would go beyond the QoS limit (270 > 264).
- Suppose you submit 5 jobs to the "medium" partition and 5 to the "long" partition, each requiring 1 node. Then, 10 total nodes would be needed. In this case, it is possible that all 10 jobs can start at once because partition node limits are separate. If all 5 jobs start, jobs on the "medium" partition.
- Suppose you submit 5 jobs to the "amperenodes" partition and 5 to "amperenodes-medium", for a total of 10 A100 GPUs. Additionally, you also submit 4 jobs to the "pascalnodes" partition totaling 8 P100 GPUs. Then 4 of the "gpu: ampere" group jobs can start at once, because the QoS limit is 4 GPUs there. Additionally, all 4 of the "gpu: pascal" group jobs, because the QoS limit is 8 GPUs there. In this case, the QoS for each group is separate.

{{ read_csv('cheaha/res/hardware_summary_cheaha.csv', keep_default_na=False) }}
<!-- fix headers -->

[Download the full table](./res/hardware_summary_cheaha.csv).

Information about GPU efficiency can be found at [Making the Most of GPUs](./slurm/gpu.md#making-the-most-of-gpus).

### Details

Detailed hardware information, including processor and GPU makes and models, core clock frequencies, and other information for current hardware are in the table below.

{{ read_csv('cheaha/res/hardware_full_all.csv', keep_default_na=False) }}

[Download the full table](./res/hardware_full_all.csv).

The table below is a theoretical analysis of FLOPS (floating point operations per second) based on processor instructions and core counts, and is not a reflection of efficiency in practice.

{{ read_csv('cheaha/res/flops_hpc.csv', keep_default_na=False) }}

[Download the full table](./res/flops_hpc.csv).

For information on using Cheaha, see our dedicated [section](./getting_started.md).
