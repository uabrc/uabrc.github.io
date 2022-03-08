# Managing Jobs

When jobs are submitted, researchers can monitor their status using Slurm commands. Additionally, researchers can get information about completed jobs regarding their CPU and memory usage during execution for planning future jobs. Both of these cases should be a regular part of using Cheaha for researchers.

In case jobs were submitted by accident or the code was written incorrectly, they can also be cancelled.

## Monitoring Jobs

Currently running jobs can be monitored using the `squeue` command. The basic command to list all jobs for a specific researcher is:

``` bash
squeue -u $USER
```

The output of `squeue` will look like:

![!Output from squeue. ><](images/squeue_output.png)

By default the fields displayed are `jobid`, `partition`, `jobname` as `name`, blazerid as `user`, job state as `st`, total run time as `time`, number of nodes as `node`, and the list of nodes as `nodelist`, used for each job a researcher has submitted.

For array jobs, the job id will be formatted as `jobid_arrayid`.

Further information about filtering by job name or partition, including information about memory or number of CPUs, and info regarding messages specific to a job's status can be seen using `man squeue`.

## Cancelling Jobs

Cancelling queued and currently running jobs can be done using the `scancel` command. Importantly, this will only cancel jobs that were initiated by the researcher running the command. `scancel` is very flexible in how it behaves:

``` bash
# cancel a single job or an entire job array
scancel <jobid>

# cancel specific job array IDs, specified as single number or a range
scancel <jobid_arrayid>

# cancel all jobs on a partition for the user
scancel -p <partition>

# cancel all jobs for a researcher
scancel -u $USER
```

<!-- markdownlint-disable MD046 -->
!!! warning

    Cancelling all jobs will also cancel the interactive jobs created on the Open OnDemand portal.
<!-- markdownlint-disable MD046 -->

More information on options to cancel jobs can be seen using `man scancel`.

## Reviewing Past Jobs

If you are planning a new set of jobs and are estimating resource requests, it is useful to review similar jobs that have already completed. To list past jobs for a researcher, use the `sacct` command.

<!-- markdownlint-disable MD046 -->
!!! tip

    To minimize queue wait times and make best use of resources, please review job efficiency using `seff`. See our [Job Efficiency](../job_efficiency.md) page for more information.
<!-- markdownlint-enable MD046 -->

### Review With Job ID

The basic form is to use `-j` along with a job ID to list information about that job.

``` bash
sacct -j [jobid]
```

This command will output basic information such as the ID, Name, Partition, Allocated CPUs, and State for the given job ID.

Jobs can have matching extern and/or batch job entries as well. These are not especially helpful for most researchers. You can remove these entries using:

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
