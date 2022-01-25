# Detailed Hardware Information

## Node Summary

The current HPC cluster is comprised of 8192 compute cores connected by low-latency Fourteen Data Rate (FDR) and Enhanced Data Rate (EDR) InfiniBand networks. In addition to the basic compute cores, there are also 72 NVIDIA Tesla P100 GPUs available.

A description of the different hardware generations are summarized in the following table:

- Gen10: (planned Sep 2021) 34 nodes with 2x64 core (4352 cores totals) 2.0 GHz AMD Epyc 7713 Milan each with 512GB RAM.
- Gen9: 52 nodes with EDR InfiniBand interconnect: 2x24 core (2496 cores total) 3.0GHz Intel Xeon Gold 6248R compute nodes each with 192GB RAM.
- Gen8: 35 2x12 core (840 cores total) 2.60GHz Intel Xeon Gold 6126 compute nodes with 21 compute nodes at 192GB RAM, 10 nodes at 768GB RAM and 4 nodes at 1.5TB of RAM
- Gen7: 18 2x14 core (504 cores total) 2.4GHz Intel Xeon E5-2680 v4 compute nodes with 256GB RAM, four NVIDIA Tesla P100 16GB GPUs, and EDR InfiniBand interconnect (supported by UAB, 2017).

| Generation | Compute Type | Partition   | Total Cores | Total Memory GB | Total GPUs | Cores Per Node | Memory Per Node GB | Nodes | CPU Info                       | GPU Info                |
|------------|--------------|-------------|-------------|-----------------|------------|----------------|--------------------|-------|--------------------------------|-------------------------|
| 7          | gpu          | pascalnodes | 504         | 4608            | 72         | 28             | 256                | 18    | Intel Xeon E5-2680 v4 2.40 GHz | NVIDIA Tesla P100 16 GB |
| 8          | cpu          | cpu         | 504         | 4032            |            | 24             | 192                | 21    | Intel Xeon E5-2680 v4 2.50 GHz |                         |
| 8          | high memory  | largemem    | 240         | 7680            |            | 24             | 768                | 10    | Intel Xeon E5-2680 v4 2.50 GHz |                         |
| 8          | high memory  | largemem    | 96          | 6144            |            | 24             | 1536               | 4     | Intel Xeon E5-2680 v4 2.50 GHz |                         |
| 9          | cpu          | cpu         | 2496        | 9984            |            | 48             | 192                | 52    | Intel Xeon Gold 6248R 3.00 GHz |                         |
| 10         | cpu          | cpu         | 4352        | 17408           |            | 128            | 512                | 34    | AMD Epyc 7713 Milan 2.00 GHz   |                         |
| TOTAL      |              |             | 8192        | 49856           | 72         |                |                    | 139   |                                |                         |

## TFLOPS

The table below is a theoretical analysis based on processor instructions and core counts, and is not a reflection of efficiency in practice.

| Generation | CPU TFLOPS Per Node | GPU TFLOPS Per Node | TFLOPS Per Node | Nodes | TFLOPS |
|------------|---------------------|---------------------|-----------------|-------|--------|
| 7          | 1.08                | 17.06               | 18.14           | 18    | 326.43 |
| 8          | 0.96                |                     | 0.96            | 21    | 20.16  |
| 8          | 0.96                |                     | 0.96            | 10    | 9.60   |
| 8          | 0.96                |                     | 0.96            | 4     | 3.84   |
| 9          | 2.30                |                     | 2.30            | 52    | 119.81 |
| 10         | 4.10                |                     | 4.10            | 34    | 139.26 |
| TOTAL      |                     |                     |                 |       | 619.10 |
