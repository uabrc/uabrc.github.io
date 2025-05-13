# Software Installation

## Anaconda on Cheaha

For additional general information on using Anaconda please see [Anaconda Environments](../../workflow_solutions/using_anaconda.md).

If you are using Jupyter Notebook, please see our section on [Packages for Jupyter](../../workflow_solutions/using_anaconda.md#packages-for-jupyter).

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

For more information on usage with examples, see [Anaconda Environments](../../workflow_solutions/using_anaconda.md). Need some hands-on experience, you can find instructions on how to install PyTorch and TensorFlow using Anaconda in this [tutorial](../tutorial/pytorch_tensorflow.md).

### Obtaining the Latest CUDA and cuDNN Modules

Please see our [CUDA and cuDNN section of the GPU page](../slurm/gpu.md#cuda-and-cudnn-modules).

## Cell Ranger

Cell Ranger is a proprietary software developed by [10x Genomics](https://www.10xgenomics.com/support/software/cell-ranger/latest).

### Licensing

(i) Usage of Cell Ranger is governed by the terms of their [End User License Agreement (EULA)](https://www.10xgenomics.com/legal/end-user-software-license-agreement). Each UAB researcher must individually review and accept the EULA to install and use the software.

(ii) Cell Ranger is strictly licensed for use with data generated on 10x Genomics instruments and may not be used with data from other platforms.

### Installation

 Cell Ranger can be installed within a researcher’s individual user account on Cheaha. Installation instructions are available on the official [10x Genomics website](https://www.10xgenomics.com/support/software/cell-ranger/latest/tutorials/cr-tutorial-in#download).

#### User-Based Installation

CellRanger can be installed on individual user accounts. You will have to use a compute node to install and run the software. For more information refer to [compute and login nodes](../../cheaha/getting_started.md#login-vs-compute-nodes). Following are the steps to install Cell Ranger in Cheaha.

(i) [Register](https://www.10xgenomics.com/products/cell-ranger/downloads/eula?closeUrl=%2Fsupport%2Fsoftware%2Fcell-ranger%2Fdownloads%23download-links&redirectUrl=%2Fsupport%2Fsoftware%2Fcell-ranger%2Fdownloads%23download-links%3Fstart%3Dcellranger-9.0.1.tar.gz) and download the desired version of `Cellranger` from the [10X Genomics site](https://www.10xgenomics.com/support/software/cell-ranger/downloads).

(ii) Use "curl" or "get" to download the .tar.gz package.

```bash

```

```bash

```

3. Extract the package with, tar -zxvf cellranger-8.0.1.tar.gz

4. Navigate to the bin directory: cd cellranger-8.0.1/bin

5. Copy the path displayed by using the command `pwd`, then add it to your "$HOME/.bashrc" file as,
export PATH=/path/to/cellranger-8.0.1/bin:$PATH

6. Close the terminal and open a new one for the changes to take effect. You can verify if cellranger 8.0.1 is installed using,
cellranger --version.

Please let us know if you have any questions.

## Singularity Containers

Containers are a very useful resource for installing software without needing administrator permission. Please read the full documentation about singularity and containers on our [main Singularity page](../../workflow_solutions/getting_containers.md#containers-on-cheaha).
