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

[Mamba](../../workflow_solutions/using_anaconda.md#speeding-things-up-with-mamba) is not installed in the base environment on Cheaha, and cannot be installed in the base environment by researchers. We are working on installing Mamba in the base environment as part of our module installation process change. In the meantime if you need the speed Mamba provides, you can follow these instructions to make it available for yourself.

1. `module load Anaconda3`
2. Create a new environment with only Mamba using `conda create --name mamba -c conda-forge mamba`
3. `conda activate mamba`
4. Use Mamba to install environments as needed. Be aware you must use the flag `--prefix=~/.conda/envs/` to put the environment in the correct location to be seen by Anaconda.
