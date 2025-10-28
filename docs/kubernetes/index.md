# UAB Kubernetes

With the rise of containerization and cloud-native application and uses, Kubernetes is gaining interest as a complementary or alternative solution to research workflow needs. As a result UAB Research Computing will be rolling out a Kubernetes platform for our research community in the near future. See below why you may want to use Kubernetes for your research workflow.

<!-- markdownlint-disable MD046 -->
!!! note

    Kubernetes is not yet available as a service to our research community, but we are putting the infrastructure and system in place to provide this. If you would like to help us test and explore our UAB Research Computing Kubernetes Instance please [contact us](../index.md#how-to-contact-us)
<!-- markdownlint-enable MD046 -->

## What Is Kubernetes?

Kubernetes (also known as `K8s`, named because there are 8 letters between 'K' and 's') can be used to automate workflows of all kinds. K8s are usually open-source systems for automating deployment, scaling and managing containerized applications. Think of it as an operating system for a cluster of computers, giving you the tools to run your research software in reliable, scalable, and portable ways.

## Why Use Kubernetes?

Below are some widely known benefits/uses of Kubernetes for researchers;

1. **Reproducible Environments:** As researchers, you can now easily run applications in [Singularity containers](../workflow_solutions/getting_containers.md), ensuring seamless collaborations and reproducibility across labs, projects and platforms. Code, dependencies, and packages can be built into container environments that can be easily reproduced to ensure workflows are replicated exactly the same. Reducing the age long problem of "It works for me with my setup".

1. **Quicker Environment Setups:** Kubernetes will give you on-demand access to isolated, fully configured environments that you can launch yourself. Whether it’s a Jupyter notebook with pre-installed libraries, a containerized web app, or an RStudio server instance, Kubernetes allows researchers to spin up tools in seconds to meet your needs.

1. **Collaborate Everywhere:** With Kubernetes, you can use many of the popular research interfaces through a browser. For example, [JupyterHub on Kubernetes](https://z2jh.jupyter.org/en/latest/#zero-to-jupyterhub-with-kubernetes) enables each researcher to access a personalized notebook environment over the web. Others like VSCode Server, RStudio, or custom data dashboards can also be deployed with minimal effort. This flexibility makes Kubernetes ideal for remote collaboration.

1. **Better Resource Usage:** Kubernetes instances will schedule jobs across available resources by dynamically allocating or scaling back resources depending on what's available and what each workflow needs. This leads to higher efficiency and avoids over-provisioning. Idle jobs are automatically terminated or paused, freeing up resources for others. For researchers, this means shorter wait times and a smoother experience for everyone.

1. **AI/ML Workloads:** Kubernetes shines in deploying scalable Jupyter, R, TensorFlow, PyTorch, and GPU-enabled jobs. Projects like [Kubeflow](https://www.kubeflow.org/docs/started/introduction/#what-is-kubeflow) make it easy to manage the full Machine Learning (ML) lifecycle, from data preparation to training, validation, and serving models all inside Kubernetes. For researchers working with AI models, it provides a highly efficient, scalable platform that traditional schedulers don’t easily support.
