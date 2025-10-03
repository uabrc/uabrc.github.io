# Hardware Information for Kubernetes Container Service

<!-- markdownlint-disable MD046 -->
!!! important

    The Kubernetes fabric is still in deployment and not ready for researcher use. We will be sure to inform you when the service is ready. The following information is planned hardware.
<!-- markdownlint-enable MD046 -->

The Kubernetes container service hardware consists of 5 Intel nodes and 4 DGX-A100 nodes. A description of the available hardware are summarized in the following table.

{{ read_csv('kubernetes/res/hardware_short_container.csv', keep_default_na=False) }}

The full table can be downloaded [here](./res/hardware_short_container.csv).

The table below is a theoretical analysis of FLOPS (floating point operations per second) based on processor instructions and core counts, and is not a reflection of efficiency in practice.

{{ read_csv('kubernetes/res/flops_container.csv', keep_default_na=False) }}

The full table can be downloaded [here](./res/flops_container.csv).
