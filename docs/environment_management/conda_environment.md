# Anaconda

Python is a high level programming language that is widely used in many branches of science. As a result, many scientific packages have been developed in Python, leading to the development of a package manager called Anaconda. Anaconda is the standard in Python package management for scientific research.

Benefits of Anaconda:

- Shareability: environments can be shared via human-readable text-based YAML files.
- Maintainability: the same YAML files can be version controlled using git.
- Repeatability: environments can be rebuilt using those same YAML files.
- Simplicity: dependency matrices are computed and solved by Anaconda, and libraries are pre-built and stored on remote servers for download instead of being built on your local machine.
- Ubiquity: nearly all Python developers are aware of the usage of Anaconda, especially in scientific research, so there are many resources available for learning how to use it, and what to do if something goes wrong.

Anaconda can also install Pip and record which Pip packages are installed, so Anaconda can do everything Pip can, and more.

## What is my best solution for installing Anaconda?

If you are using a local machine or doing general purpose software development, or have a particular package in mind, go [here](#installing-anaconda) to install Anaconda.

If you are using a virtual machine or container, go [here](#installing-miniconda) to install Miniconda.

If you are using Cheaha, go [here](../cheaha/conda.md) for how to use Anaconda on Cheaha.

### Installing Anaconda

The full Anaconda install is a good choice if you are using a local machine, or doing general Python development work, or have a particular scientific package in mind.

Anaconda installation instructions are located here: <https://docs.anaconda.com/anaconda/install/index.html>.

### Installing Miniconda

Miniconda is a lightweight version of Anaconda. While Anaconda's base environment comes with Python, the Scipy stack, and other common packages pre-installed, Miniconda comes with no packages installed. This is an excellent alternative to the full Anaconda installation for environments where minimal space is available or where setup time is important, like [virtual machines](../uab_cloud/introduction.md) and [containers](containers.md).

Miniconda installation instructions are located here: <https://docs.conda.io/en/latest/miniconda.html>.

## Using Anaconda

Anaconda is a package manager, meaning it handles all of the difficult mathematics and logistics of figuring out exactly what versions of which packages should be downloaded to meet your needs, or inform you if there is a conflict.

Anaconda is structured around environments. Environments are self-contained collections of researcher-selected packages. Environments can be changed out using a simple package without requiring tedious installing and uninstalling of packages or software, and avoiding dependency conflicts with each other. Environments allow researchers to work and collaborate on multiple projects, each with different requirements, all on the same computer. Environments can be installed from the command line, from pre-designed or shared YAML files, and can be modified or updated as needed.

The following subsections detail some of the more common commands and use cases for Anaconda usage. More complete information on this process can be found at the [Anaconda documentation](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#).

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

### Install Packages

To install packages using Anaconda, use the `conda install` command. The `-c` or `--channel` command can be used to select a specific package channel to install from. The `anaconda` channel is a curated collection of high-quality packages, but the very latest versions may not be available on this channel. The `conda-forge` channel is more open, less carefully curated, and has more recent versions.

```bash
# install most recent version of a package
conda install <package>

# install a specific version
conda install <package>=version

# install from a specific conda channel
conda install -c <channel> <package><=version>
```

Generally, if a package needs to be downloaded from a specific conda channel, it will mention that in its installation instructions.

#### Installing Packages with Pip

Some packages are not available through Anaconda. Often these packages are available via [PyPi](https://pypi.org/) and thus using the Python built-in Pip package manager. Pip may also be used to install locally-available packages as well.

```bash
# install most recent version of a package
pip install \<package\>

# install a specific version, note the double equals sign
pip install \<package\>==version

# install a list of packages from a text file
pip install -r packages.txt
```

#### Finding Packages

You may use the [Anaconda page](https://anaconda.org/) to search for packages on Anaconda, or use Google with something like `<package name> conda`. To find packages in PyPi, either use the [PyPi page](https://pypi.org/) to search, or use Google with something like `<package name> pip`.

### Deactivating an Environment

An environment can be deactivated using the following command.

```bash
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

### Creating an Environment from a YAML File

To create an environment from a YAML file `env.yml`, use the following command.

```bash
conda env create --file env.yml
```

## Good Software Development Practice

If you've ever lost a lot of hard work by accidentally deleting an important file, or forgetting what changes you've made that need to be rolled back, this section is for you.

Efficient software developers live the mantra "Don't repeat yourself". Part of not repeating yourself is keeping a detailed and meticulous record of changes made as your software grows over time. [Git](git.md) is a way to have the computer keep track of those changes digitally. Git can be used to save changes to environment files as they change over time. Remember that each time your environment changes to commit the output of [Exporting your Environment](#exporting-an-environment) to a repository for your project.

## Speeding Things up with Mamba

[Mamba](https://github.com/mamba-org/mamba#readme) is an alternative to Anaconda that uses `libsolv` and parallel processing to install environments more quickly, sometimes by an order of magnitude. Mamba will also discover conflicts very quickly. Mamba is available as a [package](https://anaconda.org/conda-forge/mamba) via Anaconda. Currently Mamba cannot be installed on Cheaha, only on self-maanged systems like cloud.rc instances. To install use the following.

```bash
conda activate base
conda update --all
conda install -n base -c conda-forge mamba
```

<!-- markdownlint-disable MD046 -->
!!! warning

    Mamba must be installed in the base environment to function correctly! If you are using Cheaha, and cannot install in the base environment, see our workaround [here](../cheaha/conda.md#using-mamba)
<!-- markdownlint-enable MD046 -->