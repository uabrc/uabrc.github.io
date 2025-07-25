# JupyterLab

As described on JupyterLab's [documentation page](https://jupyterlab.readthedocs.io/en/latest/)
>JupyterLab is a highly extensible, feature-rich notebook authoring application and editing environment, and is a part of [Project Jupyter](https://docs.jupyter.org/en/latest/), a large umbrella project centered around the goal of providing tools (and [standards](https://docs.jupyter.org/en/latest/#sub-project-documentation)) for interactive computing with computational notebooks. A [computational notebook](https://docs.jupyter.org/en/latest/#what-is-a-notebook) is a shareable document that combines computer code, plain language descriptions, data, rich visualizations like 3D models, charts, graphs and figures, and interactive controls. A notebook, along with an editor like JupyterLab, provides a fast interactive environment for prototyping and explaining code, exploring and visualizing data, and sharing ideas with others.

To launch a JupyterLab session, visit [Cheaha's Open On Demand home page](https://rc.uab.edu/), and select the menu items "Interactive Apps -> JupyterLab". The job creation and submission form appears:

![!JupyterLab home form](./images/ood_jupyterlab_home_form.png)

As with all interactive apps, you'll need to select the resources required using the job creation form. JupyterLab as with Jupyter Notebook may also require additional initial setup before the app launches.

## Environment Setup

To modify the environment that Conda and your JupyterLab will run in, please use the "Environment Setup" field to load modules and modify the environment `$PATH`. Be aware that any changes to the environment made in this window will be inherited by terminals as well as notebooks opened within your JupyterLab session.

### CUDA

See [Jupyter Notebook CUDA](./ood_jupyter.md#cuda) section.

## Extra JupyterLab Arguments

See [Jupyter Notebook Arguments](./ood_jupyter.md#extra-jupyter-notebook-arguments) section.

## Working with other programming languages within JupyterLab

Please follow the instructions found in [Working with other programming languages within Jupyter Notebook](./ood_jupyter.md#working-with-other-programming-languages-within-jupyter-notebook)

## Working with Conda Environments using JupyterLab

By default, JupyterLab on Cheaha will launch using the `base` conda environment. While this default environment includes a wide range of popular packages and can be helpful for quick or exploratory tasks, it is not recommended for research workflows that require specific package versions or custom dependencies. For reproducible and stable analysis, it’s best to create and use a dedicated Conda environment tailored to your project or research workflow. Once created, you can register the environment as a Jupyter kernel and select it directly from within JupyterLab. For information on creating and managing Conda environments please see our [Using Anaconda page](../../workflow_solutions/using_anaconda.md). Then please review our [Cheaha-specific Anaconda page](../software/software.md#anaconda-on-cheaha) for important tips and how to avoid common pitfalls.

![! Landing page of JupyterLab when you launch the Interactive session](images/ood_jupyterlab_landingpage.png)

The python icons you see in the image above, are Conda environments that open into a Notebook (like with Jupyter Notebooks) interface with the selected environment activated.

### Creating a Conda Environment for use with JupyterLab

Please see instructions for creating a Conda environment in the [Creating an Environment for use with Jupyter Notebook](./ood_jupyter.md#creating-an-environment-for-use-with-jupyter-notebook) section.

### Changing Environments using JupyterLab GUI

1. From the JupyterLab interface, click on the "Kernel" menu in the top navigation bar, and choose the "Change Kernel" option.

![!Image highlighting the Kernel tab and Change Kernel option in JupyterLab](images/ood_jupyterlab_changekernel.png)

1. A new dialog window will open, with a list of all available kernels that match your Conda environments. Select your preferred kernel and click on the "Select" button. If you do not see your environment in here, then you will need to install the "ipykernel" package with `conda install ipykernel`.

![!Select Kernel dialog window to select a Kernel in JupyterLab](images/ood_jupyterlab_selectkernel.png)

1. Your selected environment would appear in the top right corner.

![!JupyterLab notebook interface with the selected kernel highlighted](images/ood_jupyterlab_selectedkernel.png)

## Common Issues in OOD JupyterLab

### Python Executable Issues

See the [Python Executable Issues](./ood_jupyter.md#python-executable-issues) section for Jupyter Notebook.

### Unexpected/Silent Job Failure

See our [Unexpected/Silent Job Failure](./ood_jupyter.md#unexpectedsilent-job-failure) section for Jupyter Notebook.

### Tensorflow and PyTorch GPU issues

Refer to [Tensorflow and PyTorch GPU issues](./ood_jupyter.md#tensorflow-and-pytorch-gpu-issues) section for Jupyter Notebook.
