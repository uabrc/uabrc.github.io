# Detailed Hardware Information

## Node Summary

The current HPC cluster is comprised of 8192 compute cores connected by low-latency Fourteen Data Rate (FDR) and Enhanced Data Rate (EDR) InfiniBand networks. In addition to the basic compute cores, there are also 72 NVIDIA Tesla P100 GPUs available.

A description of the different hardware generations are summarized in the following table:

{{ read_csv('cheaha/res/hardware_short_df.csv', keep_default_na=False) }}

## TFLOPS

The table below is a theoretical analysis based on processor instructions and core counts, and is not a reflection of efficiency in practice.

{{ read_csv('cheaha/res/tflops_df.csv', keep_default_na=False) }}
