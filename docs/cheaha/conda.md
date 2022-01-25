# Anaconda

Python is a high level programming language that is widely used in many branches of science. The scientific python ecosystem is available to researchers as Anaconda modules on Cheaha. Modules for both python 2 and python 3 are installed. In order to see the different versions of each, use:

``` bash
module spider Anaconda
```

## Loading Anaconda

When planning a project, you should have an idea of which python version you need to use. Python 3 is the current standard and is used by the Anaconda3 modules. After loading one of the modules, use `python --version` to check the version number.

Anaconda modules and their corresponding python versions can be seen in the table below:

| Module            | Python Version |
|-------------------|----------------|
| Anaconda2/4.0.0   | 2.7.11         |
| Anaconda2/4.2.0   | 2.7.12         |
| Anaconda3/4.4.0   | 3.6.1          |
| Anaconda3/5.0.1   | 3.6.3          |
| Anaconda3/5.1.0   | 3.6.4          |
| Anaconda3/5.2.0   | 3.6.5          |
| Anaconda3/5.3.0   | 3.7.2          |
| Anaconda3/5.3.1   | 3.7.4          |
| Anaconda3/2019.10 | 3.7.4          |
| Anaconda3/2020.02 | 3.7.6          |
| Anaconda3/2020.07 | 3.8.3          |
| Anaconda3/2020.11 | 3.8.5          |

If a necessary version is not required, choose the most recent version, `Anaconda3/2020.11`. Alternatively, the necessary python version can specified when creating a virtual environment and will be downloaded and installed regardless of if it is currently installed on the cluster.

## Libraries and Virtual Environments

Anaconda virtual environments are self-contained environments with necessary packages for specific projects. It is recommended to have a separate environment for each project you have. This solves cases where different projects have dependencies on different versions of the same package.

New virtual environments include a few very common libraries such as scikit-learn, pandas, numpy, and scipy by default. However, most projects will need to install some external libraries as well using `pip` or `conda`.

Here, we will go through instructions for creating and managing Anaconda environments including installing new libraries. More complete information on this process can be found at the [Anaconda documentation](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#).

### Create an Environment

In order to create a basic environment with the default packages, use the `conda create` command:

``` bash
# create a base environment. Replace <env> with an environment name
conda create -n <env>
```

If you are trying to replicate a pipeline or analysis from another person, you can also recreate an environment using a YAML file, if they have provided one. To replicate an environment using a YAML file, use:

``` bash
# replicate an environment from a YAML file named env.yml
conda create -n <env> -f <path/to/env.yml>
```

By default, all of your conda environments are stored in `/home/<user>/.conda/envs`.

### Activate an Environment

From here, you can activate the environment using either `source` or `conda`:

``` bash
# activate the virtual environment using source
source activate <env>

# or using conda
conda activate <env>
```

To know your environment has loaded, the command line should look like:

``` text
(<env>) [blazerid@c0XXX ~]$
```

Once the environment is activated, you are allowed to install whichever python libraries you need for your analysis.

### Install Libraries

The base package manager for python is `pip`. The basic way to use `pip` is (replace \<package\> with the package name, omitting \<\>):

``` bash
# install most recent version of a package
pip install \<package\>

# install a specific version
pip install \<package\>==version

# install a list of pacakges from a text file
pip install -r packages.txt
```

`pip` searches various package indexes like [PyPi](https://pypi.org/) or local project directories. If the package you need isn't found there, it may be available in an online Anaconda channel (same as index). To install from there, use the `conda install` command.

``` bash
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

``` bash
python \<script.py\>
```

Any optional inputs the script has can be listed after the name of the script.

!!! note

   When Anaconda3 is loaded in your environment, the `python` and `python3` commands both refer to Python version 3.X.X (whatever minor version is loaded). However, when Anaconda3 is not loaded, `python` will refer to the base Python 2.7.5 instead. Be sure to load Anaconda3 before running `python`, or always use `python3` for disambiguation.

### Deactivating an Environment

An environment can be deactivated using either `source` or `conda`:

``` bash
# Using source
source deactivate

# Using conda
conda deactivate
```

Anaconda may say that using `source deactivate` is deprecated, but environment will still be deactivated.

Closing the terminal will also close out the environment.

### Exporting an Environment

To easily share environments with other researchers or replicate it on a new machine, it is useful to create an environment YAML file. You can do this using:

``` bash
# activate the environment if it is not active already
conda activate \<env\>

# export the environment to a YAML file
conda env export \> env.yml
```
