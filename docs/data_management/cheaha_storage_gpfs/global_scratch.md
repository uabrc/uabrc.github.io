# Scratch Directories

Scratch directories provide temporary, high-performance storage for data used in active computations. There are two types of scratch space:

- User Scratch: is available on login nod and also shared across compute nodes.
- Local scratch: is available only on individual compute nodes.

Scratch Directories are meant for short-term storage of intermediate or in progress data and should not be used for long-term retention.

<!-- markdownlint-disable MD046 -->
!!! important

    Starting January 2023, scratch data will have limited retention. See [Scratch Retention Policy](#policies-and-expectations) for more information.
<!-- markdownlint-enable MD046 -->

## User Scratch

All users have access to a large, temporary, work-in-progress directory for storing data, called a scratch directory in `/scratch/$USER` or `$USER_SCRATCH`. Use this directory to store very large datasets or temporary pipeline intermediates for a short period of time while running your jobs. The maximum amount of data a single user can store in network scratch is 100 TB at once.

Network scratch is available on the login node and each compute node. This storage is a GPFS high performance file system providing roughly 1 PB of storage. If using scratch, this should be your jobs' primary working directory, unless the job would benefit from local scratch (see below).

<!-- markdownlint-disable MD046 -->
!!! warning

    Research Computing expects each user to keep their scratch areas clean. **The cluster scratch areas are not to be used for archiving data.** In order to keep scratch clear and usable for everyone, files older than 30 days will be eligible for deletion.
<!-- markdownlint-enable MD046 -->

## Policies and Expectations

Data stored in `/scratch` is subject to two limited retention policies.

- Each user will have a quota of 100 TB of scratch storage.
- Files will be retained for a maximum of 30 days, after which they become eligible for deletion.
