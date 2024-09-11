# Jupyter Apps

Jupyter Notebooks and Jupyter Lab are both available as standalone apps in OOD. Jupyter is commonly used with `conda` environments. If you are unfamiliar with `conda` environments please see the [Working with `conda` Environments section](#working-with-conda-environments) below before continuing here.

To launch the Jupyter notebook, select the menus 'Interactive Apps -> Jupyter Notebook'. The job creation and submission form appears:

![!Jupyter Notebook home form](./images/ood_jupyter_notebook_home_form.png)

As with all interactive apps, you'll need to select the resources required using the job creation form. Jupyter may also require additional initial setup before the app launches.

## Environment Setup

To modify the environment that `conda` and Jupyter will run in, please use the Environment Setup field to load modules and modify the environment `$PATH`. Be aware that any changes to the environment made in this window will be inherited by terminals as well as notebooks opened within Jupyter.

### CUDA

For GPU applications you'll need to load a `CUDA/*` module to have the CUDA toolkit available. If working with deep learning workflows, you may also need to load the `cuDNN/*-CUDA-*` module corresponding to your choice of `CUDA/*` module version. These are required for popular ML/DL/AI libraries like TensorFlow, Keras, and PyTorch. Use `module spider cuda/` and `module spider cudnn` to view the list of appropriate modules. An example of what to put in the Environment Setup field when using a version of Tensorflow compatible with CUDA version 12.2.0 is shown below.

```shell
# ENVIRONMENT SETUP
module load CUDA/12.2.0
module load cuDNN/8.9.2.26-CUDA-12.2.0
```

For information on which versions of CUDA to load for Tensorflow and PyTorch, please see [Tensorflow Compatibility](../slurm/gpu.md#tensorflow-compatibility) and [PyTorch Compatibility](../slurm/gpu.md#pytorch-compatibility).

For information on partition and GPU selection, please review our [hardware information page](../hardware.md) and [GPU Page](../slurm/gpu.md)

## Extra Jupyter Arguments

The `Extra Jupyter Arguments` field allows you to pass additional arguments to the Jupyter Server as it is being started. It can be helpful to point the server to the folder containing your notebook. To do this, assuming your notebooks are stored in `/data/user/$USER`, also known as `$USER_DATA`, put `--notebook-dir=$USER_DATA` in this field. You will be able to navigate to the notebook if it is in a subdirectory of `notebook-dir`, but you won't be able to navigate to any other directories. An example is shown below.

![!Jupyter Notebook job request form Extra jupyter arguments field.](./images/ood_jupyter_notebook_extra_args_box.png)

## Working with other programming languages within Jupyter Notebook

To work with other programming languages within Jupyter Notebook, you need to install the corresponding kernel for each language, similar to the process used for Python with the `ipykernel`. This can be done using package managers such as `pip` or `conda`, or by following language-specific instructions. For example, to install `R kernel` for the R language, we can run the `conda install -c r r-essentials` command. Please ensure that the kernel is installed in your `conda` environment. Then, select the desired language environment from the kernel dropdown menu.

Once the necessary kernels are installed, if you wish, you can write and run multiple code cells in different languages within a single notebook. Easily switch between kernels and select the preferred one for each language, and then proceed to run the code cells in their respective languages.

## Working with `conda` Environments

By default, Jupyter notebooks will use the base environment that comes with the `Miniforge3` module. This environment contains a large number of popular packages and may useful for something quick, dirty, and simple. However, for any analysis needing specific package versions or special packages, you will need to create your own environment and select it from the `Kernel` menu. For information on creating and managing `conda` environments please see our [Using `conda` page](../../workflow_solutions/using_conda.md). Then please review our [Cheaha-specific `conda` page](../software/software.md#conda-on-cheaha) for important tips and how to avoid common pitfalls.

To change the kernel, use the `Kernel` dropdown and select `Change Kernel`. From the list, choose the kernel corresponding to your desired `conda` environment (see below for an example). If your environment isn't appearing, you may be missing the ipykernel package. To do so, use `conda install ipykernel` to get ipykernel packgae installed into your environment, so Jupyter can recognize your environment.

![! Select your `conda` environment from the Kernel dropdown menu in Jupyter](images/jupyter_kernel.png)

### Creating an Environment for use with Jupyter Notebook

We can create a new environment, that houses all of the packages, modules, and libraries we need for our current Jupyter Notebook to implement functions and operations, run all of its cells and deliver desired outputs. Follow the steps below to accomplish this;

1. Access the terminal using your preferred method.

    - [OOD Terminal](./ood_layout.md#opening-a-terminal). Be sure to run the following steps in a job!
    - [OOD HPC Desktop Job Terminal](./hpc_desktop.md). This method will ensure terminal commands are run in a job.

1. [Create](../../workflow_solutions/using_conda.md#create-an-environment) and [activate](../../workflow_solutions/using_conda.md#activate-an-environment) your new environment, following the linked steps.

1. [Install your desired packages into your activated environment](../../workflow_solutions/using_conda.md#install-packages).

1. Remember to install 'ipykernel' in your activated environment, using `conda install ipykernel`.

1. Go into your working Jupyter Notebook file, and [change to the created environment](#changing-environments-using-jupyter-notebook-gui).

### Changing Environments using Jupyter Notebook GUI

1. When your Jupyter Notebook Job has been created on Cheaha, and you want to load an environment you have already created. Select from the dropdown menu "New". You can find this in the top right corner of the Jupyter Notebook landing page. ![!Select Environment](images/selectenvsjupyter.png)

1. When you click new, you would see a dropdown of environments that are available for you to use. If you do not see your created environment listed, you may need to install `ipykernel` using `conda install ipykernel` in your cheaha shell within your activated environment. You may have to refresh the page to see your newly created environment. Select the preferred existing environment you created. ![!Kernel/Environment Drop Down](images/jpnotebook_landingpage_kernel.png)

    On another note, you may want to replicate an environment setup to handle a project, research, or analysis but you are already working on a Jupyter Notebook file. You can select a different environment from the Jupyter Notebook file by;

    1. Selecting the Jupyter Notebook File from your landing page.

    1. While in the file, look for the menu option "Kernel", select this. In the Kernel dropdown option, select "Change kernel". Then select your preferred kernel environment. Wait a few seconds for it to load, and you are ready to use your preferred environment. Selecting this would open a new Jupyter Notebook file with your selected environment. ![!Changing Environment](images/changingkernel.png)

    1. Your selected environment would appear in the top right corner.![!Selected Environment](images/selected_env.png)

## Common Issues in OOD Jupyter

### Python Executable Issues

Jupyter Notebook by default loads `Miniforge3`. Hence do not load any versions of `Miniforge3` module in the `Environment Setup` field in the OOD Jupyter Notebook, as it causes Python mismatch, and the errors are hard to diagnose.

Having self-installed `conda` software can cause the above issue. This includes self-installed Anaconda, Miniconda, Mambaforge, or Miniforge. If you have installations of any of these software in your personal space, delete those directories and instead use the `Miniforge3` module.

<!-- markdownlint-disable MD046 -->
!!! important

    The Anaconda and Miniconda software are subject to the Anaconda Terms of Service and may not be used for UAB business.
<!-- markdownlint-enable MD046 -->

To identify a Python mismatch, use the commands `which python` and `python --version` to confirm the desired Python executable and version. Within the `conda` environment, `which python` prints the path of the Python executable (e.g. `~/.conda/envs/remora/bin/python`). If it doesn't match the expected version, an unexpected Python version may be in use.

`conda init` append an incorrect version of Python to the front of the `$PATH`, an environment variable containing directories where the operating system looks for executable files. When you attempt to execute a Python-related command, the system will find the first matching executable in the directories listed in the modified `$PATH`. If the first entry corresponds to the version of Python added by `conda init`, that specific version will be used which lead to Python mismatch and hard-to-diagnose errors.

### Unexpected/Silent Job Failure

Having `conda activate` and `source activate` statements in the OOD Jupyter Notebooks' `Environment Setup` field can cause unexpected and silent job failure. Avoid using `conda activate` in the `Environment Setup` field.

### Timeout in Loading Jupyter Notebook

If you encounter a "Failed to Connect" message while trying to open the job, and experience a timeout issue in loading the OOD Jupyter Notebook, it is recommended to close the tab and wait for a few minutes. Jupyter is still in the process of initializing and may take some time after the job initially starts running.

### VNC Error When Launching OOD Jupyter Notebook

While launching an OOD HPC Desktop Job or any OOD Applications, if the user gets errors, `Unable to contact settings server` and/or `Unable to load a failsafe session`, it is recommended to follow the below guidelines.

![!OOD vnc error.](./images/ood_vncerror.png) ![!OOD vnc error_contd.](./images/ood_vncerror_contd.png)

Using `conda init` causes a block of code automatically inserted into the `.bashrc` file in your `$HOME` directory. This code block may interfere with the proper functioning of various OOD applications, resulting in a VNC error. To address this issue, it is recommended to follow the instructions outlined in the [FAQ entry](https://ask.cyberinfrastructure.org/t/why-do-i-get-an-error-when-launching-an-open-ondemand-hpc-interactive-session/2496).

### Installing Pip Packages Outside of Your Environments

<!-- markdownlint-disable MD046 -->
!!! danger

    Using `pip install` without loading Miniforge3 will cause hard-to-diagnose errors and broken workflows.

    Using `pip install` in the `base` environment will cause the same hard-to-diagnose errors and broken workflows.

    Read more about this issue, and how to resolve it, [here](../software/software.md#installing-pip-packages-outside-of-your-environments).
<!-- markdownlint-disable MD046 -->

### Tensorflow and PyTorch GPU issues

If you are using Jupyter with TensorFlow or PyTorch and no GPU is found, please see our Slurm GPU page sections on [TensorFlow Compatibility](../slurm/gpu.md#tensorflow-compatibility) and [PyTorch Compatibility](../slurm/gpu.md#pytorch-compatibility).
