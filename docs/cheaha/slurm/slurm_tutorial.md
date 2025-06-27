---
toc_depth: 3
---

# Writing Slurm Batch Jobs

This Slurm tutorial serves as a hands-on guide for users to create Slurm batch scripts based on their specific software needs and apply them for their respective usecases. It covers basic examples for beginners and advanced ones, including sequential and parallel jobs, array jobs, multithreaded jobs, GPU utilization jobs, and MPI (Message Passing Interface) jobs. To know which type of batch jobs are suitable for your pipeline/usecase, please refer to the [User Guide](#slurm-batch-job-user-guide) section.

<!-- markdownlint-disable MD046 -->
!!! note

    CUDA modules are used in some of these tutorials. Please note that the latest CUDA and cuDNN are now available from [Conda](../slurm/gpu.md#cuda-and-cudnn-modules). The tutorials provide good practices, but age over time. You may need to modify the scripts to be suitable for your work.
<!-- markdownlint-enable MD046 -->

## Structure of a Slurm Batch Job

Below is the template for a typical Slurm job submission in the Cheaha high-performance computing (HPC) system. The script begins with `#!/bin/bash`, indicating it is a bash script. The next step would be to declare Slurm configuration options, specifying the required resources for job execution. This section typically comprises parameters such as CPU count, partition, memory allocation, time limit, etc. Following the configuration, the script may include sections for loading necessary software or libraries required for the job.

```bash
#!/bin/bash
# Declaring Slurm configuration options and specifying required resources
...
# Loading Software/Libraries
...
# Running Code
...
```

The last portion is running the actual code or software. Here, the computational task or program intended for execution is launched using specific commands and processes, which depends on the software used and overall computational workflow. For more detailed specification, refer to [Slurm job submission](../slurm/submitting_jobs.md). The following sections present practical examples for writing a Slurm batch script to specific use cases, and prerequisites to start with the tutorial.

## Prerequisites

If you're new to using Unix/Linux commands and bash scripting, we suggest going through the software carpentry lesson, [The Unix Shell](https://swcarpentry.github.io/shell-novice/). Also, we recommend reviewing the [Cheaha Hardware Information](../../cheaha/hardware.md) to help guide you in choosing appropriate partition and resources.

## Slurm Batch Job User Guide

<!-- markdownlint-disable MD046 -->
!!! important

    All parts of the tutorials here should be run in a job context, instead of on the login node. If you are new to Cheaha, the simplest way to get started is to use an [Open OnDemand HPC Desktop Job](../open_ondemand/hpc_desktop.md).
<!-- markdownlint-enable MD046 -->

This user guide provides comprehensive insight into different types of batch jobs, facilitating in identifying the most suitable job type for your specific tasks. With clear explanations and practical examples, you will gain a deeper understanding of sequential, parallel, array, multicore, GPU, and multi-node jobs, assisting to make informed decisions when submitting jobs on the Cheaha system.

1. [A Simple Slurm Batch Job](#example-1-a-simple-slurm-batch-job) is ideal for Cheaha users who are just starting with Slurm batch job submission. It uses a simple example to introduce new users to requesting resources with `sbatch`, printing the `hostname`, and monitoring batch job submission.

1. [Sequential Job](#example-2-sequential-job) is used when tasks run one at a time sequentially. Adding more CPUs does not make a sequential job run faster. If you need to run many such sequential jobs simultaneously, you can submit it as an single [array job](#example-4-array-job). For instance, a Python or R script that executes a series of steps—such as data loading, extraction, analysis, and output reporting—where each step must be completed before the next can begin.

1. [Parallel Jobs](#example-3-parallel-jobs) is suitable for executing multiple independent tasks/jobs simultaneously and efficiently distributing them across resources. This approach is particularly beneficial for small-scale tasks that cannot be split into parallel processes within the code itself. For example, consider a Python script that operates on different data set, in such a scenario, you can utilize `srun` to execute multiple instances of the script concurrently, each operating on a different dataset and on different resources.

1. [Array Job](#example-4-array-job) is used for submitting and running multiple large number of identical tasks in parallel. They share the same code and execute with similar resource requirements. Instead of submitting multiple [sequential job](#example-2-sequential-job), you can submit a single array job, which helps to manage and schedule a large number of similar tasks efficiently. This improves efficiency, resource utilization, scalability, and ease of debugging. For instance, array jobs can be designed for executing multiple instances of the same task with slight variations in inputs or parameters such as perform [FastQC](https://home.cc.umanitoba.ca/~psgendb/doc/fastqc.help) processing on 10 different samples.

1. [Mutlithreaded or Multicore Job](#example-5-multithreaded-or-multicore-job) is used when software inherently support multithreaded parallelism i.e  run independent tasks simultaneously on multicore processors. For instance, there are numerous software such as [MATLAB](https://www.mathworks.com/help/matlab/ref/parfor.html), [FEBio](https://help.febio.org/FebioUser/FEBio_um_3-4-Section-2.6.html), [Xplor-NIH](https://nmr.cit.nih.gov/xplor-nih/doc/current/helperPrograms/options.html) support running multiple tasks at the same time on multicore processors. Users or programmers do not need to modify the code; you can simply enable multithreaded parallelism by configuring the appropriate options.

1. [GPU Jobs](#example-6-gpu-jobs) utilizes the parallel GPUs, which contain numerous cores designed to perform the same mathematical operations simultaneously. These examples may be helpful for users with pipelines and software that are designed to run on GPU-based systems and efficiently distribute tasks across cores to process large datasets in parallel. Examples of such software include, but are not limited to, [Tensorflow](https://www.tensorflow.org/guide/gpu), [Parabricks](../../education/case_studies.md#nvidia-clara-parabricks-for-performing-gpu-accelerated-genome-sequencing-analysis), and [PyTorch](https://pytorch.org/get-started/locally/).

1. [Multinode Job](#example-7-multinode-job) is for pipeline/software that can be distributed and run across multiple nodes. For example, MPI based applications/tools such as [Quantum Expresso](https://www.quantum-espresso.org/Doc/user_guide/node20.html), [Amber](https://usc-rc.github.io/tutorials/amber), [LAMMPS](https://docs.lammps.org/Run_basics.html), etc.

### Example 1: A Simple Slurm Batch Job

Let us start with a simple example to print `hostname` of the node where your job is submitted. You will have to request for the required resources to run your job using Slurm parameters (lines 5-10). To learn more about individual Slurm parameters given in the example, please refer to [Slurm flag and environment variables](../slurm/submitting_jobs.md#slurm-flags-and-environment-variables) and the official [Slurm documentation](https://slurm.schedmd.com/).
o
To test this example, copy the below script in a file named `hostname.job`. This job executes the `hostname` command (line 15) on a single node, using one task, one CPU core, 1 gigabyte of memory, with a time limit of 10 minutes. The output and error logs are directed to separate files with names based on their job name and ID (line 11 and 12). For a more detailed understanding of the individual parameters used in this script, please refer to the section on [Simple Batch Job](../slurm/submitting_jobs.md#a-simple-batch-job). The following script includes comments, marked with `###`, describing their functions. We will utilize this notation for annotating comments in subsequent examples.

```bash linenums="1"
#!/bin/bash

### Declaring Slurm configuration options and specifying required resources
#SBATCH --job-name=hostname     ### Name of the job
#SBATCH --nodes=1               ### Number of Nodes
#SBATCH --ntasks=1              ### Number of Tasks
#SBATCH --cpus-per-task=1       ### Number of Tasks per CPU
#SBATCH --mem=1G                ### Memory required, 1 gigabyte
#SBATCH --partition=express     ### Cheaha Partition
#SBATCH --time=00:10:00         ### Estimated Time of Completion, 10 minutes
#SBATCH --output=%x_%j.out      ### Slurm Output file, %x is job name, %j is job id
#SBATCH --error=%x_%j.err       ### Slurm Error file, %x is job name, %j is job id

### Running the command `hostname`
hostname
```

#### Submitting and Monitoring the Job

Now submit the script `hostname.job` for execution on Cheaha cluster using `sbatch hostname.job`. Slurm processes the job script and schedules the job for execution on the cluster. The output you see, "Submitted batch job 26035322," indicates that the job submission was successful, and Slurm has assigned a unique job ID `26035322`.

```bash
$sbatch hostname.job

Submitted batch job 26035322
```

After submitting the job, Slurm will create the output and error files with job name `hostname` and id `26035322`  as,

```bash
$ ls

hostname_26035322.err  hostname_26035322.out  hostname.sh
```

The submitted job will be added to the Slurm queue and will wait for available resources based on the specified job configuration and the current state of the cluster. You can use `squeue -j job_id` to monitor the status of your job.

```bash
$squeue -j 26035322

JOBID      PARTITION    NAME        USER    ST       TIME  NODES NODELIST(REASON)
26035322   express      hostname    USER    CG       0:01      1 c0156
```

The above output provides a snapshot of the job's status, resource usage,  indicating that it is currently running on one node (c0156). The term `CG` refers to completing its execution. For more details refer to [Managing Slurm jobs](../slurm/job_management.md). If the job is successful, the `hostname_26035322.err` file will be empty/without error statement. You can print the result using,

```bash
$ cat hostname_26035322.out
c0156
```

### Example 2: Sequential Job

This example illustrate a Slurm job that runs a Python script involving [NumPy](https://numpy.org/) operation. This python script is executed sequentially using the same resource configuration as [Example 1](../slurm/slurm_tutorial.md#example-1-a-simple-slurm-batch-job). Let us name the below script as `numpy.job`.

```bash linenums="1"
#!/bin/bash
#SBATCH --job-name=numpy            ### Name of the job
#SBATCH --nodes=1                   ### Number of Nodes
#SBATCH --ntasks=1                  ### Number of Tasks
#SBATCH --cpus-per-task=1           ### Number of Tasks per CPU
#SBATCH --mem=4G                    ### Memory required, 4 gigabyte
#SBATCH --partition=express         ### Cheaha Partition
#SBATCH --time=01:00:00             ### Estimated Time of Completion, 1 hour
#SBATCH --output=%x_%j.out          ### Slurm Output file, %x is job name, %j is job id
#SBATCH --error=%x_%j.err           ### Slurm Error file, %x is job name, %j is job id

### Loading Anaconda3 module to activate `pytools-env` conda environment
module load Anaconda3
conda activate pytools-env

### Run the script `python_test.py`
python python_test.py
```

 The batch job requires an input file `python_test.py` (line 17) for execution. Copy the input file from the [Containers page](../../workflow_solutions/getting_containers.md#create-your-own-docker-container). Place this file in the same folder as the `numpy.job`. This python script performs numerical integration and data visualization tasks, and it relies on the following packages: numpy, matplotlib, scipy for successful execution. These dependencies can be installed using [Anaconda](../../workflow_solutions/using_anaconda.md) within a `conda` environment named `pytools-env`. Prior to running the script, load the `Anaconda3` module and activate the `pytools-env` environment (line 13 and 14). Once job is successfully completed, check the slurm output file for results. Additionally, a plot named `testing.png` will be generated.

```bash
$ ls

numpy_26127143.err  numpy_26127143.out  numpy.job  python_test.py  testing.png
```

```bash
$cat numpy_26127143.out

[ 0 10 20 30 40]
[-5.  -4.5 -4.  -3.5 -3.  -2.5 -2.  -1.5 -1.  -0.5  0.   0.5  1.   1.5
  1.   2.5  3.   3.5  4.   4.5]
[ 0.   0.5  1.   1.5  2.   2.5  3.   3.5  4.   4.5  5.   5.5  6.   6.5
  1.   7.5  8.   8.5  9.   9.5 10.  10.5 11.  11.5 12.  12.5 13.  13.5
 1.   14.5 15.  15.5 16.  16.5 17.  17.5 18.  18.5 19.  19.5 20. ]
(2.0, 2.220446049250313e-14)
```

You can review detailed information about finished jobs using `sacct` command for a specific job id as shown below. For instance, this job was allocated with one CPU and has been successfully completed. The lines with ".ba+" and ".ex+" refer to batch step and external step within a job, but we will ignore them for simplicity in this and future examples. The exit code `0:0` signifies a normal exit with no errors.

```bash
$ sacct -j 26127143

       JobID    JobName  Partition    Account  AllocCPUS      State ExitCode
------------ ---------- ---------- ---------- ---------- ---------- --------
26127143          numpy    express      USER          1  COMPLETED      0:0
26127143.ba+      batch                 USER          1  COMPLETED      0:0
26127143.ex+     extern                 USER          1  COMPLETED      0:0
```

### Example 3: Parallel Jobs

Multiple jobs or tasks can be executed simultaneously using `srun` within a single batch script. In this example, the same executable `python_script_new.py` is run in parallel with distinct inputs (line 17-19). The `&` symbol at the end of each line run these commands in background. The `wait` command (line 20) performs synchronization and ensures that all background processes and parallel tasks are completed before finishing. In Line 4, three tasks are requested as there are three executables to be run in parallel. The overall job script is allocated with three CPUs, and in lines(17-19), each `srun` script utilizes 1 CPU to perform their respective task. Copy the batch script into a file named `multijob.job`. Use the same `conda` environment `pytools-env` shown in [example2](../slurm/slurm_tutorial.md#example-2-sequential-job).

```bash linenums="1"
#!/bin/bash
#SBATCH --job-name=multijob             ### Name of the job
#SBATCH --nodes=1                       ### Number of Nodes
#SBATCH --ntasks=3                      ### Number of Tasks
#SBATCH --cpus-per-task=1               ### Number of Tasks per CPU
#SBATCH --mem=4G                        ### Memory required, 4 gigabyte
#SBATCH --partition=express             ### Cheaha Partition
#SBATCH --time=01:00:00                 ### Estimated Time of Completion, 1 hour
#SBATCH --output=%x_%j.out              ### Slurm Output file, %x is job name, %j is job id
#SBATCH --error=%x_%j.err               ### Slurm Error file, %x is job name, %j is job id

### Loading Anaconda3 module to activate `pytools-env` conda environment
module load Anaconda3
conda activate pytools-env

### Runs the script `python_test.py` in parallel with distinct inputs and ensures synchronization
srun --nodes=1 --ntasks=1 python python_script_new.py 1 100000 &
srun --nodes=1 --ntasks=1 python python_script_new.py 100001 200000 &
srun --nodes=1 --ntasks=1 python python_script_new.py 200001 300000 &
wait
```

Copy the following python script and call it as `python_script_new.py`. The input file takes two command-line arguments i.e. the `start` and `end` values. The script uses these values to creates an array and compute the sum of its elements using numpy. The above batch script runs three parallel instances of this Python script with different inputs.

```bash linenums="1"
import sys
import numpy as np

### Verify if correct number of command-line arguments is provided
if len(sys.argv) != 3:
  print("Usage: python python_script_new.py <start> <end>")
  sys.exit(1)

### Passing start and end values from command-line arguments
start = int(sys.argv[1])
end = int(sys.argv[2])

### Create an array from start to end using numpy
input_array = np.arange(start, end)

### Perform addition on the array elements using numpy's sum function
sum_result = np.sum(input_array)

### Print Input Range and Sum
print("Input Range: {} to {}, Sum: {}".format(start, end, sum_result))
```

The below output shows that each line corresponds to the output of one parallel execution of python script with specific input ranges. Note that the results are in out of order. This is because each `srun` script runs independently, and their completion times may vary based on factors such as system load, resource availability, and the nature of their computations. If the results must be in order to be correct, you will need to modify your script to explicitly collect and organize them. One possible approach can be found in the section [srun for running parallel jobs](../slurm/submitting_jobs.md#srun-for-running-parallel-jobs) (refer to example 2).

```bash
$cat multijob_27099591.out

Input Range: 1 to 100000, Sum: 4999950000
Input Range: 200001 to 300000, Sum: 24999750000
Input Range: 100001 to 200000, Sum: 14999850000
```

The `sacct` report indicates that three CPUs have been allocated. The python script executes with unique task IDs 27099591.0,27099591.1,27099591.2.

```bash
$ sacct -j 27099591

       JobID    JobName  Partition    Account  AllocCPUS      State ExitCode
------------ ---------- ---------- ---------- ---------- ---------- --------
27099591       multijob    express      USER          3  COMPLETED      0:0
27099591.ba+      batch                 USER          3  COMPLETED      0:0
27099591.ex+     extern                 USER          3  COMPLETED      0:0
27099591.0       python                 USER          1  COMPLETED      0:0
27099591.1       python                 USER          1  COMPLETED      0:0
27099591.2       python                 USER          1  COMPLETED      0:0
```

### Example 4: Array Job

Array jobs are more effective when you have a larger number of similar tasks to be executed simultaneously with varied input data, unlike `srun` parallel jobs which are suitable for running a smaller number of tasks concurrently (e.g. less than 5). Array jobs are easier to manage and monitor multiple tasks through unique identifiers.

The following Slurm script is an example of how you might convert the previous `multijob` script to an array job. To start, copy the below script to a file named, `slurm_array.job`. The script requires the input file `python_script_new.py` and the `conda` environment `pytools-env`, similar to those used in [example2](../slurm/slurm_tutorial.md#example-2-sequential-job) and [example 3](../slurm/slurm_tutorial.md#example-3-parallel-jobs). Line 11 specifies the script as an array job, treating each task within the array as an independent job. For each task, lines 18-19 calculates the input range. `SLURM_ARRAY_TASK_ID` identifies the task executed using indexes, and is automatically set for array jobs. The python script (line 22) runs individual array task concurrently on respective input range. The command `awk` is used to prepend each output line with the unique task identifier and then append the results to the file, `output_all_tasks.txt`. For more details on on parameters of array jobs, please refer to [Batch Array Jobs](../slurm/submitting_jobs.md#batch-array-jobs-with-known-indices) and [Practical Batch Array Jobs](../slurm/practical_sbatch.md#).

<!-- markdownlint-disable MD046 -->
!!! important

    For large array jobs, implementing [throttling](./submitting_jobs.md#throttling-in-slurm-array-jobs) helps control the number of concurrent jobs, preventing resource contention across the Cheaha cluster. Running too many jobs at once can cause competition for CPU, memory, or I/O, which may negatively impact performance.
<!-- markdownlint-enable MD046 -->

```bash linenums="1"
#!/bin/bash
#SBATCH --job-name=slurm_array       ### Name of the job
#SBATCH --nodes=1                    ### Number of Nodes
#SBATCH --ntasks=1                   ### Number of Tasks
#SBATCH --cpus-per-task=1            ### Number of Tasks per CPU
#SBATCH --mem=4G                     ### Memory required, 4 gigabyte
#SBATCH --partition=express          ### Cheaha Partition
#SBATCH --time=01:00:00              ### Estimated Time of Completion, 1 hour
#SBATCH --output=%x_%A_%a.out        ### Slurm Output file, %x is job name, %A is array job id, %a is array job index
#SBATCH --error=%x_%A_%a.err         ### Slurm Error file, %x is job name, %A is array job id, %a is array job index
#SBATCH --array=1-3                  ### Number of Slurm array tasks, 3 tasks

### Loading Anaconda3 module to activate `pytools-env` conda environment
module load Anaconda3
conda activate pytools-env

### Calculate the input range for each task
start=$((($SLURM_ARRAY_TASK_ID - 1) * 100000 + 1))
end=$(($SLURM_ARRAY_TASK_ID * 100000))

### Run the python script with input arguments and append the results to a .txt file for each task
python python_script_new.py $start $end 2>&1 | awk -v task_id=$SLURM_ARRAY_TASK_ID '{print "array task " task_id, $0}' >> output_all_tasks.txt
```

The output shows the sum of different input range computed by individual task, making it easy to track using a task identifier, such as array task 1/2/3.

```bash
$ cat output_all_tasks.txt

array task 2 Input Range: 100001 to 200000, Sum: 14999850000
array task 3 Input Range: 200001 to 300000, Sum: 24999750000
array task 1 Input Range: 1 to 100000, Sum: 4999950000
```

The `sacct` report indicates that the job `27101430` consists of three individual tasks, namely `27101430_1`, `27101430_2`, and `27101430_3`. Each task has been allocated one CPU resource.

```bash
$ sacct -j 27101430

       JobID    JobName  Partition    Account  AllocCPUS      State ExitCode
------------ ---------- ---------- ---------- ---------- ---------- --------
27101430_3   slurm_arr+    express      USER          1  COMPLETED      0:0
27101430_3.+      batch                 USER          1  COMPLETED      0:0
27101430_3.+     extern                 USER          1  COMPLETED      0:0
27101430_1   slurm_arr+    express      USER          1  COMPLETED      0:0
27101430_1.+      batch                 USER          1  COMPLETED      0:0
27101430_1.+     extern                 USER          1  COMPLETED      0:0
27101430_2   slurm_arr+    express      USER          1  COMPLETED      0:0
27101430_2.+      batch                 USER          1  COMPLETED      0:0
27101430_2.+     extern                 USER          1  COMPLETED      0:0
```

### Example 5: Multithreaded or Multicore Job

This Slurm script illustrates execution of a MATLAB script in a multithread/multicore environemnt. Save the script as `multithread.job`. The `%` symbol in this script denotes comments within MATLAB code. Line 16 runs the MATLAB script `parfor_sum_array`, with an input array size `100` passed as argument, using 4 CPU cores (as specified in Line 5).

```bash linenums="1"
#!/bin/bash
#SBATCH --job-name=multithread          ### Name of the job
#SBATCH --nodes=1                       ### Number of Nodes
#SBATCH --ntasks=1                      ### Number of Tasks
#SBATCH --cpus-per-task=4               ### Number of Tasks per CPU
#SBATCH --mem=16G                       ### Memory required, 16 gigabyte
#SBATCH --partition=express             ### Cheaha Partition
#SBATCH --time=01:00:00                 ### Estimated Time of Completion, 1 hour
#SBATCH --output=%x_%j.out              ### Slurm Output file, %x is job name, %j is job id
#SBATCH --error=%x_%j.err               ### Slurm Error file, %x is job name, %j is job id

### Loading required MATLAB module
module load rc/matlab/R2023b

### Executing the matlab script with input arguments
matlab -nosplash -nodesktop -r "parfor_sum_array(100); quit;"
```

Copy the below MATLAB script as `parfor_sum_array.m`. At the beginning, the script defines a function `sum_array` and variable `array_size` is passed as an input argument. This function uses multithreading with the `parfor` option to calculate the sum of elements in an array. On Line 10, the number of workers (`num_workers`) is set to the value of the environment variable `SLURM_CPUS_PER_TASK` i.e. 4. The script then creates a parallel pool using lines 13-17, utilizing the specified number of workers. The parallel computation of summing up of array elements is performed using a `parfor` loop in lines 23-27. By using `parfor` with a pool of workers, operations are run in parallel for improved performance. More insights on usage of `parfor` can be found in the official [MATLAB page](https://www.mathworks.com/help/matlab/ref/parfor.html).

<!-- markdownlint-disable MD046 -->
!!! important

    Make sure that the `SLURM_CPUS_PER_TASK > 1` in order to take advantage of multithreaded performance. It is important that the  `SLURM_CPUS_PER_TASK` does not exceed the number of workers and physical cores (i.e. CPU cores) available on the node. This is to prevent high context switching, where individual CPUs are constantly switching between multiple running processes, which can negatively impact job performance of all jobs running on the node. It may also lead to overhead during job execution and result in poorer performance. Please refer to our [Hardware page](../hardware.md#hardware-information) to learn more about resource limits and selecting appropriate resources.
<!-- markdownlint-disable MD046 -->

<!-- markdownlint-disable MD046 -->
!!! bug

    There is a known issue with `parpool` and other related multi-core parallel features such as `parfor` affecting R2022a and earlier. See our [Modules Known Issues section](../software/modules.md#matlab-issues) for more information.
<!-- markdownlint-enable MD046 -->

```bash linenums="1"
% Function to calculate the sum of an array in parallel. This function takes array_size as input from command-line arguments
function sum_array(array_size)
    % Check if input array size is provided
    if nargin < 1
        disp('error: pass input array size as arguments');
        return;
    end

    % The number of workers is set based on Slurm parameter i.e. number of CPUS per task
    num_workers = str2double(getenv('SLURM_CPUS_PER_TASK'));

    % Create parallel pool
    poolobj = gcp('nocreate');
    if isempty(poolobj) || poolobj.NumWorkers ~= num_workers
        delete(poolobj);
        parpool(num_workers);
    end

    % Initialization of Array
    A = zeros(1, array_size);

    % Perform parallel computation for each element of the array
    sum_result = 0;
    parfor i = 1:array_size
        A(i) = i;
        sum_result = sum_result + A(i);
    end

    % Display the total sum
    disp(['Sum of array is: ' num2str(sum_result)]);
end
```

The below result summarizes the parallel pool initialization and its utilization of 4 workers for  computation of sum of an array. Followed by, the `sacct` report illustrates that the multithreaded job was allocated with 4 CPUs and was successfully completed.

```bash
$ cat multithread_27105035.out

MATLAB is selecting SOFTWARE OPENGL rendering.

                            < M A T L A B (R) >
                  Copyright 1984-2023 The MathWorks, Inc.
             R2023b Update 6 (23.2.0.2485118) 64-bit (glnxa64)
                             December 28, 2023

To get started, type doc.
For product information, visit www.mathworks.com.

Starting parallel pool (parpool) using the 'Processes' profile ...
Connected to parallel pool with 4 workers.
Sum of array is: 5050
Parallel pool using the 'Processes' profile is shutting down.
```

```bash
$ sacct -j 27105035

       JobID    JobName  Partition    Account  AllocCPUS      State ExitCode
------------ ---------- ---------- ---------- ---------- ---------- --------
27105035     multithre+    express      USER          4  COMPLETED      0:0
27105035.ba+      batch                 USER          4  COMPLETED      0:0
27105035.ex+     extern                 USER          4  COMPLETED      0:0
```

### Example 6: GPU Jobs

GPUs are a resource for speeding up computation in many scientific domains, so understanding how to use them effectively is important for accelerating scientific discovery. Always make sure you know your software's capabilities. Not all software can take advantage of GPUs, or multiple GPUs. Even if it can, be sure you understand what information or parameters you will need to supply to your software.

In this section there are two tutorials that show how to use (a) a single GPU, and (b) multiple GPUs. Before we get started with the specifics, we need a working directory and software to work with. Our software will be a short script performing some low-level tensor operations with Tensorflow. It is programmed to take advantage of multiple GPUs automatically, to put the focus on the job scripts and the GPUs, rather than on the software used.

<!-- markdownlint-disable MD046 -->
!!! note

    For real applications, especially AI and other large-data applications, we recommend pre-loading data onto [Local Scratch](../../data_management/cheaha_storage_gpfs/index.md#local-scratch) to [ensure good performance](../slurm/gpu.md#ensuring-io-performance-with-a100-gpus). Don't worry about doing this for the current tutorial, but do make a note of it for your own scientific work. The difference in performance is huge, especially for AI and large-data applications.
<!-- markdownlint-enable MD046 -->

#### Initial Setup

Let's create a working directory using [shell commands](../../workflow_solutions/shell.md).

```bash
mkdir -p ~/slurm_tutorials/example_6
```

Navigate to the working directory to prepare for following steps. All of the following steps will take place in this directory.

```bash
cd ~/slurm_tutorials/example_6
```

Let us create a file named `matmul_tensorflow.py` and copy the script below into it to prepare for the tutorials. You are welcome to use your favorite text editor. On Cheaha, there are two built-in options, just before the script below.

- At any terminal on Cheaha, use [nano]. Type [`nano matmul_tensorflow.py` at the terminal](../../workflow_solutions/shell.md#edit-plain-text-files-nano) to create and start editing the file.
- In an HPC Desktop job terminal, type `gedit matmul_tensorflow.py` to create the file and open a graphical editor.

Below is the script to copy into the new file.

```bash linenums="1"
import tensorflow as tf

### Print Tensorflow version and check for available number of GPUs
print("TensorFlow version:", tf.__version__)
print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))

### Get the logical GPUs and enable device placement
gpus = tf.config.list_logical_devices('GPU')
tf.debugging.set_log_device_placement(True)

if gpus:
    ### Create tensors on each GPU and Perform matrix multiplication on multiple GPUs
    c = []
    for gpu in gpus:
        with tf.device(gpu.name):
            a = tf.random.uniform(shape=(4, 3))
            b = tf.random.uniform(shape=(3, 4))
            c.append(tf.matmul(a, b))
            print(f"Computation on GPU: {gpu.name}")

    ### Calculate the Sum on CPU device
    with tf.device('/CPU:0'):
        matmul_sum = tf.add_n(c)

    ### Print the result
    print(matmul_sum)
```

We will also need to set up a [Conda environment](../software/software.md#anaconda-on-cheaha) suitable for executing this Tensorflow-based code. Please do not try to install Pip packages outside of a Conda environment, as it can result in [hard-to-diagnose errors](../../workflow_solutions/using_anaconda.md#). Copy the following into a file `environment.yml`.

```yaml
name: tensorflow
dependencies:
  - conda-forge::pip==25.0.1
  - conda-forge::python==3.11.0
  - pip:
    - tensorflow==2.15.0
```

To create the environment, run the following commands. This is a one-time setup for this tutorial. Please see our [Module page](../software/modules.md) and our [Conda page](../software/software.md#anaconda-on-cheaha) for more information about each.

```bash
module load Anaconda3
conda env create --file environment.yml
```

Each time you start a new session and want to use the environment, you'll need to use the following command to activate it. This should be done before moving on to the two GPU tutorials below.

```bash
module load Anaconda3   # unless it is already loaded in this session
conda activate tensorflow
```

#### Example 6a: Single GPU Job

The following slurm script can be used to run our script with a single GPU. The Slurm parameter `--gres=gpu:1` in line 6 requests the GPU. In line 8, note that in order to run GPU-based jobs, either the `amperenodes` or `pascalnodes` partition must be used (please refer to our [GPU page](../slurm/gpu.md) for more information). Lines 14-15 load the necessary modules, while lines 18-19 load the Anaconda module and activate a Conda environment called `tensorflow`.The last line executes the python script from the introduction.

As before, copy this script to a new file `gpu-single.job`.

```bash linenums="1"
#!/bin/bash
#SBATCH --job-name=gpu              ### Name of the job
#SBATCH --nodes=1                   ### Number of Nodes
#SBATCH --ntasks=1                  ### Number of Tasks
#SBATCH --cpus-per-task=1           ### Number of Tasks per CPU
#SBATCH --gres=gpu:1                ### Number of GPUs
#SBATCH --mem=16G                   ### Memory required, 16 gigabyte
#SBATCH --partition=amperenodes     ### Cheaha Partition
#SBATCH --time=01:00:00             ### Requested Time, 1 hour

# Slurm Output and Error files, %x is job name, %j is job id
#SBATCH --output=%x_%j.out
#SBATCH --error=%x_%j.err

### Loading the required CUDA and cuDNN modules
module load CUDA/12.2.0
module load cuDNN/8.9.2.26-CUDA-12.2.0

### Loading the Anaconda module and activating the `tensorflow` environment
module load Anaconda3
conda activate tensorflow

### Executing the python script
python matmul_tensorflow.py
```

To submit the job, use the following command from within your working directory.

```bash
sbatch gpu-single.job
```

When the job has completed, check the results using `cat` to read the Slurm output log. The results indicate that the Tensorflow version used is 2.15. The segment `/device:GPU:0` specifies which GPU the computation was executed on. The final result is a 4x4 matrix obtained by summing the matrix multiplication results. Note that the name of your output file will have a different job ID number.

```bash
$ cat gpu_27107693.out

TensorFlow version: 2.15.0
Num GPUs Available:  1
Computation on GPU: /device:GPU:0
tf.Tensor(
[[0.7417870 0.436646  0.0565315 0.5258054]
 [0.7313270 0.8445346 0.885784  0.0902905]
 [1.176963  0.9857005 1.9687731 0.6279962]
 [1.2957641 0.9410924 0.4280013 0.2470699]], shape=(4, 4), dtype=float32)
```

#### Example 6b: Multiple GPU Job

Using multiple GPUs is very similar to the single GPU job, with a couple of small, but important, changes. You must also be sure that your software is able to take advantage of multiple GPUs. Some software is designed for single-GPU usage only and, in that case, requesting more GPUs wastes resources. In this tutorial we've already designed our software to take advantage of multiple GPUs automatically.

First, we need to request two GPUs with `--gres=gpu:2`. We also need to instruct Slurm how to use CPU cores that are assigned to each GPU with `--ntasks-per-socket=1`. We also need to instruct Slurm we have two tasks, one for each socket, by using `--ntasks=2` instead of `1`. Much more detail is available at our [Using Multiple GPUs](../slurm/gpu.md#using-multiple-gpus) section.

All of the other parts of our script can remain the same, because we programmed it with multiple GPU use in mind.. That may not be the case for all software, so be sure to check its documentation.

Let us save this script as `gpu-multiple.job`.

```bash linenums="1"
#!/bin/bash
#SBATCH --job-name=gpu            ###       Name of the job
#SBATCH --nodes=1                 ###       Number of Nodes
#SBATCH --ntasks=2                ### DIFF  Number of Tasks, one for each socket
#SBATCH --ntasks-per-socket       ### NEW   Number of Tasks per Socket
#SBATCH --cpus-per-task=1         ###       Number of Tasks per CPU
#SBATCH --gres=gpu:2              ### DIFF  Number of GPUs, 2 GPUs
#SBATCH --mem=16G                 ###       Memory required, 16 gigabyte
#SBATCH --partition=amperenodes   ###       Cheaha Partition
#SBATCH --time=01:00:00           ###       Requested Time, 1 hour

# Slurm Output and Error files, %x is job name, %j is job id
#SBATCH --output=%x_%j.out
#SBATCH --error=%x_%j.err

### Loading the required CUDA and cuDNN modules
module load CUDA/12.2.0
module load cuDNN/8.9.2.26-CUDA-12.2.0

### Loading the Anaconda module and activating the `tensorflow` environment
module load Anaconda3
conda activate tensorflow

### Executing the python script
python matmul_tensorflow.py
```

We will use the same `matmul_tensorflow.py`, since we programmed it to take advantage of multiple GPUs. To submit the job, use the following command.

```bash
sbatch gpu-multiple.job
```

As before, the results indicate that the Tensorflow version used is 2.15. The segments `/device:GPU:0` and `/device:GPU:1` specify that the computations were executed on two GPUs. The final results is a 4x4 matrix obtained by summing the matrix multiplication results. In the `sacct` report, the column `AllocGRES` shows that 2 GPUs are allocated for this job.

```bash
$ cat gpu_27107694.out

TensorFlow version: 2.15.0
Num GPUs Available:  2
Computation on GPU: /device:GPU:0
Computation on GPU: /device:GPU:1
tf.Tensor(
[[1.6408134 0.9900811 1.3046092 0.9307438]
 [1.5603762 1.6812123 1.8867838 1.0662912]
 [2.481688  1.8107605 2.0444224 1.5500932]
 [2.415476  1.9280369 2.020216  1.4872619]], shape=(4, 4), dtype=float32)
```

```bash
$ sacct -j 27107694 --format=JobID,JobName,Partition,Account,AllocCPUS,allocgres,State,ExitCode

       JobID    JobName  Partition    Account  AllocCPUS    AllocGRES      State ExitCode
------------ ---------- ---------- ---------- ---------- ------------ ---------- --------
27107694            gpu amperenod+      USER          1        gpu:2  COMPLETED      0:0
27107694.ba+      batch                 USER          1        gpu:2  COMPLETED      0:0
27107694.ex+     extern                 USER          1        gpu:2  COMPLETED      0:0
```

### Example 7: Multinode Job

The below Slurm script runs a Quantum Expresso job using the `pw.x` executable on multiple nodes. In this example, we request for 2 nodes on `amd-hdr100` partition in lines 4 and 7. The suitable Quantum Expresso module is loaded in line 13. The last line is configured for a parallel computation of Quantum Expresso simulation across 2 nodes `N 2` and 4 MPI processes `-nk 4` for the input parameters in `pw.scf.silicon.in`. The input file `pw.scf.silicon.in` and psuedo potential file is taken from the [github page](https://pranabdas.github.io/espresso/hands-on/scf/). However this input is subject to change, hence according to your use case you can change the inputs.

```bash linenums="1"
#!/bin/bash

#SBATCH --job-name=mpijob               ### Name of the job
#SBATCH --nodes=2                       ### Number of Nodes
#SBATCH --ntasks 4                      ### Number of Tasks
#SBATCH --mem=64G                       ### Memory required, 64 gigabyte
#SBATCH --partition=amd-hdr100          ### Cheaha Partition
#SBATCH --time=12:00:00                 ### Estimated Time of Completion, 12 hour
#SBATCH --output=%x_%j.out              ### Slurm Output file, %x is job name, %j is job id
#SBATCH --error=%x_%j.err               ### Slurm Error file, %x is job name, %j is job id

### Load the suitable Quantum Expresso module
module load QuantumESPRESSO/6.3-foss-2018b

### Executes the executable "pw.x" across 2 nodes and 4 processes/CPU cores for the input `pw.scf.silicon.in`
srun --mpi=pmix_v3 -N 2 pw.x -nk 4 -i pw.scf.silicon.in
```

The below output shows that the workflow has been distributed across 2 nodes, with a total of 4 pools. The computations are performed based on these above-mentioned parallel execution configuration. Also, displays the metrics such as parallelization, overall performance, and successful job completion status. Note that the results only display essential information to aid in understanding the execution of this multi-node job. And, the `sacct` report indicates that the job is allocated with 4 CPUs across 2 nodes, and was completed successfully.

```bash
$ cat multinode_27108398.out

Program PWSCF v.6.3MaX starts on  8Mar2024 at 13:18:37

     This program is part of the open-source Quantum ESPRESSO suite
     for quantum simulation of materials; please cite
         "P. Giannozzi et al., J. Phys.:Condens. Matter 21 395502 (2009);
         "P. Giannozzi et al., J. Phys.:Condens. Matter 29 465901 (2017);
          URL http://www.quantum-espresso.org",
     in publications or presentations arising from this work. More details at
     http://www.quantum-espresso.org/quote

     Parallel version (MPI & OpenMP), running on       4 processor cores
     Number of MPI processes:                 4
     Threads/MPI process:                     1

     MPI processes distributed on     2 nodes
     K-points division:     npool     =       4
     Reading input from pw.scf.silicon.in

     Current dimensions of program PWSCF are:
     Max number of different atomic species (ntypx) = 10
     Max number of k-points (npk) =  40000
     Max angular momentum in pseudopotentials (lmaxx) =  3
     .....
     .....
          Parallel routines

     PWSCF        :     1.17s CPU         1.36s WALL

   This run was terminated on:  13:18:38   8Mar2024
=------------------------------------------------------------------------------=
   JOB DONE.
=------------------------------------------------------------------------------=
```

```bash
$ sacct -j 27108398 --format=JobID,JobName,Partition,Account,AllocCPUS,AllocNodes,State,ExitCode

       JobID    JobName  Partition    Account  AllocCPUS AllocNodes      State ExitCode
------------ ---------- ---------- ---------- ---------- ---------- ---------- --------
27108398      multinode amd-hdr100      USER          4          2  COMPLETED      0:0
27108398.ba+      batch                 USER          3          1  COMPLETED      0:0
27108398.ex+     extern                 USER          4          2  COMPLETED      0:0
27108398.0         pw.x                 USER          4          2  COMPLETED      0:0
```
