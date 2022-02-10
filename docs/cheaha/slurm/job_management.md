# Managing Jobs

When jobs are submitted, users can monitor their status using Slurm commands. Additionally, users can get information about completed jobs regarding their CPU and memory usage during execution for planning future jobs. Both of these cases should be a regular part of using Cheaha for users.

In case jobs were submitted by accident or the code was written incorrectly, they can also be cancelled.

## Monitoring Jobs

Currently running jobs can be monitored using the `squeue` command. The basic command to list all jobs for a specific user is:

``` bash
squeue -u $USER
```

The output of `squeue` will look like:

![image](images/squeue_output.png)

This gives the job id, name, run time, partition, user, job status, and number of nodes used for each job a user has submitted.

For array jobs, the job id will be formatted as `jobid_arrayid`.

Further information about filtering by job name or partition, including information about memory or number of CPUs, and info regarding messages specific to a job's status can be seen using `man squeue`.

## Cancelling Jobs

Cancelling queued and currently running jobs can be done using the `scancel` command. Importantly, this will only cancel jobs that were initiated by the user running the command. `scancel` is very flexible in how it behaves:

``` bash
# cancel a single job or an entire job array
scancel \<jobid\>

# cancel specific job array IDs, specified as single number or a range
scancel \<jobid_arrayid\>

# cancel all jobs on a partition for the user
scancel -p \<partition\>

# cancel all jobs for a user
scancel -u $USER
```

Keep in mind, cancelling all jobs will also cancel the interactive jobs created on the Open OnDemand portal.

More information on options to cancel jobs can be seen using `man scancel`.

## Reviewing Past Jobs

If you are planning a new set of jobs and are estimating resource requests, it is useful to review similar jobs that have already completed. To list past jobs for a user, use the `sacct` command.

### Review With Job ID

The basic form is to use `-j` along with a job ID to list information about that job.

``` bash
sacct -j [jobid]
```

This command will output basic information such as the ID, Name, Partition, Allocated CPUs, and State for the given job ID.

Jobs can have matching extern and/or batch job entries as well. These are not especially helpful for most users. You can remove these entries using:

``` bash
sacct -j [jobid] | grep -wv -e extern -e batch
```

### Review Jobs Submitted Between Specific Timepoints

If you do not remember the job ID, you can use the `-S` and `-E` flags to retrieve jobs submitted between the given start datetime and end datetime. Valid start/end time formats are:

``` text
HH:MM[:SS] [AM|PM]
MMDD[YY] or MM/DD[/YY] or MM.DD[.YY]
MM/DD[/YY]-HH:MM[:SS]
YYYY-MM-DD[THH:MM[:SS]]
```

Notes:

- Anything in `[]` is optional
- Times can be specified in either 12-hour with AM/PM or 24-hour
- For the last specification, the T itself is inserted, it is not replaced with any value. For example, requesting jobs starting after 12:30 PM on October 5, 2021, the form would be `2021-10-05T12:30`.

For example, to retrieve jobs submitted during the month of July 2021, the command could be:

``` bash
sacct -S 070121 -E 073121
sacct -S 07/01/21 -E 07/31/21
sacct -S 2021-07-01 -E 2021-07-31
```

### Customizing the Output

You can add `-o` with a list of output fields to customize the information you see.

``` bash
sacct -j [jobid] -o jobid,start,end,state,alloccpu,reqmem
```

This command will output the job ID, the start time, end time, the state, the number of allocated CPUs, and the requested memory for the specified job. All potential output fields can be seen using `sacct --helpformat`. Their descriptions can be found on the [sacct documentation](https://slurm.schedmd.com/sacct.html) under Job Accounting Fields.

## Evaluating Job Efficiency

It's important to evaluate the efficiency of your job in terms of resource usage after it completes. Remember that Cheaha is a shared resource, so requesting resources that sit unused during a job prevents others from using those resources. As well, because each user has a maximum amount of resources they can use at a given time, having inefficient jobs can increase analysis runtime across many jobs.

In order to look at job efficieny, use the `seff` command.

``` bash
seff \<jobid\>
```

The output will look like:

![image](images/seff_output.png)

The job had poor CPU efficiency, requesting 2 CPUs which were only busy for 30% of runtime. It also had poor memory efficiency, using less than 1 GB total memory of the requested 16 GB (5.73%). For subsequent jobs using a similar analysis and dataset size, decreasing the requested memory and using a single CPU would be appropriate.

!!! note

<!-- markdownlint-disable-next-line -->
    Do not aim for 100% memory efficiency for a given job. Having a couple of GB extra is recommended to prevent jobs being cancelled due to insufficient resources
