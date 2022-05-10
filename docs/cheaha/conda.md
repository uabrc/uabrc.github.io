# Anaconda

This page details specific information for using Anaconda on [Cheaha](../getting_started.md).

For general information on Anaconda usage, please see our [Environment Management/Anaconda page](../environment_management/conda.md).

## Loading Anaconda

Anaconda is installed on Cheaha as a family of modules, and does not need to be installed by Researchers. Instead, the most recent version of Anaconda installed on Cheaha may be loaded using the command `module load Anaconda3`. Other versions may be discovered using the command `module avail Anaconda`. We recommend always using the latest version.

## Using Anaconda

Anaconda works as expected once the module has been loaded, with a couple of important difference.

- The `base` environment is installed in a shared location and cannot be modified by researchers. Other environments are installed in your home directory by default.

<!-- markdownlint-disable MD046 -->
!!! danger

    Do not use `conda init` on Cheaha! Anaconda is managed as a [module](/docs/cheaha/lmod.md), including script setup. Using `conda init` can cause hard-to-diagnose issues with [Open OnDemand Interactive Jobs](/docs/cheaha/open_ondemand/ood_interactive.md). Please see our [FAQ](../help/faq.md#why-do-i-get-an-error-when-i-try-to-launch-an-hpc-interactive-session) for how to undo what `conda init` does.
<!-- markdownlint-disable MD046 -->

<!-- markdownlint-disable MD046 -->
!!! warning

    The Cheaha operating system has a version of Python installed. This version is used by `python` calls when Anaconda has not been loaded.
<!-- markdownlint-enable MD046 -->

For more information on usage with examples, see our general [Environment Management/Anaconda page](../environment_management/conda.md).

## Using Mamba

[Mamba](../environment_management/conda.md#speeding-things-up-with-mamba) is not installed in the base environment on Cheaha, and cannot be installed by researchers. We are working on making this change. In the meantime if you need the speed Mamba provides, you can follow these instructions to make it available for yourself.

1. `module load Anaconda3`
2. Create a new environment with only Mamba using `conda create --name mamba -c conda-forge mamba`
3. `conda activate mamba`
4. Use Mamba to install environments as needed. Be aware you must use the flag `--prefix=~/.conda/envs/` to put the environment in the correct location to be seen by Anaconda.
