# Open OnDemand

Open OnDemand (OOD) is the web portal to access Cheaha. On it, we can submit interactive jobs in easy to use forms. These jobs include a generic desktop as well as specific apps such as RStudio or MATLAB. There is also access to a basic file manager for viewing and moving files.

The web portal can be accessed at [https://rc.uab.edu](https://rc.uab.edu) and is available both on and off campus.

## Quickstart

To start a generic desktop job where any piece of software can run, do the following:

1. Go to [Cheaha's web portal](https://rc.uab.edu)
1. Click Interactive Apps > HPC Desktop at the top.
1. Select the resources needed for the job (number of CPUs, amount of memory, job runtime, and partition).
      1. As an example, a generic desktop job could use 1 CPU and 8 GB of RAM.
      1. See our [partition table](https://docs.rc.uab.edu/cheaha/hardware/#summary) to determine which partition fits the job. The requested amount of time should not exceed the partition limit.
1. Click Launch at the bottom. This will open the "My Interactive Sessions" page and a job card will be created for the interactive job.
1. When the job card is created, the job is added to a queue. It will remain gray while in queue but will turn green when the job has been allocated resources and is running. Click the `Launch Desktop in new tab` button to open the interactive job.

Every interactive job requested in OOD is already set on a compute node. This bypasses the login node and is the preferred method for running interactive jobs on Cheaha.

### Choosing Resources

For a more complete description of how to select resources, go [here](ood_layout.md#creating-an-interactive-job)

## Debugging OOD Job Failures

If your OOD job cards are disappearing after being allocated or during the job, see our [documentation](ood_layout.md#debugging-ood-job-failures) for instructions on how to retrieve the logs and submit a ticket to Research Computing support.

## Choosing the Right Jupyter Application

Jupyter environments have revolutionized the way researchers, analysts, and developers interact with code. Whether you have workflows in Python, visualizing genomic data, running simulations or run any kind of computational workflow on our high-performance computing (HPC) cluster, you've likely encountered using [Jupyter Notebook](./ood_jupyter.md) and/or [JupyterLab](./ood_jupyterlab.md), we have detailed information for using both on Cheaha. Both applications are open-source web tools designed for creating and sharing documents that can include your code, equations, visualizations, and narrative text. Their main purpose is to offer an interactive environment for all phases of your data analysis life cycle including, data exploration, analysis, and visualization. But when should you choose one over the other on Cheaha to run your computational workflow?

This article aims to help you decide between using Jupyter Notebook and JupyterLab, by comparing both Jupyter Apps, looking at their strengths and weaknesses, and how they measure up to your needs, especially on Cheaha.

### What They Have in Common

Before listing out some of the differences, below are similarities between Jupyter NoteBooks and JupyterLab.

1. They use the same underlying kernel system. (i.e. environments created for use with Jupyter Notebook can also be used in JupyterLab and vice-versa).
1. They both support `.ipynb` notebooks.
1. They allow interactive code execution, plotting, markdown, and data visualization.
1. They can run Python, R, Julia, and other supported languages.
1. They are both great for reproducing workflows.
1. You can access both on Cheaha, selecting the configuration and resources required for your workflow.

### Why Choose JupyterLab?

JupyterLab is the next-generation interface for Jupyter. It's designed to be a full-featured web-based IDE. JupyterLab provides an interface for interactive and exploratory computing. Although it includes many features typical of traditional integrated development environments (IDEs), its primary focus remains on interactive and exploratory computing. The following are reasons why you may use JupyterLab over Jupyter Notebook.

1. JupyterLab will be your preferred app, if you are conversant with its use, or your workflow requires you to manage multiple notebooks, terminals, and other files at the same time. JupyterLab allows you to within a single browser tab. Run your code, analyze logs, edit documentation, and move between tasks within your workflow more quickly.
1. JupyterLab allows you to manage projects that involve code, markdown, output files, and terminals all within a single browser tab. You can split these elements into separate JupyterLab tabs, eliminating the need to switch between different browser tabs. (Illustrated below are 1 - JupyterLab launch page, 2 - a Terminal, 3 - a Notebook file, 4 - another Notebook file, 5 - a Markdown file)
1. If you want a more customizable and extensible environment, JupyterLab supports extensions out-of-the-box. If you need a Git GUI or a table of contents for navigating long notebooks? JupyterLab lets you add these features easily, making it more like a lightweight IDE than just a notebook viewer. Please visit [JupyterLab's official documentation page](https://jupyterlab.readthedocs.io/en/stable/user/extensions.html#extensions) to get more information about JupyterLab Extensions.

![!Screenshot of a browser tab showing a JupyterLab interface with notebook + terminal + markdown tabs open side-by-side.](./images/jupyterlabsample.png)

### Why Choose Jupyter Notebook?

Jupyter Notebook offers the classic, streamlined experience that focuses on a single document at a time. The Jupyter Notebook interface is  ideal for teaching, learning, or lightweight research tasks. The interface is what many users are already familiar with. The following are reasons why you might use Jupyter Notebook over JupyterLab.

1. If as a beginner or a user focusing on a single notebook or analysis for a computational workflow, the simplicity of Jupyter Notebook will serve simple needs well. As there is very little to learn compared to JupyterLab, there are fewer buttons to click to complete tasks.
1. While teaching a class, developing tutorials, or conducting workshops where simplicity is a priority, Jupyter Notebook will help you minimize distractions. Compared to JupyterLab, which has many options and features, Jupyter Notebook allow the audience to stay focused on writing and running their code without navigating a complex interface.
1. Jupyter Notebook is also excellent for running very quick exploratory data analysis, you can test out sample code and data, develop quick plots. Without all of the additional complexities JupyterLab may need while setting it up.

![!Screenshot of Jupyter Notebook showing a single notebook open with code and output.](./images/jupyternotebooksample.png)
