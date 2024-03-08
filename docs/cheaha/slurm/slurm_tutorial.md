# Writing Slurm Batch Jobs

This Slurm tutorial serves as a hands-on guide for users to create Slurm batch scripts based on their specific software needs and apply them for their respective usecases.  It covers basic examples for beginners and advanced ones, including sequential and parallel jobs, array jobs, multithreaded jobs, GPU utilization jobs, and MPI (Message Passing Interface) jobs.

## Strucutre of a Slurm Batch Job

Below is the template for a typical Slurm job submission in the Cheaha high-performance computing (HPC) system. The script begins with `#!/bin/bash`, indicating it is a bash script. The next step would be to declare Slurm configuration options, specifying the required resources for job execution. This section typically comprises parameters such as CPU count, partition, memory allocation, time limit, etc. Following the configuration, the script may include sections for loading necessary software or libraries required for the job.

```bash
#!/bin/bash
# Declaring Slurm configuration Options and specifying required resources
...
# Loading Software/Libraries
...
# Running Code
...
```

The last portion is running the actual code or software. Here, the computational task or program intended for execution is launched using specific commands and processes, which depends on the software used and overall computational workflow. For more detailed specification, refer to [Slurm job submission](../slurm/submitting_jobs.md). The following sections present practical examples for writing a Slurm batch script to specific use cases, and Prerequisites to start with the tutorial.

## Prerequisites

If you're new to using Unix/Linux commands and bash scripting, we suggest going through the software carpentry lesson, [The Unix Shell](https://swcarpentry.github.io/shell-novice/). Also, we recommend reviewing the [Cheaha Hardware Information](../../cheaha/hardware.md) to help guide you in chosing appropriate partition and resources.

## Example 1: A Simple Slurm Batch Job

Let us start with a simple example to print `hostname` of the node where your job is submitted. You will have to request for the required resources required to run your job using Slurm parameters. To learn more about individual Slurm paramters given in the example, please refer to [Slurm flag and environment variables](../slurm/submitting_jobs.md/#slurm-flags-and-environment-variables) and the official [Slurm documenation](https://slurm.schedmd.com/).

To test this example, copy the below script in a file named `hostname.job`. This job executes the `hostname` command (line 15) on a single node, using one task, one CPU core, 1 gigabyte of memory, with a time limit of 10 minutes. The output and error logs are directed to separate files with names based on their job name and ID (line 11 and 12). For a more detailed understanding of the individual parameters used in this script, please refer to the section on [Simple Batch Job](../slurm/submitting_jobs.md/#a-simple-batch-job). The following script includes comments, marked with `###`, describing their functions. We will utilize this same notating for annotating comments in subsequent examples.

```py linenums="1"
#!/bin/bash

### Declaring Slurm configuration Options and specifying required resources
#SBATCH --job-name=hostname ### Name of the job
#SBATCH --nodes=1           ### Number of Nodes
#SBATCH --ntasks=1          ### Number of Tasks
#SBATCH --cpus-per-task=1   ### Number of Tasks per CPU
#SBATCH --mem=1G            ### Memory required
#SBATCH --partition=express ### Cheaha Partition
#SBATCH --time=00:10:00     ### Estimated Time of Completion
#SBATCH --output=%x_%j.out  ### Slurm Output file
#SBATCH --error=%x_%j.err   ### Slurm Error file

### Running the command `hostname`
hostname
```

### Submitting and Monitoring the Job

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

The above output provides a snapshot of the job's status, resource usage,  indicating that it is currently running on one node (c0156). The term `CG` refers to completing its execution. For more details refer to [Managing Slurm jobs](../slurm/job_management.md). If the job is successful, the `hostname__26035322.err` file will be empty/without error statement. You can print the result using,

```bash
$ cat hostname_26035322.out
c0156
```

## Example 2: Sequential Job

This example illustrate a Slurm job that runs a Python script involving [NumPy](https://numpy.org/) operation. This python script is executed sequentially using the same resource configuration as [Example 1](../slurm/slurm_tutorial.md/#example-1-a-simple-slurm-batch-job). Let us name the below script as `numpy.job`.

```py linenums="1"
#!/bin/bash
#SBATCH --job-name=numpy 
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=1G
#SBATCH --partition=express
#SBATCH --time=01:00:00
#SBATCH --output=%x_%j.out
#SBATCH --error=%x_%j.err

### Loading Anaconda3 module to activate `pytools-env` conda environment
module load Anaconda3
conda activate pytools-env

### Run the script `python_test.py`
python python_test.py
```

 The batch job requires an input file `python_test.py` (line 17) for execution. Copy the input file from the [Containers page](../../workflow_solutions/getting_containers.md/#create-your-own-docker-container). Place this file in the same folder as the `numpy.job`. This python script performs numerical integration and data visualization tasks, and it relies on the following packages: numpy, matplotlib, scipy for successful execution. These dependencies can be installed using [Anaconda](../../workflow_solutions/using_anaconda.md) within a `conda` environment named `pytools-env`. Prior to running the script, load the `Anaconda3` module and activate the `pytools-env` environment (line 13 and 14).  Once job is successfully completed, check the slurm output file for results. Additionally, a plot named `testing.png` will be generated.

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

## Example 3: Parallel Jobs

Multiple jobs or tasks can be executed simultaneously using `srun` within a single batch script. In this example, the same executable `python_script_new.py` is run in parallel with distinct inputs (line 17-19). The `&` symbol at the end of each line run these commands in background. The `wait` command (line 20) performs synchronization and ensures that all background processes and parallel tasks are completed before finishing. In Line 4, three tasks are requested as there are three executables to be run in parallel. Copy the batch script into a file named `multijob.job`. Use the `conda` environemnt `pytools-env`, as shown in [example2](../slurm/slurm_tutorial.md/#example-2-sequential-job).

```py linenums="1"
#!/bin/bash
#SBATCH --job-name=multijob
#SBATCH --nodes=1
#SBATCH --ntasks=3
#SBATCH --cpus-per-task=1
#SBATCH --mem=1G
#SBATCH --partition=express
#SBATCH --time=01:00:00
#SBATCH --output=%x_%j.out
#SBATCH --error=%x_%j.err

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

```py linenums="1"
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

### Perform addition on the array elemnts using numpy's sum function
sum_result = np.sum(input_array)

### Print Input Range and Sum
print("Input Range: {} to {}, Sum: {}".format(start, end, sum_result))
```

The below ouptut shows that each line corresponds to the output of one parallel execution of python script with specific input ranges.

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

## Example 4: Array Job

Array jobs are more effective when you have a larger number of similar tasks to be executed simultaneously with varied input data, unlike `srun` parallel jobs which are suitable for running a smaller number of tasks concurrently (e.g. less than 5). Array jobs are easier to manage and monitor multiple tasks through unique identifiers.

The following Slurm script is an example of how you might convert the previous `multijob` script to an array job. To start, copy the below script to a file named, `slurm_array.job`. The script requires the input file `python_script_new.py` and the `conda` environment `pytools-env`, similar to those used in [example 3](../slurm/slurm_tutorial.md/#example-3-parallel-jobs). Line 11 specifies the script as an array job, treating each task within the array as an independent job. For each task, line 18-19 calculates the input range. `SLURM_ARRAY_TASK_ID` identifies the task executed using indexes, and is automatically set for array jobs. The python script (line 22) runs individual array task concurrently on respective input range. The command `awk` is used to prepend each output line with the unique task identifier and then append the results to the file, `output_all_tasks.txt`. For more details on on parameters of array jobs, please refer to [Batch Array Jobs](../slurm/submitting_jobs.md/#batch-array-jobs-with-known-indices) and [Practical Batch Array Jobs](../slurm/practical_sbatch.md/#).

```py linenums="1"
#!/bin/bash
#SBATCH --job-name=slurm_array
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=1G
#SBATCH --partition=express
#SBATCH --time=01:00:00
#SBATCH --output=%x_%A_%a.out
#SBATCH --error=%x_%A_%a.err
#SBATCH --array=1-3

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

## Example 5: Multithreaded/Multicore Job

This Slurm script illustrates execution of a MATLAB script in a multithread/multicore environemnt. Save the script as `multithread.job`. The `%` symbol in this script denotes comments within MATLAB code. Line 16 runs the MATLAB script `parfor_sum_array`, with an input array size `100` passed as argument, using 4 CPU cores (as specified in Line 5).

```py linenums="1"
#!/bin/bash
#SBATCH --job-name=multithread
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=16G
#SBATCH --partition=express
#SBATCH --time=01:00:00
#SBATCH --output=%x_%j.out
#SBATCH --error=%x_%j.err

### Loading required Matlab module
module load rc/matlab/R2023b

### Executing the matlab script with input arguments
matlab -nosplash -nodesktop -r "parfor_sum_array(100); quit;"
```

Copy the below MATLAB script as `parfor_sum_array.m`. At the beginning, the script defines a function `sum_array` and variable `array_size` is passed as an input argument. This function uses multithreading with the `parfor` option to calculate the sum of elements in an array. On Line 10, the number of workers (`num_workers`) is set to the value of the environment variable `SLURM_CPUS_PER_TASK` i.e. 4. The script then creates a parallel pool using lines 13-17, utilizing the specified number of workers. The parallel computation of summing up of array elements is performed using a `parfor` loop in lines 23-27. By using `parfor` with a pool of workers, operations are run in parallel for improved performance. More insights on usage of `parfor` can be found in the official [MATLAB page](https://www.mathworks.com/help/matlab/ref/parfor.html).

<!-- markdownlint-disable MD046 -->
!!! warning

    Make sure that the `SLURM_CPUS_PER_TASK > 1` in order to take advantage of multithreaded performance. It is important that the  `SLURM_CPUS_PER_TASK` does not exceed the number of workers and physical cores (i.e. CPU cores) available on the node. This is to prevent high context switching, where individual CPUs are constantly switching between multiple running processes, which can negatively impact job performance of all jobs running on the node. It may also lead to overhead during job execution and result in poorer performance. Please refer to our [Hardware page](../hardware.md/#hardware-information) to learn more about resource limits and selecting appropriate resources.
<!-- markdownlint-disable MD046 -->

```py linenums="1"
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

## Example 6: GPU Job

## Example 7: Multinode Job
