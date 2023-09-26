# Software Installation

## Anaconda on Cheaha

For additional general information on using Anaconda please see [Anaconda Environments](../../workflow_solutions/using_anaconda.md).

If you are using Jupyter Notebook, please see our section on [Packages for Jupyter](../../workflow_solutions/using_anaconda.md#packages-for-jupyter).

### Loading Anaconda

Anaconda is installed on Cheaha as a family of modules, and does not need to be installed by Researchers. Instead, the most recent version of Anaconda installed on Cheaha may be loaded using the command `module load Anaconda3`. Other versions may be discovered using the command `module avail Anaconda`. We recommend always using the latest version.

<!-- markdownlint-disable MD046 -->
!!! note

    If you are using [Open OnDemand Jupyter Notebook](../open_ondemand/ood_interactive.md#jupyter-notebook) you do not need to use the `module load` command as part of creating the job.
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

    Do not use `conda init` on Cheaha! Anaconda is managed as a [module](./modules.md), including script setup. Using `conda init` at any point can cause hard-to-diagnose issues with [Open OnDemand Interactive Jobs](../open_ondemand/ood_interactive.md). Please see [this ask.ci FAQ](https://ask.cyberinfrastructure.org/t/why-do-i-get-an-error-when-launching-an-open-ondemand-hpc-interactive-session/2496/2) for how to undo what `conda init` does.

    If the Anaconda software instructs you to use `conda init` while on Cheaha, please ignore it to avoid future issues with [Open OnDemand](../open_ondemand/ood_main.md).
<!-- markdownlint-disable MD046 -->

For more information on usage with examples, see [Anaconda Environments](../../workflow_solutions/using_anaconda.md).

### Speedups Using Mamba

[Mamba](../../workflow_solutions/using_anaconda.md#speeding-things-up-with-mamba) is a faster alternative to Anaconda, and is installed on Cheaha as a [module](modules.md). To use the latest version of Mamba on Cheaha, please use `module load Mamba` at the terminal and in your scripts.

There are currently a couple of known issues when working with Mamba on Cheaha.

1. After using `module load Mamba`, use `source activate` before any other `mamba` or `conda` commands.
2. Using `mamba init` can cause environment instability. Do _not_ use it.
3. Mamba alters the terminal prompt while a `mamba` environment is activated. The system should function as normal otherwise.

<!-- markdownlint-disable MD046 -->
!!! warning

    Do _not_ use `mamba init`, even when instructed to do so by Mamba. Doing so can result in environment instability. If you do use `mamba init` you can resolve the issue by removing the content added to your `.bashrc` file. Please visit [our FAQ](https://ask.cyberinfrastructure.org/t/why-do-i-get-an-error-when-launching-an-open-ondemand-hpc-interactive-session/2496/2) for more details.
<!-- markdownlint-enable MD046 -->

## Singularity Containers

Containers are a very useful resource for installing software without needing administrator permission. Please read the full documentation about singularity and containers on our [main Singularity page](../../workflow_solutions/getting_containers.md#containers-on-cheaha).
