# Software Installation

## `conda` on Cheaha

For additional general information on using `conda` please see our [Using `conda` page](../../workflow_solutions/using_conda.md).

If you are using Jupyter Notebook, please see our section on [Packages for Jupyter](../../workflow_solutions/using_conda.md#packages-for-jupyter).

### Loading `conda`

`conda` is installed on Cheaha as a family of modules, and does not need to be installed by Researchers. Instead, the most recent version of `conda` installed on Cheaha may be loaded using the command `module load Miniforge3`.

<!-- markdownlint-disable MD046 -->
!!! note

    If you are using [Open OnDemand Jupyter Notebook](../open_ondemand/ood_jupyter.md) you should not use the `module load` command as part of creating the job.
<!-- markdownlint-enable MD046 -->

### Using `conda`

Once you have loaded the Miniforge module, `conda` on Cheaha works similarly to how it does on other computers. There are a couple of important differences in the callouts below.

<!-- markdownlint-disable MD046 -->
!!! note

    The `base` environment is installed in a shared location and cannot be modified by researchers. Other environments are installed in your home directory by default at `/home/$USER/.conda/`.
<!-- markdownlint-enable MD046 -->

<!-- markdownlint-disable MD046 -->
!!! important

    Only create `conda` environments on compute nodes. Environment creation consumes substantial resources and should not be run on the login node.
<!-- markdownlint-enable MD046 -->

<!-- markdownlint-disable MD046 -->
!!! warning

    The Cheaha operating system has a built-in Python version installed. This version is used by `python` calls when Miniforge has not been loaded. This can cause unexpected errors. Be sure you've loaded the Miniforge module before using Python.
<!-- markdownlint-enable MD046 -->

<!-- markdownlint-disable MD046 -->
!!! danger

    Do not use `conda init` on Cheaha, even if prompted to do so!

    `conda` is managed on Cheaha via the [module](./modules.md) `Miniforge3`, including script setup. Using `conda init` at any point can cause hard-to-diagnose issues with [Open OnDemand Interactive Jobs](../open_ondemand/ood_layout.md#interactive-apps). Please see [this ask.ci FAQ](https://ask.cyberinfrastructure.org/t/why-do-i-get-an-error-when-launching-an-open-ondemand-hpc-interactive-session/2496/2) for how to undo what `conda init` does.

    If the `conda` software instructs you to use `conda init` while on Cheaha, please ignore it to avoid future issues with [Open OnDemand](../open_ondemand/index.md).
<!-- markdownlint-enable MD046 -->

<!-- markdownlint-disable MD046 -->
!!! danger

    Using `pip install` without loading Miniforge3 will cause hard-to-diagnose errors and broken workflows.

    Using `pip install` in the `base` environment will cause the same hard-to-diagnose errors and broken workflows.

    Read more about this issue, and how to resolve it, [here](#installing-pip-packages-outside-of-your-environments).
<!-- markdownlint-enable MD046 -->

For more information on usage with examples, see [`conda` Environments](../../workflow_solutions/using_conda.md). Need some hands-on experience? You can find instructions on how to install PyTorch and TensorFlow using `conda` in this [tutorial](../tutorial/pytorch_tensorflow.md).

### Installing Pip Packages Outside of Your Environments

When installing packages within a `conda` environment using `pip`, it's crucial to ensure that you install `pip` within the same conda environment and use `pip` from that environment. If `pip` is used outside of `conda` or within an environment without `pip` installed, the packages are installed to `~/.local`. This can lead to unexpected package conflicts, as Python loads packages from `~/.local` before loading from `conda` environments, and shows the following error,

```bash
Requirement already satisfied: numpy in /home/$USER/.local/lib/python3.11/site-packages (1.26.3)
```

For the above case, resolving errors involve deleting the `~/.local` directory.

Here's an example of the correct procedure for installing `pip` packages within a `conda`:

1. Load the `Miniforge` module using `module load Miniforge3`.
1. Create or activate the desired `conda` environment. Please refer to the [`conda` documentation](../../workflow_solutions/using_conda.md#create-an-environment)
1. Install `pip` within the `conda` environment using `conda install pip` or `conda install python`. `pip` and `python` are packaged together, installing one will always install the other.
1. Use `pip` when this `conda` environment is active to install packages. Please refer to [Installing packages with `pip`](../../workflow_solutions/using_conda.md#installing-packages-with-pip)

## Singularity Containers

Containers are a very useful resource for installing software without needing administrator permission. Please read the full documentation about singularity and containers on our [main Singularity page](../../workflow_solutions/getting_containers.md#containers-on-cheaha).
