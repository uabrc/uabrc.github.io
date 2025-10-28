# Starting Up With UAB Kubernetes

<!-- markdownlint-disable MD046 -->
!!! note

    Kubernetes is not yet available as a service to our research community, but we are putting the infrastructure and system in place to provide this. If you would like to help us test and explore our UAB Research Computing Kubernetes Instance please [contact us](../index.md#how-to-contact-us)
<!-- markdownlint-enable MD046 -->

<!-- markdownlint-disable MD046 -->
!!! construction

    This page is a stub and is under construction.
<!-- markdownlint-enable MD046 -->

## UAB Kubernetes Computation Resources

- 4 DGX A100 nodes
    - GPUs aren’t virtualized, but one DGX node can be split into 1/7th of a GPU
    - 8 A100s per DGX node * 7/7ths = 56/7ths of a GPU possible
    - Can be used for classes learning to use GPUs
- Finding containers to use
    - K8s will search DockerHub and other container registries automagically.
    - Can add additional registries
