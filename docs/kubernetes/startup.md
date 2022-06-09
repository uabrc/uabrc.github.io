# UAB Kubernetes

<!-- markdownlint-disable MD046 -->
!!! construction

    This page is a stub and is under construction.
<!-- markdownlint-enable MD046 -->

Kubernetes (K8s, named because there are 8 letters between 'K' and 's') can be used to automate workflows of all kinds. Researchers can use KSoftware engineers can use it to create GitLab runners to execute continuous integration workflows to deploy code updates seemlessly.

## UAB Kubernetes Computation Resources

- 4 DGX A100 nodes
    - GPUs aren’t virtualized, but one DGX node can be split into 1/7th of a GPU
    - 8 A100s per DGX node * 7/7ths = 56/7ths of a GPU possible
    - Can be used for classes learning to use GPUs
- Finding containers to use
    - K8s will search DockerHub and other container registries automagically.
    - Can add additional registries
