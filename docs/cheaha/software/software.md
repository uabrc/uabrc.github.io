# Software Installation

## Anaconda on Cheaha

For additional general information on using Anaconda please see [Anaconda Environments](../../workflow_solutions/using_conda.md).

If you are using Jupyter Notebook, please see our section on [Packages for Jupyter](../../workflow_solutions/using_conda.md#packages-for-jupyter).

### Loading Anaconda

Anaconda is installed on Cheaha as a family of modules, and does not need to be installed by Researchers. Instead, the most recent version of Anaconda installed on Cheaha may be loaded using the command `module load Anaconda3`. Other versions may be discovered using the command `module avail Anaconda`. We recommend always using the latest version.

<!-- markdownlint-disable MD046 -->
!!! note

    If you are using [Open OnDemand Jupyter Notebook](../open_ondemand/ood_jupyter.md) you do not need to use the `module load` command as part of creating the job.
<!-- markdownlint-enable MD046 -->

### Using Anaconda

Anaconda on Cheaha works like it does on any other system, once the module has been loaded, with a couple of important differences in the callouts below.

<!-- markdownlint-disable MD046 -->
!!! note

    The `base` environment is installed in a shared location and cannot be modified by researchers. Other environments are installed in your home directory by default.
<!-- markdownlint-enable MD046 -->

<!-- markdownlint-disable MD046 -->
!!! important

    Only create environments on compute nodes. Anaconda environment creation consumes substantial resources and should not be run on the login node.
<!-- markdownlint-enable MD046 -->

<!-- markdownlint-disable MD046 -->
!!! warning

    The Cheaha operating system has a version of Python installed. This version is used by `python` calls when Anaconda has not been loaded. This can cause unexpected errors. Be sure you've loaded the Anaconda environment you need before using Python.
<!-- markdownlint-enable MD046 -->

<!-- markdownlint-disable MD046 -->
!!! danger

    Do not use `conda init` on Cheaha! Anaconda is managed as a [module](./modules.md), including script setup. Using `conda init` at any point can cause hard-to-diagnose issues with [Open OnDemand Interactive Jobs](../open_ondemand/ood_layout.md#interactive-apps). Please see [this ask.ci FAQ](https://ask.cyberinfrastructure.org/t/why-do-i-get-an-error-when-launching-an-open-ondemand-hpc-interactive-session/2496/2) for how to undo what `conda init` does.

    If the Anaconda software instructs you to use `conda init` while on Cheaha, please ignore it to avoid future issues with [Open OnDemand](../open_ondemand/index.md).
<!-- markdownlint-disable MD046 -->

For more information on usage with examples, see [Anaconda Environments](../../workflow_solutions/using_conda.md). Need some hands-on experience, you can find instructions on how to install PyTorch and TensorFlow using Anaconda in this [tutorial](../tutorial/pytorch_tensorflow.md).

## Singularity Containers

Containers are a very useful resource for installing software without needing administrator permission. Please read the full documentation about singularity and containers on our [main Singularity page](../../workflow_solutions/getting_containers.md#containers-on-cheaha).
