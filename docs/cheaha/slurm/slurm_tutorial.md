# Writing Slurm Batch Jobs

## Strucutre of a Slurm Batch Job

```bash
#!/bin/bash
# Declaring Slurm configuration Options and specifying required resources
...
# Loading Software/Libraries
...
# Running Code
...
```

## Example 1: A Simple Slurm Batch Job

Let us start with a simple example to print `hostname` of the node where your job is submitted.
To learn more about individual Slurm paramters, please refer to [Slurm Flag and Environment Variables](../slurm/submitting_jobs.md/#slurm-flags-and-environment-variables) and official [Slurm documenation](https://slurm.schedmd.com/).

```bash
### Job name "hostname.sh" ###
#!/bin/bash

### Declaring Slurm configuration Options and specifying required resources ###
#SBATCH --job-name=hostname ### Name of the job ###
#SBATCH --nodes=1           ### Number of Nodes ###
#SBATCH --ntasks=1          ### Number of Tasks ###
#SBATCH --cpus-per-task=1   ### Number of Tasks per CPU ###
#SBATCH --mem=1G            ### Memory required ###
#SBATCH --partition=express ### Cheaha Partition ###
#SBATCH --time=00:10:00     ### Estimated Time of Completion ###
#SBATCH --output=%x_%j.out  ### Slurm Output file ###
#SBATCH --error=%x_%j.err   ### Slurm Error file ###

# Running Code
hostname # Run the command `hostname`
```

### Submitting the Job

Submit the batch job using,

```bash
sbatch hostname.sh

Submitted batch job 26035322
```

After submitting the job, Slurm will create the output and error files as,

```bash
$ls
hostname_26035322.err  hostname_26035322.out  hostname.sh
```

### Monitoring the job

Check status of job using,

```bash
squeue -u $USER

JOBID      PARTITION    NAME        USER    ST       TIME  NODES NODELIST(REASON)
26035322   express      hostname    USER    CG       0:01      1 c0156
```

If the job is successful, the `hostname__26035322.err` file will be empty/without error statement. You can print the result using,

```bash
$cat hostname_26035322.out
c0156
```

## Example 2: Run Python Script

```bash
### Job name "numpy.sh" ###

#!/bin/bash
#SBATCH --job-name=numpy 
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=1G
#SBATCH --partition=express
#SBATCH --time=00:10:00
#SBATCH --output=%x_%j.out
#SBATCH --error=%x_%j.err

module load Anaconda3
conda activate pytools-env
python python_test.py
```

After submitting the job, Slurm will create the output and error files as,

```bash
$ls
numpy_26127143.err  numpy_26127143.out  numpy.sh  python_test.py  testing.png
```

The `python_test.py` script can be copied from the [Containers page](../../workflow_solutions/getting_containers/#create-your-own-docker-container) for testing.

You can now view the output via the terminal using,

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

### Example 3: Running Multiple Jobs in Parallel as a Single Batch Job

```bash
### python_script.py ###
import sys
import numpy as np

if len(sys.argv) != 3:
  print("Usage: python my_python_script.py <start> <end>")
  sys.exit(1)

input_start = int(sys.argv[1])
input_end = int(sys.argv[2])

# Create an array from input_start to input_end
input_array = np.arange(input_start, input_end)

# Perform addition on the array
sum = np.sum(input_array)

print(f"Input Range: {input_start} to {input_end}, Sum: {sum}")
```

Multiple jobs/tasks can be executed in parallel using `srun` in a single batch script. Here is an example that show case its benefits.

```bash
#!/bin/bash
#SBATCH --job-name=multijob
#SBATCH --nodes=1
#SBATCH --ntasks=3
#SBATCH --cpus-per-task=1
#SBATCH --mem=1G
#SBATCH --partition=express
#SBATCH --time=00:10:00
#SBATCH --output=%x_%j.out
#SBATCH --error=%x_%j.err

module load Anaconda3
conda activate pytools-env

srun --ntasks=1 python python_script.py 1 100000 &
srun --ntasks=1 python python_script.py 200000 300000 &
srun --ntasks=1 python python_script.py 300000 400000 &
wait
```

The output is printed as below,

```bash
Input Range: 1 to 100000, Sum: 4999950000
Input Range: 300000 to 400000, Sum: 34999950000
Input Range: 200000 to 300000, Sum: 24999950000
```