# Software Installation

<!-- markdownlint-disable MD046 -->
!!! construction

    This page is a stub and is under construction.
<!-- markdownlint-enable MD046 -->

## Anaconda on Cheaha

This page details specific information for using Anaconda on [Cheaha](../getting_started.md).

For general information on usage please see [Anaconda Environments](../../workflow_solutions/using_anaconda.md).

### Loading Anaconda

Anaconda is installed on Cheaha as a family of modules, and does not need to be installed by Researchers. Instead, the most recent version of Anaconda installed on Cheaha may be loaded using the command `module load Anaconda3`. Other versions may be discovered using the command `module avail Anaconda`. We recommend always using the latest version.

### Using Anaconda

Anaconda on Cheaha works like it does on any other system, once the module has been loaded, with a couple of important differences in the callouts below.

<!-- markdownlint-disable MD046 -->
!!! note

    The `base` environment is installed in a shared location and cannot be modified by researchers. Other environments are installed in your home directory by default.
<!-- markdownlint-enable MD046 -->

<!-- markdownlint-disable MD046 -->
!!! warning

    The Cheaha operating system has a version of Python installed. This version is used by `python` calls when Anaconda has not been loaded.
<!-- markdownlint-enable MD046 -->

<!-- markdownlint-disable MD046 -->
!!! danger

    Do not use `conda init` on Cheaha! Anaconda is managed as a [module](./modules.md), including script setup. Using `conda init` can cause hard-to-diagnose issues with [Open OnDemand Interactive Jobs](../open_ondemand/ood_interactive.md). Please see our [FAQ](../../help/faq.md#why-do-i-get-an-error-when-i-try-to-launch-an-hpc-interactive-session) for how to undo what `conda init` does.
<!-- markdownlint-disable MD046 -->

For more information on usage with examples, see [Anaconda Environments](../../workflow_solutions/using_anaconda.md).

### Speedups Using Mamba

[Mamba](../../workflow_solutions/using_anaconda.md#speeding-things-up-with-mamba) is not installed in the base environment on Cheaha, and cannot be installed in the base environment by researchers. We are working on installing Mamba in the base environment as part of our module installation process change. In the meantime if you need the speed Mamba provides, you can follow these instructions to make it available for yourself.

1. `module load Anaconda3`
2. Create a new environment with only Mamba using `conda create --name mamba -c conda-forge mamba`
3. `conda activate mamba`
4. Use Mamba to install environments as needed. Be aware you must use the flag `--prefix=~/.conda/envs/` to put the environment in the correct location to be seen by Anaconda.

## Open On Demand Sandbox App
