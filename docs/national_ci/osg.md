# The Open Science Grid (OSG)

The [Open Science Grid (OSG)](https://osg-htc.org) is a consortium of research collaborations, institutions, and national laboratories that share computing and data resources for distributed high-throughput computing (dHTC) in support of open science.

Open Science Pool (OSPool) is operated for all US-affiliated research projects and groups via [OSG Connect](https://www.osgconnect.net/) service.

To utilize the OSPool, the jobs should be run with a high-throughput computing approach (HTC). HTCondor compute scheduling software includes first-class support for submitting and managing large numbers of jobs via a single submit file or multi-step workflow.

## Computations Accelerated by the OSPool

A high throughput computing (HTC) job runs independent tasks on different cores. So problems that can be run as numerous independent jobs, and having requirements as mentioned below, can significantly take advantage of OSPool.

![!Osg requirement.](./images/osg_requirement.png)

You should be aware that,

(i) Jobs in OSPool are checkpointable.

(ii) You can work with the Multi-TB dataset on the OSPool if it can be split into pieces.

(iii) Jobs requiring larger number of cores/internode communication do not scale well on OSPool. For instance MPI jobs.

Some of the HTC-compatible work but are not limited to are,

1. Image analysis
2. Text-based analysis
3. Drug discovery analysis
4. Generates high-quality conformation ensembles
5. DNA read mapping and other bioinformatics pipeline
6. Monte Carlo simulation
7. hyper/parameter sweeps
8. Computational modeling and analysis of protein structures

### An OSPool Use Case

For instance, to get a glimpse of the OSPool use case, if you need to process 72 brain images of 168 patients, each image takes approximately 1 hour of computation time. In this scenario, the computations are independent across 168 patients.

Then 168 patients * 72 images = ~12000 tasks = ~12000 hours takes to complete the analysis.

So this computation can take in,

1. laptop (1 core) = ~1.5 years
2. 1 server (~40 cores) = ~2 weeks
3. 1 MPI job (400 cores) = ~1 day
4. A whole cluster (10000 cores) = ~1 hour

<!-- markdownlint-disable MD046 -->
!!! note
    To find out if your job is suitable for running on OSPool, you can contact the [OSG support team](https://portal.osg-htc.org/documentation/overview/references/contact-information/) for assistance.
<!-- markdownlint-disable MD046 -->

## Account Creation

You can sign up for an OSG User Account by navigating this [application link](https://portal.osg-htc.org/application), completing the form, and submitting it. The details about account setup, support service, training resources, submission of HTC workload, and tutorials are found in this [OSPool Documentation](https://portal.osg-htc.org/documentation/).

## HTCondor Hands-on Example

To start, login to your OSG access point.

Once logged in, create a new directory named `osg_example`.

```bash
$mkdir osg_example
```

### Example 1: A Simple HTCondor Job

As this is the first job, let us see the step-by-step illustration of submitting the HTCondor job to the OSG access point.

#### Step 1: Create a Job Executable and Test it Locally

Lets create a test script, `osg_hello.sh`,

```bash
#!/bin/bash
printf "Start time: "; date
printf "Hello OSPool from Job $1 running on `whoami`@`hostname`"
echo
sleep 20
echo "Job complete"
```

Make the above script executable using `chmod` and then execute the script locally with a "first argument". Note that in OSPool, we will automatically pass different arguments in the HTCondor submit file.

```bash
chmod +x hello_osg.sh
./hello_osg.sh 1
```

```bash
Start time: Wed Aug  2 18:37:57 CDT 2023
Hello OSPool from Job 1 running on username@ap20.uc.osg-htc.org
Job complete
```

<!-- markdownlint-disable MD046 -->
!!! important

    Testing the job outside of HTCondor is significant before you submit it to the OSPool.
<!-- markdownlint-enable MD046 -->

#### Step 2: Create a Submit File with the Executable Script

Now, create the HTCondor submit file `osg_example1.sub` to submit the job to OSPool.

```bash
# The executable `hello_osg.sh' is the main script that we created to perform task of a single job and arguments can be passed to the executable.
#  $(Process) will be a integer number for each job, starting with "0"
#  and increasing for the relevant number of jobs.
executable = hello_osg.sh
arguments = $(Process)

# We need to name the files that HTCondor should create to save the 
# terminal output (stdout), error (stderr) and log file created by our job. 
# The log file has the informations about a job start, end, transfer of data, 
# execution steps, and hold reason. $(Cluster) is the queue number assigned 
# by HTCondor once the job is submitted. This will help to create unique log,output, and # error files for multi-queue jobs
error = hello_osg_$(Cluster)_$(Process).error
output = hello_osg_$(Cluster)_$(Process).output
log = hello_osg_$(Cluster)_$(Process).log

# We need to request the resources that this job will need:
request_cpus = 1
request_memory = 1 MB
request_disk = 1 MB

# The last line of a submit file indicates how many jobs of the above
# script should be queued. We'll start with one job.
queue 1
```

The `$1` executable in `hello_osg.sh` will fetch the first argument's value from the above HTCondor submit file, i.e., will pass the variable `$(Process)`.

#### Step 3: Submit the HTCondor job to OSPool and Check its Status

Submit the job using `condor_submit` command,

```bash
$condor_submit osg_example1.sub
```

Check the status of currently running jobs in queue using,

```bash
$condor_q

-- Schedd: ap20.uc.osg-htc.org : <192.170.231.141:9618?... @ 08/03/23 08:04:44
OWNER      BATCH_NAME    SUBMITTED   DONE   RUN    IDLE  TOTAL JOB_IDS
username ID: 132858   8/3  08:04      _      _      1      1 132858.0

Total for query: 1 jobs; 0 completed, 0 removed, 1 idle, 0 running, 0 held, 0 suspended 
Total for username: 1 jobs; 0 completed, 0 removed, 1 idle, 0 running, 0 held, 0 suspended 
Total for all users: 11674 jobs; 0 completed, 0 removed, 2 idle, 8309 running, 3363 held, 0 suspended
```

<!-- markdownlint-disable MD046 -->
!!! note

    `IDLE` refers to a job that has not started yet, `RUN` refers to a job that is scheduled and currently running, and `DONE` refers to the job completion.
 <!-- markdownlint-disable MD046 -->

#### Step4: Validate the Output

Let us wait for the job to finish, and when the job card disappears, check for the output, log, and error files for further information or troubleshooting.

Read the output file `hello_osg.output` for the above example,

```bash
Start time: Thu Aug  3 09:06:03 EDT 2023
Hello OSPool from Job 0 running on nobody@scigrid6.physics.fsu.edu
Job complete
```

Once the job disappears in the queue, type in the command `ls -l` within the directory to view something like this,

```bash
[username@ap20 example1]$ ls -l
total 35
-rw-r--r-- 1 username osg    0 Aug  3 08:06 hello_osg_132858_0.error
-rw-r--r-- 1 username osg 2820 Aug  3 08:06 hello_osg_132858_0.log
-rw-r--r-- 1 username osg  121 Aug  3 08:06 hello_osg_132858_0.output
-rwxr-xr-x 1 username osg  140 Aug  3 07:25 hello_osg.sh
-rw-r--r-- 1 username osg  791 Aug  3 08:03 osg_example1.sub
```

You can view the output, log, and error files created with a unique cluster and process id.

### Job 2: Transferring Input and Output Files Through HTCondor and Concurrent Job Submission

We will now modify the `osg_example1.sub` submit file with the relevant input and output file details.

Create an executable script named `osg_transfer.sh` with the below code snippet,

```bash
#!/bin/bash
printf "Start time: "; date
printf "Job is running on node: "; hostname
printf "Contents of $1 is "; cat $1
cat $1 > output.txt
echo "Job complete"
```

Now, create a file named `input.txt` with the following content:

```bash
Hello OSG User !
```

You can name the new submit file as `osg_example2.sub`.

```bash
executable = hello_osg.sh

# We need the job to run the `hello_osg.sh` executable with input.txt file
# as an argument, and to transfer relevant input and output files to the OSPool
arguments = input.txt
transfer_input_files = input.txt
transfer_output_files = output.txt

# We redirect stderror, stdoutput, and log files to see the execution details
error = hello_osg_$(Cluster)_$(Process).error
output = hello_osg_$(Cluster)_$(Process).output
log = hello_osg_$(Cluster)_$(Process).log

# We need to request the resources that this job will need:
request_cpus = 1
request_memory = 1 MB
request_disk = 1 MB

# The last line of a submit file indicates HTCondor to run 3 instances of this job 
queue 3
```

You can run multiple instances of the above job in HTCondor using the script `queue n`. For instance, for the above example, `queue 3` refers to running three concurrent jobs.

```bash
$condor_submit osg_example2.sub 

Submitting job(s)...
3 job(s) submitted to cluster 134442.
```

```bash
$condor_q 134442

-- Schedd: ap20.uc.osg-htc.org : <192.170.231.141:9618?... @ 08/03/23 14:31:51
OWNER      BATCH_NAME    SUBMITTED   DONE   RUN    IDLE  TOTAL JOB_IDS
username ID: 134442   8/3  14:30      _      3      _      3 134442.0-2

Total for query: 3 jobs; 0 completed, 0 removed, 0 idle, 3 running, 0 held, 0 suspended 
Total for all users: 32855 jobs; 0 completed, 0 removed, 11823 idle, 17673 running, 3359 held, 0 suspended
```

After the job run, displaying content from one of the output files,

```bash
$cat hello_osg_134553_0.output

Start time: Thu Aug  3 17:19:19 EDT 2023
Job is running on node: iut2-c412.iu.edu
Contents of input.txt is Hello OSG User !
Job complete
```

Now you can run your own pipeline on OSPool using HTCondor!

<!--
Copy the `python_test.py` and py3-miniconda.sif to the new directory.

Lets create a test script, `python_script.sh` to execute the code `python_test.py` using the singularity image py3-miniconda.sif.

Contents of the `python_script.sh` file

```bash
#!/bin/bash
singularity run py3-miniconda.sif python python_test.py
```

Make the above script executable using and then execute the script locally,

```bash
chmod +x python_script.sh
```

```bash
$ ./python_script.sh

[ 0 10 20 30 40]
[-5.  -4.5 -4.  -3.5 -3.  -2.5 -2.  -1.5 -1.  -0.5  0.   0.5  1.   1.5
  2.   2.5  3.   3.5  4.   4.5]
[ 0.   0.5  1.   1.5  2.   2.5  3.   3.5  4.   4.5  5.   5.5  6.   6.5
  7.   7.5  8.   8.5  9.   9.5 10.  10.5 11.  11.5 12.  12.5 13.  13.5
 14.  14.5 15.  15.5 16.  16.5 17.  17.5 18.  18.5 19.  19.5 20. ]
```

Create an HTCondor submit file

Now, create a HTCondor submit file `htc_example1.sub` to submit job to OSG.

```bash
# Executable is the main program or script we created
executable = python_script.sh

# We need the job to run our executable with input file `python_test.py` as an argument, and to transfer the relevant input/output files to OSGPool.
arguments = python_test.py
transfer_input_files = python_test.py

# We need to name the files that HTCondor should create to save the terminal output, error, and log files. The log file has the informations about a job start, end, transfer of data, execution steps, and hold reason.
output = htc_example1.out
error = htc_example1.err
log = htc_example1.log

# Specify the path of the singularity image
+SingularityImage = "osdf:///ospool/ap20/data/username/old-protected/py3-miniconda.sif"

# We need to request resources that this job will need
request_cpus = 1
request_memory = 1MB
request_disk = 1MB

#This is the last line of a submit file indicates how many jobs of the above description should be queued. We will start with one job
queue 1
```

### Submit an HTCondor Job

```bash
condor_submit htc_example1.job
```
Lets wait for the job to finish and when the job card disappears, check for the output, log, and error file for further information or for troubleshooting.

Read the output file for the above example,

```bash
cat htc_example1.out
[ 0 10 20 30 40]
[-5.  -4.5 -4.  -3.5 -3.  -2.5 -2.  -1.5 -1.  -0.5  0.   0.5  1.   1.5
  2.   2.5  3.   3.5  4.   4.5]
[ 0.   0.5  1.   1.5  2.   2.5  3.   3.5  4.   4.5  5.   5.5  6.   6.5
  7.   7.5  8.   8.5  9.   9.5 10.  10.5 11.  11.5 12.  12.5 13.  13.5
 14.  14.5 15.  15.5 16.  16.5 17.  17.5 18.  18.5 19.  19.5 20. ]
(2.0, 2.220446049250313e-14)
```
--->
## Other Useful Commands to Submit and Analyze a HTCondor Job

You can watch the running job status using the below command which ouptut the status at two-second intervals:

```bash
condor_watch_q
```

Check the status of a particular job in queue,

```bash
condor_q job_id

```

Check the status of a job that is completed,

```bash
condor_history job_id
```

Remove a condor job from queue,

```bash
condor_rm job_id
```

To find out why jobs are idle or the state of the run,

```bash
condor_q -better-analyze job_id
```

List more detail condor_q output,

```bash
condor_q -nobatch cluster_id
```

Find out running jobs,

```bash
condor_q -nobatch -run
```

Determine all of the jobs that are on hold and get the hold reason,

```bash
condor_q -hold
```

Determine particular job that is on hold using,

```bash
condor_q -hold job_id
```

To see the complete hold reason use, where `af` is autoformat:

```bash
condor_q -hold -af HoldReason
```

View all details about a job,

```bash
condor_q -l job_id
```

View memory, cpu, and disk space and details using

```bash
condor_q -af RequestMemory RequestDisk MemoryUsage
```
<!--

## Guideline to run jobs on OSG

1. Reviewing the licensing policy of the software
2. Compiling software to run on OSG
3. Managing data for jobs
4. Chose the suitable workflow for your job
5. After testing the job, look for opportunities for scaling
6. See if automated workflow can be applied to your job run

## Test a first job : An alterntive example

### Prepare your software

### Manage your data

### Scaling up Jobs on OSPool

### Special use casess
-->
