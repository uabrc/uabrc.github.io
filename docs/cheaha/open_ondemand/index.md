# Open OnDemand

Open OnDemand (OOD) is the web portal to access Cheaha. On it, we can submit interactive jobs in easy to use forms. These jobs include a generic desktop as well as specific apps such as RStudio or MATLAB. There is also access to a basic file manager for viewing and moving files.

The web portal can be accessed at <https://rc.uab.edu> and is available both on and off campus.

## Quickstart

To start a generic desktop job where any piece of software can run, do the following:

1. Go to [Cheaha's web portal](https://rc.uab.edu)
1. Click Interactive Apps > HPC Desktop at the top.
1. Select resources needed for the job, such as number of CPUs, amount of memory per CPU, job runtime, and partition.
      1. As an example, a generic desktop job could use 1 CPU and 8 GB of RAM.
      1. See our [partition table](https://docs.rc.uab.edu/cheaha/hardware/#summary) to determine which partition fits the job. The requested amount of time should not exceed the partition limit.
1. Click Launch at the bottom. This will open the "My Interactive Sessions" page and a job card will be created for the interactive job.
1. When the job card is created, the job is added to a queue. It will remain gray while in the queue, then turn blue when the job starts but is not yet ready for interaction. Once the job has been allocated resources and is actively running, it will turn green. Click the `Launch Desktop in new tab` button to open the interactive job.

Every interactive job requested in OOD is already set on a compute node. This bypasses the login node and is the preferred method for running interactive jobs on Cheaha.

### Choosing Resources

For a more complete description of how to select resources, please see our [Creating an Interactive Job](ood_layout.md#creating-an-interactive-job) section.

## Debugging OOD Job Failures

If your OOD job cards are disappearing after being allocated or during the job, see our [OOD Job Failures section](ood_layout.md#debugging-ood-job-failures) for instructions on how to retrieve the logs and submit a ticket to Research Computing support.

## Choosing the Right Jupyter Application

Jupyter environments like [Jupyter Notebook](./ood_jupyter_notebook.md) and [JupyterLab](./ood_jupyterlab.md) have revolutionized the way researchers, analysts, and developers interact with code. Whether you're writing Python scripts to visualize genomic data, running simulations, or working through any computational workflow, you've likely encountered one or both of these tools. We provide detailed documentation on how to use them effectively on Cheaha. Both applications are open-source web tools designed for creating and sharing documents that can include your code, equations, visualizations, and narrative text. Their primary purpose is to offer an interactive environment for all phases of your data analysis life cycle including, data exploration, analysis, and visualization. So, how would you choose between Jupyter Notebook and JupyterLab when running your workflow on Cheaha?

This article aims to help you decide between using Jupyter Notebook and JupyterLab, by comparing both Jupyter Apps, looking at their strengths and weaknesses, and how they measure up to your needs, especially on Cheaha.

### What They Have in Common

Before listing out some of the differences, below are similarities between Jupyter NoteBooks and JupyterLab.

- They use the same kernel system, so that notebooks written in one can be used on another.
- They both support `.ipynb` notebooks.
- They allow interactive code execution, plotting, markdown, and data visualization.
- They can run Python, R, Julia, and other supported languages.
- They are both great for reproducing workflows.
- You can access both on Cheaha, selecting the configuration and resources required for your workflow.

### Why Choose JupyterLab?

JupyterLab is the next-generation interface for Jupyter, designed as a full-featured web-based IDE. While it includes many features typical of traditional integrated development environments (IDEs), its core strength lies in supporting interactive, exploratory workflows.

The following are reasons why you might choose JupyterLab over Jupyter Notebook.

- JupyterLab will be your preferred app, if you are familiar with its use, or your workflow requires you to manage multiple notebooks, terminals, and other files at the same time. JupyterLab allows you to within a single browser tab. Run your code, analyze logs, edit documentation, and move between tasks within your workflow more quickly.
- JupyterLab allows you to manage projects that involve code, markdown, output files, and terminals all within a single browser tab. You can split these elements into separate JupyterLab tabs, eliminating the need to switch between different browser tabs. (Illustrated below are 1 - JupyterLab launch page, 2 - a Terminal, 3 - a Notebook file, 4 - another Notebook file, 5 - a Markdown file)
- If you want a more customizable and extensible environment, JupyterLab supports extensions out-of-the-box. If you need a Git GUI or a table of contents for navigating long notebooks? JupyterLab lets you add these features easily, making it more like a lightweight IDE than just a notebook viewer. Please visit [JupyterLab's official documentation page](https://jupyterlab.readthedocs.io/en/stable/user/extensions.html#extensions) to get more information about JupyterLab Extensions.

![!Screenshot of a browser tab showing a JupyterLab interface with notebook + terminal + markdown tabs open side-by-side.](./images/jupyterlabsample.png)

### Why Choose Jupyter Notebook?

Jupyter Notebook offers the classic, streamlined experience that focuses on a single document at a time. The Jupyter Notebook interface is ideal for teaching, learning, or lightweight research tasks. The interface is what many users are already familiar with. The following are reasons why you might use Jupyter Notebook over JupyterLab.

- If as a beginner or a user focusing on a single notebook or analysis for a computational workflow, the simplicity of Jupyter Notebook will serve your needs well. As there is very little to learn compared to JupyterLab, there are fewer buttons to click to complete tasks.
- While teaching a class, developing tutorials, or conducting workshops where simplicity is a priority, Jupyter Notebook will help you minimize distractions. Compared to JupyterLab, which has many options and features, Jupyter Notebook allow the audience to stay focused on writing and running their code without navigating a complex interface.
- Jupyter Notebook is excellent for quick exploratory data analysis, such as testing a short Python function or generating a simple matplotlib plot, as shown in the screenshot example. You can launch it and immediately start writing code in the notebook, without dealing with additional panes or extensions, as is often the case with JupyterLab. This makes it ideal for fast iteration, quick testing, and minimal setup.

![!Screenshot of Jupyter Notebook showing a single notebook open with code and output.](./images/jupyternotebooksample.png)
