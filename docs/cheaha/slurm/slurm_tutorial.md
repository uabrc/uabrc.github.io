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

```bash
# File name `hostname.sh`
#!/bin/bash

# Declaring Slurm configuration Options and specifying required resources
#SBATCH --job-name=hostname # Name of the job
# Requesting Required Resources
#SBATCH --nodes=1 # Number of Nodes
#SBATCH --ntasks=1 # Number of Tasks
#SBATCH --cpus-per-task=1 # Number of Tasks per CPU
#SBATCH --mem=1G # Memory required
#SBATCH --partition=express # Cheaha Partition
#SBATCH --time=00:10:00 # Estimated Time of Completion
#SBATCH --output=%x_%j.out # Slurm Output file
#SBATCH --error=%x_%j.err # Slurm Error file

# Running Code
hostname # Run the command hostname
```

### Monitoring the Job

Submit the batch job using,

```bash
sbatch hostname.sh

Submitted batch job 26035322
```

Check status of job using,

```bash
squeue -u $USER

JOBID      PARTITION    NAME        USER    ST       TIME  NODES NODELIST(REASON)
26035322   express      hostname    USER    CG       0:01      1 c0156
```
