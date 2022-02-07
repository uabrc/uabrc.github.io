# Detailed Hardware Information

## Node Summary

The current HPC cluster is comprised of 8192 compute cores connected by low-latency Fourteen Data Rate (FDR) and Enhanced Data Rate (EDR) InfiniBand networks. In addition to the basic compute cores, there are also 72 NVIDIA Tesla P100 GPUs available.

A description of the different hardware generations are summarized in the following table:

{{ read_csv('resources/data/hardware_short_df.csv') }}

## TFLOPS

The table below is a theoretical analysis based on processor instructions and core counts, and is not a reflection of efficiency in practice.

{{ read_csv('resources/data/tflops_df.csv') }}
