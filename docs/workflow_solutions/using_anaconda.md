# Anaconda

Python is a high level programming language that is widely used in many branches of science. As a result, many scientific packages have been developed in Python, leading to the development of a package manager called Anaconda. Anaconda is the standard in Python package management for scientific research.

Benefits of Anaconda:

- Shareability: environments can be shared via human-readable text-based YAML files.
- Maintainability: the same YAML files can be version controlled using git.
- Repeatability: environments can be rebuilt using those same YAML files.
- Simplicity: dependency matrices are computed and solved by Anaconda, and libraries are pre-built and stored on remote servers for download instead of being built on your local machine.
- Ubiquity: nearly all Python developers are aware of the usage of Anaconda, especially in scientific research, so there are many resources available for learning how to use it, and what to do if something goes wrong.

Anaconda can also install Pip and record which Pip packages are installed, so Anaconda can do everything Pip can, and more.

<!-- markdownlint-disable MD046 -->
!!! important

    If using Anaconda on Cheaha, please see our [Anaconda on Cheaha page](../cheaha/software/software.md#anaconda-on-cheaha) for important details and restrictions.
<!-- markdownlint-enable MD046 -->

## Anaconda best practices for environment reproducibility

Creating, activating and managing environments with Anaconda can be challenging, especially when aiming for reproducibility across different systems, platforms, and projects. To tackle these challenges, below is a list of consolidated best practices drawn from some practical experiences:

1. Using Conda and Pip Effectively: While using Cheaha, or on any other platform, prioritise using Conda packages, as checks are done during package installation. This way required libraries function properly and are less likely to throw up compatibility and dependency errors. Use Conda packages instead of Pip when possible as they significantly offer a reduced risk of breaking environments. If Pip packages are necessary for your work, install them after all Conda packages to minimize conflicts and breakage of your environment. Also, in practice when packages are to be installed from an environment file, conda packages are usually installed first, before pip packages are installed.

2. Isolate Environments: Create separate Conda environments for different projects to prevent interference from conflicting dependencies, this would in turn help to maintain a clean workspace. This approach aids in managing dependencies more effectively and allows for easy replication/reproducibility across projects.

3. Recreate Environments for Changes: Instead of modifying existing environments, recreate them with updated requirements to ensure stability. This method prevents inconsistencies caused by incremental changes. You can do this by creating a `.yml` file, using any of the methods listed [here](#working-with-environment-yaml-files), and then recreate the environment.

4. Export and Store Requirements: Keep a record of Conda and Pip requirements in text files. This practice enables easy sharing and version control, making it simpler to recreate environments on different machines.

5. Consider Reproducibility and Upgradability: Balancing the need for reproducible builds with the flexibility to upgrade dependencies is crucial. Utilize tools like conda-lock to generate lock files that pin dependencies, allowing for reproducible environments that can be easily updated when necessary. Please note that using `conda-lock` will pin dependencies for reproducibility, ensuring exact version upgrades are done when needed.

6. Address Portability Issues: Make your environment files as portable as possible by excluding system-specific paths and using general package versions where appropriate. This consideration ensures that environments can be replicated across different systems without modification. For example, in your `requirements.txt`, it is advised to specify the package and version, see `numpy` example as shown below;

    `numpy=1.21.5`

    Please see more information [here](#replicability-versus-portability).

## What is my best solution for installing Anaconda?

If you are using a local machine or doing general purpose software development, or have a particular package in mind, go [here](#installing-anaconda) to install Anaconda.

If you are using a virtual machine or container, go [here](#installing-miniconda) to install Miniconda.

If you are using Cheaha, go [here](../cheaha/software/software.md#anaconda-on-cheaha) for how to use Anaconda on Cheaha.

### Installing Anaconda

The full Anaconda install is a good choice if you are using a local machine, or doing general Python development work, or have a particular scientific package in mind.

Anaconda installation instructions are located here: <https://docs.anaconda.com/anaconda/install/index.html>.

For best performance, be sure to set the default solver to `libmamba` using `conda config --set solver libmamba`. For more information see: <https://conda.github.io/conda-libmamba-solver/getting-started/#set-as-default>.

### Installing Miniconda

Miniconda is a lightweight version of Anaconda. While Anaconda's base environment comes with Python, the Scipy stack, and other common packages pre-installed, Miniconda comes with no packages installed. This is an excellent alternative to the full Anaconda installation for environments where minimal space is available or where setup time is important, like [virtual machines](../uab_cloud/index.md) and [containers](getting_containers.md).

Miniconda installation instructions are located here: <https://docs.conda.io/en/latest/miniconda.html>.

For best performance, be sure to set the default solver to `libmamba` using `conda config --set solver libmamba`. For more information see: <https://conda.github.io/conda-libmamba-solver/getting-started/#set-as-default>.

## Using Anaconda

Anaconda is a package manager, meaning it handles all of the difficult mathematics and logistics of figuring out exactly what versions of which packages should be downloaded to meet your needs, or inform you if there is a conflict.

Anaconda is structured around environments. Environments are self-contained collections of researcher-selected packages. Environments can be changed out using a simple package without requiring tedious installing and uninstalling of packages or software, and avoiding dependency conflicts with each other. Environments allow researchers to work and collaborate on multiple projects, each with different requirements, all on the same computer. Environments can be installed from the command line, from pre-designed or shared YAML files, and can be modified or updated as needed.

The following subsections detail some of the more common commands and use cases for Anaconda usage. More complete information on this process can be found at the [Anaconda documentation](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#).

<!-- markdownlint-disable MD046 -->
!!! important

    If using Anaconda on Cheaha, please see our [Anaconda on Cheaha page](../cheaha/software/software.md#anaconda-on-cheaha) for important details and restrictions.
<!-- markdownlint-enable MD046 -->

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

<!-- markdownlint-disable MD046 -->
!!! important
    Make sure `pip` is installed within the `conda` environment and use it for installing packages within the `conda` environment to prevent [Pip related issues](../cheaha/open_ondemand/ood_jupyter.md#pip-installs-packages-outside-of-environment).
<!-- markdownlint-disable MD046 -->

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

#### Packages for Jupyter

For more information about using Anaconda with Jupyter, see the section [Working with Anaconda Environments](..//cheaha/open_ondemand/ood_jupyter.md#working-with-anaconda-environments).

### Update packages in an environment

To ensure packages and their dependencies are all up to date, it is a best practice to regularly update installed packages, and libraries in your activated environment.

```bash

conda update -—all

```

### Deactivating an Environment

An environment can be deactivated using the following command.

```bash
# Using conda
conda deactivate
```

Anaconda may say that using `source deactivate` is deprecated, but environment will still be deactivated.

Closing the terminal will also close out the environment.

### Deleting an Environment

To delete an environment, use the following command. Remember to replace `<env>` with the existing environment name.

```bash

conda env remove —-name <env>

```

### Working with Environment YAML Files

#### Exporting an Environment

To easily share environments with other researchers or replicate it on a new machine, it is useful to create an environment YAML file. You can do this using:

```bash
# activate the environment if it is not active already
conda activate <env>

# export the environment to a YAML file
conda env export > env.yml
```

#### Creating an Environment from a YAML File

To create an environment from a YAML file `env.yml`, use the following command.

```bash
conda env create --file env.yml
```

#### Sharing your environment file

To share your environment for collaboration, there are primarily 3 ways to export environments, the below commands show how to create environment files that can be shared for replication. Remember to replace `<env>` with the existing environment name.

1. Cross-Platform Compatible

    ```bash

    conda env export --from-history > <env>.yml 

    ```

2. Platform + Package Specific

    Create .yml file to share, replace `<envname>` (represents the name of your environment) and `<env>` (represents the name of the file you want to export) with preferred names for file.

    ```bash

    conda env export <envname> > <env>.yml 

    ```

3. Platform + Package + Channel Specific

    ```bash

    conda list —-explicit > <env>.txt
    # OR
    conda list —-explicit > <env>.yml

    ```

#### Replicability versus Portability

An environment with only `python 3.10.4`, `numpy 1.21.5` and `jinja2 2.11.2` installed will output something like the following file when `conda env export` is used. This file may be used to precisely replicate the environment as it exists on the machine where `conda env export` was run. Note that the versioning for each package contains two `=` signs. The code like `he774522_0` after the second `=` sign contains hyper-specific build information for the compiled libraries for that package. Sharing this exact file with collaborators may result in frustration if they do not have the exact same operating system and hardware as you, and they would not be able to build this environment. We would say that this environment file is not very portable.

There are other portability issues:

- The `prefix: C:\...` line is not used by `conda` in any way and is deprecated. It also shares system information about file locations which is potentially sensitive information.
- The `channels:` group uses `- defaults`, which may vary depending on how you or your collaborator has customized their Anaconda installation. It may result in packages not being found, resulting in environment creation failure.

```yaml
name: test-env
channels:
  - defaults
dependencies:
  - blas=1.0=mkl
  - bzip2=1.0.8=he774522_0
  - ca-certificates=2022.4.26=haa95532_0
  - certifi=2021.5.30=py310haa95532_0
  - intel-openmp=2021.4.0=haa95532_3556
  - jinja2=2.11.2=pyhd3eb1b0_0
  - libffi=3.4.2=h604cdb4_1
  - markupsafe=2.1.1=py310h2bbff1b_0
  - mkl=2021.4.0=haa95532_640
  - mkl-service=2.4.0=py310h2bbff1b_0
  - mkl_fft=1.3.1=py310ha0764ea_0
  - mkl_random=1.2.2=py310h4ed8f06_0
  - numpy=1.21.5=py310h6d2d95c_2
  - numpy-base=1.21.5=py310h206c741_2
  - openssl=1.1.1o=h2bbff1b_0
  - pip=21.2.4=py310haa95532_0
  - python=3.10.4=hbb2ffb3_0
  - setuptools=61.2.0=py310haa95532_0
  - six=1.16.0=pyhd3eb1b0_1
  - sqlite=3.38.3=h2bbff1b_0
  - tk=8.6.11=h2bbff1b_1
  - tzdata=2022a=hda174b7_0
  - vc=14.2=h21ff451_1
  - vs2015_runtime=14.27.29016=h5e58377_2
  - wheel=0.37.1=pyhd3eb1b0_0
  - wincertstore=0.2=py310haa95532_2
  - xz=5.2.5=h8cc25b3_1
  - zlib=1.2.12=h8cc25b3_2
prefix: C:\Users\user\Anaconda3\envs\test-env
```

To make this a more portable file, suitable for collaboration, some planning is required. Instead of using `conda env export` we can build our own file. Create a new file called `env.yml` using your favorite text editor and add the following. Note we've only listed exactly the packages we installed, and their version numbers, only. This allows Anaconda the flexibility to choose dependencies which do not conflict and do not contain unusable hyper-specific library build information.

```yaml
name: test-env
channels:
  - anaconda
dependencies:
  - jinja2=2.11.2
  - numpy=1.21.5
  - python=3.10.4
```

This is a much more readable and portable file suitable for sharing with collaborators. We aren't quite finished though! Some scientific packages on the `conda-forge` channel, and on other channels, can contain dependency errors. Those packages may accidentally pull a version of a dependency that breaks their code.

For example, the package `markupsafe` made a not-backward-compatible change (a breaking change) to their code between `2.0.1` and `2.1.1`. Dependent packages expected `2.1.1` to be backward compatible, so their packages allowed `2.1.1` as a substitute for `2.0.1`. Since Anaconda chooses the most recent version allowable, package installs broke. To work around this for our environment, we would need to modify the environment to "pin" that package at a specific version, even though we didn't explicitly install it.

```yaml
name: test-env
channels:
  - anaconda
dependencies:
  - jinja2=2.11.2
  - markupsafe=2.0.1
  - numpy=1.21.5
  - python=3.10.4
```

Now we can be sure that the correct versions of the software will be installed on our collaborator's machines.

<!-- markdownlint-disable MD046 -->
!!! note

    The example above is provided only for illustration purposes. The error has since been fixed, but the example above really happened and is helpful to explain version pinning.
<!-- markdownlint-enable MD046 -->

#### Good Software Development Practice

Building on the example above, we can bring in good software development practices to ensure we don't lose track of how our environment is changing as we develop our software or our workflows. If you've ever lost a lot of hard work by accidentally deleting an important file, or forgetting what changes you've made that need to be rolled back, this section is for you.

Efficient software developers live the mantra "Don't repeat yourself". Part of not repeating yourself is keeping a detailed and meticulous record of changes made as your software grows over time. [Git](git_collaboration.md) is a way to have the computer keep track of those changes digitally. Git can be used to save changes to environment files as they change over time. Remember that each time your environment changes to commit the output of [Exporting your Environment](#exporting-an-environment) to a repository for your project.

## Speeding Things up with Mamba

Use of Mamba has been deprecated on Cheaha. On Cheaha, use `module load Anaconda3` and the usual `conda` commands instead. The backend of `conda` has been set to use `libmamba` and is now equally performant.

If you are using Mamba on a local machine and have Anaconda installed, you can set `libmamba` as your default solver using `conda config --set solver libmamba` as described here: <https://conda.github.io/conda-libmamba-solver/getting-started/#set-as-default>
