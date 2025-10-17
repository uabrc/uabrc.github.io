# Managing Jobs

When jobs are submitted, researchers can monitor their status using Slurm commands. Additionally, researchers can get information about completed jobs regarding their CPU and memory usage during execution for planning future jobs. Both of these cases should be a regular part of using Cheaha for researchers.

In case jobs were submitted by accident or the code was written incorrectly, they can also be cancelled.

## Monitoring Queued Jobs With `squeue`

Currently running jobs can be monitored using the `squeue` command. The basic command to list all jobs for a specific researcher is:

``` bash
squeue -u $USER
```

The output of `squeue` will look like:

![!Output from squeue.](./images/squeue_output.png)

By default the fields displayed are `jobid`, `partition`, `jobname` as `name`, BlazerID as `user`, job state as `st`, total run time as `time`, number of nodes as `node`, and the list of nodes as `nodelist`, used for each job a researcher has submitted.

For array jobs, the JobID will be formatted as `jobid_arrayid`.

More information is available at the [Official Documentation](https://slurm.schedmd.com/squeue.html).

## Cancelling Jobs With `scancel`

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

More information is available at the [Official Documentation](https://slurm.schedmd.com/scancel.html).

## Reviewing Past Jobs With `sacct`

If you are planning a new set of jobs and are estimating resource requests, it is useful to review similar jobs that have already completed. To list past jobs for a researcher, use the `sacct` command. Common use cases and information are detailed below. Full details are available at the [Official Documentation](https://slurm.schedmd.com/scancel.html).

<!-- markdownlint-disable MD046 -->
!!! tip

    To minimize queue wait times and make best use of resources, please review job efficiency using `seff`. See our [Job Efficiency](../job_efficiency.md) page for more information.
<!-- markdownlint-enable MD046 -->

### Review Jobs by JobID

The basic form is to use `-j` along with a JobID to list information about that job.

``` bash
sacct -j <jobid>
```

You can also review multiple jobs using a comma-separated list of JobIDs.

This command will output basic information such as the ID, Name, Partition, Allocated CPUs, and State for the given JobID.

Jobs can have matching extern and/or batch job entries as well. These are not especially helpful for most researchers. You can remove these entries using the `-X` flag.

``` bash
sacct -j <jobid> -X
```

### Review Jobs Submitted Between Specific Timepoints

If you do not remember the JobID, you can use the `-S` and `-E` flags to retrieve jobs submitted between the given start datetime and end datetime.

For example, to retrieve jobs submitted during the month of July 2021, the command could be:

``` bash
sacct -S 070121 -E 073121
sacct -S 07/01/21 -E 07/31/21
sacct -S 2021-07-01 -E 2021-07-31
```

### Customizing the Output

You can add `-o` with a list of [output fields](#sacct-fields) to customize the information you see.

``` bash
sacct -o jobid,start,end,state,alloccpu,reqmem
```

You may also use the format `<field>%<width>` to make columns be `<width>` characters wide. This is sometimes necessary for [TRES fields](#tres-explained) and `nodelist`, among others. An example might be `alloctres%40` to make the field 40 characters wide.

This command will output the JobID, the start time, end time, the state, the number of allocated CPUs, and the requested memory for the specified job. All potential output fields can be seen using `sacct --helpformat`. Their descriptions can be found on the [sacct documentation](https://slurm.schedmd.com/sacct.html) under Job Accounting Fields.

### Formatting the Output

You can format the output of `sacct` using a delimiter with the flags `--parsable2` and `--delimiter=<delim>`. Any number of characters may be used as a delimiter. The default is `|`. It is not recommended to use `,` as that is used in comma-separated lists throughout `sacct` fields.

### `sacct` Flags

{{ read_csv('cheaha/res/sacct_flags.csv', keep_default_na=False) }}

A complete list of flags is available at [Official Documentation](https://slurm.schedmd.com/sacct.html#SECTION_OPTIONS).

### `sacct` Fields

{{ read_csv('cheaha/res/sacct_fields.csv', keep_default_na=False) }}

A complete list of fields is available at the [Official Documentation](https://slurm.schedmd.com/sacct.html#SECTION_Job-Accounting-Fields).

## Slurm Common Reference

### Slurm JobID Formatting

JobID numbers are assigned automatically by the scheduler in the order submissions are received. All jobs have a single, unique JobID number associated with them. Some features will cause JobID numbers to be reported differently than their actual value.

- For non-array jobs submitted with `sbatch`, `salloc`, or with `srun` outside of a job context, the unique JobID number is reported directly.
- For array jobs submitted with `sbatch`, the array is assigned a master ID like `12345678`, and each task is reported as `<master-job-id>_<task-id>`. An example might be `12345678_987`. Each task still has a unique JobID number.
- For job steps submitted with `srun` inside of a job context, the JobID is reported as `<job-id>.<task-name>`. All jobs submitted generate a `.batch` step and a `.extern` step. An example might be `12345678.batch`.

### Slurm Time Formatting

Slurm formats time in two different ways: (1) time points and (2) durations. Time points are used whenever a single point in time is needed, such as the start or end of a job. Durations are needed for job requests and reported for elapsed times.

Units are given a shorthand designations:

- `YYYY` four-digit year.
- `MM` two-digit month or two-digit minutes, depending on placement.
- `DD` two-digit day.
- `HH` two-digit hour.
- `SS` two-digit seconds.
- `AM|PM` literally AM or PM.

Square brackets `[]` indicate the contents are optional.

Time points may be formatted like any of the following.

```text
HH:MM[:SS][AM|PM]
MMDD[YY][-HH:MM[:SS]]
MM.DD[.YY][-HH:MM[:SS]]
MM/DD[/YY][-HH:MM[:SS]]
YYYY-MM-DD[THH:MM[:SS]]
```

Duration requests are made like any of the following.

```text
MM[:SS]
[HH:]MM:SS
DD-HH[:MM[:SS]]
```

Durations are reported like the following.

```text
[DD-[HH:]]MM:SS
```

### Slurm States

Job states report on where the job is in the overall Slurm process. If all goes well, you will see jobs move through the following states:

1. `PENDING`
1. `RUNNING`
1. A terminal state depending on what happens
    1. `COMPLETED` if the job finished normally and returns exit code zero
    1. `CANCELLED` if the researcher cancels the job
    1. `FAILED` if there is a software error or non-zero exit code
    1. `TIMEOUT` if the job had insufficient time

Other states are possible. A complete list of job states is available at the [Official Documentation](https://slurm.schedmd.com/sacct.html#SECTION_JOB-STATE-CODES).

### Slurm Units

Slurm uses flexible units for memory to keep reports compact. It always prefers the shortest possible representation, and will choose the largest units by default. Other units may be used, and there are flags to allow reporting in uniform units.

The memory units are `KMGT` for `kilo`, `mega`, `giga`, `tera` respectively. All are in bytes. Slurm uses the convention that e.g.

$$
\begin{aligned}
1\textrm{T}
&=1024\textrm{G}\\
&=1024^{2}\textrm{M}\\
&=1024^{3}\textrm{K}
\end{aligned}
$$

### TRES Explained

The abbreviation `TRES` stands for "trackable resources". Any resource made available by Slurm that is trackable is recorded in the Slurm database and can be recovered using [sacct](#reviewing-past-jobs-with-sacct). The [fields](#sacct-fields) `reqtres` and `alloctres` can be used to review CPUs, memory, nodes and GPUs. The data is stored as a comma-separated list of `<resource>=<quantity>` pairs, and all values are totals across the entire job, not per node or per task. An example might look like:

```text
billing=8,cpu=8,gres/gpu=2,mem=64G,node=1
```

### RSS Explained

The abbreviation `RSS` stands for "resident set size", and is related to memory usage by jobs in Slurm. Memory usage is challenging to record accurately. Recording memory means a request must be made to the operating system to obtain memory usage at a single point in time, which uses computational resources. There is a balance made between resolution in time, and computational overhead.

The difficulty with recording memory usage contributes to difficulty diagnosing root causes of out of memory errors, bus errors, and segmentation faults.

RSS is recorded by Slurm in the [sacct](#reviewing-past-jobs-with-sacct) [fields](#sacct-fields) `averss` and `maxrss`. These values are both reported in bytes, rather than the usual [compact memory units](#slurm-units).

### Slurm Resource Calculations

#### Calculating CPUs

$$
\begin{aligned}
\textrm{Total CPUs}
&=\left(\textrm{--cpus-per-task}\right)
\left(\textrm{--ntasks}\right)
\left(\textrm{--nodes}\right)\\
&=\left(\frac{\textrm{CPU}}{\textrm{Task}}\right)
\left(\frac{\textrm{Task}}{\textrm{Node}}\right)
\left(\textrm{Node}\right)
\end{aligned}
$$

Example:

For a job with `--cpus-per-task=16 --ntasks=2 --nodes=3`:

$$
\begin{aligned}
\textrm{Total CPUs}
&=16\times 2\times 3\\
&=96
\end{aligned}
$$

#### Calculating Memory

$$
\begin{aligned}
\textrm{Total Memory}
&=\left(\textrm{--mem}\right)
\left(\textrm{--nodes}\right)\\
&=\left(\frac{\textrm{Memory}}{\textrm{Node}}\right)
\left(\textrm{Node}\right)\\
\\
\textrm{Total Memory}
&=\left(\textrm{--mem-per-cpu}\right)
\left(\textrm{--cpus-per-task}\right)
\left(\textrm{--ntasks}\right)
\left(\textrm{--nodes}\right)\\
&=\left(\frac{\textrm{Memory}}{\textrm{CPU}}\right)
\left(\frac{\textrm{CPU}}{\textrm{Task}}\right)
\left(\frac{\textrm{Task}}{\textrm{Node}}\right)
\left(\textrm{Node}\right)
\end{aligned}
$$

Examples:

For a job with `--mem=40G --nodes=2`:

$$
\begin{aligned}
\textrm{Total Memory}
&=\left(\textrm{--mem}\right)
\left(\textrm{--nodes}\right)\\
&=40\textrm{G}\times 2\\
&=80\textrm{G}
\end{aligned}
$$

For a job with `--mem-per-cpu=10G --cpus-per-task=8 --ntasks=2 --nodes=2`:

$$
\begin{aligned}
\textrm{Total Memory}
&=\left(\textrm{--mem-per-cpu}\right)
\left(\textrm{--cpus-per-task}\right)
\left(\textrm{--ntasks}\right)
\left(\textrm{--nodes}\right)\\
&=10\textrm{G}\times 8\times 2\times 2\\
&=320\textrm{G}
\end{aligned}
$$
