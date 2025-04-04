# Anaconda Environment Tutorial for PyTorch and TensorFlow

The below tutorial would show you steps on how to create an Anaconda environment, activate, and install libraries/packages for machine and deep learning (PyTorch and Tensorflow) using an Anaconda environment on Cheaha. There are also steps on how to access the terminal, as well as using Jupyter Notebook's Graphical User Interface (GUI) to work with these Anaconda environments. There are detailed steps here to guide your creation of a [Jupyter Notebook job.](../open_ondemand/ood_layout.md#interactive-apps)

<!-- markdownlint-disable MD046 -->
!!! note

    CUDA modules are used in this tutorial. Please note that the latest CUDA and cuDNN are now available from [Conda](../slurm/gpu.md#cuda-and-cudnn-modules). The tutorial provides good practices, but ages over time. You may need to modify the scripts to be suitable for your work.
<!-- markdownlint-enable MD046 -->

## Installing Anaconda Environments Using the Terminal

To access the terminal (shell), please do the following.

1. Login to [rc.uab.edu](https://rc.uab.edu)

1. Create a job on Cheaha using the Interactive Apps dropdown option.![!Interactive Apps Dropdown Menu](images/interactive_dropdown.png)

1. Select Jupyter Notebook, and fill out the options, as per your project needs, then click Launch.  For more information on compute needs, and a guide for selecting the right options click [here](../job_efficiency.md#estimating-compute-resources). ![!Jupyter Launch Button](images/jupyter_launch.png)

1. Click the Connect to Jupyter button ![!Connect to Jupyter Button](images/connect_to_jupyt_button.png)

    You will see the below interface. ![!Jupyter Notebook Landing Page](images/jupyter_landing_page.png)

1. When the job has been created, on the My Interactive Sessions page, click the button in front of Host (usually colored blue) in the format >_c0000.

    ![!host image](images/cheaha_shell_button.png)

    This should open into a terminal as shown below.

    ![!Cheaha Shell CLI](images/cheaha_shell_cli.png)

1. In this interface, you can create, and activate environments, as well as install packages, modules and libraries into your activated environment.

## How do we create a custom environment for PyTorch and TensorFlow

The instructions below, provide a recommended step by step guide to creating and activating an environment that has PyTorch and/or TensorFlow installed and ready to use for deep learning projects.

## Installing PyTorch Using the Terminal

There are two instances of PyTorch that can be installed, one requiring GPUs, and another utilizing only CPUs. The use of GPUs improve compute speeds and are preferred. For both instances of pytorch, please follow these steps;

1. For a correct installation of pytorch using GPUs, we have to ensure some conditions are met (Request a partition that has GPUs, and then load the requisite `CUDA` module). You can see our [documentation](../hardware.md#details) for details on our Partition offerings. The command below shows how to load the CUDA toolkit in your environment setup form (see image below) when requesting for resources.

```bash
module load CUDA/11.8.0
```

![!load CUDA](images/module_load_cuda.png)

<!-- markdownlint-disable MD046 -->
!!! note

    The cudatoolkit version may vary, as at the time of this tutorial, 11.8 is the version used. Running `nvidia-smi`, as in the image below, will show you the status, version and other information on GPUs in your created job session. The CUDA version is highlighted. The GPU CUDA Version available on Cheaha as of 2025-02-25 is `12.6.0`. Newer versions are available from [Conda](../slurm/gpu.md#cuda-and-cudnn-modules). Because the toolkit version used is lower than the Cheaha GPU version, it works.
<!-- markdownlint-enable MD046 -->

![!nvidia-smi output](images/CudaVersion.png)

1. Access the terminal following the steps [here](#installing-anaconda-environments-using-the-terminal).

1. [Create](../../workflow_solutions/using_anaconda.md#create-an-environment) and [activate](../../workflow_solutions/using_anaconda.md#activate-an-environment) an environment as stated in these links.

<!-- markdownlint-disable MD046 -->
!!! note

    When installing packages, modules and libraries into environments, remember to also install `ipykernel` using `conda install ipykernel`. This way your activated environment would appear in the list of kernels in your Jupyter Notebook. We have a [section](../../cheaha/open_ondemand/ood_jupyter.md#working-with-anaconda-environments) in our docs detailing how to switch conda environments.

<!-- markdownlint-enable MD046 -->

1. When your job has started and your environment created and activated from the terminal (see above [instructions](../../workflow_solutions/using_anaconda.md#create-an-environment)), run the below command.

```bash
conda install pytorch torchvision torchaudio cudatoolkit=11.8 -c pytorch -c nvidia
```

These commands will install a GPU compatible PyTorch version into your environment. To verify PyTorch is installed, and to see what version you have installed in your environment, use the below command.

```bash
conda list | grep "torch"
```

You should get an output like the below image.

![!PyTorch Env Output](images/pytorchversion_output.png)

```bash

# Package details

# Name        Version   Build                           Channel
ffmpeg        4.3       hf484d3e_0                      pytorch
libjpeg-turbo 2.0.0     h9bf148f_0                      pytorch
pytorch       2.2.0     py3.12_cuda11.8_cudnn8.7.0_0    pytorch
pytorch-cuda  11.8      h7e8668a_5                      pytorch
pytorch-mutex 1.0       cuda                            pytorch
torchaudio    2.2.0     py312_cu118                     pytorch
torchvision   0.17.0    py312_cu118                     pytorch
```

The same process can be followed for installing another Deep Learning library Tensorflow (see instructions [below](#install-tensorflow-gpu-using-the-terminal)) with some minute differences. You may decide to install the TensorFlow library into the same environment or create a new one. As a best practice, you may want to install these libraries in different environments.

## Using PyTorch on Jupyter Notebook

As an example we will be using a sample Jupyter Notebook with just a simple torch function to test if a GPU will be utilized with PyTorch functions. Run the command in a cell, and if your output is `True`, then you have your GPU setup to support PyTorch functions.

```python
import torch

print(torch.cuda.is_available())
x = torch.cuda.current_device()
print(torch.cuda.get_device_name(x))
```

![!PyTorch Jupyter Notebook Output](images/pytorch_output.png)

## Install TensorFlow GPU Using the Terminal

1. Create a new environment that is compatible with supported tensorflow versions, use the below command to do this. For this tutorial we will use Python 3.11.

    ```bash
    conda create -n tensorflow python=3.11
    ```

1. Activate the conda environment created in Step 1.

    ```bash
    conda activate tensorflow
    ```

1. The TensorFlow CPU and GPU versions requires pip to be up-to-date. To install and upgrade pip to the latest version, within your conda environment use the below command. See our [section](../../cheaha/open_ondemand/ood_jupyter.md#pip-installs-packages-outside-of-environment), on why installing pip within a conda environment is advised.

    ```bash
    pip install --upgrade pip
    ```

1. Install TensorFlow with pip

    ```bash
    pip install tensorflow[and-cuda]
    ```

The image below shows an output that the TensorFlow library will utilize the available GPU.

![TensorFlow GPU output](images/tensor_gpu.png)

<!-- markdownlint-disable MD046 -->
!!! note

    The information (I) and warning (W) outputs notifies you of the installed Tensorflow binary and how it would function. The I output informs you that the installed Tensorflow library will utilize your CPU for additional speed when GPUs are not the most efficient way to do processing for these operations. The W output tells you TensorRT is not available, please note TensorRT is not currently supported on our systems.
<!-- markdownlint-enable MD046 -->

Now that you have completed the tutorial, you can find more Anaconda information here, [Using Anaconda page](../../workflow_solutions/using_anaconda.md#anaconda).
