# Jupyter Apps

Jupyter Notebooks and Jupyter Lab are both available as standalone apps in OOD. Jupyter is commonly used with Anaconda environments. If you are unfamiliar with Anaconda environments please see the [Working with Anaconda Environments section](#working-with-anaconda-environments) below before continuing here.

As with all interactive apps, you'll need to select the resources required using the job creation form. Jupyter may also require additional initial setup before the app launches. To modify the environment that Anaconda and Jupyter will run in, please use the Environment Setup field to load modules. For GPU applications you'll need to load a `CUDA/*` module. If working with deep learning workflows, you will also possibly need to load the `cuDNN/*-CUDA-*` module corresponding to your choice of `CUDA/*` module version. These are required for popular ML/DL/AI libraries like TensorFlow, Keras, and PyTorch. Use `module spider cuda` and `module spider cudnn` to view the list of appropriate modules. An example of what to put in the Environment Setup field, when using Tensorflow in a Jupyter notebook, is shown below.

```shell
# ENVIRONMENT SETUP
module load CUDA/12.2.0
module load cuDNN/8.9.2.26-CUDA-12.2.0
```

For information on which versions of CUDA to load for Tensorflow and PyTorch, please see [Tensorflow Compatibility](../slurm/gpu.md#tensorflow-compatibility) and [PyTorch Compatibility](../slurm/gpu.md#pytorch-compatibility).

<!-- markdownlint-disable MD046 -->
!!! note

    If you get a Failed to Connect message when opening the job, close the tab and wait a couple of minutes. Jupyter is still initializing and takes some time after the job first begins running.
<!-- markdownlint-enable MD046 -->

<!-- markdownlint-disable MD046 -->
!!! important

    If you are not able to see your environment, you may need to install the `ipykernel` package. It is required for Jupyter to recognize your environment. See [Packages for Jupyter](../../workflow_solutions/using_anaconda.md#packages-for-jupyter) for more information.
<!-- markdownlint-enable MD046 -->

<!-- markdownlint-disable MD046 -->
!!! important

    Do not load `module load Anaconda3` in the `Environment Setup` field, as it is loaded automatically. Loading any versions of `Anaconda3` would affect the Python executable, which is used by default. These results in hard-to-diagnose errors in the OOD Jupyter notebook.
<!-- markdownlint-enable MD046 -->

<!-- markdownlint-disable MD046 -->
!!! warning

    Having `conda/mamba activate` and `source activate` statements in the `Environment Setup` field can cause unexpected and silent job failure. Avoid using `conda activate` in the `Environment Setup` field.
<!-- markdownlint-enable MD046 -->

## Environment Setup

## Extra Jupyter Arguments

The `Extra Jupyter Arguments` field allows you to pass additional arguments to the Jupyter Server as it is being started. It can be helpful to point the server to the folder containing your notebook. To do this, assuming your notebooks are stored in `/data/user/$USER`, also known as `$USER_DATA`, put `--notebook-dir=$USER_DATA` in this field. You will be able to navigate to the notebook if it is in a subdirectory of `notebook-dir`, but you won't be able to navigate to any other directories. An example is shown below.

![!Jupyter Notebook job request form Extra jupyter arguments field.](./images/ood_jupyter_notebook_extra_args_box.png)

## Working with Anaconda Environments

By default, Jupyter notebooks will use the base environment that comes with the Anaconda3 module. This environment contains a large number of popular packages and may useful for something quick, dirty, and simple. However, for any analysis needing specific package versions or special packages, you will need to create your own environment. For information on creating and managing Anaconda environments please see our [Using Anaconda page](../../workflow_solutions/using_anaconda.md). The please review our [Cheaha-specific Anaconda page](../software/software.md#anaconda-on-cheaha) for important tips and how to avoid common pitfalls.

## Help GPU is not Available with TensorFlow or PyTorch

If you are using Jupyter with TensorFlow or PyTorch and no GPU is found, please see our Slurm GPU page sections on [TensorFlow Compatibility](../slurm/gpu.md#tensorflow-compatibility) and [PyTorch Compatibility](../slurm/gpu.md#pytorch-compatibility). For MATLAB, please see [MATLAB Compatibility](../slurm/gpu.md#matlab).