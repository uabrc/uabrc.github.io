---
toc_depth: 1
---

# Glossary

## Introduction

This glossary defines key terms related to the Research Computing system to help researchers, administrators, help desks, and users effectively use our resources, and also serving as a helpful reference for understanding the system's terminology, listed alphabetically below.

 [A](#a) [**B**](#b) [**C**](#c) [**D**](#d) [**E**](#e) [**F**](#f) [**G**](#g) [**H**](#h) [**I**](#i) [**J**](#j) [**K**](#k) [**L**](#l) [**M**](#m) [**N**](#n) [**O**](#o) [**P**](#p) [**Q**](#q) [**R**](#r) [**S**](#s) [**T**](#t) [**U**](#u) [**V**](#v) [**W**](#w) [**X**](#x) [**Y**](#y) [**Z**](#z)

### A

**A100 GPU**
:  High-performance GPU from NVIDIA, commonly used in AI/ML workloads.

**section:Account**
:  Refers to the user credentials that you use to log into the Research Computing systems.

**section:ACLs**
:  Access Control Lists (ACLs) is a mechanism used to define permissions for files and directories in an HPC system.

**section:Allocation**
:  Refers to the designated LTS storage quota assigned to a individual user or their Lab or Core Facility.

**section:amperenodes**
:  Nodes that are equipped with Ampere architecture GPUs, used for high-performance computing.

**section:Anaconda**
:  A distribution of Python for scientific computing and machine learning, including package management and environment management tools.

**section:Array Job**
:  A job type in HPC used to submit and execute a large number of identical or similar tasks in parallel, managed efficiently under a single job submission.

### B

**section:Binary**
:  A compiled program, also called executable, software or file that the operating system can execute directly.

**section:BlazerID**
:  The user name that will bed used to connect to any UAB system.

**section:Bucket**
:  A bucket is the root which objects are stored in Long Term Storage (LTS) systems, it is similar to a root directory or folder in traditional file system.

**section:Bucket Policy**
:  A set of permissions defining access control for a and LTS storage bucket/object.

### C

**section:Ceph**
:  A distributed object storage system designed for scalability and fault tolerance. Please refer [Ceph](https://ceph.io/en/) for details.

**section:Cheaha**
:  A shared cluster computing environment for UAB researchers.

**section:CICD**
:  Continuous Integration (CI) and Continuous Deployment(CD) are practices for automating software testing and deployment.

**section:Cloud**
:  A network of remote servers that provide computing resources such as storage, processing power, and applications on demand over the internet.

**section:Commercial Software**
:  Licensed software (such as Amber, Ansys, Gurobi, LS-Dyna, Mathematica, SAS, Stata) used for specialized computing tasks in various scientific and engineering fields.

**section:Community Container**
:  A prebuilt, shared containerized environment designed for use by multiple researchers.

**section:Compute node**
:  A dedicated server in Cheaha cluster designed to perform computational tasks.

**section:Conda**
:  Package and environment management system for Python and other languages.

**section:Core**
:  Individual processing unit within a CPU that can execute tasks.

**section:CUDA**
:  NVIDIA's parallel computing platform and API that enables GPU acceleration for computing tasks.

### D

**section:Data transfer**
:  The process of moving files between local systems and Cheaha, or between storage locations on the Research computing system.

**section:Docker Image**
:  A snapshot of the libraries and dependencies required inside a container for an application to run.

**section: Duo 2FA**
:  A two-factor authentication system used for securing user access.

### E

**section:Exosphere**
:  please refer [Exosphere](https://ieeexplore.ieee.org/document/9308090)

### F

**section:FLOPS**
:  Floating Point Operations Per Second (FLOPS), a measure of computational performance.

### G

**section:GitLFS**
:  A Git extension for versioning large files, used to store binary files outside the repository. Please refer [GitLFS](https://git-lfs.com/) for details.

**section:Globus**
:  A data transfer tool that enables fast and secure research data transfers between our local systems and Cheaha system, or between storage locations on the Cheaha system.

**section:Globus CLI**
:  A command line tool that allows users to manage file transfers, automate workflows, and interact with Globus services without using the web interface.
**section:Globus Collection**
:  A logical representation of data storage that is accessible via the Globus service.

**section:Globus Connect Personal**
:  A software application that allows individual users to transfer files between their personal devices and other Globus-enabled storage systems.

**section:Globus Connect Server**
:  A server-side software that enables institutions or organizations to connect their storage systems to Globus.

**section:Globus Group**
:  A collection of users managed through Globus for access control and collaboration.

**section:GPFS storage**
:  General Parallel File System (GPFS) storage provides scalable and distributed storage to manage large amounts of data efficiently. For example, Cheaha project directory is a GPFS storage.

**section:GPU**
:  Graphics Processing Units (GPUs), specialized hardware for parallel processing, often used in machine learning, deep learning, and other computationally intensive tasks.

**section:GRES**
:  A Generic Resource Scheduling (GRES), refers to resources like GPUs that are shared across jobs.

### H

**section:High Performance Computing (HPC)**
:  A computing system that enables the processing of large datasets and complex computations at high speeds using parallel processing techniques (it focuses on solving a problem as quickly as possible.).

**section:High Throughput Computing (HTC)**
:  A computing model focused on maximizing the number of tasks completed in a given time frame, often used for handling large-scale batch processing (it focuses on completing a large number of jobs over a long period of time).

**section:Horizon**
:  A web-based Dashboard with graphical interface to manage and interacting with OpenStack services. Please refer [Horizon](https://docs.openstack.org/horizon/latest/?utm_source=chatgpt.com) for details.

**section:Host**
:  A computer or system that provides services or resources to other systems in a network.

### I

**section:Identity and Access Management (IAM)**
:  A framework of policies that help you securely control access to system resources.

**section:Instance**
:  A virtualized compute resource in the cloud, often running as a virtual machine, with allocated resources (such as CPU, memory, and storage resources).

**section:Interactive Apps**
:  Applications used to interact with applications in openOn Demand(OOD) portal that during job execution.

**section:Ipykernel**
:  The IPython kernel (Ipykernel) is the backend component that executes Python code in Jupyter notebooks.

### J

**section:Jetstream**
:  A cloud-based research computing platform offering on-demand computing resources, primarily for scientific research. Please refer [Jetstream](https://dl.acm.org/doi/10.1145/3437359.3465565)

**section:Jobs**
:  Tasks submitted to the Cheaha system for execution, typically managed by a SLURM scheduler.

**section:Job Composer**
:  A feature in OpenOnDemand (OOD) portal used to define and manage job specifications for execution.

**section:JobID**
:  A unique identifier assigned to a job when it is submitted for execution in the system.

**section: Job submission script**
:  A script containing resource requests and commands to execute a job on an HPC system, usually used with a scheduler like SLURM.

### K

**section:Key pairs**
:  These can be keys used to securely access virtual machines or cloud instances via SSH (a public key and private key). They can also be used as a username (access key) and password (secret key) to access LTS (Long-Term Storage).

**section:Keras**
:  A high level neural network API that runs on top of TensorFlow for training machine learning and deep learning models.

### L

**section:largemem**
:  A class of nodes or partition with large memory resources, used for running memory intensive tasks.

**section:Local Scratch**
: A local storage directly attached to compute nodes, offering fast read/write speeds, typically used for temporary storage during job execution on that node.

**section:Login node**
:  An entry point to a Cheaha cluster for users.

**section:Long-Term Storage**
:  An S3 object-storage platform hosted at UAB which is designed to hold data that is not currently being used in analysis but should be kept for data sharing or reused for further analysis in the future.

### M

**section:Mamba**
:  A replacement/reimplementation of the conda package manager that improves package dependency resolution and installation speed.

**section:Mambaforge**
:  A preconfigured distribution of Miniconda that includes Mamba as the default package manager.

**section:MATLAB**
:  Application software for numerical computation, data analysis, and visualization.

**section:Memory**
:  The system's storage, typically called RAM, allocated to a job for temporary data storage during its execution.

**section:Message Passing Interface (MPI)**
:  A standardized communication protocol used for parallel computing, enabling processes to exchange data efficiently across multiple nodes.

**section:Miniforge**
:  A minimal Conda installer that provides a flexible way to manage Python environments.

**section:Miniconda**
:  A minimal version of Anaconda that includes only Conda, Python, and essential dependencies.

**section:Module**
:  A system that manages environment settings for software packages on HPC, allowing users to load, unload, and switch between different software versions.

**section:module load**
:  A command used to load a specific software module into the environment, making it available for use.

**section:module reset**
:  A command that unloads all currently loaded modules and restores the default environment settings.

**section:My Interactive Sessions**
:  User-specific sessions in the OpenOnDemand (OOD) portal that allow us to view the list of jobs or sessions we have requested.

### N

**section:Network scratch**
:  Network scratch can be a user scratch which is available under directory `/scratch/$USER` or `$USER_SCRATCH` on the Cheaha login node and each compute node.

**section:Node**
:  A single computational unit in an HPC cluster, containing processors, and memory.

**section:noVNC**
:  A browser-based Virtual Network Computing (VNC) client that allows users to access remote graphical desktops over the web.

**section:Nvidia-smi**
:  Command for monitoring and managing NVIDIA GPU devices.

### O

**section:OOD**
:  Open OnDemand (OOD) is a web based portal that provides users with easy access to compute resources, file systems, and job management tools through a graphical interface, in HPC environment.

**section:Open Science Grid (OSG)**
:  A distributed computing infrastructure that provides high-throughput computing resources for scientific research.

**section:OpenStack**
:  An open-source cloud computing platform that controls large pools of computing, storage, and networking resources. Please refer [OpenStack](https://www.openstack.org/) for details.

### P

**section:Package**
:  A collection of software components bundled together to provide specific functionality, commonly managed via Conda, Pip.

**section:pascalnodes**
:  Nodes equipped with Pascal architecture GPUs, typically used for machine learning or simulations.

**section:P100 GPU**
:  NVIDIA's Pascal-based GPU, widely used in scientific computing and deep learning tasks.

**section:Parabricks**
:  NVIDIA-accelerated toolkit for genomic data analysis, providing fast and efficient workflows.

**section:Partition**
:  A logical group of nodes that are organized based on their hardware, usage type, or priority.

**section:PyTorch**
:  An open source framework, developed by Meta, that provides tools for developing and training deep learning models.

### Q

**section: Quality of Service (QoS) Limits**
:  A set of parameters in an HPC scheduler defining job priorities, resource limits, and execution policies. It allow us to balance usage and ensure fairness for all researchers using the cluster.

**section:Quota**
:  Limits on resources such as storage or computational time allocated to a user.

### R

**section:rclone**
:  A command-line program for managing and syncing files between local storage and cloud services, often used for data transfers in HPC environments.

**section:Remote Tunnels**
:  Secure SSH-based connections that allow forwarding of ports from an HPC system to a local machine, enabling remote access to services.

**section:RStudio**
:  An integrated development environment (IDE) for R programming, used for statistical computing and data analysis.

### S

**section:sacct**
:  A command used to retrieve job accounting data in Slurm.

**section:sbatch**
:  A SLURM command used to submit batch jobs to the scheduler.

**section:scancel**
: A command used to cancel or halt a job in Slurm.

**section:ScienceDMZ**
: Please refer [ScienceDMZ](https://fasterdata.es.net/science-dmz/)

**section:Scheduler**
:  A workload manager in an HPC system such as SLURM that allocates resources and schedules jobs based on priority, policies, and availability.

**section:Scratch Retention Policy**
:  The set of rules governing how long data can be stored in an HPC scratch Storage space before automatic deletion.

**section:Secure SHell (SSH)**
:  A protocol used for secure remote access to servers or HPC systems.

**section:Security Policy**
:  A set of rules and configurations that define access controls, permissions, and security settings to protect systems and data.

**Section:seff**
:  A command used to display job efficiency in Slurm.

**section:Shared Collection**
:  A Globus collection that allows multiple users to access and manage shared data resources securely.

**section:Shared Storage**
:  A centralized storage space (e.g Cheaha project directory, or Shared LTS allocation) used for collaborative work by multiple users, managed by the PIs.

**section:Single Sign-On (SSO)**
:  An authentication mechanism that allows users to login once and access multiple HPC and institutional services without reentering credentials.

**section:Singularity**
:  A containerization platform used for creating and running portable, reproducible environments in high-performance computing.

**section:SLURM**
:  Simple Linux Utility for Resource Management (SLURM), a popular workload manager in HPC systems. It schedules jobs based using resource requests such as number of CPUs, maximum memory (RAM) required per CPU, maximum run time, and more.

**section:SlURM Flags**
:  Options or parameters used in SlURM job scripts to control resource allocation, scheduling, and execution behavior.

**section:Snapshot**
:  A copy of a file system, disk, or virtual machine, allowing for backup, or cloning purposes.

**section:srun**
:  A command in SLURM used to launch parallel jobs directly on allocated compute resources.

**section:State**
:  The current status of a job in the scheduler, such as pending, running, completed, or failed.

**section:Storage**
:  Resources allocated for storing data that includes home/user, project, scratch directories on Cheaha and LTS.

**section:Submit Jobs**
:  The process of queuing computational tasks to run on the HPC system using a job scheduler such as SLURM.

**section:S3cmd**
:  A command-line tool for managing data in Amazon S3 and S3-compatible storage (example UAB LTS).

**section:S5cmd**
:  A command-line tool for interacting with S3 storage, optimized for speed and parallelism (example UAB LTS).

**section:squeue**
:  A command used to display the status of jobs in the SLURM queue.

### T

**section:TensorFlow**
:  An open-source machine learning framework, developed by Google, commonly used for building and training deep learning models.

**section:TRES**
:  A TRES is a resource that can be tracked for usage or used to enforce limits against. Please refer [TRES](https://slurm.schedmd.com/tres.html) for details.

### U

**section:UAB Cloud**
:  A cloud service provided by UAB Research Computing, also called "cloud.rc" is a portal based on OpenStack cloud software, for more permanent research applications such as web pages and database hosting and develop applications for high performance compute.

**section:UAB Box**
:  An alternative storage solutions provide and maintained by UAB IT, that allows users to store, access, and share documents, research data, and other files.

### V

**section:Virtual Machine (VM)**
:  A software-based computer that provides a virtualized environment, that functions like a physical computer, for running applications or operating systems.

**section:VSCode**
:  A lightweight and extensible code editor, developed by Microsoft, that support multiple programming languages.

**section:Volumes**
:  Virtual storage devices used to persist data, often associated with Virtual Machines (VM) or cloud environments.

### W

**section:Workflow Manager**
:  Software that automates the execution and management of tasks in a predefined workflow or pipeline. For example [Snakemake](https://snakemake.readthedocs.io/en/stable/), [Nextflow](https://www.nextflow.io/), etc.

### X

**section:XIAS account**
:  A guest user credential for non-UAB individuals who need access to our HPC system. It uses the guest's email, alos XIAS email, as the username.

**section:XNAT**
:  Imaging data management platform commonly used in medical and neuroscience research. Please refer [XNAT](https://www.xnat.org/) for details.

### Y

### Z
<!-- <glossary::section> -->
