# Detailed Hardware Information

## Partitions

{{ read_csv('cheaha/res/partition.csv', keep_default_na=False) }}

Notes:

- Express jobs are highest priority in scheduling meaning they will be scheduled faster
- Most partitions have a max amount of requestable memory per node at 175 GB. Largemem has a maximum memory limit of 1.5 TB.
- Pascalnodes are specifically used for access to GPUs
- Each user has a maximum amount of requestable resources across all jobs. Submitted jobs beyond this resource limit will be kept in the queue until a user's prior jobs have completed. This will appear as `QOSMaxResourceLimit` in your `squeue` list.
- If a script finishes executing before the requested time limit, the job will automatically close and resources will be released. However requesting the max amount of time will cause scheduler priority to decrease.

## Node Summary

The current HPC cluster is comprised of 8192 compute cores connected by low-latency Fourteen Data Rate (FDR) and Enhanced Data Rate (EDR) InfiniBand networks. In addition to the basic compute cores, there are also 72 NVIDIA Tesla P100 GPUs available.

A description of the different hardware generations are summarized in the following table:

{{ read_csv('cheaha/res/hardware_short_df.csv', keep_default_na=False) }}

## TFLOPS

The table below is a theoretical analysis based on processor instructions and core counts, and is not a reflection of efficiency in practice.

{{ read_csv('cheaha/res/tflops_df.csv', keep_default_na=False) }}
