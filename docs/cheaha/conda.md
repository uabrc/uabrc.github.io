# Anaconda

Python is a high level programming language that is widely used in many branches of science. The scientific python ecosystem is available to researchers as Anaconda modules on Cheaha. Modules for both python 2 and python 3 are installed. In order to see the different versions of each, use:

```bash
module spider Anaconda
```

<!-- markdownlint-disable MD046 -->
!!! danger

    Do not use `conda init` on Cheaha! Anaconda is managed as a [module](/docs/cheaha/lmod.md), including script setup. Using `conda init` can cause hard-to-diagnose issues with [Open OnDemand Interactive Jobs](/docs/cheaha/open_ondemand/ood_interactive.md). Please see our [FAQ](../help/faq.md#why-do-i-get-an-error-when-i-try-to-launch-an-hpc-interactive-session) for how to undo what `conda init` does.
<!-- markdownlint-disable MD046 -->

## Loading Anaconda

When planning a project, you should have an idea of which python version you need to use. Python 3 is the current standard and is used by the Anaconda3 modules. After loading one of the modules, use `python --version` to check the version number.

To see all of the Anaconda versions installed on Cheaha, use the command `module spider Anaconda`. Specific versions of Python can be installed in virtual environments regardless of the version of Python in the Anaconda module.

## Libraries and Virtual Environments

Anaconda virtual environments are self-contained environments with necessary packages for specific projects. It is recommended to have a separate environment for each project you have. This solves cases where different projects have dependencies on different versions of the same package.

New virtual environments include a few very common libraries such as scikit-learn, pandas, numpy, and scipy by default. However, most projects will need to install some external libraries as well using `pip` or `conda`.

Here, we will go through instructions for creating and managing Anaconda environments including installing new libraries. More complete information on this process can be found at the [Anaconda documentation](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#).

### Create an Environment

In order to create a basic environment with the default packages, use the `conda create` command:

```bash
# create a base environment. Replace <env> with an environment name
conda create -n <env>
```

If you are trying to replicate a pipeline or analysis from another person, you can also recreate an environment using a YAML file, if they have provided one. To replicate an environment using a YAML file, use:

```bash
# replicate an environment from a YAML file named env.yml
conda create -n <env> -f <path/to/env.yml>
```

By default, all of your conda environments are stored in `/home/<user>/.conda/envs`.

### Activate an Environment

From here, you can activate the environment using either `source` or `conda`:

```bash
# activate the virtual environment using source
source activate <env>

# or using conda
conda activate <env>
```

To know your environment has loaded, the command line should look like:

```text
(<env>) [blazerid@c0XXX ~]$
```

Once the environment is activated, you are allowed to install whichever python libraries you need for your analysis.

### Install Libraries

The base package manager for python is `pip`. The basic way to use `pip` is (replace \<package\> with the package name, omitting \<\>):

```bash
# install most recent version of a package
pip install \<package\>

# install a specific version
pip install \<package\>==version

# install a list of pacakges from a text file
pip install -r packages.txt
```

`pip` searches various package indexes like [PyPi](https://pypi.org/) or local project directories. If the package you need isn't found there, it may be available in an online Anaconda channel (same as index). To install from there, use the `conda install` command.

```bash
# install most recent version of a package
conda install \<package\>

# install a specific version
conda install \<package\>=version

# install from a specific conda channel
conda install -c \<channel\> \<package\>
```

Generally, if a package needs to be downloaded from a specific conda channel, it will mention that in its installation instructions.

### Running Command-Line Python

Python code can be run an individual commands from the command line. In order to access a python terminal, use the `python` or `python3` command in the terminal window. The prompt will be replaced with `>>>`. Execute any commands here. `exit()` will return you to the normal command line.

Executing scripts is the more common use case than executing individual commands interactively. To execute a script from the command line:

```bash
python \<script.py\>
```

Any optional inputs the script has can be listed after the name of the script.

<!-- markdownlint-disable MD046 -->
!!! note

    When Anaconda3 is loaded in your environment, the `python` and `python3` commands both refer to Python version 3.X.X (whatever minor version is loaded). However, when Anaconda3 is not loaded, `python` will refer to the base Python 2.7.5 instead. Be sure to load Anaconda3 before running `python`, or always use `python3` for disambiguation.
<!-- markdownlint-enable MD046 -->

### Deactivating an Environment

An environment can be deactivated using either `source` or `conda`:

```bash
# Using source
source deactivate

# Using conda
conda deactivate
```

Anaconda may say that using `source deactivate` is deprecated, but environment will still be deactivated.

Closing the terminal will also close out the environment.

### Exporting an Environment

To easily share environments with other researchers or replicate it on a new machine, it is useful to create an environment YAML file. You can do this using:

```bash
# activate the environment if it is not active already
conda activate <env>

# export the environment to a YAML file
conda env export > env.yml
```

## Speeding Things up with Mamba

[Mamba](https://github.com/mamba-org/mamba#readme) is an alternative to Anaconda that uses `libsolv` and parallel processing to install environments more quickly, sometimes by an order of magnitude. Mamba will also discover conflicts very quickly. Mamba is available as a [package](https://anaconda.org/conda-forge/mamba) via Anaconda. Currently Mamba cannot be installed on Cheaha, only on self-maanged systems like cloud.rc instances. To install use the following.

```bash
conda activate base
conda update --all
conda install -n base -c conda-forge mamba
```

<!-- markdownlint-disable MD046 -->
!!! warning

    Mamba must be installed in the base environment to function correctly!
<!-- markdownlint-enable MD046 -->